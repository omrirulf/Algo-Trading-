# Daily report

**24 Nov 2026, 19:08 Israel time (17:08 UTC)** · 80 names checked · 1 traded · 7 with a problem

**Answers with no explanation:** 13 of 60 (the model wrote only a label, like “NEUTRAL”, where its reason should be). Their main reasons are still shown.

**Run:** started by the outside scheduler (via supabase-cron), on time (planned for 14:40 UTC).

| Group | Looked at | Took a side | No clear view | Problems |
| --- | --- | --- | --- | --- |
| Companies | 16 | 3 | 13 | 0 |
| Whole-market funds | 14 | 1 | 13 | 0 |
| Sector and country funds | 41 | 1 | 40 | 0 |
| Commodities | 9 | 0 | 2 | 7 |

## Open positions

Checked before any new trade. R is what the trade risked at entry; the ladder sells a third at +1R and another at +3R, the stop-loss follows the price up every day, and it only ever moves up.

| Position | What happened |
| --- | --- |
| JPMorgan Chase (JPM) · Company | **Stop raised.** At +0.69R, following the price. Stop-loss raised 331.98 → 331.74. |
| Eli Lilly (LLY) · Company | **Stop raised.** At +0.14R, following the price. Stop-loss raised 1304.66 → 1320.29. |
| Royal Bank of Canada (RY) · Company | **Stop raised.** At +0.16R, following the price. Stop-loss raised 196.78 → 195.20. |
| Elbit Systems (ESLT) · Company | **Holding.** -0.65R, holding 7 shares. Stop-loss 640.17. |
| South Korea (EWY) · Sector or country | **Holding.** +0.38R, holding 51 shares. Stop-loss 143.75. |
| Brazil (EWZ) · Sector or country | **Holding.** +0.93R, holding 138 shares. Stop-loss 31.27. |
| HDFC Bank (HDB) · Company | **Holding.** +3.77R, holding 51 shares. Stop-loss 26.52. |
| MercadoLibre (MELI) · Company | **Holding.** +0.34R, holding 3 shares. Stop-loss 1505.92. |
| Nvidia (NVDA) · Company | **Holding.** -0.52R, holding 1 shares. Stop-loss 142.32. |
| Novo Nordisk (NVO) · Company | **Holding.** -0.64R, holding 5 shares. Stop-loss 41.18. |
| Procter & Gamble (PG) · Company | **Holding.** +1.59R, holding 2 shares. Stop-loss 165.90. |
| Toyota (TM) · Company | **Holding.** -0.64R, holding 1 shares. Stop-loss 205.44. |
| Exxon Mobil (XOM) · Company | **Holding.** -0.44R, holding 30 shares. Stop-loss 153.50. |

## How to read this

Once a day the system looks at every name on the list. For each one it reads five kinds of evidence and gives each kind a score from -1.00 (bad) to +1.00 (good). Then it picks a side and says how sure it is, from 0.00 to 1.00.

The three sides: **BULLISH** = the model thinks the price will go up; **BEARISH** = the model thinks the price will go down; **NEUTRAL** = the model has no clear view.

Being sure is not enough on its own. A trade only happens when confidence reaches **0.30**. Below that the system writes down what it thought and does nothing. The size of a trade, the stop-loss and every limit are decided by plain code, not by the model.

Open positions are checked first, before any new trade. When a trade has earned back what it risked (+1R), a third of it is sold and the stop-loss moves up to the entry price, so it can no longer lose. At three times that (+3R) another third is sold and the stop moves up again. The last third stays open. Every day the stop-loss also follows the price up, so a position only ever closes when its stop is hit. The stop only ever moves up.

Under each name you will find the five scores. Click a grey line to open it and see the exact evidence behind that score. The words inside quotation marks are the model's own; nothing there has been rewritten.

## Companies

### Microsoft (MSFT) · Company — BULLISH, confidence 0.65

**Result:** REJECTED · no room under the sleeve budget limit

**In the model's own words:**

> Strong earnings beat and AI‑driven rally, solid fundamentals and insider net buying outweigh bearish technicals.

**Main reasons it gave:**
- MSFT beat earnings estimates (10% beat) and raised dividend
- AI infrastructure demand highlighted; Nvidia-fueled rally
- Strong fundamentals: 41% profit margin, 18.8% YoY revenue growth, forward P/E 20.3
- Insider net buying of 257,656 shares (+3.1% of holdings)

<details><summary><b>News</b> — score +0.70</summary>

- [Microsoft Corporation (MSFT) Stock Price, News, Quote & History](https://ca.finance.yahoo.com/quote/MSFT/)  
  <sub>Yahoo! Finance Canada, 22 hours ago</sub>  
  556,133.20% · Previous Close 484.52 · Open 506.05 · Bid 490.02 x 400 · Ask 495.16 x 100 · Day's Range 492.02 - 509.15 · 52 Week Range 349.20 - 559.15 · Volume...
- [Microsoft Stock Jumps In Nvidia-Fueled Tech Surge; Is Microsoft A Buy Now?](https://www.investors.com/research/microsoft-msft-stock-buy-now-november-2026-2/)  
  <sub>Investor's Business Daily, 2 hours ago</sub>  
  Microsoft (MSFT)stock joined a larger tech-led relief rally Monday while remaining below a key chart level. Major technology stocks, including Microsoft,...
- [Microsoft vs. Meta: Which AI Infrastructure Stock Has An Edge Now?](https://www.google.com/goto?url=CAESowEBxCJF1_hkLynSqP3rELMWbZeDBFgl1kR7k6nP9bMPFktJojuy8Cofarl3mBF8myx5Chsw1dQDrDGldARiXIokvbFdnz-ETnygKZhsoGQFCziE0VumRlkjJDsI_bis9HYAnn6_yNlOrD6B5r-1HRXSGbemMO2NNz9uuv4cjy-lZdviANxKRr-XbuMkenZ73e-yz-CaprfB8Zh4ZPFDTwAjbVZW&gsessionid=u5bR3muQtlk5SAoYkScxTT7WVg7K09E2Tp734IqVY5FPuKDrNSYQUg)  
  <sub>Zacks Investment Research, 2 hours ago</sub>  
  Microsoft and Meta are ramping up AI infrastructure spending, but diverging monetization strategies, cash flow and growth prospects give MSFT stock an edge.
- [Microsoft Corporation (MSFT) stock price, news, quote and history](https://www.google.com/goto?url=CAESYwHEIkXXyC-oLYdsFjIPPrXrhOgE-HvN8AjiQaLmUNkiPx0nmuZaArDM0ptc8kGOvOse3eJZqJ5egUgtoiXDFo1d1qEdruMDVZebQmNeR0uFviaq57th7Cyvq7HVdQOEVr0ZNw&gsessionid=u5bR3muQtlk5SAoYkScxTT7WVg7K09E2Tp734IqVY5FPuKDrNSYQUg)  
  <sub>Yahoo Finance UK, 22 hours ago</sub>  
  556,133.20% · Previous close 484.52 · Open 506.05 · Bid 490.02 x 400 · Ask 495.16 x 100 · Day's range 492.02 - 509.15 · 52-week range 349.20 - 559.15 · Volume...
- [Microsoft beats earnings estimates and lifts dividend: Can MSFT sustain gains?](https://www.google.com/goto?url=CAESlgEBxCJF16EPNFL2AYP41MenZV7IlD8uIx-KfJzdIL820-m5QjHyEmo2B9uL04kgkFvgBv5MQh3JFthTBTC1p6AmpGwLTjLDRPOgYzhKDoxpXVIAD3VtCG4WOKrEVSlvv3TpIP9lt0R_YhVIH-aQ490i4eQWopOCtydyArE9Eehyo6t2Gv5DgqxJ8hPH9YZGRClhV5PXQc0&gsessionid=u5bR3muQtlk5SAoYkScxTT7WVg7K09E2Tp734IqVY5FPuKDrNSYQUg)  
  <sub>Traders Union, 28 minutes ago</sub>  
  Microsoft trades at $492.97, up 1.64% today after strong earnings and increased ETF buying. See latest moves and support levels.
- [Which "Magnificent Seven" Stocks Win From Anthropic’s IPO?](https://www.google.com/goto?url=CAESxwEBxCJF14vbw_DohSX6o7P85HWFNqm3XIjytae8cgFr4BqqaG2q7j40F9zq0o6Pq7_mFsXaY-VIsbAv7Qh8qcY5ppg52lMqh2vuul4M7-eOyXGKxQNYbbFMTa3yaI3IFY_Ep4k-SVdnoaCqhTqmbgO_42b8qtOpJmn4WhwoYuP9E6igOkN9MpRA4mO5mELJnmQ69QP3PgjUXJWPnU8ZgaruyrXOHntzOmSsVbz1_2pwNFkq1U-cKMqtfepNXtIo8ox4ek42jGi8&gsessionid=u5bR3muQtlk5SAoYkScxTT7WVg7K09E2Tp734IqVY5FPuKDrNSYQUg)  
  <sub>The Globe and Mail, 3 hours ago</sub>  
  Detailed price information for Microsoft Corp (MSFT-Q) from The Globe and Mail including charting and trades.
- [Nvidia Adds Record $888 Billion as Jensen Huang Returns - Microsoft (NASDAQ:MSFT), NVIDIA (NASDAQ:NVDA)](https://www.google.com/goto?url=CAESrwEBxCJF16KiUzoyVGwt9s03GXVpi6GIYvSZzBzGsieqV_PUlyDrCzXB-Xn7xv7Ihz_f4p2v2dqmLveWZaJgaMo5lcuVD-YzZ53UOnnZYfrHsZcQOLwoS4oBqFlEj9ouOQ2oi107rcLVDLa0n7p9KKvqHx3tYviYqxyKKrXrxIIAGF6NZSnYwbx12dVaAC_dKgPvmtQYjUEO1uDkdLMbDwPHMeldSVdgOqrJyoGSmyrl&gsessionid=u5bR3muQtlk5SAoYkScxTT7WVg7K09E2Tp734IqVY5FPuKDrNSYQUg)  
  <sub>Benzinga, 23 hours ago</sub>  
  Nvidia Corp. added about $888 billion in market value Monday after reinstating Jensen Huang as CEO, the largest one-day gain on record. SMH rose 13.7%.
- [Is Trending Stock Microsoft Corporation (MSFT) a Buy Now?](https://www.google.com/goto?url=CAESlQEBxCJF12qQKdlMOXhAZFTj_hGep5M200eYlakuVD4CfzOdzy_lZpc3KtSlXdmtmEzoHSDabk8YtpdC66e7VOYl3WP9ySJRMzBkNQ0XIUntxCMWYgjAtOJ582LCN5H0nmeTkWAVwlokq4UnvCEk8P1Njydy5_VQ4JBvjAD1yzuVswqmFExOTPS6ikTRLXHewRAU_4vQ_w&gsessionid=u5bR3muQtlk5SAoYkScxTT7WVg7K09E2Tp734IqVY5FPuKDrNSYQUg)  
  <sub>Yahoo Finance Singapore, 2 hours ago</sub>  
  Microsoft (MSFT) has been one of the most searched-for stocks on Zacks.com lately. So, you might want to look at some of the facts that could shape the...
- [Microsoft Stocks Rise 3.9% With a Perfect GF Score as OpenAI Contingency Plans Surface](https://www.google.com/goto?url=CAESzQEBxCJF198uSWv6TxQEOzwLqEciyrTPuA4Qanf9nRHnpWuYG2Nc5xnHJ6KtVCbK65vd7oVDbZTQXUqLYj5F_5bx3GR16-QuD-Egly7_tRAvEWIlNg7vfH8LFKo5B3lmScQQcr-wetdhHTvA27nBAx-H57e3WebnO_NYQst8tNr6RtelA1V82ziunspSO2lQ3yNCXkopFeCM4i6UtwOetVToJIgUnIgyn2y2Zh5dPkRheJdw-pMrQkzbuK9sgMi30Z0OaQ0P7MF7MvQ9p-qm&gsessionid=u5bR3muQtlk5SAoYkScxTT7WVg7K09E2Tp734IqVY5FPuKDrNSYQUg)  
  <sub>TradingView, 21 hours ago</sub>  
  Microsoft NASDAQ:MSFT shares rose 3.9% to $503.41 at 10:40 a.m. ET in regular trading on November 23, trailing the double-digit jumps in chip names.
- [Microsoft rises as warning on Chinese optical hardware ban fuels AI investment concern](https://www.google.com/goto?url=CAESigEBxCJF14jgZcWwKsVvOcUAh6aNVpbr6sAaH_nxq54V_SqZgPlR2Nq9LstlcHx7dEfOFKhR0ajleRv8jRsfYMgqc6CtohR3E-oL2UaKShRvHPWQHqCaid7sywI0yiKZIQ5JpK1XTnLFUPpDOYzqnn8aZoyPWoc8sK2cnZ3nBResrRSG-fLaWoE1Pn8&gsessionid=u5bR3muQtlk5SAoYkScxTT7WVg7K09E2Tp734IqVY5FPuKDrNSYQUg)  
  <sub>Traders Union, 18 hours ago</sub>  
  Microsoft (MSFT) stock is trading higher, with supply chain risks in focus after management highlighted geopolitical uncertainty affecting key hardware...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.70</summary>

_Not available today._

</details>

<details><summary><b>Price and chart</b> — score -0.60</summary>

```text
Last close 491.25 (bar of 2026-11-24), from 501 daily bars
Trend: vs 20d SMA 518.95 (-5.3%), 50d 519.46 (-5.4%), 200d 444.48 (+10.5%); 50d above 200d
Momentum: RSI(14) 38.6 | MACD -8.155 vs signal -3.282 (histogram -4.873)
Returns: 1d -0.3% | 5d -3.0% | 1m -7.8% | 3m -1.0%
52-week range: 352.83 - 555.80 (now 68.2% of the way up)
Volatility: ATR(14) 16.09 (3.3% of price) | annualised 20d 38.6%
Volume: 0.05x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.60</summary>

```text
Sector: Technology / Software - Infrastructure | market cap 3.65T
Valuation: trailing P/E 25.65 | forward P/E 20.31 | P/B 7.76 | PEG 1.43
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

<details><summary><b>What analysts and big funds say</b> — score +0.30</summary>

```text
Consensus: strong_buy (mean 1.34 on a 1=strong buy to 5=strong sell scale, 54 analysts)
Ratings: 14 strong buy, 41 buy, 3 hold, 0 sell, 0 strong sell
Price target: mean 637.36 (+29.7% vs last close), range 440.00 - 870.00
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

<details><summary><b>What analysts say about what this fund holds</b> — score +0.30</summary>

_Not available today._

</details>

<details><summary><b>Buying and selling by company insiders</b> — score +0.40</summary>

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

<details><summary><b>Who is positioned how</b> — score +0.40</summary>

_Not available today._

</details>

<details><summary><b>Money going into and out of this fund</b> — score +0.40</summary>

_Not available today._

</details>

### Caterpillar (CAT) · Company — BULLISH, confidence 0.55

**Result:** REJECTED · no room under the sleeve budget limit

**In the model's own words:**

> Overall view is moderately bullish: solid fundamentals and earnings record, strong analyst consensus with a high price target, modest insider net buying, and an oversold RSI suggesting short‑term upside. Technicals are bearish (downtrend, thin volume) and news is mixed and not a material catalyst, which tempers conviction.

**Main reasons it gave:**
- Forward P/E 16.86 indicates cheap valuation relative to earnings growth
- Analyst consensus buy with mean price target +48% above current price
- Three of last four quarters beat earnings expectations
- RSI 34 suggests oversold condition, potential short‑term bounce
- Insiders net bought 14,690 shares (+1.3% of holdings)

<details><summary><b>News</b> — score +0.10</summary>

- [Toromont Industries Ltd. (TIH.TO) Stock Price, News, Quote & History](https://ca.finance.yahoo.com/quote/TIH.TO/)  
  <sub>Yahoo! Finance Canada, 7 hours ago</sub>  
  Find the latest Toromont Industries Ltd. (TIH.TO) stock quote, history, news and other vital information to help you with your stock trading and investing.
- [Wall Street catches Jensen Huang fever, but is this all a dead cat bounce?](https://investinglive.com/stocks/wall-street-catches-jensen-huang-fever-but-is-this-all-a-dead-cat-bounce/)  
  <sub>investingLive, 10 hours ago</sub>  
  Nvidia reignites the animal spirits in Wall Street but the technical picture suggests that dip buyers aren't out of the woods yet.
- [Dead Cat Bounce? AI Stocks Climb 20%+, but IREN, Applied Digital Stay Down 50%+](https://www.google.com/goto?url=CAEScwHEIkXX_8B_Qt_lwMrGEGVUlS_ugtyoSq-bxsXtHxUQD3sSnjXXqdRqlJprRVFejeEe6Q44lciLlTLD4tNIOkX_FEfw1JNEvDUR_pbUcgShVzK-tCPcOj3gMURquOl32RobUrbtL12VbRCGm3Ns1sq_8jQ&gsessionid=Yp1JqrbEeGWiPtFZLYacEKfKfmNpXKJQVUziwKqrOhJgnoO96Me0fg)  
  <sub>BeInCrypto, 12 hours ago</sub>  
  Is it a dead cat bounce? AI stocks jumped 20%+ on Huang's return, yet IREN and Applied Digital sit down 50%+ in a year.
- [Unusual Machines Surges 10% as Drone Stocks Bounce Back With the Market; Ondas Rallies 9%, Red Cat Jumps 8%](https://www.google.com/goto?url=CAES0AEBxCJF1z2-Z2BQk6A5TsXGRxfdniAdZQz70P9zO47vy-M52dCBNDcnjiyTf_ZIqr5I3TVlCV7yZIpm_fLNwRsRAyzz8k6_wVjYMinnCMacrjFs8dsFvuMSsrDJITfMmcnaCfo6Lkwxdei4A6ZBM_VIz7xrcjcDhRjTL4XFLcMFeXAzLv86YitS_ajYnGrmHyZPfgjlZAvjD2TrW9ep1hPRZLVjRqXWBDyHIssjjmQ62Yjbnev716UxpTnmuDW-zm6hnCSJFlikqRieNIbAQSYM&gsessionid=Yp1JqrbEeGWiPtFZLYacEKfKfmNpXKJQVUziwKqrOhJgnoO96Me0fg)  
  <sub>24/7 Wall St., 21 hours ago</sub>  
  Unusual Machines and Ondas jumped about 10% in a relief rally, yet remain deep in the red for the year after brutal earnings-driven selloffs.
- [Why is Caterpillar stock soaring today](https://www.google.com/goto?url=CAESoAEBxCJF1wxweHhDzht0UfIo6JxN09zBUZeUT2aVstJ7cWrjOfdTa77dG3YAZyEWN9amF_rm506Ch-tuWcUlWK8Onqk4f8Zb07YRTlpHF_wZEKl8egmWJxLnlpgMi0m2FENxJe5ixWHmO7Mv9kBW3yT3a2cY3Iy5e6Zy2TJ6AF2sdKXH00MnXS6-RFI-qjJ9q6zb5GEnIpTvbDxLRLVCg7XZ&gsessionid=Yp1JqrbEeGWiPtFZLYacEKfKfmNpXKJQVUziwKqrOhJgnoO96Me0fg)  
  <sub>TradingView, 19 hours ago</sub>  
  Shares of construction equipment company Caterpillar CATjumped 7.3% in the afternoon session after Nvidia reinstated Jensen Huang as CEO, sparking a rebound...
- [Caterpillar Inc Stock (CAT) Moved Up by 7.38% on Nov 23: What Signal Does It Send?](https://www.google.com/goto?url=CAESjwEBxCJF1y4Rszz0tALjIbPRaxpR9SDzEq_MuWYSu_EI4Ft8gZHjzPtXlGN3ugcjn6qHm_7jBWL5Z6Xe3fRENi6W3XQ-3oeXtA6RTzOoIvewEPWn5IiwHvFGsMT8K3wnssM7I8cQYgFOUbGC_CR6i5GDGq-IS98udkAKc2jQ1S2w3-3kVN3zYZSeKB89EiEwUA&gsessionid=Yp1JqrbEeGWiPtFZLYacEKfKfmNpXKJQVUziwKqrOhJgnoO96Me0fg)  
  <sub>TradingKey, 19 hours ago</sub>  
  Caterpillar surged due to institutional buying and infrastructure optimism.Energy and Transportation segment demand boosted financial performance.
- [Why is Caterpillar stock surging today?](https://www.google.com/goto?url=CAESoQEBxCJF17QElk7CXrNWsBk5cStn9h0ckdX80TTTz3Dk_Txf-vhuN_qc-7JNoBFlChUZRXTQhNy0lxOylIJV4KZiwakbdm8v244fNuXieEXeImP-GPt-R1LEXBlWxJuIoD8Q4hnvH0HCoupL5k4LadsLGrZMpFkjSqz3cU3qQAsKc_orDqD2wgcbnuqq5Y7pifvZwq_zY6GasU1LU3C-m-rQ6w&gsessionid=Yp1JqrbEeGWiPtFZLYacEKfKfmNpXKJQVUziwKqrOhJgnoO96Me0fg)  
  <sub>Investing.com, 22 hours ago</sub>  
  Investing.com -- Caterpillar shares surged 7.5% in morning trading today, reaching $548.95, as a sweeping recovery in AI-linked and industrial stocks lifted...
- [Caterpillar (CAT) Falls In Broad Pullback As Undervalued Narrative Stays In Focus](https://www.google.com/goto?url=CAESogEBxCJF13UiPjpxfMIgh4M3SWbzaBmZirjsmGLN_0SltIeIxRdGSo03mp4VgvHroEWK3wppCA6aMgIVA9kZdMO-XkwOVKCA4vXESHhxiA0YoU0Rsp0sCKc1Ew2n2OfATXoA1l8heurh8bwdCXB70QGfVImTIQ4yj2F8OyNzYweRIAN46sTi8TVsZw6f50gRy2DvXyIW_PjymXjOTP5IhfDfR_Y&gsessionid=Yp1JqrbEeGWiPtFZLYacEKfKfmNpXKJQVUziwKqrOhJgnoO96Me0fg)  
  <sub>Yahoo Finance, 20 hours ago</sub>  
  Caterpillar (CAT) is back in focus after the stock fell 5.0% on November 20, 2026, during a broader pullback in AI linked companies, despite no fresh...
- [The Midterms Put Data Center Permitting Back in Play. Here Are 2 Industrial Stocks That Win if Power Moves Behind the Meter.](https://www.google.com/goto?url=CAES6gEBxCJF1-zVOPAZT_1PlXtJJUY3Wb7kCY1ybywKG8WS6wb07km6Q3-3sM2x8fhptxIivZr_HlziWDnGJtqCR9yR_PIgb8FAy5EozkuUkV80G4JC71xCuzW4iUAvkr0BaTe65_WXWcl7_vkPyNcyT5ricV5pmeYqGmysghXDQdfUXbTogITeVATYhc1GxMrKYdH6OJrVkTSS6QQso64m1svgojH1Twnq9LTGUPNO3ogAK31KUXsU3VeVA-6PE2T2RgHbhaZcXSFqdGxCuhQj0003oy3yfKaUbT_lXaJRkjrvG2_qnIOgCeG4ybU&gsessionid=Yp1JqrbEeGWiPtFZLYacEKfKfmNpXKJQVUziwKqrOhJgnoO96Me0fg)  
  <sub>The Motley Fool, 15 hours ago</sub>  
  Bloom Energy and Caterpillar have sold off sharply along with the AI sector, but shifting electricity trends could support long-term business success.
- [Nasdaq surges 7% as the AI trade roars back after Jensen Huang is reinstated as Nvidia CEO](https://www.google.com/goto?url=CAESlgEBxCJF1wRZs1-zvZ3ZadLpBvFlOEqSxAJPHzE76-y_-rzsRgfK2HNNEyvkOQ9avTVGiQvJu1U5u6BrsVNw_r3o7drXZzUkmnZ8gXghKmGRcX4Ng2YidlbTGCY7qnWKbNjJmFKbm_ctyf-WHygXgikQqhy_hZJF2HgDzFNIX05Xud7PD3jCfwXApHR-7g79Mk_X2OCLvng&gsessionid=Yp1JqrbEeGWiPtFZLYacEKfKfmNpXKJQVUziwKqrOhJgnoO96Me0fg)  
  <sub>Business Insider, 23 hours ago</sub>  
  Jensen Huang is back and the stock market couldn't be happier. AI stocks are in the midst of a sharp rebound as traders raced to buy Friday's dip and took...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.10</summary>

_Not available today._

</details>

<details><summary><b>Price and chart</b> — score -0.40</summary>

```text
Last close 542.63 (bar of 2026-11-24), from 501 daily bars
Trend: vs 20d SMA 587.64 (-7.7%), 50d 704.66 (-23.0%), 200d 802.17 (-32.4%); 50d below 200d
Momentum: RSI(14) 34.0 | MACD -47.483 vs signal -48.306 (histogram 0.823)
Returns: 1d -0.8% | 5d -4.9% | 1m -21.6% | 3m -34.0%
52-week range: 510.45 - 1,064.90 (now 5.8% of the way up)
Volatility: ATR(14) 28.89 (5.3% of price) | annualised 20d 66.1%
Volume: 0.07x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.50</summary>

```text
Sector: Industrials / Farm & Heavy Construction Machinery | market cap 248.30B
Valuation: trailing P/E 21.30 | forward P/E 16.86 | P/B 11.56 | PEG 0.96
Profitability: profit margin 15.2% | operating margin 18.8% | ROE 56.1%
Growth (YoY): revenue +17.3% | earnings +46.1%
Balance sheet: debt/equity 210.4% | free cash flow 3.97B
Risk: beta 1.64 | short interest 2.0% of float
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

<details><summary><b>What analysts and big funds say</b> — score +0.70</summary>

```text
Consensus: buy (mean 1.97 on a 1=strong buy to 5=strong sell scale, 26 analysts)
Ratings: 2 strong buy, 15 buy, 11 hold, 1 sell, 0 strong sell
Price target: mean 807.26 (+48.8% vs last close), range 575.00 - 1,027.00
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

<details><summary><b>Buying and selling by company insiders</b> — score +0.10</summary>

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

<details><summary><b>Who is positioned how</b> — score +0.10</summary>

_Not available today._

</details>

<details><summary><b>Money going into and out of this fund</b> — score +0.10</summary>

_Not available today._

</details>

### Alphabet (Google) (GOOGL) · Company — BULLISH, confidence 0.45

**Result:** REJECTED · no room under the sleeve budget limit

**In the model's own words:**

> Mixed signals: strong AI‑driven rally in news and bullish analyst consensus suggest upside, but technicals show a downtrend with low volume and a weak earnings record dampen confidence. Fundamentals are solid but earnings momentum is poor, leading to a modest bullish view with moderate conviction.

**Main reasons it gave:**
- 6% rally on AI news after Nvidia CEO reinstated
- Technical downtrend: price below 20‑day, 50‑day, 200‑day SMAs and volume at 0.08× 20‑day average
- Strong fundamentals: low trailing P/E (14.5), high profit margin (50%) and ROE (44%)
- Weak earnings record: 3 misses and 1 beat in the last 4 quarters
- Analyst consensus strong‑buy with mean price target $395.77 (+42% upside)

<details><summary><b>News</b> — score +0.80</summary>

- [Alphabet Vs Meta: Which Stock Is The Better Buy?](https://www.trefis.com/stock/googl/articles/628287/alphabet-vs-meta-which-stock-is-the-better-buy/2026-11-24)  
  <sub>Trefis, 6 hours ago</sub>  
  Alphabet and Meta Platforms are both bought for AI that sells more advertising. They part ways in how they earn from it. Alphabet also sells AI computing...
- [GOOGL Nov 2026 315.000 put (GOOGL261123P00315000) Stock Price, News, Quote & History](https://ca.finance.yahoo.com/quote/GOOGL261123P00315000/)  
  <sub>Yahoo! Finance Canada, 6 hours ago</sub>  
  Find the latest GOOGL Nov 2026 315.000 put (GOOGL261123P00315000) stock quote, history, news and other vital information to help you with your stock trading...
- [Why Is Google Stock Up Today? Alphabet Jumps 6.3% as Nvidia's Huang Return Sparks AI Rally](https://www.google.com/goto?url=CAESrwEBxCJF1zfOglCrPu4eJcjU4MIls3WXPC853Kdsg4F0zrL39lIcc6bWsGNVynwDAAaEvxpyKkg3taj-6pZ4eZbWDk-mZ24zLHy8PL0jCaPpJ53-bM-lLS_bVm6fELc-1r-COHjgC6gdUbZvVLftt0xr7erDb0x0Dx0bSuRBW3ztrsmHEmf-0GrP1oMNn1cZWSb0oKBx47RuMIvhVNL8FLLWrqAguXl4SaK6Ipm1LUxF&gsessionid=k3BdVwSEb0-gs9dqcOCNdBdMQmtoIEhxFNIbtVbeyge8PrDlYndl2Q)  
  <sub>Around Prague, 16 hours ago</sub>  
  Alphabet (GOOGL) rose 6.34% to $282.10 on Monday as Nvidia reinstated Jensen Huang as CEO, lifting AI stocks and the Nasdaq 6.51% in a broad market rebound.
- [Alphabet Stock Pops: What's Going On?](https://www.google.com/goto?url=CAESnAEBxCJF1yzEiV50hmjE5kKgpoVAxY1Te-xqz5D-NA2_IR1B_GXS-OhlX9BodK1zSzjQtHhoOoG3fEWtO5WWVCLWFNIDgTgCn1Vvwx6s45HnoeHX5tcIiE5eu0PMeabQy11a74-UK503rXLrZqbRAJAHvQnJRVIBQPiS1MPXWPLgar-r2ikxKHJzMK2op8nBU0jQTEV_tboiMtcrLoc&gsessionid=k3BdVwSEb0-gs9dqcOCNdBdMQmtoIEhxFNIbtVbeyge8PrDlYndl2Q)  
  <sub>Benzinga, 19 hours ago</sub>  
  Alphabet Inc. (NASDAQ: GOOG) shares are soaring Monday as AI stocks rebound after Nvidia reinstated Jensen Huang.
- [Alphabet rises 6% as broad market rally lifts shares (GOOG:NASDAQ)](https://www.google.com/goto?url=CAESngEBxCJF1-ZdrMkIZYSm97kfZB7rsu_DDtcD6uOcymGnOC6vfBy_gyPjfpM9DGCj3MwP6cQHJiF2QCWhEdYRChsawajMWeO_iYmlC8Y6DKERLPXc5sOCNGnG73H5heQMGjjbPHNUzh_yqOW63zPbGTp-pKfZ2TwvhnCwhota0hwxJn5LsrmpDvZJCcWsq-pwtfb37gV3fnhIprTuByLqgg&gsessionid=k3BdVwSEb0-gs9dqcOCNdBdMQmtoIEhxFNIbtVbeyge8PrDlYndl2Q)  
  <sub>Seeking Alpha, 16 hours ago</sub>  
  Google parent Alphabet (GOOG) (GOOGL) climbed almost 6% today as the shares rebounded alongside a broad market rally. The stock finished at $279.53,...
- [Which "Magnificent Seven" Stocks Win From Anthropic’s IPO?](https://www.google.com/goto?url=CAESygEBxCJF1wmSw7QSB41BwB5N0_FfDKsEMJ57q6R_UAM7xrbnlNsgbs27PK9iydtNZ139zjLyraU9491xKgSY5saMwHr5gfwxGHI0SNFnSBXjzlLMEwSqtX6Cyr9nqKLg3gETbGxsyIjtXYhWfJNcile_w1EgwsIwLtRnB0dVIZMvnSwOgamEnh3fkiOMwWYfSpe2Pnx-tuWi1luIncl8Nrq7rKzPIjme9im6-CUW09iK8xGn3s-eJS6JM2wIG-t7HWqF3wVOs0qKjqyt&gsessionid=k3BdVwSEb0-gs9dqcOCNdBdMQmtoIEhxFNIbtVbeyge8PrDlYndl2Q)  
  <sub>The Globe and Mail, 3 hours ago</sub>  
  Detailed price information for Alphabet Cl A (GOOGL-Q) from The Globe and Mail including charting and trades.
- [GOOGL Nov 2026 260.000 call (GOOGL261123C00260000) stock price, news, quote and history](https://www.google.com/goto?url=CAESdQHEIkXXIuuus76CUg67u1TKpfIaOBIQw8nAZSK-JFoIreLKqVcLoYZO_eRaX6tMGzt3qJ_nQfXtsQaP2TZyuXHa1FXQ_ssxNtc9UOz3YB2ZuBiRmBIW5AAcTPMo1kRyS7et77LqxaZwoxMnMvEocKAOqkuLwg&gsessionid=k3BdVwSEb0-gs9dqcOCNdBdMQmtoIEhxFNIbtVbeyge8PrDlYndl2Q)  
  <sub>Yahoo Finance UK, 6 hours ago</sub>  
  Find the latest GOOGL Nov 2026 260.000 call (GOOGL261123C00260000) stock quote, history, news and other vital information to help you with your stock...
- [GOOGL Dec 2026 260.000 call (GOOGL261224C00260000) stock price, news, quote and history](https://www.google.com/goto?url=CAESdQHEIkXXkVGHSs9IiMGznGAWfLUkW2LFdG6zbTkHfgoiAfMGswQuPJePu26RpbiIpE9Fqk9AdILLaf-loO66dxQtcW5yiZTN4PT4ZeF534K1ERAXrr6czs23-R_6JqTiehcB1jRS4erVKhHvIgbkqjneywwO3g&gsessionid=k3BdVwSEb0-gs9dqcOCNdBdMQmtoIEhxFNIbtVbeyge8PrDlYndl2Q)  
  <sub>Yahoo Finance UK, 6 hours ago</sub>  
  Find the latest GOOGL Dec 2026 260.000 call (GOOGL261224C00260000) stock quote, history, news and other vital information to help you with your stock...
- [GOOGL Nov 2026 300.000 put (GOOGL261123P00300000) Stock Price, News, Quote & History](https://www.google.com/goto?url=CAESdQHEIkXX8LI4TbGylEpLSFf3WJE-w4ZaXwPpJPZfG4awdy5YLVwwWvKnHSTYIdNKFezMfQ_KHYoPhIk3WrPTUye24pFupZKpfw-EYZLnax-C8114GknKZEIwaslzMgSHgwYeY2-oJx1zaGZGO40ZMYBZaJ-LJA&gsessionid=k3BdVwSEb0-gs9dqcOCNdBdMQmtoIEhxFNIbtVbeyge8PrDlYndl2Q)  
  <sub>Yahoo! Finance Canada, 10 hours ago</sub>  
  Find the latest GOOGL Nov 2026 300.000 put (GOOGL261123P00300000) stock quote, history, news and other vital information to help you with your stock trading...
- [GOOGL280121C00405000 Interactive Stock Chart | GOOGL Jan 2028 405.000 call Stock](https://www.google.com/goto?url=CAEScQHEIkXXI10K6YPy5TAjmb35tQx8ts1KYuyixkWrg0KIvzHtwhP5mwqfrju9qVSzmaV4Bgt50QEmzgbVs2c3fJuvBOZgZNrdZFwnhwPHy2SpbtBERRtwDmR-F2xWCrgubAJKt0ZQElpcvyVOAk2j8zAL&gsessionid=k3BdVwSEb0-gs9dqcOCNdBdMQmtoIEhxFNIbtVbeyge8PrDlYndl2Q)  
  <sub>Yahoo Finance, 8 hours ago</sub>  
  At Yahoo Finance, you get free stock quotes, up-to-date news, portfolio management resources, international market data, social interaction and mortgage...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.80</summary>

_Not available today._

</details>

<details><summary><b>Price and chart</b> — score -0.60</summary>

```text
Last close 278.04 (bar of 2026-11-24), from 501 daily bars
Trend: vs 20d SMA 285.59 (-2.6%), 50d 319.62 (-13.0%), 200d 336.54 (-17.4%); 50d below 200d
Momentum: RSI(14) 39.2 | MACD -12.258 vs signal -12.849 (histogram 0.591)
Returns: 1d -1.4% | 5d -0.8% | 1m -12.2% | 3m -18.7%
52-week range: 265.29 - 402.62 (now 9.3% of the way up)
Volatility: ATR(14) 11.43 (4.1% of price) | annualised 20d 58.9%
Volume: 0.08x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.30</summary>

```text
Sector: Communication Services / Internet Content & Information | market cap 3.42T
Valuation: trailing P/E 14.52 | forward P/E 18.18 | P/B 5.18 | PEG 0.94
Profitability: profit margin 50.0% | operating margin 33.3% | ROE 44.3%
Growth (YoY): revenue +24.7% | earnings -25.3%
Balance sheet: debt/equity 22.2% | free cash flow -1.16B
Risk: beta 1.23 | short interest 1.5% of float
Next earnings: 2027-02-03
```

</details>

<details><summary><b>What this fund holds</b> — score +0.30</summary>

_Not available today._

</details>

<details><summary><b>Does this company beat its own forecasts</b> — score +0.30</summary>

```text
Earnings record, last 4 quarters: 1 beat, 3 missed
  2026-09-30 missed by 14% | 2026-06-30 missed by 4% | 2026-03-31 missed by 3% | 2025-12-31 beat by 4%
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

<details><summary><b>What analysts and big funds say</b> — score +0.60</summary>

```text
Consensus: strong_buy (mean 1.38 on a 1=strong buy to 5=strong sell scale, 53 analysts)
Ratings: 10 strong buy, 43 buy, 6 hold, 0 sell, 0 strong sell
Price target: mean 395.77 (+42.3% vs last close), range 300.00 - 500.00
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

<details><summary><b>What analysts say about what this fund holds</b> — score +0.60</summary>

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

### Teva Pharmaceutical (TEVA) · Company — NEUTRAL, confidence 0.40

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Mixed signals across dimensions: news is slightly bearish but also contains bullish analyst rating; technicals show short‑term weakness; fundamentals are weak on debt and revenue growth but forward P/E suggests cheapness; analyst consensus is bullish with a sizable price target; earnings record is positive overall; insider activity provides little directional clue. The contradictions lead to a neutral stance with low conviction.

**Main reasons it gave:**
- Mixed news: bearish article on Q3 revenue decline vs bullish analyst buy rating (Seeking Alpha, analyst rating)
- Technical weakness: price below 20‑day and 50‑day SMA, RSI 44.6, volume 0.03× 20‑day avg
- Fundamentals: high debt/equity 212.9% and revenue -1.9% YoY, forward P/E 12.79 indicating cheap valuation but weak growth
- Analyst consensus: buy with mean price target $50.51 (+26% upside) suggesting bullish outlook
- Insider activity: net +0.3% shares but 10 insiders sold, no distinct buying, providing little signal

<details><summary><b>News</b> — score -0.20</summary>

- [Teva Pharmaceutical: I'm Staying Cautious Despite Its Progress (NYSE:TEVA)](https://seekingalpha.com/article/4971427-teva-pharmaceutical-im-staying-cautious-despite-its-progress)  
  <sub>Seeking Alpha, 27 minutes ago</sub>  
  The bear case on Teva Pharmaceutical Industries Limited: risk/reward seen as unattractive; Q3 revenue fell 1.8%, though Ajovy, Uzedy and Austedo sales grew.
- [Teva Pharmaceutical Industries Limited (TEVA) Stock Price, News, Quote & History](https://ca.finance.yahoo.com/quote/TEVA/latest-news/)  
  <sub>Yahoo! Finance Canada, 22 hours ago</sub>  
  Teva Pharmaceutical Industries Limited (TEVA) ... This price reflects trading activity during the overnight session on the Blue Ocean ATS, available 8 PM to 4 AM...
- [FDA Approval for TREPROSTINIL DIOLAMINE issued to ACTAVIS LABS FL](https://www.google.com/goto?url=CAESqQEBxCJF17iO0cONWQDoVfL6l1PlTMDWUhRQL5JDbHEBDOX967sHS0uDhifpM9ANxLqLK2dsAtyjsMzh4_vtCI8SfyJ6PmuijXCsyGuF6o2pcm2Vs7K7g4nLmrQcqdFVUPbpDZb5bxAF8Gi9weV1PLC1bQvL5F8tp4wOIZwTQyxdjJ8N64PyBjYs9vrbaOvhhpdtFGllhQ32ub8QeJdywtTmcZG0heuKmQWs&gsessionid=0kohENv_g80vHI9SrtCPTAmD2hGZhn5wReud1hjB_5d9JW2sQXhIPg)  
  <sub>Quantisnow, 9 hours ago</sub>  
  Submission status for ACTAVIS LABS FL's drug TREPROSTINIL DIOLAMINE (ORIG-1) with active ingredient TREPROSTINIL DIOLAMINE has changed to 'Approval' on...
- [Teva's Mixed SMA Signals: Should You Stay Invested or Exit the Stock?](https://www.google.com/goto?url=CAES1QEBxCJF151ttzMrNaIOB32uaPj0H7OZWZ_s0SKVwQNolnU8LQqeMvwAjvQVZiJTP8wNYtwhSV_aeP_N1d0Vc71g5M5cH2KiEVxhES4W-vY1gb-EkU-NXzqJfi-owfJ83ViSAHfQLSJviFLug0Zj3qVKknIIk_kOWWrxqc_DyCfjTpjd3SkfuGiGU89zW0YbCWBnGf0cLH0UCUnsdM04gW1Bij8v8nSrIepTITgoSxrGKr-vlOASbGcFu9RApZ1qpYGpveyu4PKEG3wwC2w6jvZWRadYOT8&gsessionid=0kohENv_g80vHI9SrtCPTAmD2hGZhn5wReud1hjB_5d9JW2sQXhIPg)  
  <sub>The Globe and Mail, 20 hours ago</sub>  
  Teva Pharmaceutical Industries Limited TEVA stock slipped below its 50-day simple moving average (SMA) on Nov. 19, after consistently trading above this...
- [Teva Pharmaceutical: I Was Wrong To Doubt This 5-Star Management Team (NYSE:TEVA)](https://www.google.com/goto?url=CAESqgEBxCJF1w9rJ48aFEGEMGyBCDYrdUnLTtgQdnE5j9f_1XubBVFwLCHx2oG03THbXQrHVduKNRdIsMo-TSsrWZj3niHMdEhWW0nj1dkOIqfrrXzLjgLlAkaFkwC79bsfaD8H0d0HT8FeHDZ3DFVLCwy79a7HYAXoiyAsMWBaAqy1iVqI4-6gZKnWbFvtagcxvX7HnPXCrsa387ypsR15amtvIw6vLQMITaMG7g&gsessionid=0kohENv_g80vHI9SrtCPTAmD2hGZhn5wReud1hjB_5d9JW2sQXhIPg)  
  <sub>Seeking Alpha, 59 minutes ago</sub>  
  Analyst rates Teva Pharmaceutical Industries Limited a Buy: its turnaround expands innovative medicines and leaves room for gains, with gross margins above...
- [Teva Pharmaceutical Industries Ltd. $TEVA Stock Sold by State Street Corp](https://www.google.com/goto?url=CAESwgEBxCJF1zD4fZc1Q3l0HLZv4pT99tsaLRmWS8CgInN1kowVvVzzt-vjKOS6lHO3A9hKcFey-5hASTRsi1r9hekgp4avtnoVQP-0IaSzRNYGc3ESJV2XGc298tvC2yJKeOuXERZXoUGdwSE8HdBDT7jtG5amje9zX16kL-bUrKAytVinXAtu9t4w2Tzra2Usi0tNduJXBiR6j8J-Re3wIicZwe_6MKgy6OZVb_FL2qpW2oIZBX0z5ed8PtwSfuKpRm6o9Q&gsessionid=0kohENv_g80vHI9SrtCPTAmD2hGZhn5wReud1hjB_5d9JW2sQXhIPg)  
  <sub>MarketBeat, 4 hours ago</sub>  
  State Street Corp trimmed its stake in Teva Pharmaceutical Industries Ltd. (NYSE:TEVA - Free Report) by 49.0% in the 3rd quarter, according to the company...
- [Teva Pharmaceutical Industries Limited (TEVA) stock price, news, quote and history - Yahoo Finance](https://www.google.com/goto?url=CAEScQHEIkXXtWg7keS2eITERUFQ36AWw_lStTCWaMyase_U9nzvlh-j4XsGzMQtINpCNrD4wJPPg8gV3GYRG_jnn_-yi7E0ZHtKTTETbG-sZMgbgKqFpcZQCMntxxpoOOXF0-IAg7xPBJdbiA5-DLwPopD6&gsessionid=0kohENv_g80vHI9SrtCPTAmD2hGZhn5wReud1hjB_5d9JW2sQXhIPg)  
  <sub>Yahoo Finance Singapore, 22 hours ago</sub>  
  Teva Pharmaceutical Industries (TEVA) Earnings Put Its Turnaround Valuation Back In Focus.
- [Medincell shares rebound 4.5%, supported by Teva's Uzedy sales](https://www.google.com/goto?url=CAEStAEBxCJF13S3gqxqijQkIKcYNc8K3CnfipASGzTcJh8wFVZhp8RkBA5XXL6_mQ7sxqp-HUISBqlT8VtbAx3WwYXlzsvUbk2IlxKtuaTWifa6uUsrJa3wHDNihcwhIPpmMEhqlCnM-eXC6K9XXG-qxeAnUPaBkD71Jt0qVgmCSfyDFg0TxcqDFcLXVEKWAV4WI3D0H4OzxoJZCM8jPEyUwe6Om48RgXz1a0JNLUR13YZDeEh_vwQ&gsessionid=0kohENv_g80vHI9SrtCPTAmD2hGZhn5wReud1hjB_5d9JW2sQXhIPg)  
  <sub>Idéal Investisseur, 22 hours ago</sub>  
  Medincell shares gained 4.49% to €27.90 at the close, while the SBF 120 rose 1.60% and the CAC 40 rose 1.59%. The stock is among the largest gainers in the...
- [TEVA Dec 2026 38.000 call (TEVA261204C00038000) interactive stock chart](https://www.google.com/goto?url=CAESegHEIkXXZGnXAgjoF2SztkaB0igghe8BLNDXEX9R1XJEc9iOnZtrmqdjV_o0RE7Ou46wK9EROg2TtR8_nkXjG6k64fTntCCfgccrb9gtmRo3tdeqbXvinHmdM2J3QqUP92RVQPC3Iqli29NRO0wWiSkDXQpMuhFmKBkv&gsessionid=0kohENv_g80vHI9SrtCPTAmD2hGZhn5wReud1hjB_5d9JW2sQXhIPg)  
  <sub>Yahoo Finance UK, 13 hours ago</sub>  
  Interactive chart for TEVA Dec 2026 38.000 call (TEVA261204C00038000) – analyse all of the data with a huge range of indicators.
- [TEVA Dec 2026 49.000 call (TEVA261204C00049000) Interactive Stock Chart - Yahoo Finance](https://www.google.com/goto?url=CAESegHEIkXXh05nOS5yCHByPdNSoIcU0pPhkcbWkF68Vm7nmH3l5AP-Q4e_5KzH3kuWWcu-sRFMElRNkux_ItQkEVIM2Uq2a5rBzeoq3cySF9iHfO8EKxJ_eH0b0ODEgIuOwyYEskQLPzCLS-HIb7fRWSv5SFcKRGaSFLVb&gsessionid=0kohENv_g80vHI9SrtCPTAmD2hGZhn5wReud1hjB_5d9JW2sQXhIPg)  
  <sub>Yahoo! Finance Canada, 20 hours ago</sub>  
  Interactive Chart for TEVA Dec 2026 49.000 call (TEVA261204C00049000), analyze all the data with a huge range of indicators.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score -0.20</summary>

_Not available today._

</details>

<details><summary><b>Price and chart</b> — score -0.50</summary>

```text
Last close 40.04 (bar of 2026-11-24), from 501 daily bars
Trend: vs 20d SMA 41.72 (-4.0%), 50d 40.66 (-1.5%), 200d 35.30 (+13.4%); 50d above 200d
Momentum: RSI(14) 44.6 | MACD -0.074 vs signal 0.387 (histogram -0.460)
Returns: 1d +0.2% | 5d -6.1% | 1m +0.2% | 3m +5.6%
52-week range: 24.77 - 44.50 (now 77.4% of the way up)
Volatility: ATR(14) 1.35 (3.4% of price) | annualised 20d 45.4%
Volume: 0.03x the 20-day average
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

<details><summary><b>What analysts and big funds say</b> — score +0.50</summary>

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

<details><summary><b>What analysts say about what this fund holds</b> — score +0.50</summary>

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

### ASML (ASML) · Company — NEUTRAL, confidence 0.35

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Fundamentals are very strong, but technicals are bearish and the recent price rally is driven by a broad sector move rather than a company‑specific catalyst. The mix of bullish fundamentals and bearish technicals, plus generic news, leads to a neutral view with low conviction.

**Main reasons it gave:**
- 9% price jump on chip rally (news)
- Price below 20‑day, 50‑day, 200‑day SMAs; RSI 38.8; volume 0.10× 20‑day avg (technical)
- Profit margin 34.1%, ROE 65.6%, low debt/equity 8.9% (fundamentals)
- 3 earnings beats, 1 miss in last 4 quarters (earnings)
- Consensus strong buy, mean rating 1.37, price target +56% vs last close (analyst)

<details><summary><b>News</b> — score +0.30</summary>

- [ASML (ENXTAM:ASML) Stock May Trade At A Premium Following Its 107% Run](https://finance.yahoo.com/markets/stocks/articles/asml-enxtam-asml-stock-may-111607325.html)  
  <sub>Yahoo Finance, 3 hours ago</sub>  
  ASML Holding has seen its stock more than double over the past three years, while headlines around artificial intelligence hardware keep pulling the share...
- [Why ASML Stock Popped Today](https://www.google.com/goto?url=CAESggEBxCJF1_PLAMt2PX4A7NPQSGhYnWta7AmNDVDyY31dvulMZ2EMZyO6n6tWIachkkYSp0PpM6_TjFvEnnwO0ZrEalRKk5KWHcKTcsnsSH6Q6ndo3J6AJDK7IGXGpFk3ZhehTvSjtd-f_koahVDz9LSz1ZqnkwyMKFdyK7Z1xMZ1BoV8&gsessionid=w62km_FBT-Z1Shuj6BXWO-a0vvgu3bUwBZu4g_i3TiUV0uIFxR70fA)  
  <sub>The Motley Fool, 16 hours ago</sub>  
  Shares of ASML (ASML +9.28%) were among the winners today as the semiconductor sector surged on news that Jensen Huang was returning as the CEO of Nvidia.
- [ASML surges 9% as chip stocks rally (ASML:NASDAQ)](https://www.google.com/goto?url=CAEShAEBxCJF1zOnORbh1smiV379GDh-VrLnBmXbITvQrmHj7zxtPTN5NCHQRtsM1JU0dvimimZzFBknURKxoBoAVJJdzk-oli6Ep2qHb5bDMNmZbe0SO_b2KM948UMEbgqWoh3WUbU2Wiu4qwSIRb0lV4HDMiYY74LZx-n6YpXcerrgwoX0Sss&gsessionid=w62km_FBT-Z1Shuj6BXWO-a0vvgu3bUwBZu4g_i3TiUV0uIFxR70fA)  
  <sub>Seeking Alpha, 17 hours ago</sub>  
  ASML Holding shares rise 9% to $1383.16 in a broad chip-stock rally, though they remain down more than 22% over the past month.
- [ASML Stocks Jump 9.59%; Company Bought 557 Million of Its Shares in Selloff Week](https://www.google.com/goto?url=CAESxwEBxCJF1xKFEf3kSaY0JndnZF8e3OdVzPiYs-OjbZTpnXXHLC080yOpV-AAVeQoBnNDYhRWclF2OTQVTuQ1gnNer3eI-OVZppYdOoEzLcccqvK_IEk1u8kCZbXURxH9DeVv1_bPu4Ds9CajSkHgA9WvBQueNStzLSd9wBUFpBLzAcjOBNoCzCDnx8OkF7QmqfFjwbBatxqTsp4z_KCv2e4KQ08pZ29bW7WwOXIJmfqDCuDnQSrQwo1GqBELToyTG0rvDsCrsiAI&gsessionid=w62km_FBT-Z1Shuj6BXWO-a0vvgu3bUwBZu4g_i3TiUV0uIFxR70fA)  
  <sub>TradingView, 22 hours ago</sub>  
  ASML Holding NASDAQ:ASML shares rose 9.59% to $1387.63 at 9:55 a.m. ET in regular trading on November 23, as the Dutch lithography maker joined the chip...
- [ASML Stock’s Sell-Off Looks Excessive Against Its Growth Outlook](https://www.google.com/goto?url=CAESlgEBxCJF1-wU1kB7rRUZl3dSQBGZfeFgoYGbY7hmQ2fhYRvyTr3btrXLrXXs9mrjq5FBfX2ugyYEhfrwG9KeCOHcBilK_2NloVDl4rvxwvrgCG1r-tz6mb-0MgQKj-A6AsN4cqpmkJjWkYZ0NEFGxlLHcyWYqhkyywgZBul0liaYlsMK8D_UnIH4o8T_nLRhprN7uJl_mig&gsessionid=w62km_FBT-Z1Shuj6BXWO-a0vvgu3bUwBZu4g_i3TiUV0uIFxR70fA)  
  <sub>Yahoo Finance, 17 hours ago</sub>  
  ASML Holding's (ASML) stock sell-off looks excessive against its growth outlook, in my view. The lithography equipment manufacturer reported record...
- [ASML Dec 2026 940.000 call (ASML261224C00940000) stock price, news, quote and history](https://www.google.com/goto?url=CAEScwHEIkXXgPC6HuoxUi7A1BuAXWgxJ-m6fB95g-9P1wvsaOP3aXHi_4PtfRaU2bLMVr5DiT5REH8Ci6w3Dlc-B9oii5J_QC7xYjYPzWnOD5pvTcvClrIcpTC9oI0onxHLdwrkFaRaKSlZeYXbXlSocrQpo8A&gsessionid=w62km_FBT-Z1Shuj6BXWO-a0vvgu3bUwBZu4g_i3TiUV0uIFxR70fA)  
  <sub>Yahoo Finance UK, 5 hours ago</sub>  
  Find the latest ASML Dec 2026 940.000 call (ASML261224C00940000) stock quote, history, news and other vital information to help you with your stock trading...
- [ASML Apr 2027 1710.000 call (ASML270416C01710000) stock price, news, quote and history](https://www.google.com/goto?url=CAEScwHEIkXX1aN2v-_lDjbjHKJyNxa1H9dLFPSM-WwFCcJeneXbgIwlzim8-02XtM7lo3nKln-4AeITqP_9sesUckD4qt2W90hSkyTSiRig1A_KWAl30f6u4HoUGurN2bGoFBMCyQ8d3wDXTNa1F5tPGECtpLw&gsessionid=w62km_FBT-Z1Shuj6BXWO-a0vvgu3bUwBZu4g_i3TiUV0uIFxR70fA)  
  <sub>Yahoo Finance UK, 6 hours ago</sub>  
  Find the latest ASML Apr 2027 1710.000 call (ASML270416C01710000) stock quote, history, news and other vital information to help you with your stock trading...
- [ASML Nov 2026 2130.000 call (ASML261127C02130000) Interactive Stock Chart](https://www.google.com/goto?url=CAESdgHEIkXXLw9X04rjQR2DqWu3YELz9iHkVvjyWZZJWKu2BpBV8XDSiGAz1PpQDRNlSrfR1IY7NKkjDlox9WxOgH6is9x7TS_hZXtC5Qbh7gxSeAYU6_9q5XT3TiWb4tmfM0cx5ieZBmqnY2tD0JhPcckP9BCC1B0&gsessionid=w62km_FBT-Z1Shuj6BXWO-a0vvgu3bUwBZu4g_i3TiUV0uIFxR70fA)  
  <sub>Yahoo Finance, 16 hours ago</sub>  
  Interactive Chart for ASML Nov 2026 2130.000 call (ASML261127C02130000), analyze all the data with a huge range of indicators.
- [ASML Nov 2026 1550.000 call (ASML261127C01550000) Stock Price, News, Quote & History](https://www.google.com/goto?url=CAEScwHEIkXXBwihVp5HyYaQlblo3w8OzYYJQhohH4LUUrHuYxgBMmjg89HLpao0wHKkHQ51CPeFbbMIZ8qamH_asorpUrSqKAkf2H_DXh9jiXzGREikI9t8PrRXv8kcdlsehi_uwFQ5kH6HJzT-rMvUIs5p5WM&gsessionid=w62km_FBT-Z1Shuj6BXWO-a0vvgu3bUwBZu4g_i3TiUV0uIFxR70fA)  
  <sub>Yahoo! Finance Canada, 16 hours ago</sub>  
  Find the latest ASML Nov 2026 1550.000 call (ASML261127C01550000) stock quote, history, news and other vital information to help you with your stock trading...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.30</summary>

_Not available today._

</details>

<details><summary><b>Price and chart</b> — score -0.50</summary>

```text
Last close 1,349.55 (bar of 2026-11-24), from 501 daily bars
Trend: vs 20d SMA 1,467.46 (-8.0%), 50d 1,616.08 (-16.5%), 200d 1,600.96 (-15.7%); 50d above 200d
Momentum: RSI(14) 38.8 | MACD -78.357 vs signal -70.752 (histogram -7.605)
Returns: 1d -2.5% | 5d -2.4% | 1m -15.2% | 3m -22.7%
52-week range: 987.82 - 1,989.44 (now 36.1% of the way up)
Volatility: ATR(14) 72.20 (5.3% of price) | annualised 20d 72.5%
Volume: 0.10x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.70</summary>

```text
Sector: Technology / Semiconductor Equipment & Materials | market cap 520.14B
Valuation: trailing P/E 33.21 | forward P/E 21.29 | P/B 1,158.79 | PEG 0.68
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

<details><summary><b>What analysts and big funds say</b> — score +0.20</summary>

```text
Consensus: strong_buy (mean 1.37 on a 1=strong buy to 5=strong sell scale, 17 analysts)
Ratings: 7 strong buy, 31 buy, 2 hold, 1 sell, 0 strong sell
Price target: mean 2,108.78 (+56.3% vs last close), range 849.59 - 2,790.87
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

<details><summary><b>What analysts say about what this fund holds</b> — score +0.20</summary>

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

### Elbit Systems (ESLT) · Company — no answer, no confidence given

<details><summary><b>News</b> — score n/a</summary>

- [$100 Invested In Elbit Systems 10 Years Ago Would Be Worth This Much Today](https://www.benzinga.com/news/26/11/63565838/100-invested-elbit-systems-10-years-ago-would-be-worth-much-today)  
  <sub>Benzinga, 16 hours ago</sub>  
  Elbit Systems (NASDAQ:ESLT) has outperformed the market over the past 10 years by 8.02% on an annualized basis producing an average annual return of 20.6%.
- [ESLT261120C00590000 Interactive Stock Chart | ESLT Nov 2026 590.000 call Stock](https://finance.yahoo.com/chart/ESLT261120C00590000)  
  <sub>Yahoo Finance, 9 hours ago</sub>  
  At Yahoo Finance, you get free stock quotes, up-to-date news, portfolio management resources, international market data, social interaction and mortgage...
- [Elbit : Awarded a Contract to Supply Naval EW Suites for Germany](https://www.google.com/goto?url=CAESrgEBxCJF1xStrS9AU_ClnWkXvnmmUZglpPnUzRNaeI7Pz-QGp_SZfWGIZgQbkPvtszxDPpyBrGZiX-ZZroOzLGLhmEaeUKmZPFkEdPlxI_XP661-OKw-9--rhbVywzxdb__AfBYDBB_qq5JDVfqkLR20olaWeGJbkXYOlg0ejvjkfTAdXPiTHrc2ZzWTIwzpszKNCktNvJq-bg2Q6cIXiZpcNLrFQVSblMy_z2r1rU4&gsessionid=-2MAF2MpveTlFexXY5HuQ0sC_EbyESZmxk3OJbsDJKPrdUoftfdzKA)  
  <sub>www.marketscreener.com, 3 hours ago</sub>  
  24 November, 2026 Elbit Systems Ltd.'s German subsidiary, Elbit Systems Deutschland GmbH & Co. KG , was awarded a contract to supply naval Electronic...
- [Elbit Systems stock: Radomatics plan links $80m orders to stake](https://www.google.com/goto?url=CAEStwEBxCJF16tacpIZJo2_eOkf3U8vIFyazNWpj5h7Gh9HlPD0n-hCK3V2KVuEpiWe7EXHo6nR21mxW1tnanJJOy0Cn9qrKZcvPLS5MupAALjhT_VTEw2W4Hd2YtW667Sv5IFcz6K9b9DODf5ZYIK2yYLv8x2lxFcMqIfgUcv9gRTU311KcNBITF5gtSvwUMolfdohjzc0ZX3i0pYXa3x4PcvF53Kxz0VUOTIfuM3eiMMbmbekz-wwI9A&gsessionid=-2MAF2MpveTlFexXY5HuQ0sC_EbyESZmxk3OJbsDJKPrdUoftfdzKA)  
  <sub>ad-hoc-news.de, 22 hours ago</sub>  
  Elbit Systems stock is in focus after a non-binding term sheet tied to future product orders. The framework could deepen cooperation with Radomatics.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>Price and chart</b> — score n/a</summary>

```text
Last close 667.11 (bar of 2026-11-24), from 501 daily bars
Trend: vs 20d SMA 714.73 (-6.7%), 50d 718.45 (-7.1%), 200d 785.14 (-15.0%); 50d below 200d
Momentum: RSI(14) 42.2 | MACD -15.687 vs signal -9.306 (histogram -6.381)
Returns: 1d -0.4% | 5d -7.4% | 1m -14.2% | 3m -7.7%
52-week range: 454.95 - 1,014.33 (now 37.9% of the way up)
Volatility: ATR(14) 26.82 (4.0% of price) | annualised 20d 63.0%
Volume: 0.04x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score n/a</summary>

```text
Sector: Industrials / Aerospace & Defense | market cap 31.27B
Valuation: trailing P/E 47.01 | forward P/E 32.75 | P/B 6.84 | PEG n/a
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
Price target: mean 837.33 (+25.5% vs last close), range 739.00 - 935.00
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

- [HDFC Bank Limited (HDB) stock price, news, quote and history](https://uk.finance.yahoo.com/quote/HDB/)  
  <sub>Yahoo Finance UK, 6 hours ago</sub>  
  HDFC Bank Limited (HDB) · 3.20% · 20.90% · 9.66% · -25.55% · -26.02% · -20.70% · 3,642.07%. Key events. Baseline. Advanced chart. Loading chart...
- [8,218,297 HDFC Bank Limited $HDB Shares Sold by Boston Partners](https://www.marketbeat.com/instant-alerts/filing-8218297-hdfc-bank-limited-hdb-shares-sold-by-boston-partners-2026-11-24/)  
  <sub>MarketBeat, 5 hours ago</sub>  
  Boston Partners reduced its stake in shares of HDFC Bank Limited (NYSE:HDB - Free Report) by 99.0% during the 3rd quarter, according to its most recent 13F...
- [85008HFS29 Bond Yield and Price — BSE:85008HFS29](https://www.google.com/goto?url=CAEScAHEIkXXLpP-7YIVl1aSejk3MT3CB7DtGLNxkK0Eq-vUNFfZ6IupP2_fUNXyuXzf_KSqpwXQYOvZhK7eYoU2Het3uEQFz8xyFTcUxFRyST5DfF_Z-uPWmA8DTdGvhHDM4FLIBh_HBb8tehvcTCwDvVw&gsessionid=h-Wg1Q8LcOYJEtmO5N80nJK4H7lCjvFaEdxG6W4TZIx19VkSrPDoLQ)  
  <sub>TradingView, 4 hours ago</sub>  
  Track HDB Financial Services Limited 8.5008% 04-DEC-2029 corporate bond price and yield with the live chart. Explore 85008HFS29 coupon and redemption...
- [Car believed to have skidded into HDB flower bed; driver, 66, suffers minor injuries but declines hospital treatment](https://www.google.com/goto?url=CAESxQEBxCJF11kuFmr2JFZFcoKoXBjIMZUUaqrBS8nRIJMeRmze6o7tWeAkFKDD7qfKncMr6P8oIiOD9acqKHrW2PPjw2NrIGH6fcFaYiFfGSacnCoS5FVn1P053-sHZ0AM0UPw8FVlUCjDYlYBpCrFN8n07QdsJ2BJ5-5fl9icZ0MWuINt-w_9iLwX9k-qZNv6MEw2NZd5ITFFn5wDBCqkB0arxiAR4VXOT-uyMhU466J4pwykzWgB3luIj1AEEhClgajmAS90Cg&gsessionid=h-Wg1Q8LcOYJEtmO5N80nJK4H7lCjvFaEdxG6W4TZIx19VkSrPDoLQ)  
  <sub>联合早报, 4 hours ago</sub>  
  Did an attempt to reverse into a parking space end in a flower bed? A silver car crashed into a flower bed behind open-air parking spaces beside Block 908A...
- [Man, 66, injured after car mounts kerb near Woodlands HDB block, Singapore News](https://www.google.com/goto?url=CAEShAEBxCJF18qJYjjzjnTQW0NKa00BccS36X0ckV63Xx6bdRKQRB6JKOMOkDMAbXmWiAU2kNFq1pws6cKNvBvmCW08wuCIAT_dggFZMtCgYeuwwoJbd_MJdB6lyfpB-WBcy3h8jug4pxRbk7ZdDO72Y64bnVnPskHv8CXpH5tp_ACS6Or6QH4&gsessionid=h-Wg1Q8LcOYJEtmO5N80nJK4H7lCjvFaEdxG6W4TZIx19VkSrPDoLQ)  
  <sub>AsiaOne.com, 5 hours ago</sub>  
  A man sustained minor injuries after a car mounted a kerb at an HDB block in Woodlands on Tuesday (Nov 24).A video of the accident's aftermath,...
- [A $3.5 Billion Fund Dumps These 3 Stocks](https://www.google.com/goto?url=CAESfwHEIkXXuTkAYzyBochOPUimWPjp2KRwHmhM0VIoTkD8CDyq3gLvEwc-SSVJIFCD45T38ARyELXmBqVm5R426gwUzhk2xzl7mI71AXiGnI1q0cAVvYgNICqvubh9gc94AhhxsUf2lIVljV_IMRxRGvOeowDIlKLls0qL7ZX8VJc&gsessionid=h-Wg1Q8LcOYJEtmO5N80nJK4H7lCjvFaEdxG6W4TZIx19VkSrPDoLQ)  
  <sub>TIKR.com, 21 hours ago</sub>  
  A $3.5 billion fund sold all of its HDFC Bank, News Corp and Aya Gold & Silver shares in the third quarter, its latest 13F shows. In the same quarter,...
- [10 PINE CLOSE HDB For Room Rental m_2312609](https://www.google.com/goto?url=CAESlgEBxCJF12JEsLqYvPMauVitZ01MXnGoipz7wmgKmq24bL9a3KrCYc7oPs0Sw224hr4CKKiRJ-YKllIBoFeIeF7FdXCDxXZiTYEQMR7VGFOQgMw2Thl7ETe4w50JqUcidmCx6OQ7JQKMDzuTlv1sogfpiekJqk5Ve6uwSzgudFR6-j-o2Bs8BMzprWhIHwJkxBRksdmK4fk&gsessionid=h-Wg1Q8LcOYJEtmO5N80nJK4H7lCjvFaEdxG6W4TZIx19VkSrPDoLQ)  
  <sub>EdgeProp.sg, 9 hours ago</sub>  
  PINE CLOSE Female tenants only. Rooms share for 2 possible at $ 1600.. Professional, Students and working people welcome. City-Fringe Living with Excellent...
- [5 charged over alleged illegal food delivery services, including 3 accused of abetting offences](https://www.google.com/goto?url=CAESmwEBxCJF19Y7JlfkEsLaqXwb1ujIMlvsiL0yQth_Kjl6q0xirufNDpAuheqj1fKv7mIIMppJwpv-jbzdNWWrZutULSf9gTg-d9gwQ-c-N4hv2uig9GWzQsliEElwzs5GdoLO-9cC02H_D1aooy_uA_-AiB0gqJeVEvxQQ_1tIkQIJlCHiWCaxT_e7H8hHv9wpD2pHQQ3pAC_0FOiHQ&gsessionid=h-Wg1Q8LcOYJEtmO5N80nJK4H7lCjvFaEdxG6W4TZIx19VkSrPDoLQ)  
  <sub>AsiaOne.com, 10 hours ago</sub>  
  Five people have been charged over allegedly performing or abetting illegal food delivery work, said the Ministry of Manpower (MOM) on Tuesday (Nov 24).
- [HDB DCF Analysis: Intrinsic Value $30 vs Price $27](https://www.google.com/goto?url=CAESkwEBxCJF16O4rYiLUMNFZXRrnB1Vf16FnYIa-ucrfBpAZdwXZ3NEiRvlCbpcFBv3tLkt5Gd-ZVhWpsfWbQm9mHAikkk54nfqq_FOS3U-RNqydBYCnuD11fu5fJalbZr8rNjYnprgPQjlWl-pOXSsLkELhyyFr7HxRPHkAjyQ6MTwb2dZYFFZlzJ1h9VXxCGQB7AVSL0&gsessionid=h-Wg1Q8LcOYJEtmO5N80nJK4H7lCjvFaEdxG6W4TZIx19VkSrPDoLQ)  
  <sub>GuruFocus, 2 hours ago</sub>  
  On November 24, 2026, we delve into the DCF analysis for HDFC Bank Ltd (HDB), a company that has experienced significant price fluctuations recently.
- [Largest IPOs in India: Top 10 by Issue Size (2026)](https://www.google.com/goto?url=CAEScwHEIkXXfo9OiWj_Vm5zZIDU14rz6JmtnFSHL_zDuke7cWKkRuuMcFFUny9pA4EtFe1n3Vj3H_gcR6YWc8rQhft4sx3dNIYE-MyOtIQDX-Fdfaa74TyjnCLmSHd_NtaxFSM6gK8Bh-ANgV6JbLe2V6s_G-M&gsessionid=h-Wg1Q8LcOYJEtmO5N80nJK4H7lCjvFaEdxG6W4TZIx19VkSrPDoLQ)  
  <sub>Business Outreach Magazine, 3 hours ago</sub>  
  As of October 2026, Hyundai Motor India still holds the record for the largest completed IPO in India by issue size. The National Stock Exchange (NSE) has...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>Price and chart</b> — score n/a</summary>

```text
Last close 27.30 (bar of 2026-11-24), from 501 daily bars
Trend: vs 20d SMA 25.08 (+8.8%), 50d 23.62 (+15.6%), 200d 25.19 (+8.4%); 50d below 200d
Momentum: RSI(14) 75.2 | MACD 1.108 vs signal 0.931 (histogram 0.176)
Returns: 1d +0.6% | 5d +4.0% | 1m +25.7% | 3m +17.8%
52-week range: 21.36 - 36.82 (now 38.4% of the way up)
Volatility: ATR(14) 0.63 (2.3% of price) | annualised 20d 26.4%
Volume: 0.04x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score n/a</summary>

```text
Sector: Financial Services / Banks - Regional | market cap 140.45B
Valuation: trailing P/E 17.61 | forward P/E 19.71 | P/B 10.87 | PEG n/a
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
Price target: mean 30.30 (+11.0% vs last close), range 26.20 - 33.00
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

- [JPMorgan Chase (JPM) Stock Still Looks Like A Bargain On Its 122% Run](https://finance.yahoo.com/markets/stocks/articles/jpmorgan-chase-jpm-stock-still-091521471.html)  
  <sub>Yahoo Finance, 5 hours ago</sub>  
  JPMorgan Chase has given long term shareholders a powerful ride over the past few years, and with recent swings around news on outages, cyber issues and...
- [JPMorgan Chase (JPM) Stock Looks Undervalued On Current Profitability](https://www.google.com/goto?url=CAESvAEBxCJF1-EhedjyOhKcU1qJX4PNXC67hoVdH8Y6vikNG86yIa4fhtv_9VRo5Vxa0Tmroant7L6xhVUSM4B93CP7F4srY83Y-lMPXm7hZ65JKnsruXu5NG_cayTTbb_C4lkJ_Qt4QBN0V4lMV-v319kfMc0QrbQ9oyZ52PPXSrDulMwSWAbPFEokuD70e3NkKcm0WcvyX7rPbQoarYc0qB76tMKB3abEUS99uK4_1Ucq4svAVGKCHsgTJLxyMQ&gsessionid=PG37RIUViOvK5qtbpXNIiA6yJWHLf_75MxMmKawO_yMxxcP7fTwqKA)  
  <sub>Simply Wall St, 5 hours ago</sub>  
  JPMorgan Chase has delivered a powerful 5 year share price run. The recent pullback and steady stream of headlines now put a sharper focus on whether the...
- [Bank stocks recover from Friday's tumble (JPM:NYSE)](https://www.google.com/goto?url=CAESigEBxCJF1-BAXDb5VqoECKEnyi4G0XibyJ6qj1tugldz8GjPhoiWOITJptM3hYZ7C4uPT8FuwKC4haqX3xzF2y15TkeTAlnoCrsvk9NVC65tNKRs1bT8B3FJX5VtoqpzJw_gqWIRjXTnVs1kyXBvX7LG1qPjnVeOCWNgfj3uvwx4raArQ0pzFPw-L_o&gsessionid=PG37RIUViOvK5qtbpXNIiA6yJWHLf_75MxMmKawO_yMxxcP7fTwqKA)  
  <sub>Seeking Alpha, 21 hours ago</sub>  
  Bank stocks rebound Monday, with the SPDR S&P Bank ETF up 1.7% to $63.36, but it remains 4.7% below its Nov.
- [JPM Dec 2026 355.000 put (JPM261224P00355000) interactive stock chart](https://www.google.com/goto?url=CAESeQHEIkXXg2H8tPivzgBGyIXCmxDwx0ltzVT9MVW26Q3mC_YLyb6Ft_cunNuV_aKxIW35ZHDlHuQacDjCOCPBbE7LHsDt18usfgC-AaZbc0aVlZo2oNTd_gZDl98lJpomj6C7M8-2ZJqPWC2q4XpFGeLJa-94C8YjX-8&gsessionid=PG37RIUViOvK5qtbpXNIiA6yJWHLf_75MxMmKawO_yMxxcP7fTwqKA)  
  <sub>Yahoo Finance UK, 6 hours ago</sub>  
  Interactive chart for JPM Dec 2026 355.000 put (JPM261224P00355000) – analyse all of the data with a huge range of indicators.
- [JPMorgan's bond fund will leave the NYSE on Dec. 16](https://www.google.com/goto?url=CAEStAEBxCJF14gX7YUmlwNG3s9BOKbALt-6zGvS4pNwna06wFu4Rv1cuiWKpanKWQi7P57nFYOlRD-0B1EnkQLPcQ3-obMidYXZGHoPi9ox5ONv6GqnL5-2yQikGDagG13tFA27mwcFQqTFyRg2VEmigk8WkeZN2ewATcoI4BsAPtgx8_HQu5YhUA9x0B4uYKPcYoCeh6a9v3aOcvtn53PcqmSXe2dWzBtbGSq0l80wd9XVMSsfpnU&gsessionid=PG37RIUViOvK5qtbpXNIiA6yJWHLf_75MxMmKawO_yMxxcP7fTwqKA)  
  <sub>Stock Titan, 17 hours ago</sub>  
  The transfer is set for the Dec. 16 exchange opening; references to JBND's listing venue will then change from the New York Stock Exchange to NYSE Arca.
- [JPM Nov 2026 290.000 call (JPM261127C00290000) Stock Price, News, Quote & History](https://www.google.com/goto?url=CAEScwHEIkXXL1hniL3-XXWb6zDERFyY8rOGCTqftDtr_-WFkV2Yv9oYT2YW8LEQ2V5hFf8mJzCc_es1bfUmgN3A-W_NHG7Zg7Pn-KMwym4XsDfpwvFkB56Upa51z10t1whKkuVzdJjz2V7aX9GjCdGgsgoQNrk&gsessionid=PG37RIUViOvK5qtbpXNIiA6yJWHLf_75MxMmKawO_yMxxcP7fTwqKA)  
  <sub>Yahoo! Finance Canada, 10 hours ago</sub>  
  Find the latest JPM Nov 2026 290.000 call (JPM261127C00290000) stock quote, history, news and other vital information to help you with your stock trading...
- [Top Bank Stocks To Follow Now - November 23rd](https://www.google.com/goto?url=CAESowEBxCJF1_meAPMejKghCCcPJclpIXcN2Eyfi-r8IZGOLIQmd30ZVJlLZxeB5-HcxdHtjUq08xaSu9H-3QzFcUDFVuQfArSPRLTwXs5VQvOOwwP614r0-jeBs1H_WbePJ2hH-poHaLfFF8GMwm4_zokGf7xvvBIkLQKXjScJdfkf0K5ELvg6AYoHwP_AZp3Z73clhoYVpNjVFLO8UpR7N5scIcjE&gsessionid=PG37RIUViOvK5qtbpXNIiA6yJWHLf_75MxMmKawO_yMxxcP7fTwqKA)  
  <sub>MarketBeat, 21 hours ago</sub>  
  JPMorgan Chase & Co., Bank of America, Citigroup, Charles Schwab, and NU are the five Bank stocks to watch today, according to MarketBeat's stock screener...
- [JPM Mar 2027 295.000 put (JPM270319P00295000) interactive stock chart](https://www.google.com/goto?url=CAESeQHEIkXXd8i69gAwg_SKLAxvSfnpPjfvElE1fZy6XQoAyvPaqXMTdCC-RfcddMewN6KfY-g5iTqsAmbwt3UxgfoR0DnO5PLSm3XsqotA1Hdx5_gyfW_fAdaf7g4fpNGLM5JQ4KNcuX4oOF2gS8BJEmT_S-C5gTpG2PU&gsessionid=PG37RIUViOvK5qtbpXNIiA6yJWHLf_75MxMmKawO_yMxxcP7fTwqKA)  
  <sub>Yahoo Finance UK, 11 hours ago</sub>  
  Interactive chart for JPM Mar 2027 295.000 put (JPM270319P00295000) – analyse all of the data with a huge range of indicators.
- [JPMorgan and Bank of America Just Sold Off. One Looks Better for Retirees](https://www.google.com/goto?url=CAESsQEBxCJF1-VJxr5Wv8KI0Id-SmS7HfmMWhJdXivQwszCCUVvuQUqVr4RhAHA6yM3ldG4qZKbSgxFpagXFeux5MBvAKtycEuGhFhBwHTqy2nt1XoFr-wWqKm2-Kn21LWC86kRhjMNNMO0tNvxtSVmsCL277HrCfPR2hKCqdHNpa0MBaB988hDF7KBANWh_3zjnqZEN77cor3SwSauxAtvw5eF_83gs-AOHmFvZ4spByhsEYI&gsessionid=PG37RIUViOvK5qtbpXNIiA6yJWHLf_75MxMmKawO_yMxxcP7fTwqKA)  
  <sub>24/7 Wall St., 1 hour ago</sub>  
  JPMorgan beats Bank of America for retirement portfolios, as its capital cushion and stronger record make its dividend more dependable despite a pricier...
- [J.P. Morgan Analyst Sets Tesla Stock Price Target for 2026 and 2027](https://www.google.com/goto?url=CAESpQEBxCJF1-sjy8bIlsjdaCsPgJRSxdsOMM-j_jgOQIyR6vDQwtQRBhOuvyaIXSr0q_vKW8xw-r8lXQ0tx3JwIFilPOLgce9bM7bJmWzj3qOBcFY76lz_UmUeOnl4nLdWEbI4QR9if93yGMQPxxh_LzXdBDC_OtHj58fHqTmaNsALITCUmjnIT8yJXkxoK8ePTTMl_uucEnghEAYK61ZFqY-rwAVjK1Y&gsessionid=PG37RIUViOvK5qtbpXNIiA6yJWHLf_75MxMmKawO_yMxxcP7fTwqKA)  
  <sub>Coinpedia, 15 hours ago</sub>  
  With Tesla Inc. (NASDAQ: TSLA) stock having fallen more than 12% so far in 2026, Rajat Gupta, a Wall Street analyst at JPMorgan Chase & Co. (NYSE: JPM)...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>Price and chart</b> — score n/a</summary>

```text
Last close 316.27 (bar of 2026-11-24), from 501 daily bars
Trend: vs 20d SMA 334.75 (-5.5%), 50d 335.96 (-5.9%), 200d 325.14 (-2.7%); 50d above 200d
Momentum: RSI(14) 36.6 | MACD -5.550 vs signal -2.617 (histogram -2.933)
Returns: 1d -0.1% | 5d -4.1% | 1m -5.3% | 3m -11.3%
52-week range: 282.84 - 365.18 (now 40.6% of the way up)
Volatility: ATR(14) 7.77 (2.5% of price) | annualised 20d 32.0%
Volume: 0.04x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score n/a</summary>

```text
Sector: Financial Services / Banks - Diversified | market cap 839.92B
Valuation: trailing P/E 13.27 | forward P/E 12.37 | P/B 2.39 | PEG 1.32
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

- [Eli Lilly going all-in on oncology deals: Bloomberg (LLY:NYSE)](https://seekingalpha.com/news/4676116-eli-lilly-going-all-in-on-oncology-deals-bloomberg?source=generic_rss)  
  <sub>Seeking Alpha, 1 hour ago</sub>  
  Eli Lilly (LLY) sees oncology as its next growth engine, with eight cancer drugs expected to reach market within five years amid YTD deals worth $20B. Read...
- [LLY261204P01400000 Interactive Stock Chart | LLY Dec 2026 1400.000 put Stock](https://finance.yahoo.com/chart/LLY261204P01400000)  
  <sub>Yahoo Finance, 5 hours ago</sub>  
  At Yahoo Finance, you get free stock quotes, up-to-date news, portfolio management resources, international market data, social interaction and mortgage...
- [Eli Lilly and Co(LLY) Stock Price Today | Quotes & News](https://www.google.com/goto?url=CAES_wEBxCJF17KpvdAslQRzc9mel6K4X2A8GABKQHwgkBVRYDN-k4fbNIc2BvkpXxM2DEgvbHBujZ066WTd9PeJQsElRo0z03juysBmAm1cO917KMmPVAasgtcxpYrSm7cIhyeXbGyKpDyUDNrWUFBKm-soNgyM6YtAhShT_j65HiUCq3BnYOJNv_APOMT1ig8J7ZmBnPa1NdwnnlprHtXrJTNKFplPT2zNZizScDyT6Xo1ceg4Iue8afAK6X-iKCm_f62S3j3gHSgVCpPaOeNiCT03hI1ZEAcn3oDNwG5TG-Da36ATJVMZNQGuGJ8U7sHYkPQOFVTo9s7cT5Ouz3Y-jBQ&gsessionid=C69viYWUiBHxqdv0p6CUKuvjrX6PjmyHx3KefVSpU7E86-hpuHXMDQ)  
  <sub>Moomoo, 19 hours ago</sub>  
  Track the latest Eli Lilly and Co(LLY) stock price, quotes, financial information, news and analyst rating on moomoo App for your stock trading and...
- [LLY Nov 2026 1417.500 put (LLY261127P01417500) Stock Price, News, Quote & History](https://www.google.com/goto?url=CAEScwHEIkXXb18qlPrOislDlRIJGBRpFi7gu_92LYPIFNRyyxz8cIgjpM6-P97P-5YDfn9ft_J1AGWA3F2-hFMIt7OCKVx3WE0LsGHhMg077sSX_dXb3OqhpgUE-aT7nnb1wqYfAtQrFsYIwdjVaMBcAud0fx8&gsessionid=C69viYWUiBHxqdv0p6CUKuvjrX6PjmyHx3KefVSpU7E86-hpuHXMDQ)  
  <sub>Yahoo! Finance Canada, 9 hours ago</sub>  
  Find the latest LLY Nov 2026 1417.500 put (LLY261127P01417500) stock quote, history, news and other vital information to help you with your stock trading...
- [LLY261224C01370000 Interactive Stock Chart | LLY Dec 2026 1370.000 call Stock](https://www.google.com/goto?url=CAESbwHEIkXXAZanyEmzO2dudDWmdfNUW2ONgvPGB26OPdzbmpvORQ6LQf-xmSkWVWtEfnLsqyvKRa1bXvUhk-v50nSDy1lNm-GfIIyLCjZNa3WqjvE2qKgHLEygoSgorzSSN5JlV9SOJvxemZp-PcAT3Q&gsessionid=C69viYWUiBHxqdv0p6CUKuvjrX6PjmyHx3KefVSpU7E86-hpuHXMDQ)  
  <sub>Yahoo Finance, 9 hours ago</sub>  
  At Yahoo Finance, you get free stock quotes, up-to-date news, portfolio management resources, international market data, social interaction and mortgage...
- [LLY Nov 2026 1365.000 call (LLY261127C01365000) interactive stock chart](https://www.google.com/goto?url=CAESeQHEIkXXcLjUq149IFG2mr9pWW-F0m5sL8qZPcrbCPA2rf7Kf7RSILkz5hxBezyglOd0Lhp_SDrOlzoQqZw16729FiPS5wid-yOO-q6tvpFTKe3DFBWjVsVX9XK76KHn7TflXTDc9B-4WdhgtcNNXEkjSaSzWl5tuOQ&gsessionid=C69viYWUiBHxqdv0p6CUKuvjrX6PjmyHx3KefVSpU7E86-hpuHXMDQ)  
  <sub>Yahoo Finance UK, 9 hours ago</sub>  
  Interactive chart for LLY Nov 2026 1365.000 call (LLY261127C01365000) – analyse all of the data with a huge range of indicators.
- [Will 'Anti-Pharma' Democrats Chop Away At Biotech Stocks' Big Wins?](https://www.google.com/goto?url=CAESqwEBxCJF128aHy3zO5wNEuftr-UwLLyWxf-d85YrXsPFxmbBGequ-RrnH1YEh0yHtajy-57yADiKmXM9hA7ZkLCz9oRUhn8Shnt4B6KCZP_sLzLXoYePw0hSA96kCx2mdHJSKLE4dL0jgqAhHiXSxXU6kRgsdOf3WjVs2DZ_Wh9EhocgKI0eTVleEdUdPvkdxu0EZ_gVVLLujJ-SkWDeZMSk5DpP4eTMuLzdXno&gsessionid=C69viYWUiBHxqdv0p6CUKuvjrX6PjmyHx3KefVSpU7E86-hpuHXMDQ)  
  <sub>Investor's Business Daily, 2 hours ago</sub>  
  Biotech stocks have traded somewhat uneasily in the wake of the blue tsunami that swept Washington D.C. earlier this month.
- [LLY Dec 2026 1500.000 call (LLY261231C01500000) interactive stock chart](https://www.google.com/goto?url=CAESeQHEIkXXoYgT5VP3Sqv24DPLgrmwp_TPkdBa3fw81zrCy1RIZpChH24kFYdcTB75iEOIFHT_tbOVqV00OkdWKQZztPzY9L1p7HKpo1iQXyiJ5n9pvE95F_luz7vuhd7ACnJJ7oHN9zWRYEJB2BALpnhNVUSN35-NfDk&gsessionid=C69viYWUiBHxqdv0p6CUKuvjrX6PjmyHx3KefVSpU7E86-hpuHXMDQ)  
  <sub>Yahoo Finance UK, 10 hours ago</sub>  
  Interactive chart for LLY Dec 2026 1500.000 call (LLY261231C01500000) – analyse all of the data with a huge range of indicators.
- [Eli Lilly vs. Vertex Pharmaceuticals: Which Healthcare Stock Is a Better Buy for 2027?](https://www.google.com/goto?url=CAESxgEBxCJF15aNPT6LvDugf0ts7k-VTVEtzP_GPqfrYPXSu45SgERmZANSENX7Te3yfTGimtDhFlYViN7QZWghsfruScfVFFWqaMRO_QDZLz4YM6jwZ4naCTabrFaEicmSBjhZ2IH7UFp8FnJ2qsj6Zxsf6jdX8aC82QOlh29oMUmiB_Pc_S32Le1XFr1U_wOpJ_rI1WkFucy6K4HiYL59iNLhA6iVtNunp6_V09xc9uiLwA9un42qUR3G2Yf1Fl9WgClBU6o8IlQ&gsessionid=C69viYWUiBHxqdv0p6CUKuvjrX6PjmyHx3KefVSpU7E86-hpuHXMDQ)  
  <sub>The Motley Fool, 23 hours ago</sub>  
  Will the next few years favor a diversified giant with massive volume growth or a biotech pioneer with specialized blockbusters? Eli Lilly & Co. (LLY...
- [LLY Dec 2026 1445.000 call (LLY261224C01445000) interactive stock chart](https://www.google.com/goto?url=CAESeQHEIkXXjpmin__pMHminHX_ZEFHnngHtLRUugp8yLiEszBJRUM4zoou9vSZF8ofiNXkTLk5UNNH-57XJvziI_IkFYJPkMqw6Hkp08nhkvUdtf-aaWKhy8s7_3yFkZS9WV7jGJ7SPCBgigskPv7IKl2j8pYR_LnkH_E&gsessionid=C69viYWUiBHxqdv0p6CUKuvjrX6PjmyHx3KefVSpU7E86-hpuHXMDQ)  
  <sub>Yahoo Finance UK, 13 hours ago</sub>  
  Interactive chart for LLY Dec 2026 1445.000 call (LLY261224C01445000) – analyse all of the data with a huge range of indicators.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>Price and chart</b> — score n/a</summary>

```text
Last close 1,404.79 (bar of 2026-11-24), from 501 daily bars
Trend: vs 20d SMA 1,394.33 (+0.8%), 50d 1,276.82 (+10.0%), 200d 1,121.23 (+25.3%); 50d above 200d
Momentum: RSI(14) 58.9 | MACD 28.720 vs signal 40.252 (histogram -11.531)
Returns: 1d +2.9% | 5d -0.8% | 1m +9.8% | 3m +18.1%
52-week range: 851.21 - 1,443.50 (now 93.5% of the way up)
Volatility: ATR(14) 42.07 (3.0% of price) | annualised 20d 38.2%
Volume: 0.07x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score n/a</summary>

```text
Sector: Healthcare / Drug Manufacturers - General | market cap 1.25T
Valuation: trailing P/E 45.61 | forward P/E 27.62 | P/B 31.10 | PEG 1.25
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
Price target: mean 1,470.06 (+4.6% vs last close), range 940.00 - 1,700.00
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

- [MELI Nov 2026 1780.000 call (MELI261127C01780000) interactive stock chart](https://uk.finance.yahoo.com/quote/MELI261127C01780000/chart/)  
  <sub>Yahoo Finance UK, 5 hours ago</sub>  
  Interactive chart for MELI Nov 2026 1780.000 call (MELI261127C01780000) – analyse all of the data with a huge range of indicators.
- [MELI261127C01555000 Interactive Stock Chart | MELI Nov 2026 1555.000 call Stock](https://finance.yahoo.com/chart/MELI261127C01555000)  
  <sub>Yahoo Finance, 6 hours ago</sub>  
  At Yahoo Finance, you get free stock quotes, up-to-date news, portfolio management resources, international market data, social interaction and mortgage...
- [MELI Nov 2026 1765.000 call (MELI261127C01765000) Interactive Stock Chart - Yahoo Finance](https://www.google.com/goto?url=CAESegHEIkXXFBqQ1hlEJy4NmGd7OIoDwnXxCvXogSwqvBxxMqi9S8lHE-uU207eOzjnsBROLLLGyksWs3ZNegOrnXeIUWumcvdGZIUbE80_X6tWEy0R8krBcwVfCqzL3Y0yaSXKOZxiOYlLnj5Vmw7J1Apgl312iDtB-hoM&gsessionid=hRrArQkHA_z-04nG8OBWpxkWH1bZzQnsYhHPC1eJsCI7SrjbJzqB_A)  
  <sub>Yahoo! Finance Canada, 7 hours ago</sub>  
  Interactive Chart for MELI Nov 2026 1765.000 call (MELI261127C01765000), analyze all the data with a huge range of indicators.
- [MELI Nov 2026 1805.000 call (MELI261127C01805000) stock price, news, quote and history](https://www.google.com/goto?url=CAESdAHEIkXXPUKYiT-Z_pA1ryKrx4T1UCQlF1rZSN-YLmFKe1OabLMVSkWIllO9iJJvp3Qq0pgLb_oio9Ii4FM_RYUZBwtyMpefR6iJe_TMn0Owc5B0jVSyA3uEhnm7Ep_Z9_o2DrmaQC2H5VG4fu-XtDjQOzsH&gsessionid=hRrArQkHA_z-04nG8OBWpxkWH1bZzQnsYhHPC1eJsCI7SrjbJzqB_A)  
  <sub>Yahoo Finance UK, 8 hours ago</sub>  
  Find the latest MELI Nov 2026 1805.000 call (MELI261127C01805000) stock quote, history, news and other vital information to help you with your stock trading...
- [MELI Dec 2026 1915.000 put (MELI261204P01915000) interactive stock chart](https://www.google.com/goto?url=CAESegHEIkXXIDmSc0Zmq-ruUosRnKlkz6a3WAx03H5Cd0QdOGNWdVzWHIKmbVLEEt3C_s0Kb2PHzQJplyxZmMgF_0lh_6NxpLwKjuDN9kpCgRFta4tLwtZb7RPjXfrZFQ52QhunwafmCTRU_WRSbD26DLzAsqawDlbWWpNC&gsessionid=hRrArQkHA_z-04nG8OBWpxkWH1bZzQnsYhHPC1eJsCI7SrjbJzqB_A)  
  <sub>Yahoo Finance UK, 7 hours ago</sub>  
  Interactive chart for MELI Dec 2026 1915.000 put (MELI261204P01915000) – analyse all of the data with a huge range of indicators.
- [MELI Nov 2026 1885.000 call (MELI261127C01885000) Interactive Stock Chart - Yahoo Finance](https://www.google.com/goto?url=CAESegHEIkXXQa4eZad6XJOFn8Rf6HTR9IN_zT9w3638gBdP4Jenigf-n624bivPfRBQSbJGd58KYe_KIMZLKkOPkFH2aEyX-jbEpwqpz2rRq45vYS-Kpv4AxLIJvGO0iUndO_YX4OZaRpYAWLbDe2n6lPcBTlmYD8qZ0u1x&gsessionid=hRrArQkHA_z-04nG8OBWpxkWH1bZzQnsYhHPC1eJsCI7SrjbJzqB_A)  
  <sub>Yahoo! Finance Canada, 9 hours ago</sub>  
  Interactive Chart for MELI Nov 2026 1885.000 call (MELI261127C01885000), analyze all the data with a huge range of indicators.
- [MELI Nov 2026 1600.000 put (MELI261127P01600000) stock price, news, quote and history](https://www.google.com/goto?url=CAESdAHEIkXXa04sg9pT3Nj-d8TQ410jNr2NDoioXwvvq9do2J2M95LeuuSHtgixqbSUryFxGmlOw8mqqnWas-ZVMUVh7jQPOi7xZEo7JyIMc5XuIEUeP0cRouAQekViaRGclf6cpawtFM-rE8dP3DmXHvgPSMsx&gsessionid=hRrArQkHA_z-04nG8OBWpxkWH1bZzQnsYhHPC1eJsCI7SrjbJzqB_A)  
  <sub>Yahoo Finance UK, 13 hours ago</sub>  
  Find the latest MELI Nov 2026 1600.000 put (MELI261127P01600000) stock quote, history, news and other vital information to help you with your stock trading...
- [MELI Nov 2026 1700.000 call (MELI261127C01700000) interactive stock chart](https://www.google.com/goto?url=CAESegHEIkXXXeJP2JRVpG0p5Vb2E-PR7GqZkW32Kh3RD-2GScJ6qq8Utcp7jdXkzsosS1mb1zla-9B3IeGyuLXxrza2nfUPuAHgf_-UrxvFGnFe_WPX3D1A3tf59u1DgnCEzlMiKwVq8xsMtc7pqI2BSSolgQPjvdA8Mvqr&gsessionid=hRrArQkHA_z-04nG8OBWpxkWH1bZzQnsYhHPC1eJsCI7SrjbJzqB_A)  
  <sub>Yahoo Finance UK, 13 hours ago</sub>  
  Interactive chart for MELI Nov 2026 1700.000 call (MELI261127C01700000) – analyse all of the data with a huge range of indicators.
- [MELI261127C02140000 Interactive Stock Chart | MELI Nov 2026 2140.000 call Stock](https://www.google.com/goto?url=CAEScAHEIkXXUu1LT3lKuQsejbyMxQhGUt98k14_NzdQ7cMxNxBiz-6pvdQi7r8iVYdMKNiaA38XxtYy-SSFGXiWQIVtn6jxdUdD5Om0kLj54odCuC-yFc1tvKbFYj4oDfrwGSYjJqfv6Afe6HfO17cKz5o&gsessionid=hRrArQkHA_z-04nG8OBWpxkWH1bZzQnsYhHPC1eJsCI7SrjbJzqB_A)  
  <sub>Yahoo Finance, 13 hours ago</sub>  
  At Yahoo Finance, you get free stock quotes, up-to-date news, portfolio management resources, international market data, social interaction and mortgage...
- [MELI Nov 2026 2050.000 call (MELI261127C02050000) Stock Price, News, Quote & History](https://www.google.com/goto?url=CAESdAHEIkXXE7X0NHvscqRd6_mMoP1I8TSjKyRBucTR6CL2YFzj1JiWAWvRJGEZ5Mvtuyd_NMQLYdZhJnY0xck2dH9YVQS7GAXqKi0vsjdqf0KpNw7RjBsecaoTWDEZ8K5ITxouUwnJTpj-V2npFgMfM0cPvra7&gsessionid=hRrArQkHA_z-04nG8OBWpxkWH1bZzQnsYhHPC1eJsCI7SrjbJzqB_A)  
  <sub>Yahoo! Finance Canada, 17 hours ago</sub>  
  Find the latest MELI Nov 2026 2050.000 call (MELI261127C02050000) stock quote, history, news and other vital information to help you with your stock trading...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>Price and chart</b> — score n/a</summary>

```text
Last close 1,435.97 (bar of 2026-11-24), from 501 daily bars
Trend: vs 20d SMA 1,523.60 (-5.8%), 50d 1,692.39 (-15.2%), 200d 1,760.70 (-18.4%); 50d below 200d
Momentum: RSI(14) 36.9 | MACD -93.671 vs signal -90.371 (histogram -3.300)
Returns: 1d +0.8% | 5d -0.1% | 1m -13.9% | 3m -26.4%
52-week range: 1,355.00 - 2,295.00 (now 8.6% of the way up)
Volatility: ATR(14) 61.21 (4.3% of price) | annualised 20d 57.8%
Volume: 0.05x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score n/a</summary>

```text
Sector: Consumer Cyclical / Internet Retail | market cap 72.83B
Valuation: trailing P/E 38.54 | forward P/E 27.12 | P/B 8.88 | PEG 0.74
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
Price target: mean 2,152.76 (+49.9% vs last close), range 1,600.00 - 2,700.00
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

- [NVIDIA Corporation (NVDA) Stock Price, News, Quote & History](https://ca.finance.yahoo.com/quote/NVDA/)  
  <sub>Yahoo! Finance Canada, 7 hours ago</sub>  
  NVIDIA Corporation (NVDA) · 5.71% · -21.76% · -23.35% · -11.50% · -7.73% · 419.91% · 377,157.15%. Key Events. Baseline. Advanced Chart. Loading chart...
- [Nvidia Faces an SEC Probe, According to Press Reports. Should You Still Buy the Stock?](https://www.fool.com/investing/2026/11/24/nvidia-faces-an-sec-probe-according-to-press-reports-should-you-still-buy-the-stock/)  
  <sub>The Motley Fool, 2 hours ago</sub>  
  Nvidia (NVDA +31.48%) has been a surefire artificial intelligence (AI) investment over the past few years. As the world's top AI chip designer, the company...
- [Live Updates: Huang’s Return to Nvidia Sparks Stock Rally and Lawmaker Skepticism](https://www.google.com/goto?url=CAESjQEBxCJF10Fqhac7wqiALC3sSJgu68GvLUoV5gpn5wjRAbUgMe36woU3gnEF-GWQSNvIXPwYm4UmbqCByMwl1XlA2wcymcg4a-XHZ7mGc2tD_Cz2PdsXnWIKQpqo_YWbjsCir9R4w4nMJYCdKH1Kro5D5VV3IdJJ4PoTV8wtkjWAMUlAaj7SPac-SK4H8WE&gsessionid=SningPpB0daCn3Ay9buhUC_rFaHdbQ_6zuCTDkTjrvh3bteZmjjTIQ)  
  <sub>The New York Times, 24 minutes ago</sub>  
  Mr. Huang resigned from the powerhouse chipmaker less than two weeks ago after revelations of his extramarital relationships, including one with a woman...
- [How NVDA Stock Rises To $235?](https://www.google.com/goto?url=CAESlAEBxCJF1y13m7HrSiB1sTtNxJ4orFRAOIs9CMsY3kCCI7Quokn7BKBJOCuyl4SuA2ltU9aVMhHrXVceAAlhGjnKrYsOgVLL4De_D7W0RbFkLENO161lYbEKHmGKaG1NXO2lrukqh1DryyCt1TKjcxnIE7cYkgnhCVLtMzz-_P84bfSf8UJXthm8cXRz1Gag25mvv_Wt&gsessionid=SningPpB0daCn3Ay9buhUC_rFaHdbQ_6zuCTDkTjrvh3bteZmjjTIQ)  
  <sub>Trefis, 21 hours ago</sub>  
  NVIDIA's (NVDA) board unanimously reinstated co-founder Jensen Huang as President, CEO, and director on November 23, 2026, igniting a roughly 30% intraday...
- [Jensen Huang Is Back As Nvidia CEO. Stock Jumps.](https://www.google.com/goto?url=CAEShgEBxCJF12J284Bpeykc_ehbGPFsfOnR-N4C2pp_npO4V3EBY-xC_VEG8ClAR0iMDzMd72kSN-PFq7O7wnqrQN0TUntfn-_Y7F2loahauV7mtfQTtkPGQXukI97yMIqHAAifdxKDd6GstFNuZ3RbI9l76pt8xLV-noS9KPLm2Sp22A7erbb0VQ&gsessionid=SningPpB0daCn3Ay9buhUC_rFaHdbQ_6zuCTDkTjrvh3bteZmjjTIQ)  
  <sub>Investor's Business Daily, 18 hours ago</sub>  
  Jensen Huang has been reinstated as Nvidia's CEO by the company's board. Nvidia stock rallied on the news.
- [NVIDIA Corporation (NVDA) stock price, news, quote and history](https://www.google.com/goto?url=CAESZAHEIkXXFvh_RaedRoeYuGHDVHAH6omgS-i3Cz2GsRZnRGtjV__oGPgbQJbRDrojOURb6MWtX8gIP73xOU0aoA32j0sVJU1bryITdGHAezXML7cYC6dTlmCbQCVSDNTRTS62Ul4&gsessionid=SningPpB0daCn3Ay9buhUC_rFaHdbQ_6zuCTDkTjrvh3bteZmjjTIQ)  
  <sub>Yahoo Finance UK, 10 hours ago</sub>  
  377,157.15% · Previous close 125.53 · Open 167.04 · Bid 164.00 x 100 · Ask 164.71 x 100 · Day's range 156.93 - 171.50 · 52-week range 124.50 - 243.37 · Volume...
- [Nvidia Stock Just Had Its Best Day in Over a Decade. I'd Still Buy It Now.](https://www.google.com/goto?url=CAESrwEBxCJF1346AXudJdafn9RylbWtQ_nqPkw1Lrkho-N59pGSnOyU8M73EoWKVRmD7SYhBtHvQ8_trcuxTx5H7mHTKfqVntRhwsQS9pijkIul5mfygzDMk8A5tCBX6YmVQn5-nHikhNPTEiOqB2owVT2JpYi9sECwVK24iBILQVIJH6roA_Nt3I1fB4BLL7F5Y6-5UoZIOoK-9YMOhQPyd0yjRCe9v0x1pGnu500Y86gp&gsessionid=SningPpB0daCn3Ay9buhUC_rFaHdbQ_6zuCTDkTjrvh3bteZmjjTIQ)  
  <sub>The Motley Fool, 9 hours ago</sub>  
  Nvidia (NVDA +31.48%) said on Monday, Nov. 23, that it had brought back Jensen Huang as president and CEO, effective immediately. Shares surged on the news.
- [Nvidia Shares Fall 5% in Premarket Trading as Goldman Sachs Highlights Lingering Uncertainty Following Huang’s Return](https://www.google.com/goto?url=CAESmwEBxCJF10KRa0-jcKmaywZqW-Pq6TYoR0auivVPr6o_D-vJri9FO2SiLD_zsq1bOxxOShdL4CmLyKVvuY3YiD_xw0Q-HvI8pYIzynkRK5FTXlFO6twacFe8_KqJ8Mg0eXSuiNsBY1hPUzQYxLNYw2H7Hj-gaPySFtmGEy9esZwsZYL3XYTexFIROv0lVXDUaIbPM9VlPKUGIYelIw&gsessionid=SningPpB0daCn3Ay9buhUC_rFaHdbQ_6zuCTDkTjrvh3bteZmjjTIQ)  
  <sub>Yahoo Finance, 3 hours ago</sub>  
  Nvidia (NASDAQ:NVDA) shares fell approximately 5% in premarket trading on Tuesday as investors reassessed the semiconductor company's outlook following the...
- [Breakfast News: Huang Returns. Your Next NVDA Move](https://www.google.com/goto?url=CAEShAEBxCJF18KoVZRzBgJ2nw2UCvBWpATA0j8u12EnIxyqfgM3iOEgBY7CeR3HNRVBf1JGK2EvL_9eQD7A4K61J-TkEPr38ppoxHnAPB7Kx-uBEYDzHWjR6yoJW2MdRQNXVk1cQ_PML-yIvQw7b5I-YRuyxkUVMOLs0KHR_91DbqEabFSF4Zo&gsessionid=SningPpB0daCn3Ay9buhUC_rFaHdbQ_6zuCTDkTjrvh3bteZmjjTIQ)  
  <sub>The Motley Fool, 2 hours ago</sub>  
  With Jensen Huang back as CEO of Nvidia (NVDA +31.48%), we've raised both of our five-year price predictions. Team Hidden Gems now sees the stock nearly...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>Price and chart</b> — score n/a</summary>

```text
Last close 155.37 (bar of 2026-11-24), from 501 daily bars
Trend: vs 20d SMA 175.78 (-11.6%), 50d 204.95 (-24.2%), 200d 203.07 (-23.5%); 50d above 200d
Momentum: RSI(14) 39.5 | MACD -17.267 vs signal -16.076 (histogram -1.190)
Returns: 1d -5.9% | 5d -0.1% | 1m -28.1% | 3m -25.9%
52-week range: 125.53 - 239.24 (now 26.2% of the way up)
Volatility: ATR(14) 13.09 (8.4% of price) | annualised 20d 137.8%
Volume: 0.18x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score n/a</summary>

```text
Sector: Technology / Semiconductors | market cap 3.75T
Valuation: trailing P/E 16.69 | forward P/E 9.36 | P/B 14.05 | PEG 0.15
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
Consensus: buy (mean 1.81 on a 1=strong buy to 5=strong sell scale, 57 analysts)
Ratings: 10 strong buy, 38 buy, 12 hold, 2 sell, 0 strong sell
Price target: mean 244.55 (+57.4% vs last close), range 130.00 - 425.00
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

### Novo Nordisk (NVO) · Company — no answer, no confidence given

<details><summary><b>News</b> — score n/a</summary>

- [Novo Nordisk A/S (NVO) Stock Price, News, Quote & History](https://ca.finance.yahoo.com/quote/NVO/)  
  <sub>Yahoo! Finance Canada, 20 hours ago</sub>  
  Novo Nordisk A/S (NVO) · -3.83% · 0.23% · -12.94% · -23.58% · -17.82% · -28.46% · 24,362.50%. Key Events. Baseline.
- [Novo Nordisk A/S (NVO) Is a Trending Stock: Facts to Know Before Betting on It](https://finance.yahoo.com/markets/stocks/articles/novo-nordisk-nvo-trending-stock-130004772.html)  
  <sub>Yahoo Finance, 2 hours ago</sub>  
  Novo Nordisk (NVO) has been one of the stocks most watched by Zacks.com users lately. So, it is worth exploring what lies ahead for the stock.
- [Novo Nordisk: The Wegovy Pill Opportunity Is Just Beginning (NYSE:NVO)](https://www.google.com/goto?url=CAESoAEBxCJF1ywSy8rGbogLgg1obJZDCGbWLB1e0qWh9A1M_-3aisxB8OGl7aq-eys0lFcBSLAbUWtzaBdtRyA_HHO9WQqMAW8hBS1bkaiktQeKJGs_MJqsBEptqRbGB-7Sjj4SaWPQtd95oqHaOHF4N5AkDHIydxiZqSg_1YuJeXO_yGo2wOjbCP5Va-F5sjR8m0_HyeHrnW5OIIzlz3pLz6xc&gsessionid=lnX8k8RwTJy87DB0LkywU2O1szs2sHnC5nQrk-u96KZkzDMcijrnaA)  
  <sub>Seeking Alpha, 23 hours ago</sub>  
  Analyst rates Novo Nordisk A/S a Strong Buy as 2026 adjusted sales and operating profit growth guidance rises to -2% to +2% at CER.
- [Novo Nordisk A/S (NOVO-B.CO) Stock Price, News, Quote & History](https://www.google.com/goto?url=CAESagHEIkXXE1zYjVBXq9uNwr9XEYdNlqlKx3xsMpfmJGQTn3fEZqcUMnyzfI-N16tABrchwIj5wcoGSj-Y7t1ta6DuUOaRIcISN8IbGEMSMZ-9kDjJLOIRfGMnbl7chk-gb4ck4rc8DLBPaT4&gsessionid=lnX8k8RwTJy87DB0LkywU2O1szs2sHnC5nQrk-u96KZkzDMcijrnaA)  
  <sub>Yahoo! Finance Canada, 18 hours ago</sub>  
  Find the latest Novo Nordisk A/S (NOVO-B.CO) stock quote, history, news and other vital information to help you with your stock trading and investing.
- [Novo Nordisk A/S (NVO) Latest Stock News & Headlines - Yahoo Finance](https://www.google.com/goto?url=CAESaQHEIkXXj8GLIHwGjZ2Orf126w6MiVzEt4Z9955AB_wohdXPhjZM1E78DcPXe0HXXS39wMpdLdDN2S54tZKFMGkR4axV1AOATqa7ErCyAidSPVoj3znZZRdosZjVkmbqtvuzFcdEqKVsVA&gsessionid=lnX8k8RwTJy87DB0LkywU2O1szs2sHnC5nQrk-u96KZkzDMcijrnaA)  
  <sub>Yahoo! Finance Canada, 20 hours ago</sub>  
  Novo Nordisk A/S (NVO).
- [Novo Nordisk A/S (NVO) interactive stock chart](https://www.google.com/goto?url=CAESagHEIkXXYwekKoMV7ozgUxqzUmBRrEhjLeY5fRSRyv19VSlF63kBG2Yy4-6SLg0uCfN_ZdbmMRd4KJvhfl8Caq982gRpi0fQIe7LWxSt-rZaE2q5hwLdp-1l8aRkfU_ucikqp38TvXUBElA&gsessionid=lnX8k8RwTJy87DB0LkywU2O1szs2sHnC5nQrk-u96KZkzDMcijrnaA)  
  <sub>Yahoo Finance Australia, 6 hours ago</sub>  
  Interactive chart for Novo Nordisk A/S (NVO) – analyse all of the data with a huge range of indicators.
- [Novo Nordisk A/S (NVO) stock price, news, quote and history](https://www.google.com/goto?url=CAEScAHEIkXXAa0mr4DhqAh3i1C1xddwXjqpbvUyc7FuwlKU5mcuIESuPc9W6RPpVFe3b6_J8WfdGwFGjOQnFHJAeioLHvclWRMuYXwCoR7Oh-StO4N9av2cz45J95fhvkUPbbQ_HUF5u_qnXDVmG9F0dyc&gsessionid=lnX8k8RwTJy87DB0LkywU2O1szs2sHnC5nQrk-u96KZkzDMcijrnaA)  
  <sub>Yahoo Finance UK, 20 hours ago</sub>  
  Novo Nordisk A/S (NVO) · Novo Nordisk (CPSE:NOVO B) Wins FDA Nod For First Weekly Turner Syndrome Therapy · Novo's Sogroya Gets FDA Label Expansion for...
- [Novo Nordisk A/S (NOVO-B.CO) latest stock news and headlines](https://www.google.com/goto?url=CAESbwHEIkXXFbD5H5lNJoTRcIfsiR4W8esjEh2S92be4FuC6puk2uoXYPrI57P89moDYpFi9rLqflekuqQ8oGL_nWfjYn7BpOncNeXKTbaqmW15vjNhIi53jp5TTUSdsCc3Nr9LgbAv6sEjRAjM8zV76Q&gsessionid=lnX8k8RwTJy87DB0LkywU2O1szs2sHnC5nQrk-u96KZkzDMcijrnaA)  
  <sub>Yahoo Finance Australia, 20 hours ago</sub>  
  Get the latest Novo Nordisk A/S (NOVO-B.CO) stock news and headlines to help you in your trading and investment decisions.
- [Novo Nordisk (NVO) Stock Price Prediction: Resistance is capping a low-volume rebound](https://www.google.com/goto?url=CAESmgEBxCJF1zl0iVoevh1pxQyQ1ju0jS1dj5tlkAZf7zrEX6PCmlNJzpJnYYKbePOcXEFLAPinevawSDek_I37Ti8Dkl-o5cEQqj_ou8EGOYj355kd0aPpPNLb-Y4USF9-7e0KV8pFYmS5DItsfsFLl7-9gYw76JX0vNOJ4ErQg8FKF7ASkDiom2tdmkcUZPTrHN_AxfnqH0Uq53lX&gsessionid=lnX8k8RwTJy87DB0LkywU2O1szs2sHnC5nQrk-u96KZkzDMcijrnaA)  
  <sub>Blockchain News, 4 hours ago</sub>  
  Novo Nordisk (NVO) is trading at $39.37, up 2.07% on the day, but the move is still running beneath the 20-day average and just under near-term resistance.
- [Novo Nordisk AS (NVO) Stock Up 3.5% and Still Undervalued -- GF Score: 81/100](https://www.google.com/goto?url=CAESqAEBxCJF127YLjuo_lGrE00ajnDYtzvlsFZBVV5OrQdCEU4KkcmxM0NT_n5yEvr92lzdmhrB72sf4p5zbKpen5Pl_OZxQS87CIBvbpqmdbB7ZAUoQ7woFclokc-75YpUhNrymRcTWobh8GldEW41CJAKWeWgGlDj5Icb7UdGWH-Q-C3AvFChkDR8W-OuBh84231GCnozat3hy26ddTyIfreEUOhTIZ1VSOE&gsessionid=lnX8k8RwTJy87DB0LkywU2O1szs2sHnC5nQrk-u96KZkzDMcijrnaA)  
  <sub>GuruFocus, 15 hours ago</sub>  
  On November 23, 2026, Novo Nordisk AS (NVO) shares rose 3.5% today, bringing the current price to $39.14. The stock has seen a 52-week range between $35.12...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>Price and chart</b> — score n/a</summary>

```text
Last close 40.40 (bar of 2026-11-24), from 501 daily bars
Trend: vs 20d SMA 40.21 (+0.5%), 50d 39.46 (+2.4%), 200d 42.79 (-5.6%); 50d below 200d
Momentum: RSI(14) 52.0 | MACD -0.090 vs signal 0.059 (histogram -0.149)
Returns: 1d +3.2% | 5d -0.7% | 1m +3.2% | 3m -14.4%
52-week range: 35.29 - 63.98 (now 17.8% of the way up)
Volatility: ATR(14) 1.16 (2.9% of price) | annualised 20d 39.8%
Volume: 0.09x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score n/a</summary>

```text
Sector: Healthcare / Drug Manufacturers - General | market cap 178.03B
Valuation: trailing P/E 10.20 | forward P/E 11.50 | P/B 5.44 | PEG 3.96
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
Consensus: hold (mean 2.85 on a 1=strong buy to 5=strong sell scale, 12 analysts)
Ratings: 0 strong buy, 2 buy, 10 hold, 1 sell, 0 strong sell
Price target: mean 45.73 (+13.2% vs last close), range 39.40 - 64.02
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

- [PG Jumps 17.4% in Three Months as Investors Weigh What Comes Next](https://qz.com/pg-jumps-17-4-in-three-months-as-investors-weigh-what-comes-next)  
  <sub>qz.com, 5 minutes ago</sub>  
  The Procter & Gamble $PG Company PG shares have gained 17.4% over the past three months, while the Zacks Consumer Products - Staples sub-industry declined...
- [Procter & Gamble (PG) Stock Could Be 19% Undervalued As Automation Cuts Loom](https://simplywall.st/stocks/us/household/nyse-pg/procter-gamble/news/procter-gamble-pg-stock-could-be-19-undervalued-as-automatio)  
  <sub>Simply Wall St, 11 hours ago</sub>  
  Procter & Gamble has rewarded long term shareholders over the past five years, and with the stock recently closing at US$169.60, the real question is...
- [A $1 Million Retirement Portfolio Could Generate $25,000 a Year Without Selling Shares](https://www.google.com/goto?url=CAESvAEBxCJF1wYTN9FjYwWQ_-LgsRRS_nlstHGFDHceo399vtto__rj8UcZLH3bPXpe4FasC93kCOSNMXMelI65KomujKkSAJlIuhAIXsc7U9QWWcs-K801bwByO7_SCZmyGcy_L-oWega7Nr8VUCMS7ayERNpv1ZgqQ61ARrM-tyDh2_Uf81ZiVFP2MZnWURTzg1jU7Qpe3Itfx154HvB2DctjaI0Q0K8XLseSIrmGFBLwI9aRd6BuSHS3jTdeyQ&gsessionid=JpMXxPntg0O_db9kGZ2565Wx6QK1UInySSRPhMjD9eScj9_i_UfK4w)  
  <sub>24/7 Wall St., 2 hours ago</sub>  
  Retirement reframes the question a saver asks. During your working years, the question is how big the nest egg is. Once the last paycheck arrives,...
- [Key facts: P&G to Cut 20%-30% of Supply Jobs; $1.4B Costs; Targets Up](https://www.google.com/goto?url=CAESugEBxCJF1z3uq3ugl6v7R_KvxipKzJIx1tKZG9eH-NG-h3pGzxvTFTZU7PuNsF4k-7K3LG9D2PwyvRV5SP8WAbYhSX79lnUd9ydnNQAxQLL20pj06gN-eN2FEcrufXvufqxnhAVh0Ets75C884kS8VRGT1_pBRxD6BxqNoBh_Oa0ljnpus1zFvNuxuEpvG7tO_0SaJOfpekK7yDN4-4us0tmYy55mQS0tduXDrcSmiQI0YvaD32yU4lCQqI&gsessionid=JpMXxPntg0O_db9kGZ2565Wx6QK1UInySSRPhMjD9eScj9_i_UfK4w)  
  <sub>TradingView, 7 hours ago</sub>  
  Procter & Gamble (PG) plans to cut manufacturing and logistics jobs, including contractor roles, by 20% to 30% by the end of 2030, Chief Product Supply...
- [Who Pays P&G? The American Shopper In Four Lines](https://www.google.com/goto?url=CAESpwEBxCJF1xmWCfMMWQ1Ws9BNzX9i-JE_XPoPwmBYtyHP9eRUmRNnUq7AhbJulALkAs1rr8xoY4cpksG7qa1jdi-rWiXj0uOT6hlUBMeeHbNoBrE9GyMcHn-mddYmNoI_CT9BfH8F7fn2j1zEfsuyIYaQ65LEv8uocgqnZYVrYU9EOTnXBUrsHuCdRTfWAHjg3vFeYLhxggrQik3Ixv69aXiS0XaE0IXToQ&gsessionid=JpMXxPntg0O_db9kGZ2565Wx6QK1UInySSRPhMjD9eScj9_i_UfK4w)  
  <sub>Trefis, 3 hours ago</sub>  
  Today's big story: Nvidia Added $954 Billion In A Day. Is Jensen Huang Too Big To Fire? Nvidia is paid by cloud companies such as Google.
- [Procter & Gamble Company (The) $PG Stock Acquired by State Board of Administration of Florida Retirement System](https://www.google.com/goto?url=CAES5QEBxCJF122aujHHnwPpvE3AS9d2Z4XlI2v6MBQmGFZOCDHhnmbpdCWS2p3alKQz3pVrTWHUxvClFT_yOVaAV_sy9AylomVkLzLRbkjonhhfIWNgY4zjo5kZZgb77Jf40KvjUbpBWOMauDLkelhewS1KT02OiryH6_7TuePV5i4E7cXHuVs4_x-o7Py1rVBGgp2iLOW-wk4a5C54dI5IkS_WK2__7Ox4EqCvQ0ito2Et6vpZtYNQbm96ApLRf-8M4cmctj3Ng8s0200GLDHbVONrIVjTbn13O-nROa9R7MqjYjnnZqu1&gsessionid=JpMXxPntg0O_db9kGZ2565Wx6QK1UInySSRPhMjD9eScj9_i_UfK4w)  
  <sub>MarketBeat, 3 hours ago</sub>  
  State Board of Administration of Florida Retirement System increased its position in shares of Procter & Gamble Company (The) (NYSE:PG - Free Report) by...
- [PG&E Corporation (PCG) Stock Price, News, Quote & History](https://www.google.com/goto?url=CAESZAHEIkXXI4GF5DoByIbEXbOcPGsiSYJSXiJMVKcbzSo9xFK0F7S9-R9PKBSBhn_X-fKLhaGcMLmitPEVYbq8kJZk3ONM427-NbcJVOwEcQdQcF3rjOUWVQdJnGRLaCiD5tMmdGI&gsessionid=JpMXxPntg0O_db9kGZ2565Wx6QK1UInySSRPhMjD9eScj9_i_UfK4w)  
  <sub>Yahoo! Finance Canada, 21 hours ago</sub>  
  Find the latest PG&E Corporation (PCG) stock quote, history, news and other vital information to help you with your stock trading and investing.
- [PG vs. CL: value, quality, and pair-trade setup compared](https://www.google.com/goto?url=CAESrgEBxCJF10PJC3cPsEhK5FHYEPURunEOyhyLjIpkF-VHq-qkkllNq5-ACJ79-OphTvuTFyWdmau8IFIrjgnlkndyH0U-lN0YfEHBNhWrsHUz8t0JX_VbhyYtUcGEkabFoW6xdVX9Eg7CPQVkNEGpfMDfZ9Cy6VFv-HufECBUBnJoFJSqTNt5sbcXD3sHlK7nBzkAxYUjNxQIMoSF2yaXcLbjb6Hr8Cr556nDRNXRNGg&gsessionid=JpMXxPntg0O_db9kGZ2565Wx6QK1UInySSRPhMjD9eScj9_i_UfK4w)  
  <sub>Investing.com, 18 hours ago</sub>  
  Investing.com -- Neither stock is cheap, and the two come out roughly even on value. Both trade above fair value estimates. Colgate-Palmolive (CL) looks...
- [How Many Shares of Colgate-Palmolive, Clorox or Procter & Gamble Pay $1,000 a Month in Dividends?](https://www.google.com/goto?url=CAES5AEBxCJF16aDvHMSjOsxVRaRCehYK81-VXYcNhEBNOZ-K3fQhvfE_RjO8OVPfQJHw-o1lYKqertJwvU7BCRfwqoZ8K23ucnygJ9GqM4mFlDTutSp-pkRf5qPsLPPhaLw-NOa-R8uZtXVw6AALU5OpNDzxVZrWWeBtmr9B6_G6MP5lyKir9Awreex6tyo_rWT_yEZiMpn_2cFc-tMHqp_CDvFRuSTEej_7NlpZPOh315bgy9NFpmqN8Dz8F-5UEHaftyudm0CstVxxULgef3Zi5hkR77U5lBUSWcwiYnXL-txla0k0es&gsessionid=JpMXxPntg0O_db9kGZ2565Wx6QK1UInySSRPhMjD9eScj9_i_UfK4w)  
  <sub>TIKR.com, 3 hours ago</sub>  
  At today's prices, $1,000 a month in dividends takes about 5,661 shares of Colgate-Palmolive, 2,400 shares of Clorox or 2,759 shares of Procter & Gamble.
- [Tradable Rally… Or Dead-Cat Bounce?](https://www.google.com/goto?url=CAESewHEIkXXZ2-SsNPfgRQhTtb1XK3p-K9O9e4VC1gL95tE9NbBLkNj0shY03eNVEOnj7_AhH4qfXWOZk-F2Sux1-lRZZ7egiEHqULvtGdi3rpQ-mgDsnYz5bE-dB33yTbw1DZAWFr1v6l0rCit13i2QaQmW3e53pIVIK-rAg&gsessionid=JpMXxPntg0O_db9kGZ2565Wx6QK1UInySSRPhMjD9eScj9_i_UfK4w)  
  <sub>Money & Markets, 14 hours ago</sub>  
  Is it safe to jump back in the pool? Or is the Nvidia drama as a sign that all is not well and the powers that be are scrambling...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>Price and chart</b> — score n/a</summary>

```text
Last close 171.63 (bar of 2026-11-24), from 501 daily bars
Trend: vs 20d SMA 167.09 (+2.7%), 50d 157.81 (+8.8%), 200d 150.38 (+14.1%); 50d above 200d
Momentum: RSI(14) 64.6 | MACD 3.639 vs signal 3.955 (histogram -0.315)
Returns: 1d +1.2% | 5d -0.1% | 1m +7.3% | 3m +18.4%
52-week range: 138.04 - 173.02 (now 96.0% of the way up)
Volatility: ATR(14) 3.14 (1.8% of price) | annualised 20d 19.2%
Volume: 0.09x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score n/a</summary>

```text
Sector: Consumer Defensive / Household & Personal Products | market cap 397.80B
Valuation: trailing P/E 25.85 | forward P/E 23.11 | P/B 7.32 | PEG 4.35
Profitability: profit margin 18.2% | operating margin 24.9% | ROE 29.6%
Growth (YoY): revenue +4.0% | earnings +0.8%
Balance sheet: debt/equity 70.3% | free cash flow 12.65B
Risk: beta 0.36 | short interest 1.0% of float
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
Price target: mean 176.35 (+2.7% vs last close), range 151.00 - 192.00
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

- [Royal Bank of Canada (RY) Stock Price, News, Quote & History](https://ca.finance.yahoo.com/quote/RY/)  
  <sub>Yahoo! Finance Canada, 17 hours ago</sub>  
  3,172.87% · Previous Close 183.45 · Open 187.47 · Bid -- · Ask -- · Day's Range 186.46 - 189.69 · 52 Week Range 149.13 - 218.57 · Volume 1,841,820 · Avg. Volume...
- [Royal Bank of Canada stock rises as price advances toward C$276.72 resistance](https://tradersunion.com/news/stocks/show/4392377-royal-bank-of-canada-up/)  
  <sub>Traders Union, 40 minutes ago</sub>  
  Royal Bank of Canada (RY) stock is trading at C$270.29, marking a daily gain of 2.67%. The price sits above its key short- and long-term moving averages but...
- [RY: SEC Form FWP filed by Royal Bank Of Canada](https://www.google.com/goto?url=CAESjgEBxCJF1y-llBmtOP0ijav6D8jSYqIeRp0-fEP9aTK4esZpN8cnmDwVIQfVFWuwug5zXA92qJufaXgSS0Ti8vWNNqtkMgGXIC3sO83qBsCl50SX-rA3iQjPpOOIoknlEVPv6FrajbwX1N-tMHVBqLWjIpHYrTmTjnC6RwcBi_L1zVxSG1IP7yir-29LddpH&gsessionid=NECGRAlSGoufl7SRH70vEKDR0_jfcib2cem4bOP-pkQfMq9QPivEsQ)  
  <sub>Quantisnow, 14 hours ago</sub>  
  Royal Bank of Canada is offering notes due November 29, 2028 linked to NVIDIA common stock. If NVIDIA finishes above its starting value, holders get 200% of...
- [TSE:RY Stock Earnings Estimates Boosted by Erste Group Bank](https://www.google.com/goto?url=CAESuAEBxCJF13Efks19rHmTIhxf2JT3tR8rvFwY5SZ1lP_SX_lFyg2kR0v7SIyD9SkrDrwSj_jn8lQ8zSowu-neN29nXj3MRt01qJGz8NuZ565xMGET-heP4oC6-Nw-8T9kyP9qY04Kuakiz2wyoyzb8LlvQES6ZubSIai94O9rVeFv08fTK_wVDC90hG14iHvWLv7Ta7FdKgeOrEK1CnBJJ4zVpwwfjM4hlCtpMW5eJX2A5OV4oNEUHIsb&gsessionid=NECGRAlSGoufl7SRH70vEKDR0_jfcib2cem4bOP-pkQfMq9QPivEsQ)  
  <sub>MarketBeat, 2 hours ago</sub>  
  Royal Bank of Canada (TSE:RY - Free Report) (NYSE:RY) - Equities researchers at Erste Group Bank lifted their FY2026 earnings per share estimates for shares...
- [Royal Bank of Canada Stock (RY) Moved Up by 3.28% on Nov 23: What Signal Does It Send?](https://www.google.com/goto?url=CAESjgEBxCJF1znPhWLOom9vP1wwnv6OqWSUtnfnQDJPS9nGdx7GLOer1ByB_yI66w5P-6L3vD7nHfGU4LHTL08XXMz1fv3VpmTwlmFUejNTWdPEHZiaYanC4ZQ3FubScrYeWhD5o0oDmN317i6DBE_OV2GZ3CNuwVyo6OvH3plbEvs1tVJc7yuP8qAMkKtQHCNI&gsessionid=NECGRAlSGoufl7SRH70vEKDR0_jfcib2cem4bOP-pkQfMq9QPivEsQ)  
  <sub>TradingKey, 19 hours ago</sub>  
  Royal Bank of Canada advanced due to institutional optimism and stabilizing interest rates.The lender benefits from healthier net interest margins and...
- [Why Did Royal Bank of Canada (TSX:RY) Surge 2.752% on November 23, 2026?](https://www.google.com/goto?url=CAESoAEBxCJF12MzeE8ekZHJVLviSljvfjGCV8cqXHeOqWMYdjnEz9UJAyWwJNsRYzrzc700-JcltH4ADQh4PtfjkByVJixBVZTdxlJGk5gX6c5WXeshXmze9_SsppZmp_KGDHesZt8L3mfkhQT9a9D4GYZ3buk1gYpbmUIm7mD9nbjLmHskmIajPK2nPSXxfZhXKvhvZ38xuJ2dxHoqXH1UibMg&gsessionid=NECGRAlSGoufl7SRH70vEKDR0_jfcib2cem4bOP-pkQfMq9QPivEsQ)  
  <sub>kalkine.ca, 3 hours ago</sub>  
  You are reading a free article with opinions that may differ from the recommendation given by Kalkine in its paid research reports.
- [The Toronto-Dominion Bank (TD.TO) Stock Price, News, Quote & History](https://www.google.com/goto?url=CAESZgHEIkXXK79_8OLcWwy9M38YirKf0m4L3lHZw4wwXmDTONZJ_q0bEXYbqID72nyqPLJbOW20EJxF3VVOkq90zQ6naJ8b8sczmMHNBuFpVaLqXqpna2tAeZW6t3UzL2vQmXsCP_oBCw&gsessionid=NECGRAlSGoufl7SRH70vEKDR0_jfcib2cem4bOP-pkQfMq9QPivEsQ)  
  <sub>Yahoo! Finance Canada, 17 hours ago</sub>  
  Find the latest The Toronto-Dominion Bank (TD.TO) stock quote, history, news and other vital information to help you with your stock trading and investing.
- [How Is Royal Bank (TSX:RY) Integrating Banking and Wealth Services?](https://www.google.com/goto?url=CAESqAEBxCJF13q_3sNqt2cWxUEyatwGkpHsf8qiAjNUxmSxNxsxtapg6G5jSI2N9SZARRxgR8C1n-bsfxOJxL3lz-WqSFjAj53pqi7atxUfei3DGZg_wP7V5G3JZD6zH5IHWUyzGJniaOVOYR2WtXbUCyJu6e8YTy-hq9GMUFsDwCqB-d4Z3J1cmIvPN0svUn_SOFxpQw0PJEesW2CA07p-YAEESGZkR9IEXa8&gsessionid=NECGRAlSGoufl7SRH70vEKDR0_jfcib2cem4bOP-pkQfMq9QPivEsQ)  
  <sub>Kalkine Media, 21 hours ago</sub>  
  Royal Bank of Canada's wealth arm won Best Private Bank in Canada and a global sustainable investing title at the PWM Global Private Banking Awards.
- [Royal Bank Of Canada (RY) Stock Forecasts](https://www.google.com/goto?url=CAESlAEBxCJF19tNo-H9M-aRVB4F4fPINyiE7I6OoJQD_TpLl8EA-09gefPehN8_jgKREoN3x4EQrleomlV1ePT-zE-MGvy4Si3NVwkURGN1pF1OM4X4SAnLTM-7nS2c1Ifw9u2pCsn_JPxGBAJTx5riU8gz9npdgi68KcCzedgmhXRAFyQZxCn9j7GZuFBIIQoDYVU2CvGw&gsessionid=NECGRAlSGoufl7SRH70vEKDR0_jfcib2cem4bOP-pkQfMq9QPivEsQ)  
  <sub>Yahoo! Finance Canada, 22 hours ago</sub>  
  At Yahoo Finance, you get free stock quotes, up-to-date news, portfolio management resources, international market data, social interaction and mortgage...
- [The Toronto-Dominion Bank (TD) Stock Price, News, Quote & History](https://www.google.com/goto?url=CAESYwHEIkXXLtaK9Qi1fv-YByvIkuvriO8hVVFiKmQRpuB_R_EmalyYhEpXo8B4vHVCTfspPhvs7YPNSBNp9GeKW_1gBTsEcljRYTIv89_ntZe8SHrb3oiCcDKETL3lmvj3J_0EZQ&gsessionid=NECGRAlSGoufl7SRH70vEKDR0_jfcib2cem4bOP-pkQfMq9QPivEsQ)  
  <sub>Yahoo! Finance Canada, 17 hours ago</sub>  
  Find the latest The Toronto-Dominion Bank (TD) stock quote, history, news and other vital information to help you with your stock trading and investing.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>Price and chart</b> — score n/a</summary>

```text
Last close 187.68 (bar of 2026-11-24), from 501 daily bars
Trend: vs 20d SMA 199.25 (-5.8%), 50d 198.80 (-5.6%), 200d 191.71 (-2.1%); 50d above 200d
Momentum: RSI(14) 35.6 | MACD -3.523 vs signal -1.594 (histogram -1.928)
Returns: 1d -0.3% | 5d -4.5% | 1m -7.3% | 3m -9.4%
52-week range: 149.71 - 217.87 (now 55.7% of the way up)
Volatility: ATR(14) 3.76 (2.0% of price) | annualised 20d 26.3%
Volume: 0.02x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score n/a</summary>

```text
Sector: Financial Services / Banks - Diversified | market cap 259.83B
Valuation: trailing P/E 16.41 | forward P/E 14.73 | P/B 2.72 | PEG 1.76
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
Price target: mean 208.47 (+11.1% vs last close), range 181.95 - 229.29
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

### Toyota (TM) · Company — no answer, no confidence given

<details><summary><b>News</b> — score n/a</summary>

- [Trading Systems Reacting to (TM) Volatility](https://news.stocktradersdaily.com/news_release/17/Trading_Systems_Reacting_to_TM_Volatility_112326080601_1795482361.html)  
  <sub>Stock Traders Daily, 19 hours ago</sub>  
  Price-action only: Toyota Motor Corporation (TM) movements set the tone for institutional models. Trading Systems Reacting to (TM) Volatility.
- [7-Eleven Canada gets a sports drink flavor no other retailer can sell.](https://www.stocktitan.net/news/CZZL/cizzle-brands-corporation-announces-launch-of-cwench-hydration-tm-at-vnoi7tce87w3.html)  
  <sub>Stock Titan, 2 hours ago</sub>  
  Yukon Yellow has zero sugar, five electrolytes and 10 calories. It joins three core CWENCH flavours in participating stores in 500 mL packs.
- [First Phosphate and Zeo Energy Interviews to Air Nationally on the RedChip Small Stocks, Big Money(TM) Show on Bloomberg TV](https://www.google.com/goto?url=CAES6AEBxCJF176ATkTS1VdlMRxkZPg8Hb_qWtxF0HibDV8v00W58qv9q8SPN6qlCNrGJiucqHvDtfX7hYoTTGbOcWPVfeBYtUeSWoYvB9dEYne8YmkIeJ3oQCz0BMMbod03npsdM97QuG7I4shhB0K-ICCX3ccq7YgY6SZ4ER5Yw2JNA_B1XM1o9kandfE9x1ejUcahtUq53FOzPoIuwepUhJfjVZMUaQ380wN-va2ZnLbtmYrz2qtwEYmSa9nZ4Yfl3Ge9ucHBuje0A8tnvd-PpzLhUNKQVa1dYMPPVSgwF3WKttH7nK7w4uvA&gsessionid=YdaIqF6hagPo3N78t6AL-fDqJ9-8rc0m7da3bUTMCtowROhkE8pyWA)  
  <sub>USA Today, 23 hours ago</sub>  
  ORLANDO, FL / ACCESS Newswire / November 20, 2026 / RedChip Companies will air interviews with First Phosphate Corp.
- [(HBIL) Equity Market Report (HBIL:CA)](https://www.google.com/goto?url=CAESjgEBxCJF1w8ktlN_e__ekyB956lIsRWBANyxv_xIKFrQieIy83c7cBIQOTQR0E61QCS9ZqGJglcPxk6SzilifXAuUzI-pvTfWj3ZWMtYw4Inpen0fqj1lJGBgjjKsmt3cMHUnpHfLZ75QMtLml-uHZx-utBhvfaDYk2XfxEq_08NU4-GXDVHz73g65kEzUGk&gsessionid=YdaIqF6hagPo3N78t6AL-fDqJ9-8rc0m7da3bUTMCtowROhkE8pyWA)  
  <sub>Stock Traders Daily, 4 hours ago</sub>  
  Equity Market Report for Hamilton U.S. T-Bill YIELD MAXIMIZER TM ETF (HBIL) with Buy and Sell Signals.
- [Top Toy Stocks To Consider - November 23rd](https://www.google.com/goto?url=CAESngEBxCJF18xiPvT1FmYGbkWU8VsqLdOaWeZVmka-HalSFeOzCAQwDVSn_Mz_hh4bwzQUU5KDfONb4uqX-LnNvC745DZecM1lbIX_epUmrHU_tfT2QuXKh__WyUj5Ao2hd5F3JFfiA-mH6NGc2ADqBpK4TH4XRsLIuVCV2saK4lB88BdofprNChNEMzWeYEWrtunEin0ktFdzkKZkEFcuuA&gsessionid=YdaIqF6hagPo3N78t6AL-fDqJ9-8rc0m7da3bUTMCtowROhkE8pyWA)  
  <sub>MarketBeat, 19 hours ago</sub>  
  Hasbro, Mattel, Toyota Motor, MINISO Group, JAKKS Pacific, TOYO, and Tron are the seven Toy stocks to watch today, according to MarketBeat's stock screener...
- [For a third consecutive year, Gartner names TransUnion a leader in measuring marketing results](https://www.google.com/goto?url=CAEStQEBxCJF12Pryu5yriNqK38iX9bvQRGAFwtp1EKYo4AYvrvlvt88s_48eDNUwdCWdcxtGp3lQTq4RUzyAP6MHdHgSJ-ALvh7EzvvPgJ95Lylh0cL-db3wPVAjNviUSvjyqQcUNsUqp-s8FiV2S7iAztRq-WrETDzN0oEM3CUnPMwTIDL5X2loyX5nbI2W-P6kUOjcqul-RyKkYKHrerMNGqdx9rXqj98tNyvfwl2WFogL_ESrv8x&gsessionid=YdaIqF6hagPo3N78t6AL-fDqJ9-8rc0m7da3bUTMCtowROhkE8pyWA)  
  <sub>Stock Titan, 2 hours ago</sub>  
  Its marketing mix modeling solution can be fully managed or self-served; TransUnion says AI investments have made data processing faster and less manual.
- [Estimated phosphate resources at First Phosphate are up 378%. Mining approvals are planned for Q1 2028.](https://www.google.com/goto?url=CAEStAEBxCJF16C5H7rS5iK5Svehni0KnCdMxFlOxHmb5uTuY6hiwmxVUqKQZbYxUt6musf6BPmRVS6kxF8ciVEnO4o-tPZptUGSTao6R7wWF-tbvyukg-N7Gcz2-uevgoXRjbZzieg-eCdh8tl9kAe6QJKzB-MmG6sisa3OTYeW-vyBqqWaWseCNZYk6KPe1jgUIz5RMXtCIAcQ1LSLn9T5B3miOfMpWyrVGi6Gdmj0OzRovXPj-k0&gsessionid=YdaIqF6hagPo3N78t6AL-fDqJ9-8rc0m7da3bUTMCtowROhkE8pyWA)  
  <sub>Stock Titan, 2 hours ago</sub>  
  UK Export Finance's letter of interest covers up to CAD 220M in loan support; SERV guarantees USD 212.5M toward project costs. Feasibility study is due Q1...
- [When (HBIL.U) Moves Investors should Listen (HBIL.U:CA)](https://www.google.com/goto?url=CAESnQEBxCJF1-mc1lLPUPOvm4XWGqZPu3ZIKS-WXGoCraKWT_AqH_J5PbqxGyyjx0PGgYtc2JE3ekQL9Q_gXFwkZYx4Z8cm07vzHOPnplZQiEbp4Y_R8JPzNiicXrjHe63_guZNnvkgihCIWtDn5mUA41YTbYPVhluwtDdLOJTHsfpJxgODR--0RMNlT7FVCyNsqLF6qJEdi2OzaPP6kKf9&gsessionid=YdaIqF6hagPo3N78t6AL-fDqJ9-8rc0m7da3bUTMCtowROhkE8pyWA)  
  <sub>Stock Traders Daily, 5 hours ago</sub>  
  When Hamilton U.S. T-Bill YIELD MAXIMIZER TM ETF HBIL.U Moves Investors should Listen.
- [Several December talks in Florence will cover an eye treatment’s durability and retinal-fluid control.](https://www.google.com/goto?url=CAESrQEBxCJF19wuUZ2KX890wJ9lPbjd9MABiaYWCGFga8GbhAO5VoGdQ2m-kmQGMKX-2QemzWrY_fXizZUcHhnWDzYTSChAVAv6x3qIpeQQ2pmFDTO67CcGACCZWGq0r06jTzuMK89vOxS0xtSpuOtMPXJnuVf_8I4VWDNOTxXd9dim4pdtxgmOR_7vn-a7rpN7wQkF11JQqo_JSnF09llA4DIBag8oxUjjpBF5BxOA6Q&gsessionid=YdaIqF6hagPo3N78t6AL-fDqJ9-8rc0m7da3bUTMCtowROhkE8pyWA)  
  <sub>Stock Titan, 3 hours ago</sub>  
  Talks include OTX-TKI updates for diabetic retinopathy and AMD at FLORetina in Florence; presentation titles and exact times may change.
- [Rise Nano Optics Ltd. (EYE.CN) Stock Price, News, Quote & History](https://www.google.com/goto?url=CAESZQHEIkXXlMLaryodw7c2pQE0k5iZGWU2L96fw4nrczQfZafmdaJBlfgFwjTSHfDr_Z4CmFB2Kt0HR6EoHao9jpUzFDfADWea9VXuY9wogKqNMB57HMvsJRwwX2MZOlaSRcjzO-k2&gsessionid=YdaIqF6hagPo3N78t6AL-fDqJ9-8rc0m7da3bUTMCtowROhkE8pyWA)  
  <sub>Yahoo! Finance Canada, 3 hours ago</sub>  
  Find the latest Rise Nano Optics Ltd. (EYE.CN) stock quote, history, news and other vital information to help you with your stock trading and investing.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>Price and chart</b> — score n/a</summary>

```text
Last close 208.60 (bar of 2026-11-24), from 501 daily bars
Trend: vs 20d SMA 207.73 (+0.4%), 50d 197.08 (+5.8%), 200d 197.00 (+5.9%); 50d above 200d
Momentum: RSI(14) 54.2 | MACD 4.039 vs signal 4.826 (histogram -0.787)
Returns: 1d -1.7% | 5d -2.1% | 1m +5.5% | 3m +8.7%
52-week range: 166.50 - 248.29 (now 51.5% of the way up)
Volatility: ATR(14) 4.46 (2.1% of price) | annualised 20d 40.5%
Volume: 0.20x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score n/a</summary>

```text
Sector: Consumer Cyclical / Auto Manufacturers | market cap 244.82B
Valuation: trailing P/E 9.51 | forward P/E 13.22 | P/B 16.60 | PEG 19.39
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
Price target: mean 238.08 (+14.1% vs last close), range 230.00 - 253.00
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

- [Your Exxon Dividend Needs Only About $59 Oil](https://www.trefis.com/stock/xom/articles/628301/your-exxon-dividend-needs-only-about-59-oil/2026-11-24)  
  <sub>Trefis, 5 hours ago</sub>  
  Oil has fallen, and oil stocks have fallen with it. WTI crude, the main U.S. oil price, fell 17.3% from $108.21 on Oct 16 to $89.53 on Nov 17. Exxon Mobil...
- [XOM Dec 2026 180.000 put (XOM261224P00180000) interactive stock chart](https://uk.finance.yahoo.com/quote/XOM261224P00180000/chart/)  
  <sub>Yahoo Finance UK, 16 hours ago</sub>  
  Interactive chart for XOM Dec 2026 180.000 put (XOM261224P00180000) – analyse all of the data with a huge range of indicators.
- [Fund Update: New $183.0M $XOM stock position opened by CWM, LLC](https://www.google.com/goto?url=CAESpQEBxCJF1w3h8dAK5Qz4wHYkd-r81ERRnCq09TkbWh40_sbBnv60amVjOrIs68IlO49L7z-QTN_lzVHekfEPnFv6CXNNwDPJ4gaayMvWEj7jeL7RtsDXgfYJLEIe_Z4deQe5TRsSG1T_UCJamllav-YzE7xafOEM6TDcRHU3XbdoJevN1YMFChpiI3GBLkY8INIYzHLL8-pGWZGMXu8uuRI9B6CRdJ0&gsessionid=mG9Lm1c30cVl5WYsLq65qrQFE1vNXz6zy88-lD0hf3gNKVgxM3O15Q)  
  <sub>Quiver Quantitative, 18 hours ago</sub>  
  CWM, LLC has opened a new $183.0M position in $XOM, per a new SEC 13F filing. This disclosure reflec.
- [ExxonMobil: Announces Pricing Terms, Expiration and Results of Cash...](https://www.google.com/goto?url=CAESsAEBxCJF1zXSE7IAZgeaxVSz1NiL6HTkQjJEe5cDMubFDwdZJ3h_LuVFOkVv2_NS0vw1NMpC0rkqjDziuj0MLZ7TFNmgkWJhCJzMPgBu7H_lKaqHYYTVvCwjT08GCW3qFhj54iYcqJHakgTCTLR95g790vzTuOE8YxJrFGl_POkE4hfxx__SZ53L7G5jPx8IJOReOycFmChXVcPSLhKg6dubtig0WV2rPcykH193Gzi9Uw&gsessionid=mG9Lm1c30cVl5WYsLq65qrQFE1vNXz6zy88-lD0hf3gNKVgxM3O15Q)  
  <sub>Quantisnow, 22 hours ago</sub>  
  ExxonMobil Holdings Corporation ("ExxonMobil") (NYSE: XOM) today announces the pricing terms, expiration and results of previously announced cash tender...
- [ExxonMobil Corporation $XOM Stock Position Increased by Healthcare of Ontario Pension Plan Trust Fund](https://www.google.com/goto?url=CAES3wEBxCJF1wppj6BMWmSkXnrCrlukcp9qNytj8H0Cl51E3hd3fLkq9hasCciJYAOyvlp7QF9ZUokSjo1S8KifcFzyYBLJSDOSb8aw5Ca6-slHhLx68zfKaHBRDa0U1b4AD_7dcgSDC2goXUGiJQYqbV-EF4gJXusglfhOvo-6Z5nT3rwI4uStrME1LIcOj9iKjhzmjg8QLzfE3-RJUVsWr07gbPSs_g_Hq_Cu7GwEYixoWfoLGkSvDEV-zSMGz88tHGpWvj_8ID0IU8RaFQfx-Xy3fWBbQ1vBfNBNdkDNhlf1&gsessionid=mG9Lm1c30cVl5WYsLq65qrQFE1vNXz6zy88-lD0hf3gNKVgxM3O15Q)  
  <sub>MarketBeat, 5 hours ago</sub>  
  Healthcare of Ontario Pension Plan Trust Fund increased its position in ExxonMobil Corporation (NYSE:XOM - Free Report) by 54.8% in the 3rd quarter,...
- [XOM Dec 2026 195.000 call (XOM261204C00195000) interactive stock chart](https://www.google.com/goto?url=CAESeQHEIkXXcfoGMxe6hYfZqoTyD7JAq0-kJb_0Piu0_kzY4pVs_Y-acnzDYSswDE5ZeNwk-Fjv38rQeYLuAgquIPg_wdSGZRFg0wk8u4KcwPDou3W9v4eWlux3vc4tAL6nrg11lFFf5T2Y_BoI_jFF4jQpP_vbqkJRFvM&gsessionid=mG9Lm1c30cVl5WYsLq65qrQFE1vNXz6zy88-lD0hf3gNKVgxM3O15Q)  
  <sub>Yahoo Finance Australia, 15 hours ago</sub>  
  Interactive chart for XOM Dec 2026 195.000 call (XOM261204C00195000) – analyse all of the data with a huge range of indicators.
- [Wall Street Opens Sharply Higher After the S&P 500's Seven-Day Slide](https://www.google.com/goto?url=CAESpAEBxCJF1wmik-HUlo8-L_uh1wzNq-pX8wDQMFywtxuIntIRVgGeeMEvZVKAfwcf9g4doYDmAXJKkWPyvn8cuY83dN7hHWRG1go5prSTYW0KANxpgtrCPZkpZX101nBHytAvgtU-DRU_jMNa38lxtP77UKyht-rQCyEGY-956eF8vgwhSzfdPbowPAxDjUJr8VVoq9fVD0E3dAJsaEJh52FYO5ImVQ&gsessionid=mG9Lm1c30cVl5WYsLq65qrQFE1vNXz6zy88-lD0hf3gNKVgxM3O15Q)  
  <sub>Quantisnow, 22 hours ago</sub>  
  HOUSTON, Nov. 23, 2026 /CNW/ -- Oil Market Daily News Commentary - Wall Street started the Thanksgiving week on a much brighter note. All three major U.S..
- [ExxonMobil vs. Equinor: Which is the Stronger Integrated Player?](https://www.google.com/goto?url=CAESowEBxCJF146dxzJYyGnp5Q3D7TF0GD0Vl_YNE8ETuf99qO_zH4-RFXSpKMpwQv4qfwvnqX3rw4THPJUbqR98OibIJgRFL7N1QW9CwzB3ljEPh01UcJ4yO1mV5-qDACzVso8aERcxZThseG-vYWOTUEp_6v-Sqe9fD6Hwo1y_gdezgQdJGY9HxgkLFjDSGLO2-l-5s8OkmkgCKOxoh5acZ-YS1NCE&gsessionid=mG9Lm1c30cVl5WYsLq65qrQFE1vNXz6zy88-lD0hf3gNKVgxM3O15Q)  
  <sub>Zacks Investment Research, 23 hours ago</sub>  
  EQNR beats XOM in stock gains, dividend yield and valuation. Can strong European gas prices make EQNR the better investment?
- [370,000 Shares of ExxonMobil Corporation $XOM Bought by Caxton Associates LLP](https://www.google.com/goto?url=CAESxgEBxCJF19PAnT4tbkBDT8rHxqgVfq7BJAoKklwNBmAKIUM8NDio1Y4efEPID-ZGDTUGDr4hmq8wqPQd2jWDDzMtxm8RN1o-VGcSkEM9_ZEuBOs7G8jgdrMRy4OhhqdAoC_00FbVpu53yuMLTgTmmLaWU2WJAU3b6FYVDfda2z6yxZP1csYM4g__73zCMBnRRAmudtkWTXodES3OVDRUwfNs9qFn6-uIMmULwXSJiqNPgabKHOYff9i0UCbXRNk-E2d1aVJiDgA&gsessionid=mG9Lm1c30cVl5WYsLq65qrQFE1vNXz6zy88-lD0hf3gNKVgxM3O15Q)  
  <sub>MarketBeat, 5 hours ago</sub>  
  Caxton Associates LLP purchased a new stake in ExxonMobil Corporation (NYSE:XOM - Free Report) during the third quarter, according to the company in its...
- [ExxonMobil's $4B Kizomba Redevelopment: Can It Drive Earnings Growth?](https://www.google.com/goto?url=CAESoAEBxCJF169WoRcurNip6zblANrsU6tyaZSPr6zcNrAM2BJEQkoGY1R9356IRTD0zxPB1sBIfLBApSl-mpYIvCherWAgibRxiSHy94hug-NQMXRU0nFzf8Khexca3yFAgFWRGRBz5ZfSD0o_zZNP3QdamD-ouWah8u7-KufWbR0xVxw6ZjCqSVM7GSZlGOgHfGux-nOSKZqgxEaRsUeEvQK8&gsessionid=mG9Lm1c30cVl5WYsLq65qrQFE1vNXz6zy88-lD0hf3gNKVgxM3O15Q)  
  <sub>Yahoo Finance, 22 hours ago</sub>  
  ExxonMobil Holdings Corporation XOM and its partners are advancing an estimated $4 billion redevelopment of Angola's offshore Kizomba A and B fields...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>Price and chart</b> — score n/a</summary>

```text
Last close 158.79 (bar of 2026-11-24), from 501 daily bars
Trend: vs 20d SMA 168.78 (-5.9%), 50d 168.96 (-6.0%), 200d 156.92 (+1.2%); 50d above 200d
Momentum: RSI(14) 36.7 | MACD -3.636 vs signal -2.133 (histogram -1.503)
Returns: 1d +1.2% | 5d -5.0% | 1m -14.0% | 3m +0.4%
52-week range: 114.51 - 187.25 (now 60.9% of the way up)
Volatility: ATR(14) 4.00 (2.5% of price) | annualised 20d 32.0%
Volume: 0.03x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score n/a</summary>

```text
Sector: Energy / Oil & Gas Integrated | market cap 647.72B
Valuation: trailing P/E 16.34 | forward P/E 12.72 | P/B 2.44 | PEG 1.24
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
Price target: mean 184.18 (+16.0% vs last close), range 160.00 - 213.00
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

### US government bonds, 1-3 years (SHY) · Index fund — BEARISH, confidence 0.40

**Result:** REJECTED · ATR 0.1304 is below 0.20% of price 81.59

**In the model's own words:**

> Positioning crowding suggests a bearish bias for short‑term Treasuries.

**Main reasons it gave:**
- Large speculators net short 28.8% of open interest on 2‑year note, crowding at 92nd percentile
- Positioning change +4.7% net short on the week indicates increasing bearish bets
- Technicals show modest upside vs short‑term SMAs but low volume and no decisive break
- No macro surprise in recent data; yields unchanged and VIX elevated but stable

<details><summary><b>News</b> — score +0.00</summary>

- [Which Crypto Under $5 Could Double First in 2027?](https://247wallst.com/investing/cryptocurrency/2026/11/23/which-crypto-under-5-could-double-first-in-2027/?tpid=1714277&tv=link&tc=in_content)  
  <sub>24/7 Wall St., 17 hours ago</sub>  
  XRP, Dogecoin, Cardano, Stellar, and Hedera all trade under $5. Here's which one could double first in 2027 and what each needs.
- [Tom Lee Says XRP’s Supply Grows 5.4% a Year: Could It Cap XRP’s Price by 2028?](https://247wallst.com/investing/cryptocurrency/2026/11/23/tom-lee-says-xrps-supply-grows-5-4-a-year-could-it-cap-xrps-price-by-2028/)  
  <sub>24/7 Wall St., 20 hours ago</sub>  
  Tom Lee puts XRP's annual supply growth at 5.4%. Here's what 71 billion tokens could mean for XRP's price at $1, $2, and $3.65 by 2028.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.17% (+0.03 on the week) | 5-year 4.71% (-0.19 on the week) | 10-year 4.90% (-0.20 on the week) | 30-year 5.29% (-0.17 on the week)
Yield curve, 10-year minus 3-month: +0.73 points -- upward sloping (normal)
US dollar index: 103.81 (+0.32 on the week)
Volatility (VIX): 29.34 (+3.9 on the week) -- stressed
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.1% (2026-10-01) | jobless claims 203k (2026-11-14)
Policy and expectations: Fed target 4.00% | market expects 2.1% inflation over 10 years
Rate path: 2-year Treasury 4.63% vs Fed target 3.75-4.00% -- the bond market prices about 3 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 81.58 (bar of 2026-11-24), from 501 daily bars
Trend: vs 20d SMA 81.45 (+0.2%), 50d 81.33 (+0.3%), 200d 81.99 (-0.5%); 50d below 200d
Momentum: RSI(14) 58.0 | MACD 0.027 vs signal 0.006 (histogram 0.021)
Returns: 1d +0.0% | 5d +0.3% | 1m +0.1% | 3m -0.6%
52-week range: 81.05 - 83.18 (now 24.9% of the way up)
Volatility: ATR(14) 0.13 (0.2% of price) | annualised 20d 2.4%
Volume: 0.05x the 20-day average
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

<details><summary><b>Buying and selling by company insiders</b> — score -0.40</summary>

_Not available today._

</details>

<details><summary><b>Who is positioned how</b> — score -0.40</summary>

```text
Contract: UST 2Y NOTE - CHICAGO BOARD OF TRADE (positions as of 2026-11-17, published the following Friday)
Large speculators: net short 28.8% of open interest (4,467,824 contracts)
Change on the week: +4.7% of open interest
Crowding: 92% percentile over 52 weeks -- a crowded long by the standards of the past year
Read this as crowding, not as a forecast: an extreme is as often the end of a move as the middle of one.
```

</details>

<details><summary><b>Money going into and out of this fund</b> — score -0.40</summary>

```text
Direction: money coming in (1 month)
Share count change: 1 week: -0.5% (-146.96M) over 7d | 1 month: +4.0% (1.06B) over 32d
Shares outstanding: 336.32M | fund size: 27.44B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### US small companies (IWM) · Index fund — NEUTRAL, confidence 0.10

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> The macro backdrop shows no surprise in rates or data, so there is no clear catalyst. Technicals are bearish (price below 20‑, 50‑ and 200‑day SMAs, RSI 41.9, MACD negative) but the move lacks a decisive break on strong volume. Analyst coverage is thin (1.9% of the fund) yet uniformly bullish with a +16% price target. Positioning indicates a modest net short (9.2%) that has nudged higher, suggesting some bearish sentiment among large speculators. Fund flows are flat, offering no directional bias. With these mixed signals and no material change, the appropriate view is neutral with low conviction.

**Main reasons it gave:**
- Price below 20‑, 50‑ and 200‑day SMAs (trend down)
- RSI 41.9 and MACD negative (bearish momentum)
- Large speculators net short 9.2% and increased +0.9% week‑over‑week
- Macro data stable: yields unchanged, VIX up but no surprise
- Analyst coverage thin (1.9% weight) but 100% buy with +16% target

<details><summary><b>News</b> — score -0.10</summary>

- [November 24: A date bulls have circled on the calendar](https://www.tradingview.com/news/seekingalpha:23ae903b4094b:0-november-24-a-date-bulls-have-circled-on-the-calendar/)  
  <sub>TradingView, 5 hours ago</sub>  
  Wall Street may have a date worth looking forward to. November 24 has historically delivered gains for U.S. stocks, with the S&P 500 finishing higher in 13...
- [How to Invest in the MSCI India ETF (INDA)](https://www.fool.com/investing/how-to-invest/etfs/how-to-invest-in-inda-etf/)  
  <sub>The Motley Fool, 16 hours ago</sub>  
  The iShares MSCI India ETF (INDA) provides U.S. dollar denominated exposure some of the best performing emerging market stocks.
- [November 24: A date bulls have circled on the calendar (SPY:NYSEARCA)](https://www.google.com/goto?url=CAESmAEBxCJF16BZW1zQuQ36GCDNeRhcUJJcgPX_ERphie0GyvZlc7mowDziZ1Zhj9K_6MKEpbqZ4sLLkb8QCWPyBlWGL5ZiTyUSjFijF7zT9bTkhS3V6Ajgu1IHXfG3__XjiIPKPphGQGLfz3XTLlx3Tj-XZgjAVU_orh1aSy6OPV6SQriBeXKls08WqUKK4vnGHWLJcrIx1hl7_w&gsessionid=dpL_fKbTjJRSwiSEuLMJjSajcB88lRLKlKBlant1H9VOjoWfR_F0Bw)  
  <sub>Seeking Alpha, 5 hours ago</sub>  
  Bluekurtic says the S&P 500 rose on November 24 in 13 of 14 sessions since 2000, supporting its base case for a tactical bounce this week.
- [Top Tokenized ETFs by Market Cap](https://www.google.com/goto?url=CAESXgHEIkXXSJxXR-PAYjiXg7KihCBywUdJ_BDK7sK1o_fGJBjU5QFhXTqChAutfZcJvM-xLtep54pg6WfTgnxW2mXHCakclM5dm8sLqpVgv-g0fP_pNfPQAxjFFcnI960&gsessionid=dpL_fKbTjJRSwiSEuLMJjSajcB88lRLKlKBlant1H9VOjoWfR_F0Bw)  
  <sub>Coingecko, 1 hour ago</sub>  
  Discover the top ETFs (exchange-traded funds) by tokenized market cap. Track ETF prices alongside their tokenized prices, market cap, and volume on...
- [How to Buy JPMorgan Nasdaq Equity Premium Income ETF (JEPQ)](https://www.google.com/goto?url=CAESiQEBxCJF17S1iHfvcGqwFXF6tjwF9byNTsW_XJHD2HqfFuYZyKtz0xKMYZTGrqunPeHb2bqOjpnvlr_Ju15-zD_m4KswCmqlRGOU6vSQBZOQAmaIGBJzkUv58rVF4KWJT0Wi2BKlFbGddE4cjoFhVmd_pPUemtvRLv0ke5V-Ppw4DYxaawUxndYMCA&gsessionid=dpL_fKbTjJRSwiSEuLMJjSajcB88lRLKlKBlant1H9VOjoWfR_F0Bw)  
  <sub>The Motley Fool, 19 hours ago</sub>  
  The JPMorgan Nasdaq Equity Premium Income ETF (JEPQ) can help you own tech stocks but with the benefit of higher monthly income.
- [The Selloff Has Spread Beyond AI. I'm Waiting (NYSEARCA:SPY)](https://www.google.com/goto?url=CAESkQEBxCJF1x_AS6S5GgCSGC_cgoLsMCCCG85z4ph9Y7K8psXmepxAdFlmLvYujno1PaQaIBgjCHk3-pmmR1xJ4oEr-bP_2B6A_cxZoncWrS42HN8CuNeB3m2detcre7qgKTXWfg_VTQoHbMSKKPLRpZq0qswZwPqD6-PZnC7v0nMjutvEWTg7OohWyFvBl4H2Uwr6&gsessionid=dpL_fKbTjJRSwiSEuLMJjSajcB88lRLKlKBlant1H9VOjoWfR_F0Bw)  
  <sub>Seeking Alpha, 24 hours ago</sub>  
  I rate the S&P 500 Hold as the AI selloff broadens into a growth and monetary policy scare.
- [iShares Russell 2000 ETF (IWM) Price Prediction: Small-cap rebound stalls under heavy overhead resistance](https://www.google.com/goto?url=CAESnAEBxCJF11GZBzEdMZwaS9LlGy10KyPUlEFEGHRwn5OpL6tJC-u91DVNcJFvQVtX-hnXqVn7t4OtcRtFackrsMtyKSv4XkykhDK0TW9Jsd6wotCIzzQvcddIwF0EXhYwKF_3SUlS6KzhHbwL6WCVzRERggtyJ1CrPTf7oaMBTO0rumlD-cyrgaY4TkkSYTFJqRN29UOA9iQNngFCqtg&gsessionid=dpL_fKbTjJRSwiSEuLMJjSajcB88lRLKlKBlant1H9VOjoWfR_F0Bw)  
  <sub>Blockchain News, 6 hours ago</sub>  
  iShares Russell 2000 ETF (IWM) is trading at $265.85, up 1.09% over the last 24 hours, but the move is still taking place below the 20-day and 50-day moving...
- [Before the bell: Bitcoin can’t catch a break](https://www.google.com/goto?url=CAESkQEBxCJF133D1CI-WnbYruQcpSQLGYmTVzo6eEoN0BxIXxbe9k10nkakCfJdm2HM5yklAAbOIeRRhXD-VZiA9P5D9Fl2XC9QGXUZFuxpdOcJOkeG-mKe7mj_YoTYsWCJc1k3lUWvxtHRYFx2-orDxGyfJOO87_iDyP8xocr2236Yg6o-xzB6fnnUA9h9OIb1jwgh&gsessionid=dpL_fKbTjJRSwiSEuLMJjSajcB88lRLKlKBlant1H9VOjoWfR_F0Bw)  
  <sub>TheStreet, 56 minutes ago</sub>  
  The top cryptocurrency is struggling to maintain its recent bounce, while crypto-related stocks and major U.S. equity ETFs are heading lower in premarket...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score -0.10</summary>

```text
US Treasury yields: 3-month 4.17% (+0.03 on the week) | 5-year 4.71% (-0.19 on the week) | 10-year 4.90% (-0.20 on the week) | 30-year 5.29% (-0.17 on the week)
Yield curve, 10-year minus 3-month: +0.73 points -- upward sloping (normal)
US dollar index: 103.81 (+0.32 on the week)
Volatility (VIX): 29.34 (+3.9 on the week) -- stressed
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.1% (2026-10-01) | jobless claims 203k (2026-11-14)
Policy and expectations: Fed target 4.00% | market expects 2.1% inflation over 10 years
Rate path: 2-year Treasury 4.63% vs Fed target 3.75-4.00% -- the bond market prices about 3 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score -0.35</summary>

```text
Last close 266.10 (bar of 2026-11-24), from 501 daily bars
Trend: vs 20d SMA 274.96 (-3.2%), 50d 277.44 (-4.1%), 200d 279.57 (-4.8%); 50d below 200d
Momentum: RSI(14) 41.9 | MACD -3.998 vs signal -2.594 (histogram -1.403)
Returns: 1d +0.1% | 5d -1.1% | 1m -3.9% | 3m -11.0%
52-week range: 239.61 - 305.09 (now 40.5% of the way up)
Volatility: ATR(14) 5.50 (2.1% of price) | annualised 20d 31.0%
Volume: 0.13x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.10</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score +0.10</summary>

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
Rolled up from the 5 largest holdings, 1.9% of the fund by weight  -- thin, so read this as a fact about that slice rather than the fund
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 1.54 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +16.3% above the current prices
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
Contract: RUSSELL E-MINI - CHICAGO MERCANTILE EXCHANGE (positions as of 2026-11-17, published the following Friday)
Large speculators: net short 9.2% of open interest (459,730 contracts)
Change on the week: +0.9% of open interest
Crowding: 83% percentile over 52 weeks -- within its normal range
Read this as crowding, not as a forecast: an extreme is as often the end of a move as the middle of one.
```

</details>

<details><summary><b>Money going into and out of this fund</b> — score -0.20</summary>

```text
Direction: flat (1 month)
Share count change: 1 week: +0.0% (0.00) over 7d | 1 month: +0.0% (0.00) over 31d
Shares outstanding: 281.05M | fund size: 74.79B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Farm goods basket (DBA) · Index fund — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Technical indicators show a slight bearish tilt (price below short‑ and medium‑term averages, low volume and modest RSI), while fundamentals are modestly positive (10% annual return over three years and a 3.4% yield). Fund flows are flat, indicating no new investor conviction, and there are no macro surprises or news to shift the view. The mixed signals balance out, leading to a neutral stance.

**Main reasons it gave:**
- Price below 20‑day, 50‑day and 200‑day SMAs indicating slight bearish trend
- RSI 37.4 and volume 0.02× 20‑day average suggest limited upside
- Three‑year record of +10% annual return and 3.4% yield support modest bullish view
- Flat share count over 1‑week and 1‑month shows no net investor conviction
- Macro: no policy surprise, yields unchanged, normal upward‑sloping yield curve

<details><summary><b>News</b> — score +0.00</summary>

_No news found for this one today._

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.17% (+0.03 on the week) | 5-year 4.71% (-0.19 on the week) | 10-year 4.90% (-0.20 on the week) | 30-year 5.29% (-0.17 on the week)
Yield curve, 10-year minus 3-month: +0.73 points -- upward sloping (normal)
US dollar index: 103.81 (+0.32 on the week)
Volatility (VIX): 29.34 (+3.9 on the week) -- stressed
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.1% (2026-10-01) | jobless claims 203k (2026-11-14)
Policy and expectations: Fed target 4.00% | market expects 2.1% inflation over 10 years
Rate path: 2-year Treasury 4.63% vs Fed target 3.75-4.00% -- the bond market prices about 3 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score -0.20</summary>

```text
Last close 26.32 (bar of 2026-11-24), from 501 daily bars
Trend: vs 20d SMA 26.42 (-0.4%), 50d 27.54 (-4.5%), 200d 27.42 (-4.0%); 50d above 200d
Momentum: RSI(14) 37.4 | MACD -0.391 vs signal -0.447 (histogram 0.056)
Returns: 1d +0.3% | 5d -0.2% | 1m -4.7% | 3m -8.0%
52-week range: 25.44 - 29.49 (now 21.6% of the way up)
Volatility: ATR(14) 0.23 (0.9% of price) | annualised 20d 10.6%
Volume: 0.02x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.15</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score +0.15</summary>

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
Share count change: 1 week: +0.0% (0.00) over 7d | 1 month: +0.0% (0.00) over 31d
Shares outstanding: 27.60M | fund size: 726.29M
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Commodities basket (DBC) · Index fund — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:** no explanation. It wrote only “NEUTRAL”, so the main reasons below are all it gave.

**Main reasons it gave:**
- Crude inventories built +3.4 M barrels (bearish)
- EIA forecast oil price down 13% over six months (bearish)
- Fund share count rose 5% weekly, 15% monthly (bullish inflow)
- Technicals: RSI 22 (oversold) and price below 20‑day SMA (bearish)
- No macro surprise in policy or data releases (neutral)

<details><summary><b>News</b> — score +0.00</summary>

_No news found for this one today._

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.17% (+0.03 on the week) | 5-year 4.71% (-0.19 on the week) | 10-year 4.90% (-0.20 on the week) | 30-year 5.29% (-0.17 on the week)
Yield curve, 10-year minus 3-month: +0.73 points -- upward sloping (normal)
US dollar index: 103.81 (+0.32 on the week)
Volatility (VIX): 29.34 (+3.9 on the week) -- stressed
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.1% (2026-10-01) | jobless claims 203k (2026-11-14)
Policy and expectations: Fed target 4.00% | market expects 2.1% inflation over 10 years
Rate path: 2-year Treasury 4.63% vs Fed target 3.75-4.00% -- the bond market prices about 3 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 29.17 (bar of 2026-11-24), from 501 daily bars
Trend: vs 20d SMA 31.09 (-6.2%), 50d 32.26 (-9.6%), 200d 29.79 (-2.1%); 50d above 200d
Momentum: RSI(14) 22.0 | MACD -0.944 vs signal -0.741 (histogram -0.203)
Returns: 1d +0.2% | 5d -3.4% | 1m -13.6% | 3m -4.4%
52-week range: 22.36 - 34.10 (now 58.0% of the way up)
Volatility: ATR(14) 0.47 (1.6% of price) | annualised 20d 19.7%
Volume: 0.02x the 20-day average
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
Three-year record: +11.3% a year | beta to the market 1.04
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
US inventories, week ending 2026-11-13 (published the following Wednesday)
  Crude oil: 417.8 million barrels, +3.4 on the week (a build), 25% percentile over 52 weeks
  Natural gas: 3,882.0 billion cubic feet, +20.0 on the week (a build), 96% percentile over 52 weeks -- high for the time of year
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

<details><summary><b>Buying and selling by company insiders</b> — score +0.30</summary>

_Not available today._

</details>

<details><summary><b>Who is positioned how</b> — score +0.30</summary>

_Not available today._

</details>

<details><summary><b>Money going into and out of this fund</b> — score +0.30</summary>

```text
Direction: money coming in (1 month)
Share count change: 1 week: +5.0% (91.70M) over 7d | 1 month: +15.4% (258.67M) over 32d
Shares outstanding: 66.28M | fund size: 1.93B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Developing country bonds (EMB) · Index fund — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:** no explanation. It wrote only “NEUTRAL”, so the main reasons below are all it gave.

**Main reasons it gave:**
- US macro data (inflation 3.7%, unemployment 4.1%) in line with expectations, no surprise
- Technical indicators (RSI 41.3, MACD negative) show bearish momentum but low volume, no decisive break
- Fund flows show modest inflows (+6.6% month) indicating demand but not strong conviction

<details><summary><b>News</b> — score +0.00</summary>

_No news found for this one today._

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.17% (+0.03 on the week) | 5-year 4.71% (-0.19 on the week) | 10-year 4.90% (-0.20 on the week) | 30-year 5.29% (-0.17 on the week)
Yield curve, 10-year minus 3-month: +0.73 points -- upward sloping (normal)
US dollar index: 103.81 (+0.32 on the week)
Volatility (VIX): 29.34 (+3.9 on the week) -- stressed
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.1% (2026-10-01) | jobless claims 203k (2026-11-14)
Policy and expectations: Fed target 4.00% | market expects 2.1% inflation over 10 years
Rate path: 2-year Treasury 4.63% vs Fed target 3.75-4.00% -- the bond market prices about 3 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 90.53 (bar of 2026-11-24), from 501 daily bars
Trend: vs 20d SMA 91.43 (-1.0%), 50d 91.57 (-1.1%), 200d 94.52 (-4.2%); 50d below 200d
Momentum: RSI(14) 41.3 | MACD -0.388 vs signal -0.268 (histogram -0.121)
Returns: 1d -0.2% | 5d -0.2% | 1m -1.1% | 3m -5.0%
52-week range: 89.92 - 97.74 (now 7.7% of the way up)
Volatility: ATR(14) 0.49 (0.5% of price) | annualised 20d 7.8%
Volume: 0.16x the 20-day average
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
Three-year record: +7.5% a year | beta to the market 1.06
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
Share count change: 1 week: +1.3% (168.70M) over 7d | 1 month: +6.6% (847.74M) over 31d
Shares outstanding: 150.74M | fund size: 13.65B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### US company bonds, riskier (HYG) · Index fund — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> No macro surprise; technicals show downtrend with no decisive break; fund flows positive but not strong enough to shift view

**Main reasons it gave:**
- No macro surprise: inflation 3.7% and unemployment 4.1% within expectations
- Technical indicators show downtrend with price below 20d, 50d, 200d SMAs and RSI 36.7, no decisive break
- Fund flows positive (+0.9% weekly, +6.4% monthly) but not strong enough to shift view

<details><summary><b>News</b> — score +0.00</summary>

_No news found for this one today._

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.17% (+0.03 on the week) | 5-year 4.71% (-0.19 on the week) | 10-year 4.90% (-0.20 on the week) | 30-year 5.29% (-0.17 on the week)
Yield curve, 10-year minus 3-month: +0.73 points -- upward sloping (normal)
US dollar index: 103.81 (+0.32 on the week)
Volatility (VIX): 29.34 (+3.9 on the week) -- stressed
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.1% (2026-10-01) | jobless claims 203k (2026-11-14)
Policy and expectations: Fed target 4.00% | market expects 2.1% inflation over 10 years
Rate path: 2-year Treasury 4.63% vs Fed target 3.75-4.00% -- the bond market prices about 3 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score -0.20</summary>

```text
Last close 76.39 (bar of 2026-11-24), from 501 daily bars
Trend: vs 20d SMA 77.01 (-0.8%), 50d 77.27 (-1.1%), 200d 79.18 (-3.5%); 50d below 200d
Momentum: RSI(14) 36.7 | MACD -0.260 vs signal -0.202 (histogram -0.058)
Returns: 1d -0.2% | 5d -0.3% | 1m -1.1% | 3m -4.4%
52-week range: 76.33 - 81.18 (now 1.1% of the way up)
Volatility: ATR(14) 0.30 (0.4% of price) | annualised 20d 5.0%
Volume: 0.06x the 20-day average
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

<details><summary><b>Buying and selling by company insiders</b> — score +0.30</summary>

_Not available today._

</details>

<details><summary><b>Who is positioned how</b> — score +0.30</summary>

_Not available today._

</details>

<details><summary><b>Money going into and out of this fund</b> — score +0.30</summary>

```text
Direction: money coming in (1 month)
Share count change: 1 week: +0.9% (159.02M) over 7d | 1 month: +6.4% (1.07B) over 32d
Shares outstanding: 232.33M | fund size: 17.75B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### US government bonds, 7-10 years (IEF) · Index fund — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:** no explanation. It wrote only “Neutral”, so the main reasons below are all it gave.

**Main reasons it gave:**
- Large speculators net short 39.7% of open interest, with a -2% change this week, indicating no strong directional shift
- Fund fundamentals solid: 4% yield, AA credit quality, low expense ratio, but no material macro catalyst
- Technicals show price above short‑term SMAs but below 200‑day SMA, RSI 60.7, MACD positive, no decisive breakout on volume
- Macro data: yields fell slightly across the curve, inflation and unemployment near expectations, VIX high but stable, no surprise policy move

<details><summary><b>News</b> — score +0.00</summary>

- [Think Total Market ETF Defensief (DTM) Seasonal returns chart](https://uk.finance.yahoo.com/quote/DTM/seasonality/)  
  <sub>Yahoo Finance UK, 21 hours ago</sub>  
  Think Total Market ETF Defensief (DTM) seasonal returns chart provides the mean and median returns by month to inform your investment strategy.
- [Top Tokenized ETFs by Market Cap](https://www.google.com/goto?url=CAESXgHEIkXXRRoTcEcJZ_plRvynMa3LlL7XyLw10vV_2W9h9FsgczNucSg6HxiHMWF6jYsk0_eqGMtHNFsyounLCVDzeNO6CqeyL01UTn8XVm8_s3jkLxFFSZbtv4m4bow&gsessionid=3bwhzBBOCpFLRPvPR0brcR58yu_jt3Py26DReisIK7RZyxwnAW7aGA)  
  <sub>Coingecko, 13 hours ago</sub>  
  Discover the top ETFs (exchange-traded funds) by tokenized market cap. Track ETF prices alongside their tokenized prices, market cap,...
- [Are Asian Market Rescue Measures Working? US Stock Futures…](https://www.google.com/goto?url=CAESZQHEIkXXJIaeYZVzdkVlezuNxiq2CdArdAeikJ1dH7BwKDKQlRyZioybwmeC5vJE4rN0Md2yvaB6vkwt43X1vmyyjqVlM61Nb3cv-1__XRFcTrol5h67c39Dy75BF2Y9XbR8-R-1&gsessionid=3bwhzBBOCpFLRPvPR0brcR58yu_jt3Py26DReisIK7RZyxwnAW7aGA)  
  <sub>Longbridge, 12 hours ago</sub>  
  Zhitong Finance APP notes that US Treasury futures fell as the recent equity sell-off appeared to be attracting some buyers back into the market,...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.17% (+0.03 on the week) | 5-year 4.71% (-0.19 on the week) | 10-year 4.90% (-0.20 on the week) | 30-year 5.29% (-0.17 on the week)
Yield curve, 10-year minus 3-month: +0.73 points -- upward sloping (normal)
US dollar index: 103.81 (+0.32 on the week)
Volatility (VIX): 29.34 (+3.9 on the week) -- stressed
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.1% (2026-10-01) | jobless claims 203k (2026-11-14)
Policy and expectations: Fed target 4.00% | market expects 2.1% inflation over 10 years
Rate path: 2-year Treasury 4.63% vs Fed target 3.75-4.00% -- the bond market prices about 3 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 91.75 (bar of 2026-11-24), from 501 daily bars
Trend: vs 20d SMA 91.16 (+0.6%), 50d 90.51 (+1.4%), 200d 93.46 (-1.8%); 50d below 200d
Momentum: RSI(14) 60.7 | MACD 0.153 vs signal 0.090 (histogram 0.063)
Returns: 1d +0.1% | 5d +1.5% | 1m +0.7% | 3m -1.7%
52-week range: 88.92 - 97.99 (now 31.2% of the way up)
Volatility: ATR(14) 0.47 (0.5% of price) | annualised 20d 7.0%
Volume: 0.18x the 20-day average
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
Three-year record: +3.4% a year | beta to the market 1.17
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
Share count change: 1 week: -1.7% (-763.86M) over 7d | 1 month: +3.2% (1.34B) over 32d
Shares outstanding: 475.29M | fund size: 43.61B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### US company bonds, safer (LQD) · Index fund — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> No macro surprise, no decisive technical break, and only moderate demand signals. The fund shows modest net inflows over the month (+12.6%) but a recent week outflow (-0.9%). Technicals are near the 52‑week low with neutral momentum. Macro data are unchanged and yields have fallen only modestly while the market still expects further rate hikes. Overall, the evidence does not justify a directional tilt.

**Main reasons it gave:**
- Yields fell modestly (10‑year -0.20% week) but market expects ~3 quarter‑point hikes over next 2 years
- Price near 52‑week low (101.83) with RSI 52.4 and no decisive technical break
- Net inflow of +12.6% shares over past month, offset by -0.9% outflow in last week
- VIX elevated at 29.34, indicating stressed market conditions

<details><summary><b>News</b> — score +0.00</summary>

- [SPIB: IG Bond ETF With Lower Rate Risk, But Higher Credit And Sector Risks (NYSEARCA:SPIB)](https://seekingalpha.com/article/4971413-spib-ig-bond-etf-with-lower-rate-risk-but-higher-credit-and-sector-risks?source=generic_rss)  
  <sub>Seeking Alpha, 1 hour ago</sub>  
  State Street SPDR Portfolio Intermediate Term Corporate Bond Index ETF offers diversified investment-grade exposure for stable or decreasing rates.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.17% (+0.03 on the week) | 5-year 4.71% (-0.19 on the week) | 10-year 4.90% (-0.20 on the week) | 30-year 5.29% (-0.17 on the week)
Yield curve, 10-year minus 3-month: +0.73 points -- upward sloping (normal)
US dollar index: 103.81 (+0.32 on the week)
Volatility (VIX): 29.34 (+3.9 on the week) -- stressed
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.1% (2026-10-01) | jobless claims 203k (2026-11-14)
Policy and expectations: Fed target 4.00% | market expects 2.1% inflation over 10 years
Rate path: 2-year Treasury 4.63% vs Fed target 3.75-4.00% -- the bond market prices about 3 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 103.79 (bar of 2026-11-24), from 501 daily bars
Trend: vs 20d SMA 103.76 (+0.0%), 50d 103.45 (+0.3%), 200d 107.10 (-3.1%); 50d below 200d
Momentum: RSI(14) 52.4 | MACD -0.056 vs signal -0.061 (histogram 0.005)
Returns: 1d -0.1% | 5d +1.0% | 1m -0.2% | 3m -2.8%
52-week range: 101.83 - 112.05 (now 19.2% of the way up)
Volatility: ATR(14) 0.52 (0.5% of price) | annualised 20d 6.3%
Volume: 0.07x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.30</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score +0.30</summary>

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
Share count change: 1 week: -0.9% (-286.09M) over 7d | 1 month: +12.6% (3.59B) over 32d
Shares outstanding: 308.70M | fund size: 32.04B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### S&P 500, equal weight (RSP) · Index fund — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> No macro surprise, technicals lack a decisive break, and mixed behavioural signals (net short speculators vs strong fund inflows) leave the outlook neutral.

**Main reasons it gave:**
- No macro surprise: inflation 3.7% in line with expectations and Fed target unchanged
- Technical indicators show no decisive break: RSI 44.7, MACD negative, low volume
- Positioning net short 11.2% increased 3.8% week over week, but fund inflows strong (+6.6% share count weekly) offsetting sentiment

<details><summary><b>News</b> — score +0.00</summary>

- [Invesco S&P 500 Equal Weight ETF (RSP) stock price, news, quote and history](https://sg.finance.yahoo.com/quote/RSP/)  
  <sub>Yahoo Finance Singapore, 21 hours ago</sub>  
  Invesco S&P 500 Equal Weight ETF (RSP) ... This price reflects trading activity during the overnight session on the Blue Ocean ATS, available 8 p.m. to 4 a.m. ET,...
- [The S&P 500 Just Fell Into a Correction. Your $3 Million Retirement Portfolio May Be Less Diversified Than You Think](https://247wallst.com/investing/2026/11/23/the-sp-500-just-fell-into-a-correction-your-3-million-retirement-portfolio-may-be-less-diversified-than-you-think/)  
  <sub>24/7 Wall St., 22 hours ago</sub>  
  An S&P 500 index fund hides heavy concentration: the top 10 holdings make up about 37% of SPY, so five stocks hold roughly $800,000 of $3 million.
- [Nvidia Accounts for 34% of S&P 500 Rally as Index Weight Climbs to 6.4%](https://www.google.com/goto?url=CAEShQEBxCJF1_5u9pHnNamB-bH6nH3I2k9FKYUnuM6BJrF0nRjABo7ipY9vE0Ohe_ICa25yf_jQu2OFav4lqnO8Nqml72eAbtNTAOqUCDj4jOWFjxyxdNFh7X1KDtnXJlDIhtEgcKphcR6qOwL8mSroBiiZCEehviMLwgvBYOGTI3YBVvTgqfYH&gsessionid=1mafu5cEveqyjGxJnjSGZczjAklGj7J2zRQe6VpydxEtjno7FyOtXw)  
  <sub>EBC Financial Group, 11 hours ago</sub>  
  Nvidia accounted for approximately 34% of the S&P 500's 326.78-point rally on 23 November 2026, adding about 111 points as its shares surged 31.48%...
- [Safe-Harbor ETFs: Shelter From the Storm](https://www.google.com/goto?url=CAEShAEBxCJF11AbevgAjwgFzWoxncg4rMu5tYKtoN9vDmYMmd76MpTXlSpBH84JB_-t80fewAu66pGS4FToZxhwKRiIumm7urBmZ_0NlMFca80osulKmffC7MihZu1Hwhxg2fMeclBtgHyiEMCP4q_uViLSWSlaDo4hDFFmqkJD98A6H4ULX0g&gsessionid=1mafu5cEveqyjGxJnjSGZczjAklGj7J2zRQe6VpydxEtjno7FyOtXw)  
  <sub>ETF Database, 57 minutes ago</sub>  
  Combining value, equal-weight, and quality ETFs protects portfolios during downturns without completely missing explosive growth recoveries.
- [RSPA: Defensive Income For A Market Ignoring Fundamentals (NYSEARCA:RSPA)](https://www.google.com/goto?url=CAESngEBxCJF109a5EHKdVqZh8ZbHswHl_G8WulTFArh3k__y1aOyaAhTghkiXp-ubETohp99akLuChJDnp19docUMfJSP-ybdTBYzwdrd-WAERb3bO2u3I8YSBr9tdDUyiTxO8ywZRgsX12c00gCQbQp1veQWbIRKL0Equ2RnPRhEWJGcNTcoo0bKfLIAUz4i6CAPpHb1rKn0-cn-nG39vJcA&gsessionid=1mafu5cEveqyjGxJnjSGZczjAklGj7J2zRQe6VpydxEtjno7FyOtXw)  
  <sub>Seeking Alpha, 4 hours ago</sub>  
  Invesco S&P 500 Equal Weight Income Advantage ETF offers defensive exposure and monthly income as capital rotates away from mega-cap technology.
- [Nvidia's 33% jump on Huang's return may supply roughly a fifth to a quarter of the S&P 500's rebound](https://www.google.com/goto?url=CAESpgEBxCJF14ooSetYor22blX54Rpp3npkojBl2RkjZgyp97ufGwTMnixRvNuJmIUhGc9rwjVQT_IjyVVeDvQ3LTs9ewMKWwzRYrNecahl5uXHLzr_LGyxkCs19m6V5MJQ-T2Pou68F9FiEV7Zzkz8Y747UMuGioxHV7SnxUW_v3Qg3byiyZ2i97mRJpnaPO9dJShCaCPPuvcBm-rTshIKOD9DKjYLnXuL&gsessionid=1mafu5cEveqyjGxJnjSGZczjAklGj7J2zRQe6VpydxEtjno7FyOtXw)  
  <sub>Quantisnow, 23 hours ago</sub>  
  By rough estimate, Nvidia added about $750 billion in market value by 10:20 a.m. ET, while the equal-weight S&P 500 fund rose 2.32%, less than half of SPY's...
- [The S&P 500 Just Had the Second-Biggest Point Gain in Its History](https://www.google.com/goto?url=CAESqQEBxCJF10SyBF88gcTXNhLBKuoQzWaUf3Cm_kJawgkERG5FjxWkUxvsg8SxjSQ-m1tmOaEu_6i2MDH_DTP5DXw16p7iR7TTQwWrVB3fGeL4v5xZEkGEGJGAd3WqU9PeVIrrZFQFiEaIbEH41bS-ukyfEtsAIgmxzOHhSJoafNGmSAgn4uDHIvi64HtlnSW3mQOJhLHkwT70R2meztxMnsax_tMqtQm_mRot&gsessionid=1mafu5cEveqyjGxJnjSGZczjAklGj7J2zRQe6VpydxEtjno7FyOtXw)  
  <sub>24/7 Wall St., 3 hours ago</sub>  
  SPY jumped 5% after seven straight losing days, but the record point gain overstates a rally that was far smaller in percentage terms than 2020 or 2025.
- [S&P 500 Correction Exposes Heavy Retirement Portfolio Concentration](https://www.google.com/goto?url=CAESgQEBxCJF138LURjckUZOr0vgepgk_fr-pSGwZNVA0kG7t4dLeMnS7BdkhxZGF3dlyv0-HN5xXq-xtnbs-ZDEAWJutHsXo2P7tl3pSgauL8gT49I1u1HsYj1lLqpVQdsfp_DOdBjnyx6FJHWrMBjQ7TBB2IvvffUoBEjfkh645cyWfi4&gsessionid=1mafu5cEveqyjGxJnjSGZczjAklGj7J2zRQe6VpydxEtjno7FyOtXw)  
  <sub>Demokratis.co.id, 21 hours ago</sub>  
  The S&P 500 entered correction territory after an 11.6% decline, exposing retirees' heavy exposure to major technology stocks and market volatility.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.17% (+0.03 on the week) | 5-year 4.71% (-0.19 on the week) | 10-year 4.90% (-0.20 on the week) | 30-year 5.29% (-0.17 on the week)
Yield curve, 10-year minus 3-month: +0.73 points -- upward sloping (normal)
US dollar index: 103.81 (+0.32 on the week)
Volatility (VIX): 29.34 (+3.9 on the week) -- stressed
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.1% (2026-10-01) | jobless claims 203k (2026-11-14)
Policy and expectations: Fed target 4.00% | market expects 2.1% inflation over 10 years
Rate path: 2-year Treasury 4.63% vs Fed target 3.75-4.00% -- the bond market prices about 3 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score -0.10</summary>

```text
Last close 213.12 (bar of 2026-11-24), from 501 daily bars
Trend: vs 20d SMA 217.64 (-2.1%), 50d 214.74 (-0.8%), 200d 209.34 (+1.8%); 50d above 200d
Momentum: RSI(14) 44.7 | MACD -0.967 vs signal 0.161 (histogram -1.128)
Returns: 1d +0.1% | 5d -1.2% | 1m -1.9% | 3m -4.0%
52-week range: 186.53 - 223.33 (now 72.3% of the way up)
Volatility: ATR(14) 3.26 (1.5% of price) | annualised 20d 22.5%
Volume: 0.08x the 20-day average
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

<details><summary><b>What analysts and big funds say</b> — score -0.10</summary>

_Not available today._

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score -0.10</summary>

```text
Rolled up from the 5 largest holdings, 1.4% of the fund by weight  -- thin, so read this as a fact about that slice rather than the fund
Ratings by weight: buy 38.4% | hold 61.6% | sell 0.0% (mean 2.55 on a 1=strong buy to 5=strong sell scale)
Weighted price target: -0.3% above the current prices
Holdings read: MRNA, PTC, ACN, IT, HAS
Recent rating changes among them:
  - MRNA: 2026-11-09 Goldman Sachs: main, Neutral -> Neutral
  - PTC: 2026-11-12 Wolfe Research: down, Outperform -> Peer Perform
  - ACN: 2026-10-26 Wells Fargo: main, Equal-Weight -> Equal-Weight
  - IT: 2026-11-06 Barclays: down, Equal-Weight -> Underweight
  - HAS: 2026-10-28 UBS: main, Buy -> Buy
```

</details>

<details><summary><b>Buying and selling by company insiders</b> — score -0.10</summary>

_Not available today._

</details>

<details><summary><b>Who is positioned how</b> — score -0.10</summary>

```text
Contract: E-MINI S&P 500 - CHICAGO MERCANTILE EXCHANGE (positions as of 2026-11-17, published the following Friday)
Large speculators: net short 11.2% of open interest (2,096,958 contracts)
Change on the week: +3.8% of open interest
Crowding: 100% percentile over 52 weeks -- a crowded long by the standards of the past year
Read this as crowding, not as a forecast: an extreme is as often the end of a move as the middle of one.
```

</details>

<details><summary><b>Money going into and out of this fund</b> — score -0.10</summary>

```text
Direction: money coming in (1 month)
Share count change: 1 week: +6.6% (6.42B) over 7d | 1 month: +9.4% (8.90B) over 32d
Shares outstanding: 485.34M | fund size: 103.44B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### US inflation-linked bonds (TIP) · Index fund — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> No material macro surprise, modest bullish shift in positioning, stable fundamentals, neutral technicals.

**Main reasons it gave:**
- US Treasury yields fell modestly across the curve this week
- Large speculators remain net short 39.7% of open interest but short position decreased 2% of OI
- Fund basics show high credit quality (AA) and stable 4.4% yield
- Technical indicators are neutral: price near 20‑day SMA, RSI 53.4, low volume

<details><summary><b>News</b> — score +0.00</summary>

- [CTBC TIP Customized Taiwan Growth and High Dividend ETF (00934.TW) Seasonal returns chart](https://uk.finance.yahoo.com/quote/00934.TW/seasonality/)  
  <sub>Yahoo Finance UK, 24 hours ago</sub>  
  CTBC TIP Customized Taiwan Growth and High Dividend ETF (00934.TW). 24.34 +0.44 (+1.84%). At close: 13:30:13 GMT+8. Historical seasonality.
- [Liquidity Mapping Around (TIP) Price Events](https://news.stocktradersdaily.com/news_release/1/Liquidity_Mapping_Around_TIP_Price_Events_112326074802_1795481282.html)  
  <sub>Stock Traders Daily, 19 hours ago</sub>  
  Price-action only: Ishares Tips Bond Etf (TIP) movements set the tone for institutional models. Liquidity Mapping Around (TIP) Price Events.
- [SCHD vs. VIG: Which Dividend ETF Is the Better Buy Now?](https://www.google.com/goto?url=CAESlgEBxCJF13rjeQ4itGtOVDVWehwAfKzSNaDa2qAYQXcXc-ZIfkcyjJYsX3rQuWAukiZI1Nkw5bYaYh8VbeNW71qZoD2pbYWGS9oQkRo-Cl9Z1idsST94LBixLaNPDr978qIDhweUvgentPSCmPMLB_IRJdiE4OIkPsncqAkneDU0Dc2dZP18w8BtMXuxAv3ZN-sN341nnMI&gsessionid=csqbsOYH5zgub5Doxh55ixvqPF0StaU4i84pgUMLtRLQXgenMDPuvA)  
  <sub>TipRanks, 53 minutes ago</sub>  
  For investors comparing dividend ETFs, Schwab U.S. Dividend Equity ETF ($SCHD) focuses on higher income today, while Vanguard Dividend Appreciation ETF...
- [Missed the IPO? New Anthropic-Focused ETFs Offer a Way In](https://www.google.com/goto?url=CAESmgEBxCJF13pxiXDMPd6qg-Wg_yrHooPTke1cx1zP-NmZzrevUYUZsNr9MQZue-vKTPlVI_q4r3CifAmLlk3JT0wFU46wfRRALHv3uscbWbPxOieb2HY1bX-dYh2PzaERvKwYKh7-h5LdLWB58IwZ5k3249mkVN0_PrH4rRoLyUU5MLEoVjTUYLoGV83cYIGlxXbXp2YD6BbIGDNG&gsessionid=csqbsOYH5zgub5Doxh55ixvqPF0StaU4i84pgUMLtRLQXgenMDPuvA)  
  <sub>TipRanks, 3 hours ago</sub>  
  Claude chatbot maker Anthropic ($ANT) raised a record $93.5 billion, plus additional shares, in its initial public offering (IPO) on Nasdaq on November 19.
- [VOO vs. VTI: Why One Vanguard ETF Beats the Other](https://www.google.com/goto?url=CAESkQEBxCJF1-3XG3RB3Feq3eeZdM3gyDwKHNFq2wa4oNM2s8ICToCLx10C3PyKVVvAxgz7mO_RbYiaYeTE13NQ9sqVAFMR3t1Badp268Psbtt7a0MIbLYmknIMczKscYQ1rPLgN_1JjOJS6ibjK2ChLuUy3gwR1SZ5mUhI4RmwcjkB7ShKRrqC6C_ZyzgN8GNkXUVr&gsessionid=csqbsOYH5zgub5Doxh55ixvqPF0StaU4i84pgUMLtRLQXgenMDPuvA)  
  <sub>TipRanks, 2 hours ago</sub>  
  Vanguard S&P 500 ETF ($VOO) and Vanguard Total Stock Market ETF ($VTI) are two popular choices for exposure to the U.S. stock market. VOO focuses on large...
- [Anthropic Stock Slips Below $83 IPO Price — Analysts See 50%+ Upside](https://www.google.com/goto?url=CAESmQEBxCJF1yYC3g_OmylxWyN4yFeChfo8MDYRARLUyoSmZ-Qu1U7lIaZ-wRcBJVOMHIQ_mYyQJC5vbWCXjwHup9RgqFUmxHreLL8he74_aUo2tkAT24TeY_HQ8H2RdDu9qIneXIwPdliqWLPmF0FYxPyZlssOxnT8A55QYBhTd_TtWwWuoYAowCoduhypC_4xE9k16IEG5-AyRAc&gsessionid=csqbsOYH5zgub5Doxh55ixvqPF0StaU4i84pgUMLtRLQXgenMDPuvA)  
  <sub>TipRanks, 2 hours ago</sub>  
  Anthropic stock ($ANT) fell below its $83 IPO price in Tuesday's premarket trading, giving up its gains from a record-breaking Nasdaq debut.
- [SpaceX vs. Anthropic: Which IPO Stock Offers Higher Upside, According to Analysts?](https://www.google.com/goto?url=CAESqAEBxCJF1-3Mj0HoeQiGeIJWSasknClrsku9WdTst0GZYdnTB0r-F6FSLEYOjuGRQ3Xzfs6QDA03PpYYfN9VcqS1fcPOq6ihqV6JbC_n6pAxu345DAtZlKpcmxRKqXIpAriLT41G1DyzryG8Ag6xY_udlZ6y030YN4vK-a8fQZ6hDQ7KM0oPqU0sLlYPdaxfyAesxaY6TzJvfC4ynnVTLGvptGV8hwigM1E&gsessionid=csqbsOYH5zgub5Doxh55ixvqPF0StaU4i84pgUMLtRLQXgenMDPuvA)  
  <sub>TipRanks, 2 hours ago</sub>  
  SpaceX ($SPCX) and Anthropic ($ANT) were among the most closely watched IPOs of 2026, giving investors exposure to two fast-growing industries: space...
- [Best Buy’s (BBY) Comparable Sales Jump 6.1% Ahead of Black Friday. What’s Next for Holiday Spending?](https://www.google.com/goto?url=CAEStwEBxCJF1ylJ45p2f12asTDP5shkFYcsXv4XO15_C1puuJXbPavqgm7QOodwnmNt3FCzrbsAoIqvijL1jAO_WzDCn3kph77zdAyBVNnqTMAwsAqGlUhgZk6sS2mjGMBg1U_j_Rr5V3T4sg6aUCA80_H6-gILs9By39mLu7TeOW9CbzZCD7sJEWLk6_V5D75nNh5rv7ERzr7mHeCK6XKIHopfwWI-uoFtaw0XZ48UE_Gx98dbmMuAtXc&gsessionid=csqbsOYH5zgub5Doxh55ixvqPF0StaU4i84pgUMLtRLQXgenMDPuvA)  
  <sub>TipRanks, 2 hours ago</sub>  
  Best Buy Co. ($BBY) reported strong fiscal Q3 2027 earnings on Tuesday, with comparable sales jumping 6.1%, the highest growth rate in five years.
- [Micron Stock Falls After 19% Rally — 3 Reasons Shares Could Climb Higher](https://www.google.com/goto?url=CAESnwEBxCJF127BY3cbIS473V-Alr6OWQsbZ9UPmcpuzVS9OdjPusE9Tl6shjA4FwF808TvPjEVGQ0dQSCmJlBBQqDYOvODrpra4TkSTSQtI8gq7gT9OJ8yT8jodCFdIPjkSPaL3SwDjJEbCi0Lyc-7B66TuALoizQB2jNPVeHPjbscxS8XwVsOCE_YN0-wZZ4ZV2oha8efN1y-JBIW0eDmIO8&gsessionid=csqbsOYH5zgub5Doxh55ixvqPF0StaU4i84pgUMLtRLQXgenMDPuvA)  
  <sub>TipRanks, 40 minutes ago</sub>  
  Micron Technology ($MU) stock is falling in premarket trading on Tuesday, following a 19% surge on Monday. Over the past month, Micron stock has come under...
- [Click Holdings Approves Share Repurchase Program of Up to US$1.5 Million](https://www.google.com/goto?url=CAEStwEBxCJF11N28xN_ejTecSkS_ETKkYkGrMNtMv68MBXR-u1oVkwv3pU6EaiB7taqyOyAZdkDNUQtCEiPjbT4XLxsWAgVQiIyUsGmarHHIeoxSv7kzn9T41gYOXYdvP4dZWLnX_XDVqAfIsSvKdvlSza8gKJSMQ5uNH-uWCJMj0IUHqmYU7iCNgzNWCtLXoPn4GukxfhvljMUknrCyBUt2Ig2mssgGvPAbfPOI12KkD1D2k0v0OABZfw&gsessionid=csqbsOYH5zgub5Doxh55ixvqPF0StaU4i84pgUMLtRLQXgenMDPuvA)  
  <sub>TipRanks, 17 minutes ago</sub>  
  Click Holdings Limited ( ($CLIK) ) just unveiled an announcement. Click Holdings Limited is a Hong Kong-based provider of AI-powered human resources and...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.17% (+0.03 on the week) | 5-year 4.71% (-0.19 on the week) | 10-year 4.90% (-0.20 on the week) | 30-year 5.29% (-0.17 on the week)
Yield curve, 10-year minus 3-month: +0.73 points -- upward sloping (normal)
US dollar index: 103.81 (+0.32 on the week)
Volatility (VIX): 29.34 (+3.9 on the week) -- stressed
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.1% (2026-10-01) | jobless claims 203k (2026-11-14)
Policy and expectations: Fed target 4.00% | market expects 2.1% inflation over 10 years
Rate path: 2-year Treasury 4.63% vs Fed target 3.75-4.00% -- the bond market prices about 3 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 105.67 (bar of 2026-11-24), from 501 daily bars
Trend: vs 20d SMA 105.64 (+0.0%), 50d 105.24 (+0.4%), 200d 108.45 (-2.6%); 50d below 200d
Momentum: RSI(14) 53.4 | MACD -0.077 vs signal -0.084 (histogram 0.007)
Returns: 1d +0.1% | 5d +0.8% | 1m -0.6% | 3m -1.7%
52-week range: 103.98 - 111.88 (now 21.3% of the way up)
Volatility: ATR(14) 0.36 (0.3% of price) | annualised 20d 4.6%
Volume: 0.09x the 20-day average
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
Three-year record: +3.6% a year | beta to the market 0.73
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
Share count change: 1 week: -1.0% (-150.03M) over 7d | 1 month: +2.8% (405.06M) over 32d
Shares outstanding: 138.74M | fund size: 14.66B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### US government bonds, 20+ years (TLT) · Index fund — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> No material macro surprise, technicals show modest momentum, positioning is neutral, fundamentals unchanged.

**Main reasons it gave:**
- CFTC: net short on UST futures fell 1.6% week‑over‑week, still 35.5% of open interest
- Fund basics: AA credit quality, 4.8% yield, 99.5% bonds, 0.5% cash
- Technical: price above 20‑day SMA, RSI 59.7, MACD positive, modest momentum
- Macro: 10‑year Treasury yield down 20 bps, VIX up to 29.3 indicating higher volatility

<details><summary><b>News</b> — score +0.00</summary>

- [Nasdaq, Dow, S&P 500 Futures Gain As Jensen Huang’s Return To Nvidia Sparks $3T Market Rally: SOXS, IBRX, HPE, TSM In Focus](https://www.tradingview.com/news/stocktwits:375abfa87094b:0-nasdaq-dow-s-p-500-futures-gain-as-jensen-huang-s-return-to-nvidia-sparks-3t-market-rally-soxs-ibrx-hpe-tsm-in-focus/?mobileapp_new=true)  
  <sub>TradingView, 13 hours ago</sub>  
  U.S. stock futures headed higher late Monday as the AI trade rebounded after Jensen Huang returned to Nvidia Corp. (NVDA) just two weeks after he was ousted...
- [How Much Do You Really Need Invested to Replace a $195,000 Salary With Dividends?](https://247wallst.com/personal-finance/2026/11/23/how-much-do-you-really-need-invested-to-replace-a-195000-salary-with-dividends/)  
  <sub>24/7 Wall St., 19 hours ago</sub>  
  Replacing a $195,000 salary takes roughly $5.6 million at a 3.5% yield, $3.5 million at 5.6%, or $1.6 million at 12%. Higher yields carry cut risk: BXSL...
- [Top Tokenized ETFs by Market Cap](https://www.google.com/goto?url=CAESXgHEIkXXX3bL4Up7QkIzvEK-5BG056judZ-EJJ5BPmzuWY1_0B-Yg4srkqCIEli7jKvLfq5AqmrDPW-wdWphwmnDr33-yvIdlzyQtn8TqxHBinTJGNWJfCuq27Vk5aI&gsessionid=R7r99RAbXPW6gw_ob9LdPl9sW9bYqUNMVTsWyZhHiKPuJ3DYYDPtfw)  
  <sub>Coingecko, 1 hour ago</sub>  
  Discover the top ETFs (exchange-traded funds) by tokenized market cap. Track ETF prices alongside their tokenized prices, market cap, and volume on...
- [BofA’s warning for 2027: Don’t ignore hard-landing risks (SPY:NYSEARCA)](https://www.google.com/goto?url=CAESmAEBxCJF1xxIneWfEuL4K-SDEYDqWH3-VbpZVyK7ut5nRr0Ip7OSL5mVSOiXv6N1ibOZtuw1xMX4ddAusS7Z3M1UobSYBpWE5Ji4e4qMDNJedZ4OFT3r9y3ZXkR4IWy2Mb-wMWxl6-uAPCCqMGqZGoQoL9Kos0nopzIYERm7OkOyc1UvWS8wNX7vINUKS0O5A56KTHyMgYL_8A&gsessionid=R7r99RAbXPW6gw_ob9LdPl9sW9bYqUNMVTsWyZhHiKPuJ3DYYDPtfw)  
  <sub>Seeking Alpha, 32 minutes ago</sub>  
  Investors should hedge against heavily underpriced recession risks heading into 2027 by loading up on "GRAB" assets—Government bonds (TLT) (SHY) (IEF),...
- [Australia’s Mid-Year Budget Outlook: Why Nominal GDP and Revenue Forecasts Matter](https://www.google.com/goto?url=CAEStgEBxCJF1ylKGFzGu5RjvJUgJnoaszuh4NgDZvz-9U6r5TI4rgzgVoKkEQwKUQ4IfwIm_O0WMLIWwrrNZyIBZgSmzQOkuT5YVJYzQlvb9FbJo3Ry-7GRMy1C4MjI1mDzciXSk3D7t6j5fQZTcHiFZIuvqgg9QqHMHxloUPOzrPOXfv7_LY3kJxr_JO7SBcdu2YykQc7dSVWa00NQwyqSbNsWYtflYOYCrE4GRxF47f9R6NE0RxlAHg&gsessionid=R7r99RAbXPW6gw_ob9LdPl9sW9bYqUNMVTsWyZhHiKPuJ3DYYDPtfw)  
  <sub>Kalkine, 9 hours ago</sub>  
  You are reading a free article with opinions that may differ from the recommendation given by Kalkine in its paid research reports.
- [How Did Jensen Huang Move From Resignation to Reinstatement at Nvidia (NASDAQ:NVDA) Within 11 Days?](https://www.google.com/goto?url=CAESwgEBxCJF18eMIeHKq9ktYAW875xuLiX8BI1CQog7PO9TGTxzZLge-aiDPHcrD4WZVJAIkRN-xF49tcOC_GcxaafW3M2bHt04jiHG6enxWrPmpEMCBYKhZaFWNMYNyaXLaeQ6keX_ZQCqo2e3OwwtxU2XY74YqMGi8V0XQaJTJ5DFpYXbnezuhltYubjlX8igu0hzg0UbHATxHfioeJVaCXXqoxlXenlZ2GEnDI4QUds3LZMlCUh4NdoYt-D4w3mV-3Xcqg&gsessionid=R7r99RAbXPW6gw_ob9LdPl9sW9bYqUNMVTsWyZhHiKPuJ3DYYDPtfw)  
  <sub>kalkine.ca, 24 hours ago</sub>  
  You are reading a free article with opinions that may differ from the recommendation given by Kalkine in its paid research reports.
- [Australian Business Activity: What Do Labour and Investment Data Signal for Year-End Growth?](https://www.google.com/goto?url=CAESwgEBxCJF13_ofJPc59PAbXwT8CvFBVt0A8jyhPSO6z2SOGfvhCG1784M1dM8fPNZ-MRRhTe0eKO0rBs7MAySaPVD_fGgowhZJKbfNGVUV3Bvn_Gxw_H0hgdK2F_UXd6VyK2pl91ynKWOX7iC7ITrFyMuivvOK4xXbKN-HCswHwkYhKhu0ipdpBUj1Z8I46bzUlrnpnybLsLfKjZ0H3DObfKg4s2C7VJNKX62t70FdNHDn03kV54ofpcsSN36NJzHaPWRHg&gsessionid=R7r99RAbXPW6gw_ob9LdPl9sW9bYqUNMVTsWyZhHiKPuJ3DYYDPtfw)  
  <sub>Kalkine, 9 hours ago</sub>  
  You are reading a free article with opinions that may differ from the recommendation given by Kalkine in its paid research reports.
- [What Did Washington Say After Nvidia (NASDAQ:NVDA) Brought Back Jensen Huang, and Why Should Canadian Investors Care?](https://www.google.com/goto?url=CAES0wEBxCJF18rd8zU5GQOVrdITEccaE88W2q3DMretSKWnWnwpJi2GOGz0sJpF_tn0psHny-oMbpc-qZaCcNG_ijaRolH7ss4cH0wpYt1Deqc8bj0e_0HK7-S2z_odIKWQbXKWVseXIFdr7wyULFny1mdva1J3ziNp0cBjy3QcB_yrrxPpjS43E7R_91XJelQbJayc6B4MkR313zO-MVEYxczBiqqu8TuVPv1Wu1Y3Zz8U60nbuj9AKh1skLoBInXxmJVxg5_1qgjsBwwDzeTtZjGnE1Oh&gsessionid=R7r99RAbXPW6gw_ob9LdPl9sW9bYqUNMVTsWyZhHiKPuJ3DYYDPtfw)  
  <sub>kalkine.ca, 24 hours ago</sub>  
  You are reading a free article with opinions that may differ from the recommendation given by Kalkine in its paid research reports.
- [Wall Street’s AI Trade Roars Back After Nvidia Reinstates Jensen Huang: What Nasdaq, Dow, S&P 500 Futures Signal](https://www.google.com/goto?url=CAESxAEBxCJF16vcHL6C5MHIutWCH8QH_e9zk9M2bazqnhwOlcJDD8WmYEIQ3phNz81sOq8ynq0D-ByGjvqdQQ6cFdHGroEnkR36atoOliQNv__-Nk7ucYFuFIhZYnxHW5r1c6hIj0SNlIZKFqt1oVz9leN4pN8eIIbWMe1hjN2mr9A0Kb4ZpdM6jxKdh8dDXY00pTUjfUin4bF_zrnLpacQmsJulfnaMjTur2bFjNPI4m1IFHLrU-8-E0Or83MgTOGoh6Xx6ClR&gsessionid=R7r99RAbXPW6gw_ob9LdPl9sW9bYqUNMVTsWyZhHiKPuJ3DYYDPtfw)  
  <sub>Stocktwits, 16 hours ago</sub>  
  Optimism on Wall Street soared after Nvidia announced that Huang would return as President, CEO, and board member of the company.
- [Fed Rate Hike Bets Build Ahead Of December Meet: Fed’s John Williams Says Inflation Still ‘Too High’](https://www.google.com/goto?url=CAESsQEBxCJF12hPrwwIE0t3Whdj70j99AfjLDpMXR9wzuYWIwVzzmn-gbXoYrPpbr8XFrPlZ3vNO8WGaaLE8pBTYgDHv6d64UUoL7MLcozo0Tqff_VA1gdubVkxsBPAliOR74QwEAy_Gdk-UHtxYfBC0RnPnDAbAku5Y0Aa2a_11fnLtkHpMYgViKxl2VIHHljQcQlv0GmxETvCPi38JvPHjgGu9UlDe-xcOc_Ho3aCQMC5eY8&gsessionid=R7r99RAbXPW6gw_ob9LdPl9sW9bYqUNMVTsWyZhHiKPuJ3DYYDPtfw)  
  <sub>Stocktwits, 14 hours ago</sub>  
  Federal Reserve Bank of New York President John Williams expressed confidence that inflation will get closer to the Fed's 2% target in 2027,...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.17% (+0.03 on the week) | 5-year 4.71% (-0.19 on the week) | 10-year 4.90% (-0.20 on the week) | 30-year 5.29% (-0.17 on the week)
Yield curve, 10-year minus 3-month: +0.73 points -- upward sloping (normal)
US dollar index: 103.81 (+0.32 on the week)
Volatility (VIX): 29.34 (+3.9 on the week) -- stressed
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.1% (2026-10-01) | jobless claims 203k (2026-11-14)
Policy and expectations: Fed target 4.00% | market expects 2.1% inflation over 10 years
Rate path: 2-year Treasury 4.63% vs Fed target 3.75-4.00% -- the bond market prices about 3 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 81.73 (bar of 2026-11-24), from 501 daily bars
Trend: vs 20d SMA 81.00 (+0.9%), 50d 80.11 (+2.0%), 200d 84.07 (-2.8%); 50d below 200d
Momentum: RSI(14) 59.7 | MACD 0.165 vs signal 0.098 (histogram 0.066)
Returns: 1d +0.0% | 5d +2.7% | 1m +0.1% | 3m -1.9%
52-week range: 77.11 - 90.82 (now 33.7% of the way up)
Volatility: ATR(14) 0.73 (0.9% of price) | annualised 20d 11.1%
Volume: 0.09x the 20-day average
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
Three-year record: +0.7% a year | beta to the market 2.30
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
Share count change: 1 week: +0.0% (0.00) over 7d | 1 month: +0.0% (0.00) over 31d
Shares outstanding: 109.70M | fund size: 8.97B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### US dollar (UUP) · Index fund — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:** no explanation. It wrote only “NEUTRAL”, so the main reasons below are all it gave.

**Main reasons it gave:**
- US dollar index up 0.32% on the week (modest gain, no surprise)
- Price above 20‑day, 50‑day, 200‑day SMAs but volume 0.04× 20‑day average (no decisive break)
- CFTC net short 2.2% of open interest, down 7.8% on the week (small bullish shift)
- Fund flows: +8.9% share count over 1 month, -0.5% over 1 week (mixed demand)

<details><summary><b>News</b> — score +0.00</summary>

- [UUP Dec 2026 35.000 put (UUP261218P00035000) Stock Price, News, Quote & History](https://ca.finance.yahoo.com/quote/UUP261218P00035000/)  
  <sub>Yahoo! Finance Canada, 24 hours ago</sub>  
  Find the latest UUP Dec 2026 35.000 put (UUP261218P00035000) stock quote, history, news and other vital information to help you with your stock trading and...
- [Jensen Huang Returns to Nvidia; NVDA Surges 32%, Nasdaq Rips 7%, and Taiwan Reverses Last Week’s Entire Collapse in a Single Session](https://www.theglobeandmail.com/investing/markets/stocks/NVDA/pressreleases/8970269/jensen-huang-returns-to-nvidia-nvda-surges-32-nasdaq-rips-7-and-taiwan-reverses-last-weeks-entire-collapse-in-a-single-session/)  
  <sub>The Globe and Mail, 20 hours ago</sub>  
  Detailed price information for Nvidia Corp (NVDA-Q) from The Globe and Mail including charting and trades.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.17% (+0.03 on the week) | 5-year 4.71% (-0.19 on the week) | 10-year 4.90% (-0.20 on the week) | 30-year 5.29% (-0.17 on the week)
Yield curve, 10-year minus 3-month: +0.73 points -- upward sloping (normal)
US dollar index: 103.81 (+0.32 on the week)
Volatility (VIX): 29.34 (+3.9 on the week) -- stressed
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.1% (2026-10-01) | jobless claims 203k (2026-11-14)
Policy and expectations: Fed target 4.00% | market expects 2.1% inflation over 10 years
Rate path: 2-year Treasury 4.63% vs Fed target 3.75-4.00% -- the bond market prices about 3 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 29.62 (bar of 2026-11-24), from 501 daily bars
Trend: vs 20d SMA 29.29 (+1.1%), 50d 29.02 (+2.1%), 200d 28.13 (+5.3%); 50d above 200d
Momentum: RSI(14) 65.1 | MACD 0.209 vs signal 0.178 (histogram 0.031)
Returns: 1d -0.5% | 5d +0.3% | 1m +2.1% | 3m +5.7%
52-week range: 26.47 - 29.78 (now 95.1% of the way up)
Volatility: ATR(14) 0.13 (0.4% of price) | annualised 20d 5.9%
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
Share count change: 1 week: -0.5% (-2.29M) over 7d | 1 month: +8.9% (39.33M) over 31d
Shares outstanding: 16.25M | fund size: 481.32M
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Europe (VGK) · Index fund — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Neutral stance as no macro surprise, no decisive technical break, and mixed signals from fundamentals and positioning.

**Main reasons it gave:**
- Analyst coverage thin (12% of fund) with buy rating 83.8% and price target +29% above current price
- CFTC positioning net long 4.3% of OI, weekly increase +1.6% OI, crowding at 92nd percentile
- Technical indicators: price below 20‑day, 50‑day, 200‑day SMAs; RSI 41.6; MACD negative; volume 0.08× 20‑day average
- Macro: no policy surprise; VIX up to 29.34; yields slightly higher; inflation 3.7% above Fed target

<details><summary><b>News</b> — score +0.00</summary>

- [(VGK) Movement Within Algorithmic Entry Frameworks](https://news.stocktradersdaily.com/news_release/101/VGK_Movement_Within_Algorithmic_Entry_Frameworks_112426024401_1795506241.html)  
  <sub>Stock Traders Daily, 12 hours ago</sub>  
  Key findings for Vanguard Ftse Europe Etf (NYSE: VGK). Weak Near and Mid-Term Sentiment Could Pressure Neutral Long-Term Outlook; No clear price positioning...
- [Breturn? Burnham says it's unthinkable for UK to rejoin EU without referendum](https://seekingalpha.com/news/4676000-burnham-says-its-unthinkable-for-uk-to-rejoin-eu-without-referendum?source=generic_rss)  
  <sub>Seeking Alpha, 3 hours ago</sub>  
  Andy Burnham says UK rejoining the EU without a referendum is unthinkable, but he is not proposing a rerun now and says the reset deal sets no fixed...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.17% (+0.03 on the week) | 5-year 4.71% (-0.19 on the week) | 10-year 4.90% (-0.20 on the week) | 30-year 5.29% (-0.17 on the week)
Yield curve, 10-year minus 3-month: +0.73 points -- upward sloping (normal)
US dollar index: 103.81 (+0.32 on the week)
Volatility (VIX): 29.34 (+3.9 on the week) -- stressed
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.1% (2026-10-01) | jobless claims 203k (2026-11-14)
Policy and expectations: Fed target 4.00% | market expects 2.1% inflation over 10 years
Rate path: 2-year Treasury 4.63% vs Fed target 3.75-4.00% -- the bond market prices about 3 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score -0.20</summary>

```text
Last close 84.86 (bar of 2026-11-24), from 501 daily bars
Trend: vs 20d SMA 87.45 (-3.0%), 50d 87.28 (-2.8%), 200d 87.87 (-3.4%); 50d below 200d
Momentum: RSI(14) 41.6 | MACD -0.808 vs signal -0.294 (histogram -0.514)
Returns: 1d +0.4% | 5d -2.4% | 1m -2.0% | 3m -8.5%
52-week range: 78.89 - 93.19 (now 41.7% of the way up)
Volatility: ATR(14) 1.25 (1.5% of price) | annualised 20d 24.3%
Volume: 0.08x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.00</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score +0.00</summary>

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
Rolled up from the 5 largest holdings, 12.0% of the fund by weight  -- thin, so read this as a fact about that slice rather than the fund
Ratings by weight: buy 83.8% | hold 16.2% | sell 0.0% (mean 2.08 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +29.0% above the current prices
Holdings read: ASML.AS, ROP.SW, SHEL.L, NOVN.SW, HSBA.L
Recent rating changes among them: none reported
```

</details>

<details><summary><b>Buying and selling by company insiders</b> — score -0.10</summary>

_Not available today._

</details>

<details><summary><b>Who is positioned how</b> — score -0.10</summary>

```text
Contract: MSCI EAFE  - ICE FUTURES U.S. (positions as of 2026-11-17, published the following Friday)
Large speculators: net long 4.3% of open interest (512,671 contracts)
Change on the week: +1.6% of open interest
Crowding: 92% percentile over 52 weeks -- a crowded long by the standards of the past year
Read this as crowding, not as a forecast: an extreme is as often the end of a move as the middle of one.
```

</details>

<details><summary><b>Money going into and out of this fund</b> — score -0.10</summary>

```text
Direction: money coming in (1 month)
Share count change: 1 week: +7.9% (2.80B) over 7d | 1 month: +6.1% (2.20B) over 32d
Shares outstanding: 449.76M | fund size: 38.17B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Emerging markets (VWO) · Index fund — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Neutral overall as technicals are bearish, analyst view is bullish but thin, and insider sentiment is neutral with flat flows; macro backdrop adds pressure to emerging markets.

**Main reasons it gave:**
- Technical trend below 20‑day, 50‑day, and 200‑day SMAs with RSI 39.9 indicating bearish momentum
- Analyst view strongly bullish (100% buy, +58.8% price target) but only covers 22.6% of fund, limiting impact
- Positioning shows net short 0% and flat fund flows, indicating neutral insider sentiment
- Macro backdrop: strong US dollar (+0.32% weekly) and rising yields pressuring emerging markets

<details><summary><b>News</b> — score +0.00</summary>

- [(VWO) Movement Within Algorithmic Entry Frameworks](https://news.stocktradersdaily.com/news_release/22/VWO_Movement_Within_Algorithmic_Entry_Frameworks_112426054803_1795517283.html)  
  <sub>Stock Traders Daily, 9 hours ago</sub>  
  Price-action only: Vanguard Ftse Emerging Markets Etf (VWO) movements set the tone for institutional models. (VWO) Movement Within Algorithmic Entry...
- [ETFs Investing in JD.com, Inc. Class A Stocks](https://www.tradingview.com/symbols/VIE-013C/etfs/)  
  <sub>TradingView, 13 hours ago</sub>  
  Explore funds investing in 013C in a single list with price, expense ratio, and more stats for an in-depth analysis of new opportunities.
- [ETFs Investing in Trip.com Group Ltd. Stocks](https://www.google.com/goto?url=CAESbwHEIkXXEk6uSBqc1lDDP0bfk-gYwqHbfqaQSlATwNr_Ibm3onraqQuS8XPkpuQkVZApEixb9zfKFEiv9SIpuSZiEmKVVdACKmr0H_dxSOBpHa6M2x8LcWXdjqJVLZUOlqtEcTmyrZi7JvyciduCyA&gsessionid=QgGIxJvxK5LIhCKYvLiJYeN85FPj9UirEwrgV4264SsiNBnGAvHb-g)  
  <sub>TradingView, 22 hours ago</sub>  
  Explore funds investing in CLVB in a single list with price, expense ratio, and more stats for an in-depth analysis of new opportunities.
- [Emerging Markets at Crisis-Era Valuations—Are These 5 Investments Worth the Risk?](https://www.google.com/goto?url=CAESsQEBxCJF11xnR1IBWOEdDtNRo-cKQOgBWxQpnEGXFaKGivzBKzswQ8Z2w_17JDpzWfbWq5waEBrFM0CVPHVBfWBvX1XDyLX92pt2k0vcMueVByQ9cunfFG4JgjH3WAasOLzgEjl7cfZ0ft2Um1gZi2LgfxZaTbkOj3QfPJOp_-DK2wZnHAVa1UBj3MrN-x_9voTd9TQJ_lBM9YL6_o5KjwESxGbjXF1F_bnVcM6H_QklTAk&gsessionid=QgGIxJvxK5LIhCKYvLiJYeN85FPj9UirEwrgV4264SsiNBnGAvHb-g)  
  <sub>MarketBeat, 18 hours ago</sub>  
  The MSCI Emerging Markets Index entered a bear market amid an AI stock sell-off, a strong dollar, and Brazil turmoil, pushing valuations to 2008 lows and...
- [ETFs Investing in Pop Mart International Group Limited Stocks](https://www.google.com/goto?url=CAESbwHEIkXXKLiiYMWxcLppRwRgG8zmiH5iXqQKvSb0f5jJuKaeGMCrEHuHSq8CM5WGHkUoCoFJ3oHfm7JGQj_gOYk1z__HhY1z4rMA1G8dPD4Kuz1dcSoIjUUuRocR-jDg95GRi7y5ChqJBaI-cgXfIw&gsessionid=QgGIxJvxK5LIhCKYvLiJYeN85FPj9UirEwrgV4264SsiNBnGAvHb-g)  
  <sub>TradingView, 22 hours ago</sub>  
  Explore funds investing in POPM in a single list with price, expense ratio, and more stats for an in-depth analysis of new opportunities.
- [ETFs Investing in China Shenhua Energy Co. Ltd. Class H Stocks](https://www.google.com/goto?url=CAESbgHEIkXXmtW1vwv_ZWpYYETe1XvOzK3GSkj236nODXSdCF7FGb6tI6R8VeUouyrw7dGhgU3_EN6d6hPJzIUh1Ti7nrOPFLu56hwG1KW8dCd1MqmYVgJHTAu-z9eUyelcIa1-mkhkV9f_kbQnXr72&gsessionid=QgGIxJvxK5LIhCKYvLiJYeN85FPj9UirEwrgV4264SsiNBnGAvHb-g)  
  <sub>TradingView, 22 hours ago</sub>  
  Explore funds investing in IKF in a single list with price, expense ratio, and more stats for an in-depth analysis of new opportunities.
- [ETFs Investing in China Hongqiao Group Ltd. Stocks](https://www.google.com/goto?url=CAESbgHEIkXXY7IlaZtJa-V5_-w1EktJh7V5DXqYzv7uoAE9TwBftdHFVzMjkh6LNF5eyxUU-7dOG9ctXXJHhvBt9z5xlbhVV-VIkwVx1WxlBzjosM5-GqZquXU1i-L_63D3jvNLyK1chYm6GT-OyXXj&gsessionid=QgGIxJvxK5LIhCKYvLiJYeN85FPj9UirEwrgV4264SsiNBnGAvHb-g)  
  <sub>TradingView, 22 hours ago</sub>  
  Explore funds investing in H0Q in a single list with price, expense ratio, and more stats for an in-depth analysis of new opportunities.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.17% (+0.03 on the week) | 5-year 4.71% (-0.19 on the week) | 10-year 4.90% (-0.20 on the week) | 30-year 5.29% (-0.17 on the week)
Yield curve, 10-year minus 3-month: +0.73 points -- upward sloping (normal)
US dollar index: 103.81 (+0.32 on the week)
Volatility (VIX): 29.34 (+3.9 on the week) -- stressed
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.1% (2026-10-01) | jobless claims 203k (2026-11-14)
Policy and expectations: Fed target 4.00% | market expects 2.1% inflation over 10 years
Rate path: 2-year Treasury 4.63% vs Fed target 3.75-4.00% -- the bond market prices about 3 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score -0.30</summary>

```text
Last close 53.19 (bar of 2026-11-24), from 501 daily bars
Trend: vs 20d SMA 55.10 (-3.5%), 50d 57.55 (-7.6%), 200d 58.17 (-8.6%); 50d below 200d
Momentum: RSI(14) 39.9 | MACD -1.328 vs signal -1.112 (histogram -0.216)
Returns: 1d -0.7% | 5d -2.0% | 1m -5.9% | 3m -12.3%
52-week range: 50.62 - 61.44 (now 23.8% of the way up)
Volatility: ATR(14) 1.17 (2.2% of price) | annualised 20d 35.4%
Volume: 0.12x the 20-day average
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

<details><summary><b>What analysts and big funds say</b> — score +0.40</summary>

_Not available today._

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score +0.40</summary>

```text
Rolled up from the 5 largest holdings, 22.6% of the fund by weight  -- thin, so read this as a fact about that slice rather than the fund
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 1.31 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +58.8% above the current prices
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
Share count change: 1 week: +0.0% (0.00) over 7d | 1 month: +0.0% (0.00) over 31d
Shares outstanding: 1.42B | fund size: 75.43B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

## Sector and country funds

### US media and communication (XLC) · Sector or country — BULLISH, confidence 0.40

**Result:** ACCEPTED · 66 shares · submitted buy 66 XLC @ ~104.60, stop 99.77

**In the model's own words:**

> Analyst consensus is heavily bullish (90.6% buy, +35% price target) and the fund has recorded strong weekly inflows (+8.7%/$1.79B), supporting a bullish outlook. Fundamentals remain solid with modest valuation (P/E 15.9) and solid three‑year performance (+13.5%/yr). Technicals show the price under the 50‑ and 200‑day averages and low momentum, tempering the view, so a moderate bullish bias is appropriate.

**Main reasons it gave:**
- Weekly fund inflows +8.7% (+$1.79B) over 7 days
- Analyst buy rating 90.6% and weighted price target +35.1% above current price
- Fund fundamentals: P/E 15.87, 3‑year annualized return 13.5%, yield 1.4%
- Technical: price below 50‑day SMA (-3.5%) and 200‑day SMA (-6.7%), RSI 46.7, low volume

<details><summary><b>News</b> — score +0.20</summary>

- [SPDR通信服务ETF收涨3.57%，成交额9.1亿美元](http://www.bing.com/news/apiclick.aspx?ref=FexRss&aid=&tid=6b05a36b9fb94d0e9c64631d2c0ad863&url=https%3a%2f%2ffinance.sina.com.cn%2fstock%2fusstock%2fnotice%2f2026-11-24%2fdoc-inizupfk5214020.shtml&c=9161847666063526073&mkt=en-us)  
  <sub>新浪财经, 23h ago</sub>  
  11月24日，SPDR通信服务ETF（XLC）收涨3.57%，报103.6美元，成交额9.1亿美元，市值215.02亿美元。 声明：市场有风险，投资需谨慎。本文基于第三方数据库发布，不代表新浪财经观点，任何在本文出现的信息均只作为参考，不构成个人投资建议。如有出入请以实际公告为准。如有疑问，请联系biz@staff.sina.com.cn。
- [Meta está estancada en un rango de negociación. Los gráficos muestran dónde comprar.](http://www.bing.com/news/apiclick.aspx?ref=FexRss&aid=&tid=6b05a36b9fb94d0e9c64631d2c0ad863&url=https%3a%2f%2fwww.bolsamania.com%2fcapitalbolsa%2fnoticias%2fanalisis-tecnico%2fmeta-esta-estancada-en-un-rango-de-negociacion-los-graficos-muestran-donde-comprar--24260634.html&c=3221554469186242532&mkt=en-us)  
  <sub>Bolsamania, 30h ago</sub>  
  Puntos clave Meta lleva buena parte de los últimos dos años moviéndose entre 500 y 800 dólares. Tres directrices alcistas convergen cerca de una zona donde ya han aparecido compradores. Seis saltos de ...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.20</summary>

```text
US Treasury yields: 3-month 4.17% (+0.03 on the week) | 5-year 4.71% (-0.19 on the week) | 10-year 4.90% (-0.20 on the week) | 30-year 5.29% (-0.17 on the week)
Yield curve, 10-year minus 3-month: +0.73 points -- upward sloping (normal)
US dollar index: 103.81 (+0.32 on the week)
Volatility (VIX): 29.34 (+3.9 on the week) -- stressed
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.1% (2026-10-01) | jobless claims 203k (2026-11-14)
Policy and expectations: Fed target 4.00% | market expects 2.1% inflation over 10 years
Rate path: 2-year Treasury 4.63% vs Fed target 3.75-4.00% -- the bond market prices about 3 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score -0.20</summary>

```text
Last close 104.45 (bar of 2026-11-24), from 501 daily bars
Trend: vs 20d SMA 104.43 (+0.0%), 50d 108.20 (-3.5%), 200d 111.89 (-6.7%); 50d below 200d
Momentum: RSI(14) 46.7 | MACD -1.092 vs signal -1.016 (histogram -0.076)
Returns: 1d +0.8% | 5d -0.8% | 1m +0.6% | 3m -7.2%
52-week range: 99.90 - 120.08 (now 22.5% of the way up)
Volatility: ATR(14) 2.36 (2.3% of price) | annualised 20d 28.4%
Volume: 0.05x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.30</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score +0.30</summary>

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

<details><summary><b>What analysts and big funds say</b> — score +0.70</summary>

_Not available today._

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score +0.70</summary>

```text
Rolled up from the 5 largest holdings, 52.5% of the fund by weight
Ratings by weight: buy 90.6% | hold 9.4% | sell 0.0% (mean 1.54 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +35.1% above the current prices
Holdings read: META, GOOGL, GOOG, DIS, CMCSA
Recent rating changes among them:
  - META: 2026-10-22 UBS: main, Buy -> Buy
  - GOOGL: 2026-11-02 Wells Fargo: main, Overweight -> Overweight
  - GOOG: 2026-10-29 JP Morgan: main, Overweight -> Overweight
  - DIS: 2026-10-16 Citigroup: main, Buy -> Buy
  - CMCSA: 2026-10-26 Freedom Broker: main, Hold -> Hold
```

</details>

<details><summary><b>Buying and selling by company insiders</b> — score +0.80</summary>

_Not available today._

</details>

<details><summary><b>Who is positioned how</b> — score +0.80</summary>

_Not available today._

</details>

<details><summary><b>Money going into and out of this fund</b> — score +0.80</summary>

```text
Direction: money coming in (1 month)
Share count change: 1 week: +8.7% (1.79B) over 7d | 1 month: +2.3% (503.09M) over 31d
Shares outstanding: 214.54M | fund size: 22.41B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### US health care (XLV) · Sector or country — NEUTRAL, confidence 0.20

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Fund flows show strong net inflows and analysts are uniformly positive, but macro data show no surprise and technicals indicate modest bearish momentum with price below short‑term SMA; news is mixed with recent price decline and market sell‑off. Without a decisive macro catalyst or technical breakout, the overall stance is neutral.

**Main reasons it gave:**
- Share count up +6.6% weekly and +14.3% monthly (fund flows)
- Analyst consensus 100% buy with weighted price target +10.7% (analyst view)
- Price below 20‑day SMA, MACD negative, RSI 46.2 (technicals)
- VIX at 29.34, no policy surprise (macro)
- Recent -4.5% price move and sector‑wide sell‑off (news)

<details><summary><b>News</b> — score -0.10</summary>

- [State Street Health Care Select Sector SPDR ETF (XLV) stock price, news, quote and history](https://uk.finance.yahoo.com/quote/XLV/)  
  <sub>Yahoo Finance UK, 19 hours ago</sub>  
  State Street Health Care Select Sector SPDR ETF (XLV) · -4.50% · 0.08% · 19.70% · 15.90% · 16.05% · 35.40% · 623.10%. Key events. Baseline. Advanced...
- [Safe-Harbor ETFs: Shelter From the Storm](https://www.google.com/goto?url=CAEShAEBxCJF15DgnvPOF0wndiYj0yKtBB1Be25lCEQTjW6Vq3Scw2bl7fA-XFPpDBn4Rwqad-ZI3Q8utDPnhqV5IQu0S94Eb0ESTOL-RNZkbdsiAoY3XlzVMTCtKJa3nKS0OL-tlDpkjiCkiAOD4fFE8OJzfntsPDV9BtVKExLvFRbjaKJG1zQ&gsessionid=ameDd8bqUDy72pKJdx5kNgpgniXtkWVQzd2dzTFjT2M-O75uS5USCw)  
  <sub>ETF Database, 1 hour ago</sub>  
  Combining value, equal-weight, and quality ETFs protects portfolios during downturns without completely missing explosive growth recoveries.
- [These are the favorite stocks of healthcare hedge funds – Goldman (XLV:NYSEARCA)](https://www.google.com/goto?url=CAESogEBxCJF19z5A3Zo0VD6le4TqCVzUMRZJjc8KQ-9oE5Q7qM0K3uaYr_jlDvjzfLcKUMYGCPzKLAxPP8m0snb0MGQIwVtBIJtr0WECj7U3whJqVFhFaGmVAWThPkV7QsStO9UGyYSrEddrtpYZzP9p3qwcziNxMG4zzgbzd6Brw4gH5MIDxhK7mqccRedh7QewcvwxkiIEufmyVEPM-KOIlkyM9g&gsessionid=ameDd8bqUDy72pKJdx5kNgpgniXtkWVQzd2dzTFjT2M-O75uS5USCw)  
  <sub>Seeking Alpha, 23 hours ago</sub>  
  Goldman Sachs finds Revolution Medicines leads health care specialist hedge fund holdings, owned by 41% of 27 funds; Insmed follows at 38%.
- [What Are Wall Street Analysts' Target Price for Revvity Stock?](https://www.google.com/goto?url=CAESpQEBxCJF13bf13pBMM-QpTqLdE6pcoRiFw6owBt00lNVX3wyL6m_MAA82z2z0ztj-O3YxIsKI8E0NIZTHNte0vtVCr2mBHyZI7mIwnVMQ3xSgadcHPz8OGeE84FNeFdgTAmjUEKs2l_TQpuVQ6zDmraA1GBAO4hRZ-NgHifN3nxEO-W0OPkuNWaCUhoztfI5-3W27UZgXDUyz6YwDPcge_CtbRcO-W4&gsessionid=ameDd8bqUDy72pKJdx5kNgpgniXtkWVQzd2dzTFjT2M-O75uS5USCw)  
  <sub>Barchart.com, 3 hours ago</sub>  
  Although Revvity has lagged the broader market over the past year, Wall Street analysts maintain a cautiously optimistic outlook on the stock's future...
- [3 ETFs For Owning AbbVie As Its Research Push Widens The Choice](https://www.google.com/goto?url=CAESlwEBxCJF16oT6pjlR9-E8iHqaE9mpzI2ezUFs_MlxNLcQcgsUYCAwetSemxv1IEvKstbG413uUwWdUaLa6B6C8HltQ8my0goCKRpUV7YMAgpjTFbX2CbtDmbPcWH06xx52rJutagbxX5k5Bpx0wv1d5DVFdwDlFQWRh8n_mphIfi_kzagVepsW61gVFXPhmqbb4zcnQyhyb4&gsessionid=ameDd8bqUDy72pKJdx5kNgpgniXtkWVQzd2dzTFjT2M-O75uS5USCw)  
  <sub>Yahoo Finance, 20 hours ago</sub>  
  If you like AbbVie and its drug portfolio, buying the stock outright means your money rises and falls with its specific issues.
- [ValuEngine Weekly Market Commentary: Bear Market For Nasdaq-100 Headlines Historic Weekly Meltdown](https://www.google.com/goto?url=CAESyAEBxCJF13gc1cA7uC8MxrjCqFlbd_oMjPOVd_MBj2NRgCKjIE0UafJ7NYEZblEjxS3oAay070-Ux3GXVLKmSScprwBkalQAosw_XEqgusviD7PM3If6Fos2Hgo-krbwcbxG_yp4J4uC-kJCGXhdtlJme1VoeD-RkL-sPcJtHfbfKpCu650bL8r3UWe_qxZpY3-l5U5OeUjSLftvl1vlrWMT_XFX3gOpC8Rgzkh2LZeMbs7zu8_5xCaK1KoYVEnhdlkgSRE6tEkxzg&gsessionid=ameDd8bqUDy72pKJdx5kNgpgniXtkWVQzd2dzTFjT2M-O75uS5USCw)  
  <sub>Seeking Alpha, 9 hours ago</sub>  
  U.S. equity markets experienced a sharp and broad-based selloff this week, with all major ETFs and sector benchmarks posting significant declines.
- [State Street Industrial Select Sector SPDR ETF (XLI) stock price, news, quote and history](https://www.google.com/goto?url=CAESZAHEIkXXPGsB9Q772NyVUQ_IA6TkXclA4Gn2h36KsEIBLaINhAKlsFFFyEn0Dcr7oyt0T68Gt4msEV0HsfOOn6DJL-SwKiMOwxxweMFEG3sY__JGDWYlVgG-kC0OOEeyU7GVa20&gsessionid=ameDd8bqUDy72pKJdx5kNgpgniXtkWVQzd2dzTFjT2M-O75uS5USCw)  
  <sub>Yahoo Finance Singapore, 21 hours ago</sub>  
  Find the latest State Street Industrial Select Sector SPDR ETF (XLI) stock quote, history, news and other vital information to help you with your stock...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score -0.10</summary>

```text
US Treasury yields: 3-month 4.17% (+0.03 on the week) | 5-year 4.71% (-0.19 on the week) | 10-year 4.90% (-0.20 on the week) | 30-year 5.29% (-0.17 on the week)
Yield curve, 10-year minus 3-month: +0.73 points -- upward sloping (normal)
US dollar index: 103.81 (+0.32 on the week)
Volatility (VIX): 29.34 (+3.9 on the week) -- stressed
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.1% (2026-10-01) | jobless claims 203k (2026-11-14)
Policy and expectations: Fed target 4.00% | market expects 2.1% inflation over 10 years
Rate path: 2-year Treasury 4.63% vs Fed target 3.75-4.00% -- the bond market prices about 3 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score -0.10</summary>

```text
Last close 179.65 (bar of 2026-11-24), from 501 daily bars
Trend: vs 20d SMA 184.38 (-2.6%), 50d 176.98 (+1.5%), 200d 161.10 (+11.5%); 50d above 200d
Momentum: RSI(14) 46.2 | MACD 0.610 vs signal 2.132 (histogram -1.522)
Returns: 1d +0.1% | 5d -3.0% | 1m +0.2% | 3m +3.5%
52-week range: 142.84 - 189.66 (now 78.6% of the way up)
Volatility: ATR(14) 3.51 (2.0% of price) | annualised 20d 22.8%
Volume: 0.13x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.10</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score +0.10</summary>

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
Rolled up from the 5 largest holdings, 45.4% of the fund by weight
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 1.73 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +10.7% above the current prices
Holdings read: LLY, JNJ, ABBV, MRK, UNH
Recent rating changes among them:
  - LLY: 2026-11-09 Jefferies: main, Buy -> Buy
  - JNJ: 2026-10-16 Wells Fargo: main, Overweight -> Overweight
  - ABBV: 2026-11-02 UBS: main, Neutral -> Neutral
  - MRK: 2026-11-02 Freedom Broker: main, Hold -> Hold
  - UNH: 2026-10-27 Wells Fargo: main, Overweight -> Overweight
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
Share count change: 1 week: +6.6% (3.07B) over 7d | 1 month: +14.3% (6.22B) over 32d
Shares outstanding: 277.17M | fund size: 49.79B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Biotech (XBI) · Sector or country — NEUTRAL, confidence 0.12

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> The XBI biotech ETF shows slight bullish technical and flow signals, but sector news is mixed and there is no macro catalyst or decisive technical breakout, so we maintain a neutral stance.

**Main reasons it gave:**
- Biotech sector slid in November, indicating sector weakness (negative news)
- ETF price above 20‑day and 200‑day SMAs with 1‑day gain +3.8% (technical bullish)
- Share count rose +7.4% week and +14% month, indicating net inflows (insider bullish)
- Analyst consensus 75% buy, weighted price target +9.4% above price (analyst bullish)

<details><summary><b>News</b> — score -0.20</summary>

- [Biotech Loses Ground In November’s Market Slide — These 5 Stocks Bucked The Selloff As Lilly, AbbVie And Amgen Fell](https://finance.yahoo.com/healthcare/articles/biotech-loses-ground-november-market-064155115.html)  
  <sub>Yahoo Finance, 8 hours ago</sub>  
  BBIO gained 6% through Monday. Shares were already up about 4% that day when trading halted ahead of FDA approval for Welgemda, the first U.S. treatment for...
- [These are the favorite stocks of healthcare hedge funds – Goldman (XLV:NYSEARCA)](https://seekingalpha.com/news/4675698-these-are-the-favorite-stocks-of-healthcare-hedge-funds-goldman)  
  <sub>Seeking Alpha, 23 hours ago</sub>  
  Goldman Sachs finds Revolution Medicines leads health care specialist hedge fund holdings, owned by 41% of 27 funds; Insmed follows at 38%.
- [BA, NOC, LMT, KTOS Stocks Draw Bullish Call From Mizuho: Analyst Calls The Group ‘Underappreciated’ Defense Plays](https://www.google.com/goto?url=CAESzQEBxCJF166uUzEuQ84VtLgzMLSj_10suIhVezKiu79HZpKx_FC_JTy91v7t13yCi_6guEJK28cieXMOmTjWFcGazkBzP1qj_g8YyYScz3FXIilH1a_vSWpezKLmBU3-A76DAgnBV0BUzw7nHNzsbbTaUdn0i4NUoHFY2hI3c4hd7bgPgvnixCw5fpmdlrDOyiibMGqCikkefvyqx0Zzi2r_lEROw6wQ3KnaIkcS_R44dd5wAbEOalPmiSAgMyZepSOINSWnwT0C7qTMbHaW&gsessionid=CFlGqyDwzfwbfL1zSx1hlZgb7tpAdq_hBu_k8cWAYL7nfFq61ebOjA)  
  <sub>Stocktwits, 7 hours ago</sub>  
  Boeing (BA), Northrop Grumman (NOC), Lockheed Martin (LMT) and Kratos Defense (KTOS) stocks drew bullish attention from Mizuho, which sees the defense...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score -0.20</summary>

```text
US Treasury yields: 3-month 4.17% (+0.03 on the week) | 5-year 4.71% (-0.19 on the week) | 10-year 4.90% (-0.20 on the week) | 30-year 5.29% (-0.17 on the week)
Yield curve, 10-year minus 3-month: +0.73 points -- upward sloping (normal)
US dollar index: 103.81 (+0.32 on the week)
Volatility (VIX): 29.34 (+3.9 on the week) -- stressed
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.1% (2026-10-01) | jobless claims 203k (2026-11-14)
Policy and expectations: Fed target 4.00% | market expects 2.1% inflation over 10 years
Rate path: 2-year Treasury 4.63% vs Fed target 3.75-4.00% -- the bond market prices about 3 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.10</summary>

```text
Last close 152.78 (bar of 2026-11-24), from 501 daily bars
Trend: vs 20d SMA 151.42 (+0.9%), 50d 152.48 (+0.2%), 200d 143.69 (+6.3%); 50d above 200d
Momentum: RSI(14) 52.7 | MACD -1.851 vs signal -1.542 (histogram -0.310)
Returns: 1d +3.8% | 5d +5.2% | 1m +1.5% | 3m -9.3%
52-week range: 118.46 - 169.55 (now 67.2% of the way up)
Volatility: ATR(14) 5.22 (3.4% of price) | annualised 20d 45.0%
Volume: 0.23x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.15</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score +0.15</summary>

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
Rolled up from the 5 largest holdings, 9.5% of the fund by weight  -- thin, so read this as a fact about that slice rather than the fund
Ratings by weight: buy 75.0% | hold 25.0% | sell 0.0% (mean 2.06 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +9.4% above the current prices
Holdings read: MRNA, NTRA, HALO, TWST, BIIB
Recent rating changes among them:
  - MRNA: 2026-11-09 Goldman Sachs: main, Neutral -> Neutral
  - NTRA: 2026-11-09 Baird: main, Outperform -> Outperform
  - HALO: 2026-11-11 Morgan Stanley: down, Overweight -> Equal-Weight
  - TWST: 2026-10-13 TD Cowen: main, Buy -> Buy
  - BIIB: 2026-11-09 Piper Sandler: reit, Overweight -> Overweight
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
Share count change: 1 week: +7.4% (815.76M) over 7d | 1 month: +14.0% (1.46B) over 31d
Shares outstanding: 77.85M | fund size: 11.89B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### US shopping and leisure (XLY) · Sector or country — NEUTRAL, confidence 0.10

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> The fund faces a bearish backdrop from a broad sell‑off in US equity ETFs and mixed technical signals (price above longer SMAs but negative MACD and low volume), but bullish analyst coverage (100% buy with a +16.6% price target) and strong recent inflows (+6.7% share count in a week) offset the downside, leading to a neutral overall view.

**Main reasons it gave:**
- Broad selloff across US equity ETFs this week (Seeking Alpha)
- Technical mix: price above 50d/200d SMAs but MACD negative and low volume
- Analyst consensus 100% buy with +16.6% price target
- Strong inflows: share count up 6.7% week (+$1.47B)
- High market volatility (VIX 29.34) adds uncertainty

<details><summary><b>News</b> — score -0.40</summary>

- [BATT vs. LIT: Why 2 Battery ETFs Deliver Different Exposure](https://www.etftrends.com/thematic-investing-content-hub/batt-lit-battery-etfs-different-exposure/)  
  <sub>ETF Trends, 20 hours ago</sub>  
  Compare top battery ETFs. Discover how Amplify's BATT differs from Global X's LIT in diversification, fees, and portfolio fit.
- [ValuEngine Weekly Market Commentary: Bear Market For Nasdaq-100 Headlines Historic Weekly Meltdown](https://seekingalpha.com/article/4971298-valuengine-weekly-market-commentary-bear-market-for-nasdaq-100-headlines-historic-weekly-meltdown)  
  <sub>Seeking Alpha, 9 hours ago</sub>  
  U.S. equity markets experienced a sharp and broad-based selloff this week, with all major ETFs and sector benchmarks posting significant declines.
- [State Street Industrial Select Sector SPDR ETF (XLI) stock price, news, quote and history](https://www.google.com/goto?url=CAESZAHEIkXXDfdbx1-99l-TcP_jOfUdojMPPWHfXEn5_WMz8vLcTKXmxCfWkOU-0njEDQw2tbxqvPbmHszsUvgTeKL5IIsmgQMADN1h2uYizOmQO98vEwPxDZOGMzz1Sew4mPmNn98&gsessionid=-CnH3OsayocrqsbAwZsBJ-dYLuFkR4PPdiuWhwCqnyi25MwhoyK5uQ)  
  <sub>Yahoo Finance Singapore, 21 hours ago</sub>  
  Find the latest State Street Industrial Select Sector SPDR ETF (XLI) stock quote, history, news and other vital information to help you with your stock...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score -0.40</summary>

```text
US Treasury yields: 3-month 4.17% (+0.03 on the week) | 5-year 4.71% (-0.19 on the week) | 10-year 4.90% (-0.20 on the week) | 30-year 5.29% (-0.17 on the week)
Yield curve, 10-year minus 3-month: +0.73 points -- upward sloping (normal)
US dollar index: 103.81 (+0.32 on the week)
Volatility (VIX): 29.34 (+3.9 on the week) -- stressed
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.1% (2026-10-01) | jobless claims 203k (2026-11-14)
Policy and expectations: Fed target 4.00% | market expects 2.1% inflation over 10 years
Rate path: 2-year Treasury 4.63% vs Fed target 3.75-4.00% -- the bond market prices about 3 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score -0.20</summary>

```text
Last close 117.42 (bar of 2026-11-24), from 501 daily bars
Trend: vs 20d SMA 118.03 (-0.5%), 50d 114.37 (+2.7%), 200d 115.34 (+1.8%); 50d below 200d
Momentum: RSI(14) 51.4 | MACD 0.473 vs signal 1.035 (histogram -0.562)
Returns: 1d +0.4% | 5d +0.3% | 1m +2.8% | 3m +0.2%
52-week range: 105.66 - 124.52 (now 62.4% of the way up)
Volatility: ATR(14) 2.67 (2.3% of price) | annualised 20d 34.1%
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

<details><summary><b>What analysts and big funds say</b> — score +0.50</summary>

_Not available today._

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score +0.50</summary>

```text
Rolled up from the 5 largest holdings, 54.1% of the fund by weight
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 1.80 on a 1=strong buy to 5=strong sell scale)
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

<details><summary><b>Buying and selling by company insiders</b> — score +0.70</summary>

_Not available today._

</details>

<details><summary><b>Who is positioned how</b> — score +0.70</summary>

_Not available today._

</details>

<details><summary><b>Money going into and out of this fund</b> — score +0.70</summary>

```text
Direction: money coming in (1 month)
Share count change: 1 week: +6.7% (1.47B) over 7d | 1 month: +8.2% (1.77B) over 32d
Shares outstanding: 199.21M | fund size: 23.39B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Argentina (ARGT) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Neutral overall as there is no macro surprise or decisive technical break; bullish analyst coverage and strong inflows are offset by bearish technicals and modest fundamentals.

**Main reasons it gave:**
- Technicals: price 67.71 far below 20‑day (73.58), 50‑day (82.36) and 200‑day (89.95) SMAs
- Fund flows: share count up 13.5% in the past week, indicating strong inflows
- Analyst view: 100% buy rating on top holdings with a weighted price target +73.8% above current
- Macro: no rate or policy surprise; yields stable and VIX elevated but unchanged

<details><summary><b>News</b> — score +0.00</summary>

_No news found for this one today._

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.17% (+0.03 on the week) | 5-year 4.71% (-0.19 on the week) | 10-year 4.90% (-0.20 on the week) | 30-year 5.29% (-0.17 on the week)
Yield curve, 10-year minus 3-month: +0.73 points -- upward sloping (normal)
US dollar index: 103.81 (+0.32 on the week)
Volatility (VIX): 29.34 (+3.9 on the week) -- stressed
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.1% (2026-10-01) | jobless claims 203k (2026-11-14)
Policy and expectations: Fed target 4.00% | market expects 2.1% inflation over 10 years
Rate path: 2-year Treasury 4.63% vs Fed target 3.75-4.00% -- the bond market prices about 3 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score -0.20</summary>

```text
Last close 67.71 (bar of 2026-11-24), from 501 daily bars
Trend: vs 20d SMA 73.58 (-8.0%), 50d 82.36 (-17.8%), 200d 89.95 (-24.7%); 50d below 200d
Momentum: RSI(14) 29.4 | MACD -4.717 vs signal -4.378 (histogram -0.340)
Returns: 1d +0.5% | 5d -4.3% | 1m -18.2% | 3m -28.3%
52-week range: 64.56 - 102.94 (now 8.2% of the way up)
Volatility: ATR(14) 2.18 (3.2% of price) | annualised 20d 37.4%
Volume: 0.14x the 20-day average
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
Three-year record: +12.6% a year | beta to the market 0.44
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

<details><summary><b>What analysts and big funds say</b> — score +0.80</summary>

_Not available today._

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score +0.80</summary>

```text
Rolled up from the 5 largest holdings, 51.1% of the fund by weight
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 1.61 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +73.8% above the current prices
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
Share count change: 1 week: +13.5% (76.62M) over 7d | 1 month: +13.8% (78.32M) over 31d
Shares outstanding: 9.54M | fund size: 645.85M
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Israel (EIS) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:** no explanation. It wrote only “NEUTRAL”, so the main reasons below are all it gave.

**Main reasons it gave:**
- Technical: price 104.66 below 20‑day SMA (111.16), 50‑day SMA (117.36) and 200‑day SMA (122.40)
- Technical: RSI 35.4 (oversold) and MACD negative, volume 0.06× 20‑day average
- Macro: VIX 29.34 (+3.9 on week) indicating stressed market conditions
- Analyst: 100% buy rating on top holdings with +29.5% price target (covers 39.6% of fund)
- Fund flows: share count flat over week and month (0% change), indicating no net demand

<details><summary><b>News</b> — score +0.00</summary>

_No news found for this one today._

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.17% (+0.03 on the week) | 5-year 4.71% (-0.19 on the week) | 10-year 4.90% (-0.20 on the week) | 30-year 5.29% (-0.17 on the week)
Yield curve, 10-year minus 3-month: +0.73 points -- upward sloping (normal)
US dollar index: 103.81 (+0.32 on the week)
Volatility (VIX): 29.34 (+3.9 on the week) -- stressed
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.1% (2026-10-01) | jobless claims 203k (2026-11-14)
Policy and expectations: Fed target 4.00% | market expects 2.1% inflation over 10 years
Rate path: 2-year Treasury 4.63% vs Fed target 3.75-4.00% -- the bond market prices about 3 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 104.66 (bar of 2026-11-24), from 501 daily bars
Trend: vs 20d SMA 111.16 (-5.8%), 50d 117.36 (-10.8%), 200d 122.40 (-14.5%); 50d below 200d
Momentum: RSI(14) 35.4 | MACD -3.758 vs signal -3.034 (histogram -0.724)
Returns: 1d -0.6% | 5d -4.5% | 1m -14.3% | 3m -15.4%
52-week range: 101.51 - 137.69 (now 8.7% of the way up)
Volatility: ATR(14) 2.59 (2.5% of price) | annualised 20d 39.8%
Volume: 0.06x the 20-day average
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
Three-year record: +25.8% a year | beta to the market 0.98
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
Weighted price target: +29.5% above the current prices
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
Share count change: 1 week: +0.0% (0.00) over 7d | 1 month: +0.0% (0.00) over 31d
Shares outstanding: 2.55M | fund size: 266.88M
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Poland (EPOL) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> The fund shows mixed signals: strong inflows and a bullish analyst view suggest upside, while technicals are bearish and macro data show no surprise catalyst. Overall, the evidence does not justify a directional tilt.

**Main reasons it gave:**
- Fund flows: +10.3% share count increase week-on-week, +36% month-on-month
- Analyst view: 57.7% buy rating, weighted price target +13.8% above current price
- Technicals: price below 20‑day SMA (‑4.7%), RSI 38.9, MACD negative
- Macro: yields down slightly (10‑yr −0.20% week), VIX up to 29.34, no surprise data
- Fundamentals: P/E 13.39, three‑year return +27.8% per year, yield 3.4%

<details><summary><b>News</b> — score +0.00</summary>

_No news found for this one today._

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.17% (+0.03 on the week) | 5-year 4.71% (-0.19 on the week) | 10-year 4.90% (-0.20 on the week) | 30-year 5.29% (-0.17 on the week)
Yield curve, 10-year minus 3-month: +0.73 points -- upward sloping (normal)
US dollar index: 103.81 (+0.32 on the week)
Volatility (VIX): 29.34 (+3.9 on the week) -- stressed
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.1% (2026-10-01) | jobless claims 203k (2026-11-14)
Policy and expectations: Fed target 4.00% | market expects 2.1% inflation over 10 years
Rate path: 2-year Treasury 4.63% vs Fed target 3.75-4.00% -- the bond market prices about 3 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score -0.30</summary>

```text
Last close 41.03 (bar of 2026-11-24), from 501 daily bars
Trend: vs 20d SMA 43.06 (-4.7%), 50d 43.77 (-6.2%), 200d 40.83 (+0.5%); 50d above 200d
Momentum: RSI(14) 38.9 | MACD -0.682 vs signal -0.398 (histogram -0.284)
Returns: 1d -1.4% | 5d -4.9% | 1m -5.9% | 3m -8.3%
52-week range: 32.94 - 45.76 (now 63.1% of the way up)
Volatility: ATR(14) 0.87 (2.1% of price) | annualised 20d 33.4%
Volume: 0.03x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.40</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score +0.40</summary>

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

<details><summary><b>What analysts and big funds say</b> — score +0.40</summary>

_Not available today._

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score +0.40</summary>

```text
Rolled up from the 5 largest holdings, 46.6% of the fund by weight
Ratings by weight: buy 57.7% | hold 42.3% | sell 0.0% (mean 2.19 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +13.8% above the current prices
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
Share count change: 1 week: +10.3% (98.66M) over 7d | 1 month: +36.0% (279.95M) over 31d
Shares outstanding: 25.76M | fund size: 1.06B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Australia (EWA) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:** no explanation. It wrote only “NEUTRAL”, so the main reasons below are all it gave.

**Main reasons it gave:**
- US Treasury yields up modestly, no rate surprise
- Technicals: price below 20‑day, 50‑day, 200‑day SMAs, RSI 36, low volume
- Analyst view: 57.4% hold, 42.6% sell, weighted price target -4.4% vs current price
- Fund flows: weekly share count +8.8%, monthly +12.7% indicating strong inflows

<details><summary><b>News</b> — score +0.00</summary>

- [Australia’s Mid-Year Budget Outlook: Why Nominal GDP and Revenue Forecasts Matter](https://kalkine.com.au/news/economic-news/australias-mid-year-budget-outlook-why-nominal-gdp-and-revenue-forecasts-matter)  
  <sub>Kalkine, 9 hours ago</sub>  
  You are reading a free article with opinions that may differ from the recommendation given by Kalkine in its paid research reports.
- [Australian Business Activity: What Do Labour and Investment Data Signal for Year-End Growth?](https://kalkine.com.au/news/economic-news/australian-business-activity-what-do-labour-and-investment-data-signal-for-year-end-growth)  
  <sub>Kalkine, 9 hours ago</sub>  
  You are reading a free article with opinions that may differ from the recommendation given by Kalkine in its paid research reports.
- [iShares MSCI Singapore ETF (EWS) Stock Price, News, Quote & History](https://www.google.com/goto?url=CAESZAHEIkXXO9oXRgOt8kqU4EG96H3nS6m_3lK9ZM9fQoP2HQ1_L8CNUhyxbRF9POVfHLodMwB_fWOY_G33lNuXJFV8hC1-yS3fg2HkW1wQQZUgM2vUC6DlaQccLYIMi8CHimxZP3g&gsessionid=2gtX0vOuqdiibYlwKZ3y5UYn4VMNaJyq_dEj9_8ooBRxSLMgkGoHww)  
  <sub>Yahoo! Finance Canada, 15 hours ago</sub>  
  Find the latest iShares MSCI Singapore ETF (EWS) stock quote, history, news and other vital information to help you with your stock trading and investing.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.17% (+0.03 on the week) | 5-year 4.71% (-0.19 on the week) | 10-year 4.90% (-0.20 on the week) | 30-year 5.29% (-0.17 on the week)
Yield curve, 10-year minus 3-month: +0.73 points -- upward sloping (normal)
US dollar index: 103.81 (+0.32 on the week)
Volatility (VIX): 29.34 (+3.9 on the week) -- stressed
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.1% (2026-10-01) | jobless claims 203k (2026-11-14)
Policy and expectations: Fed target 4.00% | market expects 2.1% inflation over 10 years
Rate path: 2-year Treasury 4.63% vs Fed target 3.75-4.00% -- the bond market prices about 3 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score -0.20</summary>

```text
Last close 27.42 (bar of 2026-11-24), from 501 daily bars
Trend: vs 20d SMA 28.77 (-4.7%), 50d 28.72 (-4.5%), 200d 28.98 (-5.4%); 50d below 200d
Momentum: RSI(14) 36.4 | MACD -0.477 vs signal -0.233 (histogram -0.245)
Returns: 1d +0.8% | 5d -2.6% | 1m -6.0% | 3m -9.0%
52-week range: 25.44 - 30.43 (now 39.8% of the way up)
Volatility: ATR(14) 0.41 (1.5% of price) | annualised 20d 21.0%
Volume: 0.10x the 20-day average
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

<details><summary><b>What analysts and big funds say</b> — score -0.35</summary>

_Not available today._

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score -0.35</summary>

```text
Rolled up from the 5 largest holdings, 46.5% of the fund by weight
Ratings by weight: buy 0.0% | hold 57.4% | sell 42.6% (mean 3.45 on a 1=strong buy to 5=strong sell scale)
Weighted price target: -4.4% above the current prices
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
Share count change: 1 week: +8.8% (104.20M) over 7d | 1 month: +12.7% (144.39M) over 32d
Shares outstanding: 46.74M | fund size: 1.28B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Canada (EWC) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> The fund shows a moderate bullish analyst view (87.2% buy rating, +14% price target) and strong recent inflows (+9.5% weekly, +20.7% monthly), but technicals are bearish (price below 20‑, 50‑, and 200‑day SMAs, negative MACD, low volume) and macro conditions are risk‑off (VIX 29.34, expectations of further Fed hikes). No material policy surprise or decisive technical break occurred, so the overall stance remains neutral.

**Main reasons it gave:**
- Analyst coverage of top holdings (29.5% weight) shows 87.2% buy rating and +14% price target
- Fund flows: share count up 9.5% weekly and 20.7% monthly, indicating strong inflows
- Technical indicators: price below 20‑day, 50‑day, and 200‑day SMAs; RSI 36.8; MACD negative; volume 0.07× 20‑day average
- Macro environment: VIX 29.34 (high) and market expects further Fed hikes, indicating risk‑off sentiment

<details><summary><b>News</b> — score +0.00</summary>

- [World Markets Watchlist: November 23, 2026](https://etfdb.com/china-insights-content-hub/world-markets-watchlist-november-23-2026/)  
  <sub>ETF Database, 16 hours ago</sub>  
  Our global markets watchlist tracks nine prominent indexes from economies around the world. The list includes the S&P 500 from the U.S..

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.17% (+0.03 on the week) | 5-year 4.71% (-0.19 on the week) | 10-year 4.90% (-0.20 on the week) | 30-year 5.29% (-0.17 on the week)
Yield curve, 10-year minus 3-month: +0.73 points -- upward sloping (normal)
US dollar index: 103.81 (+0.32 on the week)
Volatility (VIX): 29.34 (+3.9 on the week) -- stressed
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.1% (2026-10-01) | jobless claims 203k (2026-11-14)
Policy and expectations: Fed target 4.00% | market expects 2.1% inflation over 10 years
Rate path: 2-year Treasury 4.63% vs Fed target 3.75-4.00% -- the bond market prices about 3 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score -0.30</summary>

```text
Last close 56.55 (bar of 2026-11-24), from 501 daily bars
Trend: vs 20d SMA 59.39 (-4.8%), 50d 59.61 (-5.1%), 200d 58.63 (-3.5%); 50d above 200d
Momentum: RSI(14) 36.8 | MACD -1.074 vs signal -0.575 (histogram -0.498)
Returns: 1d +0.6% | 5d -3.6% | 1m -7.1% | 3m -9.1%
52-week range: 51.05 - 62.64 (now 47.5% of the way up)
Volatility: ATR(14) 0.98 (1.7% of price) | annualised 20d 24.3%
Volume: 0.07x the 20-day average
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
Three-year record: +18.9% a year | beta to the market 0.73
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

<details><summary><b>What analysts and big funds say</b> — score +0.30</summary>

_Not available today._

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score +0.30</summary>

```text
Rolled up from the 5 largest holdings, 29.5% of the fund by weight
Ratings by weight: buy 87.2% | hold 12.8% | sell 0.0% (mean 2.20 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +14.0% above the current prices
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
Share count change: 1 week: +9.5% (675.03M) over 7d | 1 month: +20.7% (1.34B) over 32d
Shares outstanding: 138.17M | fund size: 7.81B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Sweden (EWD) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:** no explanation. It wrote only “Neutral”, so the main reasons below are all it gave.

**Main reasons it gave:**
- Fund flows: share count up 22.3% over the past month
- Analyst consensus: 100% buy with weighted price target +12% above current price
- Technical indicators: price below 20‑day, 50‑day, and 200‑day SMAs; RSI 42.8; MACD negative
- Macro environment: VIX up 3.9 points to 29.34, indicating stressed market conditions

<details><summary><b>News</b> — score +0.00</summary>

_No news found for this one today._

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.17% (+0.03 on the week) | 5-year 4.71% (-0.19 on the week) | 10-year 4.90% (-0.20 on the week) | 30-year 5.29% (-0.17 on the week)
Yield curve, 10-year minus 3-month: +0.73 points -- upward sloping (normal)
US dollar index: 103.81 (+0.32 on the week)
Volatility (VIX): 29.34 (+3.9 on the week) -- stressed
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.1% (2026-10-01) | jobless claims 203k (2026-11-14)
Policy and expectations: Fed target 4.00% | market expects 2.1% inflation over 10 years
Rate path: 2-year Treasury 4.63% vs Fed target 3.75-4.00% -- the bond market prices about 3 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score -0.40</summary>

```text
Last close 50.12 (bar of 2026-11-24), from 501 daily bars
Trend: vs 20d SMA 51.85 (-3.3%), 50d 51.22 (-2.1%), 200d 51.47 (-2.6%); 50d below 200d
Momentum: RSI(14) 42.8 | MACD -0.412 vs signal -0.036 (histogram -0.376)
Returns: 1d +0.3% | 5d -2.2% | 1m -0.9% | 3m -7.1%
52-week range: 46.26 - 54.72 (now 45.6% of the way up)
Volatility: ATR(14) 0.86 (1.7% of price) | annualised 20d 27.8%
Volume: 0.01x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.40</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score +0.40</summary>

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
Rolled up from the 5 largest holdings, 33.9% of the fund by weight
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 1.99 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +12.0% above the current prices
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
Share count change: 1 week: +8.5% (89.55M) over 7d | 1 month: +22.3% (207.88M) over 32d
Shares outstanding: 22.73M | fund size: 1.14B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Germany (EWG) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Neutral overall: bullish analyst view (+0.45) is offset by flat fund flows (0.0) and neutral fundamentals (0.0), while technicals are bearish and macro environment shows high yields and stressed volatility, providing no clear catalyst.

**Main reasons it gave:**
- Analyst coverage of top holdings: 78% buy, price target +24.9% above current
- Fund flows flat: 0% share count change over 1 week and 1 month
- Technical indicators: price below 20d, 50d, 200d SMAs; RSI 39.5; MACD negative
- Macro environment: high Treasury yields and VIX 29.34 indicating stressed market

<details><summary><b>News</b> — score +0.00</summary>

_No news found for this one today._

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.17% (+0.03 on the week) | 5-year 4.71% (-0.19 on the week) | 10-year 4.90% (-0.20 on the week) | 30-year 5.29% (-0.17 on the week)
Yield curve, 10-year minus 3-month: +0.73 points -- upward sloping (normal)
US dollar index: 103.81 (+0.32 on the week)
Volatility (VIX): 29.34 (+3.9 on the week) -- stressed
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.1% (2026-10-01) | jobless claims 203k (2026-11-14)
Policy and expectations: Fed target 4.00% | market expects 2.1% inflation over 10 years
Rate path: 2-year Treasury 4.63% vs Fed target 3.75-4.00% -- the bond market prices about 3 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score -0.30</summary>

```text
Last close 40.11 (bar of 2026-11-24), from 501 daily bars
Trend: vs 20d SMA 41.87 (-4.2%), 50d 41.68 (-3.8%), 200d 42.10 (-4.7%); 50d below 200d
Momentum: RSI(14) 39.5 | MACD -0.454 vs signal -0.130 (histogram -0.323)
Returns: 1d +0.1% | 5d -3.7% | 1m -2.7% | 3m -9.5%
52-week range: 38.08 - 44.59 (now 31.2% of the way up)
Volatility: ATR(14) 0.71 (1.8% of price) | annualised 20d 28.4%
Volume: 0.03x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.00</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score +0.00</summary>

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
Rolled up from the 5 largest holdings, 45.1% of the fund by weight
Ratings by weight: buy 78.0% | hold 22.0% | sell 0.0% (mean 1.99 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +24.9% above the current prices
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
Share count change: 1 week: +0.0% (0.00) over 7d | 1 month: +0.0% (0.00) over 31d
Shares outstanding: 79.50M | fund size: 3.19B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Italy (EWI) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Neutral overall – no macro surprise or decisive technical break, but mixed signals from fundamentals, analyst view and flows.

**Main reasons it gave:**
- Technical downtrend: price below 20‑day, 50‑day and 200‑day SMAs (56.85, 57.38, 58.26), RSI 40.1, MACD negative
- Strong inflows: share count up 8.3% in the past week (92.86M)
- Analyst coverage bullish: 90.8% buy rating, price target +21.8% above current price
- Macro environment unchanged: yields stable, no policy surprise, VIX up 3.9 points

<details><summary><b>News</b> — score +0.00</summary>

- [iShares MSCI Italy Capped ETF (EWI.MX) Seasonal returns chart](https://uk.finance.yahoo.com/quote/EWI.MX/seasonality/)  
  <sub>Yahoo Finance UK, 22 hours ago</sub>  
  iShares MSCI Italy Capped ETF (EWI.MX) seasonal returns chart provides the mean and median returns by month to inform your investment strategy.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.17% (+0.03 on the week) | 5-year 4.71% (-0.19 on the week) | 10-year 4.90% (-0.20 on the week) | 30-year 5.29% (-0.17 on the week)
Yield curve, 10-year minus 3-month: +0.73 points -- upward sloping (normal)
US dollar index: 103.81 (+0.32 on the week)
Volatility (VIX): 29.34 (+3.9 on the week) -- stressed
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.1% (2026-10-01) | jobless claims 203k (2026-11-14)
Policy and expectations: Fed target 4.00% | market expects 2.1% inflation over 10 years
Rate path: 2-year Treasury 4.63% vs Fed target 3.75-4.00% -- the bond market prices about 3 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score -0.40</summary>

```text
Last close 54.85 (bar of 2026-11-24), from 501 daily bars
Trend: vs 20d SMA 56.85 (-3.5%), 50d 57.38 (-4.4%), 200d 58.26 (-5.9%); 50d below 200d
Momentum: RSI(14) 40.1 | MACD -0.582 vs signal -0.274 (histogram -0.309)
Returns: 1d -0.4% | 5d -3.8% | 1m -1.0% | 3m -12.9%
52-week range: 50.70 - 63.35 (now 32.8% of the way up)
Volatility: ATR(14) 0.95 (1.7% of price) | annualised 20d 30.7%
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
Three-year record: +22.0% a year | beta to the market 0.92
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
Ratings by weight: buy 90.8% | hold 9.2% | sell 0.0% (mean 2.14 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +21.8% above the current prices
Holdings read: UCG.MI, ISP.MI, ENEL.MI, ENI.MI, G.MI
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
Share count change: 1 week: +8.3% (92.86M) over 7d | 1 month: +6.3% (72.44M) over 32d
Shares outstanding: 22.15M | fund size: 1.21B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Japan (EWJ) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:** no explanation. It wrote only “NEUTRAL”, so the main reasons below are all it gave.

**Main reasons it gave:**
- Fund flows: +9.2% share count increase over 1 week (2.06B)
- Technicals: price below 20‑day, 50‑day, 200‑day SMAs, RSI 39.1, low volume
- Macro: VIX up 3.9 points to 29.34, indicating stress; yields fell slightly
- Analyst view: thin coverage (17.2% weight) all buy, price target +30% above current
- News: Asian markets rally on AI surge, Nikkei up 4%

<details><summary><b>News</b> — score +0.00</summary>

- [iShares China Large-Cap ETF (FXI) Stock Price, News, Quote & History](https://ca.finance.yahoo.com/quote/FXI/)  
  <sub>Yahoo! Finance Canada, 24 hours ago</sub>  
  Find the latest iShares China Large-Cap ETF (FXI) stock quote, history, news and other vital information to help you with your stock trading and investing.
- [Top Tokenized ETFs by Market Cap](https://www.coingecko.com/en/etfs)  
  <sub>Coingecko, 13 hours ago</sub>  
  Discover the top ETFs (exchange-traded funds) by tokenized market cap. Track ETF prices alongside their tokenized prices, market cap,...
- [Asian markets rally on Wall Street AI surge; KOSPI jumps 7%, Nikkei climbs 4%](https://www.google.com/goto?url=CAESwAEBxCJF1xPBL8DDbH4DvjwDKUSNKiwJKXC8d_vhKm23oWlQ7HVSu2RDuUs1iZHasPuhWcQvjxnq6ShkO-tXZYw7xLoDchyIVZ4pDuBTRgifzWFYkl7fqMCmqsgLagmIVm-hP_QSHA2dMaZhO70QNSmYfY7SqvNOjwX82NC_b33SG5NGes-sppF3qB1D8E3IS6Y2KsHVZgD1i0NIAKTJBGnJ6bH-7kPFKzett_RQAy3ARuv8MLDWHwTxd_-Hv8beYWA&gsessionid=Deu_xmKuIh4WaGsrEs4pgujO9vulIhPkBimhPphE9zNaUGV0neVc7w)  
  <sub>Seeking Alpha, 9 hours ago</sub>  
  Asian equity markets traded mostly higher on Tuesday, buoyed by an overnight Wall Street rally led by a sharp rebound in AI stocks, including a more than...
- [Nikkei 225 Index jumps as tech stocks rebound: is this the end of the bear market?](https://www.google.com/goto?url=CAEStAEBxCJF18vSArw55CeWBslLqn08mSufz3Y9ru3mOO1H_TJDaBEcSdyR11fo3qtvPGQHU1ticY20-JI3Eqp7tQbMA3l-21FzKLGKqL_84oo575VpvqI3gK-PA0QQH3-DWxUC7TIqNHwOAqYLc2J0OdDfAawJ-ze2sED9nPcYW61E9VmWV97Wdp_O1ZXW9DIJlFEpKU4zln2r7_80Zka8uruInA5eWRqSeSpA563wi_aXivrAfYI&gsessionid=Deu_xmKuIh4WaGsrEs4pgujO9vulIhPkBimhPphE9zNaUGV0neVc7w)  
  <sub>Invezz, 10 hours ago</sub>  
  The Nikkei 225 Index bounced back on Tuesday, driven by the ongoing global stock market rebound after Jensen Huang's return to Nvidia.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.17% (+0.03 on the week) | 5-year 4.71% (-0.19 on the week) | 10-year 4.90% (-0.20 on the week) | 30-year 5.29% (-0.17 on the week)
Yield curve, 10-year minus 3-month: +0.73 points -- upward sloping (normal)
US dollar index: 103.81 (+0.32 on the week)
Volatility (VIX): 29.34 (+3.9 on the week) -- stressed
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.1% (2026-10-01) | jobless claims 203k (2026-11-14)
Policy and expectations: Fed target 4.00% | market expects 2.1% inflation over 10 years
Rate path: 2-year Treasury 4.63% vs Fed target 3.75-4.00% -- the bond market prices about 3 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score -0.20</summary>

```text
Last close 87.07 (bar of 2026-11-24), from 501 daily bars
Trend: vs 20d SMA 90.34 (-3.6%), 50d 94.21 (-7.6%), 200d 92.09 (-5.5%); 50d above 200d
Momentum: RSI(14) 39.1 | MACD -2.241 vs signal -1.895 (histogram -0.346)
Returns: 1d +0.2% | 5d -1.8% | 1m -7.6% | 3m -8.8%
52-week range: 79.74 - 99.32 (now 37.4% of the way up)
Volatility: ATR(14) 1.88 (2.2% of price) | annualised 20d 36.4%
Volume: 0.10x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.45</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score +0.45</summary>

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
Rolled up from the 5 largest holdings, 17.2% of the fund by weight  -- thin, so read this as a fact about that slice rather than the fund
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 1.68 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +30.0% above the current prices
Holdings read: 8306.T, 7203.T, 6857.T, 6098.T, 8316.T
Recent rating changes among them: none reported
```

</details>

<details><summary><b>Buying and selling by company insiders</b> — score +0.35</summary>

_Not available today._

</details>

<details><summary><b>Who is positioned how</b> — score +0.35</summary>

```text
Contract: NIKKEI STOCK AVERAGE YEN DENOM - CHICAGO MERCANTILE EXCHANGE (positions as of 2026-11-17, published the following Friday)
Large speculators: net long 3.6% of open interest (28,271 contracts)
Change on the week: +1.4% of open interest
Crowding: 40% percentile over 52 weeks -- within its normal range
Read this as crowding, not as a forecast: an extreme is as often the end of a move as the middle of one.
```

</details>

<details><summary><b>Money going into and out of this fund</b> — score +0.35</summary>

```text
Direction: money coming in (1 month)
Share count change: 1 week: +9.2% (2.06B) over 7d | 1 month: +14.0% (3.00B) over 32d
Shares outstanding: 280.57M | fund size: 24.43B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Switzerland (EWL) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Neutral overall: analyst view modestly bullish, technicals mixed with slight downside momentum, fund flows flat, macro volatility elevated but no clear catalyst.

**Main reasons it gave:**
- Analyst view: 64.8% buy, weighted price target +3.2% above current price
- Technicals: price 1.6% below 20‑day SMA, MACD histogram -0.386, volume 0.10× 20‑day average
- Fund flows: flat, share count unchanged over past week and month
- Macro: VIX up 3.9 points to 29.34, indicating heightened market volatility

<details><summary><b>News</b> — score +0.00</summary>

_No news found for this one today._

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.17% (+0.03 on the week) | 5-year 4.71% (-0.19 on the week) | 10-year 4.90% (-0.20 on the week) | 30-year 5.29% (-0.17 on the week)
Yield curve, 10-year minus 3-month: +0.73 points -- upward sloping (normal)
US dollar index: 103.81 (+0.32 on the week)
Volatility (VIX): 29.34 (+3.9 on the week) -- stressed
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.1% (2026-10-01) | jobless claims 203k (2026-11-14)
Policy and expectations: Fed target 4.00% | market expects 2.1% inflation over 10 years
Rate path: 2-year Treasury 4.63% vs Fed target 3.75-4.00% -- the bond market prices about 3 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 63.28 (bar of 2026-11-24), from 501 daily bars
Trend: vs 20d SMA 64.30 (-1.6%), 50d 62.20 (+1.7%), 200d 62.02 (+2.0%); 50d above 200d
Momentum: RSI(14) 48.8 | MACD 0.083 vs signal 0.469 (histogram -0.386)
Returns: 1d +0.7% | 5d -1.1% | 1m +0.6% | 3m -1.4%
52-week range: 56.31 - 66.56 (now 68.0% of the way up)
Volatility: ATR(14) 0.82 (1.3% of price) | annualised 20d 21.3%
Volume: 0.10x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.20</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score +0.20</summary>

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
Share count change: 1 week: +0.0% (0.00) over 7d | 1 month: +0.0% (0.00) over 31d
Shares outstanding: 28.62M | fund size: 1.81B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Netherlands (EWN) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> The ETF shows a bearish technical picture – price is well below its 20‑, 50‑ and 200‑day averages, RSI is low and MACD is negative – but fundamentals are solid with moderate valuation metrics, a respectable 3‑year annualized return and a 4.4% yield. Analysts are strongly bullish on the largest holdings, yet fund flows are flat and there is no fresh news or macro surprise to tip the overall view. Given the mixed signals and absent catalyst, the prudent stance is neutral.

**Main reasons it gave:**
- Price below 20‑day, 50‑day, and 200‑day SMAs with negative MACD
- RSI at 38.2 indicating weak momentum
- Analyst consensus 100% buy with weighted price target +69.9%
- Fund flows flat over past month, indicating no net demand
- No macro surprise: yields stable, VIX elevated but no policy shift

<details><summary><b>News</b> — score +0.00</summary>

_No news found for this one today._

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.17% (+0.03 on the week) | 5-year 4.71% (-0.19 on the week) | 10-year 4.90% (-0.20 on the week) | 30-year 5.29% (-0.17 on the week)
Yield curve, 10-year minus 3-month: +0.73 points -- upward sloping (normal)
US dollar index: 103.81 (+0.32 on the week)
Volatility (VIX): 29.34 (+3.9 on the week) -- stressed
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.1% (2026-10-01) | jobless claims 203k (2026-11-14)
Policy and expectations: Fed target 4.00% | market expects 2.1% inflation over 10 years
Rate path: 2-year Treasury 4.63% vs Fed target 3.75-4.00% -- the bond market prices about 3 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score -0.45</summary>

```text
Last close 60.55 (bar of 2026-11-24), from 501 daily bars
Trend: vs 20d SMA 63.56 (-4.7%), 50d 65.28 (-7.2%), 200d 65.14 (-7.0%); 50d above 200d
Momentum: RSI(14) 38.2 | MACD -1.374 vs signal -0.968 (histogram -0.406)
Returns: 1d -0.4% | 5d -2.6% | 1m -5.3% | 3m -12.3%
52-week range: 55.33 - 71.61 (now 32.1% of the way up)
Volatility: ATR(14) 1.28 (2.1% of price) | annualised 20d 33.5%
Volume: 0.02x the 20-day average
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
Three-year record: +14.7% a year | beta to the market 1.13
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

<details><summary><b>What analysts and big funds say</b> — score +0.55</summary>

_Not available today._

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score +0.55</summary>

```text
Rolled up from the 5 largest holdings, 42.3% of the fund by weight
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 1.57 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +69.9% above the current prices
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
Share count change: 1 week: +0.0% (0.00) over 7d | 1 month: +0.0% (0.00) over 31d
Shares outstanding: 5.55M | fund size: 336.05M
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Spain (EWP) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Mixed signals: bullish analyst view (+11.8% price target) covering just over half the fund, solid fundamentals (moderate valuation, 3% yield, strong 3‑yr record), but weak technicals (price below 20‑, 50‑, 200‑day SMAs, RSI 40.4, MACD negative) and flat fund flows indicating no net demand. Macro environment is stressed (VIX up, yields higher, dollar stronger), providing no clear catalyst.

**Main reasons it gave:**
- Technical momentum weak: price below 20‑day, 50‑day and 200‑day SMAs, RSI 40.4, MACD negative
- Fund flows flat: 0% change in share count over week and month
- Analyst coverage positive (+11.8% price target) but only covers 53% of the fund

<details><summary><b>News</b> — score +0.00</summary>

_No news found for this one today._

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.17% (+0.03 on the week) | 5-year 4.71% (-0.19 on the week) | 10-year 4.90% (-0.20 on the week) | 30-year 5.29% (-0.17 on the week)
Yield curve, 10-year minus 3-month: +0.73 points -- upward sloping (normal)
US dollar index: 103.81 (+0.32 on the week)
Volatility (VIX): 29.34 (+3.9 on the week) -- stressed
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.1% (2026-10-01) | jobless claims 203k (2026-11-14)
Policy and expectations: Fed target 4.00% | market expects 2.1% inflation over 10 years
Rate path: 2-year Treasury 4.63% vs Fed target 3.75-4.00% -- the bond market prices about 3 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score -0.20</summary>

```text
Last close 56.32 (bar of 2026-11-24), from 501 daily bars
Trend: vs 20d SMA 57.97 (-2.8%), 50d 58.59 (-3.9%), 200d 58.17 (-3.2%); 50d above 200d
Momentum: RSI(14) 40.4 | MACD -0.518 vs signal -0.228 (histogram -0.291)
Returns: 1d -0.2% | 5d -3.6% | 1m -1.6% | 3m -10.4%
52-week range: 49.94 - 63.23 (now 48.0% of the way up)
Volatility: ATR(14) 0.95 (1.7% of price) | annualised 20d 27.1%
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
Three-year record: +26.8% a year | beta to the market 0.91
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
Weighted price target: +11.8% above the current prices
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
Share count change: 1 week: +0.0% (0.00) over 7d | 1 month: +0.0% (0.00) over 31d
Shares outstanding: 37.35M | fund size: 2.10B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Taiwan (EWT) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> No macro surprise in rates or data; technicals show price below short‑term moving averages and negative momentum; strong inflows but not enough to offset negative technicals; analyst view bullish but covers only 37.7% of the fund.

**Main reasons it gave:**
- Treasury yields down modestly this week, no rate surprise
- VIX rose to 29.34, indicating heightened market stress
- EWT price below 20‑day, 50‑day, 200‑day SMAs; RSI 41.1; MACD negative
- Fund flows: +16.4% share count increase in one week, showing strong inflows
- Analyst view: 100% buy rating with +57% price target, covering 37.7% of fund

<details><summary><b>News</b> — score +0.00</summary>

- [2 ETFs to Watch for Outsized Volume on Taiwanese & Chinese Equities](https://finance.yahoo.com/markets/stocks/articles/2-etfs-watch-outsized-volume-124300412.html)  
  <sub>Yahoo Finance, 2 hours ago</sub>  
  Taiwan and China ETFs recorded trading volumes more than triple their daily averages, signaling unusually strong investor interest.
- [iShares MSCI Taiwan ETF (EWT): Price, Holdings and Outlook](https://www.vtmarkets.com/en-mena/discover/ishares-msci-taiwan-etf-ewt/)  
  <sub>VT Markets, 7 hours ago</sub>  
  The iShares MSCI Taiwan ETF (EWT) is one of the most concentrated single-country ETFs available to retail investors, with Taiwan Semiconductor Manufacturing...
- [REG - Leverage Shares PLC Leverage -3XShrtTwn£ Leverage-3XShrtTawn$ Leverage-3XShrtTawnE - Replacement Intraday Rebalance Notice - -3x EWT](https://www.google.com/goto?url=CAESigIBxCJF1_ouYouyhNYoDgEtnm4Y1CHiC5zDjVCHrDAz4oFHwqSPkWv9PoYuVzr9ZS43nY__HUCwNxzpC7veQmDWOWEzO6OtO40m1KOpETCpalQNPMR1EzsyFwykPb530IiokC1S6aFjaF4_L8wR3feqBTOAnGKvzMXwnBQaDqeGZD3r3pUdb8OKLQ5uEhK2auQDdzr8dDHgO2iFFH-boNf4iw1mahDL_Zxc3aT8ml75UygkbmFJQ5JdSRF77i6tW7zcmkySjLUmNQ6wEZd5mQ3pNpXVJaAsmRvlzNWkXNIvfKY3WmjoLcBDAdwFSbGUVQvQfk72Dr1wxME-weC0vmy7IcxxEVN0rVgnAw&gsessionid=HHzS9QHItYfxF6dZHF7-SFsv_K0xXtCceRDBQ2umlJY-tFQufTAdPg)  
  <sub>TradingView, 21 hours ago</sub>  
  RNS Number : 4268E Leverage Shares PLC 24 November 2026 The following amendment has been made to the 'Intraday Rebalance Notice - -3x EWT' released on 23...
- [Jensen Huang Returns to Nvidia; NVDA Surges 32%, Nasdaq Rips 7%, and Taiwan Reverses Last Week’s Entire Collapse in a Single Session](https://www.google.com/goto?url=CAESkQIBxCJF1zfnbjQAVf6Uaj3WTDi84In1QQ4z2nWR1AA0nqLxCrKXtxSjlXaQ8778gV4PwP-tLUfbDiMNld5hbeKYtQ3LV5IfBwtKyr4EB_p4BcPVuQ8rAd6rB3yUSPtpYkI0L1f3K0r5e1IP8bb-Hz7Y4s4_xskf3_Kk9N-YmkLK0VvoBr_rFlkaSMwNXJYJ1uhkdUGZ-EzWOQXcTmg1E6r0wSnlOMX2Q3HniqkHQ9z5QoJ6JdV60JkFBGlD5XvsxufPzntiHxKx8QuL_wm-ZjibnThxg7RadbMjU3NCUBdjZ0srU6ZAyohimcwInijfmAb1SXNQ0XKZixbPK6UFXDLq-u2UshXVL2NZMeDGqBdFtKQ&gsessionid=HHzS9QHItYfxF6dZHF7-SFsv_K0xXtCceRDBQ2umlJY-tFQufTAdPg)  
  <sub>The Globe and Mail, 20 hours ago</sub>  
  Historic Catalyst. Trump tells CNBC “I made the deal” to reinstate Nvidia's Jensen Huang as CEO. NVDA immediately surges 32%, EWT +20%, SOXX +13%, QQQ +7%,...
- [Roundhill Memory ETF (DRAM) Stock Price, News, Quote & History](https://www.google.com/goto?url=CAESZQHEIkXXGIDzWPvlFmBJGtnKBsDvqFGP9iDhj7NMGYGRrdtd4PZv9d7Net28ii9awdM-bgvlvp__oqOj5s74mOUlltTUqdVzj-VkvdJwAhzpz2YBsa_jNwNDrrYExOxg0of912rg&gsessionid=HHzS9QHItYfxF6dZHF7-SFsv_K0xXtCceRDBQ2umlJY-tFQufTAdPg)  
  <sub>Yahoo! Finance Canada, 18 hours ago</sub>  
  Find the latest Roundhill Memory ETF (DRAM) stock quote, history, news and other vital information to help you with your stock trading and investing.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.17% (+0.03 on the week) | 5-year 4.71% (-0.19 on the week) | 10-year 4.90% (-0.20 on the week) | 30-year 5.29% (-0.17 on the week)
Yield curve, 10-year minus 3-month: +0.73 points -- upward sloping (normal)
US dollar index: 103.81 (+0.32 on the week)
Volatility (VIX): 29.34 (+3.9 on the week) -- stressed
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.1% (2026-10-01) | jobless claims 203k (2026-11-14)
Policy and expectations: Fed target 4.00% | market expects 2.1% inflation over 10 years
Rate path: 2-year Treasury 4.63% vs Fed target 3.75-4.00% -- the bond market prices about 3 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score -0.20</summary>

```text
Last close 86.35 (bar of 2026-11-24), from 501 daily bars
Trend: vs 20d SMA 93.69 (-7.8%), 50d 104.50 (-17.4%), 200d 95.27 (-9.4%); 50d above 200d
Momentum: RSI(14) 41.1 | MACD -5.730 vs signal -5.067 (histogram -0.663)
Returns: 1d -2.1% | 5d -2.6% | 1m -18.2% | 3m -18.8%
52-week range: 60.03 - 118.00 (now 45.4% of the way up)
Volatility: ATR(14) 5.30 (6.1% of price) | annualised 20d 102.6%
Volume: 0.34x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.25</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score +0.25</summary>

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
Rolled up from the 5 largest holdings, 37.7% of the fund by weight
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 1.33 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +57.2% above the current prices
Holdings read: 2330.TW, 2454.TW, 2317.TW, 3711.TW, 2308.TW
Recent rating changes among them: none reported
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
Share count change: 1 week: +16.4% (1.60B) over 7d | 1 month: +16.4% (1.60B) over 32d
Shares outstanding: 131.41M | fund size: 11.35B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### United Kingdom (EWU) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> No macro surprise, no decisive technical break, and the technicals are weak (price below SMAs, low momentum, low volume). Positive analyst coverage and recent inflows are noted but not enough to outweigh the neutral stance.

**Main reasons it gave:**
- Price below 20‑day SMA (‑2.9%) and 50‑day SMA (‑2.7%)
- RSI 41.6 and negative MACD indicate weak momentum
- VIX up 3.9 points to 29.34, showing heightened market stress
- Share count rose 7.7% in one week, indicating net inflows

<details><summary><b>News</b> — score +0.00</summary>

- [Breturn? Burnham says it's unthinkable for UK to rejoin EU without referendum](https://seekingalpha.com/news/4676000-burnham-says-its-unthinkable-for-uk-to-rejoin-eu-without-referendum?source=generic_rss)  
  <sub>Seeking Alpha, 3 hours ago</sub>  
  Andy Burnham says UK rejoining the EU without a referendum is unthinkable, but he is not proposing a rerun now and says the reset deal sets no fixed...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.17% (+0.03 on the week) | 5-year 4.71% (-0.19 on the week) | 10-year 4.90% (-0.20 on the week) | 30-year 5.29% (-0.17 on the week)
Yield curve, 10-year minus 3-month: +0.73 points -- upward sloping (normal)
US dollar index: 103.81 (+0.32 on the week)
Volatility (VIX): 29.34 (+3.9 on the week) -- stressed
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.1% (2026-10-01) | jobless claims 203k (2026-11-14)
Policy and expectations: Fed target 4.00% | market expects 2.1% inflation over 10 years
Rate path: 2-year Treasury 4.63% vs Fed target 3.75-4.00% -- the bond market prices about 3 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score -0.20</summary>

```text
Last close 45.85 (bar of 2026-11-24), from 501 daily bars
Trend: vs 20d SMA 47.21 (-2.9%), 50d 47.14 (-2.7%), 200d 47.07 (-2.6%); 50d above 200d
Momentum: RSI(14) 41.6 | MACD -0.487 vs signal -0.207 (histogram -0.280)
Returns: 1d +0.7% | 5d -2.3% | 1m -3.7% | 3m -6.2%
52-week range: 41.92 - 49.39 (now 52.7% of the way up)
Volatility: ATR(14) 0.67 (1.5% of price) | annualised 20d 23.4%
Volume: 0.03x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.10</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score +0.10</summary>

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
Rolled up from the 5 largest holdings, 36.9% of the fund by weight
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 2.07 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +19.3% above the current prices
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
Share count change: 1 week: +7.7% (273.87M) over 7d | 1 month: +9.0% (317.13M) over 32d
Shares outstanding: 83.64M | fund size: 3.84B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Mexico (EWW) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Neutral overall; technicals are weak, flows flat, and no macro surprise, while analyst view is bullish but limited to <50% of fund weight.

**Main reasons it gave:**
- Technical indicators: price below 20‑day, 50‑day, 200‑day SMAs; RSI 39.4; MACD negative; volume 0.13× 20‑day average
- Fund flows flat (0% change) indicating no net demand
- Analyst coverage: 100% buy on 47.5% of fund weight, weighted price target +18% above current price
- Macro data: no surprise in inflation, unemployment, or policy; yields modestly down, VIX high but no policy shift

<details><summary><b>News</b> — score +0.00</summary>

_No news found for this one today._

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.17% (+0.03 on the week) | 5-year 4.71% (-0.19 on the week) | 10-year 4.90% (-0.20 on the week) | 30-year 5.29% (-0.17 on the week)
Yield curve, 10-year minus 3-month: +0.73 points -- upward sloping (normal)
US dollar index: 103.81 (+0.32 on the week)
Volatility (VIX): 29.34 (+3.9 on the week) -- stressed
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.1% (2026-10-01) | jobless claims 203k (2026-11-14)
Policy and expectations: Fed target 4.00% | market expects 2.1% inflation over 10 years
Rate path: 2-year Treasury 4.63% vs Fed target 3.75-4.00% -- the bond market prices about 3 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score -0.20</summary>

```text
Last close 72.93 (bar of 2026-11-24), from 501 daily bars
Trend: vs 20d SMA 75.40 (-3.3%), 50d 74.15 (-1.6%), 200d 76.06 (-4.1%); 50d below 200d
Momentum: RSI(14) 39.4 | MACD -0.396 vs signal 0.179 (histogram -0.575)
Returns: 1d +0.3% | 5d -5.1% | 1m -3.1% | 3m -6.0%
52-week range: 66.55 - 81.23 (now 43.5% of the way up)
Volatility: ATR(14) 1.48 (2.0% of price) | annualised 20d 21.5%
Volume: 0.13x the 20-day average
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
Three-year record: +8.5% a year | beta to the market 0.99
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
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 2.12 on a 1=strong buy to 5=strong sell scale)
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
Direction: flat (1 month)
Share count change: 1 week: +0.0% (0.00) over 7d | 1 month: +0.0% (0.00) over 31d
Shares outstanding: 18.90M | fund size: 1.38B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### South Africa (EZA) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Neutral overall; technicals are bearish but lack heavy volume, analyst coverage is bullish on top holdings, fund flows are flat, and macro environment shows no surprise.

**Main reasons it gave:**
- Price below 20‑day, 50‑day and 200‑day SMAs, negative MACD
- Analyst coverage of top holdings 100% buy with +41% price target
- Fund flows flat over the past month, indicating no net demand
- VIX up 3.9 points to 29.34, indicating elevated market volatility

<details><summary><b>News</b> — score +0.00</summary>

_No news found for this one today._

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.17% (+0.03 on the week) | 5-year 4.71% (-0.19 on the week) | 10-year 4.90% (-0.20 on the week) | 30-year 5.29% (-0.17 on the week)
Yield curve, 10-year minus 3-month: +0.73 points -- upward sloping (normal)
US dollar index: 103.81 (+0.32 on the week)
Volatility (VIX): 29.34 (+3.9 on the week) -- stressed
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.1% (2026-10-01) | jobless claims 203k (2026-11-14)
Policy and expectations: Fed target 4.00% | market expects 2.1% inflation over 10 years
Rate path: 2-year Treasury 4.63% vs Fed target 3.75-4.00% -- the bond market prices about 3 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score -0.20</summary>

```text
Last close 58.58 (bar of 2026-11-24), from 501 daily bars
Trend: vs 20d SMA 63.34 (-7.5%), 50d 64.29 (-8.9%), 200d 67.54 (-13.3%); 50d below 200d
Momentum: RSI(14) 36.8 | MACD -1.709 vs signal -0.898 (histogram -0.810)
Returns: 1d -0.8% | 5d -7.0% | 1m -7.7% | 3m -18.3%
52-week range: 56.26 - 81.60 (now 9.2% of the way up)
Volatility: ATR(14) 1.75 (3.0% of price) | annualised 20d 42.2%
Volume: 0.03x the 20-day average
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
Three-year record: +17.8% a year | beta to the market 1.12
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
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 1.98 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +41.0% above the current prices
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
Share count change: 1 week: +0.0% (0.00) over 7d | 1 month: +0.0% (0.00) over 31d
Shares outstanding: 7.90M | fund size: 462.78M
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Gold mining companies (GDX) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Overall neutral as bullish analyst view and strong inflows are offset by bearish technicals and a stressed macro environment with no clear policy surprise.

**Main reasons it gave:**
- Large weekly inflows (+19.2% share count) indicate strong bullish demand
- Technical indicators show price below 20‑day, 50‑day, and 200‑day SMAs with negative momentum (RSI 38.6, MACD negative)
- Analyst consensus 100% buy with a +31.8% price target for top holdings
- Macro environment stable: normal upward yield curve, no policy surprise, but VIX elevated at 29.34 indicating market stress

<details><summary><b>News</b> — score +0.00</summary>

- [VanEck Gold Miners ETF (GDX) Options Chain - Yahoo Finance](https://ca.finance.yahoo.com/quote/GDX/options/?date=1795996800&straddle=false&type=all)  
  <sub>Yahoo! Finance Canada, 14 hours ago</sub>  
  View the basic GDX option chain and compare options of VanEck Gold Miners ETF on Yahoo Finance.
- [China Electric Truck Boom Leaves A Lithium Route Beyond GDX](https://simplywall.st/etfs/us/nysearca-gdxj/news/china-electric-truck-boom-leaves-a-lithium-route-beyond-gdx)  
  <sub>Simply Wall St, 3 hours ago</sub>  
  Metals and mining funds can look interchangeable at first glance. Two tickers, similar names, and it feels like you are picking between cola brands.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.17% (+0.03 on the week) | 5-year 4.71% (-0.19 on the week) | 10-year 4.90% (-0.20 on the week) | 30-year 5.29% (-0.17 on the week)
Yield curve, 10-year minus 3-month: +0.73 points -- upward sloping (normal)
US dollar index: 103.81 (+0.32 on the week)
Volatility (VIX): 29.34 (+3.9 on the week) -- stressed
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.1% (2026-10-01) | jobless claims 203k (2026-11-14)
Policy and expectations: Fed target 4.00% | market expects 2.1% inflation over 10 years
Rate path: 2-year Treasury 4.63% vs Fed target 3.75-4.00% -- the bond market prices about 3 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score -0.50</summary>

```text
Last close 73.09 (bar of 2026-11-24), from 501 daily bars
Trend: vs 20d SMA 80.17 (-8.8%), 50d 85.08 (-14.1%), 200d 88.79 (-17.7%); 50d below 200d
Momentum: RSI(14) 38.6 | MACD -3.571 vs signal -2.527 (histogram -1.044)
Returns: 1d +0.4% | 5d -8.1% | 1m -9.8% | 3m -28.6%
52-week range: 68.40 - 115.84 (now 9.9% of the way up)
Volatility: ATR(14) 3.63 (5.0% of price) | annualised 20d 65.6%
Volume: 0.10x the 20-day average
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
Three-year record: +35.4% a year | beta to the market 0.98
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

<details><summary><b>What analysts and big funds say</b> — score +0.50</summary>

_Not available today._

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score +0.50</summary>

```text
Rolled up from the 5 largest holdings, 42.0% of the fund by weight
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 1.70 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +31.8% above the current prices
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
Direction: money coming in (1 month)
Share count change: 1 week: +19.2% (4.09B) over 7d | 1 month: +8.7% (2.04B) over 31d
Shares outstanding: 347.94M | fund size: 25.43B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Software (IGV) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Neutral overall: no macro surprise, mixed technicals, flat fund flows, bullish analyst view but limited coverage, and negative software distress news.

**Main reasons it gave:**
- Software sector distress noted by Apollo (Seeking Alpha)
- Flat fund flows (0% change week/month)
- Technical indicators: price below 20‑day and 50‑day SMAs, RSI 39.8, low volume
- Analyst consensus: 100% buy, +39% price target for top holdings

<details><summary><b>News</b> — score +0.00</summary>

- [1 USD to IGV | Convert US Dollar to iShares Expanded Tech-Software ETF (Derivatives)](https://www.weex.com/tokens/ishares-expanded-tech-software-etf-derivatives/from-usd)  
  <sub>WEEX, 11 hours ago</sub>  
  1 USD = 0.01052 IGV. Real-time US Dollar to iShares Expanded Tech-Software ETF (Derivatives) calculator: Track live USD to IGV rates and historical charts...
- [3 ETFs For Owning Palo Alto Networks Without The Same Bet](https://finance.yahoo.com/markets/stocks/articles/3-etfs-owning-palo-alto-131058994.html)  
  <sub>Yahoo Finance, 2 hours ago</sub>  
  Owning Palo Alto Networks directly means living with its specific issues on your own, such as Simply Wall St's note that profit margins at 3.7% are well...
- [Software distress is about to get worse, Apollo says](https://www.google.com/goto?url=CAESlgEBxCJF1xLJVlEyELZJobqX9phZb2EHqVCvXWMA89dL5pOfEktaQ7hzSpn5H3vUB5xuZpi0WOGBXhTJM3-TgKMFhOmK6wv6ijmeGIXH5yheSz3AnlQMF9LOd1QEYarfNP6vX89mQYgPWmCi0LxHjwUo8BZpfl38Dx2NGVFAA7eAmZnZfVpLgdl7hbRdewyc6m0xaxEL0Ik&gsessionid=wsTbdHeTQ0YKsmdRuEhOwTp9WtOF_kMNP5zzKWQzTgBPnYWvgcrsEA)  
  <sub>Seeking Alpha, 51 minutes ago</sub>  
  Apollo Global Management chief economist Torsten Slok has indicated that distress across the software sector is set to worsen. Learn more here.
- [Invesco S&P 500 Equal Weight ETF (RSP) stock price, news, quote and history](https://www.google.com/goto?url=CAESZAHEIkXXSPkUfAbZFzPwGNoBTu-SwkIR-QLHKkXG61HxfUW44LLxzria_Qu-8NAnAPVbMXCtw39ocamkl43ww5sk-Q6aJwmwj5VMD2bgmovVv4_uQntdd-NwRP1TJ19mt8fGSqM&gsessionid=wsTbdHeTQ0YKsmdRuEhOwTp9WtOF_kMNP5zzKWQzTgBPnYWvgcrsEA)  
  <sub>Yahoo Finance Singapore, 21 hours ago</sub>  
  Find the latest Invesco S&P 500 Equal Weight ETF (RSP) stock quote, history, news and other vital information to help you with your stock trading and...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.17% (+0.03 on the week) | 5-year 4.71% (-0.19 on the week) | 10-year 4.90% (-0.20 on the week) | 30-year 5.29% (-0.17 on the week)
Yield curve, 10-year minus 3-month: +0.73 points -- upward sloping (normal)
US dollar index: 103.81 (+0.32 on the week)
Volatility (VIX): 29.34 (+3.9 on the week) -- stressed
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.1% (2026-10-01) | jobless claims 203k (2026-11-14)
Policy and expectations: Fed target 4.00% | market expects 2.1% inflation over 10 years
Rate path: 2-year Treasury 4.63% vs Fed target 3.75-4.00% -- the bond market prices about 3 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score -0.20</summary>

```text
Last close 95.96 (bar of 2026-11-24), from 501 daily bars
Trend: vs 20d SMA 100.38 (-4.4%), 50d 105.05 (-8.7%), 200d 94.55 (+1.5%); 50d above 200d
Momentum: RSI(14) 39.8 | MACD -3.087 vs signal -2.551 (histogram -0.536)
Returns: 1d +0.7% | 5d +0.2% | 1m -13.9% | 3m -6.3%
52-week range: 74.67 - 112.67 (now 56.0% of the way up)
Volatility: ATR(14) 3.29 (3.4% of price) | annualised 20d 37.6%
Volume: 0.11x the 20-day average
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
Three-year record: +6.5% a year | beta to the market 1.25
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
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 1.58 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +39.2% above the current prices
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
Share count change: 1 week: +0.0% (0.00) over 7d | 1 month: +0.0% (0.00) over 31d
Shares outstanding: 12.50M | fund size: 1.20B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### India (INDA) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Neutral overall; analyst view positive but thin coverage, significant outflows, modest fundamentals, bullish technicals with low volume, risk‑off macro.

**Main reasons it gave:**
- 1‑month fund outflows of -10.5% (-$675.46M) indicate bearish demand
- Analyst coverage of top 5 holdings (24.8% weight) all buy with +14.5% price target
- Technicals: price above 20‑day, 50‑day, 200‑day SMAs, RSI 68.5, but volume at 0.06× 20‑day average
- Macro: US Treasury yields up and VIX at 29.34, indicating risk‑off sentiment

<details><summary><b>News</b> — score +0.00</summary>

- [How to Invest in the MSCI India ETF (INDA)](https://www.fool.com/investing/how-to-invest/etfs/how-to-invest-in-inda-etf/)  
  <sub>The Motley Fool, 16 hours ago</sub>  
  Key Points. The iShares MSCI India ETF (INDA) tracks 165 Indian stocks and can be bought through a U.S. brokerage account. The fund charges 0.61% annually and...
- [World Markets Watchlist: November 23, 2026](https://etfdb.com/china-insights-content-hub/world-markets-watchlist-november-23-2026/)  
  <sub>ETF Database, 16 hours ago</sub>  
  Our global markets watchlist tracks nine prominent indexes from economies around the world. The list includes the S&P 500 from the U.S..
- [EEM Now Moves Like A Chip Fund](https://www.google.com/goto?url=CAESngEBxCJF14Q7VuecFm9bXCMDsJb3DLbWqXghh6iaB4OpbAXubbhnTsfFSnFR93EUSPSJNVOKkDGAylMqPtJvKeSh2vCN7tvmm0TfYIlPR_BqyT_e_kWU3OerZ7soz2Da_8Pe7vN7Ko4doweUHk6MzvpzDUw2802zslEBCRGs2mhCRWKb6uNulJOllp4tu5YjDe9InRW0eBBvH0CcSSBJ1g&gsessionid=u6Wl8B4MOanFV3qmHyBcDtxyR0ekBjn57WcuZYlzBrqtb_sFrsZd_w)  
  <sub>Trefis, 16 hours ago</sub>  
  Today's big story: Reported SEC Probe: Could Nvidia Stock Fall To $92? Update, Nov 23: After Nvidia's board reinstated Jensen Huang as CEO on Nov 22,...
- [Jensen Huang Returns to Nvidia; NVDA Surges 32%, Nasdaq Rips 7%, and Taiwan Reverses Last Week’s Entire Collapse in a Single Session](https://www.google.com/goto?url=CAESkAIBxCJF1z1zK50ReuAxOcRY35BqGyaqd59GEWrfQx2tLs3McS_gqn7pXw8-ACecjhI9ssKKtuoQ_D0RhJkFAIniuagc4h0y3EcyTG35R-JAetjeOj_QLVEuyIxicShMaOGhQs5Ljk4L8cbsBIopd1FEhj9GmOnS3LzB6geuxWLtfigRhVxWfJg6JGuVW57Db9jWn76ivCToyWFr3VGQvejmGKi7c1326-SEoO0bPLWptxDt7N3tCBUyqLLUUihRWhp-6sMF_6-MwFIi9gUMtdRsKBoNhBx-4sfXRylIi-fPucAOzRr_6m8q_KIqSYSHPQxCdzC_0br2XfPP0nwZByEnf-A7Gvrgh3rjQBTN2siavg&gsessionid=u6Wl8B4MOanFV3qmHyBcDtxyR0ekBjn57WcuZYlzBrqtb_sFrsZd_w)  
  <sub>The Globe and Mail, 20 hours ago</sub>  
  Detailed price information for Nvidia Corp (NVDA-Q) from The Globe and Mail including charting and trades.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.17% (+0.03 on the week) | 5-year 4.71% (-0.19 on the week) | 10-year 4.90% (-0.20 on the week) | 30-year 5.29% (-0.17 on the week)
Yield curve, 10-year minus 3-month: +0.73 points -- upward sloping (normal)
US dollar index: 103.81 (+0.32 on the week)
Volatility (VIX): 29.34 (+3.9 on the week) -- stressed
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.1% (2026-10-01) | jobless claims 203k (2026-11-14)
Policy and expectations: Fed target 4.00% | market expects 2.1% inflation over 10 years
Rate path: 2-year Treasury 4.63% vs Fed target 3.75-4.00% -- the bond market prices about 3 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.20</summary>

```text
Last close 52.32 (bar of 2026-11-24), from 501 daily bars
Trend: vs 20d SMA 50.60 (+3.4%), 50d 48.52 (+7.8%), 200d 49.07 (+6.6%); 50d below 200d
Momentum: RSI(14) 68.5 | MACD 1.184 vs signal 1.094 (histogram 0.090)
Returns: 1d +0.3% | 5d +0.8% | 1m +12.3% | 3m +5.2%
52-week range: 45.42 - 54.71 (now 74.3% of the way up)
Volatility: ATR(14) 0.60 (1.1% of price) | annualised 20d 15.3%
Volume: 0.06x the 20-day average
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

<details><summary><b>What analysts and big funds say</b> — score +0.25</summary>

_Not available today._

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score +0.25</summary>

```text
Rolled up from the 5 largest holdings, 24.8% of the fund by weight  -- thin, so read this as a fact about that slice rather than the fund
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 1.39 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +14.5% above the current prices
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
Share count change: 1 week: -2.9% (-175.53M) over 7d | 1 month: -10.5% (-675.46M) over 31d
Shares outstanding: 110.61M | fund size: 5.79B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Defence and aerospace (ITA) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Neutral overall – no macro surprise, technicals are bearish but no decisive break, strong inflows and bullish analyst view are offset by high valuations and mixed fundamentals.

**Main reasons it gave:**
- Fund flows: +211% share count increase over 1 month indicating strong inflows
- Technical: price below 20‑day, 50‑day, and 200‑day SMAs with negative MACD and RSI 45.6
- Macro: no policy surprise; yields stable and VIX elevated at 29.34

<details><summary><b>News</b> — score +0.00</summary>

- [Should You Invest in the iShares U.S. Aerospace & Defense ETF (ITA)?](https://finance.yahoo.com/markets/stocks/articles/invest-ishares-u-aerospace-defense-102003431.html)  
  <sub>Yahoo Finance, 4 hours ago</sub>  
  Sector ETF report for ITA.
- [3 ETFs That Hold RTX Very Differently After Its Outlook Lift](https://simplywall.st/etfs/us/nysearca-xli/news/3-etfs-that-hold-rtx-very-differently-after-its-outlook-lift)  
  <sub>Simply Wall St, 21 hours ago</sub>  
  You can own RTX directly or hold it inside a fund, and each route leaves you carrying something different. A single stock puts all of that business's...
- [Bitcoin Price Rises to IDR 1.12 Billion Today, but IDR 32 Trillion Flows Out of ETFs](https://www.google.com/goto?url=CAESfQHEIkXX_Bsss4erENwZMOxfM1yHVOsRO7aji8WUZX43z57MtHnYDSOygVDH7n8gAutTvI-bduIsB9ZTE5_olN-9Hgjidaeb2JeGXMlvUUcHT3oegsIYLV5uAJevvE-M95mwr5UkQZaVji7Q8P3hGFWxsQFxzafV7lZs7ocF&gsessionid=NZxc-8lVdRjsn_ru7BBkB8BaoM1EhXlnJuN8J284CYGR_ZcGeXH6IQ)  
  <sub>Aktualita.co, 11 hours ago</sub>  
  JAKARTA, Aktualita.co - The price of Bitcoin (BTC) today, Tuesday (11/24/2026), is moving upward again, even though pressure on the global crypto asset...
- [How Much RTX Do You Really Get Through 3 ETFs?](https://www.google.com/goto?url=CAESlAEBxCJF19h_cmTZDFdFuwmGGpaQSYzOIbLvoqmjrbUfF6iH7vZSwDJwN2nE7Je7Bv7qfziOQ9OOAUlPhLeeUtl7Aq1NJWhxsr1wcMdGqqXYk5wjI5yHOuRHbF89PeM7Bi7G-6OjvhCFmEetAbllo_s3UVgQuVk95dxJS2Zmh6FeomAL9f-Ir8tX-wTSh2S7E0z6PL6y&gsessionid=NZxc-8lVdRjsn_ru7BBkB8BaoM1EhXlnJuN8J284CYGR_ZcGeXH6IQ)  
  <sub>Yahoo Finance, 21 hours ago</sub>  
  If you like RTX for its mix of aerospace and defense work, owning only the stock means living with RTX specific risks alone.
- [Monument Ita AIG Fd. Inv - Glob Bal 1590 (0P0001HOBN.F) Seasonal returns chart - Yahoo Finance](https://www.google.com/goto?url=CAESeQHEIkXXlxILaLj3CKm7NxcjnvoquC_FwlaDo7Pzt2lgM3Un8a3XmIwj9GUECGfo5fchrvNwuqULw_x6mB28FgPxAPWfA_sZdBQMnFPN71izikCOnYa4SkXfpUPEvPNcLzntv2jmuAIVxxFEEfm9SorflVDgjBwKojM&gsessionid=NZxc-8lVdRjsn_ru7BBkB8BaoM1EhXlnJuN8J284CYGR_ZcGeXH6IQ)  
  <sub>Yahoo Finance Singapore, 19 hours ago</sub>  
  Monument Ita AIG Fd. Inv - Glob Bal 1590 (0P0001HOBN.F) seasonal returns chart provides the mean and median returns by month to inform your investment...
- [SPY Stock Rebounds as S&P 500 Surges: What Investors Should Watch After Wall Street’s Sell-Off](https://www.google.com/goto?url=CAESjQEBxCJF145kxbNcsuGo2nlEhhtMDY5J_tAGBwL8YlMJ_HrScJ4QLhhGfQtz4aPPBnPkERO2UlW1v1im2Ej7AgecttFItSRoszMoJjbNpLOv3z9A6u02-GRw14zF5p4X8lV1it9gf0XjZXGyaU-qlhsg4jzt-WPS8wzktxr41-uJD0qWaUF37hpB-wpgzpQ&gsessionid=NZxc-8lVdRjsn_ru7BBkB8BaoM1EhXlnJuN8J284CYGR_ZcGeXH6IQ)  
  <sub>Aktualita.co, 23 hours ago</sub>  
  NEW YORK, Aktualita.co - SPY stock is back in focus on Monday, November 23, 2026, as Wall Street stages a powerful rebound following a turbulent week that...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.17% (+0.03 on the week) | 5-year 4.71% (-0.19 on the week) | 10-year 4.90% (-0.20 on the week) | 30-year 5.29% (-0.17 on the week)
Yield curve, 10-year minus 3-month: +0.73 points -- upward sloping (normal)
US dollar index: 103.81 (+0.32 on the week)
Volatility (VIX): 29.34 (+3.9 on the week) -- stressed
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.1% (2026-10-01) | jobless claims 203k (2026-11-14)
Policy and expectations: Fed target 4.00% | market expects 2.1% inflation over 10 years
Rate path: 2-year Treasury 4.63% vs Fed target 3.75-4.00% -- the bond market prices about 3 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score -0.60</summary>

```text
Last close 68.57 (bar of 2026-11-24), from 501 daily bars
Trend: vs 20d SMA 70.15 (-2.2%), 50d 69.76 (-1.7%), 200d 75.62 (-9.3%); 50d below 200d
Momentum: RSI(14) 45.6 | MACD -0.509 vs signal -0.201 (histogram -0.308)
Returns: 1d +0.1% | 5d -1.5% | 1m -0.7% | 3m -13.0%
52-week range: 66.17 - 84.41 (now 13.2% of the way up)
Volatility: ATR(14) 1.81 (2.6% of price) | annualised 20d 35.2%
Volume: 0.03x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.10</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score +0.10</summary>

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
Rolled up from the 5 largest holdings, 54.8% of the fund by weight
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 1.73 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +19.8% above the current prices
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
Share count change: 1 week: +8.0% (933.22M) over 7d | 1 month: +211.1% (8.59B) over 31d
Shares outstanding: 184.61M | fund size: 12.66B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Transport and delivery (IYT) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Neutral overall as there is no macro surprise or decisive technical break. Analyst coverage is strongly bullish, fund inflows are positive, but technical momentum is weak and macro conditions are stressed.

**Main reasons it gave:**
- Analyst view: 90.9% buy rating with mean rating 1.87 (strong buy) and weighted price target +22.4% above current price
- Fund flows: +6.4% share count increase in 1 week (inflows) indicating strong demand
- Technical momentum: RSI 43.3, MACD negative, price below 20‑day/50‑day/200‑day SMAs, volume at 0.08× 20‑day average
- Macro: No rate or policy surprise; yields stable, upward‑sloping curve, VIX elevated but unchanged

<details><summary><b>News</b> — score +0.00</summary>

_No news found for this one today._

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.17% (+0.03 on the week) | 5-year 4.71% (-0.19 on the week) | 10-year 4.90% (-0.20 on the week) | 30-year 5.29% (-0.17 on the week)
Yield curve, 10-year minus 3-month: +0.73 points -- upward sloping (normal)
US dollar index: 103.81 (+0.32 on the week)
Volatility (VIX): 29.34 (+3.9 on the week) -- stressed
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.1% (2026-10-01) | jobless claims 203k (2026-11-14)
Policy and expectations: Fed target 4.00% | market expects 2.1% inflation over 10 years
Rate path: 2-year Treasury 4.63% vs Fed target 3.75-4.00% -- the bond market prices about 3 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score -0.30</summary>

```text
Last close 79.74 (bar of 2026-11-24), from 501 daily bars
Trend: vs 20d SMA 82.29 (-3.1%), 50d 80.89 (-1.4%), 200d 82.05 (-2.8%); 50d below 200d
Momentum: RSI(14) 43.3 | MACD -0.236 vs signal 0.251 (histogram -0.487)
Returns: 1d -0.7% | 5d -3.2% | 1m -1.2% | 3m -8.6%
52-week range: 70.18 - 90.01 (now 48.2% of the way up)
Volatility: ATR(14) 1.72 (2.2% of price) | annualised 20d 29.5%
Volume: 0.08x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score -0.20</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score -0.20</summary>

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
Rolled up from the 5 largest holdings, 52.2% of the fund by weight
Ratings by weight: buy 90.9% | hold 9.1% | sell 0.0% (mean 1.87 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +22.4% above the current prices
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
Share count change: 1 week: +6.4% (121.52M) over 7d | 1 month: +8.1% (151.52M) over 32d
Shares outstanding: 25.47M | fund size: 2.03B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### US regional banks (KRE) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Bank‑sector news shows a modest rebound (stocks up ~1.7% but still below recent highs), which is mildly positive but not a decisive catalyst. KRE’s price sits below its 20‑, 50‑ and 200‑day SMAs, RSI is 40.5 and MACD is negative, indicating continued bearish momentum. Fundamentals (P/E 12.2, P/B 1.26, 2.2% yield) are stable and unremarkable for the sector. Analyst coverage of the top holdings is thin (5.9% of assets) and split roughly 50/50 between buy and hold, with a modest +15% price‑target, giving only a slight bullish tilt. Fund flows are strongly positive (+6.4% week‑over‑week, +13.8% month‑over‑month), reflecting demand for regional‑bank exposure. No policy or rate surprise occurred this week. With mixed signals and no clear macro catalyst, we keep a neutral outlook.

**Main reasons it gave:**
- Bank stocks rebounded 1.7% but stay 4.7% below recent highs (sector news)
- KRE price below 20‑, 50‑, and 200‑day SMAs; MACD negative, RSI 40.5 (technicals)
- Share count rose 6.4% in one week and 13.8% in one month (fund flows)
- Analyst coverage of top holdings shows 50% buy rating and +15% price target (analyst view)

<details><summary><b>News</b> — score +0.15</summary>

- [Bank stocks recover from Friday's tumble](https://www.tradingview.com/news/seekingalpha:145020e27094b:0-bank-stocks-recover-from-friday-s-tumble/)  
  <sub>TradingView, 21 hours ago</sub>  
  Bank stocks' revival on Monday erased Friday's losses, but it's not enough to unwind last week's brutal decline. And while the sector showed solid gains on...
- [Daily ETF Flows: ARK ETFs Lead](https://finance.yahoo.com/markets/options/articles/daily-etf-flows-ark-etfs-230911297.html)  
  <sub>Yahoo Finance, 16 hours ago</sub>  
  Top 10 Creations (All ETFs). Ticker. Name. Net Flows ($, mm). AUM ($, mm). AUM % Change. ARKK · ARK Innovation ETF. 4,295.87. 18,656.72. 23.03%.
- [ETFs Pull In $57B Despite Tech Rout](https://www.google.com/goto?url=CAESigEBxCJF16VM1Rm60MB6V_yiNDKMTQ8IWGfvetGbArI6FX-pD_K3Ct8meQBQrq_11w4g72ThePXW0T_KLy-vmDQ6SCco9Isud9Xo4LSSqnQzlax0XRmpRb8c9yfqaTjtHe88488EThDMRjcd132igb-pfjw0PElNfFik9hC423coTXut7imzTCBVxhU&gsessionid=kVda4vHyiAUNjtPY8GW9oJPX8gGXoeicSRv9RmDpOvQ70snmF7qj5g)  
  <sub>ETF.com, 21 hours ago</sub>  
  U.S.-listed ETFs pulled in more than $57 billion last week as stocks tumbled, though nearly a third of that came from ARK funds whose inflows have already...
- [Bank stocks recover from Friday's tumble (JPM:NYSE)](https://www.google.com/goto?url=CAESigEBxCJF1497NKG_q49wWpek0lDzCa0qpq4PMcvgIrxYrtDMekZ48YlMUv1iAGnMQhQXO2OIsWKqyMeOwXH0WXx48jrqhIxfXDAozaLH9gBtXdFT7UMwvLE5d3fmZGqmu21CTmI49ht19ulMW5zYdtTjETh13zCgJ7OLsbhLz12IYRuMI1EvDiBkO7c&gsessionid=kVda4vHyiAUNjtPY8GW9oJPX8gGXoeicSRv9RmDpOvQ70snmF7qj5g)  
  <sub>Seeking Alpha, 21 hours ago</sub>  
  Bank stocks rebound Monday, with the SPDR S&P Bank ETF up 1.7% to $63.36, but it remains 4.7% below its Nov.
- [Wall Street's SpaceX sequel: Anthropic gets leveraged ETFs and options, and the original didn't end well](https://www.google.com/goto?url=CAESjQEBxCJF10sPKNRweeqmelaKEBx_2n4nfIV0EHG0kMcuFChtv6pZO28KUj1Sx0hOnmeLtcVMu0y-Q5bMLMH9LnVuMopclTuOQ02EVsJa6Kt_svqIN7JVH6c1Nlt8wTYJF6Z8an7aTSXBIBYbH3dP52VBDgPs5aFXamij_3ALRBNz0FfLmr_DnZeSduQIqfQ&gsessionid=kVda4vHyiAUNjtPY8GW9oJPX8gGXoeicSRv9RmDpOvQ70snmF7qj5g)  
  <sub>AOL.com, 22 hours ago</sub>  
  Anthropic traders get 13 leveraged ETFs and listed options on Monday. Here's how the funds work.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.15</summary>

```text
US Treasury yields: 3-month 4.17% (+0.03 on the week) | 5-year 4.71% (-0.19 on the week) | 10-year 4.90% (-0.20 on the week) | 30-year 5.29% (-0.17 on the week)
Yield curve, 10-year minus 3-month: +0.73 points -- upward sloping (normal)
US dollar index: 103.81 (+0.32 on the week)
Volatility (VIX): 29.34 (+3.9 on the week) -- stressed
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.1% (2026-10-01) | jobless claims 203k (2026-11-14)
Policy and expectations: Fed target 4.00% | market expects 2.1% inflation over 10 years
Rate path: 2-year Treasury 4.63% vs Fed target 3.75-4.00% -- the bond market prices about 3 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score -0.55</summary>

```text
Last close 69.51 (bar of 2026-11-24), from 501 daily bars
Trend: vs 20d SMA 71.86 (-3.3%), 50d 71.15 (-2.3%), 200d 71.16 (-2.3%); 50d below 200d
Momentum: RSI(14) 40.5 | MACD -0.595 vs signal -0.154 (histogram -0.441)
Returns: 1d -0.0% | 5d -1.9% | 1m -4.4% | 3m -6.8%
52-week range: 61.66 - 77.93 (now 48.2% of the way up)
Volatility: ATR(14) 1.43 (2.1% of price) | annualised 20d 21.3%
Volume: 0.11x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.00</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score +0.00</summary>

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
Rolled up from the 5 largest holdings, 5.9% of the fund by weight  -- thin, so read this as a fact about that slice rather than the fund
Ratings by weight: buy 50.1% | hold 49.9% | sell 0.0% (mean 2.45 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +15.0% above the current prices
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
Share count change: 1 week: +6.4% (245.51M) over 7d | 1 month: +13.8% (493.79M) over 31d
Shares outstanding: 58.62M | fund size: 4.07B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Saudi Arabia (KSA) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:** no explanation. It wrote only “NEUTRAL”, so the main reasons below are all it gave.

**Main reasons it gave:**
- No macro surprise: yields down modestly, VIX up but no policy shift
- Technical downtrend: price below 20d, 50d, 200d SMAs, low volume
- Fund outflows: -9.6% share count over past month
- Analyst consensus: 100% buy with +19.2% price target

<details><summary><b>News</b> — score +0.00</summary>

_No news found for this one today._

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.17% (+0.03 on the week) | 5-year 4.71% (-0.19 on the week) | 10-year 4.90% (-0.20 on the week) | 30-year 5.29% (-0.17 on the week)
Yield curve, 10-year minus 3-month: +0.73 points -- upward sloping (normal)
US dollar index: 103.81 (+0.32 on the week)
Volatility (VIX): 29.34 (+3.9 on the week) -- stressed
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.1% (2026-10-01) | jobless claims 203k (2026-11-14)
Policy and expectations: Fed target 4.00% | market expects 2.1% inflation over 10 years
Rate path: 2-year Treasury 4.63% vs Fed target 3.75-4.00% -- the bond market prices about 3 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 34.90 (bar of 2026-11-24), from 501 daily bars
Trend: vs 20d SMA 35.18 (-0.8%), 50d 35.66 (-2.1%), 200d 37.63 (-7.3%); 50d below 200d
Momentum: RSI(14) 42.0 | MACD -0.076 vs signal -0.067 (histogram -0.010)
Returns: 1d -0.2% | 5d -2.9% | 1m +2.6% | 3m -11.6%
52-week range: 33.69 - 40.63 (now 17.4% of the way up)
Volatility: ATR(14) 0.33 (1.0% of price) | annualised 20d 13.3%
Volume: 0.09x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score -0.20</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score -0.20</summary>

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
Rolled up from the 5 largest holdings, 45.3% of the fund by weight
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 2.10 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +19.2% above the current prices
Holdings read: 1120.SR, 2222.SR, 1180.SR, 7010.SR, 1211.SR
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
Share count change: 1 week: +2.0% (10.79M) over 7d | 1 month: -9.6% (-58.55M) over 31d
Shares outstanding: 15.75M | fund size: 549.67M
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### China (MCHI) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:** no explanation. It wrote only “NEUTRAL”, so the main reasons below are all it gave.

**Main reasons it gave:**
- 1-month fund flow: -2.1% net outflow (money going out)
- Price 46.60 below 20-day SMA 49.31, 50-day SMA 50.76, 200-day SMA 54.63
- RSI 31.3 (oversold) and MACD negative, volume 0.12x 20-day average
- Analyst coverage 32.6% of fund, 100% buy rating, weighted price target +75.6%
- Macro: yields down modestly, VIX up to 29.34, no policy surprise

<details><summary><b>News</b> — score +0.00</summary>

- [2 ETFs to Watch for Outsized Volume on Taiwanese & Chinese Equities](https://finance.yahoo.com/markets/stocks/articles/2-etfs-watch-outsized-volume-124300412.html)  
  <sub>Yahoo Finance, 2 hours ago</sub>  
  Taiwan and China ETFs recorded trading volumes more than triple their daily averages, signaling unusually strong investor interest.
- [ETFs Investing in China Hongqiao Group Ltd. Stocks](https://www.tradingview.com/symbols/VIE-H0Q/etfs/)  
  <sub>TradingView, 23 hours ago</sub>  
  Explore funds investing in H0Q in a single list with price, expense ratio, and more stats for an in-depth analysis of new opportunities.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.17% (+0.03 on the week) | 5-year 4.71% (-0.19 on the week) | 10-year 4.90% (-0.20 on the week) | 30-year 5.29% (-0.17 on the week)
Yield curve, 10-year minus 3-month: +0.73 points -- upward sloping (normal)
US dollar index: 103.81 (+0.32 on the week)
Volatility (VIX): 29.34 (+3.9 on the week) -- stressed
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.1% (2026-10-01) | jobless claims 203k (2026-11-14)
Policy and expectations: Fed target 4.00% | market expects 2.1% inflation over 10 years
Rate path: 2-year Treasury 4.63% vs Fed target 3.75-4.00% -- the bond market prices about 3 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score -0.20</summary>

```text
Last close 46.60 (bar of 2026-11-24), from 501 daily bars
Trend: vs 20d SMA 49.31 (-5.5%), 50d 50.76 (-8.2%), 200d 54.63 (-14.7%); 50d below 200d
Momentum: RSI(14) 31.3 | MACD -1.123 vs signal -0.790 (histogram -0.333)
Returns: 1d -1.0% | 5d -3.7% | 1m -5.1% | 3m -15.4%
52-week range: 46.02 - 64.26 (now 3.2% of the way up)
Volatility: ATR(14) 0.76 (1.6% of price) | annualised 20d 23.9%
Volume: 0.12x the 20-day average
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
Three-year record: +4.0% a year | beta to the market 0.47
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

<details><summary><b>What analysts and big funds say</b> — score +0.50</summary>

_Not available today._

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score +0.50</summary>

```text
Rolled up from the 5 largest holdings, 32.6% of the fund by weight
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 1.39 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +75.6% above the current prices
Holdings read: 0700.HK, 9988.HK, 00939, 01398, 1810.HK
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
Share count change: 1 week: +7.8% (404.17M) over 7d | 1 month: -2.1% (-122.01M) over 31d
Shares outstanding: 119.64M | fund size: 5.58B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Chip makers (SMH) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Neutral overall as no clear macro catalyst or decisive technical break is present; bullish analyst view and strong inflows are offset by bearish technicals and a risk‑off macro environment.

**Main reasons it gave:**
- Fund flows: +21.8% share count increase in 1 week (12.98B shares)
- Analyst view: 100% buy rating, weighted price target +56.9% above current price
- Technicals: price 435.32 below 20‑day SMA 484.28, RSI 38.7 (bearish momentum)
- Macro: VIX at 29.34 (stressed market) and high Treasury yields, risk‑off environment

<details><summary><b>News</b> — score +0.00</summary>

- [VanEck Semiconductor ETF (SMH) Stock Price, News, Quote & History](https://ca.finance.yahoo.com/quote/SMH/)  
  <sub>Yahoo! Finance Canada, 2 hours ago</sub>  
  VanEck Semiconductor ETF (SMH) · -5.68% · -17.69% · -24.70% · 19.44% · 33.06% · 184.32% · 790.16%. Key Events. Baseline. Advanced Chart. Loading chart...
- [Chip Stocks Just Had Their Fourth-Best Day Since 2000](https://247wallst.com/investing/2026/11/24/chip-stocks-just-had-their-fourth-best-day-since-2000/)  
  <sub>24/7 Wall St., 54 minutes ago</sub>  
  On Monday, November 23, 2026, the PHLX Semiconductor index closed at 9,588.05, up 14.03% from Friday's 8,408.59. The index tracks 30 of the largest...
- [Michael Burry cuts Nvidia puts by 75%, exits semiconductor ETF puts (NVDA:NASDAQ)](https://www.google.com/goto?url=CAESpAEBxCJF1wWRSJdkxeq_TCTDbIU48s4Q6i5k6hHIHvjCSQUZWDirqfIiSFQvqUF56bA3DXl-b--MXyNjJBPNM28RUICDwH66PT1EeHwKZmMA8juEPE3r9HmY2TfoAZRpfFW02qYJYKYpCzbhbstE_VYBHT6DWRB8e8ha_FUxVSbpjWhCgu8B_Ok_Vr6w3R-Sx_6gk9bi-s__dMq1nk0cvQK1lQ2-Sg&gsessionid=1wsF452r2diiD_xQs8QkFGsqw-EBbzg8djy_F-ZnW4bw48OwBB-t_A)  
  <sub>Seeking Alpha, 7 hours ago</sub>  
  Michael Burry sells 75% of his Nvidia bearish puts and buys long-dated calls as a hedge amid a reported SEC accounting probe.
- [Michael Burry cuts Nvidia puts by 75%, exits semiconductor ETF puts](https://www.google.com/goto?url=CAESvgEBxCJF1_M47f72NwHm6m2vzs-5K__gkAXx-jd-J5UVeh1OxaWTFaEBi4uKEj-gXQS_GA4Svxl8S9YokYuwwrYY2QFBXly0zUOFm23hUoU1IEwjBRjSNqKJJP2sm8oKd9OGDjCwgfbMwwfTjo_SsOllz9Pg41mO-VK9lLRKGMOACXjpVd2n-I8LptRQLLd7TsIfr8FEq5AeA5uPwB1X1v_6r2udo1tf4LQzpgV4gPNlr8Yu56A1MoS1OY9ou1bs&gsessionid=1wsF452r2diiD_xQs8QkFGsqw-EBbzg8djy_F-ZnW4bw48OwBB-t_A)  
  <sub>TradingView, 7 hours ago</sub>  
  'The Big Short' investor Michael Burry has sold 75% of his bearish put options on Nvidia NASDAQ:NVDA and purchased long-dated call options as a hedge,...
- [EEM Now Moves Like A Chip Fund](https://www.google.com/goto?url=CAESnwEBxCJF11IGXHHVzduwAt1yKSSMuxm2BlJHEVPqgyYlNgQRhafHYXW5AIyNAp-6Fo-d1wap75_so6BE_g4dG-Zh2zirwlURCJnr9FbBnyAXi9jDDvZRq22nyd2vLe41tQZdHbjSj0QJuwGSYPEPU-WBl2HTLHofFa9hV4oZpiZLv42pqDS_s76-d9jA-VI-ZaPWgTMwA3509-eOJyyaU90&gsessionid=1wsF452r2diiD_xQs8QkFGsqw-EBbzg8djy_F-ZnW4bw48OwBB-t_A)  
  <sub>Trefis, 16 hours ago</sub>  
  Today's big story: Reported SEC Probe: Could Nvidia Stock Fall To $92? Update, Nov 23: After Nvidia's board reinstated Jensen Huang as CEO on Nov 22,...
- [Should You Invest in the First Trust NASDAQ Semiconductor ETF (FTXL)?](https://www.google.com/goto?url=CAESpQEBxCJF1wmE9Q8icX7wh-Q19wkX2pPqdI0GzHiNqiQ0kPaE7LatuT1ObQN0S8kFRz9wnP8LvotKfCdGez9J3d1YRfnvZ5b752grakQheoyNe0l6jrc7lBKiprJnvxvut9ZE58Mr-llDKqi1Nbs7bohzncePpFy_0Fqc77-fREURCE-O3LhVhbyizXvDQG5hOsuhhrtObn46Q2wuCQ17QkYBTR5a9eE&gsessionid=1wsF452r2diiD_xQs8QkFGsqw-EBbzg8djy_F-ZnW4bw48OwBB-t_A)  
  <sub>Yahoo Finance, 4 hours ago</sub>  
  Looking for broad exposure to the Technology - Semiconductors segment of the equity market? You should consider the First Trust NASDAQ Semiconductor ETF...
- [Why is SMH stock up today? The chip ETF jumps about 16% as Nvidia soars on Jensen Huang's return](https://www.google.com/goto?url=CAESsAEBxCJF13AutPPlPSHf-_dyy_G-NlqCnBc1EokcCxKE0zyvrxGO7WpITz0xA3SlUysJ-PQaF3lvGCgoudMu0pqLAisKqNNDO3mNOgAWyrlCZ5UiCJeUgMsHf-8aED91CQAuo84l3UC9DzHFAeA5Bw2obvFUloye_gKJ9SsI0GqApQ5D5pn05fEBrYIyV7Y9cU8PTZ9WnPzrFiWOJiIJvowYdGtseS_5TACHOJPm7bmRUQ&gsessionid=1wsF452r2diiD_xQs8QkFGsqw-EBbzg8djy_F-ZnW4bw48OwBB-t_A)  
  <sub>Nacionale, 23 hours ago</sub>  
  SMH, the VanEck Semiconductor ETF, jumped Monday as Nvidia surged on Jensen Huang's reinstatement. What the fund holds and why it moved so much.
- [Nvidia's 33% jump on Huang's return may supply roughly a fifth to a quarter of the S&P 500's rebound](https://www.google.com/goto?url=CAESpgEBxCJF1_p0ECMgRFQ-iIdd8-A_MwL4UwZohkV7axFAJKGpTGCd2Xhd4D9xc7D0ZsHK108lOihliXwLs0R2zCJUwxksp19gWqdsgaCwq-qyVBmvQ5E5Ftf59zsfnOke7ZLOxLjwvoLydBBi7XUNQVCUZvIwWUWUTGTAlEFQmpR4zW95SNPCo-xQnvEfqje3RqBHqOyxXTQehbkcrqJd9sbh0zI03h6N&gsessionid=1wsF452r2diiD_xQs8QkFGsqw-EBbzg8djy_F-ZnW4bw48OwBB-t_A)  
  <sub>Quantisnow, 23 hours ago</sub>  
  By rough estimate, Nvidia added about $750 billion in market value by 10:20 a.m. ET, while the equal-weight S&P 500 fund rose 2.32%, less than half of SPY's...
- [Anthropic Went Public Into An AI Selloff, And Its Numbers Argue Against It (SMH)](https://www.google.com/goto?url=CAESrAEBxCJF12F25tcX-4T7ktuDNbpEzncRIrTzKg8GfLWV9MsrvxFSJhGhg4JyN41yj_ZrkcJG6Ry-I94Qt6ZUulsAI4lmdakas0sFuzA97mZEkgoSB34-wLrfjUCARCpSzULYGPDgMvNwiqZP1Gvr_Ik-oLZbemDoVN4zs9oVnfjXYAWSchUD7QnzlGU_Dp1I5R37N6-tHL5T3Zf7LetdXKKvEoHwGdH5njYq1OT0&gsessionid=1wsF452r2diiD_xQs8QkFGsqw-EBbzg8djy_F-ZnW4bw48OwBB-t_A)  
  <sub>Seeking Alpha, 20 hours ago</sub>  
  Analyst rates VanEck Semiconductor ETF a Buy for AI infrastructure exposure and equipment hedges, with memory looking oversold at 2–2.4x forward EBITDA.
- [Michael Burry Bought Nvidia Calls, Cut His Semiconductor Shorts Before The Rally – But He’s Not Done Questioning Jensen Huang](https://www.google.com/goto?url=CAESiAIBxCJF1w9ZfMMdg1d62c_OW5L4uYQOvLu3RvnbRVb8NWWUzIqFfeXYvuLzyOsR0otQSYBf3QC9kVtkH8Ei0j1UgOMevE7TS9PVR5DZMsy3bqeOMMrdcQ7IFLtvNMQfNZUPqMlO_eFsPXINhGQV9k78KFvtK4MR2nc6UWKREYl3lDjqV6E38gb6wJ5mHl3x7aYgTmGcAyAX7ImRzvsg05Q7YzhIMFE8eS9VxXCbrfLw_Yxlw3Mf_JO8wlNgGJPyhtNCEdJvWv9v2ot4D9u6Bpg1kF5tumzLN6RCRUkkn2D58mZ6D3cOKeRjUCl-kWesUV9M9-GLd3urfFaT3j6ZPhAXiTushBiza04&gsessionid=1wsF452r2diiD_xQs8QkFGsqw-EBbzg8djy_F-ZnW4bw48OwBB-t_A)  
  <sub>TradingView, 11 hours ago</sub>  
  Michael Burry called Jensen Huang's return as Nvidia (NVDA) CEO a “huge sign of weakness,” saying it showed how much the chipmaker's deals and customer...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.17% (+0.03 on the week) | 5-year 4.71% (-0.19 on the week) | 10-year 4.90% (-0.20 on the week) | 30-year 5.29% (-0.17 on the week)
Yield curve, 10-year minus 3-month: +0.73 points -- upward sloping (normal)
US dollar index: 103.81 (+0.32 on the week)
Volatility (VIX): 29.34 (+3.9 on the week) -- stressed
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.1% (2026-10-01) | jobless claims 203k (2026-11-14)
Policy and expectations: Fed target 4.00% | market expects 2.1% inflation over 10 years
Rate path: 2-year Treasury 4.63% vs Fed target 3.75-4.00% -- the bond market prices about 3 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score -0.40</summary>

```text
Last close 435.32 (bar of 2026-11-24), from 501 daily bars
Trend: vs 20d SMA 484.28 (-10.1%), 50d 543.75 (-19.9%), 200d 525.61 (-17.2%); 50d above 200d
Momentum: RSI(14) 38.7 | MACD -29.975 vs signal -27.190 (histogram -2.785)
Returns: 1d -5.4% | 5d -5.4% | 1m -19.6% | 3m -21.7%
52-week range: 339.12 - 668.91 (now 29.2% of the way up)
Volatility: ATR(14) 29.28 (6.7% of price) | annualised 20d 92.7%
Volume: 0.17x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.30</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score +0.30</summary>

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
Rolled up from the 5 largest holdings, 46.4% of the fund by weight
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 1.62 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +56.9% above the current prices
Holdings read: NVDA, TSM, TXN, AVGO, AMD
Recent rating changes among them:
  - NVDA: 2026-11-12 Melius Research: down, Buy -> Hold
  - TSM: 2026-11-04 Bernstein: main, Outperform -> Outperform
  - TXN: 2026-10-22 Jefferies: main, Hold -> Hold
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
Share count change: 1 week: +21.8% (12.98B) over 7d | 1 month: +23.7% (13.85B) over 32d
Shares outstanding: 166.30M | fund size: 72.40B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Turkey (TUR) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:** no explanation. It wrote only “NEUTRAL”, so the main reasons below are all it gave.

**Main reasons it gave:**
- Analyst coverage of top holdings (44.9% weight) shows 100% buy rating and +38.3% price target
- Fund flows flat (0% change) over 1 week and 1 month
- ETF trading below 20‑day, 50‑day, and 200‑day SMAs; RSI 35.3; volume 0.04× 20‑day average
- Macro environment shows no policy or data surprise; yields stable, VIX modestly higher

<details><summary><b>News</b> — score +0.00</summary>

- [VanEck Vietnam ETF (VNM) Stock Price, News, Quote & History](https://ca.finance.yahoo.com/quote/VNM/)  
  <sub>Yahoo! Finance Canada, 19 hours ago</sub>  
  Find the latest VanEck Vietnam ETF (VNM) stock quote, history, news and other vital information to help you with your stock trading and investing.
- [Why (TUR) Price Action Is Critical for Tactical Trading](https://news.stocktradersdaily.com/news_release/8/Why_TUR_Price_Action_Is_Critical_for_Tactical_Trading_112326101401_1795490041.html)  
  <sub>Stock Traders Daily, 17 hours ago</sub>  
  Key findings for Ishares Msci Turkey Etf (NYSE: TUR). Weak Near-Term Sentiment Could Catalyze Bearish Positioning; No clear price positioning signal...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.17% (+0.03 on the week) | 5-year 4.71% (-0.19 on the week) | 10-year 4.90% (-0.20 on the week) | 30-year 5.29% (-0.17 on the week)
Yield curve, 10-year minus 3-month: +0.73 points -- upward sloping (normal)
US dollar index: 103.81 (+0.32 on the week)
Volatility (VIX): 29.34 (+3.9 on the week) -- stressed
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.1% (2026-10-01) | jobless claims 203k (2026-11-14)
Policy and expectations: Fed target 4.00% | market expects 2.1% inflation over 10 years
Rate path: 2-year Treasury 4.63% vs Fed target 3.75-4.00% -- the bond market prices about 3 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 29.66 (bar of 2026-11-24), from 501 daily bars
Trend: vs 20d SMA 30.97 (-4.2%), 50d 32.95 (-10.0%), 200d 38.24 (-22.4%); 50d below 200d
Momentum: RSI(14) 35.3 | MACD -0.736 vs signal -0.694 (histogram -0.042)
Returns: 1d -1.1% | 5d -6.3% | 1m -3.8% | 3m -26.9%
52-week range: 29.53 - 43.74 (now 0.9% of the way up)
Volatility: ATR(14) 0.62 (2.1% of price) | annualised 20d 34.6%
Volume: 0.04x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.00</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score +0.00</summary>

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
Rolled up from the 5 largest holdings, 44.9% of the fund by weight
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 1.54 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +38.3% above the current prices
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
Share count change: 1 week: +0.0% (0.00) over 7d | 1 month: +0.0% (0.00) over 31d
Shares outstanding: 15.65M | fund size: 464.18M
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### US real estate (VNQ) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Neutral overall: bullish analyst consensus and net inflows are offset by bearish technicals and modestly overvalued fundamentals in a unchanged macro environment.

**Main reasons it gave:**
- Weekly share count rose 4.2% indicating net inflows
- Analyst consensus all buy with weighted price target +17.7% above current price
- Technical indicators bearish: price below 20‑day and 200‑day SMA, negative MACD, RSI 47.7
- Weak near‑term sentiment noted in news
- Macro unchanged: yields fell modestly, no policy surprise, VIX elevated

<details><summary><b>News</b> — score +0.00</summary>

- [Vanguard Real Estate Index Fund ETF Shares (VNQ) Stock Price, News, Quote & History](https://ca.finance.yahoo.com/quote/VNQ/)  
  <sub>Yahoo! Finance Canada, 14 hours ago</sub>  
  Vanguard Real Estate Index Fund ETF Shares (VNQ) · -2.66% · 1.06% · -3.20% · 4.99% · 4.58% · -13.97% · 87.90%. Key Events. Baseline.
- [(VNQ) Risk Channels and Responsive Allocation](https://news.stocktradersdaily.com/news_release/132/VNQ_Risk_Channels_and_Responsive_Allocation_112426035802_1795510682.html)  
  <sub>Stock Traders Daily, 11 hours ago</sub>  
  Key findings for Vanguard Real Estate Index Fund Etf (NYSE: VNQ). Weak Near-Term Sentiment Could Catalyze Bearish Positioning; A mid-channel oscillation...
- [ETFs Investing in SmartStop Self Storage REIT, Inc. Stocks](https://www.google.com/goto?url=CAEScwHEIkXXL-OnYEYE_1-n-eS8veJhApn6VIozY_slxqTAkowiXW_KDm1HxdsYmVqh9doaaEKspNj58sxTtQRnUuxAgmEd4-8mSNjcrxWDR85uNJ9UQmSaJajiG1M3debVs0S5qq7Ib6G9QlZgNZ4lhBZgU_Q&gsessionid=xr0vPEus4Z59LjT6G-KpJOeiOYqzeG4R1M1vpcTz7VTSCAtrE03Hzg)  
  <sub>TradingView, 23 hours ago</sub>  
  Explore funds investing in A40UUF in a single list with price, expense ratio, and more stats for an in-depth analysis of new opportunities.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.17% (+0.03 on the week) | 5-year 4.71% (-0.19 on the week) | 10-year 4.90% (-0.20 on the week) | 30-year 5.29% (-0.17 on the week)
Yield curve, 10-year minus 3-month: +0.73 points -- upward sloping (normal)
US dollar index: 103.81 (+0.32 on the week)
Volatility (VIX): 29.34 (+3.9 on the week) -- stressed
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.1% (2026-10-01) | jobless claims 203k (2026-11-14)
Policy and expectations: Fed target 4.00% | market expects 2.1% inflation over 10 years
Rate path: 2-year Treasury 4.63% vs Fed target 3.75-4.00% -- the bond market prices about 3 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 93.86 (bar of 2026-11-24), from 501 daily bars
Trend: vs 20d SMA 95.19 (-1.4%), 50d 92.87 (+1.1%), 200d 95.00 (-1.2%); 50d below 200d
Momentum: RSI(14) 47.7 | MACD 0.196 vs signal 0.629 (histogram -0.432)
Returns: 1d +0.2% | 5d -1.1% | 1m +0.7% | 3m -4.8%
52-week range: 87.00 - 100.95 (now 49.2% of the way up)
Volatility: ATR(14) 1.43 (1.5% of price) | annualised 20d 20.4%
Volume: 0.15x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score -0.15</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score -0.15</summary>

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
Rolled up from the 5 largest holdings, 40.2% of the fund by weight
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 1.56 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +17.7% above the current prices
Holdings read: VRTPX, WELL, PLD, EQIX, AMT
Recent rating changes among them:
  - WELL: 2026-11-11 UBS: main, Buy -> Buy
  - PLD: 2026-11-02 Wells Fargo: main, Overweight -> Overweight
  - EQIX: 2026-10-29 JP Morgan: main, Overweight -> Overweight
  - AMT: 2026-11-05 Argus Research: reit, Buy -> Buy
```

</details>

<details><summary><b>Buying and selling by company insiders</b> — score +0.35</summary>

_Not available today._

</details>

<details><summary><b>Who is positioned how</b> — score +0.35</summary>

_Not available today._

</details>

<details><summary><b>Money going into and out of this fund</b> — score +0.35</summary>

```text
Direction: money coming in (1 month)
Share count change: 1 week: +4.2% (2.86B) over 7d | 1 month: +3.4% (2.29B) over 32d
Shares outstanding: 750.58M | fund size: 70.45B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### US house builders (XHB) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> The fund shows strong recent inflows (+5.7% weekly, +17.1% monthly) indicating demand, while analyst coverage is thin (18.9% of the fund) but uniformly bullish (100% buy, +11.9% price target). However, macro conditions are risk‑off (yields rising, VIX at 29.34) and technicals are weak (price below 20‑day SMA, MACD negative, low volume). These opposing forces balance out, leading to a neutral overall view.

**Main reasons it gave:**
- Weekly inflows +5.7% (90.6M shares) indicate strong demand
- Analyst coverage thin (18.9% of fund) but 100% buy rating with +11.9% price target
- Macro risk: yields up, VIX high (29.34) suggests risk‑off sentiment
- Technical: price below 20‑day SMA, MACD negative, low volume

<details><summary><b>News</b> — score +0.00</summary>

- [Responsive Playbooks and the XHB Inflection](https://news.stocktradersdaily.com/news_release/132/Responsive_Playbooks_and_the_XHB_Inflection_112426084602_1795527962.html)  
  <sub>Stock Traders Daily, 6 hours ago</sub>  
  Key findings for Spdr Homebuilders Etf (NYSE: XHB). Weak Near and Mid-Term Sentiment Could Pressure Neutral Long-Term Outlook; Resistance is being tested.
- [(XHB) Financial Trading Report (XHB:CA)](https://www.google.com/goto?url=CAESkwEBxCJF11LvTJR5MhwirrD9VlXbH6iOdckYP860E6e2LSa0H3QirEPWJAKV8schHGMLYHp1apbEil2vqlWOWHjHMsiWigDp3cKfc4VPsQ8uUTEIddwwEiU2A2Y_pCK_VGz9H8FxEPOt99yY9LAqV54SCVSN_d6Sxlpw8X0TwZUnq4swFmFanBED4NL7EEWPxV-_4Ss&gsessionid=8VCthMZdA5-Zh24JgYzJMlv8JzIQ2hqWdOt-5IJjj5y0F326OAL-9g)  
  <sub>Stock Traders Daily, 16 hours ago</sub>  
  Financial Trading Report for iShares Canadian HYBrid Corporate Bond Index ETF (XHB) with Buy and Sell Indicators.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.17% (+0.03 on the week) | 5-year 4.71% (-0.19 on the week) | 10-year 4.90% (-0.20 on the week) | 30-year 5.29% (-0.17 on the week)
Yield curve, 10-year minus 3-month: +0.73 points -- upward sloping (normal)
US dollar index: 103.81 (+0.32 on the week)
Volatility (VIX): 29.34 (+3.9 on the week) -- stressed
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.1% (2026-10-01) | jobless claims 203k (2026-11-14)
Policy and expectations: Fed target 4.00% | market expects 2.1% inflation over 10 years
Rate path: 2-year Treasury 4.63% vs Fed target 3.75-4.00% -- the bond market prices about 3 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score -0.20</summary>

```text
Last close 99.07 (bar of 2026-11-24), from 501 daily bars
Trend: vs 20d SMA 101.51 (-2.4%), 50d 98.49 (+0.6%), 200d 104.20 (-4.9%); 50d below 200d
Momentum: RSI(14) 47.9 | MACD -0.076 vs signal 0.525 (histogram -0.601)
Returns: 1d -0.6% | 5d -0.0% | 1m +1.1% | 3m -6.5%
52-week range: 92.84 - 121.36 (now 21.9% of the way up)
Volatility: ATR(14) 2.87 (2.9% of price) | annualised 20d 41.0%
Volume: 0.01x the 20-day average
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

<details><summary><b>What analysts and big funds say</b> — score +0.30</summary>

_Not available today._

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score +0.30</summary>

```text
Rolled up from the 5 largest holdings, 18.9% of the fund by weight  -- thin, so read this as a fact about that slice rather than the fund
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 1.73 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +11.9% above the current prices
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
Share count change: 1 week: +5.7% (90.64M) over 7d | 1 month: +17.1% (244.87M) over 31d
Shares outstanding: 16.89M | fund size: 1.67B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### US materials and chemicals (XLB) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Neutral overall; bullish analyst coverage is offset by bearish technicals and flat fund flows, with no macro surprise.

**Main reasons it gave:**
- Technical trend: price below 20‑day, 50‑day, and 200‑day SMAs; RSI 42.1 and MACD negative indicating bearish momentum
- Fund flows flat over the past week and month, showing no net inflow or outflow
- Analyst coverage of top holdings (34% of fund) all buy with weighted price target +14.1% above current price
- Macro: no surprise data releases; yields stable, VIX up but no policy shift

<details><summary><b>News</b> — score +0.00</summary>

- [State Street Materials Select Sector SPDR ETF (XLB) Stock Price, News, Quote & History](https://ca.finance.yahoo.com/quote/XLB/)  
  <sub>Yahoo! Finance Canada, 14 hours ago</sub>  
  State Street Materials Select Sector SPDR ETF (XLB) · -3.05% · -2.75% · -0.78% · 10.03% · 15.58% · 12.72% · 380.24%. Key Events. Baseline.
- [BATT vs. LIT: Why 2 Battery ETFs Deliver Different Exposure](https://www.google.com/goto?url=CAESlgEBxCJF19LcMoTv1sJfTr28Hw01U2WaLIYU4rlZyahxo9fc1VE_kDMh-VYttmzM8nr_k_YOS4Ea5QaEXSEsZCpvVIRwJYUM0xl_-Plc37jMx2HhwEBrBs6qNtNgAtLhVAxcKc0X7OyuOhqb7ULAyYIj06iOOhp1gCn6M-tQUO1foxSfxQIokHhmJHQFgAxPdVUJuUv2Pjo&gsessionid=VqQuwGRedRFh-0le2urof8UwK6MESqpot2q4qS7uyX6_lyp6P4A2rg)  
  <sub>ETF Database, 19 hours ago</sub>  
  When investors look to capture the electrification and energy storage theme, the Amplify Lithium & Battery Technology ETF (BATT ) and the Global X Lithium...
- [State Street Industrial Select Sector SPDR ETF (XLI) stock price, news, quote and history](https://www.google.com/goto?url=CAESZAHEIkXX7-_Yw_P3LvdPxEA76FpUM_eQ9DQWhGLfNNtT7nI_0rbYgNlkrMInA-AWNuj2h_-UIS045irr8baJ3Af08k3kg7YTouAdQpS0fskeU5Ncas38ChC3ZzJ7EKChjphx7yg&gsessionid=VqQuwGRedRFh-0le2urof8UwK6MESqpot2q4qS7uyX6_lyp6P4A2rg)  
  <sub>Yahoo Finance Singapore, 21 hours ago</sub>  
  Find the latest State Street Industrial Select Sector SPDR ETF (XLI) stock quote, history, news and other vital information to help you with your stock...
- [ValuEngine Weekly Market Commentary: Bear Market For Nasdaq-100 Headlines Historic Weekly Meltdown](https://www.google.com/goto?url=CAESyAEBxCJF17dbznrnvKsSP-oQ8kAkf755LPWtRY-F6EqoGbGKJAvmk3535G9gT-2qVTRDKewCrzyeJY-31Czb0Le5fLHpqeR-j5bIPg-QqEy3IakA_SgiU1N9DpKWG8FICl4_R_lYnDh6JLbe99sCSmhM4I6VN0QjhdrmD0WRjLbpTpoqw1wnb_GAovnm907GK5zDnbERmlw0z81IpIcMM4e_dt3M1x1hvHM0wWTtghlyB3MAaa4hI5XVgqbDsTnObNS5UU3FF3AD5w&gsessionid=VqQuwGRedRFh-0le2urof8UwK6MESqpot2q4qS7uyX6_lyp6P4A2rg)  
  <sub>Seeking Alpha, 9 hours ago</sub>  
  U.S. equity markets experienced a sharp and broad-based selloff this week, with all major ETFs and sector benchmarks posting significant declines.
- [Industrial Select Sector SPDR ETF (XLI) stock price, news, quote and history](https://www.google.com/goto?url=CAESZAHEIkXXwUSfN469ORttxOY25_ZW0nrwYscz8XMWrivqX4xpgfq6H0UYZiRisUTSbBN5OUwPlsn3fcDuhWS8lgYM35Bx6v69zORE2JsrmIXwqshbL1V_etm1J2yEPjRM_bsNf2Y&gsessionid=VqQuwGRedRFh-0le2urof8UwK6MESqpot2q4qS7uyX6_lyp6P4A2rg)  
  <sub>Yahoo Finance UK, 20 hours ago</sub>  
  Find the latest Industrial Select Sector SPDR ETF (XLI) stock quote, history, news and other vital information to help you with your stock trading and...
- [State Street Industrial Select Sector SPDR ETF (XLI) Stock Price, News, Quote & History](https://www.google.com/goto?url=CAESZAHEIkXXQ6n0cKd1Q2HwnxSND6W59PIrUD9kdu00b3eljoriXDtc3kMNudX8dl9UTIRYwGwAndR0_EZdb8kAPon8iCo0gKUQOT8LL_FoYhvmcFUhOljckl3M4sXrUhoaCQ5nisk&gsessionid=VqQuwGRedRFh-0le2urof8UwK6MESqpot2q4qS7uyX6_lyp6P4A2rg)  
  <sub>Yahoo! Finance Canada, 20 hours ago</sub>  
  Find the latest State Street Industrial Select Sector SPDR ETF (XLI) stock quote, history, news and other vital information to help you with your stock...
- [State Street Health Care Select Sector SPDR ETF (XLV) stock price, news, quote and history](https://www.google.com/goto?url=CAESZAHEIkXXjyEnmkbM29KFZRWWqoK7G6xvAeiR5tapRuKeQksWeeuYddfDGgTjZTRDCSA7D_9XwG4V6W3p-kEMN2m_R3Jb8GnyC8cuCcSIDDxb5gnDSU7QN8y-kmkQ4_Uh_9ch19U&gsessionid=VqQuwGRedRFh-0le2urof8UwK6MESqpot2q4qS7uyX6_lyp6P4A2rg)  
  <sub>Yahoo Finance UK, 19 hours ago</sub>  
  Find the latest State Street Health Care Select Sector SPDR ETF (XLV) stock quote, history, news and other vital information to help you with your stock...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.17% (+0.03 on the week) | 5-year 4.71% (-0.19 on the week) | 10-year 4.90% (-0.20 on the week) | 30-year 5.29% (-0.17 on the week)
Yield curve, 10-year minus 3-month: +0.73 points -- upward sloping (normal)
US dollar index: 103.81 (+0.32 on the week)
Volatility (VIX): 29.34 (+3.9 on the week) -- stressed
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.1% (2026-10-01) | jobless claims 203k (2026-11-14)
Policy and expectations: Fed target 4.00% | market expects 2.1% inflation over 10 years
Rate path: 2-year Treasury 4.63% vs Fed target 3.75-4.00% -- the bond market prices about 3 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score -0.30</summary>

```text
Last close 49.85 (bar of 2026-11-24), from 501 daily bars
Trend: vs 20d SMA 51.76 (-3.7%), 50d 50.76 (-1.8%), 200d 51.22 (-2.7%); 50d below 200d
Momentum: RSI(14) 42.1 | MACD -0.440 vs signal -0.033 (histogram -0.406)
Returns: 1d -0.1% | 5d -1.9% | 1m -3.0% | 3m -7.1%
52-week range: 43.26 - 53.90 (now 61.9% of the way up)
Volatility: ATR(14) 1.01 (2.0% of price) | annualised 20d 26.4%
Volume: 0.09x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.20</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score +0.20</summary>

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
Rolled up from the 5 largest holdings, 34.0% of the fund by weight
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 1.65 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +14.1% above the current prices
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
Share count change: 1 week: +0.0% (0.00) over 7d | 1 month: +0.0% (0.00) over 31d
Shares outstanding: 71.92M | fund size: 3.59B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### US energy companies (XLE) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> No macro surprise or decisive technical break; bearish fundamentals (inventory builds and falling price outlook) offset bullish analyst coverage and flat fund flows, leading to a neutral stance.

**Main reasons it gave:**
- Weekly EIA inventories show builds in crude (+3.4 M bbl) and natural gas (+20 Bcf), indicating bearish supply pressure
- EIA price outlook projects WTI crude falling to $84 in six months (≈13% decline) and natural gas to $2.37 (≈11% decline)
- Analyst coverage of top holdings is 100% buy with a +17.2% price target, indicating bullish sentiment
- Fund flows flat over the past month (0% net change), indicating neutral demand

<details><summary><b>News</b> — score +0.00</summary>

- [If Inflation Stays Hot, These 5 ETFs Could Be Smart Buys](https://www.theglobeandmail.com/investing/markets/stocks/XLE-A/pressreleases/8971668/if-inflation-stays-hot-these-5-etfs-could-be-smart-buys/)  
  <sub>The Globe and Mail, 17 hours ago</sub>  
  Detailed price information for S&P 500 Energy Sector SPDR (XLE-A) from The Globe and Mail including charting and trades.
- [5 ETFs that can help protect your portfolio fro...](https://pluang.com/en/news-feed/etf-untuk-lindung-nilai-inflasi-di-pasar-bergejolak)  
  <sub>Pluang, 18 hours ago</sub>  
  Inflation reduces the purchasing power of cash, prompting investors to seek assets that can hedge against these losses. Five ETFs are highlighted for their...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.17% (+0.03 on the week) | 5-year 4.71% (-0.19 on the week) | 10-year 4.90% (-0.20 on the week) | 30-year 5.29% (-0.17 on the week)
Yield curve, 10-year minus 3-month: +0.73 points -- upward sloping (normal)
US dollar index: 103.81 (+0.32 on the week)
Volatility (VIX): 29.34 (+3.9 on the week) -- stressed
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.1% (2026-10-01) | jobless claims 203k (2026-11-14)
Policy and expectations: Fed target 4.00% | market expects 2.1% inflation over 10 years
Rate path: 2-year Treasury 4.63% vs Fed target 3.75-4.00% -- the bond market prices about 3 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 60.10 (bar of 2026-11-24), from 501 daily bars
Trend: vs 20d SMA 63.72 (-5.7%), 50d 64.49 (-6.8%), 200d 59.80 (+0.5%); 50d above 200d
Momentum: RSI(14) 34.2 | MACD -1.397 vs signal -0.925 (histogram -0.472)
Returns: 1d +0.4% | 5d -5.1% | 1m -13.7% | 3m -3.7%
52-week range: 43.81 - 70.02 (now 62.2% of the way up)
Volatility: ATR(14) 1.47 (2.4% of price) | annualised 20d 30.1%
Volume: 0.11x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score -0.50</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score -0.50</summary>

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
  Natural gas: 3,882.0 billion cubic feet, +20.0 on the week (a build), 96% percentile over 52 weeks -- high for the time of year
A build is more supply than demand and a draw is the reverse, so a build reads bearish and a draw bullish -- as a rule of thumb, not a law. Weigh the change and how unusual the level is above the level itself, and remember the market has already seen this number.
```

</details>

<details><summary><b>How the crop is growing</b> — score -0.50</summary>

_Not available today._

</details>

<details><summary><b>What analysts and big funds say</b> — score +0.50</summary>

_Not available today._

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score +0.50</summary>

```text
Rolled up from the 5 largest holdings, 59.0% of the fund by weight
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 2.10 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +17.2% above the current prices
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
Share count change: 1 week: +0.0% (0.00) over 7d | 1 month: +0.0% (0.00) over 31d
Shares outstanding: 186.42M | fund size: 11.21B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### US banks and finance (XLF) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Neutral overall; no macro surprise, no decisive technical break, flat fund flows, and moderate analyst optimism that does not outweigh other neutral factors.

**Main reasons it gave:**
- Yield curve unchanged (+0.73) and no rate surprise this week
- Technical indicators show price below 20‑day SMA, low volume, and no decisive break
- Analyst coverage of top holdings is bullish (+10.4% price target) but only covers 43.3% of the fund
- Fund flows flat over the past month, indicating no net demand shift

<details><summary><b>News</b> — score +0.00</summary>

- [What State Street Fin Select Sector SPDR (XLF) Bought: Berkshire Leads on Nov. 20](http://www.bing.com/news/apiclick.aspx?ref=FexRss&aid=&tid=6b05a328c78f44a58fb2cd667e3b84ae&url=https%3a%2f%2ffinance.yahoo.com%2fmarkets%2fstocks%2farticles%2fstate-street-fin-select-sector-110322872.html&c=2675100394789210276&mkt=en-us)  
  <sub>Yahoo Finance, 12h ago</sub>  
  XLF is an Equity Sector Financials equity fund holding 76 stocks, with 57.3% of assets in its 10 largest holdings. Financial Services accounts for 98.2% of classified stocks, Technology 1.6% and ...
- [Should you invest in the Fidelity MSCI Financials Index ETF (FNCL)?](http://www.bing.com/news/apiclick.aspx?ref=FexRss&aid=&tid=6b05a328c78f44a58fb2cd667e3b84ae&url=https%3a%2f%2fwww.msn.com%2fen-us%2fnews%2fother%2fshould-you-invest-in-the-fidelity-msci-financials-index-etf-fncl%2far-AA2i7cOG&c=14654517128919571705&mkt=en-us)  
  <sub>Zacks Investment Research on MSN, 12h ago</sub>  
  Designed to provide broad exposure to the Financials - Broad segment of the equity market, the Fidelity MSCI Financials Index ETF (FNCL) is a passively managed exchange traded fund launched on October ...
- [ETFs Bought $120 Million of Mastercard (MA) on Friday](http://www.bing.com/news/apiclick.aspx?ref=FexRss&aid=&tid=6b05a328c78f44a58fb2cd667e3b84ae&url=https%3a%2f%2fuk.finance.yahoo.com%2fnews%2fetfs-bought-120-million-mastercard-110212516.html&c=12703299396891498712&mkt=en-us)  
  <sub>Yahoo Finance UK, 17h ago</sub>  
  SPY led the move with a $82.7 million increase in value, lifting its stake by 1.34% to 9,980,354 shares. XLF added $32.6 million, raising its position 0.99% to 5,330,769 shares, while IWF contributed ...
- [ETFs Are Buying JPMorgan Chase (JPM) on Friday](http://www.bing.com/news/apiclick.aspx?ref=FexRss&aid=&tid=6b05a328c78f44a58fb2cd667e3b84ae&url=https%3a%2f%2ffinance.yahoo.com%2fmarkets%2fstocks%2farticles%2fetfs-buying-jpmorgan-chase-jpm-110146498.html&c=1990413607565461728&mkt=en-us)  
  <sub>Yahoo Finance, 12h ago</sub>  
  Thirty-nine ETFs were buying JPMorgan Chase (JPM) shares versus 15 selling in Friday's session, a net $180.0 million of ETF buying by dollar value. The buying extended a two-day streak in the same ...
- [美股避險基金做空個股速度創4年新高 金融股成重災區](http://www.bing.com/news/apiclick.aspx?ref=FexRss&aid=&tid=6b05a328c78f44a58fb2cd667e3b84ae&url=https%3a%2f%2ftw.stock.yahoo.com%2fnews%2f%25E7%25BE%258E%25E8%2582%25A1%25E9%2581%25BF%25E9%259A%25AA%25E5%259F%25BA%25E9%2587%2591%25E5%2581%259A%25E7%25A9%25BA%25E5%2580%258B%25E8%2582%25A1%25E9%2580%259F%25E5%25BA%25A6%25E5%2589%25B54%25E5%25B9%25B4%25E6%2596%25B0%25E9%25AB%2598-%25E9%2587%2591%25E8%259E%258D%25E8%2582%25A1%25E6%2588%2590%25E9%2587%258D%25E7%2581%25BD%25E5%258D%2580-014222156.html&c=4107628203585025562&mkt=en-us)  
  <sub>tw.stock, 23h ago</sub>  
  商傳媒｜方承業／綜合外電報導美股市場近期遭遇劇烈拋售潮。根據投資銀行高盛（Goldman Sachs）最新發布的資金流向報告，全球避險基金正以2022年6月以來的最快速度拋售並做空美國單一股票，做空力道遠遠壓過買盤。 避險基金的操作策略通常結合多頭買進與空頭避險。報告指出，機構投資人已連續第三週淨賣出美股，上週更出現天天做空單一股票的罕見現象，整體做空規模與買盤比例高達1.4比1。做空是指投資人預 ...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.17% (+0.03 on the week) | 5-year 4.71% (-0.19 on the week) | 10-year 4.90% (-0.20 on the week) | 30-year 5.29% (-0.17 on the week)
Yield curve, 10-year minus 3-month: +0.73 points -- upward sloping (normal)
US dollar index: 103.81 (+0.32 on the week)
Volatility (VIX): 29.34 (+3.9 on the week) -- stressed
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.1% (2026-10-01) | jobless claims 203k (2026-11-14)
Policy and expectations: Fed target 4.00% | market expects 2.1% inflation over 10 years
Rate path: 2-year Treasury 4.63% vs Fed target 3.75-4.00% -- the bond market prices about 3 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 56.02 (bar of 2026-11-24), from 501 daily bars
Trend: vs 20d SMA 57.17 (-2.0%), 50d 55.83 (+0.3%), 200d 54.03 (+3.7%); 50d above 200d
Momentum: RSI(14) 46.6 | MACD -0.070 vs signal 0.283 (histogram -0.354)
Returns: 1d +0.7% | 5d -1.8% | 1m +0.0% | 3m -3.8%
52-week range: 47.81 - 59.20 (now 72.1% of the way up)
Volatility: ATR(14) 0.99 (1.8% of price) | annualised 20d 25.0%
Volume: 0.15x the 20-day average
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

<details><summary><b>What analysts and big funds say</b> — score +0.70</summary>

_Not available today._

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score +0.70</summary>

```text
Rolled up from the 5 largest holdings, 43.3% of the fund by weight
Ratings by weight: buy 70.7% | hold 29.3% | sell 0.0% (mean 2.00 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +10.4% above the current prices
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
Share count change: 1 week: +0.0% (0.00) over 7d | 1 month: +0.0% (0.00) over 31d
Shares outstanding: 883.44M | fund size: 49.49B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### US industry (XLI) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Neutral overall; macro data unchanged, technicals bearish but not decisive, fund flows flat, analyst coverage thin despite bullish rating.

**Main reasons it gave:**
- US Treasury yields stable this week (3‑month +0.03, 10‑year -0.20) with no policy surprise
- XLI price below 20‑day, 50‑day, 200‑day SMAs; RSI 42.6, MACD negative; volume 0.09× 20‑day average
- Fund flows flat: share count unchanged over week and month
- Analyst coverage thin (24% of fund) despite 100% buy rating and +31.7% price target

<details><summary><b>News</b> — score +0.00</summary>

- [State Street Industrial Select Sector SPDR ETF (XLI) Stock Price, News, Quote & History](https://ca.finance.yahoo.com/quote/XLI/)  
  <sub>Yahoo! Finance Canada, 20 hours ago</sub>  
  State Street Industrial Select Sector SPDR ETF (XLI) · -1.93% · -1.31% · -5.41% · 4.74% · 8.58% · 52.98% · 600.21%. Key Events. Baseline.
- [Industrial Select Sector SPDR ETF (XLI) stock price, news, quote and history](https://uk.finance.yahoo.com/quote/XLI/)  
  <sub>Yahoo Finance UK, 20 hours ago</sub>  
  Industrial Select Sector SPDR ETF (XLI) · -1.93% · -1.31% · -5.41% · 4.74% · 8.58% · 52.98% · 600.21%. Key events. Baseline. Advanced chart.
- [XLI ETF (NYSEARCA: XLI) Deploys $169 Million In One-Sided Industrial Buying Spree With Zero Sales](https://www.google.com/goto?url=CAESzAEBxCJF18nvI11BV_AoY2QTCt6RY0MCiVnrpPyme0qhC9eb56BYSSJkuwM_OObcTo6676qGbbFtzbfLCis2_zAI0gi_b-UGlCoOArCsGNvTeiZtTV4ZwgNb37sdAjBJK9C6zN_d91ovD6tYq4Irp4IK_-dilcVXmD6naMrPD-q7rL9-AWteJqhDQ64dLzYmOTiDfK8c_8ErQi6vEM-ME4MXhJlIcnkxrELmfye8Rxy5_5jyqQ-JrUYau69xu19XTjvP3qdGFZcqMsQ2DEI&gsessionid=kTfkuquGQQdFiHUwEDfhDOagP9byvAv5Aao9v-jUeFyeCW0EXFmzhA)  
  <sub>Foreign Policy Journal, 20 hours ago</sub>  
  A session with no selling activity and $169.2 million in gross purchases made State Street's Industrial Select Sector SPDR ETF (NYSEARCA: XLI) the sole...
- [Select Sector SPDR Trust - State Street Industrial Select Sector SPDR ETF (ARCA:XLI) Stock Price](https://www.google.com/goto?url=CAESXwHEIkXXiSspYtf43u7yFGBmaMsxtrfD6ARvyx-cHcH-pHNYRZI5N2O0FA_LzpTw5ByUMXDMF1zOAVCmp_3d6G8TN5etZi4uy5tVxMbx0__dBmv6b1CgbWxHRcdlcmkq&gsessionid=kTfkuquGQQdFiHUwEDfhDOagP9byvAv5Aao9v-jUeFyeCW0EXFmzhA)  
  <sub>Simply Wall St, 12 hours ago</sub>  
  Find the latest The Select Sector SPDR Trust - State Street Industrial Select Sector SPDR ETF (ARCA:XLI) stock price, share price history, and explore other...
- [ValuEngine Weekly Market Commentary: Bear Market For Nasdaq-100 Headlines Historic Weekly Meltdown](https://www.google.com/goto?url=CAESyAEBxCJF1xApkEO2Pr0-ekRzI-SSYQmTUbHaCLuFhOO__Q8vQ3wteB6qTyoXHrZGcwewPPOa5lqqZofhDIlwYsv8Lnm3-N_vU-POD9fKBglK0ZNM0r5y88YZqdHWbxVMkZObPzhCzTtyPW_sfmWZaQtlZJ8pUqAC58DIPIKhJUQ3NSe5gpCLl9lKwXEuQLJA-4fOwOUtarRuv4R_eBDEA-11N99dMbrmrf86tJr98a_33QVlGbV5Xaf3wSjpuuOYfCe3RzKUViE_fw&gsessionid=kTfkuquGQQdFiHUwEDfhDOagP9byvAv5Aao9v-jUeFyeCW0EXFmzhA)  
  <sub>Seeking Alpha, 9 hours ago</sub>  
  U.S. equity markets experienced a sharp and broad-based selloff this week, with all major ETFs and sector benchmarks posting significant declines.
- [$100 Invested In State Street Technology Select Sector SPDR ETF 20 Years Ago Would Be Worth This Much Today](https://www.google.com/goto?url=CAESzQEBxCJF1zonu9Y2ruL_O8i158hvrj7GPT_3bdJf7EZ63uuwVG-CuRNclg4wVQuvvWunMKPY6r08sH6RXRzaCJTUA5qzgO-UUyxXYzx6dltq1VMGfVqnDee8pcyy4xIGD0YW-Y8USSfnSmUtwf9cYxOMgE3HEf4csroE6nob44d-MD0vNWTV6wu8TfvzytbKsnGxSLhG45aARUp0Uk6Gp4GFcRdKdGsj34ms0217u2wSbVbUUJsfWy9lm0lYLuZoKWFPVdfQTgdtkGLHhYmP&gsessionid=kTfkuquGQQdFiHUwEDfhDOagP9byvAv5Aao9v-jUeFyeCW0EXFmzhA)  
  <sub>Benzinga, 19 hours ago</sub>  
  State Street Technology Select Sector SPDR ETF (NYSE:XLK) has outperformed the market over the past 20 years by 5.49% on an annualized basis producing an...
- [State Street Industrial Select Sector SPDR ETF (XLI) stock price, news, quote and history](https://www.google.com/goto?url=CAESZAHEIkXXenjGSQOPW-1-YVyVDCKlaM9FhgTNFBFFxKAojnBUDdvmlqEegArBEdzXJq5H5Sa4xnAcGG1HhIutQ9BB7gz7SibmJtUA9VynDFkt9blQYrTCEAt4vVX3B-J_H9w8fU8&gsessionid=kTfkuquGQQdFiHUwEDfhDOagP9byvAv5Aao9v-jUeFyeCW0EXFmzhA)  
  <sub>Yahoo Finance Singapore, 21 hours ago</sub>  
  State Street Industrial Select Sector SPDR ETF (XLI) · -1.93% · -1.31% · -5.41% · 4.74% · 8.58% · 52.98% · 600.21%. Key events. Baseline.
- [State Street Industrial Select Sector SPDR ETF (ARCA:XLI) Price, Holdings, Fees & Analysis](https://www.google.com/goto?url=CAESZwHEIkXXosJjbtthrj0pGOkAl3pL27Rdl0FXLFIzNexBTEFNs4LG1LzqO4iaJz6BVGREK9jm5eidkHm_Wx9n2MKcTLZiHtPySAE90u4FnjkPmR3Gp2o5yXRJi_1vUigTrKTPl4KZjNc&gsessionid=kTfkuquGQQdFiHUwEDfhDOagP9byvAv5Aao9v-jUeFyeCW0EXFmzhA)  
  <sub>Simply Wall St, 21 hours ago</sub>  
  Research State Street Industrial Select Sector SPDR ETF (ARCA:XLI): price, returns, top holdings, fees, dividend yield, sector and region diversification,...
- [9 Of 11 Sectors Rise Monday As Growth Leads](https://www.google.com/goto?url=CAESoQEBxCJF1xlnHWKgbjmPRzp64gkbrhNPH93p7BGfa1ynFXEP-LnrtjPM3ECB_mzj_96PyZ01hN-hK4dOBqwTSTlHXq4vtL0kZoPBgYo6wk42FlBzDzr9u-QdFq2LGD-oRTuT-4bOcIGnAepGq7SzBHuow1OjJLmrAVBpS67xDL0vEBZ4LAIN6loJi0paopfQOEOJF1M0C1qQWOPw7ap9F_kd0g&gsessionid=kTfkuquGQQdFiHUwEDfhDOagP9byvAv5Aao9v-jUeFyeCW0EXFmzhA)  
  <sub>Benzinga, 23 hours ago</sub>  
  Nine of 11 sectors are higher in Monday's regular session, with growth sectors holding two of the top three positions alongside Industrials.
- [3 ETFs That Hold RTX Very Differently After Its Outlook Lift](https://www.google.com/goto?url=CAESqQEBxCJF1wTP1AiBLGQI-ECA5UOlR69fnTUwXx0r2P3ULvDKnOi9GqU4B7H7IOhaLkh9U0-s_2wEH3gVKjVXKAqZjCfExrkBlU6ey7XOM0xEyj6ZexFJtT5gx9FFNEC6kWiLiRBZIYsZWkgtrrKHLoMF0Fqz2qsd2lyUAoga0OU62lh02DLGyncLFUX5-Ii2_5avl6iDWgRoBLEihDsk1GGmDCH4mOH5h6sq&gsessionid=kTfkuquGQQdFiHUwEDfhDOagP9byvAv5Aao9v-jUeFyeCW0EXFmzhA)  
  <sub>Simply Wall St, 21 hours ago</sub>  
  You can own RTX directly or hold it inside a fund, and each route leaves you carrying something different. A single stock puts all of that business's...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.17% (+0.03 on the week) | 5-year 4.71% (-0.19 on the week) | 10-year 4.90% (-0.20 on the week) | 30-year 5.29% (-0.17 on the week)
Yield curve, 10-year minus 3-month: +0.73 points -- upward sloping (normal)
US dollar index: 103.81 (+0.32 on the week)
Volatility (VIX): 29.34 (+3.9 on the week) -- stressed
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.1% (2026-10-01) | jobless claims 203k (2026-11-14)
Policy and expectations: Fed target 4.00% | market expects 2.1% inflation over 10 years
Rate path: 2-year Treasury 4.63% vs Fed target 3.75-4.00% -- the bond market prices about 3 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score -0.20</summary>

```text
Last close 161.70 (bar of 2026-11-24), from 501 daily bars
Trend: vs 20d SMA 166.27 (-2.7%), 50d 167.63 (-3.5%), 200d 173.21 (-6.6%); 50d below 200d
Momentum: RSI(14) 42.6 | MACD -1.954 vs signal -1.275 (histogram -0.679)
Returns: 1d -0.5% | 5d -1.9% | 1m -3.2% | 3m -10.3%
52-week range: 150.00 - 186.51 (now 32.0% of the way up)
Volatility: ATR(14) 3.56 (2.2% of price) | annualised 20d 31.4%
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

<details><summary><b>What analysts and big funds say</b> — score +0.30</summary>

_Not available today._

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score +0.30</summary>

```text
Rolled up from the 5 largest holdings, 24.0% of the fund by weight  -- thin, so read this as a fact about that slice rather than the fund
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 1.73 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +31.7% above the current prices
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
Share count change: 1 week: +0.0% (0.00) over 7d | 1 month: +0.0% (0.00) over 31d
Shares outstanding: 136.63M | fund size: 22.09B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### US technology (XLK) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Mixed signals: bullish analyst consensus and strong inflows versus bearish technicals, high valuations and elevated market volatility.

**Main reasons it gave:**
- VIX 29.34 (+3.9) indicating stressed market volatility
- XLK price below 20‑day, 50‑day, and 200‑day SMAs, RSI 38.7 (bearish technicals)
- Share count up +14.3% week, +18% month (strong inflows)
- Analyst consensus 100% buy with +34.5% price target (bullish sentiment)
- High valuations (P/E 31.66, P/B 11.55) suggest caution

<details><summary><b>News</b> — score +0.00</summary>

- [$100 Invested In State Street Technology Select Sector SPDR ETF 20 Years Ago Would Be Worth This Much Today](https://www.benzinga.com/news/26/11/63559313/100-invested-state-street-technology-select-sector-spdr-etf-20-years-ago-would-be-worth-much-today)  
  <sub>Benzinga, 19 hours ago</sub>  
  State Street Technology Select Sector SPDR ETF (NYSE:XLK) has outperformed the market over the past 20 years by 5.49% on an annualized basis producing an...
- [ValuEngine Weekly Market Commentary: Bear Market For Nasdaq-100 Headlines Historic Weekly Meltdown](https://www.google.com/goto?url=CAESyAEBxCJF16kFN_KMuuNYvnwcx0VGbcz7J2OLVwtaKsi_JeYrBeA0YoG5lKMXdMGeotkG-L4kiSEDBek7W2vd4GPmo-kPnFmtyrhQOGIDk1LdgtcNDIcZt3XgIYUnErMSiPhQUKlpXjmR0LrsHZqE75RMt6HmuxIjezFUP075IoPpXy0z6vWIgc4l2DpciNlWVpzhAtmFJb6XU3EaRJk8-xCp-Pvjpu7Z56c-YaMscFSsz4dI5-kaBWZH7eOtl4VdVEp-utik7CZwCQ&gsessionid=UQnyBnT1vndK9cT_xgYH83cQOvax4HIlhQ4_JwI0P6bMukG2SsQ7iw)  
  <sub>Seeking Alpha, 9 hours ago</sub>  
  U.S. equity markets experienced a sharp and broad-based selloff this week, with all major ETFs and sector benchmarks posting significant declines.
- [Jensen Huang Back at Nvidia: 2 Sector Tilts to Consider](https://www.google.com/goto?url=CAESnQEBxCJF18e3VzHpkpUEieU75EfKZ9ikW1ZHMyPgO5YWvonT0ofkXVUljtvQKRJKKLuDCABreMCi3zbqqcw1Nl-hHQXg4XuKdmPwLmKaeLoUewIHv6WlvlVl8sv7VF8CgOYgFZbkFGONUL5_A1M6eKcMLHaVDClonEHlFdVqqnZgBQzpR_nEVqKeqGrUteWVmR4no-6q0lfqsmpLtdQy&gsessionid=UQnyBnT1vndK9cT_xgYH83cQOvax4HIlhQ4_JwI0P6bMukG2SsQ7iw)  
  <sub>ETF Database, 18 hours ago</sub>  
  The market seems to be celebrating the surprising return of Huang to the chipmaking giant, but is it time to be bullish, or bearish?
- [Tech And Chip ETFs Jumped As The AI Trade Woke Up](https://www.google.com/goto?url=CAESiwEBxCJF17jIHIheWQWdZ4pbz3Bx5UUNZaAdoI827porezRsQt-XOglT8APaeFPrhbl3IIZFk318sbE_LqwMNsRSIsolajosi3UO94mSRTPB3fTWEX0E_Z-0hXnS6EaMEhavY05OaE_oBHAYwE_NMHIo4HoMUNzxF79R2zcglzDG6Yex8B8CbeFuOvdz&gsessionid=UQnyBnT1vndK9cT_xgYH83cQOvax4HIlhQ4_JwI0P6bMukG2SsQ7iw)  
  <sub>Finimize, 20 hours ago</sub>  
  XLK gained 8.4% and SOXX rose 13% after Nvidia brought back Jensen Huang as CEO.
- [US stocks sell off sharply with tech ETFs leadi...](https://www.google.com/goto?url=CAESmAEBxCJF1xm_h4-aPjOeCVn2yjBG-5hKKhG8qgWCHxRflDbzmJRv4E-bufXT_68FiZfBhG55VBoo6IurBF8JI3QIX2F9qlkGlACW3YpB8XlWU2CXQF6mwH7D_xjEAgxijnR-NJaB6pRpLqBHqdaVyvYUKT8inzV8dbALPSwcGhGsEnBmVSHvfhISrKduCr0KU6TBLSyn7bcZjA&gsessionid=UQnyBnT1vndK9cT_xgYH83cQOvax4HIlhQ4_JwI0P6bMukG2SsQ7iw)  
  <sub>Pluang, 9 hours ago</sub>  
  US equity markets saw a broad selloff this week, with all major ETFs and sectors dropping significantly. The Nasdaq-100 ETF turned negative year-to-date,...
- [9 Of 11 Sectors Rise Monday As Growth Leads](https://www.google.com/goto?url=CAESoQEBxCJF1z7U4sLjOzv3y-ZumyhpIA5WRfA-NQqyVENjynnUdo5oy3o3DGILWMzEop8TpWNHed5k2HkvyyuTnrsBaRWALz7f2mKmWyXI54WySpmRgv4VxeeR-HzfdhGlwml6U9eNS84Uru4Q1U-Oelj3daJgtlhKqr76LN13uONgL-RNlDTkZkwT_t9JcDHvRo6HOURLa0SgLdnDMCY6O0VP4Q&gsessionid=UQnyBnT1vndK9cT_xgYH83cQOvax4HIlhQ4_JwI0P6bMukG2SsQ7iw)  
  <sub>Benzinga, 23 hours ago</sub>  
  Nine of 11 sectors are higher in Monday's regular session, with growth sectors holding two of the top three positions alongside Industrials.
- [DTD: A Well-Diversified Dividend ETF Built For This Market (NYSEARCA:DTD)](https://www.google.com/goto?url=CAESnwEBxCJF15yAQXCnn-StU-RHvNjoyy9GXa3mrXdZ8ATgDGzEZJTrXAk6POzV0JZ6lJ2NmRZjoKijFT_2oBjJqPprjtDOSrQwBZwEIgcxK7SRGGv2NM0xSUKaB5doJd2aUa4eZWbx6Qg7P-etEcFgE8Cige56Yr8MxLj1r2aDbjLy0cnlLo1qGHv5gPDTzlUW6zPgpiB5_ScRPteoA-0SecM&gsessionid=UQnyBnT1vndK9cT_xgYH83cQOvax4HIlhQ4_JwI0P6bMukG2SsQ7iw)  
  <sub>Seeking Alpha, 19 hours ago</sub>  
  Analyst rates WisdomTree U.S. Total Dividend ETF a Buy: about 18% tech exposure and broad diversification could limit losses in a prolonged downturn.
- [Applied Optoelectronics (AAOI) Shares Surge 22% Amid Broad Tech Rally on November 23, 2026](https://www.google.com/goto?url=CAESugEBxCJF18TVf6sJTWNPN1Wm3Oajl0saXD_MWlAKbiXKDipmoNdbh7ZqgiPwxTKCHpQksRFgpVSOSwMVi0EhAZqe3PTixtgE_4VLVr5bpdvFWL9GmB9euJpmnzjxX_-VjXuAMmh8XRLHzdaxY8ur-sxH_aLKUGUqPcug7E-LWs1xQo0pVxSFkxAATaY3EYnFh3S73arbyENFWLYHwRsBjleEz3Rx3qwmfbbzRWy57l2VmVMNXF8hMuia8Yo&gsessionid=UQnyBnT1vndK9cT_xgYH83cQOvax4HIlhQ4_JwI0P6bMukG2SsQ7iw)  
  <sub>GuruFocus, 22 hours ago</sub>  
  On November 23, 2026, shares of Applied Optoelectronics Inc (ticker: AAOI) jumped nearly 22% to $40.08, gaining $7.15 in a single session.
- [Dell Technologies (DELL) Shares Surge Nearly 23% Ahead of Earnin](https://www.google.com/goto?url=CAEStwEBxCJF15S_psCa6JyED3vWcS-XE9zcyMBCEfEdvL8AqS85BI7XDsDE3_BICTRR2CZj_q6-qKVlgL-k-UV6IyUBYupT_MkaR8lBgb37OF_jwqeovZ4sqtTo00lZN7YxSj4M_UaB0a56RR2ZRwpWkbc6n3ej1813Yo8YG69xoBcEWNeEQk2u72MpcZHU8kCFIuvhf3LWUZjHziXEZ-d_D78zjK7oOuZo_K1KdTrMaK5XmVad7WUTIxk&gsessionid=UQnyBnT1vndK9cT_xgYH83cQOvax4HIlhQ4_JwI0P6bMukG2SsQ7iw)  
  <sub>GuruFocus, 22 hours ago</sub>  
  On November 23, 2026, Dell Technologies Inc (NYSE: DELL) saw its stock price jump nearly 23%, closing at $340.31, driven by optimism ahead of its earnings...
- [Coherent (COHR) Surges 17% Amid Tech Rally, But GF Value™ Flags Significant Overvaluation](https://www.google.com/goto?url=CAESuAEBxCJF1xzHDqHeGY-X9A1V7XjnhRP7lkg4dtbltJSRIzyN9O_Vi7DZGx4v6UVH1ztOM6Zpx9F-kKU6PR39fDkABF5gmEP-fRJHIJlxoIxHm7EOrUx-SHn-08clrf3MP_4mQ4Q4yeWJ6erXUOysVxzvY4_fy92DvoK4oKtMkhm3g7nEOAeCdGrcbyk8lmf04meBLe8csaHfP0a6t0zn6UMolLx_g77gBDYbQl28CXCzsIcw3N7NOgd7&gsessionid=UQnyBnT1vndK9cT_xgYH83cQOvax4HIlhQ4_JwI0P6bMukG2SsQ7iw)  
  <sub>GuruFocus, 22 hours ago</sub>  
  On November 23, 2026, Coherent Corp (NYSE: COHR) rebounded strongly, gaining over 17% to close at $218.37 following a prior decline driven by AI sector...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.17% (+0.03 on the week) | 5-year 4.71% (-0.19 on the week) | 10-year 4.90% (-0.20 on the week) | 30-year 5.29% (-0.17 on the week)
Yield curve, 10-year minus 3-month: +0.73 points -- upward sloping (normal)
US dollar index: 103.81 (+0.32 on the week)
Volatility (VIX): 29.34 (+3.9 on the week) -- stressed
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.1% (2026-10-01) | jobless claims 203k (2026-11-14)
Policy and expectations: Fed target 4.00% | market expects 2.1% inflation over 10 years
Rate path: 2-year Treasury 4.63% vs Fed target 3.75-4.00% -- the bond market prices about 3 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score -0.50</summary>

```text
Last close 158.58 (bar of 2026-11-24), from 501 daily bars
Trend: vs 20d SMA 169.71 (-6.6%), 50d 183.47 (-13.6%), 200d 171.48 (-7.5%); 50d above 200d
Momentum: RSI(14) 38.7 | MACD -7.254 vs signal -6.469 (histogram -0.785)
Returns: 1d -2.3% | 5d -2.9% | 1m -14.9% | 3m -13.3%
52-week range: 127.50 - 202.00 (now 41.7% of the way up)
Volatility: ATR(14) 6.83 (4.3% of price) | annualised 20d 60.1%
Volume: 0.12x the 20-day average
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
Three-year record: +17.9% a year | beta to the market 1.56
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
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 1.72 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +34.5% above the current prices
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
Share count change: 1 week: +14.3% (15.76B) over 7d | 1 month: +18.0% (19.25B) over 32d
Shares outstanding: 796.50M | fund size: 126.31B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### US everyday goods (XLP) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Neutral overall; no material macro surprise, flat fund flows, modest analyst optimism, solid fundamentals but no decisive technical break.

**Main reasons it gave:**
- Fund flows flat (0% change week/month) indicating no net demand shift
- Analyst coverage 41.8% of fund, rating 100% buy with +4.6% price target
- Technical: price near 52‑week high, low volume (0.15× 20‑day avg) and MACD negative
- Macro: yields fell modestly, VIX high (29.34) indicating market stress

<details><summary><b>News</b> — score +0.00</summary>

- [State Street Health Care Select Sector SPDR ETF (XLV) stock price, news, quote and history](https://au.finance.yahoo.com/quote/XLV/)  
  <sub>Yahoo Finance Australia, 19 hours ago</sub>  
  State Street Health Care Select Sector SPDR ETF (XLV) · -4.50% · 0.08% · 19.70% · 15.90% · 16.05% · 35.40% · 623.10%. Key events. Baseline. Advanced...
- [Jensen Huang Back at Nvidia: 2 Sector Tilts to Consider](https://etfdb.com/sector-investing-content-hub/jensen-huang-back-nvidia-2-sector-tilts-consider/)  
  <sub>ETF Database, 18 hours ago</sub>  
  The market seems to be celebrating the surprising return of Huang to the chipmaking giant, but is it time to be bullish, or bearish?
- [ValuEngine Weekly Market Commentary: Bear Market For Nasdaq-100 Headlines Historic Weekly Meltdown](https://www.google.com/goto?url=CAESyAEBxCJF1y4ZtFnuNrj1KoZsBu7u3NZSLKCFrQ1znhXjKk3E2mFb7dkIv0QZ29_FP5fmT7wI6v7bakkipRtY-sJYz9uzW2G7V9521Zr3hlaNpXTFf-rf2Zqrr9F1rCPBDclf3f4wl4Wn5vCannqliZ_waM5-g75vYV4umxqynx8PxJfBe7hW2ST4kvMe3HXGtatFzvTHW6_9Yx6dKQKQOuYd_zMVMbLneDuoJgTd5zGcyXBghdmOH5R7x8pbqqA5RG_MaN7A9E-Jdg&gsessionid=pUFDLejXL3GxGgvtU9yz5z8FbokUKbfhov0F1sZor_hYszKCJypVUA)  
  <sub>Seeking Alpha, 9 hours ago</sub>  
  U.S. equity markets experienced a sharp and broad-based selloff this week, with all major ETFs and sector benchmarks posting significant declines.
- [State Street Industrial Select Sector SPDR ETF (XLI) stock price, news, quote and history](https://www.google.com/goto?url=CAESZAHEIkXXMNIMD80zVn8PhZjG3mRptqu_rAz94WtgDl1poDUs_wH6HDc5OMKIWFx8hEfN65XINvaCSrwDqfFJjWg3LHLxsOO5O2dwK7E8t2awxY41aoEzKaRBoGCHLy3YkDl9dtM&gsessionid=pUFDLejXL3GxGgvtU9yz5z8FbokUKbfhov0F1sZor_hYszKCJypVUA)  
  <sub>Yahoo Finance Singapore, 21 hours ago</sub>  
  Find the latest State Street Industrial Select Sector SPDR ETF (XLI) stock quote, history, news and other vital information to help you with your stock...
- [Safe-Harbor ETFs: Shelter From the Storm](https://www.google.com/goto?url=CAEShAEBxCJF11SAE_qze69-i3Lj_V4oghsN179tM6LQi3yw8sgvee6xeKXiB3unUSskYx9cInaSDe6VYfeCmzjkIzmWzHfPkggCGrBOgnz4LhjoKBHIhSOqXSRXi2ztIEBcZejSjaC0Ywy6Kf9oXxlyU4-ABhtQ_JTMGtMhuRVixxPzlrwtP5w&gsessionid=pUFDLejXL3GxGgvtU9yz5z8FbokUKbfhov0F1sZor_hYszKCJypVUA)  
  <sub>ETF Database, 1 hour ago</sub>  
  Combining value, equal-weight, and quality ETFs protects portfolios during downturns without completely missing explosive growth recoveries.
- [Tradable Rally… Or Dead-Cat Bounce?](https://www.google.com/goto?url=CAESewHEIkXXNF0Y1m8ziSzh-H-SxwbAGoOBzMdOd7Y9KsMqxvKyNnWeiB-MdUs-Jcw4V5TSlu0T9OCls2cFfQ_njcto9RrtpxJyaPFvwAiS6sWZE7HpovcM1SxeqPorBRsTKFuF0utPqexn8k439XoKCld6R6fWabUv7VKTVw&gsessionid=pUFDLejXL3GxGgvtU9yz5z8FbokUKbfhov0F1sZor_hYszKCJypVUA)  
  <sub>Money & Markets, 14 hours ago</sub>  
  Is it safe to jump back in the pool? Or is the Nvidia drama as a sign that all is not well and the powers that be are scrambling...
- [These are the favorite stocks of healthcare hedge funds – Goldman (XLV:NYSEARCA)](https://www.google.com/goto?url=CAESogEBxCJF1-LtTsfSRDrw8P8LvSL6yCdJCNBZRF_aREbSL9JMKsImiesP4ige3-HvodGuiZ0g_ojjLvbAerXAmiuxoOwxg6ALhLnMZN5uQ_XiHxM0raWtJCCymfpk2f_fB-IDD7frGq38aVxtB73nslyir1IuTyFZGJJINmUwM8d2MsbwCnQYam1WuGnKWeSsabiaQhAEwO89ureA-yZzJ-nJuVs&gsessionid=pUFDLejXL3GxGgvtU9yz5z8FbokUKbfhov0F1sZor_hYszKCJypVUA)  
  <sub>Seeking Alpha, 23 hours ago</sub>  
  Goldman Sachs finds Revolution Medicines leads health care specialist hedge fund holdings, owned by 41% of 27 funds; Insmed follows at 38%.
- [3 ETFs For Owning AbbVie As Its Research Push Widens The Choice](https://www.google.com/goto?url=CAESlwEBxCJF13Xjl4JO8MjHiQF_sG1PslCIqBOQgr5htCOL9mUAsNcHjVSPxcVlGjbRZdRrW5e0NL3A6t37OvEWqH58-NEcoVlKvh-K8_Mhdib0FeTxbyHgGUfLg0DxKPDc7_4hPDRnavRC22hy4Za077v5OszcBA2VihKqFHTeW0RvYv4J04LbNZWUzm4VD4d_6eOc5kR0b5sx&gsessionid=pUFDLejXL3GxGgvtU9yz5z8FbokUKbfhov0F1sZor_hYszKCJypVUA)  
  <sub>Yahoo Finance, 20 hours ago</sub>  
  If you like AbbVie and its drug portfolio, buying the stock outright means your money rises and falls with its specific issues.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.17% (+0.03 on the week) | 5-year 4.71% (-0.19 on the week) | 10-year 4.90% (-0.20 on the week) | 30-year 5.29% (-0.17 on the week)
Yield curve, 10-year minus 3-month: +0.73 points -- upward sloping (normal)
US dollar index: 103.81 (+0.32 on the week)
Volatility (VIX): 29.34 (+3.9 on the week) -- stressed
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.1% (2026-10-01) | jobless claims 203k (2026-11-14)
Policy and expectations: Fed target 4.00% | market expects 2.1% inflation over 10 years
Rate path: 2-year Treasury 4.63% vs Fed target 3.75-4.00% -- the bond market prices about 3 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 91.43 (bar of 2026-11-24), from 501 daily bars
Trend: vs 20d SMA 90.58 (+0.9%), 50d 86.67 (+5.5%), 200d 85.06 (+7.5%); 50d above 200d
Momentum: RSI(14) 58.4 | MACD 1.115 vs signal 1.391 (histogram -0.276)
Returns: 1d +1.2% | 5d -0.0% | 1m +4.0% | 3m +6.0%
52-week range: 76.62 - 92.60 (now 92.7% of the way up)
Volatility: ATR(14) 1.47 (1.6% of price) | annualised 20d 20.7%
Volume: 0.15x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.30</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score +0.30</summary>

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
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 1.81 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +4.6% above the current prices
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
Share count change: 1 week: +0.0% (0.00) over 7d | 1 month: +0.0% (0.00) over 31d
Shares outstanding: 210.17M | fund size: 19.22B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### US electricity and water (XLU) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> No material macro surprise, technicals mixed, analyst view bullish but limited to 39% of holdings, fundamentals solid, fund flows flat. Overall neutral.

**Main reasons it gave:**
- Yield curve normal (+0.73) with no rate surprise
- Technicals mixed: price below 200‑day SMA, MACD below signal
- Analyst coverage 80% buy, price target +12.5% above current
- Fund flows flat, no net inflows/outflows

<details><summary><b>News</b> — score +0.00</summary>

- [Safe-Harbor ETFs: Shelter From the Storm](https://etfdb.com/equity-etf-content-hub/safe-harbor-etf-storm-shelter/)  
  <sub>ETF Database, 1 hour ago</sub>  
  Combining value, equal-weight, and quality ETFs protects portfolios during downturns without completely missing explosive growth recoveries.
- [Should You Invest in the iShares U.S. Utilities ETF (IDU)?](https://uk.finance.yahoo.com/news/invest-ishares-u-utilities-etf-102002049.html)  
  <sub>Yahoo Finance UK, 4 hours ago</sub>  
  Designed to provide broad exposure to the Utilities - Broad segment of the equity market, the iShares U.S. Utilities ETF (IDU) is a passively managed...
- [ValuEngine Weekly Market Commentary: Bear Market For Nasdaq-100 Headlines Historic Weekly Meltdown](https://www.google.com/goto?url=CAESyAEBxCJF19_UlKWSde8zY-LcmXJblFX13PnFZCA2f-w6UF5Q7h9l5JVTvfbBgeJCDNG07mDgJ5Bx1WnoZVgrK5HYHp4mRgn9ldaZecU6HvemNcouQ-5dvH3xavxHiJl3cpBNlHdAlGD-v-HcqEzEY4gpbTWcDAVlAnkTxqccY8yjDEEAMQla-f-TcyFYJdqNAInr2A77_Xs2llkwZ1FAHcH_zuFaPMCEyCZJ7P1YkQKv8UggY3dc_gSAgowLcPCydJLa8obn-AJKsg&gsessionid=s7taYyFp-heIMOTl8e5vDlYqsf6FIxKxle_ycBc_F8d_RfqqkguZWw)  
  <sub>Seeking Alpha, 9 hours ago</sub>  
  U.S. equity markets experienced a sharp and broad-based selloff this week, with all major ETFs and sector benchmarks posting significant declines.
- [Nvidia's Huang Returns as CEO, Igniting Rally in AI Power and Grid Stocks](https://www.google.com/goto?url=CAESgAEBxCJF10bwDaAXAhvXE-9JngVdti5ZmGlzmYUtG7yJTGTlBkzzZsm2rQsLhBl4jqFkyHZg4ro2aTZa6M6ax7SJL2eB71h-5_hvRSl1c5nJxGikmo8-WkfeBComOXkEvJ76YDngtHmHGaT5siAu-qx831DvrYT819f2EtFXehfSQQ&gsessionid=s7taYyFp-heIMOTl8e5vDlYqsf6FIxKxle_ycBc_F8d_RfqqkguZWw)  
  <sub>BigGo Finance, 20 hours ago</sub>  
  Nvidia shares jumped more than 32% on Monday after the board reinstated Jensen Huang as chief executive, ending an 11-day leadership crisis and…
- [State Street Industrial Select Sector SPDR ETF (XLI) stock price, news, quote and history](https://www.google.com/goto?url=CAESZAHEIkXXK52NuqyJ4ltCZWmU7qTOc8t09VGcU1CCxA0mPh1UE5dLrneZD9KOR_LGyfSG1zntGYMZqeQfRnyXRb0zgGtYWqgrJRPj7P2OsVTxuiODJzuCLjuCM9BTVQ_sRJmkpOg&gsessionid=s7taYyFp-heIMOTl8e5vDlYqsf6FIxKxle_ycBc_F8d_RfqqkguZWw)  
  <sub>Yahoo Finance Singapore, 21 hours ago</sub>  
  Find the latest State Street Industrial Select Sector SPDR ETF (XLI) stock quote, history, news and other vital information to help you with your stock...
- [Investment Management Trust, LLC's State Street Utilities Select Sector SPDR ETF(XLU) Holding History](https://www.google.com/goto?url=CAESkAEBxCJF1_R0d07XzgVBhKU-6alRF2P2YRgTIK7JtKU-vd_Y7GjB-XI9SPbHetHHqmokvTkWEaX4PPuDdmiUx4K3f38qvIMoq5nZ00EKLQ6778HlAyCNKXNzlciK2Og9Znvuo0waoJsblSqnd9AF1Epj67__PLn2FITRNwuUicnhKwxBV5wsu9qyTAcopMZrZpQ&gsessionid=s7taYyFp-heIMOTl8e5vDlYqsf6FIxKxle_ycBc_F8d_RfqqkguZWw)  
  <sub>GuruFocus, 18 hours ago</sub>  
  State Street Utilities Select Sector SPDR ETF(XLU) Buys and Sells Made by Investment Management Trust, LLC. Latest and Historical Data and Chart.
- [AI Power Stocks Rally Hard as Jensen Huang’s Nvidia Return Sparks Energy Rally](https://www.google.com/goto?url=CAESqAEBxCJF1-A3rXysot-lhiFDKbe-8hwon_OQHOLG3_LF67cXK_CcJx47OcQcvIPVxxMuoI_21_TPCScwKE-pejM4sJcnjwjIKAW7vhr_GIXOWfvANraOsGfwXVrxqDSsmRy9SziLGqwIva6gDqpW6LI8NAoMLg5otU7yQFddcvs1uXCjfpzbTMkUm_xnSdg1HBJs-jdslBQ6nADjrbcXc8L4d2TdlAQJDAM&gsessionid=s7taYyFp-heIMOTl8e5vDlYqsf6FIxKxle_ycBc_F8d_RfqqkguZWw)  
  <sub>TipRanks, 21 hours ago</sub>  
  Power and grid stocks rallied hard on Monday after Nvidia's ($NVDA) board voted to bring back Jensen Huang as CEO. Huang's return ended an 11-day leadership...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.17% (+0.03 on the week) | 5-year 4.71% (-0.19 on the week) | 10-year 4.90% (-0.20 on the week) | 30-year 5.29% (-0.17 on the week)
Yield curve, 10-year minus 3-month: +0.73 points -- upward sloping (normal)
US dollar index: 103.81 (+0.32 on the week)
Volatility (VIX): 29.34 (+3.9 on the week) -- stressed
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.1% (2026-10-01) | jobless claims 203k (2026-11-14)
Policy and expectations: Fed target 4.00% | market expects 2.1% inflation over 10 years
Rate path: 2-year Treasury 4.63% vs Fed target 3.75-4.00% -- the bond market prices about 3 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score -0.10</summary>

```text
Last close 43.41 (bar of 2026-11-24), from 501 daily bars
Trend: vs 20d SMA 43.44 (-0.1%), 50d 42.01 (+3.3%), 200d 44.34 (-2.1%); 50d below 200d
Momentum: RSI(14) 54.3 | MACD 0.275 vs signal 0.401 (histogram -0.126)
Returns: 1d +0.2% | 5d -0.0% | 1m +2.0% | 3m -0.2%
52-week range: 39.25 - 47.73 (now 49.1% of the way up)
Volatility: ATR(14) 0.62 (1.4% of price) | annualised 20d 13.9%
Volume: 0.09x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.30</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score +0.30</summary>

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
Rolled up from the 5 largest holdings, 39.4% of the fund by weight
Ratings by weight: buy 80.0% | hold 20.0% | sell 0.0% (mean 2.03 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +12.5% above the current prices
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
Share count change: 1 week: +0.0% (0.00) over 7d | 1 month: +0.0% (0.00) over 31d
Shares outstanding: 163.27M | fund size: 7.09B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### South Korea (EWY) · Sector or country — no answer, no confidence given

<details><summary><b>News</b> — score n/a</summary>

- [iShares MSCI South Korea ETF (EWY) Options Chain - Yahoo Finance](https://ca.finance.yahoo.com/quote/EWY/options/?date=1798070400&straddle=false&type=all)  
  <sub>Yahoo! Finance Canada, 19 hours ago</sub>  
  View the basic EWY option chain and compare options of iShares MSCI South Korea ETF on Yahoo Finance.
- [Top Tokenized ETFs by Market Cap](https://www.coingecko.com/en/etfs)  
  <sub>Coingecko, 1 hour ago</sub>  
  Discover the top ETFs (exchange-traded funds) by tokenized market cap. Track ETF prices alongside their tokenized prices, market cap, and volume on...
- [South Korea’s central bank seen extending rate hikes as inflation and chip exports remain strong](https://www.google.com/goto?url=CAESwwEBxCJF1wEHxQ-pviDypoV8Dx7wSs8bUeMTQTsCNwNeP0sOmOAqG4WSlP6g5p5aYBMPfK6gfEqEO2h33TfeVqW1NsbIMdK1f6HI9QwGuYzi0e6qvUUzNVepCmKxSfGpWwtigbW7ZIsbIcwRClHDRDXL31Ulx_WafHv7ZmYynRovyeaGD2XuTiwef0UOS3g2c4Inf4NjPKFKVC7aUTpM4qT0_BM20L20TsD5buNH4WHbJjrVtsfFzcR-oeFinZKPn-JohtI&gsessionid=BQoRkxse9rxEYtpY9toFx7GzX5aQ6GGkIsp97kdzipJlj2gvcY3vqA)  
  <sub>Seeking Alpha, 8 hours ago</sub>  
  South Korea's central bank is expected to raise interest rates this week and deliver another increase next year, as inflation remains above target and a...
- [iShares MSCI South Korea ETF (EWY) Price Prediction: Korea ETF rebounds, but trend recovery still needs volume confirmation](https://www.google.com/goto?url=CAESnQEBxCJF1ybaX3KG0XSn6OXqEUl74k9lglOV2kh3FoSOxmNLdAb8vhlQlVYp3JeqHLnckrGbBRWEoKZcSxotzaIEnHZj_rTl16sFMBRxDSN34xI4gwnYFQE8_E0xlwUuRQZNVMVo8pDqbzP0KkTkE2yiV1QjqEN9tZ3Td34vJO80xPcEOAlnWxGeEFSzIJs6__yY0fkkXnLpNDduf0ST&gsessionid=BQoRkxse9rxEYtpY9toFx7GzX5aQ6GGkIsp97kdzipJlj2gvcY3vqA)  
  <sub>Blockchain News, 7 hours ago</sub>  
  iShares MSCI South Korea ETF (EWY) traded at $135.79, up 6.25% on the session, after moving inside a $139.89 to $127.21 range. The setup is still mixed...
- [Direxion South Korea Bull 3X ETF (KORU) Price Prediction: Bounce still lacks confirmation](https://www.google.com/goto?url=CAESmAEBxCJF16LEnVLMWNlaq0rKRk1rSeJdl5uJxNuawu-9h6cFnLX_6bKy3Cf2-GyAbAcVtklzXkYw666BRUsuoS-0bWYyptZQ55OG5XXmyJvX0ya3CrJxaZB0ppFUl4_-PudSJiLnzZoklFjWPGua3xRjweFQIVg-mf2fRNOHMUzcUKVYHcuOCf6oLA5HX2NDL1RHxlUlcVKG4Q&gsessionid=BQoRkxse9rxEYtpY9toFx7GzX5aQ6GGkIsp97kdzipJlj2gvcY3vqA)  
  <sub>Blockchain News, 7 hours ago</sub>  
  Direxion South Korea Bull 3X ETF (KORU) is trading at $6.15 after a 17.44% 24-hour move, but it remains below its 20-day SMA, 50-day SMA, 12-day EMA and...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score n/a</summary>

```text
US Treasury yields: 3-month 4.17% (+0.03 on the week) | 5-year 4.71% (-0.19 on the week) | 10-year 4.90% (-0.20 on the week) | 30-year 5.29% (-0.17 on the week)
Yield curve, 10-year minus 3-month: +0.73 points -- upward sloping (normal)
US dollar index: 103.81 (+0.32 on the week)
Volatility (VIX): 29.34 (+3.9 on the week) -- stressed
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.1% (2026-10-01) | jobless claims 203k (2026-11-14)
Policy and expectations: Fed target 4.00% | market expects 2.1% inflation over 10 years
Rate path: 2-year Treasury 4.63% vs Fed target 3.75-4.00% -- the bond market prices about 3 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score n/a</summary>

```text
Last close 132.72 (bar of 2026-11-24), from 501 daily bars
Trend: vs 20d SMA 143.01 (-7.2%), 50d 161.28 (-17.7%), 200d 164.40 (-19.3%); 50d below 200d
Momentum: RSI(14) 40.6 | MACD -8.035 vs signal -7.921 (histogram -0.114)
Returns: 1d -2.2% | 5d -1.9% | 1m -13.1% | 3m -25.9%
52-week range: 88.58 - 219.20 (now 33.8% of the way up)
Volatility: ATR(14) 7.66 (5.8% of price) | annualised 20d 83.5%
Volume: 0.17x the 20-day average
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
Share count change: 1 week: +14.9% (3.09B) over 7d | 1 month: +8.6% (1.89B) over 32d
Shares outstanding: 179.85M | fund size: 23.87B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Brazil (EWZ) · Sector or country — no answer, no confidence given

<details><summary><b>News</b> — score n/a</summary>

- [iShares China Large-Cap ETF (FXI) Stock Price, News, Quote & History](https://ca.finance.yahoo.com/quote/FXI/)  
  <sub>Yahoo! Finance Canada, 24 hours ago</sub>  
  Find the latest iShares China Large-Cap ETF (FXI) stock quote, history, news and other vital information to help you with your stock trading and investing.
- [Top Tokenized ETFs by Market Cap](https://www.coingecko.com/en/etfs)  
  <sub>Coingecko, 13 hours ago</sub>  
  Discover the top ETFs (exchange-traded funds) by tokenized market cap. Track ETF prices alongside their tokenized prices, market cap,...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score n/a</summary>

```text
US Treasury yields: 3-month 4.17% (+0.03 on the week) | 5-year 4.71% (-0.19 on the week) | 10-year 4.90% (-0.20 on the week) | 30-year 5.29% (-0.17 on the week)
Yield curve, 10-year minus 3-month: +0.73 points -- upward sloping (normal)
US dollar index: 103.81 (+0.32 on the week)
Volatility (VIX): 29.34 (+3.9 on the week) -- stressed
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.1% (2026-10-01) | jobless claims 203k (2026-11-14)
Policy and expectations: Fed target 4.00% | market expects 2.1% inflation over 10 years
Rate path: 2-year Treasury 4.63% vs Fed target 3.75-4.00% -- the bond market prices about 3 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score n/a</summary>

```text
Last close 30.09 (bar of 2026-11-24), from 501 daily bars
Trend: vs 20d SMA 31.48 (-4.4%), 50d 36.45 (-17.4%), 200d 36.75 (-18.1%); 50d below 200d
Momentum: RSI(14) 34.9 | MACD -2.091 vs signal -2.050 (histogram -0.041)
Returns: 1d +2.9% | 5d -3.0% | 1m -11.9% | 3m -15.8%
52-week range: 28.54 - 43.54 (now 10.3% of the way up)
Volatility: ATR(14) 1.03 (3.4% of price) | annualised 20d 32.1%
Volume: 0.16x the 20-day average
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
Weighted price target: +43.2% above the current prices
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
Shares outstanding: 200.55M | fund size: 6.03B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

## Commodities

### Gold (GLD) · Commodity — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:** no explanation. It wrote only “NEUTRAL”, so the main reasons below are all it gave.

**Main reasons it gave:**
- Positioning net long fell 2.5% week‑over‑week, indicating slight bearish sentiment among large speculators
- Technical indicators show GLD below 20‑day, 50‑day and 200‑day SMAs with low RSI, but no decisive break on volume
- Macro data: modest yield declines, strong dollar, high VIX, and no policy surprise, providing no clear catalyst
- Fund flows flat and cost of holding near zero, suggesting neutral demand and no structural bias

<details><summary><b>News</b> — score +0.00</summary>

- [How to Invest in SPDR Gold Shares ETF (GLD)](https://www.fool.com/investing/how-to-invest/etfs/how-to-invest-in-gld-etf/)  
  <sub>The Motley Fool, 21 hours ago</sub>  
  Key Points. SPDR Gold Shares ETF (GLD) lets you invest in physical gold through a brokerage account without storing it yourself. GLD charges 0.40% a year, while...
- [Don't Worry, Precious Metals Will Shine Again (NYSEARCA:GLD)](https://seekingalpha.com/article/4971202-dont-worry-precious-metals-will-shine-again)  
  <sub>Seeking Alpha, 17 hours ago</sub>  
  I remain bullish on precious metals, especially gold and silver, despite their recent 14-month lows. Persistent inflation, a hawkish Fed, a stronger dollar...
- [GLD NTA 23-11-2026 $3.38793](https://www.google.com/goto?url=CAESgwEBxCJF102hvaFSx_CLfu0MfARPC3NXe-0h9FDvhyE9kbqYK6_ZOznnTFjGR34vqVRlMZunr4Sp0tjPeHCM_g7--LRVNCeCvEakq4kwcy8Xb4rNTKpv8KrgDWRgOmDgadqKDpobaNFiYKndbOUjB05XZF1IEyqC_uHTRbiTq8RgW9qH8Q&gsessionid=3Zn4ygNXHXnKP8Z1PkO0AoYD7qXLbA9W1J8IoWnqqXyu6EgsH_NJiA)  
  <sub>BusinessDesk, 18 hours ago</sub>  
  View the full NZX announcement for Smart Gold ETF (GLD): GLD NTA 23-11-2026 $3.38793. Financial updates and company disclosures on BusinessDesk.
- [Gold And Silver Bounce After Wall Street's Dash For Cash](https://www.google.com/goto?url=CAESmAEBxCJF16Ty5q4CEXz5lPzEV8CIN9dM8T0BEUrLswYfyjY1K4BKt9kRBnrAr6jsRhzJrr2VPWh6N_M6Xc7TpHfD7F5vInb7m8mL72tLtbsXPivhFmHouuVPIs8BtPaTgK-tacCkNQE0lmjp40tvwUuH6QJvXga8O75NFZ9fxL2IR4O_zuak52BakvyjC1yrbkUZSjE6O6V4Sw&gsessionid=3Zn4ygNXHXnKP8Z1PkO0AoYD7qXLbA9W1J8IoWnqqXyu6EgsH_NJiA)  
  <sub>Seeking Alpha, 19 hours ago</sub>  
  In early trading Monday, spot gold rose over 3% to about $3,680 an ounce, while silver gained 6% to $44.35. That's a welcome change after gold fell roughly...
- [Huang Reinstated—Time To Add Positions In AI And Semi Stocks](https://www.google.com/goto?url=CAESqQEBxCJF159yZdxcv8nMBYg9Nubw3YkSQzcIxqoP316nNZE2Cg4H57Du4yWQFh9Myh3rHKWs-_MnezAK4NSDY8WJGyTnJ8DTQ0FtgTUVEKREZW1J4av2JVI4zRo-7zcrf5RZS4uLM8HE02gQj5iSUezSDt-nns1OxDllg8mq721feMpV58FOHOKQDvSDKSEY9arZq2te6HojF1SSbhn7Uieho0Aqb382aUgW&gsessionid=3Zn4ygNXHXnKP8Z1PkO0AoYD7qXLbA9W1J8IoWnqqXyu6EgsH_NJiA)  
  <sub>Benzinga, 20 hours ago</sub>  
  Jensen Is Back Please click here for a chart of Invesco QQQ Trust Series 1 (NASDAQ:QQQ). Note the following: The chart shows a huge rally on the news of...
- [Is It Time To Buy Silver? This Put Strategy In Options Trading Counts On A Limited Decline](https://www.google.com/goto?url=CAESngEBxCJF16T1p6-QwW9-zEt9WBuFH3zmgXRPYQSx2-RV9wwtCED6RUrAhEXV2UrjMqGo25SHI5BKZ8PEuw3MtYxwab5KDDZa4Xg34zSZvI_nSw-OhS1dU0D_Boh8csHou2l-Fyu9SySAeg8YuUrwS2cK7tsZbXA0iRKqYWBl09Am7PysJOCmSQaWAUk5--TL4QBidAXEr3cvLoV29RWVhQ&gsessionid=3Zn4ygNXHXnKP8Z1PkO0AoYD7qXLbA9W1J8IoWnqqXyu6EgsH_NJiA)  
  <sub>Investor's Business Daily, 20 hours ago</sub>  
  Is it time to buy silver after a large decline this year? This put option trade allows investors to go long at a discount.
- [BofA’s warning for 2027: Don’t ignore hard-landing risks (SPY:NYSEARCA)](https://www.google.com/goto?url=CAESmAEBxCJF1y1JeZ3mzq4ks3GJEA6Zi1_1v2Toki5GtsxwM283Oyle_tkyxh4M272Dj2HRNsSN-bdivRWQ6wh6AqxPC7fPLmSfqDE9CtQBtmtuk4qG9jvKVTl9tNwrVMS_gAvnp7vW5S-5WL0dSptP1RNoyVOMj5hk9nu1yvUY8sH-zW2RhqfRMLbq4Z6z5C5ilG8puj-ysEWcfg&gsessionid=3Zn4ygNXHXnKP8Z1PkO0AoYD7qXLbA9W1J8IoWnqqXyu6EgsH_NJiA)  
  <sub>Seeking Alpha, 40 minutes ago</sub>  
  BofA strategist favors GRAB assets to hedge recession risk; a hard landing could send the S&P 500 to 6666.
- [Precious Metals Royalty And Streaming Companies - October 2026 Report](https://www.google.com/goto?url=CAESqQEBxCJF16jWZhWNICsX47DSuvDsOcsEHcYOkDUsNKqUFF8bhoWxblCAklu_MQ5Xz0tbsyBpWyZ5_Yp9LVMblUWM7Y1iUb61atDIXeWbDN-v8l6QyK6rYv4mLByaq2Rwez5DPGezub5Ut4EVomWB3MmcuZYwF_aPQd3wcZaLhQUzsd_24u5UNDA1zOzxKTazoxIzxAd42qIH-BxBUeOkINLUP308O0blzHt3&gsessionid=3Zn4ygNXHXnKP8Z1PkO0AoYD7qXLbA9W1J8IoWnqqXyu6EgsH_NJiA)  
  <sub>Seeking Alpha, 21 hours ago</sub>  
  Precious Metals R&S fell 8.6% in October, and its equal-weighted index lost 9.85%.
- [Robinhood onchain: Nvidia trading volume reaches $67.51 million as holder wallets rise by 401](https://www.google.com/goto?url=CAESawHEIkXXvq7vJJMt64VAKQN2_DZzOiHxS5PXRtqFlXCiZ4dbo_LM6uB-bBiKmQaihJekIbKtRZLjOE7UMa9BYRqHrWcukFiHSubM1h55kOnAiRK4vHEyXpvdmkoQLuRGC-8zfDHJNKNxbpUe&gsessionid=3Zn4ygNXHXnKP8Z1PkO0AoYD7qXLbA9W1J8IoWnqqXyu6EgsH_NJiA)  
  <sub>www.tokenpost.com, 2 hours ago</sub>  
  Nvidia's tokenized stock posted $67.51 million in 24-hour trading volume, up 246.8%, while its holder count rose by 401. Trading volume across 200 tokenized...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.17% (+0.03 on the week) | 5-year 4.71% (-0.19 on the week) | 10-year 4.90% (-0.20 on the week) | 30-year 5.29% (-0.17 on the week)
Yield curve, 10-year minus 3-month: +0.73 points -- upward sloping (normal)
US dollar index: 103.81 (+0.32 on the week)
Volatility (VIX): 29.34 (+3.9 on the week) -- stressed
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.1% (2026-10-01) | jobless claims 203k (2026-11-14)
Policy and expectations: Fed target 4.00% | market expects 2.1% inflation over 10 years
Rate path: 2-year Treasury 4.63% vs Fed target 3.75-4.00% -- the bond market prices about 3 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score -0.10</summary>

```text
Last close 332.50 (bar of 2026-11-24), from 501 daily bars
Trend: vs 20d SMA 356.69 (-6.8%), 50d 372.47 (-10.7%), 200d 404.54 (-17.8%); 50d below 200d
Momentum: RSI(14) 32.7 | MACD -11.806 vs signal -8.834 (histogram -2.972)
Returns: 1d -0.2% | 5d -5.7% | 1m -9.6% | 3m -21.1%
52-week range: 322.87 - 495.90 (now 5.6% of the way up)
Volatility: ATR(14) 7.54 (2.3% of price) | annualised 20d 33.2%
Volume: 0.11x the 20-day average
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
Measured: 3 months: fund -21.1%, commodity -22.0%, gap +1.0% | 6 months: fund -18.6%, commodity -18.4%, gap -0.2% | 12 months: fund -11.2%, commodity -11.1%, gap -0.1%
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
Share count change: 1 week: +0.0% (0.00) over 7d | 1 month: +0.0% (0.00) over 31d
Shares outstanding: 260.30M | fund size: 86.55B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Silver (SLV) · Commodity — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:** no explanation. It wrote only “NEUTRAL”, so the main reasons below are all it gave.

**Main reasons it gave:**
- No macro surprise: inflation 3.7% within expectations
- Technical indicators bearish (RSI 28.1, price below 20‑day SMA) but no decisive break on volume
- Positioning shows a crowded short (net long down 2.1% week)
- Fund flows strong (+18% week) offsetting bearish positioning

<details><summary><b>News</b> — score +0.00</summary>

- [Is It Time To Buy Silver? This Put Strategy In Options Trading Counts On A Limited Decline](https://www.investors.com/research/options/is-it-time-to-buy-silver-put-options-strategy-slv-etf/)  
  <sub>Investor's Business Daily, 20 hours ago</sub>  
  Is it time to buy silver after a large decline this year? This put option trade allows investors to go long at a discount.
- [Silver ETF vs Silver FoF vs Physical Silver: 5 Criteria](https://www.valueresearchonline.com/learn/mutual-funds/silver-etf-vs-silver-fof-vs-physical-silver-five-criteria-india-2026/)  
  <sub>Value Research, 1 hour ago</sub>  
  For most investors in 2026, a silver ETF is the cheapest way to own silver if you already have a demat account and can hold for more than 12 months.
- [Silver miners fall as metal price drops on rate hike concerns By Investing.com](https://www.google.com/goto?url=CAEStwEBxCJF14sGbT5WEmA9t2zsTvy7QRxUmwNkGcVU8R0stCroyEOVfcoAWuiV06kg66G_gHf0hGNsUMl1ATfyFp07FjPmoa0eoNP5kmI6VgQxVFVExywdEiTwT4suQh663LFOBYd7XpzO4vS7pf1nRfWMZJKIl9TFxmxnvGpOy8jZMOTPOasq9H3YMS0niUljCShlTFusMEGYTI4EKraHwex42GiWgq2WV107bqxmOew3v7yMczswhYw&gsessionid=EcGROZFneXCDN_4TleU6jdyuRHBXhUq4A7qP4vqmpV_6YVeS7iEqGg)  
  <sub>Investing.com South Africa, 1 hour ago</sub>  
  Investing.com -- US-listed shares of silver mining companies declined in premarket trading Tuesday, following a drop in silver prices.
- [Global X Silver Miners Covered Call ETF (SVCC.TO) Stock Price, News, Quote & History](https://www.google.com/goto?url=CAESaAHEIkXXc0eZJf37AIysj0ygJBuf0zeOy5DVLvyDBEAXt6ET9WkACeAudIk3WCqHtBJX0qBBIaiyYFd0q7FIkFSwSV8LGV3O_D_BwbyUwpidM5n2WIISSFF9HAJbB54nkGFIZYSnITi_&gsessionid=EcGROZFneXCDN_4TleU6jdyuRHBXhUq4A7qP4vqmpV_6YVeS7iEqGg)  
  <sub>Yahoo! Finance Canada, 18 hours ago</sub>  
  Global X Silver Miners Covered Call ETF (SVCC.TO) · -8.80% · -12.08% · -29.91% · -38.66% · -38.66% · -38.66% · -38.66%.
- [How Does the Global X Silver Miners ETF (ASX:SLVM) Capture the Performance of Silver Mining Companies?](https://www.google.com/goto?url=CAESwwEBxCJF1503W61BSucK2zepHo-4X7zEesp7XXmYEb5DuPmwUkMgqjNqAGv_uehDVyI3-7RYkM61K2ulxaa72im3hzrfRPUNkFK7WGLmA1iiWLXYwnmEgQ7MnSdufdCyyb-qHIh9XaAP23L6mAgVWHCsPIiXwDq55AdLUqd1iXzSYBBHvk8q1n2xa2lFMz3gs2179vuE44Tut9MO2T9WhaABFTlMTEJWVsmAz_0AAlyYzpHO-GEs3NnueQ8D1jp0NIpeMqg&gsessionid=EcGROZFneXCDN_4TleU6jdyuRHBXhUq4A7qP4vqmpV_6YVeS7iEqGg)  
  <sub>Kalkine, 8 hours ago</sub>  
  How Does the Global X Silver Miners ETF (ASX:SLVM) Capture the Performance of Silver Mining Companies?
- [Silver miners fall as metal price drops on rate hike concerns](https://www.google.com/goto?url=CAEStwEBxCJF10vMoQAe5zkENKzAX_1Mhn-Q1LwNp1_rwxlwitcBg9L-FSWbSFhQiJ_ymZX_4pYOCeqjVo7kn-wIdWo98BuSIKCDSj9oB7vMm129sSliE1rhGjWS-P0askzTCOppn5eq0ZH6sPqB2B_CGrrx9UhghI2gYV1qPVqmEa-bTdU7Dn_i-tkP273HaZ4A-bFztASpZd2HQkbtgcQAXwfeFppIBjX2hPSFzVbx2igKTyQYD_lRBNc&gsessionid=EcGROZFneXCDN_4TleU6jdyuRHBXhUq4A7qP4vqmpV_6YVeS7iEqGg)  
  <sub>Investing.com Australia, 2 hours ago</sub>  
  Investing.com -- US-listed shares of silver mining companies declined in premarket trading Tuesday, following a drop in silver prices.
- [First Majestic Silver Corp. (AG.TO) Stock Price, News, Quote & History](https://www.google.com/goto?url=CAESZgHEIkXX8JFch6k48J5N-QuDST8KiycCIn3bIC_bEvm6ZeI7cfXfuaB2mZku1jcWMuty6vhk_0sCUq4oxPblTjQZSShoDnTk18vjQocYM6eIoBMCX0PSHFd6s_6VOgDWkNaAhQY4Aw&gsessionid=EcGROZFneXCDN_4TleU6jdyuRHBXhUq4A7qP4vqmpV_6YVeS7iEqGg)  
  <sub>Yahoo! Finance Canada, 15 hours ago</sub>  
  Find the latest First Majestic Silver Corp. (AG.TO) stock quote, history, news and other vital information to help you with your stock trading and...
- [Gold and silver ETF AUM jumps nearly 2X in a year as investor interest grows](https://www.google.com/goto?url=CAESygEBxCJF15WnMIa8ZBjEMzTErE5CIY2Y6Z8j63TpE9DPbQHvQAZqI45OO95AlbhBQkwyGCMqvdgGkJQ23avS8Kyp-t4r-Tpko_iFgnVmD1PaEzEZExEhyyh0XFLQqja-htox_Y8RmLuYRUganSjI4DMK5UOkn0v5qf_CwQYEnIaLsxfZNv8aXOmky2wUjcK7u08uebSwArCm4ncaXkD1bVaMwOfXyVrzIw1QCk2J9t1XB53N7NJbusE6S-sBMD1Q2IMMjFUtqFf-6igM&gsessionid=EcGROZFneXCDN_4TleU6jdyuRHBXhUq4A7qP4vqmpV_6YVeS7iEqGg)  
  <sub>The Economic Times, 7 hours ago</sub>  
  Gold and silver ETFs have attracted significant investor interest, with their assets under management (AUM) nearly doubling over the past year, according to...
- [Gold, Silver Price Outlook 2027: Is A Big Recovery Coming?](https://www.google.com/goto?url=CAESqQEBxCJF1_uboevsE21uThk-0-EERzvKivu5eiY0oVVmxXVnGl-hCx7cQNIajmesWpnR2WBMdJzuG-9RxVhRy0fUyfGrPNo62qgw7wIOr35u28jOrv-LlM8Qxgp2rwlXLR3BvpGnU82K2uLYW3OLZ1arDRXg8gTapTLwHamhVDyoz97k9EUEmrpvBLkh4ORhutXDPmMnp95--9sthtamY-wyJqeWUIvFOv5q&gsessionid=EcGROZFneXCDN_4TleU6jdyuRHBXhUq4A7qP4vqmpV_6YVeS7iEqGg)  
  <sub>ETV Bharat, 6 hours ago</sub>  
  New Delhi: Gold and Silver prices have witnessed a sharp decline after scaling record highs in January 2026. Despite the drop in prices, central banks and...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.17% (+0.03 on the week) | 5-year 4.71% (-0.19 on the week) | 10-year 4.90% (-0.20 on the week) | 30-year 5.29% (-0.17 on the week)
Yield curve, 10-year minus 3-month: +0.73 points -- upward sloping (normal)
US dollar index: 103.81 (+0.32 on the week)
Volatility (VIX): 29.34 (+3.9 on the week) -- stressed
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.1% (2026-10-01) | jobless claims 203k (2026-11-14)
Policy and expectations: Fed target 4.00% | market expects 2.1% inflation over 10 years
Rate path: 2-year Treasury 4.63% vs Fed target 3.75-4.00% -- the bond market prices about 3 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 38.25 (bar of 2026-11-24), from 501 daily bars
Trend: vs 20d SMA 44.12 (-13.3%), 50d 50.26 (-23.9%), 200d 60.73 (-37.0%); 50d below 200d
Momentum: RSI(14) 28.1 | MACD -3.319 vs signal -2.817 (histogram -0.502)
Returns: 1d -1.7% | 5d -10.3% | 1m -21.4% | 3m -37.9%
52-week range: 36.97 - 105.60 (now 1.9% of the way up)
Volatility: ATR(14) 1.69 (4.4% of price) | annualised 20d 52.2%
Volume: 0.22x the 20-day average
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
Cost of holding this fund instead of silver itself: -0.2% a year -- close to nothing, as a physically backed fund should be
Measured: 3 months: fund -37.9%, commodity -37.9%, gap +0.0% | 6 months: fund -43.3%, commodity -43.4%, gap +0.1% | 12 months: fund -15.6%, commodity -15.4%, gap -0.2%
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
Share count change: 1 week: +18.1% (3.87B) over 7d | 1 month: +14.3% (3.14B) over 32d
Shares outstanding: 658.92M | fund size: 25.20B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Sugar (CANE) · Commodity — no answer, no confidence given

**This one did not finish:** the full-model stage ran past its 120 minute budget before CANE was asked

<details><summary><b>News</b> — score n/a</summary>

_No news found for this one today._

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score n/a</summary>

```text
US Treasury yields: 3-month 4.17% (+0.03 on the week) | 5-year 4.71% (-0.19 on the week) | 10-year 4.90% (-0.20 on the week) | 30-year 5.29% (-0.17 on the week)
Yield curve, 10-year minus 3-month: +0.73 points -- upward sloping (normal)
US dollar index: 103.81 (+0.32 on the week)
Volatility (VIX): 29.34 (+3.9 on the week) -- stressed
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.1% (2026-10-01) | jobless claims 203k (2026-11-14)
Policy and expectations: Fed target 4.00% | market expects 2.1% inflation over 10 years
Rate path: 2-year Treasury 4.63% vs Fed target 3.75-4.00% -- the bond market prices about 3 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score n/a</summary>

```text
Last close 10.65 (bar of 2026-11-24), from 501 daily bars
Trend: vs 20d SMA 11.03 (-3.4%), 50d 11.48 (-7.2%), 200d 10.34 (+3.0%); 50d above 200d
Momentum: RSI(14) 39.2 | MACD -0.302 vs signal -0.253 (histogram -0.049)
Returns: 1d +1.1% | 5d -2.6% | 1m -7.1% | 3m -5.1%
52-week range: 9.02 - 12.47 (now 47.4% of the way up)
Volatility: ATR(14) 0.23 (2.1% of price) | annualised 20d 28.8%
Volume: 0.28x the 20-day average
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
Cost of holding this fund instead of sugar itself: -8.1% a year -- heavy: rolling contracts costs this fund real money
Measured: 3 months: fund -5.1%, commodity +1.0%, gap -6.1% | 6 months: fund +11.1%, commodity +25.7%, gap -14.6% | 12 months: fund +12.2%, commodity +20.2%, gap -8.1%
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
Contract: SUGAR NO. 11 - ICE FUTURES U.S. (positions as of 2026-11-17, published the following Friday)
Large speculators: net long 16.3% of open interest (1,144,499 contracts)
Change on the week: -0.7% of open interest
Crowding: 82% percentile over 52 weeks -- within its normal range
Read this as crowding, not as a forecast: an extreme is as often the end of a move as the middle of one.
```

</details>

<details><summary><b>Money going into and out of this fund</b> — score n/a</summary>

```text
Direction: money coming in (1 month)
Share count change: 1 week: +8.8% (4.98M) over 7d | 1 month: +30.8% (14.46M) over 31d
Shares outstanding: 5.76M | fund size: 61.33M
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Corn (CORN) · Commodity — no answer, no confidence given

**This one did not finish:** the full-model stage ran past its 120 minute budget before CORN was asked

<details><summary><b>News</b> — score n/a</summary>

- [Petrobras (PBR) to Acquire 42% Stake in Neomille S.A. Corn Ethan](https://www.gurufocus.com/news/9216599/petrobras-pbr-to-acquire-42-stake-in-neomille-sa-corn-ethanol-producer)  
  <sub>GuruFocus, 5 hours ago</sub>  
  On November 24, 2026, Petroleo Brasileiro SA (NYSE: PBR) announced its plan to acquire a 42% interest in Brazilian corn ethanol producer Neomille S.A. for...
- [Petrobras Agrees to Acquire 42% Stake in Corn Ethanol Producer](https://www.tipranks.com/news/company-announcements/petrobras-agrees-to-acquire-42-stake-in-corn-ethanol-producer)  
  <sub>TipRanks, 16 hours ago</sub>  
  The latest update is out from Petroleo Brasileiro SA ( ($BR:PETR3) ). Petrobras agreed to acquire a 42% stake in Neomille, a corn ethanol producer owned by...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score n/a</summary>

```text
US Treasury yields: 3-month 4.17% (+0.03 on the week) | 5-year 4.71% (-0.19 on the week) | 10-year 4.90% (-0.20 on the week) | 30-year 5.29% (-0.17 on the week)
Yield curve, 10-year minus 3-month: +0.73 points -- upward sloping (normal)
US dollar index: 103.81 (+0.32 on the week)
Volatility (VIX): 29.34 (+3.9 on the week) -- stressed
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.1% (2026-10-01) | jobless claims 203k (2026-11-14)
Policy and expectations: Fed target 4.00% | market expects 2.1% inflation over 10 years
Rate path: 2-year Treasury 4.63% vs Fed target 3.75-4.00% -- the bond market prices about 3 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score n/a</summary>

```text
Last close 16.96 (bar of 2026-11-24), from 501 daily bars
Trend: vs 20d SMA 17.19 (-1.4%), 50d 18.19 (-6.8%), 200d 18.16 (-6.6%); 50d above 200d
Momentum: RSI(14) 35.7 | MACD -0.313 vs signal -0.348 (histogram 0.035)
Returns: 1d -0.2% | 5d -1.7% | 1m -3.8% | 3m -15.3%
52-week range: 16.47 - 20.29 (now 12.8% of the way up)
Volatility: ATR(14) 0.24 (1.4% of price) | annualised 20d 14.6%
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
Cost of holding this fund instead of corn itself: -9.6% a year -- heavy: rolling contracts costs this fund real money
Measured: 3 months: fund -15.3%, commodity -12.3%, gap -3.1% | 6 months: fund -5.8%, commodity -0.3%, gap -5.4% | 12 months: fund -3.6%, commodity +6.0%, gap -9.6%
A commodity fund holds futures, not corn, and must sell each expiring contract to buy the next one. Where the next month costs more, that roll loses money every month. This gap is what the structure has actually cost, fees included -- it is history rather than a forecast, and it is not a direction: heavy carry is a reason to want a larger move to justify a long, and a tailwind for a short.
```

</details>

<details><summary><b>How much oil and gas is in storage</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>How the crop is growing</b> — score n/a</summary>

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

<details><summary><b>Buying and selling by company insiders</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>Who is positioned how</b> — score n/a</summary>

```text
Contract: CORN - CHICAGO BOARD OF TRADE (positions as of 2026-11-17, published the following Friday)
Large speculators: net short 1.7% of open interest (1,954,229 contracts)
Change on the week: -0.6% of open interest
Crowding: 30% percentile over 52 weeks -- within its normal range
Read this as crowding, not as a forecast: an extreme is as often the end of a move as the middle of one.
```

</details>

<details><summary><b>Money going into and out of this fund</b> — score n/a</summary>

```text
Direction: money going out (1 month)
Share count change: 1 week: +1.3% (1.34M) over 7d | 1 month: -13.5% (-16.78M) over 31d
Shares outstanding: 6.32M | fund size: 107.27M
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Copper (CPER) · Commodity — no answer, no confidence given

**This one did not finish:** the full-model stage ran past its 120 minute budget before CPER was asked

<details><summary><b>News</b> — score n/a</summary>

_No news found for this one today._

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score n/a</summary>

```text
US Treasury yields: 3-month 4.17% (+0.03 on the week) | 5-year 4.71% (-0.19 on the week) | 10-year 4.90% (-0.20 on the week) | 30-year 5.29% (-0.17 on the week)
Yield curve, 10-year minus 3-month: +0.73 points -- upward sloping (normal)
US dollar index: 103.81 (+0.32 on the week)
Volatility (VIX): 29.34 (+3.9 on the week) -- stressed
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.1% (2026-10-01) | jobless claims 203k (2026-11-14)
Policy and expectations: Fed target 4.00% | market expects 2.1% inflation over 10 years
Rate path: 2-year Treasury 4.63% vs Fed target 3.75-4.00% -- the bond market prices about 3 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score n/a</summary>

```text
Last close 32.90 (bar of 2026-11-24), from 501 daily bars
Trend: vs 20d SMA 36.89 (-10.8%), 50d 38.67 (-14.9%), 200d 37.90 (-13.2%); 50d above 200d
Momentum: RSI(14) 25.6 | MACD -1.580 vs signal -1.136 (histogram -0.444)
Returns: 1d -2.7% | 5d -8.6% | 1m -16.5% | 3m -17.9%
52-week range: 31.11 - 41.43 (now 17.4% of the way up)
Volatility: ATR(14) 0.87 (2.6% of price) | annualised 20d 30.0%
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
Cost of holding this fund instead of copper itself: -4.8% a year -- a steady drag
Measured: 3 months: fund -17.9%, commodity -15.9%, gap -2.0% | 6 months: fund -14.5%, commodity -12.0%, gap -2.5% | 12 months: fund +5.9%, commodity +10.8%, gap -4.8%
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
Contract: COPPER- #1 - COMMODITY EXCHANGE INC. (positions as of 2026-11-17, published the following Friday)
Large speculators: net long 9.1% of open interest (314,991 contracts)
Change on the week: -2.1% of open interest
Crowding: 2% percentile over 52 weeks -- a crowded short by the standards of the past year
Read this as crowding, not as a forecast: an extreme is as often the end of a move as the middle of one.
```

</details>

<details><summary><b>Money going into and out of this fund</b> — score n/a</summary>

```text
Direction: money coming in (1 month)
Share count change: 1 week: +11.0% (65.33M) over 7d | 1 month: +8.3% (50.74M) over 31d
Shares outstanding: 20.08M | fund size: 660.69M
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Soybeans (SOYB) · Commodity — no answer, no confidence given

**This one did not finish:** the full-model stage ran past its 120 minute budget before SOYB was asked

<details><summary><b>News</b> — score n/a</summary>

_No news found for this one today._

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score n/a</summary>

```text
US Treasury yields: 3-month 4.17% (+0.03 on the week) | 5-year 4.71% (-0.19 on the week) | 10-year 4.90% (-0.20 on the week) | 30-year 5.29% (-0.17 on the week)
Yield curve, 10-year minus 3-month: +0.73 points -- upward sloping (normal)
US dollar index: 103.81 (+0.32 on the week)
Volatility (VIX): 29.34 (+3.9 on the week) -- stressed
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.1% (2026-10-01) | jobless claims 203k (2026-11-14)
Policy and expectations: Fed target 4.00% | market expects 2.1% inflation over 10 years
Rate path: 2-year Treasury 4.63% vs Fed target 3.75-4.00% -- the bond market prices about 3 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score n/a</summary>

```text
Last close 25.95 (bar of 2026-11-24), from 501 daily bars
Trend: vs 20d SMA 25.74 (+0.8%), 50d 26.69 (-2.8%), 200d 25.39 (+2.2%); 50d above 200d
Momentum: RSI(14) 48.6 | MACD -0.241 vs signal -0.307 (histogram 0.066)
Returns: 1d +0.8% | 5d +0.3% | 1m -1.9% | 3m -3.0%
52-week range: 21.71 - 28.14 (now 65.9% of the way up)
Volatility: ATR(14) 0.29 (1.1% of price) | annualised 20d 15.1%
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
Cost of holding this fund instead of soybeans itself: 1.0% a year -- the roll has been paying this fund
Measured: 3 months: fund -3.0%, commodity -1.4%, gap -1.6% | 6 months: fund +4.1%, commodity +4.4%, gap -0.3% | 12 months: fund +11.0%, commodity +10.0%, gap +1.0%
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
Contract: SOYBEANS - CHICAGO BOARD OF TRADE (positions as of 2026-11-17, published the following Friday)
Large speculators: net long 11.4% of open interest (997,948 contracts)
Change on the week: -0.7% of open interest
Crowding: 28% percentile over 52 weeks -- within its normal range
Read this as crowding, not as a forecast: an extreme is as often the end of a move as the middle of one.
```

</details>

<details><summary><b>Money going into and out of this fund</b> — score n/a</summary>

```text
Direction: money going out (1 month)
Share count change: 1 week: +1.1% (448.43K) over 7d | 1 month: -10.1% (-4.47M) over 31d
Shares outstanding: 1.53M | fund size: 39.68M
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Natural gas (UNG) · Commodity — no answer, no confidence given

**This one did not finish:** the full-model stage ran past its 120 minute budget before UNG was asked

<details><summary><b>News</b> — score n/a</summary>

- [Jensen Huang Returns to Nvidia; NVDA Surges 32%, Nasdaq Rips 7%, and Taiwan Reverses Last Week’s Entire Collapse in a Single Session](https://www.theglobeandmail.com/investing/markets/stocks/NVDA/pressreleases/8970269/jensen-huang-returns-to-nvidia-nvda-surges-32-nasdaq-rips-7-and-taiwan-reverses-last-weeks-entire-collapse-in-a-single-session/)  
  <sub>The Globe and Mail, 20 hours ago</sub>  
  Detailed price information for Nvidia Corp (NVDA-Q) from The Globe and Mail including charting and trades.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score n/a</summary>

```text
US Treasury yields: 3-month 4.17% (+0.03 on the week) | 5-year 4.71% (-0.19 on the week) | 10-year 4.90% (-0.20 on the week) | 30-year 5.29% (-0.17 on the week)
Yield curve, 10-year minus 3-month: +0.73 points -- upward sloping (normal)
US dollar index: 103.81 (+0.32 on the week)
Volatility (VIX): 29.34 (+3.9 on the week) -- stressed
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.1% (2026-10-01) | jobless claims 203k (2026-11-14)
Policy and expectations: Fed target 4.00% | market expects 2.1% inflation over 10 years
Rate path: 2-year Treasury 4.63% vs Fed target 3.75-4.00% -- the bond market prices about 3 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score n/a</summary>

```text
Last close 10.21 (bar of 2026-11-24), from 501 daily bars
Trend: vs 20d SMA 9.82 (+3.9%), 50d 10.27 (-0.6%), 200d 10.90 (-6.3%); 50d below 200d
Momentum: RSI(14) 51.7 | MACD 0.041 vs signal -0.023 (histogram 0.065)
Returns: 1d +3.5% | 5d +1.7% | 1m +6.8% | 3m -1.9%
52-week range: 9.00 - 16.90 (now 15.3% of the way up)
Volatility: ATR(14) 0.44 (4.3% of price) | annualised 20d 55.5%
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
Cost of holding this fund instead of natural gas itself: -10.1% a year -- heavy: rolling contracts costs this fund real money
Measured: 3 months: fund -1.9%, commodity +28.5%, gap -30.5% | 6 months: fund -8.7%, commodity +20.2%, gap -28.8% | 12 months: fund -30.3%, commodity -20.2%, gap -10.1%
A commodity fund holds futures, not natural gas, and must sell each expiring contract to buy the next one. Where the next month costs more, that roll loses money every month. This gap is what the structure has actually cost, fees included -- it is history rather than a forecast, and it is not a direction: heavy carry is a reason to want a larger move to justify a long, and a tailwind for a short.
```

</details>

<details><summary><b>How much oil and gas is in storage</b> — score n/a</summary>

```text
US inventories, week ending 2026-11-13 (published the following Wednesday)
  Natural gas: 3,882.0 billion cubic feet, +20.0 on the week (a build), 96% percentile over 52 weeks -- high for the time of year
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
Contract: NAT GAS NYME - NEW YORK MERCANTILE EXCHANGE (positions as of 2026-11-17, published the following Friday)
Large speculators: net short 13.0% of open interest (1,630,218 contracts)
Change on the week: +0.7% of open interest
Crowding: 5% percentile over 52 weeks -- a crowded short by the standards of the past year
Read this as crowding, not as a forecast: an extreme is as often the end of a move as the middle of one.
```

</details>

<details><summary><b>Money going into and out of this fund</b> — score n/a</summary>

```text
Direction: money coming in (1 month)
Share count change: 1 week: -3.8% (-19.06M) over 7d | 1 month: +4.5% (20.88M) over 32d
Shares outstanding: 47.91M | fund size: 489.17M
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Oil (USO) · Commodity — no answer, no confidence given

**This one did not finish:** the full-model stage ran past its 120 minute budget before USO was asked

<details><summary><b>News</b> — score n/a</summary>

- [Oil And Gas Lift Energy ETFs Ahead Of Tuesday’s Open](https://finimize.com/content/oil-and-gas-lift-energy-etfs-ahead-of-tuesdays-open)  
  <sub>Finimize, 47 minutes ago</sub>  
  WTI traded near $80.68 a barrel and natural gas futures rose to about $3.28, while BP and Cmb.Tech shares ticked higher premarket.
- [Scott Bessent Unleashes Fresh Iran Sanctions as Tehran Warns Tankers Against Using Strait of Hormuz: Crud](https://www.benzinga.com/news/politics/26/11/63568282/scott-bessent-unleashes-fresh-iran-sanctions-as-tehran-warns-tankers-against-using-strait-of-hormuz-crude-oil-prices-continue-to-cool)  
  <sub>Benzinga, 9 hours ago</sub>  
  Treasury Secretary Scott Bessent sanctioned Iranian shadow banking networks, while tensions rise over Strait of Hormuz incidents.
- [One-of-a-kind Jeep Wrangler Commando 392 Raises $174,000 for USO, Giving Back to Military Families This Holiday Season](https://www.google.com/goto?url=CAES0AEBxCJF1xGlhSC-05dFGNE6JuU9m5_0CcPtfYAcqaCNhYxVakIKC8XXgnLX8nbzo4QF-AZc-ONzdNu2sb_2OVoEjtehKON2WscXmnxX4CXxxLRkg18EsNdewMN3rZhPFbRNjEMo3fzTgLbUKiNeVKn7LTELKntMmuWM2U7_mU1Mg-SP8_6sWoVbGdepJTdsSBx-lsOKLx-UZGr-BavrXrnTP2qDjPbtgxRK6gYq_-Tx6B3Hv7AX7H2lh6r8rrfSv-ZS3D6Lw90gZGRWvSPuBMrD&gsessionid=rN96I-F4JU8HOtKiZysNXneseze1fS-zhs0a36fRGOAapCePqi01uA)  
  <sub>Finviz, 17 hours ago</sub>  
  AUBURN HILLS, Mich., Nov. 23, 2026 /PRNewswire/ --. The one-of-a-kind 2026 Jeep® Wrangler Commando 392 raised $174,000. Exclusive Jeep® Wrangler Commando...
- [Senate panel probes JD Vance's role in Vitol's Venezuela oil real: report (XLE:NYSEARCA)](https://www.google.com/goto?url=CAESvAEBxCJF1_nS386mdbBOVJwwM4sKtOYqmsr1jGfAtpwF9HdOMmVCM8aPcMDP4M5FdNm0SRwuyfcozrWZG2MKoOtCGBuf6YoUP_5ZsOm20pbRwDaVr0fcwFNt7UnEjRWE509VE4frerZODV1ahzqjgVLKoABe8R3usHKX5kIm9NpFxfzrjB7qQ_GCBINyn1ezxWfF0ivJjFtrnBRwmSV1WwBIDezKNYFs-_GR8CUPKtZOHliulV2sAj_21vvNIA&gsessionid=rN96I-F4JU8HOtKiZysNXneseze1fS-zhs0a36fRGOAapCePqi01uA)  
  <sub>Seeking Alpha, 10 hours ago</sub>  
  A U.S. Senate committee is reportedly investigating whether US Vice President JD Vance played a ​role in the awarding of a lucrative Venezuelan oil deal to...
- [Huang Reinstated—Time To Add Positions In AI And Semi Stocks](https://www.google.com/goto?url=CAESqQEBxCJF17x8bzZEQ8imqDHNUUosmNoeVQXxV_okThGeVgMf0GGJx_Uz-T5qB7EeSYGcLAvB-nrafdjXpCvQ-gM3tA5KxNJZYxohUB3h5fgDG59IpVrne37s_G7dp1GWzhxzYpdjMd_AnsfiCr-ch4h2wJnJ2xNUXGo2IMbAdduMzNhVOPsYdoesV52ewv3rTxv4b2kn0Ek9hk57FxPBYwXkKk992bYta4qw&gsessionid=rN96I-F4JU8HOtKiZysNXneseze1fS-zhs0a36fRGOAapCePqi01uA)  
  <sub>Benzinga, 20 hours ago</sub>  
  Jensen Is Back Please click here for a chart of Invesco QQQ Trust Series 1 (NASDAQ:QQQ). Note the following: The chart shows a huge rally on the news of...
- [Sam Price señala una gran salida de fondos del ETF de Bitcoin en EE. UU.](https://www.google.com/goto?url=CAEStAEBxCJF18dhaOkbiFEf5mUov55tJ4P29uXnrLKiKuk2O7ipBCORR6B5WhsS0CYnOod8bsrB9oGeketqGLJlSg-SDcO2_8fgsNtp8MgKHJhYkDDbMA9pS_qLa4vh7FqrTZvDsNw_6hOGpnQf_P6tO9dhVpWoXgzJZFYgf_ZGUDsC3qGUKPsxYRCsXKpb4QywIVzKtuofRW4LlNM9tI3DuFkq5Lc6EY_MZLlA9yvHgfi6hQTW0g0&gsessionid=rN96I-F4JU8HOtKiZysNXneseze1fS-zhs0a36fRGOAapCePqi01uA)  
  <sub>WEEX, 7 hours ago</sub>  
  Según el usuario de Twitter Sam Price, el ETF de Bitcoin al contado en EE. UU. experimentó una salid.
- [Bitcoin borra el rebote del lunes y vuelve a caer por debajo de los 60.000 dólares](https://www.google.com/goto?url=CAESlQEBxCJF179BzEbgQ5wKmSo21JT-5--6ghv-I_5ilqK4Yj9hGJOU_yu2AdXWT3op1k6ly_Uffjwob_ZdYVetaM7mNzn_lkBAEEYmJrgUHxGHX1_gAkdmWyj5KQcUEJf-tKoSwtr46qhhgsgAO2R8o1prM7LtQEii__xWoCDEfVAxgkNilKLIXlZXqUKPAiatfuMH-UaPEA&gsessionid=rN96I-F4JU8HOtKiZysNXneseze1fS-zhs0a36fRGOAapCePqi01uA)  
  <sub>Observatorio Blockchain, 5 hours ago</sub>  
  Bitcoin cae por debajo de 60.000 dólares tras el rebote por Nvidia y los ETF de bitcoin y ether anotan salidas de 654,6 millones de dólares.
- [$KWEB $BABA $QQQ Estructura de gráfico interesante con un ro](https://www.google.com/goto?url=CAESgAEBxCJF14t8t4ReeGgbyMXSmeXzWMk_TqdwbmLIOY4XRGyO8vFH-5_nwnmXnZcjseMp-ZVpDvVcnen5h3A2gOGYYR04zq44QSk5Baviqg4x8XVjscD-YCfnVDiCHQTUge7Cc0nQpeRNHzMZj2Ca_uSWBbsdcULITS0IZPMaWjJXGQ&gsessionid=rN96I-F4JU8HOtKiZysNXneseze1fS-zhs0a36fRGOAapCePqi01uA)  
  <sub>KuCoin, 21 hours ago</sub>  
  KWEB $BABA $QQQ Estructura de gráfico interesante con un rompimiento de tendencia formándose aquí en el ETF de KraneShares. https://t.co/UPgzmD3wfO.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score n/a</summary>

```text
US Treasury yields: 3-month 4.17% (+0.03 on the week) | 5-year 4.71% (-0.19 on the week) | 10-year 4.90% (-0.20 on the week) | 30-year 5.29% (-0.17 on the week)
Yield curve, 10-year minus 3-month: +0.73 points -- upward sloping (normal)
US dollar index: 103.81 (+0.32 on the week)
Volatility (VIX): 29.34 (+3.9 on the week) -- stressed
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.1% (2026-10-01) | jobless claims 203k (2026-11-14)
Policy and expectations: Fed target 4.00% | market expects 2.1% inflation over 10 years
Rate path: 2-year Treasury 4.63% vs Fed target 3.75-4.00% -- the bond market prices about 3 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score n/a</summary>

```text
Last close 135.45 (bar of 2026-11-24), from 501 daily bars
Trend: vs 20d SMA 147.04 (-7.9%), 50d 150.67 (-10.1%), 200d 129.76 (+4.4%); 50d above 200d
Momentum: RSI(14) 37.1 | MACD -4.965 vs signal -3.582 (histogram -1.383)
Returns: 1d +1.6% | 5d -3.4% | 1m -18.5% | 3m +6.4%
52-week range: 66.17 - 169.53 (now 67.0% of the way up)
Volatility: ATR(14) 5.02 (3.7% of price) | annualised 20d 49.2%
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

_Not available today._

</details>

<details><summary><b>How much oil and gas is in storage</b> — score n/a</summary>

```text
US inventories, week ending 2026-11-13 (published the following Wednesday)
  Crude oil: 417.8 million barrels, +3.4 on the week (a build), 25% percentile over 52 weeks
  Petrol: 215.9 million barrels, +5.2 on the week (a build), 56% percentile over 52 weeks
  Diesel: 104.9 million barrels, +1.6 on the week (a build), 33% percentile over 52 weeks
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
Share count change: 1 week: +4.6% (83.52M) over 7d | 1 month: +31.9% (459.84M) over 32d
Shares outstanding: 14.04M | fund size: 1.90B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Wheat (WEAT) · Commodity — no answer, no confidence given

**This one did not finish:** the full-model stage ran past its 120 minute budget before WEAT was asked

<details><summary><b>News</b> — score n/a</summary>

_No news found for this one today._

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score n/a</summary>

```text
US Treasury yields: 3-month 4.17% (+0.03 on the week) | 5-year 4.71% (-0.19 on the week) | 10-year 4.90% (-0.20 on the week) | 30-year 5.29% (-0.17 on the week)
Yield curve, 10-year minus 3-month: +0.73 points -- upward sloping (normal)
US dollar index: 103.81 (+0.32 on the week)
Volatility (VIX): 29.34 (+3.9 on the week) -- stressed
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.1% (2026-10-01) | jobless claims 203k (2026-11-14)
Policy and expectations: Fed target 4.00% | market expects 2.1% inflation over 10 years
Rate path: 2-year Treasury 4.63% vs Fed target 3.75-4.00% -- the bond market prices about 3 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score n/a</summary>

```text
Last close 21.35 (bar of 2026-11-24), from 501 daily bars
Trend: vs 20d SMA 21.80 (-2.0%), 50d 23.50 (-9.1%), 200d 23.63 (-9.7%); 50d below 200d
Momentum: RSI(14) 35.8 | MACD -0.566 vs signal -0.635 (histogram 0.069)
Returns: 1d -0.8% | 5d -2.9% | 1m -5.3% | 3m -20.9%
52-week range: 19.88 - 28.00 (now 18.1% of the way up)
Volatility: ATR(14) 0.39 (1.8% of price) | annualised 20d 22.3%
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
Cost of holding this fund instead of wheat itself: -10.4% a year -- heavy: rolling contracts costs this fund real money
Measured: 3 months: fund -20.9%, commodity -19.0%, gap -1.9% | 6 months: fund -10.1%, commodity -4.9%, gap -5.2% | 12 months: fund +1.9%, commodity +12.3%, gap -10.4%
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
Contract: WHEAT-SRW - CHICAGO BOARD OF TRADE (positions as of 2026-11-17, published the following Friday)
Large speculators: net short 15.2% of open interest (558,414 contracts)
Change on the week: -0.6% of open interest
Crowding: 30% percentile over 52 weeks -- within its normal range
Read this as crowding, not as a forecast: an extreme is as often the end of a move as the middle of one.
```

</details>

<details><summary><b>Money going into and out of this fund</b> — score n/a</summary>

```text
Direction: money going out (1 month)
Share count change: 1 week: +2.0% (4.50M) over 7d | 1 month: -12.0% (-31.93M) over 31d
Shares outstanding: 10.95M | fund size: 233.71M
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

