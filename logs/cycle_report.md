# Daily report

**25 Nov 2026, 18:09 Israel time (16:09 UTC)** · 80 names checked · 3 traded · 0 with a problem

**Answers with no explanation:** 12 of 67 (the model wrote only a label, like “NEUTRAL”, where its reason should be). Their main reasons are still shown.

**Run:** started by the outside scheduler (via supabase-cron), on time (planned for 14:40 UTC).

| Group | Looked at | Took a side | No clear view | Problems |
| --- | --- | --- | --- | --- |
| Companies | 16 | 4 | 12 | 0 |
| Whole-market funds | 14 | 0 | 14 | 0 |
| Sector and country funds | 41 | 0 | 41 | 0 |
| Commodities | 9 | 1 | 8 | 0 |

## Open positions

Checked before any new trade. R is what the trade risked at entry; the ladder sells a third at +1R and another at +3R, the stop-loss follows the price up every day, and it only ever moves up.

| Position | What happened |
| --- | --- |
| South Korea (EWY) · Sector or country | **Stop raised.** At +0.95R, following the price. Stop-loss raised 143.75 → 138.53. |
| Brazil (EWZ) · Sector or country | **Stop raised.** At +1.23R, following the price. Stop-loss raised 31.27 → 31.09. |
| HDFC Bank (HDB) · Company | **Stop raised.** At +4.42R, following the price. Stop-loss raised 26.52 → 26.71. |
| JPMorgan Chase (JPM) · Company | **Stop raised.** At +1.00R, following the price. Stop-loss raised 331.74 → 327.63. |
| Procter & Gamble (PG) · Company | **Stop raised.** At +1.85R, following the price. Stop-loss raised 165.90 → 166.99. |
| Royal Bank of Canada (RY) · Company | **Stop raised.** At +0.36R, following the price. Stop-loss raised 195.20 → 193.73. |
| Elbit Systems (ESLT) · Company | **Holding.** -0.96R, holding 7 shares. Stop-loss 640.17. |
| Eli Lilly (LLY) · Company | **Holding.** -0.15R, holding 3 shares. Stop-loss 1320.29. |
| MercadoLibre (MELI) · Company | **Holding.** +0.43R, holding 3 shares. Stop-loss 1505.92. |
| Novo Nordisk (NVO) · Company | **Holding.** -0.48R, holding 5 shares. Stop-loss 41.18. |
| Toyota (TM) · Company | **Holding.** -0.01R, holding 1 shares. Stop-loss 205.44. |
| US media and communication (XLC) · Sector or country | **Holding.** -0.58R, holding 66 shares. Stop-loss 99.77. |
| Exxon Mobil (XOM) · Company | **Holding.** -0.46R, holding 30 shares. Stop-loss 153.50. |

## How to read this

Once a day the system looks at every name on the list. For each one it reads five kinds of evidence and gives each kind a score from -1.00 (bad) to +1.00 (good). Then it picks a side and says how sure it is, from 0.00 to 1.00.

The three sides: **BULLISH** = the model thinks the price will go up; **BEARISH** = the model thinks the price will go down; **NEUTRAL** = the model has no clear view.

Being sure is not enough on its own. A trade only happens when confidence reaches **0.30**. Below that the system writes down what it thought and does nothing. The size of a trade, the stop-loss and every limit are decided by plain code, not by the model.

Open positions are checked first, before any new trade. When a trade has earned back what it risked (+1R), a third of it is sold and the stop-loss moves up to the entry price, so it can no longer lose. At three times that (+3R) another third is sold and the stop moves up again. The last third stays open. Every day the stop-loss also follows the price up, so a position only ever closes when its stop is hit. The stop only ever moves up.

Under each name you will find the five scores. Click a grey line to open it and see the exact evidence behind that score. The words inside quotation marks are the model's own; nothing there has been rewritten.

## Companies

### Nvidia (NVDA) · Company — BULLISH, confidence 0.60

**Result:** ACCEPTED · 1 shares · submitted buy 1 NVDA @ ~141.94, stop 115.17

**In the model's own words:**

> Fundamentals are extremely strong and earnings record is consistently positive, while analyst consensus remains bullish. A material product‑pipeline catalyst (Vera Rubin chips) adds upside, but technicals show significant short‑term weakness, tempering conviction to a moderate level.

**Main reasons it gave:**
- Vera Rubin chips projected to generate $40B per gigawatt (product pipeline news)
- Trailing P/E 15.25, forward P/E 8.55, PEG 0.15 (valuation indicates cheap growth)
- Four consecutive earnings beats (consistent earnings record)
- Price 30% below 50-day SMA, RSI 35 (technical weakness)
- Analyst consensus 49 buy/strong-buy vs 2 sell, price target +72% (bullish analyst view)

<details><summary><b>News</b> — score +0.20</summary>

- [Jensen Huang Says Nvidia's Next-Gen Vera Rubin Chips Will Generate $40 Billion in Revenue per Gigawatt, Up From $25 Billion for Grace Blackwell. What That Means for NVDA's Growth Runway.](https://www.fool.com/investing/2026/11/25/jensen-huang-says-nvidias-next-gen-vera-rubin-chip/)  
  <sub>The Motley Fool, 3 hours ago</sub>  
  It's been an incredibly wild month for Nvidia (NVDA -5.86%) shareholders. The resignation of CEO Jensen Huang and related dynamics kicked off a surge in...
- [Nvidia’s Top Lawyer Sold $4.5 Million of Nvidia Stock the Day Before Its 14% Plunge](https://247wallst.com/investing/2026/11/25/nvidias-top-lawyer-sold-4-5-million-of-nvidia-stock-the-day-before-its-14-plunge/)  
  <sub>24/7 Wall St., 1 hour ago</sub>  
  The general counsel of NVIDIA (NASDAQ:NVDA | NVDA Price Prediction) sold 30,000 shares on Thursday, November 19, 2026. The next session, the stock fell...
- [Buy, Sell Or Hold Nvidia Stock After A 31.5% Day?](https://www.google.com/goto?url=CAESpgEBxCJF18HG8rQwHI9-KQPc7h8CeAWdQC-VkJ_TDGKSts_v-NKqIrEfkFoF__CZL06UgcCXEc4q8KPHhr71VByG1G5oHhO4y52ZUmikUp_lLObDnUOjaPDXqsAu3MIkYzamqDOg5qUsuF98dFhj5AuH3vVySdzf3imH0wXGJYw35JetAdnGQBFvKGwvB0wHSmNq_w0iI4C9EY1Y3d_hA1LUCdon5_SU&gsessionid=ASnz7Fj-NfuoOVpkWgLgPwb4Vud4nRr4jZR_ptKEwW0o8t5VJTwfOQ)  
  <sub>Trefis, 7 hours ago</sub>  
  Today's big story: Anthropic Below Its IPO Price: Do Giants Come Back? Nvidia stock rose 31.5% on Monday, Nov 23, to $165.05. It was its second-biggest...
- [Nvidia Still Faces Issues That Cost $2 Trillion in Market Value](https://www.google.com/goto?url=CAESrAEBxCJF1_DbeGbXFvjbwXWBemIABrX__k7PnzmJxuIpe7a4YRpTL9lW87mmqZ1BfZ_C7tAnQuaakn6EOwQyH3-yGqX7c6l3GiuD22QZxt3PK3GD-mpWVKRoyZNv9WHfDxFUCmPg4vi_TfEa1-0CWXoNDTtFqP-0vVTRr7Xn3QAdCHk_d6ZCpj_OGl7wZ9EzBiwZ2uNUuhEaZV9a3dUkk5GXb7eGnh1_xDKcLmTG&gsessionid=ASnz7Fj-NfuoOVpkWgLgPwb4Vud4nRr4jZR_ptKEwW0o8t5VJTwfOQ)  
  <sub>Bloomberg, 2 hours ago</sub>  
  The euphoria surrounding Nvidia Corp. shares following the return of Chief Executive Officer Jensen Huang on Monday is wearing off as investors come to...
- [Nvidia, AMD, and Micron stocks sink as investors flee AI trade](https://www.google.com/goto?url=CAESrAEBxCJF1ypm7FBkqGnmkrGBMgdbkUVBH4LFJHf3FT6NqdlRic6ncKiUeyGosCt-D4cCoyPeQeY2OxbHERqLZbjV2ii_W6maQAO-u11IYlPo-NyBHerHlJ-jGZ-o5kcZHsGhY1ba6BnGtLvutVpeQ87A0py5_ml3Wl1sNmVP5UdPEtM-ejsf4_BKfUy4JfA0evNnHX7Rt6PNGU6baUy7ARQTGIdHf-kFU9CZS-Pm&gsessionid=ASnz7Fj-NfuoOVpkWgLgPwb4Vud4nRr4jZR_ptKEwW0o8t5VJTwfOQ)  
  <sub>Yahoo Finance, 56 minutes ago</sub>  
  Nvidia (NVDA) stock retreated another 5% in premarket trading on Wednesday, following a 6% decline in the prior session as chip stocks continued to plunge.
- [Nvidia Stock Looks Like a Screaming Buy Below $160. Here's Why.](https://www.google.com/goto?url=CAESoQEBxCJF192q7vPQngiux5SOcnDGuUsoTyKBkbqaXrjXbn1u5blZoMFoj8cFkO7gNz_xGqvdJcO19buqbotLW9uG2wJY9XEoG-IEHuxt6TG0O0zA8hhQEToXnPXlnvcoN-QfIInlIoLsGHSWlMVzqGu-QioqSeIbv6jjJFbC8Q7bOpPfeOoAWB-_arF7lsVJgMmLR8Os4XwthvWJPkOQzqfj6Q&gsessionid=ASnz7Fj-NfuoOVpkWgLgPwb4Vud4nRr4jZR_ptKEwW0o8t5VJTwfOQ)  
  <sub>The Motley Fool, 2 hours ago</sub>  
  Well, that was quick. Less than two weeks after Nvidia (NVDA -5.86%) parted ways with Chief Executive Officer Jensen Huang, the board of directors brought...
- [Did Nvidia Stock Fall On Its Own?](https://www.google.com/goto?url=CAESmAEBxCJF193jpohs28P_5Bj5VokCunXZbMf2L13IXueTIb_O82Kud7e6fXoyXuCphdbbQD_XyHdGvvO11o8ytJ9uNyjVqY-2dCWCAUL6zfq6J12klyzWFj1rPmBRNHNZ0HqMmRXYdeqCWnOpU0ApuMlzW3OvYv0gG6j_cZkET1Ega4ouzZ7aSp31liBJecoluuu19o6pwVCPow&gsessionid=ASnz7Fj-NfuoOVpkWgLgPwb4Vud4nRr4jZR_ptKEwW0o8t5VJTwfOQ)  
  <sub>Trefis, 2 hours ago</sub>  
  Today's big story: Anthropic Below Its IPO Price: Do Giants Come Back? Nvidia stock fell 5.9% on November 24 and closed at $155.38.
- [Donald Trump Floats Jensen Huang Pardon, US Stake In Nvidia – But NVDA Loses Momentum](https://www.google.com/goto?url=CAESnAEBxCJF1_xYkOBLaY8vITfa5cjXv-f_pB7jzfN7lt164XispJr3IQF8tDEOxH1uQm71ZPCyab_tIW3frCNm0A70W6kQ-AFWRi6piOy293rK-7fPRJGsjQnz2DgxtsQtKd7u9TXF2KdVb2QKeCMZSjL2nPQ4lQwO1K8grSiBLCoJpjhIdNqrR0w9z_etqxKQ94pBwGIPAbeP8CmprwA&gsessionid=ASnz7Fj-NfuoOVpkWgLgPwb4Vud4nRr4jZR_ptKEwW0o8t5VJTwfOQ)  
  <sub>Yahoo Finance, 9 hours ago</sub>  
  Trump has been actively backing Huang and urged the Nvidia board to rehire him moments before it announced his return as CEO.
- [Prediction: A $10,000 Investment in Nvidia Stock Will Be Worth This Much by Year-End 2027](https://www.google.com/goto?url=CAESwQEBxCJF1_OR2uy488r8SUDTkcEo1XPaejZSZLae3bNkfe1udHtlAdvkV_0sFVInJNifwMlyoy1q72UZ-Y-iSoDO9KV8P84q-gr6PPVy6mVEGnqRK8rIw13KshYu3hdD9yIKZYejgzrvT90RZN3OhaOUy4j5F0K3dy-NGT2R4fU08KeNrOW2QdNdY4sRLSwzrBJ6LNyhPvBQBnO1pSEeZNlOEgWCl9PTbApZYRxGJtq4Fx-3liYToF89CweQfdMhAhB6&gsessionid=ASnz7Fj-NfuoOVpkWgLgPwb4Vud4nRr4jZR_ptKEwW0o8t5VJTwfOQ)  
  <sub>The Motley Fool, 18 hours ago</sub>  
  A lot has changed for Nvidia (NVDA -5.86%) in a very short period of time, and this will ultimately have a big impact on where the semiconductor stock...
- [Nvidia stock stumbles again after Jensen Huang's spectacular comeback rally](https://www.google.com/goto?url=CAESxgEBxCJF19y7aGGZ-jcO1O-ILFOJgF-WDoByBb-4ZkQ-eXO-WCH3G65wOOVrVQpD5WbxAjiBIA3ka824rwrnvVSPPEne0ypAMeGO7qSJG13W4H3Ws2SjQXk1up5Eg-Y9WbF2kMI5gUETNpmRdXgTmU6jxPXL82QkmexBEv495HEggk4bSEpUXL7YHSWnA92pNHaLSnOib-w6MAAvhbhvXGpLzhxtJEsCEW8b00_kA2oYUpjd4Xjv-5I_aZFmMS0itZXVTc3lUi8&gsessionid=ASnz7Fj-NfuoOVpkWgLgPwb4Vud4nRr4jZR_ptKEwW0o8t5VJTwfOQ)  
  <sub>Yahoo Finance, 5 hours ago</sub>  
  The imperial CEO meets Wall Street's wall of worry on AI. Shares of Nvidia (NVDA) fell more than 5% in premarket trading on Wednesday following a 5.86% drop...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.20</summary>

_Not available today._

</details>

<details><summary><b>Price and chart</b> — score -0.70</summary>

```text
Last close 142.01 (bar of 2026-11-25), from 502 daily bars
Trend: vs 20d SMA 172.11 (-17.5%), 50d 203.51 (-30.2%), 200d 202.84 (-30.0%); 50d above 200d
Momentum: RSI(14) 35.3 | MACD -17.500 vs signal -16.361 (histogram -1.139)
Returns: 1d -8.6% | 5d -5.9% | 1m -34.8% | 3m -37.7%
52-week range: 125.53 - 239.24 (now 14.5% of the way up)
Volatility: ATR(14) 13.35 (9.4% of price) | annualised 20d 140.1%
Volume: 0.16x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.90</summary>

```text
Sector: Technology / Semiconductors | market cap 3.43T
Valuation: trailing P/E 15.25 | forward P/E 8.55 | P/B 12.84 | PEG 0.15
Profitability: profit margin 62.5% | operating margin 66.1% | ROE 117.4%
Growth (YoY): revenue +103.2% | earnings +107.7%
Balance sheet: debt/equity 14.3% | free cash flow 99.24B
Risk: beta 2.25 | short interest 1.3% of float
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
Consensus: buy (mean 1.68 on a 1=strong buy to 5=strong sell scale, 58 analysts)
Ratings: 10 strong buy, 39 buy, 12 hold, 2 sell, 0 strong sell
Price target: mean 244.71 (+72.3% vs last close), range 130.00 - 425.00
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

<details><summary><b>Who is positioned how</b> — score +0.00</summary>

_Not available today._

</details>

<details><summary><b>Money going into and out of this fund</b> — score +0.00</summary>

_Not available today._

</details>

### ASML (ASML) · Company — BULLISH, confidence 0.58

**Result:** REJECTED · no room for equity ASML under its 5% cap or the sleeve budget limit: equity 99689.77, price 1238.53, existing exposure 0.00, headroom 41.12

**In the model's own words:**

> Fundamentals and earnings record are very strong, analyst consensus is bullish, and recent earnings beat with raised guidance provide a positive catalyst. However, news of potential US export curbs to China adds material downside risk and technicals show a bearish price trend and oversold momentum, tempering conviction to a moderate level.

**Main reasons it gave:**
- Q3 2026 earnings beat by 17% and raised 2026 guidance
- Dutch lawmakers push back on US export curbs targeting ASML
- Price below 20d, 50d, 200d SMAs; RSI 33.6 (oversold)
- Strong fundamentals: 55% YoY revenue growth, 135% YoY earnings growth, ROE 65.6%

<details><summary><b>News</b> — score -0.30</summary>

- [ASML Dips Premarket Amid Chip Rout: Dutch Lawmakers Push Back On Proposed US Curbs On Sales To China](https://finance.yahoo.com/markets/stocks/articles/asml-dips-premarket-amid-chip-092535583.html)  
  <sub>Yahoo Finance, 5 hours ago</sub>  
  The U.S. is close to passing a bill that would seek to have allies like the Netherlands and Japan adopt tougher export controls for China.
- [‘Disastrous' for ASML: Dutch Lawmakers Revolt Against US Push to Tighten China Chip Curbs](https://www.benzinga.com/markets/tech/26/11/63614377/dutch-china-chip-curbs-asml-us)  
  <sub>Benzinga, 8 hours ago</sub>  
  On Tuesday, Dutch lawmakers warn U.S. chip restrictions on China could hurt ASML and damage the Netherlands' economy.
- [ASML Is the Most Important Company You’ve Never Heard Of. Should You Buy the Stock?](https://www.google.com/goto?url=CAEStgEBxCJF1wdCPspT3BZN6kuPBFbWTLCuqqaGSXqtPB2G5LUXdfEBoDSESkGfwU5t6Jv_qI47CVBpYq_3QqeVAyt9CIwOgOI9oFterS1EtM3jNYvDfQA47DNgqYbvwBnNMQWTVQ4Xlhp74US1oGGQISK-uR4pqKfffdSEvXnoe5UUE9OTSUkeB7-jeauTzB3yBh6lI0GO0P1UpMm65-BD_bXFwPNiCCq2g_kN1tZh5_DJjstHEgNomw&gsessionid=6iPqzFxe0NobBON6KnYydvO8meMqlUEsGD4gVjqbaopFQ5prDaps3g)  
  <sub>The Motley Fool, 21 hours ago</sub>  
  Artificial intelligence (AI) stocks have been all over the map lately, with many falling as investors worry that companies are overspending on artificial...
- [ASML vs CAMT stock comparison - side by side](https://www.google.com/goto?url=CAESagHEIkXXl3cszG63QmfGgvomjmGedrYWTBtMQjgtd4hpRuwfjljXUC6xjQETllvN-ImiwWIssE_cEuy4ZVpEbvb5ToxIVGyjKZbBfAKO-bjrQ-OUKCuikKF7cpiiT_oEYgzll1GeQ-6DFQI&gsessionid=6iPqzFxe0NobBON6KnYydvO8meMqlUEsGD4gVjqbaopFQ5prDaps3g)  
  <sub>Quantisnow, 11 hours ago</sub>  
  Compare ASML and CAMT side by side: market cap, price performance, sector, SEC filings, analyst ratings and insider activity.
- [Key facts: ASML Beats Q3 Forecasts, Raises 2026 Guidance; Dutch Lawmakers Oppose MATCH Act](https://www.google.com/goto?url=CAES0QEBxCJF1-2O_iAQtDrv2KTZ4AHjgFdZhlcBAQ_PyoUHNjiiwy94Dgjw3CxXgS-eIUU_8o4GA45cR0Xkrea4QDoBTBlS0EhvN9bAkRW2qFyzCU7U7Qx5zZGPkyZvsWcRPncESNVOmibPLbh3QI3y4N31IR38expW3jvEyHM-z432CVPXGkpuTbytL9SQT0T-_PFY1Qc9cpIdwFblD7TjUt2OecadsH1rgNyCxz0Mz9jM347FWgES1o60e7ME-uz-8p3QPiBGd5IyPPv1MdJrPmDjPQ&gsessionid=6iPqzFxe0NobBON6KnYydvO8meMqlUEsGD4gVjqbaopFQ5prDaps3g)  
  <sub>TradingView, 7 hours ago</sub>  
  ASML posted Q3 2026 sales of €11.7 billion, net income of €5 billion and a 57.5% gross margin, topping forecasts. It expects Q4 sales of €14.2–15.2 billion...
- [Corgi ASML 2x Daily ETF ASMZ Stock Forecast & Price Target](https://www.google.com/goto?url=CAESjQEBxCJF1xSeMzKFlbN_zvjTEbQFwCv5CAiTOiV8XSaiblQHkggzqUrNQiYhpN5JijG2o09R8T0uuxbL5M6ztL_LWaGAyU25GWiyFWhNIDJJHrRpD7kw43dNbLIaf4MTRa4x5oka-nyem8Z82M5LFk9tAaxZDM1p-thttqFZVV__GVpiRB3-xvSqDZUKXQ0&gsessionid=6iPqzFxe0NobBON6KnYydvO8meMqlUEsGD4gVjqbaopFQ5prDaps3g)  
  <sub>Yahoo Finance, 7 hours ago</sub>  
  At Yahoo Finance, you get free stock quotes, up-to-date news, portfolio management resources, international market data, social interaction and mortgage...
- [ASML Apr 2027 1660.000 put (ASML270416P01660000) Interactive Stock Chart - Yahoo Finance](https://www.google.com/goto?url=CAESeAHEIkXXRRJCyv6d0To6sWfODs2ZWfZvvVwCmacV3JEaouJuY6jt7P4UFPgG1wYZNfawXrW36YVCP0KjpI2Apb-xVKmqFEgfYPjusHgoqkStHWvhB_g8jJtujTmh2eHLEY3hVbNcz3KHQCw7jn2505FY9Mu-BIHD6g&gsessionid=6iPqzFxe0NobBON6KnYydvO8meMqlUEsGD4gVjqbaopFQ5prDaps3g)  
  <sub>Yahoo! Finance Canada, 10 hours ago</sub>  
  Interactive Chart for ASML Apr 2027 1660.000 put (ASML270416P01660000), analyze all the data with a huge range of indicators.
- [Dutch lawmakers urge government to resist US MATCH bill targeting ASML](https://www.google.com/goto?url=CAESogEBxCJF1xfPAgiGVbz-Ye0xZFDd9e5MkWSZpRRxDail8AUgDDsFU8dcbP_9Pydnm_t6C30ySZRWUZjstIpk_ZuCOQQ2tIt28opUHoiE6xROb6KljfZ47vC7hJ2BRMlLXoXcmhjP_hS1yOYA0Mk4rKmZk8lieudeXEuimW-zm0LV8stk_a7DCD83cLaZ4BIuQFa8WV9zIadRHf-ag0_wD7CevBs&gsessionid=6iPqzFxe0NobBON6KnYydvO8meMqlUEsGD4gVjqbaopFQ5prDaps3g)  
  <sub>Yahoo Finance, 17 hours ago</sub>  
  By Toby Sterling AMSTERDAM, Nov 24 (Reuters) - Dutch lawmakers urged the government on Tuesday to push back against proposed US legislation that could...
- [ASML Mar 2027 2180.000 put (ASML270319P02180000) interactive stock chart](https://www.google.com/goto?url=CAESeAHEIkXX613Sno8Cy0y4k4ghCC8Kv86ApUbJfSrh_0pqhWVonOZlpLFMdtwN7pti-bPA1RKWf6ONuIXYbXKA-xLVqZZUniUTh7fm_uCQ6Zh9sKKjn37Os41OfUjLPKgw5I5TmpfNUmiL8whpbMhmlQ8aYPv-VOGRsg&gsessionid=6iPqzFxe0NobBON6KnYydvO8meMqlUEsGD4gVjqbaopFQ5prDaps3g)  
  <sub>Yahoo Finance UK, 9 hours ago</sub>  
  Interactive chart for ASML Mar 2027 2180.000 put (ASML270319P02180000) – analyse all of the data with a huge range of indicators.
- [ASML261127P01810000 Interactive Stock Chart | ASML Nov 2026 1810.000 put Stock](https://www.google.com/goto?url=CAESbwHEIkXXYeEu_dHQoYXcakx8atG6vDdjPurGfJ5lmwrF4ng8b_q2GaOdPhj5qr4fAhLAnnYkjqiSjWA9ice97Nf2N8-5U2XLXpQbBtXzZka35yLDd2bX9uf55oIpaf-NAAAVpkrXB6zz4J3VflPRYg&gsessionid=6iPqzFxe0NobBON6KnYydvO8meMqlUEsGD4gVjqbaopFQ5prDaps3g)  
  <sub>Yahoo Finance, 9 hours ago</sub>  
  At Yahoo Finance, you get free stock quotes, up-to-date news, portfolio management resources, international market data, social interaction and mortgage...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score -0.30</summary>

_Not available today._

</details>

<details><summary><b>Price and chart</b> — score -0.60</summary>

```text
Last close 1,249.80 (bar of 2026-11-25), from 502 daily bars
Trend: vs 20d SMA 1,446.13 (-13.6%), 50d 1,608.76 (-22.3%), 200d 1,600.07 (-21.9%); 50d above 200d
Momentum: RSI(14) 33.6 | MACD -85.972 vs signal -73.968 (histogram -12.004)
Returns: 1d -6.5% | 5d -10.4% | 1m -23.6% | 3m -28.0%
52-week range: 1,003.22 - 1,989.44 (now 25.0% of the way up)
Volatility: ATR(14) 75.14 (6.0% of price) | annualised 20d 74.8%
Volume: 0.16x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.80</summary>

```text
Sector: Technology / Semiconductor Equipment & Materials | market cap 481.70B
Valuation: trailing P/E 30.75 | forward P/E 19.71 | P/B 1,073.14 | PEG 0.73
Profitability: profit margin 34.1% | operating margin 38.6% | ROE 65.6%
Growth (YoY): revenue +55.2% | earnings +135.9%
Balance sheet: debt/equity 8.9% | free cash flow 10.37B
Risk: beta 1.33 | short interest 0.4% of float
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
Price target: mean 2,102.78 (+68.2% vs last close), range 847.17 - 2,782.92
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

### Teva Pharmaceutical (TEVA) · Company — BULLISH, confidence 0.55

**Result:** ACCEPTED · 1 shares · submitted buy 1 TEVA @ ~39.15, stop 36.32

**In the model's own words:**

> Positive FDA approvals and new institutional buying provide a material catalyst, outweighing weak short‑term technicals and mixed fundamentals.

**Main reasons it gave:**
- FDA approval for generic Flovent HFA inhaler (jointly with Cipla)
- IGALMI FDA clearance for sublingual film
- Marshall Wace LLP purchased new stake in TEVA
- Price below 20‑day and 50‑day SMA with low volume (technical weakness)
- Forward P/E 12.32 suggests cheap valuation despite high debt/equity

<details><summary><b>News</b> — score +0.80</summary>

- [WMG,ANT,CPRI,TEVA,DB,SQM | Stock Prices | Quote Comparison](https://ca.finance.yahoo.com/quotes/WMG,ANT,CPRI,TEVA,DB,SQM/)  
  <sub>Yahoo! Finance Canada, 17 hours ago</sub>  
  View and compare WMG,ANT,CPRI,TEVA,DB,SQM on Yahoo Finance.
- [Teva Pharmaceutical Industries (TEVA) Wins IGALMI FDA Nod As Fair Value Questions Persist](https://simplywall.st/stocks/us/pharmaceuticals-biotech/nyse-teva/teva-pharmaceutical-industries/news/teva-pharmaceutical-industries-teva-wins-igalmi-fda-nod-as-f)  
  <sub>Simply Wall St, 7 hours ago</sub>  
  Teva Pharmaceutical Industries (NYSE:TEVA) just picked up a fresh regulatory milestone, with the U.S. FDA clearing IGALMI sublingual film for at-home...
- [Cipla Secures USFDA Approval for First Generic Flovent HFA Inhaler; Shares Rise 0.86%](https://www.google.com/goto?url=CAESogEBxCJF1557W76ayYfwjywI2E9_6KqROLNSxM6bnTHWF6XVw4PdxiVeAx2y5oBqwAQ8eHh1A0oMY3giEsgUokCMuHj90XSRTuAMIDDCBclF_b4AMWGYnqpl6d-UClXUwkFwbgVYs7hSarpjdzgfkJikxPmMjezbQ1G5cKq0ARqOHPEKJCY3njdVuYpwRpuplQM68f-XWQtAkPwTRA3VRQH6NX0&gsessionid=eSGge8rNbYKc3Et2KqJxmiuWo4NquPkX6RGuLpDUYhu_9H04_URkGw)  
  <sub>HDFC Sky, 10 hours ago</sub>  
  Cipla and Teva receive USFDA approval for the first generic Flovent HFA inhaler in 110 mcg and 220 mcg strengths for asthma treatment. Shares rise 0.86%.
- [Cipla Gets USFDA Approval for First Generic Version of Flovent HFA Asthma Drug in Two Strengths](https://www.google.com/goto?url=CAESoAEBxCJF11Y8axzlRE1lNoLQJMpevyoGRGEhj9bZtG9XeNevzmW1G2LxSMd-rgNnLLvLWXW-xGNqkRSKvBCb2gj595WQNI8wz4Lv8NN-ifSYWz-V0P2Nc4Oh8CvCJvz2_WlTPvdmi2wH5oHMtVar6OCQTmRSchRpphbW003d0VVoiNS6dKKKDuKo8SotUsHmDQOFkZxU1YHQcIog7zhNbnNI&gsessionid=eSGge8rNbYKc3Et2KqJxmiuWo4NquPkX6RGuLpDUYhu_9H04_URkGw)  
  <sub>Kotak Neo, 9 hours ago</sub>  
  Cipla received USFDA approval for generic Flovent HFA in two strengths. Teva will market the asthma inhaler in the US, a market valued at $350 million.
- [Zacks Industry Outlook Highlights Viatris, Teva Pharmaceuticals and Sandoz](https://www.google.com/goto?url=CAESrQEBxCJF13RJJOubMN40XInazdIdHU4ijzYDUEKUXuyPRqZcGx7KciG5gCp7skeuXlR9VnjT86blMA8U1jgxahhzKitgIEwMB4CH-ncPm9DvrCsGXj3-D_EFZ92vf1e6Kb94pimdY3AcX-zMLimRadc1mKEy_mB0Qz3ie30Hr4w72coRc28RmEzThz4Ft9nFHC_nIJlQlN801wPo_DzRTYl7pFKGVnC1PK3Z6P5GKA&gsessionid=eSGge8rNbYKc3Et2KqJxmiuWo4NquPkX6RGuLpDUYhu_9H04_URkGw)  
  <sub>Zacks Investment Research, 24 hours ago</sub>  
  Viatris, Teva Pharmaceuticals and Sandoz stand out as complex generics, biosimilars and new product launches shape the industry's growth prospects for 2027.
- [Cipla, Teva get FDA nod for first generic Flovent HFA; eye $350-million US asthma market](https://www.google.com/goto?url=CAESzgEBxCJF1zy9Dhux1xRQZojET0U3N-MulxUg9oHkrTfcjnjk_9ECLaElxeh8jHbYtc8ES37KtjW2WrVvqftAyYrfODzqvn2OmO3Xrc7fwiW6CDKLPfiA2_7PVfb5Ey-IOSybwcBmtTup9lGi-7fM0aLGLnwB37wAo_igc_RKdFsyRyqMiHDnHkzBgVOQtKa6rcnt8hjGivBf6EtjLrqaaoZMDM_K_yzP1ACzjYr-cozDYMG3aDuu078Wx3Az81GxoJEU6gOVBLEZzTnwmKvD8Q&gsessionid=eSGge8rNbYKc3Et2KqJxmiuWo4NquPkX6RGuLpDUYhu_9H04_URkGw)  
  <sub>Moneycontrol.com, 8 hours ago</sub>  
  The product has been jointly developed by Cipla and Teva Pharmaceuticals. Cipla will manufacture and supply the drug, while Teva, which owns the ANDA,...
- [Cipla, Teva get USFDA nod for first generic Flovent HFA asthma inhaler](https://www.google.com/goto?url=CAES7AEBxCJF19fDfPk2NtbOw1V_2PakxzCv2kjBySEKgvNlvIP53LvgrDjA9_vi-VGir2DrHOIEQC40hQT4lKG-oCm9dyQjJAODRkOQQR1h7G0RfmWly5sA8bCJNwhilcUA6pj36sZ89gK0vZWW1GaND6uRtHsFaROi215kA1MGbDtFkd1l1zC_tqHC3fdyVTpDmY1g9bM1wy5-pTGaZ5ZwKdsdreLrJMf7DYf2EXgTsBKNxeDaDeId_kCG_G8L2SDmIjlWI9aDB66wNqz1WYk063XJakcCPBsJ8avLnESJMD3FaB4fG_FPUbMuhAg-BA&gsessionid=eSGge8rNbYKc3Et2KqJxmiuWo4NquPkX6RGuLpDUYhu_9H04_URkGw)  
  <sub>The Economic Times, 6 hours ago</sub>  
  Cipla announced the approval of Fluticasone HFA metered dose inhaler for asthma treatment by the US health regulator. This marks the first generic...
- [Marshall Wace LLP Buys New Stake in Teva Pharmaceutical Industries Ltd. $TEVA](https://www.google.com/goto?url=CAESxAEBxCJF13QxE9XNTs7_L5g3bt5pTkxBr_pVWOIiTZD2YXYRB6-mUfEmXvr9bI-ScUSm8-3m9-04RwaWCXWriDen6vDczsGsk3U4pI9Y0m64GZIO-yp8rPgGgN1FfMxkN9VCVHLtG6tEmBZEkrvhCLrTYCdHf6X-N9rvzwuo6-DFBMH8jBNgKbKmzFZ4H6NF2CbaJqCHFM1Yj3JXqtpUHQrumpXXLGRdjA3vaXktN0FeFLEMRy_EBX2WyrBL-Ohh3mrNJbjQ&gsessionid=eSGge8rNbYKc3Et2KqJxmiuWo4NquPkX6RGuLpDUYhu_9H04_URkGw)  
  <sub>MarketBeat, 3 hours ago</sub>  
  Marshall Wace LLP purchased a new stake in Teva Pharmaceutical Industries Ltd. (NYSE:TEVA - Free Report) during the 3rd quarter, according to its most...
- [Cipla, Teva Get USFDA Nod for Generic Flovent HFA Inhaler](https://www.google.com/goto?url=CAESqwEBxCJF11nGGfffYRzuvN9tf4zKNUeGa1NaCYxh3oi1MwCU2NMztN38_C0M6WlP4oNuDygnwA5OyREe-gfwvLThbRxScp_D2HzPUR1FOkuGTkxI9ntHUb4oUkm8wEpW9mc9S6a4Rm5r0GuOdn5586j4yhObSjnATDHEkQf4W5Zc2zLff_AqXRicOuGKCV62e7ZmPe-KKC1NWuQ7erGWrduaGOCwqizgAwhX1-k&gsessionid=eSGge8rNbYKc3Et2KqJxmiuWo4NquPkX6RGuLpDUYhu_9H04_URkGw)  
  <sub>Rediff MoneyWiz, 8 hours ago</sub>  
  Cipla and Teva receive USFDA approval for Fluticasone HFA MDI, the first generic equivalent to Flovent HFA, for asthma treatment in the US market.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.80</summary>

_Not available today._

</details>

<details><summary><b>Price and chart</b> — score -0.50</summary>

```text
Last close 38.58 (bar of 2026-11-25), from 502 daily bars
Trend: vs 20d SMA 41.65 (-7.4%), 50d 40.66 (-5.1%), 200d 35.33 (+9.2%); 50d above 200d
Momentum: RSI(14) 39.1 | MACD -0.264 vs signal 0.257 (histogram -0.521)
Returns: 1d -3.8% | 5d -8.6% | 1m -4.5% | 3m +2.6%
52-week range: 24.99 - 44.50 (now 69.7% of the way up)
Volatility: ATR(14) 1.41 (3.6% of price) | annualised 20d 47.2%
Volume: 0.06x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score -0.30</summary>

```text
Sector: Healthcare / Drug Manufacturers - Specialty & Generic | market cap 45.02B
Valuation: trailing P/E 89.72 | forward P/E 12.32 | P/B 5.64 | PEG 0.71
Profitability: profit margin 2.9% | operating margin 19.8% | ROE 6.7%
Growth (YoY): revenue -1.9% | earnings -46.0%
Balance sheet: debt/equity 212.9% | free cash flow 1.49B
Risk: beta 0.84 | short interest 2.3% of float
Next earnings: 2027-01-27
```

</details>

<details><summary><b>What this fund holds</b> — score -0.30</summary>

_Not available today._

</details>

<details><summary><b>Does this company beat its own forecasts</b> — score -0.30</summary>

```text
Earnings record, last 4 quarters: 3 beats, 1 missed
  2026-09-30 beat by 15% | 2026-06-30 missed by 92% | 2026-03-31 beat by 9% | 2025-12-31 beat by 39%
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

<details><summary><b>What analysts and big funds say</b> — score +0.60</summary>

```text
Consensus: buy (mean 1.53 on a 1=strong buy to 5=strong sell scale, 14 analysts)
Ratings: 4 strong buy, 9 buy, 2 hold, 0 sell, 0 strong sell
Price target: mean 50.51 (+30.9% vs last close), range 42.12 - 57.00
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
Distinct insiders: 0 buying, 11 selling
Sales — weak evidence on their own; often scheduled 10b5-1 plans, tax on vesting, or diversification:
  - 2026-11-20 FOX CHRISTINE (Officer): 28,229 shares, 1.10M
  - 2026-11-12 SABAG MARK (Officer): 44,710 shares, 1.97M
  - 2026-11-11 DANIELL RICHARD (Officer): 45,003 shares, 1.93M
  - 2026-11-10 FRANCIS RICHARD D (Chief Executive Officer): 250,000 shares, 10.56M
(17 grant/option/gift transaction(s) excluded — compensation, not a view on the price)
```

</details>

<details><summary><b>Who is positioned how</b> — score +0.00</summary>

_Not available today._

</details>

<details><summary><b>Money going into and out of this fund</b> — score +0.00</summary>

_Not available today._

</details>

### Alphabet (Google) (GOOGL) · Company — BEARISH, confidence 0.45

**Result:** REJECTED · no room for equity GOOGL under its 5% cap or the sleeve budget limit: equity 99689.77, price 264.09, existing exposure 0.00, headroom 41.12

**In the model's own words:**

> Technical indicators show a strong downtrend (price far below moving averages, low RSI, very low volume). Earnings record is poor (3 of last 4 quarters missed consensus). News is mixed but leans slightly bearish. Analyst consensus is bullish but may be over‑optimistic given fundamentals and earnings history. Fundamentals are modestly attractive (low P/E, high ROE) but earnings growth is negative and free cash flow is weak, tempering the bullish view.

**Main reasons it gave:**
- Technical: price 21% below 200‑day SMA, RSI 33, volume 0.13× 20‑day avg
- Earnings record: 3 of last 4 quarters missed consensus
- Analyst consensus: strong‑buy with mean target +50% vs price
- News: Google Services operating income up 17% and margin expansion
- Fundamentals: low trailing P/E 13.75, high ROE 44% indicating cheap valuation

<details><summary><b>News</b> — score -0.20</summary>

- [GOOG Stock Quote Price and Forecast](https://www.cnn.com/markets/stocks/GOOG)  
  <sub>CNN, 6 hours ago</sub>  
  Alphabet Inc. Class C ... GOOG is trading near the bottom of its 52-week range and below its 200-day simple moving average. Price change. The price of GOOG shares...
- [Is Google Services Still the Prime Earnings Engine for Alphabet Stock?](https://www.zacks.com/stock/news/3035047/is-google-services-still-the-prime-earnings-engine-for-alphabet-stock)  
  <sub>Zacks Investment Research, 31 minutes ago</sub>  
  Google Services' operating income rose 17% to $39.2 billion, with its operating margin expanding to 40.7%. AI-powered features fueled Search query growth,...
- [Alphabet (GOOGL) Stock Quotes, Company News And Chart Analysis](https://www.google.com/goto?url=CAESqgEBxCJF1zRQY47e1SUyjjQwGDqs70n0iDDXLcZdudjY_xSUpWY8qVCZfo-NYsQtisJ3a8i4jHsJVF80L2dqgB5sGr1WTjSVWV24Y4cuqZoCRKwUhLjO75EIxrGBwm4NHDJpGU_6iVOxOtwcfSur60x6X23dYD-KjDJhO8x2OI_oDYQnWn2yTGC4-XZJTL6HNSrH3iEcevc1LDanTbz_7yNXtxGiXrCQ7FC1zg&gsessionid=sycZ0M_u_hOs-59r_0bHh_OkKF9AYqCNGh_DqOY5jgweaVZ82W3MqQ)  
  <sub>Investor's Business Daily, 21 hours ago</sub>  
  Alphabet (GOOGL) Stock Quotes, Company News And Chart Analysis · IBD STAFF · Updated 12:27 PM ET 11/24/2026. (GOOGL). Chart Error...
- [Google Stock (GOOGL) Falls 1.1% as Tech Stocks Retreat (Nov 24)](https://www.google.com/goto?url=CAEShwEBxCJF11sBGYVPC_GjQOLzq1IpX6BBKrTuxhRNvjNOnHfTNMkztALkniW_BW87_uHtRdczrHE5Vm7O2cP3A-3mehFKVRZAqj4Hs2WPwZdpRCzEFpUH69Enqbq66Q8fURtyhlAmRZnNFL-XpOJIfeQDGtm5uqc-BQC4bUYePVIoNf2_UHi6cuQ&gsessionid=sycZ0M_u_hOs-59r_0bHh_OkKF9AYqCNGh_DqOY5jgweaVZ82W3MqQ)  
  <sub>Gotrade, 11 hours ago</sub>  
  Alphabet (GOOGL) fell 1.08% to $279.05 on Nov 24 as chip and AI stocks retreated, a smaller drop than the Nasdaq's 1.48% slide.
- [Not SpaceX, Not Anthropic: These Are the 2 AI Stocks I Bought During the Sell-Off](https://www.google.com/goto?url=CAES4wEBxCJF1x5UZfvcZTNkBZj8bLpeN9qRglDVNw5kuHzCA9I0XW_wof1oh2MHPMjcf3kJrvnc7nLa1FSJhSLjRaUTfZ-aCOxhdxSPXOiap2s2PZMu-YX0TnyW8QOfpvnu5rWcw4gRT4tbgZobnKI5Khwj5cd2-O0DmnSZ1G_Ak4SRIsNKncacrJ-86PFqULNJ3yWxQIkz44Y60qohFcC-BD1p3cKfq-dkI7LdRjm-a_sUC4j0cXjwdHpLtVLgeAgDxn-UOR_7ZqIsf2Uwpae_Aimp6--tcSGFmPV35ohqMe88nZ4Szw&gsessionid=sycZ0M_u_hOs-59r_0bHh_OkKF9AYqCNGh_DqOY5jgweaVZ82W3MqQ)  
  <sub>The Globe and Mail, 1 hour ago</sub>  
  Detailed price information for Alphabet Cl A (GOOGL-Q) from The Globe and Mail including charting and trades.
- [Alphabet (GOOGL) Expands AI Search With Wallet Data](https://www.google.com/goto?url=CAESmwEBxCJF1_KujK_wNAiwqQvGel3Bg5X9VCdm-4twNKwMbIXNSaPvzycRjAr-qOoYxIYUkNeY56_uD_-47zURQmtSfvsIAHIF9cRH_yIAWLfhd5GDoSZ5-Amnl-Du2uE1Bzlb9QN-rNpVjCVDXmn2E6ITSKX83nc_z8tR83a4sNQPAqtVGne4yjwjLYqWkQPziQrqWvKtCMoOIDyp_w&gsessionid=sycZ0M_u_hOs-59r_0bHh_OkKF9AYqCNGh_DqOY5jgweaVZ82W3MqQ)  
  <sub>Yahoo Finance, 23 hours ago</sub>  
  Alphabet (NasdaqGS: GOOGL) has expanded Google Search's AI Mode to draw on Wallet spending data for more tailored results. The refreshed Search experience...
- [Google GOOGLThe stock price once broke below the March low…](https://www.google.com/goto?url=CAESZAHEIkXXDOU1MKd9ob-EO2LRCRxwwVOWNNnhUIarwH47vx_sVCzerDp4bLNOA5lmqGm-CLEFR806yWCPf_q48aFJuErwr9tUCUx__bdQb6XtfSe2P4CdCeuAAm-SFSUcRSAnqz4&gsessionid=sycZ0M_u_hOs-59r_0bHh_OkKF9AYqCNGh_DqOY5jgweaVZ82W3MqQ)  
  <sub>Longbridge, 11 hours ago</sub>  
  Google GOOGL. The stock price once broke below the March low of 273. Yesterday, it rose in sync with the broader market, reclaiming levels above 273.
- [Broadcom's Google TPU Scare Puts a New Spotlight on Its Other AI Customers](https://www.google.com/goto?url=CAESqQEBxCJF1_V2eXg1muKNV8ueKyB9Dsp8z3lBi1LNDOHqooPC88Cshsbpr4CrwPs7MCGpw_Cfb_Ray92Ne5vYM9XzwP_1sDy-f4e0cnzgQ836xRIUiYp4DExLEs1_4k02t5zSZy3LZw7mOGciul3igw6XgYAdBC2CHr4du_7vviDUc3lLhnBs9C2LTaUasOR3m9uDzqH-_z94eoD_qFa-r6cCjEiiuBQe_ho5&gsessionid=sycZ0M_u_hOs-59r_0bHh_OkKF9AYqCNGh_DqOY5jgweaVZ82W3MqQ)  
  <sub>MarketBeat, 1 hour ago</sub>  
  An analyst report suggesting Alphabet cut 2027 Broadcom TPU 8i shipments by 20% weighed on Broadcom stock, raising the importance of Anthropic,...
- [Warren Buffett's Successor, Greg Abel, Has Quietly Purchased 3 Stocks Since the Start of the Fourth Quarter, Including Shares of a Legal Monopoly](https://www.google.com/goto?url=CAESogIBxCJF1yXkTx_YPco3IOFCDYBm0I6WVCQUW2ZmM_IuYhvO6zzr-EmAwN9qq68O3yr3uWMJ1J4aXGVk4FGB7l5fJTz8pdLCwv1KAYfbFCyZGIm496YTwbGE2_5vT-Qgl0YANZE4pB3fU-Z7iddMYLlWcQEGFfg69Rz7D7M8S7uvwUowSaoUZTnLQ3pngl_V59bsl5aOZVm1xQRec9Uy5cza3Bz9d5otgusMMqhy11tlRueZq2nqmxX48D_KL87uc9d_aptEEhsU0RYQjZudSBwVVLjmlKafNmoGnYBvG_2-Bm-UBInUepjTkA9nHih2Rs8x722mTKygbgggTMWGFy9ADOlaXPoGVy73ZE4yk_c2by5-RWSOs89r-H0j8rwWvBKvSg&gsessionid=sycZ0M_u_hOs-59r_0bHh_OkKF9AYqCNGh_DqOY5jgweaVZ82W3MqQ)  
  <sub>The Globe and Mail, 4 hours ago</sub>  
  Detailed price information for Alphabet Cl A (GOOGL-Q) from The Globe and Mail including charting and trades.
- [GOOG Stock Tests Support Again as Analysts Reduce Exposure and Google Spending Fears Mount](https://www.google.com/goto?url=CAESwQEBxCJF10iE2q7A6bys3nRJLhxGQ6EcBB8BpLbi7sFTDep2PZCLvEafdoPbsgYdWq3thC2V-U78tDOndksFItklvl91oqggYNLtW3VfyZdXSdwq4IGqaQHDKa2ToY_uT8w6k7iuFZjnRdqI8gfsLH-KG1gYpWkfFw2SgSqVpf8G5V-jlCmtFGUkTQ3S8qhH5cMBCTy9FN1caPnbbO4xgHLLlnDfjIEG8aFUDJKIQiO8WZOAwxqt1nCj3X37F1e03Tuc&gsessionid=sycZ0M_u_hOs-59r_0bHh_OkKF9AYqCNGh_DqOY5jgweaVZ82W3MqQ)  
  <sub>FXLeaders, 16 hours ago</sub>  
  Alphabet stock GOOG fell despite rapid Google Cloud growth and Gemini expansion, as investors question whether escalating infrastructure costs,...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score -0.20</summary>

_Not available today._

</details>

<details><summary><b>Price and chart</b> — score -0.80</summary>

```text
Last close 263.35 (bar of 2026-11-25), from 502 daily bars
Trend: vs 20d SMA 282.56 (-6.8%), 50d 318.05 (-17.2%), 200d 336.27 (-21.7%); 50d below 200d
Momentum: RSI(14) 33.2 | MACD -12.848 vs signal -12.836 (histogram -0.012)
Returns: 1d -5.6% | 5d -6.8% | 1m -17.9% | 3m -22.7%
52-week range: 263.35 - 402.62 (now 0.0% of the way up)
Volatility: ATR(14) 11.84 (4.5% of price) | annualised 20d 60.9%
Volume: 0.13x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.20</summary>

```text
Sector: Communication Services / Internet Content & Information | market cap 3.24T
Valuation: trailing P/E 13.75 | forward P/E 17.22 | P/B 4.91 | PEG 0.94
Profitability: profit margin 50.0% | operating margin 33.3% | ROE 44.3%
Growth (YoY): revenue +24.7% | earnings -25.3%
Balance sheet: debt/equity 22.2% | free cash flow -1.16B
Risk: beta 1.23 | short interest 1.3% of float
Next earnings: 2027-02-03
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

<details><summary><b>What analysts and big funds say</b> — score +0.60</summary>

```text
Consensus: strong_buy (mean 1.37 on a 1=strong buy to 5=strong sell scale, 54 analysts)
Ratings: 10 strong buy, 43 buy, 6 hold, 0 sell, 0 strong sell
Price target: mean 395.48 (+50.2% vs last close), range 300.00 - 500.00
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

<details><summary><b>Buying and selling by company insiders</b> — score +0.00</summary>

```text
Last 180 days: bought 0 shares in 0 transaction(s) | sold n/a shares in 0
Net: +0 shares | insiders hold 202,850,992 shares
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

### Caterpillar (CAT) · Company — NEUTRAL, confidence 0.35

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Mixed signals: technicals are strongly bearish while fundamentals, earnings record and analyst view are bullish; no material news catalyst. Net insider activity is neutral, leading to a low‑conviction neutral stance.

**Main reasons it gave:**
- Price 36% below 200‑day SMA and volume at 0.08× 20‑day average (technical bearish)
- Profit margin 15.2% and PEG 0.96 indicate strong fundamentals
- No material news catalyst; recent headlines focus on macro headwinds and product feature rollout
- Analyst consensus buy with mean price target $807 (+57% vs current $540) suggests upside not yet priced

<details><summary><b>News</b> — score -0.10</summary>

- [The AI Stock Slump Is Crushing Caterpillar. Here’s Why I Like the Stock More Than Ever.](https://finance.yahoo.com/markets/stocks/articles/ai-stock-slump-crushing-caterpillar-121002618.html)  
  <sub>Yahoo Finance, 3 hours ago</sub>  
  Shares of heavy equipment manufacturer Caterpillar (NYSE:CAT) hit a fresh 52-week low last week. CAT shares are now down more than 9% this year,...
- [Caterpillar (CAT) Makes Collision Warning Standard On Most New Construction Machines](https://www.google.com/goto?url=CAESpAEBxCJF1xWz8YVXE_qH9Q1mEpZCsi6S9uFa7HLo61GxUGhUNC_mecgFhxc7RAaSLzaiAZdKfD9R5lokgfjcWnOVcCRYtogUZYk5QB1Xzz6XX6_GRFEpx4DRB5_07bFk2stjXJEz56XM1fplhqNvTUXmd8nRslk7Ua_mvY1KAl0-BGfoeJGaeas1VIaes0z6R3RCoTEoqEPCJ3NkLMBrAruMzB15XA&gsessionid=Ya79sYP2-kiJzIizBjqmcnFy-q33MQVqU8JV-w68M6C1EOWSK-AruQ)  
  <sub>Yahoo Finance, 1 hour ago</sub>  
  Caterpillar (NYSE:CAT) is making advanced collision warning and mitigation systems standard on most new Cat construction machines. The safety package covers...
- [Red Cat Sinks 9%, Unusual Machines Slides 7%, Ondas Drops 4%: Is the Pentagon's Reported Push to Bring In General Motors and Ford a Threat to Drone Stocks?](https://www.google.com/goto?url=CAES_AEBxCJF13fAJuVdXoCnI3hgGnfqCi3fZ8iX_zzjUZupYXhMaGE1hjUj2G7Lh7eierWQJm33OkNn05pgq9Emen9Qm69dOrOOAKm8J7DOIQiPXQaLijYvYx4sTJsfLhGwgPWHM4W9KVjhpquxVHab3wCsthhkBHQceBHVKpIJDRZKPdwbQT9oBarX0HLBwNXL0kOl3g3uflBwrSdCIiD5LiWdZu91-WYVpzfl6i8Ut6tHJDGuNgc2DBOXNbo1tc0JKR3CkDy_mC_jrAL6VNAsDuSvTeSiXgZejnV_i2lMu-TiK0b6vsR_YjCSkAgDow7C665j6BGaYP1OD9XE8WE&gsessionid=Ya79sYP2-kiJzIizBjqmcnFy-q33MQVqU8JV-w68M6C1EOWSK-AruQ)  
  <sub>24/7 Wall St., 23 hours ago</sub>  
  Red Cat sank 9% and Unusual Machines slid 7% as a Pentagon push to enlist automakers raises competition fears for small drone suppliers.
- [Caterpillar Inc Stock (CAT) Moved Down by 3.17% on Nov 24: Key Drivers Unveiled](https://www.google.com/goto?url=CAESjgEBxCJF1yMNCWU9IQhxtpu0iWNFbv9Se_fbS51El5NVB4MOlqSL07-GF_dD5d-07hyi_MWRp6aMFNo_l_qXHwzoN5FT0je1XafBXjT9ZQmfUV2FMmwMCc7jjVsg-QP2HMBd7Dev1DU7buypCGf84-aFZ6TyOWb-zqEFwmJJDKJ06wQbVxda0pAZvl8DBBYK&gsessionid=Ya79sYP2-kiJzIizBjqmcnFy-q33MQVqU8JV-w68M6C1EOWSK-AruQ)  
  <sub>TradingKey, 22 hours ago</sub>  
  Caterpillar faced selling pressure amid macroeconomic headwinds and moderating order backlogs.Technical indicators like the MACD and Williams %R suggest...
- [Updating a Dead-Cat Bounce Trade in Nvidia Stock After a Single-Day 31.5% Pop](https://www.google.com/goto?url=CAESmwEBxCJF1wumXfKISqfRLLaCVtegJvVj8Lhd9cdyqiT6SFvp0-28jkf7H7UxpvCvnmmt-5oFq2nThEbU5y5esgfWXjhM3vTXTtGYvLoCZSEt5BLZ46dxvRE_nvkKfPET5wvldVog2vJEeixgfiW1Yenc0niWchut6yP28oJDVMdegoCtnaO43E0vuo1gtDjnlthdKApdCqeB4YLw8A&gsessionid=Ya79sYP2-kiJzIizBjqmcnFy-q33MQVqU8JV-w68M6C1EOWSK-AruQ)  
  <sub>Yahoo Finance, 20 hours ago</sub>  
  Nvidia (NVDA) is a tactical dollar-cost-averaging trade, not a stock recommendation. I made seven purchases at an average cost of $156.65.
- [Caterpillar Inc. stock outperforms competitors despite losses on the day](https://www.google.com/goto?url=CAES0gEBxCJF10wun5r8tZxKsDnUOZBKoucRFIvJdAl7xVUVNkESYiWfpJjp3aykUr_9u1rbRc33za0e6c7htkLnA1E_51vComqUWWhwsC8EBuZRN0LLFm7eqPa7dsnjp2FmBD__hXxqJSv_PNEQgduaVTrsRPIqV8VUy3FtQ2NWb9tTvYbAfCqTWzyE7fIk_5cS2d86JWd9LEmX-YjaftBmktJkDkvLLo3LGQm6CZ3fQTn04QbBg-ttm0XN7-SklCpW7BluvVUp001psvRwRNkKMBr5krM&gsessionid=Ya79sYP2-kiJzIizBjqmcnFy-q33MQVqU8JV-w68M6C1EOWSK-AruQ)  
  <sub>MarketWatch, 17 hours ago</sub>  
  Shares of Caterpillar Inc. CAT. -5.01%. slipped 1.17% to $540.63 Tuesday, on what proved to be an all-around mixed trading session for the stock market,...
- [After A 33% Plunge, Caterpillar (NYSE: CAT) And GE Vernova (NYSE: GEV) Rally At Different Speeds With Contrasting Risk Profiles](https://www.google.com/goto?url=CAES5QEBxCJF11ta6_dj-yBHfY-3rMWuu0eb2OaYMjC5tWvRiAgx7uurY7-CR0AmyP0KXS981EE2JHwceNn9j3o0Mzt0nRYZZYJ__5kq66QBt0CP5yuzNpBJgDpC60cQn91uwh5RPQcNH26P9Lupv8kZn1WMV9qyKhkfNdBBKDZZdEXDjZ1YLZ0kIayWiozMEt5xczvIPVHsu__ILRLR58rXpWYM1G7xQ-4wIr2H35dPzA6-tQmjTqEpgNmoZDOlL7IPg4lwYC4cQRjVPbyEQmZDFK8AvfBfiFBfUSv6J4mA-GBjAEKTqM8w&gsessionid=Ya79sYP2-kiJzIizBjqmcnFy-q33MQVqU8JV-w68M6C1EOWSK-AruQ)  
  <sub>Foreign Policy Journal, 19 hours ago</sub>  
  Caterpillar Inc (NYSE: CAT) has shed roughly a third of its value over the past three months, a drawdown that frames a very different recovery story than...
- [Unusual Machines Is Down 47% in a Month. Can UMAC Stock Hit Oppenheimer's $30 Target by 2030?](https://www.google.com/goto?url=CAESwQEBxCJF16qvLsX3tSnlH_6xeZ0a5d6-OD0TivB0kTdYQO2DVRAyIKGvabkyO7-cP9TJK6iKWMFPFQLemybrBJJNX61G3lGtsXTGRc-V7ZlwlyN1bsqPjqlyhYN5WtDTb5g9C2OejNWvm9Zwbb8DzyF8iEflxOPzePAFQwrsZnF4yp_2k64mZL4XqzzNb1ucgQT6X1FZZS3YVMpkmeqvuxx_cG_zRrfNLzdxpgDaTdY1hGmVuT1FBu9CEnJDim03qd12&gsessionid=Ya79sYP2-kiJzIizBjqmcnFy-q33MQVqU8JV-w68M6C1EOWSK-AruQ)  
  <sub>24/7 Wall St., 19 hours ago</sub>  
  Unusual Machines (UMAC) plunged 47% in a month despite Oppenheimer's $30 target, as a drone-sector selloff and resale share registrations weigh on the stock...
- [Black Cat expands Kal East gold footprint in strategic deal](https://www.google.com/goto?url=CAESnAEBxCJF145F5066JX7zxw2uyQjZas7ZnwAKi06W3lyRMcL8vpZf6WiWUtPyy05DXwiKKpsDSt01Hgx4BomLzmdyZ91tihvPAVPN3kWClT3xL-aWtmrPiBI0sMso0Vlv4XJrNwpDU5vXK2cuIypgLvpwwflLx7oiAExJuz3fSuwEu58WTFH0ItGegbrNhgAl6gl1dNOaE0PaUMUp2tA&gsessionid=Ya79sYP2-kiJzIizBjqmcnFy-q33MQVqU8JV-w68M6C1EOWSK-AruQ)  
  <sub>Australian Mining, 15 hours ago</sub>  
  Black Cat Syndicate has entered into a binding agreement to acquire 83km² of additional ground surrounding its Kal East gold operation in WA.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score -0.10</summary>

_Not available today._

</details>

<details><summary><b>Price and chart</b> — score -0.60</summary>

```text
Last close 512.84 (bar of 2026-11-25), from 502 daily bars
Trend: vs 20d SMA 577.51 (-11.2%), 50d 699.22 (-26.7%), 200d 801.01 (-36.0%); 50d below 200d
Momentum: RSI(14) 30.1 | MACD -48.338 vs signal -48.338 (histogram -0.000)
Returns: 1d -5.1% | 5d -8.2% | 1m -28.1% | 3m -37.2%
52-week range: 510.45 - 1,064.90 (now 0.4% of the way up)
Volatility: ATR(14) 29.43 (5.7% of price) | annualised 20d 67.2%
Volume: 0.08x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.55</summary>

```text
Sector: Industrials / Farm & Heavy Construction Machinery | market cap 234.67B
Valuation: trailing P/E 20.13 | forward P/E 15.94 | P/B 10.92 | PEG 0.96
Profitability: profit margin 15.2% | operating margin 18.8% | ROE 56.1%
Growth (YoY): revenue +17.3% | earnings +46.1%
Balance sheet: debt/equity 210.4% | free cash flow 3.97B
Risk: beta 1.64 | short interest 2.5% of float
Next earnings: 2027-02-02
```

</details>

<details><summary><b>What this fund holds</b> — score +0.55</summary>

_Not available today._

</details>

<details><summary><b>Does this company beat its own forecasts</b> — score +0.55</summary>

```text
Earnings record, last 4 quarters: 3 beats, 1 in line
  2026-09-30 in line | 2026-06-30 beat by 31% | 2026-03-31 beat by 19% | 2025-12-31 beat by 9%
```

</details>

<details><summary><b>What holding this fund costs you</b> — score +0.55</summary>

_Not available today._

</details>

<details><summary><b>How much oil and gas is in storage</b> — score +0.55</summary>

_Not available today._

</details>

<details><summary><b>How the crop is growing</b> — score +0.55</summary>

_Not available today._

</details>

<details><summary><b>What analysts and big funds say</b> — score +0.50</summary>

```text
Consensus: buy (mean 1.97 on a 1=strong buy to 5=strong sell scale, 26 analysts)
Ratings: 2 strong buy, 15 buy, 11 hold, 1 sell, 0 strong sell
Price target: mean 807.26 (+57.4% vs last close), range 575.00 - 1,027.00
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

<details><summary><b>What analysts say about what this fund holds</b> — score +0.50</summary>

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

### Microsoft (MSFT) · Company — NEUTRAL, confidence 0.35

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Mixed signals: strong fundamentals and earnings record support a bullish view, but recent negative news (outage, AI capex concerns) and technical weakness (low RSI, price below short‑term averages, thin volume) pull the outlook toward neutral.

**Main reasons it gave:**
- Recent 'Code Red' outage and AI capex concerns (negative news)
- Technical weakness: RSI 35.4, price below 20‑day and 50‑day SMA, volume 0.11× 20‑day average
- Strong fundamentals: profit margin 41.2%, ROE 34.2%, revenue growth 18.8% YoY
- Earnings record: 3 beats and 1 in‑line over last 4 quarters

<details><summary><b>News</b> — score -0.30</summary>

- [Microsoft Corporation (MSFT) stock price, news, quote and history](https://uk.finance.yahoo.com/quote/MSFT/)  
  <sub>Yahoo Finance UK, 4 hours ago</sub>  
  Microsoft Corporation (MSFT) · -2.00% · -5.41% · 18.53% · 2.59% · 4.67% · 46.82% · 560,232.96%. Key events. Baseline. Advanced chart. Loading chart for MSFT.
- [Microsoft Declares ‘Code Red’ After Recent Outage](https://www.theglobeandmail.com/investing/markets/stocks/MSFT/pressreleases/9002997/microsoft-declares-code-red-after-recent-outage/)  
  <sub>The Globe and Mail, 52 minutes ago</sub>  
  Detailed price information for Microsoft Corp (MSFT-Q) from The Globe and Mail including charting and trades.
- [Is Microsoft Stock Worth Owning as AI Capex Weighs on Free Cash Flow?](https://www.google.com/goto?url=CAESnAEBxCJF190xChbvOdMfTOiwe1aKGvLRj09R9zWhHQxXFrTNA_WVz3FT9LUS4LKmuDd-ONvMlijaLZXLFVgqzNEMVuDuo7MOQUrV_rC3EWt5unY5wgGXN7-zuW6JfYhY3zwUwj-8Dmg1BdpAnhHfj0b29azzBbDe3K_Vfja7O-GY_8N2CI4oebWGx3b4WXncca2iKVfzkMi6EbNPo0Y&gsessionid=TSkabpqmSZyRLEEILtGX5PWtUo4rDGRTX11yTX6EIirDglP2gDEAlA)  
  <sub>Yahoo Finance, 2 hours ago</sub>  
  Microsoft's MSFT accelerating AI infrastructure build-out is testing investor patience as capital spending weighs on free cash flow.
- [Microsoft Stock (MSFT) Rises 0.7% to $496.13 (Nov 24)](https://www.google.com/goto?url=CAESigEBxCJF1_v4Vp9Dx1SIxNa1K7zndM6I1229W_Hl0tG_nMePfQxth5jAQ9Pq6PW0X-dMBJU2SceggpOA4UEHMEBqD6nsOGiKNHgn8BTDjRu3LyXTMYwZJWG-iDSXOFHkeC0pX6u49d6ZnKGJ35BSgOWjaq_xCnLDT92S903Facr7fL4mOHv7UCYdhyg&gsessionid=TSkabpqmSZyRLEEILtGX5PWtUo4rDGRTX11yTX6EIirDglP2gDEAlA)  
  <sub>Gotrade, 11 hours ago</sub>  
  Microsoft (MSFT) rose 0.74% to $496.13 on Nov 24, 2026, as the Nasdaq Composite fell 1.48% on a chip sell-off. No company-specific catalyst was cited.
- [Microsoft (NASDAQ: MSFT) Stock Price Sits 11% Below Record Highs Despite Monday's Nvidia-Driven Tech Rally](https://www.google.com/goto?url=CAES0wEBxCJF1-dvWfnRlXtfvpUoBLe5YdUD96oD6pKNw1LCIGdtOIUW1wHoiud0olOkiq9kCwnS1WMI2Xi6z_aiQyXQ56r2HbliD1DIx-x9ALxcREfvUBsYasENaX4OLLonf10-kCCIfkSK0h7a5WzEuEifS9SBkX4Qa1SVcwauTIoH7ytYc9cICPkWvfDnX-6_4--i0A_JmCZWR3WN1zK3E4E1Q35QAI8ViHS5OucG0QglKAc7CatBPmOhL1LIYMLIImwVzk1eugaQR0sK77QbTMqUdbTe&gsessionid=TSkabpqmSZyRLEEILtGX5PWtUo4rDGRTX11yTX6EIirDglP2gDEAlA)  
  <sub>Foreign Policy Journal, 15 hours ago</sub>  
  Despite a broad surge in technology shares on Monday, Microsoft (NASDAQ: MSFT) remains a notable distance from its peak valuation, leaving investors to...
- [Is Microsoft the Best Big Tech Stock to Buy Now?](https://www.google.com/goto?url=CAESlgEBxCJF10Rix983xaxKpwMQVdTwXqaHzEEKN7U1kyJE_7eR0YJOpfH2BJev9XGnTt98vuty8Yk2OpN5andZOIT9rPnP-UdQCWHWz9MjabrtD3ubN2IY_fxwzE6-OIcgVwBt6V9TRh3niny5ytwPU0wsgWefrHFH1JuJIcgZso7FCvIwBkSyhlN-fACFUG4Y2TVfpXEo1xo&gsessionid=TSkabpqmSZyRLEEILtGX5PWtUo4rDGRTX11yTX6EIirDglP2gDEAlA)  
  <sub>The Motley Fool, 19 hours ago</sub>  
  Microsoft's positive cash flow is a big deal for the market.
- [Chip stocks slide again as AI trade struggles to regain footing (AMD:NASDAQ)](https://www.google.com/goto?url=CAESoQEBxCJF1wFzAX2bIRXxyBHQWJVihUsfcGKqOnEvnC7IeaHuaifmPuuSCrX2humEZHixRB0ElPZTUjnLQIV3Cp0Og1WQIpGE32ZZG4ZvEAWW41JDJdcGgx3cM5gxkZy0egon_BsKHL1qEFRG2IwKekriS9_B8rAGOYQOG_as3_co_D2tFM9pyOYyf-kA5Lp3Uten8qydCDsuZy6DpDDw0MFHbA&gsessionid=TSkabpqmSZyRLEEILtGX5PWtUo4rDGRTX11yTX6EIirDglP2gDEAlA)  
  <sub>Seeking Alpha, 3 hours ago</sub>  
  AI and chip stocks extend losses for a second session, with Nvidia down 5% in premarket and CoreWeave spreads at a record 1314 basis points.
- [Oracle Is a Higher-Leverage, Cash-Hungry Twin to Microsoft](https://www.google.com/goto?url=CAESoQEBxCJF15IyL4YWniqhun3GBY47bQH3aXO_-YKS3d6b0I08bnafr-kyDf0HTpSVHFBwEl2PyIPeRzglN47Ewa460vYwEv7nNy7oJ2WzbzImpgKhjQYMTYscq48zbM3onDpYs8B8BI2YwvIHmwkCB91w3wlC8kguF_1zghrQKRrTRf4w_dnDebhV_IDiNpz8h7HB0UmE8F1bV0vijA8qcqvq-g&gsessionid=TSkabpqmSZyRLEEILtGX5PWtUo4rDGRTX11yTX6EIirDglP2gDEAlA)  
  <sub>24/7 Wall St., 23 hours ago</sub>  
  Oracle (NYSE:ORCL | ORCL Price Prediction) and Microsoft (NASDAQ:MSFT) both opened fiscal 2027 with faster AI cloud growth and record backlogs.
- [Microsoft’s Code Red Exposes a Bigger Cloud Risk for Crypto](https://www.google.com/goto?url=CAESkgEBxCJF13li52IY_QjmzgA2TKV1Ut3YSiXNiaBny1-L-SYlKwSsLDOiatwo170fWlSFBFNqfH8bZJqBeLJhWy2V_ecm9Y3fFYdK9NXw1NflTHN6_JYM09Z6LhydjKj7jGb-NgC2880XpUWlEnj2axiJDArjieLFvxObgiOTPBQY4dpVmSSKaPqVyNDyM-pNC0J3nQ&gsessionid=TSkabpqmSZyRLEEILtGX5PWtUo4rDGRTX11yTX6EIirDglP2gDEAlA)  
  <sub>Coinpedia, 21 hours ago</sub>  
  Microsoft has launched a “Code Red” overhaul after its November 12–13 outage disrupted Exchange Online, Outlook, Teams, and Copilot worldwide for 24 hours.
- [Options Whale Alert: $735K Bullish Long Call Opened on $MSFT](https://www.google.com/goto?url=CAESoAEBxCJF1-pA4_WvS4AsDWzimeQt1HY73lR00BzNaA5BXdQfIBmz9LsfFfo0uKeMxYXb8dAcPIvj-OJOrJ6mCwoXS7ro-Q3I1qE_T78PHRfortivhL2my4jZJtunAncmrAOqaAcqnBW87vzwTvny39ZLNnSkTqRo4d8Gn59pJ7EjWS6bLFQE4ItRLqGSQ7-qaNHsW6_xiBB_Y02wV5_cxu33&gsessionid=TSkabpqmSZyRLEEILtGX5PWtUo4rDGRTX11yTX6EIirDglP2gDEAlA)  
  <sub>富途牛牛, 15 hours ago</sub>  
  Microsoft(MSFT.US)$closed up 0.74% at $496.13. A trader bought 1000 Dec 4, 2026 $510.00 calls to open a Long Call. The position carries a net debit of...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score -0.30</summary>

_Not available today._

</details>

<details><summary><b>Price and chart</b> — score -0.40</summary>

```text
Last close 479.33 (bar of 2026-11-25), from 502 daily bars
Trend: vs 20d SMA 516.61 (-7.2%), 50d 519.34 (-7.7%), 200d 444.83 (+7.8%); 50d above 200d
Momentum: RSI(14) 35.4 | MACD -9.446 vs signal -4.452 (histogram -4.994)
Returns: 1d -3.4% | 5d -5.7% | 1m -9.8% | 3m -5.1%
52-week range: 352.83 - 555.80 (now 62.3% of the way up)
Volatility: ATR(14) 16.79 (3.5% of price) | annualised 20d 40.3%
Volume: 0.11x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.50</summary>

```text
Sector: Technology / Software - Infrastructure | market cap 3.56T
Valuation: trailing P/E 25.01 | forward P/E 19.80 | P/B 7.56 | PEG 1.43
Profitability: profit margin 41.2% | operating margin 47.1% | ROE 34.2%
Growth (YoY): revenue +18.8% | earnings +32.3%
Balance sheet: debt/equity 28.5% | free cash flow 2.99B
Risk: beta 1.04 | short interest 0.9% of float
Next earnings: 2027-01-27
```

</details>

<details><summary><b>What this fund holds</b> — score +0.50</summary>

_Not available today._

</details>

<details><summary><b>Does this company beat its own forecasts</b> — score +0.50</summary>

```text
Earnings record, last 4 quarters: 3 beats, 1 in line
  2026-09-30 in line | 2026-06-30 beat by 10% | 2026-03-31 beat by 3% | 2025-12-31 beat by 3%
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

<details><summary><b>What analysts and big funds say</b> — score +0.10</summary>

```text
Consensus: strong_buy (mean 1.34 on a 1=strong buy to 5=strong sell scale, 54 analysts)
Ratings: 14 strong buy, 41 buy, 3 hold, 0 sell, 0 strong sell
Price target: mean 637.36 (+33.0% vs last close), range 440.00 - 870.00
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

<details><summary><b>What analysts say about what this fund holds</b> — score +0.10</summary>

_Not available today._

</details>

<details><summary><b>Buying and selling by company insiders</b> — score +0.00</summary>

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

<details><summary><b>Who is positioned how</b> — score +0.00</summary>

_Not available today._

</details>

<details><summary><b>Money going into and out of this fund</b> — score +0.00</summary>

_Not available today._

</details>

### Elbit Systems (ESLT) · Company — no answer, no confidence given

<details><summary><b>News</b> — score n/a</summary>

- [Elbit Systems stock: German subsidiary wins five-year naval deal](https://www.ad-hoc-news.de/boerse/news/corporate-news/elbit-systems-stock-german-subsidiary-wins-five-year-naval-deal/70550486)  
  <sub>ad-hoc-news.de, 22 hours ago</sub>  
  Elbit Systems stock remains in focus after a German naval contract. Its subsidiary will equip F-128 frigates with Aqua Marine electronic-warfare suites.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>Price and chart</b> — score n/a</summary>

```text
Last close 644.14 (bar of 2026-11-25), from 502 daily bars
Trend: vs 20d SMA 707.66 (-9.0%), 50d 716.44 (-10.1%), 200d 784.93 (-17.9%); 50d below 200d
Momentum: RSI(14) 38.9 | MACD -18.735 vs signal -11.273 (histogram -7.463)
Returns: 1d -2.5% | 5d -7.8% | 1m -18.5% | 3m -10.4%
52-week range: 454.95 - 1,014.33 (now 33.8% of the way up)
Volatility: ATR(14) 26.80 (4.2% of price) | annualised 20d 63.3%
Volume: 0.04x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score n/a</summary>

```text
Sector: Industrials / Aerospace & Defense | market cap 30.20B
Valuation: trailing P/E 45.39 | forward P/E 31.62 | P/B 6.60 | PEG n/a
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
Price target: mean 837.33 (+30.0% vs last close), range 739.00 - 935.00
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

- [HDFC Bank Limited (HDB) Stock Price, News, Quote & History](https://ca.finance.yahoo.com/quote/HDB/)  
  <sub>Yahoo! Finance Canada, 17 hours ago</sub>  
  Valuation Measures · Market Cap. 136.17B · Enterprise Value. -- · Trailing P/E. 17.65 · Forward P/E. 15.15 · PEG Ratio (current). 1.93 · Price/Sales (ttm). 4.99.
- [HDFC Bank Limited (HDB) stock price, news, quote and history](https://uk.finance.yahoo.com/quote/HDB/)  
  <sub>Yahoo Finance UK, 15 hours ago</sub>  
  HDFC Bank Limited (HDB) · 4.95% · 24.76% · 11.40% · -24.37% · -24.84% · -20.85% · 3,701.38%. Key events. Baseline. Advanced chart. Loading chart...
- [HDBank Turns to Global Investors to Fund Growth Spurt in Vietnam](https://www.google.com/goto?url=CAESuAEBxCJF15U4WU8cdhjvusx-aAx83-zwsXCCnbRpqpk-q4ZM1VV9oTUQ11vw5owi2IhIc8P0CThknnlw89N9Hf2Wwqhjcf6SY09g54Y1ZzMIWAVvid6qephklg9BRve6TYg7mdh51WFGrFOjRmi3wosRWpwXn-z7f8jjJL5XxLTXmHzTm06JX9P4wbhN6A7MNhkbqhxsTOdP3UlJOaK4V6UdclK-sOPsRPqrTuJ-fakf8kyLWGzJzuEt&gsessionid=iVnQ5i0xUk81L-G_GRGcNxhwPuUaVughHTYUdVqDHEJLjLSQRxpwnA)  
  <sub>Bloomberg, 15 hours ago</sub>  
  Ho Chi Minh City Development JSC Bank is planning to both sell global bonds and borrow via the syndicated loan market, turning to overseas investors to meet...
- [India’s Largest Private Lender Is Lagging – HDFC (HDB) Made into Our 2027 Bargain List](https://www.google.com/goto?url=CAESoAEBxCJF17dnOhPsiELVY3i8hO_16RyDQS_0kx9KRHKgqrafdFMAcrtcBbhTPDf48RRLk1Z7gMnVkuZzSRPxgPGDcN-fU3BCGnjaLs-1PxvKv5Dd4SAb9-jprqclRJRK2lh9eyEP0uThLiJ6pu7PIJ8LiST3VUjBXIDsSLPX3sU5OIhz3jR0Q7QLsEUvqSZ7l2a8hF_6nSugjMcR3EBh7q4f&gsessionid=iVnQ5i0xUk81L-G_GRGcNxhwPuUaVughHTYUdVqDHEJLjLSQRxpwnA)  
  <sub>Yahoo Finance, 17 hours ago</sub>  
  We just published our list of the 10 Dirt-Cheap Stocks Positioned to Soar in 2027, and HDFC Bank Limited (NYSE:HDB) holds the 9th spot.
- [HDBank Global Capital Summit 2026: Connecting global capital flows with Vietnam's aspirations.](https://www.google.com/goto?url=CAESpwEBxCJF1wmKhC9WCkhlM7JJpXNPo_ItxMDuIfMxwrcubt5qLpMa4H657ZM1Is8vxe-6cqkpRvUHmTm1oWMkh_TLRMgfJAVmM2dlqygIT1N2_6xfxGBzBUFt0zn2VVjhwMUlFj4SEgarOuPTkTGef-qYBHtFvprDHyCI3B8R3_YvjFDfuR5CnAm7it3eeEV2AMPuBXWbSBLiUFvg-Q57vEr1G-Yxce9A1Q&gsessionid=iVnQ5i0xUk81L-G_GRGcNxhwPuUaVughHTYUdVqDHEJLjLSQRxpwnA)  
  <sub>Vietnam.vn, 5 hours ago</sub>  
  With the theme "Global Capital – Vietnam's Next Horizon," the conference brought together prestigious names in the fields of finance and economics.
- [Stock market on November 25, foreign investors net sold nearly 5,700 billion VND](https://www.google.com/goto?url=CAESpAEBxCJF10a1omBTgwKuyfaC0sluzgaNmsFE8c2WzHa5mdWtotXaqvVDujVJ9zrlvvkoW_qWL2uwqFpIC95UxmPvq-4Y4jJfFa-sgwl_3DTp-PYMvzci5fU6tv-hfgSY-yXerJnEZDIHiqg7IV2lZPVzMm-Xnc6aD3rhRKXPgyFP-a3OInY24s4apPSDw9PzoAMbo5Mi5TcnUGWGmHgu83VWT6AhyA&gsessionid=iVnQ5i0xUk81L-G_GRGcNxhwPuUaVughHTYUdVqDHEJLjLSQRxpwnA)  
  <sub>Laodong.vn, 4 hours ago</sub>  
  Net selling pressure from foreign investors suddenly increased sharply on the stock market with a value of nearly 5700 billion VND.
- [Civil servants set for 1.55-month year-end bonus; additional one-time payment of up to $600 for select grades](https://www.google.com/goto?url=CAESlwEBxCJF19-IrD9cfUnJo0woOUMrbx9T9MqBjccg5yZEk7BD2vuhLzLVLOPYgHkvAKnRztzmg6Cp6Zqh88Sc8-HHDHdvEv2Ld6sdMm0fnxJLF3v6x2VbZ8ARkvfro-KnveneSpXOZBOczDO0KqefULKoN7hN_1LxyEnlMNDqSpL_vSDiyTWAoz3MGWXHA0s0nBTaCvnyPnPS&gsessionid=iVnQ5i0xUk81L-G_GRGcNxhwPuUaVughHTYUdVqDHEJLjLSQRxpwnA)  
  <sub>AsiaOne.com, 4 hours ago</sub>  
  Civil servants in Singapore will receive a 1.55-month year-end bonus, with junior-grade officers getting an additional one-time payment of up to $600.
- [Complex ground-floor layouts in newer HDB blocks leave residents and visitors lost](https://www.google.com/goto?url=CAEStgEBxCJF1-d4ATje9cYRcycLCbtgpZEuhj791jzeDytIYA7nQrz_msBBQUxrNvUFe8fHOPMF18n-hbAH8mQoDGoksu0Fz_5U3-EuOjsdHgyBzmXDLslFpR3aKJFZinfUYTRSbym9oBIyu1J-6JnPTsELJUMI8c8zNtkHaX_vI2HA7cDaYhjkXPWhT5KZf_oMh0l5_iL7Pf0XFKfSocNy9c8-yklNsuvL5BtI0BCQl8-YYhFOe0dN3Q&gsessionid=iVnQ5i0xUk81L-G_GRGcNxhwPuUaVughHTYUdVqDHEJLjLSQRxpwnA)  
  <sub>联合早报, 7 hours ago</sub>  
  Residents have complained about the complex ground-floor layouts of newer HDB blocks, with one who moved in five years ago still frequently encountering...
- [HDBank announces the public offering of bonds - offering tranche 1](https://www.google.com/goto?url=CAESlgEBxCJF12fPda-NryGIHIHahsSo9vezUv7KE8VwTr0c4JJerx4-ULadWtACB1QZAUFHbVexMQc8tiXLiA6EcqCeX8FZxiy-_scK7KG0dWY2MgwjxCKzbSCby7FJ1OB5qfZML3fg6jNf8UAeOxhcJ1Uv5oXJzoV0Zb9OI3N9205BNMW3Q34AoZGYye7Ejtg0sJQwXkW4J0A&gsessionid=iVnQ5i0xUk81L-G_GRGcNxhwPuUaVughHTYUdVqDHEJLjLSQRxpwnA)  
  <sub>Vietnam.vn, 3 hours ago</sub>  
  HDBank announces the public offering of bonds - offering tranche 1 (Certificate of registration for public offering of bonds No. 687/GCN-UBCK issued by the...
- [HDFC Bank jumps 18% as Bank Nifty hits a record. Has it recovered its 2026 losses?](https://www.google.com/goto?url=CAESxgEBxCJF14kbIzAC6jkePC2Y1m2neREXnRMYZ9aYIePhW_UkmoitWQgMlg4vG5mThB9Ckf3G_blTsV43t0yDQn5Uy6FuCX3m0zDQB9g5p_Wx_JMX4f0R_hpP5sLc5RbHFR-dsfgaaENd8lhVaZ7L97lWrDQPisPLLcwc--7DQJ6NdqR2iM2A0zi6HA2vxMVa_AYMyBAc1ippCjASADCPqN4yuCTOBoh4My0Y6YBDmB6wdvLwHrDHb6wIiN6FD_YajtEgXicH8NA&gsessionid=iVnQ5i0xUk81L-G_GRGcNxhwPuUaVughHTYUdVqDHEJLjLSQRxpwnA)  
  <sub>Upstox, 10 hours ago</sub>  
  HDFC Bank shares have climbed 18.0% so far in November, on course for the stock's biggest monthly gain since November 2020, and the rally helped lift Bank...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>Price and chart</b> — score n/a</summary>

```text
Last close 28.00 (bar of 2026-11-25), from 502 daily bars
Trend: vs 20d SMA 25.42 (+10.2%), 50d 23.74 (+18.0%), 200d 25.16 (+11.3%); 50d below 200d
Momentum: RSI(14) 78.5 | MACD 1.186 vs signal 0.986 (histogram 0.200)
Returns: 1d +1.6% | 5d +6.8% | 1m +31.1% | 3m +24.7%
52-week range: 21.36 - 36.82 (now 42.9% of the way up)
Volatility: ATR(14) 0.65 (2.3% of price) | annualised 20d 26.3%
Volume: 0.10x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score n/a</summary>

```text
Sector: Financial Services / Banks - Regional | market cap 144.05B
Valuation: trailing P/E 18.06 | forward P/E 20.22 | P/B 11.15 | PEG n/a
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
Price target: mean 30.30 (+8.2% vs last close), range 26.20 - 33.00
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

- [JPMorgan Chase & Co. (JPM-PJ) Stock Price, News, Quote & History](https://ca.finance.yahoo.com/quote/JPM-PJ/)  
  <sub>Yahoo! Finance Canada, 6 hours ago</sub>  
  JPMorgan Chase & Co. (JPM-PJ) · -0.18% · -3.36% · -11.52% · -16.11% · -15.56% · -33.62% · -32.35%.
- [JP Morgan Chase & (JPM): JPMorgan notes tied to S&P 500 and Russell 2000 due December 2030](https://www.quantisnow.com/insight/sec-form-fwp-filed-by-jp-morgan-chase-co-6805469)  
  <sub>Quantisnow, 19 hours ago</sub>  
  JPMorgan Chase Financial Company LLC, guaranteed by JPMorgan Chase & Co., filed a fact sheet for buffered notes linked to the S&P 500 and Russell 2000...
- [Inverse VIX Short-Term Futures ETNs due March 22, 2045 Reports Material Event](https://www.google.com/goto?url=CAESvgEBxCJF1wx9fU5vt0Li_mQJw8OAowoVrRiS72WsGGmiHJo3epi875R1M8V_fRHIJjfBx54I_PG-F-1lSiarG_mtt1Ln0rN65sf7fuoLxLJH2BJJRdSn3xQadCzTJoXyXLSj4T82yjRV_LHwPV8GME0zwop9lGUlU7qzicY0nNb1XtmiSsrJ6bdKAsvMmsyyCWzCoQCuSybCdLM4N1JejBmWKRuHpRZIsDhkQtAb4bT2QbO47PgQ8Wmxt435KDMB&gsessionid=4d0WbDMbJeyaGJkf1LgOgpYsd7BiaqG-ro-zUzdIxyEYgnJM4DzC-Q)  
  <sub>Stock Titan, 3 hours ago</sub>  
  Title of each class, Trading Symbol(s), Name of each exchange on which registered. Common stock, JPM, The New York Stock Exchange.
- [JPMorgan Chase & Co. $JPM Stock Holdings Lifted by Steward Partners Investment Advisory LLC](https://www.google.com/goto?url=CAES0AEBxCJF18syuT96TvwBJeq5_wTpy4uuXYL3pxF0Lw-T4NCPgDcCxGQ4nv0dJceq2twZSncvtdfjHRyS__D4MAPTH8S-VfnyL8zONDLK0XHZ65-2-v-ajaAIYk_r9SU_5GfdpCpr4Jz54g5l8rkREpKvCG1ACfawkU4PDV8qbS9_Vfwx1DrKziBOsmjGFgSVXT86Mpo52t7liRbESS47RHbJkbcoJYbelxmqwl7A1-EYDVlxizvf3MqLEnuo1Q41qkZhr1-bBA7XBoDR3PWWctAA&gsessionid=4d0WbDMbJeyaGJkf1LgOgpYsd7BiaqG-ro-zUzdIxyEYgnJM4DzC-Q)  
  <sub>MarketBeat, 4 hours ago</sub>  
  Steward Partners Investment Advisory LLC increased its stake in JPMorgan Chase & Co. (NYSE:JPM - Free Report) by 10.8% in the 3rd quarter, according to its...
- [JPM Dec 2026 265.000 put (JPM261224P00265000) interactive stock chart](https://www.google.com/goto?url=CAESdwHEIkXXAcE2rZDBIWZ5nrE3uId44DYRz0P18OLszyGbMyRLB7lzUzBCgB_2_0saPusnjqiO01JeMpxKellVHKRxZprDAjse729wVAgEEmRMsSEX6bohEHfZR74RpEPYoFdO3KFCpeU8MGLBc1mZkYpn5rpBNaem&gsessionid=4d0WbDMbJeyaGJkf1LgOgpYsd7BiaqG-ro-zUzdIxyEYgnJM4DzC-Q)  
  <sub>Yahoo Finance UK, 11 hours ago</sub>  
  Interactive chart for JPM Dec 2026 265.000 put (JPM261224P00265000) – analyse all of the data with a huge range of indicators.
- [J.P. Morgan Analyst Sets Tesla Stock Price Target for 2026 and 2027](https://www.google.com/goto?url=CAESowEBxCJF12y258MZoOfGXGvN1QBRt5YsU65pfVR8cNd4WKqHpMYM1mS-_qVpUpOexnYUksuYAODynWhAscy8gW0KLBbUh4vqSNbq5fbmWRu3i6U4SZ9pWC0sJIluPG1GRmahi5OUq0RZNGQXQV248hXxZK8UqBDsc9wydM7-K8fPze66_NhCU5N8fLRauCtnXN3VzIZJe9UN6dqs0k2yJYIBeshS&gsessionid=4d0WbDMbJeyaGJkf1LgOgpYsd7BiaqG-ro-zUzdIxyEYgnJM4DzC-Q)  
  <sub>Coinpedia, 24 hours ago</sub>  
  With Tesla Inc. (NASDAQ: TSLA) stock having fallen more than 12% so far in 2026, Rajat Gupta, a Wall Street analyst at JPMorgan Chase & Co. (NYSE: JPM)...
- [JPM: SEC Form FWP filed by JP Morgan Chase & Co.](https://www.google.com/goto?url=CAESigEBxCJF10z0iemfWPgsH6JfF8H5JT9bVINh_0tdMWVz8hGqCydKd_60NxSZvaAHwx_Jnhagb-y1g98nZOFnvKnBMqNmuXSn-g2TIUffXvT-MQ4g3CWJIhywlH5kU4G4KMkbPRPS88vWJOnUY-gyVucCN3gI67y8k3r-te0V4984Yg3LvyCo7u7TE60&gsessionid=4d0WbDMbJeyaGJkf1LgOgpYsd7BiaqG-ro-zUzdIxyEYgnJM4DzC-Q)  
  <sub>Quantisnow, 20 hours ago</sub>  
  JPMorgan Chase Financial Company LLC plans to sell notes tied to the S&P 500 Futures Excess Return Index, maturing December 16, 2032, with JPMorgan Chase &.
- [Bank of America Short Interest Falls From October Peak](https://www.google.com/goto?url=CAESswEBxCJF17l8eZs0ihFiIySb2_v5MiheQkyFy5vwK-pbkTNKCNbCKDwLJ8XIrejsuCT7dBhjjcEJPCRB_MMPJzX6MW8dJ7o2OQfC6O7LUFQuJvv1dyzkeSAdQ4reatEQ6v0DVSvOhedu_OtoSZWB7J9ctxbPszPb2NCIwJF7sA-TtyJK56XvLA3ZKfIX_1lDIf6nyiW7NVBfgLJ4PdAfb6K1qX464ZN0H5Kj8GtfnkMNdEcUMw&gsessionid=4d0WbDMbJeyaGJkf1LgOgpYsd7BiaqG-ro-zUzdIxyEYgnJM4DzC-Q)  
  <sub>Benzinga, 23 hours ago</sub>  
  Bank of America Corp. (NYSE:BAC) short sellers pulled back from their positions as the latest report showed a decline from the prior period.
- [JPMorgan Chase & Co. $JPM Stock: Healthcare of Ontario Pension Plan Trust Fund Cuts Holdings](https://www.google.com/goto?url=CAES0AEBxCJF17wuEFlxsO3Ke_Eod_sDx3ZnEXYOBoGXxaRRGLgsNtMMK_ncFiI8fO9vVMAs0ITGuFsRs2HzExe1vFB8MIttDhXIJA_Wu8PbTcfpVpQ6--KkOCtiY8dWBIW10A1zN44xnJjIww7-5YTRPdqS3K8c4sPNF7QZw-uMFbRdeHfjiGj3MZNX_ACbnis9TPKlJzrQLBC9gj9aP6HQgZG2wuTRPku1IKVo5Vt4lv3cH38rs2RvvwXbAGuuPhCYHjKDxb8GBaHYTcgJ9FqB60qR&gsessionid=4d0WbDMbJeyaGJkf1LgOgpYsd7BiaqG-ro-zUzdIxyEYgnJM4DzC-Q)  
  <sub>MarketBeat, 4 hours ago</sub>  
  Healthcare of Ontario Pension Plan Trust Fund reduced its stake in shares of JPMorgan Chase & Co. (NYSE:JPM - Free Report) by 49.0% in the third quarter,...
- [JPMorgan Chase & Co. (NYSE:JPM) Stock Sale Revealed by Rep. Harriet M. Hageman](https://www.google.com/goto?url=CAESwgEBxCJF1z9sClMGLXOT2lZhgzKxwEifc7OBBdrWOc7bQ5Isy2rIr5YhChkGWU0PMH6H_MglLebW2WpQ_y8T3NTDHWaVlMbk69e9fa3fdWwzwiDbxwq0G9GpBXOHY7WmUhyJlnm7n4AB6zEbdKchKipDiDE3JcQZlYweyPQtJlpDNAvfa7QJGpjlrHpDSmuRn5VziDgPscYaYmroEFBOa0Oj09qIZCFHQjBQdCKYjSTVTd-jnf2WoNEbFdT6FHGnuYu0mg&gsessionid=4d0WbDMbJeyaGJkf1LgOgpYsd7BiaqG-ro-zUzdIxyEYgnJM4DzC-Q)  
  <sub>MarketBeat, 8 hours ago</sub>  
  Representative Harriet M. Hageman (Republican-Wyoming) recently sold shares of JPMorgan Chase & Co. (NYSE:JPM). In a filing disclosed on November 23rd,...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>Price and chart</b> — score n/a</summary>

```text
Last close 311.65 (bar of 2026-11-25), from 502 daily bars
Trend: vs 20d SMA 333.41 (-6.5%), 50d 335.23 (-7.0%), 200d 325.11 (-4.1%); 50d above 200d
Momentum: RSI(14) 34.1 | MACD -6.284 vs signal -3.340 (histogram -2.944)
Returns: 1d -1.7% | 5d -3.8% | 1m -7.2% | 3m -12.0%
52-week range: 282.84 - 365.18 (now 35.0% of the way up)
Volatility: ATR(14) 7.92 (2.5% of price) | annualised 20d 32.1%
Volume: 0.07x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score n/a</summary>

```text
Sector: Financial Services / Banks - Diversified | market cap 827.62B
Valuation: trailing P/E 13.07 | forward P/E 12.19 | P/B 2.36 | PEG 1.32
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
Price target: mean 373.48 (+19.8% vs last close), range 312.00 - 425.00
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

- [Eli Lilly stock rises Tuesday: What's happening?](http://www.bing.com/news/apiclick.aspx?ref=FexRss&aid=&tid=6b06f40557fc4dbca38c3f1261f24875&url=https%3a%2f%2fwww.msn.com%2fen-us%2fmoney%2ftop-stocks%2feli-lilly-stock-rises-tuesday-what-s-happening%2far-AA2i8Gjc&c=18303177203259920783&mkt=en-us)  
  <sub>Benzinga on MSN, 29h ago</sub>  
  Eli Lilly and Company (NYSE:LLY) shares are trading higher on Tuesday. Here’s what investors need to know. Eli Lilly shares are powering higher. What’s fueling LLY momentum? Lilly Sees Cancer As Its ...
- [Forget Zepbound: Lilly's Retatrutide Just Cut Sleep Apnea Severity by Up to 60%](http://www.bing.com/news/apiclick.aspx?ref=FexRss&aid=&tid=6b06f40557fc4dbca38c3f1261f24875&url=https%3a%2f%2fwww.msn.com%2fen-us%2fnews%2fother%2fforget-zepbound-lillys-retatrutide-just-cut-sleep-apnea-severity-by-up-to-60%2far-AA2i8M7H&c=989328538325851749&mkt=en-us)  
  <sub>The Motley Fool on MSN, 30h ago</sub>  
  Recent clinical trial results could bolster the argument that Eli Lilly's key growth catalyst will stay in motion.
- [Eli Lilly earns Moody’s upgrade to Aa2 as obesity drug demand fuels earnings](http://www.bing.com/news/apiclick.aspx?ref=FexRss&aid=&tid=6b06f40557fc4dbca38c3f1261f24875&url=https%3a%2f%2fuk.finance.yahoo.com%2fnews%2feli-lilly-earns-moody-upgrade-204431978.html&c=13642278241898316813&mkt=en-us)  
  <sub>Yahoo Finance UK, 31h ago</sub>  
  Moody’s Ratings upgraded Eli Lilly and Company's (NYSE:LLY) senior unsecured notes and issuer ratings to Aa2 from Aa3 on Tuesday, citing rapid earnings momentum driven by its dominant metabolic drug ...
- [Loftus Peak Global Disruption Hedged Active ETF Discloses October 2026 Portfolio with Eli Lilly at 8.34%](http://www.bing.com/news/apiclick.aspx?ref=FexRss&aid=&tid=6b06f40557fc4dbca38c3f1261f24875&url=https%3a%2f%2fkalkine.com.au%2fnews%2fannouncements%2floftus-peak-global-disruption-hedged-active-etf-discloses-october-2026-portfolio-with-eli-lilly-at-834&c=10403115217142634716&mkt=en-us)  
  <sub>kalkine, 32h ago</sub>  
  Loftus Peak Global Disruption Hedged Active ETF (ASX:LPH) has disclosed its monthly portfolio holdings as at 31 October 2026, with Eli Lilly & Company representing the largest position at 8.34% and ...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>Price and chart</b> — score n/a</summary>

```text
Last close 1,381.17 (bar of 2026-11-25), from 502 daily bars
Trend: vs 20d SMA 1,399.11 (-1.3%), 50d 1,281.74 (+7.8%), 200d 1,123.03 (+23.0%); 50d above 200d
Momentum: RSI(14) 54.2 | MACD 26.390 vs signal 37.515 (histogram -11.125)
Returns: 1d -1.9% | 5d -0.1% | 1m +7.7% | 3m +17.4%
52-week range: 851.21 - 1,443.50 (now 89.5% of the way up)
Volatility: ATR(14) 42.34 (3.1% of price) | annualised 20d 39.3%
Volume: 0.06x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score n/a</summary>

```text
Sector: Healthcare / Drug Manufacturers - General | market cap 1.23T
Valuation: trailing P/E 44.85 | forward P/E 27.16 | P/B 30.58 | PEG 1.25
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
Price target: mean 1,470.06 (+6.4% vs last close), range 940.00 - 1,700.00
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

- [MELI Nov 2026 1610.000 call (MELI261127C01610000) Stock Price, News, Quote & History](https://ca.finance.yahoo.com/quote/MELI261127C01610000/)  
  <sub>Yahoo! Finance Canada, 7 hours ago</sub>  
  Find the latest MELI Nov 2026 1610.000 call (MELI261127C01610000) stock quote, history, news and other vital information to help you with your stock trading...
- [MercadoLibre vs. Target: Which Stock Looks More Compelling Now?](https://www.theglobeandmail.com/investing/markets/stocks/TGT-N/pressreleases/8987113/mercadolibre-vs-target-which-stock-looks-more-compelling-now/)  
  <sub>The Globe and Mail, 11 hours ago</sub>  
  MercadoLibre, Inc. MELI and Target Corporation TGT are pursuing strategic initiatives to strengthen customer engagement, expand revenue opportunities and...
- [Is MercadoLibre (MELI) Becoming A Bigger AI Play In Emerging Markets?](https://www.google.com/goto?url=CAESvQEBxCJF12xnpGPzn9vol058BobvzJzN-7G3NPai3OzwkJuOZf8Obv4nUW_WSCAR4eM6biIk_qw7jpG_F1iMJg59CaMCQlIADhQ8ZdctCIouPHAdrdSFL3b-t_UTAfpmCsHf7Nbfulla7r8xSjkBzu7ZZrfzwRnOnY8N5vFCqIxFDyQURnExExQugQMIlOkTW0wpvIlhCPC3SLULfRCg7suFuufgvEGqbYG8J4VANzRHhXg-WOBhoJhG4LpSdkk&gsessionid=ePWeR2RM82AIK9-70DjV3cf4LotH5l16ZYqJldJN1X-oDE4L-TXXtw)  
  <sub>Simply Wall St, 34 minutes ago</sub>  
  EMQQ Global has highlighted MercadoLibre (NasdaqGS:MELI) as a key beneficiary of AI adoption across emerging market e commerce and fintech.
- [MELI Dec 2026 1555.000 call (MELI261231C01555000) interactive stock chart](https://www.google.com/goto?url=CAESeAHEIkXXCgTQbxeS19piXtf3ggqoDiePFqtOcD_s7q4wVS2iVSez-Pm20DdQomA-RsfXqYDz_45C4zGTesF3h9j3OPD8aIKaIw4njGJs7RoHTbEHlGSSkPiHamtbPe8B55cyPZeT0nmbTYw0AmVgWcbJ_cyhbjTsAg&gsessionid=ePWeR2RM82AIK9-70DjV3cf4LotH5l16ZYqJldJN1X-oDE4L-TXXtw)  
  <sub>Yahoo Finance UK, 9 hours ago</sub>  
  Interactive chart for MELI Dec 2026 1555.000 call (MELI261231C01555000) – analyse all of the data with a huge range of indicators.
- [MELI261231C01505000 Interactive Stock Chart | MELI Dec 2026 1505.000 call Stock](https://www.google.com/goto?url=CAESbgHEIkXX0MsudX4hu7XyZRuwLPSmdAsTCrs4phfLVDd2EEYj_W6l9vjhxsXOpz9LA4dKrtLMwcRzm98OmxlNGeozmefn0n2IrxDr7mKSpjaaAkrHeHqQMSh6VhKKMIbkGLYcfgKVla-j_DewCrWi&gsessionid=ePWeR2RM82AIK9-70DjV3cf4LotH5l16ZYqJldJN1X-oDE4L-TXXtw)  
  <sub>Yahoo Finance, 9 hours ago</sub>  
  At Yahoo Finance, you get free stock quotes, up-to-date news, portfolio management resources, international market data, social interaction and mortgage...
- [MELI Nov 2026 1880.000 call (MELI261127C01880000) stock price, news, quote and history](https://www.google.com/goto?url=CAEScgHEIkXXeQImetSwsI_jRDqiCMLlueGMrflibv7U_3c6JqhfgGTDnHqqG1beUDuS3VraOSezZ-i9JRspxxksUQUT3gbYUoRDF8463Vdrsw3FgFU5beIIO9QEC7KE9VvF6Ap0YrXgwe_zX_UrRhJsq0FAsA&gsessionid=ePWeR2RM82AIK9-70DjV3cf4LotH5l16ZYqJldJN1X-oDE4L-TXXtw)  
  <sub>Yahoo Finance UK, 14 hours ago</sub>  
  Find the latest MELI Nov 2026 1880.000 call (MELI261127C01880000) stock quote, history, news and other vital information to help you with your stock trading...
- [MELI Dec 2028 1320.000 call (MELI281215C01320000) stock price, news, quote and history](https://www.google.com/goto?url=CAEScgHEIkXX1Iaxzv-z5as64kPzrBRhiTro_2DOD52K4T3KpndM1BKuob0g7RO7k1I7cPEACkTzbgQi1PbtgVNDstwIKevJDDaHbG_FSS2eR6zci0sSgcvw9I9A3V_MjsHd3AsMbKmZZ16aXvLsaLanpVWrzQ&gsessionid=ePWeR2RM82AIK9-70DjV3cf4LotH5l16ZYqJldJN1X-oDE4L-TXXtw)  
  <sub>Yahoo Finance UK, 17 hours ago</sub>  
  Find the latest MELI Dec 2028 1320.000 call (MELI281215C01320000) stock quote, history, news and other vital information to help you with your stock trading...
- [MELI Nov 2026 1695.000 put (MELI261127P01695000) stock price, news, quote and history](https://www.google.com/goto?url=CAEScgHEIkXXfMJD8iEvl9VQyh-X1UxjpcFKJMfAQDrTFcmibmwJQbQFTaCUkXYW7wuJBeSu5yVQ7FgsOU0rdMCSxuu7RYW7010KUwatTfnVersQF3DN6tj9GrfX-73pw2Vb4O3y9wlXrkajlTCedp6lkGA9ng&gsessionid=ePWeR2RM82AIK9-70DjV3cf4LotH5l16ZYqJldJN1X-oDE4L-TXXtw)  
  <sub>Yahoo Finance UK, 17 hours ago</sub>  
  Find the latest MELI Nov 2026 1695.000 put (MELI261127P01695000) stock quote, history, news and other vital information to help you with your stock trading...
- [MELI261127P01385000 Interactive Stock Chart | MELI Nov 2026 1385.000 put Stock](https://www.google.com/goto?url=CAESbgHEIkXXWGSP7CNIUia4BH2kiZ5BjQvs63IqlrNzbW1TG62SU1m4-K9tv4sHvIhdigMqm2r8liy79u7hTn40CaLBREu9LGwX-BJ36dT6mc3ZodPdRSDDHmMyAjBUGriajmWTw-AR5z4qcLf_aeBc&gsessionid=ePWeR2RM82AIK9-70DjV3cf4LotH5l16ZYqJldJN1X-oDE4L-TXXtw)  
  <sub>Yahoo Finance, 17 hours ago</sub>  
  At Yahoo Finance, you get free stock quotes, up-to-date news, portfolio management resources, international market data, social interaction and mortgage...
- [MELI Nov 2026 1435.000 put (MELI261127P01435000) interactive stock chart](https://www.google.com/goto?url=CAESeAHEIkXXxRYfFxQgUnQAI9hSujeZnYPbBRZqOIaUCeh_Tolw7pcBhhcdBmYpksolGJ0_u9QpYQago3Atsm-mD9oq_ozCAGogE7Hy_-XAUMcTHGXBHUIH5C7S19iKcppu4JARay5Yf4iqCyvVt0zkhYtbPrizccpT9w&gsessionid=ePWeR2RM82AIK9-70DjV3cf4LotH5l16ZYqJldJN1X-oDE4L-TXXtw)  
  <sub>Yahoo Finance UK, 18 hours ago</sub>  
  Interactive chart for MELI Nov 2026 1435.000 put (MELI261127P01435000) – analyse all of the data with a huge range of indicators.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>Price and chart</b> — score n/a</summary>

```text
Last close 1,412.02 (bar of 2026-11-25), from 502 daily bars
Trend: vs 20d SMA 1,511.26 (-6.6%), 50d 1,684.13 (-16.2%), 200d 1,757.70 (-19.7%); 50d below 200d
Momentum: RSI(14) 35.8 | MACD -89.682 vs signal -90.050 (histogram 0.368)
Returns: 1d -2.6% | 5d -0.8% | 1m -16.0% | 3m -26.9%
52-week range: 1,355.00 - 2,295.00 (now 6.1% of the way up)
Volatility: ATR(14) 60.81 (4.3% of price) | annualised 20d 58.7%
Volume: 0.07x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score n/a</summary>

```text
Sector: Consumer Cyclical / Internet Retail | market cap 71.48B
Valuation: trailing P/E 37.82 | forward P/E 26.62 | P/B 8.72 | PEG 0.74
Profitability: profit margin 4.9% | operating margin 7.4% | ROE 26.2%
Growth (YoY): revenue +45.1% | earnings +6.3%
Balance sheet: debt/equity 197.4% | free cash flow -2.57B
Risk: beta 1.39 | short interest 2.4% of float
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
Price target: mean 2,152.76 (+52.5% vs last close), range 1,600.00 - 2,700.00
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

### Novo Nordisk (NVO) · Company — no answer, no confidence given

<details><summary><b>News</b> — score n/a</summary>

- [Novo vs. Amgen: Which Healthcare Stock Is the Better Buy Now?](https://finance.yahoo.com/healthcare/articles/novo-vs-amgen-healthcare-stock-162100037.html)  
  <sub>Yahoo Finance, 22 hours ago</sub>  
  NVO and AMGN offer different paths to obesity-market growth, with contrasting earnings trends, pipeline prospects and valuations shaping their investment...
- [Novo Nordisk A/S Stock (NVO) Moved Up by 3.17% on Nov 24: What Signal Does It Send?](https://www.tradingkey.com/news/market-movers/262320517-market-movers-nvo-20261124)  
  <sub>TradingKey, 20 hours ago</sub>  
  Novo Nordisk shares rose due to strong cardiometabolic portfolio demand.Improved manufacturing capacity reinforced confidence in GLP-1 therapy delivery.
- [NVO Dec 2026 42.000 put (NVO261231P00042000) stock price, news, quote and history](https://www.google.com/goto?url=CAEScQHEIkXX6GPjELy-2frlMc6b3lsMD9OjPklwfs8xxg3Ssi8ctoBePj857Dxu9EyNFFHdccMNQshX7oHFfrhTSwfEqof4e6R60nFaIihR7dhyiLyB787yKB7XoMytdRzRCkVLZiJLXkmDZNk1LGGmznfK&gsessionid=MbtwRGxKku3WZaLbfDSAqwQxFeCIbQ8GQy_cfMWZcSb6L_EV6HM5_w)  
  <sub>Yahoo Finance UK, 22 hours ago</sub>  
  Find the latest NVO Dec 2026 42.000 put (NVO261231P00042000) stock quote, history, news and other vital information to help you with your stock trading and...
- [NVO Dec 2026 43.000 call (NVO261224C00043000) Interactive Stock Chart - Yahoo Finance](https://www.google.com/goto?url=CAESdwHEIkXXxA95x9C3s_AF94lmieMmlIzJOlWp_mk18-Pgsf5-e4Y-J9RED8c0_MR-tES5ZhvkITVxgJeHCyIL7iEGCpF1edVT2l7oqEwxxLcmNaw2RKAlH65pAgEmWq26vJmuVVeYFx_WRgOuhKDsSqhL0_pZDSrw&gsessionid=MbtwRGxKku3WZaLbfDSAqwQxFeCIbQ8GQy_cfMWZcSb6L_EV6HM5_w)  
  <sub>Yahoo! Finance Canada, 22 hours ago</sub>  
  Interactive Chart for NVO Dec 2026 43.000 call (NVO261224C00043000), analyze all the data with a huge range of indicators.
- [Novo Nordisk wins FDA Sogroya indication: NVO gains momentum](https://www.google.com/goto?url=CAESjwEBxCJF16-mX58b9pWG5CyIXfd60Uuc7I7NlA87YMgB_Imy444kqIy4hcZOD7YtnGbnjNRw07IYyQR4yJwx6p-kY2Te8A8KvZnexlu-XD-84kmNWZGHXxkhJSivxtA-X34ttGccm-5eYgCYtinoFQjtFpet58sMSwH5t4YUy7AsA8Pk0_D0NcCUPegjpMQuDA&gsessionid=MbtwRGxKku3WZaLbfDSAqwQxFeCIbQ8GQy_cfMWZcSb6L_EV6HM5_w)  
  <sub>Traders Union, 7 hours ago</sub>  
  Novo Nordisk (NVO) stock is trading at $40.31, gaining 2.99% on the day. The price sits above its key short- and medium-term moving averages, with notable...
- [NVO Nov 2026 39.500 call (NVO261127C00039500) stock price, news, quote and history](https://www.google.com/goto?url=CAEScQHEIkXXIJ8kQxHzr-0Y0rpNWUg889_k0rcvghvUl-xt6LkG1_UfhtXk7APNVQKAnG7vsSHq23yUwVfYd3s0T1NDFVN3s7uEOtIQ2w12RP1BIIUdU-z7pYKcqSWQSOCMeaGQ1_eZgwHHpobHzur-kMTd&gsessionid=MbtwRGxKku3WZaLbfDSAqwQxFeCIbQ8GQy_cfMWZcSb6L_EV6HM5_w)  
  <sub>Yahoo Finance UK, 23 hours ago</sub>  
  Find the latest NVO Nov 2026 39.500 call (NVO261127C00039500) stock quote, history, news and other vital information to help you with your stock trading and...
- [Novo Nordisk (NVO) Stock Price Prediction: Momentum improves, but Novo Nordisk still has to prove it can hold above resistance](https://www.google.com/goto?url=CAESngEBxCJF196eY8cqzgMQOa6RqzP9EvmTDOiX_0pk82yhFdJIq__9n4zHVamJ4ITXgdo_C4fAaDyAYGP4ZqLbj5RlxT0XcHwAMMvivED1fm86XFFPksX6or1I_Da_4RlN1o6Nr2IqsuTZ0fm7zzrsuAglEYBm-5W3VcOsskipc6DYYnl7IIpVVM9shAJf_1A8WkHpGtj663jjTkYmcqbReA&gsessionid=MbtwRGxKku3WZaLbfDSAqwQxFeCIbQ8GQy_cfMWZcSb6L_EV6HM5_w)  
  <sub>Blockchain News, 4 hours ago</sub>  
  Novo Nordisk (NVO) is trading at $40.72 after a 3.69% advance over the last 24 hours. The session range of $39.26 to $40.77 shows the stock pushed back...
- [UnitedHealth Group (UNH) Stock Price Prediction: Analysts turn more constructive as the stock tries to stabilize below key moving averages](https://www.google.com/goto?url=CAESnAEBxCJF13iZYbrmghe_ls-i8gaXfGWI60eCCG3fCIQXlrtQI7PEKmmEDx4jC6QMWtUewKWFIrjCMlNZj7pOAwCSKZmYAlgcC00yzVYP8xxYBJKTumczQV-9FqsFANFnAfNIpbtMNKgAsqVyux1w7yyP3X4Wyky5A_oIqDPfqH0kN_cO0rgKVn_B9Vvzl4d_K2TpkycUnZ_2Avr_bkM&gsessionid=MbtwRGxKku3WZaLbfDSAqwQxFeCIbQ8GQy_cfMWZcSb6L_EV6HM5_w)  
  <sub>Blockchain News, 4 hours ago</sub>  
  UnitedHealth Group (UNH) is trading at $340.91, up 1.02% on the day, after a sharp reset that left the stock well below its 20-day and 50-day moving...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>Price and chart</b> — score n/a</summary>

```text
Last close 40.06 (bar of 2026-11-25), from 502 daily bars
Trend: vs 20d SMA 40.30 (-0.6%), 50d 39.42 (+1.6%), 200d 42.75 (-6.3%); 50d below 200d
Momentum: RSI(14) 50.4 | MACD -0.075 vs signal 0.031 (histogram -0.106)
Returns: 1d -0.6% | 5d +1.6% | 1m +3.6% | 3m -13.4%
52-week range: 35.29 - 63.98 (now 16.6% of the way up)
Volatility: ATR(14) 1.12 (2.8% of price) | annualised 20d 39.5%
Volume: 0.08x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score n/a</summary>

```text
Sector: Healthcare / Drug Manufacturers - General | market cap 176.49B
Valuation: trailing P/E 10.11 | forward P/E 11.40 | P/B 5.40 | PEG 3.96
Profitability: profit margin 33.9% | operating margin 50.8% | ROE 58.4%
Growth (YoY): revenue +5.6% | earnings -15.8%
Balance sheet: debt/equity 61.7% | free cash flow 32.75B
Risk: beta 0.37 | short interest 1.3% of float
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
Price target: mean 45.60 (+13.9% vs last close), range 39.29 - 63.84
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

- [PG Dec 2026 90.000 call (PG261204C00090000) Stock Price, News, Quote & History](https://ca.finance.yahoo.com/quote/PG261204C00090000/)  
  <sub>Yahoo! Finance Canada, 5 hours ago</sub>  
  Find the latest PG Dec 2026 90.000 call (PG261204C00090000) stock quote, history, news and other vital information to help you with your stock trading and...
- [Will Procter & Gamble's Restructuring Plan Sharpen Its Cost Base?](https://www.tradingview.com/news/zacks:832642d90094b:0-will-procter-gamble-s-restructuring-plan-sharpen-its-cost-base/)  
  <sub>TradingView, 3 hours ago</sub>  
  The Procter & Gamble Company PG, also known as P&G, is accelerating its restructuring efforts to build a leaner and more efficient operating model amid...
- [Congress Trade: Representative Robert Onder Just Disclosed New Stock Trades](https://www.google.com/goto?url=CAESqQEBxCJF17WTUEsC2FufTEHIgxqTeLrb7cu38F-4s-gmkaR93qTfqFX8ylW4Arux_wgbwrE9ZETAsvGbBgARehSnPyzInjhBK05yGlZM7Fu0X29tcPGAkWERm0PU89H-wyd0ECnr0EaAexkSCkzfnirQMOE_I3dco9KwXmQJiAEMvna9ELnApbG-jN_cwlD5Ikm68PDBw6n9I2cumkqAbOVVlMcOijv1uG6Z&gsessionid=x8a-EauYRoqcm-NfxA_-AXocMLiY_FPCFCJJDXxCDx2-q4-GKHG09g)  
  <sub>Quiver Quantitative, 26 minutes ago</sub>  
  Representative Robert Onder just filed new stock trades, which we received from a STOCK Act disclosure. You can see the full list of trades on Quiver...
- [If the Fed Hikes on Dec. 9, These 4 Dividend Stocks Are Built to Handle It](https://www.google.com/goto?url=CAESrwEBxCJF1yaTCrzyAhFpTKuYYs91A23eMK50LNpdllOOXN-EC1fmBuFVywSPK2E0KHzjguyyK6IiyU5I_WJhCJTxA2O80D9VIhTyoJE8Uz0kO2Jw-ZOZb1zXEBWtOEhePBrOuOH9h1DUrCpVmsmudYAncqxTZFlfltoeM58U6kTfo0VqonO9g8s_IAj9n52Xjs9tS2PlC3WbNtfyzERNaWktYUDFKJHzdH75As9z1Bbr&gsessionid=x8a-EauYRoqcm-NfxA_-AXocMLiY_FPCFCJJDXxCDx2-q4-GKHG09g)  
  <sub>24/7 Wall St., 1 hour ago</sub>  
  Enterprise Products Partners covered its distribution nearly 2x with cash flow and kept $1.1 billion, so a Fed hike barely touches its payout.
- [Procter & Gamble Company (The) $PG Stock: Marshall Wace LLP Increases Stake](https://www.google.com/goto?url=CAESvgEBxCJF16-35Rg8pHM-SWni9SRRkGmCSpbdmOSHAvl_mBODZaNZV6elCqhq1hkLJOLsERHbg3TAHcMcrZzgkZkf0rX1b2fj5QPIY7XaMhof0Ehv3HGX6iTsyt4Gx-AKjS3lU_6nuHiip170Z-bIHQxpEfjdkvZlAynAPZtdKsbfOO4J1stS5Or6YeQT3rXGnSVHvPa4V_wxnYtyUUc-2A6IJhaCG5qUXTmOAoPPlP77BV4p2YyMzwZN79J5FPE2&gsessionid=x8a-EauYRoqcm-NfxA_-AXocMLiY_FPCFCJJDXxCDx2-q4-GKHG09g)  
  <sub>MarketBeat, 3 hours ago</sub>  
  Marshall Wace LLP increased its holdings in Procter & Gamble Company (The) (NYSE:PG - Free Report) by 36354.3% in the third quarter, according to its most...
- [P&G to Webcast Fireside Chat From the Morgan Stanley Global Consumer & Retail Conference, December 2](https://www.google.com/goto?url=CAESlQEBxCJF13_5_AzLkCCbMavjpD5M3EnkjsXBcXCsuk-g3DZud_I-_iW87c1ZROUdMepFDVIaGvksaK2edqWzzcqnltyjFgF2ceGwgodtR8lxnQFD_yNexmz8a9zlMRDF7GB0z_M3isjeU1oWOjDm1stYW72On2T9bRD5VKKflNHh6IXFCWA0B0QizO1P8ZkTEyrMKIg5iQ&gsessionid=x8a-EauYRoqcm-NfxA_-AXocMLiY_FPCFCJJDXxCDx2-q4-GKHG09g)  
  <sub>Yahoo Finance, 3 hours ago</sub>  
  CINCINNATI, November 25, 2026--Andre Schulten, Chief Financial Officer of The Procter & Gamble Company (NYSE:PG), will be a featured speaker at the Morgan...
- [BNP Paribas Adjusts Price Target on Procter & Gamble to $197 From $189](https://www.google.com/goto?url=CAESsgEBxCJF13YbjN3gxePNxS81URA2fGRN4RASV6ZlDVUS-EExYjj2Au0CVeHNYLkScJYI4n7cBKExUoWk3fwU9Sxq14iqvjsS0glIkqMWIllq-NsnIEI8HjzDApeWl_IF7d5DJjWVAjZs-NvbU82R_DbBDcB5PiWtEA-rC5B24a7wOhX3tuUhvf6EQDzyBXdt6E7AKxz1W3i-fs23FcyQMJ_L9Nr5n2QwKYd_vKeKEhdd06KV&gsessionid=x8a-EauYRoqcm-NfxA_-AXocMLiY_FPCFCJJDXxCDx2-q4-GKHG09g)  
  <sub>marketscreener.com, 4 hours ago</sub>  
  Procter & Gamble has an average rating of overweight and mean price target of $177.29, according to analysts polled by FactSet. -November 25, 2026 at 05:40...
- [Procter & Gamble Company (The) $PG Position Boosted by Healthcare of Ontario Pension Plan Trust Fund](https://www.google.com/goto?url=CAES2AEBxCJF126dPP9pBMX61fltwN0pCQzbqprceHZ7H3r9k27VUIp0zoH-m5vYh_DyJCjL4CVWkTxRtW35pXA4rKYhzhikuyj3XICBVCzEAgRHzTEjAQSIHT2EWxrHcubLFvV3_N9g1vMNE1yGBir8i-W3h9PnHy-nLBokdA6qQeGm9tNV0mJPYk0k3B-gvSEgdWrrN2OOcrcPhpkqnh7g06vaM8hlsn5XJhVGQoo8oU46SRJmmW4wIunuuaDPRya_htadWvCsPPODlqX_xswU6Kd0fJmWqMIp1Bg&gsessionid=x8a-EauYRoqcm-NfxA_-AXocMLiY_FPCFCJJDXxCDx2-q4-GKHG09g)  
  <sub>MarketBeat, 4 hours ago</sub>  
  Healthcare of Ontario Pension Plan Trust Fund raised its holdings in Procter & Gamble Company (The) (NYSE:PG - Free Report) by 146.6% in the third quarter,...
- [ROBERT ONDER Trading Activity](https://www.google.com/goto?url=CAESiAEBxCJF11fXb8L4KJa0bNX7D8Oe3PRiluLmb5C9L7Im-BAVz9afKfNCWR5hKYP3RYqvSDfMJUjX1hTvTJ0UHyJsdUFOS90wYUhl_9NFkWUVwJG05LoGYVh_L6lA6I7wGAsFEdVIliOsqrWJiIquqzaio52tP7Zb7HxMvW84pu5fy0oycqnk9WVO&gsessionid=x8a-EauYRoqcm-NfxA_-AXocMLiY_FPCFCJJDXxCDx2-q4-GKHG09g)  
  <sub>Quiver Quantitative, 10 minutes ago</sub>  
  Track ROBERT ONDER's stock trades, net worth, portfolio, corporate donors, proposed legislation and more.
- [PG Nov 2026 140.000 put (PG261127P00140000) stock price, news, quote and history](https://www.google.com/goto?url=CAEScAHEIkXXQBYBBTOYradsWrQeBoHFHQwFp8eLTwZvGGEjL-00CTI-mEZ6NLAR0YJLZhKEkkY-hk8H3bg9_Tqzu08XhLAVrKIAy2BOSDelIh7RVJqEBuV1j7AznQYJ96ObOtJ7EZYRKaTMSoyuKptidDU&gsessionid=x8a-EauYRoqcm-NfxA_-AXocMLiY_FPCFCJJDXxCDx2-q4-GKHG09g)  
  <sub>Yahoo Finance UK, 13 hours ago</sub>  
  Find the latest PG Nov 2026 140.000 put (PG261127P00140000) stock quote, history, news and other vital information to help you with your stock trading and...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>Price and chart</b> — score n/a</summary>

```text
Last close 172.97 (bar of 2026-11-25), from 502 daily bars
Trend: vs 20d SMA 167.87 (+3.0%), 50d 158.35 (+9.2%), 200d 150.46 (+15.0%); 50d above 200d
Momentum: RSI(14) 66.5 | MACD 3.740 vs signal 3.922 (histogram -0.183)
Returns: 1d +0.3% | 5d +1.6% | 1m +8.6% | 3m +20.8%
52-week range: 138.04 - 173.02 (now 99.9% of the way up)
Volatility: ATR(14) 3.10 (1.8% of price) | annualised 20d 19.2%
Volume: 0.08x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score n/a</summary>

```text
Sector: Consumer Defensive / Household & Personal Products | market cap 400.91B
Valuation: trailing P/E 26.05 | forward P/E 23.29 | P/B 7.38 | PEG 4.35
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
Price target: mean 176.35 (+2.0% vs last close), range 151.00 - 192.00
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

- [RY Dec 2026 200.000 call (RY261218C00200000) stock price, news, quote and history](https://uk.finance.yahoo.com/quote/RY261218C00200000/)  
  <sub>Yahoo Finance UK, 3 hours ago</sub>  
  Find the latest RY Dec 2026 200.000 call (RY261218C00200000) stock quote, history, news and other vital information to help you with your stock trading and...
- [Royal Bank of Canada stock consolidates amid range-bound trading and support pressure](https://tradersunion.com/news/stocks/show/4412878-royal-bank-of-canada-slips/)  
  <sub>Traders Union, 40 minutes ago</sub>  
  Royal Bank of Canada trades at C$269.64 today, down 0.3%. Get the latest on RY stock price movement and outlook.
- [(RY) Stock Trading Blueprint (RY:CA)](https://www.google.com/goto?url=CAESjwEBxCJF10QX37ckVuZqtz6nuyWwtOtG6cQyaJZYH-tQFu0TuZox_7pGDedimjtXv53Wd26NGUD_wq-2dkkM7O_KfXAQcWqtVtZ61rraeKCbKZ1lnwY1dJxatf71irPnKMvgNOYdXjSY4zmvofC5Pwq67xDNtLY2ibOvPuTJATHFwL4gKQJJVQXHErAkFrsS1Q&gsessionid=qeDWZ7xxUau9c6_Npsk4Kg-8MCMnwjuN2I1rGWSVaj5PSM5HkJB0vg)  
  <sub>Stock Traders Daily, 16 hours ago</sub>  
  Stock Trading Blueprint for Royal Bank of Canada (RY) with Key Buy and Sell Indicators.
- [RY Dec 2026 290.000 call (RY261218C00290000) stock price, news, quote and history](https://www.google.com/goto?url=CAEScAHEIkXXu6Aye852Uqm2-aW7yo9TNvB3VdwljJ4EeO3jP5_F5gSznAj5jelLy5TFvzKG6NW1QfvMzptjJ-QWqjoknhnDzniQRv1tglhuUun3sC_S9Wu_PPT9iTAva6DOSZoxhQQ9WEc4fevDeLQNeVk&gsessionid=qeDWZ7xxUau9c6_Npsk4Kg-8MCMnwjuN2I1rGWSVaj5PSM5HkJB0vg)  
  <sub>Yahoo Finance UK, 10 hours ago</sub>  
  Find the latest RY Dec 2026 290.000 call (RY261218C00290000) stock quote, history, news and other vital information to help you with your stock trading and...
- [New Analyst Forecast: $RY Given $294 Price Target](https://www.google.com/goto?url=CAESkwEBxCJF116CTB_kimTfKwKRZM33q7JDlAk6SxWBVy55lcvNfIYqHuYYKkNdJTuZxi8vO_vQAq43VmtEGVQ9r_Wz1r2562WQ18PqplZZNaxb91xhdnCSepO5lsYTcedhMOobaZXVN6j_EbofGw1U28XCd8V2O3ZO4Th1jimqsscaETfYvV5gRQCcCYgYjKjax43K1Ok&gsessionid=qeDWZ7xxUau9c6_Npsk4Kg-8MCMnwjuN2I1rGWSVaj5PSM5HkJB0vg)  
  <sub>Quiver Quantitative, 18 hours ago</sub>  
  We just received data on a new analyst forecast for $RY. Paul Holden from CIBC set a price target of.
- [Why Did Royal Bank of Canada (TSX:RY) Fall 0.24% on November 24, 2026?](https://www.google.com/goto?url=CAESnAEBxCJF165rANuiz6_bi3dIF-wikK7pnCi_j0puiCmvlnhlL0LJodHiRJZ_m0SBZCFle4U0yr45l0xREAfnX5iikApysFhqmtguTue02MIypednUZUu3Tb4f6ttzwMeZP25JzBIMvO4EztQFOTxhoYeyMt0XE1jp87kaGlnpD6Adw-epkkT07-AjD3thWz5T8jaco4adRvmokDf7rA&gsessionid=qeDWZ7xxUau9c6_Npsk4Kg-8MCMnwjuN2I1rGWSVaj5PSM5HkJB0vg)  
  <sub>kalkine.ca, 3 hours ago</sub>  
  You are reading a free article with opinions that may differ from the recommendation given by Kalkine in its paid research reports.
- [Royal Bank of Canada (TSE:RY) Stock Price Target Lowered at Jefferies Financial Group](https://www.google.com/goto?url=CAESzQEBxCJF1ywlE7IwuPano6BaSb7geEHuJAN7AUIPaDMnQY9o75JNVuRifBrh0PJvDNKVvlADXqz6UjjUcCXza3URmggr2A_68h5LxtROzDou2-RXzh4n8xjYQlsMZYiIzc6dF1jnH78l8zlyfocd73QG8f-hwfhLxh9-K2s6l2iOnDjeKrIkVcQC3ATXrGFr-ZVpezuH_nsXBCZf98VaqOJVdIvDP8UdQyGCAwMstBxpIRGjhWW-ICGDbVh64OTIq1hQlPEyMHzbWO8cxbdA&gsessionid=qeDWZ7xxUau9c6_Npsk4Kg-8MCMnwjuN2I1rGWSVaj5PSM5HkJB0vg)  
  <sub>MarketBeat, 18 hours ago</sub>  
  Jefferies Financial Group cut their target price on shares of Royal Bank of Canada from C$271.00 to C$269.00 and set a "hold" rating for the company in a...
- [Market Outlook: Which Canadian Stocks Could Outperform Before Year-End?](https://www.google.com/goto?url=CAES1wEBxCJF14p7gH89IjfLrM88QNaAixNUJI2T6kXeteQZnPIeBa9Nj-C2VlZAD0ythqJt2434nTyxWQPMgIh76mRu2Qv8ad761jkqH3KkV33IjlMhaxmwCubg7Y1yZHD4SGYN4D__35jGGqcX0curBq9fWegFuq9LUFjxpO2Fg1rKsMri-T18pqF97ylPh5UpB9iqyXYvrr_Yl8tavFo6v2QtbmrAzcGAHBKqrS_Of4ZbffERkS6xX2GdLXDjyMrUHyQsMEb003vg8J748hsRScSDeULDs-2sZA&gsessionid=qeDWZ7xxUau9c6_Npsk4Kg-8MCMnwjuN2I1rGWSVaj5PSM5HkJB0vg)  
  <sub>The Globe and Mail, 8 hours ago</sub>  
  (About StockTargetAdvisor.com (STA Research) is a Canadian investment research company specializing in advanced stock research and analysis).
- [RY Dec 2026 175.000 call (RY261218C00175000) stock price, news, quote and history](https://www.google.com/goto?url=CAEScAHEIkXXtnYsYgn7yb1FKAsAGQ2OUuRQ_Rngz1D2TOH5oLMel1JsulyIdXYlwtethdsmMAIDtrRei7S9MyCygiMSPEa3BRKHkMhWjLzVPfLZFvzi9lWAfeEaWQVagzvAbBIw5QeGrSIvbdU9rIbPfHw&gsessionid=qeDWZ7xxUau9c6_Npsk4Kg-8MCMnwjuN2I1rGWSVaj5PSM5HkJB0vg)  
  <sub>Yahoo Finance UK, 10 hours ago</sub>  
  Find the latest RY Dec 2026 175.000 call (RY261218C00175000) stock quote, history, news and other vital information to help you with your stock trading and...
- [Royal Bank vs. a Canadian Bank ETF: Which Would I Choose for My First $10,000?](https://www.google.com/goto?url=CAESpAEBxCJF10C5DLq3ECFMiBahNFQoACssylVVghkCDRIhF2zxucwqylSZkBhER57GYNGtaqEjYJO0OkIwxSaxtlqLm11Nt874GK0ErMJGCDxsfxsXUuMqONqwiSJrCpDnKxb830f47Nlb3JnUtVoiSsL9t_XmVK1fK89WUwhioHRweEiSQKnhavSORiKHOa2Xm2-Y7v5FITJdC0XbO-th-KJPYHYzuw&gsessionid=qeDWZ7xxUau9c6_Npsk4Kg-8MCMnwjuN2I1rGWSVaj5PSM5HkJB0vg)  
  <sub>The Motley Fool Canada, 13 hours ago</sub>  
  Royal Bank offers a strong business, while ZEB spreads a first bank allocation across six lenders for a modest fee.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>Price and chart</b> — score n/a</summary>

```text
Last close 186.12 (bar of 2026-11-25), from 502 daily bars
Trend: vs 20d SMA 198.39 (-6.2%), 50d 198.51 (-6.2%), 200d 191.77 (-2.9%); 50d above 200d
Momentum: RSI(14) 34.7 | MACD -3.761 vs signal -2.009 (histogram -1.751)
Returns: 1d -1.6% | 5d -2.1% | 1m -8.3% | 3m -9.0%
52-week range: 152.22 - 217.87 (now 51.6% of the way up)
Volatility: ATR(14) 3.84 (2.1% of price) | annualised 20d 26.4%
Volume: 0.03x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score n/a</summary>

```text
Sector: Financial Services / Banks - Diversified | market cap 257.67B
Valuation: trailing P/E 16.27 | forward P/E 14.61 | P/B 2.70 | PEG 1.76
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
Price target: mean 209.44 (+12.5% vs last close), range 182.80 - 230.36
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

- [multiQure Announces Agreement to Access Apertura Gene Therapy's TfR1 CapX(TM), A Next-Generation Blood-Brain Barrier-Crossing Capsid](https://www.tradingview.com/news/acceswire:4fee60695094b:0-multiqure-announces-agreement-to-access-apertura-gene-therapy-s-tfr1-capx-tm-a-next-generation-blood-brain-barrier-crossing-capsid/)  
  <sub>TradingView, 2 hours ago</sub>  
  WARSAW, PL AND NEW YORK, NY / ACCESS Newswire / November 25, 2026 / multiQure S.A. (WSE:MQR), a Warsaw Stock Exchange-listed biotechnology company...
- [374Water Clears Second Factory Acceptance Test at 59% Above Accepted Capacity; AirSCWO(TM) System Ships to Orange County Sanitation District Next Week](https://finance.yahoo.com/technology/articles/374water-clears-second-factory-acceptance-130500007.html)  
  <sub>Yahoo Finance, 2 hours ago</sub>  
  Upgraded AirSCWO 6 processed an average of 5.2 tons per day of municipal biosolids over 48 hours with sustained throughput of up to 5.
- [Form 4 IES Holdings Inc: Jeffrey L. ET AL Gendell (Director, 10% Owner, Executive Chairman) For: 20 November](https://www.google.com/goto?url=CAES3QEBxCJF1x1CLggCVbwjTgJNBWlNyYlxQq4JS-ai7ER3AXZ9mgE4r0Kjy5WwaVbcvbWdXt5vbYXH0uQ1X0AeI6suNTqxdZTBALT7PAN-cGyGK3L5uNtuQjBVAbJSWZhWwBfwq5PBw6VcJ23jl_LqeaaMX25yPQQoRxv1wNGziWrGBPDh9YMfL3nHoY-AKFHLd-290A2oq0ePoyCMckv52JCyGE0W8N3ZHyd60ar4UevOT-bf_8BcmbnvnPUNm6FQ7JPpA5SMuw6f0YmplQ0InmhinMmYImbrGP4OTqR2Eg&gsessionid=eWu4PvYx4Tdkj6Z-IJ0TJtxtSQg3oSlGsWsnqwBh8kcod5QmC23QXQ)  
  <sub>Investing.com Nigeria, 9 hours ago</sub>  
  FORM 4, UNITED STATES SECURITIES AND EXCHANGE COMMISSION Washington, D.C. 20549. STATEMENT OF CHANGES IN BENEFICIAL OWNERSHIP
- [One utility moves over 500 tons of wet biosolids daily. 374Water's system is expected to ship next week.](https://www.google.com/goto?url=CAEStQEBxCJF1xNE2bhTd9x2yAEDC407HqaziILorURDxz5CbrDbH03P6pwk5A4b57PD921NeufrNK7SOdae93H1inxqmgNHR1zhLs3CEDy5S5r4_z2yiT4rPjaeVxBhdPYotkhL3IuJg-QNNkoSYyarVMK9mS1XXlqBn2mvVf7c_r04xDH2vEi_1NcfuNz9nyCLo0Rnui1YRghPBwou81pcJqCxfdH4qXCNnygpkvYkMzSTxIwTkcjO&gsessionid=eWu4PvYx4Tdkj6Z-IJ0TJtxtSQg3oSlGsWsnqwBh8kcod5QmC23QXQ)  
  <sub>Stock Titan, 2 hours ago</sub>  
  374Water (SCWO) completed a second factory acceptance test of its upgraded AirSCWO 6 system for the Orange County Sanitation District.
- [Virtuix Holdings (VTIX) CFO McGinnis bought 20,000 shares for $7,378 at $0.37](https://www.google.com/goto?url=CAESowEBxCJF12WC6Py8_HAhBsmpYxnbqCwrqvLdQBTSDHdPi7cgYgGZMredlcvPAXKbE5yDd7F42zaBpaHWduKnU3djs21azAvWb8TypCgPX9NQjZ_jR5v_0Gdp7m-C7XbLozO4sqmuceVQi5JkiL-oCpx3Rm3ctH7Sf18z4g6Jqif7yIKrhs4nWR8VFkCLhM1dLFbmwcUC1AlapVpZFpjMuVNBpgfI&gsessionid=eWu4PvYx4Tdkj6Z-IJ0TJtxtSQg3oSlGsWsnqwBh8kcod5QmC23QXQ)  
  <sub>Quantisnow, 13 hours ago</sub>  
  Thomas Lynn McGinnis (Chief Financial Officer at Virtuix Holdings Inc., VTIX) reported that they bought 20000 shares for $7378 at $0.37 on Nov 24, 2026.
- [(HBND) Market Dynamics and Trading Signals (HBND:CA)](https://www.google.com/goto?url=CAESnQEBxCJF11EF9DwuYQg7nqh6RvLq-xC1sKNiEvWYIbR1LelO2qVWVFvxKEwdcw574yiknFFrrpJ1ZIJXFSHDuNr2i_ixpKKzzGeYGdmHKUeTenS9xxNuZTBxYOdM-xuvGP51suAHbFoHeeS5wHotlgylOxd--fzRt5q-hHJH3GmsNv-KwxSOc5FKEgi2xnOy03EOkCLmOqduGwWv7jFL&gsessionid=eWu4PvYx4Tdkj6Z-IJ0TJtxtSQg3oSlGsWsnqwBh8kcod5QmC23QXQ)  
  <sub>Stock Traders Daily, 4 hours ago</sub>  
  Market Dynamics Report for Hamilton U.S. Bond YIELD MAXIMIZER TM ETF (HBND) Featuring Key Trading Signals.
- [TM 3Q PATAMI Slips To RM494 Million, Declares 10 Sen Dividend](https://www.google.com/goto?url=CAESpAEBxCJF123vcsxhhxIGhqzFpC_ujb34G2e7TFH1Y0rOCsppgRUXqFwZ-wTyToDmsVuxpVDF0RJ70IyxfKU9grdxKCKrH3IY0KFgWN8tmA__k8CBFXV-n9cIS5DR5eup-1OjcdCPYxILOGrmA4URrPewseMX1Iw42FC8H-xgpSa0H8hJHaqZKJK3kCt7W9scQIQ7iNN-WzptR-lHOnqgA-2t8Qw_1g&gsessionid=eWu4PvYx4Tdkj6Z-IJ0TJtxtSQg3oSlGsWsnqwBh8kcod5QmC23QXQ)  
  <sub>BusinessToday Malaysia, 5 hours ago</sub>  
  Telekom Malaysia Bhd (TM) recorded a 20.8% year-on-year decline in net profit to RM1.18 billion for the nine months ended September 30, 2026 (9M2026),...
- [TM's 3Q net profit falls 28% on absence of one-off gain, declares 10 sen dividend](https://www.google.com/goto?url=CAESYgHEIkXXpPewWJJPep1imvosGLIj2KkEWxqdApn0Ri5lyi7pSj9k_DbahALSWkFg9ii0C89KV340b41kbE3wZAfOFnXPTygItZ6f5dWMNLVK0zbm4ora_QFKmzrsY0aAV293&gsessionid=eWu4PvYx4Tdkj6Z-IJ0TJtxtSQg3oSlGsWsnqwBh8kcod5QmC23QXQ)  
  <sub>The Edge Malaysia, 4 hours ago</sub>  
  Telekom Malaysia Bhd's (KL:TM) third-quarter net profit fell 28%, largely due to the absence of a one-off investment gain recognised a year earlier and...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>Price and chart</b> — score n/a</summary>

```text
Last close 213.79 (bar of 2026-11-25), from 502 daily bars
Trend: vs 20d SMA 208.74 (+2.4%), 50d 197.54 (+8.2%), 200d 196.89 (+8.6%); 50d above 200d
Momentum: RSI(14) 60.2 | MACD 4.148 vs signal 4.708 (histogram -0.560)
Returns: 1d +1.8% | 5d +1.7% | 1m +8.8% | 3m +11.3%
52-week range: 166.50 - 248.29 (now 57.8% of the way up)
Volatility: ATR(14) 4.50 (2.1% of price) | annualised 20d 40.1%
Volume: 0.06x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score n/a</summary>

```text
Sector: Consumer Cyclical / Auto Manufacturers | market cap 250.90B
Valuation: trailing P/E 9.75 | forward P/E 13.55 | P/B 17.02 | PEG 19.39
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

- [Chevron Pays a Bigger Dividend, but Exxon May Be the Better Retirement Stock](https://finance.yahoo.com/markets/stocks/articles/chevron-pays-bigger-dividend-exxon-131755842.html)  
  <sub>Yahoo Finance, 1 hour ago</sub>  
  Exxon beats Chevron for retirees who want a dividend that keeps growing, with 44 straight annual raises against Chevron's 39. Exxon kept raising its payout...
- [Exxon Mobil stock tests support at $156.92 amid sell pressure: weekly analysis](https://www.google.com/goto?url=CAESkAEBxCJF124q_vLGzRS1VvbNd8m5n3rYWQKVx_kZciv-YeDY78EoLoRcCkk1qVMfUzvhfxdr0rfBXczRK-vA30sPft9Sxi11Ym6KckMo7xsSUzM_ZfaJXg3buZPurdTY_bfQxnfoxKD9WbP7cMdfH9UYIRIYw5HECOmkaCSwKVrs2oYfMquZgaPZe-cEBc-LjZo&gsessionid=m2JOpnRe7cTqpsDVw6K1TPt01rwMmwGbrGhpmmKoIyjgBpQ_F5iuLA)  
  <sub>Traders Union, 31 minutes ago</sub>  
  Shares of Exxon Mobil Corporation (XOM) are trading near $158 as the stock slips further into oversold territory this week. Daily technical signals remain...
- ['Exxon Got Walloped': $340 Million Legal Blow Paves The Way For More](https://www.google.com/goto?url=CAESiQEBxCJF17yvu5Zvm7Dsl7_3KWfxXSUAuJRJokZ5tTGiT3rY_82i0rE7Jta9aih65amPUjjRxbExjMF76jjaaXpw4aW9MBkpHDoaeM_FO89zbAU5tO6ROnBQlVhadH41fVR2BYOmt_LMtPANI0lMEwjCo2V_7TZILs865lJTDme5sD61fcpVv0ZAPg&gsessionid=m2JOpnRe7cTqpsDVw6K1TPt01rwMmwGbrGhpmmKoIyjgBpQ_F5iuLA)  
  <sub>Investor's Business Daily, 21 hours ago</sub>  
  ExxonMobil faces a $339.56 million fine plus legal fees over sludge that's "continuously seeped" in northwest Louisiana for half a century.
- [ExxonMobil (NYSE:XOM) Stock Sale Revealed by Rep. Harriet M. Hageman](https://www.google.com/goto?url=CAESugEBxCJF1_xc0zSd4FsrK4ZoAksutCCcPTS9UBXdnV6ycTUv148MmPf8N7Bg_H4Q7nZC4YZmOhFD6xUOxAPHnR11ry8EevrGaSpfdsPXKADKNlytx7BQtyndiYkluF-AoLqeLxB9DZXZ_aO1pDTkLrWYyNc3BAvt7BMoPrDiueHbuM-3FnMWTYtPharMfW7Y0r510N0NJl9hYk94OStZvkGvH4FNO4kxaCm6wvu77gnzz0Rq7L29DZAMvh0&gsessionid=m2JOpnRe7cTqpsDVw6K1TPt01rwMmwGbrGhpmmKoIyjgBpQ_F5iuLA)  
  <sub>MarketBeat, 8 hours ago</sub>  
  Representative Harriet M. Hageman (Republican-Wyoming) recently sold shares of ExxonMobil Corporation (NYSE:XOM). In a filing disclosed on November 23rd,...
- [XOM Nov 2026 167.500 put (XOM261127P00167500) stock price, news, quote and history](https://www.google.com/goto?url=CAEScQHEIkXXX0XxG8LIea_-ZbJF1HdkadytJ9OHbOuiHfuwTu5IHm8V69sMdgkyGDI0EsPQGrah9FzgfoaZjxK_Jxuj42ChrZG6oxpL-xn9fGRz8wv2VOvnGaMNIntleXDSMsl_f3f4ZN-4OtK4FJ4oZYFB&gsessionid=m2JOpnRe7cTqpsDVw6K1TPt01rwMmwGbrGhpmmKoIyjgBpQ_F5iuLA)  
  <sub>Yahoo Finance UK, 9 hours ago</sub>  
  Find the latest XOM Nov 2026 167.500 put (XOM261127P00167500) stock quote, history, news and other vital information to help you with your stock trading and...
- [Can Exxon Mobil sustain gains as lower debt and flexible allocation shape shareholder returns?](https://www.google.com/goto?url=CAEShwEBxCJF1yQy2A5RoVBscfqorDf0aBwaDwUKktb1W2zOZlTOBGbJb-O0Z5b2QJdrRi0C-XjiBrfacpnTZ8MzjPBHmMcBy1C4t2Z3zIDSNPVms7bn27tN4r0DwVk4tGnMOO5C1_vYQta5D31IZ6a3UIDEsqKTewldk3Tq2hwHTnjI-8jyeRzm4jM&gsessionid=m2JOpnRe7cTqpsDVw6K1TPt01rwMmwGbrGhpmmKoIyjgBpQ_F5iuLA)  
  <sub>Traders Union, 17 hours ago</sub>  
  Exxon Mobil (XOM) stock is trading higher, with recent balance sheet actions bringing attention to its funding flexibility and shareholder value.
- [Short-Term Bond Funds vs. Dividend Stocks: Which Income Holds Up Better for Retirees?](https://www.google.com/goto?url=CAESuQEBxCJF16QB6_BA1l-LyVGLenCbrb57T02mv0GQggPFADGhMnJ9oeWhDCDz-Le8YQk2DRbBX3wtFtm588oGAyaoCcYkPioG9CLWWrkfK0R_zl22AzUS5rjmmYfmNVJI57B07KM4qxkpoDoV7w6k3PGq2ZTMQX3gDGDbvSpNLSdVUAfQeufpMEVPsSr-i-g5b3U3GUCT2dCT2Wb1xDj41jwf-MamubuY7_Bm_M7PTIjbKHupP87wlX9uJg&gsessionid=m2JOpnRe7cTqpsDVw6K1TPt01rwMmwGbrGhpmmKoIyjgBpQ_F5iuLA)  
  <sub>24/7 Wall St., 20 hours ago</sub>  
  Treasury bills maturing in 0 to 3 months, the paper held inside iShares 0-3 Month Treasury Bond ETF (NYSEARCA:SGOV), carried an average yield of 4.11% on...
- [EP Wealth Advisors LLC Buys 956,158 Shares of ExxonMobil Corporation $XOM](https://www.google.com/goto?url=CAESwAEBxCJF18NxlkLh26ZiP1PjcylgID7-QpmouwZg65RviIldkJDISY3CGCkh8etYHnPeCmmX8AxZ8uEUjNjedeIKABjL6Awf_lmrnCK-Lg8e0uaFeQpjjBbtEXDRTQ93cwXMSbVmYyl5NSCwjQ_nRqGydBqSgIxygbqN90oCHR_MjPBL-0eJDqxC0cFNE3ZuShULiztf80i_DvaejDqjoovqjolkCaqrcupHSJnp7OQlXZKyzBp78q6wdO9L5mK6ZBM&gsessionid=m2JOpnRe7cTqpsDVw6K1TPt01rwMmwGbrGhpmmKoIyjgBpQ_F5iuLA)  
  <sub>MarketBeat, 5 hours ago</sub>  
  EP Wealth Advisors LLC purchased a new stake in shares of ExxonMobil Corporation (NYSE:XOM - Free Report) during the third quarter, according to the company...
- [XOM Dec 2026 155.000 call (XOM261224C00155000) stock price, news, quote and history](https://www.google.com/goto?url=CAEScQHEIkXXLrMa1YthnOY_ekseLBHPpEjh2nZZifGvlqVMFCxymZcV_NKgClTLYiqAlrDlJue0I0hUYpjwmbM8Lxv5Oziqgw9f73FbpevJha1127tqaQ-SuSOIH17i7cKfZsbdMkWi3_k_6V4tBaFKTtmM&gsessionid=m2JOpnRe7cTqpsDVw6K1TPt01rwMmwGbrGhpmmKoIyjgBpQ_F5iuLA)  
  <sub>Yahoo Finance UK, 15 hours ago</sub>  
  Find the latest XOM Dec 2026 155.000 call (XOM261224C00155000) stock quote, history, news and other vital information to help you with your stock trading...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>Price and chart</b> — score n/a</summary>

```text
Last close 158.14 (bar of 2026-11-25), from 502 daily bars
Trend: vs 20d SMA 167.56 (-5.6%), 50d 168.85 (-6.3%), 200d 156.95 (+0.8%); 50d above 200d
Momentum: RSI(14) 35.6 | MACD -3.834 vs signal -2.480 (histogram -1.353)
Returns: 1d -0.1% | 5d -1.5% | 1m -12.1% | 3m +1.1%
52-week range: 114.51 - 187.25 (now 60.0% of the way up)
Volatility: ATR(14) 3.85 (2.4% of price) | annualised 20d 31.1%
Volume: 0.06x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score n/a</summary>

```text
Sector: Energy / Oil & Gas Integrated | market cap 645.09B
Valuation: trailing P/E 16.27 | forward P/E 12.67 | P/B 2.43 | PEG 1.24
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
Price target: mean 184.18 (+16.5% vs last close), range 160.00 - 213.00
Recent rating changes:
  - 2026-11-12 Bernstein: main, Outperform -> Outperform
  - 2026-11-07 Freedom Broker: main, Hold -> Hold
  - 2026-11-04 Citigroup: main, Neutral -> Neutral
  - 2026-11-04 TD Cowen: main, Buy -> Buy
  - 2026-11-02 UBS: main, Buy -> Buy
  - 2026-11-02 Morgan Stanley: main, Overweight -> Overweight
Institutional ownership: 67.2%
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

> No material macro surprise, technicals lack decisive break on volume, flows flat, fundamentals neutral.

**Main reasons it gave:**
- Price 26.24 below 20‑day SMA (26.38), 50‑day SMA (27.49) and 200‑day SMA (27.42)
- RSI 35.5 (oversold) with volume 0.02× 20‑day average
- Fund flows flat: share count change +0.0% over 1 week and 1 month
- Yield 3.4% with expense ratio 0.85% and 47.9% cash allocation
- Macro: VIX 31.72 (+7.2 on week) indicating stressed market, no rate or data surprise

<details><summary><b>News</b> — score +0.00</summary>

_No news found for this one today._

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.16% (+0.01 on the week) | 5-year 4.62% (-0.26 on the week) | 10-year 4.83% (-0.24 on the week) | 30-year 5.24% (-0.17 on the week)
Yield curve, 10-year minus 3-month: +0.67 points -- upward sloping (normal)
US dollar index: 103.93 (+0.07 on the week)
Volatility (VIX): 31.72 (+7.2 on the week) -- stressed
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.1% (2026-10-01) | jobless claims 189k (2026-11-21)
Policy and expectations: Fed target 4.00% | market expects 2.1% inflation over 10 years
Rate path: 2-year Treasury 4.63% vs Fed target 3.75-4.00% -- the bond market prices about 3 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 26.24 (bar of 2026-11-25), from 502 daily bars
Trend: vs 20d SMA 26.38 (-0.5%), 50d 27.49 (-4.5%), 200d 27.42 (-4.3%); 50d above 200d
Momentum: RSI(14) 35.5 | MACD -0.373 vs signal -0.433 (histogram 0.060)
Returns: 1d -0.2% | 5d +0.8% | 1m -4.2% | 3m -9.0%
52-week range: 25.44 - 29.49 (now 19.8% of the way up)
Volatility: ATR(14) 0.23 (0.9% of price) | annualised 20d 10.0%
Volume: 0.02x the 20-day average
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
Three-year record: +10.3% a year | beta to the market 0.37
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
Share count change: 1 week: +0.0% (0.00) over 7d | 1 month: +0.0% (0.00) over 32d
Shares outstanding: 27.60M | fund size: 724.22M
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Commodities basket (DBC) · Index fund — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Neutral overall: positive fund inflows (+16.1% in 1 month) suggest demand, but bearish fundamentals (inventory builds and EIA price forecasts) offset the bullish flow. Technicals show oversold RSI but very low volume, providing no decisive signal. No macro surprise or policy shift observed.

**Main reasons it gave:**
- Fund inflows +16.1% over past month (money coming in)
- Crude inventories +3.4M barrels (build) and natural gas +20 BCF (build) – bearish
- EIA forecasts WTI price down 13% over six months – bearish
- RSI 19.7 (oversold) with volume 0.02× 20‑day average – weak technical signal

<details><summary><b>News</b> — score +0.00</summary>

_No news found for this one today._

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.16% (+0.01 on the week) | 5-year 4.62% (-0.26 on the week) | 10-year 4.83% (-0.24 on the week) | 30-year 5.24% (-0.17 on the week)
Yield curve, 10-year minus 3-month: +0.67 points -- upward sloping (normal)
US dollar index: 103.93 (+0.07 on the week)
Volatility (VIX): 31.72 (+7.2 on the week) -- stressed
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.1% (2026-10-01) | jobless claims 189k (2026-11-21)
Policy and expectations: Fed target 4.00% | market expects 2.1% inflation over 10 years
Rate path: 2-year Treasury 4.63% vs Fed target 3.75-4.00% -- the bond market prices about 3 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 28.92 (bar of 2026-11-25), from 502 daily bars
Trend: vs 20d SMA 30.84 (-6.2%), 50d 32.18 (-10.1%), 200d 29.81 (-3.0%); 50d above 200d
Momentum: RSI(14) 19.7 | MACD -0.979 vs signal -0.791 (histogram -0.188)
Returns: 1d -0.4% | 5d -2.0% | 1m -13.9% | 3m -6.3%
52-week range: 22.36 - 34.10 (now 55.9% of the way up)
Volatility: ATR(14) 0.46 (1.6% of price) | annualised 20d 18.9%
Volume: 0.02x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score -0.25</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score -0.25</summary>

```text
Fund type: Commodities Broad Basket
What it holds: P/E n/a | P/B 0.00 | P/S 0.00 | 3y earnings growth n/a
Yield: 2.2%
Three-year record: +11.2% a year | beta to the market 1.04
Cost and size: expense ratio 0.85% | net assets 1.94B
What it is made of: Other 50.0%, Cash 45.2%, Bonds 2.7%, Stocks 2.1%
Largest holdings: Invesco Shrt-Trm Inv Gov&Agcy Instl 41.8%, Brent Crude Future Jan 27 11.0%, Invesco Short Term Treasury ETF 5.8%, Mini Ibovespa Future Dec 26 2.1%
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
US inventories, week ending 2026-11-13 (published the following Wednesday)
  Crude oil: 417.8 million barrels, +3.4 on the week (a build), 25% percentile over 52 weeks
  Natural gas: 3,882.0 billion cubic feet, +20.0 on the week (a build), 96% percentile over 52 weeks -- high for the time of year
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
Share count change: 1 week: +5.6% (101.44M) over 8d | 1 month: +16.1% (266.97M) over 33d
Shares outstanding: 66.64M | fund size: 1.93B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Developing country bonds (EMB) · Index fund — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> EMB shows mixed signals. Technicals are bearish – price (90.26) sits below the 20‑day, 50‑day and 200‑day SMAs, MACD is negative and RSI is only mildly oversold (39.2). However, fund flows are strongly positive (+6.1% share count, 783.57 M over the past month), indicating demand for EM‑bond exposure. Recent news highlights emerging‑market equities entering a bear market because of Fed hikes and a strong dollar, which could pressure EM issuers and dampen sentiment for EM bonds. Macro data show no surprise (Fed target unchanged, yields slightly lower, VIX higher), so there is no clear policy or data catalyst. With bearish technicals offset by positive inflows and no decisive macro trigger, a neutral outlook is appropriate.

**Main reasons it gave:**
- Price 90.26 below 20‑day SMA 91.34, 50‑day SMA 91.52 and 200‑day SMA 94.49
- RSI (14) at 39.2, indicating mild oversold condition
- Fund inflows +6.1% share count (783.57 M) over past month
- Emerging‑market stocks entered bear market per news, citing Fed hikes and strong dollar

<details><summary><b>News</b> — score -0.20</summary>

- [Emerging Market Stocks 2026: Bear Market, Fed Hikes & Dollar](https://intellectia.ai/blog/emerging-market-stocks-bear-market-fed-hike-strong-dollar-2027-guide)  
  <sub>Intellectia AI, 22 hours ago</sub>  
  Emerging market stocks fell into a bear market in November 2026. See how Fed hikes, a strong dollar and AI chip exposure hit EM, and how to invest for 2027.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score -0.20</summary>

```text
US Treasury yields: 3-month 4.16% (+0.01 on the week) | 5-year 4.62% (-0.26 on the week) | 10-year 4.83% (-0.24 on the week) | 30-year 5.24% (-0.17 on the week)
Yield curve, 10-year minus 3-month: +0.67 points -- upward sloping (normal)
US dollar index: 103.93 (+0.07 on the week)
Volatility (VIX): 31.72 (+7.2 on the week) -- stressed
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.1% (2026-10-01) | jobless claims 189k (2026-11-21)
Policy and expectations: Fed target 4.00% | market expects 2.1% inflation over 10 years
Rate path: 2-year Treasury 4.63% vs Fed target 3.75-4.00% -- the bond market prices about 3 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score -0.30</summary>

```text
Last close 90.26 (bar of 2026-11-25), from 502 daily bars
Trend: vs 20d SMA 91.34 (-1.2%), 50d 91.52 (-1.4%), 200d 94.49 (-4.5%); 50d below 200d
Momentum: RSI(14) 39.2 | MACD -0.418 vs signal -0.299 (histogram -0.118)
Returns: 1d -0.1% | 5d -0.6% | 1m -1.8% | 3m -5.1%
52-week range: 89.92 - 97.74 (now 4.4% of the way up)
Volatility: ATR(14) 0.49 (0.5% of price) | annualised 20d 7.8%
Volume: 0.06x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.00</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score +0.00</summary>

```text
Fund type: Emerging Markets Bond
Yield: 5.4%
Credit quality: BBB 33.9%, BB 25.6%, B 19.2%, A 17.3% | US government debt 87.8%
Three-year record: +7.6% a year | beta to the market 1.06
Cost and size: expense ratio 0.39% | net assets 13.57B
What it is made of: Bonds 99.2%, Cash 0.8%
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

<details><summary><b>Buying and selling by company insiders</b> — score +0.40</summary>

_Not available today._

</details>

<details><summary><b>Who is positioned how</b> — score +0.40</summary>

_Not available today._

</details>

<details><summary><b>Money going into and out of this fund</b> — score +0.40</summary>

```text
Direction: money coming in (1 month)
Share count change: 1 week: +0.5% (71.66M) over 7d | 1 month: +6.1% (783.57M) over 32d
Shares outstanding: 150.06M | fund size: 13.55B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### US company bonds, riskier (HYG) · Index fund — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Neutral overall as no material macro surprise, policy shift, or decisive technical break occurred. Positive inflows suggest some demand, but technicals are bearish and market stress is high.

**Main reasons it gave:**
- Net inflows: +6% share count increase over the past month
- Technical: price below 20‑day, 50‑day, and 200‑day SMAs; RSI 33.9; MACD negative
- Macro: VIX up 7.2 points to 31.7, indicating stressed market conditions
- Policy: Fed target unchanged at 4.00% and market expects ~3 quarter‑point hikes

<details><summary><b>News</b> — score +0.00</summary>

- [iShares iBoxx $ High Yield Corporate Bond ETF (HYG) options chain](https://au.finance.yahoo.com/quote/HYG/options/?date=1795737600&straddle=false&type=all)  
  <sub>Yahoo Finance Australia, 23 hours ago</sub>  
  View the basic HYG option chain and compare options of iShares iBoxx $ High Yield Corporate Bond ETF on Yahoo Finance.
- [HYGH: Rate-Hedged High-Yield Bond ETF, Good Performance, Terrible Price](https://seekingalpha.com/article/4971849-hygh-rate-hedged-high-yield-bond-etf-good-performance-terrible-price)  
  <sub>Seeking Alpha, 1 hour ago</sub>  
  The analyst prefers a simpler, cheaper high-yield bond ETF over HYGH, whose rate-hedged portfolio has a 6.5% dividend yield and a 0.52% expense ratio.
- [CDX Is The Hedge You Were Looking For, For What's About To Happen In The Markets (CDX)](https://www.google.com/goto?url=CAESsgEBxCJF1xmQTaE6JUivvEJheBl-xNsDuRjoGV6flJEwgBn-ClCPODLoM5cv5mlL8XMYVEaKJkDkJVxi90wdDdhk-D6NsiwOycC1FPMccksnitH2GmQwZlkNnPvaox9b9uxK6YXzteqlPM-wQXCPUqhe6RzJa0SypizIhvoCnDm68o6imgd5TpRfcSD6_TMNzgxqi-13urjUVxgLaotPSKDSsYMcpt_95MxI7ZFuOK2WQtF7&gsessionid=E9_tXtVkctKxbixHctaf0-yByFzqq7yC5aJRLyISe63ju3Yw3XcLtA)  
  <sub>Seeking Alpha, 19 hours ago</sub>  
  The Simplify High-Yield ETF at near-zero net spread sensitivity may help in a nervous market, though normalization may not favor returns.
- [Debt Costs With Higher Interest Rates](https://www.google.com/goto?url=CAESlwEBxCJF1_f0xo9t3AjN3yzdoHGVfcJ1f9VqUiD1ScjuTPpa9HolGwL8aOen_18t9-8Irio2Hjnp1Rj2zdXzOxR1gQnJeg57AVYQjjyU5IFmFJooNe2DrerOMsxr7Mwc1nDfmGbffXr1mUjllFo2SRAt-RIyOEccvEYkGZSK7aboW2oHuIVAcOVzcKyOtFWBbvYW3TplHzNH&gsessionid=E9_tXtVkctKxbixHctaf0-yByFzqq7yC5aJRLyISe63ju3Yw3XcLtA)  
  <sub>Seeking Alpha, 3 hours ago</sub>  
  The biggest financial problem facing the United States is the ongoing $2 trillion-plus federal deficit. We are borrowing approximately 6-7% of our annual...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.16% (+0.01 on the week) | 5-year 4.62% (-0.26 on the week) | 10-year 4.83% (-0.24 on the week) | 30-year 5.24% (-0.17 on the week)
Yield curve, 10-year minus 3-month: +0.67 points -- upward sloping (normal)
US dollar index: 103.93 (+0.07 on the week)
Volatility (VIX): 31.72 (+7.2 on the week) -- stressed
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.1% (2026-10-01) | jobless claims 189k (2026-11-21)
Policy and expectations: Fed target 4.00% | market expects 2.1% inflation over 10 years
Rate path: 2-year Treasury 4.63% vs Fed target 3.75-4.00% -- the bond market prices about 3 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score -0.30</summary>

```text
Last close 76.20 (bar of 2026-11-25), from 502 daily bars
Trend: vs 20d SMA 76.94 (-1.0%), 50d 77.23 (-1.3%), 200d 79.16 (-3.7%); 50d below 200d
Momentum: RSI(14) 33.9 | MACD -0.279 vs signal -0.217 (histogram -0.062)
Returns: 1d -0.3% | 5d -0.6% | 1m -1.8% | 3m -4.6%
52-week range: 76.20 - 81.18 (now 0.0% of the way up)
Volatility: ATR(14) 0.30 (0.4% of price) | annualised 20d 5.0%
Volume: 0.10x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score -0.20</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score -0.20</summary>

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

<details><summary><b>Buying and selling by company insiders</b> — score +0.40</summary>

_Not available today._

</details>

<details><summary><b>Who is positioned how</b> — score +0.40</summary>

_Not available today._

</details>

<details><summary><b>Money going into and out of this fund</b> — score +0.40</summary>

```text
Direction: money coming in (1 month)
Share count change: 1 week: +0.5% (80.38M) over 8d | 1 month: +6.0% (991.55M) over 33d
Shares outstanding: 231.30M | fund size: 17.63B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### US government bonds, 7-10 years (IEF) · Index fund — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> No material macro surprise, modest bearish positioning, stable fundamentals, and neutral technicals.

**Main reasons it gave:**
- Large speculators net short 39.7% of open interest, down 2% week-over-week (POSITIONING)
- Fund fundamentals stable: AA credit quality, 4.0% yield, low expense ratio (FUND BASICS)
- Technical indicators: price above 20‑day and 50‑day SMA but below 200‑day SMA, RSI 66, modest momentum (TECHNICALS)
- Macro: 10‑year yield slipped 0.24% this week, VIX rose to 31.72, no policy surprise (MACRO)

<details><summary><b>News</b> — score +0.00</summary>

- [IEF Nov 2026 77.000 call (IEF261116C00077000) stock price, news, quote and history](https://uk.finance.yahoo.com/quote/IEF261116C00077000/)  
  <sub>Yahoo Finance UK, 16 hours ago</sub>  
  Find the latest IEF Nov 2026 77.000 call (IEF261116C00077000) stock quote, history, news and other vital information to help you with your stock trading and...
- [Top Tokenized ETFs by Market Cap](https://www.coingecko.com/en/etfs)  
  <sub>Coingecko, 13 hours ago</sub>  
  Discover the top ETFs (exchange-traded funds) by tokenized market cap. Track ETF prices alongside their tokenized prices, market cap,...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.16% (+0.01 on the week) | 5-year 4.62% (-0.26 on the week) | 10-year 4.83% (-0.24 on the week) | 30-year 5.24% (-0.17 on the week)
Yield curve, 10-year minus 3-month: +0.67 points -- upward sloping (normal)
US dollar index: 103.93 (+0.07 on the week)
Volatility (VIX): 31.72 (+7.2 on the week) -- stressed
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.1% (2026-10-01) | jobless claims 189k (2026-11-21)
Policy and expectations: Fed target 4.00% | market expects 2.1% inflation over 10 years
Rate path: 2-year Treasury 4.63% vs Fed target 3.75-4.00% -- the bond market prices about 3 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 92.33 (bar of 2026-11-25), from 502 daily bars
Trend: vs 20d SMA 91.23 (+1.2%), 50d 90.54 (+2.0%), 200d 93.44 (-1.2%); 50d below 200d
Momentum: RSI(14) 66.2 | MACD 0.231 vs signal 0.117 (histogram 0.114)
Returns: 1d +0.8% | 5d +1.8% | 1m +1.4% | 3m -1.0%
52-week range: 88.92 - 97.99 (now 37.6% of the way up)
Volatility: ATR(14) 0.50 (0.5% of price) | annualised 20d 7.3%
Volume: 0.09x the 20-day average
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
Share count change: 1 week: -1.8% (-782.03M) over 8d | 1 month: +3.1% (1.33B) over 33d
Shares outstanding: 475.14M | fund size: 43.87B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### US small companies (IWM) · Index fund — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:** no explanation. It wrote only “NEUTRAL”, so the main reasons below are all it gave.

**Main reasons it gave:**
- No macro data surprise (inflation 3.7% in line with expectations)
- Technical indicators show IWM below 20‑day, 50‑day, 200‑day SMAs with RSI 38.5, but no decisive break on volume
- CFTC positioning shows net short 9.2% with a modest increase of +0.9% OI
- Analyst coverage thin (1.9% of fund) despite 100% buy rating and +22% price target
- Fund fundamentals moderate (P/E 16.28, 3‑year return +15.5%/yr, low expense ratio 0.19%)

<details><summary><b>News</b> — score +0.00</summary>

- [Opinion: What the options market says to do with Nvidia’s stock — and the rest of the stock market](https://www.marketwatch.com/story/what-the-options-market-says-to-do-with-nvidias-stock-and-the-rest-of-the-stock-market-de9584ae)  
  <sub>MarketWatch, 2 hours ago</sub>  
  The put-call ratio is sending a strong message about Nvidia's stock, and history suggests a post-Thanksgiving “bull spread” strategy for the Russell 2000...
- [Exchange-Traded Funds, US Equities Mixed After Midday](https://news.futunn.com/en/post/1005507863/exchange-traded-funds-us-equities-mixed-after-midday)  
  <sub>富途牛牛, 13 hours ago</sub>  
  BroadMarket IndicatorsBroad-market exchange-traded fund IWM rose while IVV fell. Actively traded Invesco QQQ Trust (QQQ) eased 1.9%.US equity indexes were...
- [ETF market surges past $15 trillion in a selloff-driven week](https://www.google.com/goto?url=CAESogEBxCJF1-fkuYC3STyCNRvEJtNG_syY3cEipFazfivdvnuvg7Dt7BOKZDEhFHjDCBzy_bBFs6d2zE3qB5evs6zEouYL45g0uS-RJqBP0qIFq3fx7AT9fSBa7IdEn9xJHEJKDYU4wxVxCbIZo8EYUS4iCLPr3RDUkVJcw5Isru1YDjtfpz7M8CAtq1w2oXenXndFdPczbKv2qA6rUZJzq6SsRtw&gsessionid=CsJmbpqeYCYo8IrFukwqRUuMjjnQbXXyrXKCHLg2GBu-4B9PPTjpnw)  
  <sub>InvestmentNews, 3 hours ago</sub>  
  Investors pulled $33.9 billion into U.S. ETFs as tech and cyclicals cratered, while perpetual futures emerge as a new competitive threat.
- [Market Moves From Volatility to Stock Picking](https://www.google.com/goto?url=CAESlQEBxCJF1xv9yHy4BuNvu2A54yuE2zOipei3hS9KzlSn7m0i-QTj_fA4TLZPA7HL9fa83NFMRiW2_ysJVjffICwEB4etVyAE1-DOrtMcwy4gcvCBc80d5MSpIBffTlQot2eZ_h9V2z853pZcX_uMF71OZJnizTGqc32_OYIDFK4eMSk8hjt88TZK8jb8DL1_izqudqPgMA&gsessionid=CsJmbpqeYCYo8IrFukwqRUuMjjnQbXXyrXKCHLg2GBu-4B9PPTjpnw)  
  <sub>RealMoney Pro, 23 hours ago</sub>  
  The Invesco QQQ Trust (QQQ) is down 1.7% on Tuesday but is off its early lows after some panicky selling at the open. Nvidia (NVDA) and Anthropic (ANT) are...
- [Stock Market Today: Jensen’s Return to Nvidia Is Causing Index Indigestion](https://www.google.com/goto?url=CAESsAEBxCJF1_qGHCKV4XbcP91N84us4mWuOdtxodRaaB3doQNDHLjjJxTiHTVBaG17sew7HwQLB0rFEtK6QvYfkSzKK_cPYcf25Mi1dfHakj3wpDZ50Hv_7DmwRF64vZ5wH8kVVNqILDtDf2LoZ7eMUYQ2tQ-jbxgasl0ol-aPtw5MxuMRPrv0X-o_xBXD3A9mYPkY5paekP1CXcT-HE1KncdA369TDjb2Zxgr3tmQt38lqQ&gsessionid=CsJmbpqeYCYo8IrFukwqRUuMjjnQbXXyrXKCHLg2GBu-4B9PPTjpnw)  
  <sub>24/7 Wall St., 22 hours ago</sub>  
  Nvidia (NVDA) sank 8% to about $151 as bipartisan criticism of Jensen Huang's return as CEO erased Monday's relief rally. The Nasdaq-100 (QQQ) fell 3% and...
- [iShares Russell 2000 ETF (IWM) Price Prediction: Small-cap rebound faces overhead resistance as momentum stays mixed](https://www.google.com/goto?url=CAESogEBxCJF1-lP92FrXbvzHSCO0TKmscPLgDU7RmfAPSzumJlJJ46AP6JakEE-rYz4PqBBmnyJ2CQMt1qhJqmf8O5Lxudc6V5m0mOf3nTvY2wF3yGS5CMpkJr7EQ_NdeE2Jh91Dv9cZQVoeOQiKTwy6Qdeu9wZLhILLaAHVP1BZ-l4luyyVcepDMdXwAYurxl5R-Mnj4bpkKgFnFCpa8q1tpBEeyk&gsessionid=CsJmbpqeYCYo8IrFukwqRUuMjjnQbXXyrXKCHLg2GBu-4B9PPTjpnw)  
  <sub>Blockchain News, 6 hours ago</sub>  
  iShares Russell 2000 ETF (IWM) is holding near $265.71 after a flat 24-hour move, but the ETF remains below the 20-day and 50-day moving averages. Binance.
- [SanDisk (SNDK) Stock Price Prediction: Oversold plunge collides with heavy analyst support and split-adjusted volatility](https://www.google.com/goto?url=CAESowEBxCJF17rNiIgcic1SXgsnB3_94ZBeqJxe6mVPCJC-Sogyy6FBdDiS3m3co_2PQ7lghtuzOx2j0XBn8jfm_Y12swcG6GCf_iHlybbQLWjCYes9SLUNWrwga8HGecnLpevtPFzAuqL1HXTV1THZn-oTmUvIvuqUIbBLOPeKCAbz2WVj2_qIDp6nhdawlWD1QDTrkRdGBTdODVeTSb6QYEb3gK1R&gsessionid=CsJmbpqeYCYo8IrFukwqRUuMjjnQbXXyrXKCHLg2GBu-4B9PPTjpnw)  
  <sub>Blockchain News, 6 hours ago</sub>  
  SanDisk (SNDK) fell 11.45% in the latest 24 hours to $74.14, while the daily RSI at 15.13 and stochastic readings near zero point to a deeply oversold tape.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.16% (+0.01 on the week) | 5-year 4.62% (-0.26 on the week) | 10-year 4.83% (-0.24 on the week) | 30-year 5.24% (-0.17 on the week)
Yield curve, 10-year minus 3-month: +0.67 points -- upward sloping (normal)
US dollar index: 103.93 (+0.07 on the week)
Volatility (VIX): 31.72 (+7.2 on the week) -- stressed
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.1% (2026-10-01) | jobless claims 189k (2026-11-21)
Policy and expectations: Fed target 4.00% | market expects 2.1% inflation over 10 years
Rate path: 2-year Treasury 4.63% vs Fed target 3.75-4.00% -- the bond market prices about 3 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 261.29 (bar of 2026-11-25), from 502 daily bars
Trend: vs 20d SMA 274.01 (-4.6%), 50d 277.01 (-5.7%), 200d 279.55 (-6.5%); 50d below 200d
Momentum: RSI(14) 38.5 | MACD -4.311 vs signal -2.924 (histogram -1.387)
Returns: 1d -2.2% | 5d -3.3% | 1m -6.7% | 3m -12.8%
52-week range: 239.61 - 305.09 (now 33.1% of the way up)
Volatility: ATR(14) 5.68 (2.2% of price) | annualised 20d 31.7%
Volume: 0.14x the 20-day average
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
Three-year record: +15.5% a year | beta to the market 1.26
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
Weighted price target: +22.0% above the current prices
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
Share count change: 1 week: +0.0% (0.00) over 7d | 1 month: +0.0% (0.00) over 32d
Shares outstanding: 281.05M | fund size: 73.44B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### US company bonds, safer (LQD) · Index fund — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> No macro surprise, modest technical bias with very low volume, mixed fund flows (net monthly inflow but recent weekly outflow), fundamentals unchanged.

**Main reasons it gave:**
- No policy or data surprise this week (inflation 3.7% and unemployment 4.1% within expectations)
- Technical indicators show slight bullish bias (RSI 57.3, MACD positive) but volume is 0.04x 20‑day average
- Fund flows show net inflow over the month (+12.4%) offset by a recent weekly outflow (-1.1%)
- Fund fundamentals unchanged: yield 4.8%, credit quality stable, three‑year return +4.2% per year

<details><summary><b>News</b> — score +0.00</summary>

- [Saba Capital Management, L.P. Adds 2.78 Million DXYZ Shares: Ins](https://www.gurufocus.com/news/9218856/saba-capital-management-lp-adds-278-million-dxyz-shares-inside-the-destiny-tech100-inc-stake)  
  <sub>GuruFocus, 13 hours ago</sub>  
  Saba Capital Management, L.P. (Trades, Portfolio) has expanded its position in Destiny Tech100 Inc (DXYZ), adding 2775709 shares at a transaction price of...
- [Saba Capital Management, L.P. Adds to BNY Mellon Strategic Munic](https://www.gurufocus.com/news/9218817/saba-capital-management-lp-adds-to-bny-mellon-strategic-municipal-bond-fund-inc-dsm-shares-look-54-undervalued-on-gf-value)  
  <sub>GuruFocus, 13 hours ago</sub>  
  A Small Add to a Long-Standing Municipal Bond Position Saba Capital Management, L.P. (Trades, Portfolio) reported an add to its stake in BNY Mellon...
- [Saba Capital Management, L.P. Adds to NEW GERMANY FUND INC (GF) Stake With Latest Purchase](https://www.google.com/goto?url=CAEStwEBxCJF1-fcR6NOFCuEW2q5StHygkIJI_wVqC_Ierm0BxIZ2fFVqhd72fFDL-P7Jhxb5GVdjEkyG_82xnOx0d0VAVrlMHPZZHC6zEGImP_JhiMdm51HXU7kYlwzZIUjkDHs-GTdBddBvnBZQKgaucHl9oGUDE62DjI10mEqP3FTW02lQESXPccN7uvjUDp4fEgmVnlZSQWWoUPIj8SPTJgEyDXnnTui7XF-K8n2hORrKP2injGNwXg&gsessionid=EFIELPZ5tdVLCdV8ywg3pzeRbOaNqHBTkMsm9pvE0SJyuR6CdL-TgA)  
  <sub>GuruFocus, 13 hours ago</sub>  
  A Modest but Deliberate Addition to an Existing Position Saba Capital Management, L.P. (Trades, Portfolio) reported an incremental purchase of shares in NEW...
- [Saba Capital Management, L.P. Adds to Highland Opportunities and Income Fund (HFRO) Stake](https://www.google.com/goto?url=CAEStgEBxCJF11dfEV89M5Q3HgSwsQ8rjE3XjrtWxCKrDr3jyEFcPvRPVCdNiWBKtifkciCtfUfRYTgtgiI6YlIOlH6vZpZQ0bl0TrPJbj7O3Wb_K8h4VbuvhkXEwqRJS9EPvoMGsAk_h9rRcEW4Rcn3d6V3R6R-dlGnXtbl_WBSK6i2g-4KZnscg3tLiDfA_I0J6hYyw_kxvj8GICVYBiepniK1WGv-5jm0TUpeSuHXXJjv2Wfkh1D_yg&gsessionid=EFIELPZ5tdVLCdV8ywg3pzeRbOaNqHBTkMsm9pvE0SJyuR6CdL-TgA)  
  <sub>GuruFocus, 14 hours ago</sub>  
  A Modest but Deliberate Addition to a Closed-End Fund Position Saba Capital Management, L.P. (Trades, Portfolio) reported an add transaction in Highland...
- [Saba Capital Management, L.P. Adds 255,199 Shares of Highland Op](https://www.google.com/goto?url=CAESvwEBxCJF1wjR7z_8TIjo5F9eysk-RNHpgKKF_No8wXwEBn1-m7arAfT9LcIOzcnbNWme5GOum_XE7mfVL7_DkE4lXc3dQLyTqVcTe29v_nE5o1l0AJBTxrJC3joW6kHuQRWMFJhdJqbejGhbVrjm6h38FNsjICWfKIZw23s9ZQWXwtxl5S7zsi1a84nnz2TqAHOaqaeWjsKZyj2eLSkVNBTXAeZPHM45PxjL-YRbh4ip8F5P2RTfiOHXtgUcF7KgQg&gsessionid=EFIELPZ5tdVLCdV8ywg3pzeRbOaNqHBTkMsm9pvE0SJyuR6CdL-TgA)  
  <sub>GuruFocus, 12 hours ago</sub>  
  A Measured Addition to a Closed-End Fund Position Saba Capital Management, L.P. (Trades, Portfolio) reported an addition to its stake in Highland...
- [Saba Capital Management, L.P. Adds to Gabelli Ellsworth Growth &](https://www.google.com/goto?url=CAES3wEBxCJF1_nfyu2pmpFMY4SL314GrcB2zvcw2qP9UCLBpScpnzles26iPVKanEZu3Ywb8SE7nYrMkMlfoIVGKb9SwgnhGdaJENkg_WOFvL_rKI9ajztOEoJKhGMqiiOdQzVNdUKRViMI6k1yh0OdCEWwC1OV5I3V6EQ5yzvom-_BeuFA_FgXV60xn0MH3a7-ne4aaVplXR91QEU55Qdef7dW4-Rrzm0zgvyp7V1D_knrK-iNfAEcrZHgtc5vMk6P18_rAhDiC2whlMiAwjj8zO_6G2qDywEUNxydbabzuNFO&gsessionid=EFIELPZ5tdVLCdV8ywg3pzeRbOaNqHBTkMsm9pvE0SJyuR6CdL-TgA)  
  <sub>GuruFocus, 13 hours ago</sub>  
  Saba Capital Management, L.P. (Trades, Portfolio) has increased its position in Gabelli Ellsworth Growth & Income Fund Ltd (ECF), according to a 13D/G...
- [Saba Capital Management, L.P. Adds to Mexico Fund Inc (MXF) -- Shares Look 36% Undervalued on GF Value](https://www.google.com/goto?url=CAESwAEBxCJF1xdirFZnj98E_pBrWfvdk0SFzeTaxzrTr9o2tG46QSz6IHNbIUX1B4Dwxo9OthhT0bDmbXBJDhxOZon_GKJYQv_STHJEYnCVgn_CsuzA9Imk8uQYrDk380g8M4Utu3WgOwrxljot5FqQRn3mr_1bWa8-tpSug5YPMxs9FHvQOaXagdN2cwau2au_nYDkaFpkTSuOLNVSC8XsGMcHcAOTBqu-8YAQsjba_rPwGTIdRS9UV2TCtjnYh6ChuZ8&gsessionid=EFIELPZ5tdVLCdV8ywg3pzeRbOaNqHBTkMsm9pvE0SJyuR6CdL-TgA)  
  <sub>GuruFocus, 13 hours ago</sub>  
  A Modest but Telling Add-On Purchase Saba Capital Management, L.P. (Trades, Portfolio) disclosed an incremental purchase of Mexico Fund Inc (MXF) shares...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.16% (+0.01 on the week) | 5-year 4.62% (-0.26 on the week) | 10-year 4.83% (-0.24 on the week) | 30-year 5.24% (-0.17 on the week)
Yield curve, 10-year minus 3-month: +0.67 points -- upward sloping (normal)
US dollar index: 103.93 (+0.07 on the week)
Volatility (VIX): 31.72 (+7.2 on the week) -- stressed
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.1% (2026-10-01) | jobless claims 189k (2026-11-21)
Policy and expectations: Fed target 4.00% | market expects 2.1% inflation over 10 years
Rate path: 2-year Treasury 4.63% vs Fed target 3.75-4.00% -- the bond market prices about 3 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 104.23 (bar of 2026-11-25), from 502 daily bars
Trend: vs 20d SMA 103.77 (+0.4%), 50d 103.44 (+0.8%), 200d 107.07 (-2.7%); 50d below 200d
Momentum: RSI(14) 57.3 | MACD 0.002 vs signal -0.049 (histogram 0.051)
Returns: 1d +0.4% | 5d +1.0% | 1m -0.1% | 3m -2.3%
52-week range: 101.83 - 112.05 (now 23.5% of the way up)
Volatility: ATR(14) 0.52 (0.5% of price) | annualised 20d 6.4%
Volume: 0.04x the 20-day average
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
Share count change: 1 week: -1.1% (-355.92M) over 8d | 1 month: +12.4% (3.53B) over 33d
Shares outstanding: 308.05M | fund size: 32.11B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### S&P 500, equal weight (RSP) · Index fund — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Mixed signals: bearish positioning from CFTC, bearish technical momentum, but bullish fund inflows and slight analyst optimism. No macro surprise or decisive technical break, so overall neutral.

**Main reasons it gave:**
- CFTC data shows net short 11.2% of open interest, up 3.8% week over week – bearish positioning
- Fund flows indicate share count up 6.7% over the past month – bullish demand
- Technical indicators: price below 20‑day and 50‑day SMA, RSI 41.8, MACD negative – bearish momentum
- Analyst view of top holdings: 38.4% buy, weighted price target +0.2% – slight bullish bias
- News: RSP rose 0.55% while SPY fell 0.51% on the day analog devices dropped – equal‑weight resilience

<details><summary><b>News</b> — score +0.00</summary>

- [Does RSP Hold Up Better Than SPY In Sell-Offs?](https://www.trefis.com/stock/rsp/articles/628734/does-rsp-hold-up-better-than-spy-in-sell-offs/2026-11-25)  
  <sub>Trefis, 8 hours ago</sub>  
  Our latest piece, Did Nvidia's Rebound Make VOO Owners Whole?, began with Nvidia's board reinstating Jensen Huang as CEO on Monday, Nov 23,...
- [RSPS: Consumer Staples ETF Reduces Company Risk](https://seekingalpha.com/article/4966643-rsps-consumer-staples-etf-reduces-company-risk)  
  <sub>Seeking Alpha, 20 hours ago</sub>  
  The Invesco S&P 500 Equal Weight Consumer Staples ETF offers equal-weight exposure to 33 consumer staples stocks, reducing company-specific risk. RSPS has...
- [Equal-Weight ETFs Still Deserve Attention Despite NVIDIA-Led Rebound](https://www.google.com/goto?url=CAES1QEBxCJF178Act91unMAXJ6dZuhYVTqWoP_IhLenuyrws6SDu2tYLYVKPNwIINhNJHF0TZghgpxvrYwnuwUHqNymdhH2z7zyZJGaUXXA33coeUXFTBcvSnd4Sd-yfbBWhijGygg1Y2c7RR5o56VGLUTyrxfgPpq6epcncMeX9fZW5qIatJ5VoJVb89n7ooPsQuKfhUs3hfmXhylZm9M69nyNf0wiVxYhSF-AWa9KXU4Y9WZmWViQ4q4jrqebW4DXJvhlfbsUcZkKhN1712ZQZJD0fpgLpS0&gsessionid=GPrKtrhPDPOFqD3oMUoOnH1585x353aX-kLKA9mkS_ZiO-Ds29aLFw)  
  <sub>The Globe and Mail, 22 hours ago</sub>  
  Recent developments in the U.S. equity market have brought concentration risks into sharper focus, highlighting the market's continued sensitivity to news...
- [Chip stocks erase more than half of Monday's gain as the average stock edges up](https://www.google.com/goto?url=CAEStgEBxCJF1zA7avuYQIMtQmNlhkHaIPtsTSjluUW7IPejCrVRG_iI9IG_4ZY-n7vCjaiPzwpQc-wTJsm0uYiqx356x7pYHetKPm5_yAffKI9PO-pGbNkVydiLwbRR1rtehrILU272jlTxOhvYvMHZlZbQa2KM0G5i7CpF1XSdi9Y2Xx2wALyLc5kH6FRBjp0ogZnCEAo-GuSK6Mk1ZRsmfCziCvVTqT6gxqc7rO3nU0w-mMqqT2SfoQ&gsessionid=GPrKtrhPDPOFqD3oMUoOnH1585x353aX-kLKA9mkS_ZiO-Ds29aLFw)  
  <sub>Quantisnow, 23 hours ago</sub>  
  At 10:20 a.m. ET Tuesday, the VanEck Semiconductor ETF was down 7.21%, about 56% of its 14.9% gain on Nov. 23 in price terms, while the Nasdaq 100 fund had...
- [Safe-Harbor ETFs: Shelter From the Storm - VettaFi - Commentaries](https://www.google.com/goto?url=CAESiQEBxCJF16EH4djOf3XjLL2eapRQzw7Jh_F5vPmKkPC_fEhicGb0Nw8qASW4n24DBUM80oBRuzPKq76ouaB9VqY0XdD_2xxXpSHY57kgzHyk41fFbGiHMHBsdJWnYhQn06hmoRafCkjbgOMe6yK1dKOlPyFQRRH3fPF-VaqbsT3KeZDq7ZmCE0FyPA&gsessionid=GPrKtrhPDPOFqD3oMUoOnH1585x353aX-kLKA9mkS_ZiO-Ds29aLFw)  
  <sub>Advisor Perspectives, 23 hours ago</sub>  
  You might be tempted to call whiplash the new normal in today's market — and you wouldn't be wrong. Markets stumbled into the fourth quarter with a brutal...
- [RSP Dec 2026 230.000 call (RSP261204C00230000) Stock Price, News, Quote & History](https://www.google.com/goto?url=CAEScQHEIkXX6tGWpnUdyU1mdJ7Mwo0Uer2hP-1yJ_Fiw-vATIavuEIW5rb2sGTOfMzHSLvFFfejfCbg2xOjYk71z6KUlfR74x7mhuAa23dvngMwbZy1Dtc4w71_D8LcWzzYGDb6Bme38hNOzdp88pVSnI2B&gsessionid=GPrKtrhPDPOFqD3oMUoOnH1585x353aX-kLKA9mkS_ZiO-Ds29aLFw)  
  <sub>Yahoo! Finance Canada, 7 hours ago</sub>  
  Find the latest RSP Dec 2026 230.000 call (RSP261204C00230000) stock quote, history, news and other vital information to help you with your stock trading...
- [RSP Dec 2028 215.000 call (RSP281215C00215000) stock price, news, quote and history](https://www.google.com/goto?url=CAEScQHEIkXXfavVQWMc5UM0UPvLLj6bz63VCCKqiXnXMB5tWiP9hpPch0MId6_S_fd_SkdXeIPH1cM5XRpH90HYcHK-M3PzkZUi8d8VR-U8EJ5Sr_zllNSa2tXzsgvgb29SUhbB6X-c_x9-grsaeL3Teeh-&gsessionid=GPrKtrhPDPOFqD3oMUoOnH1585x353aX-kLKA9mkS_ZiO-Ds29aLFw)  
  <sub>Yahoo Finance UK, 16 hours ago</sub>  
  Find the latest RSP Dec 2028 215.000 call (RSP281215C00215000) stock quote, history, news and other vital information to help you with your stock trading...
- [Analog Devices falls 17.3%, dragging the Nasdaq 100 down while equal-weight stocks rise](https://www.google.com/goto?url=CAESsAEBxCJF1zqqaxYWenVXjgpOZM-kbe7DMcRS9l_rACueEm44MIkB-vymw12d9hmEfMj8QeuODGXtynHgIUeAdj_qzUf6p2mGfKv36smxjY4UX9aNsllq4arN5M-PCUwjnPBGdWS1cT2LGOh4iUkeVpHWk1ni9f8Hi4zhUagh0Smt8uqU2MPy-5xH_yMgEm9wc5nzWQgZ4d_X5cEYzLnNmUPwnFtWPVCbdv5J_GcQQGFPnA&gsessionid=GPrKtrhPDPOFqD3oMUoOnH1585x353aX-kLKA9mkS_ZiO-Ds29aLFw)  
  <sub>Quantisnow, 16 hours ago</sub>  
  On Nov 24, 2026, the equal-weight S&P 500 (RSP) rose 0.55% while the cap-weighted SPY fell 0.51%, a gap of about 1.06 points. Analog Devices fell 17.30% on...
- [ETFs Are Net Sellers of Yum! Brands (YUM) on Monday](https://www.google.com/goto?url=CAESkgEBxCJF1-pWhXgXSrR4DG1_mO1bdQnEoIiORzo9ieislwF36aQJnFL41dBh1ru8OfO4sChevatnLiFoTAq-d5tG5kh_YZjvIv6bn6EEfvCOZrxoqS-Rl12f7IqyEn5tdgKCWAFbIGmboDMlnccM1B9mW8c1z3JZwyY5pVJr_CZHuWk59LLEkgNg6MuV0Nfrjm7wRw&gsessionid=GPrKtrhPDPOFqD3oMUoOnH1585x353aX-kLKA9mkS_ZiO-Ds29aLFw)  
  <sub>GuruFocus, 3 hours ago</sub>  
  ETFs sold $78.2 million in Yum! Brands (YUM) stock on Monday, a net outflow driven by dollar value even though more funds traded the other way.
- [CHAI TRUST CO LLC Trims Ardent Health (ARDT) Stake by 7.1 Millio](https://www.google.com/goto?url=CAESpwEBxCJF1_jUquPdehDYlhLUfULcoXFWreIID95iemfkA660n1OVGycePLXCgSBueGUsA95OVQpF0H3zudnxABVpP5Dnkegacf5jaApDunD3KjaeDweg82Q7d6ZTTCp_oX6Hf61n-C8rUbFgmtncOEj6MiB8BfuUnaQi1nFGD5Cm2fwMVLaCzzKE6KJ5ZSf1Q-icmZjGp3ZwNfs3RLvLDfHZikZbYDt5AA&gsessionid=GPrKtrhPDPOFqD3oMUoOnH1585x353aX-kLKA9mkS_ZiO-Ds29aLFw)  
  <sub>GuruFocus, 14 hours ago</sub>  
  A Concentrated Position Gets Slightly Smaller CHAI TRUST CO LLC (Trades, Portfolio) executed a sale of Ardent Health Inc (ARDT) shares on 2026-11-19,...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.16% (+0.01 on the week) | 5-year 4.62% (-0.26 on the week) | 10-year 4.83% (-0.24 on the week) | 30-year 5.24% (-0.17 on the week)
Yield curve, 10-year minus 3-month: +0.67 points -- upward sloping (normal)
US dollar index: 103.93 (+0.07 on the week)
Volatility (VIX): 31.72 (+7.2 on the week) -- stressed
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.1% (2026-10-01) | jobless claims 189k (2026-11-21)
Policy and expectations: Fed target 4.00% | market expects 2.1% inflation over 10 years
Rate path: 2-year Treasury 4.63% vs Fed target 3.75-4.00% -- the bond market prices about 3 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score -0.20</summary>

```text
Last close 210.92 (bar of 2026-11-25), from 502 daily bars
Trend: vs 20d SMA 217.35 (-3.0%), 50d 214.73 (-1.8%), 200d 209.38 (+0.7%); 50d above 200d
Momentum: RSI(14) 41.8 | MACD -1.175 vs signal -0.096 (histogram -1.080)
Returns: 1d -1.4% | 5d -2.1% | 1m -3.0% | 3m -4.8%
52-week range: 188.07 - 223.33 (now 64.8% of the way up)
Volatility: ATR(14) 3.38 (1.6% of price) | annualised 20d 23.1%
Volume: 0.14x the 20-day average
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
Three-year record: +15.1% a year | beta to the market 0.80
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
Ratings by weight: buy 38.4% | hold 61.6% | sell 0.0% (mean 2.55 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +0.2% above the current prices
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
Share count change: 1 week: +3.9% (3.77B) over 8d | 1 month: +6.7% (6.23B) over 33d
Shares outstanding: 473.09M | fund size: 99.78B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### US government bonds, 1-3 years (SHY) · Index fund — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Neutral overall: modest bearish pressure from speculators offset by net inflows and stable fundamentals; technicals show mixed signals and macro stress without a clear surprise.

**Main reasons it gave:**
- Large speculators net short 28.8% of open interest, increased by 4.7% week‑over‑week
- Fund flows show net inflow over the past month (+4.1% share count)
- Technicals: price above 20‑day and 50‑day SMAs but below 200‑day SMA, RSI 63.1
- Macro: VIX up 7.2 points to 31.7, indicating stressed market conditions
- Fundamentals: short‑government ETF with AA‑rated holdings, 3.6% yield, stable composition

<details><summary><b>News</b> — score +0.00</summary>

- [Aviva’s CEO: “Many active ETFs are shy active”](https://delano.lu/article/avivas-ceo-many-active-etfs-are-shy-active)  
  <sub>Paperjam.lu, 3 hours ago</sub>  
  Build, buy or partner? As European asset managers pursue private markets and active ETFs, their growth strategies are diverging.
- [The New York Fed’s John Williams Won’t Rule Out Back-to-Back Rate Hikes](https://247wallst.com/investing/2026/11/24/the-new-york-feds-john-williams-wont-rule-out-back-to-back-rate-hikes/)  
  <sub>24/7 Wall St., 24 hours ago</sub>  
  The S&P 500 rose 4.73% to 7,237.17 on Monday, November 23. That same day, New York Fed President John Williams told reporters he would not rule out raising...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.16% (+0.01 on the week) | 5-year 4.62% (-0.26 on the week) | 10-year 4.83% (-0.24 on the week) | 30-year 5.24% (-0.17 on the week)
Yield curve, 10-year minus 3-month: +0.67 points -- upward sloping (normal)
US dollar index: 103.93 (+0.07 on the week)
Volatility (VIX): 31.72 (+7.2 on the week) -- stressed
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.1% (2026-10-01) | jobless claims 189k (2026-11-21)
Policy and expectations: Fed target 4.00% | market expects 2.1% inflation over 10 years
Rate path: 2-year Treasury 4.63% vs Fed target 3.75-4.00% -- the bond market prices about 3 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 81.72 (bar of 2026-11-25), from 502 daily bars
Trend: vs 20d SMA 81.46 (+0.3%), 50d 81.33 (+0.5%), 200d 81.98 (-0.3%); 50d below 200d
Momentum: RSI(14) 63.1 | MACD 0.047 vs signal 0.014 (histogram 0.032)
Returns: 1d +0.2% | 5d +0.5% | 1m +0.3% | 3m -0.4%
52-week range: 81.05 - 83.18 (now 31.7% of the way up)
Volatility: ATR(14) 0.13 (0.2% of price) | annualised 20d 2.5%
Volume: 0.22x the 20-day average
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

<details><summary><b>Buying and selling by company insiders</b> — score -0.35</summary>

_Not available today._

</details>

<details><summary><b>Who is positioned how</b> — score -0.35</summary>

```text
Contract: UST 2Y NOTE - CHICAGO BOARD OF TRADE (positions as of 2026-11-17, published the following Friday)
Large speculators: net short 28.8% of open interest (4,467,824 contracts)
Change on the week: +4.7% of open interest
Crowding: 92% percentile over 52 weeks -- a crowded long by the standards of the past year
Read this as crowding, not as a forecast: an extreme is as often the end of a move as the middle of one.
```

</details>

<details><summary><b>Money going into and out of this fund</b> — score -0.35</summary>

```text
Direction: money coming in (1 month)
Share count change: 1 week: -0.5% (-134.21M) over 8d | 1 month: +4.1% (1.07B) over 33d
Shares outstanding: 336.48M | fund size: 27.50B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### US inflation-linked bonds (TIP) · Index fund — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> No material macro surprise, technicals are mixed, positioning and flows show modest but not decisive changes.

**Main reasons it gave:**
- US Treasury yields slipped modestly this week (10‑yr -0.24%, 5‑yr -0.26%)
- CFTC data shows net short position at 39.7% of open interest, down 2% week‑over‑week
- Fund flows indicate a net inflow of 2.9% over the past month
- Technical indicators are mixed: price above 20‑day SMA, RSI 56.8, low volume

<details><summary><b>News</b> — score +0.00</summary>

- [iShares $ TIPS 0-5 UCITS ETF EUR Hedged (Dist) (CBUL.DE) Seasonal returns chart](https://uk.finance.yahoo.com/quote/CBUL.DE/seasonality/)  
  <sub>Yahoo Finance UK, 8 hours ago</sub>  
  iShares $ TIPS 0-5 UCITS ETF EUR Hedged (Dist) (CBUL.DE) seasonal returns chart provides the mean and median returns by month to inform your investment...
- [iShares 0-5 Year TIPS Bond ETF (STIP.MX) Seasonal returns chart](https://uk.finance.yahoo.com/quote/STIP.MX/seasonality/)  
  <sub>Yahoo Finance UK, 12 hours ago</sub>  
  iShares 0-5 Year TIPS Bond ETF (STIP.MX) seasonal returns chart provides the mean and median returns by month to inform your investment strategy.
- [Huang’s Return to Nvidia Amplifies the Allure and Danger of All-or-Nothing ETFs](https://www.google.com/goto?url=CAESvwEBxCJF13-igGmjyIvIw2RNj_rfzF7j2lxxe3zpzk87Y3BDnUgpSFdZS7_g-A2RfZGjQW7BKFWYJP3HHyTsYGdKzR2zxdWAZNsNjo2YMmpXKSUojovanNt6KqM4A1Q8ftoAqgIYLeN-cdLpuyyhzDNIa5neft1Ipkjt2OLhAdtRABL8R07weoy_qGMxUMO1P9_iCvxUO_9WyOZKJgbiLTVrI0LEqvetPuySQDCldHKexYv96By_HY-Wd4MgAJ-4LQ&gsessionid=OgVhskoJeu8WMR0oF60G2p6P3Vn_Z0Vehw7wm9Wd8_yLFlnTVajx0Q)  
  <sub>Bloomberg.com, 22 hours ago</sub>  
  Nvidia's stock-price surge created big winners and losers among leveraged ETF investors.
- [Top Tokenized ETFs by Market Cap](https://www.google.com/goto?url=CAESXAHEIkXXqrZSrB7H21Er3ZnRASRnLhcC7Dx8T2MnSRr58lIA9zDao7PVlO9ggxwOHtpdTZTTHo926BKIWa-sLGef0ALpM9emqDQPSDMvAWEBQrhUXv5W2pJ7Co35&gsessionid=OgVhskoJeu8WMR0oF60G2p6P3Vn_Z0Vehw7wm9Wd8_yLFlnTVajx0Q)  
  <sub>Coingecko, 13 hours ago</sub>  
  Discover the top ETFs (exchange-traded funds) by tokenized market cap. Track ETF prices alongside their tokenized prices, market cap,...
- [iShares $ TIPS ETF USD Acc (ITPS.SW) Seasonal returns chart](https://www.google.com/goto?url=CAEScgHEIkXXZMLnWELMNzfKaI6sFPI2-ydpZQbEK4FfXOqwTKYlWY7R9WXc9BCT1g54ozy3pz9LBrZdO17lPkFfGI6YtOnR6t7SQKrOIaOBMl9KG1PDKy6cIKepbQR9qKi70qKFU72hPfnS_tAipO4v7_SZzg&gsessionid=OgVhskoJeu8WMR0oF60G2p6P3Vn_Z0Vehw7wm9Wd8_yLFlnTVajx0Q)  
  <sub>Yahoo Finance UK, 21 hours ago</sub>  
  iShares $ TIPS ETF USD Acc (ITPS.SW) seasonal returns chart provides the mean and median returns by month to inform your investment strategy.
- [Cathie Wood’s ARK Bets Big on Anthropic (ANT) – Buys $61.6M in Shares. Here’s What It Sold](https://www.google.com/goto?url=CAESqwEBxCJF14mGy1ZyVvefQAb8MTqWcsxDnTorh22UMtOORxEXkJYa9VN-IaXX_pehcwDoM49mJtp_lmCkYSqX0tbsPj_Ah-R9ghxT8TmOxbUIIyBw0Pil3Qb3ub-6nPsuWP3fKvaOKHwOD58l_16wEwX7DF1DFBWldVeDIdOfcvG2vZok8_Rv3aOSRxanT064XSd6f_DKWNuDfIv4q8nWCOAHxpqLocnEq93QlnA&gsessionid=OgVhskoJeu8WMR0oF60G2p6P3Vn_Z0Vehw7wm9Wd8_yLFlnTVajx0Q)  
  <sub>TipRanks, 3 hours ago</sub>  
  Cathie Wood's ARK Invest purchased 751710 shares of Anthropic ($ANT) on Tuesday, November 24, as the stock slipped below its IPO (initial public offering)...
- [RKLB Stock Price Forecast: Technical Signals Say Sell, but Analysts See 100% Upside](https://www.google.com/goto?url=CAESqQEBxCJF101onllJ07fgytet6fxB6UTij75nYlN_n_DzGjssJX6bRqS3Bs4UTh3tTSTo18id-qdXwY7Jj6tNeG3mxE4MpoUdtREERfQXw0yB5LdYKLj0m0EJdLVgKPhw2xPdyr6BTY2OG_FCi6pXNd1gLNUOWoNdDkb4QTJm0xvXfYNI7PWkqk_1x1qiKrF-qQdvfp8a0KswMMsye9r34pF6gOgRKkxIqBNy&gsessionid=OgVhskoJeu8WMR0oF60G2p6P3Vn_Z0Vehw7wm9Wd8_yLFlnTVajx0Q)  
  <sub>TipRanks, 32 minutes ago</sub>  
  Aerospace company Rocket Lab USA ($RKLB) stock currently trades at $45.98, down 34% year-to-date due to delays in the launch of its reusable medium-lift...
- [Why SpaceX Stock Is Falling Today — and Why Analysts Still See 100% Upside](https://www.google.com/goto?url=CAESoAEBxCJF11QWJ2bloIF9gqSskbd7pnIxatFQZ0VtE691OQVVTaVOBlPpaCTxQNBxNZ6L01NJHRE_Jtf53uNHjsXonPbQ02ZjQ1akBx64Gqj7CzUkjOD5siuz30_mijH2rGWdEjLdIjVFEt2bejT7Eh1-T_bx9ad-w8_RHyR6H6XqhEPuIC8_DHqRkPK70uEW_Z7lojDMRfWjcAgSsjzVfuUE&gsessionid=OgVhskoJeu8WMR0oF60G2p6P3Vn_Z0Vehw7wm9Wd8_yLFlnTVajx0Q)  
  <sub>TipRanks, 1 hour ago</sub>  
  SpaceX ($SPCX) stock is falling in premarket trading today, extending losses from the previous session. The decline comes after Anthropic ($ANT),...
- [Stock Futures Under Pressure as October PCE Data Sparks Rate-Hike Fears; AI Jitters Persist](https://www.google.com/goto?url=CAESswEBxCJF1_Zo06-95PKoExgni9YCzHNrivytGyHVcLXWrCpcD_0yRK0_udbclNIBRXMo7MpKyAjRn4_gv-zs2UZCT402-HG41Ln9pcKBizK_ilbIeehgkj1yXoOVBBUu0ESjf9uovkBUKaK6EF_YdHhmsedPlE2lXSdXPjpnqkbcABu0RNPqCOsNWNQy5KSm9K9pFyoTeGuZ_zhMsYEChXEd3Tfn1AqQdFvpk4lrfUmaSAutZA&gsessionid=OgVhskoJeu8WMR0oF60G2p6P3Vn_Z0Vehw7wm9Wd8_yLFlnTVajx0Q)  
  <sub>TipRanks, 56 minutes ago</sub>  
  U.S. stock futures fell Wednesday morning as AI plays remained under pressure and investors digested October inflation data.
- [Prediction: AMD Stock Could Rally 58% as Analysts Maintain Strong Buy Rating](https://www.google.com/goto?url=CAESowEBxCJF15Kjktk-EkywFoqd4Rc7007U05gJVNI98kAfT4838kHopoHzyZ_vJ8L7nw4gBLQNnsG44icOPe4jU30kItf9hmae0uo6xSpoh9JGe32k2ZczuQqrWL6Sv7_Vl8ytCNr8WWR_-HwxXUFU5Yu-lag8_ns-X9v3FbJ4IE-gluqNP7D5nxaf3hKCho-4lCVzONIS-AuiclFzNzyvQlmBA4Rx&gsessionid=OgVhskoJeu8WMR0oF60G2p6P3Vn_Z0Vehw7wm9Wd8_yLFlnTVajx0Q)  
  <sub>TipRanks, 1 hour ago</sub>  
  Advanced Micro Devices ($AMD) shares have pulled back in recent weeks, but Wall Street remains bullish on the chipmaker. According to TipRanks data,...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.16% (+0.01 on the week) | 5-year 4.62% (-0.26 on the week) | 10-year 4.83% (-0.24 on the week) | 30-year 5.24% (-0.17 on the week)
Yield curve, 10-year minus 3-month: +0.67 points -- upward sloping (normal)
US dollar index: 103.93 (+0.07 on the week)
Volatility (VIX): 31.72 (+7.2 on the week) -- stressed
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.1% (2026-10-01) | jobless claims 189k (2026-11-21)
Policy and expectations: Fed target 4.00% | market expects 2.1% inflation over 10 years
Rate path: 2-year Treasury 4.63% vs Fed target 3.75-4.00% -- the bond market prices about 3 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 105.91 (bar of 2026-11-25), from 502 daily bars
Trend: vs 20d SMA 105.61 (+0.3%), 50d 105.25 (+0.6%), 200d 108.42 (-2.3%); 50d below 200d
Momentum: RSI(14) 56.8 | MACD -0.042 vs signal -0.078 (histogram 0.036)
Returns: 1d +0.4% | 5d +1.0% | 1m -0.4% | 3m -1.4%
52-week range: 103.98 - 111.88 (now 24.4% of the way up)
Volatility: ATR(14) 0.38 (0.4% of price) | annualised 20d 4.9%
Volume: 0.05x the 20-day average
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
Share count change: 1 week: -0.9% (-137.91M) over 8d | 1 month: +2.9% (418.46M) over 33d
Shares outstanding: 138.86M | fund size: 14.71B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### US government bonds, 20+ years (TLT) · Index fund — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Neutral overall; modest bearish positioning offset by favorable fundamentals and slight technical upside.

**Main reasons it gave:**
- Large speculators net short 35.5% of open interest (CFTC positioning)
- 10-year Treasury yield fell 0.24% on the week
- Fund's yield 4.8% with AA credit quality
- RSI 63.9 and MACD above signal indicate modest bullish momentum

<details><summary><b>News</b> — score +0.00</summary>

- [The 10-Year Treasury Yields 4.92%. JPMorgan's Income ETF Paid 5.7% Over the Past Year, BlackRock's Paid 6.06%, and Neither Has a Maturity Date](https://247wallst.com/investing/etf/2026/11/24/the-10-year-treasury-yields-4-92-jpmorgans-income-etf-paid-5-7-over-the-past-year-blackrocks-paid-6-06-and-neither-has-a-maturity-date/)  
  <sub>24/7 Wall St., 15 hours ago</sub>  
  Two bond ETFs out-earned the 10-year Treasury's current yield over the past year, yet something else shrank while the checks kept arriving.
- [Majority Of Fed Regional Boards Were In Favor To Raise Rates In October, Minutes Show](https://www.tradingview.com/news/stocktwits:9775a3f32094b:0-majority-of-fed-regional-boards-were-in-favor-to-raise-rates-in-october-minutes-show/)  
  <sub>TradingView, 17 hours ago</sub>  
  A majority of regional Federal Reserve bank boards favored lifting discount rates ahead of the central bank's late-October policy decision, according to...
- [Bessent Warns the Fed Could Be Making a "Policy Mistake" if It Over-Tightens](https://www.google.com/goto?url=CAES1QEBxCJF1-6J55O-tHLctFO4Y4_IT0BHRa_E7sFiROcJk_F7dCo6sy5o7louP2NG_WqbR_D_UKy6TY4pgrAtD52glm0pAdtyHWUy1TA0-LQD2tL9hUjdvVgz6jx6KnMyexYL-SlQIc9PumaapYnqvrkN_nFuj_isms9YsnEo8ym0KSeKKeut7U57nwM1acQUmHuOBjSyx8uyj4nzJQL7hqBdnACbo-cYXpS3KJtrbIguTs6zByjILrMTx6tx2OUQlPDK924K3wplruAN82QQ-tbm0aIHBUw&gsessionid=A_KWxrweq2NUHAxqCnHBKlILSBaZwEdoYuKBkReUzLKZ02fsXWOX3Q)  
  <sub>24/7 Wall St., 23 hours ago</sub>  
  Treasury Secretary Scott Bessent appeared on Face the Nation on Sunday, November 22, after a hard week for stocks. He gave both a political and a monetary...
- [Debt Costs With Higher Interest Rates](https://www.google.com/goto?url=CAEShAEBxCJF10dT4ZeebDo5NRkwluj06nexU0MSH6YZwOUoeP1xGLWUcZSLV3YtoCya1Kwar8CFrVURl5Ar4tOYSPIvF0O2hps7xMVAMUAJmi6fZsCl86i5qcN9LZ2hhyw_uGcPRHsx2206UNzKMAOua2DTff7TAVVenepPJq3RaFEn_Rbu4gc&gsessionid=A_KWxrweq2NUHAxqCnHBKlILSBaZwEdoYuKBkReUzLKZ02fsXWOX3Q)  
  <sub>Seeking Alpha, 3 hours ago</sub>  
  The biggest financial problem facing the United States is the ongoing $2 trillion-plus federal deficit. We are borrowing approximately 6-7% of our annual...
- [The New York Fed’s John Williams Won’t Rule Out Back-to-Back Rate Hikes](https://www.google.com/goto?url=CAESrAEBxCJF1_9OiLpFQ1DIgONrIA8Xg-MXgO0U-AFx0Z7DtxZImLBnRF91rSU7764IW9adHHGiHLEX6VeEtkCgi-AZVXs1-181nEAPXq1HYDqOYP5c3Mu2FrKa80uoXs3HZGHdApvDA-_W59BoYxSsMiw_ool1jW9y2R4U_uIn6OFtgGwU4AxdKIUoZoIH0mQcOQmCSQ9aBFK0nE9lsmLnX-_7iw5aMTrYDomF7jtP&gsessionid=A_KWxrweq2NUHAxqCnHBKlILSBaZwEdoYuKBkReUzLKZ02fsXWOX3Q)  
  <sub>24/7 Wall St., 24 hours ago</sub>  
  The S&P 500 rose 4.73% to 7,237.17 on Monday, November 23. That same day, New York Fed President John Williams told reporters he would not rule out raising...
- [Top Tokenized ETFs by Market Cap](https://www.google.com/goto?url=CAESXAHEIkXXCzoIOkLljXsWTzBxbk29lZBOM3QwrTKSx-8d8nGbmhM27RIvIQ4R7cIq7XBQCr_OQq-AC6ACnPYTSjxOmeOrdAEpBez5uIuY1hZajJ6X5AG25S4hUNEL&gsessionid=A_KWxrweq2NUHAxqCnHBKlILSBaZwEdoYuKBkReUzLKZ02fsXWOX3Q)  
  <sub>Coingecko, 13 hours ago</sub>  
  Discover the top ETFs (exchange-traded funds) by tokenized market cap. Track ETF prices alongside their tokenized prices, market cap, and volume on...
- [Gold Stopped Protecting Portfolios When Stocks Needed It Most (NYSEARCA:GLD)](https://www.google.com/goto?url=CAESoQEBxCJF1x-wH8wEd5S0jWMSx8sB92z0Op5vU3Y4VrDkBikrYnLr0mzZo-qQCTO8cGBLlAsTM6BeizbOucs7PCCaW3GQXGmZ-Z9VOWNdwdYkdAG14fKOLW4olnFNFlWQs5IcCsOQczVpVEY1TQirleftLD-j4AddJSydPvejG0o6bM4uBjbcAiWAxG0aheabjjFTHFafz5Xl83osh7jgTKyBmw&gsessionid=A_KWxrweq2NUHAxqCnHBKlILSBaZwEdoYuKBkReUzLKZ02fsXWOX3Q)  
  <sub>Seeking Alpha, 5 hours ago</sub>  
  SPDR Gold Shares ETF is a hold as central bank buying and liquidity-driven selling support retain gold despite its sharp decline.
- [Bill Ackman Says the Fed Is "About to Make Another Mistake" on Dec. 9](https://www.google.com/goto?url=CAESqQEBxCJF1-fB54hIClvksH8eMbgeVl2c7Z2Yz59sPSq20TeclP8uq6w74ZxLmRb0fnBkYEbIwuUzUGCCRQEQNExeEGNc1rOqSM-S8KfuidxE5HCNC73KLs8P785HdRy62FfgWH8b-2gk03QT0orzd15utCaGIU54FfYbbAQ2mogYpKwcWwfyCWHiwtZJiKjYZG8BoRe1lMkwkQCR0FD-YttXMcYOdp-JDSK6&gsessionid=A_KWxrweq2NUHAxqCnHBKlILSBaZwEdoYuKBkReUzLKZ02fsXWOX3Q)  
  <sub>24/7 Wall St., 23 hours ago</sub>  
  Bill Ackman says the Fed is "about to make another mistake on December 9th," as markets price a 96% chance of a hike hitting SPY and TLT.
- [Fundstrat's Tom Lee Sees Less Downside Into 2026 Year-End: Here's Why](https://www.google.com/goto?url=CAESvQEBxCJF18tuMzIUGKhpSI2ru0sLEJj7WMNahOD3aETJniOIUxzE8QD2KFNJt2jRTO3CI-njLuj422lw470hXf09i-dg9EEs3LhIuA3A4yD7vDw6JJNaC6GkbDkoVmzfs4JRGq2I13lnpMBHbaxLc8YTAOyeS67xvj0gseHIYMvS7XKLFfg7ziysOooB1lFA3omlTbs_RxEfaC5KWGFdnPz_Rg1JWcFThZBXPuEtCwSB4X39iKmdngDvP11SXac&gsessionid=A_KWxrweq2NUHAxqCnHBKlILSBaZwEdoYuKBkReUzLKZ02fsXWOX3Q)  
  <sub>TradingView, 8 hours ago</sub>  
  Fundstrat's Tom Lee said on Tuesday that while the market is concerned that 2026 is tracking like 2018, when stocks fell into year-end, the firm does not...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.16% (+0.01 on the week) | 5-year 4.62% (-0.26 on the week) | 10-year 4.83% (-0.24 on the week) | 30-year 5.24% (-0.17 on the week)
Yield curve, 10-year minus 3-month: +0.67 points -- upward sloping (normal)
US dollar index: 103.93 (+0.07 on the week)
Volatility (VIX): 31.72 (+7.2 on the week) -- stressed
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.1% (2026-10-01) | jobless claims 189k (2026-11-21)
Policy and expectations: Fed target 4.00% | market expects 2.1% inflation over 10 years
Rate path: 2-year Treasury 4.63% vs Fed target 3.75-4.00% -- the bond market prices about 3 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 82.46 (bar of 2026-11-25), from 502 daily bars
Trend: vs 20d SMA 81.06 (+1.7%), 50d 80.14 (+2.9%), 200d 84.04 (-1.9%); 50d below 200d
Momentum: RSI(14) 63.9 | MACD 0.264 vs signal 0.128 (histogram 0.135)
Returns: 1d +1.2% | 5d +2.8% | 1m +1.0% | 3m -0.8%
52-week range: 77.11 - 90.82 (now 39.0% of the way up)
Volatility: ATR(14) 0.78 (0.9% of price) | annualised 20d 11.5%
Volume: 0.17x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.10</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score +0.10</summary>

```text
Fund type: Long Government
Yield: 4.8%
Credit quality: AA 100.0% | US government debt 99.5%
Three-year record: +0.7% a year | beta to the market 2.30
Cost and size: expense ratio 0.15% | net assets 47.52B
What it is made of: Bonds 99.5%, Cash 0.5%
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
Contract: ULTRA UST BOND - CHICAGO BOARD OF TRADE (positions as of 2026-11-17, published the following Friday)
Large speculators: net short 35.5% of open interest (2,444,093 contracts)
Change on the week: -1.6% of open interest
Crowding: 35% percentile over 52 weeks -- within its normal range
Read this as crowding, not as a forecast: an extreme is as often the end of a move as the middle of one.
```

</details>

<details><summary><b>Money going into and out of this fund</b> — score -0.10</summary>

```text
Direction: flat (1 month)
Share count change: 1 week: +0.0% (0.00) over 7d | 1 month: +0.0% (0.00) over 32d
Shares outstanding: 109.70M | fund size: 9.05B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### US dollar (UUP) · Index fund — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:** no explanation. It wrote only “NEUTRAL”, so the main reasons below are all it gave.

**Main reasons it gave:**
- Dollar index +0.07% week‑over‑week, no significant move
- 10‑yr Treasury yield down 0.24% on the week, no rate hike surprise
- CFTC speculators net short 2.2% with -7.8% change (reduced short), modest bullish bias
- Price at 96.8% of 52‑week high, RSI 67, low volume, no decisive breakout
- Analyst view provides no rating, leaving analyst_score neutral

<details><summary><b>News</b> — score +0.00</summary>

- [The Dollar Just Hit Its Strongest Level Since March 2025](https://finance.yahoo.com/markets/currencies/articles/dollar-just-hit-strongest-level-175806416.html)  
  <sub>Yahoo Finance, 21 hours ago</sub>  
  UUP is up 10% this year, but the dollar's rally leans heavily on a Fed rate raise on December 9. Futures now price a December quarter-point hike at about...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.16% (+0.01 on the week) | 5-year 4.62% (-0.26 on the week) | 10-year 4.83% (-0.24 on the week) | 30-year 5.24% (-0.17 on the week)
Yield curve, 10-year minus 3-month: +0.67 points -- upward sloping (normal)
US dollar index: 103.93 (+0.07 on the week)
Volatility (VIX): 31.72 (+7.2 on the week) -- stressed
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.1% (2026-10-01) | jobless claims 189k (2026-11-21)
Policy and expectations: Fed target 4.00% | market expects 2.1% inflation over 10 years
Rate path: 2-year Treasury 4.63% vs Fed target 3.75-4.00% -- the bond market prices about 3 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 29.67 (bar of 2026-11-25), from 502 daily bars
Trend: vs 20d SMA 29.32 (+1.2%), 50d 29.04 (+2.2%), 200d 28.14 (+5.5%); 50d above 200d
Momentum: RSI(14) 67.1 | MACD 0.209 vs signal 0.184 (histogram 0.025)
Returns: 1d +0.2% | 5d +0.2% | 1m +1.9% | 3m +5.9%
52-week range: 26.47 - 29.78 (now 96.8% of the way up)
Volatility: ATR(14) 0.12 (0.4% of price) | annualised 20d 5.8%
Volume: 0.18x the 20-day average
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

<details><summary><b>Buying and selling by company insiders</b> — score +0.20</summary>

_Not available today._

</details>

<details><summary><b>Who is positioned how</b> — score +0.20</summary>

```text
Contract: USD INDEX - ICE FUTURES U.S. (positions as of 2026-11-17, published the following Friday)
Large speculators: net short 2.2% of open interest (55,775 contracts)
Change on the week: -7.8% of open interest
Crowding: 67% percentile over 52 weeks -- within its normal range
Read this as crowding, not as a forecast: an extreme is as often the end of a move as the middle of one.
```

</details>

<details><summary><b>Money going into and out of this fund</b> — score +0.20</summary>

```text
Direction: money coming in (1 month)
Share count change: 1 week: -0.8% (-4.06M) over 7d | 1 month: +8.3% (36.82M) over 32d
Shares outstanding: 16.16M | fund size: 479.67M
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Europe (VGK) · Index fund — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:** no explanation. It wrote only “NEUTRAL”, so the main reasons below are all it gave.

**Main reasons it gave:**
- No macro surprise: Treasury yields moved modestly, VIX up but no policy shift
- Technical indicators bearish (RSI 37.6, price below 20d/50d/200d SMAs) but no decisive break on volume
- Analyst coverage thin (12% of fund) despite bullish rating (83.8% buy, +33.7% price target)
- CFTC positioning shows modest net long increase (+1.6% OI) with high crowding (92% percentile)
- Fund fundamentals stable (P/E 16.7, 3-year return +15% p.a.)

<details><summary><b>News</b> — score +0.00</summary>

- [Liberation Day Round 2.0? The Next Wave of Trump Tariffs Is Reportedly Close](https://247wallst.com/investing/2026/11/25/liberation-day-round-2-0-the-next-wave-of-trump-tariffs-is-reportedly-close/)  
  <sub>24/7 Wall St., 3 hours ago</sub>  
  On April 2, 2025, the S&P 500 closed at 5,670.97. Over the next two sessions, it fell 4.84% and 5.97% and closed at 5,074.08. That 10.5% two-day drop is the...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.16% (+0.01 on the week) | 5-year 4.62% (-0.26 on the week) | 10-year 4.83% (-0.24 on the week) | 30-year 5.24% (-0.17 on the week)
Yield curve, 10-year minus 3-month: +0.67 points -- upward sloping (normal)
US dollar index: 103.93 (+0.07 on the week)
Volatility (VIX): 31.72 (+7.2 on the week) -- stressed
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.1% (2026-10-01) | jobless claims 189k (2026-11-21)
Policy and expectations: Fed target 4.00% | market expects 2.1% inflation over 10 years
Rate path: 2-year Treasury 4.63% vs Fed target 3.75-4.00% -- the bond market prices about 3 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 83.55 (bar of 2026-11-25), from 502 daily bars
Trend: vs 20d SMA 87.26 (-4.3%), 50d 87.17 (-4.2%), 200d 87.84 (-4.9%); 50d below 200d
Momentum: RSI(14) 37.6 | MACD -0.958 vs signal -0.428 (histogram -0.530)
Returns: 1d -1.5% | 5d -2.7% | 1m -4.0% | 3m -9.5%
52-week range: 79.18 - 93.19 (now 31.2% of the way up)
Volatility: ATR(14) 1.26 (1.5% of price) | annualised 20d 24.7%
Volume: 0.05x the 20-day average
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
Three-year record: +15.0% a year | beta to the market 0.88
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

<details><summary><b>What analysts and big funds say</b> — score +0.50</summary>

_Not available today._

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score +0.50</summary>

```text
Rolled up from the 5 largest holdings, 12.0% of the fund by weight  -- thin, so read this as a fact about that slice rather than the fund
Ratings by weight: buy 83.8% | hold 16.2% | sell 0.0% (mean 2.08 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +33.7% above the current prices
Holdings read: ASML.AS, ROP.SW, SHEL.L, NOVN.SW, HSBA.L
Recent rating changes among them: none reported
```

</details>

<details><summary><b>Buying and selling by company insiders</b> — score +0.20</summary>

_Not available today._

</details>

<details><summary><b>Who is positioned how</b> — score +0.20</summary>

```text
Contract: MSCI EAFE  - ICE FUTURES U.S. (positions as of 2026-11-17, published the following Friday)
Large speculators: net long 4.3% of open interest (512,671 contracts)
Change on the week: +1.6% of open interest
Crowding: 92% percentile over 52 weeks -- a crowded long by the standards of the past year
Read this as crowding, not as a forecast: an extreme is as often the end of a move as the middle of one.
```

</details>

<details><summary><b>Money going into and out of this fund</b> — score +0.20</summary>

```text
Direction: money coming in (1 month)
Share count change: 1 week: +5.5% (1.91B) over 8d | 1 month: +3.7% (1.32B) over 33d
Shares outstanding: 439.58M | fund size: 36.73B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Emerging markets (VWO) · Index fund — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:** no explanation. It wrote only “NEUTRAL”, so the main reasons below are all it gave.

**Main reasons it gave:**
- No macro surprise: US yields down slightly, VIX up but no policy shift
- Technical trend bearish: price below 20d, 50d, 200d SMAs, RSI 34, low volume
- Analyst view bullish on top holdings but only 22.6% coverage
- Positioning flat: net short 0% with -2.2% change, indicating slight reduction in short bias

<details><summary><b>News</b> — score +0.00</summary>

- [Prime Buchholz LLC's Vanguard FTSE Emerging Markets ETF(VWO) Holding History](https://www.gurufocus.com/guru-portfolio/Prime%20Buchholz%20LLC/VWO)  
  <sub>GuruFocus, 17 hours ago</sub>  
  Vanguard FTSE Emerging Markets ETF(VWO) Buys and Sells Made by Prime Buchholz LLC. Latest and Historical Data and Chart.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.16% (+0.01 on the week) | 5-year 4.62% (-0.26 on the week) | 10-year 4.83% (-0.24 on the week) | 30-year 5.24% (-0.17 on the week)
Yield curve, 10-year minus 3-month: +0.67 points -- upward sloping (normal)
US dollar index: 103.93 (+0.07 on the week)
Volatility (VIX): 31.72 (+7.2 on the week) -- stressed
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.1% (2026-10-01) | jobless claims 189k (2026-11-21)
Policy and expectations: Fed target 4.00% | market expects 2.1% inflation over 10 years
Rate path: 2-year Treasury 4.63% vs Fed target 3.75-4.00% -- the bond market prices about 3 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score -0.20</summary>

```text
Last close 51.19 (bar of 2026-11-25), from 502 daily bars
Trend: vs 20d SMA 54.79 (-6.6%), 50d 57.38 (-10.8%), 200d 58.14 (-11.9%); 50d below 200d
Momentum: RSI(14) 34.1 | MACD -1.483 vs signal -1.191 (histogram -0.292)
Returns: 1d -3.2% | 5d -4.8% | 1m -9.9% | 3m -16.1%
52-week range: 50.62 - 61.44 (now 5.3% of the way up)
Volatility: ATR(14) 1.25 (2.4% of price) | annualised 20d 36.8%
Volume: 0.09x the 20-day average
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
Three-year record: +12.9% a year | beta to the market 0.78
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

<details><summary><b>What analysts and big funds say</b> — score +0.35</summary>

_Not available today._

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score +0.35</summary>

```text
Rolled up from the 5 largest holdings, 22.6% of the fund by weight  -- thin, so read this as a fact about that slice rather than the fund
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 1.31 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +64.4% above the current prices
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
Share count change: 1 week: +0.0% (0.00) over 7d | 1 month: +0.0% (0.00) over 32d
Shares outstanding: 1.42B | fund size: 72.59B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

## Sector and country funds

### Argentina (ARGT) · Sector or country — NEUTRAL, confidence 0.12

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> The fund shows modest fundamentals (mid‑single‑digit valuation multiples, low beta and steady three‑year return) and bullish analyst coverage (+79.5% price target on 51% of the portfolio). Recent inflows (+4.9% weekly share increase) add a bullish tilt, but technicals are clearly bearish – price is well below its 20/50/200‑day moving averages and momentum indicators (RSI 24.7, MACD histogram) are negative. Macro data show only incremental changes in yields and a high VIX, with no surprise policy or data releases. With no clear macro catalyst or decisive technical breakout, the overall view remains neutral.

**Main reasons it gave:**
- 1‑week share count up 4.9% indicating net inflows
- Analyst coverage of 51.1% of fund weight with 100% buy rating and +79.5% price target
- Price below 20‑day, 50‑day and 200‑day SMAs; RSI 24.7 (oversold) and MACD histogram negative
- Macro yields modestly higher and VIX elevated at 31.7, but no surprise data or policy moves
- Fund fundamentals: P/E 13.9, P/B 1.59, low beta 0.44, expense ratio 0.59%

<details><summary><b>News</b> — score +0.00</summary>

- [ARGT Dec 2027 85.000 call (ARGT271217C00085000) Stock Price, News, Quote & History](https://ca.finance.yahoo.com/quote/ARGT271217C00085000/)  
  <sub>Yahoo! Finance Canada, 16 hours ago</sub>  
  Find the latest ARGT Dec 2027 85.000 call (ARGT271217C00085000) stock quote, history, news and other vital information to help you with your stock trading...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.16% (+0.01 on the week) | 5-year 4.62% (-0.26 on the week) | 10-year 4.83% (-0.24 on the week) | 30-year 5.24% (-0.17 on the week)
Yield curve, 10-year minus 3-month: +0.67 points -- upward sloping (normal)
US dollar index: 103.93 (+0.07 on the week)
Volatility (VIX): 31.72 (+7.2 on the week) -- stressed
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.1% (2026-10-01) | jobless claims 189k (2026-11-21)
Policy and expectations: Fed target 4.00% | market expects 2.1% inflation over 10 years
Rate path: 2-year Treasury 4.63% vs Fed target 3.75-4.00% -- the bond market prices about 3 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score -0.50</summary>

```text
Last close 64.76 (bar of 2026-11-25), from 502 daily bars
Trend: vs 20d SMA 72.63 (-10.8%), 50d 81.76 (-20.8%), 200d 89.79 (-27.9%); 50d below 200d
Momentum: RSI(14) 24.7 | MACD -4.898 vs signal -4.500 (histogram -0.399)
Returns: 1d -2.3% | 5d -6.4% | 1m -21.9% | 3m -31.2%
52-week range: 64.56 - 102.94 (now 0.5% of the way up)
Volatility: ATR(14) 2.20 (3.4% of price) | annualised 20d 37.2%
Volume: 0.17x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.20</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score +0.20</summary>

```text
Fund type: Focused Region
What it holds: P/E 13.90 | P/B 1.59 | P/S 1.22 | 3y earnings growth n/a
Yield: 1.3%
Three-year record: +14.6% a year | beta to the market 0.44
Cost and size: expense ratio 0.59% | net assets 620.12M
What it is made of: Stocks 100.0%, Cash 0.1%
Largest holdings: MercadoLibre Inc 22.2%, YPF SA ADR 10.6%, Vista Energy SAB de CV ADR 8.2%, Grupo Financiero Galicia SA ADR 5.4%, Pampa Energia SA ADR 4.8%
Sector mix: Consumer cyclical 28.3%, Energy 22.6%, Financial services 13.7%, Basic materials 10.3%
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
Rolled up from the 5 largest holdings, 51.1% of the fund by weight
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 1.61 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +79.5% above the current prices
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
Share count change: 1 week: +4.9% (27.79M) over 7d | 1 month: +9.7% (52.74M) over 32d
Shares outstanding: 9.20M | fund size: 595.61M
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Israel (EIS) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Neutral overall – technicals are bearish but low‑volume and not a decisive break; fund flows are flat indicating no net demand; analyst coverage is strongly bullish but only spans 39.6% of the fund; macro environment shows stress (VIX up) with no policy surprise.

**Main reasons it gave:**
- Technical indicators bearish (RSI 32.2, MACD -4.03) with low volume (0.06x 20‑day avg) – no decisive break
- Fund flows flat (share count unchanged) – no net demand
- Analyst coverage limited to 39.6% of fund, rating 100% buy but weight small
- Macro stress: VIX up 7.2 points to 31.7, no policy surprise

<details><summary><b>News</b> — score +0.00</summary>

_No news found for this one today._

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.16% (+0.01 on the week) | 5-year 4.62% (-0.26 on the week) | 10-year 4.83% (-0.24 on the week) | 30-year 5.24% (-0.17 on the week)
Yield curve, 10-year minus 3-month: +0.67 points -- upward sloping (normal)
US dollar index: 103.93 (+0.07 on the week)
Volatility (VIX): 31.72 (+7.2 on the week) -- stressed
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.1% (2026-10-01) | jobless claims 189k (2026-11-21)
Policy and expectations: Fed target 4.00% | market expects 2.1% inflation over 10 years
Rate path: 2-year Treasury 4.63% vs Fed target 3.75-4.00% -- the bond market prices about 3 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score -0.30</summary>

```text
Last close 102.01 (bar of 2026-11-25), from 502 daily bars
Trend: vs 20d SMA 110.30 (-7.5%), 50d 116.92 (-12.8%), 200d 122.29 (-16.6%); 50d below 200d
Momentum: RSI(14) 32.2 | MACD -4.029 vs signal -3.245 (histogram -0.784)
Returns: 1d -1.7% | 5d -5.7% | 1m -18.0% | 3m -18.5%
52-week range: 101.51 - 137.69 (now 1.4% of the way up)
Volatility: ATR(14) 2.61 (2.6% of price) | annualised 20d 37.2%
Volume: 0.06x the 20-day average
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
Three-year record: +26.6% a year | beta to the market 0.98
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

<details><summary><b>What analysts and big funds say</b> — score +1.00</summary>

_Not available today._

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score +1.00</summary>

```text
Rolled up from the 5 largest holdings, 39.6% of the fund by weight
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 1.00 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +31.7% above the current prices
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
Shares outstanding: 2.55M | fund size: 260.13M
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Poland (EPOL) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Mixed signals – bullish analyst view and strong inflows versus bearish short‑term technicals and a stressed macro backdrop (high VIX). No material macro surprise or decisive technical break, so overall neutral.

**Main reasons it gave:**
- RSI 34.4 indicating oversold momentum
- Analyst ratings 57.7% buy and +18.2% price target
- Share count up 30.7% over past month
- VIX 31.72 up 7.2 points, indicating stressed market

<details><summary><b>News</b> — score +0.00</summary>

_No news found for this one today._

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.16% (+0.01 on the week) | 5-year 4.62% (-0.26 on the week) | 10-year 4.83% (-0.24 on the week) | 30-year 5.24% (-0.17 on the week)
Yield curve, 10-year minus 3-month: +0.67 points -- upward sloping (normal)
US dollar index: 103.93 (+0.07 on the week)
Volatility (VIX): 31.72 (+7.2 on the week) -- stressed
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.1% (2026-10-01) | jobless claims 189k (2026-11-21)
Policy and expectations: Fed target 4.00% | market expects 2.1% inflation over 10 years
Rate path: 2-year Treasury 4.63% vs Fed target 3.75-4.00% -- the bond market prices about 3 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score -0.20</summary>

```text
Last close 39.85 (bar of 2026-11-25), from 502 daily bars
Trend: vs 20d SMA 42.83 (-7.0%), 50d 43.68 (-8.8%), 200d 40.84 (-2.4%); 50d above 200d
Momentum: RSI(14) 34.4 | MACD -0.836 vs signal -0.487 (histogram -0.349)
Returns: 1d -2.6% | 5d -6.7% | 1m -9.7% | 3m -8.6%
52-week range: 33.44 - 45.76 (now 52.0% of the way up)
Volatility: ATR(14) 0.92 (2.3% of price) | annualised 20d 34.4%
Volume: 0.07x the 20-day average
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
Three-year record: +30.2% a year | beta to the market 0.85
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
Weighted price target: +18.2% above the current prices
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
Share count change: 1 week: +5.4% (50.56M) over 7d | 1 month: +30.7% (231.70M) over 32d
Shares outstanding: 24.75M | fund size: 986.23M
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Australia (EWA) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Mixed signals: negative macro surprise (Australian inflation 4.9% > 4.7% expectations), bearish technicals (price below 20‑, 50‑ and 200‑day SMAs), analyst sell bias (weighted rating 3.45, price target -3.3%), but strong inflows (share count +7.2% week, +11% month).

**Main reasons it gave:**
- Australian inflation 4.9% exceeds expectations (negative surprise)
- Share count up 7.2% in one week (positive flow)
- Price below 20‑, 50‑, 200‑day SMAs (bearish technical)
- Analyst rating weighted mean 3.45 (sell bias)

<details><summary><b>News</b> — score -0.20</summary>

- [EWA Apr 2027 23.000 call (EWA270416C00023000) Interactive Stock Chart - Yahoo Finance](https://ca.finance.yahoo.com/quote/EWA270416C00023000/chart/)  
  <sub>Yahoo! Finance Canada, 24 hours ago</sub>  
  Interactive Chart for EWA Apr 2027 23.000 call (EWA270416C00023000), analyze all the data with a huge range of indicators.
- [Australia's October inflation tops forecasts at 4.9% as energy costs surge](https://seekingalpha.com/news/4676435-australias-october-inflation-tops-forecasts-at-49-as-energy-costs-surge)  
  <sub>Seeking Alpha, 10 hours ago</sub>  
  Australia's annual inflation rate accelerated to 4.9% in October 2026 from 4.3% in September, surpassing market expectations of 4.7% and moving further...
- [IAF: Finding Value Down Under, In A Market Where Value Is Hard To Find (Rating Upgrade)](https://www.google.com/goto?url=CAESuAEBxCJF159RM84VUIUmMA9t7ohKMeuwTJnJ1zziRD-plV6zVPAMTsiE_Nl_6fNUlhFh7sYuuAHrIoZ7NWQakpjxYUebWv-dSwtUnpivWkioAxyUjksIdI67-gyFsZzDfaEPvVseMnq42e0qvcvpEuFyoAQRHGpRbFwZ81_n8bddXj19CA_wnTJTFgK0T-Q97QcEwZqvzXXOpiqGtoQg-Cz2fyMQXJi8e7Xd15KwrCK3lwLFBLvDJjMu&gsessionid=Bxsn85S1f8NZCxBtrUOG9uHNtRuAzrLYpm-rHlHE8QcYVT1A-EZwYg)  
  <sub>Seeking Alpha, 18 hours ago</sub>  
  The abrdn Australia Equity Fund is evaluated as an investment at its current market price. IAF fund has a 13% discount to NAV, which is attractive in an...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score -0.20</summary>

```text
US Treasury yields: 3-month 4.16% (+0.01 on the week) | 5-year 4.62% (-0.26 on the week) | 10-year 4.83% (-0.24 on the week) | 30-year 5.24% (-0.17 on the week)
Yield curve, 10-year minus 3-month: +0.67 points -- upward sloping (normal)
US dollar index: 103.93 (+0.07 on the week)
Volatility (VIX): 31.72 (+7.2 on the week) -- stressed
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.1% (2026-10-01) | jobless claims 189k (2026-11-21)
Policy and expectations: Fed target 4.00% | market expects 2.1% inflation over 10 years
Rate path: 2-year Treasury 4.63% vs Fed target 3.75-4.00% -- the bond market prices about 3 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score -0.40</summary>

```text
Last close 26.88 (bar of 2026-11-25), from 502 daily bars
Trend: vs 20d SMA 28.63 (-6.1%), 50d 28.69 (-6.3%), 200d 28.97 (-7.2%); 50d below 200d
Momentum: RSI(14) 31.1 | MACD -0.542 vs signal -0.296 (histogram -0.245)
Returns: 1d -1.5% | 5d -3.2% | 1m -8.8% | 3m -10.7%
52-week range: 25.58 - 30.43 (now 26.8% of the way up)
Volatility: ATR(14) 0.42 (1.6% of price) | annualised 20d 20.9%
Volume: 0.16x the 20-day average
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
Three-year record: +10.7% a year | beta to the market 0.94
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

<details><summary><b>What analysts and big funds say</b> — score -0.45</summary>

_Not available today._

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score -0.45</summary>

```text
Rolled up from the 5 largest holdings, 46.5% of the fund by weight
Ratings by weight: buy 0.0% | hold 57.4% | sell 42.6% (mean 3.45 on a 1=strong buy to 5=strong sell scale)
Weighted price target: -3.3% above the current prices
Holdings read: BHP.AX, CBA.AX, NAB.AX, WBC.AX, ANZ.AX
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
Share count change: 1 week: +7.2% (83.52M) over 8d | 1 month: +11.0% (122.91M) over 33d
Shares outstanding: 46.05M | fund size: 1.24B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Canada (EWC) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Technical indicators show bearish momentum, but recent strong inflows and a largely bullish analyst consensus offset the downside, while macro conditions remain unchanged, leading to a neutral overall stance.

**Main reasons it gave:**
- Technical: price 55.62 below 20d SMA 59.08, 50d SMA 59.52, 200d SMA 58.62; RSI 33, MACD negative (bearish momentum)
- Fund flows: share count +6.8% week, +17.9% month indicating strong inflows (bullish demand)
- Analyst coverage: 87.2% buy on 29.5% of holdings, weighted price target +17% (moderate bullish outlook)
- Macro: no policy or data surprise, yields stable, VIX high but unchanged (neutral backdrop)

<details><summary><b>News</b> — score +0.00</summary>

- [CORO: Country Picks That Have Paid Off So Far (NASDAQ:CORO)](https://seekingalpha.com/article/4971650-coro-country-picks-that-have-paid-off-so-far?source=feed_tag_etf_analysis)  
  <sub>Seeking Alpha, 3 hours ago</sub>  
  The iShares International Country Rotation Active ETF is a “Buy” for its encouraging start and timely international exposure, with prudent sizing.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.16% (+0.01 on the week) | 5-year 4.62% (-0.26 on the week) | 10-year 4.83% (-0.24 on the week) | 30-year 5.24% (-0.17 on the week)
Yield curve, 10-year minus 3-month: +0.67 points -- upward sloping (normal)
US dollar index: 103.93 (+0.07 on the week)
Volatility (VIX): 31.72 (+7.2 on the week) -- stressed
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.1% (2026-10-01) | jobless claims 189k (2026-11-21)
Policy and expectations: Fed target 4.00% | market expects 2.1% inflation over 10 years
Rate path: 2-year Treasury 4.63% vs Fed target 3.75-4.00% -- the bond market prices about 3 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score -0.50</summary>

```text
Last close 55.62 (bar of 2026-11-25), from 502 daily bars
Trend: vs 20d SMA 59.08 (-5.9%), 50d 59.52 (-6.5%), 200d 58.62 (-5.1%); 50d above 200d
Momentum: RSI(14) 33.0 | MACD -1.182 vs signal -0.699 (histogram -0.483)
Returns: 1d -1.4% | 5d -2.8% | 1m -8.9% | 3m -10.7%
52-week range: 51.56 - 62.64 (now 36.6% of the way up)
Volatility: ATR(14) 0.98 (1.8% of price) | annualised 20d 24.1%
Volume: 0.14x the 20-day average
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
Three-year record: +20.0% a year | beta to the market 0.73
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

<details><summary><b>What analysts and big funds say</b> — score +0.40</summary>

_Not available today._

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score +0.40</summary>

```text
Rolled up from the 5 largest holdings, 29.5% of the fund by weight
Ratings by weight: buy 87.2% | hold 12.8% | sell 0.0% (mean 2.20 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +17.0% above the current prices
Holdings read: RY, TD, SHOP, BMO.TO, CNQ.TO
Recent rating changes among them:
  - RY: 2025-08-29 Argus Research: main, Buy -> Buy
  - TD: 2026-06-01 RBC Capital: main, Outperform -> Outperform
  - SHOP: 2026-11-05 Argus Research: reit, Buy -> Buy
  - BMO.TO: 2026-05-28 RBC Capital: main, Sector Perform -> Sector Perform
  - CNQ.TO: 2026-03-12 Goldman Sachs: main, Buy -> Buy
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
Share count change: 1 week: +6.8% (480.68M) over 8d | 1 month: +17.9% (1.14B) over 33d
Shares outstanding: 134.87M | fund size: 7.50B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Sweden (EWD) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> No macro surprise; technicals show price below SMAs and negative momentum but low volume; analyst coverage is uniformly bullish with a +14.7% price target; fund inflows are strong (+5.1% week, +18.4% month). The mix of positive fundamentals and demand is offset by bearish technicals and lack of a macro catalyst, leading to a neutral overall view.

**Main reasons it gave:**
- No macro data surprise (inflation, unemployment, jobless claims within expectations)
- Price below 20‑day, 50‑day, 200‑day SMAs; RSI 39.1, MACD negative
- Analyst coverage 100% buy; weighted price target +14.7% above current
- Fund inflows: share count +5.1% week, +18.4% month

<details><summary><b>News</b> — score +0.00</summary>

_No news found for this one today._

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.16% (+0.01 on the week) | 5-year 4.62% (-0.26 on the week) | 10-year 4.83% (-0.24 on the week) | 30-year 5.24% (-0.17 on the week)
Yield curve, 10-year minus 3-month: +0.67 points -- upward sloping (normal)
US dollar index: 103.93 (+0.07 on the week)
Volatility (VIX): 31.72 (+7.2 on the week) -- stressed
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.1% (2026-10-01) | jobless claims 189k (2026-11-21)
Policy and expectations: Fed target 4.00% | market expects 2.1% inflation over 10 years
Rate path: 2-year Treasury 4.63% vs Fed target 3.75-4.00% -- the bond market prices about 3 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score -0.30</summary>

```text
Last close 49.38 (bar of 2026-11-25), from 502 daily bars
Trend: vs 20d SMA 51.75 (-4.6%), 50d 51.18 (-3.5%), 200d 51.44 (-4.0%); 50d below 200d
Momentum: RSI(14) 39.1 | MACD -0.512 vs signal -0.133 (histogram -0.379)
Returns: 1d -1.2% | 5d -2.9% | 1m -3.6% | 3m -8.4%
52-week range: 46.79 - 54.72 (now 32.7% of the way up)
Volatility: ATR(14) 0.86 (1.7% of price) | annualised 20d 27.9%
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
Three-year record: +15.5% a year | beta to the market 1.18
Cost and size: expense ratio 0.51% | net assets 1.10B
What it is made of: Stocks 99.2%, Cash 0.8%
Largest holdings: Spotify Technology SA 11.4%, Investor AB Class B 9.9%, Volvo AB Class B 6.4%, Atlas Copco AB Class A 6.2%, Sandvik AB 4.9%
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
Rolled up from the 4 largest holdings, 29.0% of the fund by weight
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 1.98 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +14.7% above the current prices
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
Share count change: 1 week: +5.1% (52.42M) over 8d | 1 month: +18.4% (168.99M) over 33d
Shares outstanding: 22.01M | fund size: 1.09B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Germany (EWG) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Neutral overall view; bullish analyst coverage is offset by weak German GDP revision and bearish technicals, while fund flows are flat.

**Main reasons it gave:**
- German Q3 GDP revised down to 0.1% (weak exports and investment)
- Technical indicators bearish: price below 20‑day, 50‑day, 200‑day SMAs; RSI 36; MACD negative
- Analyst coverage bullish: 78% buy, weighted price target +26.5% above current price
- Fund flows flat: share count unchanged over week and month

<details><summary><b>News</b> — score +0.00</summary>

- [iShares MSCI Germany ETF (EWG.MX) Seasonal returns chart](https://uk.finance.yahoo.com/quote/EWG.MX/seasonality/)  
  <sub>Yahoo Finance UK, 22 hours ago</sub>  
  iShares MSCI Germany ETF (EWG.MX) seasonal returns chart provides the mean and median returns by month to inform your investment strategy.
- [CORO: Country Picks That Have Paid Off So Far (NASDAQ:CORO)](https://seekingalpha.com/article/4971650-coro-country-picks-that-have-paid-off-so-far?source=feed_tag_etf_analysis)  
  <sub>Seeking Alpha, 3 hours ago</sub>  
  The iShares International Country Rotation Active ETF is a “Buy” for its encouraging start and timely international exposure, with prudent sizing.
- [Germany's Q3 GDP growth cut to 0.1% on weaker exports and investment (EWG:NYSEARCA)](https://www.google.com/goto?url=CAESogEBxCJF17Y9KaQD9xYaLWKs9I18V6Xv1cT3qHlqK7CnOLGR8gYRhpI-14yumIDI-MiZRqXnOH9fHWKPYUMzerNryNjwZdybpUveAewZJhgvxy_cRL1FdFraLJy3Y9omtObPfpvinFxK001Fi5PXY5m4CBaiV53-uEjh6yOd-ohMOwQGy0nIKie6vEUilTNs7IBC68_mUmvHGpwvWJBGV_d57ik&gsessionid=DXURgaf39CWHsOII9VvwUCEIti3dswVlfnQOAVyjCCU2ceAGG3R0QA)  
  <sub>Seeking Alpha, 7 hours ago</sub>  
  Germany's Q3 2026 GDP grew 0.1%, revised down from 0.2%, as weaker exports, declining retail sales and falling business investment weighed.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.16% (+0.01 on the week) | 5-year 4.62% (-0.26 on the week) | 10-year 4.83% (-0.24 on the week) | 30-year 5.24% (-0.17 on the week)
Yield curve, 10-year minus 3-month: +0.67 points -- upward sloping (normal)
US dollar index: 103.93 (+0.07 on the week)
Volatility (VIX): 31.72 (+7.2 on the week) -- stressed
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.1% (2026-10-01) | jobless claims 189k (2026-11-21)
Policy and expectations: Fed target 4.00% | market expects 2.1% inflation over 10 years
Rate path: 2-year Treasury 4.63% vs Fed target 3.75-4.00% -- the bond market prices about 3 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score -0.30</summary>

```text
Last close 39.48 (bar of 2026-11-25), from 502 daily bars
Trend: vs 20d SMA 41.75 (-5.4%), 50d 41.62 (-5.1%), 200d 42.08 (-6.2%); 50d below 200d
Momentum: RSI(14) 36.1 | MACD -0.549 vs signal -0.214 (histogram -0.335)
Returns: 1d -1.5% | 5d -3.8% | 1m -4.9% | 3m -11.4%
52-week range: 38.08 - 44.59 (now 21.5% of the way up)
Volatility: ATR(14) 0.73 (1.8% of price) | annualised 20d 28.6%
Volume: 0.06x the 20-day average
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
Three-year record: +15.1% a year | beta to the market 0.95
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

<details><summary><b>What analysts and big funds say</b> — score +0.50</summary>

_Not available today._

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score +0.50</summary>

```text
Rolled up from the 5 largest holdings, 45.1% of the fund by weight
Ratings by weight: buy 78.0% | hold 22.0% | sell 0.0% (mean 1.99 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +26.5% above the current prices
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
Shares outstanding: 79.50M | fund size: 3.14B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Italy (EWI) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> The fund shows mixed signals: bullish analyst coverage (90.8% buy, +24.4% price target) and strong inflows (+6.2% share count in one week) are offset by bearish technicals (price below 20‑, 50‑, 200‑day SMAs; RSI 36; negative MACD) and a stressed macro environment (VIX up to 31.72). The recent manager change is material but its impact is uncertain, so the overall view remains neutral.

**Main reasons it gave:**
- Price below 20‑day, 50‑day and 200‑day SMAs; RSI 36 and negative MACD indicate bearish technical momentum
- VIX up 7.2 points to 31.72, showing heightened market stress
- Fund flows: share count rose 6.2% in one week, indicating fresh inflows
- Analyst coverage: 90.8% buy rating and price target +24.4% above current price
- Management change: Saba Capital Management appointed as new manager with £565 m tender offer

<details><summary><b>News</b> — score +0.00</summary>

- [Saba to replace Baillie Gifford at Edinburgh Worldwide, with £565m tender offer and shift to discounted closed-end funds](https://www.scottishfinancialnews.com/articles/saba-to-replace-baillie-gifford-at-edinburgh-worldwide-with-ps565m-tender-offer-and-shift-to-discounted-closed-end-funds)  
  <sub>Scottish Financial News, 7 hours ago</sub>  
  The board of Edinburgh Worldwide Investment Trust (EWI) has proposed a new investment strategy, appoint Saba Capital Management as its new fund manager,...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.16% (+0.01 on the week) | 5-year 4.62% (-0.26 on the week) | 10-year 4.83% (-0.24 on the week) | 30-year 5.24% (-0.17 on the week)
Yield curve, 10-year minus 3-month: +0.67 points -- upward sloping (normal)
US dollar index: 103.93 (+0.07 on the week)
Volatility (VIX): 31.72 (+7.2 on the week) -- stressed
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.1% (2026-10-01) | jobless claims 189k (2026-11-21)
Policy and expectations: Fed target 4.00% | market expects 2.1% inflation over 10 years
Rate path: 2-year Treasury 4.63% vs Fed target 3.75-4.00% -- the bond market prices about 3 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score -0.40</summary>

```text
Last close 53.78 (bar of 2026-11-25), from 502 daily bars
Trend: vs 20d SMA 56.73 (-5.2%), 50d 57.25 (-6.1%), 200d 58.24 (-7.7%); 50d below 200d
Momentum: RSI(14) 36.0 | MACD -0.726 vs signal -0.364 (histogram -0.361)
Returns: 1d -1.9% | 5d -3.8% | 1m -3.7% | 3m -13.5%
52-week range: 50.70 - 63.35 (now 24.3% of the way up)
Volatility: ATR(14) 0.98 (1.8% of price) | annualised 20d 31.3%
Volume: 0.01x the 20-day average
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
Three-year record: +23.5% a year | beta to the market 0.92
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

<details><summary><b>What analysts and big funds say</b> — score +0.50</summary>

_Not available today._

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score +0.50</summary>

```text
Rolled up from the 5 largest holdings, 52.1% of the fund by weight
Ratings by weight: buy 90.8% | hold 9.2% | sell 0.0% (mean 2.14 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +24.4% above the current prices
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
Share count change: 1 week: +6.2% (68.03M) over 8d | 1 month: +4.3% (48.01M) over 33d
Shares outstanding: 21.72M | fund size: 1.17B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Japan (EWJ) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Neutral overall as no material macro surprise or decisive technical break is present; bullish analyst and insider signals are modest and offset by negative technicals and recent sell‑off news.

**Main reasons it gave:**
- Asian equities sell‑off due to hot inflation data in Japan and Australia
- Technical downtrend: price below 20‑day, 50‑day, and 200‑day SMAs, RSI 35.5, negative MACD
- Modest net long position (+3.6%) and increase (+1.4%) in NIKKEI futures speculators
- Fund inflows: share count up 4.5% weekly and 9.1% monthly indicating demand
- Analyst coverage thin (17.2% of fund) but all‑buy ratings with +34.8% price target

<details><summary><b>News</b> — score +0.00</summary>

- [1 TRY to IGV: Live Exchange Rate](https://www.weex.com/tokens/ishares-expanded-tech-software-etf-derivatives/from-try)  
  <sub>WEEX, 20 hours ago</sub>  
  Convert TRY to IGV in real time. Check the latest TRY to IGV rate, conversion tables, and price charts with WEEX's free converter.
- [1 JPY to IGV: Live Exchange Rate](https://www.weex.com/tokens/ishares-expanded-tech-software-etf-derivatives/from-jpy)  
  <sub>WEEX, 23 hours ago</sub>  
  The Japanese yen (JPY) is the official currency of Japan. It is issued by the Bank of Japan and subdivided into 100 sen (though sen are not used in...
- [Asian stocks sell off broadly on hot inflation data and U.S. tariff concerns](https://www.google.com/goto?url=CAESqwEBxCJF19egWc7llh4JARpnjmfY3QT47jS3T-lZMibelAEFSUKexj5WwbZP_dS_TeXxDy31s0GOIpu-TfVANMvdJdTXtnFddtdWnVMNwdJevB_W3Mvpewe4ZiZ8y2arGBjhD9Y7GRpOsFGrgLcnGvX-4FVnXYfzazoQ8dilnvimKP97cMQaWWA24XKWnWtQZWoJ9C4cx10yJmBiAp7-zrdNNN1mK83QC2Leh84&gsessionid=3hbJ5Vy2eSYw28GDs1rpNjSnv7UKa3aU86vBxXj8bTqOkC_nLEzyIA)  
  <sub>Seeking Alpha, 9 hours ago</sub>  
  Asian equity markets traded broadly lower on Wednesday, weighed down by hotter-than-expected inflation data in Japan and Australia, escalating U.S. tariff...
- [Top Tokenized ETFs by Market Cap](https://www.google.com/goto?url=CAESXAHEIkXXitOC8gvINnLl8AQF3dMGB84xOcknz93-xNE9tYNxzyANh4eS4OjzQTLPTndOIclqWX8TQVObvhTY_uQd8Z6EnaO9_xJnNcmIuUAzu1nw5avA2yP5l6Tq&gsessionid=3hbJ5Vy2eSYw28GDs1rpNjSnv7UKa3aU86vBxXj8bTqOkC_nLEzyIA)  
  <sub>Coingecko, 13 hours ago</sub>  
  Discover the top ETFs (exchange-traded funds) by tokenized market cap. Track ETF prices alongside their tokenized prices, market cap,...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.16% (+0.01 on the week) | 5-year 4.62% (-0.26 on the week) | 10-year 4.83% (-0.24 on the week) | 30-year 5.24% (-0.17 on the week)
Yield curve, 10-year minus 3-month: +0.67 points -- upward sloping (normal)
US dollar index: 103.93 (+0.07 on the week)
Volatility (VIX): 31.72 (+7.2 on the week) -- stressed
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.1% (2026-10-01) | jobless claims 189k (2026-11-21)
Policy and expectations: Fed target 4.00% | market expects 2.1% inflation over 10 years
Rate path: 2-year Treasury 4.63% vs Fed target 3.75-4.00% -- the bond market prices about 3 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score -0.20</summary>

```text
Last close 85.42 (bar of 2026-11-25), from 502 daily bars
Trend: vs 20d SMA 89.84 (-4.9%), 50d 93.97 (-9.1%), 200d 92.05 (-7.2%); 50d above 200d
Momentum: RSI(14) 35.5 | MACD -2.347 vs signal -1.991 (histogram -0.356)
Returns: 1d -1.4% | 5d -3.0% | 1m -10.3% | 3m -10.9%
52-week range: 79.74 - 99.32 (now 29.0% of the way up)
Volatility: ATR(14) 1.89 (2.2% of price) | annualised 20d 36.5%
Volume: 0.12x the 20-day average
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
Three-year record: +14.9% a year | beta to the market 0.86
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

<details><summary><b>What analysts and big funds say</b> — score +0.25</summary>

_Not available today._

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score +0.25</summary>

```text
Rolled up from the 5 largest holdings, 17.2% of the fund by weight  -- thin, so read this as a fact about that slice rather than the fund
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 1.66 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +34.8% above the current prices
Holdings read: 8306.T, 7203.T, 6857.T, 6098.T, 8316.T
Recent rating changes among them: none reported
```

</details>

<details><summary><b>Buying and selling by company insiders</b> — score +0.15</summary>

_Not available today._

</details>

<details><summary><b>Who is positioned how</b> — score +0.15</summary>

```text
Contract: NIKKEI STOCK AVERAGE YEN DENOM - CHICAGO MERCANTILE EXCHANGE (positions as of 2026-11-17, published the following Friday)
Large speculators: net long 3.6% of open interest (28,271 contracts)
Change on the week: +1.4% of open interest
Crowding: 40% percentile over 52 weeks -- within its normal range
Read this as crowding, not as a forecast: an extreme is as often the end of a move as the middle of one.
```

</details>

<details><summary><b>Money going into and out of this fund</b> — score +0.15</summary>

```text
Direction: money coming in (1 month)
Share count change: 1 week: +4.5% (993.46M) over 8d | 1 month: +9.1% (1.91B) over 33d
Shares outstanding: 268.51M | fund size: 22.94B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Switzerland (EWL) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:** no explanation. It wrote only “NEUTRAL”, so the main reasons below are all it gave.

**Main reasons it gave:**
- Fund flows flat: share count unchanged over 1 week and 1 month
- Analyst coverage of 49.6% of fund: 64.8% buy, weighted price target +2.3% above current price
- Technicals: price above 50‑day and 200‑day SMA but below 20‑day SMA; RSI 50.4, MACD negative, volume 0.05× 20‑day average
- Macro: yields down modestly, VIX up to 31.7, no policy or data surprise

<details><summary><b>News</b> — score +0.00</summary>

_No news found for this one today._

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.16% (+0.01 on the week) | 5-year 4.62% (-0.26 on the week) | 10-year 4.83% (-0.24 on the week) | 30-year 5.24% (-0.17 on the week)
Yield curve, 10-year minus 3-month: +0.67 points -- upward sloping (normal)
US dollar index: 103.93 (+0.07 on the week)
Volatility (VIX): 31.72 (+7.2 on the week) -- stressed
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.1% (2026-10-01) | jobless claims 189k (2026-11-21)
Policy and expectations: Fed target 4.00% | market expects 2.1% inflation over 10 years
Rate path: 2-year Treasury 4.63% vs Fed target 3.75-4.00% -- the bond market prices about 3 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 63.55 (bar of 2026-11-25), from 502 daily bars
Trend: vs 20d SMA 64.33 (-1.2%), 50d 62.27 (+2.1%), 200d 62.02 (+2.5%); 50d above 200d
Momentum: RSI(14) 50.4 | MACD 0.092 vs signal 0.397 (histogram -0.305)
Returns: 1d +0.0% | 5d +0.3% | 1m +0.2% | 3m -0.3%
52-week range: 56.31 - 66.56 (now 70.6% of the way up)
Volatility: ATR(14) 0.80 (1.3% of price) | annualised 20d 21.5%
Volume: 0.05x the 20-day average
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
Three-year record: +14.1% a year | beta to the market 0.82
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

<details><summary><b>What analysts and big funds say</b> — score +0.30</summary>

_Not available today._

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score +0.30</summary>

```text
Rolled up from the 5 largest holdings, 49.6% of the fund by weight
Ratings by weight: buy 64.8% | hold 35.2% | sell 0.0% (mean 2.46 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +2.3% above the current prices
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

> No material macro surprise, flat fund flows, technicals not decisive, analyst view bullish but limited coverage, fundamentals modestly positive.

**Main reasons it gave:**
- No news found in past 24h
- Fund flows flat: 0% share count change over 1 week and 1 month
- Technical: price 58.62 below 20‑day SMA 63.20, RSI 33.2, MACD negative, volume 0.04× 20‑day average
- Macro: VIX up 7.2% to 31.72, inflation 3.7% above Fed target 4.0%
- Analyst coverage 42.3% of fund, 100% buy rating, price target +82.8% above current

<details><summary><b>News</b> — score +0.00</summary>

_No news found for this one today._

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.16% (+0.01 on the week) | 5-year 4.62% (-0.26 on the week) | 10-year 4.83% (-0.24 on the week) | 30-year 5.24% (-0.17 on the week)
Yield curve, 10-year minus 3-month: +0.67 points -- upward sloping (normal)
US dollar index: 103.93 (+0.07 on the week)
Volatility (VIX): 31.72 (+7.2 on the week) -- stressed
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.1% (2026-10-01) | jobless claims 189k (2026-11-21)
Policy and expectations: Fed target 4.00% | market expects 2.1% inflation over 10 years
Rate path: 2-year Treasury 4.63% vs Fed target 3.75-4.00% -- the bond market prices about 3 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 58.62 (bar of 2026-11-25), from 502 daily bars
Trend: vs 20d SMA 63.20 (-7.2%), 50d 65.12 (-10.0%), 200d 65.12 (-10.0%); 50d above 200d
Momentum: RSI(14) 33.2 | MACD -1.564 vs signal -1.090 (histogram -0.474)
Returns: 1d -2.8% | 5d -5.6% | 1m -9.9% | 3m -15.0%
52-week range: 55.33 - 71.61 (now 20.2% of the way up)
Volatility: ATR(14) 1.35 (2.3% of price) | annualised 20d 34.3%
Volume: 0.04x the 20-day average
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
Three-year record: +16.6% a year | beta to the market 1.13
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

<details><summary><b>What analysts and big funds say</b> — score +0.80</summary>

_Not available today._

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score +0.80</summary>

```text
Rolled up from the 5 largest holdings, 42.3% of the fund by weight
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 1.57 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +82.8% above the current prices
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
Shares outstanding: 5.55M | fund size: 325.34M
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Spain (EWP) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Neutral overall – bearish technicals and stressed market conditions offset a bullish analyst outlook and solid fundamentals.

**Main reasons it gave:**
- Technical: price below 20‑day, 50‑day and 200‑day SMAs (55.49 vs 57.91, 58.49, 58.16) and RSI 37.2 indicating bearish momentum
- Macro: VIX up 7.2 points to 31.72, indicating stressed market conditions
- Fund flows flat (share count unchanged), indicating no net demand
- Analyst view: 76.3% buy rating and weighted price target +14.6% above current price (bullish outlook)

<details><summary><b>News</b> — score +0.00</summary>

_No news found for this one today._

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.16% (+0.01 on the week) | 5-year 4.62% (-0.26 on the week) | 10-year 4.83% (-0.24 on the week) | 30-year 5.24% (-0.17 on the week)
Yield curve, 10-year minus 3-month: +0.67 points -- upward sloping (normal)
US dollar index: 103.93 (+0.07 on the week)
Volatility (VIX): 31.72 (+7.2 on the week) -- stressed
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.1% (2026-10-01) | jobless claims 189k (2026-11-21)
Policy and expectations: Fed target 4.00% | market expects 2.1% inflation over 10 years
Rate path: 2-year Treasury 4.63% vs Fed target 3.75-4.00% -- the bond market prices about 3 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score -0.40</summary>

```text
Last close 55.49 (bar of 2026-11-25), from 502 daily bars
Trend: vs 20d SMA 57.91 (-4.2%), 50d 58.49 (-5.1%), 200d 58.16 (-4.6%); 50d above 200d
Momentum: RSI(14) 37.2 | MACD -0.623 vs signal -0.303 (histogram -0.319)
Returns: 1d -1.9% | 5d -3.5% | 1m -3.8% | 3m -11.1%
52-week range: 50.84 - 63.23 (now 37.5% of the way up)
Volatility: ATR(14) 0.98 (1.8% of price) | annualised 20d 27.4%
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
Three-year record: +27.7% a year | beta to the market 0.91
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
Weighted price target: +14.6% above the current prices
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
Shares outstanding: 37.35M | fund size: 2.07B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Taiwan (EWT) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Neutral overall: bullish analyst coverage and net inflows are offset by bearish technicals and a stressed macro environment.

**Main reasons it gave:**
- Analyst view: 100% buy rating with +66% price target for top holdings
- Fund flows: share count increased 12.5% in one week (net inflows)
- Technicals: price 13.7% below 20‑day SMA, RSI 36.2, MACD negative
- Macro: VIX up 7.2 points to 31.72, indicating heightened market stress

<details><summary><b>News</b> — score +0.00</summary>

- [EWT Jan 2029 50.000 put (EWT290119P00050000) stock price, news, quote and history](https://uk.finance.yahoo.com/quote/EWT290119P00050000/)  
  <sub>Yahoo Finance UK, 16 hours ago</sub>  
  Find the latest EWT Jan 2029 50.000 put (EWT290119P00050000) stock quote, history, news and other vital information to help you with your stock trading and...
- [CORO: Country Picks That Have Paid Off So Far (NASDAQ:CORO)](https://seekingalpha.com/article/4971650-coro-country-picks-that-have-paid-off-so-far?source=feed_sector_etf_portfolio_strategy)  
  <sub>Seeking Alpha, 3 hours ago</sub>  
  The iShares International Country Rotation Active ETF is a “Buy” for its encouraging start and timely international exposure, with prudent sizing.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.16% (+0.01 on the week) | 5-year 4.62% (-0.26 on the week) | 10-year 4.83% (-0.24 on the week) | 30-year 5.24% (-0.17 on the week)
Yield curve, 10-year minus 3-month: +0.67 points -- upward sloping (normal)
US dollar index: 103.93 (+0.07 on the week)
Volatility (VIX): 31.72 (+7.2 on the week) -- stressed
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.1% (2026-10-01) | jobless claims 189k (2026-11-21)
Policy and expectations: Fed target 4.00% | market expects 2.1% inflation over 10 years
Rate path: 2-year Treasury 4.63% vs Fed target 3.75-4.00% -- the bond market prices about 3 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score -0.40</summary>

```text
Last close 79.53 (bar of 2026-11-25), from 502 daily bars
Trend: vs 20d SMA 92.13 (-13.7%), 50d 103.88 (-23.4%), 200d 95.30 (-16.5%); 50d above 200d
Momentum: RSI(14) 36.2 | MACD -6.197 vs signal -5.316 (histogram -0.881)
Returns: 1d -5.9% | 5d -10.4% | 1m -25.8% | 3m -26.8%
52-week range: 60.03 - 118.00 (now 33.6% of the way up)
Volatility: ATR(14) 5.53 (7.0% of price) | annualised 20d 104.1%
Volume: 0.15x the 20-day average
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
Three-year record: +30.6% a year | beta to the market 1.35
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

<details><summary><b>What analysts and big funds say</b> — score +0.60</summary>

_Not available today._

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score +0.60</summary>

```text
Rolled up from the 5 largest holdings, 37.7% of the fund by weight
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 1.33 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +66.1% above the current prices
Holdings read: 2330.TW, 2454.TW, 2317.TW, 3711.TW, 2308.TW
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
Share count change: 1 week: +12.5% (1.13B) over 8d | 1 month: +12.6% (1.13B) over 33d
Shares outstanding: 127.08M | fund size: 10.11B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### United Kingdom (EWU) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> No material macro surprise, technicals are bearish but low volume, modest inflows, and analyst view is bullish but limited to ~37% of the fund. Overall the evidence does not justify a directional tilt.

**Main reasons it gave:**
- Price 45.49 below 20‑day SMA 47.12 (-3.5%) and 50‑day SMA 47.10 (-3.4%)
- RSI 39.4 and MACD -0.527 (negative momentum)
- VIX 31.72 (+7.2 on week) indicating stressed market volatility
- Share count up 5.8% week‑over‑week (moderate inflows)
- Analyst coverage 36.9% of fund, 100% buy with +20.8% price target (bullish but limited)

<details><summary><b>News</b> — score +0.00</summary>

_No news found for this one today._

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.16% (+0.01 on the week) | 5-year 4.62% (-0.26 on the week) | 10-year 4.83% (-0.24 on the week) | 30-year 5.24% (-0.17 on the week)
Yield curve, 10-year minus 3-month: +0.67 points -- upward sloping (normal)
US dollar index: 103.93 (+0.07 on the week)
Volatility (VIX): 31.72 (+7.2 on the week) -- stressed
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.1% (2026-10-01) | jobless claims 189k (2026-11-21)
Policy and expectations: Fed target 4.00% | market expects 2.1% inflation over 10 years
Rate path: 2-year Treasury 4.63% vs Fed target 3.75-4.00% -- the bond market prices about 3 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score -0.20</summary>

```text
Last close 45.49 (bar of 2026-11-25), from 502 daily bars
Trend: vs 20d SMA 47.12 (-3.5%), 50d 47.10 (-3.4%), 200d 47.06 (-3.3%); 50d above 200d
Momentum: RSI(14) 39.4 | MACD -0.527 vs signal -0.270 (histogram -0.256)
Returns: 1d -0.8% | 5d -1.3% | 1m -3.6% | 3m -6.5%
52-week range: 42.52 - 49.39 (now 43.2% of the way up)
Volatility: ATR(14) 0.66 (1.5% of price) | annualised 20d 23.5%
Volume: 0.05x the 20-day average
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
Three-year record: +16.8% a year | beta to the market 0.66
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

<details><summary><b>What analysts and big funds say</b> — score +0.40</summary>

_Not available today._

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score +0.40</summary>

```text
Rolled up from the 5 largest holdings, 36.9% of the fund by weight
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 2.07 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +20.8% above the current prices
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
Share count change: 1 week: +5.8% (205.60M) over 8d | 1 month: +7.1% (248.52M) over 33d
Shares outstanding: 82.18M | fund size: 3.74B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Mexico (EWW) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Neutral overall as there is no material macro surprise, fund flows are flat, technicals are bearish but lack decisive break, and analyst coverage is limited despite a bullish rating.

**Main reasons it gave:**
- Fund flows flat: share count unchanged (+0.0% over 1 week and 1 month)
- Technical indicators bearish (RSI 31.4, MACD -0.720) with low volume (0.10x 20‑day average)
- Macro data stable: inflation 3.7% near Fed target, VIX up 7.2 points indicating stress but no surprise
- Analyst coverage limited to 47.5% of fund, rating 100% buy with +20.6% price target

<details><summary><b>News</b> — score +0.00</summary>

_No news found for this one today._

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.16% (+0.01 on the week) | 5-year 4.62% (-0.26 on the week) | 10-year 4.83% (-0.24 on the week) | 30-year 5.24% (-0.17 on the week)
Yield curve, 10-year minus 3-month: +0.67 points -- upward sloping (normal)
US dollar index: 103.93 (+0.07 on the week)
Volatility (VIX): 31.72 (+7.2 on the week) -- stressed
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.1% (2026-10-01) | jobless claims 189k (2026-11-21)
Policy and expectations: Fed target 4.00% | market expects 2.1% inflation over 10 years
Rate path: 2-year Treasury 4.63% vs Fed target 3.75-4.00% -- the bond market prices about 3 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score -0.20</summary>

```text
Last close 70.81 (bar of 2026-11-25), from 502 daily bars
Trend: vs 20d SMA 75.16 (-5.8%), 50d 74.08 (-4.4%), 200d 76.00 (-6.8%); 50d below 200d
Momentum: RSI(14) 31.4 | MACD -0.720 vs signal -0.014 (histogram -0.706)
Returns: 1d -1.5% | 5d -3.8% | 1m -5.6% | 3m -8.2%
52-week range: 67.45 - 81.23 (now 24.3% of the way up)
Volatility: ATR(14) 1.56 (2.2% of price) | annualised 20d 22.2%
Volume: 0.10x the 20-day average
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
Three-year record: +9.1% a year | beta to the market 0.99
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
Weighted price target: +20.6% above the current prices
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
Shares outstanding: 18.90M | fund size: 1.34B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### South Africa (EZA) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:** no explanation. It wrote only “NEUTRAL”, so the main reasons below are all it gave.

**Main reasons it gave:**
- US Treasury yields fell modestly (10-year -0.24%) while VIX rose 7.2 points to 31.72, indicating higher risk aversion
- ETF trades below 20‑day, 50‑day and 200‑day SMAs with RSI 33.4 and negative MACD, showing bearish momentum
- Analyst coverage of top 5 holdings (41.8% weight) is 100% buy with a +46.7% price target, bullish on a portion of the fund
- Fund flows are flat over the past month, indicating no net demand or supply pressure
- Fund fundamentals show low P/E 10.65 and high dividend yield 8.2%, suggesting attractive valuation

<details><summary><b>News</b> — score +0.00</summary>

_No news found for this one today._

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.16% (+0.01 on the week) | 5-year 4.62% (-0.26 on the week) | 10-year 4.83% (-0.24 on the week) | 30-year 5.24% (-0.17 on the week)
Yield curve, 10-year minus 3-month: +0.67 points -- upward sloping (normal)
US dollar index: 103.93 (+0.07 on the week)
Volatility (VIX): 31.72 (+7.2 on the week) -- stressed
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.1% (2026-10-01) | jobless claims 189k (2026-11-21)
Policy and expectations: Fed target 4.00% | market expects 2.1% inflation over 10 years
Rate path: 2-year Treasury 4.63% vs Fed target 3.75-4.00% -- the bond market prices about 3 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score -0.40</summary>

```text
Last close 56.87 (bar of 2026-11-25), from 502 daily bars
Trend: vs 20d SMA 62.96 (-9.7%), 50d 64.07 (-11.2%), 200d 67.44 (-15.7%); 50d below 200d
Momentum: RSI(14) 33.4 | MACD -1.937 vs signal -1.109 (histogram -0.828)
Returns: 1d -2.6% | 5d -4.5% | 1m -11.2% | 3m -20.5%
52-week range: 56.26 - 81.60 (now 2.4% of the way up)
Volatility: ATR(14) 1.77 (3.1% of price) | annualised 20d 42.7%
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
Three-year record: +20.8% a year | beta to the market 1.12
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

<details><summary><b>What analysts and big funds say</b> — score +0.70</summary>

_Not available today._

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score +0.70</summary>

```text
Rolled up from the 5 largest holdings, 41.8% of the fund by weight
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 1.98 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +46.7% above the current prices
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
Share count change: 1 week: +0.0% (0.00) over 7d | 1 month: +0.0% (0.00) over 32d
Shares outstanding: 7.90M | fund size: 449.27M
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Gold mining companies (GDX) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> No macro surprise; technicals bearish but low volume; strong inflows; analyst view bullish but limited coverage.

**Main reasons it gave:**
- Weekly fund inflow +8.4% (1.73B) shows strong demand
- Technical trend below 20d, 50d, 200d SMAs indicates bearish momentum
- Analyst coverage 42% of fund weight, 100% buy rating with +40.4% price target
- No macro surprise: Fed target unchanged, inflation 3.7% in line with expectations

<details><summary><b>News</b> — score +0.00</summary>

- [VanEck Gold Miners ETF (Derivatives) Price Today in Turkey | GDX to TRY | GDX/TRY Live Price](https://www.binance.com/en-TR/price/vaneck-gold-miners-etf-derivaties)  
  <sub>Binance, 18 hours ago</sub>  
  1 VanEck Gold Miners ETF (Derivatives) currently costs ₺ 3.6K, down 1.74% in the last 24h. Track the live GDX price in Türkiye, market cap,...
- [VanEck Gold Miners ETF Explained: Gold Price, Miner Holdings and Outlook](https://kalkinemedia.com/au/stocks/etf/vaneck-gold-miners-etf-explained-gold-price-miner-holdings-and-outlook)  
  <sub>Kalkine Media, 14 hours ago</sub>  
  The VanEck fund offers a diversified basket of gold mining companies rather than exposure to bullion itself.
- [YieldMax® ETFs Announces Weekly Distributions for Group 2 ETFs](https://www.google.com/goto?url=CAESwgEBxCJF1z9LAOe3q6U-ZazUTPhgE7Z3fQW5AM6eeAuD8L_920MZuZMQ5gfrLhF1cC7XyeisOK1s0CLwy1lmMGQGiBPo_3r4yF8p3_n-dnGI6t5d1DTrsizY7CtG--tOMro9eBrRm9HlQAEtiYxb09ltixzkDp2I0H1-G-4rKq-_23EkwL8L7WmbwnWnl-hdfxgKGYOk6GGJFchbYFDxwfs8W9yZavz0PRGJm5Yj4SPTeWaSEugJ9IqlsfUck4M3-P8CkQ&gsessionid=mqYGC7rFkfvLRKBQhgunU7bOy_iXJsRcqqr5cwBl6xN2_xKT7JI9uQ)  
  <sub>GlobeNewswire, 3 hours ago</sub>  
  CHICAGO and MILWAUKEE and NEW YORK, Nov. 25, 2026 (GLOBE NEWSWIRE) -- YieldMax® ETFs today announced distributions for the YieldMax® Group 2 weekly pay ETFs...
- [GDX ETF Price Forecast — GDX ($71.90) $80 Upside Target on $1,650/oz Miner Margins After Gold Crash](https://www.google.com/goto?url=CAEStAEBxCJF160CBCVwuqfiWejbF3Vs7uqSHUDiYhJyGKYRaFxVXVceqodmRq76f8CZrKzUex_owWA4yfYALtkeOgHxfILDSSKXZLrOHJ65ndTNdgGYoubQflxIRoe6noZ6CmiyTUzLLgmn7wuYTgkqOssf47Lx9VESGeJJ4JH86aWwP3qPqvsbRbCG7XHpAO9Uom-QWj7cb0tEs412xM2azNxfUvV1ATh4J8aWA6iCt86bQZpysf4&gsessionid=mqYGC7rFkfvLRKBQhgunU7bOy_iXJsRcqqr5cwBl6xN2_xKT7JI9uQ)  
  <sub>TradingNEWS, 17 hours ago</sub>  
  Trading News GDX holds $71.90 after a 6.43% rebound from its $68.40 52-week low as gold steadies near $3600, with miners still earning $1650/oz, putting ...
- [Gold Price Forecast — XAU/USD ($3,605) $3,850 Upside Target on PCE and Fed Hike Risk](https://www.google.com/goto?url=CAESqwEBxCJF12IDzQQHP_r1xI9d_Vbfuqqv-hNqbS0Lo-pHD8tBePyZHZhDKLHiTBthny2PSH6Bhc0wqwdIw_US1IHc7NqfSI4A6pMlbA5NV8p3V2l_4BBPkO3276c-VIdV_dcTMC28vIyUT_hsq1HjzxS2lgkTTxDtavQB_rW7AwqZCQ5mtWVFwMzc2EVBDcie2Oe8E2A8U_R7R-xUuteh8ijPufC3V272kZ42t4U&gsessionid=mqYGC7rFkfvLRKBQhgunU7bOy_iXJsRcqqr5cwBl6xN2_xKT7JI9uQ)  
  <sub>TradingNEWS, 22 hours ago</sub>  
  Trading News Gold fell 1.27% to $3605 after a $3691 rejection as GLD holdings slid to 1031 tonnes, while 321 tonnes of central bank buying backs a $3,85...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.16% (+0.01 on the week) | 5-year 4.62% (-0.26 on the week) | 10-year 4.83% (-0.24 on the week) | 30-year 5.24% (-0.17 on the week)
Yield curve, 10-year minus 3-month: +0.67 points -- upward sloping (normal)
US dollar index: 103.93 (+0.07 on the week)
Volatility (VIX): 31.72 (+7.2 on the week) -- stressed
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.1% (2026-10-01) | jobless claims 189k (2026-11-21)
Policy and expectations: Fed target 4.00% | market expects 2.1% inflation over 10 years
Rate path: 2-year Treasury 4.63% vs Fed target 3.75-4.00% -- the bond market prices about 3 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score -0.30</summary>

```text
Last close 68.10 (bar of 2026-11-25), from 502 daily bars
Trend: vs 20d SMA 79.29 (-14.1%), 50d 84.56 (-19.5%), 200d 88.61 (-23.1%); 50d below 200d
Momentum: RSI(14) 33.3 | MACD -4.102 vs signal -2.864 (histogram -1.238)
Returns: 1d -4.6% | 5d -9.0% | 1m -18.1% | 3m -34.3%
52-week range: 68.10 - 115.84 (now 0.0% of the way up)
Volatility: ATR(14) 3.67 (5.4% of price) | annualised 20d 66.8%
Volume: 0.16x the 20-day average
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
Three-year record: +37.1% a year | beta to the market 0.98
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
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 1.68 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +40.4% above the current prices
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
Share count change: 1 week: +8.4% (1.73B) over 7d | 1 month: +2.4% (512.69M) over 32d
Shares outstanding: 327.51M | fund size: 22.30B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Software (IGV) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Neutral overall as no material macro surprise or decisive technical break occurred; bullish analyst view is limited to 42% of holdings, flows are flat, and technicals show bearish momentum but low volume.

**Main reasons it gave:**
- Analyst coverage of top holdings (42.2% weight) is 100% buy with +47.9% price target
- Fund flows are flat over the past month, indicating no net demand
- Technical indicators (RSI 32.6, MACD negative, price below 20d/50d/200d SMAs) show bearish momentum but low volume
- Fund basics show high valuation multiples (P/E 30.79) with modest 3-year return (+7.9% per year)
- Macro data shows elevated VIX (31.7) and no surprise in inflation or policy, supporting a neutral stance

<details><summary><b>News</b> — score +0.00</summary>

- [1 TRY to IGV: Live Exchange Rate](https://www.weex.com/tokens/ishares-expanded-tech-software-etf-derivatives/from-try)  
  <sub>WEEX, 20 hours ago</sub>  
  Convert TRY to IGV in real time. Check the latest TRY to IGV rate, conversion tables, and price charts with WEEX's free converter.
- [3 Ways To Own Palo Alto Networks Through ETFs After The AI Security Deal](https://simplywall.st/stocks/us/software/nasdaq-panw/palo-alto-networks/news/3-ways-to-own-palo-alto-networks-through-etfs-after-the-ai-s)  
  <sub>Simply Wall St, 24 hours ago</sub>  
  You can own Palo Alto Networks directly, or you can hold it inside a fund and let other holdings share the load. Owning just the stock means you carry its...
- [(IGV) as a Liquidity Pulse for Institutional Tactics](https://www.google.com/goto?url=CAESvgEBxCJF10Or8P3phEgK5lFnoSD55n7CCSfq7VlguluqxWs2fLQnmYi7x7qKVZxwh3kTOSj-iKcIfRDTQxLDWlyPPC0vCMfXtdviLFEvRlFSI5WETh3iIvpeg-sPBpCVRnnB46S5g8YixYpnzGcWV1tK9DcYvAD70lB_IMcVMkN6OESt5KSJshoX92BNXd6d4U4YF5DdOxV4bn6Bd3mqi4SYMld5yRkQAUKpOhMdNQE7OEU1HhJdeFO0z_bbgmR6&gsessionid=hel9MB4QB_DvbrU1E3DlRCWTpQrfLJ-gDVW1PwpA_wrYdO0hiaezOQ)  
  <sub>Stock Traders Daily, 21 hours ago</sub>  
  Key findings for Ishares Expanded Tech-software Sector Etf (NYSE: IGV). Weak Near and Mid-Term Sentiment Could Pressure Neutral Long-Term Outlook...
- [1 JPY to IGV: Live Exchange Rate](https://www.google.com/goto?url=CAESjgEBxCJF12O91hVM-lwmLSqVTwbxjEaWK4lxJvziAtnneoverum8QHzWyKDWKXgNcn0SU7h-greszdghO3H4xLCdMjO1yF1-YUAz2lIKly8bDYgVN7Bik7N4UaPUOfBSmXQqp6lszaNDUz4S_04q-Mtv-RNuldByYZYKRIyceAveuT-Ksyt8gmoCdBkzYH9B&gsessionid=hel9MB4QB_DvbrU1E3DlRCWTpQrfLJ-gDVW1PwpA_wrYdO0hiaezOQ)  
  <sub>WEEX, 23 hours ago</sub>  
  Convert JPY to IGV in real time. Check the latest JPY to IGV rate, conversion tables, and price charts with WEEX's free converter.
- [How to Buy Oracle Stock (ORCL) in 2026](https://www.google.com/goto?url=CAESjQEBxCJF10rYtCzwMiI1Okw3m6IlBuhHanbSRDbHX-fF5QCDiwdbF-SDfXmGnSPqsCUatjbEZSIk19rlEWC0CBUdg3hGH0eT3kROOZDHmkK2HQjHISFhy9ylvAE3puSAs8e5WlEnx724QTVjOlHhOQhZZkpiTiTD3iI04M__i6SneJpbnf2DRdHyXFw-fKA&gsessionid=hel9MB4QB_DvbrU1E3DlRCWTpQrfLJ-gDVW1PwpA_wrYdO0hiaezOQ)  
  <sub>The Motley Fool, 19 hours ago</sub>  
  Oracle's dominant position in database software and accelerating AI-driven cloud computing business has captured many investors' interests.
- [Software ETF Up 1.2% as Chip ETF Falls 6.9%, an 8-Point Gap](https://www.google.com/goto?url=CAESjwEBxCJF17t0vxCSjFvXY9rkmtiRJPvvN4b9c17GjfViUenaFY5De4-vfh6gOIiXOqnAAkv-Cn7rieMacApawwnqREBZyOavQaXZGu4YWVthecJZkEGRg7NYStQPqknG_Lfn09fOyZW7LW3EPXvsqRsAWFOH9E5lLaanOF9-Wviy4o9ZOXrJMxfyrnyN8wgRiQ&gsessionid=hel9MB4QB_DvbrU1E3DlRCWTpQrfLJ-gDVW1PwpA_wrYdO0hiaezOQ)  
  <sub>FourWeekMBA, 20 hours ago</sub>  
  The iShares Expanded Tech-Software Sector ETF (IGV) was up 1.20% at 1:00 p.m. ET (18:00 UTC) on Tuesday, while the VanEck Semiconductor ETF (SMH) was down...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.16% (+0.01 on the week) | 5-year 4.62% (-0.26 on the week) | 10-year 4.83% (-0.24 on the week) | 30-year 5.24% (-0.17 on the week)
Yield curve, 10-year minus 3-month: +0.67 points -- upward sloping (normal)
US dollar index: 103.93 (+0.07 on the week)
Volatility (VIX): 31.72 (+7.2 on the week) -- stressed
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.1% (2026-10-01) | jobless claims 189k (2026-11-21)
Policy and expectations: Fed target 4.00% | market expects 2.1% inflation over 10 years
Rate path: 2-year Treasury 4.63% vs Fed target 3.75-4.00% -- the bond market prices about 3 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score -0.20</summary>

```text
Last close 91.13 (bar of 2026-11-25), from 502 daily bars
Trend: vs 20d SMA 99.31 (-8.2%), 50d 104.76 (-13.0%), 200d 94.57 (-3.6%); 50d above 200d
Momentum: RSI(14) 32.6 | MACD -3.421 vs signal -2.733 (histogram -0.688)
Returns: 1d -4.4% | 5d -6.0% | 1m -18.5% | 3m -17.4%
52-week range: 74.67 - 112.67 (now 43.3% of the way up)
Volatility: ATR(14) 3.39 (3.7% of price) | annualised 20d 39.3%
Volume: 0.12x the 20-day average
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
Three-year record: +7.9% a year | beta to the market 1.25
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

<details><summary><b>What analysts and big funds say</b> — score +0.60</summary>

_Not available today._

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score +0.60</summary>

```text
Rolled up from the 5 largest holdings, 42.2% of the fund by weight
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 1.57 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +47.9% above the current prices
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
Share count change: 1 week: +0.0% (0.00) over 7d | 1 month: +0.0% (0.00) over 32d
Shares outstanding: 12.50M | fund size: 1.14B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### India (INDA) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> The fund shows mixed signals: strong analyst buy coverage for its top holdings (+12% price target) suggests bullish fundamentals, but recent outflows of -9% over the past month indicate bearish investor sentiment. Technicals are bullish (price above SMAs) yet overbought (RSI 70.8) with low volume, and macro conditions are stressed (VIX 31.72). No clear macro catalyst or decisive technical break is present, so the overall stance remains neutral.

**Main reasons it gave:**
- Share count fell 9% in the past month (outflows)
- Analyst coverage of top holdings (24.8% of fund) shows 100% buy rating and +12% price target
- Price above 20‑day, 50‑day, 200‑day SMAs; RSI 70.8 (overbought) with volume 0.14× 20‑day average
- VIX rose 7.2 points to 31.72, indicating high market volatility

<details><summary><b>News</b> — score +0.00</summary>

- [Technical Reactions to INDA Trends in Macro Strategies](https://news.stocktradersdaily.com/news_release/20/Technical_Reactions_to_INDA_Trends_in_Macro_Strategies_112426054402_1795560242.html)  
  <sub>Stock Traders Daily, 21 hours ago</sub>  
  Key findings for Ishares Msci India Etf (NASDAQ: INDA). If Near and Mid-Term Strong Sentiment Holds, It Could Extend to Long Term...
- [News by CNBC TV18 on TradingView, 2026-11-25 — cnbctv:ebe66b75d094b:0](https://www.tradingview.com/news/cnbctv:ebe66b75d094b:0/)  
  <sub>TradingView, 14 hours ago</sub>  
  Jensen Huang's return to Nvidia may have rekindled the AI trade. But there's still a case for playing defense and diversifying – owning the market's safer...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.16% (+0.01 on the week) | 5-year 4.62% (-0.26 on the week) | 10-year 4.83% (-0.24 on the week) | 30-year 5.24% (-0.17 on the week)
Yield curve, 10-year minus 3-month: +0.67 points -- upward sloping (normal)
US dollar index: 103.93 (+0.07 on the week)
Volatility (VIX): 31.72 (+7.2 on the week) -- stressed
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.1% (2026-10-01) | jobless claims 189k (2026-11-21)
Policy and expectations: Fed target 4.00% | market expects 2.1% inflation over 10 years
Rate path: 2-year Treasury 4.63% vs Fed target 3.75-4.00% -- the bond market prices about 3 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 52.78 (bar of 2026-11-25), from 502 daily bars
Trend: vs 20d SMA 50.92 (+3.7%), 50d 48.64 (+8.5%), 200d 49.07 (+7.6%); 50d below 200d
Momentum: RSI(14) 70.8 | MACD 1.220 vs signal 1.124 (histogram 0.096)
Returns: 1d +0.1% | 5d +2.6% | 1m +12.9% | 3m +6.6%
52-week range: 45.42 - 54.71 (now 79.3% of the way up)
Volatility: ATR(14) 0.60 (1.1% of price) | annualised 20d 15.5%
Volume: 0.14x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score -0.10</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score -0.10</summary>

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
Rolled up from the 5 largest holdings, 24.8% of the fund by weight  -- thin, so read this as a fact about that slice rather than the fund
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 1.39 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +12.0% above the current prices
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
Share count change: 1 week: -1.2% (-73.88M) over 7d | 1 month: -9.0% (-589.14M) over 32d
Shares outstanding: 112.36M | fund size: 5.93B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Defence and aerospace (ITA) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Neutral overall due to mixed signals: strong analyst bullishness and massive inflows are offset by weak technicals and a stressed macro environment.

**Main reasons it gave:**
- Technical downtrend: price below 20d/50d/200d SMAs, RSI 39.8, negative MACD
- Macro stress: VIX 31.72, no policy surprise
- Analyst consensus: 100% buy, +22.7% price target covering 54.8% of fund
- Fund flows: share count +200.8% increase over 1 month

<details><summary><b>News</b> — score +0.00</summary>

- [RTX Corp (NYSE: RTX) Posts $340B Backlog And 11% Sales Growth, Pushing Investors To Weigh ETF Exposure Options](https://www.foreignpolicyjournal.com/2026/11/25/rtx-corp-nyse-rtx-posts-340b-backlog-and-11-sales-growth-pushing-investors-to-weigh-etf-exposure-options/)  
  <sub>Foreign Policy Journal, 2 hours ago</sub>  
  A record order backlog of $340 billion and an 11% year-over-year revenue gain in the third quarter of 2026 have put RTX Corp (NYSE: RTX) squarely back on.
- [CM: SEC Form FWP filed by Canadian Imperial Bank of Commerce](https://www.quantisnow.com/insight/sec-form-fwp-filed-by-canadian-imperial-bank-of-commerce-6806103)  
  <sub>Quantisnow, 17 hours ago</sub>  
  Canadian Imperial Bank of Commerce is offering notes tied to the iShares U.S. Aerospace & Defense ETF (ITA) with a term of about 14 months.
- [Are Wall Street Analysts Bullish on Lockheed Martin Stock?](https://www.google.com/goto?url=CAESoQEBxCJF1xCKEo6IFD4NtMWGyUMt0wY7TrxU1Y-vDd8ZWrEg-gDmSTg6Bj1UF1jOUYblS0mJ006oxDEYUuAKI6GOFrQ2Kq_xh8V9L2b7jVJOuqJYNOVa0Reyc8vaRqLVWKcrBt9BfQ_3-r1sAPJmMCFh6dxO9w5LSOTznajLv9PvAgGSOyPBnBuNgWSU7yN84GnV63Ul5ZpJRsKYd0njBdkxyQ&gsessionid=d2fykYkDJixAJjLXXb1ocyfEHwia2Fz4rPkWXGnp4SXbJ1CirNvlPQ)  
  <sub>Yahoo Finance, 24 hours ago</sub>  
  Lockheed Martin has outperformed the broader market over the past year, and analysts are cautiously optimistic about the stock's prospects.
- [Army orders nationwide storage review over deteriorating explosives in Iowa (PPA:NYSEARCA)](https://www.google.com/goto?url=CAESrAEBxCJF1-ZXll5E_t6xrY3us-P01irHr8QYag3-1LTZRo-KeaSzO4vi40f1S9JfztOl2BrU7c13_kQP70ZX_prD9STsKvKS0pSC1pgGdF0P2VxJ9awD0ZiKm-SXFA98ewXVf-kphldlnuDdgag6rb30_05C96iNqOWv4eLemywJMrtt8-_hjpHROHJ0H0BMGq-RtLDGzP1zBKFJDX13cqWBvb-fgkwVSaAwdGzu&gsessionid=d2fykYkDJixAJjLXXb1ocyfEHwia2Fz4rPkWXGnp4SXbJ1CirNvlPQ)  
  <sub>Seeking Alpha, 21 hours ago</sub>  
  The U.S. Army will inspect all weapons storage facilities after finding deteriorated explosives in Iowa; a possible lead plume could reach about 350 farms.
- [Sendero Closes $1.96 Million Placement for La Ollita Deep Drilling](https://www.google.com/goto?url=CAESsAEBxCJF12FHECaUJjdXBNE2D65XA8QghNgBrSEIauXAvYfZuxeSjH1nNvw2_PMxjeoh2rs33SFUVy0YEy2sFevECVqsCVShShUL465rzkPVqb2mzSYRUX5twWQ0lerX8haM3G6k0QF_x5IL2pAgEXws3cX0svtDQ9WtMJEXoJyOBQ21PiRy315KDwHDN-IMTXZfChn0IIQCEMDrwzPHq42UBPuAaI8Iidm2C9QT5X4VRg&gsessionid=d2fykYkDJixAJjLXXb1ocyfEHwia2Fz4rPkWXGnp4SXbJ1CirNvlPQ)  
  <sub>TipRanks, 15 hours ago</sub>  
  Sendero Resources Corp. ( ($TSE:SEND) ) has provided an announcement. Sendero Resources Corp. closed a non-brokered private placement, issuing 3700000 units...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.16% (+0.01 on the week) | 5-year 4.62% (-0.26 on the week) | 10-year 4.83% (-0.24 on the week) | 30-year 5.24% (-0.17 on the week)
Yield curve, 10-year minus 3-month: +0.67 points -- upward sloping (normal)
US dollar index: 103.93 (+0.07 on the week)
Volatility (VIX): 31.72 (+7.2 on the week) -- stressed
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.1% (2026-10-01) | jobless claims 189k (2026-11-21)
Policy and expectations: Fed target 4.00% | market expects 2.1% inflation over 10 years
Rate path: 2-year Treasury 4.63% vs Fed target 3.75-4.00% -- the bond market prices about 3 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score -0.60</summary>

```text
Last close 66.58 (bar of 2026-11-25), from 502 daily bars
Trend: vs 20d SMA 69.99 (-4.9%), 50d 69.65 (-4.4%), 200d 75.56 (-11.9%); 50d below 200d
Momentum: RSI(14) 39.8 | MACD -0.710 vs signal -0.309 (histogram -0.401)
Returns: 1d -2.3% | 5d -4.0% | 1m -3.1% | 3m -14.7%
52-week range: 66.17 - 84.41 (now 2.2% of the way up)
Volatility: ATR(14) 1.83 (2.8% of price) | annualised 20d 36.0%
Volume: 0.07x the 20-day average
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

<details><summary><b>What analysts and big funds say</b> — score +0.80</summary>

_Not available today._

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score +0.80</summary>

```text
Rolled up from the 5 largest holdings, 54.8% of the fund by weight
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 1.74 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +22.7% above the current prices
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
Share count change: 1 week: +1.7% (203.56M) over 7d | 1 month: +200.8% (7.93B) over 32d
Shares outstanding: 178.50M | fund size: 11.88B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Transport and delivery (IYT) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Mixed signals: bullish analyst coverage and fund inflows versus bearish technicals and stressed macro environment.

**Main reasons it gave:**
- Price below 20‑day SMA (78.95 vs 82.23) indicating bearish trend
- RSI 41.1 and MACD negative showing weak momentum
- Share count increased 5.8% over past month, indicating net inflows
- Analyst coverage 90.9% buy, weighted price target +23% above current price
- VIX up 7.2 points to 31.72, reflecting heightened market volatility

<details><summary><b>News</b> — score +0.00</summary>

_No news found for this one today._

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.16% (+0.01 on the week) | 5-year 4.62% (-0.26 on the week) | 10-year 4.83% (-0.24 on the week) | 30-year 5.24% (-0.17 on the week)
Yield curve, 10-year minus 3-month: +0.67 points -- upward sloping (normal)
US dollar index: 103.93 (+0.07 on the week)
Volatility (VIX): 31.72 (+7.2 on the week) -- stressed
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.1% (2026-10-01) | jobless claims 189k (2026-11-21)
Policy and expectations: Fed target 4.00% | market expects 2.1% inflation over 10 years
Rate path: 2-year Treasury 4.63% vs Fed target 3.75-4.00% -- the bond market prices about 3 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score -0.40</summary>

```text
Last close 78.95 (bar of 2026-11-25), from 502 daily bars
Trend: vs 20d SMA 82.23 (-4.0%), 50d 80.88 (-2.4%), 200d 82.03 (-3.8%); 50d below 200d
Momentum: RSI(14) 41.1 | MACD -0.372 vs signal 0.136 (histogram -0.509)
Returns: 1d -1.9% | 5d -4.7% | 1m -3.9% | 3m -8.6%
52-week range: 71.45 - 90.01 (now 40.4% of the way up)
Volatility: ATR(14) 1.74 (2.2% of price) | annualised 20d 29.7%
Volume: 0.11x the 20-day average
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
Three-year record: +11.0% a year | beta to the market 1.24
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

<details><summary><b>What analysts and big funds say</b> — score +0.50</summary>

_Not available today._

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score +0.50</summary>

```text
Rolled up from the 5 largest holdings, 52.2% of the fund by weight
Ratings by weight: buy 90.9% | hold 9.1% | sell 0.0% (mean 1.87 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +23.0% above the current prices
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
Share count change: 1 week: +4.2% (78.95M) over 8d | 1 month: +5.8% (108.65M) over 33d
Shares outstanding: 24.95M | fund size: 1.97B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

**Data that was missing** (counted as 0.00, never guessed):
- news unavailable: Bright Data returned an empty body with its 200; nothing to parse (Bright Data said: x-brd-status-code 502; x-brd-error captcha or protection page found) (Bing's feed, direct: 5 headline(s), none naming IYT)

### US regional banks (KRE) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> No macro surprise (yields stable, no policy shift, VIX high but unchanged); technicals bearish (price below 20‑day/50‑day/200‑day SMAs, RSI 38.9) but no decisive break on volume; fund flows positive (+11.9% share count increase over 1 month); analyst coverage thin (5.9% weight) with slight bullish bias (50% buy rating, price target +16%).

**Main reasons it gave:**
- No macro surprise: yields stable, no policy shift, VIX high but unchanged
- Technical indicators bearish (price below 20d/50d/200d SMAs, RSI 38.9) but no decisive break on volume
- Fund flows positive: +11.9% share count increase over 1 month
- Analyst coverage thin (5.9% weight) with slight bullish bias: 50% buy rating, price target +16%

<details><summary><b>News</b> — score +0.00</summary>

- [Banks' Q3 earnings dip from Q2 but rise from a year ago, FDIC says (KBE:NYSEARCA)](https://seekingalpha.com/news/4676310-banks-q3-earnings-dip-from-q2-but-rise-from-a-year-ago-fdic-says)  
  <sub>Seeking Alpha, 20 hours ago</sub>  
  FDIC-insured banks' Q3 earnings fell 5.9% from Q2 to $84.8B but rose 7% year over year, while net interest margin climbed to 3.39%.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.16% (+0.01 on the week) | 5-year 4.62% (-0.26 on the week) | 10-year 4.83% (-0.24 on the week) | 30-year 5.24% (-0.17 on the week)
Yield curve, 10-year minus 3-month: +0.67 points -- upward sloping (normal)
US dollar index: 103.93 (+0.07 on the week)
Volatility (VIX): 31.72 (+7.2 on the week) -- stressed
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.1% (2026-10-01) | jobless claims 189k (2026-11-21)
Policy and expectations: Fed target 4.00% | market expects 2.1% inflation over 10 years
Rate path: 2-year Treasury 4.63% vs Fed target 3.75-4.00% -- the bond market prices about 3 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score -0.20</summary>

```text
Last close 69.03 (bar of 2026-11-25), from 502 daily bars
Trend: vs 20d SMA 71.72 (-3.8%), 50d 71.08 (-2.9%), 200d 71.14 (-3.0%); 50d below 200d
Momentum: RSI(14) 38.9 | MACD -0.666 vs signal -0.253 (histogram -0.413)
Returns: 1d -1.1% | 5d -2.1% | 1m -4.9% | 3m -7.2%
52-week range: 62.62 - 77.93 (now 41.8% of the way up)
Volatility: ATR(14) 1.42 (2.1% of price) | annualised 20d 21.5%
Volume: 0.19x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.30</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score +0.30</summary>

```text
Fund type: Financial
What it holds: P/E 12.17 | P/B 1.26 | P/S 3.63 | 3y earnings growth n/a
Yield: 2.2%
Three-year record: +19.4% a year | beta to the market 0.97
Cost and size: expense ratio 0.35% | net assets 4.01B
What it is made of: Stocks 99.9%, Cash 0.1%
Largest holdings: Glacier Bancorp Inc 1.2%, United Community Banks Inc 1.2%, Texas Capital Bancshares Inc 1.2%, Bank OZK 1.2%, Eastern Bankshares Inc Ordinary Shares 1.2%
Sector mix: Financial services 100.0%
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

<details><summary><b>What analysts and big funds say</b> — score +0.10</summary>

_Not available today._

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score +0.10</summary>

```text
Rolled up from the 5 largest holdings, 5.9% of the fund by weight  -- thin, so read this as a fact about that slice rather than the fund
Ratings by weight: buy 50.1% | hold 49.9% | sell 0.0% (mean 2.45 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +16.0% above the current prices
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
Share count change: 1 week: +3.9% (150.67M) over 7d | 1 month: +11.9% (423.81M) over 32d
Shares outstanding: 57.66M | fund size: 3.98B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Saudi Arabia (KSA) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> No macro surprise, technicals bearish, net outflows bearish, but analyst view bullish; overall neutral.

**Main reasons it gave:**
- Price below 20d, 50d, and 200d SMAs with negative momentum (RSI 37.3, MACD negative)
- Monthly net outflows of -8.1% (approx -49M) indicating bearish investor sentiment
- Analyst coverage of 45.3% of fund weight with 100% buy rating and +20.1% price target
- Elevated VIX at 31.72 and no macro surprise in recent US data (inflation 3.7% in line with expectations)

<details><summary><b>News</b> — score +0.00</summary>

- [XASB ETF Holdings List — TRADEGATE:XASB](https://www.tradingview.com/symbols/TRADEGATE-XASB/holdings/)  
  <sub>TradingView, 18 hours ago</sub>  
  Explore Xtrackers II SICAV - Xtrackers II Salam USD Global Aggregate Sukuk UCITS ETF -1D- Distribution holdings with weight, market value, and other helpful...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.16% (+0.01 on the week) | 5-year 4.62% (-0.26 on the week) | 10-year 4.83% (-0.24 on the week) | 30-year 5.24% (-0.17 on the week)
Yield curve, 10-year minus 3-month: +0.67 points -- upward sloping (normal)
US dollar index: 103.93 (+0.07 on the week)
Volatility (VIX): 31.72 (+7.2 on the week) -- stressed
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.1% (2026-10-01) | jobless claims 189k (2026-11-21)
Policy and expectations: Fed target 4.00% | market expects 2.1% inflation over 10 years
Rate path: 2-year Treasury 4.63% vs Fed target 3.75-4.00% -- the bond market prices about 3 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score -0.40</summary>

```text
Last close 34.53 (bar of 2026-11-25), from 502 daily bars
Trend: vs 20d SMA 35.17 (-1.8%), 50d 35.60 (-3.0%), 200d 37.60 (-8.2%); 50d below 200d
Momentum: RSI(14) 37.3 | MACD -0.134 vs signal -0.081 (histogram -0.053)
Returns: 1d -0.8% | 5d -3.0% | 1m -0.3% | 3m -12.1%
52-week range: 33.69 - 40.63 (now 12.1% of the way up)
Volatility: ATR(14) 0.34 (1.0% of price) | annualised 20d 13.7%
Volume: 0.22x the 20-day average
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
Three-year record: -1.1% a year | beta to the market 0.20
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

<details><summary><b>What analysts and big funds say</b> — score +0.40</summary>

_Not available today._

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score +0.40</summary>

```text
Rolled up from the 5 largest holdings, 45.3% of the fund by weight
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 2.10 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +20.1% above the current prices
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
Share count change: 1 week: +2.9% (15.57M) over 7d | 1 month: -8.1% (-48.95M) over 32d
Shares outstanding: 16.01M | fund size: 552.91M
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### China (MCHI) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> No macro surprise, technicals bearish but low volume, mixed fund flows, analyst view bullish but limited coverage, fundamentals modest.

**Main reasons it gave:**
- Technicals: price 45.32, 16.9% below 200‑day SMA, RSI 26.6 (oversold) with low volume
- Fund flows: -4.7% net share count change over 1‑month (outflows) despite +4.1% weekly inflow
- Analyst view: 100% buy rating for top holdings covering 32.6% of fund, weighted price target +77% above current price
- Macro: no policy or data surprise; yields stable, VIX up 7.2 points indicating stressed market

<details><summary><b>News</b> — score +0.00</summary>

_No news found for this one today._

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.16% (+0.01 on the week) | 5-year 4.62% (-0.26 on the week) | 10-year 4.83% (-0.24 on the week) | 30-year 5.24% (-0.17 on the week)
Yield curve, 10-year minus 3-month: +0.67 points -- upward sloping (normal)
US dollar index: 103.93 (+0.07 on the week)
Volatility (VIX): 31.72 (+7.2 on the week) -- stressed
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.1% (2026-10-01) | jobless claims 189k (2026-11-21)
Policy and expectations: Fed target 4.00% | market expects 2.1% inflation over 10 years
Rate path: 2-year Treasury 4.63% vs Fed target 3.75-4.00% -- the bond market prices about 3 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score -0.20</summary>

```text
Last close 45.32 (bar of 2026-11-25), from 502 daily bars
Trend: vs 20d SMA 49.12 (-7.7%), 50d 50.62 (-10.5%), 200d 54.54 (-16.9%); 50d below 200d
Momentum: RSI(14) 26.6 | MACD -1.268 vs signal -0.885 (histogram -0.382)
Returns: 1d -2.8% | 5d -5.2% | 1m -7.7% | 3m -17.4%
52-week range: 45.32 - 64.26 (now 0.0% of the way up)
Volatility: ATR(14) 0.81 (1.8% of price) | annualised 20d 25.5%
Volume: 0.07x the 20-day average
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
Three-year record: +5.4% a year | beta to the market 0.47
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
Weighted price target: +77.0% above the current prices
Holdings read: 0700.HK, 9988.HK, 00939, 01398, 1810.HK
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
Share count change: 1 week: +4.1% (205.91M) over 7d | 1 month: -4.7% (-259.52M) over 32d
Shares outstanding: 116.53M | fund size: 5.28B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Chip makers (SMH) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Neutral overall: technicals show a bearish downtrend but with low volume; fund flows are positive indicating demand; analyst consensus is strongly bullish with a +71% price target; macro environment unchanged with no policy surprise.

**Main reasons it gave:**
- Price 397.20 is 16.4% below 20‑day SMA (475.33) – bearish trend
- Weekly share count rose 5.8% (3.12B) – net inflows
- Analyst consensus 100% buy, weighted price target +71% above current price
- Macro unchanged: Treasury yields stable, VIX up but no policy surprise

<details><summary><b>News</b> — score +0.00</summary>

- [If You Invested $1000 In VanEck Semiconductor ETF Stock 5 Years Ago, You Would Have This Much Today](https://www.benzinga.com/news/26/11/63620768/if-you-invested-1000-vaneck-semiconductor-etf-stock-5-years-ago-you-would-have-much-today)  
  <sub>Benzinga, 51 minutes ago</sub>  
  VanEck Semiconductor ETF (NASDAQ:SMH) has outperformed the market over the past 5 years by 13.31% on an annualized basis producing an average annual return...
- [The Semiconductor ETF Kept Falling After Nvidia Raised Its Forecast. Time to Buy?](https://finance.yahoo.com/markets/stocks/articles/semiconductor-etf-kept-falling-nvidia-045702115.html)  
  <sub>Yahoo Finance, 10 hours ago</sub>  
  The VanEck Semiconductor ETF (NASDAQ:SMH) slid about 7% on Tuesday, Nov. 24, while chip shares fell broadly. The fund traded near $420 as I write,...
- [VanEck Semiconductor ETF SMH](https://www.google.com/goto?url=CAEScwHEIkXXYe3r2KCU1onUfezVV3L7MRGq4Z1n-CHlQHFHW7WTIyFuI2MxsbfQGZuecg9r40FpDYQkSKS-xE5f9GOO3PTHvjHgp8tt_bOxxzm3KbJRRWAq8TFHwhJEVwDZCixDB-2Z_8N-3OrhA3Cak8mHDTQ&gsessionid=dkEs59JA1PFVP5Fjn60HZcFOyuNoBFuWrptto0a6-_zyV6s1Oun1wg)  
  <sub>Kavout, 21 hours ago</sub>  
  SMH: Cover The Shorts For Now (Rating Upgrade). VanEck Semiconductors ETF (SMH) fell nearly 30% from its June peak, but Nvidia's positive earnings report makes...
- [Micron Jumped 19% Monday, Then Sank Double Digits. Here's What That Swing Means for SMH Holders](https://www.google.com/goto?url=CAESxwEBxCJF12oENfpkSeI2vcDaPjYlGpdL8cKaKl0skHNFYX14dJ5K2Zv3Nq8i1tOx9mymCuyC35IT00GFI_Mu13KSisZuWuN3P_YBWZA0WiHhYfOQOE3SDCEJ4PANtmZbP8l0NBmYzv0CNuLqRiET-gJO8XXBrG6E-wYny5Efz0KLab4Gqm0vj-tK66lZBEh4VsUcAlFt547J7fwhUWCkQNMYlp9NG61pLNEXkcWYXc6ksiifY1A5x3_BcCzQKXBE8hyrBIATM1Ic&gsessionid=dkEs59JA1PFVP5Fjn60HZcFOyuNoBFuWrptto0a6-_zyV6s1Oun1wg)  
  <sub>24/7 Wall St., 22 hours ago</sub>  
  Micron's 19% Monday surge and double-digit Tuesday reversal reflect a sector-wide AI chip selloff, not company news, and SMH fell about 9%.
- [VanEck Semiconductor ETF drops 7%, Nvidia raises fiscal 2028 revenue forecast by 75%.](https://www.google.com/goto?url=CAESmQEBxCJF11j_OWbT4EAyREArlRVGteDbnKyvmBBLgLBnhLqisZLfxOf_b4GiSurd7hD89Y4m4gyBTvoe-bMA8dZXQfm0FR_irC1PbApT2i4ApkHMgUK1Hgstr-omn61KtbyqV4GiuPFswoNTfNRZBsIdjwqwJ-_16JJYyVoM90069BgQ_enZ7LS8pnhkItBXJNfTg2VyaOV4NMY&gsessionid=dkEs59JA1PFVP5Fjn60HZcFOyuNoBFuWrptto0a6-_zyV6s1Oun1wg)  
  <sub>Pluang, 10 hours ago</sub>  
  The VanEck Semiconductor ETF fell about 7% on November 24, trading near $420, down 37% from its June peak but still up 19% for 2026.
- [Chip ETF Slides 7% Despite Nvidia's Raised Outlook as Huang's Return Fails to Halt Selloff](https://www.google.com/goto?url=CAESfgHEIkXX38RnGvIARcitoENrzsK_LNsAnGI3NeBGvf-CpGN6OYkPDkTKJUYL_6LmOF3ZXG_1sLRwLPj1gEv7og0e1UH175yW4Cy1sN6JB0Ll_i4tCmS9UXccIF-W1Y8-9DHGPkMEU4GU16FfQC2chq-VL_G4ufiJ8R5ci1ytwQ&gsessionid=dkEs59JA1PFVP5Fjn60HZcFOyuNoBFuWrptto0a6-_zyV6s1Oun1wg)  
  <sub>BigGo Finance, 9 hours ago</sub>  
  The VanEck Semiconductor ETF dropped about 7% on Nov. 24, extending losses even after Nvidia raised its fiscal 2028 revenue growth outlook to roughly…
- [Chip stocks erase more than half of Monday's gain as the average stock edges up](https://www.google.com/goto?url=CAEStgEBxCJF1z8f0XiAhZAezShTU2INNtFVV2vD_hR-njsCbxE3-T_G3orxOaYzYGcVCNnuq7rixoZqOsyUCOAxx12yrOL3qojyNMyGyETQbrTJZCz8aCLPYPDSgXAbTI4edS0KHaHi6r2nM1-UkkdyNhrKJ3yXBG4xwxfOjarcs0V_4G87MYHZG7bqJc0LJSJOdhpGy-NWwSGqy1kXs1PuOMAAUGrboRAZECmTLyTwM5I1m8jc7JAzOw&gsessionid=dkEs59JA1PFVP5Fjn60HZcFOyuNoBFuWrptto0a6-_zyV6s1Oun1wg)  
  <sub>Quantisnow, 23 hours ago</sub>  
  At 10:20 a.m. ET Tuesday, the VanEck Semiconductor ETF was down 7.21%, about 56% of its 14.9% gain on Nov. 23 in price terms, while the Nasdaq 100 fund had...
- [Ed Yardeni Says Jensen Huang’s Return To Nvidia Could Ease AI Financing Concerns But Intensify Regulatory Scrutiny](https://www.google.com/goto?url=CAES6wEBxCJF1-HtGPgbSysodR7Wr4MZkh3IxCXj_3BkqdSgiMGFnwfo5a0mi8-EfL2z_VuXs4gSrgncW36ONYEKc_EwQdFkWqsMrF6d1Wc4Rq6xCwga__Uq4rC7wgdA_pW4rvR2Mwa6RAUqm837IY6_Zj6vJgnSoIXoxsicxW6hoM741o5ql0KiyBDJJgOd-ABik3u19W-ndkHfI7IGUYaFtnYzOG0DN9CLdrjmlslrGUDAf0hIge0fRNZIUBhjkUFJeegR9TRozMNjiOG4stYoHIS1TkWhxKJGUBX86toDk96o9K9oz2lRxvTww4MQ&gsessionid=dkEs59JA1PFVP5Fjn60HZcFOyuNoBFuWrptto0a6-_zyV6s1Oun1wg)  
  <sub>TradingView, 4 hours ago</sub>  
  Yardeni Research president Ed Yardeni said Jensen Huang's return as CEO of Nvidia (NVDA) could ease financial constraints on the artificial intelligence...
- [Huang’s Return And Anthropic’s Shaky Debut Prove AI Is Now A National Security Trade](https://www.google.com/goto?url=CAEStQEBxCJF15HVJWq4NAQL60wnv7-gSKEv8cD4rMxxh1ZcGp907joYBQ1lPZ59-XIzUH4QQ_hn0Hh9bR_addU5Q2lgrgB1a9N2rw2hO50DQQUkP3ZbS33OuUob97HSA_rqEOZhA5HN01UftOGa-Pfti_-Sul6v07DYLxLG5z3qCbIz9qPoVuJQVCb0sW36VhTIenWJyYliodEsnB4gsPFQM5NjyEjKTrqkUPugouKoE4HIqiuwri72&gsessionid=dkEs59JA1PFVP5Fjn60HZcFOyuNoBFuWrptto0a6-_zyV6s1Oun1wg)  
  <sub>Seeking Alpha, 26 minutes ago</sub>  
  Analyst sees the AI trade as vulnerable: Anthropic's roughly $900 billion compute commitments and expected junk-rated borrowing spotlight funding risks.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.16% (+0.01 on the week) | 5-year 4.62% (-0.26 on the week) | 10-year 4.83% (-0.24 on the week) | 30-year 5.24% (-0.17 on the week)
Yield curve, 10-year minus 3-month: +0.67 points -- upward sloping (normal)
US dollar index: 103.93 (+0.07 on the week)
Volatility (VIX): 31.72 (+7.2 on the week) -- stressed
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.1% (2026-10-01) | jobless claims 189k (2026-11-21)
Policy and expectations: Fed target 4.00% | market expects 2.1% inflation over 10 years
Rate path: 2-year Treasury 4.63% vs Fed target 3.75-4.00% -- the bond market prices about 3 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score -0.30</summary>

```text
Last close 397.20 (bar of 2026-11-25), from 502 daily bars
Trend: vs 20d SMA 475.33 (-16.4%), 50d 540.61 (-26.5%), 200d 525.53 (-24.4%); 50d above 200d
Momentum: RSI(14) 33.8 | MACD -33.425 vs signal -28.547 (histogram -4.878)
Returns: 1d -6.9% | 5d -13.6% | 1m -28.8% | 3m -30.7%
52-week range: 339.24 - 668.91 (now 17.6% of the way up)
Volatility: ATR(14) 30.24 (7.6% of price) | annualised 20d 95.5%
Volume: 0.17x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.00</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score +0.00</summary>

```text
Fund type: Technology
What it holds: P/E 28.22 | P/B 9.76 | P/S 11.19 | 3y earnings growth n/a
Yield: 0.2%
Three-year record: +42.2% a year | beta to the market 2.12
Cost and size: expense ratio 0.35% | net assets 66.44B
What it is made of: Stocks 99.9%, Cash 0.1%
Largest holdings: NVIDIA Corp 20.2%, Taiwan Semiconductor Manufacturing Co Ltd ADR 9.6%, Texas Instruments Inc 5.7%, Broadcom Inc 5.6%, Advanced Micro Devices Inc 5.3%
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
Rolled up from the 5 largest holdings, 46.4% of the fund by weight
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 1.56 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +71.1% above the current prices
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
Share count change: 1 week: +5.8% (3.12B) over 8d | 1 month: +7.3% (3.92B) over 33d
Shares outstanding: 144.35M | fund size: 57.34B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Turkey (TUR) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Neutral overall – no macro surprise, flat flows, mixed fundamentals, bullish analyst view but no decisive technical breakout.

**Main reasons it gave:**
- Price 24.6% below 200‑day SMA (38.17) and RSI 31.1 with low volume
- Flat share count change (+0.0% week, +0.0% month) indicating no net flow
- Analyst rating 100% buy with weighted price target +41.7% above current price
- Low valuation (P/E 11.63, P/B 1.01) but three‑year return -3.4% per year

<details><summary><b>News</b> — score +0.00</summary>

- [Lider Faktoring Completes TL 120 Million Bill Sale](https://www.tipranks.com/news/company-announcements/lider-faktoring-completes-tl-120-million-bill-sale)  
  <sub>TipRanks, 9 hours ago</sub>  
  Lider Faktoring Anonim Sirketi ( ($TR:LIDFA) ) just unveiled an update. Lider Faktoring A.Ş. completed the domestic sale to qualified investors of a TL 120...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.16% (+0.01 on the week) | 5-year 4.62% (-0.26 on the week) | 10-year 4.83% (-0.24 on the week) | 30-year 5.24% (-0.17 on the week)
Yield curve, 10-year minus 3-month: +0.67 points -- upward sloping (normal)
US dollar index: 103.93 (+0.07 on the week)
Volatility (VIX): 31.72 (+7.2 on the week) -- stressed
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.1% (2026-10-01) | jobless claims 189k (2026-11-21)
Policy and expectations: Fed target 4.00% | market expects 2.1% inflation over 10 years
Rate path: 2-year Treasury 4.63% vs Fed target 3.75-4.00% -- the bond market prices about 3 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score -0.40</summary>

```text
Last close 28.77 (bar of 2026-11-25), from 502 daily bars
Trend: vs 20d SMA 30.86 (-6.8%), 50d 32.80 (-12.3%), 200d 38.17 (-24.6%); 50d below 200d
Momentum: RSI(14) 31.1 | MACD -0.856 vs signal -0.729 (histogram -0.126)
Returns: 1d -2.2% | 5d -7.6% | 1m -6.7% | 3m -29.0%
52-week range: 28.77 - 43.74 (now 0.0% of the way up)
Volatility: ATR(14) 0.65 (2.3% of price) | annualised 20d 35.7%
Volume: 0.18x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.35</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score +0.35</summary>

```text
Fund type: Focused Region
What it holds: P/E 11.63 | P/B 1.01 | P/S 0.62 | 3y earnings growth n/a
Yield: 2.8%
Three-year record: -3.4% a year | beta to the market 0.60
Cost and size: expense ratio 0.59% | net assets 146.42M
What it is made of: Stocks 99.9%, Cash 0.1%
Largest holdings: Aselsan Elektronik Sanayi Ve Ticaret AS 13.3%, Tupras-Turkiye Petrol Rafineleri AS 10.9%, Bim Birlesik Magazalar AS 9.8%, Akbank TAS 6.2%, Turk Hava Yollari AO 4.6%
Sector mix: Industrials 30.8%, Financial services 16.9%, Consumer defensive 12.9%, Energy 10.9%
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

<details><summary><b>What analysts and big funds say</b> — score +0.73</summary>

_Not available today._

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score +0.73</summary>

```text
Rolled up from the 5 largest holdings, 44.9% of the fund by weight
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 1.54 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +41.7% above the current prices
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
Share count change: 1 week: +0.0% (0.00) over 7d | 1 month: +0.0% (0.00) over 32d
Shares outstanding: 15.65M | fund size: 450.25M
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### US real estate (VNQ) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> No macro surprise; technicals mixed with bearish MACD and low volume; modest inflows; analyst view strongly bullish but not enough to outweigh neutral macro/technical backdrop.

**Main reasons it gave:**
- Fund flows: +3% share count increase over 1 week (moderate inflow)
- Technical: MACD below signal (histogram -0.334) and price below 20‑day SMA, low volume
- Macro: No policy surprise; yields down modestly, VIX up 7.2 points
- Analyst view: 100% buy rating with +17.5% price target (bullish but not decisive)

<details><summary><b>News</b> — score +0.00</summary>

- [Vanguard Real Estate Index Fund ETF Shares (VNQ) Stock Price, News, Quote & History](https://ca.finance.yahoo.com/quote/VNQ/)  
  <sub>Yahoo! Finance Canada, 20 hours ago</sub>  
  Vanguard Real Estate Index Fund ETF Shares Overview Vanguard / Real Estate · Daily – Vickers Top Buyers & Sellers for 11/24/2026 · AMD Earnings: More Upside in...
- [REIT Quant rankings: Apple Hospitality leads mid-cap stocks, while Lineage lags](https://www.tradingview.com/news/seekingalpha:1506bff66094b:0-reit-quant-rankings-apple-hospitality-leads-mid-cap-stocks-while-lineage-lags/?mobileapp_new=true)  
  <sub>TradingView, 22 hours ago</sub>  
  With earnings season wrapping up, investors are turning to updated Quant Ratings to see how stocks stack up following their latest quarterly results.
- [VNQ Dec 2026 86.000 put (VNQ261218P00086000) Stock Price, News, Quote & History](https://www.google.com/goto?url=CAEScQHEIkXXwWuSUpfcM3xBHndcdjUfP2A81NeP2uEYKu4U3BHLockHzrb5KBxtCdDp2rgBQwHsi4PWOMr6h1BVYjzBRfzhKNSuzRd92wsek_mdIQjtA7XD2_BkyhdC8LzY4Kr6n81MSCClbRB0bvfEFUoX&gsessionid=YmO_fLVLyyuMjwwFuheDt7kasDy6MlEh0TegGgYTnBl7xrY3hJfzrA)  
  <sub>Yahoo! Finance Canada, 10 hours ago</sub>  
  Find the latest VNQ Dec 2026 86.000 put (VNQ261218P00086000) stock quote, history, news and other vital information to help you with your stock trading and...
- [Small-cap REITs: Top 5 quant picks and 5 stocks to avoid after earning season](https://www.google.com/goto?url=CAESxwEBxCJF16SAWndsCBlq1NUKAl67AnzNa7RgATfMn5LzzI0bRdABLOzmUvlaU1r0Gp6bl15F1qpLpLBF8QLgQACAT4E0SbkOGFhiiF1d9G4ChtVIPccuUHR1YzGuUFdEbD0oMq3DHt-uprswy_-PvtlBFznbuf1s7toCsvX3m8KZ7m52v0BWvXM9hs1ZQYoJZ0b0aNt0GQtAPmJs8lz1gblumRU1yDiZK5UglJNk1Eo34-W76hpN-8ZjeTWmUV52CCIF6PVkyNYA&gsessionid=YmO_fLVLyyuMjwwFuheDt7kasDy6MlEh0TegGgYTnBl7xrY3hJfzrA)  
  <sub>TradingView, 22 hours ago</sub>  
  With earnings season wrapping up, investors are turning to updated Quant Ratings to see how stocks stack up following their latest quarterly results.
- [Best and worst large-mega-cap REIT quant picks as earnings season wraps up](https://www.google.com/goto?url=CAESxQEBxCJF1_j8g45pPqYbYqMAYlXAcx9EXRDK92XqHQ4pbP1exq8ADKKlbDt5-GDuOnsK3TurR_FX_oNtxg_reYPjsXxwAsWWSEm-40AEkeIZRVBR3rGHBAFHL0xnQb5VlpbeWr5ibVaAl7WBD8mGk8DFtQX6LvNpMakvn8HBqg93n6E_HSQuKsGYdqym2p7S20lmbJrXsAMxYTsB5JKZuKVdi_t3Xu7oMJ04sV9JIvFvSzS0HrVbrVv10wGxokujA5wYjWywaA&gsessionid=YmO_fLVLyyuMjwwFuheDt7kasDy6MlEh0TegGgYTnBl7xrY3hJfzrA)  
  <sub>TradingView, 21 hours ago</sub>  
  With earnings season wrapping up, investors are turning to updated Quant Ratings to see how stocks stack up following their latest quarterly results.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.16% (+0.01 on the week) | 5-year 4.62% (-0.26 on the week) | 10-year 4.83% (-0.24 on the week) | 30-year 5.24% (-0.17 on the week)
Yield curve, 10-year minus 3-month: +0.67 points -- upward sloping (normal)
US dollar index: 103.93 (+0.07 on the week)
Volatility (VIX): 31.72 (+7.2 on the week) -- stressed
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.1% (2026-10-01) | jobless claims 189k (2026-11-21)
Policy and expectations: Fed target 4.00% | market expects 2.1% inflation over 10 years
Rate path: 2-year Treasury 4.63% vs Fed target 3.75-4.00% -- the bond market prices about 3 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score -0.20</summary>

```text
Last close 94.41 (bar of 2026-11-25), from 502 daily bars
Trend: vs 20d SMA 95.37 (-1.0%), 50d 92.91 (+1.6%), 200d 95.01 (-0.6%); 50d below 200d
Momentum: RSI(14) 50.0 | MACD 0.226 vs signal 0.560 (histogram -0.334)
Returns: 1d -0.4% | 5d -0.8% | 1m +2.2% | 3m -3.3%
52-week range: 87.00 - 100.95 (now 53.1% of the way up)
Volatility: ATR(14) 1.43 (1.5% of price) | annualised 20d 20.7%
Volume: 0.12x the 20-day average
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
Three-year record: +9.8% a year | beta to the market 0.92
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
Weighted price target: +17.5% above the current prices
Holdings read: VRTPX, WELL, PLD, EQIX, AMT
Recent rating changes among them:
  - WELL: 2026-11-11 UBS: main, Buy -> Buy
  - PLD: 2026-11-02 Wells Fargo: main, Overweight -> Overweight
  - EQIX: 2026-10-29 JP Morgan: main, Overweight -> Overweight
  - AMT: 2026-11-05 Argus Research: reit, Buy -> Buy
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
Share count change: 1 week: +3.0% (2.03B) over 8d | 1 month: +2.1% (1.46B) over 33d
Shares outstanding: 741.68M | fund size: 70.02B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Biotech (XBI) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:** no explanation. It wrote only “NEUTRAL”, so the main reasons below are all it gave.

**Main reasons it gave:**
- VIX up 7.2 points to 31.72 (stressed market conditions)
- No policy or rate surprise this week (Fed target unchanged at 4.00%)
- Technicals: price above 200‑day SMA (+5.8%) but low volume (0.21× 20‑day avg) and mixed recent returns
- Fund flows: +9% month inflow (933.8M) but -0.6% weekly outflow
- Analyst coverage thin (9.5% of fund) with modest buy bias (75% buy)

<details><summary><b>News</b> — score +0.00</summary>

- [Market Moves From Volatility to Stock Picking](https://pro.thestreet.com/market-commentary/market-moves-from-volatility-to-stock-picking)  
  <sub>RealMoney Pro, 23 hours ago</sub>  
  The Invesco QQQ Trust (QQQ) is down 1.7% on Tuesday but is off its early lows after some panicky selling at the open. Nvidia (NVDA) and Anthropic (ANT) are...
- [Anthropic Drops Below IPO Prices, Nvidia Sinks 7% After Record Rally: Stock Market Today](https://www.tradingview.com/news/benzinga:10db8656d094b:0-anthropic-drops-below-ipo-prices-nvidia-sinks-7-after-record-rally-stock-market-today/)  
  <sub>TradingView, 21 hours ago</sub>  
  The artificial-intelligence trade cracked on two fronts Tuesday. Anthropic PBC NASDAQ:ANT slipped below its $83 IPO price less than a week after its record...
- [SBIO: Diversified Exposure To Biotech M&A Upside, Best Used As A Portfolio Diversifier](https://www.google.com/goto?url=CAES0AEBxCJF1y-_yT1F8AT-17z-0ZK2optgEJ0Bi96sKETbCkOEg5LwaX4keiea5wQG1AkXnFnPSMtZYw-FLfDnW2vY1BggOBWWBqS0tyNmlLabwP6q7aGueCdYs5KWuhJjQYxLaC4tJZ3E0r-Uv264EFsKPMIpTksqqy1CEBdV8a7a50H3kghW1S6o5vlIGruqv9nX6gs436ySM1JJttOxEWEBkmRAWLnuJ7HxjPNRSLPv2dAPw4u7SoFed28yGe7NFUshiu6LF52Hv88HYsweAW0a&gsessionid=UfaJo-FhJxEIpesoCoeRWaFh20eWu3W8ClF0yhV6oahjQURc_T6EuQ)  
  <sub>Seeking Alpha, 1 hour ago</sub>  
  SBIO ETF seeks an acquisition-driven upside while diversifying the risk of failed trials; its index requires at least 24 months of cash-burn coverage.
- [Market Enjoys Productive Day After 2 Crazy Ones](https://www.google.com/goto?url=CAESlgEBxCJF18jQaFQ55msSsLmtUajEOk13gYgjESoROy_ZRfHq8Sjg60nwEKfCr7h3d92m7z7TLOHigwIuaJ1fp6Rrdp4QKc31rCjcLmu-U8GYTmbielrq4eEWFee8jqG8uOYjVDaTeXAQAjB-G87e-g4wXzQscKxNub-mNFjQVvCPj8G8XU71xHeEWo-kVI5nte0c_jlKX2c&gsessionid=UfaJo-FhJxEIpesoCoeRWaFh20eWu3W8ClF0yhV6oahjQURc_T6EuQ)  
  <sub>RealMoney Pro, 18 hours ago</sub>  
  The Invesco QQQ Trust (QQQ) dropped 1.8% and the SPDR S&P 500 ETF (SPY) gave up 0.4% on Tuesday as technology and chips were weak again, but after two days...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.16% (+0.01 on the week) | 5-year 4.62% (-0.26 on the week) | 10-year 4.83% (-0.24 on the week) | 30-year 5.24% (-0.17 on the week)
Yield curve, 10-year minus 3-month: +0.67 points -- upward sloping (normal)
US dollar index: 103.93 (+0.07 on the week)
Volatility (VIX): 31.72 (+7.2 on the week) -- stressed
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.1% (2026-10-01) | jobless claims 189k (2026-11-21)
Policy and expectations: Fed target 4.00% | market expects 2.1% inflation over 10 years
Rate path: 2-year Treasury 4.63% vs Fed target 3.75-4.00% -- the bond market prices about 3 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 152.21 (bar of 2026-11-25), from 502 daily bars
Trend: vs 20d SMA 151.36 (+0.6%), 50d 152.52 (-0.2%), 200d 143.84 (+5.8%); 50d above 200d
Momentum: RSI(14) 51.4 | MACD -1.173 vs signal -1.416 (histogram 0.243)
Returns: 1d -2.9% | 5d +4.9% | 1m -1.7% | 3m -9.5%
52-week range: 118.46 - 169.55 (now 66.1% of the way up)
Volatility: ATR(14) 5.47 (3.6% of price) | annualised 20d 49.7%
Volume: 0.21x the 20-day average
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
Three-year record: +26.7% a year | beta to the market 1.01
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

<details><summary><b>What analysts and big funds say</b> — score +0.20</summary>

_Not available today._

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score +0.20</summary>

```text
Rolled up from the 5 largest holdings, 9.5% of the fund by weight  -- thin, so read this as a fact about that slice rather than the fund
Ratings by weight: buy 75.0% | hold 25.0% | sell 0.0% (mean 2.06 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +14.1% above the current prices
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
Share count change: 1 week: -0.6% (-64.05M) over 7d | 1 month: +9.0% (933.80M) over 32d
Shares outstanding: 74.41M | fund size: 11.33B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### US house builders (XHB) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Neutral overall as no macro surprise or decisive technical break occurred; bullish analyst view and strong inflows are offset by bearish technicals and a modest macro backdrop.

**Main reasons it gave:**
- Analyst view: 100% buy rating and +14.4% price target for top holdings covering 18.9% of fund
- Fund flows: share count up 13.4% over the past month, indicating strong inflows
- Technicals: price 2% below 20‑day SMA, negative MACD, volume 0.04× 20‑day average
- Macro: yields up slightly, VIX up 7.2 points to 31.72, inflation 3.7% above Fed target, no policy surprise

<details><summary><b>News</b> — score +0.00</summary>

- [Tesla Helped Ignite Austin’s Housing Boom. But Now the Party’s Over](https://www.benzinga.com/real-estate/26/11/63582708/austin-home-prices-tesla-boom)  
  <sub>Benzinga, 24 hours ago</sub>  
  Tesla helped fuel Austin's housing boom. Now oversupply and softer demand are pushing prices down, giving homebuyers more leverage.
- [Guardian International Equity Select ETF (GIES.TO) Seasonal returns chart](https://uk.finance.yahoo.com/quote/GIES.TO/seasonality/)  
  <sub>Yahoo Finance UK, 20 hours ago</sub>  
  Guardian International Equity Select ETF (GIES.TO) seasonal returns chart provides the mean and median returns by month to inform your investment strategy.
- [iShares Global Energy ETF (IXC.MX) Seasonal returns chart](https://www.google.com/goto?url=CAEScQHEIkXXkoGg27kLqN0qpzakldfhhj5Ub2rniMlhHeLy0wUVpviauOhesuGelxEkt-M_0igRc0MQsRkYFe4WpgYIEhuFHvO1WYtJC7xiqBFlwRmNEdRQ1RSRe6CSjWG2KzvFcMJEstQhAesdy5RxcGzT&gsessionid=VcU5jRFoRfqwlGlmWHbeRi9WmBXmMwlKl9ttvvQcNJRl5-gzEByqoQ)  
  <sub>Yahoo Finance UK, 21 hours ago</sub>  
  iShares Global Energy ETF (IXC.MX) seasonal returns chart provides the mean and median returns by month to inform your investment strategy.
- [NYLI U.S. Large Cap R&D Leaders ETF (LRND) Seasonal returns chart](https://www.google.com/goto?url=CAESbwHEIkXXE3CHX8s8zvedHNvYKVtNzqrVh1gnOZIk9wjWlVHlnBHJbTzzJ-I-StEHn3SFiIEjPNN-GnQkAFMdqJeFSih-4DNUYZBzjnrQxMahuYcjxve8rN_xRhvdjuwrp7fTceuyMpPqfW7qJ_dsyw&gsessionid=VcU5jRFoRfqwlGlmWHbeRi9WmBXmMwlKl9ttvvQcNJRl5-gzEByqoQ)  
  <sub>Yahoo Finance UK, 21 hours ago</sub>  
  NYLI U.S. Large Cap R&D Leaders ETF (LRND). 39.52 0.00 (0.00%). As of 23 November at 16:00:00 GMT-5. Market open. Historical seasonality.
- [WisdomTree USD Floating Rate Treasury Bond UCITS ETF - USD Acc (TFRN.L) Seasonal returns chart](https://www.google.com/goto?url=CAEScQHEIkXXJvT19Quyl4D8ZMqdawuNyNcu8cQdOQcCailEg7OCgQ61jx6YpJbM5lmiyzFy8-GFwf2FthtYeoILocu0npr7StD0JOKmnfi7Yxoq_cudaaNrOtmRxUOYmcG33ETD1YC-hc82GQKJUgFkr4NJ&gsessionid=VcU5jRFoRfqwlGlmWHbeRi9WmBXmMwlKl9ttvvQcNJRl5-gzEByqoQ)  
  <sub>Yahoo Finance UK, 19 hours ago</sub>  
  WisdomTree USD Floating Rate Treasury Bond UCITS ETF - USD Acc (TFRN.L). 62.04 -0.01 (-0.02%). At close: 24 November at 16:29:38 GMT...
- [Invesco US Treasury Bond 7-10 Year UCITS ETF USD Dist (TRXG.L) Seasonal returns chart](https://www.google.com/goto?url=CAEScQHEIkXXTVnvZHS_t-qvFE7DwG4_o5iAUk_qpVcPramUUA57w6_aXQELFJClhU7dgcCVLT8cfs-kPBEa2VtRG2T-KucwHrcnhZbSPveFVFQidUwRHXRkaA1pQt4VxzOnnDUKQ8zdG-ESvoj072l6kSBd&gsessionid=VcU5jRFoRfqwlGlmWHbeRi9WmBXmMwlKl9ttvvQcNJRl5-gzEByqoQ)  
  <sub>Yahoo Finance Australia, 19 hours ago</sub>  
  Invesco US Treasury Bond 7-10 Year UCITS ETF USD Dist (TRXG.L). 2,629.00 -11.00 (-0.42%). At close: 3:13:59 pm GMT. Historical seasonality.
- [Invesco S&P 500 UCITS ETF (SPXDL.XC) Seasonal returns chart](https://www.google.com/goto?url=CAEScwHEIkXXwqYK5PnvP9AS1_qAD5bTqzRjK56I0l118EAiQJKFnCGwil1sSr9WmL693Io9RygoqMCGEk_SGV5tqQOWKU_PLGbQ3pBwLkze6Aa5I7PfjF6qx0SnIBNgwEHUAqo6J7Hi2Cvt-H9BBhkmFwjM8pc&gsessionid=VcU5jRFoRfqwlGlmWHbeRi9WmBXmMwlKl9ttvvQcNJRl5-gzEByqoQ)  
  <sub>Yahoo Finance Australia, 21 hours ago</sub>  
  Historical seasonality. Average monthly price return, 2023 - 2026. 3Y 5Y 10y. 20Y All. Related tickers. BBP Virtus Biotech ETF. 103.46 +4.90%.
- [KICK Space Data Center and Infastructure Index ETF (SDC) holdings](https://www.google.com/goto?url=CAESawHEIkXXoStuQsL2xKNBgOw1gIOX7RQq6VpIlq5dB6_U6sMaegvHVw8dlNg4T_M-mGSjGWdMFnadL40brKbi_aJ8JFK0e7mzc3h9DWHisTlKJIU1kr7Ey3n_AZeBWlNZ1CrIKotRDPNmARpn&gsessionid=VcU5jRFoRfqwlGlmWHbeRi9WmBXmMwlKl9ttvvQcNJRl5-gzEByqoQ)  
  <sub>Yahoo Finance Australia, 21 hours ago</sub>  
  ETF summary. Under normal circumstances, the fund invests at least 80% of its net assets (plus the amount of any borrowings for investment purposes) in...
- [iShares-ESTXX Mid UCITS ETF R (IQQM.DU) Seasonal returns chart](https://www.google.com/goto?url=CAEScgHEIkXXBHHub3xk1WDLWiElqHe_9GZOE6gzqA_Snr-FTP-9V6j45-E811xIr6u1je71W8avuIMTV25Sbyoy2Yj3gVB4BpiZnDZOCVJrnhZ8rUTFjYDSSK212e3B8u_n-iw0JCsqOYXMOmsGywIWOFsTQA&gsessionid=VcU5jRFoRfqwlGlmWHbeRi9WmBXmMwlKl9ttvvQcNJRl5-gzEByqoQ)  
  <sub>Yahoo Finance Australia, 21 hours ago</sub>  
  iShares-ESTXX Mid UCITS ETF R (IQQM.DU) seasonal returns chart provides the mean and median returns by month to inform your investment strategy.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.16% (+0.01 on the week) | 5-year 4.62% (-0.26 on the week) | 10-year 4.83% (-0.24 on the week) | 30-year 5.24% (-0.17 on the week)
Yield curve, 10-year minus 3-month: +0.67 points -- upward sloping (normal)
US dollar index: 103.93 (+0.07 on the week)
Volatility (VIX): 31.72 (+7.2 on the week) -- stressed
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.1% (2026-10-01) | jobless claims 189k (2026-11-21)
Policy and expectations: Fed target 4.00% | market expects 2.1% inflation over 10 years
Rate path: 2-year Treasury 4.63% vs Fed target 3.75-4.00% -- the bond market prices about 3 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score -0.30</summary>

```text
Last close 99.63 (bar of 2026-11-25), from 502 daily bars
Trend: vs 20d SMA 101.70 (-2.0%), 50d 98.59 (+1.1%), 200d 104.10 (-4.3%); 50d below 200d
Momentum: RSI(14) 48.9 | MACD 0.036 vs signal 0.455 (histogram -0.420)
Returns: 1d -1.6% | 5d -1.1% | 1m +0.5% | 3m -4.7%
52-week range: 92.84 - 121.36 (now 23.8% of the way up)
Volatility: ATR(14) 2.90 (2.9% of price) | annualised 20d 41.5%
Volume: 0.04x the 20-day average
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
Three-year record: +7.5% a year | beta to the market 1.40
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

<details><summary><b>What analysts and big funds say</b> — score +0.40</summary>

_Not available today._

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score +0.40</summary>

```text
Rolled up from the 5 largest holdings, 18.9% of the fund by weight  -- thin, so read this as a fact about that slice rather than the fund
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 1.55 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +14.4% above the current prices
Holdings read: ALLE, SN, MAS, W, CVCO
Recent rating changes among them:
  - ALLE: 2026-11-03 Morgan Stanley: main, Equal-Weight -> Equal-Weight
  - SN: 2026-11-09 Guggenheim: main, Buy -> Buy
  - MAS: 2026-11-05 Argus Research: main, Buy -> Buy
  - W: 2026-11-12 Argus Research: main, Buy -> Buy
  - CVCO: 2026-11-02 Oppenheimer: reit, Outperform -> Outperform
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
Share count change: 1 week: +1.3% (20.43M) over 7d | 1 month: +13.4% (193.07M) over 32d
Shares outstanding: 16.36M | fund size: 1.63B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### US materials and chemicals (XLB) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Neutral overall; bullish analyst view is offset by bearish technicals, flat fund flows and stressed macro environment.

**Main reasons it gave:**
- Analyst view: 100% buy rating and +15.9% price target for top holdings (34% weight)
- Technicals: price below 20‑day, 50‑day and 200‑day SMAs; RSI 40.8, MACD negative; volume 0.13× 20‑day average
- Fund flows: flat share count (0% change over 1 week and 1 month)
- Macro: VIX up 7.2 points to 31.72 indicating market stress; yields unchanged, no policy surprise

<details><summary><b>News</b> — score +0.00</summary>

- [State Street Materials Select Sector SPDR ETF (XLB) Stock Price, News, Quote & History](https://ca.finance.yahoo.com/quote/XLB/)  
  <sub>Yahoo! Finance Canada, 20 hours ago</sub>  
  State Street Materials Select Sector SPDR ETF (XLB) · -1.32% · -2.22% · -0.24% · 10.63% · 15.97% · 14.14% · 382.84%. Key Events. Baseline.
- [(XLB) Strategic Investment Report (XLB:CA)](https://news.stocktradersdaily.com/canada/xlb-strategic-investment-report_20261124_f028a7)  
  <sub>Stock Traders Daily, 12 hours ago</sub>  
  Strategic Investment Report for iShares Core Canadian Long Term Bond Index ETF (XLB) Highlighting Buy and Sell Opportunities.
- [Five materials stocks with attractive valuations following Q3 earnings (XLB:NYSEARCA)](https://www.google.com/goto?url=CAESpwEBxCJF16k5fCzwLTuEWaGGPbejAzDqFgEeEahpWAdy6tQjGgYrbDMTD2PTN-N2bJgrXQ0bBca1znpTM5b0xDcYigpu72uGeMrF__JsWFTmlTbBaWj13R-TE3ml9bSygD6jhTEtNJEGbWelBFNsWofXjLrVH4-CU1iTc6nn0eUBlUiI2M0xQlY7yvr293LGmcOwLZXKOGEt4ZylTBwbq52yluy7O4Mt-g&gsessionid=zLwtzhcpVz5njip8sOLRaEub1ZDut60NDADS91wJ2XtuaHKzojPihA)  
  <sub>Seeking Alpha, 2 hours ago</sub>  
  Seeking Alpha's Quant Ratings put Century Aluminum and LyondellBasell atop the materials valuation screen after Q3, both with A grades; three others earn...
- [State Street Industrial Select Sector SPDR ETF (XLI) Stock Price, News, Quote & History](https://www.google.com/goto?url=CAESYgHEIkXXsBgkW5Jnr16A7qwMjxMIr5tnqeF9A1DJ3iAXvagY2LCwY4iVlrl2axT9sSv9788Le17RS0SPcfiw5cUWcCUL1C24p-H7CoDks1lRjl8tS3llBFbV_9nXLhXuOPXR&gsessionid=zLwtzhcpVz5njip8sOLRaEub1ZDut60NDADS91wJ2XtuaHKzojPihA)  
  <sub>Yahoo! Finance Canada, 6 hours ago</sub>  
  Find the latest State Street Industrial Select Sector SPDR ETF (XLI) stock quote, history, news and other vital information to help you with your stock...
- [BATT Vs. LIT: Why 2 Battery ETFs Deliver Different Exposure](https://www.google.com/goto?url=CAESnQEBxCJF1zRgX_tU1mGoj6-t3Cytx1typqNDS2T3pSFBkaCsF_BXAtLHv5tAgwiJDx90hmO5BTArHFt50OqOylguyh2VrwTXTNBOh5OC_3ivmPfiT4Ty7FFx4sb78ynR1tWrlke3tVBFUavcfPa2sZPmWcUI2FRPWyy_dRpagy1_pStpl6uZ-kijdfkzw6ozMO-bgHoN16M-27Z5q9VJ&gsessionid=zLwtzhcpVz5njip8sOLRaEub1ZDut60NDADS91wJ2XtuaHKzojPihA)  
  <sub>Seeking Alpha, 17 hours ago</sub>  
  Despite sharing similar mandates on paper, the two battery ETFs BATT and LIT share only a 32% holdings overlap and take fundamentally different approaches...
- [XLB Dec 2026 47.500 put (XLB261211P00047500) stock price, news, quote and history](https://www.google.com/goto?url=CAEScQHEIkXXMvLeAX_wGr6t5zOXRzvaRD4HiAYTZYuwdMzq_WDe_JQcuqxNtx8iuAAu7TefFpDJsqugzsvO8fu68awRGXR4pVMnkWMa701uuhBsyqhVgJ394-H1luqTIYYQlbN1oiK6nysykc-zizvR6pL3&gsessionid=zLwtzhcpVz5njip8sOLRaEub1ZDut60NDADS91wJ2XtuaHKzojPihA)  
  <sub>Yahoo Finance UK, 16 hours ago</sub>  
  Find the latest XLB Dec 2026 47.500 put (XLB261211P00047500) stock quote, history, news and other vital information to help you with your stock trading and...
- [XLB Dec 2026 50.000 put (XLB261211P00050000) Stock Price, News, Quote & History](https://www.google.com/goto?url=CAEScQHEIkXXomRdRuMZ6zjC7qf6FFS3-DQ6qY7G85t3UdK_bSOeJjNPm29oL2xJxAZ92q4S_tTo1t1YiMJgEZVn7jLMtD2t3K8tjKhTX8eyHpfXO4PIUfSuGNz6MwnX3CZAzWaReKY0SL5eIqPG0FOelen_&gsessionid=zLwtzhcpVz5njip8sOLRaEub1ZDut60NDADS91wJ2XtuaHKzojPihA)  
  <sub>Yahoo! Finance Canada, 19 hours ago</sub>  
  Find the latest XLB Dec 2026 50.000 put (XLB261211P00050000) stock quote, history, news and other vital information to help you with your stock trading and...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.16% (+0.01 on the week) | 5-year 4.62% (-0.26 on the week) | 10-year 4.83% (-0.24 on the week) | 30-year 5.24% (-0.17 on the week)
Yield curve, 10-year minus 3-month: +0.67 points -- upward sloping (normal)
US dollar index: 103.93 (+0.07 on the week)
Volatility (VIX): 31.72 (+7.2 on the week) -- stressed
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.1% (2026-10-01) | jobless claims 189k (2026-11-21)
Policy and expectations: Fed target 4.00% | market expects 2.1% inflation over 10 years
Rate path: 2-year Treasury 4.63% vs Fed target 3.75-4.00% -- the bond market prices about 3 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score -0.40</summary>

```text
Last close 49.50 (bar of 2026-11-25), from 502 daily bars
Trend: vs 20d SMA 51.66 (-4.2%), 50d 50.75 (-2.5%), 200d 51.20 (-3.3%); 50d below 200d
Momentum: RSI(14) 40.8 | MACD -0.480 vs signal -0.119 (histogram -0.361)
Returns: 1d -1.3% | 5d -1.9% | 1m -4.4% | 3m -7.0%
52-week range: 43.39 - 53.90 (now 58.1% of the way up)
Volatility: ATR(14) 1.01 (2.0% of price) | annualised 20d 26.9%
Volume: 0.13x the 20-day average
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
Three-year record: +9.4% a year | beta to the market 0.76
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

<details><summary><b>What analysts and big funds say</b> — score +0.50</summary>

_Not available today._

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score +0.50</summary>

```text
Rolled up from the 5 largest holdings, 34.0% of the fund by weight
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 1.65 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +15.9% above the current prices
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
Shares outstanding: 71.92M | fund size: 3.56B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### US energy companies (XLE) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Neutral overall: bullish analyst coverage (+16.8% price target) is offset by bearish fundamentals (inventory builds and falling price outlook) and flat fund flows; no macro surprise or decisive technical break.

**Main reasons it gave:**
- Energy inventories show builds across crude, gasoline, diesel, and natural gas (bearish)
- EIA forecasts WTI crude price to fall ~13% over six months (bearish)
- Analyst coverage of top holdings is 100% buy with a +16.8% price target (bullish)
- Fund flows are flat, indicating no net demand shift (neutral)

<details><summary><b>News</b> — score +0.00</summary>

- [Why Chevron Investors Could Make Sense Of ETFs Now](https://sg.finance.yahoo.com/news/why-chevron-investors-could-sense-121452095.html)  
  <sub>Yahoo Finance Singapore, 3 hours ago</sub>  
  You might like Chevron for its global energy reach, but owning the stock directly means carrying its specific risks by yourself. Simply Wall St highlights...
- [Energy Leads Earnings Surge in Europe and the U.S.](https://etfdb.com/sector-investing-content-hub/energy-leads-earnings-surge-europe-us/)  
  <sub>ETF Database, 16 hours ago</sub>  
  European and U.S. earnings growth topped 30% last quarter, with energy leading both, per State Street and FactSet.
- [Ten undervalued energy stocks after Q3 earnings, led by Par Pacific (XLE:NYSEARCA)](https://www.google.com/goto?url=CAESowEBxCJF11a6fEMwl0wd7FJ9NYh2FPBNLPHBkgiMiQgusTZzAtNdxYBokMgjzTnnX1Ax3fWTpIsL68zKHwa0Yk3jxKq39pSX76XQYtJ3sqKwUmTMsfg-aLCcFXIDcmmzUuqV7iQ4iAPWUPZ3RcZ7B7vBM-XGUnHDMRuEtsjO4m1ckV8pTsIeL_wdjC-B1G7nMKHOmCPjUucs2OZjGgsMRmIPbD88&gsessionid=-apFs-zrEHFYM_k9VBVsSUJszlo5L1-fxFQ1kXav83FTuOmh4bK3mA)  
  <sub>Seeking Alpha, 3 hours ago</sub>  
  The U.S. energy sector is navigating an uncertain outlook as investors weigh crude oil prices, refining margins and the prospects for global energy demand...
- [Quant check: Top- and bottom-rated small-cap energy stocks post-earnings](https://www.google.com/goto?url=CAESwQEBxCJF1-j0RE8knSuHDfSGm_u0jMrtnP63Nxqt5E1-5Tdw5ofeTSr1bJgAiJvdQLMGe_fBm-sF29yRqjJaa0gLdOLmAdBbIx5uOIFDKcFEuIaYkqTMHIROhcZlMjXnyaiqH3FDRCGGaZ0-8gx_Xf0GdhiaGreXuKa2Y-xCyMS9ntSQ80Cj5t9xq6QyQYsGcz0fnyoXEMb-vwZ6CTarhtYQnB9i5-7_JBKbgV89ql_rZjzFQt8DpDQyyZrhq6Pl7Ha0&gsessionid=-apFs-zrEHFYM_k9VBVsSUJszlo5L1-fxFQ1kXav83FTuOmh4bK3mA)  
  <sub>TradingView, 21 hours ago</sub>  
  With earnings season wrapping up, investors are turning to updated Quant ratings to see how stocks stack up following their latest quarterly results.
- [Global X USD High Interest Savings ETF - Class V (UCSH-V.TO) latest stock news and headlines](https://www.google.com/goto?url=CAESbQHEIkXXPXYa1ehqGKzHh9DGYKpIYdWtQNnvSrPwfur2k9DvZH5LNEbUDtqUy8INzEqkCwUm2auWbGGv2GzsG5SpGudvMd_glPGaUeAgqPiLCR97Fy2JOmO6JUOKVV4FeId0lvU-dSmbws0B5ic&gsessionid=-apFs-zrEHFYM_k9VBVsSUJszlo5L1-fxFQ1kXav83FTuOmh4bK3mA)  
  <sub>Yahoo Finance UK, 22 hours ago</sub>  
  Global X USD High Interest Savings ETF - Class V (UCSH-V.TO). 50.97 -0.01 (-0.02%). As of 20 November at 9:30:00 GMT-5. Market open.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.16% (+0.01 on the week) | 5-year 4.62% (-0.26 on the week) | 10-year 4.83% (-0.24 on the week) | 30-year 5.24% (-0.17 on the week)
Yield curve, 10-year minus 3-month: +0.67 points -- upward sloping (normal)
US dollar index: 103.93 (+0.07 on the week)
Volatility (VIX): 31.72 (+7.2 on the week) -- stressed
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.1% (2026-10-01) | jobless claims 189k (2026-11-21)
Policy and expectations: Fed target 4.00% | market expects 2.1% inflation over 10 years
Rate path: 2-year Treasury 4.63% vs Fed target 3.75-4.00% -- the bond market prices about 3 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 60.42 (bar of 2026-11-25), from 502 daily bars
Trend: vs 20d SMA 63.34 (-4.6%), 50d 64.42 (-6.2%), 200d 59.84 (+1.0%); 50d above 200d
Momentum: RSI(14) 36.0 | MACD -1.404 vs signal -1.016 (histogram -0.388)
Returns: 1d -0.1% | 5d -1.4% | 1m -11.4% | 3m -3.0%
52-week range: 43.81 - 70.02 (now 63.4% of the way up)
Volatility: ATR(14) 1.45 (2.4% of price) | annualised 20d 30.2%
Volume: 0.12x the 20-day average
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
Three-year record: +15.9% a year | beta to the market -0.22
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

<details><summary><b>What analysts and big funds say</b> — score +0.80</summary>

_Not available today._

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score +0.80</summary>

```text
Rolled up from the 5 largest holdings, 59.0% of the fund by weight
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 2.10 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +16.8% above the current prices
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
Shares outstanding: 186.42M | fund size: 11.26B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### US banks and finance (XLF) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:** no explanation. It wrote only “Neutral”, so the main reasons below are all it gave.

**Main reasons it gave:**
- Macro: yields stable, Fed target unchanged, no surprise in inflation or unemployment data
- Technical: price below 20‑day SMA, RSI 43.6, low volume, MACD negative – no decisive break
- Fund flows: share count flat over week and month, indicating no net demand shift
- Analyst view: 70.7% buy on 43% of fund, price target +11.5% above current but limited coverage

<details><summary><b>News</b> — score +0.00</summary>

- [Should You Invest in the State Street Financial Select Sector SPDR ETF (XLF)?](https://finance.yahoo.com/markets/stocks/articles/invest-state-street-financial-select-102002762.html)  
  <sub>Yahoo Finance, 4 hours ago</sub>  
  Launched on December 16, 1998, the State Street Financial Select Sector SPDR ETF (XLF) is a passively managed exchange traded fund designed to provide a...
- [Mid-Cap Financial Stocks: Top and bottom quant-rated names after Q3](https://www.tradingview.com/news/seekingalpha:b37148705094b:0-mid-cap-financial-stocks-top-and-bottom-quant-rated-names-after-q3/?mobileapp_new=true)  
  <sub>TradingView, 20 hours ago</sub>  
  The latest earnings season has provided investors with an updated view of mid-cap financial companies' performance and fundamentals.
- [Large-cap financial stocks: Top and bottom quant-rated picks after Q3](https://www.google.com/goto?url=CAESvwEBxCJF1_4KVAT3pqy8YXLG7c0Uh5Xzi87g_I_rkHYn3U9tBcGH9LKaHtYRxPz7PXLcL0vyEJdBroWAAtSmM99hWZNoPSL9E1ywMaw_-f17071kXJBJfFaETIZqH_Yf3V4yH29BPz7485dDkPIdIAcTBO0e-U8a2kJenjqG2Xomzkxdx1netSVStKdDLD1kZI2cNjE9aYO7_6NdBBgfRDd3ToyZVO43optOBFVwPNVZEyGzrPRI5uZ_Q4y_jHRH7A&gsessionid=bT8h0TVaOXU2dHmLaLfe-37IrWXcWdW2lou-kozqdd4Kn9Qo3rNy-w)  
  <sub>TradingView, 20 hours ago</sub>  
  The latest earnings season has provided investors with an updated view of large-cap financial companies' performance and fundamentals.
- [Energy Leads Earnings Surge in Europe and the U.S.](https://www.google.com/goto?url=CAESkAEBxCJF11okAVSAfTuGNgD5RMX_Nv_bnv2r6d-_R0cRfXhTnuKNkFb4ZVmGytgNNhj9WsGLpLDRuFTVs3WwaVsDmilr4UjLFIX--nqQ_GD1RjIqqASkcanzRq2VjGElsbBm-ZKVGvEx9YzEohJFQf15JpyktoF8xp5JzxrpR8p4d8-oFO7dhRvl8YwekGp3Ai8&gsessionid=bT8h0TVaOXU2dHmLaLfe-37IrWXcWdW2lou-kozqdd4Kn9Qo3rNy-w)  
  <sub>ETF Database, 16 hours ago</sub>  
  European and U.S. earnings growth topped 30% last quarter, with energy leading both, per State Street and FactSet.
- [Small-cap financial stocks: Top and bottom quant-rated picks after Q3](https://www.google.com/goto?url=CAESvwEBxCJF19urQP6zY7tmbEanpSFkoiNg5vs5741N68S8Xon0gLYGKCfkspZPPrXIkheYfEqbA2qrMerzHnDflF05xYc9mIrWq5_nYe1jKuoLAg9JIOzx9ZdQLWPKiumzliVcynrpCMsgwuSgEbXgUOeGbUPjof2f0_2fkZNhhgzDWnoooKS38mHsD-dAJ0tq_Xk1uVXtQCkSd0gJiPYwWdKTceyHYMa-UTn_zNPQfQ7P-vedoCnyg_gKlSBshyN8kA&gsessionid=bT8h0TVaOXU2dHmLaLfe-37IrWXcWdW2lou-kozqdd4Kn9Qo3rNy-w)  
  <sub>TradingView, 21 hours ago</sub>  
  The latest earnings season has provided investors with an updated view of small-cap financial companies' performance and fundamentals.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.16% (+0.01 on the week) | 5-year 4.62% (-0.26 on the week) | 10-year 4.83% (-0.24 on the week) | 30-year 5.24% (-0.17 on the week)
Yield curve, 10-year minus 3-month: +0.67 points -- upward sloping (normal)
US dollar index: 103.93 (+0.07 on the week)
Volatility (VIX): 31.72 (+7.2 on the week) -- stressed
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.1% (2026-10-01) | jobless claims 189k (2026-11-21)
Policy and expectations: Fed target 4.00% | market expects 2.1% inflation over 10 years
Rate path: 2-year Treasury 4.63% vs Fed target 3.75-4.00% -- the bond market prices about 3 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 55.40 (bar of 2026-11-25), from 502 daily bars
Trend: vs 20d SMA 57.14 (-3.0%), 50d 55.82 (-0.7%), 200d 54.04 (+2.5%); 50d above 200d
Momentum: RSI(14) 43.6 | MACD -0.150 vs signal 0.198 (histogram -0.348)
Returns: 1d -1.3% | 5d -1.8% | 1m -0.9% | 3m -4.3%
52-week range: 47.81 - 59.20 (now 66.6% of the way up)
Volatility: ATR(14) 0.99 (1.8% of price) | annualised 20d 25.4%
Volume: 0.11x the 20-day average
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
Three-year record: +18.2% a year | beta to the market 0.68
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

<details><summary><b>What analysts and big funds say</b> — score +0.40</summary>

_Not available today._

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score +0.40</summary>

```text
Rolled up from the 5 largest holdings, 43.3% of the fund by weight
Ratings by weight: buy 70.7% | hold 29.3% | sell 0.0% (mean 2.00 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +11.5% above the current prices
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
Shares outstanding: 883.44M | fund size: 48.94B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### US industry (XLI) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Neutral overall – no material macro surprise, flat fund flows, and technicals show a downtrend but lack decisive break on heavy volume. Analyst coverage is bullish for the top‑holdings slice (24% of fund) but does not dominate the fund.

**Main reasons it gave:**
- Flat fund flows (0% change in share count over 1 week and 1 month)
- Technical downtrend with negative MACD and RSI 37.3, low volume and no decisive break
- Analyst coverage of top holdings bullish (100% buy, mean rating 1.74) but only covers 24% of fund
- Macro backdrop: normal upward yield curve, VIX high at 31.7, inflation 3.7% (no major surprise)

<details><summary><b>News</b> — score +0.00</summary>

- [State Street Industrial Select Sector SPDR ETF (XLI) Stock Price, News, Quote & History](https://ca.finance.yahoo.com/quote/XLI/)  
  <sub>Yahoo! Finance Canada, 6 hours ago</sub>  
  State Street Industrial Select Sector SPDR ETF (XLI) · -1.91% · -1.83% · -5.91% · 4.18% · 7.74% · 52.35% · 596.50%. Key Events. Baseline.
- [RTX Corp (NYSE: RTX) Posts $340B Backlog And 11% Sales Growth, Pushing Investors To Weigh ETF Exposure Options](https://www.foreignpolicyjournal.com/2026/11/25/rtx-corp-nyse-rtx-posts-340b-backlog-and-11-sales-growth-pushing-investors-to-weigh-etf-exposure-options/)  
  <sub>Foreign Policy Journal, 2 hours ago</sub>  
  A record order backlog of $340 billion and an 11% year-over-year revenue gain in the third quarter of 2026 have put RTX Corp (NYSE: RTX) squarely back on.
- [American Airlines tops undervalued industrials stocks ahead of holiday travel rush (XLI:NYSEARCA)](https://www.google.com/goto?url=CAESswEBxCJF17M-g1w1eT0ZuB8mapUw6sm7piKoqDusRFNtoWmG7PqW20srq_QWWYWG6Go4_aWiFr43SAEUV4XMx3piNXsjGsRxhjihWqqGwWY6y2hKiZjBkWWxu0xLDvJyH60HO8w3MgSSksYDlZMw8ofRYqg_iRqcEeA3Y99WgNSl8q277X9BMrBVParTd-zo_Vhmy5079-tvt9ir-L-BSS-vmJdJNQblraKBXoO2YlybapBOvw&gsessionid=zzusAGyPGUOzZh3pd3aWfiPchfzx5UF2m3V98vStU4cTSQ7GHU4kag)  
  <sub>Seeking Alpha, 1 hour ago</sub>  
  American Airlines leads Seeking Alpha's 15-stock industrials valuation screen with an A+ grade, joined by Allegiant, Southwest and StandardAero.
- [Energy Leads Earnings Surge in Europe and the U.S.](https://www.google.com/goto?url=CAESmAEBxCJF1ykNTjmw_ctJwubPBqUL3oSbxBiUL2VhCaWXWwmrLFfwHfBNX5rv0BxeL9dpxS5tCt4_Z1ad7-9K2biDuEoS4w_2EV7zjNJtR0_iwinZehZ73PR7FHIC34at6C5c1k6JgmrxCtcljZ27pLh8uuMzy-RwEFEsI_QU-H_6zgJjB3VHtNPDSsrBsRhr6ni4jVYZHkYbiA&gsessionid=zzusAGyPGUOzZh3pd3aWfiPchfzx5UF2m3V98vStU4cTSQ7GHU4kag)  
  <sub>ETF Trends, 19 hours ago</sub>  
  European and U.S. earnings growth topped 30% last quarter, with energy leading both, per State Street and FactSet.
- [Dell Reports Today. Here’s How Much of Your Tech ETF Is Riding on Its AI Server Business](https://www.google.com/goto?url=CAESwgEBxCJF1-cVgxd9MajshBsrEiLZ2BN21LPEHz4_R6I6GKiebON3dr23gbw_LHCX2-ZNbc1hJk2Ju0yo0V8LOJQL2E6rdBhO88sjxb5xSpSV858ojukbAP2yVrW1sQy17CfrD0wGUBeVE583hlceEKmZMv1LyVW2eTj1G94p-qwTYfWzoc6tJJOGtPBLDjjGkuvnooGchlCoBvJLBb4mHR8s3ODr-6SLCYzaNEAlHrYocPWHtpQVPSEDP5UA6rdIH5Tbyw&gsessionid=zzusAGyPGUOzZh3pd3aWfiPchfzx5UF2m3V98vStU4cTSQ7GHU4kag)  
  <sub>24/7 Wall St., 21 hours ago</sub>  
  Dell's stock is sliding into tonight's earnings, and tech fund owners are bracing for the fallout. The bigger risk to your retirement account may not be...
- [RDVI: Great Job Balancing Growth And Income For Today's Volatile Market (BATS:RDVI)](https://www.google.com/goto?url=CAESxwEBxCJF14YMwBSbMP9qmebR11pbaN6Au3xjEoe_Qo82W7gyTi8e90e8Sv7kzboi7mCFDt2FhY9O6iTnZnu9Y-RF29aoo4lay9HbtWMOHJ_kTbv5_wCvq4s87G6kxmIkJ9Td6PHA1Lpdb990aBztON9iXtiZmh_X29tNhT9MI7ZvEYaEVSrDJrkb8zN8PHcsvJ_nA_0wBS0ob-jyVelC4BgyF8UDr1M0gPPBpY6Nl8Qr0OA2BE_-n6rEKSpw9hK-KDwhPd8vxx9-&gsessionid=zzusAGyPGUOzZh3pd3aWfiPchfzx5UF2m3V98vStU4cTSQ7GHU4kag)  
  <sub>Seeking Alpha, 5 hours ago</sub>  
  The FT Vest Rising Dividend Achievers Target Income ETF is a strong buy: the recent sell-off offers a compelling entry for income and growth investors.
- [Form 4 State Street® Industrial Select Sector SPDR® ETF For: 24 November By Investing.com](https://www.google.com/goto?url=CAESvgEBxCJF1xmGJklqvq4Dqlliz-Gysaac3KgdlYJimOwzzw7HHc05amMxMwsd3eRYJjDLZA05dzeKEKWQvpzSXHzCJBBfQnKAJjYH6kZHqCoesw3t9C7bTQtNFY5-n_5MO9PF68XNjuh8R7oUJ-6bozvEvXHXzpyJuw1C6mmKBOuNq-bw9lTyyPVyTU65fXd9OyjEmLXxJOTyRE4oWSSIAqYkR24S0-Zuk0dnftjjZ5lXCZkRdgeJkgnvqz-bK88r&gsessionid=zzusAGyPGUOzZh3pd3aWfiPchfzx5UF2m3V98vStU4cTSQ7GHU4kag)  
  <sub>Investing.com India, 18 hours ago</sub>  
  Filed Pursuant to Rule 424(b)(2). Registration No. 333-277211. November 20, 2026. PRICING SUPPLEMENT. (To Product Supplement No. 2 dated May 8, 2024, ETF...
- [Cramer Turns Eyes to Retail Stocks and Highlights His 2 Favorites](https://www.google.com/goto?url=CAESfgHEIkXXDIQGHlWGURdKXszLgU2-RuFwf8TJVkn-EbrMyEH-J5o7wQrwMf-aOVUVl9krsmZ7gMlPnnH8sfKjEitn_mhoz3mziTP4xF6duhwT_hwTiNUzvedPpfpE-Im5EB0VNw65zxgYVdxp-U3KwMI7LK5SNDuisB0j6ODMkQ&gsessionid=zzusAGyPGUOzZh3pd3aWfiPchfzx5UF2m3V98vStU4cTSQ7GHU4kag)  
  <sub>BeInCrypto, 8 hours ago</sub>  
  Jim Cramer sorts six retail stocks after Tuesday earnings and praises 2 as the sector outpaces tech this quarter.
- [XLK eyes critical support as AI credit fears mount](https://www.google.com/goto?url=CAESmAEBxCJF12YdMp0mVbs5SyGQsLw_z_nY38wTwCtlGmRw8V-yeCJKbruPRrH9Vcb_no-5VJ_8lipZZwD14BV6tMUFBrRO25I9GCz8KQ0vf5hreO-rx8-kUGYAFRtZDO1s-szKOkRjVT73MMPcYKY_8lEoEVo_dxinedQ4T1CsOUnFJo00j_8aYFtUPW3qfJ7PRpay5JgVXp-TuQ&gsessionid=zzusAGyPGUOzZh3pd3aWfiPchfzx5UF2m3V98vStU4cTSQ7GHU4kag)  
  <sub>FXStreet, 5 hours ago</sub>  
  Over the past month, the news cycle has been relentless for technology stock holders. Jensen Huang departed Nvidia on 12 November, the board rejected his...
- [Weekly ETFs: Seven of 11 sectors record outflows; Communication services sector leads inflows](https://www.google.com/goto?url=CAES1gEBxCJF1w_aFeoNJxSOnOw1wOApPzvrTtHtlU0xDDdM8px7M-r2ir-0Vem1tTfUWI3hP6NZgRNS1UOfMLS32nSKJhrQachN78MgvuTnT7CMzcUSrhzW3maEzoyT8MpBwAnmD62kRzJIt4qxZ15sRAcV-Buc5LAF7FGovIc2x7SLddfPN8B2n9X80f7cuy0QU3hr5JwVFFWmVKFnfGodkCMCQE3omO9jAO7LzAMCeYn35XzDO5fVRky1z9Anc9DUqtA2Itx0EV8HFJip-Sq_5mV1HdY0fwRk&gsessionid=zzusAGyPGUOzZh3pd3aWfiPchfzx5UF2m3V98vStU4cTSQ7GHU4kag)  
  <sub>TradingView, 18 hours ago</sub>  
  The world's largest exchange-traded fund, SPDR S&P 500 ETF Trust AMEX:SPY, saw outflows of $2.50B for the week ended November 20, while its price...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.16% (+0.01 on the week) | 5-year 4.62% (-0.26 on the week) | 10-year 4.83% (-0.24 on the week) | 30-year 5.24% (-0.17 on the week)
Yield curve, 10-year minus 3-month: +0.67 points -- upward sloping (normal)
US dollar index: 103.93 (+0.07 on the week)
Volatility (VIX): 31.72 (+7.2 on the week) -- stressed
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.1% (2026-10-01) | jobless claims 189k (2026-11-21)
Policy and expectations: Fed target 4.00% | market expects 2.1% inflation over 10 years
Rate path: 2-year Treasury 4.63% vs Fed target 3.75-4.00% -- the bond market prices about 3 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score -0.20</summary>

```text
Last close 157.53 (bar of 2026-11-25), from 502 daily bars
Trend: vs 20d SMA 165.72 (-4.9%), 50d 167.41 (-5.9%), 200d 173.13 (-9.0%); 50d below 200d
Momentum: RSI(14) 37.3 | MACD -2.323 vs signal -1.486 (histogram -0.838)
Returns: 1d -2.5% | 5d -4.3% | 1m -6.2% | 3m -11.9%
52-week range: 151.44 - 186.51 (now 17.4% of the way up)
Volatility: ATR(14) 3.68 (2.3% of price) | annualised 20d 32.4%
Volume: 0.14x the 20-day average
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

<details><summary><b>What analysts and big funds say</b> — score +0.65</summary>

_Not available today._

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score +0.65</summary>

```text
Rolled up from the 5 largest holdings, 24.0% of the fund by weight  -- thin, so read this as a fact about that slice rather than the fund
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 1.74 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +37.1% above the current prices
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
Shares outstanding: 136.63M | fund size: 21.52B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### US technology (XLK) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Neutral overall; bullish analyst view and strong inflows are offset by bearish technicals and a stressed macro environment.

**Main reasons it gave:**
- Fund flows show inflows: share count +4.9% week, +8.3% month
- Analyst view is bullish: all buy ratings, weighted price target +42.7% above current price
- Technical indicators are bearish: price below 20‑day, 50‑day, 200‑day SMAs, RSI 33.3 indicating oversold
- Macro environment stressed: VIX 31.7, yields up, Fed rate hike expectations

<details><summary><b>News</b> — score +0.00</summary>

- [State Street Technology Select Sector SPDR ETF (XLK) stock price, news, quote and history](https://uk.finance.yahoo.com/quote/XLK/)  
  <sub>Yahoo Finance UK, 3 hours ago</sub>  
  State Street Technology Select Sector SPDR ETF (XLK) · -3.78% · -14.27% · -12.92% · 9.11% · 12.32% · 84.55% · 869.50%. Key events. Baseline.
- [Large-Cap Tech Stocks Remain More Promising Than Semiconductor Stocks, Including Memory](https://seekingalpha.com/article/4971812-large-cap-tech-stocks-remain-more-promising-than-semiconductor-stocks-including-memory)  
  <sub>Seeking Alpha, 3 hours ago</sub>  
  Analyst sees the tech correction as no bear market yet, though prices could fall after a rebound; prefers XLK over QQQ for mega-cap tech exposure.
- [XLK eyes critical support as AI credit fears mount](https://www.google.com/goto?url=CAESmQEBxCJF1wND2sXHDSzr5U_mn9IlzaWXoO3KmX71Mn79BCZvUAFQlYdB39Q38-jCH-pBOVljB_WK-CkMR8qdlqmoKyX59qEwHvjlyb7A3cxw_44q27cikb6EyGtcGg1BQGwQwLHIb4Y1Z-pZDtTezTJsuX_hu-3iODhQt-koRbq5QyaA_39wagvmHj64uu47ijpLTnBh_dFw44A&gsessionid=OhwF31whz1sQyJ6XMHX5CSjo-Vh2QQW1l6TqczoLLlwLpDVykoT70A)  
  <sub>FXStreet, 5 hours ago</sub>  
  Over the past month, the news cycle has been relentless for technology stock holders. Jensen Huang departed Nvidia on 12 November, the board rejected his...
- [Cramer Turns Eyes to Retail Stocks and Highlights His 2 Favorites](https://www.google.com/goto?url=CAESfwHEIkXXL5l_VQwms2KIv0J364WEJVk2dpnSdOWjqi-8sgHZMPo6ZKlRSk19ywo0Q5J2dvNKlEM4UvRioTwBL94pIBOS5DDiwhTmSaXqp6qzysH_jIxeQoWUbnzKvR6Esdva5V4RPf80wER70VTvMLStr-wsJ_AcsTYSO7Vl2x4&gsessionid=OhwF31whz1sQyJ6XMHX5CSjo-Vh2QQW1l6TqczoLLlwLpDVykoT70A)  
  <sub>BeInCrypto, 8 hours ago</sub>  
  Jim Cramer sorts six retail stocks after Tuesday earnings and praises 2 as the sector outpaces tech this quarter.
- [Dell Reports Today. Here’s How Much of Your Tech ETF Is Riding on Its AI Server Business](https://www.google.com/goto?url=CAESwwEBxCJF175Bw8Ix9dVB5tDABa-O3DkT1cO9tjDVMpBggd4HOJz3MO-ApR9HnjSdMEnoUA7wNmVmAzzTUa7EnOo39amfWMKvnjUvuNZ_prmnsgwk-NC4QrkhV_XdIBQ-xc9860hjkE1EPoyMMs02DPsuuE8OGw6sqhXZIps7Oc2RhHqCLt8twF0tc9QXaxrjcFTVgCZfbhSw5ezsQ-ILVtBONm8oeAkjGjgxBBOoo3VX_yjdwFkBmi9pthcUEAWdx3LoFmU&gsessionid=OhwF31whz1sQyJ6XMHX5CSjo-Vh2QQW1l6TqczoLLlwLpDVykoT70A)  
  <sub>24/7 Wall St., 21 hours ago</sub>  
  Dell's stock is sliding into tonight's earnings, and tech fund owners are bracing for the fallout. The bigger risk to your retirement account may not be...
- [News by CNBC TV18 on TradingView, 2026-11-25 — cnbctv:0df8688d0094b:0](https://www.google.com/goto?url=CAESdAHEIkXX_wUoqwacQ5HKPTxbQydMBWSLS3ivhZrL5aocVb8pzp4_mqTKC3TZttdAMHn9rLbTf78BAngVHprY_TMgnfLmxPl6NVrsiB-uHDpHIfH8c_mmyTvzJ797T0NXpXZuaTWuPE2VViBtzJDpLmNiCo5r&gsessionid=OhwF31whz1sQyJ6XMHX5CSjo-Vh2QQW1l6TqczoLLlwLpDVykoT70A)  
  <sub>TradingView, 2 hours ago</sub>  
  US stock futures fell sharply on Wednesday, November 25, as the sell-off in artificial intelligence-linked stocks gathered pace again, with investors also...
- [Can Technology Stocks Regain Their Leadership Role?](https://www.google.com/goto?url=CAESmgEBxCJF17ZtxRHryQuN2_woxNTtJD16SM_iVXJ1X5t9DQAyTlj2AVIuXhwbbgQXPExVNIGCiA8gqvNaOq1pNmZPbwK3ux8VcIbSwk4Xxpn1mH-gA-UL6xWdmH8nQCkRhULXIooXOcWwordb2Y0n2r4xocTXr43PzyJ2UspUlnTV6E8Pokot1U3zH9d0pkR8zJO0JnhYSpy_Df8F&gsessionid=OhwF31whz1sQyJ6XMHX5CSjo-Vh2QQW1l6TqczoLLlwLpDVykoT70A)  
  <sub>Investing.com Canada, 1 hour ago</sub>  
  Market Analysis by James Picerno covering: SPDR® S&P 500® ETF Trust, NVIDIA Corporation, VanEck Semiconductor ETF, iShares Expanded Tech-Software Sector ETF...
- [Jim Cramer Says Tuesday’s Stock Market Pullback Is Actually Good News](https://www.google.com/goto?url=CAESrAEBxCJF17sbk2NA8hwcUVqrTB8YLMLh0PRDORhtPlahZ8NkwLp4tklfOBqlpHy58O5bW47Om0CldH-tN4teKi9x31zegmhgqVrdIPhaEMp3s4KlS7KfvN4el8HxFQV1SsVYz1UjxrXpsv_ZrfHUuLrJhypIiOFJ6yyDDtkfwhYnLoBPc2HPYzaXc-AE0bt1-Oc8GSpe2OyMzxeGxOsyno1vPIjd-eRcciFM_G4V&gsessionid=OhwF31whz1sQyJ6XMHX5CSjo-Vh2QQW1l6TqczoLLlwLpDVykoT70A)  
  <sub>24/7 Wall St., 2 hours ago</sub>  
  Jim Cramer called NVIDIA's 6% drop after Monday's 32% surge "an encouraging sign" for recovery, even as XLK sank 3% and finished last.
- [Nasdaq plunges 3.8% as AI stocks slide and inflation fuels Fed rate hike bets](https://www.google.com/goto?url=CAEStQEBxCJF1_PLfkKNfKEa8SDiP7pX6rDnjx3SJk6IjwYLgIbruHBq239XB-XXahXZwtc6eSXQfKFlCQlTMNqCWMSfwZU8NW9jG5Dx2BxVKVCqExtpZWGda9m2fWiG9kiiayKLPEegYoEfujHWT_48okg1dU0Gl6EC91GjtxrJ9DUd6MztsogGEd_MRZ142uOLninr_2X5AMAcpMjy1tjmp2h4akcQ6IFM8vaktwqw5KDhBGcriVUE&gsessionid=OhwF31whz1sQyJ6XMHX5CSjo-Vh2QQW1l6TqczoLLlwLpDVykoT70A)  
  <sub>Invezz, 1 minute ago</sub>  
  US stocks tumbled as the Nasdaq fell 3.8%, led by AI stock losses, while elevated October inflation reinforced expectations of a December Fed rate hike.
- [AXT Inc (AXTI) Shares Drop 14% Amid Tech Selloff on November 24, 2026](https://www.google.com/goto?url=CAESpAEBxCJF16LR0hAoFbrpLTYdQLF3EjNWdREKjr_vWIWDpfX-7huspxyQBYq44CaauKvZ9e3ty0SA1VqeI8XxIf0ycRjFvr3Swc-6yQRdWQkwihnYE4nqKnbv3P1uObIv8MB0vpsGtYCmqfoct1sGdq1QtimWsjfe4rg6yGcnj4Rsik6yhbltrjz_8PurCbFeOq9lnBBIv4Aft-wYrI_tT9hcNaSBgw&gsessionid=OhwF31whz1sQyJ6XMHX5CSjo-Vh2QQW1l6TqczoLLlwLpDVykoT70A)  
  <sub>GuruFocus, 22 hours ago</sub>  
  On November 24, 2026, AXT Inc (NASDAQ: AXTI) experienced a sharp decline in its stock price, falling approximately 14% to close at $32.70.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.16% (+0.01 on the week) | 5-year 4.62% (-0.26 on the week) | 10-year 4.83% (-0.24 on the week) | 30-year 5.24% (-0.17 on the week)
Yield curve, 10-year minus 3-month: +0.67 points -- upward sloping (normal)
US dollar index: 103.93 (+0.07 on the week)
Volatility (VIX): 31.72 (+7.2 on the week) -- stressed
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.1% (2026-10-01) | jobless claims 189k (2026-11-21)
Policy and expectations: Fed target 4.00% | market expects 2.1% inflation over 10 years
Rate path: 2-year Treasury 4.63% vs Fed target 3.75-4.00% -- the bond market prices about 3 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score -0.20</summary>

```text
Last close 149.13 (bar of 2026-11-25), from 502 daily bars
Trend: vs 20d SMA 167.55 (-11.0%), 50d 182.75 (-18.4%), 200d 171.51 (-13.0%); 50d above 200d
Momentum: RSI(14) 33.3 | MACD -8.005 vs signal -6.795 (histogram -1.210)
Returns: 1d -5.1% | 5d -9.0% | 1m -21.3% | 3m -20.9%
52-week range: 127.50 - 202.00 (now 29.0% of the way up)
Volatility: ATR(14) 7.07 (4.7% of price) | annualised 20d 62.0%
Volume: 0.16x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score -0.40</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score -0.40</summary>

```text
Fund type: Technology
What it holds: P/E 31.66 | P/B 11.55 | P/S 8.87 | 3y earnings growth n/a
Yield: 0.5%
Three-year record: +21.4% a year | beta to the market 1.56
Cost and size: expense ratio 0.08% | net assets 118.67B
What it is made of: Stocks 100.0%, Cash 0.1%
Largest holdings: Apple Inc 15.3%, NVIDIA Corp 15.1%, Microsoft Corp 11.8%, Broadcom Inc 4.7%, Advanced Micro Devices Inc 4.5%
Sector mix: Technology 100.0%
```

</details>

<details><summary><b>Does this company beat its own forecasts</b> — score -0.40</summary>

_Not available today._

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

<details><summary><b>What analysts and big funds say</b> — score +0.90</summary>

_Not available today._

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score +0.90</summary>

```text
Rolled up from the 5 largest holdings, 51.5% of the fund by weight
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 1.68 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +42.7% above the current prices
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
Share count change: 1 week: +4.9% (5.05B) over 8d | 1 month: +8.3% (8.32B) over 33d
Shares outstanding: 730.94M | fund size: 109.00B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### US everyday goods (XLP) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Neutral overall; no macro surprise, flat fund flows, technicals show no decisive break, analyst view bullish but limited coverage.

**Main reasons it gave:**
- Flat fund flows (share count unchanged over week and month)
- Technicals show price near 52‑week high with no decisive break (MACD below signal, low volume)
- Macro data unchanged: yields stable, VIX up but no policy surprise
- Analyst view bullish (100% buy, +4% price target) but covers only 41.8% of fund

<details><summary><b>News</b> — score +0.00</summary>

- [Should You Invest in the State Street Consumer Staples Select Sector SPDR ETF (XLP)?](https://finance.yahoo.com/markets/stocks/articles/invest-state-street-consumer-staples-102003027.html)  
  <sub>Yahoo Finance, 5 hours ago</sub>  
  The State Street Consumer Staples Select Sector SPDR ETF (XLP) was launched on December 16, 1998, and is a passively managed exchange traded fund designed...
- [RSPS: Consumer Staples ETF Reduces Company Risk](https://seekingalpha.com/article/4966643-rsps-consumer-staples-etf-reduces-company-risk)  
  <sub>Seeking Alpha, 20 hours ago</sub>  
  The Invesco S&P 500 Equal Weight Consumer Staples ETF offers equal-weight exposure to 33 consumer staples stocks, reducing company-specific risk.
- [State Street Technology Select Sector SPDR ETF (XLK) stock price, news, quote and history](https://www.google.com/goto?url=CAESYwHEIkXX4ULR6BbSwdAeOOVijqQoCv9nMsREbX4R-g1xTB7R8roEG4cz6n0gQ6TSPsz_iwQDR6XJoPkYSZgU_k9iVyEocG5CHBEM7FMQoK8FwPmPmLCJm1hiKahN2CfPrJ1K2g&gsessionid=v92vkXA7WIzFoZB0dug9_Ob12lmXvGVIrhsbFY0Wxh4r22sF6T6Eaw)  
  <sub>Yahoo Finance UK, 3 hours ago</sub>  
  Find the latest State Street Technology Select Sector SPDR ETF (XLK) stock quote, history, news and other vital information to help you with your stock...
- [Weekly ETFs: Seven of 11 sectors record outflows; Communication services sector leads inflows](https://www.google.com/goto?url=CAES1wEBxCJF1z55TZV6dRq62ncqBHTL6pRElnrn9zl6zkSXcn5XgspY6BS-tINebTboOR0sFXPNfYLwRPBXVfLfk_2W7V3aHyboL7Ny7CMEKWpGSYESKgkAHCCcirNb_1gREtq6TeoCdiq-6YoYLsL4yZITBbjCNfCI_b-XaS57FOKiq_1f1VnfKz-zFPoEur6ogoAxOAEN7f4TXnbjeqNDed0m17uI2-A_hSWx-poLaXHea9-_B4Vg-lCoTvw0XJ5eoK2edHtgW2Ruufg5S2Mpp_lm0E5QEYL41w&gsessionid=v92vkXA7WIzFoZB0dug9_Ob12lmXvGVIrhsbFY0Wxh4r22sF6T6Eaw)  
  <sub>TradingView, 18 hours ago</sub>  
  The world's largest exchange-traded fund, SPDR S&P 500 ETF Trust AMEX:SPY, saw outflows of $2.50B for the week ended November 20, while its price...
- [Bunker essentials get costlier amid doomsday prepping - report](https://www.google.com/goto?url=CAES2QEBxCJF10SZqe77Cpy1O1R_oexwuUeVkyVY7VauyljxW75_qZzvVMRKbBNfBxAo8FLBCn_pku5xmlhZwf6ykUDy5r_-08OZWSR6IEAFY5AIShXHi4zpnzp9MZtO_Madr4JS6isf2jHoai6OuDGqQfIjOYlR_LmDAf2lFLh-I32Ho6FCa--kVPv4JS5BzPikHkEWMomomj4GpAUZ1AuRIGP615mHqApfPwooBnY2xGViXpSPV-5-apt_TNTrnKwEjIHrEiWBBQRa0gIHwel1AWPAHwqYl3-4YEYI&gsessionid=v92vkXA7WIzFoZB0dug9_Ob12lmXvGVIrhsbFY0Wxh4r22sF6T6Eaw)  
  <sub>Seeking Alpha, 4 hours ago</sub>  
  Nov 25, 2026, 5:26 AM ET State Street Consumer Staples Sel Sect SPDR ETF (XLP), XLY, VDC, VCR, FDIS, IYKWMT, COSTBy: Jessica Kuruthukulangara,...
- [Palm.Sq.EO CLO Sen.Dt Idx ETF R (PCLD.DE) stock price, news, quote and history](https://www.google.com/goto?url=CAESZwHEIkXXiRANZav4gdDLbl1-dOofp_YYzHko4Q8sWkwFIahBVuqTirM-1VhmXPKAXkghTINHIhaX42T_NNjPTKw0jRK4jsO5EXuwWpdXM8RQkG0tgz7g5PXD7FQJvpH-0EZAxuHdzIs&gsessionid=v92vkXA7WIzFoZB0dug9_Ob12lmXvGVIrhsbFY0Wxh4r22sF6T6Eaw)  
  <sub>Yahoo Finance UK, 10 hours ago</sub>  
  Find the latest Palm.Sq.EO CLO Sen.Dt Idx ETF R (PCLD.DE) stock quote, history, news and other vital information to help you with your stock trading and...
- [Anthropic Drops Below IPO Prices, Nvidia Sinks 7% After Record Rally: Stock Market Today](https://www.google.com/goto?url=CAESzQEBxCJF12H_AJgdiaulrq_dcL6HRskSAfLiiiQknWxxxLzFAj1GT_6Uo5KJFzlpJtg5OWVIG6LRxLD92JuRNuxCyOFkdfxse_wqX_OtSo6tFu8oaAvGMjxmVbPVrVpRRw9vo-3Z05Z1OsOBcJoGnCLLKbhTe73ndErbyyzjhgYojSRM7kxuRAwKlotYSkxnvOpyu29UnCdB7fmQ8jdVZ8oPss-h0BumONwtMtA750E7i8Cyc-Gu6dxPQ1aMhytfbyuOzZPVB8A4Ml491vo-&gsessionid=v92vkXA7WIzFoZB0dug9_Ob12lmXvGVIrhsbFY0Wxh4r22sF6T6Eaw)  
  <sub>TradingView, 21 hours ago</sub>  
  The artificial-intelligence trade cracked on two fronts Tuesday. Anthropic PBC NASDAQ:ANT slipped below its $83 IPO price less than a week after its record...
- [Looking for safe havens in a volatile tech environment (XLP:NYSEARCA)](https://www.google.com/goto?url=CAESmAEBxCJF12VfgoEX2LssNZwH1i57worP8SkhfWGUKWKxM4xifRqPy7A4z55oiOCODyBYxgYpRbvP4vhHpjTdkyDTDETutxbFUVVZo7gDhbf9De4dGRgHWAxFK01PDVN7nzAW6FtyMxmYgvTcos0ft9iZOSaVxuQiO7ZySm8GWpOH4WpVCGgO4m8-PQI2r8dmqiUCaOFMvu9oLQ&gsessionid=v92vkXA7WIzFoZB0dug9_Ob12lmXvGVIrhsbFY0Wxh4r22sF6T6Eaw)  
  <sub>Seeking Alpha, 20 hours ago</sub>  
  Analysts see utilities and consumer staples as defensive after they fell less than tech in the latest selloff, though elevated valuations may limit appeal.
- [UBS Core BBG EUR Gov 1-10 UCITS (CHSFD.XC) company profile and facts](https://www.google.com/goto?url=CAEScAHEIkXXD4sZk-BG0jBpKGlZ0ZuEp1uR_zI-V81sefMvKu-SS3buZKVzKDFCDlgJCT630shffgV08Dhh26UXS5cN14px96AMDIkVHK0WpmLlwQ8O3aunFF6R5vQnOtNfwuioRwhq2leJpVZZc-SsN10&gsessionid=v92vkXA7WIzFoZB0dug9_Ob12lmXvGVIrhsbFY0Wxh4r22sF6T6Eaw)  
  <sub>Yahoo Finance UK, 21 hours ago</sub>  
  See the company profile for UBS Core BBG EUR Gov 1-10 UCITS (CHSFD.XC), including business summary, industry/sector information, number of employees,...
- [Deutsche Invest I - Deutsche Invest I Top Dividend (HVJH.MU) Seasonal returns chart](https://www.google.com/goto?url=CAEScwHEIkXXnBTa_rze8gRzos-W2dMQ-h7eeflq5VfRcU_0js0YHRRrC7UkpQTXwW83fidGXbzQ6OulQYtDlj1EObc-v8EG4Z9iuNmFgFnpfkD-TJTvnQxG_nzpIcKzh5HeIICiJSaAXu-PvAudiS3o-yRYs2g&gsessionid=v92vkXA7WIzFoZB0dug9_Ob12lmXvGVIrhsbFY0Wxh4r22sF6T6Eaw)  
  <sub>Yahoo Finance UK, 21 hours ago</sub>  
  Deutsche Invest I - Deutsche Invest I Top Dividend (HVJH.MU) seasonal returns chart provides the mean and median returns by month to inform your investment...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.16% (+0.01 on the week) | 5-year 4.62% (-0.26 on the week) | 10-year 4.83% (-0.24 on the week) | 30-year 5.24% (-0.17 on the week)
Yield curve, 10-year minus 3-month: +0.67 points -- upward sloping (normal)
US dollar index: 103.93 (+0.07 on the week)
Volatility (VIX): 31.72 (+7.2 on the week) -- stressed
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.1% (2026-10-01) | jobless claims 189k (2026-11-21)
Policy and expectations: Fed target 4.00% | market expects 2.1% inflation over 10 years
Rate path: 2-year Treasury 4.63% vs Fed target 3.75-4.00% -- the bond market prices about 3 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 92.00 (bar of 2026-11-25), from 502 daily bars
Trend: vs 20d SMA 90.86 (+1.3%), 50d 86.85 (+5.9%), 200d 85.08 (+8.1%); 50d above 200d
Momentum: RSI(14) 60.3 | MACD 1.156 vs signal 1.350 (histogram -0.194)
Returns: 1d +0.1% | 5d +0.9% | 1m +5.6% | 3m +8.1%
52-week range: 76.62 - 92.60 (now 96.2% of the way up)
Volatility: ATR(14) 1.47 (1.6% of price) | annualised 20d 21.0%
Volume: 0.24x the 20-day average
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
Three-year record: +11.8% a year | beta to the market 0.39
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
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 1.81 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +4.0% above the current prices
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
Shares outstanding: 210.17M | fund size: 19.34B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### US electricity and water (XLU) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Neutral overall; no macro surprise, flat fund flows, technicals lack decisive break, analyst view bullish but limited coverage, fundamentals stable.

**Main reasons it gave:**
- Flat fund flows (0% change in share count over 1 week and 1 month)
- Technicals: price below 200‑day SMA, MACD below signal, low volume (0.09× 20‑day avg)
- Macro: no policy surprise; yields modestly changed, VIX up but no shock
- Analyst view: 80% buy rating, price target +13.3% above current, coverage 39.4% of fund
- Fund basics stable: P/E 17.87, yield 2.8%, beta 0.34

<details><summary><b>News</b> — score +0.00</summary>

- [UTES ETF: Tilt To Nuclear-Powered Utility Sector (NYSEARCA:UTES)](https://seekingalpha.com/article/4971604-utes-etf-tilt-to-nuclear-powered-utility-sector)  
  <sub>Seeking Alpha, 16 hours ago</sub>  
  The Virtus Reaves Utilities ETF is a broad utilities investment vehicle with a strong tilt toward nuclear power operators.
- [State Street Industrial Select Sector SPDR ETF (XLI) Stock Price, News, Quote & History](https://ca.finance.yahoo.com/quote/XLI/)  
  <sub>Yahoo! Finance Canada, 6 hours ago</sub>  
  Find the latest State Street Industrial Select Sector SPDR ETF (XLI) stock quote, history, news and other vital information to help you with your stock...
- [Weekly ETFs: Seven of 11 sectors record outflows; Communication services sector leads inflows](https://www.google.com/goto?url=CAES1gEBxCJF193gBa3lXRTno6MX2XIX3ITYqJ0xQ1-a_r-omrIBl2P__JBZl3cXES-ineRWl1jUr-_JFKQaKJuNmChV3P0mRoo7FatBIxOi2usnA4c8XwUew9fUQ3QalpHCGoM33fbuLXFnNGG930J_d4lpu6zXzFsmQepbTuD4GJJRsrO8ZX3pDEjTVdY0J1hOLYbrx5IbSEl7mAtMp0vUDcdTxBZ3BT-QPydunXpdkAJiQyU-deQzBLyIor9CeIqiX3XSWqzZAx-X4oBMerGS1Qqf-iwLpXWu&gsessionid=yJjgWvDTnkRUmuL5q0PzkFo3DKRzTftRGaU_A47HgamGvcTGLJN2vA)  
  <sub>TradingView, 18 hours ago</sub>  
  The world's largest exchange-traded fund, SPDR S&P 500 ETF Trust AMEX:SPY, saw outflows of $2.50B for the week ended November 20, while its price...
- [State Street Materials Select Sector SPDR ETF (XLB) Stock Price, News, Quote & History](https://www.google.com/goto?url=CAESYgHEIkXX6yIzIPATj3t9ug9cSrWjOV_dBTAqNAvd6183WD3sGwOG0CX4klv8s9l5wI-iVV8i3thpX7_2x7--c-QOuYL4MzdKu7ZBBTZHyfnK1HiT3ioJpIT1c9DPXSpIng1r&gsessionid=yJjgWvDTnkRUmuL5q0PzkFo3DKRzTftRGaU_A47HgamGvcTGLJN2vA)  
  <sub>Yahoo! Finance Canada, 20 hours ago</sub>  
  Find the latest State Street Materials Select Sector SPDR ETF (XLB) stock quote, history, news and other vital information to help you with your stock...
- [Looking for safe havens in a volatile tech environment (XLP:NYSEARCA)](https://www.google.com/goto?url=CAESlwEBxCJF17SndaKSy976x95MRR1DQ7Gho2KCsDRtYgIMluWN2KjwMuKssJML1HH89w8CKESFUgliTdslhQj8TLho4wG6YDX4UmY8PrteGZtzdu3hiMTBy2fM1-zBZqj1GsUlR-TAo_w2mHY6vRIE6mWyLDS-CcCDFuPKiO4GXOGah6nH6ZRM6TWkY4mF5InMRijWEBuUvCT3&gsessionid=yJjgWvDTnkRUmuL5q0PzkFo3DKRzTftRGaU_A47HgamGvcTGLJN2vA)  
  <sub>Seeking Alpha, 20 hours ago</sub>  
  Analysts see utilities and consumer staples as defensive after they fell less than tech in the latest selloff, though elevated valuations may limit appeal.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.16% (+0.01 on the week) | 5-year 4.62% (-0.26 on the week) | 10-year 4.83% (-0.24 on the week) | 30-year 5.24% (-0.17 on the week)
Yield curve, 10-year minus 3-month: +0.67 points -- upward sloping (normal)
US dollar index: 103.93 (+0.07 on the week)
Volatility (VIX): 31.72 (+7.2 on the week) -- stressed
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.1% (2026-10-01) | jobless claims 189k (2026-11-21)
Policy and expectations: Fed target 4.00% | market expects 2.1% inflation over 10 years
Rate path: 2-year Treasury 4.63% vs Fed target 3.75-4.00% -- the bond market prices about 3 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 43.42 (bar of 2026-11-25), from 502 daily bars
Trend: vs 20d SMA 43.49 (-0.2%), 50d 42.05 (+3.2%), 200d 44.33 (-2.1%); 50d below 200d
Momentum: RSI(14) 54.4 | MACD 0.259 vs signal 0.372 (histogram -0.114)
Returns: 1d +0.0% | 5d -0.3% | 1m +1.3% | 3m +0.5%
52-week range: 39.25 - 47.73 (now 49.1% of the way up)
Volatility: ATR(14) 0.60 (1.4% of price) | annualised 20d 13.5%
Volume: 0.09x the 20-day average
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
Three-year record: +14.8% a year | beta to the market 0.34
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
Share count change: 1 week: +0.0% (0.00) over 7d | 1 month: +0.0% (0.00) over 32d
Shares outstanding: 163.27M | fund size: 7.09B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### US health care (XLV) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> No macro surprise, no decisive technical break on heavy volume, and while analyst coverage, fund flows and fundamentals are positive, they do not constitute a material catalyst to tilt the overall view.

**Main reasons it gave:**
- Fund flows: +12.9% share count increase over past month
- Analyst view: 100% buy rating on top holdings, weighted price target +10.6% above current
- Technicals: price below 20‑day SMA, MACD below signal, volume 0.14× 20‑day average
- Macro: yields stable, VIX up to 31.7, no surprise data releases
- Fundamentals: P/E 30.14, low beta 0.41, 3‑yr annualized return 13.1%

<details><summary><b>News</b> — score +0.00</summary>

- [Palm.Sq.EO CLO Sen.Dt Idx ETF R (PCLD.DE) stock price, news, quote and history](https://uk.finance.yahoo.com/quote/PCLD.DE/)  
  <sub>Yahoo Finance UK, 10 hours ago</sub>  
  Find the latest Palm.Sq.EO CLO Sen.Dt Idx ETF R (PCLD.DE) stock quote, history, news and other vital information to help you with your stock trading and...
- [UBS ETF (CH)-UBS Palladium ETFN (UFU2.HA) interactive stock chart](https://uk.finance.yahoo.com/quote/UFU2.HA/chart/)  
  <sub>Yahoo Finance UK, 13 hours ago</sub>  
  Interactive chart for UBS ETF (CH)-UBS Palladium ETFN (UFU2.HA) – analyse all of the data with a huge range of indicators.
- [AXA World Funds - Global Inflation Bonds (XRUG.MU) stock price, news, quote and history](https://www.google.com/goto?url=CAESZgHEIkXX3MClpT13D3FvFfTq0fy5-0vrPtr5ALbZ0BerpVTN4Ixcc7dkM841yxcQb00oNyG6C56UHgaSG_HOB6eiPBYugCO6570QVlLwNVdbPMnhtWLgOhLhld9FrCEhtSbKG1ezHA&gsessionid=sDhJzmHbrcW5clEOC5XKZfH9YgU-RQ9kOxvfnttSBBxxagzQMpZFNQ)  
  <sub>Yahoo Finance Australia, 15 hours ago</sub>  
  Find the latest AXA World Funds - Global Inflation Bonds (XRUG.MU) stock quote, history, news and other vital information to help you with your stock...
- [UBSLFS-UBS CoreBBG US Tr.10+UEN (CHSS.HA) latest stock news and headlines](https://www.google.com/goto?url=CAESawHEIkXX0qljWlvpBGh250S2N3XW_fjrIfv6PDUaRC0DWJd8Pni_fRD_y5PKJAT9u-JRsOB2N3e5oEbuUDJJ6sM4v5yjx--Sin4Y4P7FGqBV63aJKgP9bdk6prXTrdyptG0b2Xv8dOT9Eq2u&gsessionid=sDhJzmHbrcW5clEOC5XKZfH9YgU-RQ9kOxvfnttSBBxxagzQMpZFNQ)  
  <sub>Yahoo Finance UK, 13 hours ago</sub>  
  UBSLFS-UBS CoreBBG US Tr.10+UEN (CHSS.HA). 8.44 +0.10 (+1.15%). At close: 24 November at 8:21:30 CET. Related ETF news. Consumer Staples ETFs Back in Favor...
- [BNP P.Easy-Energy&Met.Enh.RollN (GSDE.HA) stock price, news, quote and history](https://www.google.com/goto?url=CAESZgHEIkXXCc3Q_wQ7BHPBmKofQT9bJVGBzIRlvt73XEZViQSBKm3UPKUGIzNUc6Vls7VDCxn657YjOHFh4zXwOm7MgXMnqFgKkSKxnL_kRvSMYJgDVj2A07TLhORrDYLF0LKyAfYzPg&gsessionid=sDhJzmHbrcW5clEOC5XKZfH9YgU-RQ9kOxvfnttSBBxxagzQMpZFNQ)  
  <sub>Yahoo Finance UK, 16 hours ago</sub>  
  Find the latest BNP P.Easy-Energy&Met.Enh.RollN (GSDE.HA) stock quote, history, news and other vital information to help you with your stock trading and...
- [HAMILTON CANADIAN FINANCIALS YI (HMAX.NE) stock price, news, quote and history](https://www.google.com/goto?url=CAESZgHEIkXX6iq1k8JAZOiNgFlT3lLCMMdLOCeV7Rgybr41p3XIgqdtjdGhi-tUrvn-L3boaC6xmuUUPZ5gKoFAVESbsyz14JNEcAXH6Deowi_pFYd4YrE8svDDWKoz-5NG3vyGQf23jg&gsessionid=sDhJzmHbrcW5clEOC5XKZfH9YgU-RQ9kOxvfnttSBBxxagzQMpZFNQ)  
  <sub>Yahoo Finance Australia, 14 hours ago</sub>  
  Find the latest HAMILTON CANADIAN FINANCIALS YI (HMAX.NE) stock quote, history, news and other vital information to help you with your stock trading and...
- [Schroder ISF Europ.Special Si.N (XR5D.DU) latest stock news and headlines](https://www.google.com/goto?url=CAESawHEIkXXyXLRwY64IyDlv8YOldb5CaR8PhT3mtJGMj-ziUCvnVrQpQdeSdoqfgQUAVnWMZHISQ954ZjtWCwJROl8u3FZKSkPwusaLe1Sd6FjNwGftcCj7xhtXhdzva-zRt8ZAloH22dbBc9c&gsessionid=sDhJzmHbrcW5clEOC5XKZfH9YgU-RQ9kOxvfnttSBBxxagzQMpZFNQ)  
  <sub>Yahoo Finance UK, 15 hours ago</sub>  
  Schroder ISF Europ.Special Si.N (XR5D.DU). 273.93 -0.68 (-0.25%). At close: 21:45:02 CET. Related ETF news. Consumer Staples ETFs Back in Favor Amid Growing...
- [VANECK ETF TR (^DAPP) Seasonal returns chart](https://www.google.com/goto?url=CAEScgHEIkXX--6HWecSrFSE5BzNgky4AHHw5o-qpIdTyF9seY5YcXIm8ze8HLGSeesY8PVCDPvTz9TdYiLAqQeY_VKA8Ex7PDOcX4FTda_1ny1H-MmPxxp33RIBNHt7XMSZw3zUK284h4VVql9XO5rwV6-KHw&gsessionid=sDhJzmHbrcW5clEOC5XKZfH9YgU-RQ9kOxvfnttSBBxxagzQMpZFNQ)  
  <sub>Yahoo Finance UK, 10 hours ago</sub>  
  VANECK ETF TR (^DAPP) seasonal returns chart provides the mean and median returns by month to inform your investment strategy.
- [Scotia All-Equity ETF (SBEQ.NE)](https://www.google.com/goto?url=CAESawHEIkXXXJ5VrRyGyl9zl7JYAbcCa87gdJU_yDwUEimF2ASctor8fe5JhG6An4tOc5ksN4tmeP_SvxUq_XG20jdotmgwpo3MxtyuMrIR8wBmg5stZp1P2JoDCwi6Kq5_Yf3c_WBm9ps4zinR&gsessionid=sDhJzmHbrcW5clEOC5XKZfH9YgU-RQ9kOxvfnttSBBxxagzQMpZFNQ)  
  <sub>Yahoo! Finance Canada, 15 hours ago</sub>  
  View Historical Risk Statistics for Scotia All-Equity ETF (SBEQ.NE).
- [THOR Equal Weight Low Volatility ETF (THLV) Seasonal returns chart](https://www.google.com/goto?url=CAESbwHEIkXXQ5ba8NE1KrZCTgNKuRU3X8oW0KTfSlI0WSutG4XnwAruJAbgLyxVTs1R8lq2F5VRuipjScHdyHB4Z6i-lUlxN9vpQ6KPdPiwvPu4QK6cawvNTV20SgRrq-AlNXbXq3Nar0gFBU17oMMkow&gsessionid=sDhJzmHbrcW5clEOC5XKZfH9YgU-RQ9kOxvfnttSBBxxagzQMpZFNQ)  
  <sub>Yahoo Finance UK, 16 hours ago</sub>  
  THOR Equal Weight Low Volatility ETF (THLV) seasonal returns chart provides the mean and median returns by month to inform your investment strategy.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.16% (+0.01 on the week) | 5-year 4.62% (-0.26 on the week) | 10-year 4.83% (-0.24 on the week) | 30-year 5.24% (-0.17 on the week)
Yield curve, 10-year minus 3-month: +0.67 points -- upward sloping (normal)
US dollar index: 103.93 (+0.07 on the week)
Volatility (VIX): 31.72 (+7.2 on the week) -- stressed
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.1% (2026-10-01) | jobless claims 189k (2026-11-21)
Policy and expectations: Fed target 4.00% | market expects 2.1% inflation over 10 years
Rate path: 2-year Treasury 4.63% vs Fed target 3.75-4.00% -- the bond market prices about 3 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 182.20 (bar of 2026-11-25), from 502 daily bars
Trend: vs 20d SMA 184.75 (-1.4%), 50d 177.36 (+2.7%), 200d 161.26 (+13.0%); 50d above 200d
Momentum: RSI(14) 50.8 | MACD 0.883 vs signal 1.946 (histogram -1.064)
Returns: 1d -1.4% | 5d +0.6% | 1m +1.7% | 3m +6.2%
52-week range: 142.84 - 189.66 (now 84.1% of the way up)
Volatility: ATR(14) 3.60 (2.0% of price) | annualised 20d 25.6%
Volume: 0.14x the 20-day average
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
Three-year record: +13.1% a year | beta to the market 0.41
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

<details><summary><b>What analysts and big funds say</b> — score +0.50</summary>

_Not available today._

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score +0.50</summary>

```text
Rolled up from the 5 largest holdings, 45.4% of the fund by weight
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 1.73 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +10.6% above the current prices
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
Share count change: 1 week: +5.3% (2.49B) over 8d | 1 month: +12.9% (5.68B) over 33d
Shares outstanding: 273.74M | fund size: 49.87B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### US shopping and leisure (XLY) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Mixed signals: strong analyst consensus and inflows are bullish, but technicals, high valuations, and macro headwinds are bearish, leading to a neutral overall view.

**Main reasons it gave:**
- Analyst consensus 100% buy with +22.7% price target (covers 54.1% of fund weight)
- Fund inflows: share count up 2.6% week‑over‑week and 4.0% month‑over‑month
- Technical indicators: price below 20‑, 50‑ and 200‑day SMAs, negative MACD, low volume
- Macro environment: high yields (10‑yr 4.83%) and elevated VIX (31.7) pressure consumer discretionary
- Fundamentals: high valuation (P/E 24.15, P/B 5.62) with modest growth

<details><summary><b>News</b> — score +0.00</summary>

- [Undervalued consumer discretionary stocks ahead of holiday season (XLY:NYSEARCA)](https://seekingalpha.com/news/4676577-undervalued-consumer-discretionary-stocks-ahead-of-holiday-season?source=generic_rss)  
  <sub>Seeking Alpha, 29 minutes ago</sub>  
  As the third-quarter earnings season draws to a close, investors are turning their attention to the upcoming holiday shopping period for clues about the...
- [Two Measures of Consumer Attitudes: November 2026](https://www.advisorperspectives.com/dshort/updates/2026/11/24/two-measures-of-consumer-attitudes-november-2026?topic=etf)  
  <sub>Advisor Perspectives, 20 hours ago</sub>  
  What are consumers thinking about the economy? Their collective mood offers crucial clues for businesses, investors, and policymakers alike.
- [State Street Materials Select Sector SPDR ETF (XLB) Stock Price, News, Quote & History](https://www.google.com/goto?url=CAESYwHEIkXXUqzamZ-_MhEK671lKFGo4W1QxSXJLX5gbuurJgTufqt4vh7gYE7JlmRaBjVcSgG9RdQLluGC_0Y_LhXKrVljCVeILomsFRuNViSnJLfLXmMTNjPmZqX6ok7-WiGCwg&gsessionid=AJj5ajcc4scAy3emq21HbFVUYK_BzSEiSgPus2HEz6EC7KCSc1JtSg)  
  <sub>Yahoo! Finance Canada, 20 hours ago</sub>  
  Find the latest State Street Materials Select Sector SPDR ETF (XLB) stock quote, history, news and other vital information to help you with your stock...
- [Bunker essentials get costlier amid doomsday prepping - report](https://www.google.com/goto?url=CAESqgEBxCJF11TtYWELSXgRka9d3UC0JqchRSFByPE8EengTaQyNQZ3NrroYU_fULj1TBmz6X7dUPKWVNJ0ugc0J9PnXRISROq8YME6SzKwGh1yb6XZprTSyHJatn7TfQfa3zl1s7bwKwywC0tQPONfxcAw3SFfQEwqq53cSOL5nzD7GfxmdJW99IfhFCUXYnnh5EeZ9TEQDJ8c1obrrNPBr41ElTuBe7mZiBfINg&gsessionid=AJj5ajcc4scAy3emq21HbFVUYK_BzSEiSgPus2HEz6EC7KCSc1JtSg)  
  <sub>Seeking Alpha, 4 hours ago</sub>  
  Emergency-supply buying lifts freeze-dried food prices 12% since September after tech outages, with more than a third of tracked listings sold out.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.16% (+0.01 on the week) | 5-year 4.62% (-0.26 on the week) | 10-year 4.83% (-0.24 on the week) | 30-year 5.24% (-0.17 on the week)
Yield curve, 10-year minus 3-month: +0.67 points -- upward sloping (normal)
US dollar index: 103.93 (+0.07 on the week)
Volatility (VIX): 31.72 (+7.2 on the week) -- stressed
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.1% (2026-10-01) | jobless claims 189k (2026-11-21)
Policy and expectations: Fed target 4.00% | market expects 2.1% inflation over 10 years
Rate path: 2-year Treasury 4.63% vs Fed target 3.75-4.00% -- the bond market prices about 3 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score -0.40</summary>

```text
Last close 113.95 (bar of 2026-11-25), from 502 daily bars
Trend: vs 20d SMA 117.97 (-3.4%), 50d 114.45 (-0.4%), 200d 115.32 (-1.2%); 50d below 200d
Momentum: RSI(14) 44.6 | MACD 0.188 vs signal 0.870 (histogram -0.681)
Returns: 1d -3.2% | 5d -4.4% | 1m -1.3% | 3m -1.7%
52-week range: 105.66 - 124.52 (now 44.0% of the way up)
Volatility: ATR(14) 2.80 (2.5% of price) | annualised 20d 36.1%
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
Three-year record: +12.6% a year | beta to the market 1.10
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

<details><summary><b>What analysts and big funds say</b> — score +0.45</summary>

_Not available today._

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score +0.45</summary>

```text
Rolled up from the 5 largest holdings, 54.1% of the fund by weight
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 1.80 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +22.7% above the current prices
Holdings read: AMZN, TSLA, HD, MCD, TJX
Recent rating changes among them:
  - AMZN: 2026-11-03 Freedom Broker: main, Buy -> Buy
  - TSLA: 2026-11-05 GLJ Research: reit, Sell -> Sell
  - HD: 2026-11-10 Bernstein: main, Market Perform -> Market Perform
  - MCD: 2026-11-06 Argus Research: main, Buy -> Buy
  - TJX: 2026-11-10 UBS: main, Buy -> Buy
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
Share count change: 1 week: +2.6% (552.03M) over 8d | 1 month: +4.0% (847.86M) over 33d
Shares outstanding: 191.54M | fund size: 21.83B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### South Korea (EWY) · Sector or country — no answer, no confidence given

<details><summary><b>News</b> — score n/a</summary>

- [Top Tokenized ETFs by Market Cap](https://www.coingecko.com/en/etfs)  
  <sub>Coingecko, 14 hours ago</sub>  
  Discover the top ETFs (exchange-traded funds) by tokenized market cap. Track ETF prices alongside their tokenized prices, market cap, and volume on...
- [iShares MSCI South Korea ETF (EWY) Price Prediction: South Korea ETF breaks lower as momentum turns fragile](https://blockchain.news/news/20261125-price-prediction-ewy-south-korea-etf-breaks-lower-as)  
  <sub>Blockchain News, 7 hours ago</sub>  
  iShares MSCI South Korea ETF (EWY) fell 6.02% to $127.73, pushing back below its short-term averages and closer to lower Bollinger Band support. The move...
- [Direxion South Korea Bull 3X ETF (KORU) Price Prediction: Bears still have the trend, but buyers are trying to defend the lower band](https://www.google.com/goto?url=CAESlQEBxCJF19KJtMJU5ZxG1MQBjtE_it70Q-SnDlp1T9GEqWrhxwKjxNMcL-fnSgzmpZ_j-tXep7bie9eIOMmU5sKeiMgMq_bi-KZihcYgIdho5QBaOf6SAZ2xiN_zp2r57KJAQ9OKwL3q0t3-SvKIXFojShwu6LsCWIKTsHXwdUwjpgaoNQcXWFYY7p_CpwEAhvtgDNFb6w&gsessionid=3redyA5SmhW-EGT4lDtN4OKYYP6jSNaBOuhQh8Ay3s5XBZ29p2lzkA)  
  <sub>Blockchain News, 7 hours ago</sub>  
  Direxion South Korea Bull 3X ETF (KORU) is trading at $5.08 after a 17.49% drop over 24 hours, leaving it below its short-, medium- and long-term moving...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score n/a</summary>

```text
US Treasury yields: 3-month 4.16% (+0.01 on the week) | 5-year 4.62% (-0.26 on the week) | 10-year 4.83% (-0.24 on the week) | 30-year 5.24% (-0.17 on the week)
Yield curve, 10-year minus 3-month: +0.67 points -- upward sloping (normal)
US dollar index: 103.93 (+0.07 on the week)
Volatility (VIX): 31.72 (+7.2 on the week) -- stressed
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.1% (2026-10-01) | jobless claims 189k (2026-11-21)
Policy and expectations: Fed target 4.00% | market expects 2.1% inflation over 10 years
Rate path: 2-year Treasury 4.63% vs Fed target 3.75-4.00% -- the bond market prices about 3 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score n/a</summary>

```text
Last close 123.93 (bar of 2026-11-25), from 502 daily bars
Trend: vs 20d SMA 140.81 (-12.0%), 50d 160.21 (-22.6%), 200d 164.39 (-24.6%); 50d below 200d
Momentum: RSI(14) 36.1 | MACD -8.627 vs signal -8.088 (histogram -0.539)
Returns: 1d -5.2% | 5d -9.4% | 1m -21.3% | 3m -32.0%
52-week range: 88.58 - 219.20 (now 27.1% of the way up)
Volatility: ATR(14) 7.86 (6.3% of price) | annualised 20d 82.1%
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
Three-year record: +32.4% a year | beta to the market 2.62
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
Share count change: 1 week: +5.9% (1.14B) over 8d | 1 month: +0.1% (14.48M) over 33d
Shares outstanding: 165.74M | fund size: 20.54B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Brazil (EWZ) · Sector or country — no answer, no confidence given

<details><summary><b>News</b> — score n/a</summary>

- [Top Tokenized ETFs by Market Cap](https://www.coingecko.com/en/etfs)  
  <sub>Coingecko, 13 hours ago</sub>  
  Discover the top ETFs (exchange-traded funds) by tokenized market cap. Track ETF prices alongside their tokenized prices, market cap,...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score n/a</summary>

```text
US Treasury yields: 3-month 4.16% (+0.01 on the week) | 5-year 4.62% (-0.26 on the week) | 10-year 4.83% (-0.24 on the week) | 30-year 5.24% (-0.17 on the week)
Yield curve, 10-year minus 3-month: +0.67 points -- upward sloping (normal)
US dollar index: 103.93 (+0.07 on the week)
Volatility (VIX): 31.72 (+7.2 on the week) -- stressed
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.1% (2026-10-01) | jobless claims 189k (2026-11-21)
Policy and expectations: Fed target 4.00% | market expects 2.1% inflation over 10 years
Rate path: 2-year Treasury 4.63% vs Fed target 3.75-4.00% -- the bond market prices about 3 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score n/a</summary>

```text
Last close 29.35 (bar of 2026-11-25), from 502 daily bars
Trend: vs 20d SMA 31.23 (-6.0%), 50d 36.27 (-19.1%), 200d 36.70 (-20.0%); 50d below 200d
Momentum: RSI(14) 29.9 | MACD -2.099 vs signal -2.070 (histogram -0.029)
Returns: 1d +0.2% | 5d -2.4% | 1m -14.4% | 3m -17.9%
52-week range: 28.54 - 43.54 (now 5.4% of the way up)
Volatility: ATR(14) 0.98 (3.3% of price) | annualised 20d 29.3%
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
Three-year record: +1.1% a year | beta to the market 0.92
Cost and size: expense ratio 0.59% | net assets 9.62B
What it is made of: Stocks 98.0%, Cash 1.6%, Preferred 0.4%
Largest holdings: Vale SA 8.7%, Petroleo Brasileiro SA Petrobras 8.5%, Nu Holdings Ltd Ordinary Shares Class A 8.5%, Itau Unibanco Holding SA 8.0%, Weg SA 3.4%
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
Rolled up from the 5 largest holdings, 37.1% of the fund by weight
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 1.75 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +45.5% above the current prices
Holdings read: VALE3.SA, PETR3.SA, NU, ITUB4, WEGE3.SA
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
Shares outstanding: 200.55M | fund size: 5.89B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### US media and communication (XLC) · Sector or country — no answer, no confidence given

<details><summary><b>News</b> — score n/a</summary>

- [Your $300,000 in XLC Holds $130,206 in Just Meta and Alphabet](https://247wallst.com/investing/etf/2026/11/24/your-300000-in-xlc-holds-130206-in-just-meta-and-alphabet/)  
  <sub>24/7 Wall St., 14 hours ago</sub>  
  A fund labeled communication services sounds like a broad bet on telecom, media, and entertainment. The latest SEC filing shows something far narrower,...
- [Weekly ETFs: Seven of 11 sectors record outflows; Communication services sector leads inflows](https://www.tradingview.com/news/seekingalpha:103a2d5ed094b:0-weekly-etfs-seven-of-11-sectors-record-outflows-communication-services-sector-leads-inflows/)  
  <sub>TradingView, 18 hours ago</sub>  
  The world's largest exchange-traded fund, SPDR S&P 500 ETF Trust AMEX:SPY, saw outflows of $2.50B for the week ended November 20, while its price...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score n/a</summary>

```text
US Treasury yields: 3-month 4.16% (+0.01 on the week) | 5-year 4.62% (-0.26 on the week) | 10-year 4.83% (-0.24 on the week) | 30-year 5.24% (-0.17 on the week)
Yield curve, 10-year minus 3-month: +0.67 points -- upward sloping (normal)
US dollar index: 103.93 (+0.07 on the week)
Volatility (VIX): 31.72 (+7.2 on the week) -- stressed
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.1% (2026-10-01) | jobless claims 189k (2026-11-21)
Policy and expectations: Fed target 4.00% | market expects 2.1% inflation over 10 years
Rate path: 2-year Treasury 4.63% vs Fed target 3.75-4.00% -- the bond market prices about 3 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score n/a</summary>

```text
Last close 101.75 (bar of 2026-11-25), from 502 daily bars
Trend: vs 20d SMA 104.36 (-2.5%), 50d 107.98 (-5.8%), 200d 111.81 (-9.0%); 50d below 200d
Momentum: RSI(14) 41.0 | MACD -1.238 vs signal -1.061 (histogram -0.177)
Returns: 1d -2.6% | 5d -3.6% | 1m -1.8% | 3m -8.7%
52-week range: 99.90 - 120.08 (now 9.1% of the way up)
Volatility: ATR(14) 2.46 (2.4% of price) | annualised 20d 29.9%
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
Three-year record: +14.6% a year | beta to the market 0.93
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
Weighted price target: +40.4% above the current prices
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
Share count change: 1 week: +3.1% (636.46M) over 7d | 1 month: -1.3% (-269.40M) over 32d
Shares outstanding: 207.08M | fund size: 21.07B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

## Commodities

### Oil (USO) · Commodity — BEARISH, confidence 0.35

**Result:** ACCEPTED · 28 shares · submitted sell 28 USO @ ~138.66, stop 148.83

**In the model's own words:**

> The macro backdrop shows no new policy surprise and yields are stable, but the VIX is elevated, indicating a risk‑off tone. Fundamental data— a modest weekly crude build and the EIA’s forecast of WTI prices falling to $84 in six months—both point to weaker oil demand, and CFTC speculators have slightly reduced their net‑long position, adding a bearish tilt. Technicals show USO trading below its 20‑day and 50‑day SMAs with a negative MACD, reinforcing a short‑term bearish bias. These factors together outweigh a neutral news flow, leading to a bearish bias with low conviction.

**Main reasons it gave:**
- Weekly U.S. crude inventories build +3.4 mbbl (bearish)
- EIA forecast shows WTI price falling to $84 in six months (bearish)
- CFTC positioning net long 0.8% OI and weekly decrease -0.5% (weak bullish, bearish tilt)
- Technicals: price below 20‑day and 50‑day SMA, MACD negative (short‑term bearish)

<details><summary><b>News</b> — score +0.00</summary>

- [Weekly ETFs: Seven of 11 sectors record outflows; Communication services sector leads inflows](https://www.tradingview.com/news/seekingalpha:103a2d5ed094b:0-weekly-etfs-seven-of-11-sectors-record-outflows-communication-services-sector-leads-inflows/)  
  <sub>TradingView, 18 hours ago</sub>  
  The world's largest exchange-traded fund, SPDR S&P 500 ETF Trust AMEX:SPY, saw outflows of $2.50B for the week ended November 20, while its price...
- [Oil And Gas Lift Energy ETFs Ahead Of Tuesday’s Open](https://finimize.com/content/oil-and-gas-lift-energy-etfs-ahead-of-tuesdays-open)  
  <sub>Finimize, 22 hours ago</sub>  
  WTI traded near $80.68 a barrel and natural gas futures rose to about $3.28, while BP and Cmb.Tech shares ticked higher premarket.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.16% (+0.01 on the week) | 5-year 4.62% (-0.26 on the week) | 10-year 4.83% (-0.24 on the week) | 30-year 5.24% (-0.17 on the week)
Yield curve, 10-year minus 3-month: +0.67 points -- upward sloping (normal)
US dollar index: 103.93 (+0.07 on the week)
Volatility (VIX): 31.72 (+7.2 on the week) -- stressed
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.1% (2026-10-01) | jobless claims 189k (2026-11-21)
Policy and expectations: Fed target 4.00% | market expects 2.1% inflation over 10 years
Rate path: 2-year Treasury 4.63% vs Fed target 3.75-4.00% -- the bond market prices about 3 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score -0.10</summary>

```text
Last close 138.73 (bar of 2026-11-25), from 502 daily bars
Trend: vs 20d SMA 145.65 (-4.8%), 50d 150.32 (-7.7%), 200d 130.07 (+6.7%); 50d above 200d
Momentum: RSI(14) 41.8 | MACD -4.762 vs signal -3.818 (histogram -0.944)
Returns: 1d +2.4% | 5d +1.9% | 1m -15.3% | 3m +6.7%
52-week range: 66.17 - 169.53 (now 70.2% of the way up)
Volatility: ATR(14) 5.04 (3.6% of price) | annualised 20d 49.9%
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

_Not available today._

</details>

<details><summary><b>How much oil and gas is in storage</b> — score -0.30</summary>

```text
US inventories, week ending 2026-11-13 (published the following Wednesday)
  Crude oil: 417.8 million barrels, +3.4 on the week (a build), 25% percentile over 52 weeks
  Petrol: 215.9 million barrels, +5.2 on the week (a build), 56% percentile over 52 weeks
  Diesel: 104.9 million barrels, +1.6 on the week (a build), 33% percentile over 52 weeks
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
Share count change: 1 week: +8.8% (163.67M) over 8d | 1 month: +37.2% (549.09M) over 33d
Shares outstanding: 14.60M | fund size: 2.03B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Corn (CORN) · Commodity — NEUTRAL, confidence 0.25

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Macro conditions are unchanged – yields and Fed policy show no surprise – and the news item is a company‑specific story that does not affect the broad corn exposure. Technicals show the price under both the 50‑day and 200‑day SMAs and a low RSI, indicating a mild downtrend. CFTC positioning reveals a small net short (1.7%) that shrank by 0.6% over the week, a slight bullish shift in speculator behavior. The fund’s roll cost is heavy (‑9.7% annual gap), which is a tailwind for short positions but not a decisive price driver. With no clear catalyst, the overall view remains neutral.

**Main reasons it gave:**
- Price below 50‑day (‑5.9%) and 200‑day (‑6.0%) SMAs
- RSI 39.3 indicates near‑oversold but still bearish
- CFTC large speculators net short 1.7% of OI, reduced by –0.6% week‑over‑week
- Cost of holding fund vs corn: –9.7% annual roll gap (heavy carry cost)
- No macro surprise – yields flat, Fed policy unchanged

<details><summary><b>News</b> — score +0.00</summary>

- [Key facts: PETR3 Buys Neomille Stake, Takes Logum; Weighs Corn Plants](https://www.tradingview.com/news/tradingview:2ae4249b0c83d:0-key-facts-petr3-buys-neomille-stake-takes-logum-weighs-corn-plants/)  
  <sub>TradingView, 4 hours ago</sub>  
  This is an AI-generated summary and may contain inaccuracies. Please verify any important information with the original sources.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.16% (+0.01 on the week) | 5-year 4.62% (-0.26 on the week) | 10-year 4.83% (-0.24 on the week) | 30-year 5.24% (-0.17 on the week)
Yield curve, 10-year minus 3-month: +0.67 points -- upward sloping (normal)
US dollar index: 103.93 (+0.07 on the week)
Volatility (VIX): 31.72 (+7.2 on the week) -- stressed
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.1% (2026-10-01) | jobless claims 189k (2026-11-21)
Policy and expectations: Fed target 4.00% | market expects 2.1% inflation over 10 years
Rate path: 2-year Treasury 4.63% vs Fed target 3.75-4.00% -- the bond market prices about 3 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score -0.20</summary>

```text
Last close 17.07 (bar of 2026-11-25), from 502 daily bars
Trend: vs 20d SMA 17.18 (-0.6%), 50d 18.14 (-5.9%), 200d 18.16 (-6.0%); 50d below 200d
Momentum: RSI(14) 39.3 | MACD -0.290 vs signal -0.336 (histogram 0.046)
Returns: 1d +0.4% | 5d +1.1% | 1m -2.1% | 3m -13.8%
52-week range: 16.47 - 20.29 (now 15.7% of the way up)
Volatility: ATR(14) 0.23 (1.4% of price) | annualised 20d 14.7%
Volume: 0.11x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score -0.15</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score -0.15</summary>

_Not available today._

</details>

<details><summary><b>Does this company beat its own forecasts</b> — score -0.15</summary>

_Not available today._

</details>

<details><summary><b>What holding this fund costs you</b> — score -0.15</summary>

```text
Cost of holding this fund instead of corn itself: -9.7% a year -- heavy: rolling contracts costs this fund real money
Measured: 3 months: fund -13.8%, commodity -11.4%, gap -2.4% | 6 months: fund -6.3%, commodity -0.8%, gap -5.5% | 12 months: fund -3.0%, commodity +6.7%, gap -9.7%
A commodity fund holds futures, not corn, and must sell each expiring contract to buy the next one. Where the next month costs more, that roll loses money every month. This gap is what the structure has actually cost, fees included -- it is history rather than a forecast, and it is not a direction: heavy carry is a reason to want a larger move to justify a long, and a tailwind for a short.
```

</details>

<details><summary><b>How much oil and gas is in storage</b> — score -0.15</summary>

_Not available today._

</details>

<details><summary><b>How the crop is growing</b> — score -0.15</summary>

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

<details><summary><b>Buying and selling by company insiders</b> — score +0.20</summary>

_Not available today._

</details>

<details><summary><b>Who is positioned how</b> — score +0.20</summary>

```text
Contract: CORN - CHICAGO BOARD OF TRADE (positions as of 2026-11-17, published the following Friday)
Large speculators: net short 1.7% of open interest (1,954,229 contracts)
Change on the week: -0.6% of open interest
Crowding: 30% percentile over 52 weeks -- within its normal range
Read this as crowding, not as a forecast: an extreme is as often the end of a move as the middle of one.
```

</details>

<details><summary><b>Money going into and out of this fund</b> — score +0.20</summary>

```text
Direction: money going out (1 month)
Share count change: 1 week: +1.4% (1.46M) over 7d | 1 month: -13.8% (-17.19M) over 32d
Shares outstanding: 6.31M | fund size: 107.67M
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Sugar (CANE) · Commodity — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> No material macro surprise, no decisive technical break, and mixed behavioural signals. Positioning shows a modest net‑long that slipped slightly, heavy roll cost penalises longs, and strong inflows offset but do not constitute a catalyst.

**Main reasons it gave:**
- Positioning: net long 16.3% of open interest, down -0.7% week‑over‑week
- Cost of holding: -8.2% annual roll cost penalizes long exposure
- Technicals: price below 20‑day and 50‑day SMAs, RSI 45.9, MACD slightly negative, low volume
- Fund flows: +26.5% share count increase over past month indicating strong inflows

<details><summary><b>News</b> — score +0.00</summary>

_No news found for this one today._

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.16% (+0.01 on the week) | 5-year 4.62% (-0.26 on the week) | 10-year 4.83% (-0.24 on the week) | 30-year 5.24% (-0.17 on the week)
Yield curve, 10-year minus 3-month: +0.67 points -- upward sloping (normal)
US dollar index: 103.93 (+0.07 on the week)
Volatility (VIX): 31.72 (+7.2 on the week) -- stressed
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.1% (2026-10-01) | jobless claims 189k (2026-11-21)
Policy and expectations: Fed target 4.00% | market expects 2.1% inflation over 10 years
Rate path: 2-year Treasury 4.63% vs Fed target 3.75-4.00% -- the bond market prices about 3 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 10.91 (bar of 2026-11-25), from 502 daily bars
Trend: vs 20d SMA 10.99 (-0.7%), 50d 11.47 (-4.8%), 200d 10.35 (+5.4%); 50d above 200d
Momentum: RSI(14) 45.9 | MACD -0.268 vs signal -0.256 (histogram -0.013)
Returns: 1d +2.2% | 5d +0.5% | 1m -5.3% | 3m -4.8%
52-week range: 9.02 - 12.47 (now 54.9% of the way up)
Volatility: ATR(14) 0.24 (2.2% of price) | annualised 20d 30.0%
Volume: 0.36x the 20-day average
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
Cost of holding this fund instead of sugar itself: -8.2% a year -- heavy: rolling contracts costs this fund real money
Measured: 3 months: fund -4.8%, commodity -0.3%, gap -4.5% | 6 months: fund +15.3%, commodity +30.2%, gap -14.9% | 12 months: fund +14.2%, commodity +22.3%, gap -8.2%
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
Share count change: 1 week: +3.6% (2.08M) over 7d | 1 month: +26.5% (12.73M) over 32d
Shares outstanding: 5.57M | fund size: 60.74M
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Copper (CPER) · Commodity — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:** no explanation. It wrote only “NEUTRAL”, so the main reasons below are all it gave.

**Main reasons it gave:**
- Crowded short: net short ~90.9% of OI, crowding at 2% percentile
- Heavy cost of holding: -5.9% annual cost vs copper
- Technical downtrend: price below 20d/50d/200d SMAs, RSI 22.2 (oversold)
- Fund inflows: share count up 6.6% week, 5.5% month (bullish) – contradictory to positioning

<details><summary><b>News</b> — score +0.00</summary>

_No news found for this one today._

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.16% (+0.01 on the week) | 5-year 4.62% (-0.26 on the week) | 10-year 4.83% (-0.24 on the week) | 30-year 5.24% (-0.17 on the week)
Yield curve, 10-year minus 3-month: +0.67 points -- upward sloping (normal)
US dollar index: 103.93 (+0.07 on the week)
Volatility (VIX): 31.72 (+7.2 on the week) -- stressed
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.1% (2026-10-01) | jobless claims 189k (2026-11-21)
Policy and expectations: Fed target 4.00% | market expects 2.1% inflation over 10 years
Rate path: 2-year Treasury 4.63% vs Fed target 3.75-4.00% -- the bond market prices about 3 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 31.66 (bar of 2026-11-25), from 502 daily bars
Trend: vs 20d SMA 36.43 (-13.1%), 50d 38.53 (-17.8%), 200d 37.87 (-16.4%); 50d above 200d
Momentum: RSI(14) 22.2 | MACD -1.768 vs signal -1.268 (histogram -0.500)
Returns: 1d -2.6% | 5d -7.2% | 1m -21.0% | 3m -20.8%
52-week range: 31.18 - 41.43 (now 4.6% of the way up)
Volatility: ATR(14) 0.93 (2.9% of price) | annualised 20d 31.0%
Volume: 0.17x the 20-day average
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
Cost of holding this fund instead of copper itself: -5.9% a year -- heavy: rolling contracts costs this fund real money
Measured: 3 months: fund -20.8%, commodity -18.9%, gap -1.9% | 6 months: fund -19.0%, commodity -16.5%, gap -2.5% | 12 months: fund +1.8%, commodity +7.7%, gap -5.9%
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
Share count change: 1 week: +6.6% (38.52M) over 7d | 1 month: +5.5% (32.09M) over 32d
Shares outstanding: 19.55M | fund size: 618.86M
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Gold (GLD) · Commodity — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> No macro surprise or decisive technical break; positioning shows a slight reduction in net long; cost of holding drags performance; technicals are bearish but lack strong volume confirmation.

**Main reasons it gave:**
- Positioning net long fell 2.5% week‑over‑week
- Cost of holding -1.8% annual drag
- Technicals: price below 20‑day, 50‑day, 200‑day SMAs; RSI 27.3 (oversold) but low volume and no decisive break

<details><summary><b>News</b> — score -0.10</summary>

- [SPDR Gold Shares (GLD) falls toward 52-week low as Fed rate hike bets rise](https://beinsure.com/news/spdr-gold-shares-gld-falls-toward-52-week-low-as-fed-rate-hike-bets-rise/)  
  <sub>Beinsure, 1 hour ago</sub>  
  Gold prices fall as Fed rate hike expectations, higher margin requirements and ETF outflows pressure SPDR Gold Shares (GLD), while US Treasuries outperform...
- [Gold Stopped Protecting Portfolios When Stocks Needed It Most (NYSEARCA:GLD)](https://seekingalpha.com/article/4971769-gold-stopped-protecting-portfolios-when-stocks-needed-it-most)  
  <sub>Seeking Alpha, 5 hours ago</sub>  
  SPDR Gold Shares ETF is a hold as central bank buying and liquidity-driven selling support retain gold despite its sharp decline.
- [Stocks or Gold? GDE Refuses to Choose: Every $100 Buys $90 of Each](https://www.google.com/goto?url=CAESqQEBxCJF1_UBqH2Bw8kaM8b1vhSDJHPeh34bTIAJUeIdC679K9RCmYDjvDjjcuH6oe_2dt2VGaZ1-u9AEjlDTa19s7RDMdOznaJwOLrQnru9Lo0wfh4RGCEkQBiWO9a8D1bK58q38qubAci0btGfqElMpHqI3J9W7s4RU-Xbc4yYzluBd-9vIoWUls7sZsOjA7PVLAA21vDyONd9B0qT-R4MsYDpKc937zI6&gsessionid=J5TZvni8ChY8Zxt3c_Kyioc4P9Fbh7JVn8nEyhZMUnJ2K3szm2fNhw)  
  <sub>24/7 Wall St., 1 hour ago</sub>  
  One WisdomTree fund provides exposure to stocks and gold, using futures leverage to stretch each dollar. Then stocks and gold fell together,...
- [Why is SPDR Gold Shares ETF sliding today?](https://www.google.com/goto?url=CAESogEBxCJF14KkT8-p-bNodreomk0iydVGC6WmhP1UwGUAdoG4Q9JTzaTPEfByGEoy2Zn-hjsfQ1KYIIR3gLUbEG7puJOrZCnm_NGw-7k9PX8JWp8czA8V5HyWx5oksp-0rtocEr-61Dwr-XYYqtpnvwxfmUIBxlZ5yZnhbW1NB2KHlBhXc_Alk1n4hJcIVHwcvPRcxCmWuw91ouiC3zabj-evfhE&gsessionid=J5TZvni8ChY8Zxt3c_Kyioc4P9Fbh7JVn8nEyhZMUnJ2K3szm2fNhw)  
  <sub>Investing.com, 3 hours ago</sub>  
  Investing.com -- SPDR® Gold Shares fell 1.3% in pre-open trading to reach $321.15, extending a multi-day retreat in bullion prices as markets fully priced...
- [Gold’s 35% Slide Tests GLD And Newmont Differently](https://www.google.com/goto?url=CAESogEBxCJF10ut0vWMlf8i1OrIgNWzbuzKOBltVFGJtJFuizVNUJVgmdDflW_oPeTji3kQmjVQ7_IdU3EEdtOQ4IFzkWCAjhHUWZ7Kc-8ks1Uc4KYPtsU7hNbVSS93Inm4g9EP1iAYqho72mekjP2Yl1_p3VCgQvTsZQfnY7pqWeK2iDly6DItJC-0j6GY60iLkpbXNrwyh3JQD9oGsB2S_IvaRZY&gsessionid=J5TZvni8ChY8Zxt3c_Kyioc4P9Fbh7JVn8nEyhZMUnJ2K3szm2fNhw)  
  <sub>Benzinga, 5 hours ago</sub>  
  Gold has not behaved like an automatic refuge during November's retreat in risk assets. Spot bullion was quoted at $3616.51 an ounce early on November 23,...
- [Gold ETFs Bleed $2.15 Billion in a Week, the Biggest Exit Since June](https://www.google.com/goto?url=CAESfgHEIkXXcDyLQLAl62bKgkrfajzXLn6ClLDcT1Z8OduZ9ZyVFSmEzCdfazAYhsVeyan2Q8e7MbK_0_VhQ12HUZGFufH3VXzhpzNXhGbmoYVhMRIWsIDhf7Q_ue0tDhbNjVWaCPRcO0VzNo8GF_sxDJ5UYnLimmRXpzUowq_shA&gsessionid=J5TZvni8ChY8Zxt3c_Kyioc4P9Fbh7JVn8nEyhZMUnJ2K3szm2fNhw)  
  <sub>BigGo Finance, 2 hours ago</sub>  
  Gold ETFs lost $2.149 billion in the week ended November 20, the largest weekly outflow since June, with holdings down 20.7 tonnes to 4247.3 tonnes,…
- [Weekly ETFs: Seven of 11 sectors record outflows; Communication services sector leads inflows](https://www.google.com/goto?url=CAES1gEBxCJF1_5Oi0i7jh70P8qAARR6gImRr6LWtCZTMGI_ciG2HwEf-odn1JAYPBIzMkzc5Jk-EVLVhy0H2bXmxw-qHKDxlymDFHfkA1-eOqZLbHXQWmJAYNZWtkeF_O_wMgowK5jf-Pdz6P0Jmh7JoZsQoWeCuJCZj1fgoT3nzASx7jmvd-fSbcr3FmBxgsrugNeV6QTdnelgxS7nHWT_GaSd_ywVhAGwl506OccrSp2nBfn-I940f35gCDYRMeFqweEQb5JgZ6xjg8oBpo0sCNW8M_0m_MmC&gsessionid=J5TZvni8ChY8Zxt3c_Kyioc4P9Fbh7JVn8nEyhZMUnJ2K3szm2fNhw)  
  <sub>TradingView, 18 hours ago</sub>  
  The world's largest exchange-traded fund, SPDR S&P 500 ETF Trust AMEX:SPY, saw outflows of $2.50B for the week ended November 20, while its price...
- [Global X Gold Explorers ETF (GOEX) Stock Price | Quotes & News](https://www.google.com/goto?url=CAES_AEBxCJF19ql5i-7WX8rswDt4EhqrxxoPSPgx7KKVFfwssuH1vBUYsXmieqT27R4A9a_RrfaAIxVF14MmzxA0jkni_xHuYKfC9lJUkoeK6EPWJtx-uCwZ9F8cdgyRMLlOvWNbbHNiFoqQwJ-gJVlq8ARSsKdds5S2CYvki5WD9Nh0E8FkNBwsiAm7LSthfLjyvkYsB1upaxpHCbjYM5EJFg_X4bo3IhaoFusE8Dn-k4fZEt-Zn_3lC9MHxdteRJ2OZ1UGv3U1FyDpPHPG5kozqS4dh848f7ZBnj-WNeg--NSh6qq1Ghq_SrNxyrT0Xf2mP9YhY9QWDx_62gIhlc&gsessionid=J5TZvni8ChY8Zxt3c_Kyioc4P9Fbh7JVn8nEyhZMUnJ2K3szm2fNhw)  
  <sub>Moomoo, 21 hours ago</sub>  
  Global X Gold Explorers ETF (GOEX) News. Gold and Silver Stocks Drop: What's Going On? SPDR Gold Shares ETF (NYSE:GLD) and iShares Silver Trust (NYSE:SLV)...
- [GLD NTA 24-11-2026 $3.52752](https://www.google.com/goto?url=CAESgQEBxCJF1zbubH96eyJqCwtIRr8dunoqLvnW0Mb4Y_0oxWU-u-7p0Nfro5nKHgh1OYD2I1mrkezHk8MSpkPMYWQvtHSStL4dsFPF-X9iX5Isqrk3mrofPHyyFduNckjZAhP5PTOBC85ENDI9BoASfOTpyYxFjAN67TD467eq9GL1ZV4&gsessionid=J5TZvni8ChY8Zxt3c_Kyioc4P9Fbh7JVn8nEyhZMUnJ2K3szm2fNhw)  
  <sub>BusinessDesk, 16 hours ago</sub>  
  View the full NZX announcement for Smart Gold ETF (GLD): GLD NTA 24-11-2026 $3.52752. Financial updates and company disclosures on BusinessDesk.
- [Gold ETF options draw neutral premium trade as bullion tracks stocks](https://www.google.com/goto?url=CAESlgEBxCJF1yszJ5v6MuYmKHjfmdjujytoEPIQkwBEyz-O3jlzMe8Z8fi9Obd8QFiSCEA54SJY8vgqGM5xkdejnXtdz183yX4_7V8dWWYpdDtk8bNX0KHqPRLFkgOXXtXgOkkEkqiwS1JOwbBXnIdGqYXw6-7fhzi4VyrtMOtuB_jmP1EeOsL35qDF1srPozJ9Osm_OB47Uts&gsessionid=J5TZvni8ChY8Zxt3c_Kyioc4P9Fbh7JVn8nEyhZMUnJ2K3szm2fNhw)  
  <sub>Traders Union, 18 hours ago</sub>  
  Gold's behavior in 2026 resembles equities, with ETFs showing neutral premium trades as bullion tracks stocks and options favor downside protection.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score -0.10</summary>

```text
US Treasury yields: 3-month 4.16% (+0.01 on the week) | 5-year 4.62% (-0.26 on the week) | 10-year 4.83% (-0.24 on the week) | 30-year 5.24% (-0.17 on the week)
Yield curve, 10-year minus 3-month: +0.67 points -- upward sloping (normal)
US dollar index: 103.93 (+0.07 on the week)
Volatility (VIX): 31.72 (+7.2 on the week) -- stressed
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.1% (2026-10-01) | jobless claims 189k (2026-11-21)
Policy and expectations: Fed target 4.00% | market expects 2.1% inflation over 10 years
Rate path: 2-year Treasury 4.63% vs Fed target 3.75-4.00% -- the bond market prices about 3 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score -0.20</summary>

```text
Last close 317.60 (bar of 2026-11-25), from 502 daily bars
Trend: vs 20d SMA 353.54 (-10.2%), 50d 370.85 (-14.4%), 200d 403.78 (-21.3%); 50d below 200d
Momentum: RSI(14) 27.3 | MACD -13.579 vs signal -9.873 (histogram -3.706)
Returns: 1d -2.4% | 5d -6.9% | 1m -14.7% | 3m -24.8%
52-week range: 317.60 - 495.90 (now 0.0% of the way up)
Volatility: ATR(14) 8.05 (2.5% of price) | annualised 20d 34.1%
Volume: 0.24x the 20-day average
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
Cost of holding this fund instead of gold itself: -1.8% a year -- a steady drag
Measured: 3 months: fund -24.8%, commodity -25.1%, gap +0.3% | 6 months: fund -23.1%, commodity -22.4%, gap -0.7% | 12 months: fund -16.5%, commodity -14.7%, gap -1.8%
A commodity fund holds futures, not gold, and must sell each expiring contract to buy the next one. Where the next month costs more, that roll loses money every month. This gap is what the structure has actually cost, fees included -- it is history rather than a forecast, and it is not a direction: heavy carry is a reason to want a larger move to justify a long, and a tailwind for a short.
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
Share count change: 1 week: +0.0% (0.00) over 7d | 1 month: +0.0% (0.00) over 32d
Shares outstanding: 260.30M | fund size: 82.67B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Silver (SLV) · Commodity — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Neutral as no material macro surprise, technicals show strong downtrend but no decisive breakout, positioning indicates net short sentiment, fund flows show strong inflows, and cost of holding drags long performance.

**Main reasons it gave:**
- Macro: yields stable, no policy surprise
- Technical: price far below SMAs, RSI 23.7, low volume, no breakout
- Positioning: net long 1% OI, down 2.1% week, crowded short
- Fund flows: share count +17.7% week, +13.9% month
- Cost of holding: -2.2% annual drag

<details><summary><b>News</b> — score +0.00</summary>

- [Pan American Silver Corp. (PAAS) Stock Price, News, Quote & History](https://ca.finance.yahoo.com/quote/PAAS/)  
  <sub>Yahoo! Finance Canada, 6 hours ago</sub>  
  Find the latest Pan American Silver Corp. (PAAS) stock quote, history, news and other vital information to help you with your stock trading and investing.
- [SLVR: Physical Silver And Silver Miners' Coverage In One Vehicle (NASDAQ:SLVR)](https://seekingalpha.com/article/4971863-slvr-physical-silver-and-silver-miners-coverage-in-one-solitary-vehicle)  
  <sub>Seeking Alpha, 52 minutes ago</sub>  
  SLVR is a Silver Miners ETF, its 5.5% yield comes with over two-thirds in miners, 17.5% capped holdings in physical silver and a 0.65% expense ratio.
- [Weekly ETFs: Seven of 11 sectors record outflows; Communication services sector leads inflows](https://www.google.com/goto?url=CAES1gEBxCJF1ysKrORaNVBuOs-Kq-_zWZI19qhY9wEiuVSYVAhxGmTILMCta0CqVh5GBnMKIUIoyK_3kxDJdzWpq0vv_dbdLl6ZNYDmu1o-AqPSI0ueb2lFOlQIJvDmrvpnY-qbtU5dkyJbzTJfWPlpMJYPMrGt1Vfc52iWtfVVsczyTD3fUrNFePKH8cVHfUne-hKPpoadhdZKmKIlKeEB7mhBxhaCrsf0-w_LZG2UowtNUT5OnTCRzxu1COTPCRUA2hngdew2kEIwnxYjbjrklvjqpOBH0K_3&gsessionid=kdDPBvH0swsUaKPoQ_7hFqylk-5rwrHR2iP0nsppQAnHx4-do2nwOg)  
  <sub>TradingView, 18 hours ago</sub>  
  The world's largest exchange-traded fund, SPDR S&P 500 ETF Trust AMEX:SPY, saw outflows of $2.50B for the week ended November 20, while its price...
- [Gold, Silver in focus: Tech analyst decodes charts of Gold, Silver ETFs](https://www.google.com/goto?url=CAES1wEBxCJF1zQbfvMZHSfqzrKf10TeEJ3WJMpyAtzqt1w4NZx5XUrdIBnyfWGljLekhuiOl7LGuozEJdTFoZhdzbRJN7ngNunwBzuQlOcXpS1o2uXXUbyU3H6FHN4b1ub1JHEi9KOuYJzOMofwelZlFHZpF82sG4Uk57f5CdqX-SZiKDL1Zpb2uqB7CKxU_6UecKomgs6Czlb-F0eLpoNu7Gpvkpyb_kP70Fg3o8OmAAXQJ_7gjprSSB9-iVoAZ2mLr2sfnyegNLbvIg-mDp3skx5JtLzW25z7MA&gsessionid=kdDPBvH0swsUaKPoQ_7hFqylk-5rwrHR2iP0nsppQAnHx4-do2nwOg)  
  <sub>Business Standard, 9 hours ago</sub>  
  Nippon India Silver and Gold ETF: Drumil Vithlani, Senior Technical Research Analyst at Tiny Epic believes that Nippon India ETF Gold BeES and Nippon India...
- [First Majestic Silver Corp. (AG.TO) Stock Price, News, Quote & History](https://www.google.com/goto?url=CAESZAHEIkXXay8TzpsWKQeTbkFspi7yarObGseOH14PlkEFseN36mSC5K0kby2MufLpXE5GQu4CgwahYOngX9V42owKdA4dB6HGHjM-DwI8VKdkXZnOdqO-gKqZdast_pXZTsX6wzU&gsessionid=kdDPBvH0swsUaKPoQ_7hFqylk-5rwrHR2iP0nsppQAnHx4-do2nwOg)  
  <sub>Yahoo! Finance Canada, 6 hours ago</sub>  
  Find the latest First Majestic Silver Corp. (AG.TO) stock quote, history, news and other vital information to help you with your stock trading and...
- [Silver ETFs plunge over 5%, gold ETFs fall nearly 3% as bullion prices extend losses while stock markets...](https://www.google.com/goto?url=CAES6AEBxCJF10pRAxkTpgSB6gZ7epaH4ETrAEHYOU4IfBv7Mw5V9wGTlP34B3fyv3jnqNfKENvF7Cc8SBAfkX-I4OKOVFMIagWlTxnPNzI3snorggZqlKrYoM0dEmTMRMcVXKFAHmylegO9ukXELqEXzUmDnpYWZ3FpJi5xv4KZ0W-U2fX0xb8kHt-86cGp9r0jELICtiqKuzlgl8S7wG9HQCnHszNwev7iJiHPwstvtwy2uMKoBMKxhK3N6CkygsjGqfxcRmMxO0sLG5ylHVFB9cACUfdV7cGqT8XVxP574_6Q239artc5Bqzi&gsessionid=kdDPBvH0swsUaKPoQ_7hFqylk-5rwrHR2iP0nsppQAnHx4-do2nwOg)  
  <sub>Moneycontrol.com, 5 hours ago</sub>  
  Gold and silver exchange-traded funds (ETFs) witnessed sharp selling pressure on Wednesday, November 25, even as benchmark equity indices rallied more than...
- [Gold, silver ETF AUM nearly double in a year; gold funds lead the rise: Franklin Templeton](https://www.google.com/goto?url=CAESuQEBxCJF1_Fr0oTYQ23AWfCRrgjJOUv5rpOeesCEC6cT71yJMILMa31kji_QjS3CSzTIa62YgWJbpeHS1iOlX0NNozuV3jIgwIfTFYa4tXWGnof0-OdD1iKCKEDUyL41mUkfCQfvydnLK8j9BkecfhaCXtW90L7zNFePg7DoUPDBkir2y8IPlYaboKq7EaT389RuVZoA9wY2bWRin2V6ghoEZ1NUQrdwiF_dLPk9DAc9xR_dS4fmuusv9Q&gsessionid=kdDPBvH0swsUaKPoQ_7hFqylk-5rwrHR2iP0nsppQAnHx4-do2nwOg)  
  <sub>CNBC TV18, 13 hours ago</sub>  
  Assets under management (AUM) of gold and silver exchange-traded funds (ETFs) have expanded significantly over the past year, with gold ETF assets rising...
- [Gold, Silver ETFs Plunge Up to 5.6% in a Day While Sensex Jumps 1.7%. What’s Going On?](https://www.google.com/goto?url=CAESeQHEIkXXHK8e85XHkJ6NECMTziu2D5dN9OZVT3PMsny7dKsKVEq7IeZAfMg2SyTx2-3iIvxQqRuJYUBpuPTyaUyUV40Cni-BJcfeYnsB4JAmXeKKsKUVaigEXSQwdHgBNQNU7caQDqIwDpgW2ATwjwR8Ntf0-UPar-M&gsessionid=kdDPBvH0swsUaKPoQ_7hFqylk-5rwrHR2iP0nsppQAnHx4-do2nwOg)  
  <sub>NiftyTrader, 4 hours ago</sub>  
  Silver ETFs Plunge Up to 5.6% and gold ETFs fell nearly 3% on November 25 as bullion prices extended losses.
- [Aya Gold & Silver Inc. (AYA.TO) Stock Price, News, Quote & History](https://www.google.com/goto?url=CAESZQHEIkXXu50I6KE-jb4yAhBxnb1TzU87w7PwmlX6X21gC5YFosN8-7_yNEoVOvJsDyCdRWVLT5hzRpbRxyZkvLtX7C6tNrGmURaaUiXGiHEmrmohzF2AVYE6qD8Hzvx7SghXOtGj&gsessionid=kdDPBvH0swsUaKPoQ_7hFqylk-5rwrHR2iP0nsppQAnHx4-do2nwOg)  
  <sub>Yahoo! Finance Canada, 12 hours ago</sub>  
  Find the latest Aya Gold & Silver Inc. (AYA.TO) stock quote, history, news and other vital information to help you with your stock trading and investing.
- [Current price of silver as of Tuesday, Nov. 24, 2026](https://www.google.com/goto?url=CAESegHEIkXX6zcl81b3Qr41Nxi4sumia7ozbg3kClHuBRuu8W6ZmyHF4uFVowkMamjb6NmYCJkApXCLtpOQC-c7LVKm2trXdCCKc-LH8OcQuoAuWY0n9LLAqWMasib-Ej2mP96iafj10Zv_G5yOAe6Nisg4DTdEh9ivy_c_&gsessionid=kdDPBvH0swsUaKPoQ_7hFqylk-5rwrHR2iP0nsppQAnHx4-do2nwOg)  
  <sub>Fortune, 16 hours ago</sub>  
  If you're worried about increased inflation, adding precious metals like silver to your portfolio can be a smart choice.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.16% (+0.01 on the week) | 5-year 4.62% (-0.26 on the week) | 10-year 4.83% (-0.24 on the week) | 30-year 5.24% (-0.17 on the week)
Yield curve, 10-year minus 3-month: +0.67 points -- upward sloping (normal)
US dollar index: 103.93 (+0.07 on the week)
Volatility (VIX): 31.72 (+7.2 on the week) -- stressed
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.1% (2026-10-01) | jobless claims 189k (2026-11-21)
Policy and expectations: Fed target 4.00% | market expects 2.1% inflation over 10 years
Rate path: 2-year Treasury 4.63% vs Fed target 3.75-4.00% -- the bond market prices about 3 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score -0.40</summary>

```text
Last close 35.22 (bar of 2026-11-25), from 502 daily bars
Trend: vs 20d SMA 43.35 (-18.8%), 50d 49.80 (-29.3%), 200d 60.53 (-41.8%); 50d below 200d
Momentum: RSI(14) 23.7 | MACD -3.672 vs signal -3.006 (histogram -0.666)
Returns: 1d -4.4% | 5d -13.5% | 1m -28.4% | 3m -43.9%
52-week range: 35.22 - 105.60 (now 0.0% of the way up)
Volatility: ATR(14) 1.80 (5.1% of price) | annualised 20d 55.0%
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
Cost of holding this fund instead of silver itself: -2.2% a year -- a steady drag
Measured: 3 months: fund -43.9%, commodity -43.7%, gap -0.2% | 6 months: fund -48.5%, commodity -48.3%, gap -0.2% | 12 months: fund -24.5%, commodity -22.2%, gap -2.2%
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
Share count change: 1 week: +17.7% (3.48B) over 8d | 1 month: +13.9% (2.81B) over 33d
Shares outstanding: 656.62M | fund size: 23.12B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Soybeans (SOYB) · Commodity — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:** no explanation. It wrote only “NEUTRAL”, so the main reasons below are all it gave.

**Main reasons it gave:**
- Positioning net long decreased 0.7% week‑over‑week (small bearish shift)
- Cost of holding 1.2% per year (roll drag on longs)
- Technical indicators mixed: price above 20‑day SMA but below 50‑day SMA, MACD just above signal
- No macro surprise: yields stable, VIX high but unchanged

<details><summary><b>News</b> — score +0.00</summary>

- [A Look At The Soybean Boom, From Farm To Global Markets](https://seekingalpha.com/article/4971713-look-at-the-soybean-boom-from-farm-to-global-markets)  
  <sub>Seeking Alpha, 10 hours ago</sub>  
  An estimated 4.5 billion bushel soybean harvest is underway across the U.S., with strong demand from renewable diesel producers and export markets...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.16% (+0.01 on the week) | 5-year 4.62% (-0.26 on the week) | 10-year 4.83% (-0.24 on the week) | 30-year 5.24% (-0.17 on the week)
Yield curve, 10-year minus 3-month: +0.67 points -- upward sloping (normal)
US dollar index: 103.93 (+0.07 on the week)
Volatility (VIX): 31.72 (+7.2 on the week) -- stressed
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.1% (2026-10-01) | jobless claims 189k (2026-11-21)
Policy and expectations: Fed target 4.00% | market expects 2.1% inflation over 10 years
Rate path: 2-year Treasury 4.63% vs Fed target 3.75-4.00% -- the bond market prices about 3 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 25.86 (bar of 2026-11-25), from 502 daily bars
Trend: vs 20d SMA 25.72 (+0.5%), 50d 26.65 (-3.0%), 200d 25.40 (+1.8%); 50d above 200d
Momentum: RSI(14) 46.7 | MACD -0.219 vs signal -0.290 (histogram 0.071)
Returns: 1d -0.1% | 5d +1.1% | 1m -1.6% | 3m -3.4%
52-week range: 21.71 - 28.14 (now 64.5% of the way up)
Volatility: ATR(14) 0.28 (1.1% of price) | annualised 20d 14.7%
Volume: 0.18x the 20-day average
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
Cost of holding this fund instead of soybeans itself: 1.2% a year -- the roll has been paying this fund
Measured: 3 months: fund -3.4%, commodity -2.0%, gap -1.4% | 6 months: fund +2.5%, commodity +3.1%, gap -0.6% | 12 months: fund +10.9%, commodity +9.7%, gap +1.2%
A commodity fund holds futures, not soybeans, and must sell each expiring contract to buy the next one. Where the next month costs more, that roll loses money every month. This gap is what the structure has actually cost, fees included -- it is history rather than a forecast, and it is not a direction: heavy carry is a reason to want a larger move to justify a long, and a tailwind for a short.
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
Contract: SOYBEANS - CHICAGO BOARD OF TRADE (positions as of 2026-11-17, published the following Friday)
Large speculators: net long 11.4% of open interest (997,948 contracts)
Change on the week: -0.7% of open interest
Crowding: 28% percentile over 52 weeks -- within its normal range
Read this as crowding, not as a forecast: an extreme is as often the end of a move as the middle of one.
```

</details>

<details><summary><b>Money going into and out of this fund</b> — score -0.10</summary>

```text
Direction: money going out (1 month)
Share count change: 1 week: +0.2% (70.88K) over 7d | 1 month: -10.7% (-4.69M) over 32d
Shares outstanding: 1.52M | fund size: 39.31M
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Natural gas (UNG) · Commodity — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:** no explanation. It wrote only “NEUTRAL”, so the main reasons below are all it gave.

**Main reasons it gave:**
- Large speculators net short 13% of open interest (crowded short)
- Cost of holding -9.2% per year heavy roll cost
- US natural gas inventories up 20 BCF, 96th percentile (high build)
- EIA forecast price fall 11% over six months
- Price below 200‑day SMA (-6.1%) indicating long‑term bearish trend

<details><summary><b>News</b> — score +0.00</summary>

- [UNG Jan 2028 6.000 call (UNG280121C00006000) Seasonal Returns Chart](https://ca.finance.yahoo.com/quote/UNG280121C00006000/seasonality/)  
  <sub>Yahoo! Finance Canada, 19 hours ago</sub>  
  UNG Jan 2028 6.000 call (UNG280121C00006000) seasonal returns chart provides the mean and median returns by month to inform your investment strategy.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.16% (+0.01 on the week) | 5-year 4.62% (-0.26 on the week) | 10-year 4.83% (-0.24 on the week) | 30-year 5.24% (-0.17 on the week)
Yield curve, 10-year minus 3-month: +0.67 points -- upward sloping (normal)
US dollar index: 103.93 (+0.07 on the week)
Volatility (VIX): 31.72 (+7.2 on the week) -- stressed
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.1% (2026-10-01) | jobless claims 189k (2026-11-21)
Policy and expectations: Fed target 4.00% | market expects 2.1% inflation over 10 years
Rate path: 2-year Treasury 4.63% vs Fed target 3.75-4.00% -- the bond market prices about 3 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 10.23 (bar of 2026-11-25), from 502 daily bars
Trend: vs 20d SMA 9.87 (+3.6%), 50d 10.27 (-0.4%), 200d 10.89 (-6.1%); 50d below 200d
Momentum: RSI(14) 51.7 | MACD 0.054 vs signal -0.007 (histogram 0.060)
Returns: 1d -0.9% | 5d -3.6% | 1m +6.1% | 3m -2.0%
52-week range: 9.00 - 16.90 (now 15.5% of the way up)
Volatility: ATR(14) 0.44 (4.3% of price) | annualised 20d 56.3%
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
Cost of holding this fund instead of natural gas itself: -9.2% a year -- heavy: rolling contracts costs this fund real money
Measured: 3 months: fund -2.0%, commodity +25.4%, gap -27.4% | 6 months: fund -14.0%, commodity +11.0%, gap -25.0% | 12 months: fund -29.0%, commodity -19.9%, gap -9.2%
A commodity fund holds futures, not natural gas, and must sell each expiring contract to buy the next one. Where the next month costs more, that roll loses money every month. This gap is what the structure has actually cost, fees included -- it is history rather than a forecast, and it is not a direction: heavy carry is a reason to want a larger move to justify a long, and a tailwind for a short.
```

</details>

<details><summary><b>How much oil and gas is in storage</b> — score -0.50</summary>

```text
US inventories, week ending 2026-11-13 (published the following Wednesday)
  Natural gas: 3,882.0 billion cubic feet, +20.0 on the week (a build), 96% percentile over 52 weeks -- high for the time of year
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

<details><summary><b>Buying and selling by company insiders</b> — score -0.30</summary>

_Not available today._

</details>

<details><summary><b>Who is positioned how</b> — score -0.30</summary>

```text
Contract: NAT GAS NYME - NEW YORK MERCANTILE EXCHANGE (positions as of 2026-11-17, published the following Friday)
Large speculators: net short 13.0% of open interest (1,630,218 contracts)
Change on the week: +0.7% of open interest
Crowding: 5% percentile over 52 weeks -- a crowded short by the standards of the past year
Read this as crowding, not as a forecast: an extreme is as often the end of a move as the middle of one.
```

</details>

<details><summary><b>Money going into and out of this fund</b> — score -0.30</summary>

```text
Direction: money coming in (1 month)
Share count change: 1 week: +2.4% (12.11M) over 8d | 1 month: +11.1% (52.12M) over 33d
Shares outstanding: 50.96M | fund size: 521.09M
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Wheat (WEAT) · Commodity — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:** no explanation. It wrote only “NEUTRAL”, so the main reasons below are all it gave.

**Main reasons it gave:**
- Large speculators net short 15.2% of OI, weekly change -0.6% (insider positioning).
- Fund flows: share count down 12.5% over past month, indicating outflows.
- Cost of holding -9.9% annualized, heavy roll cost (fundamental).
- Crop condition: 48% good/excellent, down 7 points YoY (less supply, bullish).
- Technicals: price below 20d, 50d, 200d SMAs, RSI 34.8, low volume – no decisive break.

<details><summary><b>News</b> — score +0.00</summary>

_No news found for this one today._

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.16% (+0.01 on the week) | 5-year 4.62% (-0.26 on the week) | 10-year 4.83% (-0.24 on the week) | 30-year 5.24% (-0.17 on the week)
Yield curve, 10-year minus 3-month: +0.67 points -- upward sloping (normal)
US dollar index: 103.93 (+0.07 on the week)
Volatility (VIX): 31.72 (+7.2 on the week) -- stressed
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.1% (2026-10-01) | jobless claims 189k (2026-11-21)
Policy and expectations: Fed target 4.00% | market expects 2.1% inflation over 10 years
Rate path: 2-year Treasury 4.63% vs Fed target 3.75-4.00% -- the bond market prices about 3 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 21.25 (bar of 2026-11-25), from 502 daily bars
Trend: vs 20d SMA 21.75 (-2.3%), 50d 23.39 (-9.1%), 200d 23.64 (-10.1%); 50d below 200d
Momentum: RSI(14) 34.8 | MACD -0.556 vs signal -0.619 (histogram 0.063)
Returns: 1d -0.4% | 5d +0.4% | 1m -4.9% | 3m -21.9%
52-week range: 19.88 - 28.00 (now 16.9% of the way up)
Volatility: ATR(14) 0.38 (1.8% of price) | annualised 20d 22.1%
Volume: 0.07x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score -0.15</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score -0.15</summary>

_Not available today._

</details>

<details><summary><b>Does this company beat its own forecasts</b> — score -0.15</summary>

_Not available today._

</details>

<details><summary><b>What holding this fund costs you</b> — score -0.15</summary>

```text
Cost of holding this fund instead of wheat itself: -9.9% a year -- heavy: rolling contracts costs this fund real money
Measured: 3 months: fund -21.9%, commodity -21.2%, gap -0.7% | 6 months: fund -10.8%, commodity -6.2%, gap -4.6% | 12 months: fund +2.2%, commodity +12.1%, gap -9.9%
A commodity fund holds futures, not wheat, and must sell each expiring contract to buy the next one. Where the next month costs more, that roll loses money every month. This gap is what the structure has actually cost, fees included -- it is history rather than a forecast, and it is not a direction: heavy carry is a reason to want a larger move to justify a long, and a tailwind for a short.
```

</details>

<details><summary><b>How much oil and gas is in storage</b> — score -0.15</summary>

_Not available today._

</details>

<details><summary><b>How the crop is growing</b> — score -0.15</summary>

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

<details><summary><b>Buying and selling by company insiders</b> — score -0.10</summary>

_Not available today._

</details>

<details><summary><b>Who is positioned how</b> — score -0.10</summary>

```text
Contract: WHEAT-SRW - CHICAGO BOARD OF TRADE (positions as of 2026-11-17, published the following Friday)
Large speculators: net short 15.2% of open interest (558,414 contracts)
Change on the week: -0.6% of open interest
Crowding: 30% percentile over 52 weeks -- within its normal range
Read this as crowding, not as a forecast: an extreme is as often the end of a move as the middle of one.
```

</details>

<details><summary><b>Money going into and out of this fund</b> — score -0.10</summary>

```text
Direction: money going out (1 month)
Share count change: 1 week: +0.4% (977.24K) over 7d | 1 month: -12.5% (-33.01M) over 32d
Shares outstanding: 10.89M | fund size: 231.45M
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

