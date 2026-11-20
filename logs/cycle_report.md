# Daily report

**20 Nov 2026, 18:39 Israel time (16:39 UTC)** · 80 names checked · 0 traded · 11 with a problem

**Answers with no explanation:** 9 of 57 (the model wrote only a label, like “NEUTRAL”, where its reason should be). Their main reasons are still shown.

**Run:** started by the outside scheduler (via supabase-cron), on time (planned for 14:40 UTC).

| Group | Looked at | Took a side | No clear view | Problems |
| --- | --- | --- | --- | --- |
| Companies | 16 | 3 | 13 | 0 |
| Whole-market funds | 14 | 0 | 13 | 1 |
| Sector and country funds | 41 | 0 | 39 | 2 |
| Commodities | 9 | 0 | 1 | 8 |

## Open positions

Checked before any new trade. R is what the trade risked at entry; the ladder sells a third at +1R and another at +3R, the stop-loss follows the price up every day, and it only ever moves up.

| Position | What happened |
| --- | --- |
| Brazil (EWZ) · Sector or country | **Sold part.** Sold 69 of 207 shares at +1.15R, 138 still held. Stop-loss raised 32.01 → 31.36. |
| South Korea (EWY) · Sector or country | **Stop raised.** At +0.45R, following the price. Stop-loss raised 148.87 → 143.75. |
| HDFC Bank (HDB) · Company | **Stop raised.** At +4.21R, following the price. Stop-loss raised 25.40 → 26.52. |
| JPMorgan Chase (JPM) · Company | **Stop raised.** At +0.40R, following the price. Stop-loss raised 340.79 → 335.02. |
| MercadoLibre (MELI) · Company | **Stop raised.** At +0.68R, following the price. Stop-loss raised 1538.52 → 1505.92. |
| Nvidia (NVDA) · Company | **Stop raised.** At +6.44R, following the price. Stop-loss raised 174.60 → 158.72. |
| Elbit Systems (ESLT) · Company | **Holding.** -0.48R, holding 7 shares. Stop-loss 640.17. |
| Eli Lilly (LLY) · Company | **Holding.** -0.33R, holding 3 shares. Stop-loss 1304.66. |
| Procter & Gamble (PG) · Company | **Holding.** +1.52R, holding 2 shares. Stop-loss 165.90. |
| Toyota (TM) · Company | **Holding.** -0.42R, holding 1 shares. Stop-loss 205.44. |
| US house builders (XHB) · Sector or country | **Holding.** -0.49R, holding 68 shares. Stop-loss 97.50. |
| Exxon Mobil (XOM) · Company | **Holding.** -0.33R, holding 30 shares. Stop-loss 153.50. |

## How to read this

Once a day the system looks at every name on the list. For each one it reads five kinds of evidence and gives each kind a score from -1.00 (bad) to +1.00 (good). Then it picks a side and says how sure it is, from 0.00 to 1.00.

The three sides: **BULLISH** = the model thinks the price will go up; **BEARISH** = the model thinks the price will go down; **NEUTRAL** = the model has no clear view.

Being sure is not enough on its own. A trade only happens when confidence reaches **0.30**. Below that the system writes down what it thought and does nothing. The size of a trade, the stop-loss and every limit are decided by plain code, not by the model.

Open positions are checked first, before any new trade. When a trade has earned back what it risked (+1R), a third of it is sold and the stop-loss moves up to the entry price, so it can no longer lose. At three times that (+3R) another third is sold and the stop moves up again. The last third stays open. Every day the stop-loss also follows the price up, so a position only ever closes when its stop is hit. The stop only ever moves up.

Under each name you will find the five scores. Click a grey line to open it and see the exact evidence behind that score. The words inside quotation marks are the model's own; nothing there has been rewritten.

## Companies

### Microsoft (MSFT) · Company — BULLISH, confidence 0.70

**Result:** REJECTED · no room under the sleeve budget limit

**In the model's own words:** no explanation. It wrote only “BUY”, so the main reasons below are all it gave.

**Main reasons it gave:**
- Anthropic commits $47.2B minimum to Azure (AI partnership)
- Stifel Nicolaus maintains Buy rating, $650 price target
- Insider net purchase of 257,656 shares (+3.1% of holdings) in last 180 days
- Technical indicators: price below 20‑day SMA, RSI 38.4, low volume (bearish)

<details><summary><b>News</b> — score +0.80</summary>

- [What Could Stall Microsoft Stock’s Run?](https://www.trefis.com/stock/msft/articles/627236/what-could-stall-microsoft-stocks-run/2026-11-20)  
  <sub>Trefis, 5 hours ago</sub>  
  Today's big story: Will 2027 Be A 2022 Repeat For Stocks?Microsoft (MSFT) stock returned 19.4% over the six months to November 19, 2026, while the S&P 500...
- [New Buy Rating for Microsoft (MSFT), the Technology Giant](https://www.theglobeandmail.com/investing/markets/stocks/MSFT/pressreleases/8935286/new-buy-rating-for-microsoft-msft-the-technology-giant/)  
  <sub>The Globe and Mail, 60 minutes ago</sub>  
  Stifel Nicolaus analyst Brad Reback maintained a Buy rating on Microsoft today and set a price target of $650.00. According to TipRanks, Reback is a 4-star...
- [Key facts: Azure $47.2B pact; $100B revenue; $1B Anthropic shares](https://www.google.com/goto?url=CAEStgEBxCJF101S7nPrkr_zIAxwg1TSe01_VSrRP9AboANrC9pPsYKiWLZjXAev-ixEY25rf1Fbh2Moh-VUmGoEfeZbS188aMkE1B7fovoaUArL5khvfpaUW9y9QqWSFRTFFRdmRdnWLQnohl0J4LfZ0Pr6rdgjOYfIipx1UkBKfBn7Fi9SrL84wWBMgkxjBwOeYg2joJXveGhEquQKeIN_ukOee4XwQ2u5juiic8xanOC2VqQAXHLrwg&gsessionid=iqQLgKlFOm4j6KgUYk09qNZNPqZ-xZDrd5fcg-GWdVf5uLF530KbjA)  
  <sub>TradingView, 7 hours ago</sub>  
  This is an AI-generated summary and may contain inaccuracies. Please verify any important information with the original sources.
- [Microsoft Stocks Rise 3.16% as Anthropic Commits $47.2 Billion Minimum to Azure](https://www.google.com/goto?url=CAESmAEBxCJF180JMLOO60uaH2WwGAsPZanFg96o3NG81N1THP3n-P-MKCeNcxc6MkQGC52ePEMJI_XlChNYJUAedJl8FYb8wZLDm_3bDBNzvMCGhm8w35kCZi548j12PsIGVExgD4jYOujgdYWAPjB6AIo__XF3uiVuyr5k9ubqhR6S95RHAqU3iGwOAm-kB-nJG4d_CMwnICOP0A&gsessionid=iqQLgKlFOm4j6KgUYk09qNZNPqZ-xZDrd5fcg-GWdVf5uLF530KbjA)  
  <sub>Yahoo Finance, 21 hours ago</sub>  
  This article first appeared on GuruFocus. Microsoft (NASDAQ:MSFT) shares rose 3.16% to $524.36 at 9:45 a.m. ET on November 19 in regular trading,...
- [White House names Kirsten Davies as cyber chief after outages hit MSFT, banks (MSFT:NASDAQ)](https://www.google.com/goto?url=CAESrwEBxCJF1_rNgI0BuPwe39257BVNS1aaqyWBniMa5banPDceg4UaKWhCKz6s-KrJWBewt4lzr0smDJ4AiH1b4D18hueHGrRCaG0pg9f6R2iDuHjCbGaeJa2YOYYJXtR5lezoZh9q-XIbTKVQUMmx_GAzZNqXx7N4lDfGYKLHWnCVib9TEivGf-hide10bF9NHbgxs7sl-HyzwABuF8Yh9JpeXVdkBbCYKOM6QPcBibH_&gsessionid=iqQLgKlFOm4j6KgUYk09qNZNPqZ-xZDrd5fcg-GWdVf5uLF530KbjA)  
  <sub>Seeking Alpha, 9 hours ago</sub>  
  The White House appoints Defense Department CIO Kirsten Davies as national cyber director, replacing Sean Cairncross amid widespread service disruptions.
- [$1 Million In Microsoft 10 Years Ago: Worth It?](https://www.google.com/goto?url=CAESpgEBxCJF17IrlNAgC4bDxyIq5wwktOjHfF-93eGlI_oO358YKo72ntjQIrzdeHHA_nnmNhNoIQ6x7Svu6PVrG3JIEdMpZ90EFbojMNmQnj1w4LjRf7WxRALJW61CQ65vEjuYqc88pOgRcf5oCcZFyc7xvMFT59tU0e8kYzL0HxX6npnY2Str-GLfftRjKb2VrHPcCRrN9A_PZrxzwVSFD9vPzd9u8bsQ&gsessionid=iqQLgKlFOm4j6KgUYk09qNZNPqZ-xZDrd5fcg-GWdVf5uLF530KbjA)  
  <sub>Trefis, 6 hours ago</sub>  
  Today's big story: Will 2027 Be A 2022 Repeat For Stocks? $1 million put into Microsoft at the Friday, Nov 18, 2016 close was worth about $9.25 million at...
- [(MSFT) Equity Trading Insights (MSFT:CA)](https://www.google.com/goto?url=CAESkwEBxCJF1xRMg194DZaCae45nYLxRRtj843Qiz_8tgncdyNSqr9T2qh6MSm37_HiGED1t4Qi-2cptsI0nFpdRJoVngcVUwmvHlWQO5FR4UKQSnK5U_L4GieZI4P2DWnaYY1Kws0ZwtjnYMdNoYNwqjuga48BjsEXNrIj3tMMkrF3o5f3fQ0Krj_tNkJgtUfV0_Hc4AM&gsessionid=iqQLgKlFOm4j6KgUYk09qNZNPqZ-xZDrd5fcg-GWdVf5uLF530KbjA)  
  <sub>Stock Traders Daily, 10 hours ago</sub>  
  Equity Trading Insights for Microsoft CDR (CAD Hedged) (MSFT) Featuring Key Buy and Sell Signals.
- [Bill Ackman Says His Microsoft “Sale” Was Really a Swap Into Options](https://www.google.com/goto?url=CAESqwEBxCJF1-suNb95ZCNWgzr5Jtyyu5tF2iUp8EqPn_d05drZOPVfPKm8P9-qfyiTxx1kC9qei83VXsNgVHubQS3ivRmtEIieaJYtVpcdb6zXDz9gHx-IRYOuEHZQT_15liY1O8AchS3ApsXMP6Y3Ctf2b44kvQBS947OCTQWzfwfZbNflGWbmLntd6EtEEf9YVa2TlGZ-5_lJd0plN00n8Fui4nCgLfnOi1e5u4&gsessionid=iqQLgKlFOm4j6KgUYk09qNZNPqZ-xZDrd5fcg-GWdVf5uLF530KbjA)  
  <sub>24/7 Wall St., 22 hours ago</sub>  
  Bill Ackman says Pershing Square's Microsoft sale was half a trade: he sold two million shares but bought two million deep-in-the-money options.
- [Why this fund manager loves Microsoft right now](https://www.google.com/goto?url=CAESkwEBxCJF16jUAlrYiukdqzYsRi3R8uZCUATASvibXwfrFdce1uAz-QZe_Rrz3D6rkI4TH8hjLHHDkZqYiR-wCRPmvuJUMVwEwp9t9sDmzIFI882pLgpDBaGCXQbtgjyHbPpjlanqLBI-jgqSkWJecFWG4CRB2mf2snjQW3bPo0WMOD7w8lq00k_7SIn1QP8Ly8Zichs&gsessionid=iqQLgKlFOm4j6KgUYk09qNZNPqZ-xZDrd5fcg-GWdVf5uLF530KbjA)  
  <sub>Cantech Letter, 21 hours ago</sub>  
  Microsoft's (Microsoft Stock Quote, Chart, News, Analysts, Financials NASDAQ:MSFT) strong cash flow and balance sheet make it an attractive investment in...
- [The Stocks That Win From Anthropic's IPO](https://www.google.com/goto?url=CAESjwEBxCJF1zEC0bwrmVdpzVKaJldXBQ6SO5IMZuMxnrYGXDfL8AHw-hdIY9u1bzYm3AaUST41rMJXXhqTHZerOVqYCNB95aHFvOwF4bRD-DjTuCXNz7Djq-0A_Lc4NtYYXmZag_I03ufzLQchJKZ7kLBB_E229fronmj_WUDNdX3CHv09BGAodGkoJpNposq6Xg&gsessionid=iqQLgKlFOm4j6KgUYk09qNZNPqZ-xZDrd5fcg-GWdVf5uLF530KbjA)  
  <sub>The Motley Fool, 22 hours ago</sub>  
  Anthropic (ANT +17.07%) successfully debuted on the stock market Nov. 19, with shares beginning trading on the Nasdaq just before noon Eastern time at...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.80</summary>

_Not available today._

</details>

<details><summary><b>Price and chart</b> — score -0.60</summary>

```text
Last close 496.00 (bar of 2026-11-20), from 502 daily bars
Trend: vs 20d SMA 523.53 (-5.3%), 50d 520.07 (-4.6%), 200d 443.69 (+11.8%); 50d above 200d
Momentum: RSI(14) 38.4 | MACD -5.129 vs signal -0.591 (histogram -4.538)
Returns: 1d -0.5% | 5d -5.3% | 1m -4.8% | 3m +1.8%
52-week range: 352.83 - 555.80 (now 70.5% of the way up)
Volatility: ATR(14) 15.32 (3.1% of price) | annualised 20d 37.5%
Volume: 0.15x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.50</summary>

```text
Sector: Technology / Software - Infrastructure | market cap 3.68T
Valuation: trailing P/E 25.89 | forward P/E 20.50 | P/B 7.83 | PEG 1.50
Profitability: profit margin 41.2% | operating margin 47.1% | ROE 34.2%
Growth (YoY): revenue +18.8% | earnings +32.3%
Balance sheet: debt/equity 28.5% | free cash flow 2.99B
Risk: beta 1.04 | short interest 0.8% of float
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

<details><summary><b>What analysts and big funds say</b> — score +0.70</summary>

```text
Consensus: strong_buy (mean 1.38 on a 1=strong buy to 5=strong sell scale, 54 analysts)
Ratings: 12 strong buy, 41 buy, 5 hold, 0 sell, 0 strong sell
Price target: mean 636.12 (+28.3% vs last close), range 440.00 - 870.00
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

<details><summary><b>Buying and selling by company insiders</b> — score +0.30</summary>

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

<details><summary><b>Who is positioned how</b> — score +0.30</summary>

_Not available today._

</details>

<details><summary><b>Money going into and out of this fund</b> — score +0.30</summary>

_Not available today._

</details>

### Caterpillar (CAT) · Company — BULLISH, confidence 0.55

**Result:** REJECTED · no room under the sleeve budget limit

**In the model's own words:** no explanation. It wrote only “BUY”, so the main reasons below are all it gave.

**Main reasons it gave:**
- Q3 earnings beat expectations ($7.20 EPS, $20.7B revenue)
- Analyst consensus buy with mean price target $807 (+53% upside)
- RSI 25.8 indicates oversold condition despite downtrend
- Strong fundamentals: ROE 56.1%, profit margin 15.2%, revenue growth 17.3% YoY

<details><summary><b>News</b> — score -0.20</summary>

- [The cat came back: Roaring Kitty tweet sends GameStop stock higher amid GTA VI fervor](https://finance.yahoo.com/markets/stocks/article/the-cat-came-back-roaring-kitty-tweet-sends-gamestop-stock-higher-amid-gta-vi-fervor-184220345.html)  
  <sub>Yahoo Finance, 20 hours ago</sub>  
  Influential investor Keith Gill, also known as Roaring Kitty, has returned, and GameStop (GME) shares are rising after the meme stock trader who made...
- [Unusual Machines Rallies 7% on Oppenheimer's $30 Target; Red Cat Falls 7% in Extended Post-Earnings Rout, Ondas Holds Steady](https://247wallst.com/investing/2026/11/19/unusual-machines-rallies-7-on-oppenheimers-30-target-red-cat-falls-7-in-extended-post-earnings-rout-ondas-holds-steady/)  
  <sub>24/7 Wall St., 23 hours ago</sub>  
  Small drone stocks are splitting into two camps, and the line runs between the parts suppliers and the system builders. Unusual Machines (NYSEAMERICAN:UMAC)...
- [Caterpillar (CAT) Isn’t Just a Bulldozer Stock Anymore, and Ken Fisher Knows Why](https://www.google.com/goto?url=CAESmAEBxCJF1x0fpELtIQf6RSBHc06hVZxgLMBlO-S6b37BXygDuiq9Hb10AhFM_75anb9PYI7cCLRB7iPUJTzfFOustxG-IJ6LfPJd-DGu-TvKyNm0LmbjFNXKlK1SXg1coFLEN862rUNNPZkLL5EliNJmtvaWo9SktmAq_Z0fmJ-8VnCf5WnjWg_WKpaYUDHYXZfgftJNYTboaw&gsessionid=snjVGoQbmZdN-aac90egznjPhGZTHVrKYXOW5Hzq0rNU37J1Bvy8Og)  
  <sub>Yahoo Finance, 20 hours ago</sub>  
  Caterpillar Inc. (NYSE:CAT) landed 8th in our new ranking of the Top 10 Stocks to Buy According to Billionaire Ken Fisher. Ken Fisher has spent more than...
- [Caterpillar vs. Deere: Which Heavy Equipment Stock Should You Bet On?](https://www.google.com/goto?url=CAESqAEBxCJF115F2gQaHuYYPHYA5BROOGytpwpiYT5UblnckU1Bc4Sl4pqiAHb44XOaBDyOw6fl3pzY1r0WaXLUoqtIubqgCwTwfIg01PhynnJorjoEzmCStt6DimRL74OtTvuH081JrMbY5tQR5t2EfdJldDbBsSVMiH1uW6wGPN8znJHBE6K-w_CZKsBKKrSFKFlbW939RYjphtReqQaqCjbCKO5LioZjmSM&gsessionid=snjVGoQbmZdN-aac90egznjPhGZTHVrKYXOW5Hzq0rNU37J1Bvy8Og)  
  <sub>Zacks Investment Research, 23 hours ago</sub>  
  DE edges out CAT as the better heavy equipment stock, backed by improving earnings prospects, upward 2027 estimate revisions and strong share gains.
- [Roaring Kitty is back on X with a 'Cat Mario' post, and GameStop stock edges up on GTA 6 day](https://www.google.com/goto?url=CAESpQEBxCJF11jbugB9MNn4tfFUhHOBeri-JIhHrfKrRzSfeeUhSahB78vPy6IUN9n8n6uQW408YcXhnWziQK8rWFhguLJGRxPsjA-t4DB_asfxmgFbooMEwMvDo1g2y3e8pgCTlSHr-g-jX7MxxUkbKSiTFPU8-e1uAIDliEj3TeBhtia_uOD1yD2buQrp5bj2NpIh6EPkED9IEu_iLNxIMGQ8xTEYePw&gsessionid=snjVGoQbmZdN-aac90egznjPhGZTHVrKYXOW5Hzq0rNU37J1Bvy8Og)  
  <sub>Nacionale, 18 hours ago</sub>  
  Keith Gill posted a Cat Mario image on X on Thursday, November 19. GameStop shares rose a few percent. What he posted and what it means so far.
- [Caterpillar stock hits 52-week low at 537.0 USD](https://www.google.com/goto?url=CAESowEBxCJF15Sd3rgt04Yt33fO8X67bKw-XgeUyCMQnhxPHsAID99EHRKW6XV4ne5UxPn37_wT3LiGHScv0_pAO3-vB-XOdcCFhXarEwkmqEfodQdwsXQD52b2AjCvkUMPxltTyGrcwSHzYbdePKcPOxk95uQlpHD59m6VqvTSKbjoJ_kjExUYVzzEQG5_XVTPdHMNYFAhDs8mIZOCvveVG2Ai2QZy&gsessionid=snjVGoQbmZdN-aac90egznjPhGZTHVrKYXOW5Hzq0rNU37J1Bvy8Og)  
  <sub>Investing.com, 22 hours ago</sub>  
  Caterpillar Inc.'s stock reached a 52-week low, hitting 537.0 USD, amid a challenging year for the industrial giant. The decline has been particularly steep...
- [Caterpillar Inc Stock (CAT) Moved Down by 3.78% on Nov 19: Key Drivers Unveiled](https://www.google.com/goto?url=CAESjwEBxCJF1w73LehcvOrzXP4Wu2vwKHFLOlRnTzGfFDOfJwlPCq23GQyMi4X2phBG71PMO-IfL4xYV4nFB8-0u1BCtnN4hmcgqCD6xAoIBJFTR366xGeFnvkKZZ9yaoGROFtJmnK-htz-tn6IemyFSEa1YpKIqjL417Aton7oth1gCTuaiNtJDTp_i7yo0r4muA&gsessionid=snjVGoQbmZdN-aac90egznjPhGZTHVrKYXOW5Hzq0rNU37J1Bvy8Og)  
  <sub>TradingKey, 21 hours ago</sub>  
  Caterpillar faced downward stock pressure from macroeconomic headwinds and cyclical profit-taking.Sluggish global manufacturing and high borrowing costs...
- [Dow Jones Decliners: UNH, NKE, CAT Lead Today's Session](https://www.google.com/goto?url=CAESogEBxCJF1zrgPDBiVz0qrKLY1nWyMRNQH-v_AZsQOP9saNpw5oT3_di3DsyipMuuuwD-dd41pDXp4uweXcQWa1d6rZ44NNE7xewjMGddw7h0hMybSsus71z890g1f5HN9t3ebTNi6fMn_1GjamxDeY34EJNossXAnEfxRrBxK089f0vV_MeE4jmFb3X89oP8AgADkjML0UV7YybXJKHDwae9AEU&gsessionid=snjVGoQbmZdN-aac90egznjPhGZTHVrKYXOW5Hzq0rNU37J1Bvy8Og)  
  <sub>ChartMill, 21 hours ago</sub>  
  Dow Jones decliners in today's session include UnitedHealth, Nike, Caterpillar, Merck, Visa, Coca-Cola, Goldman Sachs, Honeywell and Johnson & Johnson,...
- [Caterpillar posts strong earnings and rising inventories: Can CAT recover from recent losses?](https://www.google.com/goto?url=CAESmgEBxCJF10SLkC676vGm9psBwHAwhmtnL_lgoXbzsUabing2htgc4wQBynFlf_Q5OOzvpGwd2q-TJxst4bqtlzJFcNqIejUzuRGmevzeu01iBw3Ex37AgmM_t7DQlsAO3ZhWh9Vx_k5jwoXYNt8L41VHjeHjwRh5dLltnx7FFw1H75Ubv5LcYf4XXosKv9GMc1GbU-LBgG5ra3Bo&gsessionid=snjVGoQbmZdN-aac90egznjPhGZTHVrKYXOW5Hzq0rNU37J1Bvy8Og)  
  <sub>Traders Union, 21 hours ago</sub>  
  Highlights. Caterpillar delivered third-quarter adjusted earnings of $7.20 per share and revenue of $20.7 billion, exceeding analyst forecasts.
- [GME Stock Rises Overnight: Roaring Kitty’s Return After Nearly 2 Years Flips Retail Sentiment Bullish Amid GTA 6 Frenzy](https://www.google.com/goto?url=CAES8QEBxCJF1-Var8GFESRGCVomekexRmmOlNcvfSZilyJtbbEtVESAv_71J7i9VvrX9Lq5S62dZI-nsuds2_k0HH9ilvLlfVmZiKVEAvx1Yrt_2nDlZadTaTf17UOUtAsy9uJ_izffDvI4gy8y66O6vAvqsAU7MBxeeU9OWjrHPWgLelP21uTyplEwkUCekm5Os4YXxRQSHVkhAB0Ios3i_MLX-BHyPzXFKOLbELt9FOFiQe9CQdmK9wQUvo1EeB0UeuZOGU_bICb_H1PtgrV4aSSTY476ttVC9jdUxgMJE0Sgi1vkSwKE-TvefGxnmrk2k-FX&gsessionid=snjVGoQbmZdN-aac90egznjPhGZTHVrKYXOW5Hzq0rNU37J1Bvy8Og)  
  <sub>TradingView, 12 hours ago</sub>  
  GameStop Corp. (GME) stock edged higher overnight after Keith Gill, better known as Roaring Kitty, returned to X with his first post since January 2025.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score -0.20</summary>

_Not available today._

</details>

<details><summary><b>Price and chart</b> — score -0.50</summary>

```text
Last close 527.28 (bar of 2026-11-20), from 502 daily bars
Trend: vs 20d SMA 604.27 (-12.7%), 50d 714.55 (-26.2%), 200d 804.15 (-34.4%); 50d below 200d
Momentum: RSI(14) 25.8 | MACD -49.084 vs signal -48.149 (histogram -0.935)
Returns: 1d -1.9% | 5d -12.2% | 1m -25.1% | 3m -35.0%
52-week range: 527.28 - 1,064.90 (now 0.0% of the way up)
Volatility: ATR(14) 27.62 (5.2% of price) | annualised 20d 59.5%
Volume: 0.11x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.50</summary>

```text
Sector: Industrials / Farm & Heavy Construction Machinery | market cap 241.28B
Valuation: trailing P/E 20.69 | forward P/E 16.39 | P/B 11.23 | PEG 0.94
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

<details><summary><b>What analysts and big funds say</b> — score +0.60</summary>

```text
Consensus: buy (mean 1.97 on a 1=strong buy to 5=strong sell scale, 26 analysts)
Ratings: 2 strong buy, 15 buy, 11 hold, 1 sell, 0 strong sell
Price target: mean 807.26 (+53.1% vs last close), range 575.00 - 1,027.00
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

<details><summary><b>What analysts say about what this fund holds</b> — score +0.60</summary>

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

### ASML (ASML) · Company — BEARISH, confidence 0.45

**Result:** REJECTED · no room under the sleeve budget limit

**In the model's own words:**

> Mixed news but no catalyst; technicals show strong bearish trend (price far below SMAs, RSI near oversold, thin volume); fundamentals and earnings record are strong but are longer‑term drivers; analyst consensus remains bullish but already priced in. Short‑term outlook leans lower.

**Main reasons it gave:**
- Price 6% lower, trading well below 20‑day, 50‑day, 200‑day SMAs (-12.6% to -18.5%)
- RSI 30.8 near oversold, volume 0.2× 20‑day average (thin trading)
- Strong fundamentals: profit margin 34%, ROE 65.6%, revenue growth +55% YoY, forward P/E 20.6, PEG 0.74
- Earnings record: 3 beats (last beat +17%) vs 1 miss
- Analyst consensus strong buy, mean price target +61.6% vs last close

<details><summary><b>News</b> — score +0.00</summary>

- [Why Is ASML Stock Falling, and is it a Buying Opportunity?](https://www.fool.com/investing/2026/11/20/why-is-asml-stock-falling-and-is-it-a-buying-opportunity/)  
  <sub>The Motley Fool, 3 hours ago</sub>  
  When our analyst team has a stock tip, it can pay to listen. After all, Stock Advisor's total average return is 790%* — a market-crushing outperformance...
- [Why is ASML stock sliding today?](https://www.investing.com/news/stock-market-news/why-is-asml-stock-sliding-today-93CH-5041123)  
  <sub>Investing.com, 4 hours ago</sub>  
  Investing.com -- Shares of ASML fell 6.0% to trade at €1,211.2 on Friday, pulled down by a sweeping global selloff in AI-exposed technology stocks that...
- [ASML Dec 2026 1340.000 call (ASML261211C01340000) Stock Price, News, Quote & History](https://www.google.com/goto?url=CAESdAHEIkXXJeUBVD4KIzQafvNc6UvnhmJR71WKFWYKWISeUIVCtoPgQ0ZgphlT0YgVeO7kI6PchJouABAD6QmoUudnDc8kfL03MSs4QWgUUK5EE5h_GweKq6j2jwfBl1POo3vRDzxGhFkXskUnTTay4xgW7RZ3&gsessionid=7-v1CJetAqigMOGKtz7IzLX5cpMblzeZNIXdHnKjEHdWeHteekr_ng)  
  <sub>Yahoo! Finance Canada, 4 hours ago</sub>  
  Find the latest ASML Dec 2026 1340.000 call (ASML261211C01340000) stock quote, history, news and other vital information to help you with your stock trading...
- [ASML is down 30% from its high 🔥 What's next? ❓](https://www.google.com/goto?url=CAESoAEBxCJF18cgrrSP9gNcTpss2i3Wk4bDTDaS4uD-vd5WaEEbMsX1NSyT6HzhDe46bgc6ndwj_KQ_9ClV-YfvWHxT_0H8WWWu6nqkxDOY5q39avnMGCBCuuYnWsFAh99zEJSOfY-Zcxz_SD1bctneuNoYwS71Af5mh6BPIJHSa2LEC43b0vorNX8miJPfz1ve5SyvJ_cednjPNC4jkDLeVT8W&gsessionid=7-v1CJetAqigMOGKtz7IzLX5cpMblzeZNIXdHnKjEHdWeHteekr_ng)  
  <sub>XTB.com, 2 hours ago</sub>  
  Shares of the Dutch lithography systems manufacturer (ASML) are down more than 6% today, falling to around 1209 EUR and leading the declines among European...
- [ASML Rides on Improving Profitability: Will It Sustain?](https://www.google.com/goto?url=CAESqgEBxCJF1xSwU7gV2zVXtdipmhnSem2v95hUx8JbYjk2-bxYmtzR6uVRQODqhevivcuJ7L9EEq1LKVXSLjAW70f7Y7NFNEiLaFM9DMs5HkXxtdhKTTqnJiSW9ijOfVvRTP5FdYfj2hQfH9yU5TLIRbPZTNsPCTynaqp8gZvpQB5d_DJTGSVRtg_msqLc4FL1K6VkMDJni_KyqB6ZDUBBeqcb2OHzXTXu23z50w&gsessionid=7-v1CJetAqigMOGKtz7IzLX5cpMblzeZNIXdHnKjEHdWeHteekr_ng)  
  <sub>TradingView, 22 hours ago</sub>  
  ASML Holding N.V. ASML is witnessing a significant improvement in profitability. The company reported third-quarter 2026 total net sales of €11.66 billion,...
- [Why Ken Fisher Keeps Adding to ASML Holding (ASML) While Its Order Book Is Sold Out](https://www.google.com/goto?url=CAESmQEBxCJF11W_ntW96Moxgw7mJkWmfPGUt3HZy_O9g8kvhNWBeH6AgguutCF0-lDq7ourKuuhR8wmfM51a1GcjcOUrrUPz47OUiwquw8jR_1F93JHNrZyBKaHyZ3r1UOHiz9hVnYp2ZKuJr0It1nGSDhZ7ZDG-RbLWj-61FVmbNlGfGFt2NUIt3wSVVkDdNefOkSU-IXPjyibtT8&gsessionid=7-v1CJetAqigMOGKtz7IzLX5cpMblzeZNIXdHnKjEHdWeHteekr_ng)  
  <sub>Yahoo Finance, 21 hours ago</sub>  
  We just published our list of the Top 10 Stocks to Buy According to Billionaire Ken Fisher, and ASML Holding N.V. (NASDAQ:ASML) ranked 6th on this list.
- [Behavioral Patterns of ASML and Institutional Flows](https://www.google.com/goto?url=CAESwgEBxCJF194eHr_K5MQySAjSSb6q2MLMOCmuzVStsP-seK7O_ZiKzU0wo3F8wUgiR6U4HVG3BIOxC-o2J8VC0zOs8pL37iW4UKre52ety04q-PPuIaOn59fYGPJYfK1JxYZfx7qd5jIDsaGnfrIFCszBwHmVQj_uQkNM1ctslk6vvoJmz6NNkqmb9myFWggp2aoh_-bH3zRSpruzGp4r7m5APobTxCwxiq1pW41o7rKghG6SwngdDzO4H8jvO-rInq4n9A&gsessionid=7-v1CJetAqigMOGKtz7IzLX5cpMblzeZNIXdHnKjEHdWeHteekr_ng)  
  <sub>Stock Traders Daily, 17 hours ago</sub>  
  Key findings for Asml Holding N.v. (NASDAQ: ASML). Weak Near and Mid-Term Sentiment Could Challenge Long-Term Positive Outlook; No clear price positioning...
- [European stocks close about 1% lower as SAP and drugmakers fall on Anthropic debut day, while ASML gains](https://www.google.com/goto?url=CAESrQEBxCJF19pgbkKNCzr5vMin1XmlzUiJ0hSd4Fg6T8aZBaD3iEssr7YIWwYjRQX5j5UfU9rv2EUpDv-WqlgSxQfCEUGmvkiwNbpvaPpEIBa8iid_36sXbLFjBJFCVK_2PeCcL114ZCDsRgjqTi3onN_J_vZdYgcACuXwpoIAZcpJu2LaUOT2IXQHUUEUgPQS0pNesekSf27NXlEzTD0kQOw27HWyw0AAJQoKw1rlhA&gsessionid=7-v1CJetAqigMOGKtz7IzLX5cpMblzeZNIXdHnKjEHdWeHteekr_ng)  
  <sub>MLQ.ai, 20 hours ago</sub>  
  European stocks closed lower on Thursday, Nov. 19, after an early rebound faded. The STOXX 600 fell 0.88% to 638.41, Germany's DAX 1.06% to 25463.81,...
- [Jensen Huang Stepped Away From Nvidia. The Stock Has Crashed. Instead of Rushing to Buy the Dip, Here Are 2 AI Stocks Down More Than 15% to Buy Instead.](https://www.google.com/goto?url=CAES_AEBxCJF16r2kptkJUuJIB3BEHBl-awt0WZAxOmTrx62Vf8pIuhWdj3h8l87hsY2Z4VlvxrRaTfLVeY2_k6OdC79INRnyuWXHHk2xmIH1ih7Jo5Osm511z43yHWI8mL0VVwDN6Ag7GcNaUrkmPJF66RN-5zsXbN6W5-swj70iW0fDcwBJE45Pq18FZXSxhz2N8OgRpgYw1lpjHOZTvDdttbayVRt3ybYlpaUl3vExnMpS7bTJhjm50d_iL5RdpU_uw_i-EXlu8XBl3KLTUMctPnBy0XiCzhFvOCh7Uv8AtmUIQkrFafh8tVf9YoEksyRFpzJRTi5QwAOweiN9ic&gsessionid=7-v1CJetAqigMOGKtz7IzLX5cpMblzeZNIXdHnKjEHdWeHteekr_ng)  
  <sub>The Motley Fool, 24 hours ago</sub>  
  Nvidia (NVDA -3.30%) investors have learned a quick lesson in downside risks. Investors couldn't have predicted that the founder and CEO would abruptly...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

_Not available today._

</details>

<details><summary><b>Price and chart</b> — score -0.60</summary>

```text
Last close 1,305.45 (bar of 2026-11-20), from 502 daily bars
Trend: vs 20d SMA 1,494.08 (-12.6%), 50d 1,625.53 (-19.7%), 200d 1,601.70 (-18.5%); 50d above 200d
Momentum: RSI(14) 30.8 | MACD -78.380 vs signal -65.759 (histogram -12.622)
Returns: 1d -3.7% | 5d -12.7% | 1m -16.3% | 3m -25.0%
52-week range: 966.57 - 1,989.44 (now 33.1% of the way up)
Volatility: ATR(14) 65.27 (5.0% of price) | annualised 20d 61.4%
Volume: 0.20x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.70</summary>

```text
Sector: Technology / Semiconductor Equipment & Materials | market cap 503.14B
Valuation: trailing P/E 32.12 | forward P/E 20.59 | P/B 1,120.92 | PEG 0.74
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

<details><summary><b>What analysts and big funds say</b> — score +0.50</summary>

```text
Consensus: strong_buy (mean 1.37 on a 1=strong buy to 5=strong sell scale, 17 analysts)
Ratings: 7 strong buy, 31 buy, 2 hold, 1 sell, 0 strong sell
Price target: mean 2,109.83 (+61.6% vs last close), range 849.97 - 2,792.10
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

### Royal Bank of Canada (RY) · Company — NEUTRAL, confidence 0.38

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> The technicals show strong bearish signals (price below 20‑, 50‑ and 200‑day SMAs, low volume, negative MACD) while fundamentals, analyst consensus and insider buying are bullish. The news is slightly negative. Conflicting signals lead to a neutral stance with modest conviction.

**Main reasons it gave:**
- Technical indicators: price below 20‑, 50‑, and 200‑day SMAs, RSI 30.3, MACD negative, volume 0.04× 20‑day average (bearish)
- Analyst consensus: buy with mean price target +11% vs last close (bullish)
- Insider activity: cluster of open‑market purchases totaling 745 shares on 2026‑10‑30 (bullish)
- News: weak momentum, seller pressure, and inflation‑linked concerns for banks (slightly bearish)

<details><summary><b>News</b> — score -0.20</summary>

- [Royal Bank Of Canada (RY) Stock Forecasts](https://finance.yahoo.com/research/reports/MS_0P000004QB_AnalystReport_1795136071000)  
  <sub>Yahoo Finance, 10 hours ago</sub>  
  At Yahoo Finance, you get free stock quotes, up-to-date news, portfolio management resources, international market data, social interaction and mortgage...
- [Royal Bank of Canada stock outlook: Weak momentum persists as seller pressure dominates session](https://tradersunion.com/news/stocks/show/4340270-royal-bank-of-canada-slides/)  
  <sub>Traders Union, 40 minutes ago</sub>  
  Royal Bank of Canada (RY) stock is trading at C$269.45, down 1.03% on the session. The price is currently positioned below its key short- and medium-term...
- [Purpose Investments Launches Purpose Anthropic (ANT) Yield Shares ETF and Purpose Micron (MU) Yield Shares ETF](https://www.google.com/goto?url=CAES8AEBxCJF1wUCluTQl2U_Qd87JHQ3EsgmoIbo40PMqPNpJ6wbPWo4m6i4iEliKgHk7vUr7rBuRmC4kMyM375l5duqtQsyA8o5g7g34WjWticjkc36ju7Gtrj0jqToDNjicBhyw-Uua0bPE2nVybZHeDpkespE_gb7I8mXKgKYm2IHzgz93EwkoOijZxzVHZJI2DsOC852xWYKOsJM8DobZ-9-WjBeppiuSXjzmEeBrCPVCgIYl_6j1N9rHhTJjKRr9mta9QtQDkZVi3IebOh4u3AA067OteW1PzubQaiPpy1zmEaoox2L6CnlNP_RvFwfZuk&gsessionid=DjdIh43hQeOwa0wg4MooEPdEylHZFj4w1iFKVxMzBrzzbLHVkitKFw)  
  <sub>GlobeNewswire, 2 hours ago</sub>  
  Single-stock ETFs built to pay enhanced*, tax-efficient monthly income from high-growth AI names, while keeping investors meaningfully exposed to the...
- [The Toronto-Dominion Bank (TD.TO) stock price, news, quote and history](https://www.google.com/goto?url=CAESZgHEIkXXhyKBXjxQ2CwMYBkiwcwzA_bpHMg4ZpMiI937Dgkk4mUhjvCe87FX49LOy33c4xrC5pTYnyOaXnWdlJ0u2pgYqb5DBajoS3K0l6fVgsn8Q1J3ZRLcU8nS0f05U_6cj12G8A&gsessionid=DjdIh43hQeOwa0wg4MooEPdEylHZFj4w1iFKVxMzBrzzbLHVkitKFw)  
  <sub>Yahoo Finance UK, 13 hours ago</sub>  
  Find the latest The Toronto-Dominion Bank (TD.TO) stock quote, history, news and other vital information to help you with your stock trading and investing.
- [RBC Capital Markets Hosts Global Industrials Conference in New York with 90+ Companies](https://www.google.com/goto?url=CAESqwEBxCJF13pf12f8KgNdU_Guggh28vgNIMZu0WhF6TTQTg_QWQSs5yLlS0FR6Wn3i8h38TNf4dDQ0TE98VwJ-rO_rMw35ETBKXWUmvFdk9A3vywO201r7uKxpxCdZEd043nZ9BCGBgrNiUcjgxot5OhGhR6rbqs4xtsIqfm67QQx7Zr08ofaJDJQtSnB1jgG79y_KHKqeXueZrZOlmXsMgydQo1yppCrA_yPEw0&gsessionid=DjdIh43hQeOwa0wg4MooEPdEylHZFj4w1iFKVxMzBrzzbLHVkitKFw)  
  <sub>Quantisnow, 24 hours ago</sub>  
  Two-day event convenes senior management and institutional investors across aerospace, defense, chemicals, transportation, homebuilders and diversified...
- [Royal Bank of Canada (TSE:RY) Stock Gets Price Target Boost from Scotiabank](https://www.google.com/goto?url=CAESxQEBxCJF10L60QeA8pFXTfeHYPKgJNGQbuzWyKmvmZfbO1GEDOVtmcz88Ge9gLluSFfynKeNiZysf_kE4EIMw6_JNCcW4kOHNmMuBqNUFN8QYTfcH6YuZ6JDNcOFprLVHFE8UqSnFSa3bkn964l0u4yO_o6bjL5p-m70b8cdnsVk5qKT8A3Lcziijgz9FLYXODAsHzo2o1Z_-zuu82iw7wHeWmE8Q1XbAYTRHXgR3Icq_-ERDAwyhq8C-hCGZvI0-le8n4YA4Q&gsessionid=DjdIh43hQeOwa0wg4MooEPdEylHZFj4w1iFKVxMzBrzzbLHVkitKFw)  
  <sub>MarketBeat, 18 hours ago</sub>  
  Scotiabank lifted their price target on Royal Bank of Canada from C$312.00 to C$313.00 and gave the company a "sector outperform" rating in a research note...
- [Carolina Financial Advisors, Inc - Portfolio Stock Holdings](https://www.google.com/goto?url=CAESjAEBxCJF1ylvijExazFCGKT3JBrg4rfQwPRGxV_weFLmSFuyE8tjHsos4UCml2ucP31Pig49XsgO3eDFeMpCbdHdrD-Eu9tM_Gl1-F0nBhOzIHZZM_SvfOAEWvaNZF6__ASYlFdkZSc-SQoun08lYwoiAvBv_n5jfuX2KMk4z5IVhduWfMSdzUl-ZVJ78g&gsessionid=DjdIh43hQeOwa0wg4MooEPdEylHZFj4w1iFKVxMzBrzzbLHVkitKFw)  
  <sub>Quiver Quantitative, 14 hours ago</sub>  
  Track which stocks Carolina Financial Advisors, Inc is buying and selling. See stock portfolio updates, holdings by sector, and more.
- [Bank Stocks or a Dividend ETF? Where I’d Put $25,000 for Retirement Income](https://www.google.com/goto?url=CAESjAEBxCJF12eNWmLxuJ0EVltaosAGUVmerJLctL3ViTYukSNk8afSzvAxD4xkPgfHT8QAfRx2ufB9d8ViY850OSg_TJ56kPIuYg9-63kwAVTn8IiJcncyO2LodAGKg5C5I4Z2ht1PW_fg63sgpl3uAtPK5wuzUPicJHQkqq0GpjMK_Tn8kVy74rxCJH24wg&gsessionid=DjdIh43hQeOwa0wg4MooEPdEylHZFj4w1iFKVxMzBrzzbLHVkitKFw)  
  <sub>Yahoo! Finance Canada, 18 hours ago</sub>  
  Two bank stocks can pay a decent retirement cheque. I'd give the next $25000 to a dividend ETF if I already own plenty of Canadian banks.
- [Why Is Royal Bank (TSX:RY) Monitoring Canada's Economic Conditions?](https://www.google.com/goto?url=CAESqAEBxCJF1-V_ebji1jQ2v9HB7vp1DinvbNsLiftmlOqf0M5Figq2bZheYV9UfgnqdBKP1nN__RYyj1nJVaBKgGwn8AQ5w2BHbqWABhZXLhRtf63RouZkbKo0owechg04jqbDBoCYgsZ8kocpXpde9CXR-bsfCKdFPJZ_EFLQLJDSr7MtfIknBxLg2PKemVCF_L6VXaZzG4cWXgSAJNU74r1DrRqyQTKK41w&gsessionid=DjdIh43hQeOwa0wg4MooEPdEylHZFj4w1iFKVxMzBrzzbLHVkitKFw)  
  <sub>Kalkine Media, 13 hours ago</sub>  
  Royal Bank and peers slide as energy-linked inflation fears hit banks, with fiscal fourth-quarter results due in early December.
- [Canadian Market Overview](https://www.google.com/goto?url=CAESYgHEIkXXg9AnxoqRQTPogQhz9DmHTn3DAwdi47tPOXxCmGlybu_IGppxOvszfYRZ5svfypfAQwqUjXlA--A_6_TqF48eMxithv573uPYw5CEM0oBTroX4z-jbgrlZqMUgaMx&gsessionid=DjdIh43hQeOwa0wg4MooEPdEylHZFj4w1iFKVxMzBrzzbLHVkitKFw)  
  <sub>https://kalkine.ca/, 21 hours ago</sub>  
  Live snapshot of Canadian markets: trending stocks, highest volume, most volatile, top gainers and losers, plus the latest market news.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score -0.20</summary>

_Not available today._

</details>

<details><summary><b>Price and chart</b> — score -0.60</summary>

```text
Last close 187.34 (bar of 2026-11-20), from 502 daily bars
Trend: vs 20d SMA 200.92 (-6.8%), 50d 199.55 (-6.1%), 200d 191.57 (-2.2%); 50d above 200d
Momentum: RSI(14) 30.3 | MACD -2.512 vs signal -0.525 (histogram -1.987)
Returns: 1d -0.2% | 5d -7.4% | 1m -7.3% | 3m -8.2%
52-week range: 147.35 - 217.87 (now 56.7% of the way up)
Volatility: ATR(14) 3.55 (1.9% of price) | annualised 20d 23.4%
Volume: 0.04x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.20</summary>

```text
Sector: Financial Services / Banks - Diversified | market cap 259.36B
Valuation: trailing P/E 16.38 | forward P/E 14.71 | P/B 2.72 | PEG 1.79
Profitability: profit margin 33.9% | operating margin 45.7% | ROE 16.2%
Growth (YoY): revenue +8.9% | earnings +12.8%
Balance sheet: debt/equity n/a | free cash flow n/a
Risk: beta 0.92 | short interest n/a of float
Next earnings: 2026-12-03
```

</details>

<details><summary><b>What this fund holds</b> — score +0.20</summary>

_Not available today._

</details>

<details><summary><b>Does this company beat its own forecasts</b> — score +0.20</summary>

```text
Earnings record, last 4 quarters: 2 beats, 2 in line
  2026-09-30 in line | 2026-06-30 in line | 2026-03-31 beat by 3% | 2026-03-31 beat by 3%
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
Consensus: buy (mean 2.21 on a 1=strong buy to 5=strong sell scale, 3 analysts)
Ratings: 4 strong buy, 4 buy, 5 hold, 0 sell, 1 strong sell
Price target: mean 208.24 (+11.2% vs last close), range 181.75 - 229.03
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

<details><summary><b>What analysts say about what this fund holds</b> — score +0.60</summary>

_Not available today._

</details>

<details><summary><b>Buying and selling by company insiders</b> — score +0.40</summary>

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

<details><summary><b>Who is positioned how</b> — score +0.40</summary>

_Not available today._

</details>

<details><summary><b>Money going into and out of this fund</b> — score +0.40</summary>

_Not available today._

</details>

### Alphabet (Google) (GOOGL) · Company — NEUTRAL, confidence 0.35

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Mixed signals across dimensions: technicals strongly bearish, fundamentals moderately bullish, earnings record weak, news mixed, analyst view bullish but likely priced in, no insider activity.

**Main reasons it gave:**
- Technical indicators show price below 20‑day, 50‑day, and 200‑day SMAs, low RSI (34.9) and low volume (0.15× avg) – bearish
- Mixed news: AI product launch (Gemini) positive vs high‑profile investor (Stanley Druckenmiller) selling shares – conflicting
- Fundamentals: cheap trailing P/E 14.5, high profit margin 50% and ROE 44% but earnings growth negative (-25.3%) and free cash flow -$1.16B – mixed
- Earnings record: 3 of last 4 quarters missed consensus, latest miss 14% – bearish
- Analyst consensus strong buy with mean price target $400 (+44%); likely already priced in – limited incremental signal

<details><summary><b>News</b> — score +0.10</summary>

- [Stanley Druckenmiller dumps Google stock in a bid to ‘not lose money’ as the outlook darkens. Here’s what he’s buying](https://finance.yahoo.com/markets/stocks/articles/stanley-druckenmiller-dumps-google-stock-121500032.html)  
  <sub>Yahoo Finance, 2 hours ago</sub>  
  Moneywise and Yahoo Finance LLC may earn commission or revenue through links in the content below. After five decades in the investment business,...
- [Google's Gemini Tasks Seen As Challenger To Meta's Muse In AI Battle](https://www.investors.com/news/technology/google-stock-gemini-tasks-challenger-to-meta-muse-ai-agent/)  
  <sub>Investor's Business Daily, 1 hour ago</sub>  
  Alphabet's release of a personal AI agent will challenge Meta's Muse and should provide upside for Google stock, says JPMorgan.
- [Cramer: My favorite chartist sees two major signs of a rally brewing in Alphabet stock](https://www.google.com/goto?url=CAESjAEBxCJF126IMzPM7CoOHiCFxxhMWn6GDDvfqjf6E0AuNm3IORNq3Ofj5PbaVXOKtCPO0RFIkNJ6xMDALIKkqZ7QT5A7QebZjp7hQL3Wmn2Zj0V-Z_44gFoXEAPxK9klgLkNeQYMIIhyMXZOLNz-NRJwPA4V_ZogzkOB-maZv_mYDnMKXWHxfW4RTznKuA&gsessionid=7yQ5j-yeulsiBxXyFEx29BaaQ32tSymJQsJN7Q6i560TqUft1RaZpQ)  
  <sub>CNBC, 15 hours ago</sub>  
  CNBC's Jim Cramer said that veteran chartist Larry Williams believes Alphabet shares look ready for a rebound. Williams' analysis of both the fundamentals...
- [Google Stock Is Back Near Its 2025 Bottom Valuation. Can It Rebound Again?](https://www.google.com/goto?url=CAESdgHEIkXX_ViUZOvjqTpQoEFtBfIlT-v2THFb8QHzvAzqlpP6ec-77iEn1XLGAX7LVxw3eh-tCaQdZ0fa5boyjtSO1Oh5e0FOPU4yu8vgbkEjQfaRpm-6gwdoa7jOKqCj8EF5NBGovKlTMa1hNmQUZwwJOQdnbEY&gsessionid=7yQ5j-yeulsiBxXyFEx29BaaQ32tSymJQsJN7Q6i560TqUft1RaZpQ)  
  <sub>BeInCrypto, 6 hours ago</sub>  
  Google stock trades near 15 times earnings, close to its spring 2025 valuation low, as Alphabet's AI spending climbs.
- [Alphabet: A 30% Decline From All-Time High Is Probably Not Enough](https://www.google.com/goto?url=CAEStAEBxCJF1xLp75EVWtvMBs7L_6so60mUVt3QPh6bEDNl1Yg4P0EhG9XVNN7G98TwpvwfrOEU9vRad24tYcbrM6r88C7SKCZyde-g3wSpYJPh8BBbGyJ9FYmkqpeL7OiGhiJpwxJ5n4TsgmfnAaXOf-zsDmB-MjeuLs5DphapMMk94dDYJEjaeaGGCACWM5k_Q9xaNOhVdWblqkty2gwaaJAhuMsdG4fmSRhvX945d_2E6kIyraA&gsessionid=7yQ5j-yeulsiBxXyFEx29BaaQ32tSymJQsJN7Q6i560TqUft1RaZpQ)  
  <sub>Seeking Alpha, 4 hours ago</sub>  
  Summary. Alphabet delivered strong Q3 results, with revenue growing 24.7% year-over-year and Google Cloud revenue surging 102.7%, but earnings per share...
- [Stock Market Today, Nov. 19: Alphabet Shares Fall as Anthropic Nasdaq Debut Puts Fresh Value on Google's Stake](https://www.google.com/goto?url=CAES5AEBxCJF11QMgohU515oFWySfYBswzqZPko-oxHG8R09LiCLz3SW_7KggHDscOcJsjYCpmaBdEWItwTETjsK8xyBUMS--l-FrN5qLU7hzqk47w1DtkX2EfiYiKl87T61LorTqnp6gNPaSDEI7mBL3bEgGONiClaSMThmuR5INjg1-Rd3A0cYMFhHcNuJZF17z5KTKuQ2IFZwRq-tQpUkXqvnsy0HGYMC0UwimTqgwyFU_A_UY8ovG9e2TUtd42N-1DOUJzoJSGhBH0UfLP7QGLsE1W4BygsumtoG33a0js8mnFtfdKw&gsessionid=7yQ5j-yeulsiBxXyFEx29BaaQ32tSymJQsJN7Q6i560TqUft1RaZpQ)  
  <sub>The Motley Fool, 17 hours ago</sub>  
  Today, Nov. 19, 2026, Alphabet's slide came as investors weighed its private AI holdings and a heavy trading session.
- [Alphabet Stock Is Jumping. 2 Reasons the Comeback Starts Now.](https://www.google.com/goto?url=CAESgQEBxCJF15CvLhw1uT6XTx1mKW1zP9lan_S2OehcukGyfSaArAzG2L8xSXAgooBbRRmcSB8_A20kcKQlIt-n9I6vns2lPZoJd7kkGVbmjgYl69PD3SXfCULkIB-gXEymI4yoTZp33CFwYfmSqfEMSY27yPwZNid5TKWnRxYVqEi2Pes&gsessionid=7yQ5j-yeulsiBxXyFEx29BaaQ32tSymJQsJN7Q6i560TqUft1RaZpQ)  
  <sub>Barron's, 24 hours ago</sub>  
  Alphabet stock rises as investors get excited about Anthropic's trading debut, which stands to net Google $149 billion.
- [Why did Alphabet stock fall on Anthropic's IPO day? Google's big stake was mostly priced in](https://www.google.com/goto?url=CAESqgEBxCJF1-ihPdGAWwzsrJaJ9XfHxCr-wcRdkNaAT9mgmu51iiBNt1h_j-9rIziPwcv_xPqDlztDLCTE1uNgaVH-kK2fm0Ovxb6ZW_r6rW-xDajswVe3wOi6YNodtgLsHDWPCfDceJnFTIqVrcy3BFRhF3zVUYAwqZO8b6IV1nFoRkmrIKgLC8n0M9l7O_8sOipvhkly7zPxenWmVHJT79Bua6Sg04sMIXwGcQ&gsessionid=7yQ5j-yeulsiBxXyFEx29BaaQ32tSymJQsJN7Q6i560TqUft1RaZpQ)  
  <sub>Nacionale, 12 hours ago</sub>  
  Google owns about 13-14% of Anthropic, worth roughly $170 billion at Thursday's close. Why Alphabet still fell 3.5% on the IPO day.
- [Are You Overpaying For Alphabet Stock Versus Its Tech Rivals?](https://www.google.com/goto?url=CAEStgEBxCJF1_jTUWgl-XVkOovCYeeIdPihd--jAIGI35eSF3l4XNS3EtyInq8dTT4-xQ4Gh74Rn7Obru53oX4CqcWUuWgBy4SK9B2LxhtkUmKpU1v5PFHhwCNXAMBvGaBzDThj0xts1DfI4P8vLqO8jWx6o851mcErKz9QNW2NZVOTmcMMimlGA69X-ahDvJOFiZsf9mXFohA9J46Duso-7MwAKPQNVRU2zMRKQnBKz8EmD0fLWwvpQg&gsessionid=7yQ5j-yeulsiBxXyFEx29BaaQ32tSymJQsJN7Q6i560TqUft1RaZpQ)  
  <sub>Trefis, 21 hours ago</sub>  
  Today's big story: Could Anthropic Stock Fall 25%? Alphabet (GOOGL) has the lowest price-to-earnings ratio among six large tech...
- [Google’s SpaceX Stake Lost More Than $10 Billion in Value Last Quarter While Its Share Count Edged Up](https://www.google.com/goto?url=CAESzAEBxCJF14Xu_StmafP14PpnqDdUfKvikIYnVs88Rw6tXtJFyF7Ela210YAoyHpJjZcs11XU7r3WfGVkID1PLlUo-k0yQxcyWsJe_AHmzJvwZwEh_g5-Ix0VPrf_3B137FALxqKdrdULgMJnIJtKVHbK1lYK_mOfppLYB2mat8wb5MyOVhUMibdViHxLhXwUXvuC5mgypLb_7lEG-7keq3WXlqGZkz_MM9cz4NnlEw4K5Sd5Ltgni6eLSAr8D78OU8BBo_w0ISQIRsNkkfQ&gsessionid=7yQ5j-yeulsiBxXyFEx29BaaQ32tSymJQsJN7Q6i560TqUft1RaZpQ)  
  <sub>24/7 Wall St., 17 hours ago</sub>  
  The third-quarter 13F from Alphabet (NASDAQ:GOOGL | GOOGL Price Prediction), covering positions as of Sept. 30 and filed Nov. 6, shows its stake in SpaceX...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.10</summary>

_Not available today._

</details>

<details><summary><b>Price and chart</b> — score -0.70</summary>

```text
Last close 277.49 (bar of 2026-11-20), from 502 daily bars
Trend: vs 20d SMA 290.06 (-4.3%), 50d 322.54 (-14.0%), 200d 337.03 (-17.7%); 50d below 200d
Momentum: RSI(14) 34.9 | MACD -12.617 vs signal -12.866 (histogram 0.249)
Returns: 1d +1.8% | 5d -6.2% | 1m -14.4% | 3m -20.3%
52-week range: 272.66 - 402.62 (now 3.7% of the way up)
Volatility: ATR(14) 10.38 (3.7% of price) | annualised 20d 53.7%
Volume: 0.15x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.30</summary>

```text
Sector: Communication Services / Internet Content & Information | market cap 3.41T
Valuation: trailing P/E 14.49 | forward P/E 18.14 | P/B 5.17 | PEG 0.96
Profitability: profit margin 50.0% | operating margin 33.3% | ROE 44.3%
Growth (YoY): revenue +24.7% | earnings -25.3%
Balance sheet: debt/equity 22.2% | free cash flow -1.16B
Risk: beta 1.23 | short interest 1.5% of float
Next earnings: 2026-10-28
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

<details><summary><b>What analysts and big funds say</b> — score +0.20</summary>

```text
Consensus: strong_buy (mean 1.34 on a 1=strong buy to 5=strong sell scale, 53 analysts)
Ratings: 10 strong buy, 43 buy, 5 hold, 0 sell, 0 strong sell
Price target: mean 400.15 (+44.2% vs last close), range 300.00 - 500.00
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
(3 grant/option/gift transaction(s) excluded — compensation, not a view on the price)
```

</details>

<details><summary><b>Who is positioned how</b> — score +0.00</summary>

_Not available today._

</details>

<details><summary><b>Money going into and out of this fund</b> — score +0.00</summary>

_Not available today._

</details>

### Novo Nordisk (NVO) · Company — NEUTRAL, confidence 0.35

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> The news includes a material catalyst (positive weight‑loss data) and a bullish analyst note, but technicals are clearly bearish (price below SMAs, negative MACD, very low volume). Fundamentals are solid but growth is weak, earnings record is mixed with recent misses, and analyst consensus is hold with recent downgrades. No insider activity. The contradictory signals lead to a neutral stance with low conviction.

**Main reasons it gave:**
- Positive weight‑loss data reported (bullish news)
- Price below 20‑day, 50‑day, and 200‑day SMAs (bearish technicals)
- Very low trading volume (0.09× 20‑day average) indicating weak participation (bearish technicals)
- Mixed earnings record: 2 misses, 1 beat, 1 in line (slightly bearish earnings)
- Consensus hold with recent downgrades (neutral/weak analyst view)

<details><summary><b>News</b> — score +0.50</summary>

- [Forget the Headlines: Novo Nordisk's (NVO) 4.6% Dividend Yield Is the Real Story for Patient Investors](https://www.fool.com/investing/2026/11/20/forget-the-headlines-novo-nordisks-nvo-46-dividend/)  
  <sub>The Motley Fool, 1 hour ago</sub>  
  There are exciting headlines galore regarding Danish healthcare company Novo Nordisk (NVO -1.42%): "Novo Nordisk Shares Rise on Positive Weight-Loss Data,...
- [Novo Nordisk A/S (NVO) latest stock news and headlines](https://au.finance.yahoo.com/quote/NVO/news/)  
  <sub>Yahoo Finance Australia, 23 hours ago</sub>  
  Novo Nordisk A/S (NVO).
- [Objective long/short (NVO) Report (NVO:CA)](https://www.google.com/goto?url=CAEShwEBxCJF1zbhpXZIKRaDRI0T5pfhBf790y5RCFQXbnNzi9vuhPWCKxxavfEG8Afodb23-z_QAfte7jRNJTePJDNTVdqRy1FpQ3XEl_3a70pmUZ4ie86nUDHkJUGyJNPJYGw2OilT6h6g7KE0f0-hj6i7V4byhu1KQXCFPqlPyOSNDvVJ_GndnS8&gsessionid=k0j4AbbZYTxtZmQd028RiASvLBWYDx2nTDps85QBh0bqYjQ-wjuxQA)  
  <sub>Stock Traders Daily, 2 hours ago</sub>  
  Trading Report for Novo Resources Corp. NVO With Buy and Sell Signals.
- [Novo Nordisk: A Return To Growth May Be Just Around The Corner (NYSE:NVO)](https://www.google.com/goto?url=CAESowEBxCJF1-2GvX8AipkovGJsY-TSH1foWX2zHJNLYg59afM9Q-B27nb7duE6QTfeb8N7-echXWKIhS6QE5jLkB9StO2WOlewN90NVY7O3yoFDfUGUTWDEp6l4_drUGqU1zb4VTQ5q7aFiBDsBgn6j_L9F_dhwQ5DujkQ9YA4P5ReLKx9eUa7KV7KucHvyMjexesNw1HeMS44IGWj3Y0hLhZJirYk&gsessionid=k0j4AbbZYTxtZmQd028RiASvLBWYDx2nTDps85QBh0bqYjQ-wjuxQA)  
  <sub>Seeking Alpha, 15 hours ago</sub>  
  Analyst rates Novo Nordisk A/S a Buy, calling its 10–11x forward P/E inexpensive; stronger-than-expected 2027 guidance could restore momentum.
- [NVO slides as weak momentum and sellers dominate intraday trading](https://www.google.com/goto?url=CAESlQEBxCJF18hi9z5bPc_BLeO7MdUEyDahCaS5Jv_m2RFHQn7g-kmzBbEs6kkmWTO16bVqAqCRAob0VFDC8RGMr5k_uiVgaA3o0CRGh4ihXLPg2xM2amU7YNWVxygczaW_veWmmGiwR4FwNOh6V-Wc0--R7g9ZB8wcV_JKoq84qSnbeN6lIgjNGnCsjScZgLEuiWdcH6uVjA&gsessionid=k0j4AbbZYTxtZmQd028RiASvLBWYDx2nTDps85QBh0bqYjQ-wjuxQA)  
  <sub>Traders Union, 7 hours ago</sub>  
  Novo Nordisk trades at $38.75, down 1.72% today, as sellers dominate the session and technical signals point to further downside.
- [Novo Nordisk (NVO) Stock Price Prediction: Bearish momentum meets a low-volume pullback near support](https://www.google.com/goto?url=CAESmwEBxCJF1ygWsVcgcG1jPKwFCG9o8qBEcmMGs12hBvXvHxAfcMbvX8Bm-sKuLF9R39ECAAt4J_DXfQO0R7B9qY-xbc6Dbv22x96vqlExzDhxLPkcCE5i5KgaGBICqmWPje0SWCi2yw83kGcHtA660Eai1nbp-vHOAZJLPFlQ5mvZVCDIOOWi3zPoQCRUVmV71PBJw_J5puOvkn3Xdg&gsessionid=k0j4AbbZYTxtZmQd028RiASvLBWYDx2nTDps85QBh0bqYjQ-wjuxQA)  
  <sub>Blockchain News, 1 hour ago</sub>  
  Novo Nordisk (NVO) is quoted at $38.40, down 2.04% over 24 hours, after trading in a $39.83 to $38.24 range. That keeps the stock below its 7-day SMA of...
- [Novo Nordisk (NVO) Stock Price Prediction: Pullback holds near lower Bollinger support as futures positioning builds](https://www.google.com/goto?url=CAESowEBxCJF11mBS3Z94DrrL3M5Jo_opC9QzTVKLxMaDaqQKNkd1zTy_X3adoPG4vzsnocXnxIqh7-cvqcArwY8djvurleBH4Ngx87Go2qJpm3_OXyiHFFZt_9BODlZieeLwedsqcGxDbJIL3ROpWlG2npldun-GHb_JFjCmBmDVIpHu_acaX80P6J9cKZJ8aTWWO_Z985tdSyl3oDw6GDFieuvxoYB&gsessionid=k0j4AbbZYTxtZmQd028RiASvLBWYDx2nTDps85QBh0bqYjQ-wjuxQA)  
  <sub>Blockchain News, 15 hours ago</sub>  
  Novo Nordisk (NVO) is trading at $39.18, down 2.73% on the session and hovering just under the Bollinger lower band at $39.21. Binance Futures data show a.
- [UnitedHealth Group (UNH) Stock Price Prediction: Oversold bounce setup meets heavy trend damage after a sharp selloff](https://www.google.com/goto?url=CAESnwEBxCJF10WrA-fTndJBMYSD78zr52cvmfk6KIJxAhhjRSDI_Sk_OWt-qBtwNMZIURobOs7mbJAjLCe4KdqJO4E9QdGwZcvMxgBXCYVphovd8mjDFmKbQ4bhpG7OPDz9I7hSmrzYCsPnHjZADjtmwaeUYl9bzwhYjXwVkCCd3kubUKQzSEEvE0uZ9Q85aiBp8cpKqFcM8jcgbv6E12spVTI&gsessionid=k0j4AbbZYTxtZmQd028RiASvLBWYDx2nTDps85QBh0bqYjQ-wjuxQA)  
  <sub>Blockchain News, 15 hours ago</sub>  
  UnitedHealth Group (UNH) fell 9.37% to $351.91, leaving the stock below its short- and medium-term moving averages and inside the lower half of its recent.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.50</summary>

_Not available today._

</details>

<details><summary><b>Price and chart</b> — score -0.60</summary>

```text
Last close 38.84 (bar of 2026-11-20), from 502 daily bars
Trend: vs 20d SMA 40.18 (-3.3%), 50d 39.61 (-1.9%), 200d 42.88 (-9.4%); 50d below 200d
Momentum: RSI(14) 42.4 | MACD -0.014 vs signal 0.174 (histogram -0.188)
Returns: 1d -0.1% | 5d -6.7% | 1m -1.5% | 3m -17.2%
52-week range: 35.29 - 63.98 (now 12.4% of the way up)
Volatility: ATR(14) 1.06 (2.7% of price) | annualised 20d 35.0%
Volume: 0.09x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.20</summary>

```text
Sector: Healthcare / Drug Manufacturers - General | market cap 171.18B
Valuation: trailing P/E 9.81 | forward P/E 11.06 | P/B 5.23 | PEG 4.06
Profitability: profit margin 33.9% | operating margin 50.8% | ROE 58.4%
Growth (YoY): revenue +5.6% | earnings -15.8%
Balance sheet: debt/equity 61.7% | free cash flow 32.75B
Risk: beta 0.37 | short interest 1.2% of float
Next earnings: 2027-02-03
```

</details>

<details><summary><b>What this fund holds</b> — score +0.20</summary>

_Not available today._

</details>

<details><summary><b>Does this company beat its own forecasts</b> — score +0.20</summary>

```text
Earnings record, last 4 quarters: 1 beat, 1 in line, 2 missed
  2026-09-30 missed by 22% | 2026-06-30 missed by 6% | 2026-03-31 beat by 23% | 2025-12-31 in line
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

<details><summary><b>What analysts and big funds say</b> — score -0.10</summary>

```text
Consensus: hold (mean 2.85 on a 1=strong buy to 5=strong sell scale, 12 analysts)
Ratings: 0 strong buy, 2 buy, 10 hold, 1 sell, 0 strong sell
Price target: mean 45.71 (+17.7% vs last close), range 39.42 - 64.05
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

<details><summary><b>What analysts say about what this fund holds</b> — score -0.10</summary>

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

### Teva Pharmaceutical (TEVA) · Company — NEUTRAL, confidence 0.35

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> The recent R&D head departure and legal overhang provide a negative news catalyst, while technicals show the price well below short‑term averages with very low volume, indicating bearish short‑term pressure. Fundamentals remain weak (high debt, low margins, negative growth) despite a modest forward P/E. Analyst consensus is bullish with a +30% price target, but the upgrades are not fresh. Earnings record is positive (3 beats, 1 miss). The mix of bearish and bullish signals is contradictory, leading to a neutral stance with low conviction.

**Main reasons it gave:**
- R&D head exit and legal overhang (negative news)
- Price below 20-day and 50-day SMA, volume 0.05× average (bearish technicals)
- Trailing P/E 90, forward P/E 12.36, debt/equity 212.9% (weak fundamentals)
- Buy consensus, price target +30% vs current price (bullish analyst view)
- 3 earnings beats, 1 miss (positive earnings record)

<details><summary><b>News</b> — score -0.60</summary>

- [Teva Pharmaceutical Industries Limited (TEVA) Stock Price, News, Quote & History](https://ca.finance.yahoo.com/quote/TEVA/latest-news/)  
  <sub>Yahoo! Finance Canada, 4 hours ago</sub>  
  Teva Pharmaceutical Industries Limited (TEVA).
- [Teva (TEVA) Stock Fair Value Edges Higher After Constructive Analyst Commentary](https://sg.finance.yahoo.com/news/teva-teva-stock-fair-value-100743345.html)  
  <sub>Yahoo Finance Singapore, 5 hours ago</sub>  
  The blended fair value estimate for Teva Pharmaceutical Industries has shifted from US$48.94 to US$50.51. This provides a fresh reference point for current...
- [Teva falls as R&D head exits amid shift to innovative medicines](https://www.google.com/goto?url=CAESgQEBxCJF13645ZhoOxYWykLZWeaQkY9P2V2D81uRB1ywlsOGN4VypygspBilGerQZya_QPPxSInLD-qMjnF86HVk_hIp-NBa3KrvxM7r7E0z0vwvTzzVBkqv8xCA13SxikXgn1kH4COsvM61z7jnq3_cWh88-DERcAE-r1W9YR-W2DM&gsessionid=aczlBo6H22nih35Zrfs2jrH369mCRZECcc_ZNUEjtbmou5vbrw0ROQ)  
  <sub>Seeking Alpha, 20 hours ago</sub>  
  Teva Pharmaceutical (TEVA) stock falls as R&D head Eric Hughes departs at a time the company is focusing on its innovative drugs. Read more here.
- [H.C. Wainwright reiterates Buy on Teva Pharma stock, $54 target By Investing.com](https://www.google.com/goto?url=CAEStQEBxCJF19lhMR9zNzvev_pakFPgmlypKcOMWzi7evFAz_CF-F6bPj8GDzz79RSaosuC9qKD6-52uOfaAf9DYKVYpyu4eKRDToP0BvAJCg7nthNlCGp9doYtt_Qj8lIxUAjYV-ZaHn9t_AEW3Gw-h3cYadAgh_7_QnP1ekneKXUoMii1W4BTmLreQCu5XX_NyHwfjpPyuiP_3C-ZmppO_jLLZzn8ngnPxLQEyQ_c67ZJk33fa0Fe&gsessionid=aczlBo6H22nih35Zrfs2jrH369mCRZECcc_ZNUEjtbmou5vbrw0ROQ)  
  <sub>Investing.com Canada, 2 hours ago</sub>  
  Investing.com - H.C. Wainwright reiterated a Buy rating on Teva Pharmaceutical Industries (NYSE:TEVA) with a $54.00 price target.
- [Teva Pharmaceutical Industries (NYSE:TEVA) Stock Breaks Below 50 Day Moving Average - Here's Why](https://www.google.com/goto?url=CAES1QEBxCJF1wgKhUFHoBTV3clZqfQHhAvKtQHJa67XHvIqH91t-ZAoQQ83wA0Wyio2EkzQRMETF_c_PXQPHk-J7POWt5AiGkWMOFZe4WMVJUlgorOD4ide1vcthijtFoonV1tojkqQqad5d0fycDaKZEGDu7ZFIoCZKZ-7VwkzlP8FDO4ye-3XGfgH_o5HenZlnzsKe_x2NYHzPcGwv3xPVoQ3P6Yh4v3M-Zqb06jN5hnoRG0WN5ffCVgxinJjN6mzD7RBp3XNg78L2gSo562WK6j_joiPPe8&gsessionid=aczlBo6H22nih35Zrfs2jrH369mCRZECcc_ZNUEjtbmou5vbrw0ROQ)  
  <sub>MarketBeat, 5 hours ago</sub>  
  Teva Pharmaceutical Industries (NYSE:TEVA) Stock Price Crosses Below 50 Day Moving Average - Here's Why.
- [Teva shares fall as R&D leadership change and legal overhang unsettle investors](https://www.google.com/goto?url=CAESrwEBxCJF12nDBvRlNtKCLSHMR97-hvYxID7soVnBWA2cemYZSOHN03KsxO4LCha17ZOcGZtFO2hrVrZU4YgZ6FV3up6C2zAAql8Duf8ZY7J3_iWjJacixIzZxeNasgq_HGb8tWYIY1T_md38Ge9h8qmf0WAo0YdP0etQMIT3s4gHG-jFcdUQZao7Mbq5CwbKQdXLe3MYq8154olBxinzRgvvAeDyCxRxEUihK86oF-w7&gsessionid=aczlBo6H22nih35Zrfs2jrH369mCRZECcc_ZNUEjtbmou5vbrw0ROQ)  
  <sub>Quiver Quantitative, 21 hours ago</sub>  
  Teva Pharmaceutical Industries (TEVA) is down 6.7% today. Here is some analysis on what might have c.
- [Teva Pharmaceutical Industries (TEVA) Stock Forecasts](https://www.google.com/goto?url=CAESkgEBxCJF13yoGyb8PthdxpFJfzlcleDJuWjlFaavH5DpxbVwQd02wRJyNVzzwWJuKLaoeRTDQEQukkchAJQeRtGbNE3gWcCIOwS47wiUoQHnOYcu2FaeOllZ6TVQO1tJLuthHrGTWecqGbzaf3MO48216XjxvwUCPVJhA-EVIJ9rtSd4gefyO4MkzQuyg7ugeKcchg&gsessionid=aczlBo6H22nih35Zrfs2jrH369mCRZECcc_ZNUEjtbmou5vbrw0ROQ)  
  <sub>Yahoo Finance, 16 hours ago</sub>  
  At Yahoo Finance, you get free stock quotes, up-to-date news, portfolio management resources, international market data, social interaction and mortgage...
- [Barclays maintains Teva Pharmaceutical Indus at Overweight, raises price target to $50 from $47](https://www.google.com/goto?url=CAES2AEBxCJF127Klzmsu7eEM4_vC6lzXVox0qPOROZBatwtOm3dI49jOgpDACA9bbdVu4wDAMCt_mJRIty1dAJ2U_PqA7dGRjXXcwHgUFduQ7BkqJTxtQQRk04LmPvxlxRX13kIuYAQ8QRkh5iqqqNd9WFG6ttKj4Vx7eOSiaxhFCuJ64EqlPhS_eeWsGNdWw_7HueYJBEUCRD9cBmpKulCKIetnew3nHUypUfMJPqrmkP4_UVrGNzCwzHPpEnHH8BJjWbd96DxqrwNE6oRYTkjp9VhQfkQ5FCRhCc&gsessionid=aczlBo6H22nih35Zrfs2jrH369mCRZECcc_ZNUEjtbmou5vbrw0ROQ)  
  <sub>TradingView, 23 hours ago</sub>  
  Barclays maintained Teva Pharmaceutical Indus at Overweight and raised its price target to $50 from $47, a 6.4% increase.The price target implies a downside...
- [Zacks Research Upgrades Teva Pharmaceutical Industries (NYSE:TEVA) to "Hold"](https://www.google.com/goto?url=CAESxAEBxCJF190JLLccFeiYMVbQO0dFTGaWbKy6SxvF4gFRp-WgCLEea35zsBN0qpv5YZDzS8yE-mRgiwSeqeBOCEsKKD-56IDdtG2jnYzabaceTuA9VchCfkFcXJf4v9Hgpru04EZopSCbhQ_K2g2dZs_CRElkWidtIhsZJRGjqNemXPKD9eRa-4kNiEWBvrsi5mjtw-7v9VpU4wvxbgPxzjX7jhE6GJTf3uRjmEyWsDBMyHZOpNN-5aqFYjIYA02BiRQ9Ob6F&gsessionid=aczlBo6H22nih35Zrfs2jrH369mCRZECcc_ZNUEjtbmou5vbrw0ROQ)  
  <sub>MarketBeat, 3 hours ago</sub>  
  Zacks Research raised Teva Pharmaceutical Industries from a "strong sell" rating to a "hold" rating in a research note on Wednesday.
- [Barclays Forecasts Strong Price Appreciation for Teva Pharmaceutical Industries (NYSE:TEVA) Stock](https://www.google.com/goto?url=CAES2wEBxCJF157n0_trc5USwLNFVTuk4RGHgaZkdow9OUKHp_ly_067JL6Z-l8Pn9rabVmdJxUC7v9D4eqYyrGTSwU6eHLqDe34ZzZ9_e4WhTHq3sOs8DCSG-7WjIoXfSiHjMUBga4J6HmAn86Z_sljkRJckUAU5jg8OkRvaM4dNsBNX62NOushVzjDCzXbk2pAf1Lz6LXMU3C8YZ7lkuaIOlw1zNR81QiCH29FnBTlMwBtwgyayv8UN7wsvhHHhykxAZje6L-5irCjUPnDXe7iqABWkWk8PlHLcbAc3DQ&gsessionid=aczlBo6H22nih35Zrfs2jrH369mCRZECcc_ZNUEjtbmou5vbrw0ROQ)  
  <sub>MarketBeat, 23 hours ago</sub>  
  Barclays lifted their price objective on Teva Pharmaceutical Industries from $47.00 to $50.00 and gave the company an "overweight" rating in a research...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score -0.60</summary>

_Not available today._

</details>

<details><summary><b>Price and chart</b> — score -0.80</summary>

```text
Last close 38.70 (bar of 2026-11-20), from 502 daily bars
Trend: vs 20d SMA 41.71 (-7.2%), 50d 40.61 (-4.7%), 200d 35.25 (+9.8%); 50d above 200d
Momentum: RSI(14) 37.6 | MACD 0.117 vs signal 0.612 (histogram -0.495)
Returns: 1d +0.4% | 5d -13.0% | 1m -3.8% | 3m +4.8%
52-week range: 24.21 - 44.50 (now 71.4% of the way up)
Volatility: ATR(14) 1.37 (3.5% of price) | annualised 20d 44.8%
Volume: 0.05x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score -0.55</summary>

```text
Sector: Healthcare / Drug Manufacturers - Specialty & Generic | market cap 45.16B
Valuation: trailing P/E 90.00 | forward P/E 12.36 | P/B 5.66 | PEG 0.71
Profitability: profit margin 2.9% | operating margin 19.8% | ROE 6.7%
Growth (YoY): revenue -1.9% | earnings -46.0%
Balance sheet: debt/equity 212.9% | free cash flow 1.49B
Risk: beta 0.84 | short interest 2.4% of float
Next earnings: 2027-01-27
```

</details>

<details><summary><b>What this fund holds</b> — score -0.55</summary>

_Not available today._

</details>

<details><summary><b>Does this company beat its own forecasts</b> — score -0.55</summary>

```text
Earnings record, last 4 quarters: 3 beats, 1 missed
  2026-09-30 beat by 15% | 2026-06-30 missed by 92% | 2026-03-31 beat by 9% | 2025-12-31 beat by 39%
```

</details>

<details><summary><b>What holding this fund costs you</b> — score -0.55</summary>

_Not available today._

</details>

<details><summary><b>How much oil and gas is in storage</b> — score -0.55</summary>

_Not available today._

</details>

<details><summary><b>How the crop is growing</b> — score -0.55</summary>

_Not available today._

</details>

<details><summary><b>What analysts and big funds say</b> — score +0.25</summary>

```text
Consensus: buy (mean 1.53 on a 1=strong buy to 5=strong sell scale, 14 analysts)
Ratings: 4 strong buy, 9 buy, 2 hold, 0 sell, 0 strong sell
Price target: mean 50.51 (+30.5% vs last close), range 42.12 - 57.00
Recent rating changes:
  - 2026-11-12 Piper Sandler: main, Overweight -> Overweight
  - 2026-11-05 Leerink Partners: main, Outperform -> Outperform
  - 2026-11-04 TD Cowen: main, Buy -> Buy
  - 2026-11-04 HC Wainwright & Co.: main, Buy -> Buy
  - 2026-11-02 HC Wainwright & Co.: init, ? -> Buy
  - 2026-10-15 Barclays: main, Overweight -> Overweight
Institutional ownership: 69.5%
Largest holders: Blackrock Inc. (5.4%), Phoenix Financial Ltd. (3.6%), WCM Investment Management, LLC (3.6%), Clal Insurance Enterprises Holdings Ltd (3.6%), Migdal Insurance & Financial Holdings Ltd. (3.4%)
```

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score +0.25</summary>

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

- [Elbit’s $33 Billion Backlog Signals More Growth Ahead](https://news.clearancejobs.com/2026/11/19/elbits-33-billion-backlog-signals-more-growth-ahead/)  
  <sub>Clearance Jobs, 23 hours ago</sub>  
  Driven partially by rapidly growing revenue from Israel, in line with my previous expectations, Israel-based defense contractor Elbit Systems (ESLT)...
- [Elbit Systems Ltd. Stock 12‑Month Price Target Cut to $830.89, Implies 19% Upside](https://www.tradingview.com/news/tradingview:d99b5742c83db:0-elbit-systems-ltd-stock-12-month-price-target-cut-to-830-89-implies-19-upside/)  
  <sub>TradingView, 19 hours ago</sub>  
  Explore more price target data and ratings for Elbit Systems Ltd. on the Forecasts tab, and track all previous and future analyst recommendations for Elbit...
- [Elbit Systems Ltd.: 12-Monats-Kursziel auf $830,89 gesenkt, Aufwärtspotenzial von 19%](https://www.google.com/goto?url=CAESegHEIkXXX9_mC0Mbw9urGvTdQdVRtCq6h5WXiDi0hcBUI8fQDHPDkbNALJ7ydpe0MrJL3NShS4rTGi0xXxcdWORke7koe_T7jBnlSUZbcwuMMG__Fleya1PX8WyB4BNwm99PT9ms7-uVMMXjnkoZhfizPY70fq0LsewO&gsessionid=XBCQIJdHxFu0up47TnZo4HFISd5d-f5qIhHa0oBygjQnTI6Rfkqf3g)  
  <sub>TradingView, 19 hours ago</sub>  
  Mehr Kursziele und Analystenratings zu Elbit Systems Ltd. gibt es im Tab „Prognosen“. Alle bisherigen und künftigen Analystenempfehlungen lassen sich im...
- [Elbit Systems stock: Jefferies raises target, keeps Hold](https://www.google.com/goto?url=CAESsgEBxCJF16SyCP2O2ySwv7MfMLN2tlR03GhLU6YmifG7XByQ5EgXfcvHSyFLKCVEVbY6GAuEiftBEDvx-1CCZooMmKFQC36VI1Zl5Pz1xCDmpPJaoEuSiV88opNhxJJnu1V_wbzC8YE6VzRivrfWhy5yzyY93qhz_z4QZ2aoxPZ8f4qf8CxHoINM3acMcAKizZ4S5oH_RwLoutThCFzSuMu5FPEfKfdg5TBC3T3KhIgxt76k&gsessionid=XBCQIJdHxFu0up47TnZo4HFISd5d-f5qIhHa0oBygjQnTI6Rfkqf3g)  
  <sub>ad-hoc-news.de, 22 hours ago</sub>  
  Elbit Systems stock gets a higher Jefferies target after the 2027 outlook. The Hold rating stays unchanged as investors assess growth and execution.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>Price and chart</b> — score n/a</summary>

```text
Last close 673.97 (bar of 2026-11-20), from 502 daily bars
Trend: vs 20d SMA 727.18 (-7.3%), 50d 721.20 (-6.5%), 200d 785.22 (-14.2%); 50d below 200d
Momentum: RSI(14) 42.3 | MACD -11.420 vs signal -5.749 (histogram -5.671)
Returns: 1d -1.2% | 5d -4.6% | 1m -9.3% | 3m -7.7%
52-week range: 454.95 - 1,014.33 (now 39.2% of the way up)
Volatility: ATR(14) 27.79 (4.1% of price) | annualised 20d 65.8%
Volume: 0.03x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score n/a</summary>

```text
Sector: Industrials / Aerospace & Defense | market cap 31.60B
Valuation: trailing P/E 47.50 | forward P/E 33.77 | P/B 6.91 | PEG n/a
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
Price target: mean 837.33 (+24.2% vs last close), range 739.00 - 935.00
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
  <sub>Yahoo! Finance Canada, 22 hours ago</sub>  
  HDFC Bank Limited (HDB) · 1.59% · 13.69% · 8.16% · -27.99% · -28.03% · -27.09% · 3,519.31%. Key Events. Baseline. Advanced Chart. Loading chart...
- [Woori Financial Group Inc. (WF) Stock Price, News, Quote & History](https://ca.finance.yahoo.com/quote/WF/)  
  <sub>Yahoo! Finance Canada, 5 hours ago</sub>  
  Find the latest Woori Financial Group Inc. (WF) stock quote, history, news and other vital information to help you with your stock trading and investing.
- [Trump bought up to $323k of Nvidia stock in September, disclosure shows, Money News](https://www.google.com/goto?url=CAESlAEBxCJF16mo7wpyOhppmKkuYNotMKdNDs1Fh4MP1HMwg-c-ujmhUO7QqKzVOVoAyIGArLBDBJCDmbEdrsHEJuKPybKEAKNkKhDNgXGItXLvocVPqj7lAuEl7g7lg4GN4Ytt2n0lSVvRR6cYJgRymdtiLEiVEwaGP3LI9pvuyAIwj3nT4pmBWUVywZBM2WGS4zCsEnVe&gsessionid=aOsImo5mwkneRV1BZwYYbMUw7oWWP9HvTld0nARPmFBS09-0xjz74w)  
  <sub>AsiaOne.com, 13 hours ago</sub>  
  WASHINGTON — US President Donald Trump bought as much as US$265000 (S$323000) in Nvidia stock and sold as much as US$15000 worth of the stock ​in September,...
- [Bedroom fire at Teck Whye Avenue HDB block: 20 evacuated, one declines hospital treatment after smoke inhalation](https://www.google.com/goto?url=CAESygEBxCJF17C7vb-vK70O6uuI6ysjQ7iKGRmi66W8OQJKseo6aCPNcMsQeSc35xR7CF1dDPadAUlL7st4JzBil-XcxjwyQb-Qm-DML-W7iDqjZSME7EB3QAC3RiOs5w69JP4GO5u88rglCmaZq1PWz7YVbgXpzb4reYQEEy63jArZlXXDXaHWixoBYCgympoa6HnJl8VHF1IpL2VJ0jElrFwrxe3XbY1NkP5mAr3dRS7jrpYxWvmyCtCbDMpVSiZH1v5T6hycvMZhogGF&gsessionid=aOsImo5mwkneRV1BZwYYbMUw7oWWP9HvTld0nARPmFBS09-0xjz74w)  
  <sub>联合早报, 4 hours ago</sub>  
  A fire broke out in the bedroom of a seventh-floor flat at Block 6 Teck Whye Avenue, prompting the Singapore Civil Defence Force (SCDF) and police to...
- [HDFC Bank Limited (HDFCBANK.NS) Stock Price, News, Quote & History](https://www.google.com/goto?url=CAESbAHEIkXXgeZj6o9H43fhQgAOeHggpIhMNuxXuezT5j0NsnLWYNsOEoZ7jspoTlqpKJ2Lmd2BNu2KYmGNAHOPDVLNy4kkQvGtcyeohaxER2F5qC5nb5WkW8nPFBhdUSkSQgJPIjVbgmjsO2LauA&gsessionid=aOsImo5mwkneRV1BZwYYbMUw7oWWP9HvTld0nARPmFBS09-0xjz74w)  
  <sub>Yahoo! Finance Canada, 20 hours ago</sub>  
  Find the latest HDFC Bank Limited (HDFCBANK.NS) stock quote, history, news and other vital information to help you with your stock trading and investing.
- [20 evacuated after fire breaks out in Teck Whye HDB flat, no injuries reported, Singapore News](https://www.google.com/goto?url=CAESeQHEIkXX3THKlLkvHXOWg6un8_pWihFkyYVGP4NEUjGg079NO_kV8QxG7viSl3he1NHRmgZaptjsrgCzvx_9EyWJ0Oelxm5fEhOpVK_2lnylbWd94VMB7h-MgftPBjiJqYFm_lEqcgkzvOnKC29uib9PYJUfKhwxIds&gsessionid=aOsImo5mwkneRV1BZwYYbMUw7oWWP9HvTld0nARPmFBS09-0xjz74w)  
  <sub>AsiaOne.com, 2 hours ago</sub>  
  About 20 people were evacuated after a fire broke out in a HDB flat at Block 6 Teck Whye Avenue on Nov 20 (Friday) at about 3.40pm.
- [Three injured, 30 evacuated after fire breaks out in Jalan Bukit Merah HDB flat, Singapore News](https://www.google.com/goto?url=CAESgwEBxCJF12QHuc9d7PI_ax_CMN4u9yWiQ0QX2eL8Tc21VbKYWKFJNoJ78Ga2AoZCTcvZqLRs8JdUNKlE06156N2LGLuZHClcX2Y851zwrWVFDaMdm5NETjkt8zLzQPWPWeID6PspuVZHEG6VLUi8d4cTagAgbgHDU2eEdz6L2Y4g4edyqA&gsessionid=aOsImo5mwkneRV1BZwYYbMUw7oWWP9HvTld0nARPmFBS09-0xjz74w)  
  <sub>AsiaOne.com, 2 hours ago</sub>  
  Around 30 people were evacuated and three persons taken to the hospital after a fire broke out in a HDB flat at Jalan Bukit Merah on Thursday night (Nov 19)...
- [Firefighting hero nominated for community award charged with allegedly starting Punggol HDB fires](https://www.google.com/goto?url=CAESkQEBxCJF119Wr-N9z73lWtViYvwEMbgoYUqQ4sYoBCP7iC4CP0I0mzfQRhOf99rIJGv2SO9w5aHtoJLIIA1O77i3syl4V-uYZQueLCTDcs-d_rRkm0Fcbj3SlefVCmn7DnDE-Wz64l6agQTqACFxpwHajAr2WoNvC-5xSnvNlgFTiWsLu0gDOlqS0iUd7uxxOwWc&gsessionid=aOsImo5mwkneRV1BZwYYbMUw7oWWP9HvTld0nARPmFBS09-0xjz74w)  
  <sub>AsiaOne.com, 4 hours ago</sub>  
  A Punggol resident who was set to be commended for putting out fires at the central refuse chute of a HDB block in Punggol, has been charged with allegedly...
- [HDFC Bank stock draws focus from Axis and ICICI views](https://www.google.com/goto?url=CAESsQEBxCJF1zKgIPAo079VkcL21_sAjd59ftJebd5sqOJOd0Cwqq0CRJpjXqDFjmFEyG8rhSso66NTrcP3pZajSRG-3onP4ApNLKNjLBvFHSplLfY-bcienAq_BETw5JQ9wEeGDJdJLF_LWqAXZU2cA1evh_wZ0xZidQWsKydei0dUCcUe0HInKG5Q8EKyA-7T7zLqDy5DRD0sTCJGkaXaCP7Qpg4_ZZ-TlB_2BHIVHIv33j4&gsessionid=aOsImo5mwkneRV1BZwYYbMUw7oWWP9HvTld0nARPmFBS09-0xjz74w)  
  <sub>ad-hoc-news.de, 6 hours ago</sub>  
  HDFC Bank stock is in focus as brokerages assess its recovery prospects. Retail growth, deposits and margins remain key investor questions.
- [HDB Financial Servic Investor Analysis | StockIQ](https://www.google.com/goto?url=CAESmwEBxCJF19e19dcnQ7R4v6KjlVVHlN2QiZT2wyis7aqiWYUNOL4PKYK7Z_qoHbg9pF5Tp7wWkwG-jd8rhfHI6N4IAemcBK8fUjidRRTnWxc7WYtxf9R9mEfSjjBG8fA66jeOnIMYlvJ--kD_dggwuUpXR2bIoj_Mhnufquh2L7YDpTnEpVOz8mh80kEgC0-J4rNE4fs_gcbrNQ6evw&gsessionid=aOsImo5mwkneRV1BZwYYbMUw7oWWP9HvTld0nARPmFBS09-0xjz74w)  
  <sub>The Economic Times, 16 hours ago</sub>  
  Explore HDB Financial Servic investor analysis with StockIQ. Get AI scores, financial health insights, investment risks and management commentary.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>Price and chart</b> — score n/a</summary>

```text
Last close 27.72 (bar of 2026-11-20), from 502 daily bars
Trend: vs 20d SMA 24.53 (+13.0%), 50d 23.45 (+18.2%), 200d 25.26 (+9.7%); 50d below 200d
Momentum: RSI(14) 80.0 | MACD 1.077 vs signal 0.843 (histogram 0.234)
Returns: 1d +5.6% | 5d +7.3% | 1m +23.5% | 3m +17.7%
52-week range: 21.36 - 36.88 (now 40.9% of the way up)
Volatility: ATR(14) 0.64 (2.3% of price) | annualised 20d 30.9%
Volume: 0.32x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score n/a</summary>

```text
Sector: Financial Services / Banks - Regional | market cap 142.61B
Valuation: trailing P/E 17.88 | forward P/E 20.02 | P/B 11.04 | PEG n/a
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
Price target: mean 30.30 (+9.3% vs last close), range 26.20 - 33.00
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

- [What Does JPMorgan Chase (JPM) Naming A New CFO Mean For Investors?](https://finance.yahoo.com/markets/stocks/articles/does-jpmorgan-chase-jpm-naming-060933124.html)  
  <sub>Yahoo Finance, 9 hours ago</sub>  
  JPMorgan Chase (NYSE:JPM) said Bregje de Best will become group CFO, succeeding Jeremy Barnum after Q1 2027. De Best currently serves as CFO of JPMorgan's...
- [JPMorgan Chase (JPM) Receives a Rating Update from a Top Analyst](https://www.theglobeandmail.com/investing/markets/stocks/JPM-N/pressreleases/8928697/jpmorgan-chase-jpm-receives-a-rating-update-from-a-top-analyst/)  
  <sub>The Globe and Mail, 13 hours ago</sub>  
  Detailed price information for JP Morgan Chase & Company (JPM-N) from The Globe and Mail including charting and trades.
- [JPM: SEC Form FWP filed by JP Morgan Chase & Co.](https://www.google.com/goto?url=CAESkAEBxCJF1zIGCsX0hZnRkRismFi3fCXBOSfsUEvSahSC0WEPiSx9-lMmZETXVGKvgAvxcICelq-Is1BLjLFPiDSFNfahxxRS_0J31RVcUfIu5PVtKllxYyi4H1bgoVcUShNjkKe5r2WsPmvqpYfIn21OSm4E8G46z-mL6H4mWHC1KlSy1ItS0e__i1nVOVjSa4A&gsessionid=Ezhdj97mjDqzXK4rUgVjTb9C_lrtTlC5s51iscBVU0lfWFmHSN0HKg)  
  <sub>Quantisnow, 19 hours ago</sub>  
  JPMorgan Chase Financial Company LLC is offering a 12-month contingent income note linked to American Express common shares, guaranteed by JPMorgan Chase &.
- [JPMorgan Chase's certain third-party vendors reportedly hit by cyberattack (JPM:NYSE)](https://www.google.com/goto?url=CAES7AEBxCJF1_u44Z8GiGtUhYXI6yWwTBHHNzKBs5qPmyhrAcagI8Q4AP3iB4g4cIaDO4ou72f8W9KRRFa_ASfkRbV-K5YQNvituudWEXz_q0Vs_Ws9kqMQZPNdY-I6N1MmmXD_mpCcpzkqDE-oXaDUZV51qxOFvJBIZIhhaXmap0dCGZYY584QKUKlaEuoAbbebYA81-Wfhr7dGoqTAayiJDkpp7NVFp_Vf3dGCZzbzbKW_y5F-_4FLL9uHpme72U0MRjUQsLPbpBljHjKg8i9jtqEAMsdcs3f8U5RN5bv4B1Vk_9s9JKTWRsWN3fiPA&gsessionid=Ezhdj97mjDqzXK4rUgVjTb9C_lrtTlC5s51iscBVU0lfWFmHSN0HKg)  
  <sub>Seeking Alpha, 24 hours ago</sub>  
  JPMorgan Chase (JPM) said some of its third-party vendors were the target of ​a cyberattack, Reuters reported on Thursday, citing a spokesperson.
- [Wells Fargo Short Interest Rises As Bears Near August Peak](https://www.google.com/goto?url=CAESuQEBxCJF11sM9DxirEbEKWr10FM88osCVnfJ2PlTJfsKmdDDyibQ6luuNx5AxCKBxBSlKgncnFCwZUkpeba_Cy7a6Ji2vjDpLnuo59FPf2f3qRW9xusvjwd7smjIfEPxqWxiVY0R0sNMJhDuFGRkgiEqJ1GyqWj9KyW_p1iWfzYeVmY_0LPvBq31RZTORhZIUcnDJfsaFwksa2leJ4BmJSZFO4QjXUAOxRo0q7-5O_x_ntxoDUGWGVbqIw&gsessionid=Ezhdj97mjDqzXK4rUgVjTb9C_lrtTlC5s51iscBVU0lfWFmHSN0HKg)  
  <sub>Benzinga, 23 hours ago</sub>  
  Wells Fargo & Co. (NYSE:WFC) saw short sellers add to their positions.Short interest rose 19.91% to 32.02 million shares as of the Oct. 30 settlement date,...
- [Is JPMorgan Chase (NYSE:JPM) Steady Into Year-End After a Firm Run?](https://www.google.com/goto?url=CAESqAEBxCJF19Kac5TG-YqOXSxWWSw0TsjuJWXwW4GvnaXxi6fe03xp8EntNkP4y-qEg5_jMBfKGnAbwub2YPYlon74L3-S3nzdnaoW7iuxnTyTzQsuJYnBK16qEknYSG2ualMCCf0DH8Vb8NBnee46X_vjEAV3KhMQWNuJ4RDqYCBf4aXTgwd7d-fCSzeCiI5T43v_VpKd0QISL6A_bX2GVaPvAa7PAOP3gUA&gsessionid=Ezhdj97mjDqzXK4rUgVjTb9C_lrtTlC5s51iscBVU0lfWFmHSN0HKg)  
  <sub>Kalkine Media, 9 hours ago</sub>  
  JPMorgan Chase (NYSE:JPM) is in focus after firm third-quarter results and an ongoing market debate over private credit as banks steady into year-end.
- [Visa, Mastercard, JPMorgan Hit By Reported Data Leak, Payment Information Not Affected](https://www.google.com/goto?url=CAESnwEBxCJF1xSUgqPEwOe3fxSCTOXU4gD6R_m9BqJYv2ZpspwlqX6AfGY9pGq_8UA58HflfSVYDTCIsIKF7gcgCGIVKHw02nvXWPwAgb23jhYk7Ahzif31UYNVPAlWTFvXV_vS4vmq_sIAAPgvqoZqWNr5pYbYbmwDyd0mxVpsUAPREfc-7lwrl068P5tBlkIFaZ1iHgqyPbbh_-L00jH82PI&gsessionid=Ezhdj97mjDqzXK4rUgVjTb9C_lrtTlC5s51iscBVU0lfWFmHSN0HKg)  
  <sub>Yahoo Finance, 22 hours ago</sub>  
  According to The Wall Street Journal, the breach reportedly involved a third-party service provider, but none of the three companies identified the...
- [J.P. Morgan sees Fed rate hikes at next three meetings as inflation persists](https://www.google.com/goto?url=CAESrgEBxCJF116IH-KQRHTe88A1PwES0SIlStOWU_NT3g0xm3voG02LSkAG-2FoVxt3lQaOpWwlNoV5cqTqcT3R4tbiTCfLHR-upjcthJEX0vq7TpSNHfs9xkg1fSXLBJaPCwIVWgRaZxr4k-aoyzykZx1Isi4FGqGYbZHtefFucgd7Va3xw63_zYPHhlzobpey0wRo8BBzY1wk6W0xnz7s4G7Optm7Fmmb8bAPvVGFt_8&gsessionid=Ezhdj97mjDqzXK4rUgVjTb9C_lrtTlC5s51iscBVU0lfWFmHSN0HKg)  
  <sub>Reuters, 20 hours ago</sub>  
  J.P. Morgan on Thursday said it expects the US Federal Reserve to deliver quarter-point rate ​hikes in January and March next year, ‌on top of a previously...
- [Scout24 shares fall 6% as J.P. Morgan flags AI threat to property portals](https://www.google.com/goto?url=CAESvAEBxCJF19dynplubRX7OAYgbpocTrLSV0Jtl-6Ht2qmqj4xeZTDDaLO-_q2yr8yP4h6jLiSPEExHndNRil1QtSkoqBOCustFn5ofWFdq_wmZnURBBw2AYYP3Ckax4a_90IBwea5769Cm4AdknD9yWQ3Y2-d6zB92jiASZ5U86jMrNGHs8bf1YdD7lURFjQ5abRThBWyfpviDHJMa5tS6SHZpHwSos5xEhVIakZy_Xb-hJIzXMR6Eg-zoBmGJQ&gsessionid=Ezhdj97mjDqzXK4rUgVjTb9C_lrtTlC5s51iscBVU0lfWFmHSN0HKg)  
  <sub>Investing.com, 3 hours ago</sub>  
  Investing.com -- Shares in German online listings operator Scout24 fell over 6% on Friday after J.P. Morgan downgraded the stock to “neutral” from...
- [J.P. Morgan Asset Management Launches JPMorgan All Country Research Enhanced Equity ETF (JALL) on NYSE Arca](https://www.google.com/goto?url=CAESsgEBxCJF1wKLUbhuXPXAS0svJb_e7TjRxrow9sFFwpJrIgVZ4arwux0outRouDqRI78jwTZNA6iNirpxrPePr16pmrtYeEWZCcQK65JEZVrgvfhuvPr6uCCQEMrZszYCvBQlpLvLuoOqtW5V3PBWwcxyha7NNtfBvxYwSleVCP0O7Nb0U0iL3XII9Zf4ikMO0AUuCWjuGyDZb6pN_ltH6HjzzAeXC4bxY973R9JX5ffNellk&gsessionid=Ezhdj97mjDqzXK4rUgVjTb9C_lrtTlC5s51iscBVU0lfWFmHSN0HKg)  
  <sub>Quantisnow, 24 hours ago</sub>  
  Fund seeks long-term capital appreciation through active investment in global developed and emerging markets Active ETFs are becoming a preferred way to...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>Price and chart</b> — score n/a</summary>

```text
Last close 320.67 (bar of 2026-11-20), from 502 daily bars
Trend: vs 20d SMA 337.10 (-4.9%), 50d 337.55 (-5.0%), 200d 325.25 (-1.4%); 50d above 200d
Momentum: RSI(14) 36.2 | MACD -3.315 vs signal -0.958 (histogram -2.356)
Returns: 1d +0.1% | 5d -7.4% | 1m -4.7% | 3m -10.0%
52-week range: 282.84 - 365.18 (now 45.9% of the way up)
Volatility: ATR(14) 7.29 (2.3% of price) | annualised 20d 29.7%
Volume: 0.16x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score n/a</summary>

```text
Sector: Financial Services / Banks - Diversified | market cap 851.58B
Valuation: trailing P/E 13.45 | forward P/E 12.54 | P/B 2.42 | PEG 1.36
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
Price target: mean 373.48 (+16.5% vs last close), range 312.00 - 425.00
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

- [Eli Lilly (LLY) – The Only Healthcare Name in Ken Fisher’s Fastest-Growing Top Positions](https://finance.yahoo.com/markets/stocks/articles/eli-lilly-lly-only-healthcare-181758283.html)  
  <sub>Yahoo Finance, 20 hours ago</sub>  
  Eli Lilly and Company (NYSE:LLY) rounds out our list of the Top 10 Stocks to Buy According to Billionaire Ken Fisher at number 10. Ken Fisher has spent more...
- [About Eli Lilly & Co Tokenized Stock (Coinbase)](https://www.coinbase.com/en-ar/price/eli-lilly--co-base-0xb200000000000000000000f1a0f91e34892e4718)  
  <sub>Coinbase, 20 hours ago</sub>  
  Eli Lilly & Co Tokenized Stock (Coinbase) (LLYC) Price ARS Today is ARS 2118621.83. News, predictions, charts, market cap, buy, sell, convert, and invest on...
- [LLY 261120 1520.00C (LLY261120C1520000) Stock Options Chain | Quotes & News](https://www.google.com/goto?url=CAEScAHEIkXXhCBr0cgYvYqnIB8UvODc2yTknXPp7_M_bLeYw4EKfEWQW2Hci4E0oL43e1o00VGLbrGoSisx93_rRQDdI8ENORcCv5crkgS9gHdBZQoOAcWzC7CM0hD6TY06clv6N94GaMLBON9cbrJq94Q&gsessionid=VkvCAtpxmY76RdEOMVAA_WUALbe7L6U72EZseX47gIAr72Z2EOylhA)  
  <sub>Moomoo, 24 hours ago</sub>  
  Track real-time LLY 261120 1520.00C (LLY261120C1520000) stock options chain data and pricing information and news on moomoo App for your options trading and...
- [Eli Lilly Updates Early-Stage Study of New Obesity Drug LY4167586](https://www.google.com/goto?url=CAES1QEBxCJF1wQV9nzqOegfwxEZKS_JyL_oV8Sw2tobJPQErDOKueP_3yKFW1ib_X-a9DgdZ_ysVO3XFn_hx_BveRjjpGI1YjxX348T7mJsUXzgqDwHkD1HkBMwdOWck24gRB81uAocZZL-7DMa7nY1BTTY0GEUdxkfml2Au516GlxRWmRRvMaWNJpZws0s8Dw8zVO3iMd_Lgnx3ZT3riXDOCq6wctdzqemmpQh67_JPpBl_c2P3mEY2s3AnCu_itXWc1CnxSe4ckN-UF_3r-GPbc80QZRVUH8&gsessionid=VkvCAtpxmY76RdEOMVAA_WUALbe7L6U72EZseX47gIAr72Z2EOylhA)  
  <sub>The Globe and Mail, 22 hours ago</sub>  
  Detailed price information for Eli Lilly and Company (LLY-N) from The Globe and Mail including charting and trades.
- [What Do Eli Lilly (LLY) Vendor Hack And Canada Approval Mean Now?](https://www.google.com/goto?url=CAESzgEBxCJF15NPHudwhWs9Q1ziA_CI7XO5o8NPoY1ZJdNNMG7QW4WXQW3bM6zg86sXnFK0b_mfw8Whq7sHJkQKJk4Cdudwurtq78VFCUbsPqvtbHbU6d1W4n3QEjpAVYBAEtJQwl_CUp3dWTST8lgu2FJphVosmTKrUDTkA-EndHIsIvzDT2CKaheath3O3ErGPakGwm3yU4M7X3ALGq2lPp1SxdTVEvXtQUQo-oKZO0dEK4QTaJBK_upaQErrxxTLQDn0Jmh-WYKYiytZ4dyPlg&gsessionid=VkvCAtpxmY76RdEOMVAA_WUALbe7L6U72EZseX47gIAr72Z2EOylhA)  
  <sub>Simply Wall St, 11 hours ago</sub>  
  Eli Lilly (NYSE: LLY) reported that a third-party vendor was hacked, exposing sensitive data tied to about 1.2 million patients.
- [Jefferies Has Wall Street’s Highest Target on Eli Lilly (LLY). Why?](https://www.google.com/goto?url=CAESkgEBxCJF1yTKBIpy6KIrolqQBl9clCXc5lLjqZ7rVe3R4W8mi0ckSDOw1Nk_IOCLkaaJYs_OKLd1h5N7dmSY6D-jbISh2cLYYTyhkk0jctdZdkNx3nyZgsdLqAqTvpv7_cNcHdp6jaYR_KsXWumVEus-GBhFNBZfW4bIG1eePRRPgoJ9IQmdmMA7BpwnORHy1zMhGg&gsessionid=VkvCAtpxmY76RdEOMVAA_WUALbe7L6U72EZseX47gIAr72Z2EOylhA)  
  <sub>Yahoo Finance Australia, 16 hours ago</sub>  
  We just published a list of the Morgan Stanley's Vintage Values 2027: 10 Stocks Analysts See Climbing Further and Eli Lilly (NYSE:LLY) ranked 10th on this...
- [What Did ObesityWeek Data Reveal for Eli Lilly (NYSE:LLY) Investors?](https://www.google.com/goto?url=CAESqwEBxCJF16LGM2eavJbunycrj76LegX_RuY9lhAX_WAhbjqVnb5cu1If31ZmN55tO_aO9EZZbLGUd7HO-IdvmeKH0mMzCCMwPCWztva_zOGvTcgWQb1NMFYdsht15XUIf6Ox4CB0SjF6h9Q9Z82lw4rSuCvqiKEyedHKC4hEVUipqYBkipczQRtNwqaTToQojSF8LcB43YlAiW5qDngzRg54WVR3iBP_P4GW-vc&gsessionid=VkvCAtpxmY76RdEOMVAA_WUALbe7L6U72EZseX47gIAr72Z2EOylhA)  
  <sub>Kalkine Media, 5 hours ago</sub>  
  Eli Lilly (NYSE:LLY) drew fresh attention this week as its ObesityWeek data slate spotlighted a widening metabolic-medicine franchise.
- [History Says This Brilliant ETF Could Help You Turn $500 Per Month Into $784,100 While Barely Lifting a Finger.](https://www.google.com/goto?url=CAESgAIBxCJF1y2Wzw8R3Ascj7u5zyV3N16cBNmmpRcPXYrDJ2KKHG7-3wHj51NqiZZYrTnJfVXGzYdnxMfKKkefieXne2h1ZqHWhCNfzS9MENYnPNvcA3ysOSms4iQGEPbjltbLMx5OSA_o__-x_U6n5h-6lRoyDmbJ8op_2nwp1Mkmrga3ad13QuueFdfuXP-1uen9o0gIoJCJCw9JXVb_VQUBWbwlt6Tf9bnP_EdSIzPMlmjHQWdM5X33H2LDQ7gLpPfK8_9MkeHzwGI7jFs62vVW7Tkh4pPxrqbXK5kaW9uucI0rMYhp0OrYXnMvyKzBc8cpyaTfDr_YRE_X-xQByTwG&gsessionid=VkvCAtpxmY76RdEOMVAA_WUALbe7L6U72EZseX47gIAr72Z2EOylhA)  
  <sub>The Globe and Mail, 13 hours ago</sub>  
  Detailed price information for Eli Lilly and Company (LLY-N) from The Globe and Mail including charting and trades.
- [LLY Nov 2026 1425.000 put (LLY261120P01425000) stock price, news, quote and history](https://www.google.com/goto?url=CAEScwHEIkXXYctJUKHFatbph8lqghDJjbJFExCA8nC_qGv_tsf_o9KTixv9_0_zKJpP2a38s1d_0fqqjLo-kXZRgGFySdw3QcCWJDjsbw64-KNsyet1O7Ky-Rqx9WFe7Slz5yjFeL_17RCfj8e4x8FaafwbRrI&gsessionid=VkvCAtpxmY76RdEOMVAA_WUALbe7L6U72EZseX47gIAr72Z2EOylhA)  
  <sub>Yahoo Finance UK, 21 hours ago</sub>  
  Find the latest LLY Nov 2026 1425.000 put (LLY261120P01425000) stock quote, history, news and other vital information to help you with your stock trading...
- [Is Anthropic Really Worth More Than $1 Trillion?](https://www.google.com/goto?url=CAESwgEBxCJF16GV-wurVcOJbwfYing6uPFmt6bV0v_Mz32fHmGXZyL35vj7f90EU8j_BHvB98OKa-OJOKUmPv6xvSTRUKEJ_Zg313HJoZBx404Wbhlrebt_QOvyCtjuUJSCeOozvtvD7vQFD9xRDwj7ebivedjGrSt1PNgFyExc3NRWxaC4XiS_kH9YHuiw_tSF5GCn5gG6xlc2RtFzWL7zHFrWatKnXLpBuD8KFog8OsvvbmTU4T7tu89VmfSmPIiaEl6Lvw&gsessionid=VkvCAtpxmY76RdEOMVAA_WUALbe7L6U72EZseX47gIAr72Z2EOylhA)  
  <sub>The Globe and Mail, 20 hours ago</sub>  
  Detailed price information for Eli Lilly and Company (LLY-N) from The Globe and Mail including charting and trades.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>Price and chart</b> — score n/a</summary>

```text
Last close 1,365.12 (bar of 2026-11-20), from 502 daily bars
Trend: vs 20d SMA 1,384.81 (-1.4%), 50d 1,267.28 (+7.7%), 200d 1,117.99 (+22.1%); 50d above 200d
Momentum: RSI(14) 52.5 | MACD 34.674 vs signal 46.932 (histogram -12.258)
Returns: 1d +1.0% | 5d -5.4% | 1m +4.5% | 3m +9.5%
52-week range: 851.21 - 1,443.50 (now 86.8% of the way up)
Volatility: ATR(14) 41.36 (3.0% of price) | annualised 20d 37.0%
Volume: 0.12x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score n/a</summary>

```text
Sector: Healthcare / Drug Manufacturers - General | market cap 1.22T
Valuation: trailing P/E 44.31 | forward P/E 26.84 | P/B 30.21 | PEG 1.25
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
Price target: mean 1,470.06 (+7.7% vs last close), range 940.00 - 1,700.00
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
Last 180 days: bought 39,858 shares in 43 transaction(s) | sold 313,215 shares in 9
Net: -273,357 shares (-13.7% of insider holdings) | insiders hold 1,728,045 shares
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

- [MercadoLibre (MELI) Stock Price Prediction: Oversold breakdown meets a fresh analyst reset](http://www.bing.com/news/apiclick.aspx?ref=FexRss&aid=&tid=6b005c82be4c419db29b5f7b7eead335&url=https%3a%2f%2fblockchain.news%2fnews%2f20261120-price-prediction-meli-oversold-breakdown-meets-a-fresh-analyst&c=947032844716168766&mkt=en-us)  
  <sub>Blockchain News, 10h ago</sub>  
  MercadoLibre (MELI) is under pressure after sliding 6.89% to $1,343.79, with the stock trading below its short- and medium-term moving averages and ...
- [Should you avoid MercadoLibre (MELI) stock, even now that it's near a 52-week low?](http://www.bing.com/news/apiclick.aspx?ref=FexRss&aid=&tid=6b005c82be4c419db29b5f7b7eead335&url=https%3a%2f%2fwww.msn.com%2fen-us%2fnews%2fother%2fshould-you-avoid-mercadolibre-meli-stock-even-now-that-its-near-a-52-week-low%2far-AA2hOW9K&c=10781441224346960420&mkt=en-us)  
  <sub>The Motley Fool on MSN, 21h ago</sub>  
  The stock has fallen far, but the company retains solid growth prospects.
- [MercadoLibre (MELI) Stock Price Prediction: Oversold bounce risk meets a still-heavy trend](http://www.bing.com/news/apiclick.aspx?ref=FexRss&aid=&tid=6b005c82be4c419db29b5f7b7eead335&url=https%3a%2f%2fblockchain.news%2fnews%2f20261119-price-prediction-meli-oversold-bounce-risk-meets-a-still&c=11376238219804727213&mkt=en-us)  
  <sub>Blockchain News, 24h ago</sub>  
  MercadoLibre (MELI) is trading at $1,449.05, slightly above its pivot point but still below the 7-day, 12-day and 20-day moving averages. Daily RSI at ...
- [MercadoLibre grew sales 44%—so why did the stock crash 28%?](http://www.bing.com/news/apiclick.aspx?ref=FexRss&aid=&tid=6b005c82be4c419db29b5f7b7eead335&url=https%3a%2f%2ffinance.yahoo.com%2fmarkets%2fstocks%2farticles%2fmercadolibre-grew-sales-44-why-134756984.html&c=2067228782545405262&mkt=en-us)  
  <sub>Yahoo Finance, 22h ago</sub>  
  Latin America's dominant e-commerce and fintech platform—has not escaped either, crashing 27.9% over the past month to $1,355.49, including a 9.1% slide in the past week alone. MercadoLibre's sales ...
- [A $10 Billion Fund Just Bought These 3 Stocks](http://www.bing.com/news/apiclick.aspx?ref=FexRss&aid=&tid=6b005c82be4c419db29b5f7b7eead335&url=https%3a%2f%2ffinance.yahoo.com%2fmarkets%2fstocks%2farticles%2f10-billion-fund-just-bought-125834355.html&c=11239582875840096748&mkt=en-us)  
  <sub>Yahoo Finance, 10h ago</sub>  
  MercadoLibre was the only brand-new position of the three. The fund held 70,000 shares worth $121 million at Sept. 30, which was 2.5% of SCGE's 13F holdings and its ninth-biggest holding. The stock is ...
- [MercadoLibre stock expands Amazon merchant financing with IFC](http://www.bing.com/news/apiclick.aspx?ref=FexRss&aid=&tid=6b005c82be4c419db29b5f7b7eead335&url=https%3a%2f%2fwww.ad-hoc-news.de%2fboerse%2fnews%2fcorporate-news%2fmercadolibre-stock-expands-amazon-merchant-financing-with-ifc%2f70539975&c=7836511564427981269&mkt=en-us)  
  <sub>Ad Hoc News, 9h ago</sub>  
  On November 18, the International Finance Corporation announced a financing partnership with Mercado Libre to expand working capital access for small businesses in Brazil's Amazon region. IFC said the ...
- [MercadoLibre stock forecast: Seller pressure points to continued downside risk](http://www.bing.com/news/apiclick.aspx?ref=FexRss&aid=&tid=6b005c82be4c419db29b5f7b7eead335&url=https%3a%2f%2ftradersunion.com%2fnews%2fstocks%2fshow%2f4326817-mercadolibre-slides-3-95percent-to-usd1366%2f&c=5553047705768776919&mkt=en-us)  
  <sub>tradersunion, 28h ago</sub>  
  MercadoLibre trades at $1,366, down 3.95% today as technicals signal further downside risk amid subdued short-term sentiment.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>Price and chart</b> — score n/a</summary>

```text
Last close 1,381.24 (bar of 2026-11-20), from 502 daily bars
Trend: vs 20d SMA 1,549.32 (-10.8%), 50d 1,710.28 (-19.2%), 200d 1,766.55 (-21.8%); 50d below 200d
Momentum: RSI(14) 29.4 | MACD -100.507 vs signal -86.836 (histogram -13.670)
Returns: 1d +1.9% | 5d -7.4% | 1m -24.3% | 3m -29.1%
52-week range: 1,355.49 - 2,295.00 (now 2.7% of the way up)
Volatility: ATR(14) 62.21 (4.5% of price) | annualised 20d 59.6%
Volume: 0.14x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score n/a</summary>

```text
Sector: Consumer Cyclical / Internet Retail | market cap 70.02B
Valuation: trailing P/E 37.05 | forward P/E 26.08 | P/B 8.54 | PEG 0.78
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
Price target: mean 2,152.76 (+55.9% vs last close), range 1,600.00 - 2,700.00
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

- [NVIDIA Corporation (NVDA) stock price, news, quote and history](https://uk.finance.yahoo.com/quote/NVDA/)  
  <sub>Yahoo Finance UK, 5 hours ago</sub>  
  NVIDIA Corporation (NVDA) · -12.16% · -32.76% · -33.83% · -21.73% · -21.73% · 342.56% · 333,568.58%. Key events. Baseline. Advanced chart. Loading...
- [Will Jensen Huang’s Exit Break NVDA Stock’s Momentum?](https://www.forbes.com/sites/greatspeculations/2026/11/20/will-jensen-huangs-exit-break-nvda-stocks-momentum/)  
  <sub>Forbes, 1 hour ago</sub>  
  how did stocks fare when a founder walked away from a market leader?
- [Prediction: Nvidia Will Hit a New All-Time High in 2027 (Hint: Watch This Metric)](https://www.google.com/goto?url=CAEStQEBxCJF19y7XkR-eT7hV3UtA1DErraKSbhLqtfiASvQ8Rs8X7PfPAKK3_CzPmmxcCwukep1vaHfxfWt6jTF47kca47tDR5o0LyMQOBDfSaJ2vq_50dM7SNVYdcHML2zI9WIMcbdLiZ8VI3W3BMdFD6w1OCoEpNL6WDyMZsum2Lp25vSCrtiD9mCxUCIwxFvWeZXI-nHN_wVvf-iD_gWvbBjnx61zG0qqmAEhPCNcqfgdF4owo4b&gsessionid=JG_SBLXiufwcJeFGO6aKVp9nNP6q_0K3nFzYcApyHPbcdIQbzFwExQ)  
  <sub>The Motley Fool, 1 hour ago</sub>  
  It's been a turbulent November for Nvidia (NVDA -3.30%) as the company deals with the unexpected resignation of founder and longtime CEO Jensen Huang.
- [Should You Sell Nvidia Stock For A Tax Loss?](https://www.google.com/goto?url=CAESpQEBxCJF14e5ZknoN8YpqtjQp5Jwt0Hroi1DMGX4r2rTZ-FctsKQ_ZXWi5_gRNiYOCvQfGy8dZh1bW48OkYCh5ceM4rMjjJ4-kMnUqNqGUEYe7DzHonNAIlP3KyfymV-cbw3zDBbx-JSi1tuSGU6BB_wh0QEgvUKOkwCiACZmuSCoFT1mK1UIPDYE8HjHv2Ok714iGQhZcjxxf1NSI67hSGSGcntr28&gsessionid=JG_SBLXiufwcJeFGO6aKVp9nNP6q_0K3nFzYcApyHPbcdIQbzFwExQ)  
  <sub>Trefis, 5 hours ago</sub>  
  Today's big story: Will 2027 Be A 2022 Repeat For Stocks? Nvidia announced on Nov 12 that Jensen Huang resigned as chief executive.
- [Nvidia Stock Hits New 52-Week Low: Buy the Dip or Stay Away?](https://www.google.com/goto?url=CAESrAEBxCJF12knM2rM3oDyEXzMPrgdXXSce5BDacD7NyYm6wAGGlxJifzd0rkZPi7jBOZgmF11fICQ5ejt4WwsxBglng5cE4N-HmJ-PjBKiZ7R9tc8mVmJiebbjvjFTMAT4KeXlrZkH_Iw3CzgcZnFgGNAxBpzFWtFOucsCtCg9gZ8hAzYgS8zeRlDLAtuyiclwak8cVIaRoc8D-N7I_rvAx2N0llEbE6WYiBH0mr5&gsessionid=JG_SBLXiufwcJeFGO6aKVp9nNP6q_0K3nFzYcApyHPbcdIQbzFwExQ)  
  <sub>Benzinga, 3 hours ago</sub>  
  NVIDIA stock slid to a new 52-week low following Jensen Huang's abrupt departure. See how Amazon's Andy Jassy, Brad Gerstner, Jim Cramer, and fund managers...
- [The post earnings slide in Nvidia stock is getting uglier by the day](https://www.google.com/goto?url=CAESwgEBxCJF131T00k6sPNyX9m_9Mev3tNYH9Z_r0C9eWD5_JAwMnIInhK2INjFZvLxasWjAjozX9XNbqHGfh3ys3lNnpLJURDmtpffN-KLqzA-p1gg8c6NaFYmv54koyFsBnWPx8luwt3zeTuAZYliYHJYf_gQ9RcSVUSzhnxMMSh9Bhbx8MqXobqHWsZZ_SvKC7XO4LvoHZeMR6DQG7iHAOVKta2C5tkcbP860L92DlDSzdUq_S077KaFQ04UQx9EomwjMQ&gsessionid=JG_SBLXiufwcJeFGO6aKVp9nNP6q_0K3nFzYcApyHPbcdIQbzFwExQ)  
  <sub>Yahoo Finance, 3 hours ago</sub>  
  The Nvidia (NVDA) stock rout after earnings refuses to let up. Shares of the fallen AI chip darling are down more than 10% since the company's Nov.
- [The Stock Market Has Problems Even Anthropic Can’t Solve](https://www.google.com/goto?url=CAESiAEBxCJF16Yp-U9nKEZdCf-D42J9w1G2ySl2yrbMCpo57jXhkVYUa8EhLFmH59D466JQpECBDisVedQXz_8krx-CYzQmeELAiphXkqxFq86WQ2hVExqrK158vkkw-copSR3NN7GjtBV4i63aznoVu3u-lYHwiWz_1ZESLrnMyFHbgGCiMR6kBfxs&gsessionid=JG_SBLXiufwcJeFGO6aKVp9nNP6q_0K3nFzYcApyHPbcdIQbzFwExQ)  
  <sub>Barron's, 2 hours ago</sub>  
  Anthropic stock price, Nvidia, Micron, Sandisk all fall, and more things to know about the stock market today.
- [Nvidia and Micron Can't Make AI Chips Without This Growth Stock. Here's Why It Could Soar.](https://www.google.com/goto?url=CAESvwEBxCJF19N5O6NAfBHpotccHllo_vGw0cL9nLNz-7rxayyRpAVA31Bwx0_NgFM4g1_byxAHRwYcnFyt3en6S3LbkSXbVdSXcNmvipb6BmojPJlagxNAO3gZtMarBmNyFvVIQzyrSq-IxqvVkkgOtrYJq7VfJx1rVbDeO5cwzVyKL2qF8kko33sGxZaF811-_yF4bAhdqNE8SHV2AZGyR9oZLnWYxEMuYMwiue2ebXCqJqVIqEnk-oF1aP61BJKM_A&gsessionid=JG_SBLXiufwcJeFGO6aKVp9nNP6q_0K3nFzYcApyHPbcdIQbzFwExQ)  
  <sub>The Motley Fool, 2 hours ago</sub>  
  Nvidia (NVDA -3.30%) and Micron Technology (MU -2.10%) both make chips that are essential to the continued AI build-out, but their chips couldn't be more...
- [QUICK SPARK: Nvidia Stock Is Bleeding Like It's 2008](https://www.google.com/goto?url=CAESnQEBxCJF11ULgGPjCNytL78dsEl087lzFb41TXrePqfpAmgQkkyaKOYhA3Yma8yDWU_x2Nd4V4SZ19e6gStisL8YTT1pRv8LzVcQEQdzXo4P-uv3AEOTTTEyIapT7RRBUSTBjtLu_AyrVQw4CNtuSGkohIKrrGKMdsA3CgjC-DK2iQO5eZo7-znjILOnX05xR-gG5BPAY8wMFpllh_bd&gsessionid=JG_SBLXiufwcJeFGO6aKVp9nNP6q_0K3nFzYcApyHPbcdIQbzFwExQ)  
  <sub>Benzinga, 18 hours ago</sub>  
  NVIDIA Corp. (NASDAQ:NVDA) just reported revenue that more than doubled, but the stock keeps falling anyway. Shares are on track for a seventh straight...
- [‘Dean Of Valuation’ Says Nvidia Is 30% Below Fair Value, Waits For $140 — Calls Jensen Huang ‘Great CEO, But Human’](https://www.google.com/goto?url=CAESmwEBxCJF1w4NS2E8qZpLQvm81dZLesL6RioibUGClSTZu61sZ_bRdhlh-IA4xdYgvt_UQuHcf-gMjuCq6Gsd4RyQCxCG_MmA7M987QwwzRXZwG1Ou25DSM5t5QE1kNt4VMeJVmL8Z8_yK2sZoEdLgrgwolboohX2V4XAwDhpuop5ovNpUmKla48xX8ROopciu3dDYXVYG_DGJc97wg&gsessionid=JG_SBLXiufwcJeFGO6aKVp9nNP6q_0K3nFzYcApyHPbcdIQbzFwExQ)  
  <sub>Yahoo Finance, 6 hours ago</sub>  
  Damodaran said he would buy NVDA if it drops below $140. Nvidia's market capitalization has shrunk by more than $2 trillion to $3.52 trillion since Haung...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>Price and chart</b> — score n/a</summary>

```text
Last close 139.49 (bar of 2026-11-20), from 502 daily bars
Trend: vs 20d SMA 182.15 (-23.4%), 50d 207.28 (-32.7%), 200d 203.42 (-31.4%); 50d above 200d
Momentum: RSI(14) 17.9 | MACD -18.719 vs signal -14.982 (histogram -3.738)
Returns: 1d -4.4% | 5d -14.3% | 1m -34.3% | 3m -33.1%
52-week range: 139.49 - 239.24 (now 0.0% of the way up)
Volatility: ATR(14) 9.65 (6.9% of price) | annualised 20d 50.5%
Volume: 0.23x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score n/a</summary>

```text
Sector: Technology / Semiconductors | market cap 3.37T
Valuation: trailing P/E 14.98 | forward P/E 8.40 | P/B 12.61 | PEG 0.18
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
Price target: mean 246.67 (+76.8% vs last close), range 130.00 - 425.00
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

<details><summary><b>Who is positioned how</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>Money going into and out of this fund</b> — score n/a</summary>

_Not available today._

</details>

### Procter & Gamble (PG) · Company — no answer, no confidence given

<details><summary><b>News</b> — score n/a</summary>

- [Procter & Gamble Plans up to 30% Supply Job Cuts by 2030, Aims for $10 Billion in Cost Savings](https://www.benzinga.com/trading-ideas/movers/26/11/63467356/procter-gamble-plans-up-to-30-supply-job-cuts-by-2030-aims-for-10-billion-in-cost-savings)  
  <sub>Benzinga, 2 hours ago</sub>  
  Procter & Gamble Company (NYSE:PG) stock edged slightly higher during Friday's premarket session after closing roughly 1.4% lower after the consumer goods...
- [Procter & Gamble plans to use AI and automation to free up cash (PG:NYSE)](https://seekingalpha.com/news/4674720-procter-gamble-plans-to-use-ai-and-automation-to-free-up-cash)  
  <sub>Seeking Alpha, 2 hours ago</sub>  
  Procter & Gamble (PG) is in the spotlight after the consumer products giant unveiled a renewed cost savings program during its Investor Day event on...
- [PG Dec 2026 142.000 put (PG261204P00142000) interactive stock chart – Yahoo Finance](https://www.google.com/goto?url=CAESeAHEIkXXvOHltoGpfuCn3uqSueRslbbWBe_LiW-THRBW15d9PwJNjBFSYM1UFivbkQf8oms2ADk4-qnfYdrL1V6UaAKtkz-3gUz5Qi7_JMRz_3J5_h_Hwutmly1BMDFiMFXLNnXANJZR9IgMmxPpeRliPeDJs75wGA&gsessionid=b2T66WDXDNQP6ZmdjQ-3WKAvw0JG8lZNqfr2UlknA554UMmeg0CdCQ)  
  <sub>Yahoo Finance Singapore, 2 hours ago</sub>  
  Interactive chart for PG Dec 2026 142.000 put (PG261204P00142000) – analyse all of the data with a huge range of indicators.
- [Procter & Gamble Company (The) $PG Stock Position Trimmed by USS Investment Management Ltd](https://www.google.com/goto?url=CAES0AEBxCJF15-qsXdBTGjRyEf0ZHiN7EcIrbwtRfadr8cftnBl6OJgEsBRLBT3rySKrGOd2UiIaDZ7Ks80y52GFF1o64vZcCztiOhPKlkDb6WlxDSZqAFWmK1OadqPq3zvuWufLBOzwqzhaSjokxvsaBPDPBWprQi7EPohNPJU7Cc5pts-5RI4tjJpaFa-a8QDSkzfBZp5CP0cxPvoYaU5LbasqCASLB-sKOeKOZNL8J-OiGWQGGo-1gMKyQlZMYyHWNlEv56OWSyMqpa7nlXiWcn3&gsessionid=b2T66WDXDNQP6ZmdjQ-3WKAvw0JG8lZNqfr2UlknA554UMmeg0CdCQ)  
  <sub>MarketBeat, 3 hours ago</sub>  
  USS Investment Management Ltd decreased its position in Procter & Gamble Company (The) (NYSE:PG - Free Report) by 11.4% in the 3rd quarter, according to its...
- [Can Procter & Gamble (PG) Justify Its Price As Valuation Views Split?](https://www.google.com/goto?url=CAESwAEBxCJF16tlKCpmionohpihyj1TccanxLqjL3c-tVIi-MS9EZv6dQDa3rfRznUwN2-exbNmwJvUnZp09uTp76UlbbHVr1kpe7eBjPXfhMHm64HcrdqYBaWZ5XmR-FiHFDL_CdIlP_jmeLiQtWWBeYX3Mu5mNNKEF4Duhfsj292d9SWq3_P0LHHO_ZYqC5ynzo5oxRUMgFIz4BwXB295JRiCX0Y2f1b8cDWqqbn5qqnJqt341P743sdQc1YL361vgmk&gsessionid=b2T66WDXDNQP6ZmdjQ-3WKAvw0JG8lZNqfr2UlknA554UMmeg0CdCQ)  
  <sub>Simply Wall St, 34 minutes ago</sub>  
  Procter & Gamble (PG) just rolled out the limited-time Old Spice Holidudes Collection, a seasonal grooming lineup aimed at holiday shoppers that gives...
- [Is PG Worth Buying as Growth Improves but Its Valuation Stays Rich?](https://www.google.com/goto?url=CAEStwEBxCJF106TI9xRlmFGX1ie0tXLaNhAmo0boAyLN8wneaGGFkSbQXQh4l2Ase6muwE7_B44qJZwsaysKyOwZ4Y2vsv5fZ2SzhbcnfZyR2Za2WXxe8D-qAhA2cIIzfjk8kVANA5bJmLXkQdSffE5sJEw0xDLHvA7S0yjknBfMP4lzjwDgztmy9p0hijhaA_q_sYWHEMRUf1ZAUhs96PAUuXmc885ni7EJuzAcOzvxzRdpeac8iscZso&gsessionid=b2T66WDXDNQP6ZmdjQ-3WKAvw0JG8lZNqfr2UlknA554UMmeg0CdCQ)  
  <sub>TradingView, 23 hours ago</sub>  
  The Procter & Gamble Company PG is showing better operating momentum, but the investment case remains balanced. Fiscal first-quarter organic sales growth...
- [PG Jumps 17.4% in Three Months as Investors Weigh What Comes Next](https://www.google.com/goto?url=CAESkQEBxCJF15E8Y_-yo4ysJBzbQpzN9iBvny1XjIa9Lw5oYBfR_CYERm0apnrdv_t9jKG_0xiNRpi2kaPiwmU4lwdRoOPv_XkqB531bdsyg7qdqgX0x3WHO3LDzr4FklMteW-E4M6j8hPqXEcPFNbCN99btqtf97Py74hKVDml3ItXeX-RQF9QONOIAeYhG2etonHN&gsessionid=b2T66WDXDNQP6ZmdjQ-3WKAvw0JG8lZNqfr2UlknA554UMmeg0CdCQ)  
  <sub>Yahoo Finance, 23 hours ago</sub>  
  The Procter & Gamble Company PG shares have gained 17.4% over the past three months, while the Zacks Consumer Products - Staples sub-industry declined 0.3%.
- [How Are Raised Guidance and Cash Returns Shaping P&G (NYSE:PG) Today?](https://www.google.com/goto?url=CAESqQEBxCJF16R7aZZAeCPtkOSAa9b46ie5BQAYD6oQJp3pT0ermZjilwrwJijzIVbT3gFxYRL6BrseJQWUPG970vw67ThaV5gqcwXlkdWuVUBQPleBkDM2gnIPXTgjiG-cLNRidwtDn8ZzD2zUl2rPduZsTHlVYoYSmF5wZfEqwxgwSecuxpQbKiq5VyCE9whB_JoF3kcwLgfLDMWcFcL_6o8JFWCjvIH5ywfK&gsessionid=b2T66WDXDNQP6ZmdjQ-3WKAvw0JG8lZNqfr2UlknA554UMmeg0CdCQ)  
  <sub>Kalkine Media, 9 hours ago</sub>  
  Procter & Gamble (NYSE:PG) draws attention as the consumer-goods group lifts its guidance and widens its cash-return plans on volume-led organic sales...
- [PG Raises Sales Outlook as Thorne Acquisition Adds Growth Potential](https://www.google.com/goto?url=CAESuAEBxCJF1xmBl543BVwZtUgE0WAd3xf7jY8Zxyfeh8D_ZyJ7v_9TmSYbk8X0ubQzwNV-0UYZqAJWyru7Cb9Anxu3L-PQo9G6RpOHyVp7y7-eN8KOXgSSuP63cLv7o_gtX1sCyVsSA6G1bsds70LR6KT0t8M0wTc6BvrRExZnvNk4W_svnym7uHY7jAITrprdTjVPxLyz_wtrm1Xm7yZtNnKVw1y242QpyU8cKO4dTU6HSQE0shTCEQsi&gsessionid=b2T66WDXDNQP6ZmdjQ-3WKAvw0JG8lZNqfr2UlknA554UMmeg0CdCQ)  
  <sub>TradingView, 23 hours ago</sub>  
  The Procter & Gamble Company PG raised its fiscal 2027 all-in sales growth outlook after completing the Thorne acquisition, adding a new source of reported...
- [263,227 Shares of Procter & Gamble Company (The) $PG Bought by Advisors Asset Management Inc.](https://www.google.com/goto?url=CAES0QEBxCJF19aSq64Z6Wi3puLaSonYQEcW6IX08LamYLvXqhrtrv15oT2xq3d0VNraSUi7plcsZtD_590ixzWd89F6hE7lXyT_LzEmfupj-jpuv1bOwpsQE4qDYlJJOuXWSCw0_UgJxrZBG1zSGCR56UF0qmdWzUAqA1oBaGM97c-zP96tm129n7s5VBb_4wIbnktKxTWmh7D1ge8wGn4UNAIgn15TQmCgPRhtNOxuN2brgxizeaJbEjhpn7FPb2vUQu_HLRBptQfBrg0DTaEFxVL9ug&gsessionid=b2T66WDXDNQP6ZmdjQ-3WKAvw0JG8lZNqfr2UlknA554UMmeg0CdCQ)  
  <sub>MarketBeat, 6 hours ago</sub>  
  Advisors Asset Management Inc. purchased a new position in shares of Procter & Gamble Company (The) (NYSE:PG - Free Report) during the third quarter,...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>Price and chart</b> — score n/a</summary>

```text
Last close 171.32 (bar of 2026-11-20), from 502 daily bars
Trend: vs 20d SMA 166.08 (+3.1%), 50d 156.88 (+9.2%), 200d 150.27 (+14.0%); 50d above 200d
Momentum: RSI(14) 63.7 | MACD 3.996 vs signal 4.158 (histogram -0.162)
Returns: 1d +2.1% | 5d +0.9% | 1m +3.5% | 3m +16.9%
52-week range: 138.04 - 173.02 (now 95.1% of the way up)
Volatility: ATR(14) 3.22 (1.9% of price) | annualised 20d 20.4%
Volume: 0.14x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score n/a</summary>

```text
Sector: Consumer Defensive / Household & Personal Products | market cap 397.07B
Valuation: trailing P/E 25.80 | forward P/E 23.07 | P/B 7.31 | PEG 4.32
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
Price target: mean 174.78 (+2.0% vs last close), range 151.00 - 190.00
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

- [Samsung keeps co-CEOs, names new memory, mobile, system LSI heads](https://www.kedglobal.com/leadership-management/newsView/ked202611200002)  
  <sub>KED Global, 6 hours ago</sub>  
  Samsung Electronics Co. retained co-Chief Executives Jun Young-hyun and TM Roh in its annual executive reshuffle on Friday, while naming new heads for...
- [DataMeds AI (MEDS) Stock Surges Over 55% After Hours: Here's Why](https://www.benzinga.com/markets/equities/26/11/63463799/datameds-ai-shares-surge-after-hours-todos-medical-cancer-diagnostics-deal)  
  <sub>Benzinga, 10 hours ago</sub>  
  DataMeds AI shares surged 55.28% in after-hours after announcing an acquisition deal for cancer diagnostics assets from Todos Medical.
- [S&P 500 logs worst losing streak in 2 years as Anthropic’s hyped debut fails to spark a turnaround](https://www.google.com/goto?url=CAESmgEBxCJF19iCMwI14eATDwg0rCs6MWTiAL202lKp9pJsqGnwd0VKQXgyro9tm-CdcsdvHWZaiabuurEyF8_JeW87tel5YVExzPo8ntbLpweZUkFD7HRTvWJcn6BOanIddLGyxjDWkH0ofnlJALJ5Gle1W9XX7JxAGNVGwpS1EqprtGLqeAmC2H66t9e-wvv7V-qpyYZ2a_S59ZzF&gsessionid=lImzBqxr-a-T4UE6zNXPr26bHEFBv8ohx6c2_Vae6xYZxbYGxQHFvw)  
  <sub>Business Insider, 17 hours ago</sub>  
  Even the largest IPO in history couldn't stop the AI trade from tumbling lower this week. US stocks initially jumped on Thursday amid the massive hype for...
- [(SWIN) Equity Market Report (SWIN:CA)](https://www.google.com/goto?url=CAESkAEBxCJF12DNP9Kc4P6v3zjAnTSXszFdfviuUBeXRu9J2vft_9ksowF-Uy3j5Ukl49hFtNKHb6ysArFhdiPgOaaCUWwKCVihWWp3JVd-LspubpFDi-JlwWDRnARWoBv9vxqKbckdbNhED6YYrf4bqW4ZDPKcKagjUW18KnpnPqPObrw4b2YjU1N1xWSdstD9N0w&gsessionid=lImzBqxr-a-T4UE6zNXPr26bHEFBv8ohx6c2_Vae6xYZxbYGxQHFvw)  
  <sub>Stock Traders Daily, 9 hours ago</sub>  
  Equity Market Report for HAMILTON CHAMPIONS TM Enhanced U.S. Dividend ETF (SWIN) with Buy and Sell Signals.
- [First Phosphate and Zeo Energy Interviews to Air Nationally on the RedChip Small Stocks, Big Money(TM) Show on Bloomberg TV](https://www.google.com/goto?url=CAES1AEBxCJF1-8316gZcUs-Y7MXcNoz9dRB0Zzbpal3tg4qOqS7eGsr2LBMnClIYcwBoy9r9ZzrgIoh3iFeBH5Ufeg8eo0NfILYpEY4C1Oddich8e9jPwXKRlor7o7OYNKh7QSwCJtmycC5EzK0s2n0eiXz2PYV0R4he84d_JYyfaGA2vumM6F9qSliy_udJXnYELl46wyPaUtvXPzntYhVXlMWi_KNg-G1hpZibAoS7FPdT4eMWmN2SJudsW3_cyv7f6qeP2KDPeOVhHdQhp-P9SDgOuXV3g&gsessionid=lImzBqxr-a-T4UE6zNXPr26bHEFBv8ohx6c2_Vae6xYZxbYGxQHFvw)  
  <sub>ACCESS Newswire, 42 minutes ago</sub>  
  ORLANDO, FL / ACCESS Newswire / November 20, 2026 / RedChip Companies will air interviews with First Phosphate Corp.
- [(SMVP) Advanced Trading Insights (SMVP:CA)](https://www.google.com/goto?url=CAESlQEBxCJF11TBhfdkjYEF3_XH5kJxM2igRan3WjlFjq1Hk2Wr0F7FGjpBYqAriUA1oKia5rTNyg0Luw9FdYSWFun0NYdDzOsE5pB4ZnGh-77t740FJMNSwGdgbwAltCdsBIvEIKCbEt9dECmjhdckxp0JuDh_9m53oj4q_FU00P9ARBFQL7SXq0PxaBYyoWpLext7JB6ExA&gsessionid=lImzBqxr-a-T4UE6zNXPr26bHEFBv8ohx6c2_Vae6xYZxbYGxQHFvw)  
  <sub>Stock Traders Daily, 9 hours ago</sub>  
  Advanced Trading Insights for HAMILTON CHAMPIONS TM U.S. Dividend Index ETF (SMVP) with Key Buy and Sell Signals.
- [Indian Stock Market News, Equity Market and Sensex Today in India](https://www.google.com/goto?url=CAESiAIBxCJF1yy5Xq8vnsrc1MLMAJHbyul56Jxyy6QeLVMMumKe0wu8SqMo2grHfMN5HL0u3EHvSEIDsgr15M15oejoEC4zRLIcRdTKWs9lwSr3xcg8e81iu_QjSj2m-1UT8_hU5ylNNAbnIDzqhE5wvfbqrh8siq-o4GoI_LUO2flXp3ABCBKP7LgTuLFF82gZGNfLzxZi79MVvP1InTrlMN0N1kfKw6quJfeiVl-R4lLpA8k-Z1FkLuVkktmh_sRuG0LZuov-G_GsPrneHgo4B2w9LGy66bNa9vuZv6nOAd255zo06SwaNKBEgQXkOXE-svk6mXPU5WqH2LWLBdnm95JM1coKPKkB5i4&gsessionid=lImzBqxr-a-T4UE6zNXPr26bHEFBv8ohx6c2_Vae6xYZxbYGxQHFvw)  
  <sub>Equitymaster, 14 hours ago</sub>  
  Top cues to track in today's stock market session.
- [When (CWIN) Moves Investors should Listen (CWIN:CA)](https://www.google.com/goto?url=CAESngEBxCJF1wpC3EcrFNQmHwUmSUtc4Aaqit8lYWqvYOdh7LAiQrk5r_xueAzDRSQr6qFtGdcidW1wALAlQ2vchkHaAbX-k1cdcPV3UAQawmZ4a6ACoBqgjvh6a-bx0mqH5hosLAVzytiepPC_35Iw0ybYwQwvJutd-jyL-q4lrch6eH-oDfH_BffjBmy_lHyx0oozuc-RNrgO0F5gXf0epw&gsessionid=lImzBqxr-a-T4UE6zNXPr26bHEFBv8ohx6c2_Vae6xYZxbYGxQHFvw)  
  <sub>Stock Traders Daily, 9 hours ago</sub>  
  When HAMILTON CHAMPIONS TM Enhanced Canadian Dividend ETF CWIN Moves Investors should Listen.
- [(CMVP) Trading Advice (CMVP:CA)](https://www.google.com/goto?url=CAESigEBxCJF16Z73TZL4yfqSJnCTabMGgyn9QMT-8MG6meq5XE5qFXS9zNQ4C_5mWnjw6vLft0GmJQUSnw5LjZcQRM2V-l5oP24Y5dwg26TFw5krXFNCepu-9Y5qABHYDfE_DB4qUoCqEfAhBUUyYpbpOtQlSBLUamk84TyUz1emOklAad-fc4x335HHt0&gsessionid=lImzBqxr-a-T4UE6zNXPr26bHEFBv8ohx6c2_Vae6xYZxbYGxQHFvw)  
  <sub>Stock Traders Daily, 9 hours ago</sub>  
  Trading Advice for HAMILTON CHAMPIONS TM Canadian Dividend Index ETF CMVP including day trading swing trading and long term investing plans for CMVP.
- [Jaguar Health, Inc. Announces Reverse Stock Split](https://www.google.com/goto?url=CAESrAEBxCJF1zmLRQXt-vEoD0WJFE0TeixDi2J1CygysYtQoJX4L8zbu5fvbqIVzPXx8ThLgKtQSlApkB5DyVFEIugmPiuhLA7otCOl4BfHm2mFbb-Ep-Bnip3znvOazAkBIVIM4Mu7ePCzoje6YUKWLLsR7V0OSlFxbbQ77kaLZXO5m9TyWiBIn0oIQueaMviHWyPCehSpoXbae4FmnU1x9D27Oh9jTHghzCihpIuy&gsessionid=lImzBqxr-a-T4UE6zNXPr26bHEFBv8ohx6c2_Vae6xYZxbYGxQHFvw)  
  <sub>The Des Moines Register, 16 minutes ago</sub>  
  Reverse split approved at November 2026 Special Meeting of Stockholders. Shares of Jaguar Health common stock to begin trading on split-adjusted basis on...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>Price and chart</b> — score n/a</summary>

```text
Last close 210.04 (bar of 2026-11-20), from 502 daily bars
Trend: vs 20d SMA 206.53 (+1.7%), 50d 196.58 (+6.8%), 200d 197.35 (+6.4%); 50d below 200d
Momentum: RSI(14) 57.9 | MACD 4.812 vs signal 5.200 (histogram -0.388)
Returns: 1d -0.4% | 5d -1.1% | 1m +6.0% | 3m +8.4%
52-week range: 166.50 - 248.29 (now 53.2% of the way up)
Volatility: ATR(14) 4.05 (1.9% of price) | annualised 20d 38.7%
Volume: 0.09x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score n/a</summary>

```text
Sector: Consumer Cyclical / Auto Manufacturers | market cap 246.51B
Valuation: trailing P/E 9.58 | forward P/E 13.31 | P/B 16.72 | PEG 19.73
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
Price target: mean 238.08 (+13.3% vs last close), range 230.00 - 253.00
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

- [Angola's ANPG says Exxon takes $4 billion FID on Kizomba fields, makes discovery](https://www.reuters.com/business/energy/angolas-anpg-says-exxon-takes-4-billion-fid-kizomba-fields-makes-discovery-2026-11-20/)  
  <sub>Reuters, 2 hours ago</sub>  
  Exxon Mobil and its partners in ​Angola's offshore Block 15 have taken a ‌final investment decision on a $4 billion redevelopment of the Kizomba A and B...
- [ExxonMobil Holdings (XOM) Gets Mozambique Approval For $30 Billion Rovuma LNG Plan](https://finance.yahoo.com/energy/articles/exxonmobil-holdings-xom-gets-mozambique-211612645.html)  
  <sub>Yahoo Finance, 17 hours ago</sub>  
  ExxonMobil Holdings (NYSE:XOM) secured Mozambican government approval for its redesigned Rovuma LNG project, a roughly US$30b development.
- [Here’s How Much You Would Have Made Owning ExxonMobil Holdings Stock In The Last 5 Years](https://www.google.com/goto?url=CAESuwEBxCJF14aBFB8zQVx70P2Q9W3EyEkPiboHv4W97DaYULAoMQHd26xsfJm3d78GwLW32xJ88ya-Gh9ZNR3sCyc53lojlmvoq8ekDNj3HFFHEP5Cv3mWYWaozaKGVuBTtUp4C2rX-TUtGKlharf2jdWqnJks38n5WOWIqMcUFjMs0dw2XYSh-lYduyj8Y1Ghh_YuNRE4iux2q9MP-Ab1KLqWr4mCtzqe-FTHrn3IbSdfA44Uda5zeFkmGozM&gsessionid=uM_Bp84nvc70zS6UrO21HNZOmuN33mRwm79OWUPoECZ5DxZWxMesNw)  
  <sub>Benzinga, 18 hours ago</sub>  
  ExxonMobil Holdings (NYSE:XOM) has outperformed the market over the past 5 years by 11.41% on an annualized basis producing an average annual return of...
- [How XOM's Strong Balance Sheet Helps Manage Oil Market Volatility](https://www.google.com/goto?url=CAES1QEBxCJF13Jc_q3rhRe7iAnBAvnkfbVAwQ4FAY0vRFnNxnjHvNUMjcmHQmDGcK5dyv2-pQWLabwbN9xWAlt_h105cOYe8NLjZi2suz_C-IaQ2QvVqQC5WpjphJUJQdzrhm2SYcjWfWiXCqfbtdqfoEolV7RDD75XNpbYcB4FP5IeVnVllkT-loUjfiBZvPa1BgndUJG7hvl1lzpl4HFxF8S2jwrk_9u_tOh7xUE6HsRKazbxO3VGqNIRr5bgls3y7Gow9MslnVUQvE1W2XjjacTt0QL9UvI&gsessionid=uM_Bp84nvc70zS6UrO21HNZOmuN33mRwm79OWUPoECZ5DxZWxMesNw)  
  <sub>The Globe and Mail, 11 hours ago</sub>  
  ExxonMobil Holdings Corporation XOM, an integrated energy giant, generates the bulk of its earnings from its upstream operations. With a strong presence in...
- [Elliott Wave view: Exxon Mobil (XOM) shows bearish sequence with downside objective near $144 [Video]](https://www.google.com/goto?url=CAESyAEBxCJF17MYRINcrEZv28IvlOo0Pz6Zdo4XJJWuz8mEMIDV7liYF2a0MQxc4WAk7f65M6cbsveDHParG7g319nj_7A0V-ru0o4LQjFGtOZKnlxbyrdXVjbw_7vEuWcWdwIdVEQkGWzCYPTej9zi6GQpGGNO6OX68VCWQWmkykQ0ythBGAMnBnUX5A8_n95I5T5_KRqK-wlqoTJHTlIjITKiQX26tOHsxOGG9G7nMtkN2SSpxs4PgHoCdjEhLJMPLKh6p869MUIopg&gsessionid=uM_Bp84nvc70zS6UrO21HNZOmuN33mRwm79OWUPoECZ5DxZWxMesNw)  
  <sub>FXStreet, 10 hours ago</sub>  
  Short-Term Elliott Wave analysis of Exxon Mobil (XOM) continues to favor further downside following the peak registered on October 30, 2026. The stock...
- [Exxon’s revised $30B Rovuma LNG plan approved by Mozambique's government (XOM:NYSE)](https://www.google.com/goto?url=CAESqQEBxCJF1_DHmKwgbC7ozjiDkIpwtE9lphCwV4uAANYz5YcpM8emXLiARBMxbzm9eRz4aTCCl1l6-7K3E_pxL6pVb_ayaKRgouVNcDjTZAp14-GekSrZ47OHWDZJpkCYTvZLAePI6bSnGwegF4yTSojUUPTkPMbzn6li8dGUr6XE3mKl6FNfAzkSTtGOX1d9JLeXmHFKn6gnuhQ5jujUPf0mVVN3p0cLW5JA&gsessionid=uM_Bp84nvc70zS6UrO21HNZOmuN33mRwm79OWUPoECZ5DxZWxMesNw)  
  <sub>Seeking Alpha, 20 hours ago</sub>  
  ExxonMobil's (XOM) revised development plan for its Rovuma liquefied natural gas project was approved by Mozambique's government this week, clearing a key...
- [Xometry, Inc. (XMTR) Stock Price, News, Quote & History](https://www.google.com/goto?url=CAESZQHEIkXX2j5yT5R2MxHxjbwSHlsTpep3Uh3wjNgSIbc50-Ctdx1i-7aceQLyJk1g55mosTOdNLPHX95ldl1OnrrK6RtTUEc8tgw3_e6uhF4w2mlJshjtl9kwExTQJnj-oJm6Ngzr&gsessionid=uM_Bp84nvc70zS6UrO21HNZOmuN33mRwm79OWUPoECZ5DxZWxMesNw)  
  <sub>Yahoo! Finance Canada, 9 hours ago</sub>  
  Find the latest Xometry, Inc. (XMTR) stock quote, history, news and other vital information to help you with your stock trading and investing.
- [Energy Stocks And Industry News: Oil, Gas, Solar, Coal And Nuclear Energy](https://www.google.com/goto?url=CAESxgEBxCJF12ahbfqR2eA41Kj4EU1HZjQHm4pX9I6lx2ZuxeVKczlsKbr_dw1m2VfXl5BGfXGgAzdR0ZEndgf8Z9mFxnH8jdNEwLKk065t29p2rA05Y5Nh_tSYwhpp3oaOKoQiYId6slr0NKSh9ZKtNinPvggMD18wjadfK1PhVrPgIKfDJALW46_J68S8y3U6UqC1WYyhA00ovBc4uA9dd1XIgwE5YKuTEVTGzi0-_YpVL43EjLcu8pRd3aWc0tUcTH68yIlvRbE&gsessionid=uM_Bp84nvc70zS6UrO21HNZOmuN33mRwm79OWUPoECZ5DxZWxMesNw)  
  <sub>Investor's Business Daily, 21 hours ago</sub>  
  Track the latest news, trends and analysis on oil stocks and energy industry news.
- [ExxonMobil (NYSE:XOM) Shares Down 1% - Should You Sell?](https://www.google.com/goto?url=CAESqgEBxCJF1z10Le6YWl8ZT9vSW2uroDcB7vA4S4SFRbsyVUGCFPjit-2LC7_C8GUwxwUuuO0Ms5ejl4vTL-FkyOkxuvzjz34CJwWPlNQgTrK6IGRBAS3ufruBqnnPBeR6cG0IihYsROsjWJU6ceRVAifS-L0UApZWOeeERs4wcSWdTa6i5qYfTYE4e97SlxwcTaqjcM7g4R0hshI0JgY8O_8JFyRAD6OpyvekeA&gsessionid=uM_Bp84nvc70zS6UrO21HNZOmuN33mRwm79OWUPoECZ5DxZWxMesNw)  
  <sub>MarketBeat, 16 hours ago</sub>  
  Shares of ExxonMobil Corporation (NYSE:XOM - Get Free Report) traded down 1% during mid-day trading on Thursday. The company traded as low as $158.60 and...
- [How Did ExxonMobil (NYSE:XOM) Deliver a Disciplined Quarter This Time?](https://www.google.com/goto?url=CAESqgEBxCJF1_-90qrwPftyCdojPFG2SyvwyN_71gR_1KEiyFaqcCq2h9XMPkxfgm91sjCdgf5opHJ66olIkp015nCPdG7_Tw34YUMbWVEUoI5AjsB1C__ZfTEhON61A4VnolSjGDlKYKQiw8yxijy42ieQMX8KGH5ryPpzsLZp7cQbeoiU-7A0cdirnKxbLM2MFSEV5goyDlmjmX-KRy5H1-6tQKFfH9tXUJoFfQ&gsessionid=uM_Bp84nvc70zS6UrO21HNZOmuN33mRwm79OWUPoECZ5DxZWxMesNw)  
  <sub>Kalkine Media, 8 hours ago</sub>  
  ExxonMobil (NYSE:XOM) moved into focus after third-quarter results spotlighted disciplined spending, rising Permian and Guyana volumes, and steady operating...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>Price and chart</b> — score n/a</summary>

```text
Last close 158.70 (bar of 2026-11-20), from 502 daily bars
Trend: vs 20d SMA 171.16 (-7.3%), 50d 169.31 (-6.3%), 200d 156.84 (+1.2%); 50d above 200d
Momentum: RSI(14) 34.0 | MACD -3.051 vs signal -1.357 (histogram -1.694)
Returns: 1d -0.1% | 5d -7.0% | 1m -11.0% | 3m -3.3%
52-week range: 114.51 - 187.25 (now 60.8% of the way up)
Volatility: ATR(14) 4.09 (2.6% of price) | annualised 20d 31.8%
Volume: 0.12x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score n/a</summary>

```text
Sector: Energy / Oil & Gas Integrated | market cap 647.37B
Valuation: trailing P/E 16.33 | forward P/E 12.71 | P/B 2.44 | PEG 1.25
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

**In the model's own words:** no explanation. It wrote only “Neutral”, so the main reasons below are all it gave.

**Main reasons it gave:**
- Technicals: price below 20‑day SMA (26.55) and 50‑day SMA (27.65), RSI 32.8 (oversold) but volume only 0.06× 20‑day average
- Macro: US dollar index up to 103.69 and VIX up 10.2 points to 29.46, indicating risk aversion and pressure on commodity prices
- Fund flows: flat share count change (0% over 1 week and 1 month), indicating no net demand shift
- Fund holdings: 47.9% cash and 49.6% other, with large short‑term Treasury exposure, suggesting de‑risking from commodity exposure
- Analyst view: no ratings or price targets for holdings (AGPXX, TBLL), providing no directional guidance

<details><summary><b>News</b> — score +0.00</summary>

_No news found for this one today._

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.14% (+0.02 on the week) | 5-year 4.78% (-0.20 on the week) | 10-year 4.99% (-0.17 on the week) | 30-year 5.37% (-0.11 on the week)
Yield curve, 10-year minus 3-month: +0.84 points -- upward sloping (normal)
US dollar index: 103.69 (+0.28 on the week)
Volatility (VIX): 29.46 (+10.2 on the week) -- stressed
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.1% (2026-10-01) | jobless claims 203k (2026-11-14)
Policy and expectations: Fed target 4.00% | market expects 2.2% inflation over 10 years
Rate path: 2-year Treasury 4.80% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 26.21 (bar of 2026-11-20), from 502 daily bars
Trend: vs 20d SMA 26.55 (-1.3%), 50d 27.65 (-5.2%), 200d 27.41 (-4.4%); 50d above 200d
Momentum: RSI(14) 32.8 | MACD -0.437 vs signal -0.470 (histogram 0.034)
Returns: 1d +0.0% | 5d -1.3% | 1m -6.1% | 3m -7.4%
52-week range: 25.44 - 29.49 (now 19.0% of the way up)
Volatility: ATR(14) 0.24 (0.9% of price) | annualised 20d 10.7%
Volume: 0.06x the 20-day average
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
Three-year record: +9.9% a year | beta to the market 0.37
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
Shares outstanding: 27.60M | fund size: 723.40M
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Developing country bonds (EMB) · Index fund — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> No policy surprise, technicals bearish but low volume, positive fund inflows, elevated VIX indicating stress but no decisive macro catalyst.

**Main reasons it gave:**
- Fund flows net inflows: +6% share count over past month
- Technical indicators bearish: price below 20d/50d/200d SMAs, RSI 34.8, MACD negative
- Macro: Fed target unchanged at 4.0% with no policy surprise
- VIX rose 10% week‑over‑week to 29.46, indicating market stress

<details><summary><b>News</b> — score +0.00</summary>

- [A Monthly Check at 3 Levels of Risk: VTEB, TLT and EMB, Ranked](https://247wallst.com/investing/etf/2026/11/19/a-monthly-check-at-3-levels-of-risk-vteb-tlt-and-emb-ranked/)  
  <sub>24/7 Wall St., 21 hours ago</sub>  
  A retiree's monthly bond fund check can stay steady while the share price behind it quietly collapses. Ranking three popular payers on both risks produces...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.14% (+0.02 on the week) | 5-year 4.78% (-0.20 on the week) | 10-year 4.99% (-0.17 on the week) | 30-year 5.37% (-0.11 on the week)
Yield curve, 10-year minus 3-month: +0.84 points -- upward sloping (normal)
US dollar index: 103.69 (+0.28 on the week)
Volatility (VIX): 29.46 (+10.2 on the week) -- stressed
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.1% (2026-10-01) | jobless claims 203k (2026-11-14)
Policy and expectations: Fed target 4.00% | market expects 2.2% inflation over 10 years
Rate path: 2-year Treasury 4.80% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score -0.20</summary>

```text
Last close 90.24 (bar of 2026-11-20), from 502 daily bars
Trend: vs 20d SMA 91.55 (-1.4%), 50d 91.68 (-1.6%), 200d 94.58 (-4.6%); 50d below 200d
Momentum: RSI(14) 34.8 | MACD -0.361 vs signal -0.196 (histogram -0.164)
Returns: 1d -0.1% | 5d -1.0% | 1m -1.8% | 3m -4.9%
52-week range: 90.14 - 97.74 (now 1.3% of the way up)
Volatility: ATR(14) 0.46 (0.5% of price) | annualised 20d 7.1%
Volume: 0.08x the 20-day average
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
Three-year record: +8.1% a year | beta to the market 1.06
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
Share count change: 1 week: +1.4% (191.05M) over 7d | 1 month: +6.0% (761.83M) over 30d
Shares outstanding: 149.72M | fund size: 13.51B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### US company bonds, riskier (HYG) · Index fund — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> No macro surprise, flat fund flows, technicals weak but no decisive break, fundamentals balanced.

**Main reasons it gave:**
- Fund flows flat: 0% share count change over 1 week and 1 month
- Technicals: price below 20‑day, 50‑day, 200‑day SMAs; RSI 37.8; MACD -0.221; volume 0.13× 20‑day average
- Macro: no policy or data surprise; Fed target unchanged at 4.00%; yields stable; VIX high but no new shock

<details><summary><b>News</b> — score +0.00</summary>

- [HYG Vs. HYGH: Hedging Works Here, Too (NYSEARCA:HYG)](https://seekingalpha.com/article/4970121-hyg-vs-hygh-hedging-works-here-too)  
  <sub>Seeking Alpha, 2 hours ago</sub>  
  Analyst rates HYHG ETF a Buy because rate hedging lowers historical volatility across periods, and HYG a Hold for investors who do not want to hedge.
- [How to Build $9,450 a Month in Dividend Income Without Selling a Single Share](https://247wallst.com/personal-finance/2026/11/19/how-to-build-9450-a-month-in-dividend-income-without-selling-a-single-share/)  
  <sub>24/7 Wall St., 21 hours ago</sub>  
  Generating $113,400 a year from dividends takes about $3 million at a 3.5% yield, $1.6 million at 7%, or roughly $1 million at 12%. A six-holding mix,...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.14% (+0.02 on the week) | 5-year 4.78% (-0.20 on the week) | 10-year 4.99% (-0.17 on the week) | 30-year 5.37% (-0.11 on the week)
Yield curve, 10-year minus 3-month: +0.84 points -- upward sloping (normal)
US dollar index: 103.69 (+0.28 on the week)
Volatility (VIX): 29.46 (+10.2 on the week) -- stressed
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.1% (2026-10-01) | jobless claims 203k (2026-11-14)
Policy and expectations: Fed target 4.00% | market expects 2.2% inflation over 10 years
Rate path: 2-year Treasury 4.80% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score -0.20</summary>

```text
Last close 76.57 (bar of 2026-11-20), from 502 daily bars
Trend: vs 20d SMA 77.12 (-0.7%), 50d 77.36 (-1.0%), 200d 79.23 (-3.4%); 50d below 200d
Momentum: RSI(14) 37.8 | MACD -0.221 vs signal -0.169 (histogram -0.052)
Returns: 1d +0.1% | 5d -0.5% | 1m -0.7% | 3m -3.9%
52-week range: 76.53 - 81.18 (now 0.9% of the way up)
Volatility: ATR(14) 0.28 (0.4% of price) | annualised 20d 5.3%
Volume: 0.13x the 20-day average
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

<details><summary><b>Buying and selling by company insiders</b> — score +0.00</summary>

_Not available today._

</details>

<details><summary><b>Who is positioned how</b> — score +0.00</summary>

_Not available today._

</details>

<details><summary><b>Money going into and out of this fund</b> — score +0.00</summary>

```text
Direction: flat (1 month)
Share count change: 1 week: +0.0% (0.00) over 10d | 1 month: +0.0% (0.00) over 30d
Shares outstanding: 195.60M | fund size: 14.98B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### US government bonds, 7-10 years (IEF) · Index fund — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> No material macro surprise, modest bearish positioning, flat flows, mixed technicals, and stable fundamentals lead to a neutral view.

**Main reasons it gave:**
- Fed target unchanged at 4.00% and inflation/unemployment data in line with expectations
- Positioning shows net short 37.8% with only +0.3% change, indicating modest bearish bias
- Fund flows flat over the past month, indicating no new demand
- Technical indicators mixed: price above 20‑day and 50‑day SMAs but below 200‑day SMA, low volume, no decisive break
- 10‑year Treasury yield fell 0.17% this week, easing pressure on bond prices

<details><summary><b>News</b> — score +0.00</summary>

- [Bond ETFs Haven’t Been This Rewarding in Years, So Why Is Wall Street Dumping Them?](https://finance.yahoo.com/markets/options/articles/bond-etfs-haven-t-rewarding-184149666.html)  
  <sub>Yahoo Finance, 20 hours ago</sub>  
  AGG is down about 1% over five years while TLT has lost 35%, as investors flee bonds just when the 10-year yields 5%. Eric Balchunas notes fixed income ETFs...
- [Treasury Bonds At 5%: Dividend Stocks Are Still Worth It](https://seekingalpha.com/article/4970220-treasury-bonds-at-5-percent-dividend-stocks-are-still-worth-it)  
  <sub>Seeking Alpha, 2 hours ago</sub>  
  The bull case for dividend stocks over 5% Treasury yields: dividend growth can boost long-term returns, and low valuations could add upside.
- [IEF Sep 2027 94.000 call (IEF270917C00094000) stock price, news, quote and history](https://www.google.com/goto?url=CAEScwHEIkXXyBMjhxfWSWs7WGN7oVmj_hRuc32NRzrk6nDEJ0De5tH9Ejq8JMrxBlvICHCpP9KEMUfd6SyMMjE3i8DDcJUXMN-20aw1CKkAU1hnjIb-sKefrAZXPqHGkrQ0Nc2fVTjTrr43vTJPx11mLbprVN8&gsessionid=JDT6esP1dYrH1R3RfI_-7rtEzQgfO32FcsEe8mqPPFRXbFPvWkRIFA)  
  <sub>Yahoo Finance UK, 24 hours ago</sub>  
  Find the latest IEF Sep 2027 94.000 call (IEF270917C00094000) stock quote, history, news and other vital information to help you with your stock trading and...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.14% (+0.02 on the week) | 5-year 4.78% (-0.20 on the week) | 10-year 4.99% (-0.17 on the week) | 30-year 5.37% (-0.11 on the week)
Yield curve, 10-year minus 3-month: +0.84 points -- upward sloping (normal)
US dollar index: 103.69 (+0.28 on the week)
Volatility (VIX): 29.46 (+10.2 on the week) -- stressed
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.1% (2026-10-01) | jobless claims 203k (2026-11-14)
Policy and expectations: Fed target 4.00% | market expects 2.2% inflation over 10 years
Rate path: 2-year Treasury 4.80% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 91.34 (bar of 2026-11-20), from 502 daily bars
Trend: vs 20d SMA 91.09 (+0.3%), 50d 90.47 (+1.0%), 200d 93.50 (-2.3%); 50d below 200d
Momentum: RSI(14) 56.7 | MACD 0.022 vs signal 0.062 (histogram -0.041)
Returns: 1d +0.6% | 5d +1.4% | 1m +0.2% | 3m -1.8%
52-week range: 88.92 - 97.99 (now 26.7% of the way up)
Volatility: ATR(14) 0.47 (0.5% of price) | annualised 20d 6.5%
Volume: 0.07x the 20-day average
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
Three-year record: +3.1% a year | beta to the market 1.17
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

<details><summary><b>Buying and selling by company insiders</b> — score -0.10</summary>

_Not available today._

</details>

<details><summary><b>Who is positioned how</b> — score -0.10</summary>

```text
Contract: UST 10Y NOTE - CHICAGO BOARD OF TRADE (positions as of 2026-11-10, published the following Friday)
Large speculators: net short 37.8% of open interest (6,095,194 contracts)
Change on the week: +0.3% of open interest
Crowding: 60% percentile over 52 weeks -- within its normal range
Read this as crowding, not as a forecast: an extreme is as often the end of a move as the middle of one.
```

</details>

<details><summary><b>Money going into and out of this fund</b> — score -0.10</summary>

```text
Direction: flat (1 month)
Share count change: 1 week: +0.0% (0.00) over 10d | 1 month: +0.0% (0.00) over 30d
Shares outstanding: 146.00M | fund size: 13.34B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### US small companies (IWM) · Index fund — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Neutral overall: bearish technicals are offset by neutral fundamentals and mixed behavioural signals.

**Main reasons it gave:**
- Technical downtrend: price below 20‑day, 50‑day and 200‑day SMAs; RSI 35.4; MACD negative
- Positioning: large speculators net short 10.1% of open interest, short position rose 2.2% week‑over‑week
- Analyst view: thin coverage (1.9% of fund) but all buy ratings with a +19.8% price target
- Macro: VIX up 10.2 points to 29.46 (stressed market) with no policy or data surprise

<details><summary><b>News</b> — score +0.00</summary>

- [If You Have $1,000 to Invest Right Now, Here's the 1 ETF I'd Buy Without a Second Thought](https://www.fool.com/investing/2026/11/19/if-you-have-1000-to-invest-right-now-heres-the-1-etf-id-buy-without-a-second-thought/)  
  <sub>The Motley Fool, 22 hours ago</sub>  
  If you're hesitant to pour new money into the stock market at this time, you're not alone. While still growing, the S&P 500's (^GSPC -2.02%) earnings growth...
- [Anthropic IPO Was a Success and a Nasty Trap for the Rest of the Market](https://pro.thestreet.com/market-commentary/anthropic-ipo-was-a-success-and-a-nasty-trap-for-the-rest-of-the-market)  
  <sub>RealMoney Pro, 17 hours ago</sub>  
  Investors who planned to sell into the strength never got the chance, and the result was a broad liquidation.
- [Invesco S&P 500 Equal Weight ETF (RSP) stock price, news, quote and history](https://www.google.com/goto?url=CAESZAHEIkXXp5IshkbTq0yQQVoe1wJ5xjPrwZZKXWwD0I-m45fbn-W5bLKoJHYi6YCtOq5eE-Toy7PxywyMviUakXeClDlWOvZyosmaVDijzKlLIs991YLr5bMz4jzJA3TC6SfKung&gsessionid=yS0foAfDoPc8LRYftP6tx8HivW0aE1gVHQxQ4Gooth8KEpOYJHc7kg)  
  <sub>Yahoo Finance UK, 22 hours ago</sub>  
  Find the latest Invesco S&P 500 Equal Weight ETF (RSP) stock quote, history, news and other vital information to help you with your stock trading and...
- [iShares Russell 2000 ETF (IWM) Price Prediction: Small caps slip back under key moving averages as momentum stays soft](https://www.google.com/goto?url=CAESlgEBxCJF1-E93rAtNGGzIftBfLKaZioq8Gg3jRGy8f08O1G4ShhVVm41qFYZtikSYNV96yLK_vZWpu_rzyFpndVERZqppDjLHkbvzHTNb5nBAAVuqkFPvac-5jQ7i1iOqd3SdLF4kj4muxw_PvDSHXuk9izKeJPZeiMbfJDY_ieAOdk9a-ZP-Dy4w8zV7krB31Pxq0J_WmM&gsessionid=yS0foAfDoPc8LRYftP6tx8HivW0aE1gVHQxQ4Gooth8KEpOYJHc7kg)  
  <sub>Blockchain News, 4 hours ago</sub>  
  iShares Russell 2000 ETF (IWM) is trading at $265.00, down 2.57% over the last 24 hours, with price sitting below its 7-, 20- and 50-day moving averages...
- [iShares Russell 2000 ETF (IWM) Price Prediction: Small-cap ETF slips back under short-term trend as selling pressure outweighs the bounce](https://www.google.com/goto?url=CAESlgEBxCJF16BhEj5Dm39MB56XudaYw7Kts-bc2AHgMBvP3FQbTiE1KSHUysgKYufr91b2Bx8hQTlTAnd6HEM3B96GZZUPWfwQ0SDY_YxpwkpZupof2WHdAGfENw1mTt5Q0kqIMZ_keMtadTXEfUBW9XgzIGnEyd7MmquHBeo5MjASzo-CcwQ-mBVQXqePdt5M3WRkdd8evFA&gsessionid=yS0foAfDoPc8LRYftP6tx8HivW0aE1gVHQxQ4Gooth8KEpOYJHc7kg)  
  <sub>Blockchain News, 21 hours ago</sub>  
  iShares Russell 2000 ETF (IWM) is trading at $272.37 after a 1.05% 24-hour gain, but the ETF remains below its 7-day, 20-day and 50-day moving averages...
- [SanDisk (SNDK) Stock Price Prediction: Selloff collides with heavy positioning and mixed support from analysts](https://www.google.com/goto?url=CAESpAEBxCJF19nCnwkXVBkx2GMSQ6046YcZxt4LDx5TSyJCJkpNVCnI-ks684R-Xza92UdOcVXqf-xt2jyapOifH1tCRPZtRd5nLyGMLKCV3GMUe4zdF8YOjmJf1mmFN4wxR2NOZtSYI9Or6tzZ1mKivh50v2c9c5EnYBMChLyFDy5DFiFD34GVW-PR2TsuIh0aRkS3SXc5614MnvWWPKIGxE3fiz-cOA&gsessionid=yS0foAfDoPc8LRYftP6tx8HivW0aE1gVHQxQ4Gooth8KEpOYJHc7kg)  
  <sub>blockchain.news, 4 hours ago</sub>  
  SanDisk (SNDK) is trading at $89.67 after a sharp 24-hour drop, with Binance Futures showing heavy volume, a bearish moving-average stack, and deeply...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.14% (+0.02 on the week) | 5-year 4.78% (-0.20 on the week) | 10-year 4.99% (-0.17 on the week) | 30-year 5.37% (-0.11 on the week)
Yield curve, 10-year minus 3-month: +0.84 points -- upward sloping (normal)
US dollar index: 103.69 (+0.28 on the week)
Volatility (VIX): 29.46 (+10.2 on the week) -- stressed
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.1% (2026-10-01) | jobless claims 203k (2026-11-14)
Policy and expectations: Fed target 4.00% | market expects 2.2% inflation over 10 years
Rate path: 2-year Treasury 4.80% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score -0.40</summary>

```text
Last close 264.12 (bar of 2026-11-20), from 502 daily bars
Trend: vs 20d SMA 276.60 (-4.5%), 50d 278.41 (-5.1%), 200d 279.61 (-5.5%); 50d below 200d
Momentum: RSI(14) 35.4 | MACD -3.191 vs signal -1.697 (histogram -1.494)
Returns: 1d -0.0% | 5d -4.8% | 1m -4.5% | 3m -11.4%
52-week range: 229.11 - 305.09 (now 46.1% of the way up)
Volatility: ATR(14) 4.90 (1.9% of price) | annualised 20d 26.5%
Volume: 0.28x the 20-day average
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
Three-year record: +16.1% a year | beta to the market 1.26
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
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 1.47 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +19.8% above the current prices
Holdings read: GKOS, BTSG, FROG, TWST, MOG-A
Recent rating changes among them:
  - GKOS: 2026-10-29 HC Wainwright & Co.: main, Buy -> Buy
  - BTSG: 2026-11-03 Guggenheim: main, Buy -> Buy
  - FROG: 2026-11-12 Morgan Stanley: main, Equal-Weight -> Equal-Weight
  - TWST: 2026-10-13 TD Cowen: main, Buy -> Buy
  - MOG-A: 2026-10-13 JP Morgan: main, Overweight -> Overweight
```

</details>

<details><summary><b>Buying and selling by company insiders</b> — score -0.30</summary>

_Not available today._

</details>

<details><summary><b>Who is positioned how</b> — score -0.30</summary>

```text
Contract: RUSSELL E-MINI - CHICAGO MERCANTILE EXCHANGE (positions as of 2026-11-10, published the following Friday)
Large speculators: net short 10.1% of open interest (440,576 contracts)
Change on the week: +2.2% of open interest
Crowding: 77% percentile over 52 weeks -- within its normal range
Read this as crowding, not as a forecast: an extreme is as often the end of a move as the middle of one.
```

</details>

<details><summary><b>Money going into and out of this fund</b> — score -0.30</summary>

```text
Direction: flat (1 month)
Share count change: 1 week: +0.0% (0.00) over 7d | 1 month: +0.0% (0.00) over 30d
Shares outstanding: 281.05M | fund size: 74.23B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### US company bonds, safer (LQD) · Index fund — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:** no explanation. It wrote only “Neutral”, so the main reasons below are all it gave.

**Main reasons it gave:**
- Fund flows flat: 0% change over 1 month
- Fund yield 4.8% below 10-year Treasury yield 4.99%
- US Treasury yields down slightly this week (10-year -0.17%)
- Technical indicators neutral: RSI 48.8, MACD -0.154, volume 0.08x 20-day avg

<details><summary><b>News</b> — score +0.00</summary>

- [Bond ETFs Haven’t Been This Rewarding in Years, So Why Is Wall Street Dumping Them?](https://finance.yahoo.com/markets/options/articles/bond-etfs-haven-t-rewarding-184149666.html)  
  <sub>Yahoo Finance, 20 hours ago</sub>  
  AGG is down about 1% over five years while TLT has lost 35%, as investors flee bonds just when the 10-year yields 5%. Eric Balchunas notes fixed income ETFs...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.14% (+0.02 on the week) | 5-year 4.78% (-0.20 on the week) | 10-year 4.99% (-0.17 on the week) | 30-year 5.37% (-0.11 on the week)
Yield curve, 10-year minus 3-month: +0.84 points -- upward sloping (normal)
US dollar index: 103.69 (+0.28 on the week)
Volatility (VIX): 29.46 (+10.2 on the week) -- stressed
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.1% (2026-10-01) | jobless claims 203k (2026-11-14)
Policy and expectations: Fed target 4.00% | market expects 2.2% inflation over 10 years
Rate path: 2-year Treasury 4.80% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 103.46 (bar of 2026-11-20), from 502 daily bars
Trend: vs 20d SMA 103.78 (-0.3%), 50d 103.46 (+0.0%), 200d 107.17 (-3.5%); 50d below 200d
Momentum: RSI(14) 48.8 | MACD -0.154 vs signal -0.061 (histogram -0.093)
Returns: 1d +0.4% | 5d +0.6% | 1m -0.8% | 3m -2.6%
52-week range: 101.83 - 112.05 (now 15.9% of the way up)
Volatility: ATR(14) 0.53 (0.5% of price) | annualised 20d 6.1%
Volume: 0.08x the 20-day average
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
Share count change: 1 week: +0.0% (0.00) over 10d | 1 month: +0.0% (0.00) over 30d
Shares outstanding: 293.50M | fund size: 30.37B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### S&P 500, equal weight (RSP) · Index fund — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:** no explanation. It wrote only “NEUTRAL”, so the main reasons below are all it gave.

**Main reasons it gave:**
- VIX rose 10.2 points to 29.46, indicating heightened market volatility
- Technical: price above 200‑day SMA but below 20‑day and 50‑day SMAs, MACD negative, RSI 40.9, low volume
- Analyst coverage thin (1.4% of fund) with modest bullish tilt (38% buy, price target +1%)
- CFTC positioning shows net short 15% of open interest, up 3.7% week‑over‑week

<details><summary><b>News</b> — score +0.00</summary>

- [Invesco S&P 500 Equal Weight ETF (RSP) stock price, news, quote and history](https://uk.finance.yahoo.com/quote/RSP/)  
  <sub>Yahoo Finance UK, 22 hours ago</sub>  
  Invesco S&P 500 Equal Weight ETF (RSP) · -4.12% · -0.83% · 4.96% · 9.53% · 14.40% · 31.70% · 738.14%. Key events. Baseline. Advanced chart.
- [Moomoo Singapore Review (2026): My likes and dislikes of this trading platform](https://growbeansprout.com/reviews/brokerage-account/moomoo-singapore-review)  
  <sub>Beansprout, 8 hours ago</sub>  
  Read our Moomoo Singapore review for the latest fees, CPF/SRS investing, CDP linkage, trading tools, and access to US, Singapore, Hong Kong, Japan and Korea...
- [Tech Rout Deepens, VIX Breaks Above 30](https://www.google.com/goto?url=CAESlwEBxCJF11rHkcUSUSXsMMbI8_0zm6MtDRTYkx1RB9OAEYmg_5WfBunfYrya6THD9i4-52TdtKoKxBpYoVHyh8G-GwfuyValTtdRgADES4zo0S89Mz5D5PSjuzUoSDZPpWjpqiA8E5FMXILEAyWxmIxe1BlbMwiFtru-49CymhEblJu3uQ0w3eG8DvyCOh0SWHCri3PJ64Ed&gsessionid=NEoXv8I-iBgg2LFiSRCwGwEM6eJnWTZJ0iJuP_z3mk5uOZqrZENLtw)  
  <sub>Moomoo, 2 hours ago</sub>  
  Tap the related stocks on the image above to add them to your Watchlist. Market Overview Overnight futures are pointing lower again, with tech leading...
- [S&P 500 drops 2% for a sixth straight loss as an early AI rally collapses](https://www.google.com/goto?url=CAESogEBxCJF17qsCNh09hJ8CKAZg5cM9XODZPMX62Ml5xoVApJIz0Iwsi7a4lew09Qopmzl3lWudrf3GgJy16-cMFj2YovOR_8ESC2wtm0pqgdKPAzUREWe0hTBF6SHIwJGvnH-eBCcch7foktIcp6KXZBu6VBLHFBaKwwswltmE-k1y2dNGpOUgZQnJwy0fWYuDYIqJv0FRmCRvdknGXxF4oj9OxM&gsessionid=NEoXv8I-iBgg2LFiSRCwGwEM6eJnWTZJ0iJuP_z3mk5uOZqrZENLtw)  
  <sub>Quantisnow, 17 hours ago</sub>  
  On Nov. 19, 2026, the S&P 500 fund SPY fell 1.98%, its biggest one-day drop since Nov. 5 in Quantisnow's records, while the equal-weight fund RSP fell 1.74%...
- [Peter Lynch Made "Growth at a Reasonable Price" Famous. SPGP Runs the S&P 500 Through That Filter and Keeps 75 Stocks](https://www.google.com/goto?url=CAES3gEBxCJF14YnTh4t3n-N2GIDb9y8Z0y3O-kA2NF73eMV7Wny2nPL8diWX-WCzHeyu8v0j1FN2g3MAC0YEcXre0YqIpY6fvNyN5NopngVsFbOhuBACwfgBsJbw3d5l60AcZj8UTaApO2CuvNOlghU_Kowyb6pJylCxhgqHpmNhUEMwEEZq8z55cKet72aImUaVE-NFSoONNHoKcPjSqtqDozA_O_fGaxexTKBP2RrWuZ_8NHvGJX7h_p9zeM1qSrmWaAvEqyM4qeGRMYfmkfXYcAU39_eBzBovBXa7kquYc0&gsessionid=NEoXv8I-iBgg2LFiSRCwGwEM6eJnWTZJ0iJuP_z3mk5uOZqrZENLtw)  
  <sub>24/7 Wall St., 24 hours ago</sub>  
  Your S&P 500 index fund buys everything, expensive or not. One lesser-known ETF filters the index down to 75 stocks, and its top holdings look nothing like...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.14% (+0.02 on the week) | 5-year 4.78% (-0.20 on the week) | 10-year 4.99% (-0.17 on the week) | 30-year 5.37% (-0.11 on the week)
Yield curve, 10-year minus 3-month: +0.84 points -- upward sloping (normal)
US dollar index: 103.69 (+0.28 on the week)
Volatility (VIX): 29.46 (+10.2 on the week) -- stressed
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.1% (2026-10-01) | jobless claims 203k (2026-11-14)
Policy and expectations: Fed target 4.00% | market expects 2.2% inflation over 10 years
Rate path: 2-year Treasury 4.80% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 212.62 (bar of 2026-11-20), from 502 daily bars
Trend: vs 20d SMA 218.34 (-2.6%), 50d 214.90 (-1.1%), 200d 209.26 (+1.6%); 50d above 200d
Momentum: RSI(14) 40.9 | MACD -0.233 vs signal 0.848 (histogram -1.081)
Returns: 1d +0.5% | 5d -3.9% | 1m -2.6% | 3m -4.2%
52-week range: 182.18 - 223.33 (now 74.0% of the way up)
Volatility: ATR(14) 2.78 (1.3% of price) | annualised 20d 19.2%
Volume: 0.12x the 20-day average
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
Three-year record: +15.8% a year | beta to the market 0.80
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
Ratings by weight: buy 38.4% | hold 61.6% | sell 0.0% (mean 2.56 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +1.0% above the current prices
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
Direction: flat (1 month)
Share count change: 1 week: +0.0% (0.00) over 10d | 1 month: +0.0% (0.00) over 30d
Shares outstanding: 155.55M | fund size: 33.07B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### US government bonds, 1-3 years (SHY) · Index fund — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Neutral overall; no clear macro catalyst, technicals flat, and positioning unchanged.

**Main reasons it gave:**
- Net short 33.5% of 2Y note futures, down 1% OI this week (small bullish shift but still bearish bias)
- Technicals flat: price just above 20‑day SMA, RSI 57, MACD near zero (no decisive trend)
- Fund basics unchanged: AA credit quality, 3.6% yield, low beta 0.25 (stable fundamentals)
- Fund flows flat, no net creations/redemptions (no demand shift)
- Yield curve unchanged, 10y‑3m spread +0.84 (normal upward slope) and yields down slightly on the week

<details><summary><b>News</b> — score +0.00</summary>

_No news found for this one today._

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.14% (+0.02 on the week) | 5-year 4.78% (-0.20 on the week) | 10-year 4.99% (-0.17 on the week) | 30-year 5.37% (-0.11 on the week)
Yield curve, 10-year minus 3-month: +0.84 points -- upward sloping (normal)
US dollar index: 103.69 (+0.28 on the week)
Volatility (VIX): 29.46 (+10.2 on the week) -- stressed
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.1% (2026-10-01) | jobless claims 203k (2026-11-14)
Policy and expectations: Fed target 4.00% | market expects 2.2% inflation over 10 years
Rate path: 2-year Treasury 4.80% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 81.54 (bar of 2026-11-20), from 502 daily bars
Trend: vs 20d SMA 81.43 (+0.1%), 50d 81.31 (+0.3%), 200d 82.00 (-0.6%); 50d below 200d
Momentum: RSI(14) 57.0 | MACD -0.005 vs signal -0.004 (histogram -0.001)
Returns: 1d +0.2% | 5d +0.5% | 1m +0.0% | 3m -0.6%
52-week range: 81.05 - 83.18 (now 22.8% of the way up)
Volatility: ATR(14) 0.13 (0.2% of price) | annualised 20d 2.3%
Volume: 0.07x the 20-day average
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
Direction: flat (1 month)
Share count change: 1 week: +0.0% (0.00) over 10d | 1 month: +0.0% (0.00) over 30d
Shares outstanding: 209.30M | fund size: 17.07B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### US inflation-linked bonds (TIP) · Index fund — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Neutral overall; no material policy surprise, modest bearish positioning but not decisive, technicals near neutral, and fundamentals stable.

**Main reasons it gave:**
- Large speculators net short 37.8% of 10Y note, change +0.3% (modest bearish pressure)
- 10-year Treasury yield rose 0.17% on the week (bond price pressure but limited)
- RSI 49 and MACD -0.176 vs signal -0.085 (technicals near neutral, low volume)
- Fed target unchanged at 4.0%, inflation 3.7% (no policy surprise)

<details><summary><b>News</b> — score +0.00</summary>

_No news found for this one today._

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.14% (+0.02 on the week) | 5-year 4.78% (-0.20 on the week) | 10-year 4.99% (-0.17 on the week) | 30-year 5.37% (-0.11 on the week)
Yield curve, 10-year minus 3-month: +0.84 points -- upward sloping (normal)
US dollar index: 103.69 (+0.28 on the week)
Volatility (VIX): 29.46 (+10.2 on the week) -- stressed
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.1% (2026-10-01) | jobless claims 203k (2026-11-14)
Policy and expectations: Fed target 4.00% | market expects 2.2% inflation over 10 years
Rate path: 2-year Treasury 4.80% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 105.36 (bar of 2026-11-20), from 502 daily bars
Trend: vs 20d SMA 105.69 (-0.3%), 50d 105.24 (+0.1%), 200d 108.50 (-2.9%); 50d below 200d
Momentum: RSI(14) 49.0 | MACD -0.176 vs signal -0.085 (histogram -0.091)
Returns: 1d +0.3% | 5d +0.7% | 1m -0.9% | 3m -1.8%
52-week range: 103.98 - 111.88 (now 17.4% of the way up)
Volatility: ATR(14) 0.37 (0.3% of price) | annualised 20d 4.0%
Volume: 0.08x the 20-day average
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
Share count change: 1 week: +0.0% (0.00) over 10d | 1 month: +0.0% (0.00) over 30d
Shares outstanding: 177.70M | fund size: 18.72B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

**Data that was missing** (counted as 0.00, never guessed):
- news unavailable: Bright Data returned an empty body with its 200; nothing to parse (Bright Data said: x-brd-status-code 502; x-brd-error redirect location was rejected) (Bing's feed, direct: 10 headline(s), none naming TIP)

### US government bonds, 20+ years (TLT) · Index fund — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Slightly bearish due to net short positioning and potential rate hike, but fundamentals remain solid.

**Main reasons it gave:**
- Large speculators net short 33.9% of open interest (POSITIONING)
- Fed officials signal possible half-point rate hike in October (NEWS)
- Technicals: price below 200‑day SMA and MACD negative (TECHNICALS)
- Fund fundamentals: AA credit quality and 4.8% yield (FUND BASICS)

<details><summary><b>News</b> — score -0.20</summary>

- [iShares 20+ Year U.S. Treasury Bond Index ETF (CAD-Hedged) (XTLH.TO) Stock Price, News, Quote & History](https://ca.finance.yahoo.com/quote/XTLH.TO/)  
  <sub>Yahoo! Finance Canada, 3 hours ago</sub>  
  Find the latest iShares 20+ Year U.S. Treasury Bond Index ETF (CAD-Hedged) (XTLH.TO) stock quote, history, news and other vital information to help you with...
- [A Monthly Check at 3 Levels of Risk: VTEB, TLT and EMB, Ranked](https://247wallst.com/investing/etf/2026/11/19/a-monthly-check-at-3-levels-of-risk-vteb-tlt-and-emb-ranked/)  
  <sub>24/7 Wall St., 21 hours ago</sub>  
  A retiree's monthly bond fund check can stay steady while the share price behind it quietly collapses. Ranking three popular payers on both risks produces...
- [Options Whale Alert: $5.09M Bullish Long Call Opened on $TLT](https://www.google.com/goto?url=CAESngEBxCJF19fuCaSLfb9QHKm6_yBTXPmsBXn8k2LSvqMqv5KNlaKKXZMxtAZXtBbgHqoXi1LeBCoo0LOWJgIQvLejjNnq4369XImPVrYf-6q_FU8oJtr9wuIvIqHY1Kyw4dRjw8TDOBwnXm-huq__qsB-KmT2xLGmoEGMvd9yb3mxbEUhUJu6y4zt8i4kRBij-tt_w-TK8Dxd3qYUoT9AsQ&gsessionid=8z_ptRMhd9GjRAZkmGeCrl_KN6SdNAGPeFEC_Ib5OnLbdiIQzb-xGQ)  
  <sub>Moomoo, 15 hours ago</sub>  
  iShares20+ Year Treasury Bond ETF(TLT.US)$ closed up 0.16% at $80.35. A trader bought 19980 Nov 19, 2027 $84.00 calls to open a Long Call.
- [TLTY ETF Holdings List — EURONEXT:TLTY](https://www.google.com/goto?url=CAESeAHEIkXXKiy21L1zxq2MVQAskCt2d439aYj0Z8Vxd_cDQuNF9r5KbeOBO4M5W2sqOpzIc9Wij-KploC7jdCIso8oljVki4Z7-UilplRC9HuqGaey03MHL7f6KsgIqXyseR76iotvb6s6F8gZdVCl0kY6uhSc9iLPiA&gsessionid=8z_ptRMhd9GjRAZkmGeCrl_KN6SdNAGPeFEC_Ib5OnLbdiIQzb-xGQ)  
  <sub>TradingView, 22 hours ago</sub>  
  Explore IncomeShares 20+ Year Treasury (TLT) Options ETP holdings with weight, market value, and other helpful data to make more informed decisions for TLTY...
- [Some Fed Officials Wanted to Hike in October. A Half-Point Hike Is on the Table.](https://www.google.com/goto?url=CAEStwEBxCJF10RPc8QFLYAPNVYiCa4gU7tlLgfkI3Wu1AM3CDOMFiQVPdFl5haqME8shJ7SCJD9w11Y0WRsIJuylClOOTXZkrkyKr1rTe-RM_THMlgaL8iZjR_ZNewK1wL-N0QzdxLuKoSxXpBdX5dZxuwF5oZ1moApdBp4zn2-kpHzKyceeBQVa6EndX16MMUQGZUVLPYupr0o5f_i5Vl2KvQVAZhrSqrka1kuWeYj296yYSj0ERGkScI&gsessionid=8z_ptRMhd9GjRAZkmGeCrl_KN6SdNAGPeFEC_Ib5OnLbdiIQzb-xGQ)  
  <sub>24/7 Wall St., 24 hours ago</sub>  
  Fed Governor Christopher Waller says the Fed may need to "shock people," and a half-point December hike now threatens TLT, which closed at $80.
- [Chart Of The Day: A Tale Of Two 'Safe Havens'](https://www.google.com/goto?url=CAESigEBxCJF13SGur_8aaGQ2RiGxImDeqqTYhofs-6N-4iu8DIEZ46R_0RP4oIeIv8pdmXFd3vC7YWOJNgDAwiEjg0XQgO0HeYNLUURdNUlubd75hwDZS2RbnQTZh16jofnqyXyEdsHEWjkE6eTUz1HFetgk_J-ro_OiUMjSEdioprr-qg4pCB-CKCrlZY&gsessionid=8z_ptRMhd9GjRAZkmGeCrl_KN6SdNAGPeFEC_Ib5OnLbdiIQzb-xGQ)  
  <sub>Seeking Alpha, 4 hours ago</sub>  
  The stock market is sliding. Tech stocks are getting tossed out. And investors are seeking safe havens. Two typical refuges in times of market turmoil are...
- [Stagflation could be seen as the Fed's failure, says Chicago Fed's Goolsbee (TLT:NASDAQ)](https://www.google.com/goto?url=CAESqwEBxCJF10WVLdMksfbq8YzDSDcTjLjjAHqndqKTHsEHk-xcnb4f6bIyPR7wKL1uzWsIbC-14UO86FC2tw_DU1T4kITqjXqAj4CVbUZQEdS6rp0t42PXI6yho1R3PIpNo-iisgi7R6OOTwKLmEq0-tZdDivoS3vqnrXqWBuC3dZRHqMzwaio30Wnwf_rd1VHRZt3DztVQZ22IyOu7QDHyiTlufJjNZswIYOgifw&gsessionid=8z_ptRMhd9GjRAZkmGeCrl_KN6SdNAGPeFEC_Ib5OnLbdiIQzb-xGQ)  
  <sub>Seeking Alpha, 20 hours ago</sub>  
  Stagflation could be measured as a failure on the side of the Federal Reserve, and that has not happened, according to Federal Reserve Bank of Chicago...
- [Bond ETFs Haven’t Been This Rewarding in Years, So Why Is Wall Street Dumping Them?](https://www.google.com/goto?url=CAESmgEBxCJF1zbh7wQ4bOhBJhjPBTvSE8HfOlb8xKsv1AlB6-fo5CKGwTfLog5uSUd69JnvSazeYo-5AMoX2Mm60RXUdjom_dW1tinNCDPczjU9VcBIaUkU8dZLAFPK5kExRsuKpNMxkxqqUoiAZk_iKUu8GPb6VpXB4U_3AfLbDLEjn-A_bFVu9vN5gHHHgHyiVPQMuJx3tUf5ludO&gsessionid=8z_ptRMhd9GjRAZkmGeCrl_KN6SdNAGPeFEC_Ib5OnLbdiIQzb-xGQ)  
  <sub>Yahoo Finance, 20 hours ago</sub>  
  AGG is down about 1% over five years while TLT has lost 35%, as investors flee bonds just when the 10-year yields 5%. Eric Balchunas notes fixed income ETFs...
- [Nasdaq, Dow, S&P 500 Futures Slip As Anthropic’s Record Debut Fails To Lift AI Stocks: SLV, GLD, AMD, NVDA In Focus](https://www.google.com/goto?url=CAES6AEBxCJF12IIneJopFq8w0DIiWvg6Zl9AbgX9iP4DqWLTbuTGXBBexhuqOUkJYk4jI_B1VXmha2NoUsTNpxKYkT-6pkSAMp2BtMm8aoMdxIAmMuHG9zqkZZ_4cPWGR6VbNWboDV_UBCYZ9cUIFPW2TEnRk3j08xxG8Kw4Gl5pYyPKmhOR8CChV3GOyuiwTP7gjpUJfXLy_8haP0WdaZWfTUmHTYJ49zvuanqJI0nJ41uGfAADEs86d6DsN6YzlFIde-_r6Selgqn0Okg6h5pCm-mVDoqazG77L9pGaPoBMr-0Cn3KXKMqybC&gsessionid=8z_ptRMhd9GjRAZkmGeCrl_KN6SdNAGPeFEC_Ib5OnLbdiIQzb-xGQ)  
  <sub>TradingView, 12 hours ago</sub>  
  U.S. stock futures slipped overnight late Thursday as broader markets faced pressure following Anthropic's (ANT) record debut on Nasdaq.As of 9:21 p.m. EST,...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score -0.20</summary>

```text
US Treasury yields: 3-month 4.14% (+0.02 on the week) | 5-year 4.78% (-0.20 on the week) | 10-year 4.99% (-0.17 on the week) | 30-year 5.37% (-0.11 on the week)
Yield curve, 10-year minus 3-month: +0.84 points -- upward sloping (normal)
US dollar index: 103.69 (+0.28 on the week)
Volatility (VIX): 29.46 (+10.2 on the week) -- stressed
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.1% (2026-10-01) | jobless claims 203k (2026-11-14)
Policy and expectations: Fed target 4.00% | market expects 2.2% inflation over 10 years
Rate path: 2-year Treasury 4.80% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score -0.20</summary>

```text
Last close 80.92 (bar of 2026-11-20), from 502 daily bars
Trend: vs 20d SMA 80.97 (-0.1%), 50d 80.06 (+1.1%), 200d 84.12 (-3.8%); 50d below 200d
Momentum: RSI(14) 53.9 | MACD -0.043 vs signal 0.071 (histogram -0.114)
Returns: 1d +0.7% | 5d +1.9% | 1m -1.0% | 3m -2.0%
52-week range: 77.11 - 90.82 (now 27.8% of the way up)
Volatility: ATR(14) 0.74 (0.9% of price) | annualised 20d 10.3%
Volume: 0.16x the 20-day average
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
Three-year record: +0.4% a year | beta to the market 2.30
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
Contract: ULTRA UST BOND - CHICAGO BOARD OF TRADE (positions as of 2026-11-10, published the following Friday)
Large speculators: net short 33.9% of open interest (2,403,991 contracts)
Change on the week: -0.7% of open interest
Crowding: 48% percentile over 52 weeks -- within its normal range
Read this as crowding, not as a forecast: an extreme is as often the end of a move as the middle of one.
```

</details>

<details><summary><b>Money going into and out of this fund</b> — score -0.30</summary>

```text
Direction: flat (1 month)
Share count change: 1 week: +0.0% (0.00) over 7d | 1 month: +0.0% (0.00) over 30d
Shares outstanding: 109.70M | fund size: 8.88B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### US dollar (UUP) · Index fund — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> No policy or rate surprise; macro and technical factors are mixed, leading to a neutral view.

**Main reasons it gave:**
- Fed target unchanged at 4.00% and no policy surprise this week
- US dollar index up 0.28% on the week, supporting a bullish dollar fund
- Technical trend shows price near 52‑week high with RSI 69.1, but volume is only 0.09× the 20‑day average
- Positioning shows net long 5.5% decreasing by 1.2% of OI, indicating slight bearish pressure
- Fund flows show net inflow over the month (+9.5% shares) indicating demand despite a weekly outflow

<details><summary><b>News</b> — score +0.00</summary>

- [Invesco DB US Dollar Index Bullish Fund (UUP) Stock Price, News, Quote & History](https://ca.finance.yahoo.com/quote/UUP/)  
  <sub>Yahoo! Finance Canada, 6 hours ago</sub>  
  Find the latest Invesco DB US Dollar Index Bullish Fund (UUP) stock quote, history, news and other vital information to help you with your stock trading and...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.14% (+0.02 on the week) | 5-year 4.78% (-0.20 on the week) | 10-year 4.99% (-0.17 on the week) | 30-year 5.37% (-0.11 on the week)
Yield curve, 10-year minus 3-month: +0.84 points -- upward sloping (normal)
US dollar index: 103.69 (+0.28 on the week)
Volatility (VIX): 29.46 (+10.2 on the week) -- stressed
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.1% (2026-10-01) | jobless claims 203k (2026-11-14)
Policy and expectations: Fed target 4.00% | market expects 2.2% inflation over 10 years
Rate path: 2-year Treasury 4.80% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 29.59 (bar of 2026-11-20), from 502 daily bars
Trend: vs 20d SMA 29.22 (+1.3%), 50d 28.96 (+2.2%), 200d 28.10 (+5.3%); 50d above 200d
Momentum: RSI(14) 69.1 | MACD 0.197 vs signal 0.158 (histogram 0.038)
Returns: 1d -0.1% | 5d +0.3% | 1m +2.4% | 3m +5.8%
52-week range: 26.47 - 29.63 (now 98.7% of the way up)
Volatility: ATR(14) 0.12 (0.4% of price) | annualised 20d 5.4%
Volume: 0.09x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.20</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score +0.20</summary>

```text
Fund type: Trading--Miscellaneous
What it holds: P/E n/a | P/B 0.00 | P/S 0.00 | 3y earnings growth n/a
Yield: 3.2%
Three-year record: +5.1% a year | beta to the market -7.93
Cost and size: expense ratio 0.75% | net assets 481.36M
What it is made of: Cash 100.0%
Largest holdings: Invesco Shrt-Trm Inv Gov&Agcy Instl 49.5%
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
Share count change: 1 week: -1.3% (-6.29M) over 7d | 1 month: +9.5% (41.69M) over 30d
Shares outstanding: 16.31M | fund size: 482.51M
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Europe (VGK) · Index fund — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Neutral overall – modest bullish signals from analyst coverage and positioning are offset by bearish technical momentum and elevated market stress, with no material macro surprise.

**Main reasons it gave:**
- Price 4.4% below 20‑day SMA, 4.1% below 50‑day SMA, 4.6% below 200‑day SMA
- RSI 34.2 (oversold) and MACD negative indicating bearish momentum
- VIX up 10.2 points on the week (stressed market)
- Analyst coverage thin (12% of fund) despite 83.8% buy rating and +30.5% price target
- CFTC net long 2.8% of open interest, +5.4% weekly increase

<details><summary><b>News</b> — score +0.00</summary>

_No news found for this one today._

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.14% (+0.02 on the week) | 5-year 4.78% (-0.20 on the week) | 10-year 4.99% (-0.17 on the week) | 30-year 5.37% (-0.11 on the week)
Yield curve, 10-year minus 3-month: +0.84 points -- upward sloping (normal)
US dollar index: 103.69 (+0.28 on the week)
Volatility (VIX): 29.46 (+10.2 on the week) -- stressed
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.1% (2026-10-01) | jobless claims 203k (2026-11-14)
Policy and expectations: Fed target 4.00% | market expects 2.2% inflation over 10 years
Rate path: 2-year Treasury 4.80% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score -0.30</summary>

```text
Last close 83.89 (bar of 2026-11-20), from 502 daily bars
Trend: vs 20d SMA 87.73 (-4.4%), 50d 87.48 (-4.1%), 200d 87.92 (-4.6%); 50d below 200d
Momentum: RSI(14) 34.2 | MACD -0.518 vs signal -0.000 (histogram -0.518)
Returns: 1d -0.8% | 5d -5.8% | 1m -3.4% | 3m -9.4%
52-week range: 77.90 - 93.19 (now 39.2% of the way up)
Volatility: ATR(14) 1.13 (1.4% of price) | annualised 20d 21.5%
Volume: 0.05x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.10</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score +0.10</summary>

```text
Fund type: Europe Stock
What it holds: P/E 16.72 | P/B 2.27 | P/S 1.51 | 3y earnings growth n/a
Yield: 2.9%
Three-year record: +15.7% a year | beta to the market 0.88
Cost and size: expense ratio 0.06% | net assets 37.08B
What it is made of: Stocks 99.3%, Cash 0.5%, Other 0.2%
Largest holdings: ASML Holding NV 3.9%, Roche Holding AG Ordinary Shares new 2.2%, Shell PLC 2.0%, Novartis AG Registered Shares 1.9%, HSBC Holdings PLC 1.9%
Sector mix: Financial services 23.8%, Industrials 18.9%, Healthcare 13.5%, Technology 8.9%
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
Rolled up from the 5 largest holdings, 12.0% of the fund by weight  -- thin, so read this as a fact about that slice rather than the fund
Ratings by weight: buy 83.8% | hold 16.2% | sell 0.0% (mean 2.08 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +30.5% above the current prices
Holdings read: ASML.AS, ROP.SW, SHEL.L, NOVN.SW, HSBA.L
Recent rating changes among them: none reported
```

</details>

<details><summary><b>Buying and selling by company insiders</b> — score +0.20</summary>

_Not available today._

</details>

<details><summary><b>Who is positioned how</b> — score +0.20</summary>

```text
Contract: MSCI EAFE  - ICE FUTURES U.S. (positions as of 2026-11-10, published the following Friday)
Large speculators: net long 2.8% of open interest (506,737 contracts)
Change on the week: +5.4% of open interest
Crowding: 87% percentile over 52 weeks -- within its normal range
Read this as crowding, not as a forecast: an extreme is as often the end of a move as the middle of one.
```

</details>

<details><summary><b>Money going into and out of this fund</b> — score +0.20</summary>

```text
Direction: flat (1 month)
Share count change: 1 week: +0.0% (0.00) over 10d | 1 month: +0.0% (0.00) over 30d
Shares outstanding: 282.09M | fund size: 23.66B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Emerging markets (VWO) · Index fund — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:** no explanation. It wrote only “NEUTRAL”, so the main reasons below are all it gave.

**Main reasons it gave:**
- VWO fell 8.5% this week after Taiwan's market slump
- No macro policy or data surprise this week
- Technical downtrend with RSI 26.8 and low volume, no decisive break
- Analyst coverage thin (22.6% of fund) despite all‑buy rating
- Positioning net long modest (2.1% of open interest) and low crowding (30th percentile)

<details><summary><b>News</b> — score +0.00</summary>

- [Vanguard's VXUS Falls 7% and VWO Drops 8.5% This Week as Taiwan's Stock Market Posts Its Worst Week Since 1991. Here's the Loss on a $1 Million IRA and What Rebalancing Rules Say to Do](https://247wallst.com/investing/2026/11/20/vanguards-vxus-falls-7-and-vwo-drops-8-5-this-week-as-taiwans-stock-market-posts-its-worst-week-since-1991-heres-the-loss-on-a-1-million-ira-and-what-rebalancing-rules-say-to-do/)  
  <sub>24/7 Wall St., 2 hours ago</sub>  
  VXUS is down 7% this week and VWO 8.5%, counting Friday's pre-market trades, after Taiwan's stock market fell 6.2% on Friday to finish its worst week since...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.14% (+0.02 on the week) | 5-year 4.78% (-0.20 on the week) | 10-year 4.99% (-0.17 on the week) | 30-year 5.37% (-0.11 on the week)
Yield curve, 10-year minus 3-month: +0.84 points -- upward sloping (normal)
US dollar index: 103.69 (+0.28 on the week)
Volatility (VIX): 29.46 (+10.2 on the week) -- stressed
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.1% (2026-10-01) | jobless claims 203k (2026-11-14)
Policy and expectations: Fed target 4.00% | market expects 2.2% inflation over 10 years
Rate path: 2-year Treasury 4.80% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 51.78 (bar of 2026-11-20), from 502 daily bars
Trend: vs 20d SMA 55.49 (-6.7%), 50d 57.81 (-10.4%), 200d 58.22 (-11.1%); 50d below 200d
Momentum: RSI(14) 26.8 | MACD -1.280 vs signal -0.969 (histogram -0.311)
Returns: 1d -1.7% | 5d -8.2% | 1m -8.9% | 3m -13.7%
52-week range: 51.78 - 61.44 (now 0.0% of the way up)
Volatility: ATR(14) 0.93 (1.8% of price) | annualised 20d 24.9%
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
Three-year record: +13.1% a year | beta to the market 0.78
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

<details><summary><b>What analysts and big funds say</b> — score +0.30</summary>

_Not available today._

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score +0.30</summary>

```text
Rolled up from the 5 largest holdings, 22.6% of the fund by weight  -- thin, so read this as a fact about that slice rather than the fund
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 1.31 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +74.6% above the current prices
Holdings read: 2330.TW, 0700.HK, 9988.HK, 2454.TW, 00939
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
Share count change: 1 week: +0.0% (0.00) over 7d | 1 month: +0.0% (0.00) over 30d
Shares outstanding: 1.42B | fund size: 73.43B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Commodities basket (DBC) · Index fund — no answer, no confidence given

**This one did not finish:** https://api.deepinfra.com/v1/openai/chat/completions unreachable: the streamed answer ran past the 480s ceiling (gave up after 2 attempt(s))

<details><summary><b>News</b> — score n/a</summary>

- [UBS(IE)ETF-UBS Gl.Eq.Inc.Pl.UER (FFGZJ.DE) latest stock news and headlines – Yahoo Finance](https://sg.finance.yahoo.com/quote/FFGZJ.DE/news/)  
  <sub>Yahoo Finance Singapore, 20 hours ago</sub>  
  Get the latest UBS(IE)ETF-UBS Gl.Eq.Inc.Pl.UER (FFGZJ.DE) stock news and headlines to help you in your trading and investment decisions.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score n/a</summary>

```text
US Treasury yields: 3-month 4.14% (+0.02 on the week) | 5-year 4.78% (-0.20 on the week) | 10-year 4.99% (-0.17 on the week) | 30-year 5.37% (-0.11 on the week)
Yield curve, 10-year minus 3-month: +0.84 points -- upward sloping (normal)
US dollar index: 103.69 (+0.28 on the week)
Volatility (VIX): 29.46 (+10.2 on the week) -- stressed
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.1% (2026-10-01) | jobless claims 203k (2026-11-14)
Policy and expectations: Fed target 4.00% | market expects 2.2% inflation over 10 years
Rate path: 2-year Treasury 4.80% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score n/a</summary>

```text
Last close 29.27 (bar of 2026-11-20), from 502 daily bars
Trend: vs 20d SMA 31.54 (-7.2%), 50d 32.43 (-9.8%), 200d 29.74 (-1.6%); 50d above 200d
Momentum: RSI(14) 21.6 | MACD -0.879 vs signal -0.634 (histogram -0.245)
Returns: 1d -1.2% | 5d -4.9% | 1m -12.8% | 3m -5.4%
52-week range: 22.36 - 34.10 (now 58.9% of the way up)
Volatility: ATR(14) 0.49 (1.7% of price) | annualised 20d 19.5%
Volume: 0.06x the 20-day average
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
Three-year record: +12.0% a year | beta to the market 1.04
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
US inventories, week ending 2026-11-13 (published the following Wednesday)
  Crude oil: 417.8 million barrels, +3.4 on the week (a build), 25% percentile over 52 weeks
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
Share count change: 1 week: +1.4% (25.13M) over 7d | 1 month: +11.9% (199.80M) over 34d
Shares outstanding: 64.22M | fund size: 1.88B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

## Sector and country funds

### Argentina (ARGT) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Neutral overall as no macro surprise or decisive technical break; technicals show downtrend, macro stress, but fund inflows and strong analyst buy rating provide some bullish support.

**Main reasons it gave:**
- VIX up 10.2% on the week to 29.46 (stressed market)
- ETF price 66.73 below 20‑day, 50‑day, and 200‑day SMAs (downtrend)
- Share count rose 6.5% week‑over‑week (net inflow)
- Analyst view: 100% buy rating, weighted price target +78% above current

<details><summary><b>News</b> — score +0.00</summary>

- [(ARGT) Volatility Zones as Tactical Triggers](https://news.stocktradersdaily.com/news_release/24/ARGT_Volatility_Zones_as_Tactical_Triggers_111926092802_1795141682.html)  
  <sub>Stock Traders Daily, 17 hours ago</sub>  
  Key findings for Global X Msci Argentina Etf (NASDAQ: ARGT). Weak Near and Mid-Term Sentiment Could Pressure Neutral Long-Term Outlook...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.14% (+0.02 on the week) | 5-year 4.78% (-0.20 on the week) | 10-year 4.99% (-0.17 on the week) | 30-year 5.37% (-0.11 on the week)
Yield curve, 10-year minus 3-month: +0.84 points -- upward sloping (normal)
US dollar index: 103.69 (+0.28 on the week)
Volatility (VIX): 29.46 (+10.2 on the week) -- stressed
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.1% (2026-10-01) | jobless claims 203k (2026-11-14)
Policy and expectations: Fed target 4.00% | market expects 2.2% inflation over 10 years
Rate path: 2-year Treasury 4.80% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score -0.30</summary>

```text
Last close 66.73 (bar of 2026-11-20), from 502 daily bars
Trend: vs 20d SMA 75.22 (-11.3%), 50d 83.50 (-20.1%), 200d 90.23 (-26.0%); 50d below 200d
Momentum: RSI(14) 19.8 | MACD -4.688 vs signal -4.125 (histogram -0.563)
Returns: 1d +0.3% | 5d -9.5% | 1m -22.2% | 3m -29.7%
52-week range: 66.56 - 102.94 (now 0.5% of the way up)
Volatility: ATR(14) 2.13 (3.2% of price) | annualised 20d 34.0%
Volume: 0.06x the 20-day average
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
Three-year record: +19.5% a year | beta to the market 0.44
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

<details><summary><b>What analysts and big funds say</b> — score +0.80</summary>

_Not available today._

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score +0.80</summary>

```text
Rolled up from the 5 largest holdings, 51.1% of the fund by weight
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 1.61 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +78.0% above the current prices
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
Share count change: 1 week: +6.5% (36.34M) over 7d | 1 month: +8.6% (47.21M) over 30d
Shares outstanding: 8.96M | fund size: 597.80M
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Israel (EIS) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Neutral overall as macro risk‑off conditions, bearish technicals and flat flows offset bullish analyst coverage and solid fundamentals.

**Main reasons it gave:**
- Analyst view: 39.6% coverage, 100% buy, +29.3% price target
- Technical: price below 20d/50d/200d SMAs, RSI 28.9 (oversold), low volume
- Macro: VIX up 10.2 points to 29.46, indicating heightened market stress
- Fund flows: flat share count, no net inflows/outflows

<details><summary><b>News</b> — score +0.00</summary>

_No news found for this one today._

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.14% (+0.02 on the week) | 5-year 4.78% (-0.20 on the week) | 10-year 4.99% (-0.17 on the week) | 30-year 5.37% (-0.11 on the week)
Yield curve, 10-year minus 3-month: +0.84 points -- upward sloping (normal)
US dollar index: 103.69 (+0.28 on the week)
Volatility (VIX): 29.46 (+10.2 on the week) -- stressed
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.1% (2026-10-01) | jobless claims 203k (2026-11-14)
Policy and expectations: Fed target 4.00% | market expects 2.2% inflation over 10 years
Rate path: 2-year Treasury 4.80% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score -0.30</summary>

```text
Last close 103.52 (bar of 2026-11-20), from 502 daily bars
Trend: vs 20d SMA 113.09 (-8.5%), 50d 118.11 (-12.4%), 200d 122.57 (-15.5%); 50d below 200d
Momentum: RSI(14) 28.9 | MACD -3.472 vs signal -2.610 (histogram -0.861)
Returns: 1d -0.3% | 5d -7.9% | 1m -13.8% | 3m -14.7%
52-week range: 99.40 - 137.69 (now 10.8% of the way up)
Volatility: ATR(14) 2.39 (2.3% of price) | annualised 20d 38.4%
Volume: 0.12x the 20-day average
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
Three-year record: +28.8% a year | beta to the market 0.98
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

<details><summary><b>What analysts and big funds say</b> — score +0.40</summary>

_Not available today._

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score +0.40</summary>

```text
Rolled up from the 5 largest holdings, 39.6% of the fund by weight
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 1.00 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +29.3% above the current prices
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
Shares outstanding: 2.55M | fund size: 263.97M
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Poland (EPOL) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Neutral overall – strong fund inflows and bullish analyst outlook are offset by weak short‑term technical momentum and no macro catalyst.

**Main reasons it gave:**
- Fund flows: share count up 27.1% in the past month
- Analyst view: weighted price target +14.6% above current price
- Technicals: price below 20‑day SMA and RSI 32.4 indicating oversold momentum
- Macro: no policy or data surprise; VIX elevated at 29.46

<details><summary><b>News</b> — score +0.00</summary>

_No news found for this one today._

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.14% (+0.02 on the week) | 5-year 4.78% (-0.20 on the week) | 10-year 4.99% (-0.17 on the week) | 30-year 5.37% (-0.11 on the week)
Yield curve, 10-year minus 3-month: +0.84 points -- upward sloping (normal)
US dollar index: 103.69 (+0.28 on the week)
Volatility (VIX): 29.46 (+10.2 on the week) -- stressed
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.1% (2026-10-01) | jobless claims 203k (2026-11-14)
Policy and expectations: Fed target 4.00% | market expects 2.2% inflation over 10 years
Rate path: 2-year Treasury 4.80% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score -0.20</summary>

```text
Last close 40.90 (bar of 2026-11-20), from 502 daily bars
Trend: vs 20d SMA 43.37 (-5.7%), 50d 43.94 (-6.9%), 200d 40.81 (+0.2%); 50d above 200d
Momentum: RSI(14) 32.4 | MACD -0.471 vs signal -0.240 (histogram -0.231)
Returns: 1d -2.4% | 5d -7.3% | 1m -7.3% | 3m -8.1%
52-week range: 32.56 - 45.76 (now 63.2% of the way up)
Volatility: ATR(14) 0.73 (1.8% of price) | annualised 20d 24.7%
Volume: 0.14x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.20</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score +0.20</summary>

```text
Fund type: Focused Region
What it holds: P/E 13.39 | P/B 2.08 | P/S 1.40 | 3y earnings growth n/a
Yield: 3.4%
Three-year record: +31.7% a year | beta to the market 0.85
Cost and size: expense ratio 0.59% | net assets 1.03B
What it is made of: Stocks 99.4%, Cash 0.6%
Largest holdings: PKO Bank Polski SA 15.0%, Orlen SA 12.8%, Bank Polska Kasa Opieki SA 7.0%, Powszechny Zaklad Ubezpieczen SA 6.1%, Allegro.EU SA Ordinary Shares 5.7%
Sector mix: Financial services 45.2%, Consumer cyclical 14.9%, Energy 13.2%, Basic materials 5.6%
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
Rolled up from the 5 largest holdings, 46.6% of the fund by weight
Ratings by weight: buy 57.7% | hold 42.3% | sell 0.0% (mean 2.19 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +14.6% above the current prices
Holdings read: PKO.WA, PKN.WA, PEO.WA, PZU.WA, ALE.WA
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
Share count change: 1 week: +1.7% (16.74M) over 7d | 1 month: +27.1% (209.89M) over 30d
Shares outstanding: 24.04M | fund size: 983.32M
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Australia (EWA) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Neutral overall as no clear macro catalyst or decisive technical break is present; mixed signals from technical, analyst view, fundamentals and flows offset each other.

**Main reasons it gave:**
- ETF price below 20‑day, 50‑day and 200‑day SMAs (downtrend)
- Analyst coverage: 57.4% hold, 42.6% sell, weighted price target -2.7%
- Fund flows flat over past month (no net creation/redemption)
- VIX up 10.2 points to 29.46, indicating market stress
- Fund fundamentals: P/E 20.37, 3‑year annualized return 11.5%

<details><summary><b>News</b> — score +0.00</summary>

- [Advasa Explores VISA Prepaid Card Partnership with Enagic](https://www.tipranks.com/news/company-announcements/advasa-explores-visa-prepaid-card-partnership-with-enagic)  
  <sub>TipRanks, 19 hours ago</sub>  
  The latest announcement is out from Advasa Holdings, Inc. ( ($ADBT) ). Advasa Holdings, Inc. is a fintech payment holding company delivering Earned Wage...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.14% (+0.02 on the week) | 5-year 4.78% (-0.20 on the week) | 10-year 4.99% (-0.17 on the week) | 30-year 5.37% (-0.11 on the week)
Yield curve, 10-year minus 3-month: +0.84 points -- upward sloping (normal)
US dollar index: 103.69 (+0.28 on the week)
Volatility (VIX): 29.46 (+10.2 on the week) -- stressed
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.1% (2026-10-01) | jobless claims 203k (2026-11-14)
Policy and expectations: Fed target 4.00% | market expects 2.2% inflation over 10 years
Rate path: 2-year Treasury 4.80% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score -0.30</summary>

```text
Last close 27.23 (bar of 2026-11-20), from 502 daily bars
Trend: vs 20d SMA 28.99 (-6.1%), 50d 28.80 (-5.5%), 200d 28.99 (-6.1%); 50d below 200d
Momentum: RSI(14) 28.7 | MACD -0.358 vs signal -0.093 (histogram -0.266)
Returns: 1d +0.1% | 5d -6.4% | 1m -6.0% | 3m -9.4%
52-week range: 24.95 - 30.43 (now 41.5% of the way up)
Volatility: ATR(14) 0.37 (1.4% of price) | annualised 20d 19.3%
Volume: 0.16x the 20-day average
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
Three-year record: +11.5% a year | beta to the market 0.94
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
Ratings by weight: buy 0.0% | hold 57.4% | sell 42.6% (mean 3.45 on a 1=strong buy to 5=strong sell scale)
Weighted price target: -2.7% above the current prices
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
Share count change: 1 week: +0.0% (0.00) over 10d | 1 month: +0.0% (0.00) over 30d
Shares outstanding: 63.60M | fund size: 1.73B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Canada (EWC) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Neutral overall: bullish analyst view limited to 29.5% coverage, flat fund flows, moderate fundamentals, and no macro surprise. Technicals show price below key SMAs, low RSI and negative MACD but no decisive break on volume.

**Main reasons it gave:**
- Technical indicators show price below 20‑day, 50‑day and 200‑day SMAs with RSI 28.8 (oversold) and negative MACD
- Fund flows are flat over the past month, indicating no net demand for the ETF
- Analyst coverage of the top 5 holdings (29.5% of fund) is 87.2% buy with a +15.2% price target, but coverage is limited
- Macro environment unchanged: no policy surprise, yields modestly down, VIX up but no new data shock

<details><summary><b>News</b> — score +0.00</summary>

- [Energy World Reports Late Filing of Final Director Notices](https://www.tipranks.com/news/company-announcements/energy-world-reports-late-filing-of-final-director-notices)  
  <sub>TipRanks, 9 hours ago</sub>  
  The latest update is out from Energy World Corporation Ltd ( ($AU:EWC) ). Energy World Corporation said it lodged final director interest notices for Brian...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.14% (+0.02 on the week) | 5-year 4.78% (-0.20 on the week) | 10-year 4.99% (-0.17 on the week) | 30-year 5.37% (-0.11 on the week)
Yield curve, 10-year minus 3-month: +0.84 points -- upward sloping (normal)
US dollar index: 103.69 (+0.28 on the week)
Volatility (VIX): 29.46 (+10.2 on the week) -- stressed
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.1% (2026-10-01) | jobless claims 203k (2026-11-14)
Policy and expectations: Fed target 4.00% | market expects 2.2% inflation over 10 years
Rate path: 2-year Treasury 4.80% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score -0.20</summary>

```text
Last close 56.18 (bar of 2026-11-20), from 502 daily bars
Trend: vs 20d SMA 59.91 (-6.2%), 50d 59.79 (-6.0%), 200d 58.63 (-4.2%); 50d above 200d
Momentum: RSI(14) 28.8 | MACD -0.813 vs signal -0.286 (histogram -0.527)
Returns: 1d -0.1% | 5d -6.5% | 1m -7.8% | 3m -9.6%
52-week range: 49.91 - 62.64 (now 49.3% of the way up)
Volatility: ATR(14) 0.86 (1.5% of price) | annualised 20d 20.8%
Volume: 0.04x the 20-day average
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
Three-year record: +20.7% a year | beta to the market 0.73
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

<details><summary><b>What analysts and big funds say</b> — score +0.35</summary>

_Not available today._

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score +0.35</summary>

```text
Rolled up from the 5 largest holdings, 29.5% of the fund by weight
Ratings by weight: buy 87.2% | hold 12.8% | sell 0.0% (mean 2.20 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +15.2% above the current prices
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
Share count change: 1 week: +0.0% (0.00) over 10d | 1 month: +0.0% (0.00) over 30d
Shares outstanding: 94.80M | fund size: 5.33B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Sweden (EWD) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> The fund shows mixed signals: bearish technicals and stressed macro conditions are offset by a fully bullish analyst view of the top holdings and solid fundamentals, while fund flows are flat. No clear macro catalyst or decisive technical break is present, so the overall stance remains neutral.

**Main reasons it gave:**
- Price below 20‑day, 50‑day and 200‑day SMAs (49.49 vs 51.99/51.29/51.50) – bearish technicals
- RSI 35.3 and MACD negative – low momentum
- Analyst coverage of top holdings (33.9% of fund) all buy with weighted price target +13.4% – bullish
- Fund flows flat over past month (share count unchanged) – neutral demand
- VIX up 10.2 points to 29.46 and yields high – heightened market stress

<details><summary><b>News</b> — score +0.00</summary>

_No news found for this one today._

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.14% (+0.02 on the week) | 5-year 4.78% (-0.20 on the week) | 10-year 4.99% (-0.17 on the week) | 30-year 5.37% (-0.11 on the week)
Yield curve, 10-year minus 3-month: +0.84 points -- upward sloping (normal)
US dollar index: 103.69 (+0.28 on the week)
Volatility (VIX): 29.46 (+10.2 on the week) -- stressed
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.1% (2026-10-01) | jobless claims 203k (2026-11-14)
Policy and expectations: Fed target 4.00% | market expects 2.2% inflation over 10 years
Rate path: 2-year Treasury 4.80% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score -0.30</summary>

```text
Last close 49.49 (bar of 2026-11-20), from 502 daily bars
Trend: vs 20d SMA 51.99 (-4.8%), 50d 51.29 (-3.5%), 200d 51.50 (-3.9%); 50d below 200d
Momentum: RSI(14) 35.3 | MACD -0.203 vs signal 0.180 (histogram -0.383)
Returns: 1d -1.0% | 5d -6.1% | 1m -1.7% | 3m -7.6%
52-week range: 45.38 - 54.72 (now 44.0% of the way up)
Volatility: ATR(14) 0.79 (1.6% of price) | annualised 20d 23.8%
Volume: 0.02x the 20-day average
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
Three-year record: +16.6% a year | beta to the market 1.18
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

<details><summary><b>What analysts and big funds say</b> — score +0.30</summary>

_Not available today._

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score +0.30</summary>

```text
Rolled up from the 5 largest holdings, 33.9% of the fund by weight
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 1.97 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +13.4% above the current prices
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
Share count change: 1 week: +0.0% (0.00) over 10d | 1 month: +0.0% (0.00) over 30d
Shares outstanding: 7.65M | fund size: 378.60M
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Germany (EWG) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Mixed signals: bullish analyst coverage vs. bearish technicals, flat fund flows, and neutral macro.

**Main reasons it gave:**
- Price below 20‑day, 50‑day and 200‑day SMAs (‑5% to ‑5.4%)
- RSI 34.6 and MACD negative, indicating weak momentum
- Analyst ratings 78% buy with weighted price target +26% above current price
- Fund flows flat (0% change in share count over 1 week and 1 month)
- Macro data unchanged; yields slightly down, VIX up 10 points, no policy surprise

<details><summary><b>News</b> — score +0.00</summary>

_No news found for this one today._

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.14% (+0.02 on the week) | 5-year 4.78% (-0.20 on the week) | 10-year 4.99% (-0.17 on the week) | 30-year 5.37% (-0.11 on the week)
Yield curve, 10-year minus 3-month: +0.84 points -- upward sloping (normal)
US dollar index: 103.69 (+0.28 on the week)
Volatility (VIX): 29.46 (+10.2 on the week) -- stressed
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.1% (2026-10-01) | jobless claims 203k (2026-11-14)
Policy and expectations: Fed target 4.00% | market expects 2.2% inflation over 10 years
Rate path: 2-year Treasury 4.80% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score -0.40</summary>

```text
Last close 39.88 (bar of 2026-11-20), from 502 daily bars
Trend: vs 20d SMA 42.03 (-5.1%), 50d 41.80 (-4.6%), 200d 42.15 (-5.4%); 50d below 200d
Momentum: RSI(14) 34.6 | MACD -0.250 vs signal 0.048 (histogram -0.298)
Returns: 1d -0.8% | 5d -7.0% | 1m -3.6% | 3m -9.6%
52-week range: 38.08 - 44.59 (now 27.6% of the way up)
Volatility: ATR(14) 0.69 (1.7% of price) | annualised 20d 25.9%
Volume: 0.08x the 20-day average
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
Three-year record: +15.9% a year | beta to the market 0.95
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

<details><summary><b>What analysts and big funds say</b> — score +0.50</summary>

_Not available today._

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score +0.50</summary>

```text
Rolled up from the 5 largest holdings, 45.1% of the fund by weight
Ratings by weight: buy 78.0% | hold 22.0% | sell 0.0% (mean 1.99 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +26.3% above the current prices
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
Shares outstanding: 79.50M | fund size: 3.17B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Italy (EWI) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:** no explanation. It wrote only “NEUTRAL”, so the main reasons below are all it gave.

**Main reasons it gave:**
- Analyst coverage 52% of fund, 90.8% buy rating, +18.1% price target
- Price below 20‑day, 50‑day, 200‑day SMAs; RSI 37.6; low volume
- Fund flows flat (share count unchanged) indicating no net demand shift
- No macro surprise (inflation 3.7% within expectations, Fed target unchanged)

<details><summary><b>News</b> — score +0.00</summary>

_No news found for this one today._

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.14% (+0.02 on the week) | 5-year 4.78% (-0.20 on the week) | 10-year 4.99% (-0.17 on the week) | 30-year 5.37% (-0.11 on the week)
Yield curve, 10-year minus 3-month: +0.84 points -- upward sloping (normal)
US dollar index: 103.69 (+0.28 on the week)
Volatility (VIX): 29.46 (+10.2 on the week) -- stressed
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.1% (2026-10-01) | jobless claims 203k (2026-11-14)
Policy and expectations: Fed target 4.00% | market expects 2.2% inflation over 10 years
Rate path: 2-year Treasury 4.80% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 54.95 (bar of 2026-11-20), from 502 daily bars
Trend: vs 20d SMA 56.97 (-3.5%), 50d 57.64 (-4.7%), 200d 58.28 (-5.7%); 50d below 200d
Momentum: RSI(14) 37.6 | MACD -0.326 vs signal -0.104 (histogram -0.222)
Returns: 1d -0.8% | 5d -5.8% | 1m -0.1% | 3m -12.4%
52-week range: 50.70 - 63.35 (now 33.6% of the way up)
Volatility: ATR(14) 0.91 (1.7% of price) | annualised 20d 28.4%
Volume: 0.03x the 20-day average
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
Three-year record: +23.9% a year | beta to the market 0.92
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
Ratings by weight: buy 90.8% | hold 9.2% | sell 0.0% (mean 2.17 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +18.1% above the current prices
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
Share count change: 1 week: +0.0% (0.00) over 10d | 1 month: +0.0% (0.00) over 30d
Shares outstanding: 8.55M | fund size: 469.82M
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Japan (EWJ) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> No material macro surprise, technicals show downtrend without decisive break, analyst coverage thin despite bullish rating, positioning net long small and decreasing.

**Main reasons it gave:**
- Japan export growth positive but not a surprise
- Price below 20d, 50d, 200d SMAs; RSI 29.5, no decisive technical break
- Analyst coverage thin (17.2% of fund) despite 100% buy rating
- CFTC positioning net long 2.2% and decreased by 5.8% week over week

<details><summary><b>News</b> — score +0.00</summary>

- [Japan's Solid Export Growth Puts These ETFs in the Limelight](https://www.zacks.com/stock/news/3033176/japans-solid-export-growth-puts-these-etfs-in-the-limelight)  
  <sub>Zacks Investment Research, 27 minutes ago</sub>  
  Japan's record export growth, driven by AI and semiconductor demand, puts these yen and Japan equity ETFs in focus.
- [iShares MSCI Japan ETF Tokenized bStocks price today, EWJB to USD chart, marketcap and volume](https://cryptoslate.com/coins/ishares-msci-japan-etf-tokenized-bstocks/)  
  <sub>CryptoSlate, 4 hours ago</sub>  
  iShares MSCI Japan ETF Tokenized bStocks price is $85.65 on Nov 20, 2026. Market cap $541.7K; 24h volume $298.87K.
- [AI Selloff Spreads From Wall Street To Asia Despite Anthropic Debut: SPY, QQQ, DIA, Asian Stocks Head For Steep Weekly Losses](https://www.google.com/goto?url=CAES9AEBxCJF12Ir3lNu3PDQGla39Pvp-e91Mj0ghXAhxD2_zKESX9X59GdX3CbmdWarwtqMeiCTaur0mGaHlGb3kSGrxLSAapDteKPkpPgJFcOFgFuyh2-7BnmfPfbLGKbtrKPC08R4xeHuGScjlXHoKKSYIgByhqDX9uN3g_JR7VmPxb_SP3Jbx3tg5A001FQ9ELWVw0HI0fFqiq3ogwhaB-TiU3yXdIdM-2tW7i7yxSz-6Iq0PKSJMoT-M3rOGKPwrh3CK0cFkWKbYFYWmFQp6gYlF9PmPpDO2Bi4o80gWvw6EN2_cSuvN3bd77O_pv6U5PxATfa5&gsessionid=t-YMTCvWctNCLpJ1pzpyL3ELY97R9bfEJGTIPDP0xfHU1fhXSJsO4A)  
  <sub>TradingView, 10 hours ago</sub>  
  Global stock markets are headed for a steep red close this week despite Claude-maker Anthropic's (ANT) record debut on the Nasdaq.
- [SPY, QQQ, DIA, Asian Stocks Plunge As Anthropic’s Record IPO Fails To Stop AI Rout](https://www.google.com/goto?url=CAEStAEBxCJF18YzJ_iN6nOOcFSEoIs2AOW9ejDUQhCM3QbXKYpU5UOY0ekZNev4OKXQuf_gOt2oGxs3iBq8sRG0f1r2DYopes4P7VM5E32zQ9B6Yr088iXE2N7AoD1BeiCzNyLUm8di61NBuEFFBQ9y9uEfsLgS8JYeC3latdesIhv9ABXuDTkY9xhJbRWr-zU4sedGoJlvDeqK-390avKZKSuzIxmCORPbqXOO13ct9D_i6WP3ae0&gsessionid=t-YMTCvWctNCLpJ1pzpyL3ELY97R9bfEJGTIPDP0xfHU1fhXSJsO4A)  
  <sub>Stocktwits, 10 hours ago</sub>  
  While Anthropic's stock surged more than 17% on its debut on Thursday, other AI stocks across the U.S. and Asian markets fell sharply.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.14% (+0.02 on the week) | 5-year 4.78% (-0.20 on the week) | 10-year 4.99% (-0.17 on the week) | 30-year 5.37% (-0.11 on the week)
Yield curve, 10-year minus 3-month: +0.84 points -- upward sloping (normal)
US dollar index: 103.69 (+0.28 on the week)
Volatility (VIX): 29.46 (+10.2 on the week) -- stressed
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.1% (2026-10-01) | jobless claims 203k (2026-11-14)
Policy and expectations: Fed target 4.00% | market expects 2.2% inflation over 10 years
Rate path: 2-year Treasury 4.80% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score -0.10</summary>

```text
Last close 85.81 (bar of 2026-11-20), from 502 daily bars
Trend: vs 20d SMA 91.24 (-6.0%), 50d 94.67 (-9.4%), 200d 92.14 (-6.9%); 50d above 200d
Momentum: RSI(14) 29.5 | MACD -2.078 vs signal -1.653 (histogram -0.424)
Returns: 1d -1.4% | 5d -6.5% | 1m -9.3% | 3m -9.5%
52-week range: 79.49 - 99.32 (now 31.9% of the way up)
Volatility: ATR(14) 1.64 (1.9% of price) | annualised 20d 30.1%
Volume: 0.13x the 20-day average
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
Three-year record: +15.5% a year | beta to the market 0.86
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
Weighted price target: +37.1% above the current prices
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
Share count change: 1 week: +0.0% (0.00) over 10d | 1 month: +0.0% (0.00) over 30d
Shares outstanding: 227.85M | fund size: 19.55B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Switzerland (EWL) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Neutral overall as there is no material macro surprise, technical break, or flow shift. Analyst view is modestly bullish but limited, fundamentals show high valuations, and technicals are mixed.

**Main reasons it gave:**
- Flat fund flows: 0% change in share count over week and month
- Technical indicators mixed: price below 20‑day SMA, RSI 42, MACD below signal
- Macro unchanged: yields stable, VIX up but no surprise data releases
- Analyst coverage modestly bullish (+3.9% price target) covering 49.6% of fund
- Valuations high (P/E 23.9, P/B 4.2) suggesting modest bearish pressure

<details><summary><b>News</b> — score +0.00</summary>

_No news found for this one today._

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.14% (+0.02 on the week) | 5-year 4.78% (-0.20 on the week) | 10-year 4.99% (-0.17 on the week) | 30-year 5.37% (-0.11 on the week)
Yield curve, 10-year minus 3-month: +0.84 points -- upward sloping (normal)
US dollar index: 103.69 (+0.28 on the week)
Volatility (VIX): 29.46 (+10.2 on the week) -- stressed
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.1% (2026-10-01) | jobless claims 203k (2026-11-14)
Policy and expectations: Fed target 4.00% | market expects 2.2% inflation over 10 years
Rate path: 2-year Treasury 4.80% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 62.47 (bar of 2026-11-20), from 502 daily bars
Trend: vs 20d SMA 64.34 (-2.9%), 50d 62.10 (+0.6%), 200d 62.02 (+0.7%); 50d above 200d
Momentum: RSI(14) 42.1 | MACD 0.258 vs signal 0.688 (histogram -0.429)
Returns: 1d -0.0% | 5d -3.6% | 1m -1.9% | 3m -2.7%
52-week range: 55.69 - 66.56 (now 62.4% of the way up)
Volatility: ATR(14) 0.77 (1.2% of price) | annualised 20d 20.0%
Volume: 0.08x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score -0.20</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score -0.20</summary>

```text
Fund type: Focused Region
What it holds: P/E 23.89 | P/B 4.18 | P/S 2.64 | 3y earnings growth n/a
Yield: 1.7%
Three-year record: +14.6% a year | beta to the market 0.82
Cost and size: expense ratio 0.50% | net assets 3.02B
What it is made of: Stocks 99.0%, Cash 1.0%
Largest holdings: Roche Holding AG Ordinary Shares new 15.0%, Novartis AG Registered Shares 12.9%, Nestle SA 11.4%, UBS Group AG Registered Shares 5.8%, Zurich Insurance Group AG 4.6%
Sector mix: Healthcare 40.1%, Financial services 19.2%, Consumer defensive 13.5%, Industrials 11.2%
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

<details><summary><b>What analysts and big funds say</b> — score +0.27</summary>

_Not available today._

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score +0.27</summary>

```text
Rolled up from the 5 largest holdings, 49.6% of the fund by weight
Ratings by weight: buy 64.8% | hold 35.2% | sell 0.0% (mean 2.46 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +3.9% above the current prices
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
Shares outstanding: 28.62M | fund size: 1.79B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Spain (EWP) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Neutral overall as no macro surprise, flat fund flows, mixed technical and fundamental signals, and analyst view is bullish but limited to ~53% of holdings.

**Main reasons it gave:**
- Price 56.20 below 20‑day SMA 58.12 (-3.3%) and 50‑day SMA 58.79 (-4.4%)
- Volume 0.03× the 20‑day average, indicating low trading activity
- Analyst coverage 53.1% weight, 76.3% buy rating, weighted price target +12.4%
- Fund flows flat over the past month (share count unchanged)
- Macro data shows no surprise; yields stable, VIX high but unchanged, no policy shift

<details><summary><b>News</b> — score +0.00</summary>

_No news found for this one today._

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.14% (+0.02 on the week) | 5-year 4.78% (-0.20 on the week) | 10-year 4.99% (-0.17 on the week) | 30-year 5.37% (-0.11 on the week)
Yield curve, 10-year minus 3-month: +0.84 points -- upward sloping (normal)
US dollar index: 103.69 (+0.28 on the week)
Volatility (VIX): 29.46 (+10.2 on the week) -- stressed
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.1% (2026-10-01) | jobless claims 203k (2026-11-14)
Policy and expectations: Fed target 4.00% | market expects 2.2% inflation over 10 years
Rate path: 2-year Treasury 4.80% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score -0.20</summary>

```text
Last close 56.20 (bar of 2026-11-20), from 502 daily bars
Trend: vs 20d SMA 58.12 (-3.3%), 50d 58.79 (-4.4%), 200d 58.18 (-3.4%); 50d above 200d
Momentum: RSI(14) 37.2 | MACD -0.290 vs signal -0.070 (histogram -0.220)
Returns: 1d -0.4% | 5d -6.0% | 1m -2.3% | 3m -11.1%
52-week range: 49.37 - 63.23 (now 49.3% of the way up)
Volatility: ATR(14) 0.93 (1.7% of price) | annualised 20d 25.6%
Volume: 0.03x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.40</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score +0.40</summary>

```text
Fund type: Focused Region
What it holds: P/E 16.25 | P/B 2.19 | P/S 1.75 | 3y earnings growth n/a
Yield: 3.0%
Three-year record: +28.7% a year | beta to the market 0.91
Cost and size: expense ratio 0.50% | net assets 1.94B
What it is made of: Stocks 99.4%, Cash 0.6%
Largest holdings: Banco Santander SA 16.4%, Iberdrola SA 14.3%, Banco Bilbao Vizcaya Argentaria SA 12.6%, Repsol SA 5.3%, Industria De Diseno Textil SA Share From Split 4.6%
Sector mix: Financial services 40.5%, Utilities 22.9%, Industrials 14.9%, Technology 6.3%
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
Rolled up from the 5 largest holdings, 53.1% of the fund by weight
Ratings by weight: buy 76.3% | hold 23.7% | sell 0.0% (mean 2.29 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +12.4% above the current prices
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
Shares outstanding: 37.35M | fund size: 2.10B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Taiwan (EWT) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Neutral overall: macro stress (VIX up, rising yields) and negative news on Taiwan tech offset a bullish analyst view limited to ~38% of the fund; flat fund flows show no net demand; fundamentals are solid but valuations are high.

**Main reasons it gave:**
- AI selloff pushes Taiwan's benchmark to worst week since 1990, TSMC down 4.2%
- VIX rose 10.2 points on the week, indicating stressed market conditions
- Fund flows flat (0% share count change) show no net inflow or outflow
- Analyst coverage of top holdings (37.7% weight) all buy with +79% price target

<details><summary><b>News</b> — score +0.00</summary>

- [EWT: Anthropic Sucking Up The AI Air, Taiwan's P/E Improves (NYSEARCA:EWT)](https://seekingalpha.com/article/4970157-ewt-anthropic-sucking-up-the-ai-air-taiwans-pe-improves)  
  <sub>Seeking Alpha, 23 hours ago</sub>  
  iShares MSCI Taiwan ETF trades below 16 times earnings, with 36% long-term earnings growth and still-upbeat 2027 earnings expectations.
- [AMD Stock Drops Another 7% Before the Bell and Taiwan Semiconductor Slides 4.2% as Nasdaq Futures Fall 1.6% After Asia's Chip Selloff](https://247wallst.com/investing/2026/11/20/amd-stock-drops-another-7-0-before-the-bell-and-taiwan-semiconductor-slides-4-2-as-nasdaq-futures-fall-1-6-after-asias-chip-selloff/)  
  <sub>24/7 Wall St., 3 hours ago</sub>  
  AMD was down another 7% before the bell after Thursday's 7.7% drop, a two-day loss of 14.2%. Taiwan Semiconductor was down 4.2%, Micron 4.8%, Intel 5.3% and...
- [Taiwan Stocks Post Worst Week Since 1990 on 16nm Chip Curbs - Taiwan Semiconductor (NYSE:TSM)](https://www.google.com/goto?url=CAESrAEBxCJF10zQJ1mPXGD14Lty6KwPqVdwai1SEtya7NZ4FwcQhwOX2V-t-7Gyk6-UvLay4QtEmrJ2ixzdJleS7a22EN8P4FEStt0on2CaH4tNOPPuGSpECi9lNo-qw4rHUXykhSruFCWKKPlP84ZR9QTVfoXly4ot32rPcn0_zINsjv-unZ0vmpn6mAVb0rnjtF391g7bcfMldF6HRHabCZsS5bK276qnrNuBpoW3&gsessionid=xwUiULvKxxJqh4MVakT2or4b-PI59f_Zo1jLW81z4NmUImaqAZGWXw)  
  <sub>Benzinga, 32 minutes ago</sub>  
  Taiwan's index had its worst week since 1990, as new U.S. export rules hit chips at 16nm. TSMC and the EWT ETF slid as the AI trade unwound.
- [AI Selloff Spreads From Wall Street To Asia Despite Anthropic Debut: SPY, QQQ, DIA, Asian Stocks Head For Steep Weekly Losses](https://www.google.com/goto?url=CAES9AEBxCJF1wEJfi1QTZRBulzUFeUxvuHTlStaMpzJwesIDnr6raIHPpOvkjK00-49sy3VcaHPjgpyFnloxs604YI_Gc47odEA4BlCiquqSkJaskxG3zWeyQb0OMqN1ayU3oJ3oWhTV0y6KmOt75PpaX1X24sFguoQjypUYIjYWg9jNPI7KZEcfWHo9PFp5lgz6WNOrokrnv7nzgeGYrNqKbPpDF8SUnyPfdzFeANbI6-LiUrnqxF1nuQHNmr4-MRp7QnEpw7PwM2hUPPkhXlH21Lsoy6uRnc2VOlwFoi0bZP4te2QvCsPEUuoGPsg3kDWWCTBx-gH&gsessionid=xwUiULvKxxJqh4MVakT2or4b-PI59f_Zo1jLW81z4NmUImaqAZGWXw)  
  <sub>TradingView, 10 hours ago</sub>  
  Global stock markets are headed for a steep red close this week despite Claude-maker Anthropic's (ANT) record debut on the Nasdaq.
- [AI selloff: Taiwan's benchmark index posts worst week since 1991](https://www.google.com/goto?url=CAESoQEBxCJF155IVrcrrMcSZXsJ2a4AL4L_XG9cqd7u2S5kDKD3WGCkxw8ovh51A98nwV_11GIY1Sgiu056ZBDJW6p-SLBikXq5CwCwrUl5pZKbYP95WE9B_nGSf3tqqX3q-JGNTinYppJvSHa4gjrAMvmXw2QNUADGU9eWDORH-dDo6gWzQhGx57Qey5vgPELAS9hfEQ-qdwle7GV7pb_9nwCUxQ&gsessionid=xwUiULvKxxJqh4MVakT2or4b-PI59f_Zo1jLW81z4NmUImaqAZGWXw)  
  <sub>Seeking Alpha, 4 hours ago</sub>  
  Taiwan's stock market extended losses on Friday, capping off its worst week in decades, tracking the global tech selloff as Anthropic's (ANT) IPO failed to...
- [South Korea's Stock Market and the Nikkei 225 Sink More Than 4% as the AI Selloff Spreads From Wall Street. Here's How Much of a Target-Date Fund Is in Samsung, SK Hynix and TSMC](https://www.google.com/goto?url=CAESlwIBxCJF1wkyxxjiJgcUg-41pb2uhagZtZ6OGUwNkkDsrkoqccOoha7_1Iuecfv0Ikjn94uH2j0qHjmZ0JNxdtQuGyKsJcnXz8LKhkBu1eMIk-iW03LTxQ3utKILcBSL7N3f2_SPwA22e0JWxv_asP_y3GtyQ3zw0pFIG1MWxp9IaArAtGOKupGZjmNyWhiWsQpptD8TcKmvO8JBd_tzguGXZ8dfaMhQU8yzreyt7A1ANBCwbzOQs-RQQ-OXxkhg37tbOGejf-XN1UdYbD-9HQr6B0Dw6sueJ6ILikwP9CMT3ees_hIkHIK6TYhTrXSf-LD_SUfbzfmzsWE4m7PzbeJPxqQTlb1XARW3c7_Yen542PZLvV_HfEw&gsessionid=xwUiULvKxxJqh4MVakT2or4b-PI59f_Zo1jLW81z4NmUImaqAZGWXw)  
  <sub>24/7 Wall St., 11 hours ago</sub>  
  The KOSPI was down 5.04% at 4,879.10 early Friday afternoon in Seoul, setting off a sell-side sidecar, and the Nikkei 225 was down 4.52%.
- [SPY, QQQ, DIA, Asian Stocks Plunge As Anthropic’s Record IPO Fails To Stop AI Rout](https://www.google.com/goto?url=CAEStAEBxCJF13etRZxbP3HKy8ytHeXSkwsK2ATSKHlnVsEXa141x6n_K_2XtTmP1nX1tMWWmUAZBwu7ovBnzkC7hoNjleRHxnhZ3AfDU5Uxc8ZVYKBOePoHLQ8BLzPTfp1G9yi8yzxiP922nf8c4ISxOI80EdSjQFuJDfcBmYDA2x_3DWnd00mC2Cx1UtHDUDZEywVdtn3NqhQ-ajOw0_hYZKV3BxhhASgINPCEAugmXR1xse0EUAo&gsessionid=xwUiULvKxxJqh4MVakT2or4b-PI59f_Zo1jLW81z4NmUImaqAZGWXw)  
  <sub>Stocktwits, 10 hours ago</sub>  
  While Anthropic's stock surged more than 17% on its debut on Thursday, other AI stocks across the U.S. and Asian markets fell sharply.
- [Anthropic Defies Tech Rout On Debut — Tom Lee Sees ‘Big Payoff’ Ahead And Says Cisco’s Wild 1997 Ride Shows Why](https://www.google.com/goto?url=CAESwQEBxCJF18EPIN6irqh-DBQi-YyuuXvy-wQabN4QSQqLUh3_VrW6Biyc_rn1JD2oVbVfDM75ziGwgEZkkegk0SdgxPP6BV29FdI3GtOyk9htv2khXZ-jbcNzayiTm6mavu6107uEHmoJ6lqjg8oM4IbYzrEVCSqs5KIr956fAR63kY2LIbMVCq4rzKCcNdBA3F8-rb7tgfGbL654fR2j5rxxkY6C2wAHuvNUlWxzLz1JPzST7E3pqBQYiD5oefpCgUSI&gsessionid=xwUiULvKxxJqh4MVakT2or4b-PI59f_Zo1jLW81z4NmUImaqAZGWXw)  
  <sub>Stocktwits, 10 hours ago</sub>  
  After six straight S&P 500 losses, Lee noted that the index rose the following week in all 10 prior cases he analyzed.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.14% (+0.02 on the week) | 5-year 4.78% (-0.20 on the week) | 10-year 4.99% (-0.17 on the week) | 30-year 5.37% (-0.11 on the week)
Yield curve, 10-year minus 3-month: +0.84 points -- upward sloping (normal)
US dollar index: 103.69 (+0.28 on the week)
Volatility (VIX): 29.46 (+10.2 on the week) -- stressed
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.1% (2026-10-01) | jobless claims 203k (2026-11-14)
Policy and expectations: Fed target 4.00% | market expects 2.2% inflation over 10 years
Rate path: 2-year Treasury 4.80% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score -0.10</summary>

```text
Last close 79.53 (bar of 2026-11-20), from 502 daily bars
Trend: vs 20d SMA 95.84 (-17.0%), 50d 105.38 (-24.5%), 200d 95.12 (-16.4%); 50d above 200d
Momentum: RSI(14) 27.3 | MACD -5.812 vs signal -4.579 (histogram -1.233)
Returns: 1d -5.3% | 5d -18.3% | 1m -23.5% | 3m -23.0%
52-week range: 60.03 - 118.00 (now 33.6% of the way up)
Volatility: ATR(14) 4.13 (5.2% of price) | annualised 20d 69.1%
Volume: 0.34x the 20-day average
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
Three-year record: +31.2% a year | beta to the market 1.35
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

<details><summary><b>What analysts and big funds say</b> — score +0.50</summary>

_Not available today._

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score +0.50</summary>

```text
Rolled up from the 5 largest holdings, 37.7% of the fund by weight
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 1.33 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +79.2% above the current prices
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
Share count change: 1 week: +0.0% (0.00) over 10d | 1 month: +0.0% (0.00) over 30d
Shares outstanding: 85.00M | fund size: 6.76B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### United Kingdom (EWU) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Neutral overall: bearish technicals and high market volatility offset bullish analyst coverage and neutral fund flows.

**Main reasons it gave:**
- Price below 20‑day, 50‑day, and 200‑day SMAs (down ~4%)
- RSI 34.5 and MACD negative indicating weak bearish momentum
- VIX up 10.2 points to 29.46, indicating stressed market conditions
- Fund flows flat (share count unchanged over the past month)
- Analyst coverage of top holdings (36.9% weight) all buy with +20.7% price target

<details><summary><b>News</b> — score +0.00</summary>

- [EWU’s 0.50% Expense Ratio Doesn’t Show What the Fund Pays in UK Stamp Duty](https://247wallst.com/investing/etf/2026/11/19/ewus-0-50-expense-ratio-doesnt-show-what-the-fund-pays-in-uk-stamp-duty/)  
  <sub>24/7 Wall St., 12 hours ago</sub>  
  Ask most retirement savers what the iShares MSCI United Kingdom ETF (NYSEARCA:EWU) costs, and they will quote one number: the 0.50% expense ratio.
- [Why AstraZeneca Could Make Sense Through ETFs Now](https://finance.yahoo.com/markets/stocks/articles/why-astrazeneca-could-sense-etfs-160904771.html)  
  <sub>Yahoo Finance, 23 hours ago</sub>  
  Owning AstraZeneca directly means your results lean heavily on what happens to that single business. Simply Wall St highlights that the group has a high...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.14% (+0.02 on the week) | 5-year 4.78% (-0.20 on the week) | 10-year 4.99% (-0.17 on the week) | 30-year 5.37% (-0.11 on the week)
Yield curve, 10-year minus 3-month: +0.84 points -- upward sloping (normal)
US dollar index: 103.69 (+0.28 on the week)
Volatility (VIX): 29.46 (+10.2 on the week) -- stressed
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.1% (2026-10-01) | jobless claims 203k (2026-11-14)
Policy and expectations: Fed target 4.00% | market expects 2.2% inflation over 10 years
Rate path: 2-year Treasury 4.80% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score -0.40</summary>

```text
Last close 45.40 (bar of 2026-11-20), from 502 daily bars
Trend: vs 20d SMA 47.41 (-4.2%), 50d 47.24 (-3.9%), 200d 47.08 (-3.6%); 50d above 200d
Momentum: RSI(14) 34.5 | MACD -0.343 vs signal -0.044 (histogram -0.300)
Returns: 1d -0.1% | 5d -5.4% | 1m -5.1% | 3m -7.5%
52-week range: 41.34 - 49.39 (now 50.4% of the way up)
Volatility: ATR(14) 0.64 (1.4% of price) | annualised 20d 21.7%
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
Three-year record: +17.3% a year | beta to the market 0.66
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
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 2.07 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +20.7% above the current prices
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
Share count change: 1 week: +0.0% (0.00) over 10d | 1 month: +0.0% (0.00) over 30d
Shares outstanding: 67.80M | fund size: 3.08B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Mexico (EWW) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Neutral overall as no material macro surprise, policy shift, or decisive technical break on heavy volume is present. Technicals are bearish, macro stress is elevated, but analyst coverage is bullish and fundamentals are relatively cheap, leading to a balanced view.

**Main reasons it gave:**
- VIX up 10.2 points on the week, indicating heightened market stress
- EWW price below 20‑day, 50‑day and 200‑day SMAs; RSI 37.1 and MACD negative
- Fund flows flat over the past week and month, showing no net demand
- Analyst coverage of 47.5% of holdings all buy with a +19% price target

<details><summary><b>News</b> — score +0.00</summary>

_No news found for this one today._

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.14% (+0.02 on the week) | 5-year 4.78% (-0.20 on the week) | 10-year 4.99% (-0.17 on the week) | 30-year 5.37% (-0.11 on the week)
Yield curve, 10-year minus 3-month: +0.84 points -- upward sloping (normal)
US dollar index: 103.69 (+0.28 on the week)
Volatility (VIX): 29.46 (+10.2 on the week) -- stressed
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.1% (2026-10-01) | jobless claims 203k (2026-11-14)
Policy and expectations: Fed target 4.00% | market expects 2.2% inflation over 10 years
Rate path: 2-year Treasury 4.80% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score -0.20</summary>

```text
Last close 72.75 (bar of 2026-11-20), from 502 daily bars
Trend: vs 20d SMA 75.66 (-3.9%), 50d 74.22 (-2.0%), 200d 76.14 (-4.5%); 50d below 200d
Momentum: RSI(14) 37.1 | MACD -0.052 vs signal 0.481 (histogram -0.533)
Returns: 1d +0.3% | 5d -5.7% | 1m -2.9% | 3m -5.7%
52-week range: 66.02 - 81.23 (now 44.2% of the way up)
Volatility: ATR(14) 1.41 (1.9% of price) | annualised 20d 21.3%
Volume: 0.11x the 20-day average
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
Three-year record: +9.7% a year | beta to the market 0.99
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
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 1.91 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +19.0% above the current prices
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
Shares outstanding: 18.90M | fund size: 1.37B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### South Africa (EZA) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> No macro surprise or policy shift; technicals show a downtrend with low volume; fund flows flat; analyst view bullish but technicals weak, leading to a neutral overall stance.

**Main reasons it gave:**
- VIX up 10.2 points to 29.46, indicating stressed market conditions
- Price 58.06, 9.2% below 20‑day SMA (downtrend)
- RSI 30.3 (near oversold) with volume 0.03× 20‑day average, suggesting low conviction
- Fund flows flat (0% change) over past month, indicating no net demand
- Analyst coverage 100% buy with +44.2% price target, but technicals weak

<details><summary><b>News</b> — score +0.00</summary>

_No news found for this one today._

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.14% (+0.02 on the week) | 5-year 4.78% (-0.20 on the week) | 10-year 4.99% (-0.17 on the week) | 30-year 5.37% (-0.11 on the week)
Yield curve, 10-year minus 3-month: +0.84 points -- upward sloping (normal)
US dollar index: 103.69 (+0.28 on the week)
Volatility (VIX): 29.46 (+10.2 on the week) -- stressed
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.1% (2026-10-01) | jobless claims 203k (2026-11-14)
Policy and expectations: Fed target 4.00% | market expects 2.2% inflation over 10 years
Rate path: 2-year Treasury 4.80% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 58.06 (bar of 2026-11-20), from 502 daily bars
Trend: vs 20d SMA 63.93 (-9.2%), 50d 64.72 (-10.3%), 200d 67.71 (-14.3%); 50d below 200d
Momentum: RSI(14) 30.3 | MACD -1.306 vs signal -0.445 (histogram -0.861)
Returns: 1d +0.2% | 5d -10.1% | 1m -9.1% | 3m -18.6%
52-week range: 57.96 - 81.60 (now 0.4% of the way up)
Volatility: ATR(14) 1.55 (2.7% of price) | annualised 20d 36.7%
Volume: 0.03x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.50</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score +0.50</summary>

```text
Fund type: Focused Region
What it holds: P/E 10.65 | P/B 1.96 | P/S 1.68 | 3y earnings growth n/a
Yield: 8.2%
Three-year record: +20.3% a year | beta to the market 1.12
Cost and size: expense ratio 0.59% | net assets 438.81M
What it is made of: Stocks 99.9%, Cash 0.1%
Largest holdings: Anglogold Ashanti PLC 11.3%, Naspers Ltd Class N 8.4%, Gold Fields Ltd 8.2%, Firstrand Ltd 7.5%, Standard Bank Group Ltd 6.4%
Sector mix: Financial services 36.0%, Basic materials 35.9%, Consumer cyclical 13.0%, Communication services 7.2%
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
Rolled up from the 5 largest holdings, 41.8% of the fund by weight
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 1.99 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +44.2% above the current prices
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
Shares outstanding: 7.90M | fund size: 458.67M
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Gold mining companies (GDX) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Mixed signals: strong bullish analyst consensus (+37.6% price target) and robust inflows (+14.1% share count weekly) versus bearish technicals (price below 20‑, 50‑, 200‑day SMAs, RSI 31.8) and macro pressure from higher rates and a strong dollar. No material policy surprise or decisive technical break, so overall neutral.

**Main reasons it gave:**
- Analyst consensus 100% buy with +37.6% price target
- Strong weekly inflows: share count +14.1% (2.77B) over 7 days
- Technical downtrend: price below 20‑, 50‑, 200‑day SMAs, RSI 31.8
- Macro: higher rates and strong dollar pressure gold prices lower

<details><summary><b>News</b> — score +0.00</summary>

- [GDXJ: Gold At $3800 Isn't The End Of The Bull Case (NYSEARCA:GDXJ)](https://seekingalpha.com/article/4970497-gdxj-gold-at-3800-isnt-the-end-of-the-bull-case)  
  <sub>Seeking Alpha, 6 hours ago</sub>  
  VanEck Junior Gold Miners ETF is a cautious Buy after falling 16.34% YTD; its 11.15x trailing P/E offers a reasonable entry point.
- [VanEck Junior Gold Miners ETF down 16.34% YTD b...](https://pluang.com/en/news-feed/gdxj-emas-di-3800-bukan-akhir-dari-kasus-bull)  
  <sub>Pluang, 6 hours ago</sub>  
  VanEck Junior Gold Miners ETF (GDXJ) has fallen 16.34% year-to-date, presenting a cautious buying opportunity with a trailing P/E of 11.15x.
- [GDXJ Stock Price, Quote & News](https://www.google.com/goto?url=CAESYAHEIkXXtpTub_wsgB83ru-CnRNrc0yPgofNYtLUMW79EFBprE4VvmxvRWUmN1Kt2-gR92RVmvzUDWYOE0y7jhi469Mr2X1QycerHd5_SPnqNgnIvhrl6aV2QhGpUmps2Q&gsessionid=wLWSVA-IPSe4VaWnMTcwxB19L7BpPrWM1WyBzBYO0ZyKpJPaNOTyDw)  
  <sub>Syfe, 22 hours ago</sub>  
  Overview. VanEck Junior Gold Miners ETF (GDXJ) is trading at US$87.73, down 2.60% today as of Nov 19, 11:26 EST. Over the past 52 weeks, GDXJ has traded between...
- [GDX Nov 2026 105.000 put (GDX261118P00105000) Seasonal returns chart - Yahoo Finance](https://www.google.com/goto?url=CAESfwHEIkXX35TCxzElHbBKzlpL-Iuh00zdxP6AxdEC8_8Ypmjf-2RQJ07A5yikNu3ZT7a4_7sbXoBpR9BVAknvbfiht2O5IhJwLohBvm4TmUrqUb5xBWVB7_OTqO3y_NN92XCDeMpqahF1kUryF4DSA221NMi73HfwibeDz5Q_M30&gsessionid=wLWSVA-IPSe4VaWnMTcwxB19L7BpPrWM1WyBzBYO0ZyKpJPaNOTyDw)  
  <sub>Yahoo Finance Singapore, 23 hours ago</sub>  
  GDX Nov 2026 105.000 put (GDX261118P00105000) seasonal returns chart provides the mean and median returns by month to inform your investment strategy.
- [Gold slide deepens as market anxiety overtakes real-rate pressures (GLD:NYSEARCA)](https://www.google.com/goto?url=CAES5wEBxCJF1-dUjEgcf3egTyhtI2jyC6FQmpgR2AjrLNB3h82_eW8pPUMQNDCdo07qebjEnNe15dLEx4GMu0LwULmavlSCmUteGCmv4rc_4BMJnOBMpUfYMbYN59HaX23MSXqjcF_N54ccYiuq26zZTcXKKGZUqZ0Vc6VeQvapn4uZDSSjlEtIAn211Mo1y1xAV_Udd3Vrb0r2qVde8fkomkBnNn87YQHokT2XyVbQkDbMt4IoUp0FqEqZnMrzO5G2ltuPnSTS-v7UI6x8tkaNilYtZT7WFZevYBFQ2vGQ-ZCshfV4QXTjvQw&gsessionid=wLWSVA-IPSe4VaWnMTcwxB19L7BpPrWM1WyBzBYO0ZyKpJPaNOTyDw)  
  <sub>Seeking Alpha, 4 hours ago</sub>  
  Gold prices are tumbling as the Federal Reserve's aggressive rate-hiking cycle sparks a "fear factor" in markets that may be triggering a deleveraging wave,...
- [GDX Nov 2026 88.000 call (GDX261118C00088000) interactive stock chart – Yahoo Finance](https://www.google.com/goto?url=CAESeQHEIkXX9nP0aZYG8i3ubMQrvTUpp_FnAS0O0bbhE4cTHOPrRx0oPBN5HMdNDsHMa0mpkl4esvb-z3966LV1gCCE_yaItXuJl7O5jfJR30Qlonseomo8pfCglraSaDAGfuDkiXYpw0lMeGFR-R8YVkTyZicCKkEzPA8&gsessionid=wLWSVA-IPSe4VaWnMTcwxB19L7BpPrWM1WyBzBYO0ZyKpJPaNOTyDw)  
  <sub>Yahoo Finance Singapore, 20 hours ago</sub>  
  Interactive chart for GDX Nov 2026 88.000 call (GDX261118C00088000) – analyse all of the data with a huge range of indicators.
- [GDX ETF Price, Price Change and Fund Facts](https://www.google.com/goto?url=CAESZAHEIkXXnTDOSKr9TWJRrEAhZ_5Xv68hGPyvwqLOYqzm7HFBxB3pbwu1pHCZzLfjMOulo4yz3jOpamKHXKi1nJKfwX5TZdZ_52BJqpvhgiuk8I7Cjbqlh5X-_-LruwHR4rJAXj8&gsessionid=wLWSVA-IPSe4VaWnMTcwxB19L7BpPrWM1WyBzBYO0ZyKpJPaNOTyDw)  
  <sub>SilverTrade, 18 hours ago</sub>  
  The GDX share price, delayed, on a daily chart with indicators and drawing tools, its price change against gold, and the four miners ETFs side by side.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.14% (+0.02 on the week) | 5-year 4.78% (-0.20 on the week) | 10-year 4.99% (-0.17 on the week) | 30-year 5.37% (-0.11 on the week)
Yield curve, 10-year minus 3-month: +0.84 points -- upward sloping (normal)
US dollar index: 103.69 (+0.28 on the week)
Volatility (VIX): 29.46 (+10.2 on the week) -- stressed
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.1% (2026-10-01) | jobless claims 203k (2026-11-14)
Policy and expectations: Fed target 4.00% | market expects 2.2% inflation over 10 years
Rate path: 2-year Treasury 4.80% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score -0.50</summary>

```text
Last close 70.70 (bar of 2026-11-20), from 502 daily bars
Trend: vs 20d SMA 81.20 (-12.9%), 50d 85.98 (-17.8%), 200d 89.07 (-20.6%); 50d below 200d
Momentum: RSI(14) 31.8 | MACD -3.113 vs signal -1.924 (histogram -1.189)
Returns: 1d -1.8% | 5d -13.4% | 1m -13.5% | 3m -31.7%
52-week range: 70.70 - 115.84 (now 0.0% of the way up)
Volatility: ATR(14) 3.43 (4.8% of price) | annualised 20d 59.8%
Volume: 0.22x the 20-day average
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
Three-year record: +39.7% a year | beta to the market 0.98
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
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 1.71 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +37.6% above the current prices
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
Direction: money coming in (1 month)
Share count change: 1 week: +14.1% (2.77B) over 7d | 1 month: +4.9% (1.05B) over 30d
Shares outstanding: 317.94M | fund size: 22.48B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Software (IGV) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Neutral overall; no material macro surprise, flat fund flows, weak technical momentum, and bullish analyst view limited to 42% of holdings.

**Main reasons it gave:**
- Fund flows flat: 0% net change in share count over 1 week and 1 month
- Technical momentum weak: RSI 33.3 (oversold) and MACD negative
- Macro unchanged: Treasury yields stable, no policy surprise
- Analyst view bullish for 42.2% of holdings: 100% buy rating, +40% price target

<details><summary><b>News</b> — score +0.00</summary>

- [iShares Expanded Tech-Software ETF (Derivatives) to Euro Price Today | Live IGV to EUR Converter & Exchange Rate](https://cryptorank.io/price/ishares-expanded-tech-software-etf-derivatives/eur)  
  <sub>CryptoRank, 11 hours ago</sub>  
  Current iShares Expanded Tech-Software ETF (Derivatives) (IGV) token data: Price to Euro (EUR) - € 86.41, Trading Volume 97.00K, Market Cap N/A.
- [iShares Expanded Tech-Software ETF (Derivatives)](https://cryptorank.io/price/ishares-expanded-tech-software-etf-derivatives/cny)  
  <sub>CryptoRank, 11 hours ago</sub>  
  Current iShares Expanded Tech-Software ETF (Derivatives) (IGV) token data: Price to Chinese Yuan (CNY) - CN¥ 633.26, Trading Volume 710.89K, Market Cap N/A.
- [iShares Expanded Tech-Software ETF (Derivatives) Exchanges IGV Markets | Buy & Sell & Trade](https://www.google.com/goto?url=CAESkQEBxCJF16EFvcy1HQhwgUUDy1_eZDj8tEe-debt-vgpE8a95ujB37P5Vkr7-irv4Cd87gJMVn3XdWMqo0DOoXeB1r2id_EO3hMYBrgC4LtYAKptyZxUv7G-CL81eyYKbk9wRTloUB1tmhi-TG3V34eLUDKObw6ka18bSAZPIHNrU6VVAgbgcW50OX0e1KJlZSml&gsessionid=qg6PFnkpvKBgB-p0kRlk6KVTjMeYR52zHPfLM6-XTY8MI9P0ucYHWw)  
  <sub>CryptoRank, 11 hours ago</sub>  
  Discover 7 Best Exchanges Offering 1 IGV Markets for Buying, Selling, and Trading iShares Expanded Tech-Software ETF (Derivatives). Get insights on spread,...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.14% (+0.02 on the week) | 5-year 4.78% (-0.20 on the week) | 10-year 4.99% (-0.17 on the week) | 30-year 5.37% (-0.11 on the week)
Yield curve, 10-year minus 3-month: +0.84 points -- upward sloping (normal)
US dollar index: 103.69 (+0.28 on the week)
Volatility (VIX): 29.46 (+10.2 on the week) -- stressed
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.1% (2026-10-01) | jobless claims 203k (2026-11-14)
Policy and expectations: Fed target 4.00% | market expects 2.2% inflation over 10 years
Rate path: 2-year Treasury 4.80% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score -0.20</summary>

```text
Last close 95.14 (bar of 2026-11-20), from 502 daily bars
Trend: vs 20d SMA 102.15 (-6.9%), 50d 105.54 (-9.9%), 200d 94.45 (+0.7%); 50d above 200d
Momentum: RSI(14) 33.3 | MACD -2.849 vs signal -2.177 (histogram -0.673)
Returns: 1d -1.0% | 5d -6.0% | 1m -12.5% | 3m -7.1%
52-week range: 74.67 - 112.67 (now 53.9% of the way up)
Volatility: ATR(14) 3.04 (3.2% of price) | annualised 20d 30.7%
Volume: 0.15x the 20-day average
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
Three-year record: +9.0% a year | beta to the market 1.25
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
Weighted price target: +40.2% above the current prices
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

### India (INDA) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Neutral overall; bullish analyst view is thin, bearish fund outflows dominate, fundamentals are modest, macro stress and mixed technicals support a balanced stance.

**Main reasons it gave:**
- Analyst view: 100% buy rating on top 5 holdings (+11.8% price target) but only 24.8% weight
- Fund flows: net outflows of -7.5% over the month (~$491M) indicating bearish sentiment
- Macro: VIX up 10.2 points to 29.46, indicating stressed market conditions
- Technical: RSI 77.9 (overbought) and volume at 0.17x 20‑day average
- Fund basics: P/E 21.32 and three‑year return +4.8% a year, modest valuation and performance

<details><summary><b>News</b> — score +0.00</summary>

- [Ask India: Deutsche Bank says AI adoption outweighs model race (INDA:BATS)](https://seekingalpha.com/news/4674800-ask-india-deutsche-bank-says-ai-adoption-outweighs-model-race?utm_source=feed_news_all&utm_medium=referral&feed_item_type=news)  
  <sub>Seeking Alpha, 22 hours ago</sub>  
  India (INDA) is emerging as the premier test case for whether adopting AI at scale matters more than building frontier models, offering investors a unique...
- [SMIN: The Stars Appear To Be Aligning (Rating Upgrade)](https://seekingalpha.com/article/4970148-smin-stars-appear-to-be-aligning-rating-upgrade)  
  <sub>Seeking Alpha, 23 hours ago</sub>  
  The iShares MSCI India Small-Cap ETF has barely moved and performed in line with global stocks since I last covered it in February 2026 (3%),...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.14% (+0.02 on the week) | 5-year 4.78% (-0.20 on the week) | 10-year 4.99% (-0.17 on the week) | 30-year 5.37% (-0.11 on the week)
Yield curve, 10-year minus 3-month: +0.84 points -- upward sloping (normal)
US dollar index: 103.69 (+0.28 on the week)
Volatility (VIX): 29.46 (+10.2 on the week) -- stressed
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.1% (2026-10-01) | jobless claims 203k (2026-11-14)
Policy and expectations: Fed target 4.00% | market expects 2.2% inflation over 10 years
Rate path: 2-year Treasury 4.80% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 53.12 (bar of 2026-11-20), from 502 daily bars
Trend: vs 20d SMA 50.06 (+6.1%), 50d 48.36 (+9.9%), 200d 49.09 (+8.2%); 50d below 200d
Momentum: RSI(14) 77.9 | MACD 1.243 vs signal 1.042 (histogram 0.201)
Returns: 1d +2.1% | 5d +3.3% | 1m +12.2% | 3m +7.6%
52-week range: 45.42 - 54.72 (now 82.8% of the way up)
Volatility: ATR(14) 0.57 (1.1% of price) | annualised 20d 14.0%
Volume: 0.17x the 20-day average
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
Three-year record: +4.8% a year | beta to the market 0.61
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

<details><summary><b>What analysts and big funds say</b> — score +0.20</summary>

_Not available today._

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score +0.20</summary>

```text
Rolled up from the 5 largest holdings, 24.8% of the fund by weight  -- thin, so read this as a fact about that slice rather than the fund
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 1.37 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +11.8% above the current prices
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
Share count change: 1 week: +0.8% (50.72M) over 7d | 1 month: -7.5% (-491.44M) over 30d
Shares outstanding: 113.89M | fund size: 6.05B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Defence and aerospace (ITA) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Neutral overall: no macro surprise, technicals in downtrend with low volume, strong analyst buy rating and price target, massive inflows, but high valuation metrics suggest overvaluation.

**Main reasons it gave:**
- No macro surprise; yields stable and VIX up modestly
- Technical downtrend: price below 20-day, 50-day and 200-day SMAs, RSI 44.4
- Analyst view: 100% buy rating with +20.4% price target covering 54.8% of fund
- Fund flows: share count up 202% in past month, indicating strong demand
- Fund fundamentals: high valuation metrics (P/E 30.9, P/B 5.67) suggest overvaluation

<details><summary><b>News</b> — score +0.00</summary>

_No news found for this one today._

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.14% (+0.02 on the week) | 5-year 4.78% (-0.20 on the week) | 10-year 4.99% (-0.17 on the week) | 30-year 5.37% (-0.11 on the week)
Yield curve, 10-year minus 3-month: +0.84 points -- upward sloping (normal)
US dollar index: 103.69 (+0.28 on the week)
Volatility (VIX): 29.46 (+10.2 on the week) -- stressed
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.1% (2026-10-01) | jobless claims 203k (2026-11-14)
Policy and expectations: Fed target 4.00% | market expects 2.2% inflation over 10 years
Rate path: 2-year Treasury 4.80% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score -0.30</summary>

```text
Last close 68.80 (bar of 2026-11-20), from 502 daily bars
Trend: vs 20d SMA 70.31 (-2.2%), 50d 69.95 (-1.6%), 200d 75.73 (-9.1%); 50d below 200d
Momentum: RSI(14) 44.4 | MACD -0.223 vs signal 0.007 (histogram -0.231)
Returns: 1d +0.9% | 5d -3.8% | 1m +0.9% | 3m -11.6%
52-week range: 66.08 - 84.41 (now 14.9% of the way up)
Volatility: ATR(14) 1.69 (2.5% of price) | annualised 20d 32.3%
Volume: 0.09x the 20-day average
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
Three-year record: +22.5% a year | beta to the market 1.03
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

<details><summary><b>What analysts and big funds say</b> — score +0.45</summary>

_Not available today._

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score +0.45</summary>

```text
Rolled up from the 5 largest holdings, 54.8% of the fund by weight
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 1.74 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +20.4% above the current prices
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
Share count change: 1 week: +3.9% (458.15M) over 7d | 1 month: +202.4% (8.08B) over 30d
Shares outstanding: 175.51M | fund size: 12.07B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Transport and delivery (IYT) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Neutral overall: no macro surprise, technicals mixed, modest inflows, bullish analyst view but limited coverage.

**Main reasons it gave:**
- Weekly share count rose 1.8% (34.5M) and monthly +3.2% (60.99M) indicating modest net inflows
- Analyst coverage of top holdings (52% weight) is 90.9% buy with a weighted price target +19.5% above current prices
- Technicals mixed: price below 20‑day SMA, 50‑day SMA below 200‑day SMA, RSI 48, MACD negative, volume 0.05× 20‑day average
- Macro environment stressed: VIX up 10.2 points to 29.5, Fed expected to hike further, yields high

<details><summary><b>News</b> — score +0.00</summary>

- [iShares U.S. Transportation ETF (IYT) Stock Price, News, Quote & History](https://ca.finance.yahoo.com/quote/IYT/)  
  <sub>Yahoo! Finance Canada, 18 hours ago</sub>  
  The fund generally will invest at least 80% of its assets in the component securities of its underlying index. The underlying index measures the performance of...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.14% (+0.02 on the week) | 5-year 4.78% (-0.20 on the week) | 10-year 4.99% (-0.17 on the week) | 30-year 5.37% (-0.11 on the week)
Yield curve, 10-year minus 3-month: +0.84 points -- upward sloping (normal)
US dollar index: 103.69 (+0.28 on the week)
Volatility (VIX): 29.46 (+10.2 on the week) -- stressed
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.1% (2026-10-01) | jobless claims 203k (2026-11-14)
Policy and expectations: Fed target 4.00% | market expects 2.2% inflation over 10 years
Rate path: 2-year Treasury 4.80% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 81.64 (bar of 2026-11-20), from 502 daily bars
Trend: vs 20d SMA 82.58 (-1.1%), 50d 81.03 (+0.8%), 200d 82.08 (-0.5%); 50d below 200d
Momentum: RSI(14) 48.0 | MACD 0.302 vs signal 0.535 (histogram -0.232)
Returns: 1d +1.0% | 5d -2.5% | 1m -0.3% | 3m -6.0%
52-week range: 68.14 - 90.01 (now 61.8% of the way up)
Volatility: ATR(14) 1.56 (1.9% of price) | annualised 20d 27.7%
Volume: 0.05x the 20-day average
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
Three-year record: +12.6% a year | beta to the market 1.24
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

<details><summary><b>What analysts and big funds say</b> — score +0.45</summary>

_Not available today._

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score +0.45</summary>

```text
Rolled up from the 5 largest holdings, 52.2% of the fund by weight
Ratings by weight: buy 90.9% | hold 9.1% | sell 0.0% (mean 1.87 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +19.5% above the current prices
Holdings read: UNP, UBER, CSX, UPS, NSC
Recent rating changes among them:
  - UNP: 2026-11-05 Baird: down, Outperform -> Neutral
  - UBER: 2026-11-06 UBS: main, Buy -> Buy
  - CSX: 2026-10-27 Susquehanna: main, Positive -> Positive
  - UPS: 2026-10-28 UBS: main, Buy -> Buy
  - NSC: 2026-10-23 Citigroup: main, Neutral -> Neutral
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
Share count change: 1 week: +1.8% (34.49M) over 7d | 1 month: +3.2% (60.99M) over 34d
Shares outstanding: 24.34M | fund size: 1.99B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### US regional banks (KRE) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Neutral overall as no macro surprise, technicals are bearish, but modest inflows and slightly positive fundamentals and analyst view provide limited bullish bias.

**Main reasons it gave:**
- Fund flows: +5.9% share count increase over 30 days
- Technical: price below 20‑day, 50‑day, 200‑day SMAs; RSI 40.3; MACD negative
- Macro: yields stable, no policy surprise; VIX up 10.2 points indicating stress
- Analyst view thin (5.9% coverage) with price target +14.7% bullish
- Fundamentals: low P/E 12.17, P/B 1.26, 3‑year record +19.1% annual return

<details><summary><b>News</b> — score +0.00</summary>

- [Daily ETF Flows: ARKW Makes An Appearance](https://www.etf.com/sections/daily-etf-flows/daily-etf-flows-arkw-makes-appearance)  
  <sub>ETF.com, 21 hours ago</sub>  
  Here are the daily ETF fund flows for November 18, 2026.
- [KRE Dec 2026 74.000 call (KRE261204C00074000) Stock Price, News, Quote & History](https://ca.finance.yahoo.com/quote/KRE261204C00074000/)  
  <sub>Yahoo! Finance Canada, 23 hours ago</sub>  
  Find the latest KRE Dec 2026 74.000 call (KRE261204C00074000) stock quote, history, news and other vital information to help you with your stock trading and...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.14% (+0.02 on the week) | 5-year 4.78% (-0.20 on the week) | 10-year 4.99% (-0.17 on the week) | 30-year 5.37% (-0.11 on the week)
Yield curve, 10-year minus 3-month: +0.84 points -- upward sloping (normal)
US dollar index: 103.69 (+0.28 on the week)
Volatility (VIX): 29.46 (+10.2 on the week) -- stressed
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.1% (2026-10-01) | jobless claims 203k (2026-11-14)
Policy and expectations: Fed target 4.00% | market expects 2.2% inflation over 10 years
Rate path: 2-year Treasury 4.80% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score -0.20</summary>

```text
Last close 69.86 (bar of 2026-11-20), from 502 daily bars
Trend: vs 20d SMA 72.25 (-3.3%), 50d 71.36 (-2.1%), 200d 71.21 (-1.9%); 50d above 200d
Momentum: RSI(14) 40.3 | MACD -0.310 vs signal 0.102 (histogram -0.411)
Returns: 1d +0.9% | 5d -4.0% | 1m -3.5% | 3m -6.6%
52-week range: 59.59 - 77.93 (now 56.0% of the way up)
Volatility: ATR(14) 1.39 (2.0% of price) | annualised 20d 20.1%
Volume: 0.18x the 20-day average
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
Three-year record: +19.1% a year | beta to the market 0.97
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

<details><summary><b>What analysts and big funds say</b> — score +0.20</summary>

_Not available today._

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score +0.20</summary>

```text
Rolled up from the 5 largest holdings, 5.9% of the fund by weight  -- thin, so read this as a fact about that slice rather than the fund
Ratings by weight: buy 50.1% | hold 49.9% | sell 0.0% (mean 2.45 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +14.7% above the current prices
Holdings read: GBCI, UCB, TXCP, OZK, EBC
Recent rating changes among them:
  - GBCI: 2026-10-26 Piper Sandler: main, Overweight -> Overweight
  - UCB: 2026-10-21 Stephens & Co.: main, Overweight -> Overweight
  - TXCP: 2026-11-03 Barclays: main, Equal-Weight -> Equal-Weight
  - OZK: 2026-10-30 Keefe, Bruyette & Woods: main, Market Perform -> Market Perform
  - EBC: 2026-11-03 Barclays: main, Equal-Weight -> Equal-Weight
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
Share count change: 1 week: +3.1% (120.07M) over 7d | 1 month: +5.9% (220.93M) over 30d
Shares outstanding: 56.52M | fund size: 3.95B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Saudi Arabia (KSA) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Mixed signals: bullish analyst coverage (+17.4% price target) vs bearish fund outflows and technical weakness; no macro surprise.

**Main reasons it gave:**
- Analyst coverage of top holdings (45.3% of fund) shows 100% buy rating and +17.4% price target
- Fund flows show net outflow of -6.3% over the past month, indicating bearish sentiment
- Technical indicators show price below 50‑day and 200‑day SMA, low volume, mixed momentum

<details><summary><b>News</b> — score +0.00</summary>

- [Ashoka Buildcon shares tank 6% as ₹846-cr Saudi Arabia project cancelled](https://www.business-standard.com/markets/news/ashoka-buildcon-shares-tank-6-as-846-cr-saudi-arabia-project-cancelled-126112000220_1.html)  
  <sub>Business Standard, 11 hours ago</sub>  
  Ashoka Buildcon share price: According to a press release shared by the company, a Saudi Arabia project worth Rs ₹846.38 crore was cancelled by Diriyah...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.14% (+0.02 on the week) | 5-year 4.78% (-0.20 on the week) | 10-year 4.99% (-0.17 on the week) | 30-year 5.37% (-0.11 on the week)
Yield curve, 10-year minus 3-month: +0.84 points -- upward sloping (normal)
US dollar index: 103.69 (+0.28 on the week)
Volatility (VIX): 29.46 (+10.2 on the week) -- stressed
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.1% (2026-10-01) | jobless claims 203k (2026-11-14)
Policy and expectations: Fed target 4.00% | market expects 2.2% inflation over 10 years
Rate path: 2-year Treasury 4.80% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score -0.20</summary>

```text
Last close 35.25 (bar of 2026-11-20), from 502 daily bars
Trend: vs 20d SMA 35.13 (+0.3%), 50d 35.77 (-1.5%), 200d 37.68 (-6.4%); 50d below 200d
Momentum: RSI(14) 46.9 | MACD 0.013 vs signal -0.064 (histogram 0.078)
Returns: 1d +0.3% | 5d -2.1% | 1m +4.6% | 3m -9.7%
52-week range: 33.69 - 40.63 (now 22.5% of the way up)
Volatility: ATR(14) 0.33 (0.9% of price) | annualised 20d 14.7%
Volume: 0.44x the 20-day average
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
Three-year record: -0.6% a year | beta to the market 0.20
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
Share count change: 1 week: +1.0% (5.44M) over 7d | 1 month: -6.3% (-37.31M) over 30d
Shares outstanding: 15.61M | fund size: 550.36M
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### China (MCHI) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> The fund has an extremely bullish analyst view (100% buy rating, +79% price target) but technicals show a clear downtrend (price below 20‑day, 50‑day, 200‑day SMAs, RSI 25) and macro conditions are risk‑off (VIX up 10.2 points to 29.46, dollar index higher). Fund flows are mixed, with a net outflow of -2.2% over the month despite a +6.1% weekly inflow. No material policy surprise or decisive technical break occurred, so the overall stance remains neutral.

**Main reasons it gave:**
- Analyst view: 100% buy rating with +79% price target (strong bullish)
- Technicals: price below 20‑day, 50‑day, 200‑day SMAs, RSI 25 (bearish momentum)
- Macro: VIX up 10.2 points to 29.46, dollar index up 0.28 (risk‑off environment)
- Fund flows: net outflow of -2.2% over month despite +6.1% weekly inflow (mixed)

<details><summary><b>News</b> — score +0.00</summary>

- [How Can ETFs Soften Alibaba Risk As Chip Scrutiny Grows?](https://simplywall.st/etfs/us/nasdaq-aia/news/how-can-etfs-soften-alibaba-risk-as-chip-scrutiny-grows)  
  <sub>Simply Wall St, 2 hours ago</sub>  
  If you like Alibaba Group Holding for its e-commerce reach and cloud services, you need to remember that holding the stock directly means taking on its...
- [Why Alibaba’s Risks May Look Different Inside 3 ETFs](https://finance.yahoo.com/markets/stocks/articles/why-alibaba-risks-may-look-141157680.html)  
  <sub>Yahoo Finance, 43 minutes ago</sub>  
  You might like Alibaba Group Holding for its e commerce reach or cloud ambitions, but owning the stock directly means carrying its own company specific...
- [AI Selloff Spreads From Wall Street To Asia Despite Anthropic Debut: SPY, QQQ, DIA, Asian Stocks Head For Steep Weekly Losses](https://www.google.com/goto?url=CAES9AEBxCJF185vMq3WjuQmhd6UNlS4WwyqHlNEynkMYdOtCMDok1FhPzRBamGKf5IQlhym25hd7X_wxn5eT25st-MgUgEazMEU1rzjHM_Jn5QBM27WLV_WUQbB-LBcR0h91Vyq9P3dmAPVWsZk2ofLNBcB4fxbK6U5s_UmULbw4AXsmAxXck7hpVc8J80gZaWT9EpB8p8em46m8fE98edlBLmbGV05CeQ9LfYu20_tYsnogwY8x0V_a0Ll0F06tCXup8gYCQBEKiEEV-R8Br_GqP8LsDXcx1keqB9ro6K1pbwG5RVn9Vn8hokjf6wQNRtzw3IM7AGA&gsessionid=S6chH6z-UTNubhCpO_bhN-DaagcyUsvW8svOeEWGFUm17gB1rjbhWg)  
  <sub>TradingView, 10 hours ago</sub>  
  Global stock markets are headed for a steep red close this week despite Claude-maker Anthropic's (ANT) record debut on the Nasdaq.
- [SPY, QQQ, DIA, Asian Stocks Plunge As Anthropic’s Record IPO Fails To Stop AI Rout](https://www.google.com/goto?url=CAEStAEBxCJF17TFkItDp0nBiRW3O8Wy6nb4oL2JbO7MS_P-sTNiJIbaC9BXiCbT0c-kY8EQu942Z4DdaqJi6NCSp-ZLlswv-TCyavvOsRN6TkgW_aUYboZMPHQYY0pNJZEAYgwVqqbsNSrVILDOaLgYREoYdJD3PrX4BKaJlZYbCC8F3RXNkLxzDISprSzojS8lpejyUjC9Cesx1ek8Zs_gZQCe7fs58HLCGFRYA-xDrZfts8Wl6q0&gsessionid=S6chH6z-UTNubhCpO_bhN-DaagcyUsvW8svOeEWGFUm17gB1rjbhWg)  
  <sub>Stocktwits, 10 hours ago</sub>  
  While Anthropic's stock surged more than 17% on its debut on Thursday, other AI stocks across the U.S. and Asian markets fell sharply.
- [Anthropic Defies Tech Rout On Debut — Tom Lee Sees ‘Big Payoff’ Ahead And Says Cisco’s Wild 1997 Ride Shows Why](https://www.google.com/goto?url=CAESwQEBxCJF13xvC92BhzzQjIrME_mSRobBDRn00A7GkbcTKW4pG7t-vd25VCWwmmUIlQtzu0sQpBhb9xsS8kZ4UWZWHTZwhM4afUO4bF6yykBlcjHlqAPZ6eAiDIa8wqJQ9fStnEw3OF0CdZoAdIfKrmu27BxbQYOzaEV_z7J8pKA1ms_5rMy8vlnkatFNVGH0fvveyEIBr67bFizQAeC8njJxH3y4pPSN0-jeTxQBM4NdPGNifmJm55aMD5tnJ5Dkmtbz&gsessionid=S6chH6z-UTNubhCpO_bhN-DaagcyUsvW8svOeEWGFUm17gB1rjbhWg)  
  <sub>Stocktwits, 10 hours ago</sub>  
  After six straight S&P 500 losses, Lee noted that the index rose the following week in all 10 prior cases he analyzed.
- [Could Tesla Become The Next Lumentum? Gary Black Warns A SpaceX Stock Deal Could Send TSLA Down 25%](https://www.google.com/goto?url=CAESygEBxCJF1-iqJb07JcTs0SxK0dw_sh9q4jor08SOn-Yaz26YSXaLKxZ9AeMOTc7GEuruNrvwN12KhygQS_4pprDF5F-McklXjc0embQxAaDbgk6OVqY8VP_NE2oScZR_pYaZrnsoozYNu5-bs-FOp09tfhc9n5TenxY6FJjswAFxhM9bEAVys9B5cKBd_82KDstmmMub8jT2zKiZDk7T_hix9T1IILxeC8amYQJatavcyiQ6axtfQnIETmOk65yqzd-qZdRy7r4CXaqC&gsessionid=S6chH6z-UTNubhCpO_bhN-DaagcyUsvW8svOeEWGFUm17gB1rjbhWg)  
  <sub>Stocktwits, 9 hours ago</sub>  
  Lumentum CEO Michael Hurlston said upcoming earnings and a merger filing could help win back shareholders.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.14% (+0.02 on the week) | 5-year 4.78% (-0.20 on the week) | 10-year 4.99% (-0.17 on the week) | 30-year 5.37% (-0.11 on the week)
Yield curve, 10-year minus 3-month: +0.84 points -- upward sloping (normal)
US dollar index: 103.69 (+0.28 on the week)
Volatility (VIX): 29.46 (+10.2 on the week) -- stressed
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.1% (2026-10-01) | jobless claims 203k (2026-11-14)
Policy and expectations: Fed target 4.00% | market expects 2.2% inflation over 10 years
Rate path: 2-year Treasury 4.80% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score -0.40</summary>

```text
Last close 46.58 (bar of 2026-11-20), from 502 daily bars
Trend: vs 20d SMA 49.56 (-6.0%), 50d 51.02 (-8.7%), 200d 54.78 (-15.0%); 50d below 200d
Momentum: RSI(14) 25.1 | MACD -0.949 vs signal -0.611 (histogram -0.338)
Returns: 1d -0.9% | 5d -6.0% | 1m -5.0% | 3m -15.2%
52-week range: 46.58 - 64.26 (now 0.0% of the way up)
Volatility: ATR(14) 0.69 (1.5% of price) | annualised 20d 21.1%
Volume: 0.13x the 20-day average
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
Three-year record: +6.0% a year | beta to the market 0.47
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

<details><summary><b>What analysts and big funds say</b> — score +0.95</summary>

_Not available today._

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score +0.95</summary>

```text
Rolled up from the 5 largest holdings, 32.6% of the fund by weight
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 1.39 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +79.3% above the current prices
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
Direction: money going out (1 month)
Share count change: 1 week: +6.1% (308.24M) over 7d | 1 month: -2.2% (-119.98M) over 30d
Shares outstanding: 114.65M | fund size: 5.34B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Chip makers (SMH) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Neutral overall; macro risk and technical weakness offset by strong inflows and bullish analyst coverage.

**Main reasons it gave:**
- VIX up 10.2 points to 29.46, indicating heightened market stress
- SMH price below 20‑day, 50‑day and 200‑day SMAs; RSI 30.4; volume 0.17× 20‑day average
- Share count up 13.4% in past month, showing net inflows
- Analyst coverage 100% buy, weighted price target +61.7% above current price

<details><summary><b>News</b> — score +0.00</summary>

- [2026 Semiconductor Stock Selloff: The Long-Term Outlook](https://seekingalpha.com/article/4970526-2026-semiconductor-stock-selloff-long-term-outlook?source=generic_rss)  
  <sub>Seeking Alpha, 5 hours ago</sub>  
  Leadership within the semiconductor industry changes over time, which supports a diversified approach across each layer of the AI stack with a semiconductor...
- [S&P 500, Nasdaq, Dow End Lower As Anthropic Trading Debut Fails To Provide Adequate Confidence — ANT, META, AAPL, GME In Focus](https://www.tradingview.com/news/stocktwits:1104f5657094b:0-s-p-500-nasdaq-dow-end-lower-as-anthropic-trading-debut-fails-to-provide-adequate-confidence-ant-meta-aapl-gme-in-focus/)  
  <sub>TradingView, 16 hours ago</sub>  
  U.S. stock indices ended lower on Thursday, with the S&P 500 recording its longest losing streak since 2024 as Anthropic's first trading session failed to...
- [VanEck Semiconductor ETF up 28% in 2026, aiming for a fourth straight year beating S&P 500.](https://www.google.com/goto?url=CAESmwEBxCJF19fibn6LtZjPSzHOgmfHHrIqz72OZ54O6uCrCG9nv-umdWK_kUjL-c42-GXUmlsg1SrrRXnx2hxQ6gBT0WgTdiwM0OyecAyjKj8rp23337_DzkoRHatEbrUKzcWyB8dBB_QSQ3sfGwdmTnGidLDqMZVhWa-aVmTHiRCfcLoKD9UFP0-DKzhML4_xGKS9dgJoY_7cRGKTVQ&gsessionid=apNh4zf_O72-TwMnJ0XR5M3i68HC3GcZgJz_n5c15Yw4dwTYK4-ieQ)  
  <sub>Pluang, 14 hours ago</sub>  
  The VanEck Semiconductor ETF has risen about 28% in 2026, outperforming the S&P 500's 7% gain so far this year. If it maintains this lead, it will mark the...
- [The Semiconductor ETF Is on Track to Beat the S&P 500 for a 4th Straight Year. It Has Never Done That Before.](https://www.google.com/goto?url=CAESnAEBxCJF1wh7AeNmE1N1giJ5z_Bp7M-AX6E0bAa8LRfh_YIzOlHkM49bfh53eFvHZBN2WSbf8tikSq3nlM6x6EYS0EQxT1dmV1hN5F0oxX9O6SZSBxUVwmFDntqo3nkF8PMyJPqg77TEzbIY2DgSvZ1iKEIjrN4_JcpurcsbSTBJs_aC3kYD6S_nx7htzWvLkOxjTQAFmap_281bQKQ&gsessionid=apNh4zf_O72-TwMnJ0XR5M3i68HC3GcZgJz_n5c15Yw4dwTYK4-ieQ)  
  <sub>Yahoo Finance, 15 hours ago</sub>  
  The VanEck Semiconductor ETF (NASDAQ:SMH) closed on Nov. 17 at $460.10, putting it up around 28% in 2026. The S&P 500 (SNPINDEX:^GSPC) rose about 7% during...
- [Anthropic Soared in Its IPO. The ETFs That Held It Didn’t](https://www.google.com/goto?url=CAES1gEBxCJF19yo_EjgpyP9djUWDUhVnNVqd8vw-WsFrllk6V_qF8BgSp1uR0pCw3xzEK8j9JImFZn-b2vg7kH5F9kS3MZbBZpBE06TGEB-d6XnPHlCUGKNMoL46GW09HW4_yzi90Z_p23A4RFN4Va7jZH0yi7wHZDYs-PQQ7YrDHSvveeolQdrtw3nLthB5W_SSRyN0fevUHobwDxo7xlcjKHFky-xPDMDwn-W2IQuSlIw7-UaIozKfLiF4ipA8SxPSbqS9SxELrn-BvodV8G-qzKfpMxXVtJA&gsessionid=apNh4zf_O72-TwMnJ0XR5M3i68HC3GcZgJz_n5c15Yw4dwTYK4-ieQ)  
  <sub>ETF.com, 16 hours ago</sub>  
  Anthropic jumped 17% in its debut, but the Tema Photonics & Optical ETF (LAZR), one of the ETFs most heavily invested in the company, fell 3.3%.
- [Chip ETF Eyes Unprecedented Fourth Straight Year of Beating the S&P 500](https://www.google.com/goto?url=CAESgAEBxCJF1yshZDvODCWJsvw2vC9eVQT8SQOezLLayijUgVKLl_yGS7x5xe0yugYu1hZTHgVOfKMr4cADszzrCvtocJ8hpoX5NcU0uZs3VDpNTWn7W2AO37yMmHhqmeVLQRZJkh8pgA1wufh3VbxXiGkfNjUWHK8rCP7cWLxvOvParg&gsessionid=apNh4zf_O72-TwMnJ0XR5M3i68HC3GcZgJz_n5c15Yw4dwTYK4-ieQ)  
  <sub>BigGo Finance, 14 hours ago</sub>  
  The VanEck Semiconductor ETF is on pace to beat the S&P 500 for a fourth consecutive year, a first in its history, with a roughly 28% gain in 2026…
- [IMF’s Georgieva Sees Little More AI Market Correction Ahead – Here’s Her Take On What Could Lead To Potential Financial Stability Risks](https://www.google.com/goto?url=CAESgAIBxCJF1-IFOZdrQSl7k6iLuGTIu0laABDFQBi87ebyb7LH1S-36hYD5u6lY_hXOFlNJIZ_Q5ULXbTmE7RvKcv8FHv70fTtNjGtOTLPnP_e2Qzy0I9V4Ka42yEnDdAkSohKhkvTt9UWt13p1ALawMr8BeqYJ8rv8_w29om9vQadudDCeYO6TlfJzvBMyqJ4e5HBTJWKU4-qFtqAK3-gYqpBvAOmWEIXlgkdIhOP2lb24QBbi90-TKPXAW3Oe4uXhww583T2C845DkdoC3jJMkrJgK89WPO1bwWE04KnoDxheJ5fban2MiVy6IJfc-9vUMjtTMQjkfyMJ14Jo1JzEvHh&gsessionid=apNh4zf_O72-TwMnJ0XR5M3i68HC3GcZgJz_n5c15Yw4dwTYK4-ieQ)  
  <sub>TradingView, 23 hours ago</sub>  
  International Monetary Fund (IMF) Managing Director Kristalina Georgieva said Thursday that AI-related financial markets could face further correction,...
- [VanEck Semiconductor ETF Falls 7.54% Below Three Moving Averages](https://www.google.com/goto?url=CAESawHEIkXXq_KHKAwE7PIJMr401RlXZcLz2XGgkumYv-PwJ5s4ILpAt5xnMdVW1Zd0bxhz08_eJeWkJN6pAVdhcHthBC5353h0I265ZkT19nvzyESP7so_UQ-ZvFF4oB0_82lZp-ssV525qsRe&gsessionid=apNh4zf_O72-TwMnJ0XR5M3i68HC3GcZgJz_n5c15Yw4dwTYK4-ieQ)  
  <sub>www.tokenpost.com, 4 hours ago</sub>  
  The VanEck Semiconductor ETF (SMH) fell 7.54% over 24 hours to $438.48 in a Nov. 20 snapshot published at 5:42 a.m. ET (10:42 UTC), placing the fund below...
- [VanEck Semiconductor ETF (SMH) Price Prediction: Semiconductors Break Lower as Momentum Weakens and Positioning Turns Mixed](https://www.google.com/goto?url=CAESpgEBxCJF18M3V6kKPAU3qh4ASBIttsv6HRmoPjeZ82ttdjqKUNFHrJSfKFzgk7jG6HXw7BcxiVsK9UN4li1CQGfrPwGBm6vm8TuMLmZKdXewS95k0fK1rF_gqeMBAmcxOCDLspEmpGMFJkELriWKnCJyczjChH4gqkpWKvxTAzUFxNQApL57PThiRre1OBBTzf5eXs7m0QYTRUNtELYQ3OdV67B9YQNV&gsessionid=apNh4zf_O72-TwMnJ0XR5M3i68HC3GcZgJz_n5c15Yw4dwTYK4-ieQ)  
  <sub>blockchain.news, 4 hours ago</sub>  
  VanEck Semiconductor ETF (SMH) is trading at $438.48, down 7.54% on the day after a sharp slide that left price below the 7-, 20- and 50-day moving...
- [VanEck Semiconductor ETF (SMH) Price Prediction: Semiconductor ETF stalls below key averages as sellers lean on rebounds](https://www.google.com/goto?url=CAESowEBxCJF16kypUlEDL_kmcQw_T0spazE8EdyfvVLHFb2ij9D5x_YOgSz21Hm5ODQit_BnUbD7DHj5Hta4jJGX9uTWMBq7lAqvPoOumPFtAxFS7EAVyyZGuaesXm5NZCgZhCrJTMNI2UNC_-Lj0FBT1pOgqxnwVnh5SydqwLLDDTOTf6NnmBgKLAjUdm9bcwi1vkdU1XoTEeVmViZ0-9tUIE9_x62&gsessionid=apNh4zf_O72-TwMnJ0XR5M3i68HC3GcZgJz_n5c15Yw4dwTYK4-ieQ)  
  <sub>Blockchain News, 21 hours ago</sub>  
  VanEck Semiconductor ETF (SMH) is trading at $474.29, roughly flat on the day, after a sharp early-November selloff that pushed the fund well below its...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.14% (+0.02 on the week) | 5-year 4.78% (-0.20 on the week) | 10-year 4.99% (-0.17 on the week) | 30-year 5.37% (-0.11 on the week)
Yield curve, 10-year minus 3-month: +0.84 points -- upward sloping (normal)
US dollar index: 103.69 (+0.28 on the week)
Volatility (VIX): 29.46 (+10.2 on the week) -- stressed
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.1% (2026-10-01) | jobless claims 203k (2026-11-14)
Policy and expectations: Fed target 4.00% | market expects 2.2% inflation over 10 years
Rate path: 2-year Treasury 4.80% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score -0.30</summary>

```text
Last close 432.20 (bar of 2026-11-20), from 502 daily bars
Trend: vs 20d SMA 496.10 (-12.9%), 50d 548.15 (-21.2%), 200d 525.33 (-17.7%); 50d above 200d
Momentum: RSI(14) 30.4 | MACD -28.865 vs signal -25.182 (histogram -3.683)
Returns: 1d -3.4% | 5d -11.2% | 1m -17.4% | 3m -21.0%
52-week range: 325.10 - 668.91 (now 31.2% of the way up)
Volatility: ATR(14) 23.93 (5.5% of price) | annualised 20d 64.6%
Volume: 0.17x the 20-day average
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
Three-year record: +42.0% a year | beta to the market 2.12
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

<details><summary><b>What analysts and big funds say</b> — score +0.80</summary>

_Not available today._

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score +0.80</summary>

```text
Rolled up from the 5 largest holdings, 46.4% of the fund by weight
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 1.62 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +61.7% above the current prices
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
Share count change: 1 week: +5.1% (3.03B) over 7d | 1 month: +13.4% (7.36B) over 34d
Shares outstanding: 144.32M | fund size: 62.38B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Turkey (TUR) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Neutral overall; no macro surprise, technicals show downtrend but no decisive break, analyst view bullish but limited coverage, flows flat, risk‑off market conditions.

**Main reasons it gave:**
- Price below 20‑day SMA (31.09), 50‑day SMA (33.34), and 200‑day SMA (38.35)
- RSI(14) at 35.5 indicates oversold condition with low volume
- Analyst coverage of top holdings (44.9% weight) is 100% buy with +36% price target
- Fund flows flat (share count unchanged over 1‑month)
- VIX up 10.2 points to 29.46, indicating stressed market risk‑off sentiment

<details><summary><b>News</b> — score +0.00</summary>

_No news found for this one today._

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.14% (+0.02 on the week) | 5-year 4.78% (-0.20 on the week) | 10-year 4.99% (-0.17 on the week) | 30-year 5.37% (-0.11 on the week)
Yield curve, 10-year minus 3-month: +0.84 points -- upward sloping (normal)
US dollar index: 103.69 (+0.28 on the week)
Volatility (VIX): 29.46 (+10.2 on the week) -- stressed
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.1% (2026-10-01) | jobless claims 203k (2026-11-14)
Policy and expectations: Fed target 4.00% | market expects 2.2% inflation over 10 years
Rate path: 2-year Treasury 4.80% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score -0.20</summary>

```text
Last close 30.07 (bar of 2026-11-20), from 502 daily bars
Trend: vs 20d SMA 31.09 (-3.3%), 50d 33.34 (-9.8%), 200d 38.35 (-21.6%); 50d below 200d
Momentum: RSI(14) 35.5 | MACD -0.597 vs signal -0.676 (histogram 0.079)
Returns: 1d -1.6% | 5d -6.6% | 1m -3.3% | 3m -25.7%
52-week range: 29.53 - 43.74 (now 3.8% of the way up)
Volatility: ATR(14) 0.62 (2.1% of price) | annualised 20d 32.5%
Volume: 0.44x the 20-day average
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
Three-year record: -1.9% a year | beta to the market 0.60
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
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 1.60 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +36.0% above the current prices
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
Shares outstanding: 15.65M | fund size: 470.60M
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### US real estate (VNQ) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Analyst coverage of top holdings (40.2% weight) all buy with +16.9% price target; fund flows flat over past week and month, indicating neutral demand; fund fundamentals: P/E 29.6, yield 3.6%, 3‑year return +10.6%/yr, moderate valuation; macro: yields high (10‑yr 4.99%) with slight decline, VIX elevated at 29.5, no surprise data; technicals: price below 20‑day SMA, 50‑day SMA above 20‑day, 50‑day below 200‑day, RSI 47.5, MACD negative

**Main reasons it gave:**
- Analyst coverage of top holdings (40.2% weight) all buy with +16.9% price target
- Fund flows flat over past week and month, indicating neutral demand
- Fund fundamentals: P/E 29.6, yield 3.6%, 3‑year return +10.6%/yr, moderate valuation
- Macro: yields high (10‑yr 4.99%) with slight decline, VIX elevated at 29.5, no surprise data
- Technical: price below 20‑day SMA, 50‑day SMA above 20‑day, 50‑day below 200‑day, RSI 47.5, MACD negative

<details><summary><b>News</b> — score +0.00</summary>

- [Real Estate Income, Diversified: 3 Top REIT ETFs](https://www.barchart.com/story/news/8922147/real-estate-income-diversified-3-top-reit-etfs)  
  <sub>Barchart.com, 21 hours ago</sub>  
  If you want to own real estate the easy way, these REIT ETFs deliver diversification and income for reasonable fees.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.14% (+0.02 on the week) | 5-year 4.78% (-0.20 on the week) | 10-year 4.99% (-0.17 on the week) | 30-year 5.37% (-0.11 on the week)
Yield curve, 10-year minus 3-month: +0.84 points -- upward sloping (normal)
US dollar index: 103.69 (+0.28 on the week)
Volatility (VIX): 29.46 (+10.2 on the week) -- stressed
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.1% (2026-10-01) | jobless claims 203k (2026-11-14)
Policy and expectations: Fed target 4.00% | market expects 2.2% inflation over 10 years
Rate path: 2-year Treasury 4.80% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 94.03 (bar of 2026-11-20), from 502 daily bars
Trend: vs 20d SMA 95.17 (-1.2%), 50d 92.92 (+1.2%), 200d 94.99 (-1.0%); 50d below 200d
Momentum: RSI(14) 47.5 | MACD 0.528 vs signal 0.873 (histogram -0.346)
Returns: 1d +0.6% | 5d -2.5% | 1m +1.5% | 3m -5.1%
52-week range: 87.00 - 100.95 (now 50.4% of the way up)
Volatility: ATR(14) 1.37 (1.5% of price) | annualised 20d 20.1%
Volume: 0.14x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.20</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score +0.20</summary>

```text
Fund type: Real Estate
What it holds: P/E 29.56 | P/B 2.43 | P/S 4.77 | 3y earnings growth n/a
Yield: 3.6%
Three-year record: +10.6% a year | beta to the market 0.92
Cost and size: expense ratio 0.13% | net assets 69.46B
What it is made of: Stocks 99.4%, Cash 0.3%, Other 0.3%
Largest holdings: Vanguard Real Estate II Index 14.6%, Welltower Inc 8.9%, Prologis Inc 6.5%, Equinix Inc 5.4%, American Tower Corp 4.8%
Sector mix: Real estate 99.5%, Communication services 0.4%, Energy 0.1%, Industrials 0.0%
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
Rolled up from the 5 largest holdings, 40.2% of the fund by weight
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 1.56 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +16.9% above the current prices
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
Share count change: 1 week: +0.0% (0.00) over 10d | 1 month: +0.0% (0.00) over 30d
Shares outstanding: 370.18M | fund size: 34.81B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Biotech (XBI) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Neutral overall: no macro surprise, technicals lack decisive break, positive flows but not a catalyst, thin analyst coverage.

**Main reasons it gave:**
- Yield curve unchanged, VIX up 10.2 points indicating market stress but no policy surprise
- Price below 20d and 50d SMA, MACD negative, volume 0.08x average
- Share count up 6.7% in one week, indicating net inflows
- Analyst coverage thin (9.5% weight) despite 75% buy rating

<details><summary><b>News</b> — score +0.00</summary>

- [GS Finance Corp. Launches Auto-Callable Jump Securities Linked to XLE, XLV, and XBI ETFs Maturing in 2032](https://kalkinemedia.com/us/news/announcements/gs-finance-corp-launches-auto-callable-jump-securities-linked-to-xle-xlv-and-xbi-etfs-maturing-in-2032)  
  <sub>Kalkine Media, 17 hours ago</sub>  
  On November 19, 2026, GS Finance Corp. submitted a Free Writing Prospectus detailing terms for Jump Securities featuring an Auto-Callable option tied to the...
- [3 ETFs That Give You Pfizer With Very Different Mixes](https://finance.yahoo.com/healthcare/articles/3-etfs-pfizer-very-different-151806815.html)  
  <sub>Yahoo Finance, 24 hours ago</sub>  
  If you like Pfizer for its pipeline and global reach, owning the stock directly means carrying its company specific issues on your own.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.14% (+0.02 on the week) | 5-year 4.78% (-0.20 on the week) | 10-year 4.99% (-0.17 on the week) | 30-year 5.37% (-0.11 on the week)
Yield curve, 10-year minus 3-month: +0.84 points -- upward sloping (normal)
US dollar index: 103.69 (+0.28 on the week)
Volatility (VIX): 29.46 (+10.2 on the week) -- stressed
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.1% (2026-10-01) | jobless claims 203k (2026-11-14)
Policy and expectations: Fed target 4.00% | market expects 2.2% inflation over 10 years
Rate path: 2-year Treasury 4.80% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score -0.20</summary>

```text
Last close 144.68 (bar of 2026-11-20), from 502 daily bars
Trend: vs 20d SMA 151.92 (-4.8%), 50d 152.80 (-5.3%), 200d 143.47 (+0.8%); 50d above 200d
Momentum: RSI(14) 40.4 | MACD -2.205 vs signal -1.150 (histogram -1.054)
Returns: 1d +0.4% | 5d -3.9% | 1m -4.6% | 3m -11.9%
52-week range: 113.83 - 169.55 (now 55.4% of the way up)
Volatility: ATR(14) 4.70 (3.2% of price) | annualised 20d 39.0%
Volume: 0.08x the 20-day average
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
Three-year record: +26.2% a year | beta to the market 1.01
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

<details><summary><b>What analysts and big funds say</b> — score +0.25</summary>

_Not available today._

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score +0.25</summary>

```text
Rolled up from the 5 largest holdings, 9.5% of the fund by weight  -- thin, so read this as a fact about that slice rather than the fund
Ratings by weight: buy 75.0% | hold 25.0% | sell 0.0% (mean 2.06 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +14.8% above the current prices
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
Share count change: 1 week: +6.7% (685.03M) over 7d | 1 month: +4.7% (489.07M) over 30d
Shares outstanding: 75.18M | fund size: 10.88B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### US materials and chemicals (XLB) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Neutral overall; technicals are bearish but volume is low and there is no decisive macro catalyst. Analyst coverage is bullish (+15% price target) but not enough to outweigh the lack of flow and macro surprise. Fund flows are flat, indicating no net demand.

**Main reasons it gave:**
- Price 49.65 below 20‑day, 50‑day and 200‑day SMAs (‑4.5% to ‑3.1%)
- RSI 37.2 and MACD negative, showing bearish momentum
- Volume 0.18× 20‑day average, indicating weak participation
- Fund flows flat (0% change week‑to‑week), no net demand
- No macro surprise: yields stable, VIX up but no policy shift

<details><summary><b>News</b> — score +0.00</summary>

- [iShares 20+ Year U.S. Treasury Bond Index ETF (CAD-Hedged) (XTLH.TO) Stock Price, News, Quote & History](https://ca.finance.yahoo.com/quote/XTLH.TO/)  
  <sub>Yahoo! Finance Canada, 3 hours ago</sub>  
  Find the latest iShares 20+ Year U.S. Treasury Bond Index ETF (CAD-Hedged) (XTLH.TO) stock quote, history, news and other vital information to help you with...
- [Where Are Investors Parking Money Beyond Tech?](https://www.zacks.com/stock/news/3032977/where-are-investors-parking-money-beyond-tech)  
  <sub>Zacks Investment Research, 1 hour ago</sub>  
  Investors are diversifying away from tech amid AI valuation concerns. Healthcare, short-term bonds and materials are attracting fresh interest.
- [State Street Industrial Select Sector SPDR ETF (XLI) stock price, news, quote and history](https://www.google.com/goto?url=CAESZAHEIkXXE06kiB2x2bN9J1yGJAx8E_7QitNtdnusJ70j9XpGFSCrdmsiGxOBt2Zf8SOHn_Ijdk_VblQRQwTcnVmzXKEUno8YX3lUudze0TYlkANzngLFdQ4Q-n7nb0GpGD9ssXs&gsessionid=dFjKd6RiF4iej1wLFDNmNqnw5livW4gPFG3Cz4P_1FNb2ahNIAePZA)  
  <sub>Yahoo Finance Singapore, 15 hours ago</sub>  
  Find the latest State Street Industrial Select Sector SPDR ETF (XLI) stock quote, history, news and other vital information to help you with your stock...
- [State Street Industrial Select Sector SPDR ETF (XLI) Stock Price, News, Quote & History](https://www.google.com/goto?url=CAESZAHEIkXXWNkfmnHQ0xxnDp-0ple3jArjkg5TJp1Loc-HFo8UfwgUgP3-HuVJLETHZl_51W1Vr6agYGLh_QCHE_GpLs6GFqSrrlMe8gS5G_R1MRlszjmqqi23_2zmZCxOwEqqpbU&gsessionid=dFjKd6RiF4iej1wLFDNmNqnw5livW4gPFG3Cz4P_1FNb2ahNIAePZA)  
  <sub>Yahoo! Finance Canada, 16 hours ago</sub>  
  Find the latest State Street Industrial Select Sector SPDR ETF (XLI) stock quote, history, news and other vital information to help you with your stock...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.14% (+0.02 on the week) | 5-year 4.78% (-0.20 on the week) | 10-year 4.99% (-0.17 on the week) | 30-year 5.37% (-0.11 on the week)
Yield curve, 10-year minus 3-month: +0.84 points -- upward sloping (normal)
US dollar index: 103.69 (+0.28 on the week)
Volatility (VIX): 29.46 (+10.2 on the week) -- stressed
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.1% (2026-10-01) | jobless claims 203k (2026-11-14)
Policy and expectations: Fed target 4.00% | market expects 2.2% inflation over 10 years
Rate path: 2-year Treasury 4.80% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score -0.30</summary>

```text
Last close 49.65 (bar of 2026-11-20), from 502 daily bars
Trend: vs 20d SMA 52.00 (-4.5%), 50d 50.81 (-2.3%), 200d 51.24 (-3.1%); 50d below 200d
Momentum: RSI(14) 37.2 | MACD -0.227 vs signal 0.204 (histogram -0.431)
Returns: 1d +0.5% | 5d -4.9% | 1m -4.0% | 3m -7.3%
52-week range: 42.23 - 53.90 (now 63.5% of the way up)
Volatility: ATR(14) 0.91 (1.8% of price) | annualised 20d 22.6%
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
Three-year record: +10.0% a year | beta to the market 0.76
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
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 1.69 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +15.2% above the current prices
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
Shares outstanding: 71.92M | fund size: 3.57B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### US media and communication (XLC) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> No clear macro catalyst or decisive technical break; market stress (VIX up 10%) and bearish technicals offset bullish analyst coverage and modest inflows.

**Main reasons it gave:**
- VIX rose 10% on the week, indicating stressed market conditions
- Technical indicators show bearish momentum: price below 20d/50d/200d SMAs, RSI 39.7
- Analyst coverage of top holdings is 90.6% buy with a weighted price target +37.3% above current
- Fund flows are modestly positive (+2.3% share count increase in the last week) but overall flat

<details><summary><b>News</b> — score +0.00</summary>

- [What Is Going on With Alphabet Stock on Thursday?](https://www.benzinga.com/markets/tech/26/11/63440383/what-is-going-on-with-alphabet-stock-on-thursday-2)  
  <sub>Benzinga, 22 hours ago</sub>  
  Alphabet stock rose nearly 4% on Thursday as strong demand for Anthropic's $83 IPO boosted big tech. See how GOOGL's Google Cloud ties, equity stake,...
- [XLC Nov 2026 108.500 call (XLC261120C00108500) Stock Price, News, Quote & History](https://ca.finance.yahoo.com/quote/XLC261120C00108500/)  
  <sub>Yahoo! Finance Canada, 23 hours ago</sub>  
  Find the latest XLC Nov 2026 108.500 call (XLC261120C00108500) stock quote, history, news and other vital information to help you with your stock trading...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.14% (+0.02 on the week) | 5-year 4.78% (-0.20 on the week) | 10-year 4.99% (-0.17 on the week) | 30-year 5.37% (-0.11 on the week)
Yield curve, 10-year minus 3-month: +0.84 points -- upward sloping (normal)
US dollar index: 103.69 (+0.28 on the week)
Volatility (VIX): 29.46 (+10.2 on the week) -- stressed
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.1% (2026-10-01) | jobless claims 203k (2026-11-14)
Policy and expectations: Fed target 4.00% | market expects 2.2% inflation over 10 years
Rate path: 2-year Treasury 4.80% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score -0.20</summary>

```text
Last close 102.98 (bar of 2026-11-20), from 502 daily bars
Trend: vs 20d SMA 104.54 (-1.5%), 50d 108.68 (-5.2%), 200d 112.03 (-8.1%); 50d below 200d
Momentum: RSI(14) 39.7 | MACD -0.921 vs signal -0.908 (histogram -0.013)
Returns: 1d +0.2% | 5d -5.3% | 1m -4.1% | 3m -8.3%
52-week range: 99.90 - 120.08 (now 15.3% of the way up)
Volatility: ATR(14) 2.09 (2.0% of price) | annualised 20d 23.9%
Volume: 0.08x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.10</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score +0.10</summary>

```text
Fund type: Communications
What it holds: P/E 15.87 | P/B 3.10 | P/S 2.22 | 3y earnings growth n/a
Yield: 1.4%
Three-year record: +16.0% a year | beta to the market 0.93
Cost and size: expense ratio 0.08% | net assets 21.45B
What it is made of: Stocks 99.8%, Cash 0.2%
Largest holdings: Meta Platforms Inc Class A 22.0%, Alphabet Inc Class A 11.1%, Alphabet Inc Class C 8.9%, The Walt Disney Co 5.6%, Comcast Corp Class A 4.9%
Sector mix: Communication services 100.0%
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
Rolled up from the 5 largest holdings, 52.5% of the fund by weight
Ratings by weight: buy 90.6% | hold 9.4% | sell 0.0% (mean 1.52 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +37.3% above the current prices
Holdings read: META, GOOGL, GOOG, DIS, CMCSA
Recent rating changes among them:
  - META: 2026-10-22 UBS: main, Buy -> Buy
  - GOOGL: 2026-11-02 Wells Fargo: main, Overweight -> Overweight
  - GOOG: 2026-10-29 JP Morgan: main, Overweight -> Overweight
  - DIS: 2026-10-16 Citigroup: main, Buy -> Buy
  - CMCSA: 2026-10-26 Freedom Broker: main, Hold -> Hold
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
Share count change: 1 week: +2.3% (481.73M) over 7d | 1 month: -0.2% (-48.55M) over 30d
Shares outstanding: 203.75M | fund size: 20.98B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### US energy companies (XLE) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Mixed signals: bullish analyst coverage (+16.8% price target) vs bearish inventory builds and falling price outlook, flat fund flows, and ambiguous technicals with low volume. No macro surprise or decisive technical break, so overall neutral.

**Main reasons it gave:**
- Energy inventories show builds across crude, gasoline, diesel, and natural gas (bearish)
- EIA price outlook forecasts falling oil and gas prices over next six months (bearish)
- Analyst coverage of top holdings is 100% buy with +16.8% price target (bullish)
- Fund flows are flat, indicating no net demand shift (neutral)
- Technicals show price below 20‑day and 50‑day SMAs with low volume, no decisive break (neutral)

<details><summary><b>News</b> — score +0.00</summary>

- [ORLEN, Carlyle sign preliminary agreement to explore energy investments (XLE:NYSEARCA)](https://seekingalpha.com/news/4674746-orlen-carlyle-sign-preliminary-agreement-to-explore-energy-investments)  
  <sub>Seeking Alpha, 24 hours ago</sub>  
  ORLEN and Carlyle sign a non-binding MOU to explore energy investments in Poland and beyond, with no projects or capital commitments specified.
- [GS Finance Corp. Launches Auto-Callable Jump Securities Linked to XLE, XLV, and XBI ETFs Maturing in 2032](https://kalkinemedia.com/us/news/announcements/gs-finance-corp-launches-auto-callable-jump-securities-linked-to-xle-xlv-and-xbi-etfs-maturing-in-2032)  
  <sub>Kalkine Media, 17 hours ago</sub>  
  On November 19, 2026, GS Finance Corp. submitted a Free Writing Prospectus detailing terms for Jump Securities featuring an Auto-Callable option tied to the...
- [Stock Market Rally Fails As Dow Tumbles 1,101 Points; Anthropic's IPO Leaves AI Trade Cold](https://www.google.com/goto?url=CAESnwEBxCJF153trGN8h81miNn8_JSIeWYFW43OEf5xh3ok09Mn155LeQcJhyTl2DSDSNGXy3ZTG7yO-BqKQLiLP4cMQd3Ewl7gNkZ2L482RMTvY-h9dGmoRsb4ms82cS_Qi7ok_03H8PsA45exh1AHsOn6HcRg1rqf7AmoAPAzwwAPZ5311SKYFRFNlSpmldunZbVWz9omrUzWxaXdnX3kOR4&gsessionid=H_PwHlqDKB13T0j52xBq_UeJW99jn031dDEoACN5ihsu9pD50Yhwag)  
  <sub>Investor's Business Daily, 16 hours ago</sub>  
  The stock market's rally attempt failed Thursday, leaving the Nasdaq and the Dow sharply lower despite Anthropic's IPO trading debut.
- [13Fs show active managers at most defensive stance ever - Wells Fargo (SPY:NYSEARCA)](https://www.google.com/goto?url=CAES5gEBxCJF1yxmkG_yEliOSShE_gGS9p6gtzKy-56q5q6a_1kpdLjP3zbcs7zpFhJT6IqUhEW56Pb6ziuQXybWy2v3wKVlzjCrKcWKk1FOyP9bX6tTyQbvtN3bu6STShDAyFZCWqdi6ZquyacKWsBPWogQTxBRZmzpF05j2xMptJq6gkUN4OydnTItewzZ_BiMVgfaLXdqEMeWZytGf4eAethzPBkdR3E0Mhdm5JIE22x9a6WhDADfJlHcb5LnjWDy2wi5XEBubkNIKfTJ9xTqzZVaodt0w4sMKm6TzvGhlypeDKHEQFEsGQ&gsessionid=H_PwHlqDKB13T0j52xBq_UeJW99jn031dDEoACN5ihsu9pD50Yhwag)  
  <sub>Seeking Alpha, 12 minutes ago</sub>  
  Active long-only funds show their most defensive positioning on record in Q3 13F filings, overweighting consumer staples and real estate over cyclicals.
- [Stock Market Selloff Hits Every Sector as Consumer Stocks Lead Declines](https://www.google.com/goto?url=CAESogEBxCJF14eJD5wdRrvM8IrpJa0tKILZ-SWyK7xu1cFacIwk-H2VaCKG1qZH4mav-tqjBopch8F2icjhODs1qHSYXFx856ApEd9PxHpkeLnqholXAWq0dXOkucxYGFsVM2MbZm4vJ02uAPEHN3_jsZ9TknYAnMAcps9EdXo_nI0LjQvWmGZZp0EZVVkxyC3q-EzPQdVM5PRxzn7eWA7-I-mJPmY&gsessionid=H_PwHlqDKB13T0j52xBq_UeJW99jn031dDEoACN5ihsu9pD50Yhwag)  
  <sub>TipRanks, 19 hours ago</sub>  
  U.S. stocks sold off on Thursday afternoon, with all 11 major S&P 500 sectors declining as investors pulled back from riskier assets.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.14% (+0.02 on the week) | 5-year 4.78% (-0.20 on the week) | 10-year 4.99% (-0.17 on the week) | 30-year 5.37% (-0.11 on the week)
Yield curve, 10-year minus 3-month: +0.84 points -- upward sloping (normal)
US dollar index: 103.69 (+0.28 on the week)
Volatility (VIX): 29.46 (+10.2 on the week) -- stressed
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.1% (2026-10-01) | jobless claims 203k (2026-11-14)
Policy and expectations: Fed target 4.00% | market expects 2.2% inflation over 10 years
Rate path: 2-year Treasury 4.80% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score -0.20</summary>

```text
Last close 60.82 (bar of 2026-11-20), from 502 daily bars
Trend: vs 20d SMA 64.63 (-5.9%), 50d 64.70 (-6.0%), 200d 59.74 (+1.8%); 50d above 200d
Momentum: RSI(14) 35.5 | MACD -1.129 vs signal -0.676 (histogram -0.453)
Returns: 1d -0.1% | 5d -6.4% | 1m -10.0% | 3m -3.6%
52-week range: 43.81 - 70.02 (now 64.9% of the way up)
Volatility: ATR(14) 1.50 (2.5% of price) | annualised 20d 30.5%
Volume: 0.13x the 20-day average
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
Three-year record: +16.7% a year | beta to the market -0.22
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
Share count change: 1 week: +0.0% (0.00) over 7d | 1 month: +0.0% (0.00) over 30d
Shares outstanding: 186.42M | fund size: 11.34B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### US banks and finance (XLF) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:** no explanation. It wrote only “NEUTRAL”, so the main reasons below are all it gave.

**Main reasons it gave:**
- No macro surprise: Fed policy unchanged and data in line with expectations
- Financial sector index fell 1% in afternoon trading
- Technical indicators show slight bearish bias but no decisive break
- Fund flows flat, indicating neutral demand
- Analyst coverage overwhelmingly bullish but limited to 43% of fund

<details><summary><b>News</b> — score +0.00</summary>

- [State Street Financial Sel Sec SPDR ETF (Derivatives) Exchanges XLF Markets | Buy & Sell & Trade](https://cryptorank.io/price/state-street-financial-sel-sec-spdr-etf-derivatives/exchanges)  
  <sub>CryptoRank, 16 hours ago</sub>  
  Discover 5 Best Exchanges Offering 1 XLF Markets for Buying, Selling, and Trading State Street Financial Sel Sec SPDR ETF (Derivatives).
- [Sector Update: Financial Stocks Lower in Afternoon Trading](https://www.moomoo.com/news/post/1005218340/sector-update-financial-stocks-lower-in-afternoon-trading)  
  <sub>Moomoo, 15 hours ago</sub>  
  Financialstocks retreated in Thursday afternoon trading, with the NYSE Financial Index falling 1% and the State Street Financial Select Sector SPDR ETF...
- [State Street Financial Sel Sec SPDR ETF (Derivatives) XLF/EUR Price](https://www.google.com/goto?url=CAESkAEBxCJF11iexd2ekgnzVjNVQBUbuU5eYQ_gYnyPgFNPbki5ypvphczrMzbmyX5cap4gd-vQc7D359FheLaSbIovUdaqK9XjhO_FPiv4zLa1fiPcyRwN9lHpdwIU7vwySCvqYG7A--ahkuN0sdJmyrNHneyeYh6fqf7gOSghCAJCPG3pFxcH47D7V-qbXAAQTmU&gsessionid=aOphLYu2_IdgDpZ6-mMKGKXWjHHRLFdpOTYN159mFexGJ_sd6mhavw)  
  <sub>CryptoRank, 16 hours ago</sub>  
  Current State Street Financial Sel Sec SPDR ETF (Derivatives) (XLF) token data: Price to Euro (EUR) - € 50.87, Trading Volume 330.21K, Market Cap N/A.
- [State Street Financial Sel Sec SPDR ETF (Derivatives) XLF/JPY Price](https://www.google.com/goto?url=CAESkAEBxCJF11BpXjZ1uYJ0xvEMWMPkFEZuBQLZrKc2MKXiVyzO09f4xyq7V-SXRu0mI3aRXNlzjF02_dOHhyW5hnCT_b-iB2WQmkA6f4HgMboYHw0vC2MvIKyR3tL8OCIcsvLluPg3e3pW2vZY4_J3Wb2jTn6Y2MMHxaFAbyoeFZ30yH6RMBWrn_SxjN_GlXv_Mro&gsessionid=aOphLYu2_IdgDpZ6-mMKGKXWjHHRLFdpOTYN159mFexGJ_sd6mhavw)  
  <sub>CryptoRank, 16 hours ago</sub>  
  Current State Street Financial Sel Sec SPDR ETF (Derivatives) (XLF) token data: Price to Japanese Yen (JPY) - ¥ 8909, Trading Volume 57.83M, Market Cap N/A.
- [State Street Financial Sel Sec SPDR ETF (Derivatives) Analytics](https://www.google.com/goto?url=CAESlgEBxCJF1wHPwmTXlGGj22bV2MqYAxlh8rrg3vB-MDYcyDONFVu0ZbpG0faM4qCKSP8HOM5w0FZvJIDFMshwTy_TgTTkE7yV_807MyWdDe6ZkyHnWkT306Wx5DvMqocXSVF-Ka4NQ1CiOcrjBPMk2oU87niWXivgFoTrzBKmF2hVErz9mwuEr3P-ipMx6ou_V1LzVCzaxAA&gsessionid=aOphLYu2_IdgDpZ6-mMKGKXWjHHRLFdpOTYN159mFexGJ_sd6mhavw)  
  <sub>CryptoRank, 16 hours ago</sub>  
  Comprehensive analysis of State Street Financial Sel Sec SPDR ETF (Derivatives) price dynamics, quarterly returns, and annual trends in dollars.
- [State Street Financial Sel Sec SPDR ETF (Derivatives) XLF/CNY Price](https://www.google.com/goto?url=CAESkAEBxCJF16laRLzH9B80Cf6XEBEsda0bCEEAGNQfaPu0eFJCpTJSQ3xzQcAW_O1Up1VPR7KTIMqXAI_2Q3ktRDcmgC5xTRyOznAeHWJiRu6_jDBGukhEfwDRSoGTDabNRWu8lHHqbvoziFP28JK_wffOdEbaBSDe2W06eJzzys30Jm18GBrrhhwHrh2hY1Hf4pc&gsessionid=aOphLYu2_IdgDpZ6-mMKGKXWjHHRLFdpOTYN159mFexGJ_sd6mhavw)  
  <sub>CryptoRank, 16 hours ago</sub>  
  Current State Street Financial Sel Sec SPDR ETF (Derivatives) (XLF) token data: Price to Chinese Yuan (CNY) - CN¥ 372.12, Trading Volume 2.42M,...
- [How do I convert State Street Financial Sel Sec SPDR ETF (Derivatives) (XLF) to South Korean Won (KRW)?](https://www.google.com/goto?url=CAESkAEBxCJF1w0iQ3v-e0dbYl4PF9_SVWNbZV1TpDlFYTDa0VAdbMgYJw23zBwxcXFQ8-3HXfQrW95SoZDbSnSgYwHEYqdtxJzpUPslcmIhMbK5fx32oBcjthC8Hj6pU_tSqAUzwX4VndJOFaYc5MvvFBi95M3U3yMJIYZ4lf-oMEqQWOJ7vawVHLuNUHTvGKXVvJg&gsessionid=aOphLYu2_IdgDpZ6-mMKGKXWjHHRLFdpOTYN159mFexGJ_sd6mhavw)  
  <sub>CryptoRank, 16 hours ago</sub>  
  Current State Street Financial Sel Sec SPDR ETF (Derivatives) (XLF) token data: Price to South Korean Won (KRW) - ₩ 74474, Trading Volume 483.40M,...
- [State Street Financial Sel Sec SPDR ETF (Derivatives) XLF/RUB Price](https://www.google.com/goto?url=CAESkAEBxCJF17gxts6FQoPo6dWL7lrk0mt3dygfybdIJQ_9-5gqdJsEdN-twj_I7vEZKryeNmQ9JnWlDY6a-iLcBB8063iWB_xH6YClyjfXqkKMXySmy1YfVeWwUGGulJKZ4n62iG-4aAKTcgTvEneRet7y4Ha5MMqLd87BvYZF2paa2LbD5uFxobCxSVzRscGQXm0&gsessionid=aOphLYu2_IdgDpZ6-mMKGKXWjHHRLFdpOTYN159mFexGJ_sd6mhavw)  
  <sub>CryptoRank, 18 hours ago</sub>  
  Current State Street Financial Sel Sec SPDR ETF (Derivatives) (XLF) token data: Price to Russian Ruble (RUB) - ₽ 4575, Trading Volume 29.65M,...
- [How do I convert State Street Financial Sel Sec SPDR ETF (Derivatives) (XLF) to Vietnamese Dong (VND)?](https://www.google.com/goto?url=CAESkAEBxCJF116LOVGCMrjtM_UkLk9GhyoiahRnulPRWXlqo4K1F-1yHncWfbhDsvuoj7d8gJMVfXtIirjAI8U7oJ53vb6t5X3Gy6CPE8g2rRXNTpQYSm1q44pSBwvCBA_0jtP1HdrElqEwQCjDKcb2Xyghw4kRTVvMm7A4pQC7irKd8NNWO275goRUgWphO2T48nY&gsessionid=aOphLYu2_IdgDpZ6-mMKGKXWjHHRLFdpOTYN159mFexGJ_sd6mhavw)  
  <sub>CryptoRank, 16 hours ago</sub>  
  Current State Street Financial Sel Sec SPDR ETF (Derivatives) (XLF) token data: Price to Vietnamese Dong (VND) - ₫ 1437051, Trading Volume 9.33B,...
- [State Street Financial Sel Sec SPDR ETF (Derivatives) Price Today](https://www.google.com/goto?url=CAESjAEBxCJF1xInBun0RJtM1nE6JBXeZgn2OJggW9g6eajXWSWqhJCgTxRbY9oLKe4UIljd5WXjAbeKrQXJfkTLspJBBPDbUdm8szTsZFtUt7FqLlqfEebjQnQmjuI4DXWy6fBjzMgLRs4kx4m41l50dbIFDUKIdID9zGh9SoX0MnfN1T-uvQ3zzdB6NEpm_A&gsessionid=aOphLYu2_IdgDpZ6-mMKGKXWjHHRLFdpOTYN159mFexGJ_sd6mhavw)  
  <sub>CryptoRank, 20 hours ago</sub>  
  Current State Street Financial Sel Sec SPDR ETF (Derivatives) (XLF) token data: Price $ 55.80, Trading Volume $ 362.16K, Market Cap $ 0.00, Circ.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.14% (+0.02 on the week) | 5-year 4.78% (-0.20 on the week) | 10-year 4.99% (-0.17 on the week) | 30-year 5.37% (-0.11 on the week)
Yield curve, 10-year minus 3-month: +0.84 points -- upward sloping (normal)
US dollar index: 103.69 (+0.28 on the week)
Volatility (VIX): 29.46 (+10.2 on the week) -- stressed
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.1% (2026-10-01) | jobless claims 203k (2026-11-14)
Policy and expectations: Fed target 4.00% | market expects 2.2% inflation over 10 years
Rate path: 2-year Treasury 4.80% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 55.86 (bar of 2026-11-20), from 502 daily bars
Trend: vs 20d SMA 57.25 (-2.4%), 50d 55.90 (-0.1%), 200d 54.02 (+3.4%); 50d above 200d
Momentum: RSI(14) 43.9 | MACD 0.178 vs signal 0.491 (histogram -0.313)
Returns: 1d +0.5% | 5d -4.8% | 1m -1.4% | 3m -4.1%
52-week range: 47.81 - 59.20 (now 70.7% of the way up)
Volatility: ATR(14) 0.90 (1.6% of price) | annualised 20d 23.0%
Volume: 0.17x the 20-day average
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
Three-year record: +19.1% a year | beta to the market 0.68
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
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 1.86 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +10.8% above the current prices
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
Shares outstanding: 883.44M | fund size: 49.35B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### US industry (XLI) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Neutral overall: technicals are bearish but with low volume, analyst coverage is thin despite a positive rating, fund flows are flat, fundamentals show high valuation but strong historical performance, and macro conditions show no clear catalyst.

**Main reasons it gave:**
- Technical: price below 20‑day (167.06), 50‑day (168.03) and 200‑day (173.35) SMAs; RSI 37.4, MACD negative
- Fund flows: flat share count change (0.0% week, 0.0% month)
- Analyst coverage thin (24% weight) but all‑buy rating with +32% price target
- Fundamentals: high valuation (P/E 26.85, P/B 6.33) offset by strong 3‑year record (+17.6% per year)
- Macro: VIX up to 29.46 (stressed) and no surprise data releases

<details><summary><b>News</b> — score +0.00</summary>

- [State Street Industrial Select Sector SPDR ETF (XLI) Stock Price, News, Quote & History](https://ca.finance.yahoo.com/quote/XLI/)  
  <sub>Yahoo! Finance Canada, 16 hours ago</sub>  
  State Street Industrial Select Sector SPDR ETF (XLI) · -4.77% · -3.19% · -4.37% · 4.02% · 7.32% · 52.62% · 595.42%. Key Events. Baseline.
- [State Street Industrial Select Sector SPDR ETF (XLI) stock price, news, quote and history](https://sg.finance.yahoo.com/quote/XLI/)  
  <sub>Yahoo Finance Singapore, 15 hours ago</sub>  
  State Street Industrial Select Sector SPDR ETF (XLI) · -4.77% · -3.19% · -4.37% · 4.02% · 7.32% · 52.62% · 595.42%. Key events. Baseline.
- [Select Sector SPDR Trust - State Street Industrial Select Sector SPDR ETF (ARCA:XLI) Stock Price](https://www.google.com/goto?url=CAESYAHEIkXXyXb4k_WttLM5xC1PFmSxZB-kBGdtZEIW-H6zZz4DH_3p8PRMaI0nQ9ZRscIGqsnmt2AIxzqarQk0-HUk-phuhqt22GCAgdgIBYt2kBuxD01y0kQhcjvZuDa_dg&gsessionid=Bi2rfd-xBa_dOGT4-BqfnrcMQ4lVCZH1-XA0idXBmDIip9j0Eq0TWQ)  
  <sub>Simply Wall St, 9 hours ago</sub>  
  Find the latest The Select Sector SPDR Trust - State Street Industrial Select Sector SPDR ETF (ARCA:XLI) stock price, share price history, and explore other...
- [Rising business costs test profit growth, but investment plans hold up (XLI:NYSEARCA)](https://www.google.com/goto?url=CAESqAEBxCJF13p7fzWPO52U-AtfS4IqZqI2bGpnkoz0hNxmuenE8HBg7eJ6m2mYosFGAgXE7X64agxbMw9yGUKK1m5V5S979Ag0LKlr1QWWotz06BI10qd_-90M_v9fmytYU3xhpgm588c1GGnu9czoRcJ4bRqEAecUyOKWjl75XNxrANJBvuErxSBhXEHTUvP4E9mXOdTDbRnwqA06CydG8zWIEl996YqNEqc&gsessionid=Bi2rfd-xBa_dOGT4-BqfnrcMQ4lVCZH1-XA0idXBmDIip9j0Eq0TWQ)  
  <sub>Seeking Alpha, 18 hours ago</sub>  
  Bank of America Institute finds small-business profitability growth flat in October and mid-sized growth negative, while 85% planned to seek financing.
- [Stock Market Rally Fails As Dow Tumbles 1,101 Points; Anthropic's IPO Leaves AI Trade Cold](https://www.google.com/goto?url=CAESowEBxCJF16PqxGsKkKwKGT_V2rjiEEtjG4Dv86YnOH2DbO1bH6Tik3juZsujwSB5mcSZT5HM8KIJwawekzsM6q_iFOYWEuRa2ywEvxX51m5CLZgCYT320Mudyx7XAOqo1I0xYjhKzOIRHtdMFcevNwecYpPjE-rH7Db_qxmHSr1tGqFKpkCmQezZJujDIznFkTwKX9xq93hDdfEZxLqAtIZW2ddP&gsessionid=Bi2rfd-xBa_dOGT4-BqfnrcMQ4lVCZH1-XA0idXBmDIip9j0Eq0TWQ)  
  <sub>Investor's Business Daily, 16 hours ago</sub>  
  The stock market's rally attempt failed Thursday, leaving the Nasdaq and the Dow sharply lower despite Anthropic's IPO trading debut.
- [(XLK) Risk Channels and Responsive Allocation](https://www.google.com/goto?url=CAESuAEBxCJF18ZvQSR6PhkGJ6nh6pTNB0yShOg70BjPZlw5K89n0PC0VeTvkFVU_Hyr4j5FJVJ_q3UgpZ689xuZFeDUlmp_iHQRnFqzeNuRNYrg5eNGiYMJMm_XJt2RaZqewPN4wSC9MnxEF8T8-FZW5c58qcP2g-bLfbyWif7aqDzzBTo65-Wvc8L9-AV7Bt72l49QlDBl0DU3b2TCGPqIzyy3nbsOD8eSYRIN87HQ3Xc0NfrPs0Q2Tqbk&gsessionid=Bi2rfd-xBa_dOGT4-BqfnrcMQ4lVCZH1-XA0idXBmDIip9j0Eq0TWQ)  
  <sub>Stock Traders Daily, 24 hours ago</sub>  
  Key findings for Technology Select Sector Spdr Etf (NYSE: XLK). Weak Near and Mid-Term Sentiment Could Challenge Long-Term Positive Outlook...
- [The Big Four Recession Indicators: Industrial Production](https://www.google.com/goto?url=CAESmQEBxCJF1zBSnjbBc3_gCzQoboe8zfXSmHIZl0GW70HCdscIxmqV-Xoje2a-drzWRcGa3vI0KzbvstBTnUwhlBoqVJDNMj-QXEMjKBA-_WgOjoDMZh40FMuNXGg_3OVPyUcWtXvwS-TeSjXbBxHDRr1AsZDbHqosSvpINAf6XS1aBNVYgQeh6kPlC5qQeG6d8OMAJi8b-nSa-Hw&gsessionid=Bi2rfd-xBa_dOGT4-BqfnrcMQ4lVCZH1-XA0idXBmDIip9j0Eq0TWQ)  
  <sub>Seeking Alpha, 14 hours ago</sub>  
  By Jennifer Nash. Official recession calls are the responsibility of the NBER Business Cycle Dating Committee, which is understandably vague about the...
- [XLK ETF Forecast & Price Target (2026)](https://www.google.com/goto?url=CAESZgHEIkXXKkXk_z-g1L_J1gaPQ_PzE0EuwpyYODrpiqKPc50zOPmpor_DxB16Q4HsuZYD1CYgsS37nyd_L-NfpkCfkjWv9l78r56dltGWjhS5o1XzYkEjttZn08hIGSB3iiJwwdMu0g&gsessionid=Bi2rfd-xBa_dOGT4-BqfnrcMQ4lVCZH1-XA0idXBmDIip9j0Eq0TWQ)  
  <sub>TipRanks, 15 hours ago</sub>  
  Based on Wall Street analyst 12-month price targets for 76 of Technology Select Sector SPDR Fund's holdings in the last 3 months. The average price target is...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.14% (+0.02 on the week) | 5-year 4.78% (-0.20 on the week) | 10-year 4.99% (-0.17 on the week) | 30-year 5.37% (-0.11 on the week)
Yield curve, 10-year minus 3-month: +0.84 points -- upward sloping (normal)
US dollar index: 103.69 (+0.28 on the week)
Volatility (VIX): 29.46 (+10.2 on the week) -- stressed
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.1% (2026-10-01) | jobless claims 203k (2026-11-14)
Policy and expectations: Fed target 4.00% | market expects 2.2% inflation over 10 years
Rate path: 2-year Treasury 4.80% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score -0.20</summary>

```text
Last close 161.41 (bar of 2026-11-20), from 502 daily bars
Trend: vs 20d SMA 167.06 (-3.4%), 50d 168.03 (-3.9%), 200d 173.35 (-6.9%); 50d below 200d
Momentum: RSI(14) 37.4 | MACD -1.448 vs signal -0.830 (histogram -0.618)
Returns: 1d +0.0% | 5d -4.4% | 1m -3.2% | 3m -9.8%
52-week range: 147.83 - 186.51 (now 35.1% of the way up)
Volatility: ATR(14) 3.11 (1.9% of price) | annualised 20d 26.2%
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
Three-year record: +17.6% a year | beta to the market 1.00
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
Weighted price target: +32.0% above the current prices
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
Shares outstanding: 136.63M | fund size: 22.05B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### US everyday goods (XLP) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Neutral overall; no material macro surprise, flat fund flows, mixed technicals, solid fundamentals but no catalyst.

**Main reasons it gave:**
- Flat fund flows: share count unchanged over the past week and month
- Technicals: price near 52‑week high, MACD below signal, low volume
- Macro: yields fell on longer end while VIX rose 10 points, no surprise data
- Analyst view: 100% buy rating with +3.6% price target covering 41.8% of the fund

<details><summary><b>News</b> — score +0.00</summary>

- [Consumer staples companies with the highest EPS surprises (XLP:NYSEARCA)](https://seekingalpha.com/news/4675148-consumer-staples-companies-with-the-highest-eps-surprises?source=generic_rss)  
  <sub>Seeking Alpha, 1 hour ago</sub>  
  As corporate earnings season comes to a close, investors are tracking sector performance metrics to gauge underlying consumer demand and corporate...
- [State Street Industrial Select Sector SPDR ETF (XLI) stock price, news, quote and history](https://sg.finance.yahoo.com/quote/XLI/)  
  <sub>Yahoo Finance Singapore, 15 hours ago</sub>  
  Find the latest State Street Industrial Select Sector SPDR ETF (XLI) stock quote, history, news and other vital information to help you with your stock...
- [Sector Update: Consumer](https://www.google.com/goto?url=CAESfwHEIkXXZ7aWDARg90JGiwZK5Wn3oewT4l4jzOBoW4ZGX4-GEqDC_IDwVCrsLIq1yNUi21XjQARJWMWfTrQEHwbdFx1xcffXQ41Cots49kQTcUna-8Ap8I7sAfUek_oYw964kjssej3JInY8vGAJ_RJymePNqW4CI1xzpeWX5FU&gsessionid=LlaAID_kFkoSz-Ob-yjdpmZOo5o3A1f-sG1udkoJSxrNsay0ZhH5hQ)  
  <sub>Moomoo, 21 hours ago</sub>  
  Consumerstocks declined Thursday afternoon with the State Street Consumer Staples Select Sector SPDR ETF (XLP) and the State Street Consumer Discretionary...
- [Why Owning AbbVie Through ETFs Could Change The Risks You Carry](https://www.google.com/goto?url=CAESqQEBxCJF1yrO3nuFJ7HAsfEydCALtdyRPjpY4XYZHvA3K4MtEG8-58ztK3r632K97nFPzGyF-2S4diNtg1UjB7C0iwriYytjHaCmYF-Qn9U79JN6NFKiaaFHs4Kn7tDBB6fA_zb_SjnHoYoFX9_jVF7mmMTkL0fX6YiYaL5mH5Ig3gCMlIFc98aZAPSYaB-NcnR9-iz_kPWQHFRPLfwKEdJekWN2uQwboXIF&gsessionid=LlaAID_kFkoSz-Ob-yjdpmZOo5o3A1f-sG1udkoJSxrNsay0ZhH5hQ)  
  <sub>Simply Wall St, 21 hours ago</sub>  
  Anyone buying AbbVie stock directly takes on its company-specific risks alone. Simply Wall St notes that AbbVie carries a high level of debt and that its...
- [Healthcare ETFs Shine as Investors Rotate Out of Tech](https://www.google.com/goto?url=CAESqgEBxCJF19mWEXABPAbA1n8Wl4Urpl3ex6YIc5b9EhJ0_XHgO4uVMUzGhuDGd39xSHWSAWMrjNmgn2dlGGmC6VuA0uafb3Ss5JKh1ysJ9005c5ESh-BS0snfQiZJseQj9WGnZ3fU-Lh3zQF5wJzWR9P1TVOu_maE0vT_7ua_T6Yt2YhrbDJXSAJNgvPj9K9LjXU4dgTfVP_LF9X7u00r7hBB_nQTxG2E9D6q3g&gsessionid=LlaAID_kFkoSz-Ob-yjdpmZOo5o3A1f-sG1udkoJSxrNsay0ZhH5hQ)  
  <sub>TradingView, 18 hours ago</sub>  
  The healthcare sector is one of the best-performing sectors this year. Over the past six months, healthcare is up about 24%, while technology is down about...
- [Which Merck ETF Best Balances Its Drug Upside And Risks?](https://www.google.com/goto?url=CAESlgEBxCJF19gUPvgrNb-hDm5z3svBxKxZDa9lj0vj5J9cgKsl4RqVbkdSQF3lly8uwpEYxJ4OcQFalWTIH2v8ZJ_vKK2vlM7sUEh_EIK4NmkkQY3xttdyNz57LKRCIu8_y449D-KS3ET8r9tnJZSRgM6PHx3_Gu-UWy_iZ_Y9OhDAtq_KYa8oteq6XaW98s9mmtaCHmA-_jU&gsessionid=LlaAID_kFkoSz-Ob-yjdpmZOo5o3A1f-sG1udkoJSxrNsay0ZhH5hQ)  
  <sub>Yahoo Finance, 2 hours ago</sub>  
  Owning Merck stock outright means you feel every bump in its specific issues yourself. Simply Wall St flags that Merck's profit margins of 3.6% are far...
- [XLP Mar 2027 96.000 call (XLP270319C00096000) Interactive Stock Chart - Yahoo Finance](https://www.google.com/goto?url=CAESeQHEIkXXv06RfoSKyR7fvKcYNB5LRldVg5i37gPSx7hglmprEjLDbw_0BcVZtsRQP5Erhc3b9hyo7wxeAbnt508KxGXgj2iH_z6PCw2_Ssb48as8QxbpxIkMuAULPoW1J2iI_yG3UzI9RqcJzG_UWfClHrHexPVObls&gsessionid=LlaAID_kFkoSz-Ob-yjdpmZOo5o3A1f-sG1udkoJSxrNsay0ZhH5hQ)  
  <sub>Yahoo! Finance Canada, 20 hours ago</sub>  
  Interactive Chart for XLP Mar 2027 96.000 call (XLP270319C00096000), analyze all the data with a huge range of indicators.
- [Walmart (WMT) and Costco (COST) Stocks Could Benefit from Tech Outages Thanks to Doomsday Preppers](https://www.google.com/goto?url=CAESuQEBxCJF13HfZd2l1rvkh9MdT3w6FkipoGtvd1BqQ7cQK3KlBxF2ncHpDzzHNmqX4xT9nN6Op4QdzXar_jXzzuQAwmFErU-tXo7Y3538X3ODkA44jVJGFIEiTo0_nBmw5Ab_a73KnUNhTe9JWNw-fP01Ca4y2prCRFhVcxWbkiGfoKLH0aL3jNH_4Nw_J-knd0Yd9irRv-a5sVcbgPnRoDqkVaGLI2LZ0Fi32i21MEPh0AXN9vPaxt_h6A&gsessionid=LlaAID_kFkoSz-Ob-yjdpmZOo5o3A1f-sG1udkoJSxrNsay0ZhH5hQ)  
  <sub>TipRanks, 19 hours ago</sub>  
  Walmart and Costco stocks could benefit from doomsday preppers buying goods due to tech outages.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.14% (+0.02 on the week) | 5-year 4.78% (-0.20 on the week) | 10-year 4.99% (-0.17 on the week) | 30-year 5.37% (-0.11 on the week)
Yield curve, 10-year minus 3-month: +0.84 points -- upward sloping (normal)
US dollar index: 103.69 (+0.28 on the week)
Volatility (VIX): 29.46 (+10.2 on the week) -- stressed
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.1% (2026-10-01) | jobless claims 203k (2026-11-14)
Policy and expectations: Fed target 4.00% | market expects 2.2% inflation over 10 years
Rate path: 2-year Treasury 4.80% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 91.22 (bar of 2026-11-20), from 502 daily bars
Trend: vs 20d SMA 90.28 (+1.0%), 50d 86.41 (+5.6%), 200d 85.03 (+7.3%); 50d above 200d
Momentum: RSI(14) 57.3 | MACD 1.322 vs signal 1.552 (histogram -0.231)
Returns: 1d +1.5% | 5d -1.2% | 1m +1.4% | 3m +4.3%
52-week range: 76.62 - 92.60 (now 91.4% of the way up)
Volatility: ATR(14) 1.49 (1.6% of price) | annualised 20d 21.4%
Volume: 0.27x the 20-day average
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
Three-year record: +12.5% a year | beta to the market 0.39
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
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 1.80 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +3.6% above the current prices
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
Shares outstanding: 210.17M | fund size: 19.17B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### US electricity and water (XLU) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Neutral overall: analyst view is bullish, fundamentals are solid, but technicals show bearish momentum and macro stress (high VIX) with flat fund flows providing no directional pressure.

**Main reasons it gave:**
- Analyst coverage: 80% buy, 20% hold, weighted price target +12.5%
- Fund flows flat: 0% net share count change over week and month
- Technical indicators: price below 20‑day SMA, MACD histogram negative, 50‑day SMA below 200‑day SMA
- Fundamentals: P/E 17.9, yield 2.8%, 3‑year return +15.2%/yr
- Macro: VIX up 10.2 points to 29.46, indicating heightened market stress

<details><summary><b>News</b> — score +0.00</summary>

- [XLU vs VPU: Which Utility ETF Gets More From the AI Power Rush?](https://247wallst.com/investing/etf/2026/11/19/xlu-vs-vpu-which-utility-etf-gets-more-from-the-ai-power-rush/)  
  <sub>24/7 Wall St., 23 hours ago</sub>  
  XLU or VPU deliver nearly identical returns, yet they hold very different bets on who profits from data centers' hunger for electricity.
- [AI Power Demand Is Sending Utility ETFs In Different Directions](https://simplywall.st/etfs/us/nasdaq-igf/news/ai-power-demand-is-sending-utility-etfs-in-different-directi)  
  <sub>Simply Wall St, 3 hours ago</sub>  
  Two funds in this story can both say “utilities” on the tin, yet one, XLU, has roughly 65% in electric utilities while IGF has only about 27% there and a...
- [State Street Industrial Select Sector SPDR ETF (XLI) Stock Price, News, Quote & History](https://www.google.com/goto?url=CAESYwHEIkXXu3TGcndFTzWDnYfVg6UvBlCmZDLmJYpV8gsqIwEzt-XAQaMXp63vByrl5Ou4L8XaB-ziq5yelkl8PJs8V94WNDoxftQewEjM2VFMntpilwXaLrjjUjBS2SeUhhmk8w&gsessionid=DA2T2-vRibUNvYGNtgwGyfJtQVFpxC2IiQIKM1HXkdXKede257aueg)  
  <sub>Yahoo! Finance Canada, 16 hours ago</sub>  
  Find the latest State Street Industrial Select Sector SPDR ETF (XLI) stock quote, history, news and other vital information to help you with your stock...
- [Form 4 State Street® Utilities Select Sector SPDR® ETF For: 19 November By Investing.com](https://www.google.com/goto?url=CAESvgEBxCJF12-BAW0Xy5K-oVA3LK7hoYvMxHoGlLnM6tqneyqegK618FdIS1A2f23w8kHgkYUWIqj3p2HCQpXYZkr4hyI57I0JscBuzmSBbyr-Q0lTy6cx0AOEv3lE5Anun0jGQYalxPUd5SY5eB-v4Po-GWgydxfBNFRf-2t94CQOTffqBxRfMCi6Inh_ztLbAnc_e1zaA6dc8FZ8DHERNbG3YLEqOrBX48u8oiJ24P5NCqjSSSWfCIf7klBzTcOl&gsessionid=DA2T2-vRibUNvYGNtgwGyfJtQVFpxC2IiQIKM1HXkdXKede257aueg)  
  <sub>Investing.com India, 18 hours ago</sub>  
  Filed Pursuant to Rule 424(b)(2). Registration No. 333-277211. November 17, 2026. PRICING SUPPLEMENT. (To Prospectus dated February 21, 2024,.
- [(XLU) and the Role of Price-Sensitive Allocations](https://www.google.com/goto?url=CAESuwEBxCJF15UveSgWfm95XvKyGaL0DJxKIB0s2nNCJhvCZIqBprfHI1hhIuDBXSaTKbm7Jy9GHfBNP1AYVsCUdR5pX5fcYMRFrz5HK8IpFWRtYpVJovWFS5mU7eWi9M9Qog2gDCKwuawXJdThpl2kcCI4O8_XPMFPi-EnVWEPjDld1vMjlzApGhLWXIA4fNag9YmEt8yqRMLvEeloRnYFBHEBc9RomR_XBLLpwTN6qJ1CYtC172j9RlmNwbHc&gsessionid=DA2T2-vRibUNvYGNtgwGyfJtQVFpxC2IiQIKM1HXkdXKede257aueg)  
  <sub>Stock Traders Daily, 24 hours ago</sub>  
  Key findings for Utilities Select Sector Spdr Etf (NYSE: XLU). Full Alignment in Neutral Sentiment Favors Wait-and-See Approach; Resistance is being tested.
- [State Street Industrial Select Sector SPDR ETF (XLI) stock price, news, quote and history](https://www.google.com/goto?url=CAESYwHEIkXXuUsVgKxOaCN0dvqkM_Im1tq9wlCi-FokHEz8PAAKXSQEn1EwXO7NW-VdJuVjDdV863ImhUZMkluD9vq6rgApKQBB1ClGCOH2jQb0AjSOXwg8mw17cPJpwvCsVUb-QA&gsessionid=DA2T2-vRibUNvYGNtgwGyfJtQVFpxC2IiQIKM1HXkdXKede257aueg)  
  <sub>Yahoo Finance Australia, 19 hours ago</sub>  
  Find the latest State Street Industrial Select Sector SPDR ETF (XLI) stock quote, history, news and other vital information to help you with your stock...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.14% (+0.02 on the week) | 5-year 4.78% (-0.20 on the week) | 10-year 4.99% (-0.17 on the week) | 30-year 5.37% (-0.11 on the week)
Yield curve, 10-year minus 3-month: +0.84 points -- upward sloping (normal)
US dollar index: 103.69 (+0.28 on the week)
Volatility (VIX): 29.46 (+10.2 on the week) -- stressed
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.1% (2026-10-01) | jobless claims 203k (2026-11-14)
Policy and expectations: Fed target 4.00% | market expects 2.2% inflation over 10 years
Rate path: 2-year Treasury 4.80% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score -0.20</summary>

```text
Last close 43.22 (bar of 2026-11-20), from 502 daily bars
Trend: vs 20d SMA 43.40 (-0.4%), 50d 41.95 (+3.0%), 200d 44.34 (-2.5%); 50d below 200d
Momentum: RSI(14) 52.1 | MACD 0.359 vs signal 0.476 (histogram -0.117)
Returns: 1d +0.5% | 5d -1.9% | 1m +0.8% | 3m -0.0%
52-week range: 39.25 - 47.73 (now 46.8% of the way up)
Volatility: ATR(14) 0.59 (1.4% of price) | annualised 20d 12.8%
Volume: 0.11x the 20-day average
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
Three-year record: +15.2% a year | beta to the market 0.34
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
Share count change: 1 week: +0.0% (0.00) over 7d | 1 month: +0.0% (0.00) over 30d
Shares outstanding: 163.27M | fund size: 7.06B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### US health care (XLV) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Neutral overall; no policy or rate surprise, technical indicators mixed, market stress high, sector rotation noted but not decisive.

**Main reasons it gave:**
- No policy or rate surprise; Fed target unchanged at 4.00% and yields stable
- Technical: price above 50‑day SMA but MACD below signal, low volume
- VIX up 10.2 points to 29.46, indicating heightened market stress
- Healthcare sector outperformance noted (up ~24% YTD) in news, but not a decisive catalyst

<details><summary><b>News</b> — score +0.00</summary>

- [Why Owning AbbVie Through ETFs Could Change The Risks You Carry](https://simplywall.st/etfs/us/nysearca-xlv/news/why-owning-abbvie-through-etfs-could-change-the-risks-you-ca)  
  <sub>Simply Wall St, 21 hours ago</sub>  
  Anyone buying AbbVie stock directly takes on its company-specific risks alone. Simply Wall St notes that AbbVie carries a high level of debt and that its...
- [GS Finance Corp. Launches Auto-Callable Jump Securities Linked to XLE, XLV, and XBI ETFs Maturing in 2032](https://kalkinemedia.com/us/news/announcements/gs-finance-corp-launches-auto-callable-jump-securities-linked-to-xle-xlv-and-xbi-etfs-maturing-in-2032)  
  <sub>Kalkine Media, 17 hours ago</sub>  
  On November 19, 2026, GS Finance Corp. submitted a Free Writing Prospectus detailing terms for Jump Securities featuring an Auto-Callable option tied to the...
- [Which Merck ETF Best Balances Its Drug Upside And Risks?](https://www.google.com/goto?url=CAESlgEBxCJF1-9FONGepCUbxycQJ00X-yHtlBdQmDt_rjThP52_IiYFsqZJ8kFykb21aOquVpW3zthDbImZCPL1qynBhMujIyt-FePdb_q-ccsMhFUCFb3g5nuOCCNHMseMDNHQaqKGVle12mrqMv9j9-5_EkBTaf4904K_ny3Y9Sz2JPUApGmMO7J7zzpolpVIoYWqnR2UJD0&gsessionid=DLxzhyj-95CJXb9LusLvX0GBp1yRsgz-ttkWt-lNb_VzD6TppjnQqw)  
  <sub>Yahoo Finance, 2 hours ago</sub>  
  Owning Merck stock outright means you feel every bump in its specific issues yourself. Simply Wall St flags that Merck's profit margins of 3.6% are far...
- [3 ETFs That Give You Johnson & Johnson In Different Doses](https://www.google.com/goto?url=CAESmgEBxCJF1-vdz5ruUUftfRiLOb2vqOdwyJBFqE0E-dBLQQYJao6FPaW0yaFg0EsAX2PbU-Xa4ldiW_JAjSx4xALdwkM9OHVHIiUgI-3pKEiM_TMRpUpV58KfkuYKsZVpYYPF1lrgejbIxa63z8qfL5gRPBLCIqtElRVPSspOiozu0NNOOdiVYeql2MYCRSyxXxw_99k7YzMWxrFa&gsessionid=DLxzhyj-95CJXb9LusLvX0GBp1yRsgz-ttkWt-lNb_VzD6TppjnQqw)  
  <sub>Yahoo Finance, 3 hours ago</sub>  
  You might like Johnson & Johnson for its mix of medicine and medical devices, but owning a single stock means living with its specific risks.
- [Healthcare ETFs Shine as Investors Rotate Out of Tech](https://www.google.com/goto?url=CAESmwEBxCJF15aoNXiAriccngfh12OQ16SAxBi_bjMGH-kh_N4c0x5oKtnomVlw4DXnEQbflIkLUE3Hg8m5rNlJiYn_YzFRFOOVWPw6hcmb6ehn_tb7yBjaR-UF3vBXplBMOYzf2_dxYFC8W5eZv2v9RopK5ITxdfRcIfXrZ1QMFVNXNZmZMrFUNYDCiBsu_0oBOYCrntacdxwqPYppQQ&gsessionid=DLxzhyj-95CJXb9LusLvX0GBp1yRsgz-ttkWt-lNb_VzD6TppjnQqw)  
  <sub>Zacks Investment Research, 18 hours ago</sub>  
  The healthcare sector is one of the best-performing sectors this year. Over the past six months, healthcare is up about 24%, while technology is down about...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.14% (+0.02 on the week) | 5-year 4.78% (-0.20 on the week) | 10-year 4.99% (-0.17 on the week) | 30-year 5.37% (-0.11 on the week)
Yield curve, 10-year minus 3-month: +0.84 points -- upward sloping (normal)
US dollar index: 103.69 (+0.28 on the week)
Volatility (VIX): 29.46 (+10.2 on the week) -- stressed
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.1% (2026-10-01) | jobless claims 203k (2026-11-14)
Policy and expectations: Fed target 4.00% | market expects 2.2% inflation over 10 years
Rate path: 2-year Treasury 4.80% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 179.85 (bar of 2026-11-20), from 502 daily bars
Trend: vs 20d SMA 184.48 (-2.5%), 50d 176.55 (+1.9%), 200d 160.89 (+11.8%); 50d above 200d
Momentum: RSI(14) 46.1 | MACD 1.510 vs signal 2.954 (histogram -1.444)
Returns: 1d +1.3% | 5d -4.8% | 1m -0.8% | 3m +2.9%
52-week range: 142.84 - 189.66 (now 79.0% of the way up)
Volatility: ATR(14) 3.43 (1.9% of price) | annualised 20d 22.8%
Volume: 0.17x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.20</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score +0.20</summary>

```text
Fund type: Health
What it holds: P/E 30.14 | P/B 4.82 | P/S 1.66 | 3y earnings growth n/a
Yield: 1.4%
Three-year record: +14.1% a year | beta to the market 0.41
Cost and size: expense ratio 0.08% | net assets 49.10B
What it is made of: Stocks 99.8%, Cash 0.2%
Largest holdings: Eli Lilly and Co 16.9%, Johnson & Johnson 9.8%, AbbVie Inc 7.8%, Merck & Co Inc 5.5%, UnitedHealth Group Inc 5.4%
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

<details><summary><b>What analysts and big funds say</b> — score +0.45</summary>

_Not available today._

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score +0.45</summary>

```text
Rolled up from the 5 largest holdings, 45.4% of the fund by weight
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 1.74 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +12.3% above the current prices
Holdings read: LLY, JNJ, ABBV, MRK, UNH
Recent rating changes among them:
  - LLY: 2026-11-09 Jefferies: main, Buy -> Buy
  - JNJ: 2026-10-16 Wells Fargo: main, Overweight -> Overweight
  - ABBV: 2026-11-02 UBS: main, Neutral -> Neutral
  - MRK: 2026-11-02 Freedom Broker: main, Hold -> Hold
  - UNH: 2026-10-27 Wells Fargo: main, Overweight -> Overweight
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
Share count change: 1 week: +2.0% (916.78M) over 7d | 1 month: +3.7% (1.68B) over 34d
Shares outstanding: 265.09M | fund size: 47.68B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### US shopping and leisure (XLY) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Neutral overall: macro stress (VIX up, inflation above target) and mixed technicals offset bullish analyst coverage and modest net inflows.

**Main reasons it gave:**
- VIX rose 10.2 points to 29.46, indicating heightened market volatility
- Fund share count increased 3.4% over the past week, showing net inflows
- Analyst coverage of top holdings is 100% buy with a +17.9% price target
- Technical indicators mixed: price below 20‑day SMA, MACD histogram negative, RSI 47.6

<details><summary><b>News</b> — score +0.00</summary>

- [Q3 earnings season winds down: 10 consumer discretionary stocks that beat estimates (XLY:NYSEARCA)](https://seekingalpha.com/news/4675068-q3-earnings-season-winds-down-10-consumer-discretionary-stocks-that-beat-estimates)  
  <sub>Seeking Alpha, 4 hours ago</sub>  
  Hilton Grand Vacations leads Seeking Alpha's 10 consumer discretionary Q3 EPS surprise screen at $2.92, ahead of RH at $2.24.
- [Stock Market Rally Fails As Dow Tumbles 1,101 Points; Anthropic's IPO Leaves AI Trade Cold](https://investors.com/market-trend/the-big-picture/dow-jones-sp500-nasdaq-anthropic-ant-stock-ipo/)  
  <sub>Investor's Business Daily, 16 hours ago</sub>  
  The stock market's rally attempt failed Thursday, leaving the Nasdaq and the Dow sharply lower despite Anthropic's IPO trading debut.
- [Stock Market Selloff Hits Every Sector as Consumer Stocks Lead Declines](https://www.google.com/goto?url=CAESoQEBxCJF1xPZGyKYGKah12c_2hHB6r65dxQaKE0sFg-uitun0WODErcX0QlH-RLhjmrCDA9_9XPpIx6f8yyayB82eZlfdo3aSXIdLHpe7sGNGIHrNjJ_0bCJXwZzOcd2rE8hrBU_MWgz_ghVAcHNFT4SMvGKh8VmNDZ1AlQDuhvfV-sajnZkY_qltjwLuXkwM7x9NxqwAH0t3QjeJW7pjuesBQ&gsessionid=Qh1-Bb7I1q03EcBCR9XrW5MqySN_L_lrqJLyhyK01LAFuXilBJotAw)  
  <sub>TipRanks, 19 hours ago</sub>  
  U.S. stocks sold off on Thursday afternoon, with all 11 major S&P 500 sectors declining as investors pulled back from riskier assets.
- [Home Depot (HD) Sees $76.7 Million in Net ETF Buying on Nov. 18](https://www.google.com/goto?url=CAESiAIBxCJF1xgYXKnLWrjWmUSGjlOVsFOJd7WiGG9sMm2cSQUIZb7k6egLY-JFQXQQZbYTFZQoEcodTkXEmdF3N0CxSIZ257fEbh3Eaj0EQUHSGHehgzMPaks05xfeM2ZgFBqiRYh44m7PTT5Tm9AVkU34AW1Lg11UlNeS_txiP22O_iqzBph9NO_jZfSzLK_4apIc2uOJNleL13LSfDxjEe1_wut3TV7G0FEGwDFR8Sg0lw4PzXUPb6c1W617Ng3jHv3l2LmsBIExMBZtqI8dxQreSmcW8oLelRyvrTqz65l7bgtLwBtxovCDcLiXSsy1oYDXmB4CBSgofD6t52QLV34ScuSW0C9lrz4&gsessionid=Qh1-Bb7I1q03EcBCR9XrW5MqySN_L_lrqJLyhyK01LAFuXilBJotAw)  
  <sub>GuruFocus, 3 hours ago</sub>  
  Thirty-one ETFs were buying Home Depot (HD) shares on Wednesday versus 19 selling, for net ETF buying of $76.7 million. ETF activity has run in the same...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.14% (+0.02 on the week) | 5-year 4.78% (-0.20 on the week) | 10-year 4.99% (-0.17 on the week) | 30-year 5.37% (-0.11 on the week)
Yield curve, 10-year minus 3-month: +0.84 points -- upward sloping (normal)
US dollar index: 103.69 (+0.28 on the week)
Volatility (VIX): 29.46 (+10.2 on the week) -- stressed
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.1% (2026-10-01) | jobless claims 203k (2026-11-14)
Policy and expectations: Fed target 4.00% | market expects 2.2% inflation over 10 years
Rate path: 2-year Treasury 4.80% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 116.10 (bar of 2026-11-20), from 502 daily bars
Trend: vs 20d SMA 117.98 (-1.6%), 50d 114.23 (+1.6%), 200d 115.36 (+0.6%); 50d below 200d
Momentum: RSI(14) 47.6 | MACD 0.865 vs signal 1.403 (histogram -0.538)
Returns: 1d +0.2% | 5d -3.2% | 1m +0.9% | 3m -1.9%
52-week range: 105.66 - 124.52 (now 55.4% of the way up)
Volatility: ATR(14) 2.32 (2.0% of price) | annualised 20d 29.3%
Volume: 0.20x the 20-day average
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
Three-year record: +13.5% a year | beta to the market 1.10
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
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 1.81 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +17.9% above the current prices
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
Share count change: 1 week: +3.4% (720.90M) over 7d | 1 month: +1.0% (216.44M) over 34d
Shares outstanding: 191.22M | fund size: 22.20B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Netherlands (EWN) · Sector or country — no answer, no confidence given

**This one did not finish:** https://api.deepinfra.com/v1/openai/chat/completions unreachable: the streamed answer ran past the 480s ceiling (gave up after 2 attempt(s))

<details><summary><b>News</b> — score n/a</summary>

_No news found for this one today._

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score n/a</summary>

```text
US Treasury yields: 3-month 4.14% (+0.02 on the week) | 5-year 4.78% (-0.20 on the week) | 10-year 4.99% (-0.17 on the week) | 30-year 5.37% (-0.11 on the week)
Yield curve, 10-year minus 3-month: +0.84 points -- upward sloping (normal)
US dollar index: 103.69 (+0.28 on the week)
Volatility (VIX): 29.46 (+10.2 on the week) -- stressed
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.1% (2026-10-01) | jobless claims 203k (2026-11-14)
Policy and expectations: Fed target 4.00% | market expects 2.2% inflation over 10 years
Rate path: 2-year Treasury 4.80% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score n/a</summary>

```text
Last close 59.92 (bar of 2026-11-20), from 502 daily bars
Trend: vs 20d SMA 64.02 (-6.4%), 50d 65.54 (-8.6%), 200d 65.16 (-8.0%); 50d above 200d
Momentum: RSI(14) 30.0 | MACD -1.144 vs signal -0.727 (histogram -0.417)
Returns: 1d -1.4% | 5d -7.5% | 1m -6.6% | 3m -13.4%
52-week range: 55.33 - 71.61 (now 28.2% of the way up)
Volatility: ATR(14) 1.12 (1.9% of price) | annualised 20d 27.2%
Volume: 0.01x the 20-day average
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
Three-year record: +17.3% a year | beta to the market 1.13
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
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 1.57 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +72.5% above the current prices
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
Share count change: 1 week: +0.0% (0.00) over 7d | 1 month: +0.0% (0.00) over 30d
Shares outstanding: 5.55M | fund size: 332.56M
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### South Korea (EWY) · Sector or country — no answer, no confidence given

<details><summary><b>News</b> — score n/a</summary>

- [AI Selloff Spreads From Wall Street To Asia Despite Anthropic Debut: SPY, QQQ, DIA, Asian Stocks Head For Steep Weekly Losses](https://www.tradingview.com/news/stocktwits:747710fe0094b:0-ai-selloff-spreads-from-wall-street-to-asia-despite-anthropic-debut-spy-qqq-dia-asian-stocks-head-for-steep-weekly-losses/)  
  <sub>TradingView, 10 hours ago</sub>  
  Global stock markets are headed for a steep red close this week despite Claude-maker Anthropic's (ANT) record debut on the Nasdaq.
- [South Korea's Stock Market Sinks 4.6% as KOSPI Heavyweights SK Hynix and Samsung Fall 6% After Wall Street's AI Selloff](https://247wallst.com/investing/2026/11/19/south-koreas-stock-market-sinks-4-6-as-kospi-heavyweights-sk-hynix-and-samsung-fall-6-after-wall-streets-ai-selloff/?tpid=1709558&tv=link&tc=in_content)  
  <sub>24/7 Wall St., 12 hours ago</sub>  
  South Korea's KOSPI was down 4.6% at 4,900.95 at 11:37 a.m. Seoul time on Friday. Samsung Electronics fell 6.1% and SK Hynix 5.8%, and the index dipped...
- [EWY Dec 2026 198.000 call (EWY261204C00198000) Interactive Stock Chart - Yahoo Finance](https://www.google.com/goto?url=CAESeQHEIkXX3YeYqPoMzdSL8Pp4EyEIMfJZaVjHv6OgR-x8JLIdNG1Pf_pJYofJzINyMdJ3jz_b1HsTtsDzf3lsF1_jU0-zEqMvTBwIZtpzv96gJCmWlLRX3hkjU7aWFpiz3-EMsjnbFSOjT8p8aZ2XX7FA_LAaH-LgORA&gsessionid=OgviGAJ06XB78lCyQuHuhIHdCrKJR2AFDvnAMUzElFOwtiQdzKS2xQ)  
  <sub>Yahoo! Finance Canada, 20 hours ago</sub>  
  Interactive Chart for EWY Dec 2026 198.000 call (EWY261204C00198000), analyze all the data with a huge range of indicators.
- [South Korea's Stock Market and the Nikkei 225 Sink More Than 4% as the AI Selloff Spreads From Wall Street. Here's How Much of a Target-Date Fund Is in Samsung, SK Hynix and TSMC](https://www.google.com/goto?url=CAESlwIBxCJF11a0LlxvHaoKk2WipwhoWaCdRceBn2B2TeGRJCtaQN--_KrzTW1D_-o-HSMxebGIyWmSkTR1ZTwn8rtmMF9j2ltlSqPemqOJMRkOXzFuc91TgoP0sWzrzqiWkIORt184u2eGCXwANLIhBL-uoc2zX3yjJiMv-STbm4DnQVRp1VzpZiZ_SaRsOx6IHNsbWyxov1ZPv4ESDiJer7GtKRPm6KDtz6PPb4e60EisYFPFUEJzRz8vJRmmeaFA3iS4u7vultSXH8I-9IWepbK9UvvbmTnfW3iLa6X_xd71od9t43DUwcxRkZ6sJ6zIWnF_XC2xPN6olR8idWkNV68kED6OKsTOZWIHD9AR50BcJBMcuh5LtpQ&gsessionid=OgviGAJ06XB78lCyQuHuhIHdCrKJR2AFDvnAMUzElFOwtiQdzKS2xQ)  
  <sub>24/7 Wall St., 11 hours ago</sub>  
  The KOSPI was down 5.04% at 4,879.10 early Friday afternoon in Seoul, setting off a sell-side sidecar, and the Nikkei 225 was down 4.52%.
- [SPY, QQQ, DIA, Asian Stocks Plunge As Anthropic’s Record IPO Fails To Stop AI Rout](https://www.google.com/goto?url=CAEStAEBxCJF10glgkOYlBFV9ueMNc7LZxSMitA422FAXxfmyr8TTQQRLvAjyCYC1ed4FW9G6FUhSg8MTdIKMD101h6cFoajLQn9rnTEGqY6WPyVwNhYokx61tP5YNoWMbkjU4YtZR83Foqia7-FeieId8VcEYoQwyXjCvj6aDa4TmspUfpdAjhfbBEo8Ije8m25LYo7SrPxonLEr-poJbG6YQVL0Ee5BFFy1qHoC_IXyXjNTT5kRRI&gsessionid=OgviGAJ06XB78lCyQuHuhIHdCrKJR2AFDvnAMUzElFOwtiQdzKS2xQ)  
  <sub>Stocktwits, 10 hours ago</sub>  
  While Anthropic's stock surged more than 17% on its debut on Thursday, other AI stocks across the U.S. and Asian markets fell sharply.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score n/a</summary>

```text
US Treasury yields: 3-month 4.14% (+0.02 on the week) | 5-year 4.78% (-0.20 on the week) | 10-year 4.99% (-0.17 on the week) | 30-year 5.37% (-0.11 on the week)
Yield curve, 10-year minus 3-month: +0.84 points -- upward sloping (normal)
US dollar index: 103.69 (+0.28 on the week)
Volatility (VIX): 29.46 (+10.2 on the week) -- stressed
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.1% (2026-10-01) | jobless claims 203k (2026-11-14)
Policy and expectations: Fed target 4.00% | market expects 2.2% inflation over 10 years
Rate path: 2-year Treasury 4.80% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score n/a</summary>

```text
Last close 131.53 (bar of 2026-11-20), from 502 daily bars
Trend: vs 20d SMA 145.51 (-9.6%), 50d 163.14 (-19.4%), 200d 164.35 (-20.0%); 50d below 200d
Momentum: RSI(14) 35.3 | MACD -7.974 vs signal -7.680 (histogram -0.294)
Returns: 1d -2.3% | 5d -7.9% | 1m -11.8% | 3m -24.3%
52-week range: 88.53 - 219.20 (now 32.9% of the way up)
Volatility: ATR(14) 6.70 (5.1% of price) | annualised 20d 69.7%
Volume: 0.22x the 20-day average
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
Three-year record: +33.2% a year | beta to the market 2.62
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
Share count change: 1 week: +0.0% (0.00) over 10d | 1 month: +0.0% (0.00) over 30d
Shares outstanding: 75.60M | fund size: 9.94B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Brazil (EWZ) · Sector or country — no answer, no confidence given

<details><summary><b>News</b> — score n/a</summary>

_No news found for this one today._

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score n/a</summary>

```text
US Treasury yields: 3-month 4.14% (+0.02 on the week) | 5-year 4.78% (-0.20 on the week) | 10-year 4.99% (-0.17 on the week) | 30-year 5.37% (-0.11 on the week)
Yield curve, 10-year minus 3-month: +0.84 points -- upward sloping (normal)
US dollar index: 103.69 (+0.28 on the week)
Volatility (VIX): 29.46 (+10.2 on the week) -- stressed
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.1% (2026-10-01) | jobless claims 203k (2026-11-14)
Policy and expectations: Fed target 4.00% | market expects 2.2% inflation over 10 years
Rate path: 2-year Treasury 4.80% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score n/a</summary>

```text
Last close 29.50 (bar of 2026-11-20), from 502 daily bars
Trend: vs 20d SMA 31.99 (-7.8%), 50d 36.79 (-19.8%), 200d 36.84 (-19.9%); 50d below 200d
Momentum: RSI(14) 26.2 | MACD -2.116 vs signal -1.987 (histogram -0.128)
Returns: 1d -0.1% | 5d -8.5% | 1m -29.5% | 3m -16.1%
52-week range: 29.50 - 43.54 (now 0.0% of the way up)
Volatility: ATR(14) 0.98 (3.3% of price) | annualised 20d 72.4%
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
Three-year record: +2.3% a year | beta to the market 0.92
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
Weighted price target: +43.0% above the current prices
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
Shares outstanding: 200.55M | fund size: 5.92B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### US house builders (XHB) · Sector or country — no answer, no confidence given

<details><summary><b>News</b> — score n/a</summary>

- [How to Invest in iShares U.S. Home Construction ETF (ITB)](https://www.fool.com/investing/how-to-invest/etfs/how-to-invest-in-itb-etf/)  
  <sub>The Motley Fool, 21 hours ago</sub>  
  The iShares U.S. Home Construction ETF (ITB) can help investors capitalize on long-term demand for housing.
- [Form 4 State Street® SPDR® S&P® Homebuilders ETF For: 20 November](https://ng.investing.com/news/stock-market-news/form-4-state-street-spdr-sp-homebuilders-etf-for-20-november-93CH-2820089)  
  <sub>Investing.com Nigeria, 9 hours ago</sub>  
  Are you sure your AI has the whole picture? It sounds confident, but what if it's missing an important angle? InvestingPro is purpose-built AI for investors...
- [Mortgage rates jump, weighing on application activity (XLRE:NYSEARCA)](https://www.google.com/goto?url=CAESlwEBxCJF13yHWS2vXP3b9D46jjOjFgt2x5_vY59B3sfFJip5b6Cj1vXjU7x-hr_vqQaHW-PMj4XntHVaZEsFGVhZmTM3ZDFZW4cZ0blEFAadOD-sOkcWYqfnQZqCSeDxZlo0q75vnxXJ70r3_bp4SJJ8_K4o6xtV3IM3EV0QoHJ3ogho7JqYzKctHBSuDdiSMiSFFzxSKosf&gsessionid=1IlM2Vuvq-56p4hyqCAk6IY2L_8kOhQu17QEZ9Db8YPta9IAmtJRcQ)  
  <sub>Seeking Alpha, 22 hours ago</sub>  
  Mortgage rates jumped in the previous week, weighing on application activity. The direction of rates in the coming weeks is expected to shape the housing...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score n/a</summary>

```text
US Treasury yields: 3-month 4.14% (+0.02 on the week) | 5-year 4.78% (-0.20 on the week) | 10-year 4.99% (-0.17 on the week) | 30-year 5.37% (-0.11 on the week)
Yield curve, 10-year minus 3-month: +0.84 points -- upward sloping (normal)
US dollar index: 103.69 (+0.28 on the week)
Volatility (VIX): 29.46 (+10.2 on the week) -- stressed
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.1% (2026-10-01) | jobless claims 203k (2026-11-14)
Policy and expectations: Fed target 4.00% | market expects 2.2% inflation over 10 years
Rate path: 2-year Treasury 4.80% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score n/a</summary>

```text
Last close 99.22 (bar of 2026-11-20), from 502 daily bars
Trend: vs 20d SMA 101.56 (-2.3%), 50d 98.49 (+0.7%), 200d 104.39 (-4.9%); 50d below 200d
Momentum: RSI(14) 47.6 | MACD 0.267 vs signal 0.883 (histogram -0.616)
Returns: 1d +1.4% | 5d -2.8% | 1m +0.0% | 3m -6.7%
52-week range: 92.84 - 121.36 (now 22.4% of the way up)
Volatility: ATR(14) 2.82 (2.8% of price) | annualised 20d 39.5%
Volume: 0.08x the 20-day average
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
Three-year record: +7.8% a year | beta to the market 1.40
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
Weighted price target: +12.5% above the current prices
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
Share count change: 1 week: +2.3% (36.48M) over 7d | 1 month: +6.6% (98.77M) over 30d
Shares outstanding: 16.19M | fund size: 1.61B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### US technology (XLK) · Sector or country — no answer, no confidence given

**This one did not finish:** https://api.deepinfra.com/v1/openai/chat/completions unreachable: the streamed answer ran past the 480s ceiling (gave up after 2 attempt(s))

<details><summary><b>News</b> — score n/a</summary>

- [The Technology Select Sector SPDR® Fund (XLK) Stock Price | Quotes & News](https://www.moomoo.com/stock/XLK-US?chain_id=Name1K9-3FXPhg.1lfvkug&global_content=%7B%22promote_id%22%3A%22%22%2C%22sub_promote_id%22%3A64%2C%22subpromote_id%22%3A%22%22%2C%22f%22%3A%22www.moomoo.com%2Fcommunity%2Fprofile%2Fmoomoo-recap-us-77777011%22%7D)  
  <sub>Moomoo, 9 hours ago</sub>  
  Track the latest The Technology Select Sector SPDR® Fund (XLK) price, quotes, financial information, news, and analyst ratings on moomoo App for your ETF...
- [WCLD: Equal-Weight ETF In Cloud Computing (NASDAQ:WCLD)](https://seekingalpha.com/article/4968000-wcld-equal-weight-etf-in-cloud-computing)  
  <sub>Seeking Alpha, 12 hours ago</sub>  
  Analyst sees WCLD as a tactical trade, not a long-term holding; it is cheaper than XLK with higher growth, yet underperforms amid AI headwinds.
- [(XLK) Risk Channels and Responsive Allocation](https://www.google.com/goto?url=CAESuAEBxCJF1wF32DGpELsy8XzLCBQYPIvl2rTqlszrxPCl7MvPy53lx_3wioK-SUb8WI1sJN_uq_axGDLxxZ7QZRgvyDt5U2LCbCX9SMHLLeBdKzqbYTQLm8b-wAUcscydKtsCX5HOPPayVVzp_O2iQ5QhdDdK-EqB2zxxR1Uew7GoLx6RTrepdRq9TcUWBRcODO0g95P1F1E5fwPZCcsbvuLEPd-Pdz_UWaRXv5wlSFZm20Dfg_JL2oT2&gsessionid=Lc77pytO_kCqYa2qItsBvpxm-uab9UWOWYhJOKk1o725mmtSCeXCog)  
  <sub>Stock Traders Daily, 24 hours ago</sub>  
  Key findings for Technology Select Sector Spdr Etf (NYSE: XLK). Weak Near and Mid-Term Sentiment Could Challenge Long-Term Positive Outlook...
- [Most of 2026’s 15 biggest tech IPOs now trade below day 1 close - DataTrek (XLK:NYSEARCA)](https://www.google.com/goto?url=CAESqwEBxCJF13KF1fF1xB0vniRGUGdp0WAJZxbceEQGbvYarz4_lwP7Jd0mkl7vdLXZamjK4i_4ULxSd0XgLQcIBRlMe85zChIptREdYY-uKPrr1yVgMGotoODKzRs90YNoOYJ-xkwVQ5BNlCJtAln3wwKeHB1nhUcr3ljUkl0411QSbrwn9VGr2nTtFYao9-n8nKOzIGd4IunND1RKmsnw3pm2KhIWMGzgujpdwCs&gsessionid=Lc77pytO_kCqYa2qItsBvpxm-uab9UWOWYhJOKk1o725mmtSCeXCog)  
  <sub>Seeking Alpha, 20 hours ago</sub>  
  Most of 2026's largest technology and AI-related initial public offerings have surrendered their strong opening gains, leaving investors who bought into the...
- [3 Funds Riding Anthropic IPO Optimism Through Very Different Chip Bets](https://www.google.com/goto?url=CAESlgEBxCJF191NYbiLA5ArG5JtlOVb44czlAawrm36F8NseItx8bm3aOEsUs1cF3Gm_CXndp_4-A5CvqfkiqmVYBSyQ4WVlnPCPyAkZ5BNsyyf0cmBy6sOF-XgIXo-dKvffMCwJhdWFcfodo9qmX02Yv1ODb3pAzd8JMa-_g1vhWBPBW1JoWs-d4zUyJeuzbrmwnY9kmEgVfE&gsessionid=Lc77pytO_kCqYa2qItsBvpxm-uab9UWOWYhJOKk1o725mmtSCeXCog)  
  <sub>Yahoo Finance, 3 hours ago</sub>  
  Two funds here are almost entirely in semiconductors, while one, XLK, has less than half of its portfolio in chip makers despite sharing the same AI story...
- [XLK ETF Forecast & Price Target (2026)](https://www.google.com/goto?url=CAESZgHEIkXX7zQo4KCNb3zLCFIKpuMa6vKrXgBM2on8ojETDL4l6Jzfw6ucvLfVVoG6NQNkk_-LJOOzZ3joD8lZS8tRMc2txVtj91htkuuR6Nqv6Y_3xTFKqIqR38lcw5dU0PHQQg7Gyw&gsessionid=Lc77pytO_kCqYa2qItsBvpxm-uab9UWOWYhJOKk1o725mmtSCeXCog)  
  <sub>TipRanks, 15 hours ago</sub>  
  Based on Wall Street analyst 12-month price targets for 76 of Technology Select Sector SPDR Fund's holdings in the last 3 months. The average price target is...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score n/a</summary>

```text
US Treasury yields: 3-month 4.14% (+0.02 on the week) | 5-year 4.78% (-0.20 on the week) | 10-year 4.99% (-0.17 on the week) | 30-year 5.37% (-0.11 on the week)
Yield curve, 10-year minus 3-month: +0.84 points -- upward sloping (normal)
US dollar index: 103.69 (+0.28 on the week)
Volatility (VIX): 29.46 (+10.2 on the week) -- stressed
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.1% (2026-10-01) | jobless claims 203k (2026-11-14)
Policy and expectations: Fed target 4.00% | market expects 2.2% inflation over 10 years
Rate path: 2-year Treasury 4.80% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score n/a</summary>

```text
Last close 157.57 (bar of 2026-11-20), from 502 daily bars
Trend: vs 20d SMA 172.89 (-8.9%), 50d 184.59 (-14.6%), 200d 171.34 (-8.0%); 50d above 200d
Momentum: RSI(14) 30.2 | MACD -6.885 vs signal -5.887 (histogram -0.999)
Returns: 1d -1.9% | 5d -7.5% | 1m -13.6% | 3m -12.5%
52-week range: 127.50 - 202.00 (now 40.4% of the way up)
Volatility: ATR(14) 5.62 (3.6% of price) | annualised 20d 44.1%
Volume: 0.20x the 20-day average
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
Three-year record: +22.2% a year | beta to the market 1.56
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
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 1.73 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +36.7% above the current prices
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
Share count change: 1 week: +3.5% (3.85B) over 7d | 1 month: +12.1% (12.32B) over 34d
Shares outstanding: 726.91M | fund size: 114.54B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

## Commodities

### Gold (GLD) · Commodity — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:** no explanation. It wrote only “NEUTRAL”, so the main reasons below are all it gave.

**Main reasons it gave:**
- No Fed policy surprise; rate hike expectations unchanged
- Technical indicators show bearish momentum (RSI 25.2, MACD negative) but low volume
- Positioning shows modest net long increase (+1.8% week) but overall net long 27.8% is moderate
- Cost of holding near zero (-0.1% annual), indicating no structural bias

<details><summary><b>News</b> — score +0.00</summary>

- [Banks, Airlines, Tech: Prep Portfolios for Outage Volatility in ETFs](https://etfdb.com/equity-etf-content-hub/banks-airlines-tech-prep-portfolios-outage-volatility-etfs/)  
  <sub>ETF Database, 34 minutes ago</sub>  
  Worried by recent system and infrastructure outages? Outage volatility may hold signals for investors to consider via ETFs.
- [GLD Technical Levels: Support $335, Resistance $363](https://www.moomoo.com/community/feed/gld-technical-levels-support-335-resistance-363-117647938945029?chain_id=Name1K9-3FXPhg.1lg0a1g&global_content=%7B%22promote_id%22%3A13764%2C%22sub_promote_id%22%3A107%2C%22f%22%3A%22www.moomoo.com%2Fetfs%2FGLD-US%2Fcommunity%22%7D)  
  <sub>Moomoo, 6 hours ago</sub>  
  SPDR Gold ETF (GLD.US)$ options tape: calls $47.9M, puts $682.3M (total $730.3M) (93% puts). Largest bet: $49.8M on 17074 put contracts expiring Nov...
- [Gold slide deepens as market anxiety overtakes real-rate pressures (GLD:NYSEARCA)](https://www.google.com/goto?url=CAES5wEBxCJF1xAnM1YC7adph7ohwEzVFKwU26p9BTpKEfe4WwXeHj_m6Ucfv6aS3Yp99uZiSlQQ9GG82P1aq9uvYgo-D5oAVoEQA6O233ULFVk1-a5VfCswF6EusWM39g9eDaWDaGgoKzvN5Iwgm6o9F36Yq1rqC8Vlc0QhPtg-aJfdGoQGm4IWfH90C8lULA77yP696W7CGR0xGNdaPXEFY75ZtuipUdNnirC5_51RbbEUxvGibHJN-9liMe3JRlFGGofcXPR5C_6Sz-vOoAmLmM32HdofE7rlToLp96Imyr2WptEDyNmuTL8&gsessionid=q9FHT4IlkDgrP2hYcJs2qPnsACLtGNYYHGcc_cYbOejD89rlNmyoZQ)  
  <sub>Seeking Alpha, 4 hours ago</sub>  
  Gold prices are tumbling as the Federal Reserve's aggressive rate-hiking cycle sparks a "fear factor" in markets that may be triggering a deleveraging wave,...
- [Chart of the Day 11/20/26: A Tale of Two "Safe Havens"](https://www.google.com/goto?url=CAESpgEBxCJF1zFDxPCJB2NcwAiwiHlnBmUOm6t8t0ItC0l6M-tVWvFjytw3r8pyu5hdIWN-7KL0qP2-1RpjQ2NzwZfpOKxTeIktQr-4OjfWxs2vSPM1Mcbm9PjmAB6n9e31tNt5EpL5_jQ8Bn952M8tdKOg4j6jGTe-x6U1_V5lmFIaAs9WW6WaVPj2a4YAZuIKCFL8LjQEb_-0UonD4g4AVyEZk8ETrmYM&gsessionid=q9FHT4IlkDgrP2hYcJs2qPnsACLtGNYYHGcc_cYbOejD89rlNmyoZQ)  
  <sub>www.moneyshow.com, 9 hours ago</sub>  
  The stock market is sliding. Tech stocks are getting tossed out. And investors are seeking “Safe Havens.” But two typical refuges in times of market turmoil...
- [Gold Stocks Fall: What's Going On?](https://www.google.com/goto?url=CAESmQEBxCJF1--OAn3G3i9ASY3JYE0SU97WbIo3BsPAR1BG6n8iugRWEBJZLZQN5FqW9QgH6TEBYKvE4vlf6gFb2OxItoVSIm7ITyBDvr5qfC58QuJge8dkkq_rgZMIQ-efAL-tFAYDaBvZjuXlHFlk-dsLXC3QGYu8U-t9Xh8XmbqSdiXSw-dEm-n6xWQWbU2AFBCpTVZIgaxSRjU&gsessionid=q9FHT4IlkDgrP2hYcJs2qPnsACLtGNYYHGcc_cYbOejD89rlNmyoZQ)  
  <sub>Benzinga, 21 hours ago</sub>  
  SPDR Gold (NYSE: GLD) shares are falling Thursday after gold set a new low under $3700 an ounce. Here's what you should know.
- [Gold, Silver Plunge Further Amid Fed Rate Hike Concerns: Buy The Dip Or Brace For More Pain?](https://www.google.com/goto?url=CAES1AEBxCJF1yX8Ci8GVMtfPIM0Nb6iorr8OVZmCRDyUInq39fEMkmoMjfAXIVduLG7DDszktwLZsYXCeeH9vzTdbHcfqm6OtUgHP_BF4vdPibn6lpFt3xPYnE_o4gowO0Umk0AOWflbPtGsTeDSloRpZwCNhRId1vZUsow7I3m85NrPlTKhso2k8Km3oI2a_1faDXDzgHNxI27IICe9EcGivZild3xg4h4U-8lVIvgPmSpIOirC2oUk-6Hej9Dbkns6NSjsI7lwfJIxw2a31aP_R79fTsMcw&gsessionid=q9FHT4IlkDgrP2hYcJs2qPnsACLtGNYYHGcc_cYbOejD89rlNmyoZQ)  
  <sub>TradingView, 13 hours ago</sub>  
  Precious metals prices are dipping persistently amid rising concerns about rate hikes at the Federal Reserve's December policy meeting,...
- [Chart Of The Day: A Tale Of Two 'Safe Havens'](https://www.google.com/goto?url=CAESigEBxCJF1_urUKgJZq4gbSi77KPhydMsSQF2Cv_9ZXLz6pwreRh74MH5_Fxcr9mg6qv-MZVtD9jmes65gacq09ly6Lqt_3JI_6ynxFMyhqUXyzE-CtIvJi86CGeDTOBy64IJlZQpJhi-zHDbXWiKAeOjuWQiB5WpzH6OqJfl27CkRLEH62krruRO41o&gsessionid=q9FHT4IlkDgrP2hYcJs2qPnsACLtGNYYHGcc_cYbOejD89rlNmyoZQ)  
  <sub>Seeking Alpha, 4 hours ago</sub>  
  The stock market is sliding. Tech stocks are getting tossed out. And investors are seeking safe havens. Two typical refuges in times of market turmoil are...
- [Patience In Gold Paid Off, Now Let's Get Bullish](https://www.google.com/goto?url=CAESlAEBxCJF1yphJF9rGZy62vgSF1Y1xcggmagihB4gu_mgoXllY7RUAzSbk-DHwPJngbsIJUWtagdIo_RlLl2D0oSENQ3HTBhrAfPWLe_Hd7olBGa578i-8mg7-zU5tyhllfRlJP5wHPChuAoVRy1AbKlBzM1vHUcnLgd9Gmabv2PDF29Rbo6Nw_2Dxz-uEb71caUhAgyW&gsessionid=q9FHT4IlkDgrP2hYcJs2qPnsACLtGNYYHGcc_cYbOejD89rlNmyoZQ)  
  <sub>Seeking Alpha, 2 hours ago</sub>  
  The bull case for gold: the writer sees the forecast cut as a contrarian buying opportunity after the correction, with central banks still net buyers.
- [Gold Demand Trends: India Focus Q3 2026](https://www.google.com/goto?url=CAESjAEBxCJF1xk8yIyhR4oVT_w59wYbdUtc5LKC4UwqM4jUCblQ0D9j8Zys32VD08xO93HoaDVnyqxXz_EhMYm8k4iCv1y8mNZ2bvzKKQ15XKsJz2h7aZUjRGAggM3jj4UdhKqcKf2yr9mu6q0VeO1ck36KXPu9DuvFkKcGOt-EgFAXwso1zLiJFPlHmH_Zug&gsessionid=q9FHT4IlkDgrP2hYcJs2qPnsACLtGNYYHGcc_cYbOejD89rlNmyoZQ)  
  <sub>Seeking Alpha, 10 hours ago</sub>  
  India's gold market improved from the subdued second quarter, with sequential growth across all segments, albeit to varying degrees.
- [Gold extends losses below $3,700, pressured by rate-hike bets (GLD:NYSEARCA)](https://www.google.com/goto?url=CAESnQEBxCJF1wGd5lFVTeyetOJVl2dd-LQKVA7c7YzwawuAKmLsZ_eBEFZwR18IxNbwmm3KkgqEruGcxtoRnFwWp324pSvY3GMmKaNx06jQaVL3aHbzMHT_QmlnZc_YxMn4Bnj_9g9VxXomQlkqOMWd3ujbTtQmAoqcUwKTl2yf_Ppn1aNXrjxfXdVhhVFBbI_2VmJMtm_F3ALrC0GPJ-0K&gsessionid=q9FHT4IlkDgrP2hYcJs2qPnsACLtGNYYHGcc_cYbOejD89rlNmyoZQ)  
  <sub>Seeking Alpha, 16 hours ago</sub>  
  Gold futures fell to fresh 14-month lows as the market's overwhelming consensus anticipates a rate hike at the Federal Reserve's December meeting to combat...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.14% (+0.02 on the week) | 5-year 4.78% (-0.20 on the week) | 10-year 4.99% (-0.17 on the week) | 30-year 5.37% (-0.11 on the week)
Yield curve, 10-year minus 3-month: +0.84 points -- upward sloping (normal)
US dollar index: 103.69 (+0.28 on the week)
Volatility (VIX): 29.46 (+10.2 on the week) -- stressed
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.1% (2026-10-01) | jobless claims 203k (2026-11-14)
Policy and expectations: Fed target 4.00% | market expects 2.2% inflation over 10 years
Rate path: 2-year Treasury 4.80% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score -0.20</summary>

```text
Last close 327.62 (bar of 2026-11-20), from 502 daily bars
Trend: vs 20d SMA 360.66 (-9.2%), 50d 374.99 (-12.6%), 200d 405.85 (-19.3%); 50d below 200d
Momentum: RSI(14) 25.2 | MACD -10.486 vs signal -7.177 (histogram -3.309)
Returns: 1d -2.3% | 5d -7.8% | 1m -11.2% | 3m -23.2%
52-week range: 327.62 - 495.90 (now 0.0% of the way up)
Volatility: ATR(14) 7.02 (2.1% of price) | annualised 20d 29.7%
Volume: 0.39x the 20-day average
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
Measured: 3 months: fund -23.2%, commodity -24.0%, gap +0.8% | 6 months: fund -20.8%, commodity -21.1%, gap +0.2% | 12 months: fund -12.6%, commodity -12.5%, gap -0.1%
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
Shares outstanding: 260.30M | fund size: 85.28B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Sugar (CANE) · Commodity — no answer, no confidence given

**This one did not finish:** the full-model stage ran past its 90 minute budget before CANE was asked

<details><summary><b>News</b> — score n/a</summary>

_No news found for this one today._

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score n/a</summary>

```text
US Treasury yields: 3-month 4.14% (+0.02 on the week) | 5-year 4.78% (-0.20 on the week) | 10-year 4.99% (-0.17 on the week) | 30-year 5.37% (-0.11 on the week)
Yield curve, 10-year minus 3-month: +0.84 points -- upward sloping (normal)
US dollar index: 103.69 (+0.28 on the week)
Volatility (VIX): 29.46 (+10.2 on the week) -- stressed
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.1% (2026-10-01) | jobless claims 203k (2026-11-14)
Policy and expectations: Fed target 4.00% | market expects 2.2% inflation over 10 years
Rate path: 2-year Treasury 4.80% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score n/a</summary>

```text
Last close 10.18 (bar of 2026-11-20), from 502 daily bars
Trend: vs 20d SMA 11.11 (-8.4%), 50d 11.51 (-11.6%), 200d 10.33 (-1.5%); 50d above 200d
Momentum: RSI(14) 25.4 | MACD -0.314 vs signal -0.224 (histogram -0.091)
Returns: 1d -1.4% | 5d -8.7% | 1m -15.6% | 3m -9.6%
52-week range: 9.02 - 12.47 (now 33.5% of the way up)
Volatility: ATR(14) 0.21 (2.1% of price) | annualised 20d 31.1%
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
Cost of holding this fund instead of sugar itself: -7.3% a year -- heavy: rolling contracts costs this fund real money
Measured: 3 months: fund -9.6%, commodity -4.4%, gap -5.1% | 6 months: fund +2.8%, commodity +14.8%, gap -12.0% | 12 months: fund +7.8%, commodity +15.1%, gap -7.3%
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
Share count change: 1 week: +2.6% (1.41M) over 7d | 1 month: +24.8% (10.95M) over 30d
Shares outstanding: 5.41M | fund size: 55.09M
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Corn (CORN) · Commodity — no answer, no confidence given

**This one did not finish:** the full-model stage ran past its 90 minute budget before CORN was asked

<details><summary><b>News</b> — score n/a</summary>

- [2 Farm ETFs Own What Every Grocery Store Depends On](https://247wallst.com/investing/etf/2026/11/20/2-farm-etfs-own-what-every-grocery-store-depends-on/)  
  <sub>24/7 Wall St., 3 hours ago</sub>  
  Two funds beat the S&P 500 this past year, yet both lagged it badly over five. One spreads bets across the food chain while the other leans on a single...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score n/a</summary>

```text
US Treasury yields: 3-month 4.14% (+0.02 on the week) | 5-year 4.78% (-0.20 on the week) | 10-year 4.99% (-0.17 on the week) | 30-year 5.37% (-0.11 on the week)
Yield curve, 10-year minus 3-month: +0.84 points -- upward sloping (normal)
US dollar index: 103.69 (+0.28 on the week)
Volatility (VIX): 29.46 (+10.2 on the week) -- stressed
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.1% (2026-10-01) | jobless claims 203k (2026-11-14)
Policy and expectations: Fed target 4.00% | market expects 2.2% inflation over 10 years
Rate path: 2-year Treasury 4.80% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score n/a</summary>

```text
Last close 16.95 (bar of 2026-11-20), from 502 daily bars
Trend: vs 20d SMA 17.25 (-1.8%), 50d 18.32 (-7.5%), 200d 18.17 (-6.7%); 50d above 200d
Momentum: RSI(14) 34.1 | MACD -0.329 vs signal -0.364 (histogram 0.035)
Returns: 1d -0.7% | 5d -1.3% | 1m -4.7% | 3m -11.8%
52-week range: 16.47 - 20.29 (now 12.6% of the way up)
Volatility: ATR(14) 0.23 (1.4% of price) | annualised 20d 14.5%
Volume: 0.26x the 20-day average
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
Cost of holding this fund instead of corn itself: -9.4% a year -- heavy: rolling contracts costs this fund real money
Measured: 3 months: fund -11.8%, commodity -8.3%, gap -3.5% | 6 months: fund -7.7%, commodity -2.7%, gap -5.0% | 12 months: fund -4.5%, commodity +4.9%, gap -9.4%
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
Share count change: 1 week: +2.5% (2.57M) over 7d | 1 month: -12.3% (-15.02M) over 30d
Shares outstanding: 6.34M | fund size: 107.41M
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Copper (CPER) · Commodity — no answer, no confidence given

**This one did not finish:** the full-model stage ran past its 90 minute budget before CPER was asked

<details><summary><b>News</b> — score n/a</summary>

- [Whatever Happens to Copper Next, These 3 Investments Offer Different Ways to Play It](https://www.marketbeat.com/articles/whatever-happens-to-copper-next-these-3-investments-offer-different-ways-to-play-it/)  
  <sub>MarketBeat, 22 hours ago</sub>  
  Copper prices have slid amid demand and supply concerns, pressuring Freeport-McMoRan, COPX, and CPER, three distinct ways investors can gain exposure to...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score n/a</summary>

```text
US Treasury yields: 3-month 4.14% (+0.02 on the week) | 5-year 4.78% (-0.20 on the week) | 10-year 4.99% (-0.17 on the week) | 30-year 5.37% (-0.11 on the week)
Yield curve, 10-year minus 3-month: +0.84 points -- upward sloping (normal)
US dollar index: 103.69 (+0.28 on the week)
Volatility (VIX): 29.46 (+10.2 on the week) -- stressed
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.1% (2026-10-01) | jobless claims 203k (2026-11-14)
Policy and expectations: Fed target 4.00% | market expects 2.2% inflation over 10 years
Rate path: 2-year Treasury 4.80% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score n/a</summary>

```text
Last close 33.57 (bar of 2026-11-20), from 502 daily bars
Trend: vs 20d SMA 37.56 (-10.6%), 50d 38.89 (-13.7%), 200d 37.93 (-11.5%); 50d above 200d
Momentum: RSI(14) 21.9 | MACD -1.365 vs signal -0.902 (histogram -0.462)
Returns: 1d -0.6% | 5d -8.1% | 1m -12.7% | 3m -16.2%
52-week range: 30.77 - 41.43 (now 26.3% of the way up)
Volatility: ATR(14) 0.73 (2.2% of price) | annualised 20d 27.9%
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
Cost of holding this fund instead of copper itself: -3.1% a year -- a steady drag
Measured: 3 months: fund -16.2%, commodity -15.8%, gap -0.4% | 6 months: fund -13.7%, commodity -12.4%, gap -1.4% | 12 months: fund +7.8%, commodity +11.0%, gap -3.1%
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
Share count change: 1 week: +11.1% (65.13M) over 7d | 1 month: +7.8% (47.10M) over 30d
Shares outstanding: 19.45M | fund size: 652.80M
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Silver (SLV) · Commodity — no answer, no confidence given

**This one did not finish:** the full-model stage ran past its 90 minute budget before SLV was asked

<details><summary><b>News</b> — score n/a</summary>

- [Nasdaq, Dow, S&P 500 futures slip as Anthropic’s record debut fails to lift AI stocks: SLV, GLD, AMD, NVDA in focus](http://www.bing.com/news/apiclick.aspx?ref=FexRss&aid=&tid=6b005ff56765432caf5b1a35c48f29d6&url=https%3a%2f%2fwww.msn.com%2fen-us%2fnews%2fother%2fnasdaq-dow-s-p-500-futures-slip-as-anthropic-s-record-debut-fails-to-lift-ai-stocks-slv-gld-amd-nvda-in-focus%2far-AA2hOZ3f&c=3597220065891809694&mkt=en-us)  
  <sub>Stocktwits on MSN, 20h ago</sub>  
  ANT stock soared more than 17% at close, ending the session at $97.17 and taking its valuation to roughly $1.76 trillion. ・Chipmakers posted a selloff despite the Anthropic IPO and Nvidia’s recent ...
- [Silver Is Down 65% From Its Record. The 15-Minute Question Misses the Point](http://www.bing.com/news/apiclick.aspx?ref=FexRss&aid=&tid=6b005ff56765432caf5b1a35c48f29d6&url=https%3a%2f%2fwww.ainvest.com%2fnews%2fsilver-65-record-15-minute-question-misses-point-2611%2f&c=9797105109265890880&mkt=en-us)  
  <sub>ainvest, 13h ago</sub>  
  Silver fell 65% from its January 2026 record to $42.41/oz by November 2026, despite a 217% surge since October 2025.
- [Gold, Silver Plunge Further Amid Fed Rate Hike Concerns: Buy The Dip Or Brace For More Pain?](http://www.bing.com/news/apiclick.aspx?ref=FexRss&aid=&tid=6b005ff56765432caf5b1a35c48f29d6&url=https%3a%2f%2fstocktwits.com%2fnews-articles%2fmarkets%2fequity%2fgold-silver-plunge-further-amid-fed-rate-hike-concerns-buy-the-dip-or-brace-for-more-pain%2fcNb1CasR90U&c=11066885578489250305&mkt=en-us)  
  <sub>Stocktwits, 21h ago</sub>  
  Gold spot prices fell below $3,600 an ounce, while silver spot prices are currently trading at $42.38, both near Aug. 2025 levels.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score n/a</summary>

```text
US Treasury yields: 3-month 4.14% (+0.02 on the week) | 5-year 4.78% (-0.20 on the week) | 10-year 4.99% (-0.17 on the week) | 30-year 5.37% (-0.11 on the week)
Yield curve, 10-year minus 3-month: +0.84 points -- upward sloping (normal)
US dollar index: 103.69 (+0.28 on the week)
Volatility (VIX): 29.46 (+10.2 on the week) -- stressed
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.1% (2026-10-01) | jobless claims 203k (2026-11-14)
Policy and expectations: Fed target 4.00% | market expects 2.2% inflation over 10 years
Rate path: 2-year Treasury 4.80% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score n/a</summary>

```text
Last close 38.24 (bar of 2026-11-20), from 502 daily bars
Trend: vs 20d SMA 45.21 (-15.4%), 50d 51.03 (-25.1%), 200d 61.08 (-37.4%); 50d below 200d
Momentum: RSI(14) 22.1 | MACD -3.056 vs signal -2.535 (histogram -0.521)
Returns: 1d -3.5% | 5d -13.3% | 1m -22.5% | 3m -38.5%
52-week range: 38.24 - 105.60 (now 0.0% of the way up)
Volatility: ATR(14) 1.59 (4.2% of price) | annualised 20d 43.7%
Volume: 0.47x the 20-day average
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
Cost of holding this fund instead of silver itself: -0.7% a year -- close to nothing, as a physically backed fund should be
Measured: 3 months: fund -38.5%, commodity -38.5%, gap -0.0% | 6 months: fund -44.1%, commodity -44.5%, gap +0.4% | 12 months: fund -17.7%, commodity -17.0%, gap -0.7%
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
Share count change: 1 week: +0.0% (0.00) over 10d | 1 month: +0.0% (0.00) over 30d
Shares outstanding: 341.45M | fund size: 13.06B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Soybeans (SOYB) · Commodity — no answer, no confidence given

**This one did not finish:** the full-model stage ran past its 90 minute budget before SOYB was asked

<details><summary><b>News</b> — score n/a</summary>

- [Del campo a la bolsa: los 10 Cedears para apostar al negocio agropecuario](https://rosariofinanzas.ar/noticias/del-campo-a-la-bolsa-los-10-cedears-para-apostar-al-negocio-agropecuario)  
  <sub>Rosario Finanzas, 18 hours ago</sub>  
  La oferta de Cedears vinculados al agro se divide en ETFs y empresas, ofreciendo diez alternativas para inversores argentinos interesados en el sector.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score n/a</summary>

```text
US Treasury yields: 3-month 4.14% (+0.02 on the week) | 5-year 4.78% (-0.20 on the week) | 10-year 4.99% (-0.17 on the week) | 30-year 5.37% (-0.11 on the week)
Yield curve, 10-year minus 3-month: +0.84 points -- upward sloping (normal)
US dollar index: 103.69 (+0.28 on the week)
Volatility (VIX): 29.46 (+10.2 on the week) -- stressed
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.1% (2026-10-01) | jobless claims 203k (2026-11-14)
Policy and expectations: Fed target 4.00% | market expects 2.2% inflation over 10 years
Rate path: 2-year Treasury 4.80% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score n/a</summary>

```text
Last close 25.57 (bar of 2026-11-20), from 502 daily bars
Trend: vs 20d SMA 25.79 (-0.8%), 50d 26.77 (-4.5%), 200d 25.36 (+0.8%); 50d above 200d
Momentum: RSI(14) 40.0 | MACD -0.303 vs signal -0.335 (histogram 0.032)
Returns: 1d +0.5% | 5d -1.5% | 1m -4.0% | 3m -1.4%
52-week range: 21.71 - 28.14 (now 60.1% of the way up)
Volatility: ATR(14) 0.28 (1.1% of price) | annualised 20d 15.0%
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
Cost of holding this fund instead of soybeans itself: 1.9% a year -- the roll has been paying this fund
Measured: 3 months: fund -1.4%, commodity +0.0%, gap -1.4% | 6 months: fund +2.0%, commodity +1.7%, gap +0.4% | 12 months: fund +9.0%, commodity +7.0%, gap +1.9%
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
Share count change: 1 week: +1.3% (511.90K) over 7d | 1 month: -9.5% (-4.10M) over 30d
Shares outstanding: 1.53M | fund size: 39.16M
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Natural gas (UNG) · Commodity — no answer, no confidence given

**This one did not finish:** the full-model stage ran past its 90 minute budget before UNG was asked

<details><summary><b>News</b> — score n/a</summary>

_No news found for this one today._

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score n/a</summary>

```text
US Treasury yields: 3-month 4.14% (+0.02 on the week) | 5-year 4.78% (-0.20 on the week) | 10-year 4.99% (-0.17 on the week) | 30-year 5.37% (-0.11 on the week)
Yield curve, 10-year minus 3-month: +0.84 points -- upward sloping (normal)
US dollar index: 103.69 (+0.28 on the week)
Volatility (VIX): 29.46 (+10.2 on the week) -- stressed
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.1% (2026-10-01) | jobless claims 203k (2026-11-14)
Policy and expectations: Fed target 4.00% | market expects 2.2% inflation over 10 years
Rate path: 2-year Treasury 4.80% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score n/a</summary>

```text
Last close 10.22 (bar of 2026-11-20), from 502 daily bars
Trend: vs 20d SMA 9.76 (+4.7%), 50d 10.28 (-0.5%), 200d 10.93 (-6.4%); 50d below 200d
Momentum: RSI(14) 52.5 | MACD 0.036 vs signal -0.064 (histogram 0.099)
Returns: 1d -0.4% | 5d +0.7% | 1m +3.4% | 3m +0.7%
52-week range: 9.00 - 16.90 (now 15.5% of the way up)
Volatility: ATR(14) 0.38 (3.8% of price) | annualised 20d 47.2%
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
Cost of holding this fund instead of natural gas itself: -10.3% a year -- heavy: rolling contracts costs this fund real money
Measured: 3 months: fund +0.7%, commodity +30.6%, gap -29.9% | 6 months: fund -6.6%, commodity +25.0%, gap -31.6% | 12 months: fund -30.5%, commodity -20.1%, gap -10.3%
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
Share count change: 1 week: +0.0% (0.00) over 10d | 1 month: +0.0% (0.00) over 30d
Shares outstanding: 12.08M | fund size: 123.54M
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Oil (USO) · Commodity — no answer, no confidence given

**This one did not finish:** the full-model stage ran past its 90 minute budget before USO was asked

<details><summary><b>News</b> — score n/a</summary>

- [Decline in U.S. diesel prices likely to continue, Energy Secretary says (USO:NYSEARCA)](https://seekingalpha.com/news/4674991-decline-in-us-diesel-prices-likely-to-continue-energy-secretary-says)  
  <sub>Seeking Alpha, 14 hours ago</sub>  
  US diesel prices should continue to decline from record highs as refined products from the Persian Gulf return to the market, Secretary of Energy Chris...
- [‘Eyes on Hormuz’: Analyst Warns Iran May Defy US Blockade With Oil Exports, Flags Hormuz Vessel Strikes a](https://www.benzinga.com/news/politics/26/11/63463938/eyes-on-hormuz-analyst-warns-iran-may-defy-us-blockade-with-oil-exports-flags-hormuz-vessel-strikes-as-trump-is-not-rushing-decisions)  
  <sub>Benzinga, 9 hours ago</sub>  
  Obsidian Risk Advisors' Managing Principal Brett Erickson said Thursday that Iran may try to export oil despite the U.S. naval blockade of the Strait of...
- [Plunging oil refining margins signal inflation relief for central banks (USO:NYSEARCA)](https://www.google.com/goto?url=CAESqgEBxCJF14y1dgfXgrbpQu9tCOX4pwiLt4qRXL1p0fLIkytWOrHOxNtOfsIof33rUOwHCxcS_z5ZKaFek09i6Ibxo1_Vc1MB0ef7siS0NIu164QwotQ9qhTy-phapPWTasWbrdCozn7HmttVXAam5bl7S4nZibV44TItw6Dtm-Z4m6VY2P3RBjqVQmXt_SXvPYYOjGs9BkMKxAy3g0mfPmUXnF7dNCnilsr_0A&gsessionid=KE_Nb6lg3De7lRkPArBShKeHrGIWy2Nz2iFdJK2hn58XsuBeCAvsmg)  
  <sub>Seeking Alpha, 18 hours ago</sub>  
  Oil refining margins fall toward pre-war levels as 3-2-1 spreads drop to $25-$40 a barrel from $60-$75, signaling cooling inflation.
- [Tether invierte en SCRYPT para ampliar el uso institucional de stablecoins](https://www.google.com/goto?url=CAESpgEBxCJF10lX7Riob-tnBaGRFN2hUbDrL9waYDoSjuSSbx1j7Lxb17Pw7_CAtux6NiR57DPdqAkVo63axW7kxS0mA6BsrN7SM47XWx-XexYsQOQ_Xz6jdv1lf_B3IdjmtzBO9Ty1_0tYvmexHCZ7ItfsXPKL1s9gd2xW_b0zWsSpU1c4Bbs6ovBxzJjiwcsadt8PWMRASguNIL9sZ0FAdetMum5anLIY&gsessionid=KE_Nb6lg3De7lRkPArBShKeHrGIWy2Nz2iFdJK2hn58XsuBeCAvsmg)  
  <sub>Crypto Economy, 23 hours ago</sub>  
  Tether invierte en la plataforma suiza SCRYPT para ampliar la infraestructura institucional de trading, custodia, liquidez y pagos con stablecoins.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score n/a</summary>

```text
US Treasury yields: 3-month 4.14% (+0.02 on the week) | 5-year 4.78% (-0.20 on the week) | 10-year 4.99% (-0.17 on the week) | 30-year 5.37% (-0.11 on the week)
Yield curve, 10-year minus 3-month: +0.84 points -- upward sloping (normal)
US dollar index: 103.69 (+0.28 on the week)
Volatility (VIX): 29.46 (+10.2 on the week) -- stressed
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.1% (2026-10-01) | jobless claims 203k (2026-11-14)
Policy and expectations: Fed target 4.00% | market expects 2.2% inflation over 10 years
Rate path: 2-year Treasury 4.80% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score n/a</summary>

```text
Last close 135.78 (bar of 2026-11-20), from 502 daily bars
Trend: vs 20d SMA 149.91 (-9.4%), 50d 151.59 (-10.4%), 200d 129.17 (+5.1%); 50d above 200d
Momentum: RSI(14) 35.1 | MACD -4.661 vs signal -2.901 (histogram -1.760)
Returns: 1d -1.7% | 5d -6.7% | 1m -16.4% | 3m +2.7%
52-week range: 66.17 - 169.53 (now 67.3% of the way up)
Volatility: ATR(14) 4.99 (3.7% of price) | annualised 20d 46.2%
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
Share count change: 1 week: +0.0% (0.00) over 10d | 1 month: +0.0% (0.00) over 30d
Shares outstanding: 119.10M | fund size: 16.17B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Wheat (WEAT) · Commodity — no answer, no confidence given

**This one did not finish:** the full-model stage ran past its 90 minute budget before WEAT was asked

<details><summary><b>News</b> — score n/a</summary>

_No news found for this one today._

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score n/a</summary>

```text
US Treasury yields: 3-month 4.14% (+0.02 on the week) | 5-year 4.78% (-0.20 on the week) | 10-year 4.99% (-0.17 on the week) | 30-year 5.37% (-0.11 on the week)
Yield curve, 10-year minus 3-month: +0.84 points -- upward sloping (normal)
US dollar index: 103.69 (+0.28 on the week)
Volatility (VIX): 29.46 (+10.2 on the week) -- stressed
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.1% (2026-10-01) | jobless claims 203k (2026-11-14)
Policy and expectations: Fed target 4.00% | market expects 2.2% inflation over 10 years
Rate path: 2-year Treasury 4.80% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score n/a</summary>

```text
Last close 21.30 (bar of 2026-11-20), from 502 daily bars
Trend: vs 20d SMA 21.89 (-2.7%), 50d 23.69 (-10.1%), 200d 23.63 (-9.8%); 50d above 200d
Momentum: RSI(14) 34.9 | MACD -0.619 vs signal -0.672 (histogram 0.053)
Returns: 1d -0.8% | 5d -2.6% | 1m -6.7% | 3m -16.4%
52-week range: 19.88 - 28.00 (now 17.5% of the way up)
Volatility: ATR(14) 0.41 (1.9% of price) | annualised 20d 22.5%
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

```text
Cost of holding this fund instead of wheat itself: -9.9% a year -- heavy: rolling contracts costs this fund real money
Measured: 3 months: fund -16.4%, commodity -13.5%, gap -2.9% | 6 months: fund -13.2%, commodity -8.7%, gap -4.5% | 12 months: fund +0.0%, commodity +9.9%, gap -9.9%
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
Share count change: 1 week: +4.4% (10.00M) over 7d | 1 month: -7.0% (-17.71M) over 30d
Shares outstanding: 11.07M | fund size: 235.82M
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

