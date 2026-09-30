# Daily report

**30 Sep 2026, 19:02 Israel time (16:02 UTC)** · 80 names checked · 0 traded · 0 with a problem

**Answers with no explanation:** 15 of 58 (the model wrote only a label, like “NEUTRAL”, where its reason should be). Their main reasons are still shown.

**Run:** started by the outside scheduler (via supabase-cron), on time (planned for 14:40 UTC).

| Group | Looked at | Took a side | No clear view | Problems |
| --- | --- | --- | --- | --- |
| Companies | 16 | 2 | 14 | 0 |
| Whole-market funds | 14 | 0 | 14 | 0 |
| Sector and country funds | 41 | 0 | 41 | 0 |
| Commodities | 9 | 0 | 9 | 0 |

## Open positions

Checked before any new trade. R is what the trade risked at entry; the ladder sells a third at +1R and another at +3R, the stop-loss follows the price up every day, and it only ever moves up.

| Position | What happened |
| --- | --- |
| Developing country bonds (EMB) · Index fund | **Stop raised.** At +2.83R, following the price. Stop-loss raised 92.34 → 92.14. |
| US government bonds, 7-10 years (IEF) · Index fund | **Stop raised.** At +2.37R, following the price. Stop-loss raised 90.37 → 90.26. |
| US regional banks (KRE) · Sector or country | **Stop raised.** At +0.72R, following the price. Stop-loss raised 72.49 → 71.93. |
| Microsoft (MSFT) · Company | **Stop raised.** At +1.24R, following the price. Stop-loss raised 492.61 → 493.66. |
| Teva Pharmaceutical (TEVA) · Company | **Stop raised.** At +0.14R, following the price. Stop-loss raised 37.12 → 37.20. |
| US government bonds, 20+ years (TLT) · Index fund | **Stop raised.** At +2.52R, following the price. Stop-loss raised 79.80 → 79.30. |
| ASML (ASML) · Company | **Holding.** +0.84R, holding 1 shares. Stop-loss 1733.63. |
| Caterpillar (CAT) · Company | **Holding.** +0.14R, holding 2 shares. Stop-loss 780.92. |
| Taiwan (EWT) · Sector or country | **Holding.** -0.37R, holding 33 shares. Stop-loss 110.28. |
| Gold (GLD) · Commodity | **Holding.** +0.46R, holding 10 shares. Stop-loss 393.48. |
| HDFC Bank (HDB) · Company | **Holding.** -0.96R, holding 90 shares. Stop-loss 22.23. |
| JPMorgan Chase (JPM) · Company | **Holding.** -0.26R, holding 6 shares. Stop-loss 327.15. |
| Eli Lilly (LLY) · Company | **Holding.** +0.55R, holding 4 shares. Stop-loss 1130.70. |
| Nvidia (NVDA) · Company | **Holding.** +1.18R, holding 16 shares. Stop-loss 219.12. |
| Novo Nordisk (NVO) · Company | **Holding.** +0.39R, holding 123 shares. Stop-loss 40.52. |
| Procter & Gamble (PG) · Company | **Holding.** +0.04R, holding 14 shares. Stop-loss 143.66. |
| S&P 500, equal weight (RSP) · Index fund | **Holding.** +0.71R, holding 14 shares. Stop-loss 212.66. |
| Royal Bank of Canada (RY) · Company | **Holding.** -0.56R, holding 10 shares. Stop-loss 195.58. |
| US inflation-linked bonds (TIP) · Index fund | **Holding.** +2.96R, holding 4 shares. Stop-loss 104.79. |
| US dollar (UUP) · Index fund | **Holding.** +1.60R, holding 282 shares. Stop-loss 28.54. |
| US shopping and leisure (XLY) · Sector or country | **Holding.** +0.25R, holding 63 shares. Stop-loss 112.09. |
| Exxon Mobil (XOM) · Company | **Holding.** +0.21R, holding 13 shares. Stop-loss 156.50. |

## How to read this

Once a day the system looks at every name on the list. For each one it reads five kinds of evidence and gives each kind a score from -1.00 (bad) to +1.00 (good). Then it picks a side and says how sure it is, from 0.00 to 1.00.

The three sides: **BULLISH** = the model thinks the price will go up; **BEARISH** = the model thinks the price will go down; **NEUTRAL** = the model has no clear view.

Being sure is not enough on its own. A trade only happens when confidence reaches **0.30**. Below that the system writes down what it thought and does nothing. The size of a trade, the stop-loss and every limit are decided by plain code, not by the model.

Open positions are checked first, before any new trade. When a trade has earned back what it risked (+1R), a third of it is sold and the stop-loss moves up to the entry price, so it can no longer lose. At three times that (+3R) another third is sold and the stop moves up again. The last third stays open. Every day the stop-loss also follows the price up, so a position only ever closes when its stop is hit. The stop only ever moves up.

Under each name you will find the five scores. Click a grey line to open it and see the exact evidence behind that score. The words inside quotation marks are the model's own; nothing there has been rewritten.

## Companies

### MercadoLibre (MELI) · Company — BULLISH, confidence 0.65

**Result:** REJECTED · no room under the sleeve budget limit

**In the model's own words:** no explanation. It wrote only “BUY”, so the main reasons below are all it gave.

**Main reasons it gave:**
- Credit portfolio grew 75% YoY to $16.4B (NEWS)
- Two insiders bought shares (124 and 600) in last 180 days (INSIDER)
- Consensus rating Moderate Buy with mean target +33% vs last close (ANALYST)
- RSI 33.3 indicates oversold condition (TECHNICAL)
- Revenue growth 49.8% YoY despite high debt/equity 168.6% (FUNDAMENTALS)

<details><summary><b>News</b> — score +0.65</summary>

- [Credit Portfolio Growth Might Change The Case For Investing In MercadoLibre Stock (MELI)](https://simplywall.st/stocks/us/retail/nasdaq-meli/mercadolibre/news/credit-portfolio-growth-might-change-the-case-for-investing)  
  <sub>Simply Wall St, 10 minutes ago</sub>  
  MercadoLibre reported that its credit portfolio reached US$16.4b in Q2 2026, reflecting 75% year-over-year expansion supported by stronger credit card...
- [MercadoLibre, Inc. (NASDAQ:MELI) Receives Consensus Recommendation of "Moderate Buy" from Analysts](https://www.marketbeat.com/instant-alerts/consensus-mercadolibre-inc-nasdaq-meli-receives-consensus-recommendation-of-moderate-buy-from-analysts-2026-09-30/)  
  <sub>MarketBeat, 8 hours ago</sub>  
  Shares of MercadoLibre, Inc. (NASDAQ:MELI - Get Free Report) have been given an average recommendation of "Moderate Buy" by the eighteen ratings firms that...
- [MercadoLibre stock trades at EUR 1,518.80 and shows minus 0.27 percent](https://www.ad-hoc-news.de/boerse/news/corporate-news/mercadolibre-stock-trades-at-eur-1-518-80-and-shows-minus-0-27-percent/70203690)  
  <sub>AD HOC NEWS, 4 hours ago</sub>  
  MELI, US58733R1023. MercadoLibre stock trades at EUR 1,518.80 and shows minus 0.27 percent. Published on 09/30/2026 at 12:25 | Editorial responsibility:...
- [MercadoLibre stock pre-market at EUR 1,523.20: plus 0.02 percent](https://www.ad-hoc-news.de/boerse/news/vorboerse/mercadolibre-stock-pre-market-at-eur-1-523-20-plus-0-02-percent/70202267)  
  <sub>AD HOC NEWS, 8 hours ago</sub>  
  MELI, US58733R1023. MercadoLibre stock pre-market at EUR 1,523.20: plus 0.02 percent. Published on 09/30/2026 at 08:37 | Editorial responsibility: Rafael...
- [MercadoLibre stock after-hours at EUR 1,522.60: plus 1.08 percent](https://www.ad-hoc-news.de/boerse/news/nachboerse/mercadolibre-stock-after-hours-at-eur-1-522-60-plus-1-08-percent/70200688)  
  <sub>AD HOC NEWS, 19 hours ago</sub>  
  MELI, US58733R1023. MercadoLibre stock after-hours at EUR 1,522.60: plus 1.08 percent. Published on 09/29/2026 at 21:34 | Editorial responsibility: Rafael...
- [Sea Limited (SE) Stock Price, News, Quote & History](https://ca.finance.yahoo.com/quote/SE/)  
  <sub>Yahoo! Finance Canada, 22 hours ago</sub>  
  Find the latest Sea Limited (SE) stock quote, history, news and other vital information to help you with your stock trading and investing.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.65</summary>

_Not available today._

</details>

<details><summary><b>Price and chart</b> — score -0.40</summary>

```text
Last close 1,709.05 (bar of 2026-09-30), from 502 daily bars
Trend: vs 20d SMA 1,843.15 (-7.3%), 50d 1,864.20 (-8.3%), 200d 1,840.52 (-7.1%); 50d above 200d
Momentum: RSI(14) 33.3 | MACD -45.278 vs signal -27.789 (histogram -17.489)
Returns: 1d -0.9% | 5d -5.0% | 1m -11.7% | 3m -1.9%
52-week range: 1,546.81 - 2,360.76 (now 19.9% of the way up)
Volatility: ATR(14) 56.57 (3.3% of price) | annualised 20d 26.0%
Volume: 0.23x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score -0.20</summary>

```text
Sector: Consumer Cyclical / Internet Retail | market cap 86.64B
Valuation: trailing P/E 46.44 | forward P/E 30.57 | P/B 11.06 | PEG 1.00
Profitability: profit margin 5.3% | operating margin 6.7% | ROE 27.5%
Growth (YoY): revenue +49.8% | earnings -10.9%
Balance sheet: debt/equity 168.6% | free cash flow 353.38M
Risk: beta 1.31 | short interest 1.6% of float
Next earnings: 2026-11-04
```

</details>

<details><summary><b>What this fund holds</b> — score -0.20</summary>

_Not available today._

</details>

<details><summary><b>Does this company beat its own forecasts</b> — score -0.20</summary>

```text
Earnings record, last 4 quarters: 1 beat, 3 missed
  2026-06-30 beat by 4% | 2026-03-31 missed by 7% | 2025-12-31 missed by 6% | 2025-09-30 missed by 13%
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
Consensus: buy (mean 1.54 on a 1=strong buy to 5=strong sell scale, 26 analysts)
Ratings: 4 strong buy, 17 buy, 5 hold, 0 sell, 0 strong sell
Price target: mean 2,273.40 (+33.0% vs last close), range 1,750.00 - 2,800.00
Recent rating changes:
  - 2026-09-03 BTIG: reit, Buy -> Buy
  - 2026-08-11 JP Morgan: main, Neutral -> Neutral
  - 2026-08-06 Cantor Fitzgerald: main, Overweight -> Overweight
  - 2026-08-06 BTIG: reit, Buy -> Buy
  - 2026-07-15 Citigroup: main, Neutral -> Neutral
  - 2026-06-02 BTIG: reit, Buy -> Buy
Institutional ownership: 80.3%
Largest holders: Capital Research Global Investors (6.2%), BAILLIE GIFFORD & CO (6.0%), Capital International Investors (3.7%), Capital World Investors (3.5%), Morgan Stanley (2.9%)
```

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score +0.60</summary>

_Not available today._

</details>

<details><summary><b>Buying and selling by company insiders</b> — score +0.40</summary>

```text
Last 180 days: bought 0 shares in 0 transaction(s) | sold n/a shares in 0
Net: +0 shares | insiders hold 3,529,511 shares
Distinct insiders: 2 buying, 0 selling
Open-market purchases — insiders spending their own money:
  - 2026-06-11 MELAMUD MARCELO (Officer): 124 shares, 200.00K
  - 2026-05-22 AGUZIN ALEJANDRO NICOLAS (Director): 600 shares, 993.56K
(4 grant/option/gift transaction(s) excluded — compensation, not a view on the price)
```

</details>

<details><summary><b>Who is positioned how</b> — score +0.40</summary>

_Not available today._

</details>

<details><summary><b>Money going into and out of this fund</b> — score +0.40</summary>

_Not available today._

</details>

### Alphabet (Google) (GOOGL) · Company — BULLISH, confidence 0.45

**Result:** REJECTED · no room under the sleeve budget limit

**In the model's own words:**

> Positive news on AI chips and valuation, strong fundamentals, technicals in an uptrend, and bullish analyst price targets outweigh mixed earnings record and low volume, supporting a moderate‑conviction buy.

**Main reasons it gave:**
- AI chips slated for space test, indicating new AI hardware opportunity (Barchart.com)
- Trailing P/E 17.48 and profit margin 54.8% show cheap valuation and high profitability (Fundamentals)
- Price above 20d, 50d, 200d SMAs with positive MACD (Technical)
- Analysts' mean price target $429.36 implies ~23% upside (Analyst View)
- Mixed earnings record (2 beats, 2 misses) adds modest downside risk (Earnings Record)

<details><summary><b>News</b> — score +0.50</summary>

- [The Dates That Matter Most For Alphabet Stock](https://www.google.com/goto?url=CAESpgEB6zswFdjXOOTPNoJ4qQTCPlttmq_NauGYQHfgchJzHJuLsRkSEl__EQpXBUgMF3zGJ17xLX6EMajonTXva_n1tKVrjmGgJUlTh0UZsZzPdhoQtvDUsI1d95WdLmXODia8iyrYPFWUwbLLSA8Vx8wRr4IygRaHNQlQquCBkWQCvbW_2ObE1LTfMfolVRw2OGBHuTJSUDfGM7ITGYitMrrRHBjbJaD3)  
  <sub>Trefis, 2 hours ago</sub>  
  Alphabet (GOOGL) stock has returned 39% over the past year, against 16.8% for the S&P 500. In July 2026, management raised its 2026 capital spending plan to...
- [What Is Going On With Alphabet Stock?](https://www.google.com/goto?url=CAESkAEB6zswFfPqqrYfbD-6WxauvCcvzyddKn9ZXwVtXvn0SYMfdj0DjCWNajp8T9KHgnCZ4ZsjOqZgnlC3cS_DfWmzCIbygtzgQ6kkXXZYfzQLb_cRGIl-KjNUMTY-vIbn0FTxrrBbVDXvcyeRM93uhUM9K5lTkDMtqMLw5Yiw6CrSQJMEyRd_eZ9zYDk1bA-WF7Y)  
  <sub>Yahoo Finance, 1 hour ago</sub>  
  Alphabet (GOOGL) stock costs 22% less than the median S&P 500 company, measured by price against the past year's earnings. Alphabet's revenue still grew...
- [Google's AI Chips Are Set to Be Sent to Space. What This Means for GOOGL Stock.](https://www.google.com/goto?url=CAEStAEB6zswFYz0UpJ31B87-Jc2DVCVhESunqcLQBRxDEnyPcIVb9Z6ywmlcNxrI9mNvy7w51HW_Ybdy9Y4IC1WEDUugvGEuywJOQKoY3R9Xa7j0Zhq6kPLcu5m0A6A9z4u9CBBA14SiBuaAfAKuq2pofP8iFoLi4JViLrYEAGw4X_0n4C-wjxpgEES0G6RxYuCqP3GjcMrcmAJVogrB7UJ_5Ja0Pn-VBOXYpVOEMxVet9qINk9U_c)  
  <sub>Barchart.com, 42 minutes ago</sub>  
  Alphabet's (GOOGL) Google is looking to live up to its name of cosmic scale as the company is set to test its artificial intelligence (AI) chips in low...
- [Is This The Right Time To Buy Google Stock?](https://www.google.com/goto?url=CAESoAEB6zswFanxalUv3MVzwVOzryxbDr3e8jwewI01iO4DxolsQXQ6XiIwpBzhWeAK0_e4kUJxrY0iJYXQQ2AgFzPyOknqPdg3IHqBpAiFDZ5u9-nc1RGeQp9zrm0ZYptA_vldXOIISjHEkFGEsCFQ9eD6SQWTHLjx9221J9f7PoBl-A7M8C_rWyk0MsOcNJ5hxeLD6ac4Bdb_fLlEwPRPuuf-)  
  <sub>Forbes, 2 hours ago</sub>  
  This article was written by Doug Nathman, with research by his team at Trefis. Measured by price relative to the past year's earnings, Alphabet (GOOGL)...
- [GOOGL Stock Falls Out Of Favor In June – Analysts See More Upside In These Big Tech](https://www.google.com/goto?url=CAESzQEB6zswFdZ3u9EQrspiPXNrQ4gUDNEyZLhnq4NB0RK_LBQ8bkkaoFkHSrl7VtCnM9mt97yunhrC6n2o7NeAEN85RPFl0k89Fr8kgdHigqGb2vst1Vmuga-5e03OZ4jjwJG5pozasPZP5NEdOM2BymsNmQmYSCe1Z46RMwJg6UC-nP5qzZb-BS8gTaj864x8x1nVVRzpyfxq8IZE93Va_xxgp58NPnrp5-597zoACb9BS_pblsdeJJCQiaTRUgr3GPGHlmC44uA7JKTxNy0S)  
  <sub>Stocktwits, 15 hours ago</sub>  
  Currently, 57 out of 64 analysts rate GOOGL stock 'Buy' or higher, and seven rate it 'Hold,' per Koyfin. Their average price target of $337.37 implies an upside...
- [Alphabet: The AI Winner Nobody Is Talking About (NASDAQ:GOOGL)](https://www.google.com/goto?url=CAESkgEB6zswFdamms6Dz-BzdFdqr2j-D-g5bOw7Do2vJWubMou_ImvtiHwX5KlEUV4_DrDqFggh4UM6PjMInUNQED2tOXvuy8K_35IPlwZ2YcoMzfWrOf9PB9s9jPjQFZWVLr9PWuvNpFHiV4Cchx-KAXLmBPdriuuQtgCPRtpxswfyGVRIco74kvrnFOD1LPG7HXPLWQ)  
  <sub>Seeking Alpha, 15 hours ago</sub>  
  Alphabet remains well positioned in the agentic AI race, leveraging its ecosystem, infrastructure, and diversified revenue streams. Click for this GOOGL...
- [Google GOOG Stock Rebounds Above $350 but Needs $365 Breakout as Gemini Growth and Spending Risks Collide](https://www.google.com/goto?url=CAESzgEB6zswFdxtR4kAH3BzmgLXo5XarXFkrdLIUVPbKvctz9NHKixTLBtFixi2U2T20xm59CMq5CdE9S3k1467PzE485U2KCz4EBWPoEXInKm7Yg-Mvqt17wO-8abQLiqcrU-gM3OVyBkIfj3VFEtfyJ-yx_PUdsTkePf3S8TcOcKJV6VYKKQkzVGp8qpPjmshtOHeEXnLhBFHgZTgFP55ntCOcgk_yLhI8FF9UKEVbDgiWVuO7o9omTiniE1iQzgkZH7BuEHNHU0j7PWjSXzWnA)  
  <sub>FXLeaders, 7 minutes ago</sub>  
  Alphabet shares have rebounded above $350 after finding support, but the recovery remains tentative as Gemini expansion, heavy infrastructure spending and...
- [AMZN, MSFT, GOOGL Need $1 Trillion in Revenue To Earn 15% Return on AI Capex — Here's What Goldman Says A](https://www.google.com/goto?url=CAES9wEB6zswFZgBbY8MjmmrQVeia2nC4r3AgRlb6hiGU3qnxoAf_dHk-zI-zOd75B46eBlGcqgyUrP7Y6YAFjNL8lowSg9CXZCtk0W-ZPSe4Z9mMkBDjgGIibjUmWlnx28jZlPJrC7ScSKbIELpQxhL3SSq2mu_8Pf7WEeY2A7LHOP-delY6NotvDxIWkhhP0oJ9HNB7xDX1P6TiLbTTNI0pJ37l7qdZgYCbaVMwRml5_m2AJTAYqL6fN1QegG6QPWWDkNS6Nbo6umx6-lhyIigPW2os0YE5gFnzm-RKTW8JkGwIodDwIuJEI8VHcRZEsWBQqi9cPLjdb9R)  
  <sub>Benzinga, 6 hours ago</sub>  
  Goldman Sachs notes Big Tech's $1.7T cloud backlog covers 60% of the $1T revenue needed by 2030 to de-risk AI investments.
- [Alphabet Inc (GOOGL) Shares Fall 0.5% -- What GF Score of 97 Tel](https://www.google.com/goto?url=CAESpwEB6zswFesXZgg4DV0CD1myDEnlDDuf4caTp3voIvIlH9qq5oUot5yEYiAAarvC8U6idAHxuQf2VBr6g9JM8rIrDTe6KG4aAvpycbMsS3aM34Bi5H08fph574YPsfHFQX8C6IT1CSl18J0k1-ISx-bakr4FYvBzL1rsJWBipLYN1UOKtmB8TCRavo7aZ2a6zzvowPui0Kxv3QatngwEXU-Ke4KVIo8N8w)  
  <sub>GuruFocus, 15 hours ago</sub>  
  On September 29, 2026, Alphabet Inc (GOOGL) shares fell 0.5% to a current price of $340.92. The stock has experienced a 52-week range of $235.84 to $408.61,...
- [Alphabet (GOOG) CEO Sundar Pichai receives 3,671 shares as stock awards vest.](https://www.google.com/goto?url=CAESpQEB6zswFQ4wwBrYOPZz8rIZ_wjlVUMw4i1vEl16KyA1IW5LwVtVBFHCgwtLsS9aTPwj4gngA8SLTAP9hNk86Z65eLP475nLpZ-kQ7rAz_4N4guWfDzeY2ywhgCkHi__kZfZCoN-s_t3SFxvF-0swRNYga2H6ytgjyczG51qYrQFjdljFwgOdVoqnc25j_45qnaZTHY3tLzfEcwHdwN-oREe390-GfA)  
  <sub>Stock Titan, 14 hours ago</sub>  
  Alphabet Inc. Chief Executive Officer Sundar Pichai had 3,671 Class C Google Stock Units vest on September 25, 2026, converting into 3,671 shares of Class C...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.50</summary>

_Not available today._

</details>

<details><summary><b>Price and chart</b> — score +0.20</summary>

```text
Last close 348.65 (bar of 2026-09-30), from 502 daily bars
Trend: vs 20d SMA 342.74 (+1.7%), 50d 344.02 (+1.3%), 200d 338.62 (+3.0%); 50d above 200d
Momentum: RSI(14) 53.6 | MACD 0.132 vs signal -0.215 (histogram 0.346)
Returns: 1d +2.3% | 5d +3.2% | 1m +2.7% | 3m -3.5%
52-week range: 236.57 - 402.62 (now 67.5% of the way up)
Volatility: ATR(14) 8.46 (2.4% of price) | annualised 20d 26.3%
Volume: 0.35x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.70</summary>

```text
Sector: Communication Services / Internet Content & Information | market cap 4.26T
Valuation: trailing P/E 17.48 | forward P/E 23.13 | P/B 6.85 | PEG 1.25
Profitability: profit margin 54.8% | operating margin 34.0% | ROE 48.7%
Growth (YoY): revenue +24.2% | earnings +294.0%
Balance sheet: debt/equity 18.9% | free cash flow 22.67B
Risk: beta 1.23 | short interest 1.5% of float
Next earnings: 2026-10-28
```

</details>

<details><summary><b>What this fund holds</b> — score +0.70</summary>

_Not available today._

</details>

<details><summary><b>Does this company beat its own forecasts</b> — score +0.70</summary>

```text
Earnings record, last 4 quarters: 2 beats, 2 missed
  2026-06-30 missed by 4% | 2026-03-31 missed by 3% | 2025-12-31 beat by 4% | 2025-09-30 beat by 29%
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

<details><summary><b>What analysts and big funds say</b> — score +0.40</summary>

```text
Consensus: strong_buy (mean 1.38 on a 1=strong buy to 5=strong sell scale, 54 analysts)
Ratings: 13 strong buy, 43 buy, 5 hold, 0 sell, 0 strong sell
Price target: mean 429.36 (+23.2% vs last close), range 340.00 - 515.00
Recent rating changes:
  - 2026-09-28 Piper Sandler: reit, Overweight -> Overweight
  - 2026-09-18 Tigress Financial: main, Strong Buy -> Strong Buy
  - 2026-09-17 Evercore ISI Group: main, Outperform -> Outperform
  - 2026-09-03 Rosenblatt: main, Buy -> Buy
  - 2026-07-23 UBS: main, Neutral -> Neutral
  - 2026-07-23 Morgan Stanley: main, Overweight -> Overweight
Institutional ownership: 81.0%
Largest holders: Blackrock Inc. (7.9%), Vanguard Capital Management LLC (6.5%), FMR, LLC (4.3%), State Street Corporation (4.1%), Geode Capital Management, LLC (2.6%)
```

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score +0.40</summary>

_Not available today._

</details>

<details><summary><b>Buying and selling by company insiders</b> — score +0.00</summary>

```text
Last 180 days: bought 0 shares in 0 transaction(s) | sold n/a shares in 0
Net: +0 shares | insiders hold 195,190,800 shares
Distinct insiders: 0 buying, 0 selling
(2 grant/option/gift transaction(s) excluded — compensation, not a view on the price)
```

</details>

<details><summary><b>Who is positioned how</b> — score +0.00</summary>

_Not available today._

</details>

<details><summary><b>Money going into and out of this fund</b> — score +0.00</summary>

_Not available today._

</details>

### Elbit Systems (ESLT) · Company — NEUTRAL, confidence 0.35

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Mixed signals: technicals are bearish (low RSI, negative MACD, thin volume), fundamentals appear expensive (high P/E), but earnings record is strong (four consecutive beats) and analyst view is neutral with modest upside target. No material news catalyst. Overall view leans neutral with low conviction.

**Main reasons it gave:**
- Technical: RSI 30.5, MACD negative, volume 0.32× 20‑day average indicating weak momentum
- Fundamentals: high trailing P/E 51.7 and forward P/E 37.4 suggest expensive valuation
- Earnings record: four consecutive beats show strong performance
- Analyst view: price target +18.8% vs last close but consensus neutral, no recent upgrades

<details><summary><b>News</b> — score +0.00</summary>

- [Elbit Systems Ltd. (ESLT) stock price, news, quote and history](https://uk.finance.yahoo.com/quote/ESLT/)  
  <sub>Yahoo Finance UK, 16 hours ago</sub>  
  Elbit Systems Ltd. (ESLT) · -5.27% · -0.75% · -19.14% · 21.48% · 41.28% · 386.59% · 17,484.25%. Key events. Baseline. Advanced chart. Loading...
- [VE4H ETF Holdings List — HAN:VE4H](https://www.tradingview.com/symbols/HAN-VE4H/holdings/)  
  <sub>TradingView, 10 hours ago</sub>  
  Explore detailed ETF holdings data, including weight, shares, and market value. Unlock more data. Made by humans. EnglishEnglish.
- [Israel shares higher at close of trade; TA 35 up 0.02%](https://uk.investing.com/news/stock-market-news/israel-shares-higher-at-close-of-trade-ta-35-up-002-4887951)  
  <sub>Investing.com UK, 24 hours ago</sub>  
  Investing.com – Israel equities were higher at the close on Tuesday, as gains in the Real Estate, Communication and Technology sectors propelled shares...
- [DFEN ETF Holdings List — HAN:DFEN](https://www.tradingview.com/symbols/HAN-DFEN/holdings/)  
  <sub>TradingView, 15 hours ago</sub>  
  Explore detailed ETF holdings data, including weight, shares, and market value. Unlock more data. Made by humans. EnglishEnglish.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

_Not available today._

</details>

<details><summary><b>Price and chart</b> — score -0.60</summary>

```text
Last close 687.08 (bar of 2026-09-30), from 502 daily bars
Trend: vs 20d SMA 724.13 (-5.1%), 50d 759.03 (-9.5%), 200d 771.94 (-11.0%); 50d below 200d
Momentum: RSI(14) 30.5 | MACD -9.988 vs signal -7.545 (histogram -2.444)
Returns: 1d -2.3% | 5d -7.5% | 1m -1.9% | 3m -9.6%
52-week range: 454.95 - 1,014.33 (now 41.5% of the way up)
Volatility: ATR(14) 17.40 (2.5% of price) | annualised 20d 21.1%
Volume: 0.32x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.00</summary>

```text
Sector: Industrials / Aerospace & Defense | market cap 32.20B
Valuation: trailing P/E 51.70 | forward P/E 37.42 | P/B 7.29 | PEG n/a
Profitability: profit margin 7.4% | operating margin 9.6% | ROE 15.2%
Growth (YoY): revenue +15.9% | earnings +34.2%
Balance sheet: debt/equity 19.3% | free cash flow -38.48M
Risk: beta -0.30 | short interest 0.9% of float
Next earnings: 2026-11-24
```

</details>

<details><summary><b>What this fund holds</b> — score +0.00</summary>

_Not available today._

</details>

<details><summary><b>Does this company beat its own forecasts</b> — score +0.00</summary>

```text
Earnings record, last 4 quarters: 4 beats
  2026-06-30 beat by 10% | 2026-03-31 beat by 16% | 2025-12-31 beat by 16% | 2025-09-30 beat by 21%
```

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

```text
Consensus: none (mean n/a on a 1=strong buy to 5=strong sell scale, 6 analysts)
Ratings: 0 strong buy, 1 buy, 5 hold, 0 sell, 0 strong sell
Price target: mean 816.33 (+18.8% vs last close), range 518.00 - 960.00
Recent rating changes:
  - 2026-08-19 JP Morgan: main, Neutral -> Neutral
  - 2026-06-24 Jefferies: main, Hold -> Hold
  - 2026-05-27 Jefferies: main, Hold -> Hold
  - 2026-05-27 JP Morgan: main, Neutral -> Neutral
  - 2026-04-13 JP Morgan: main, Neutral -> Neutral
  - 2026-03-22 Jefferies: main, Hold -> Hold
Institutional ownership: 23.0%
Largest holders: Clal Insurance Enterprises Holdings Ltd (3.5%), Vanguard Capital Management LLC (1.6%), Van Eck Associates Corporation (1.2%), Y.D. More Investments Ltd (1.0%), Altshuler Shaham Ltd (1.0%)
```

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score +0.00</summary>

_Not available today._

</details>

<details><summary><b>Buying and selling by company insiders</b> — score +0.00</summary>

```text
Last 180 days: bought 82,000 shares in 7 transaction(s) | sold 69,736 shares in 7
Net: +12,264 shares (+0.1% of insider holdings) | insiders hold 19,278,816 shares
Distinct insiders: 0 buying, 5 selling
Sales — weak evidence on their own; often scheduled 10b5-1 plans, tax on vesting, or diversification:
  - 2026-04-09 DELMAR HAIM DANIEL (Officer): 7,654 shares, 6.79M
  - 2026-04-09 MACHLIS BEZHALEL (Chief Executive Officer): 25,514 shares, 22.64M
  - 2026-04-09 VERED YEHUDA (Officer): 5,953 shares, 5.28M
  - 2026-04-09 KRIL RAN (Officer): 6,803 shares, 6.04M
(5 grant/option/gift transaction(s) excluded — compensation, not a view on the price)
```

</details>

<details><summary><b>Who is positioned how</b> — score +0.00</summary>

_Not available today._

</details>

<details><summary><b>Money going into and out of this fund</b> — score +0.00</summary>

_Not available today._

</details>

### Toyota (TM) · Company — NEUTRAL, confidence 0.35

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Mixed signals: negative news and bearish technicals offset bullish fundamentals and analyst consensus; no insider activity. Net view is ambiguous, leading to a neutral stance with low conviction.

**Main reasons it gave:**
- China sales slump in August (23% decline) – negative news
- Price below 20‑day, 50‑day, and 200‑day SMAs; RSI 40.1 – bearish technicals
- Trailing P/E 8.32 and earnings growth +86.9% YoY – supportive fundamentals
- Analyst consensus strong buy with 26% price target – bullish analyst view
- No insider transactions in the last 180 days – neutral insider activity

<details><summary><b>News</b> — score -0.60</summary>

- [Toyota's China Problem: Is TM Stock a Buy, Hold or Sell?](https://www.zacks.com/stock/news/2998213/toyotas-china-problem-is-tm-stock-a-buy-hold-or-sell)  
  <sub>Zacks Investment Research, 1 hour ago</sub>  
  TM's China sales slump weighs on August results, but hybrids, financing income, buybacks and low valuation provide support amid profit pressures.
- [Walmart is among the retailers carrying Be Water, whose bottles feature seven messages.](https://www.stocktitan.net/news/INKW/more-than-a-logo-greene-concepts-builds-be-water-tm-into-a-brand-fgsonwpjuqk2.html)  
  <sub>Stock Titan, 3 hours ago</sub>  
  Blue Ridge spring water is bottled at Greene Concepts' 60000-square-foot North Carolina plant; Be Water packaging carries seven messages.
- [Toyota Motor Corp (TM) Shares Fall 0.8% -- What GF Score of 76 T](https://www.gurufocus.com/news/9102514/toyota-motor-corp-tm-shares-fall-08-what-gf-score-of-76-tells-investors)  
  <sub>GuruFocus, 14 hours ago</sub>  
  On September 29, 2026, Toyota Motor Corp (TM) shares fell 0.8% to a current price of $186.71. This decline comes amid a 52-week trading range of $166.10 to...
- [Integrated Quantum Technologies Announces Veil(TM) Channel Partnership with Synergis](https://finance.yahoo.com/technology/ai/articles/integrated-quantum-technologies-announces-veil-123000663.html)  
  <sub>Yahoo Finance, 2 hours ago</sub>  
  Vancouver, British Columbia--(Newsfile Corp. - September 30, 2026) - Integrated Quantum Technologies Inc. (CSE: VEIL) (OTCQB: IGCRF) (FSE: Y4G1)...
- [(FMAX) Technical Analysis and Trading Signals (FMAX:CA)](https://news.stocktradersdaily.com/canada/fmax-technical-analysis-and-trading-signals_20260930_00885a)  
  <sub>Stock Traders Daily, 4 hours ago</sub>  
  Technical Analysis Report for Hamilton U.S. Financials YIELD MAXIMIZER TM ETF (FMAX) with Key Trading Signals.
- [MA Switching Surges Among Dually Eligible Adults: Grace Mackleby, PhD](https://www.ajmc.com/view/ma-switching-surges-among-dually-eligible-adults-grace-mackleby-phd)  
  <sub>AJMC, 17 hours ago</sub>  
  Grace Mackleby, PhD, explores why dually eligible beneficiaries more often switch MA plans than leave for traditional Medicare.
- [The EU weighs how to crack down on imported electric vehicles (TM:NYSE)](https://seekingalpha.com/news/4648128-the-eu-weighs-how-to-crack-down-on-imported-electric-vehicles)  
  <sub>Seeking Alpha, 23 hours ago</sub>  
  EU's draft Industrial Accelerator Act may require 70% EU-made EV content to access subsidies—impacting Toyota, Honda, Nissan, Nio, BYD & XPeng.
- [Patients may soon compare medication experiences with others like them.](https://www.stocktitan.net/news/GCTK/lokahi-therapeutics-tm-announces-qare-tm-the-first-real-time-tvxs76a1p3ai.html)  
  <sub>Stock Titan, 2 hours ago</sub>  
  Qare is designed to let users document, organize and analyze treatment experiences; additional drug classes are expected in future releases.
- [Toyota Motor stock trades at EUR 164.00 as August sales fall](https://www.ad-hoc-news.de/boerse/news/corporate-news/toyota-motor-stock-trades-at-eur-164-00-as-august-sales-fall/70202574)  
  <sub>AD HOC NEWS, 8 hours ago</sub>  
  TM, US8923313071. Toyota Motor stock trades at EUR 164.00 as August sales fall. Published on 09/30/2026 at 09:11 | Editorial responsibility: Rafael Müller,...
- [Toyota stock falls as China sales drop on fuel price surge By Investing.com](https://za.investing.com/news/stock-market-news/toyota-stock-falls-as-china-sales-drop-on-fuel-price-surge-93CH-4481888)  
  <sub>Investing.com South Africa, 17 hours ago</sub>  
  Investing.com - Toyota Motor (NYSE:TM) reported a 23% decline in China sales for August, marking the seventh consecutive monthly drop as rising fuel prices...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score -0.60</summary>

_Not available today._

</details>

<details><summary><b>Price and chart</b> — score -0.60</summary>

```text
Last close 185.54 (bar of 2026-09-30), from 502 daily bars
Trend: vs 20d SMA 192.58 (-3.7%), 50d 190.57 (-2.6%), 200d 201.69 (-8.0%); 50d below 200d
Momentum: RSI(14) 40.1 | MACD -1.128 vs signal 0.025 (histogram -1.154)
Returns: 1d -0.6% | 5d -2.5% | 1m -5.6% | 3m +9.4%
52-week range: 166.50 - 248.29 (now 23.3% of the way up)
Volatility: ATR(14) 3.12 (1.7% of price) | annualised 20d 21.7%
Volume: 0.17x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.30</summary>

```text
Sector: Consumer Cyclical / Auto Manufacturers | market cap 219.71B
Valuation: trailing P/E 8.32 | forward P/E 11.76 | P/B 15.09 | PEG n/a
Profitability: profit margin 8.6% | operating margin 7.9% | ROE 12.4%
Growth (YoY): revenue +10.4% | earnings +86.9%
Balance sheet: debt/equity 115.0% | free cash flow -3.60T
Risk: beta 0.34 | short interest 0.1% of float
Next earnings: 2026-11-05
```

</details>

<details><summary><b>What this fund holds</b> — score +0.30</summary>

_Not available today._

</details>

<details><summary><b>Does this company beat its own forecasts</b> — score +0.30</summary>

```text
Earnings record, last 4 quarters: 4 beats
  2026-06-30 beat by 44% | 2026-03-31 beat by 12% | 2025-12-31 beat by 27% | 2025-09-30 beat by 24%
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
Consensus: strong_buy (mean 1.50 on a 1=strong buy to 5=strong sell scale, 4 analysts)
Ratings: 2 strong buy, 2 buy, 0 hold, 0 sell, 0 strong sell
Price target: mean 234.08 (+26.2% vs last close), range 230.00 - 239.31
Recent rating changes:
  - 2025-11-07 Freedom Broker: down, Buy -> Hold
  - 2025-02-04 Macquarie: up, Neutral -> Outperform
  - 2024-06-14 Erste Group: down, Buy -> Hold
  - 2023-07-11 Morgan Stanley: down, Overweight -> Equal-Weight
  - 2022-10-06 UBS: down, Buy -> Neutral
  - 2022-07-07 Jefferies: main, ? -> Hold
Institutional ownership: 2.2%
Largest holders: Fisher Asset Management, LLC (0.5%), Morgan Stanley (0.2%), FMR, LLC (0.1%), Goldman Sachs Group Inc (0.1%), Northern Trust Corporation (0.1%)
```

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score +0.50</summary>

_Not available today._

</details>

<details><summary><b>Buying and selling by company insiders</b> — score +0.00</summary>

```text
Last 180 days: bought 0 shares in 0 transaction(s) | sold n/a shares in 0
Net: +0 shares | insiders hold 757,877 shares
Distinct insiders: 0 buying, 0 selling
```

</details>

<details><summary><b>Who is positioned how</b> — score +0.00</summary>

_Not available today._

</details>

<details><summary><b>Money going into and out of this fund</b> — score +0.00</summary>

_Not available today._

</details>

### ASML (ASML) · Company — no answer, no confidence given

<details><summary><b>News</b> — score n/a</summary>

- [Here is What to Know Beyond Why ASML Holding N.V. (ASML) is a Trending Stock](https://finance.yahoo.com/markets/stocks/articles/know-beyond-why-asml-holding-120006769.html)  
  <sub>Yahoo Finance, 3 hours ago</sub>  
  ASML (ASML) has been one of the stocks most watched by Zacks.com users lately. So, it is worth exploring what lies ahead for the stock.
- [ASML Stock Gains Over 5% — Why Bernstein Thinks ASML Holding Can Keep Climbing After Nearly 140% Run In The Past Year](https://stocktwits.com/news-articles/markets/equity/asml-stock-why-bernstein-sees-more-upside-after-140-percent-rally/cZm11SiR7lF)  
  <sub>Stocktwits, 14 hours ago</sub>  
  Shares of ASML Holding NV (ASML) surged nearly 5.5% on Monday after Bernstein significantly raised its price target on the semiconductor equipment maker.
- [ASML Holding N.V. vs. Marvell Technology: Which Technology Stock Is a Better Buy in 2026?](https://www.fool.com/coverage/better-buy/2026/09/30/asml-holding-n-v-vs-marvell-technology-which-technology-stock-is-a-better-buy-in-2026/)  
  <sub>The Motley Fool, 3 hours ago</sub>  
  ASML commands a near-monopoly on chip-making equipment with a 29% net margin, while Marvell surged 42% in revenue but trades at a steeper valuation.
- [ASML Stocks Slip as High-NA Adoption Extends Into 2030](https://www.gurufocus.com/news/9103537/asml-stocks-slip-as-highna-adoption-extends-into-2030)  
  <sub>GuruFocus, 18 minutes ago</sub>  
  ASML Holding (ASML), the advanced-lithography equipment leader, maintained its High-NA momentum as major chipmakers mapped out production plans. U.S. shares...
- [ASML, TSM earnings could test market expectations, Sara Awad says (ASML:NASDAQ)](https://seekingalpha.com/news/4648351-asml-tsm-earnings-could-test-market-expectations-sara-awad-says)  
  <sub>Seeking Alpha, 5 hours ago</sub>  
  Watch ASML and TSM Q3 earnings as a market test or catalyst.
- [Why is ASML NV ADR stock rising today?](https://www.investing.com/news/stock-market-news/why-is-asml-nv-adr-stock-rising-today-93CH-4922972)  
  <sub>Investing.com, 12 hours ago</sub>  
  Investing.com -- ASML Holding NV ADR stock rose 2.5% in morning trading to reach $1,815.84, lifted by a Buy rating reiteration from UBS analyst...
- [What's Going On With ASML Stock Tuesday?](https://www.benzinga.com/markets/tech/26/09/62058006/whats-going-on-with-asml-stock-tuesday)  
  <sub>Benzinga, 22 hours ago</sub>  
  ASML Holding NV (NASDAQ:ASML) stock rose nearly 3% Tuesday, outperforming the broader market as investors favored large-cap semiconductor equipment stocks.
- [ASML Stock Surges 3.8% as AI Rebound Returns to Lithography](https://finance.yahoo.com/markets/stocks/articles/asml-stock-surges-3-8-184836110.html)  
  <sub>Yahoo Finance, 20 hours ago</sub>  
  This article first appeared on GuruFocus. ASML Holding (NASDAQ:ASML), the Dutch maker of advanced chipmaking equipment, rose about 3.8% to $1,837.99 by...
- [ASML Rises as Chip Equipment Stocks Gain on AI Demand Optimism](https://www.quiverquant.com/news/ASML+Rises+as+Chip+Equipment+Stocks+Gain+on+AI+Demand+Optimism)  
  <sub>Quiver Quantitative, 24 hours ago</sub>  
  ASML Holding N.V. (ASML) is up 3.3% today. Here is some analysis on what might have caused this pric.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>Price and chart</b> — score n/a</summary>

```text
Last close 1,817.75 (bar of 2026-09-30), from 502 daily bars
Trend: vs 20d SMA 1,704.79 (+6.6%), 50d 1,720.28 (+5.7%), 200d 1,535.28 (+18.4%); 50d above 200d
Momentum: RSI(14) 60.8 | MACD 18.978 vs signal -0.560 (histogram 19.538)
Returns: 1d -0.9% | 5d +4.2% | 1m +7.2% | 3m -1.4%
52-week range: 936.19 - 1,989.44 (now 83.7% of the way up)
Volatility: ATR(14) 50.88 (2.8% of price) | annualised 20d 41.7%
Volume: 0.26x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score n/a</summary>

```text
Sector: Technology / Semiconductor Equipment & Materials | market cap 698.20B
Valuation: trailing P/E 62.72 | forward P/E 30.90 | P/B 1,563.05 | PEG 1.58
Profitability: profit margin 30.1% | operating margin 37.1% | ROE 53.9%
Growth (YoY): revenue +21.3% | earnings +28.5%
Balance sheet: debt/equity 9.1% | free cash flow 8.44B
Risk: beta 1.36 | short interest 0.4% of float
Next earnings: 2026-10-14
```

</details>

<details><summary><b>What this fund holds</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>Does this company beat its own forecasts</b> — score n/a</summary>

```text
Earnings record, last 4 quarters: 2 beats, 1 in line, 1 missed
  2026-06-30 beat by 9% | 2026-03-31 beat by 7% | 2025-12-31 missed by 5% | 2025-09-30 in line
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
Consensus: strong_buy (mean 1.40 on a 1=strong buy to 5=strong sell scale, 16 analysts)
Ratings: 7 strong buy, 31 buy, 3 hold, 1 sell, 0 strong sell
Price target: mean 2,115.58 (+16.4% vs last close), range 878.74 - 2,813.86
Recent rating changes:
  - 2026-07-16 JP Morgan: main, Overweight -> Overweight
  - 2026-07-16 Wells Fargo: main, Overweight -> Overweight
  - 2026-07-16 RBC Capital: main, Outperform -> Outperform
  - 2026-07-14 RBC Capital: main, Outperform -> Outperform
  - 2026-07-06 Bernstein: main, Outperform -> Outperform
  - 2026-06-22 B of A Securities: main, Buy -> Buy
Institutional ownership: 20.4%
Largest holders: FMR, LLC (1.4%), Fisher Asset Management, LLC (1.2%), Capital World Investors (1.0%), Invesco Ltd. (0.8%), State Farm Mutual Automobile Insurance Co (0.7%)
```

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>Buying and selling by company insiders</b> — score n/a</summary>

```text
Last 180 days: bought 0 shares in 0 transaction(s) | sold n/a shares in 0
Net: +0 shares | insiders hold 3,414,222 shares
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

<details><summary><b>News</b> — score n/a</summary>

- [Caterpillar (CAT) Stock May Be Reasonably Priced Despite Its 368% Run](https://finance.yahoo.com/markets/stocks/articles/caterpillar-cat-stock-may-reasonably-081146094.html)  
  <sub>Yahoo Finance, 7 hours ago</sub>  
  Caterpillar has delivered a striking run for shareholders over the past few years, and the stock now trades at a level that puts real weight on what its...
- [Why Caterpillar Stock Has Surged 75% Over the Past Year on AI Power Demand](https://www.tikr.com/blog/why-caterpillar-stock-has-surged-75-over-the-past-year-on-ai-power-demand)  
  <sub>TIKR.com, 7 hours ago</sub>  
  Caterpillar stock has orders booked into 2030, yet the shares fell from $1065 to $827. What the Street's $976 target says about the AI debate.
- [Caterpillar plans a roughly $1 billion North Carolina plant to make machines that move materials.](https://www.stocktitan.net/news/CAT/caterpillar-to-invest-1-billion-in-north-carolina-to-expand-cat-o4bshuci0tgd.html)  
  <sub>Stock Titan, 2 hours ago</sub>  
  The planned Sanford plant would increase production of compact track loaders and telehandlers; it is expected to create manufacturing career opportunities.
- [Has CAT Stock Become A Different Bet?](https://www.trefis.com/stock/cat/articles/616924/has-cat-stock-become-a-different-bet/2026-09-29)  
  <sub>Trefis, 19 hours ago</sub>  
  Caterpillar's shifting revenue mix reveals a company changing its core narrative. Management sounds notably different on its earnings calls today compared...
- [Caterpillar plans $1B North Carolina expansion, agrees to buy Fabick dealership (CAT:NYSE)](https://seekingalpha.com/news/4648514-caterpillar-plans-1b-north-carolina-expansion-agrees-to-buy-fabick-dealership)  
  <sub>Seeking Alpha, 1 hour ago</sub>  
  Caterpillar (CAT) invests $1B in North Carolina to expand compact equipment and buys dealer John Fabick.
- [LUCK,LINE,RSG,CAT,ITT,ANF,SEIC,KIDS,PETZ,THC | Stock Prices | Quote Comparison](https://ca.finance.yahoo.com/quotes/LUCK,LINE,RSG,CAT,ITT,ANF,SEIC,KIDS,PETZ,THC/)  
  <sub>Yahoo! Finance Canada, 4 hours ago</sub>  
  View and compare LUCK,LINE,RSG,CAT,ITT,ANF,SEIC,KIDS,PETZ,THC on Yahoo Finance.
- [Which dow jones stocks are moving on Tuesday?](https://www.chartmill.com/news/MRK/Chartmill-55523-Which-dow-jones-stocks-are-moving-on-Tuesday)  
  <sub>ChartMill, 20 hours ago</sub>  
  Let's have a look at the top dow jones gainers and losers one hour before the close of the markets of today's session.
- [Is Caterpillar Inc (CAT) Overvalued After 0.8% Rally? GF Value S](https://www.gurufocus.com/news/9102456/is-caterpillar-inc-cat-overvalued-after-08-rally-gf-value-says-overvalued)  
  <sub>GuruFocus, 15 hours ago</sub>  
  On September 29, 2026, Caterpillar Inc (CAT) shares rose 0.8% to $826.64, staying well within its 52-week range of $470.24 to $1073.46. The stock has shown...
- [Caterpillar (NYSE:CAT) Stock: Data Center Power Demand Lifts an Equipment Giant](https://kalkine.ca/news/industrials/caterpillar-nysecat-stock-data-center-power-demand-lifts-an-equipment-giant)  
  <sub>kalkine.ca, 20 hours ago</sub>  
  Caterpillar (NYSE:CAT) Stock: Data Center Power Demand Lifts an Equipment Giant.
- [Advanced AI-Powered Crypto Investment Research Platform](https://sosovalue.com/stocks/cat)  
  <sub>SoSoValue, 19 hours ago</sub>  
  Caterpillar's Power Generation Business Is Nearly as Big as Its Construction Segment. Here's What That Shift Means for the Stock's Multiple. Aug 29, 2026.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>Price and chart</b> — score n/a</summary>

```text
Last close 815.60 (bar of 2026-09-30), from 502 daily bars
Trend: vs 20d SMA 807.57 (+1.0%), 50d 825.79 (-1.2%), 200d 792.70 (+2.9%); 50d above 200d
Momentum: RSI(14) 49.8 | MACD -2.497 vs signal -6.889 (histogram 4.392)
Returns: 1d -1.3% | 5d +0.4% | 1m +2.3% | 3m -17.7%
52-week range: 477.15 - 1,064.90 (now 57.6% of the way up)
Volatility: ATR(14) 21.80 (2.7% of price) | annualised 20d 24.5%
Volume: 0.16x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score n/a</summary>

```text
Sector: Industrials / Farm & Heavy Construction Machinery | market cap 374.91B
Valuation: trailing P/E 35.11 | forward P/E 25.19 | P/B 19.33 | PEG 1.42
Profitability: profit margin 14.5% | operating margin 22.2% | ROE 57.0%
Growth (YoY): revenue +24.0% | earnings +68.2%
Balance sheet: debt/equity 232.8% | free cash flow 5.05B
Risk: beta 1.59 | short interest 2.0% of float
Next earnings: 2026-10-29
```

</details>

<details><summary><b>What this fund holds</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>Does this company beat its own forecasts</b> — score n/a</summary>

```text
Earnings record, last 4 quarters: 4 beats
  2026-06-30 beat by 31% | 2026-03-31 beat by 19% | 2025-12-31 beat by 9% | 2025-09-30 beat by 8%
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
Consensus: buy (mean 2.07 on a 1=strong buy to 5=strong sell scale, 26 analysts)
Ratings: 1 strong buy, 14 buy, 11 hold, 1 sell, 1 strong sell
Price target: mean 975.61 (+19.6% vs last close), range 575.00 - 1,225.00
Recent rating changes:
  - 2024-10-14 JP Morgan: main, Overweight -> Overweight
  - 2024-10-14 Morgan Stanley: down, Equal-Weight -> Underweight
  - 2024-10-09 Citigroup: main, Buy -> Buy
  - 2024-10-09 Truist Securities: main, Buy -> Buy
  - 2024-09-30 B of A Securities: main, Buy -> Buy
  - 2024-08-19 Evercore ISI Group: main, In-Line -> In-Line
Institutional ownership: 73.5%
Largest holders: Blackrock Inc. (8.3%), State Street Corporation (7.5%), Vanguard Capital Management LLC (6.5%), State Farm Mutual Automobile Insurance Co (3.2%), Vanguard Portfolio Management LLC (2.6%)
```

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>Buying and selling by company insiders</b> — score n/a</summary>

```text
Last 180 days: bought 169,246 shares in 20 transaction(s) | sold 128,174 shares in 10
Net: +41,072 shares (+4.2% of insider holdings) | insiders hold 1,011,284 shares
Distinct insiders: 1 buying, 8 selling
Open-market purchases — insiders spending their own money:
  - 2026-05-04 MACLENNAN DAVID W (Director): 250 shares, 219.21K
Sales — weak evidence on their own; often scheduled 10b5-1 plans, tax on vesting, or diversification:
  - 2026-08-28 CREED JOSEPH E (Chief Executive Officer): 32,401 shares, 26.21M
  - 2026-05-14 JOHNSON DENISE C. (Officer): 12,605 shares, 11.44M
  - 2026-05-13 JOHNSON DENISE C. (Officer): 6,196 shares, 5.64M
  - 2026-05-13 SCHAUPP WILLIAM E (Officer): 360 shares, 326.16K
(19 grant/option/gift transaction(s) excluded — compensation, not a view on the price)
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

_No news found for this one today._

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>Price and chart</b> — score n/a</summary>

```text
Last close 22.29 (bar of 2026-09-30), from 502 daily bars
Trend: vs 20d SMA 22.81 (-2.3%), 50d 23.16 (-3.8%), 200d 27.20 (-18.0%); 50d below 200d
Momentum: RSI(14) 42.9 | MACD -0.178 vs signal -0.165 (histogram -0.013)
Returns: 1d -1.5% | 5d -2.2% | 1m -1.8% | 3m -12.8%
52-week range: 21.84 - 37.18 (now 2.9% of the way up)
Volatility: ATR(14) 0.52 (2.3% of price) | annualised 20d 36.1%
Volume: 0.09x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score n/a</summary>

```text
Sector: Financial Services / Banks - Regional | market cap 114.56B
Valuation: trailing P/E 15.59 | forward P/E 16.02 | P/B 9.03 | PEG n/a
Profitability: profit margin 26.8% | operating margin 33.3% | ROE 13.8%
Growth (YoY): revenue +16.6% | earnings +18.1%
Balance sheet: debt/equity n/a | free cash flow n/a
Risk: beta 0.40 | short interest 0.7% of float
Next earnings: 2026-10-17
```

</details>

<details><summary><b>What this fund holds</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>Does this company beat its own forecasts</b> — score n/a</summary>

```text
Earnings record, last 4 quarters: 2 beats, 2 in line
  2026-06-30 in line | 2026-03-31 in line | 2025-12-31 beat by 61% | 2025-09-30 beat by 10%
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
Price target: mean 30.52 (+36.9% vs last close), range 26.10 - 35.00
Recent rating changes:
  - 2024-07-22 JP Morgan: down, Overweight -> Neutral
  - 2019-09-09 Bernstein: down, Outperform -> Market Perform
  - 2019-06-11 Nomura: down, Buy -> Neutral
  - 2017-03-21 Morgan Stanley: down, Overweight -> Equal-Weight
  - 2016-09-14 Goldman Sachs: main, ? -> Buy
  - 2015-03-11 Societe Generale: init, ? -> Buy
Institutional ownership: 13.6%
Largest holders: Morgan Stanley (1.0%), Royal Bank of Canada (0.8%), Schroder Investment Management Group (0.4%), JPMORGAN CHASE & CO (0.4%), Bank of America Corporation (0.3%)
```

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>Buying and selling by company insiders</b> — score n/a</summary>

```text
Last 180 days: bought 0 shares in 0 transaction(s) | sold n/a shares in 0
Net: +0 shares | insiders hold 6,928,096 shares
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

- [JPMorgan Chase & Co. $JPM Stock Holdings Boosted by Saudi Central Bank](https://www.marketbeat.com/instant-alerts/filing-jpmorgan-chase-co-jpm-stock-holdings-boosted-by-saudi-central-bank-2026-09-30/)  
  <sub>MarketBeat, 7 hours ago</sub>  
  Saudi Central Bank raised its stake in shares of JPMorgan Chase & Co. (NYSE:JPM - Free Report) by 86.9% in the 2nd quarter, according to the company in its...
- [JPMorgan Chase (NYSE:JPM) Stock: Trading and Dealmaking Strength Fund a Higher Quarterly Dividend](https://kalkine.ca/news/financial/jpmorgan-chase-nysejpm-stock-trading-and-dealmaking-strength-fund-a-higher-quarterly-dividend)  
  <sub>kalkine.ca, 19 hours ago</sub>  
  JPMorgan Chase (NYSE:JPM) Stock: Trading and Dealmaking Strength Fund a Higher Quarterly Dividend.
- [JPMorgan Chase & Co (JPM) Shares Fall 0.5% -- What GF Score of 8](https://www.gurufocus.com/news/9102442/jpmorgan-chase-co-jpm-shares-fall-05-what-gf-score-of-85-tells-investors)  
  <sub>GuruFocus, 15 hours ago</sub>  
  On September 29, 2026, JPMorgan Chase & Co (JPM) shares fell 0.5% to a current price of $334.98, continuing a downtrend seen over the past month,...
- [JPGR ETF Holdings List — HAN:JPGR](https://www.tradingview.com/symbols/HAN-JPGR/holdings/)  
  <sub>TradingView, 20 hours ago</sub>  
  JPMorgan ETFS Ireland ICAV - JPM Active US Growth UCITS ETF. JPGR Hannover Stock Exchange. JPGR Hannover Stock Exchange. JPGR Hannover Stock Exchange.
- [Banks And Financial Stocks: Latest News And Analysis](https://www.investors.com/news/banks-and-financial-stocks-news-and-analysis-bofa-wellsfargo-jpmorgan-goldmansachs/)  
  <sub>Investor's Business Daily, 23 hours ago</sub>  
  Bookmark this page for news and stock analysis of companies like JPMorgan Chase (JPM), Bank of America (BAC), Wells Fargo (WFC), Goldman Sachs (GS) and more...
- [JPM Oct 2026 382.500 put (JPM261002P00382500) Stock Price, News, Quote & History](https://ca.finance.yahoo.com/quote/JPM261002P00382500/)  
  <sub>Yahoo! Finance Canada, 17 hours ago</sub>  
  Find the latest JPM Oct 2026 382.500 put (JPM261002P00382500) stock quote, history, news and other vital information to help you with your stock trading and...
- [11,737 Shares in JPMorgan Chase & Co. $JPM Purchased by Compass Financial Management LLC](https://www.marketbeat.com/instant-alerts/filing-11737-shares-in-jpmorgan-chase-co-jpm-purchased-by-compass-financial-management-llc-2026-09-30/)  
  <sub>MarketBeat, 8 hours ago</sub>  
  Compass Financial Management LLC acquired a new stake in shares of JPMorgan Chase & Co. (NYSE:JPM) during the 2nd quarter, according to the company in its...
- [JPM vs. GS: The Dividend Raiser That Won’t Flinch When Markets Crack](https://247wallst.com/investing/2026/09/29/jpm-vs-gs-the-dividend-raiser-that-wont-flinch-when-markets-crack/)  
  <sub>24/7 Wall St., 22 hours ago</sub>  
  JPMorgan built its reputation as the safe megabank, yet one crisis revealed a dividend surprise that upends the conventional wisdom about which Wall Street...
- [CNMD Stock Hits Highest Level In Over Four Months – Why JPMorgan Believes Firm Would Be Highly Attractive To ‘Financial Acquirers’](https://stocktwits.com/news-articles/markets/equity/cnmd-stock-hits-highest-level-in-over-four-months-why-jp-morgan-believes-firm-would-be-highly-attractive-to-financial-acquirers-1/cZmzvNGR7Yi)  
  <sub>Stocktwits, 13 hours ago</sub>  
  Shares of Conmed (CNMD) attracted significant investor attention on Monday after analysts commented on the reported buyout interest received by the medical...
- [Bank of America (NYSE:BAC) Stock: Sharply Higher Trading and Advisory Income Fund a Bigger Payout](https://kalkine.ca/news/financial/bank-of-america-nysebac-stock-sharply-higher-trading-and-advisory-income-fund-a-bigger-payout)  
  <sub>kalkine.ca, 20 hours ago</sub>  
  You are reading a free article with opinions that may differ from the recommendation given by Kalkine in its paid research reports.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>Price and chart</b> — score n/a</summary>

```text
Last close 334.40 (bar of 2026-09-30), from 502 daily bars
Trend: vs 20d SMA 348.13 (-3.9%), 50d 352.96 (-5.3%), 200d 321.65 (+4.0%); 50d above 200d
Momentum: RSI(14) 34.2 | MACD -4.805 vs signal -3.039 (histogram -1.765)
Returns: 1d -0.2% | 5d -0.9% | 1m -6.1% | 3m +0.1%
52-week range: 282.84 - 365.18 (now 62.6% of the way up)
Volatility: ATR(14) 6.28 (1.9% of price) | annualised 20d 19.1%
Volume: 0.10x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score n/a</summary>

```text
Sector: Financial Services / Banks - Diversified | market cap 888.90B
Valuation: trailing P/E 14.32 | forward P/E 13.35 | P/B 2.51 | PEG 1.57
Profitability: profit margin 34.9% | operating margin 50.4% | ROE 17.8%
Growth (YoY): revenue +30.4% | earnings +46.9%
Balance sheet: debt/equity n/a | free cash flow n/a
Risk: beta 0.97 | short interest 0.9% of float
Next earnings: 2026-10-13
```

</details>

<details><summary><b>What this fund holds</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>Does this company beat its own forecasts</b> — score n/a</summary>

```text
Earnings record, last 4 quarters: 4 beats
  2026-06-30 beat by 4% | 2026-03-31 beat by 8% | 2025-12-31 beat by 3% | 2025-09-30 beat by 4%
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
Consensus: buy (mean 2.08 on a 1=strong buy to 5=strong sell scale, 21 analysts)
Ratings: 4 strong buy, 9 buy, 11 hold, 0 sell, 0 strong sell
Price target: mean 375.81 (+12.4% vs last close), range 305.00 - 436.00
Recent rating changes:
  - 2026-09-28 HSBC: main, Hold -> Hold
  - 2026-08-14 Wells Fargo: main, Overweight -> Overweight
  - 2026-08-03 UBS: main, Buy -> Buy
  - 2026-07-20 Citigroup: main, Neutral -> Neutral
  - 2026-07-17 Evercore ISI Group: main, Outperform -> Outperform
  - 2026-07-16 B of A Securities: main, Buy -> Buy
Institutional ownership: 75.7%
Largest holders: Blackrock Inc. (7.8%), Vanguard Capital Management LLC (6.1%), State Street Corporation (4.7%), Bank of America Corporation (2.6%), Morgan Stanley (2.5%)
```

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>Buying and selling by company insiders</b> — score n/a</summary>

```text
Last 180 days: bought 137,226 shares in 11 transaction(s) | sold 230,236 shares in 19
Net: -93,010 shares (-0.9% of insider holdings) | insiders hold 10,393,508 shares
Distinct insiders: 0 buying, 10 selling
Sales — weak evidence on their own; often scheduled 10b5-1 plans, tax on vesting, or diversification:
  - 2026-09-10 LEOPOLD ROBIN (Officer): 2,500 shares, 882.03K
  - 2026-08-11 LEOPOLD ROBIN (Officer): 2,500 shares, 903.52K
  - 2026-06-22 FRIEDMAN STACEY R. (General Counsel): 5,467 shares, 1.81M
  - 2026-05-20 FRIEDMAN STACEY R. (General Counsel): 5,468 shares, 1.64M
(7 grant/option/gift transaction(s) excluded — compensation, not a view on the price)
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

- [4 Stocks That Could Split Next—and Why Investors Are Watching](https://www.marketbeat.com/articles/4-stocks-that-could-split-nextand-why-investors-are-watching/)  
  <sub>MarketBeat, 1 hour ago</sub>  
  AutoZone, Eli Lilly, Meta Platforms, and Costco all trade at high share prices, making them candidates for stock splits as analysts raise price targets and...
- [ETFs Are Buying Eli Lilly (LLY) on Monday](https://www.gurufocus.com/news/9102991/etfs-are-buying-eli-lilly-lly-on-monday)  
  <sub>GuruFocus, 3 hours ago</sub>  
  DCOR led ETF activity on Monday, adding $474.0 million of Eli Lilly (LLY) shares. In total, ETFs were net buyers of $694.1 million of the stock,...
- [Lilly Stock Drops Lowwer Foundayo Claims an Oral Edge](https://finance.yahoo.com/markets/stocks/articles/lilly-stock-drops-lowwer-foundayo-161006238.html)  
  <sub>Yahoo Finance, 23 hours ago</sub>  
  This article first appeared on GuruFocus. Eli Lilly (NYSE:LLY), the obesity and diabetes drugmaker, slipped about 0.3% to $1,181.45 at 10.15 EST time in...
- [Opinion: Eli Lilly Stock Is a No-Brainer Pick to Buy on the Dip](https://www.fool.com/investing/2026/09/29/opinion-eli-lilly-stock-is-a-no-brainer-pick-to-bu/)  
  <sub>The Motley Fool, 13 hours ago</sub>  
  There's no rule that says a leading pharma stock can't go down. On that note, shares of Eli Lilly (LLY -0.01%) are still down by 7% from their recent high...
- [Is Eli Lilly Stock a Good Fit For Your Portfolio Risk?](https://www.trefis.com/stock/lly/articles/616950/is-eli-lilly-stock-a-good-fit-for-your-portfolio-risk/2026-09-29)  
  <sub>Trefis, 20 hours ago</sub>  
  You may own Eli Lilly (LLY), a drugmaker worth about $1.05 trillion, beside funds that already track the S&P 500. A single stock can become a big part of...
- [What's Behind Eli Lilly's (NYSE:LLY) Big Moment in Healthcare Stocks Today?](https://kalkinemedia.com/us/stocks/healthcare/whats-behind-eli-lillys-nyselly-big-moment-in-healthcare-stocks-today)  
  <sub>Kalkine Media, 13 minutes ago</sub>  
  Eli Lilly (NYSE:LLY) is in focus as fresh retatrutide data extends the obesity-and-diabetes pipeline debate. See the September 30 setup, key risks,...
- [ATAI Stock Slips After Blockbuster Week: Cathie Wood Calls $3.8B Lilly Deal ‘Well-Deserved’ Return For Shareholders](https://stocktwits.com/news-articles/markets/equity/atai-cathie-wood-lilly-deal-well-deserved-return-shareholders/cZZLrZTR7MA)  
  <sub>Stocktwits, 11 hours ago</sub>  
  ARKG sold 1.12 million ATAI shares last week but still held 3.19 million shares as of Friday.
- [Prediction: Eli Lilly’s Next Growth Wave Could Surprise Investors](https://247wallst.com/investing/2026/09/29/prediction-eli-lillys-next-growth-wave-could-surprise-investors/)  
  <sub>24/7 Wall St., 21 hours ago</sub>  
  Eli Lilly (LLY) earns a BUY rating with a $1,401 price target, implying ~20% upside, backed by 90% model confidence and 47% revenue growth.
- [Eli Lilly (LLY) Wins FDA Breakthrough Tag For Pancreatic Cancer Drug](https://simplywall.st/stocks/us/pharmaceuticals-biotech/nyse-lly/eli-lilly/news/eli-lilly-lly-wins-fda-breakthrough-tag-for-pancreatic-cance)  
  <sub>Simply Wall St, 14 hours ago</sub>  
  Eli Lilly (NYSE: LLY) received FDA Breakthrough Therapy designation for olomorasib in advanced pancreatic cancer, according to a recent company update.
- [Competition Fears Are Overblown, and Eli Lilly’s Growth Engine Remains Strong](https://nai500.com/blog/2026/09/competition-fears-are-overblown-and-eli-lillys-growth-engine-remains-strong/)  
  <sub>NAI500, 7 hours ago</sub>  
  Although Eli Lilly's (LLY) stock price has pulled back from its recent high, its core growth logic has not changed. Tirzepatide continues to gain volume…

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>Price and chart</b> — score n/a</summary>

```text
Last close 1,185.70 (bar of 2026-09-30), from 502 daily bars
Trend: vs 20d SMA 1,154.00 (+2.7%), 50d 1,178.49 (+0.6%), 200d 1,072.94 (+10.5%); 50d above 200d
Momentum: RSI(14) 56.3 | MACD 2.109 vs signal -4.076 (histogram 6.185)
Returns: 1d +0.1% | 5d +3.0% | 1m +2.5% | 3m -0.5%
52-week range: 763.00 - 1,280.34 (now 81.7% of the way up)
Volatility: ATR(14) 31.77 (2.7% of price) | annualised 20d 17.4%
Volume: 0.35x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score n/a</summary>

```text
Sector: Healthcare / Drug Manufacturers - General | market cap 1.06T
Valuation: trailing P/E 39.88 | forward P/E 25.04 | P/B 31.20 | PEG 1.14
Profitability: profit margin 33.5% | operating margin 54.2% | ROE 102.3%
Growth (YoY): revenue +47.7% | earnings +26.2%
Balance sheet: debt/equity 162.1% | free cash flow 11.07B
Risk: beta 0.50 | short interest 0.8% of float
Next earnings: 2026-10-29
```

</details>

<details><summary><b>What this fund holds</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>Does this company beat its own forecasts</b> — score n/a</summary>

```text
Earnings record, last 4 quarters: 4 beats
  2026-06-30 beat by 38% | 2026-03-31 beat by 27% | 2025-12-31 beat by 12% | 2025-09-30 beat by 22%
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
Consensus: buy (mean 1.63 on a 1=strong buy to 5=strong sell scale, 29 analysts)
Ratings: 6 strong buy, 19 buy, 3 hold, 1 sell, 1 strong sell
Price target: mean 1,328.83 (+12.1% vs last close), range 930.00 - 1,600.00
Recent rating changes:
  - 2026-09-28 JP Morgan: main, Overweight -> Overweight
  - 2026-09-22 TD Cowen: reit, Buy -> Buy
  - 2026-09-18 Guggenheim: main, Buy -> Buy
  - 2026-09-10 HSBC: main, Reduce -> Reduce
  - 2026-08-07 Truist Securities: main, Buy -> Buy
  - 2026-08-06 Wells Fargo: main, Overweight -> Overweight
Institutional ownership: 85.3%
Largest holders: Lilly Endowment, Inc (9.6%), Blackrock Inc. (7.2%), Vanguard Capital Management LLC (5.7%), PNC Financial Services Group, Inc. (5.5%), State Street Corporation (3.9%)
```

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>Buying and selling by company insiders</b> — score n/a</summary>

```text
Last 180 days: bought 1,479 shares in 28 transaction(s) | sold 308,215 shares in 8
Net: -306,736 shares (-18.0% of insider holdings) | insiders hold 1,399,430 shares
Distinct insiders: 0 buying, 5 selling
Sales — weak evidence on their own; often scheduled 10b5-1 plans, tax on vesting, or diversification:
  - 2026-08-17 JONSSON PATRIK (Officer): 6,500 shares, 7.64M
  - 2026-08-10 ZAKROWSKI DONALD A (Officer): 2,000 shares, 2.37M
  - 2026-08-07 HAKIM ANAT (General Counsel): 5,000 shares, 5.95M
  - 2026-06-10 YUFFA ILYA (Officer): 2,500 shares, 2.88M
(28 grant/option/gift transaction(s) excluded — compensation, not a view on the price)
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

- [Has MSFT Stock Run Out Of Steam?](https://www.trefis.com/stock/msft/articles/616915/has-msft-stock-run-out-of-steam/2026-09-29)  
  <sub>Trefis, 18 hours ago</sub>  
  Just see what has actually been driving Microsoft stock. Over three years, revenue growth and wider margins did the heavy lifting while the P/E multiple...
- [Microsoft Stock: The Xbox Segment Revamp (NASDAQ:MSFT)](https://seekingalpha.com/article/4950992-microsoft-the-xbox-segment-revamp)  
  <sub>Seeking Alpha, 1 hour ago</sub>  
  Microsoft's Xbox is set to rebound after FY2026 via restructuring, Game Pass growth, and exclusive releases ahead of the Helix launch. See why MSFT stock is...
- [MSFT Tokenized Shares Eye Resistance; Stifel Target $575](https://www.tradingpedia.com/2026/09/30/msft-tokenized-shares-eye-resistance-stifel-target-575/)  
  <sub>TradingPedia, 2 hours ago</sub>  
  Sandra Leggero. Sandra Leggero has a background in financial markets, having spent more than 9 years in commodities trading for several European and Asian...
- [Microsoft Stock Has Grown Roughly 14-Fold Since Satya Nadella Became CEO in 2014, a 23% Annual Growth Rate That Ended 14 Years of Negative Growth. Can That Pace Continue Under Heavy AI Spending?](https://www.fool.com/investing/2026/09/30/microsoft-stock-grown-satya-nadella-ai-spend/)  
  <sub>The Motley Fool, 5 hours ago</sub>  
  Bill Gates handed over the reins of Microsoft (MSFT +1.50%) to Steve Ballmer in early 2000. Gates had built the software business into the world's largest...
- [Microsoft To Rally Around 20%? Here Are 10 Top Analyst Forecasts For Wednesday](https://www.benzinga.com/analyst-stock-ratings/price-target/26/09/62076005/microsoft-to-rally-around-20-here-are-10-top-analyst-forecasts-for-wednesday)  
  <sub>Benzinga, 2 hours ago</sub>  
  Analysts revised targets and ratings for KMX, ARX, JKHY, MRNA, GO, HNGE, AYTU and MSFT, with mixed upgrades, downgrades and reiterations.
- [Nasdaq, S&P 500 Futures Rise On Hormuz Deal Hopes, ADP Jobs Data Eyed: Why AMD, SPCX, ASTS, MSFT, PLTR, RKLB, SLV Are In Focus](https://stocktwits.com/news-articles/markets/equity/nasdaq-dow-sp500-futures-hormuz-deal-hopes-adp-jobs-data-why-amd-spcx-asts-msft-pltr-rklb-slv-are-in-focus/cZo4lgJRJI3)  
  <sub>Stocktwits, 13 hours ago</sub>  
  Retail sentiment on Stocktwits has improved, turning 'neutral' on SPY, and 'bullish' on QQQ.
- [A Look at Microsoft Corp (MSFT) After 0.1% Decline -- GF Value $588.50 vs Price $508.96](https://www.gurufocus.com/news/9102426/a-look-at-microsoft-corp-msft-after-01-decline-gf-value-58850-vs-price-50896)  
  <sub>GuruFocus, 15 hours ago</sub>  
  On September 29, 2026, Microsoft Corp (MSFT) shares fell 0.1% to a current price of $508.96. Over the past 52 weeks, the stock has ranged from a low of...
- [Microsoft in focus as Piper Sandler sees uplift in Copilot, M365 (MSFT:NASDAQ)](https://seekingalpha.com/news/4648477-microsoft-in-focus-as-piper-sandler-sees-uplift-in-copilot-m365)  
  <sub>Seeking Alpha, 2 hours ago</sub>  
  Microsoft stock in focus: Piper Sandler sees Copilot revenue upside and M365 E7 rollout boosting ARR; learn the $2B impact per 10% upgrade—read now.
- [Could Microsoft (NASDAQ:MSFT) Be the Next Big AI Stocks Story?](https://kalkinemedia.com/us/stocks/artificial-intelligence/could-microsoft-nasdaqmsft-be-the-next-big-ai-stocks-story)  
  <sub>Kalkine Media, 11 minutes ago</sub>  
  Microsoft (NASDAQ:MSFT) is in focus as AI optimism and a voluntary industry self-regulation accord keep hyperscaler strategy in focus. See the September 30...
- [EUROPEAN OPEN: UCG IM faces German conditions over CBK GY control; MT NA considers BRL 5bln Pecem steel mill expansion; LUND DC mulls Xeris Biopharma deal; GRG LN raises profit view; TOM2 NA expands MSFT collab](https://www.newsquawk.com/headlines/european-open-ucg-im-faces-german-conditions-over-cbk-gy-control-mt-na-considers-brl-5bln-pecem-steel-mill-expansion-lund-dc-mulls-xeris-biopharma-deal-grg-ln-raises-profit-view-tom2-na-expands-msft-collab)  
  <sub>Newsquawk, 7 hours ago</sub>  
  Open the platform and use it. The whole workspace is free to try, with no signup and no card. When you want the headlines arriving live instead of on a...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>Price and chart</b> — score n/a</summary>

```text
Last close 517.16 (bar of 2026-09-30), from 502 daily bars
Trend: vs 20d SMA 500.72 (+3.3%), 50d 482.64 (+7.2%), 200d 432.47 (+19.6%); 50d above 200d
Momentum: RSI(14) 62.2 | MACD 7.633 vs signal 7.408 (histogram 0.225)
Returns: 1d +1.6% | 5d +3.3% | 1m +1.9% | 3m +34.6%
52-week range: 352.83 - 542.07 (now 86.8% of the way up)
Volatility: ATR(14) 11.81 (2.3% of price) | annualised 20d 24.8%
Volume: 0.28x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score n/a</summary>

```text
Sector: Technology / Software - Infrastructure | market cap 3.84T
Valuation: trailing P/E 28.78 | forward P/E 21.88 | P/B 8.68 | PEG 1.62
Profitability: profit margin 40.3% | operating margin 45.1% | ROE 34.0%
Growth (YoY): revenue +17.7% | earnings +31.7%
Balance sheet: debt/equity 29.1% | free cash flow 16.55B
Risk: beta 1.11 | short interest 0.9% of float
Next earnings: 2026-10-28
```

</details>

<details><summary><b>What this fund holds</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>Does this company beat its own forecasts</b> — score n/a</summary>

```text
Earnings record, last 4 quarters: 4 beats
  2026-06-30 beat by 10% | 2026-03-31 beat by 3% | 2025-12-31 beat by 3% | 2025-09-30 beat by 10%
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
Consensus: strong_buy (mean 1.33 on a 1=strong buy to 5=strong sell scale, 52 analysts)
Ratings: 14 strong buy, 39 buy, 2 hold, 0 sell, 0 strong sell
Price target: mean 578.42 (+11.8% vs last close), range 440.00 - 870.00
Recent rating changes:
  - 2026-09-30 Piper Sandler: main, Overweight -> Overweight
  - 2026-09-23 Stifel: up, Hold -> Buy
  - 2026-09-22 Oppenheimer: main, Outperform -> Outperform
  - 2026-09-21 Cantor Fitzgerald: main, Overweight -> Overweight
  - 2026-09-15 Citizens: reit, Market Outperform -> Market Outperform
  - 2026-09-04 Stifel: main, Hold -> Hold
Institutional ownership: 75.8%
Largest holders: Blackrock Inc. (8.2%), Vanguard Capital Management LLC (6.5%), State Street Corporation (4.2%), Geode Capital Management, LLC (2.5%), FMR, LLC (2.5%)
```

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>Buying and selling by company insiders</b> — score n/a</summary>

```text
Last 180 days: bought 513,644 shares in 16 transaction(s) | sold 242,344 shares in 9
Net: +271,300 shares (+4.2% of insider holdings) | insiders hold 6,831,502 shares
Distinct insiders: 0 buying, 5 selling
Sales — weak evidence on their own; often scheduled 10b5-1 plans, tax on vesting, or diversification:
  - 2026-09-14 HOOD AMY E (Chief Financial Officer): 41,674 shares, 20.76M
  - 2026-09-01 NADELLA SATYA (Chief Executive Officer): 86,525 shares, 43.39M
  - 2026-08-05 ALTHOFF JUDSON (Officer): 10,000 shares, 4.88M
  - 2026-08-04 NUMOTO TAKESHI (Officer): 4,810 shares, 2.39M
(15 grant/option/gift transaction(s) excluded — compensation, not a view on the price)
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
  <sub>Yahoo Finance UK, 9 hours ago</sub>  
  519,237.16% · Previous close 228.86 · Open 230.99 · Bid 219.34 x 100 · Ask 229.33 x 500 · Day's range 227.02 - 232.82 · 52-week range 164.27 - 236.54 · Volume...
- [Price Prediction: 5 Years From Now, This Could Be Nvidia Stock’s Price](https://247wallst.com/investing/2026/09/30/price-prediction-5-years-from-now-this-could-be-nvidia-stocks-price/)  
  <sub>24/7 Wall St., 12 minutes ago</sub>  
  Nvidia just doubled its revenue while its stock barely moved, and Wall Street is split on what comes next. The math behind a $500 price target by 2031 is...
- [NVDA Stock Climbs Over 1% — Nvidia Says Its AI ‘Roadmap Is Intact’ After Report Of Kyber Rack Delay](https://stocktwits.com/news-articles/markets/equity/nvda-stock-rises-after-nvidia-says-ai-roadmap-intact-despite-kyber-delay-report/cZm1ke5R7lr)  
  <sub>Stocktwits, 13 hours ago</sub>  
  NVDA Stock Climbs Over 1% — Nvidia Says Its AI 'Roadmap Is Intact' After Report Of Kyber Rack Delay. The chipmaker said its product roadmap remains on track...
- [NVDA Stock Eyes Third Straight Monthly Gain: Nvidia Adds Data Center Digital Twin Deal](https://finance.yahoo.com/markets/stocks/articles/nvda-stock-eyes-third-straight-122645287.html)  
  <sub>Yahoo Finance, 2 hours ago</sub>  
  Nvidia selected Jacobs to deploy its Omniverse-based digital twin platform at a large-scale U.S. AI research and development facility.
- [NVIDIA (NVDA) Put Options Trade Signals Market Caution Amid $227 Share Price](https://www.gurufocus.com/news/9103331/nvidia-nvda-put-options-trade-signals-market-caution-amid-227-share-price)  
  <sub>GuruFocus, 1 hour ago</sub>  
  On September 30, 2026, an intriguing options transaction involving NVIDIA Corp (NASDAQ: NVDA) caught market attention as a buyer accepted $14.15 for 4629...
- [NVIDIA Corporation $NVDA Shares Sold by Pursue Wealth Partners LLC](https://www.marketbeat.com/instant-alerts/filing-nvidia-corporation-nvda-shares-sold-by-pursue-wealth-partners-llc-2026-09-30/)  
  <sub>MarketBeat, 7 hours ago</sub>  
  Pursue Wealth Partners LLC lowered its stake in NVIDIA Corporation (NASDAQ:NVDA - Free Report) by 20.5% in the second quarter, according to its most recent...
- [NVIDIA Corporation $NVDA Shares Sold by Covestor Ltd](https://www.marketbeat.com/instant-alerts/filing-nvidia-corporation-nvda-shares-sold-by-covestor-ltd-2026-09-30/)  
  <sub>MarketBeat, 8 hours ago</sub>  
  Covestor Ltd lessened its position in shares of NVIDIA Corporation (NASDAQ:NVDA - Free Report) by 21.5% during the 2nd quarter, according to the company in...
- [MU, SKHY, NVDA, AMD, INTC Extend Rally Premarket, But Chip Stocks Still On Track For Worst Month Since 2002](https://stocktwits.com/news-articles/markets/equity/mu-skhy-nvda-amd-intc-extend-rally-premarket-but-chip-stocks-still-on-track-for-worst-month-since-2002/cZN4TMURJ2D)  
  <sub>Stocktwits, 13 hours ago</sub>  
  Morningstar maintained its $850 fair value estimate on Meta, implying a 58% upside from current levels, and said the market's reaction to the company's latest...
- [NVIDIA (NVDA) Approves Record Buyback, Is The Stock Still Undervalued?](https://finance.yahoo.com/markets/stocks/articles/nvidia-nvda-approves-record-buyback-111241523.html)  
  <sub>Yahoo Finance, 3 hours ago</sub>  
  NVIDIA (NVDA) just signed off on a record US$150b expansion of its share repurchase plan, lifting total buyback authorization to US$235b and putting capital...
- [NVIDIA Corporation $NVDA Shares Sold by Rice Hall James & Associates LLC](https://www.marketbeat.com/instant-alerts/filing-nvidia-corporation-nvda-shares-sold-by-rice-hall-james-associates-llc-2026-09-30/)  
  <sub>MarketBeat, 7 hours ago</sub>  
  Rice Hall James & Associates LLC cut its holdings in NVIDIA Corporation (NASDAQ:NVDA - Free Report) by 27.9% in the 2nd quarter, according to the company in...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>Price and chart</b> — score n/a</summary>

```text
Last close 230.60 (bar of 2026-09-30), from 502 daily bars
Trend: vs 20d SMA 223.30 (+3.3%), 50d 217.44 (+6.1%), 200d 200.16 (+15.2%); 50d above 200d
Momentum: RSI(14) 59.7 | MACD 2.980 vs signal 2.337 (histogram 0.643)
Returns: 1d +1.5% | 5d +2.3% | 1m +4.4% | 3m +16.7%
52-week range: 165.17 - 235.74 (now 92.7% of the way up)
Volatility: ATR(14) 5.96 (2.6% of price) | annualised 20d 27.5%
Volume: 0.27x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score n/a</summary>

```text
Sector: Technology / Semiconductors | market cap 5.57T
Valuation: trailing P/E 29.16 | forward P/E 14.71 | P/B 24.32 | PEG 0.48
Profitability: profit margin 63.7% | operating margin 66.2% | ROE 117.2%
Growth (YoY): revenue +105.9% | earnings +127.8%
Balance sheet: debt/equity 17.0% | free cash flow 41.81B
Risk: beta 2.22 | short interest 1.3% of float
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
Consensus: strong_buy (mean 1.30 on a 1=strong buy to 5=strong sell scale, 59 analysts)
Ratings: 10 strong buy, 48 buy, 2 hold, 1 sell, 0 strong sell
Price target: mean 327.70 (+42.1% vs last close), range 180.00 - 515.00
Recent rating changes:
  - 2026-09-29 Rosenblatt: main, Buy -> Buy
  - 2026-09-10 Piper Sandler: init, ? -> Overweight
  - 2026-09-04 Rosenblatt: main, Buy -> Buy
  - 2026-09-04 Needham: reit, Buy -> Buy
  - 2026-08-27 Citigroup: main, Buy -> Buy
  - 2026-08-27 Mizuho: main, Outperform -> Outperform
Institutional ownership: 71.4%
Largest holders: Blackrock Inc. (8.1%), Vanguard Capital Management LLC (6.4%), FMR, LLC (4.3%), State Street Corporation (4.2%), Geode Capital Management, LLC (2.5%)
```

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>Buying and selling by company insiders</b> — score n/a</summary>

```text
Last 180 days: bought 2,452,825 shares in 17 transaction(s) | sold 6,198,325 shares in 9
Net: -3,745,500 shares (-0.4% of insider holdings) | insiders hold 965,687,040 shares
Distinct insiders: 0 buying, 4 selling
Sales — weak evidence on their own; often scheduled 10b5-1 plans, tax on vesting, or diversification:
  - 2026-09-21 TETER TIMOTHY S (General Counsel): 30,460 shares, 6.79M
  - 2026-09-18 STEVENS MARK A (Director): 1,366,000 shares, 300.15M
  - 2026-09-04 STEVENS MARK A (Director): 1,022,239 shares, 235.64M
  - 2026-09-02 STEVENS MARK A (Director): 1,848,501 shares, 410.84M
(17 grant/option/gift transaction(s) excluded — compensation, not a view on the price)
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

- [If You Love Speculating, You Should Keep a Close Eye on Novo Nordisk Stock](https://www.barchart.com/story/news/4881736/if-you-love-speculating-you-should-keep-a-close-eye-on-novo-nordisk-stock)  
  <sub>Barchart.com, 40 minutes ago</sub>  
  Yes, NVO is a stinker but powerhouse names caught in a bearish wind tend to enjoy transitional swings.
- [An experimental obesity drug changed brain responses to tempting foods and reduced cravings](https://www.stocktitan.net/news/NVO/novo-s-investigational-obesity-and-diabetes-drug-cagri-sema-reduces-02he7u0spps1.html)  
  <sub>Stock Titan, 2 hours ago</sub>  
  Novo Nordisk (NVO) presented new CagriSema data at EASD 2026 showing changes in food-related brain responses and organ fat. A 52-week brain-imaging study in...
- [Novo Nordisk (NVO) Dips More Than Broader Market: What You Should Know](https://sg.finance.yahoo.com/news/novo-nordisk-nvo-dips-more-204504473.html)  
  <sub>Yahoo Finance Singapore, 18 hours ago</sub>  
  Novo Nordisk (NVO) closed at $38.31 in the latest trading session, marking a -1.03% move from the prior day. The stock trailed the S&P 500, which registered...
- [VLO Stock Heads For Best Year Since 1982 — Michael Burry Says It Has Become A ‘Huge Position’](https://stocktwits.com/news-articles/markets/equity/vlo-stock-best-year-1982-michael-burry-huge-position/cZtlx8lRBR0)  
  <sub>Stocktwits, 14 hours ago</sub>  
  Burry recovered his initial investment “and then some” for charity, while retaining a sizable stake that is “deep into house's money.”
- [Novo Nordisk: After A 70+% Drop, It's A Great Investment (NYSE:NVO)](https://seekingalpha.com/article/4950687-novo-nordisk-after-a-70-plus-percent-drop-its-a-great-investment)  
  <sub>Seeking Alpha, 24 hours ago</sub>  
  Novo Nordisk remains a compelling long-term investment despite a 70% share price decline amid GLP-1 competition. Click here to read this NVO stock update.
- [Novo vs. Pfizer: Which Large Drugmaker Offers Better Growth Prospects?](https://www.theglobeandmail.com/investing/markets/stocks/NVO/pressreleases/4859409/novo-vs-pfizer-which-large-drugmaker-offers-better-growth-prospects/)  
  <sub>The Globe and Mail, 23 hours ago</sub>  
  Detailed price information for Novo Nordisk A/S ADR (NVO-N) from The Globe and Mail including charting and trades.
- [Can Novo's Licensing Strategy Build Its Next Wave of Oral Medicines?](https://www.zacks.com/stock/news/2998019/can-novos-licensing-strategy-build-its-next-wave-of-oral-medicines)  
  <sub>Zacks Investment Research, 2 hours ago</sub>  
  NVO's latest Hengrui deal adds a phase I-ready, once-weekly oral GLP-1/GIP candidate, building on deals for oral drug-delivery tech and small-molecule...
- [Prediction: Eli Lilly’s Next Growth Wave Could Surprise Investors](https://247wallst.com/investing/2026/09/29/prediction-eli-lillys-next-growth-wave-could-surprise-investors/)  
  <sub>24/7 Wall St., 21 hours ago</sub>  
  Eli Lilly (LLY) earns a BUY rating with a $1,401 price target, implying ~20% upside, backed by 90% model confidence and 47% revenue growth.
- [Tirzepatide or Wegovy? Novo Nordisk Says Higher Semaglutide Dose Shows Cardiovascular Edge Over Eli Lilly](https://www.benzinga.com/news/health-care/26/09/62058481/tirzepatide-or-wegovy-novo-nordisk-says-higher-semaglutide-dose-shows-cardiovascular-edge-over-eli-lillys-tirzepatide)  
  <sub>Benzinga, 22 hours ago</sub>  
  Novo Nordisk A/S (NYSE:NVO) announced on Tuesday new real-world evidence demonstrating that escalating semaglutide dosage reduces major adverse...
- [BMO reiterates Novo Nordisk stock rating on Hengrui licensing deal By Investing.com](https://za.investing.com/news/stock-market-news/bmo-reiterates-novo-nordisk-stock-rating-on-hengrui-licensing-deal-93CH-4482854)  
  <sub>Investing.com South Africa, 24 hours ago</sub>  
  Investing.com - BMO Capital reiterated a Market Perform rating on Novo Nordisk (NYSE:NVO) with a $47.00 price target following the company's licensing...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>Price and chart</b> — score n/a</summary>

```text
Last close 38.64 (bar of 2026-09-30), from 502 daily bars
Trend: vs 20d SMA 42.11 (-8.2%), 50d 45.13 (-14.4%), 200d 45.78 (-15.6%); 50d below 200d
Momentum: RSI(14) 31.8 | MACD -2.078 vs signal -1.789 (histogram -0.288)
Returns: 1d +0.9% | 5d +1.2% | 1m -14.8% | 3m -20.8%
52-week range: 35.29 - 63.98 (now 11.7% of the way up)
Volatility: ATR(14) 1.15 (3.0% of price) | annualised 20d 40.7%
Volume: 0.68x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score n/a</summary>

```text
Sector: Healthcare / Drug Manufacturers - General | market cap 170.62B
Valuation: trailing P/E 9.68 | forward P/E 11.52 | P/B 5.08 | PEG 4.32
Profitability: profit margin 35.3% | operating margin 42.5% | ROE 59.8%
Growth (YoY): revenue +2.1% | earnings -20.6%
Balance sheet: debt/equity 63.3% | free cash flow 37.67B
Risk: beta 0.34 | short interest 0.8% of float
Next earnings: 2026-11-04
```

</details>

<details><summary><b>What this fund holds</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>Does this company beat its own forecasts</b> — score n/a</summary>

```text
Earnings record, last 4 quarters: 1 beat, 1 in line, 2 missed
  2026-06-30 missed by 6% | 2026-03-31 beat by 23% | 2025-12-31 in line | 2025-09-30 missed by 7%
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
Price target: mean 46.29 (+19.8% vs last close), range 39.60 - 62.67
Recent rating changes:
  - 2026-09-11 Morgan Stanley: down, Equal-Weight -> Underweight
  - 2026-03-02 Goldman Sachs: down, Buy -> Neutral
  - 2026-02-24 JP Morgan: down, Overweight -> Neutral
  - 2026-01-09 CICC: init, ? -> Outperform
  - 2025-12-08 Argus Research: down, Buy -> Hold
  - 2025-11-28 Goldman Sachs: main, Buy -> Buy
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
Net: +0 shares | insiders hold 132,841 shares
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

- [Procter & Gamble Company (The) (PG) Is a Trending Stock: Facts to Know Before Betting on It](https://ca.finance.yahoo.com/news/procter-gamble-company-pg-trending-120004651.html)  
  <sub>Yahoo! Finance Canada, 3 hours ago</sub>  
  Zacks.com users have recently been watching P&G (PG) quite a bit. Thus, it is worth knowing the facts that could determine the stock's prospects.
- [Procter & Gamble's (PG) Hold Rating Reiterated at TD Cowen](https://www.marketbeat.com/instant-alerts/analyst-procter-gambles-pg-hold-rating-reiterated-at-td-cowen-2026-09-30/)  
  <sub>MarketBeat, 2 hours ago</sub>  
  TD Cowen reaffirmed a "hold" rating and issued a $150.00 target price on shares of Procter & Gamble in a report on Wednesday.
- [PG Reiterates by TD Cowen -- Price Target Maintained at $150](https://www.gurufocus.com/news/9103456/pg-reiterates-by-td-cowen-price-target-maintained-at-150)  
  <sub>GuruFocus, 1 hour ago</sub>  
  On October 3, 2023, TD Cowen maintained a 'Hold' rating for Procter & Gamble (PG). The price target remains unchanged at $150.00. GF Valueâ„¢ verdict.
- [Top 3 Dividend Stocks To Watch In September 2026](https://simplywall.st/stocks/us/healthcare/nyse-cvs/cvs-health/news/top-3-dividend-stocks-to-watch-in-september-2026-1)  
  <sub>Simply Wall St, 5 hours ago</sub>  
  With U.S. Treasury yields sitting near multi decade highs, cash and bonds are paying more, and expensive growth stories are under pressure.
- [TD Cowen reiterates Hold rating on Procter & Gamble, $150 price target](https://www.tradingview.com/news/tradingview:076e1d3e49c57:0-td-cowen-reiterates-hold-rating-on-procter-gamble-150-price-target/)  
  <sub>TradingView, 2 hours ago</sub>  
  TD Cowen reiterated their Hold rating on Procter & Gamble's stock with a price target of $150.00.The price target implies an upside of 1.1% from the Sep 29...
- [P&G Fiscal 2027 Outlook Brings an 8% Core EPS Headwind Into Focus](https://qz.com/p-g-fiscal-2027-outlook-brings-an-8-core-eps-headwind-into-focus)  
  <sub>qz.com, 16 hours ago</sub>  
  PG faces an 8% fiscal 2027 core EPS headwind from higher input costs, financing expense, lower non-operating income and currency pressures.
- [Procter & Gamble (NYSE:PG) Stock: Can Reinvesting in Marketing Restart Growth After a Flat Quarter?](https://kalkine.ca/news/consumer/procter-gamble-nysepg-stock-can-reinvesting-in-marketing-restart-growth-after-a-flat-quarter)  
  <sub>kalkine.ca, 20 hours ago</sub>  
  Procter & Gamble (NYSE:PG) Stock: Can Reinvesting in Marketing Restart Growth After a Flat Quarter?
- [Forever Stocks: 4 Undervalued Dividend Stocks Investors Can Buy Now and Hold Forever](https://www.theglobeandmail.com/investing/markets/stocks/PG/pressreleases/4869800/forever-stocks-4-undervalued-dividend-stocks-investors-can-buy-now-and-hold-forever/)  
  <sub>The Globe and Mail, 10 hours ago</sub>  
  Detailed price information for Procter & Gamble (PG-N) from The Globe and Mail including charting and trades.
- [Procter & Gamble Co (PG) Stock Down 0.5% -- Now Undervalued? GF Score: 87/100](https://www.gurufocus.com/news/9102462/procter-gamble-co-pg-stock-down-05-now-undervalued-gf-score-87100)  
  <sub>GuruFocus, 15 hours ago</sub>  
  On September 29, 2026, Procter & Gamble Co (PG) shares fell 0.5% to $148.32, trading within a 52-week range of $137.62 to $167.25.
- [PREATONI Group (BIT:PG) Stock Eyes Profit Reset As Valuation Debate Deepens](https://simplywall.st/stocks/fr/consumer-services/epa-alpg/preatoni-group-shares/news/preatoni-group-bitpg-stock-eyes-profit-reset-as-valuation-de/amp)  
  <sub>Simply Wall St, 15 hours ago</sub>  
  PREATONI Group stock closed at €36.8 today after a flat week and a weak three month stretch, yet the fresh half year figures tell a more complicated story.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>Price and chart</b> — score n/a</summary>

```text
Last close 147.71 (bar of 2026-09-30), from 502 daily bars
Trend: vs 20d SMA 146.49 (+0.8%), 50d 145.93 (+1.2%), 200d 147.65 (+0.0%); 50d below 200d
Momentum: RSI(14) 54.1 | MACD 0.593 vs signal 0.381 (histogram 0.212)
Returns: 1d -0.4% | 5d +0.2% | 1m +1.8% | 3m +0.2%
52-week range: 138.04 - 167.20 (now 33.2% of the way up)
Volatility: ATR(14) 2.32 (1.6% of price) | annualised 20d 15.3%
Volume: 0.13x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score n/a</summary>

```text
Sector: Consumer Defensive / Household & Personal Products | market cap 343.08B
Valuation: trailing P/E 22.31 | forward P/E 19.96 | P/B 6.44 | PEG 3.79
Profitability: profit margin 18.4% | operating margin 22.1% | ROE 30.3%
Growth (YoY): revenue +1.5% | earnings -15.5%
Balance sheet: debt/equity 64.5% | free cash flow 13.28B
Risk: beta 0.38 | short interest 1.0% of float
Next earnings: 2026-10-22
```

</details>

<details><summary><b>What this fund holds</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>Does this company beat its own forecasts</b> — score n/a</summary>

```text
Earnings record, last 4 quarters: 4 in line
  2026-06-30 in line | 2026-03-31 in line | 2025-12-31 in line | 2025-09-30 in line
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
Consensus: buy (mean 2.20 on a 1=strong buy to 5=strong sell scale, 23 analysts)
Ratings: 6 strong buy, 7 buy, 12 hold, 0 sell, 0 strong sell
Price target: mean 160.61 (+8.7% vs last close), range 143.00 - 186.00
Recent rating changes:
  - 2026-09-30 TD Cowen: reit, Hold -> Hold
  - 2026-08-07 Argus Research: down, Buy -> Hold
  - 2026-07-30 HSBC: down, Buy -> Hold
  - 2026-07-30 Citigroup: main, Buy -> Buy
  - 2026-07-21 Barclays: main, Equal-Weight -> Equal-Weight
  - 2026-07-16 JP Morgan: main, Overweight -> Overweight
Institutional ownership: 71.8%
Largest holders: Blackrock Inc. (8.2%), Vanguard Capital Management LLC (6.6%), State Street Corporation (4.4%), Geode Capital Management, LLC (2.9%), Vanguard Portfolio Management LLC (2.7%)
```

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>Buying and selling by company insiders</b> — score n/a</summary>

```text
Last 180 days: bought 90,364 shares in 25 transaction(s) | sold 40,243 shares in 13
Net: +50,121 shares (+2.4% of insider holdings) | insiders hold 2,115,234 shares
Distinct insiders: 0 buying, 10 selling
Sales — weak evidence on their own; often scheduled 10b5-1 plans, tax on vesting, or diversification:
  - 2026-08-24 JANZARUK MATTHEW W. (Officer): 359 shares, 52.14K
  - 2026-08-21 RAMAN SUNDAR G. (Officer): 3,435 shares, 491.27K
  - 2026-08-20 JANZARUK MATTHEW W. (Officer): 156 shares, 22.43K
  - 2026-08-20 PURUSHOTHAMAN BALAJI (Officer): 2,019 shares, 290.31K
(24 grant/option/gift transaction(s) excluded — compensation, not a view on the price)
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

- [Royal Bank of Canada (RY.TO) stock price, news, quote and history](https://au.finance.yahoo.com/quote/RY.TO/)  
  <sub>Yahoo Finance Australia, 20 hours ago</sub>  
  Royal Bank of Canada (RY.TO) · -1.35% · -0.31% · 28.85% · 21.06% · 38.39% · 123.57% · 4,135.96%. Key events. Baseline. Advanced chart.
- [Royal Bank of Canada (TSE:RY) Share Price Crosses Above 200 Day Moving Average - Here's What Happened](https://www.marketbeat.com/instant-alerts/price-royal-bank-of-canada-tse-ry-share-price-crosses-above-200-day-moving-average-heres-what-happened-2026-09-30/)  
  <sub>MarketBeat, 9 hours ago</sub>  
  Royal Bank of Canada (TSE:RY) Stock Crosses Above 200-Day Moving Average - What's Next?
- [Royal Bank of Canada (RY) Shares Fall 0.6% -- GF Value Says Still Overvalued](https://www.gurufocus.com/news/9102482/royal-bank-of-canada-ry-shares-fall-06-gf-value-says-still-overvalued)  
  <sub>GuruFocus, 15 hours ago</sub>  
  On September 29, 2026, Royal Bank of Canada (RY) shares fell 0.6% to a current price of $199.80, reflecting a decline in the context of a 52-week range of...
- [Top 3 Canadian Dividend Stocks To Watch In September 2026](https://simplywall.st/stocks/ca/banks/tsx-ry/royal-bank-of-canada-shares/news/top-3-canadian-dividend-stocks-to-watch-in-september-2026-2)  
  <sub>Simply Wall St, 1 hour ago</sub>  
  Australian inflation recently accelerated to 4% as housing and transport costs pushed the Reserve Bank's cash rate to a 15 year high of 4.6%.
- [Canadian Imperial Bank of Commerce (CM.TO) Stock Price, News, Quote & History](https://ca.finance.yahoo.com/quote/CM.TO/)  
  <sub>Yahoo! Finance Canada, 7 hours ago</sub>  
  Find the latest Canadian Imperial Bank of Commerce (CM.TO) stock quote, history, news and other vital information to help you with your stock trading and...
- [BCFD ETF Holdings List — HAN:BCFD](https://www.tradingview.com/symbols/HAN-BCFD/holdings/)  
  <sub>TradingView, 7 hours ago</sub>  
  UBS (Irl) ETF PLC - UBS MSCI Canada Universal UCITS ETF Accum CAD. BCFD Hannover Stock Exchange. BCFD Hannover Stock Exchange. BCFD Hannover Stock Exchange.
- [Royal Bank of Canada stock gains 1.03 percent on Q3 results](https://www.ad-hoc-news.de/boerse/news/corporate-news/royal-bank-of-canada-stock-gains-1-03-percent-on-q3-results/70204008)  
  <sub>AD HOC NEWS, 3 hours ago</sub>  
  Royal Bank of Canada stock posted adjusted Q3 EPS of CAD 4.28, up 11.00 percent year over year. Capital Markets revenue rose 16.00 percent in Q3 2026.
- [Why Bloom Energy Stock Is Powering Higher Today](https://www.theglobeandmail.com/investing/markets/stocks/RY-N/pressreleases/4862526/why-bloom-energy-stock-is-powering-higher-today/)  
  <sub>The Globe and Mail, 21 hours ago</sub>  
  Detailed price information for Royal Bank of Canada (RY-N) from The Globe and Mail including charting and trades.
- [1 Industrials Stock to Own for Decades and 2 Facing Challenges](http://markets.chroniclejournal.com/chroniclejournal/article/stockstory-2026-9-30-1-industrials-stock-to-own-for-decades-and-2-facing-challenges)  
  <sub>The Chronicle-Journal, 10 hours ago</sub>  
  Whether you see them or not, industrials businesses play a crucial part in our daily activities. Unfortunately, this role also comes with a demand profile...
- [Royal Bank Of Canada (NYSE:RY) Sees Significant Decrease in Short Interest](https://www.marketbeat.com/instant-alerts/options-royal-bank-of-canada-nyse-ry-sees-significant-decrease-in-short-interest-2026-09-29/)  
  <sub>MarketBeat, 17 hours ago</sub>  
  Royal Bank Of Canada (NYSE:RY - Get Free Report) (TSE:RY) was the recipient of a significant decline in short interest during the month of September.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>Price and chart</b> — score n/a</summary>

```text
Last close 197.97 (bar of 2026-09-30), from 502 daily bars
Trend: vs 20d SMA 204.32 (-3.1%), 50d 207.29 (-4.5%), 200d 186.10 (+6.4%); 50d above 200d
Momentum: RSI(14) 36.2 | MACD -2.185 vs signal -1.695 (histogram -0.490)
Returns: 1d -0.9% | 5d -0.7% | 1m -3.0% | 3m -5.0%
52-week range: 143.64 - 217.87 (now 73.2% of the way up)
Volatility: ATR(14) 3.02 (1.5% of price) | annualised 20d 17.6%
Volume: 0.15x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score n/a</summary>

```text
Sector: Financial Services / Banks - Diversified | market cap 274.08B
Valuation: trailing P/E 17.66 | forward P/E 15.70 | P/B 2.87 | PEG 2.26
Profitability: profit margin 33.9% | operating margin 46.4% | ROE 16.2%
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
Consensus: buy (mean 2.13 on a 1=strong buy to 5=strong sell scale, 3 analysts)
Ratings: 4 strong buy, 5 buy, 5 hold, 0 sell, 1 strong sell
Price target: mean 208.26 (+5.2% vs last close), range 183.36 - 225.62
Recent rating changes:
  - 2025-08-29 Argus Research: main, Buy -> Buy
  - 2024-12-05 BMO Capital: main, Outperform -> Outperform
  - 2024-08-29 BMO Capital: main, Outperform -> Outperform
  - 2024-06-06 Argus Research: main, Buy -> Buy
  - 2024-04-05 BMO Capital: up, Market Perform -> Outperform
  - 2023-12-18 B of A Securities: up, Neutral -> Buy
Institutional ownership: 49.5%
Largest holders: Royal Bank of Canada (5.1%), Bank of Montreal /CAN/ (4.4%), Vanguard Capital Management LLC (3.1%), FIL LTD (1.7%), TD Asset Management, Inc (1.7%)
```

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>Buying and selling by company insiders</b> — score n/a</summary>

```text
Last 180 days: bought 0 shares in 0 transaction(s) | sold n/a shares in 0
Net: +0 shares | insiders hold 387,640 shares
Distinct insiders: 1 buying, 0 selling
Open-market purchases — insiders spending their own money:
  - 2026-08-31 Royal Bank of Canada (Issuer): 350,000 shares, 71.49M
  - 2026-08-28 Royal Bank of Canada (Issuer): 350,000 shares, 71.50M
  - 2026-07-31 Royal Bank of Canada (Issuer): 140 shares, 29.28K
  - 2026-07-31 Royal Bank of Canada (Issuer): 153 shares, 32.23K
(105 grant/option/gift transaction(s) excluded — compensation, not a view on the price)
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

- [Teva Pharmaceutical Industries Limited (TEVA) Stock Price, News, Quote & History](https://ca.finance.yahoo.com/quote/TEVA/)  
  <sub>Yahoo! Finance Canada, 15 hours ago</sub>  
  Teva Pharmaceutical Industries Limited (TEVA) · 2.05% · 9.25% · 40.42% · 27.56% · 97.08% · 308.73% · 4,292.83%. Key Events. Baseline. Advanced Chart. Loading...
- [Teva Pharmaceutical Industries Ltd. (NYSE:TEVA) Receives Average Rating of "Moderate Buy" from Analysts](https://www.marketbeat.com/instant-alerts/consensus-teva-pharmaceutical-industries-ltd-nyse-teva-receives-average-rating-of-moderate-buy-from-analysts-2026-09-30/)  
  <sub>MarketBeat, 6 hours ago</sub>  
  Teva Pharmaceutical Industries Ltd. (NYSE:TEVA - Get Free Report) has earned a consensus recommendation of "Moderate Buy" from the twelve ratings firms that...
- [FDA Approves Denosumab Biosimilar for Skeletal-Related Events, GCTB, and Hypercalcemia of Malignancy](https://www.onclive.com/view/fda-approves-denosumab-biosimilar-for-skeletal-related-events-gctb-and-hypercalcemia-of-malignancy)  
  <sub>OncLive, 1 hour ago</sub>  
  Denosumab-adet (Degevma) is FDA approved as an Xgeva biosimilar for SRE prevention in myeloma and bone metastases, giant cell tumor of bone, and HCM.
- [Teva Pharmaceutical Industries Limited (TEVA) stock price, news, quote and history](https://uk.finance.yahoo.com/quote/TEVA/)  
  <sub>Yahoo Finance UK, 19 hours ago</sub>  
  Teva Pharmaceutical Industries Limited (TEVA) · 2.05% · 9.25% · 40.42% · 27.56% · 97.08% · 308.73% · 4,292.83%. Key events. Baseline. Advanced chart. Loading...
- [Tel Aviv Stock Exchange is booming. Look closer and the picture is very different](https://www.ynetnews.com/business/article/rk500ar5cml)  
  <sub>Ynetnews, 3 hours ago</sub>  
  A handful of heavyweight winners, led by Tower and insurance stocks, are carrying the market higher even as 67 of 126 major shares have fallen;...
- [Gerresheimer's quarterly sales recovery boosts shares](https://www.aol.com/articles/gerresheimer-reports-lower-half-core-071923000.html)  
  <sub>AOL.com, 5 hours ago</sub>  
  Sept 30 (Reuters) - Gerresheimer reported a sequential recovery in its second-quarter revenue on Wednesday, sending its shares 8% higher in early trading,...
- [Why CADL Stock Plunged Nearly 15% In After-Hours Trading Today](https://stocktwits.com/news-articles/markets/equity/why-cadl-stock-plunged-in-after-hours-trading-today/cZRZFbVR4DK)  
  <sub>Stocktwits, 15 hours ago</sub>  
  Candel is pushing ahead with an equity raise and also lined up $100 million in royalty funding from RTW Investments, contingent on FDA approval of CAN-2409.
- [ConocoPhillips Reportedly Mulls Sale Of Permian Assets For $2B](https://stocktwits.com/news-articles/markets/equity/conocophillips-reportedly-mulls-sale-of-permian-assets-for-2b/cZRN1FfR4xM)  
  <sub>Stocktwits, 17 hours ago</sub>  
  According to a report from Bloomberg, which cited people familiar with the matter, the assets being considered were acquired through deals with Concho...
- [Tue: Nice falls sharply on flat TASE](https://en.globes.co.il/en/article-tue-nice-falls-sharply-on-flat-tase-1001557942)  
  <sub>Globes - Israel Business News, 23 hours ago</sub>  
  The Tel Aviv Stock Exchange was flat today. The Tel Aviv 35 Index rose 0.02% to 4,221.94 points, the Tel Aviv 125 Index rose 0.17% to 4,084.27 points;...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>Price and chart</b> — score n/a</summary>

```text
Last close 39.60 (bar of 2026-09-30), from 502 daily bars
Trend: vs 20d SMA 38.42 (+3.0%), 50d 36.58 (+8.3%), 200d 33.59 (+17.9%); 50d above 200d
Momentum: RSI(14) 58.5 | MACD 0.876 vs signal 0.886 (histogram -0.010)
Returns: 1d -0.5% | 5d +1.5% | 1m +9.8% | 3m +18.4%
52-week range: 18.95 - 40.22 (now 97.1% of the way up)
Volatility: ATR(14) 1.24 (3.1% of price) | annualised 20d 33.3%
Volume: 0.11x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score n/a</summary>

```text
Sector: Healthcare / Drug Manufacturers - Specialty & Generic | market cap 46.18B
Valuation: trailing P/E 65.99 | forward P/E 13.00 | P/B 5.95 | PEG n/a
Profitability: profit margin 4.1% | operating margin 4.0% | ROE 9.7%
Growth (YoY): revenue -0.8% | earnings n/a
Balance sheet: debt/equity 217.8% | free cash flow 2.22B
Risk: beta 0.80 | short interest 2.7% of float
Next earnings: 2026-11-03
```

</details>

<details><summary><b>What this fund holds</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>Does this company beat its own forecasts</b> — score n/a</summary>

```text
Earnings record, last 4 quarters: 3 beats, 1 missed
  2026-06-30 missed by 92% | 2026-03-31 beat by 9% | 2025-12-31 beat by 39% | 2025-09-30 beat by 17%
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
Consensus: buy (mean 1.71 on a 1=strong buy to 5=strong sell scale, 6 analysts)
Ratings: 3 strong buy, 3 buy, 1 hold, 0 sell, 0 strong sell
Price target: mean 44.83 (+13.2% vs last close), range 40.00 - 50.00
Recent rating changes:
  - 2026-09-23 Oppenheimer: init, ? -> Outperform
  - 2026-09-09 Leerink Partners: init, ? -> Outperform
  - 2026-09-04 UBS: main, Buy -> Buy
  - 2026-08-12 Barclays: main, Overweight -> Overweight
  - 2026-07-28 Piper Sandler: main, Overweight -> Overweight
  - 2026-05-06 Barclays: main, Overweight -> Overweight
Institutional ownership: 23.0%
Largest holders: Blackrock Inc. (5.5%), Harel Insurance Investments & Financial Services Ltd. (4.1%), Phoenix Financial Ltd. (3.7%), WCM Investment Management, LLC (3.5%), Clal Insurance Enterprises Holdings Ltd (3.5%)
```

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>Buying and selling by company insiders</b> — score n/a</summary>

```text
Last 180 days: bought 43,476 shares in 3 transaction(s) | sold 194,459 shares in 6
Net: -150,983 shares (-2.4% of insider holdings) | insiders hold 6,094,499 shares
Distinct insiders: 0 buying, 10 selling
Sales — weak evidence on their own; often scheduled 10b5-1 plans, tax on vesting, or diversification:
  - 2026-09-18 SAVAGE BRIAN (Officer): 7,342 shares, 285.21K
  - 2026-09-18 MIGNONE ROBERTO A. (Director): 367,600 shares, 14.36M
  - 2026-08-21 WEISS AMIR (Officer): 9,445 shares, 355.30K
  - 2026-08-03 HUGHES ERIC A (Officer): 25,578 shares, 892.05K
(13 grant/option/gift transaction(s) excluded — compensation, not a view on the price)
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

- [ExxonMobil (XOM) Stock Could Be 15% Undervalued After Vietnam Supply Deal](https://simplywall.st/stocks/us/energy/nyse-xom/exxonmobil-holdings/news/exxonmobil-xom-stock-could-be-15-undervalued-after-vietnam-s)  
  <sub>Simply Wall St, 15 hours ago</sub>  
  ExxonMobil Holdings has powered through the last few years with a strong share price run, and that kind of track record naturally puts the focus on whether...
- [Oil Hovers Around $90: Are Permian Stocks Well Poised to Gain?](https://www.theglobeandmail.com/investing/markets/stocks/XOM/pressreleases/4881081/oil-hovers-around-90-are-permian-stocks-well-poised-to-gain/)  
  <sub>The Globe and Mail, 38 minutes ago</sub>  
  Detailed price information for Exxonmobil Holdings Corp (XOM-N) from The Globe and Mail including charting and trades.
- [What's Going On With ExxonMobil Stock Tuesday?](https://www.benzinga.com/markets/large-cap/26/09/62061419/whats-going-on-with-exxonmobil-stock-tuesday)  
  <sub>Benzinga, 21 hours ago</sub>  
  Exxon Mobil (XOM) stock dips Tuesday amid energy sector drag. TD Cowen hikes price target to $180, forecasting strong Q3 refining earnings.
- [Is ExxonMobil Stock Increasing Your Market Risk?](https://www.trefis.com/stock/xom/articles/616949/is-exxonmobil-stock-increasing-your-market-risk/2026-09-29)  
  <sub>Trefis, 17 hours ago</sub>  
  You hold ExxonMobil (XOM) alongside index funds, and in the last five sessions, the stock rose 2.7% as the S&P 500 fell 1.0%. You already own the market's...
- [Exxon Stock Trades Near Its High After a 44% Run. Here’s What Could Stall the Rally](https://www.tikr.com/blog/exxon-stock-trades-near-its-high-after-a-44-run-heres-what-could-stall-the-rally)  
  <sub>TIKR.com, 22 hours ago</sub>  
  Here's why Exxon stock's 44% rally over the past year leaves little upside in the valuation model.
- [ExxonMobil Holdings Corp (XOM) Shares Fall 0.7% -- GF Value Says Still Overvalued](https://www.gurufocus.com/news/9102445/exxonmobil-holdings-corp-xom-shares-fall-07-gf-value-says-still-overvalued)  
  <sub>GuruFocus, 15 hours ago</sub>  
  On September 29, 2026, ExxonMobil Holdings Corp (XOM) shares fell 0.7% today, bringing the current price to $161.35. The stock has experienced a 52-week...
- [Xometry, Inc. (XMTR) stock price, news, quote and history](https://uk.finance.yahoo.com/quote/XMTR/)  
  <sub>Yahoo Finance UK, 15 hours ago</sub>  
  Xometry, Inc. (XMTR) · -0.86% · 10.75% · 176.91% · 75.26% · 86.42% · 87.46% · 55.54%. Key events. Baseline. Advanced chart. Loading chart for...
- [ExxonMobil (NYSE:XOM) Stock: New Corporate Identity, Same Trading Symbol](https://kalkine.ca/news/energy/exxonmobil-nysexom-stock-new-corporate-identity-same-trading-symbol)  
  <sub>kalkine.ca, 19 hours ago</sub>  
  Key Highlights. ExxonMobil Holdings Corporation replaced Exxon Mobil Corporation as the public parent on July 1, 2026, with the XOM symbol unchanged.
- [S&P 500, Nasdaq, Dow End Higher On SpaceX Strong Debut And US-Iran Peace Signals — SPCX, SHEL, ROKU, XOM, HOOD In Focus](https://stocktwits.com/news-articles/markets/equity/s-and-p-500-nasdaq-dow-end-higher-on-space-x-strong-debut-and-us-iran-peace-signals-spcx-shel-roku-xom-hood-in-focus/cZKdaEuR75L)  
  <sub>Stocktwits, 17 hours ago</sub>  
  U.S. stock indices gained on Friday to end the week higher amid renewed hopes of diplomacy between the U.S. and Iran, while SpaceX's strong trading debut...
- [If You Invested $1000 In ExxonMobil Holdings Stock 5 Years Ago, You Would Have This Much Today](https://www.benzinga.com/news/26/09/62068825/if-you-invested-1000-exxonmobil-holdings-stock-5-years-ago-you-would-have-much-today)  
  <sub>Benzinga, 15 hours ago</sub>  
  ExxonMobil Holdings (NYSE:XOM) has outperformed the market over the past 5 years by 8.93% on an annualized basis producing an average annual return of...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>Price and chart</b> — score n/a</summary>

```text
Last close 162.50 (bar of 2026-09-30), from 502 daily bars
Trend: vs 20d SMA 162.69 (-0.1%), 50d 160.20 (+1.4%), 200d 148.64 (+9.3%); 50d above 200d
Momentum: RSI(14) 52.2 | MACD 0.471 vs signal 0.874 (histogram -0.404)
Returns: 1d +0.7% | 5d +0.8% | 1m +1.0% | 3m +19.2%
52-week range: 110.64 - 171.47 (now 85.3% of the way up)
Volatility: ATR(14) 3.51 (2.2% of price) | annualised 20d 24.8%
Volume: 0.13x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score n/a</summary>

```text
Sector: Energy / Oil & Gas Integrated | market cap 668.19B
Valuation: trailing P/E 20.89 | forward P/E 14.60 | P/B 2.58 | PEG 1.38
Profitability: profit margin 9.1% | operating margin 15.9% | ROE 12.6%
Growth (YoY): revenue +44.1% | earnings +112.8%
Balance sheet: debt/equity 15.9% | free cash flow 20.67B
Risk: beta 0.17 | short interest 1.1% of float
Next earnings: 2026-10-30
```

</details>

<details><summary><b>What this fund holds</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>Does this company beat its own forecasts</b> — score n/a</summary>

```text
Earnings record, last 4 quarters: 2 beats, 2 in line
  2026-06-30 in line | 2026-03-31 beat by 14% | 2025-12-31 in line | 2025-09-30 beat by 2%
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
Consensus: buy (mean 2.32 on a 1=strong buy to 5=strong sell scale, 22 analysts)
Ratings: 3 strong buy, 7 buy, 15 hold, 0 sell, 0 strong sell
Price target: mean 173.09 (+6.5% vs last close), range 142.00 - 200.00
Recent rating changes:
  - 2026-09-28 TD Cowen: main, Buy -> Buy
  - 2026-09-03 Piper Sandler: main, Neutral -> Neutral
  - 2026-08-19 Morgan Stanley: main, Overweight -> Overweight
  - 2026-08-17 Barclays: main, Overweight -> Overweight
  - 2026-08-07 TD Cowen: main, Buy -> Buy
  - 2026-08-04 Freedom Broker: up, Sell -> Hold
Institutional ownership: 67.2%
Largest holders: Blackrock Inc. (8.1%), Vanguard Capital Management LLC (6.5%), State Street Corporation (5.0%), FMR, LLC (3.3%), Vanguard Portfolio Management LLC (2.8%)
```

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>Buying and selling by company insiders</b> — score n/a</summary>

```text
Last 180 days: bought 10,818,651 shares in 251 transaction(s) | sold 3,904,152 shares in 49
Net: +6,914,499 shares (-194.8% of insider holdings) | insiders hold 3,371,767 shares
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

> Neutral overall: macro unchanged, flat fund flows, mixed technicals, modestly positive fundamentals but heavy cash allocation.

**Main reasons it gave:**
- Flat fund flows: 0.0% share count change over the week
- Technical indicators mixed: price below 20-day SMA and negative MACD histogram
- Macro data unchanged: yields modestly higher, VIX low, no surprise releases
- Fundamentals show strong 3-year return (+13.5% per year) but 46% cash allocation limiting upside

<details><summary><b>News</b> — score +0.00</summary>

_No news found for this one today._

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.03% (+0.00 on the week) | 5-year 5.05% (+0.06 on the week) | 10-year 5.27% (+0.15 on the week) | 30-year 5.62% (+0.22 on the week)
Yield curve, 10-year minus 3-month: +1.24 points -- upward sloping (normal)
US dollar index: 101.27 (+0.17 on the week)
Volatility (VIX): 15.90 (+0.7 on the week) -- elevated
Latest US data: inflation 3.4% (2026-08-01) | unemployment 4.1% (2026-08-01) | jobless claims 197k (2026-09-19)
Policy and expectations: Fed target 4.00% | market expects 2.4% inflation over 10 years
Rate path: 2-year Treasury 4.92% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 28.34 (bar of 2026-09-30), from 502 daily bars
Trend: vs 20d SMA 28.73 (-1.4%), 50d 28.34 (-0.0%), 200d 27.12 (+4.5%); 50d above 200d
Momentum: RSI(14) 45.5 | MACD -0.034 vs signal 0.057 (histogram -0.091)
Returns: 1d +0.3% | 5d -0.7% | 1m -3.4% | 3m +5.5%
52-week range: 25.44 - 29.49 (now 71.5% of the way up)
Volatility: ATR(14) 0.27 (1.0% of price) | annualised 20d 13.0%
Volume: 0.12x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.20</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score +0.20</summary>

```text
Fund type: Commodities Focused
What it holds: P/E n/a | P/B 0.00 | P/S 0.00 | 3y earnings growth n/a
Yield: 3.1%
Three-year record: +13.5% a year | beta to the market 0.35
Cost and size: expense ratio 0.85% | net assets 1.33B
What it is made of: Other 51.8%, Cash 46.2%, Bonds 2.0%
Largest holdings: Invesco Shrt-Trm Inv Gov&Agcy Instl 43.1%, Invesco Short Term Treasury ETF 4.4%
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
Rolled up from the 2 largest holdings, 47.5% of the fund by weight
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
Direction: flat (1 week)
Share count change: 1 week: +0.0% (0.00) over 7d
Shares outstanding: 27.60M | fund size: 782.11M
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Commodities basket (DBC) · Index fund — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:** no explanation. It wrote only “NEUTRAL”, so the main reasons below are all it gave.

**Main reasons it gave:**
- Crude inventories up 3.0 M barrels (build) – 58th percentile
- EIA forecasts WTI price to decline from $88 to $79 over six months
- Price near 52‑week high (90% of range) with MACD below signal
- Fund flows flat (0% change) over past week
- 10‑yr minus 3‑mo yield curve unchanged (+1.24) and VIX up 0.7 to 15.90

<details><summary><b>News</b> — score +0.00</summary>

_No news found for this one today._

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.03% (+0.00 on the week) | 5-year 5.05% (+0.06 on the week) | 10-year 5.27% (+0.15 on the week) | 30-year 5.62% (+0.22 on the week)
Yield curve, 10-year minus 3-month: +1.24 points -- upward sloping (normal)
US dollar index: 101.27 (+0.17 on the week)
Volatility (VIX): 15.90 (+0.7 on the week) -- elevated
Latest US data: inflation 3.4% (2026-08-01) | unemployment 4.1% (2026-08-01) | jobless claims 197k (2026-09-19)
Policy and expectations: Fed target 4.00% | market expects 2.4% inflation over 10 years
Rate path: 2-year Treasury 4.92% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 32.55 (bar of 2026-09-30), from 502 daily bars
Trend: vs 20d SMA 32.73 (-0.5%), 50d 31.10 (+4.7%), 200d 28.07 (+15.9%); 50d above 200d
Momentum: RSI(14) 54.4 | MACD 0.402 vs signal 0.591 (histogram -0.189)
Returns: 1d +1.7% | 5d -1.0% | 1m +4.0% | 3m +23.1%
52-week range: 22.07 - 33.68 (now 90.3% of the way up)
Volatility: ATR(14) 0.51 (1.6% of price) | annualised 20d 19.6%
Volume: 0.36x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score -0.40</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score -0.40</summary>

```text
Fund type: Commodities Broad Basket
What it holds: P/E n/a | P/B 0.00 | P/S 0.00 | 3y earnings growth n/a
Yield: 2.4%
Three-year record: +13.7% a year | beta to the market 1.05
Cost and size: expense ratio 0.85% | net assets 1.80B
What it is made of: Other 50.6%, Cash 44.8%, Bonds 2.7%, Stocks 1.9%
Largest holdings: Invesco Shrt-Trm Inv Gov&Agcy Instl 40.8%, Brent Crude Future Nov 26 8.9%, Invesco Short Term Treasury ETF 6.2%, Mini Ibovespa Future Dec 26 1.9%
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
US inventories, week ending 2026-09-18 (published the following Wednesday)
  Crude oil: 426.4 million barrels, +3.0 on the week (a build), 58% percentile over 52 weeks
  Natural gas: 3,351.0 billion cubic feet, +53.0 on the week (a build), 73% percentile over 52 weeks
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
Rolled up from the 4 largest holdings, 57.7% of the fund by weight
Ratings by weight: buy n/a | hold n/a | sell n/a (mean n/a on a 1=strong buy to 5=strong sell scale)
Weighted price target: n/a above the current prices
Holdings read: AGPXX, BRNF6, TBLL, WINZ26
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
Direction: flat (1 week)
Share count change: 1 week: +0.0% (0.00) over 12d
Shares outstanding: 111.40M | fund size: 3.63B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### US company bonds, riskier (HYG) · Index fund — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:** no explanation. It wrote only “Neutral”, so the main reasons below are all it gave.

**Main reasons it gave:**
- Flat fund flows (0% change) over the past week
- Price below 20‑day, 50‑day, and 200‑day SMAs (77.43 vs 78.45/79.11/79.92)
- RSI 23.4 indicating oversold conditions but no decisive technical breakout
- Treasury yields rose modestly (10‑yr +0.15% week) with no policy surprise

<details><summary><b>News</b> — score +0.00</summary>

- [Amplify HYG High Yield 10% Target Income ETF declares $0.2004 dividend](https://www.tradingview.com/news/seekingalpha:2086c86b9094b:0-amplify-hyg-high-yield-10-target-income-etf-declares-0-2004-dividend/)  
  <sub>TradingView, 17 hours ago</sub>  
  Content provided by Seeking Alpha is intended for information purposes only, and that Seeking Alpha does not offer any personalist investment advice and is...
- [4 ETFs Seeing Unusual Options Volume Today](https://www.schaeffersresearch.com/content/options/2026/09/29/4-etfs-seeing-unusual-options-volume-today)  
  <sub>Schaeffer's Investment Research, 22 hours ago</sub>  
  Four exchange-traded funds (ETFs) are seeing notable options activity today, with iShares iBoxx $ High Yield Corporate Bond ETF (HYG), iShares MSCI Brazil...
- [The Credit Rout Is No Longer a Distant Threat: 4 ETFs Show How a Looming Debt Collapse Could Hit Stocks](https://www.inkl.com/news/the-credit-rout-is-no-longer-a-distant-threat-4-etfs-show-how-a-looming-debt-collapse-could-hit-stocks)  
  <sub>inkl, 20 hours ago</sub>  
  If you want to know where stock market liquidity is actually headed, stop looking at headline equity indexes and start watching the credit “chain.”
- [Tom McClellan: Junk bond ETF pool shrinking as T-Bond prices decline](https://tradersunion.com/news/market-voices/show/3569256-junk-bond-etf-trend/)  
  <sub>Traders Union, 23 hours ago</sub>  
  Tom McClellan highlights a shrinking pool of junk bonds in ETFs like HYG, which aligns with falling U.S. Treasury bond prices.
- [S&P 500 Holds Up As High Yield And Global Credit Weaken - TalkMarkets](https://t.co/MZLZ9SHGDf)  
  <sub>Howl.Link, 14 hours ago</sub>  
  The S&P 500 faces a critical retest of its uptrend as global credit spreads widen and high-yield bonds break lower.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.03% (+0.00 on the week) | 5-year 5.05% (+0.06 on the week) | 10-year 5.27% (+0.15 on the week) | 30-year 5.62% (+0.22 on the week)
Yield curve, 10-year minus 3-month: +1.24 points -- upward sloping (normal)
US dollar index: 101.27 (+0.17 on the week)
Volatility (VIX): 15.90 (+0.7 on the week) -- elevated
Latest US data: inflation 3.4% (2026-08-01) | unemployment 4.1% (2026-08-01) | jobless claims 197k (2026-09-19)
Policy and expectations: Fed target 4.00% | market expects 2.4% inflation over 10 years
Rate path: 2-year Treasury 4.92% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 77.43 (bar of 2026-09-30), from 502 daily bars
Trend: vs 20d SMA 78.45 (-1.3%), 50d 79.11 (-2.1%), 200d 79.92 (-3.1%); 50d below 200d
Momentum: RSI(14) 23.4 | MACD -0.480 vs signal -0.370 (histogram -0.110)
Returns: 1d +0.1% | 5d -0.9% | 1m -3.0% | 3m -2.7%
52-week range: 77.36 - 81.28 (now 1.7% of the way up)
Volatility: ATR(14) 0.28 (0.4% of price) | annualised 20d 3.9%
Volume: 0.49x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.00</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score +0.00</summary>

```text
Fund type: High Yield Bond
Yield: 5.9%
Credit quality: BB 57.9%, B 32.2%, Below B 8.3%, BBB 1.1%
Three-year record: +7.9% a year | beta to the market 0.67
Cost and size: expense ratio 0.49% | net assets 16.19B
What it is made of: Bonds 98.6%, Cash 1.2%, Preferred 0.2%
Largest holdings: BlackRock Cash Funds Treasury SL Agency 1.3%
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
Direction: flat (1 week)
Share count change: 1 week: +0.0% (0.00) over 12d
Shares outstanding: 195.60M | fund size: 15.14B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### US small companies (IWM) · Index fund — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:** no explanation. It wrote only “NEUTRAL”, so the main reasons below are all it gave.

**Main reasons it gave:**
- No macro surprise: yields rose modestly, Fed policy unchanged
- Technical mix: price above 200‑day SMA but below 20‑day/50‑day SMAs, RSI 33.3 (oversold), MACD negative, low volume
- Analyst coverage thin (1.7% of fund) despite 100% buy rating and +21.4% price target
- CFTC positioning: net short 26% of OI, short reduced by 6.4% week, short crowding at 5% percentile

<details><summary><b>News</b> — score +0.00</summary>

- [Exchange-Traded Funds Lower as US Equities Drop After Midday](https://finance.yahoo.com/markets/articles/exchange-traded-funds-lower-us-171654357.html)  
  <sub>Yahoo Finance, 22 hours ago</sub>  
  Broad Market Indicators Broad-market exchange-traded funds IWM and IVV fell. Actively traded Invesco QQQ Trust (QQQ) eased 0.1%.
- [30-Year Yield Hits 2002 High; Credit-Score Giant FICO Plunges 27%: Stock Market Today](https://www.tradingview.com/news/benzinga:0b9ed21e4094b:0-30-year-yield-hits-2002-high-credit-score-giant-fico-plunges-27-stock-market-today/)  
  <sub>TradingView, 22 hours ago</sub>  
  U.S. stocks were little changed by midday Tuesday, with small caps and the Dow lagging while tech held up, as the 10-year Treasury yield pushed to its...
- [The Credit Rout Is No Longer a Distant Threat: 4 ETFs Show How a Looming Debt Collapse Could Hit Stocks](https://www.inkl.com/news/the-credit-rout-is-no-longer-a-distant-threat-4-etfs-show-how-a-looming-debt-collapse-could-hit-stocks)  
  <sub>inkl, 20 hours ago</sub>  
  If you want to know where stock market liquidity is actually headed, stop looking at headline equity indexes and start watching the credit “chain.”

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.03% (+0.00 on the week) | 5-year 5.05% (+0.06 on the week) | 10-year 5.27% (+0.15 on the week) | 30-year 5.62% (+0.22 on the week)
Yield curve, 10-year minus 3-month: +1.24 points -- upward sloping (normal)
US dollar index: 101.27 (+0.17 on the week)
Volatility (VIX): 15.90 (+0.7 on the week) -- elevated
Latest US data: inflation 3.4% (2026-08-01) | unemployment 4.1% (2026-08-01) | jobless claims 197k (2026-09-19)
Policy and expectations: Fed target 4.00% | market expects 2.4% inflation over 10 years
Rate path: 2-year Treasury 4.92% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 279.83 (bar of 2026-09-30), from 502 daily bars
Trend: vs 20d SMA 286.54 (-2.3%), 50d 293.12 (-4.5%), 200d 276.06 (+1.4%); 50d above 200d
Momentum: RSI(14) 33.3 | MACD -4.074 vs signal -3.568 (histogram -0.506)
Returns: 1d +0.3% | 5d -0.7% | 1m -4.8% | 3m -6.5%
52-week range: 229.11 - 305.09 (now 66.8% of the way up)
Volatility: ATR(14) 3.34 (1.2% of price) | annualised 20d 11.9%
Volume: 0.29x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.00</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score +0.00</summary>

```text
Fund type: Small Blend
What it holds: P/E 17.30 | P/B 2.13 | P/S 1.31 | 3y earnings growth n/a
Yield: 0.9%
Three-year record: +17.7% a year | beta to the market 1.24
Cost and size: expense ratio 0.19% | net assets 80.46B
What it is made of: Stocks 99.5%, Cash 0.5%, Other 0.1%
Largest holdings: JFrog Ltd Ordinary Shares 0.3%, Moog Inc Class A 0.3%, BlackRock Cash Funds Treasury SL Agency 0.3%, UMB Financial Corp 0.3%, Glaukos Corp 0.3%
Sector mix: Healthcare 21.0%, Financial services 18.1%, Technology 13.8%, Industrials 13.2%
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
Rolled up from the 5 largest holdings, 1.7% of the fund by weight  -- thin, so read this as a fact about that slice rather than the fund
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 1.59 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +21.4% above the current prices
Holdings read: FROG, MOG-A, XTSLA, UMBF, GKOS
Recent rating changes among them:
  - FROG: 2026-09-04 DA Davidson: main, Buy -> Buy
  - MOG-A: 2026-09-15 Guggenheim: init, ? -> Neutral
  - UMBF: 2026-09-28 Morgan Stanley: main, Overweight -> Overweight
  - GKOS: 2026-09-22 Jefferies: main, Buy -> Buy
```

</details>

<details><summary><b>Buying and selling by company insiders</b> — score +0.10</summary>

_Not available today._

</details>

<details><summary><b>Who is positioned how</b> — score +0.10</summary>

```text
Contract: RUSSELL E-MINI - CHICAGO MERCANTILE EXCHANGE (positions as of 2026-09-22, published the following Friday)
Large speculators: net short 26.0% of open interest (415,047 contracts)
Change on the week: -6.4% of open interest
Crowding: 5% percentile over 52 weeks -- a crowded short by the standards of the past year
Read this as crowding, not as a forecast: an extreme is as often the end of a move as the middle of one.
```

</details>

<details><summary><b>Money going into and out of this fund</b> — score +0.10</summary>

```text
Direction: flat (1 week)
Share count change: 1 week: +0.0% (0.00) over 7d
Shares outstanding: 281.05M | fund size: 78.65B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### US company bonds, safer (LQD) · Index fund — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:** no explanation. It wrote only “Neutral”, so the main reasons below are all it gave.

**Main reasons it gave:**
- Flat fund flows: share count unchanged (+0.0% over 1 week)
- US Treasury yields rose modestly: 10‑year +0.15% on the week
- Technical RSI 25.4 (oversold) but no decisive break; volume 0.35× 20‑day average
- Inflation 3.4% and unemployment 4.1% in line with expectations, no macro surprise

<details><summary><b>News</b> — score +0.00</summary>

- [4 ETFs Seeing Unusual Options Volume Today](https://www.schaeffersresearch.com/content/options/2026/09/29/4-etfs-seeing-unusual-options-volume-today)  
  <sub>Schaeffer's Investment Research, 22 hours ago</sub>  
  HYG, EWZ, LQD, and XLU are seeing elevated options volume today, even as all four ETFs stick close to the flatline.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.03% (+0.00 on the week) | 5-year 5.05% (+0.06 on the week) | 10-year 5.27% (+0.15 on the week) | 30-year 5.62% (+0.22 on the week)
Yield curve, 10-year minus 3-month: +1.24 points -- upward sloping (normal)
US dollar index: 101.27 (+0.17 on the week)
Volatility (VIX): 15.90 (+0.7 on the week) -- elevated
Latest US data: inflation 3.4% (2026-08-01) | unemployment 4.1% (2026-08-01) | jobless claims 197k (2026-09-19)
Policy and expectations: Fed target 4.00% | market expects 2.4% inflation over 10 years
Rate path: 2-year Treasury 4.92% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 102.35 (bar of 2026-09-30), from 502 daily bars
Trend: vs 20d SMA 104.32 (-1.9%), 50d 105.51 (-3.0%), 200d 108.50 (-5.7%); 50d below 200d
Momentum: RSI(14) 25.4 | MACD -0.872 vs signal -0.663 (histogram -0.209)
Returns: 1d -0.1% | 5d -1.5% | 1m -3.6% | 3m -5.6%
52-week range: 102.35 - 112.92 (now 0.0% of the way up)
Volatility: ATR(14) 0.59 (0.6% of price) | annualised 20d 7.0%
Volume: 0.35x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.00</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score +0.00</summary>

```text
Fund type: Corporate Bond
Yield: 4.7%
Credit quality: A 46.6%, BBB 40.2%, AA 12.3%, AAA 1.0%
Three-year record: +4.7% a year | beta to the market 1.35
Cost and size: expense ratio 0.14% | net assets 32.04B
What it is made of: Bonds 98.9%, Cash 1.1%, Convertible 0.0%
Largest holdings: BlackRock Cash Funds Treasury SL Agency 1.0%
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
Direction: flat (1 week)
Share count change: 1 week: +0.0% (0.00) over 12d
Shares outstanding: 293.50M | fund size: 30.04B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### US government bonds, 1-3 years (SHY) · Index fund — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> No clear macro surprise, technicals show slight bearishness but no decisive break, insider positioning is modestly bearish with high crowding, and fund flows are flat. Overall the evidence does not justify a directional tilt.

**Main reasons it gave:**
- Fed rate‑hike odds fell to ~35% after softer PCE inflation (3.4%)
- U.S. Treasury yields rose for second week, 10‑yr up 15 bps to 5.27%
- Large speculators net short 29.8% of 2‑yr note, crowding at 92nd percentile
- Technical indicators show slight bearishness (RSI 39.8, price below 20‑day SMA)
- Fund flows flat, no net inflows/outflows

<details><summary><b>News</b> — score +0.00</summary>

- [Fed rate-hike odds slide after softer PCE inflation print](https://seekingalpha.com/news/4648581-fed-rate-hike-odds-slide-after-softer-pce-inflation-print)  
  <sub>Seeking Alpha, 32 minutes ago</sub>  
  Market-implied chances of a Federal Reserve interest rate increase at the October 28–29 FOMC meeting fell sharply to 34.9% after Wednesday's personal...
- [The Weekly Spread: What Shaped US Yields And The Dollar This Week](https://stocktwits.com/news-articles/markets/equity/the-weekly-spread-what-shaped-yields-and-the-dollar-this-week-1/cZMXz82RBO8)  
  <sub>Stocktwits, 13 hours ago</sub>  
  U.S. bond yields climbed for the second straight week across the curve, with yields at their highest in over a decade, as hawkish commentary from multiple...
- [Have October Fed Hike Odds Really Collapsed from 72.5 Percent to a Coin Flip in a Single Day?](https://kalkine.ca/news/general-news/have-october-fed-hike-odds-really-collapsed-from-725-percent-to-a-coin-flip-in-a-single-day)  
  <sub>kalkine.ca, 35 minutes ago</sub>  
  You are reading a free article with opinions that may differ from the recommendation given by Kalkine in its paid research reports. Become a Kalkine member...
- [Is the Fed Split on a Second Hike After Williams Urges Patience and Goolsbee Warns of Playing with Fire?](https://kalkine.ca/news/general-news/is-the-fed-split-on-a-second-hike-after-williams-urges-patience-and-goolsbee-warns-of-playing-with-fire)  
  <sub>kalkine.ca, 35 minutes ago</sub>  
  You are reading a free article with opinions that may differ from the recommendation given by Kalkine in its paid research reports. Become a Kalkine member...
- [Wells Fargo lifts 2027 Fed Funds target and yield forecasts](https://seekingalpha.com/news/4648082-wells-fargo-lifts-2027-fed-funds-target-and-yield-forecasts)  
  <sub>Seeking Alpha, 24 hours ago</sub>  
  Wells Fargo Investment Institute has revised most of its 2027 forecasts higher to reflect firmer global inflation and rising U.S. borrowing costs.
- [Will ADP Payrolls Rebounding to 70,000 from 38,000 Revive Fed Hike Bets Before Friday's Jobs Report?](https://kalkine.ca/news/general-news/will-adp-payrolls-rebounding-to-70000-from-38000-revive-fed-hike-bets-before-fridays-jobs-report)  
  <sub>kalkine.ca, 35 minutes ago</sub>  
  You are reading a free article with opinions that may differ from the recommendation given by Kalkine in its paid research reports.
- [US PCE inflation rises 3.4% in August, below expectations as economy stays resilient](https://invezz.com/nz/news/2026/09/30/us-pce-inflation-rises-34percent-in-august-below-expectations-as-economy-stays-resilient/)  
  <sub>Invezz, 1 hour ago</sub>  
  US consumer inflation rose less than expected in August, offering some relief to markets while keeping price pressures well above the Federal Reserve's 2%...
- [Asian stocks rise as bonds steady ahead of key US inflation data](https://invezz.com/pk/news/2026/09/30/asian-stocks-rise-as-bonds-steady-ahead-of-key-us-inflation-data/)  
  <sub>Invezz, 10 hours ago</sub>  
  Asian stocks rose Wednesday while bonds steadied after a bruising selloff, as investors awaited a key US inflation reading for clues on the Federal...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.03% (+0.00 on the week) | 5-year 5.05% (+0.06 on the week) | 10-year 5.27% (+0.15 on the week) | 30-year 5.62% (+0.22 on the week)
Yield curve, 10-year minus 3-month: +1.24 points -- upward sloping (normal)
US dollar index: 101.27 (+0.17 on the week)
Volatility (VIX): 15.90 (+0.7 on the week) -- elevated
Latest US data: inflation 3.4% (2026-08-01) | unemployment 4.1% (2026-08-01) | jobless claims 197k (2026-09-19)
Policy and expectations: Fed target 4.00% | market expects 2.4% inflation over 10 years
Rate path: 2-year Treasury 4.92% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score -0.20</summary>

```text
Last close 81.24 (bar of 2026-09-30), from 502 daily bars
Trend: vs 20d SMA 81.36 (-0.2%), 50d 81.70 (-0.6%), 200d 82.28 (-1.3%); 50d below 200d
Momentum: RSI(14) 39.8 | MACD -0.171 vs signal -0.172 (histogram 0.001)
Returns: 1d +0.1% | 5d +0.1% | 1m -0.8% | 3m -0.7%
52-week range: 81.09 - 83.18 (now 6.9% of the way up)
Volatility: ATR(14) 0.11 (0.1% of price) | annualised 20d 1.8%
Volume: 0.28x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score -0.10</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score -0.10</summary>

```text
Fund type: Short Government
Yield: 3.6%
Credit quality: AA 100.0% | US government debt 99.2%
Three-year record: +3.9% a year | beta to the market 0.22
Cost and size: expense ratio 0.15% | net assets 25.91B
What it is made of: Bonds 99.2%, Cash 0.8%
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
Contract: UST 2Y NOTE - CHICAGO BOARD OF TRADE (positions as of 2026-09-22, published the following Friday)
Large speculators: net short 29.8% of open interest (4,539,374 contracts)
Change on the week: -0.6% of open interest
Crowding: 92% percentile over 52 weeks -- a crowded long by the standards of the past year
Read this as crowding, not as a forecast: an extreme is as often the end of a move as the middle of one.
```

</details>

<details><summary><b>Money going into and out of this fund</b> — score -0.20</summary>

```text
Direction: flat (1 week)
Share count change: 1 week: +0.0% (0.00) over 12d
Shares outstanding: 209.30M | fund size: 17.00B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Europe (VGK) · Index fund — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:** no explanation. It wrote only “NEUTRAL”, so the main reasons below are all it gave.

**Main reasons it gave:**
- Macro: Treasury yields flat week‑on‑week, inflation 3.4% and unemployment 4.1% in line with expectations, no policy surprise
- Technical: Price below 20‑day (89.34) and 50‑day (90.54) SMAs, RSI 36.2, MACD negative, no breakout on heavy volume
- Analyst view: Only 11.4% of fund covered, 65.7% buy rating, +13.5% price target, coverage thin
- Positioning: MSCI EAFE futures net long 6% of OI, crowding 100% percentile, weekly change +1.3% OI, crowded long but not a clear directional signal
- Fund basics: P/E 17.85, dividend yield 2.8%, expense ratio 0.06%, stable three‑year record, no material change

<details><summary><b>News</b> — score +0.00</summary>

- [5 International ETFs Up at Least 20% in 2026 & Beating the S&P 500](https://www.tradingview.com/news/zacks:89dcd6767094b:0-5-international-etfs-up-at-least-20-in-2026-beating-the-s-p-500/)  
  <sub>TradingView, 3 hours ago</sub>  
  Wall Street has been in solid shape so far this year. State Street SPDR S&P 500 ETF Trust SPY has gained 12.1% while the tech-heavy Nasdaq-100 ETF Invesco...
- [ETFs Investing in Neste Corporation Stocks](https://www.tradingview.com/symbols/HAN-NEF/etfs/)  
  <sub>TradingView, 18 hours ago</sub>  
  Explore funds investing in NEF in a single list with price, expense ratio, and more stats for an in-depth analysis of new opportunities.
- [ETFs Investing in Technoprobe SpA Stocks](https://www.tradingview.com/symbols/HAN-K8B/etfs/)  
  <sub>TradingView, 19 hours ago</sub>  
  Explore funds investing in K8B in a single list with price, expense ratio, and more stats for an in-depth analysis of new opportunities.
- [ETFs Investing in Unicaja Banco S.A. Stocks](https://www.tradingview.com/symbols/HAN-7UB/etfs/)  
  <sub>TradingView, 23 hours ago</sub>  
  Explore funds investing in 7UB in a single list with price, expense ratio, and more stats for an in-depth analysis of new opportunities.
- [ETFs Investing in Aker BP ASA Stocks](https://www.tradingview.com/symbols/HAN-ARC/etfs/)  
  <sub>TradingView, 23 hours ago</sub>  
  Explore funds investing in ARC in a single list with price, expense ratio, and more stats for an in-depth analysis of new opportunities.
- [ETFs Investing in Derwent London plc Stocks](https://www.tradingview.com/symbols/HAN-DVK/etfs/)  
  <sub>TradingView, 18 hours ago</sub>  
  Explore funds investing in DVK in a single list with price, expense ratio, and more stats for an in-depth analysis of new opportunities.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.03% (+0.00 on the week) | 5-year 5.05% (+0.06 on the week) | 10-year 5.27% (+0.15 on the week) | 30-year 5.62% (+0.22 on the week)
Yield curve, 10-year minus 3-month: +1.24 points -- upward sloping (normal)
US dollar index: 101.27 (+0.17 on the week)
Volatility (VIX): 15.90 (+0.7 on the week) -- elevated
Latest US data: inflation 3.4% (2026-08-01) | unemployment 4.1% (2026-08-01) | jobless claims 197k (2026-09-19)
Policy and expectations: Fed target 4.00% | market expects 2.4% inflation over 10 years
Rate path: 2-year Treasury 4.92% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 87.51 (bar of 2026-09-30), from 502 daily bars
Trend: vs 20d SMA 89.34 (-2.0%), 50d 90.54 (-3.3%), 200d 87.61 (-0.1%); 50d above 200d
Momentum: RSI(14) 36.2 | MACD -0.830 vs signal -0.682 (histogram -0.148)
Returns: 1d -0.4% | 5d -0.6% | 1m -4.5% | 3m -0.3%
52-week range: 77.90 - 93.19 (now 62.9% of the way up)
Volatility: ATR(14) 0.91 (1.0% of price) | annualised 20d 12.2%
Volume: 0.73x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.00</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score +0.00</summary>

```text
Fund type: Europe Stock
What it holds: P/E 17.85 | P/B 2.31 | P/S 1.64 | 3y earnings growth n/a
Yield: 2.8%
Three-year record: +18.8% a year | beta to the market 0.90
Cost and size: expense ratio 0.06% | net assets 39.06B
What it is made of: Stocks 99.0%, Cash 0.7%, Other 0.3%
Largest holdings: ASML Holding NV 4.0%, HSBC Holdings PLC 2.2%, Roche Holding AG Ordinary Shares new 1.9%, Novartis AG Registered Shares 1.7%, Shell PLC 1.6%
Sector mix: Financial services 25.3%, Industrials 19.8%, Healthcare 12.1%, Technology 9.0%
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
Rolled up from the 5 largest holdings, 11.4% of the fund by weight  -- thin, so read this as a fact about that slice rather than the fund
Ratings by weight: buy 65.7% | hold 34.3% | sell 0.0% (mean 2.11 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +13.5% above the current prices
Holdings read: ASML.AS, HSBA.L, ROP.SW, NOVN.SW, SHEL.L
Recent rating changes among them: none reported
```

</details>

<details><summary><b>Buying and selling by company insiders</b> — score +0.00</summary>

_Not available today._

</details>

<details><summary><b>Who is positioned how</b> — score +0.00</summary>

```text
Contract: MSCI EAFE  - ICE FUTURES U.S. (positions as of 2026-09-22, published the following Friday)
Large speculators: net long 6.0% of open interest (487,063 contracts)
Change on the week: +1.3% of open interest
Crowding: 100% percentile over 52 weeks -- a crowded long by the standards of the past year
Read this as crowding, not as a forecast: an extreme is as often the end of a move as the middle of one.
```

</details>

<details><summary><b>Money going into and out of this fund</b> — score +0.00</summary>

```text
Direction: flat (1 week)
Share count change: 1 week: +0.0% (0.00) over 12d
Shares outstanding: 282.09M | fund size: 24.69B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Emerging markets (VWO) · Index fund — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> No material macro surprise, technicals mixed, analyst view thin, modest speculator net long, equity ETF inflows cooling

**Main reasons it gave:**
- Equity ETF inflows have cooled from mid-year peak
- Analyst view covers 22.2% of fund, 100% buy, price target +36.4% above price
- CFTC positioning net long 4.6% of open interest, up 1.3% week over week
- Technical: price below 20-day and 50-day SMA, RSI 43.6, MACD near zero
- Macro: 10-year yield up 0.15% week, VIX 15.9, no surprise data

<details><summary><b>News</b> — score +0.00</summary>

- [Equity ETF flows slide as summer unwind takes hold](https://seekingalpha.com/news/4648503-equity-etf-flows-slide-as-summer-unwind-takes-hold)  
  <sub>Seeking Alpha, 2 hours ago</sub>  
  Equity ETF inflows have cooled from their mid-year peak, according to Baird Strategas. Learn more here.
- [ETFs Investing in Aluminum Corporation of China Limited Class H Stocks](https://www.tradingview.com/symbols/HAN-AOC/etfs/)  
  <sub>TradingView, 9 hours ago</sub>  
  Explore funds investing in AOC in a single list with price, expense ratio, and more stats for an in-depth analysis of new opportunities.
- [ETFs Investing in Gold Fields Limited Stocks](https://www.tradingview.com/symbols/HAN-EDGA/etfs/)  
  <sub>TradingView, 18 hours ago</sub>  
  Explore funds investing in EDGA in a single list with price, expense ratio, and more stats for an in-depth analysis of new opportunities.
- [ETFs Investing in Jiangxi Copper Company Limited Class H Stocks](https://www.tradingview.com/symbols/HAN-JIX/etfs/)  
  <sub>TradingView, 12 hours ago</sub>  
  Explore funds investing in JIX in a single list with price, expense ratio, and more stats for an in-depth analysis of new opportunities.
- [ETFs Investing in CITIC Limited Stocks](https://www.tradingview.com/symbols/HAN-CPF/etfs/)  
  <sub>TradingView, 16 hours ago</sub>  
  Explore funds investing in CPF in a single list with price, expense ratio, and more stats for an in-depth analysis of new opportunities.
- [ETFs Investing in CMOC Group Limited Class H Stocks](https://www.tradingview.com/symbols/HAN-D7N/etfs/)  
  <sub>TradingView, 22 hours ago</sub>  
  Explore funds investing in D7N in a single list with price, expense ratio, and more stats for an in-depth analysis of new opportunities.
- [ETFs Investing in Shandong Gold Mining Co., Ltd. Class H Stocks](https://www.tradingview.com/symbols/HAN-188H/etfs/)  
  <sub>TradingView, 23 hours ago</sub>  
  Explore funds investing in 188H in a single list with price, expense ratio, and more stats for an in-depth analysis of new opportunities.
- [ETFs Investing in Chongqing Rural Commercial Bank Co. Ltd. Class H Stocks](https://www.tradingview.com/symbols/HAN-C3B/etfs/)  
  <sub>TradingView, 22 hours ago</sub>  
  Explore funds investing in C3B in a single list with price, expense ratio, and more stats for an in-depth analysis of new opportunities.
- [ETFs Investing in Wuxi Biologics (Cayman) Inc. Stocks](https://www.tradingview.com/symbols/HAN-1FW2/etfs/)  
  <sub>TradingView, 21 hours ago</sub>  
  Explore funds investing in 1FW2 in a single list with price, expense ratio, and more stats for an in-depth analysis of new opportunities.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.03% (+0.00 on the week) | 5-year 5.05% (+0.06 on the week) | 10-year 5.27% (+0.15 on the week) | 30-year 5.62% (+0.22 on the week)
Yield curve, 10-year minus 3-month: +1.24 points -- upward sloping (normal)
US dollar index: 101.27 (+0.17 on the week)
Volatility (VIX): 15.90 (+0.7 on the week) -- elevated
Latest US data: inflation 3.4% (2026-08-01) | unemployment 4.1% (2026-08-01) | jobless claims 197k (2026-09-19)
Policy and expectations: Fed target 4.00% | market expects 2.4% inflation over 10 years
Rate path: 2-year Treasury 4.92% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 59.44 (bar of 2026-09-30), from 502 daily bars
Trend: vs 20d SMA 60.23 (-1.3%), 50d 59.90 (-0.8%), 200d 57.90 (+2.7%); 50d above 200d
Momentum: RSI(14) 43.6 | MACD -0.106 vs signal 0.005 (histogram -0.111)
Returns: 1d -0.3% | 5d -1.1% | 1m -1.8% | 3m +0.4%
52-week range: 52.42 - 61.44 (now 77.8% of the way up)
Volatility: ATR(14) 0.61 (1.0% of price) | annualised 20d 13.9%
Volume: 0.42x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.30</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score +0.30</summary>

```text
Fund type: Diversified Emerging Mkts
What it holds: P/E 15.91 | P/B 2.13 | P/S 1.86 | 3y earnings growth n/a
Yield: 2.3%
Three-year record: +18.3% a year | beta to the market 0.75
Cost and size: expense ratio 0.06% | net assets 168.36B
What it is made of: Stocks 95.3%, Cash 4.6%, Other 0.1%, Preferred 0.0%
Largest holdings: Taiwan Semiconductor Manufacturing Co Ltd 14.7%, Tencent Holdings Ltd 2.9%, Alibaba Group Holding Ltd Ordinary Shares 2.2%, MediaTek Inc 1.5%, Delta Electronics Inc 0.9%
Sector mix: Technology 31.8%, Financial services 20.2%, Consumer cyclical 9.9%, Basic materials 7.9%
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
Rolled up from the 5 largest holdings, 22.2% of the fund by weight  -- thin, so read this as a fact about that slice rather than the fund
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 1.33 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +36.4% above the current prices
Holdings read: 2330.TW, 0700.HK, 9988.HK, 2454.TW, 2308.TW
Recent rating changes among them: none reported
```

</details>

<details><summary><b>Buying and selling by company insiders</b> — score +0.20</summary>

_Not available today._

</details>

<details><summary><b>Who is positioned how</b> — score +0.20</summary>

```text
Contract: MSCI EM INDEX - ICE FUTURES U.S. (positions as of 2026-09-22, published the following Friday)
Large speculators: net long 4.6% of open interest (1,036,240 contracts)
Change on the week: +1.3% of open interest
Crowding: 60% percentile over 52 weeks -- within its normal range
Read this as crowding, not as a forecast: an extreme is as often the end of a move as the middle of one.
```

</details>

<details><summary><b>Money going into and out of this fund</b> — score +0.20</summary>

```text
Direction: flat (1 week)
Share count change: 1 week: +0.0% (0.00) over 7d
Shares outstanding: 1.42B | fund size: 84.29B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Developing country bonds (EMB) · Index fund — no answer, no confidence given

<details><summary><b>News</b> — score n/a</summary>

_No news found for this one today._

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score n/a</summary>

```text
US Treasury yields: 3-month 4.03% (+0.00 on the week) | 5-year 5.05% (+0.06 on the week) | 10-year 5.27% (+0.15 on the week) | 30-year 5.62% (+0.22 on the week)
Yield curve, 10-year minus 3-month: +1.24 points -- upward sloping (normal)
US dollar index: 101.27 (+0.17 on the week)
Volatility (VIX): 15.90 (+0.7 on the week) -- elevated
Latest US data: inflation 3.4% (2026-08-01) | unemployment 4.1% (2026-08-01) | jobless claims 197k (2026-09-19)
Policy and expectations: Fed target 4.00% | market expects 2.4% inflation over 10 years
Rate path: 2-year Treasury 4.92% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score n/a</summary>

```text
Last close 91.18 (bar of 2026-09-30), from 502 daily bars
Trend: vs 20d SMA 93.15 (-2.1%), 50d 94.20 (-3.2%), 200d 95.52 (-4.5%); 50d below 200d
Momentum: RSI(14) 23.5 | MACD -0.815 vs signal -0.606 (histogram -0.210)
Returns: 1d -0.1% | 5d -1.6% | 1m -3.8% | 3m -5.0%
52-week range: 91.18 - 97.74 (now 0.0% of the way up)
Volatility: ATR(14) 0.49 (0.5% of price) | annualised 20d 6.8%
Volume: 0.30x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score n/a</summary>

```text
Fund type: Emerging Markets Bond
Yield: 5.1%
Credit quality: BBB 33.9%, BB 25.2%, B 19.3%, A 17.6% | US government debt 87.3%
Three-year record: +9.0% a year | beta to the market 1.08
Cost and size: expense ratio 0.39% | net assets 14.92B
What it is made of: Bonds 98.4%, Cash 1.6%
Largest holdings: BlackRock Cash Funds Treasury SL Agency 1.5%
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
Direction: money coming in (1 week)
Share count change: 1 week: +1.4% (204.50M) over 7d
Shares outstanding: 162.15M | fund size: 14.78B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### US government bonds, 7-10 years (IEF) · Index fund — no answer, no confidence given

<details><summary><b>News</b> — score n/a</summary>

- [A Rare Bullish Call on U.S. Treasuries: ETFs to Play](https://sg.finance.yahoo.com/news/rare-bullish-call-u-treasuries-130000338.html)  
  <sub>Yahoo Finance Singapore, 2 hours ago</sub>  
  Treasury yields near two-decade highs are creating an attractive entry point for bond investors. Here are ETFs to consider.
- [Fed rate-hike odds slide after softer PCE inflation print](https://seekingalpha.com/news/4648581-fed-rate-hike-odds-slide-after-softer-pce-inflation-print)  
  <sub>Seeking Alpha, 34 minutes ago</sub>  
  Market-implied chances of a Federal Reserve interest rate increase at the October 28–29 FOMC meeting fell sharply to 34.9% after Wednesday's personal...
- [Strange September Market Sets Up a Pivotal October](https://pro.thestreet.com/market-commentary/strange-september-market-sets-up-a-pivotal-october)  
  <sub>TheStreet Pro, 4 hours ago</sub>  
  September lived up to its poor reputation, but October has a history of starting year-end runs, especially in midterm years.
- [RARE Stock Slumps On Multiple Wall Street Price Target Slashes, Clinical Pipeline Uncertainty](https://stocktwits.com/news-articles/markets/equity/rare-stock-slumps-on-multiple-wall-street-price-target-slashes-clinical-pipeline-uncertainty/cZR5z5FR4t4)  
  <sub>Stocktwits, 12 hours ago</sub>  
  Ultragenyx said on Thursday that the FDA has again refused approval for UX111 in the treatment of Sanfilippo syndrome type A.
- [Wells Fargo lifts 2027 Fed Funds target and yield forecasts](https://seekingalpha.com/news/4648082-wells-fargo-lifts-2027-fed-funds-target-and-yield-forecasts)  
  <sub>Seeking Alpha, 24 hours ago</sub>  
  Wells Fargo Investment Institute has revised most of its 2027 forecasts higher to reflect firmer global inflation and rising U.S. borrowing costs.
- [US PCE inflation rises 3.4% in August, below expectations as economy stays resilient](https://invezz.com/nz/news/2026/09/30/us-pce-inflation-rises-34percent-in-august-below-expectations-as-economy-stays-resilient/)  
  <sub>Invezz, 1 hour ago</sub>  
  US consumer inflation rose less than expected in August, offering some relief to markets while keeping price pressures well above the Federal Reserve's 2%...
- [Asian stocks rise as bonds steady ahead of key US inflation data](https://invezz.com/uk/news/2026/09/30/asian-stocks-rise-as-bonds-steady-ahead-of-key-us-inflation-data/)  
  <sub>Invezz, 10 hours ago</sub>  
  Asian stocks rose Wednesday while bonds steadied after a bruising selloff, as investors awaited a key US inflation reading for clues on the Federal...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score n/a</summary>

```text
US Treasury yields: 3-month 4.03% (+0.00 on the week) | 5-year 5.05% (+0.06 on the week) | 10-year 5.27% (+0.15 on the week) | 30-year 5.62% (+0.22 on the week)
Yield curve, 10-year minus 3-month: +1.24 points -- upward sloping (normal)
US dollar index: 101.27 (+0.17 on the week)
Volatility (VIX): 15.90 (+0.7 on the week) -- elevated
Latest US data: inflation 3.4% (2026-08-01) | unemployment 4.1% (2026-08-01) | jobless claims 197k (2026-09-19)
Policy and expectations: Fed target 4.00% | market expects 2.4% inflation over 10 years
Rate path: 2-year Treasury 4.92% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score n/a</summary>

```text
Last close 89.43 (bar of 2026-09-30), from 502 daily bars
Trend: vs 20d SMA 90.90 (-1.6%), 50d 92.19 (-3.0%), 200d 94.55 (-5.4%); 50d below 200d
Momentum: RSI(14) 27.2 | MACD -0.807 vs signal -0.685 (histogram -0.122)
Returns: 1d -0.0% | 5d -0.8% | 1m -3.6% | 3m -4.9%
52-week range: 89.43 - 97.99 (now 0.0% of the way up)
Volatility: ATR(14) 0.45 (0.5% of price) | annualised 20d 6.2%
Volume: 0.29x the 20-day average
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
Three-year record: +3.0% a year | beta to the market 1.16
Cost and size: expense ratio 0.15% | net assets 41.82B
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
Contract: UST 10Y NOTE - CHICAGO BOARD OF TRADE (positions as of 2026-09-22, published the following Friday)
Large speculators: net short 35.6% of open interest (5,407,726 contracts)
Change on the week: -0.9% of open interest
Crowding: 87% percentile over 52 weeks -- within its normal range
Read this as crowding, not as a forecast: an extreme is as often the end of a move as the middle of one.
```

</details>

<details><summary><b>Money going into and out of this fund</b> — score n/a</summary>

```text
Direction: flat (1 week)
Share count change: 1 week: +0.0% (0.00) over 12d
Shares outstanding: 146.00M | fund size: 13.06B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### S&P 500, equal weight (RSP) · Index fund — no answer, no confidence given

<details><summary><b>News</b> — score n/a</summary>

- [Should Invesco S&P 500 Equal Weight ETF (RSP) Be on Your Investing Radar?](https://finance.yahoo.com/markets/stocks/articles/invesco-p-500-equal-weight-092002654.html)  
  <sub>Yahoo Finance, 5 hours ago</sub>  
  Designed to provide broad exposure to the Large Cap Blend segment of the US equity market, the Invesco S&P 500 Equal Weight ETF (RSP) is a passively managed...
- [The Charts Just Issued a Technical Warning: The S&P 500 Is Losing the Battle](https://www.barchart.com/story/news/4863403/the-charts-just-issued-a-technical-warning-the-s-p-500-is-losing-the-battle)  
  <sub>Barchart.com, 20 hours ago</sub>  
  The RSP ETF should have bulls worried. Very worried.
- [Royal Bank of Canada Announces Accelerated Return Notes Tied to Invesco S&P 500 Equal Weight ETF](https://kalkinemedia.com/us/news/announcements/royal-bank-of-canada-announces-accelerated-return-notes-tied-to-invesco-sp-500-equal-weight-etf)  
  <sub>Kalkine Media, 20 hours ago</sub>  
  On September 29, 2026, Royal Bank of Canada filed a free writing prospectus revealing terms for Accelerated Return Notes linked to the Invesco S&P 500 Equal...
- [Exploring the catalysts driving health and hospital systems’ ETF usage](https://www.invesco.com/us/en/insights/hospital-health-etf-usage.html)  
  <sub>Invesco, 17 hours ago</sub>  
  See how health and hospital systems are putting ETFs to work for cash management, portfolio transitions, tactical views, and core allocations.
- [Form 4 Invesco S&P 500® Equal Weight ETF For: 29 September](https://ng.investing.com/news/stock-market-news/form-4-invesco-sp-500-equal-weight-etf-for-29-september-93CH-2715002)  
  <sub>Investing.com Nigeria, 16 hours ago</sub>  
  Units. $10 principal amount per unit. CUSIP No. Pricing Date*. Settlement Date*. Maturity Date*. October , 2026. November , 2026. October , 2028.
- [Form FWP ROYAL BANK OF CANADA Filed by: ROYAL BANK OF CANADA](https://www.streetinsider.com/SEC+Filings/Form+FWP+ROYAL+BANK+OF+CANADA+Filed+by%3A+ROYAL+BANK+OF+CANADA/27120021.html)  
  <sub>StreetInsider, 23 hours ago</sub>  
  Registration Statement No. 333-275898. Filed Pursuant to Rule 433. ACCELERATED RETURN NOTES<sup>®</sup> (ARNs<sup>®</sup>). Accelerated Return Notes<sup>®</sup> Linked to the Invesco S&P...
- [How I Traded the QQQ ETF for a 20X Gain – and What It Taught Me About Managing Risk](https://www.inkl.com/news/how-i-traded-the-qqq-etf-for-a-20x-gain-and-what-it-taught-me-about-managing-risk)  
  <sub>inkl, 18 hours ago</sub>  
  On Thursday, Sept. 17, 2026, as momentum indicators flashed a short-term oversold condition, I placed a simple tactical trade using short-dated...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score n/a</summary>

```text
US Treasury yields: 3-month 4.03% (+0.00 on the week) | 5-year 5.05% (+0.06 on the week) | 10-year 5.27% (+0.15 on the week) | 30-year 5.62% (+0.22 on the week)
Yield curve, 10-year minus 3-month: +1.24 points -- upward sloping (normal)
US dollar index: 101.27 (+0.17 on the week)
Volatility (VIX): 15.90 (+0.7 on the week) -- elevated
Latest US data: inflation 3.4% (2026-08-01) | unemployment 4.1% (2026-08-01) | jobless claims 197k (2026-09-19)
Policy and expectations: Fed target 4.00% | market expects 2.4% inflation over 10 years
Rate path: 2-year Treasury 4.92% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score n/a</summary>

```text
Last close 209.52 (bar of 2026-09-30), from 502 daily bars
Trend: vs 20d SMA 213.54 (-1.9%), 50d 216.82 (-3.4%), 200d 205.59 (+1.9%); 50d above 200d
Momentum: RSI(14) 32.4 | MACD -2.205 vs signal -1.818 (histogram -0.386)
Returns: 1d +0.0% | 5d -0.8% | 1m -4.5% | 3m -1.8%
52-week range: 182.18 - 222.77 (now 67.4% of the way up)
Volatility: ATR(14) 1.75 (0.8% of price) | annualised 20d 8.9%
Volume: 0.31x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score n/a</summary>

```text
Fund type: Large Blend
What it holds: P/E 21.39 | P/B 3.11 | P/S 1.95 | 3y earnings growth n/a
Yield: 1.5%
Three-year record: +15.7% a year | beta to the market 0.83
Cost and size: expense ratio 0.20% | net assets 100.87B
What it is made of: Stocks 99.9%, Cash 0.1%
Largest holdings: Moderna Inc 0.6%, Veeva Systems Inc Class A 0.3%, Zebra Technologies Corp Ordinary Shares - Class A 0.3%, Charles River Laboratories International Inc 0.3%, DoorDash Inc Ordinary Shares - Class A 0.3%
Sector mix: Technology 17.3%, Industrials 14.7%, Financial services 14.6%, Healthcare 13.1%
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
Rolled up from the 5 largest holdings, 1.8% of the fund by weight  -- thin, so read this as a fact about that slice rather than the fund
Ratings by weight: buy 67.9% | hold 32.1% | sell 0.0% (mean 2.11 on a 1=strong buy to 5=strong sell scale)
Weighted price target: -3.2% above the current prices
Holdings read: MRNA, VEEV, ZBRA, CRL, DASH
Recent rating changes among them:
  - MRNA: 2026-09-30 Citigroup: down, Neutral -> Sell
  - VEEV: 2026-08-28 Citigroup: main, Neutral -> Neutral
  - ZBRA: 2026-09-15 Needham: main, Buy -> Buy
  - CRL: 2026-09-28 Jefferies: main, Buy -> Buy
  - DASH: 2026-09-09 Scotiabank: init, ? -> Sector Outperform
```

</details>

<details><summary><b>Buying and selling by company insiders</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>Who is positioned how</b> — score n/a</summary>

```text
Contract: E-MINI S&P 500 - CHICAGO MERCANTILE EXCHANGE (positions as of 2026-09-22, published the following Friday)
Large speculators: net short 19.9% of open interest (1,890,653 contracts)
Change on the week: -7.9% of open interest
Crowding: 50% percentile over 52 weeks -- within its normal range
Read this as crowding, not as a forecast: an extreme is as often the end of a move as the middle of one.
```

</details>

<details><summary><b>Money going into and out of this fund</b> — score n/a</summary>

```text
Direction: flat (1 week)
Share count change: 1 week: +0.0% (0.00) over 12d
Shares outstanding: 155.55M | fund size: 32.59B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### US inflation-linked bonds (TIP) · Index fund — no answer, no confidence given

<details><summary><b>News</b> — score n/a</summary>

- [TIP5 ETF Holdings List — HAN:TIP5](https://www.tradingview.com/symbols/HAN-TIP5/holdings/)  
  <sub>TradingView, 18 hours ago</sub>  
  Explore Leverage Shares 5x Long TIPS Inflation Protected US Bond ETP holdings with weight, market value, and other helpful data to make more informed...
- [Can a 0.3 Percent Core PCE Print Today Decide Whether the Fed Hikes Again on October 27 to 28?](https://kalkine.ca/news/general-news/can-a-03-percent-core-pce-print-today-decide-whether-the-fed-hikes-again-on-october-27-to-28)  
  <sub>kalkine.ca, 37 minutes ago</sub>  
  You are reading a free article with opinions that may differ from the recommendation given by Kalkine in its paid research reports. Become a Kalkine member...
- [UIMB ETF Holdings List — HAN:UIMB](https://www.tradingview.com/symbols/HAN-UIMB/holdings/)  
  <sub>TradingView, 21 hours ago</sub>  
  Explore UBS (Lux) Fund Solutions - UBS BBG TIPS 10+ UCITS ETF Adis- Distribution holdings with weight, market value, and other helpful data to make more...
- [PPV2 Exploit Remains Active as Users Urged to Revoke Approvals](https://www.tokenpost.com/news/technology/25574)  
  <sub>TOKENPOST, 14 hours ago</sub>  
  A wallet lost 0.15246 WETH after accepting an offer, with nearly all of the funds paid as a tip to Titan Builder.
- [The 10.84% Yield REIT ETF That Pays Monthly Like a Rental Property, Without the Tenants](https://247wallst.com/investing/etf/2026/09/29/the-10-84-yield-reit-etf-that-pays-monthly-like-a-rental-property-without-the-tenants/)  
  <sub>24/7 Wall St., 20 hours ago</sub>  
  Publicly traded REITs currently have an implied cap rate of roughly 5.7% according to Nareit's Q2 2026 data, while direct property ownership introduces...
- [VOO vs. SPY: Are You Picking the Right S&P 500 ETF for the Long Run?](https://www.tipranks.com/news/voo-vs-spy-are-you-picking-the-right-sp-500-etf-for-the-long-run)  
  <sub>TipRanks, 5 hours ago</sub>  
  Vanguard SP 500 ETF ($VOO) and SPDR SP 500 ETF Trust ($SPY) are two of the most popular ETFs that track the SP 500 ($SPX). For long-term investors, V...
- [Want to Play Micron Earnings Without Buying the Stock? This $23B ETF Makes MU Its Largest Holding](https://www.tipranks.com/news/want-to-play-micron-earnings-without-buying-the-stock-this-23b-etf-makes-mu-its-largest-holding)  
  <sub>TipRanks, 49 minutes ago</sub>  
  Micron Technology($MU) will report fiscal fourth-quarter earningsafter the market closes on Wednesday. Investors who want exposure to the memory chip ma...
- [SpaceX Stock Forecast: 2 ETFs to Capture SPCX’s 56% Upside Potential as Cathie Wood Invests $1.3M](https://www.tipranks.com/news/spacex-stock-forecast-2-etfs-to-capture-spcxs-56-upside-potential-as-cathie-wood-invests-1-3m)  
  <sub>TipRanks, 4 hours ago</sub>  
  SpaceX ($SPCX) is one of the most closely watched names in the space sector, with analysts projecting about 56% upside for the stock over the next 12 months...
- [SPDR Dow Jones Industrial Average ETF Trust Announces Interim Distribution Schedule](https://www.tipranks.com/news/company-announcements/spdr-dow-jones-industrial-average-etf-trust-announces-interim-distribution-schedule)  
  <sub>TipRanks, 3 hours ago</sub>  
  SPDR Dow Jones Industrial Average ETF Trust ( ($DIA) ) just unveiled an update. The SPDR Dow Jones Industrial Average ETF Trust has declared an interim cash...
- [UFOX ETF and the Orbital Buildout: Starship Reaches Orbit, Starlink V3 Deploys, and Google’s First AI Satellite Flies on a SpaceX Rocket This Week](https://www.tipranks.com/news/ufox-etf-and-the-orbital-buildout-starship-reaches-orbit-starlink-v3-deploys-and-googles-first-ai-satellite-flies-on-a-spacex-rocket-this-week)  
  <sub>TipRanks, 4 hours ago</sub>  
  Presented by Defiance ETFs On September 28, 2026, SpaceX's ($SPCX) Starship reached orbit for the first time on its 14th test flight,...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score n/a</summary>

```text
US Treasury yields: 3-month 4.03% (+0.00 on the week) | 5-year 5.05% (+0.06 on the week) | 10-year 5.27% (+0.15 on the week) | 30-year 5.62% (+0.22 on the week)
Yield curve, 10-year minus 3-month: +1.24 points -- upward sloping (normal)
US dollar index: 101.27 (+0.17 on the week)
Volatility (VIX): 15.90 (+0.7 on the week) -- elevated
Latest US data: inflation 3.4% (2026-08-01) | unemployment 4.1% (2026-08-01) | jobless claims 197k (2026-09-19)
Policy and expectations: Fed target 4.00% | market expects 2.4% inflation over 10 years
Rate path: 2-year Treasury 4.92% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score n/a</summary>

```text
Last close 104.12 (bar of 2026-09-30), from 502 daily bars
Trend: vs 20d SMA 105.60 (-1.4%), 50d 106.58 (-2.3%), 200d 109.40 (-4.8%); 50d below 200d
Momentum: RSI(14) 27.6 | MACD -0.767 vs signal -0.626 (histogram -0.141)
Returns: 1d +0.1% | 5d -0.7% | 1m -2.5% | 3m -3.7%
52-week range: 104.01 - 112.20 (now 1.3% of the way up)
Volatility: ATR(14) 0.39 (0.4% of price) | annualised 20d 4.8%
Volume: 0.24x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score n/a</summary>

```text
Fund type: Inflation-Protected Bond
Yield: 5.0%
Credit quality: AA 99.9% | US government debt 99.9%
Three-year record: +3.5% a year | beta to the market 0.68
Cost and size: expense ratio 0.18% | net assets 15.01B
What it is made of: Bonds 99.9%, Cash 0.1%
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
Contract: UST 10Y NOTE - CHICAGO BOARD OF TRADE (positions as of 2026-09-22, published the following Friday)
Large speculators: net short 35.6% of open interest (5,407,726 contracts)
Change on the week: -0.9% of open interest
Crowding: 87% percentile over 52 weeks -- within its normal range
Read this as crowding, not as a forecast: an extreme is as often the end of a move as the middle of one.
```

</details>

<details><summary><b>Money going into and out of this fund</b> — score n/a</summary>

```text
Direction: flat (1 week)
Share count change: 1 week: +0.0% (0.00) over 12d
Shares outstanding: 177.70M | fund size: 18.50B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### US government bonds, 20+ years (TLT) · Index fund — no answer, no confidence given

<details><summary><b>News</b> — score n/a</summary>

- [ETF Fund Flows: Defense ETF Takes In Over $700M](https://finance.yahoo.com/markets/stocks/articles/etf-fund-flows-defense-etf-210004693.html)  
  <sub>Yahoo Finance, 18 hours ago</sub>  
  Top 10 Creations (All ETFs). Ticker. Name. Net Flows ($, mm). AUM ($, mm). AUM % Change. IVV · iShares Core S&P 500 ETF. 2,208.01. 890,641.62. 0.25%.
- [US Treasury Yields Hit Two-Decade Highs as Traders Pile Into BlackRock Fixed-Income ETF Options at Record Pace](https://finance.biggo.com/news/e944ccea-3716-4483-a672-3ab9f141af96)  
  <sub>finance.biggo.com, 20 hours ago</sub>  
  US 10-year and 30-year Treasury yields have surged to two-decade highs, prompting traders to flood into fixed-income ETF options at an unprecedented…
- [Discipline and Rules-Based Execution in TLT Response](https://news.stocktradersdaily.com/news_release/139/Discipline_and_Rules-Based_Execution_in_TLT_Response_092926092802_1790731682.html)  
  <sub>Stock Traders Daily, 17 hours ago</sub>  
  Key findings for Ishares 20+ Year Treasury Bond Etf (NYSE: TLT). Weak Near-Term Sentiment Could Catalyze Bearish Positioning; No clear price positioning...
- [30-year U.S. Treasuries have lost 60% of value since 2020, wiping out two decades of gains.](https://pluang.com/en/news-feed/penurunan-harga-obligasi-30-tahun-treasury-hancurkan-keuntungan-dua-dekade)  
  <sub>Pluang, 23 hours ago</sub>  
  The 30-year U.S. Treasury bonds have crashed by 60% since 2020, erasing nearly 20 years of gains due to rising yields and massive government debt issuance.
- [Long-Term Treasuries Could Be a Good Contrarian Bet](https://www.barrons.com/articles/long-term-treasuries-could-be-a-good-contrarian-bet-4247cc19)  
  <sub>Barron's, 7 hours ago</sub>  
  Bonds that mature in 20 to 30 years could offer competitive returns if equity market returns cool.
- [Heavy Bond Pressure Continues to Hurt Stocks](https://pro.thestreet.com/market-commentary/heavy-bond-pressure-continues-to-hurt-stocks)  
  <sub>TheStreet Pro, 23 hours ago</sub>  
  Dismal market action continued on Tuesday morning. The most notable development was new lows in bonds despite oversold technical conditions.
- [The Weekly Spread: What Shaped US Yields And The Dollar This Week](https://stocktwits.com/news-articles/markets/equity/the-weekly-spread-what-shaped-yields-and-the-dollar-this-week-1/cZMXz82RBO8)  
  <sub>Stocktwits, 13 hours ago</sub>  
  U.S. bond yields climbed for the second straight week across the curve, with yields at their highest in over a decade, as hawkish commentary from multiple...
- [Fed rate-hike odds slide after softer PCE inflation print](https://seekingalpha.com/news/4648581-fed-rate-hike-odds-slide-after-softer-pce-inflation-print)  
  <sub>Seeking Alpha, 34 minutes ago</sub>  
  Market-implied chances of a Federal Reserve interest rate increase at the October 28–29 FOMC meeting fell sharply to 34.9% after Wednesday's personal...
- [Best Performing ETFs: Top Returns at a Glance](https://www.tradingkey.com/markets/etf/best-performing)  
  <sub>TradingKey, 19 hours ago</sub>  
  View TradingKey's list of the best performing ETFs, including price changes, trading volume, multi-period returns, and performance charts.
- [Horizon over which FOMC can achieve dual mandate could be communicated: St. Louis Fed's Musalem (TLT:NASDAQ)](https://seekingalpha.com/news/4648153-horizon-over-which-fomc-can-achieve-dual-mandate-could-be-communicated-st-louis-feds-musalem)  
  <sub>Seeking Alpha, 21 hours ago</sub>  
  The horizon over which the Federal Open Market Committee expects to achieve mandate-consistent levels of inflation and employment could be a useful...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score n/a</summary>

```text
US Treasury yields: 3-month 4.03% (+0.00 on the week) | 5-year 5.05% (+0.06 on the week) | 10-year 5.27% (+0.15 on the week) | 30-year 5.62% (+0.22 on the week)
Yield curve, 10-year minus 3-month: +1.24 points -- upward sloping (normal)
US dollar index: 101.27 (+0.17 on the week)
Volatility (VIX): 15.90 (+0.7 on the week) -- elevated
Latest US data: inflation 3.4% (2026-08-01) | unemployment 4.1% (2026-08-01) | jobless claims 197k (2026-09-19)
Policy and expectations: Fed target 4.00% | market expects 2.4% inflation over 10 years
Rate path: 2-year Treasury 4.92% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score n/a</summary>

```text
Last close 77.92 (bar of 2026-09-30), from 502 daily bars
Trend: vs 20d SMA 80.74 (-3.5%), 50d 81.90 (-4.9%), 200d 85.52 (-8.9%); 50d below 200d
Momentum: RSI(14) 25.3 | MACD -1.007 vs signal -0.696 (histogram -0.311)
Returns: 1d -0.4% | 5d -3.2% | 1m -5.6% | 3m -8.9%
52-week range: 77.92 - 92.06 (now 0.0% of the way up)
Volatility: ATR(14) 0.75 (1.0% of price) | annualised 20d 10.4%
Volume: 0.42x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score n/a</summary>

```text
Fund type: Long Government
Yield: 4.7%
Credit quality: AA 100.0% | US government debt 99.6%
Three-year record: +0.2% a year | beta to the market 2.39
Cost and size: expense ratio 0.15% | net assets 47.05B
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
Contract: ULTRA UST BOND - CHICAGO BOARD OF TRADE (positions as of 2026-09-22, published the following Friday)
Large speculators: net short 33.3% of open interest (2,476,197 contracts)
Change on the week: -0.4% of open interest
Crowding: 50% percentile over 52 weeks -- within its normal range
Read this as crowding, not as a forecast: an extreme is as often the end of a move as the middle of one.
```

</details>

<details><summary><b>Money going into and out of this fund</b> — score n/a</summary>

```text
Direction: flat (1 week)
Share count change: 1 week: +0.0% (0.00) over 7d
Shares outstanding: 109.70M | fund size: 8.55B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### US dollar (UUP) · Index fund — no answer, no confidence given

<details><summary><b>News</b> — score n/a</summary>

- [UUP: A Broad Dollar Signal From FX Swap Points Analysis (NYSEARCA:UUP)](https://seekingalpha.com/article/4950798-uup-a-broad-dollar-signal-from-fx-swap-points-analysis)  
  <sub>Seeking Alpha, 18 hours ago</sub>  
  The Invesco DB US Dollar Index Bullish Fund ETF is positioned for continued US dollar appreciation, supported by swap-point analysis. Click for more on UUP.
- [Soybean price analysis: Here’s what to expect with US PCE, NFP in focus](https://invezz.com/au/news/2026/09/29/soybean-price-analysis-heres-what-to-expect-with-us-pce-nfp-in-focus/)  
  <sub>Invezz, 17 hours ago</sub>  
  Soybean price hovered near the short-term MA while holding steady above the medium-term MA. The choppy market has been fueled by the opposing forces of a...
- [Copper price analysis: forecast as rally loses momentum ahead of key events](https://invezz.com/au/news/2026/09/29/copper-price-analysis-forecast-as-rally-loses-momentum-ahead-of-key-events/)  
  <sub>Invezz, 17 hours ago</sub>  
  Copper prices have been on selling pressure in recent sessions as profit-taking influences momentum. While the bulls are still in control, choppy trading is...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score n/a</summary>

```text
US Treasury yields: 3-month 4.03% (+0.00 on the week) | 5-year 5.05% (+0.06 on the week) | 10-year 5.27% (+0.15 on the week) | 30-year 5.62% (+0.22 on the week)
Yield curve, 10-year minus 3-month: +1.24 points -- upward sloping (normal)
US dollar index: 101.27 (+0.17 on the week)
Volatility (VIX): 15.90 (+0.7 on the week) -- elevated
Latest US data: inflation 3.4% (2026-08-01) | unemployment 4.1% (2026-08-01) | jobless claims 197k (2026-09-19)
Policy and expectations: Fed target 4.00% | market expects 2.4% inflation over 10 years
Rate path: 2-year Treasury 4.92% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score n/a</summary>

```text
Last close 28.73 (bar of 2026-09-30), from 502 daily bars
Trend: vs 20d SMA 28.35 (+1.3%), 50d 28.25 (+1.7%), 200d 27.74 (+3.5%); 50d above 200d
Momentum: RSI(14) 70.3 | MACD 0.159 vs signal 0.112 (histogram 0.048)
Returns: 1d -0.1% | 5d +0.3% | 1m +2.2% | 3m +0.8%
52-week range: 26.47 - 28.75 (now 98.9% of the way up)
Volatility: ATR(14) 0.10 (0.4% of price) | annualised 20d 4.6%
Volume: 0.12x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score n/a</summary>

```text
Fund type: Trading--Miscellaneous
What it holds: P/E n/a | P/B 0.00 | P/S 0.00 | 3y earnings growth n/a
Yield: 3.3%
Three-year record: +3.6% a year | beta to the market -9.48
Cost and size: expense ratio 0.75% | net assets 298.71M
What it is made of: Cash 100.0%
Largest holdings: Invesco Shrt-Trm Inv Gov&Agcy Instl 48.8%
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
Rolled up from the 1 largest holdings, 48.8% of the fund by weight
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
Contract: USD INDEX - ICE FUTURES U.S. (positions as of 2026-09-22, published the following Friday)
Large speculators: net short 9.7% of open interest (46,328 contracts)
Change on the week: +1.5% of open interest
Crowding: 58% percentile over 52 weeks -- within its normal range
Read this as crowding, not as a forecast: an extreme is as often the end of a move as the middle of one.
```

</details>

<details><summary><b>Money going into and out of this fund</b> — score n/a</summary>

```text
Direction: money going out (1 week)
Share count change: 1 week: -0.8% (-2.54M) over 7d
Shares outstanding: 10.44M | fund size: 299.80M
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

## Sector and country funds

### Argentina (ARGT) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:** no explanation. It wrote only “NEUTRAL”, so the main reasons below are all it gave.

**Main reasons it gave:**
- US Treasury yields rose modestly (10y +0.15% week) with no policy surprise
- Technical indicators show price below 20d, 50d, 200d SMAs, RSI 26.3, low volume
- Share count increased 4.3% over the week, indicating net inflows
- Analyst coverage: 100% buy, weighted price target +39.1% above current

<details><summary><b>News</b> — score +0.00</summary>

- [Technical Reactions to ARGT Trends in Macro Strategies](https://news.stocktradersdaily.com/news_release/134/Technical_Reactions_to_ARGT_Trends_in_Macro_Strategies_093026055001_1790761801.html)  
  <sub>Stock Traders Daily, 9 hours ago</sub>  
  Key findings for Global X Msci Argentina Etf (NASDAQ: ARGT). Weak Near and Mid-Term Sentiment Could Challenge Long-Term Positive Outlook...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.03% (+0.00 on the week) | 5-year 5.05% (+0.06 on the week) | 10-year 5.27% (+0.15 on the week) | 30-year 5.62% (+0.22 on the week)
Yield curve, 10-year minus 3-month: +1.24 points -- upward sloping (normal)
US dollar index: 101.27 (+0.17 on the week)
Volatility (VIX): 15.90 (+0.7 on the week) -- elevated
Latest US data: inflation 3.4% (2026-08-01) | unemployment 4.1% (2026-08-01) | jobless claims 197k (2026-09-19)
Policy and expectations: Fed target 4.00% | market expects 2.4% inflation over 10 years
Rate path: 2-year Treasury 4.92% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 86.25 (bar of 2026-09-30), from 502 daily bars
Trend: vs 20d SMA 92.92 (-7.2%), 50d 93.21 (-7.5%), 200d 92.63 (-6.9%); 50d above 200d
Momentum: RSI(14) 26.3 | MACD -1.905 vs signal -0.939 (histogram -0.966)
Returns: 1d +0.2% | 5d -5.3% | 1m -8.8% | 3m -5.3%
52-week range: 67.55 - 102.94 (now 52.8% of the way up)
Volatility: ATR(14) 1.77 (2.1% of price) | annualised 20d 18.2%
Volume: 0.25x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.20</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score +0.20</summary>

```text
Fund type: Focused Region
What it holds: P/E 15.48 | P/B 1.77 | P/S 1.36 | 3y earnings growth n/a
Yield: 1.1%
Three-year record: +28.9% a year | beta to the market 0.50
Cost and size: expense ratio 0.59% | net assets 815.33M
What it is made of: Stocks 99.9%, Cash 0.1%
Largest holdings: MercadoLibre Inc 25.4%, YPF SA ADR 9.5%, Vista Energy SAB de CV ADR 6.2%, Grupo Financiero Galicia SA ADR 5.6%, Banco Macro SA ADR 4.3%
Sector mix: Consumer cyclical 30.4%, Energy 19.4%, Financial services 14.4%, Basic materials 12.0%
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
Rolled up from the 5 largest holdings, 51.1% of the fund by weight
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 1.62 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +39.1% above the current prices
Holdings read: MELI, YPF, VIST, GGAL, BMA
Recent rating changes among them:
  - MELI: 2026-09-03 BTIG: reit, Buy -> Buy
  - YPF: 2026-09-01 JP Morgan: main, Overweight -> Overweight
  - VIST: 2026-09-01 JP Morgan: main, Overweight -> Overweight
  - GGAL: 2026-06-25 JP Morgan: main, Overweight -> Overweight
  - BMA: 2026-06-25 JP Morgan: main, Overweight -> Overweight
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
Direction: money coming in (1 week)
Share count change: 1 week: +4.3% (32.57M) over 7d
Shares outstanding: 9.19M | fund size: 792.81M
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Israel (EIS) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Neutral overall as no material macro surprise or decisive technical break; analyst view bullish but limited coverage, technicals slightly bearish, flows flat.

**Main reasons it gave:**
- Analyst view: 100% buy rating on 37.6% of fund, weighted price target +22% above current prices
- Technical indicators: price below 20‑day, 50‑day, 200‑day SMAs; RSI 43.3; MACD negative, indicating slight bearish momentum
- Fund flows: flat share count change (0% over 1 week), indicating no net demand
- Macro environment: yields modestly higher, VIX low, no surprise data or policy shift

<details><summary><b>News</b> — score +0.00</summary>

- [ISRL Archives](https://247wallst.com/companies/isrl/)  
  <sub>24/7 Wall St., 7 hours ago</sub>  
  Defiance KSM Israel 120 ETF (ISRL) stock news, price prediction, earnings and analysis from 24/7 Wall St. Israel Acquisitions Corp is a company based in…

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.03% (+0.00 on the week) | 5-year 5.05% (+0.06 on the week) | 10-year 5.27% (+0.15 on the week) | 30-year 5.62% (+0.22 on the week)
Yield curve, 10-year minus 3-month: +1.24 points -- upward sloping (normal)
US dollar index: 101.27 (+0.17 on the week)
Volatility (VIX): 15.90 (+0.7 on the week) -- elevated
Latest US data: inflation 3.4% (2026-08-01) | unemployment 4.1% (2026-08-01) | jobless claims 197k (2026-09-19)
Policy and expectations: Fed target 4.00% | market expects 2.4% inflation over 10 years
Rate path: 2-year Treasury 4.92% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score -0.20</summary>

```text
Last close 121.26 (bar of 2026-09-30), from 502 daily bars
Trend: vs 20d SMA 124.04 (-2.2%), 50d 122.53 (-1.0%), 200d 122.46 (-1.0%); 50d above 200d
Momentum: RSI(14) 43.3 | MACD -0.211 vs signal 0.293 (histogram -0.504)
Returns: 1d -0.1% | 5d -2.9% | 1m -1.3% | 3m +0.5%
52-week range: 97.88 - 137.69 (now 58.7% of the way up)
Volatility: ATR(14) 1.73 (1.4% of price) | annualised 20d 20.5%
Volume: 0.23x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.30</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score +0.30</summary>

```text
Fund type: Focused Region
What it holds: P/E 17.89 | P/B 2.43 | P/S 2.45 | 3y earnings growth n/a
Yield: 1.5%
Three-year record: +32.6% a year | beta to the market 1.07
Cost and size: expense ratio 0.59% | net assets 897.28M
What it is made of: Stocks 99.5%, Cash 0.5%
Largest holdings: Teva Pharmaceutical Industries Ltd ADR 10.1%, Bank Leumi Le-Israel BM 9.0%, Bank Hapoalim BM 8.1%, Tower Semiconductor Ltd 5.5%, Elbit Systems Ltd 4.8%
Sector mix: Financial services 36.1%, Technology 18.1%, Healthcare 10.7%, Industrials 10.0%
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
Rolled up from the 5 largest holdings, 37.6% of the fund by weight
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 1.27 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +22.0% above the current prices
Holdings read: TEVA, LUMI.TA, POLI.TA, TSEM.TA, ESLT.TA
Recent rating changes among them:
  - TEVA: 2026-09-23 Oppenheimer: init, ? -> Outperform
  - TSEM.TA: 2026-09-25 Mizuho: init, ? -> Outperform
  - ESLT.TA: 2026-08-19 JP Morgan: main, Neutral -> Neutral
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
Direction: flat (1 week)
Share count change: 1 week: +0.0% (0.00) over 7d
Shares outstanding: 2.55M | fund size: 309.21M
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Poland (EPOL) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> No macro surprise, no decisive technical breakout, modest outflows offset by strong analyst buy consensus and solid fundamentals.

**Main reasons it gave:**
- Fund flows: -0.6% share count (outflows) over 1 week
- Analyst consensus: 90.3% buy, price target +0.2% above current price
- Technicals: price near 52‑week high, MACD histogram negative, volume 0.29× 20‑day average
- Macro: US Treasury yields modestly higher, VIX low, no policy surprise

<details><summary><b>News</b> — score +0.00</summary>

- [ETFs Investing in TAURON Polska Energia S.A. Stocks](https://www.tradingview.com/symbols/HAN-1T5/etfs/)  
  <sub>TradingView, 20 hours ago</sub>  
  Explore funds investing in 1T5 in a single list with price, expense ratio, and more stats for an in-depth analysis of new opportunities.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.03% (+0.00 on the week) | 5-year 5.05% (+0.06 on the week) | 10-year 5.27% (+0.15 on the week) | 30-year 5.62% (+0.22 on the week)
Yield curve, 10-year minus 3-month: +1.24 points -- upward sloping (normal)
US dollar index: 101.27 (+0.17 on the week)
Volatility (VIX): 15.90 (+0.7 on the week) -- elevated
Latest US data: inflation 3.4% (2026-08-01) | unemployment 4.1% (2026-08-01) | jobless claims 197k (2026-09-19)
Policy and expectations: Fed target 4.00% | market expects 2.4% inflation over 10 years
Rate path: 2-year Treasury 4.92% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 44.63 (bar of 2026-09-30), from 502 daily bars
Trend: vs 20d SMA 44.90 (-0.6%), 50d 44.02 (+1.4%), 200d 39.44 (+13.2%); 50d above 200d
Momentum: RSI(14) 51.0 | MACD 0.180 vs signal 0.322 (histogram -0.142)
Returns: 1d +1.0% | 5d +0.1% | 1m +1.2% | 3m +15.4%
52-week range: 31.78 - 45.76 (now 92.0% of the way up)
Volatility: ATR(14) 0.66 (1.5% of price) | annualised 20d 19.3%
Volume: 0.29x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.35</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score +0.35</summary>

```text
Fund type: Focused Region
What it holds: P/E 13.47 | P/B 2.00 | P/S 1.36 | 3y earnings growth n/a
Yield: 3.3%
Three-year record: +45.2% a year | beta to the market 0.73
Cost and size: expense ratio 0.59% | net assets 848.26M
What it is made of: Stocks 99.3%, Cash 0.7%
Largest holdings: PKO Bank Polski SA 15.4%, Orlen SA 13.8%, Bank Polska Kasa Opieki SA 7.1%, Powszechny Zaklad Ubezpieczen SA 6.4%, KGHM Polska Miedz SA 4.6%
Sector mix: Financial services 46.1%, Energy 14.5%, Consumer cyclical 12.7%, Basic materials 6.8%
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
Rolled up from the 5 largest holdings, 47.4% of the fund by weight
Ratings by weight: buy 90.3% | hold 9.7% | sell 0.0% (mean 2.32 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +0.2% above the current prices
Holdings read: PKO.WA, PKN.WA, PEO.WA, PZU.WA, KGH.WA
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
Direction: money going out (1 week)
Share count change: 1 week: -0.6% (-4.98M) over 7d
Shares outstanding: 18.97M | fund size: 846.91M
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Australia (EWA) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Neutral overall; no macro surprise, flat fund flows, moderate bearish analyst view but not enough to shift stance, technicals not decisive.

**Main reasons it gave:**
- Australian August inflation rose to 4.0%, slightly below expectations (no surprise)
- US Treasury yields rose modestly; 10‑yr minus 3‑mo spread +1.24 points (normal upward slope)
- Analyst ratings for top holdings: 40.4% sell, weighted price target -6.1% vs current price
- Technical: price below 20‑day (29.08) and 50‑day (29.46) SMAs, RSI 40.8, MACD negative but no decisive break
- Fund flows flat over past week; share count unchanged

<details><summary><b>News</b> — score +0.00</summary>

- [Australia's August inflation rises to 4.0%, slightly below expectations](https://www.tradingview.com/news/seekingalpha:c28ac86bb094b:0-australia-s-august-inflation-rises-to-4-0-slightly-below-expectations/)  
  <sub>TradingView, 11 hours ago</sub>  
  Australia's annual inflation rate accelerated to a three-month high of 4.0% in August 2026, up from 3.5% in July, driven primarily by surging transport...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.03% (+0.00 on the week) | 5-year 5.05% (+0.06 on the week) | 10-year 5.27% (+0.15 on the week) | 30-year 5.62% (+0.22 on the week)
Yield curve, 10-year minus 3-month: +1.24 points -- upward sloping (normal)
US dollar index: 101.27 (+0.17 on the week)
Volatility (VIX): 15.90 (+0.7 on the week) -- elevated
Latest US data: inflation 3.4% (2026-08-01) | unemployment 4.1% (2026-08-01) | jobless claims 197k (2026-09-19)
Policy and expectations: Fed target 4.00% | market expects 2.4% inflation over 10 years
Rate path: 2-year Treasury 4.92% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score -0.20</summary>

```text
Last close 28.48 (bar of 2026-09-30), from 502 daily bars
Trend: vs 20d SMA 29.08 (-2.0%), 50d 29.46 (-3.3%), 200d 28.62 (-0.5%); 50d above 200d
Momentum: RSI(14) 40.8 | MACD -0.334 vs signal -0.268 (histogram -0.066)
Returns: 1d +0.4% | 5d +0.4% | 1m -5.1% | 3m +2.8%
52-week range: 24.95 - 30.43 (now 64.4% of the way up)
Volatility: ATR(14) 0.36 (1.3% of price) | annualised 20d 18.4%
Volume: 0.35x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.00</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score +0.00</summary>

```text
Fund type: Focused Region
What it holds: P/E 21.06 | P/B 2.81 | P/S 3.39 | 3y earnings growth n/a
Yield: 2.8%
Three-year record: +13.4% a year | beta to the market 0.96
Cost and size: expense ratio 0.50% | net assets 1.33B
What it is made of: Stocks 99.5%, Cash 0.5%
Largest holdings: BHP Group Ltd 16.3%, Commonwealth Bank of Australia 13.0%, National Australia Bank Ltd 5.9%, Westpac Banking Corp 5.7%, ANZ Group Holdings Ltd 5.5%
Sector mix: Financial services 41.1%, Basic materials 26.7%, Consumer cyclical 6.5%, Healthcare 5.2%
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
Rolled up from the 5 largest holdings, 46.4% of the fund by weight
Ratings by weight: buy 0.0% | hold 59.6% | sell 40.4% (mean 3.48 on a 1=strong buy to 5=strong sell scale)
Weighted price target: -6.1% above the current prices
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
Direction: flat (1 week)
Share count change: 1 week: +0.0% (0.00) over 12d
Shares outstanding: 63.60M | fund size: 1.81B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Canada (EWC) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Overall neutral: analyst view modestly bullish (+6% price target, 74% buy), but technicals show weak short‑term momentum (price below 20‑day/50‑day SMAs, RSI 34.4, MACD negative) and fund flows are flat. Macro environment shows modest yield rise with no surprise, and VIX is low. News of strong inflows into single‑country ETFs is positive but not enough to tip the balance.

**Main reasons it gave:**
- Analyst view: 74.3% buy rating and weighted price target +6% (moderate bullish)
- Technicals: price below 20‑day and 50‑day SMAs, RSI 34.4, MACD negative (weak momentum)
- Fund flows: flat share count over the past week (no net demand)
- Macro: modest rise in Treasury yields, no policy surprise; VIX low (neutral environment)
- News: single‑country ETFs have attracted $26B YTD, indicating strong demand for Canada exposure

<details><summary><b>News</b> — score +0.00</summary>

- [Single-country ETFs surge as investors target AI, reform plays](https://www.investmentnews.com/etfs/single-country-etfs-surge-as-investors-target-ai-reform-plays/268410)  
  <sub>InvestmentNews, 4 hours ago</sub>  
  US-listed single-country ETFs have pulled in over $26 billion year-to-date, more than four times their full-year 2025 haul, TD Securities data shows.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.03% (+0.00 on the week) | 5-year 5.05% (+0.06 on the week) | 10-year 5.27% (+0.15 on the week) | 30-year 5.62% (+0.22 on the week)
Yield curve, 10-year minus 3-month: +1.24 points -- upward sloping (normal)
US dollar index: 101.27 (+0.17 on the week)
Volatility (VIX): 15.90 (+0.7 on the week) -- elevated
Latest US data: inflation 3.4% (2026-08-01) | unemployment 4.1% (2026-08-01) | jobless claims 197k (2026-09-19)
Policy and expectations: Fed target 4.00% | market expects 2.4% inflation over 10 years
Rate path: 2-year Treasury 4.92% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score -0.20</summary>

```text
Last close 58.71 (bar of 2026-09-30), from 502 daily bars
Trend: vs 20d SMA 60.35 (-2.7%), 50d 60.72 (-3.3%), 200d 57.68 (+1.8%); 50d above 200d
Momentum: RSI(14) 34.4 | MACD -0.538 vs signal -0.332 (histogram -0.206)
Returns: 1d -0.4% | 5d -1.6% | 1m -4.4% | 3m +1.8%
52-week range: 49.72 - 62.64 (now 69.6% of the way up)
Volatility: ATR(14) 0.64 (1.1% of price) | annualised 20d 13.9%
Volume: 0.22x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.20</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score +0.20</summary>

```text
Fund type: Focused Region
What it holds: P/E 19.49 | P/B 2.83 | P/S 2.79 | 3y earnings growth n/a
Yield: 1.2%
Three-year record: +22.8% a year | beta to the market 0.79
Cost and size: expense ratio 0.50% | net assets 6.85B
What it is made of: Stocks 99.8%, Cash 0.2%
Largest holdings: Royal Bank of Canada 9.0%, The Toronto-Dominion Bank 6.3%, Shopify Inc Registered Shs -A- Subord Vtg 5.7%, Bank of Montreal 3.7%, Bank of Nova Scotia 3.6%
Sector mix: Financial services 39.2%, Energy 17.9%, Basic materials 16.1%, Industrials 8.8%
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
Rolled up from the 5 largest holdings, 28.3% of the fund by weight
Ratings by weight: buy 74.3% | hold 25.7% | sell 0.0% (mean 2.20 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +6.0% above the current prices
Holdings read: RY, TD, SHOP, BMO.TO, BNS.TO
Recent rating changes among them:
  - RY: 2025-08-29 Argus Research: main, Buy -> Buy
  - TD: 2026-06-01 RBC Capital: main, Outperform -> Outperform
  - SHOP: 2026-09-23 Wedbush: reit, Outperform -> Outperform
  - BMO.TO: 2026-05-28 RBC Capital: main, Sector Perform -> Sector Perform
  - BNS.TO: 2026-05-28 RBC Capital: main, Sector Perform -> Sector Perform
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
Direction: flat (1 week)
Share count change: 1 week: +0.0% (0.00) over 12d
Shares outstanding: 94.80M | fund size: 5.57B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Sweden (EWD) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Neutral overall – no material macro surprise, technicals are weak but not decisive, analyst view is bullish but limited to ~30% of the fund, and flows are flat.

**Main reasons it gave:**
- Price below 20‑day, 50‑day and 200‑day SMAs (50.50 vs 51.72/52.28/51.38) with RSI 38.8 and volume 0.06× 20‑day average
- Analyst coverage 29.5% of fund, 82.1% buy rating, weighted price target +11.9% above current price
- Fund flows flat (share count change +0.0% over 12 days), indicating no net demand

<details><summary><b>News</b> — score +0.00</summary>

_No news found for this one today._

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.03% (+0.00 on the week) | 5-year 5.05% (+0.06 on the week) | 10-year 5.27% (+0.15 on the week) | 30-year 5.62% (+0.22 on the week)
Yield curve, 10-year minus 3-month: +1.24 points -- upward sloping (normal)
US dollar index: 101.27 (+0.17 on the week)
Volatility (VIX): 15.90 (+0.7 on the week) -- elevated
Latest US data: inflation 3.4% (2026-08-01) | unemployment 4.1% (2026-08-01) | jobless claims 197k (2026-09-19)
Policy and expectations: Fed target 4.00% | market expects 2.4% inflation over 10 years
Rate path: 2-year Treasury 4.92% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score -0.20</summary>

```text
Last close 50.50 (bar of 2026-09-30), from 502 daily bars
Trend: vs 20d SMA 51.72 (-2.4%), 50d 52.28 (-3.4%), 200d 51.38 (-1.7%); 50d above 200d
Momentum: RSI(14) 38.8 | MACD -0.459 vs signal -0.333 (histogram -0.126)
Returns: 1d -0.2% | 5d -1.6% | 1m -5.4% | 3m +1.7%
52-week range: 45.38 - 54.72 (now 54.8% of the way up)
Volatility: ATR(14) 0.69 (1.4% of price) | annualised 20d 15.4%
Volume: 0.06x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.00</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score +0.00</summary>

```text
Fund type: Focused Region
What it holds: P/E 14.99 | P/B 2.88 | P/S 2.90 | 3y earnings growth n/a
Yield: 3.4%
Three-year record: +19.6% a year | beta to the market 1.19
Cost and size: expense ratio 0.51% | net assets 755.74M
What it is made of: Stocks 98.9%, Cash 1.1%
Largest holdings: Spotify Technology SA 10.2%, Investor AB Class B 9.5%, Volvo AB Class B 7.1%, Atlas Copco AB Class A 6.9%, Sandvik AB 5.3%
Sector mix: Industrials 46.0%, Financial services 24.9%, Communication services 13.9%, Technology 6.2%
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
Rolled up from the 4 largest holdings, 29.5% of the fund by weight
Ratings by weight: buy 82.1% | hold 17.9% | sell 0.0% (mean 1.97 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +11.9% above the current prices
Holdings read: SPOT, VOLV-B.ST, ATCO-A.ST, SAND.ST
Recent rating changes among them:
  - SPOT: 2026-09-29 Evercore ISI Group: main, Outperform -> Outperform
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
Direction: flat (1 week)
Share count change: 1 week: +0.0% (0.00) over 12d
Shares outstanding: 7.65M | fund size: 386.32M
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Germany (EWG) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Neutral overall: bullish analyst coverage is offset by bearish technicals and flat fund flows, while macro data remain stable and fundamentals are moderate.

**Main reasons it gave:**
- Flat fund flows (0.0% change) indicating no net demand
- Technical indicators bearish: price below 20‑day, 50‑day, and 200‑day SMAs; RSI 34.9; MACD negative
- Analyst coverage bullish: 78% buy, price target +17.4% above current price
- Macro data stable: yields modestly higher, VIX low (15.9), inflation 3.4% near target

<details><summary><b>News</b> — score +0.00</summary>

_No news found for this one today._

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.03% (+0.00 on the week) | 5-year 5.05% (+0.06 on the week) | 10-year 5.27% (+0.15 on the week) | 30-year 5.62% (+0.22 on the week)
Yield curve, 10-year minus 3-month: +1.24 points -- upward sloping (normal)
US dollar index: 101.27 (+0.17 on the week)
Volatility (VIX): 15.90 (+0.7 on the week) -- elevated
Latest US data: inflation 3.4% (2026-08-01) | unemployment 4.1% (2026-08-01) | jobless claims 197k (2026-09-19)
Policy and expectations: Fed target 4.00% | market expects 2.4% inflation over 10 years
Rate path: 2-year Treasury 4.92% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score -0.30</summary>

```text
Last close 41.55 (bar of 2026-09-30), from 502 daily bars
Trend: vs 20d SMA 42.64 (-2.6%), 50d 43.10 (-3.6%), 200d 42.39 (-2.0%); 50d above 200d
Momentum: RSI(14) 34.9 | MACD -0.417 vs signal -0.313 (histogram -0.104)
Returns: 1d -0.8% | 5d -0.8% | 1m -6.1% | 3m +0.8%
52-week range: 38.08 - 44.59 (now 53.3% of the way up)
Volatility: ATR(14) 0.47 (1.1% of price) | annualised 20d 12.6%
Volume: 0.19x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.20</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score +0.20</summary>

```text
Fund type: Focused Region
What it holds: P/E 18.40 | P/B 1.94 | P/S 1.28 | 3y earnings growth n/a
Yield: 1.9%
Three-year record: +19.7% a year | beta to the market 0.98
Cost and size: expense ratio 0.49% | net assets 1.82B
What it is made of: Stocks 99.8%, Cash 0.2%
Largest holdings: Siemens AG 12.1%, SAP SE 11.3%, Allianz SE 10.0%, Siemens Energy AG Ordinary Shares 6.4%, Deutsche Telekom AG 5.6%
Sector mix: Industrials 28.7%, Financial services 23.2%, Technology 15.9%, Consumer cyclical 7.4%
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
Rolled up from the 5 largest holdings, 45.5% of the fund by weight
Ratings by weight: buy 78.0% | hold 22.0% | sell 0.0% (mean 1.87 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +17.4% above the current prices
Holdings read: SIE.DE, SAP.DE, ALV.DE, ENR.DE, DTE.DE
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
Direction: flat (1 week)
Share count change: 1 week: +0.0% (0.00) over 7d
Shares outstanding: 79.50M | fund size: 3.30B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Italy (EWI) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Neutral overall: no macro surprise, flat fund flows, mixed technicals, and strong but limited analyst coverage.

**Main reasons it gave:**
- Flat fund flows (0% share count change) indicating no net demand
- Analyst coverage of 50.9% of fund weighted all buy with +12.8% price target
- Technicals: price below 20‑day and 50‑day SMA, RSI 35.7 (oversold), low volume
- Macro: no surprise in rates or data, yields modestly up, VIX low

<details><summary><b>News</b> — score +0.00</summary>

- [EWI: Capturing Italy's Banking And Infrastructure Investment Cycle (NYSEARCA:EWI)](https://seekingalpha.com/article/4950867-ewi-capturing-italys-banking-and-infrastructure-investment-cycle)  
  <sub>Seeking Alpha, 10 hours ago</sub>  
  EWI's performance is driven by Italian banking consolidation, EU recovery investments, and European defense and energy spending. See why EWI ETF is a Buy.
- [iShares MSCI Italy ETF offers value amid sector consolidation and EU investments despite Italy's slow growth](https://pluang.com/en/news-feed/menangkap-siklus-investasi-perbankan-dan-infrastruktur-italia)  
  <sub>Pluang, 9 hours ago</sub>  
  The iShares MSCI Italy ETF (EWI) provides focused exposure to Italian financials, utilities, and industrial sectors, benefiting from banking consolidation...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.03% (+0.00 on the week) | 5-year 5.05% (+0.06 on the week) | 10-year 5.27% (+0.15 on the week) | 30-year 5.62% (+0.22 on the week)
Yield curve, 10-year minus 3-month: +1.24 points -- upward sloping (normal)
US dollar index: 101.27 (+0.17 on the week)
Volatility (VIX): 15.90 (+0.7 on the week) -- elevated
Latest US data: inflation 3.4% (2026-08-01) | unemployment 4.1% (2026-08-01) | jobless claims 197k (2026-09-19)
Policy and expectations: Fed target 4.00% | market expects 2.4% inflation over 10 years
Rate path: 2-year Treasury 4.92% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 59.12 (bar of 2026-09-30), from 502 daily bars
Trend: vs 20d SMA 60.77 (-2.7%), 50d 61.66 (-4.1%), 200d 57.97 (+2.0%); 50d above 200d
Momentum: RSI(14) 35.7 | MACD -0.598 vs signal -0.448 (histogram -0.150)
Returns: 1d -0.8% | 5d -1.4% | 1m -5.1% | 3m -0.0%
52-week range: 50.31 - 63.35 (now 67.6% of the way up)
Volatility: ATR(14) 0.72 (1.2% of price) | annualised 20d 16.1%
Volume: 0.12x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.20</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score +0.20</summary>

```text
Fund type: Focused Region
What it holds: P/E 15.25 | P/B 1.85 | P/S 1.64 | 3y earnings growth n/a
Yield: 3.0%
Three-year record: +29.8% a year | beta to the market 0.88
Cost and size: expense ratio 0.50% | net assets 1.13B
What it is made of: Stocks 99.8%, Cash 0.2%
Largest holdings: UniCredit SpA 16.8%, Intesa Sanpaolo 13.6%, Enel SpA 10.3%, Ferrari NV 5.2%, Eni SpA 5.0%
Sector mix: Financial services 52.6%, Utilities 16.3%, Industrials 9.7%, Consumer cyclical 9.0%
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
Rolled up from the 5 largest holdings, 50.9% of the fund by weight
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 2.02 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +12.8% above the current prices
Holdings read: UCG.MI, ISP.MI, ENEL.MI, RACE.MI, ENI.MI
Recent rating changes among them:
  - RACE.MI: 2026-09-30 Morgan Stanley: main, Overweight -> Overweight
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
Direction: flat (1 week)
Share count change: 1 week: +0.0% (0.00) over 12d
Shares outstanding: 8.55M | fund size: 505.52M
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Japan (EWJ) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> No macro surprise, modest net long decreasing, thin analyst coverage, technicals not decisive, flat fund flows.

**Main reasons it gave:**
- Analyst coverage only 17% of fund, all buy with +16.5% price target
- Net long 3.6% of open interest, down 0.7% week-over-week
- Technical trend above 20d, 50d, 200d SMAs but MACD histogram negative
- Macro data unchanged; yields up modestly, no surprise
- Fund flows flat; share count unchanged

<details><summary><b>News</b> — score +0.00</summary>

- [5 International ETFs Up at Least 20% in 2026 & Beating the S&P 500](https://www.tradingview.com/news/zacks:89dcd6767094b:0-5-international-etfs-up-at-least-20-in-2026-beating-the-s-p-500/)  
  <sub>TradingView, 4 hours ago</sub>  
  Wall Street has been in solid shape so far this year. State Street SPDR S&P 500 ETF Trust SPY has gained 12.1% while the tech-heavy Nasdaq-100 ETF Invesco...
- [Single-country ETFs surge as investors target AI, reform plays](https://www.investmentnews.com/etfs/single-country-etfs-surge-as-investors-target-ai-reform-plays/268410)  
  <sub>InvestmentNews, 4 hours ago</sub>  
  US-listed single-country ETFs have pulled in over $26 billion year-to-date, more than four times their full-year 2025 haul, TD Securities data shows.
- [How Can a Japan ETF Move When Japan’s Stock Market Is Closed?](https://www.ebc.com/forex/japan-etf-move-when-stock-market-closed)  
  <sub>EBC Financial Group, 5 hours ago</sub>  
  Learn why US-listed Japan ETFs move after Tokyo closes, including the roles of the yen, futures, NAV, global markets and price discovery.
- [Asian equity markets mixed on rising yields and regional economic data](https://seekingalpha.com/news/4648325-asian-equity-markets-mixed-on-rising-yields-and-regional-economic-data)  
  <sub>Seeking Alpha, 9 hours ago</sub>  
  Asian equity markets traded mixed on Wednesday, following overnight losses on Wall Street, driven by elevated U.S. Treasury yields reaching fresh multiyear...
- [Yardeni blames unwinding of yen carry trade for global bond rout (FXY:NYSEARCA)](https://seekingalpha.com/news/4648124-yardeni-blames-unwinding-of-yen-carry-trade-for-global-bond-rout)  
  <sub>Seeking Alpha, 23 hours ago</sub>  
  Yen carry trade unwind after BOJ rate hikes is fueling a global bond rout and “bond vigilantes” as deficits meet higher yields.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.03% (+0.00 on the week) | 5-year 5.05% (+0.06 on the week) | 10-year 5.27% (+0.15 on the week) | 30-year 5.62% (+0.22 on the week)
Yield curve, 10-year minus 3-month: +1.24 points -- upward sloping (normal)
US dollar index: 101.27 (+0.17 on the week)
Volatility (VIX): 15.90 (+0.7 on the week) -- elevated
Latest US data: inflation 3.4% (2026-08-01) | unemployment 4.1% (2026-08-01) | jobless claims 197k (2026-09-19)
Policy and expectations: Fed target 4.00% | market expects 2.4% inflation over 10 years
Rate path: 2-year Treasury 4.92% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 98.27 (bar of 2026-09-30), from 502 daily bars
Trend: vs 20d SMA 97.39 (+0.9%), 50d 95.73 (+2.7%), 200d 90.26 (+8.9%); 50d above 200d
Momentum: RSI(14) 55.4 | MACD 0.405 vs signal 0.509 (histogram -0.104)
Returns: 1d +1.8% | 5d +1.3% | 1m +2.5% | 3m +5.6%
52-week range: 78.36 - 98.78 (now 97.5% of the way up)
Volatility: ATR(14) 1.49 (1.5% of price) | annualised 20d 19.8%
Volume: 0.93x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.20</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score +0.20</summary>

```text
Fund type: Japan Stock
What it holds: P/E 19.11 | P/B 2.01 | P/S 1.68 | 3y earnings growth n/a
Yield: 3.7%
Three-year record: +20.0% a year | beta to the market 0.86
Cost and size: expense ratio 0.49% | net assets 22.69B
What it is made of: Stocks 99.8%, Cash 0.2%
Largest holdings: Mitsubishi UFJ Financial Group Inc 4.6%, Toyota Motor Corp 3.5%, Sumitomo Mitsui Financial Group Inc 3.0%, Tokyo Electron Ltd 3.0%, Advantest Corp 2.9%
Sector mix: Industrials 22.9%, Technology 21.5%, Financial services 19.1%, Consumer cyclical 11.6%
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
Rolled up from the 5 largest holdings, 17.0% of the fund by weight  -- thin, so read this as a fact about that slice rather than the fund
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 1.68 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +16.5% above the current prices
Holdings read: 8306.T, 7203.T, 8316.T, 8035.T, 6857.T
Recent rating changes among them: none reported
```

</details>

<details><summary><b>Buying and selling by company insiders</b> — score -0.10</summary>

_Not available today._

</details>

<details><summary><b>Who is positioned how</b> — score -0.10</summary>

```text
Contract: NIKKEI STOCK AVERAGE YEN DENOM - CHICAGO MERCANTILE EXCHANGE (positions as of 2026-09-22, published the following Friday)
Large speculators: net long 3.6% of open interest (21,974 contracts)
Change on the week: -0.7% of open interest
Crowding: 32% percentile over 52 weeks -- within its normal range
Read this as crowding, not as a forecast: an extreme is as often the end of a move as the middle of one.
```

</details>

<details><summary><b>Money going into and out of this fund</b> — score -0.10</summary>

```text
Direction: flat (1 week)
Share count change: 1 week: +0.0% (0.00) over 12d
Shares outstanding: 227.85M | fund size: 22.39B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Switzerland (EWL) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Neutral overall; no macro surprise, flat fund flows, mixed fundamentals, and technicals lack a decisive break.

**Main reasons it gave:**
- Flat fund flows (share count unchanged)
- No macro surprise: yields up modestly, no policy change
- Technical momentum weak: RSI 34, price below 20‑day SMA, low volume
- Analyst coverage 48.5% of fund, 74.5% buy rating with +10.5% price target

<details><summary><b>News</b> — score +0.00</summary>

_No news found for this one today._

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.03% (+0.00 on the week) | 5-year 5.05% (+0.06 on the week) | 10-year 5.27% (+0.15 on the week) | 30-year 5.62% (+0.22 on the week)
Yield curve, 10-year minus 3-month: +1.24 points -- upward sloping (normal)
US dollar index: 101.27 (+0.17 on the week)
Volatility (VIX): 15.90 (+0.7 on the week) -- elevated
Latest US data: inflation 3.4% (2026-08-01) | unemployment 4.1% (2026-08-01) | jobless claims 197k (2026-09-19)
Policy and expectations: Fed target 4.00% | market expects 2.4% inflation over 10 years
Rate path: 2-year Treasury 4.92% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 59.47 (bar of 2026-09-30), from 502 daily bars
Trend: vs 20d SMA 60.85 (-2.3%), 50d 62.42 (-4.7%), 200d 61.62 (-3.5%); 50d above 200d
Momentum: RSI(14) 34.1 | MACD -0.735 vs signal -0.713 (histogram -0.022)
Returns: 1d -0.8% | 5d -1.5% | 1m -5.3% | 3m -4.8%
52-week range: 55.06 - 65.08 (now 44.1% of the way up)
Volatility: ATR(14) 0.68 (1.1% of price) | annualised 20d 14.0%
Volume: 0.30x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.10</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score +0.10</summary>

```text
Fund type: Focused Region
What it holds: P/E 24.65 | P/B 4.25 | P/S 2.78 | 3y earnings growth n/a
Yield: 1.7%
Three-year record: +13.7% a year | beta to the market 0.91
Cost and size: expense ratio 0.50% | net assets 2.42B
What it is made of: Stocks 99.0%, Cash 1.0%
Largest holdings: Roche Holding AG Ordinary Shares new 13.6%, Novartis AG Registered Shares 12.4%, Nestle SA 11.1%, UBS Group AG Registered Shares 6.8%, Compagnie Financiere Richemont SA Class A 4.6%
Sector mix: Healthcare 37.5%, Financial services 20.6%, Consumer defensive 13.3%, Industrials 11.8%
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
Rolled up from the 5 largest holdings, 48.5% of the fund by weight
Ratings by weight: buy 74.5% | hold 25.5% | sell 0.0% (mean 2.40 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +10.5% above the current prices
Holdings read: ROP.SW, NOVN.SW, NESN.SW, UBSG.SW, CFR.SW
Recent rating changes among them:
  - UBSG.SW: 2026-04-20 Barclays: up, Underweight -> Equal-Weight
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
Direction: flat (1 week)
Share count change: 1 week: +0.0% (0.00) over 7d
Shares outstanding: 28.62M | fund size: 1.70B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Netherlands (EWN) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Neutral overall; bullish analyst view limited to 44% coverage, flat fund flows, and neutral technicals offset each other.

**Main reasons it gave:**
- Flat fund flows: share count unchanged (+0.0% over 7d)
- Technical indicators neutral: RSI 51.3, price near 20‑day SMA (+0.6%) and below 50‑day SMA (-0.1%)
- Analyst view bullish (+26.9% price target) but covers only 44.1% of fund
- Macro environment unchanged: yields modestly higher, no surprise in inflation or Fed policy

<details><summary><b>News</b> — score +0.00</summary>

_No news found for this one today._

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.03% (+0.00 on the week) | 5-year 5.05% (+0.06 on the week) | 10-year 5.27% (+0.15 on the week) | 30-year 5.62% (+0.22 on the week)
Yield curve, 10-year minus 3-month: +1.24 points -- upward sloping (normal)
US dollar index: 101.27 (+0.17 on the week)
Volatility (VIX): 15.90 (+0.7 on the week) -- elevated
Latest US data: inflation 3.4% (2026-08-01) | unemployment 4.1% (2026-08-01) | jobless claims 197k (2026-09-19)
Policy and expectations: Fed target 4.00% | market expects 2.4% inflation over 10 years
Rate path: 2-year Treasury 4.92% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 68.18 (bar of 2026-09-30), from 502 daily bars
Trend: vs 20d SMA 67.76 (+0.6%), 50d 68.23 (-0.1%), 200d 64.23 (+6.1%); 50d above 200d
Momentum: RSI(14) 51.3 | MACD -0.093 vs signal -0.236 (histogram 0.143)
Returns: 1d -0.6% | 5d +1.4% | 1m -0.2% | 3m -0.2%
52-week range: 55.33 - 71.61 (now 78.9% of the way up)
Volatility: ATR(14) 0.87 (1.3% of price) | annualised 20d 15.9%
Volume: 0.07x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.30</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score +0.30</summary>

```text
Fund type: Focused Region
What it holds: P/E 18.97 | P/B 2.54 | P/S 1.84 | 3y earnings growth n/a
Yield: 4.1%
Three-year record: +25.4% a year | beta to the market 1.14
Cost and size: expense ratio 0.50% | net assets 626.66M
What it is made of: Stocks 99.8%, Cash 0.2%
Largest holdings: ASML Holding NV 21.8%, ING Groep NV 9.0%, Prosus NV Ordinary Shares - Class N 5.1%, Nebius Group NV Shs Class-A- 4.3%, ASM International NV 4.0%
Sector mix: Technology 31.5%, Financial services 21.4%, Industrials 10.8%, Consumer defensive 10.7%
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
Rolled up from the 5 largest holdings, 44.1% of the fund by weight
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 1.62 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +26.9% above the current prices
Holdings read: ASML.AS, INGA.AS, PRX.AS, NBIS, ASM.AS
Recent rating changes among them:
  - NBIS: 2026-09-24 BNP Paribas: up, Neutral -> Outperform
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
Direction: flat (1 week)
Share count change: 1 week: +0.0% (0.00) over 7d
Shares outstanding: 5.55M | fund size: 378.40M
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Spain (EWP) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Overall neutral as no macro surprise, no decisive technical break, and mixed signals from fundamentals and analyst view.

**Main reasons it gave:**
- Technical: price 59.59 below 20‑day SMA 61.27 (‑2.7%) and RSI 38.3 (bearish)
- Fundamentals: strong 3‑yr record (+34.5%/yr) with moderate valuation (P/E 16.28)
- Analyst view: 52% buy rating, weighted price target +3.5% above current price
- Fund flows: flat share count change (0% over 1 week)

<details><summary><b>News</b> — score +0.00</summary>

- [ETFs Investing in International Consolidated Airlines Group SA Stocks](https://www.tradingview.com/symbols/HAN-INR/etfs/)  
  <sub>TradingView, 21 hours ago</sub>  
  Explore funds investing in INR in a single list with price, expense ratio, and more stats for an in-depth analysis of new opportunities.
- [ETFs Investing in Bankinter SA Stocks](https://www.tradingview.com/symbols/HAN-BAKA/etfs/)  
  <sub>TradingView, 21 hours ago</sub>  
  Explore funds investing in BAKA in a single list with price, expense ratio, and more stats for an in-depth analysis of new opportunities.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.03% (+0.00 on the week) | 5-year 5.05% (+0.06 on the week) | 10-year 5.27% (+0.15 on the week) | 30-year 5.62% (+0.22 on the week)
Yield curve, 10-year minus 3-month: +1.24 points -- upward sloping (normal)
US dollar index: 101.27 (+0.17 on the week)
Volatility (VIX): 15.90 (+0.7 on the week) -- elevated
Latest US data: inflation 3.4% (2026-08-01) | unemployment 4.1% (2026-08-01) | jobless claims 197k (2026-09-19)
Policy and expectations: Fed target 4.00% | market expects 2.4% inflation over 10 years
Rate path: 2-year Treasury 4.92% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score -0.20</summary>

```text
Last close 59.59 (bar of 2026-09-30), from 502 daily bars
Trend: vs 20d SMA 61.27 (-2.7%), 50d 61.64 (-3.3%), 200d 57.55 (+3.5%); 50d above 200d
Momentum: RSI(14) 38.3 | MACD -0.428 vs signal -0.248 (histogram -0.180)
Returns: 1d -0.8% | 5d -1.3% | 1m -4.5% | 3m +1.1%
52-week range: 48.33 - 63.23 (now 75.6% of the way up)
Volatility: ATR(14) 0.81 (1.4% of price) | annualised 20d 17.0%
Volume: 0.05x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.40</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score +0.40</summary>

```text
Fund type: Focused Region
What it holds: P/E 16.28 | P/B 2.22 | P/S 1.82 | 3y earnings growth n/a
Yield: 2.7%
Three-year record: +34.5% a year | beta to the market 0.87
Cost and size: expense ratio 0.50% | net assets 2.26B
What it is made of: Stocks 99.7%, Cash 0.3%
Largest holdings: Banco Santander SA 19.2%, Banco Bilbao Vizcaya Argentaria SA 14.0%, Iberdrola SA 12.1%, CaixaBank SA 4.6%, Industria De Diseno Textil SA Share From Split 4.4%
Sector mix: Financial services 45.4%, Utilities 20.0%, Industrials 14.4%, Technology 5.9%
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

<details><summary><b>What analysts and big funds say</b> — score +0.30</summary>

_Not available today._

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score +0.30</summary>

```text
Rolled up from the 5 largest holdings, 54.5% of the fund by weight
Ratings by weight: buy 52.0% | hold 48.0% | sell 0.0% (mean 2.17 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +3.5% above the current prices
Holdings read: SAN.MC, BBVA.MC, IBE.MC, CABK.MC, ITX.MC
Recent rating changes among them:
  - SAN.MC: 2023-11-08 JP Morgan: main, Neutral -> Neutral
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
Direction: flat (1 week)
Share count change: 1 week: +0.0% (0.00) over 7d
Shares outstanding: 37.35M | fund size: 2.23B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### United Kingdom (EWU) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Neutral overall: analyst view is moderately bullish but not enough to outweigh slightly bearish technicals, flat fund flows, and no macro catalyst.

**Main reasons it gave:**
- Analyst consensus: 69.5% buy, weighted price target +12.9% above current price
- Technicals: price below 20‑day SMA (47.67) and 50‑day SMA (48.03), RSI 36.9, volume 0.18× 20‑day average
- Fund flows: flat, share count unchanged (+0.0% over 12 days)
- Macro: yields stable (3‑month 4.03%, 10‑year 5.27%), no policy surprise, VIX low at 15.9

<details><summary><b>News</b> — score +0.00</summary>

_No news found for this one today._

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.03% (+0.00 on the week) | 5-year 5.05% (+0.06 on the week) | 10-year 5.27% (+0.15 on the week) | 30-year 5.62% (+0.22 on the week)
Yield curve, 10-year minus 3-month: +1.24 points -- upward sloping (normal)
US dollar index: 101.27 (+0.17 on the week)
Volatility (VIX): 15.90 (+0.7 on the week) -- elevated
Latest US data: inflation 3.4% (2026-08-01) | unemployment 4.1% (2026-08-01) | jobless claims 197k (2026-09-19)
Policy and expectations: Fed target 4.00% | market expects 2.4% inflation over 10 years
Rate path: 2-year Treasury 4.92% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score -0.20</summary>

```text
Last close 46.79 (bar of 2026-09-30), from 502 daily bars
Trend: vs 20d SMA 47.67 (-1.8%), 50d 48.03 (-2.6%), 200d 46.65 (+0.3%); 50d above 200d
Momentum: RSI(14) 36.9 | MACD -0.314 vs signal -0.214 (histogram -0.100)
Returns: 1d -0.1% | 5d -0.6% | 1m -3.3% | 3m +1.9%
52-week range: 41.34 - 49.39 (now 67.7% of the way up)
Volatility: ATR(14) 0.46 (1.0% of price) | annualised 20d 11.5%
Volume: 0.18x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.30</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score +0.30</summary>

```text
Fund type: Focused Region
What it holds: P/E 17.08 | P/B 2.29 | P/S 1.52 | 3y earnings growth n/a
Yield: 3.1%
Three-year record: +18.7% a year | beta to the market 0.68
Cost and size: expense ratio 0.50% | net assets 3.79B
What it is made of: Stocks 97.9%, Other 1.1%, Cash 0.9%
Largest holdings: HSBC Holdings PLC 11.0%, Shell PLC 7.8%, AstraZeneca PLC 7.6%, Rolls-Royce Holdings PLC 5.3%, Unilever PLC 4.3%
Sector mix: Financial services 26.4%, Consumer defensive 14.3%, Industrials 13.9%, Healthcare 12.7%
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
Rolled up from the 5 largest holdings, 36.0% of the fund by weight
Ratings by weight: buy 69.5% | hold 30.5% | sell 0.0% (mean 2.17 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +12.9% above the current prices
Holdings read: HSBA.L, SHEL.L, AZN.L, RR.L, ULVR.L
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
Direction: flat (1 week)
Share count change: 1 week: +0.0% (0.00) over 12d
Shares outstanding: 67.80M | fund size: 3.17B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Mexico (EWW) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> The fund shows a modestly bullish analyst view (100% buy rating, +16.3% price target) and solid fundamentals (low P/E, decent yield, strong 3‑year record), but fund flows are flat and technicals are bearish (price below key SMAs, RSI 36.3). Macro data show no surprise catalyst. Overall, the evidence does not justify a directional tilt beyond neutral.

**Main reasons it gave:**
- Analyst view: 47.6% coverage, 100% buy rating, +16.3% price target
- Technicals: price below 20‑day, 50‑day, 200‑day SMAs; RSI 36.3 (oversold)
- Fund flows: flat share count change (0% over 1 week)
- Macro: US dollar up 0.17% on week; yields up (10‑yr +0.15%)

<details><summary><b>News</b> — score +0.00</summary>

_No news found for this one today._

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.03% (+0.00 on the week) | 5-year 5.05% (+0.06 on the week) | 10-year 5.27% (+0.15 on the week) | 30-year 5.62% (+0.22 on the week)
Yield curve, 10-year minus 3-month: +1.24 points -- upward sloping (normal)
US dollar index: 101.27 (+0.17 on the week)
Volatility (VIX): 15.90 (+0.7 on the week) -- elevated
Latest US data: inflation 3.4% (2026-08-01) | unemployment 4.1% (2026-08-01) | jobless claims 197k (2026-09-19)
Policy and expectations: Fed target 4.00% | market expects 2.4% inflation over 10 years
Rate path: 2-year Treasury 4.92% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score -0.20</summary>

```text
Last close 71.95 (bar of 2026-09-30), from 502 daily bars
Trend: vs 20d SMA 74.34 (-3.2%), 50d 75.55 (-4.8%), 200d 75.80 (-5.1%); 50d below 200d
Momentum: RSI(14) 36.3 | MACD -1.009 vs signal -0.778 (histogram -0.231)
Returns: 1d -0.1% | 5d -2.0% | 1m -6.2% | 3m -4.4%
52-week range: 64.39 - 81.23 (now 44.9% of the way up)
Volatility: ATR(14) 1.22 (1.7% of price) | annualised 20d 16.6%
Volume: 0.30x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.30</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score +0.30</summary>

```text
Fund type: Focused Region
What it holds: P/E 12.68 | P/B 1.98 | P/S 1.49 | 3y earnings growth n/a
Yield: 3.2%
Three-year record: +11.3% a year | beta to the market 1.05
Cost and size: expense ratio 0.50% | net assets 1.82B
What it is made of: Stocks 99.5%, Cash 0.5%
Largest holdings: Grupo Mexico SAB de CV Class B 16.6%, Grupo Financiero Banorte SAB de CV Class O 11.1%, Fomento Economico Mexicano SAB de CV Units Cons. Of 1 Shs-B- And 4 Shs-D- 8.3%, America Movil SAB de CV Ordinary Shares - Class B 7.2%, Cemex SAB de CV 4.4%
Sector mix: Basic materials 27.3%, Consumer defensive 24.4%, Financial services 19.7%, Industrials 11.7%
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
Rolled up from the 5 largest holdings, 47.6% of the fund by weight
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 2.12 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +16.3% above the current prices
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
Direction: flat (1 week)
Share count change: 1 week: +0.0% (0.00) over 7d
Shares outstanding: 18.90M | fund size: 1.36B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### South Korea (EWY) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Neutral outlook based on flat flows, lack of analyst guidance, neutral technicals, and macro data in line with expectations.

**Main reasons it gave:**
- Flat fund flows (0% change) indicating no net demand
- Analyst view provides no rating or price target, implying neutral outlook
- Technical indicators neutral: RSI 51, MACD below signal, price near 20‑day SMA
- Macro data (inflation 3.4%, unemployment 4.1%) in line with expectations, no surprise

<details><summary><b>News</b> — score +0.00</summary>

- [Single-country ETFs surge as investors target AI, reform plays](https://www.investmentnews.com/etfs/single-country-etfs-surge-as-investors-target-ai-reform-plays/268410)  
  <sub>InvestmentNews, 4 hours ago</sub>  
  US-listed single-country ETFs have pulled in over $26 billion year-to-date, more than four times their full-year 2025 haul, TD Securities data shows.
- [KOR3 ETF Holdings List — HAN:KOR3](https://www.tradingview.com/symbols/HAN-KOR3/holdings/)  
  <sub>TradingView, 19 hours ago</sub>  
  Explore Leverage Shares 3x Long South Korea ETP holdings with weight, market value, and other helpful data to make more informed decisions for KOR3 trading.
- [Robinhood adds perpetual futures trading to platform, expanding beyond crypto into traditional assets](https://cryptobriefing.com/robinhood-perpetual-futures-traditional-assets/)  
  <sub>Crypto Briefing, 16 hours ago</sub>  
  Robinhood expands perpetual futures trading in Europe to include gold, oil, ETFs, and forex pairs with up to 10x leverage, moving beyond.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.03% (+0.00 on the week) | 5-year 5.05% (+0.06 on the week) | 10-year 5.27% (+0.15 on the week) | 30-year 5.62% (+0.22 on the week)
Yield curve, 10-year minus 3-month: +1.24 points -- upward sloping (normal)
US dollar index: 101.27 (+0.17 on the week)
Volatility (VIX): 15.90 (+0.7 on the week) -- elevated
Latest US data: inflation 3.4% (2026-08-01) | unemployment 4.1% (2026-08-01) | jobless claims 197k (2026-09-19)
Policy and expectations: Fed target 4.00% | market expects 2.4% inflation over 10 years
Rate path: 2-year Treasury 4.92% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 183.51 (bar of 2026-09-30), from 502 daily bars
Trend: vs 20d SMA 184.19 (-0.4%), 50d 175.99 (+4.3%), 200d 155.28 (+18.2%); 50d above 200d
Momentum: RSI(14) 51.0 | MACD 1.984 vs signal 2.243 (histogram -0.258)
Returns: 1d -1.9% | 5d -1.2% | 1m +1.5% | 3m -1.1%
52-week range: 80.10 - 219.20 (now 74.3% of the way up)
Volatility: ATR(14) 6.12 (3.3% of price) | annualised 20d 47.2%
Volume: 0.28x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.00</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score +0.00</summary>

```text
Fund type: Focused Region
What it holds: P/E 10.41 | P/B 1.83 | P/S 1.70 | 3y earnings growth n/a
Yield: 1.1%
Three-year record: +49.3% a year | beta to the market 2.50
Cost and size: expense ratio 0.59% | net assets 27.72B
What it is made of: Stocks 99.5%, Cash 0.5%
Largest holdings: SK hynix Inc 23.7%, Samsung Electronics Co Ltd 22.2%, SK Square 2.9%, Samsung Electro-Mechanics Co Ltd 2.7%, KB Financial Group Inc 2.0%
Sector mix: Technology 54.6%, Industrials 17.0%, Financial services 11.1%, Consumer cyclical 5.1%
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
Rolled up from the 5 largest holdings, 53.5% of the fund by weight
Ratings by weight: buy n/a | hold n/a | sell n/a (mean n/a on a 1=strong buy to 5=strong sell scale)
Weighted price target: n/a above the current prices
Holdings read: 000660.KQ, 005930.KQ, 402340.KQ, 009150.KQ, 105560.KQ
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
Direction: flat (1 week)
Share count change: 1 week: +0.0% (0.00) over 12d
Shares outstanding: 75.60M | fund size: 13.87B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Brazil (EWZ) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:** no explanation. It wrote only “Neutral”, so the main reasons below are all it gave.

**Main reasons it gave:**
- Flat fund flows (0% change) over the past week
- Technical indicators mixed: price above 50‑day/200‑day SMA but MACD below signal and low volume (0.34x avg)
- No macro surprise: US Treasury yields rose modestly, dollar up 0.17, VIX low at 15.9
- Analyst coverage bullish (100% buy, +31% price target) but only 40.9% of fund weight
- Fund basics show low valuation (P/E 10.48) and 4.1% yield, but macro risk from rising US rates

<details><summary><b>News</b> — score +0.00</summary>

- [4 ETFs Seeing Unusual Options Volume Today](https://www.schaeffersresearch.com/content/options/2026/09/29/4-etfs-seeing-unusual-options-volume-today)  
  <sub>Schaeffer's Investment Research, 22 hours ago</sub>  
  HYG, EWZ, LQD, and XLU are seeing elevated options volume today, even as all four ETFs stick close to the flatline.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.03% (+0.00 on the week) | 5-year 5.05% (+0.06 on the week) | 10-year 5.27% (+0.15 on the week) | 30-year 5.62% (+0.22 on the week)
Yield curve, 10-year minus 3-month: +1.24 points -- upward sloping (normal)
US dollar index: 101.27 (+0.17 on the week)
Volatility (VIX): 15.90 (+0.7 on the week) -- elevated
Latest US data: inflation 3.4% (2026-08-01) | unemployment 4.1% (2026-08-01) | jobless claims 197k (2026-09-19)
Policy and expectations: Fed target 4.00% | market expects 2.4% inflation over 10 years
Rate path: 2-year Treasury 4.92% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 37.13 (bar of 2026-09-30), from 502 daily bars
Trend: vs 20d SMA 37.65 (-1.4%), 50d 36.29 (+2.3%), 200d 36.33 (+2.2%); 50d below 200d
Momentum: RSI(14) 51.7 | MACD 0.160 vs signal 0.381 (histogram -0.221)
Returns: 1d +1.8% | 5d -0.6% | 1m +3.1% | 3m +8.6%
52-week range: 28.79 - 41.73 (now 64.5% of the way up)
Volatility: ATR(14) 0.76 (2.1% of price) | annualised 20d 24.4%
Volume: 0.34x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.00</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score +0.00</summary>

```text
Fund type: Focused Region
What it holds: P/E 10.48 | P/B 1.79 | P/S 1.28 | 3y earnings growth n/a
Yield: 4.1%
Three-year record: +12.3% a year | beta to the market 0.84
Cost and size: expense ratio 0.59% | net assets 8.17B
What it is made of: Stocks 96.5%, Cash 2.7%, Preferred 0.8%
Largest holdings: Vale SA 10.1%, Nu Holdings Ltd Ordinary Shares Class A 9.5%, Itau Unibanco Holding SA Participating Preferred 7.7%, Petroleo Brasileiro SA Petrobras Participating Preferred 7.0%, Petroleo Brasileiro SA Petrobras 6.6%
Sector mix: Financial services 34.1%, Energy 17.4%, Basic materials 14.5%, Utilities 12.4%
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
Rolled up from the 5 largest holdings, 40.9% of the fund by weight
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 1.80 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +31.0% above the current prices
Holdings read: VALE3.SA, NU, ITUB4, PETR4, PETR3.SA
Recent rating changes among them:
  - NU: 2026-09-28 Needham: reit, Buy -> Buy
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
Direction: flat (1 week)
Share count change: 1 week: +0.0% (0.00) over 7d
Shares outstanding: 200.55M | fund size: 7.45B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### South Africa (EZA) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:** no explanation. It wrote only “NEUTRAL”, so the main reasons below are all it gave.

**Main reasons it gave:**
- Technical indicators bearish: price below 20‑day, 50‑day, and 200‑day SMAs; RSI 35.3; MACD negative
- Analyst view bullish: 45.6% of fund covered, all buy, weighted price target +31.3% above current price
- Fund flows flat: share count unchanged over the past week
- Macro environment unchanged: yields rose modestly, no surprise data releases

<details><summary><b>News</b> — score +0.00</summary>

_No news found for this one today._

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.03% (+0.00 on the week) | 5-year 5.05% (+0.06 on the week) | 10-year 5.27% (+0.15 on the week) | 30-year 5.62% (+0.22 on the week)
Yield curve, 10-year minus 3-month: +1.24 points -- upward sloping (normal)
US dollar index: 101.27 (+0.17 on the week)
Volatility (VIX): 15.90 (+0.7 on the week) -- elevated
Latest US data: inflation 3.4% (2026-08-01) | unemployment 4.1% (2026-08-01) | jobless claims 197k (2026-09-19)
Policy and expectations: Fed target 4.00% | market expects 2.4% inflation over 10 years
Rate path: 2-year Treasury 4.92% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score -0.30</summary>

```text
Last close 64.18 (bar of 2026-09-30), from 502 daily bars
Trend: vs 20d SMA 68.38 (-6.1%), 50d 67.75 (-5.3%), 200d 69.20 (-7.3%); 50d below 200d
Momentum: RSI(14) 35.3 | MACD -1.067 vs signal -0.429 (histogram -0.638)
Returns: 1d -1.0% | 5d -3.4% | 1m -9.0% | 3m +2.3%
52-week range: 60.43 - 81.60 (now 17.7% of the way up)
Volatility: ATR(14) 1.31 (2.0% of price) | annualised 20d 26.6%
Volume: 0.10x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.40</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score +0.40</summary>

```text
Fund type: Focused Region
What it holds: P/E 9.31 | P/B 2.24 | P/S 1.92 | 3y earnings growth n/a
Yield: 7.1%
Three-year record: +26.3% a year | beta to the market 1.02
Cost and size: expense ratio 0.59% | net assets 578.49M
What it is made of: Stocks 99.7%, Cash 0.3%
Largest holdings: Anglogold Ashanti PLC 13.7%, Gold Fields Ltd 9.9%, Naspers Ltd Class N 8.8%, Firstrand Ltd 7.1%, Standard Bank Group Ltd 6.1%
Sector mix: Basic materials 41.0%, Financial services 33.2%, Consumer cyclical 12.8%, Communication services 6.2%
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
Rolled up from the 5 largest holdings, 45.6% of the fund by weight
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 1.98 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +31.3% above the current prices
Holdings read: AU, GFI.JO, NPN.JO, FSR.JO, SBK.JO
Recent rating changes among them:
  - AU: 2026-09-16 RBC Capital: main, Outperform -> Outperform
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
Direction: flat (1 week)
Share count change: 1 week: +0.0% (0.00) over 7d
Shares outstanding: 7.90M | fund size: 506.98M
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Gold mining companies (GDX) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Neutral overall: no macro surprise, technicals bearish but not decisive, positive flows and analyst view offsetting, fundamentals solid but not a catalyst.

**Main reasons it gave:**
- Treasury yields rose modestly (10y +0.15% on week) with no policy surprise
- GDX price below 20d/50d/200d SMAs (88.39 vs 94.91) and RSI 41, MACD negative, low volume
- Share count increased 3% over 7 days (860.18M) indicating net inflows
- Analyst coverage 39.9% of fund, all buy rating, price target +19% above current price

<details><summary><b>News</b> — score +0.00</summary>

- [YieldMax® ETFs Announces Weekly Distributions for Group 2 ETFs](https://www.globenewswire.com/news-release/2026/09/30/3371725/0/en/yieldmax-etfs-announces-weekly-distributions-for-group-2-etfs.html)  
  <sub>GlobeNewswire, 4 hours ago</sub>  
  CHICAGO and MILWAUKEE and NEW YORK, Sept. 30, 2026 (GLOBE NEWSWIRE) -- YieldMax® ETFs today announced distributions for the YieldMax® Group 2 weekly pay...
- [Global X Gold Explorers ETF (GOEX) Stock Price | Quotes & News](https://www.moomoo.com/stock/GOEX-US?chain_id=Name1K9-3FXPhg.1lbo660&global_content=%7B%22promote_id%22%3A13764%2C%22sub_promote_id%22%3A57%2C%22f%22%3A%22www.moomoo.com%2Fstock%2FWPM-US%22%7D)  
  <sub>Moomoo, 19 hours ago</sub>  
  $XAU/USD (XAUUSD.CFD)$ $SPDR Gold ETF (GLD.US)$ $Abrdn Gold ETF Trust (SGOL.US)$ $VanEck Gold Miners Equity ETF (GDX.US)$ $VanEck Junior Gold Miners ETF...
- [ETFs Investing in Sinda Limited Stocks](https://www.tradingview.com/symbols/NYSE-SIND/etfs/)  
  <sub>TradingView, 10 hours ago</sub>  
  Explore funds investing in SIND in a single list with price, expense ratio, and more stats for an in-depth analysis of new opportunities.
- [ETFs Investing in OceanaGold Corporation Stocks](https://www.tradingview.com/symbols/HAN-RQQ0/etfs/)  
  <sub>TradingView, 19 hours ago</sub>  
  Explore funds investing in RQQ0 in a single list with price, expense ratio, and more stats for an in-depth analysis of new opportunities.
- [ETFs Investing in SSR Mining Inc Stocks](https://www.tradingview.com/symbols/HAN-ZSV/etfs/)  
  <sub>TradingView, 20 hours ago</sub>  
  Explore funds investing in ZSV in a single list with price, expense ratio, and more stats for an in-depth analysis of new opportunities.
- [ETFs Investing in Alamos Gold Inc. Stocks](https://www.tradingview.com/symbols/HAN-1AL/etfs/)  
  <sub>TradingView, 21 hours ago</sub>  
  Explore funds investing in 1AL in a single list with price, expense ratio, and more stats for an in-depth analysis of new opportunities.
- [ETFs Investing in DPM Metals Inc. Stocks](https://www.tradingview.com/symbols/HAN-DPU0/etfs/)  
  <sub>TradingView, 23 hours ago</sub>  
  Explore funds investing in DPU0 in a single list with price, expense ratio, and more stats for an in-depth analysis of new opportunities.
- [Silver Has Now Lost Nearly Half Its Value. Here’s What Broke the Metals Trade](https://247wallst.com/investing/2026/09/30/silver-has-now-lost-nearly-half-its-value-heres-what-broke-the-metals-trade/)  
  <sub>24/7 Wall St., 4 hours ago</sub>  
  Silver just recorded one of its worst stretches in decades, and the forces behind the selloff are still building pressure. Understanding what broke the...
- [iShares Core Equity ETF Portfolio (XEQT.TO) Stock Price, News, Quote & History](https://ca.finance.yahoo.com/quote/XEQT.TO/)  
  <sub>Yahoo! Finance Canada, 18 hours ago</sub>  
  Find the latest iShares Core Equity ETF Portfolio (XEQT.TO) stock quote, history, news and other vital information to help you with your stock trading and...
- [ETFs Investing in Regis Resources Limited Stocks](https://www.tradingview.com/symbols/HAN-RKQ/etfs/)  
  <sub>TradingView, 23 hours ago</sub>  
  Explore funds investing in RKQ in a single list with price, expense ratio, and more stats for an in-depth analysis of new opportunities.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.03% (+0.00 on the week) | 5-year 5.05% (+0.06 on the week) | 10-year 5.27% (+0.15 on the week) | 30-year 5.62% (+0.22 on the week)
Yield curve, 10-year minus 3-month: +1.24 points -- upward sloping (normal)
US dollar index: 101.27 (+0.17 on the week)
Volatility (VIX): 15.90 (+0.7 on the week) -- elevated
Latest US data: inflation 3.4% (2026-08-01) | unemployment 4.1% (2026-08-01) | jobless claims 197k (2026-09-19)
Policy and expectations: Fed target 4.00% | market expects 2.4% inflation over 10 years
Rate path: 2-year Treasury 4.92% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score -0.20</summary>

```text
Last close 88.39 (bar of 2026-09-30), from 502 daily bars
Trend: vs 20d SMA 94.91 (-6.9%), 50d 90.99 (-2.9%), 200d 91.07 (-2.9%); 50d below 200d
Momentum: RSI(14) 41.0 | MACD -0.960 vs signal 0.326 (histogram -1.287)
Returns: 1d -0.8% | 5d -5.5% | 1m -10.3% | 3m +17.7%
52-week range: 68.28 - 115.84 (now 42.3% of the way up)
Volatility: ATR(14) 3.21 (3.6% of price) | annualised 20d 41.9%
Volume: 0.29x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.30</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score +0.30</summary>

```text
Fund type: Equity Precious Metals
What it holds: P/E 12.84 | P/B 2.68 | P/S 4.10 | 3y earnings growth n/a
Yield: 0.6%
Three-year record: +49.8% a year | beta to the market 0.83
Cost and size: expense ratio 0.51% | net assets 30.54B
What it is made of: Stocks 100.0%
Largest holdings: Newmont Corp 10.7%, Agnico Eagle Mines Ltd 10.7%, Barrick Mining Corp 7.4%, Wheaton Precious Metals Corp 5.8%, Anglogold Ashanti PLC 5.3%
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
Rolled up from the 5 largest holdings, 39.9% of the fund by weight
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 1.66 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +19.0% above the current prices
Holdings read: NEM, AEM.TO, ABX.TO, WPM.TO, AU
Recent rating changes among them:
  - NEM: 2026-09-16 RBC Capital: main, Outperform -> Outperform
  - AEM.TO: 2026-09-16 RBC Capital: main, Sector Perform -> Sector Perform
  - ABX.TO: 2026-09-16 RBC Capital: main, Outperform -> Outperform
  - WPM.TO: 2026-09-16 RBC Capital: main, Outperform -> Outperform
  - AU: 2026-09-16 RBC Capital: main, Outperform -> Outperform
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
Direction: money coming in (1 week)
Share count change: 1 week: +3.0% (860.18M) over 7d
Shares outstanding: 328.99M | fund size: 29.08B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Software (IGV) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Neutral overall call based on mixed evidence: flat fund flows, mixed technicals, modest bullish analyst view, and high valuation multiples.

**Main reasons it gave:**
- Flat fund flows (share count change +0.0% over 1 week)
- Technical uptrend but MACD below signal and low volume
- Analyst consensus all buy with +4% price target
- High valuation multiples (P/E 34.2) suggest caution

<details><summary><b>News</b> — score +0.00</summary>

- [What's Going On With Oracle Stock Tuesday?](https://www.benzinga.com/trading-ideas/movers/26/09/62075824/whats-going-on-with-oracle-stock-tuesday-7)  
  <sub>Benzinga, 3 hours ago</sub>  
  Oracle stock trades down near $137 key support. Discover ORCL's technical analysis, moving averages, and premarket price action.
- [Oracle Jumps 5% as Fusion Claw Launch Adds 25 Agentic Applications; Salesforce Holds Flat, ServiceNow Slips](https://247wallst.com/investing/2026/09/29/oracle-jumps-5-as-fusion-claw-launch-adds-25-agentic-applications-salesforce-holds-flat-servicenow-slips/)  
  <sub>24/7 Wall St., 23 hours ago</sub>  
  Oracle surged 6% after launching Fusion Claw with 25 agentic apps, directly targeting enterprise workflows where Salesforce and ServiceNow compete. IGV and...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.03% (+0.00 on the week) | 5-year 5.05% (+0.06 on the week) | 10-year 5.27% (+0.15 on the week) | 30-year 5.62% (+0.22 on the week)
Yield curve, 10-year minus 3-month: +1.24 points -- upward sloping (normal)
US dollar index: 101.27 (+0.17 on the week)
Volatility (VIX): 15.90 (+0.7 on the week) -- elevated
Latest US data: inflation 3.4% (2026-08-01) | unemployment 4.1% (2026-08-01) | jobless claims 197k (2026-09-19)
Policy and expectations: Fed target 4.00% | market expects 2.4% inflation over 10 years
Rate path: 2-year Treasury 4.92% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 107.04 (bar of 2026-09-30), from 502 daily bars
Trend: vs 20d SMA 105.11 (+1.8%), 50d 102.18 (+4.7%), 200d 93.60 (+14.4%); 50d above 200d
Momentum: RSI(14) 56.0 | MACD 1.069 vs signal 1.220 (histogram -0.151)
Returns: 1d +1.7% | 5d -1.0% | 1m -2.7% | 3m +14.7%
52-week range: 74.67 - 117.08 (now 76.3% of the way up)
Volatility: ATR(14) 2.46 (2.3% of price) | annualised 20d 30.7%
Volume: 0.33x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score -0.20</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score -0.20</summary>

```text
Fund type: Technology
What it holds: P/E 34.20 | P/B 8.09 | P/S 9.07 | 3y earnings growth n/a
Yield: 0.0%
Three-year record: +15.8% a year | beta to the market 1.21
Cost and size: expense ratio 0.38% | net assets 15.74B
What it is made of: Stocks 100.0%, Cash 0.1%
Largest holdings: Palantir Technologies Inc Ordinary Shares - Class A 10.3%, Palo Alto Networks Inc 9.7%, Microsoft Corp 9.2%, CrowdStrike Holdings Inc Class A 7.4%, Salesforce Inc 6.6%
Sector mix: Technology 94.4%, Communication services 3.8%, Financial services 1.5%, Consumer cyclical 0.2%
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
Rolled up from the 5 largest holdings, 43.2% of the fund by weight
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 1.67 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +4.0% above the current prices
Holdings read: PLTR, PANW, MSFT, CRWD, CRM
Recent rating changes among them:
  - PLTR: 2026-09-23 Rosenblatt: main, Buy -> Buy
  - PANW: 2026-09-28 BTIG: main, Buy -> Buy
  - MSFT: 2026-09-30 Piper Sandler: main, Overweight -> Overweight
  - CRWD: 2026-09-21 Morgan Stanley: main, Overweight -> Overweight
  - CRM: 2026-09-18 Citizens: reit, Market Outperform -> Market Outperform
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
Direction: flat (1 week)
Share count change: 1 week: +0.0% (0.00) over 7d
Shares outstanding: 12.50M | fund size: 1.34B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### India (INDA) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> No macro surprise, technicals not decisive, thin analyst coverage, modest inflows

**Main reasons it gave:**
- Analyst coverage thin (24.7% of fund) despite 100% buy rating and +35% price target
- Modest inflows: share count up 0.6% over 1 week
- Technical: price below 20‑day, 50‑day, 200‑day SMAs; RSI 31.5; no decisive break on volume
- Macro: yields up modestly, no surprise data; VIX low at 15.9

<details><summary><b>News</b> — score +0.00</summary>

_No news found for this one today._

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.03% (+0.00 on the week) | 5-year 5.05% (+0.06 on the week) | 10-year 5.27% (+0.15 on the week) | 30-year 5.62% (+0.22 on the week)
Yield curve, 10-year minus 3-month: +1.24 points -- upward sloping (normal)
US dollar index: 101.27 (+0.17 on the week)
Volatility (VIX): 15.90 (+0.7 on the week) -- elevated
Latest US data: inflation 3.4% (2026-08-01) | unemployment 4.1% (2026-08-01) | jobless claims 197k (2026-09-19)
Policy and expectations: Fed target 4.00% | market expects 2.4% inflation over 10 years
Rate path: 2-year Treasury 4.92% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 46.68 (bar of 2026-09-30), from 502 daily bars
Trend: vs 20d SMA 48.24 (-3.2%), 50d 49.05 (-4.8%), 200d 49.92 (-6.5%); 50d below 200d
Momentum: RSI(14) 31.5 | MACD -0.594 vs signal -0.460 (histogram -0.134)
Returns: 1d -0.6% | 5d -2.9% | 1m -6.1% | 3m -5.1%
52-week range: 45.42 - 55.29 (now 12.8% of the way up)
Volatility: ATR(14) 0.45 (1.0% of price) | annualised 20d 14.1%
Volume: 0.45x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.00</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score +0.00</summary>

```text
Fund type: India Equity
What it holds: P/E 22.87 | P/B 3.14 | P/S 2.72 | 3y earnings growth n/a
Yield: n/a
Three-year record: +2.3% a year | beta to the market 0.56
Cost and size: expense ratio 0.61% | net assets 6.75B
What it is made of: Stocks 100.1%, Cash -0.1%
Largest holdings: HDFC Bank Ltd 6.4%, Reliance Industries Ltd 6.0%, ICICI Bank Ltd 5.7%, Bharti Airtel Ltd 4.1%, Infosys Ltd 2.6%
Sector mix: Financial services 30.1%, Consumer cyclical 12.8%, Industrials 9.7%, Energy 8.6%
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
Rolled up from the 5 largest holdings, 24.7% of the fund by weight  -- thin, so read this as a fact about that slice rather than the fund
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 1.36 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +35.0% above the current prices
Holdings read: HDFCBANK.NS, RELIANCE.NS, ICICIBANK.NS, BHARTIARTL.NS, INFY.NS
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
Direction: money coming in (1 week)
Share count change: 1 week: +0.6% (39.48M) over 7d
Shares outstanding: 140.79M | fund size: 6.57B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Defence and aerospace (ITA) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> No macro surprise, technicals lack decisive break, sector news negative but not material, flat fund flows

**Main reasons it gave:**
- Yield curve unchanged: 10y-3m spread +1.24 (normal), yields up modestly
- RSI 26.5 (oversold) with volume 0.27x 20‑day average, no decisive break
- Sector news: defense stocks down 7 straight weeks (record streak)
- Fund flows flat: share count +0.0% week, indicating no net demand

<details><summary><b>News</b> — score +0.00</summary>

- [ARK Space & Defense or SPDR Aerospace & Defense: Which ETF Can Power Your Portfolio?](https://finance.yahoo.com/markets/stocks/articles/ark-space-defense-spdr-aerospace-144121851.html)  
  <sub>Yahoo Finance, 21 minutes ago</sub>  
  The ARK Space & Defense Innovation ETF (NYSEMKT:ARKX) offers active management in space technology, while State Street SPDR S&P Aerospace & Defense ETF...
- [Royal Bank of Canada Registers Accelerated Return Notes Linked to iShares U.S. Aerospace and Defense ETF](https://kalkinemedia.com/us/news/announcements/royal-bank-of-canada-registers-accelerated-return-notes-linked-to-ishares-us-aerospace-and-defense-etf)  
  <sub>Kalkine Media, 5 hours ago</sub>  
  On September 30, 2026, Royal Bank of Canada submitted a free writing prospectus under Registration Statement No. 333-275898, outlining preliminary details...
- [ETFs Investing in HEICO Corporation Stocks](https://www.tradingview.com/symbols/HAN-HC1/etfs/)  
  <sub>TradingView, 18 hours ago</sub>  
  Explore funds investing in HC1 in a single list with price, expense ratio, and more stats for an in-depth analysis of new opportunities.
- [Defense Stocks Fall 7 Straight Weeks, Worst Streak on Record - iShares U.S. Aerospace & Defense ETF (BATS](https://www.benzinga.com/etfs/specialty-etfs/26/09/62054200/defense-stocks-7-straight-weeks-xar-record-losing-streak)  
  <sub>Benzinga, 24 hours ago</sub>  
  Defense stocks are on track for a seventh straight weekly loss, a first for XAR since 2011, as Iran peace talk and a stalled budget erase the 2026 gain.
- [Five Drone Stocks to Watch as Tariffs Reshape U.S. Market](https://nai500.com/blog/2026/09/five-drone-stocks-to-watch-as-tariffs-reshape-u-s-market/)  
  <sub>NAI500, 12 hours ago</sub>  
  From battlefield surveillance to weekend aerial photography, drones are carving out an ever-larger footprint across the U.S. economy — and Washington is...
- [ETFs Investing in Karman Holdings Inc. Stocks](https://www.tradingview.com/symbols/HAN-VF4/etfs/)  
  <sub>TradingView, 18 hours ago</sub>  
  Explore funds investing in VF4 in a single list with price, expense ratio, and more stats for an in-depth analysis of new opportunities.
- [ETFs Investing in AeroVironment, Inc. Stocks](https://www.tradingview.com/symbols/HAN-JPX/etfs/)  
  <sub>TradingView, 22 hours ago</sub>  
  Explore funds investing in JPX in a single list with price, expense ratio, and more stats for an in-depth analysis of new opportunities.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.03% (+0.00 on the week) | 5-year 5.05% (+0.06 on the week) | 10-year 5.27% (+0.15 on the week) | 30-year 5.62% (+0.22 on the week)
Yield curve, 10-year minus 3-month: +1.24 points -- upward sloping (normal)
US dollar index: 101.27 (+0.17 on the week)
Volatility (VIX): 15.90 (+0.7 on the week) -- elevated
Latest US data: inflation 3.4% (2026-08-01) | unemployment 4.1% (2026-08-01) | jobless claims 197k (2026-09-19)
Policy and expectations: Fed target 4.00% | market expects 2.4% inflation over 10 years
Rate path: 2-year Treasury 4.92% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 209.39 (bar of 2026-09-30), from 502 daily bars
Trend: vs 20d SMA 216.38 (-3.2%), 50d 231.93 (-9.7%), 200d 230.49 (-9.2%); 50d above 200d
Momentum: RSI(14) 26.5 | MACD -6.181 vs signal -6.255 (histogram 0.074)
Returns: 1d +0.0% | 5d -2.1% | 1m -8.3% | 3m -14.1%
52-week range: 198.23 - 253.22 (now 20.3% of the way up)
Volatility: ATR(14) 3.91 (1.9% of price) | annualised 20d 14.0%
Volume: 0.27x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score -0.10</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score -0.10</summary>

```text
Fund type: Industrials
What it holds: P/E 34.66 | P/B 6.62 | P/S 3.21 | 3y earnings growth n/a
Yield: 0.5%
Three-year record: +26.4% a year | beta to the market 0.99
Cost and size: expense ratio 0.37% | net assets 13.63B
What it is made of: Stocks 99.8%, Cash 0.2%
Largest holdings: GE Aerospace 21.6%, RTX Corp 17.2%, Boeing Co 9.1%, General Dynamics Corp 4.8%, Lockheed Martin Corp 4.7%
Sector mix: Industrials 100.0%
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
Rolled up from the 5 largest holdings, 57.5% of the fund by weight
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 1.75 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +28.5% above the current prices
Holdings read: GE, RTX, BA, GD, LMT
Recent rating changes among them:
  - GE: 2026-09-23 Jefferies: main, Buy -> Buy
  - RTX: 2026-09-23 Bernstein: main, Market Perform -> Market Perform
  - BA: 2026-09-21 Jefferies: main, Buy -> Buy
  - GD: 2026-09-23 Bernstein: main, Market Perform -> Market Perform
  - LMT: 2026-09-08 UBS: up, Neutral -> Buy
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
Direction: flat (1 week)
Share count change: 1 week: +0.0% (5.60M) over 7d
Shares outstanding: 63.75M | fund size: 13.35B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Transport and delivery (IYT) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> The technicals are bearish (price below 20‑, 50‑ and 200‑day SMAs, RSI 32.8, negative MACD) while analyst coverage of the top holdings is strongly bullish (90.8% buy, +26.3% price target). Fund flows are flat, indicating no net demand, and the macro backdrop shows an upward‑sloping yield curve with modest rate hikes but no surprise data. The mixed signals lead to a neutral overall view.

**Main reasons it gave:**
- Technical indicators show price below 20‑day, 50‑day and 200‑day SMAs with RSI 32.8, indicating bearish momentum
- Analyst coverage of top holdings is 90.8% buy with a weighted price target +26.3% above current levels
- Fund flows are flat over the past week, indicating no net demand for the ETF
- Macro backdrop shows an upward‑sloping yield curve and modestly higher rates, but no surprise data

<details><summary><b>News</b> — score +0.00</summary>

- [State Street SPDR S&P Transportation ETF (XTN) Stock Price, News, Quote & History](https://ca.finance.yahoo.com/quote/XTN/)  
  <sub>Yahoo! Finance Canada, 6 hours ago</sub>  
  Find the latest State Street SPDR S&P Transportation ETF (XTN) stock quote, history, news and other vital information to help you with your stock trading...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.03% (+0.00 on the week) | 5-year 5.05% (+0.06 on the week) | 10-year 5.27% (+0.15 on the week) | 30-year 5.62% (+0.22 on the week)
Yield curve, 10-year minus 3-month: +1.24 points -- upward sloping (normal)
US dollar index: 101.27 (+0.17 on the week)
Volatility (VIX): 15.90 (+0.7 on the week) -- elevated
Latest US data: inflation 3.4% (2026-08-01) | unemployment 4.1% (2026-08-01) | jobless claims 197k (2026-09-19)
Policy and expectations: Fed target 4.00% | market expects 2.4% inflation over 10 years
Rate path: 2-year Treasury 4.92% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score -0.40</summary>

```text
Last close 79.25 (bar of 2026-09-30), from 502 daily bars
Trend: vs 20d SMA 81.07 (-2.2%), 50d 84.43 (-6.1%), 200d 81.23 (-2.4%); 50d above 200d
Momentum: RSI(14) 32.8 | MACD -1.610 vs signal -1.581 (histogram -0.029)
Returns: 1d -0.3% | 5d -0.6% | 1m -6.9% | 3m -9.5%
52-week range: 68.14 - 90.01 (now 50.8% of the way up)
Volatility: ATR(14) 1.14 (1.4% of price) | annualised 20d 13.3%
Volume: 0.20x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.00</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score +0.00</summary>

```text
Fund type: Industrials
What it holds: P/E 20.28 | P/B 4.25 | P/S 1.45 | 3y earnings growth n/a
Yield: 0.9%
Three-year record: +11.8% a year | beta to the market 1.28
Cost and size: expense ratio 0.37% | net assets 2.20B
What it is made of: Stocks 99.8%, Cash 0.2%
Largest holdings: Union Pacific Corp 17.8%, Uber Technologies Inc 15.4%, CSX Corp 9.4%, United Parcel Service Inc Class B 5.6%, Norfolk Southern Corp 4.9%
Sector mix: Industrials 83.8%, Technology 16.2%
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
Rolled up from the 5 largest holdings, 53.1% of the fund by weight
Ratings by weight: buy 90.8% | hold 9.2% | sell 0.0% (mean 1.84 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +26.3% above the current prices
Holdings read: UNP, UBER, CSX, UPS, NSC
Recent rating changes among them:
  - UNP: 2026-09-16 UBS: up, Neutral -> Buy
  - UBER: 2026-09-09 Scotiabank: init, ? -> Sector Outperform
  - CSX: 2026-09-18 B of A Securities: main, Buy -> Buy
  - UPS: 2026-07-29 Stifel: main, Buy -> Buy
  - NSC: 2026-07-27 BMO Capital: main, Market Perform -> Market Perform
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
Direction: flat (1 week)
Share count change: 1 week: +0.0% (0.00) over 12d
Shares outstanding: 2.80M | fund size: 221.91M
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Saudi Arabia (KSA) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> No macro policy or data surprise; technicals show downtrend with low volume and no decisive break; analyst coverage limited to 44.4% of fund despite bullish rating; modest positive fund flows; energy sector pressure despite high oil prices.

**Main reasons it gave:**
- No macro policy or data surprise (inflation 3.4%, unemployment 4.1%)
- Technical downtrend: price below 20d, 50d, 200d SMAs; RSI 27.7; volume 0.5x avg
- Analyst coverage limited to 44.4% of fund, 90% buy rating, price target +18.1%
- Fund flows: share count +1.4% (money in) over 1 week
- Energy sector pressure: oil near $100 but XLE ETF falling

<details><summary><b>News</b> — score +0.00</summary>

- [VH10 ETF Holdings List — HAN:VH10](https://www.tradingview.com/symbols/HAN-VH10/holdings/)  
  <sub>TradingView, 18 hours ago</sub>  
  Explore HSBC Global Funds ICAV - Global Sukuk UCITS ETF Accum Shs -ETFC- USD holdings with weight, market value, and other helpful data to make more...
- [Nokia Deepfield Cloud Intelligence Expands Across Zain KSA Network](https://www.benzinga.com/trading-ideas/movers/26/09/62059357/nokia-deepfield-cloud-intelligence-expands-across-zain-ksa-network)  
  <sub>Benzinga, 22 hours ago</sub>  
  Nokia's Deepfield Cloud Intelligence provides Zain KSA real-time visibility into applications and services to proactively identify congestion and latency...
- [Oil Near $100 Should Lift Energy. Instead XLE ETF Is Falling — Here's Why](https://www.tradingview.com/news/benzinga:2050858ae094b:0-oil-near-100-should-lift-energy-instead-xle-etf-is-falling-here-s-why/)  
  <sub>TradingView, 23 hours ago</sub>  
  Oil prices above $100 a barrel and Treasury yields near multi-year highs would ordinarily create a favorable backdrop for energy stocks and a challenging...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.03% (+0.00 on the week) | 5-year 5.05% (+0.06 on the week) | 10-year 5.27% (+0.15 on the week) | 30-year 5.62% (+0.22 on the week)
Yield curve, 10-year minus 3-month: +1.24 points -- upward sloping (normal)
US dollar index: 101.27 (+0.17 on the week)
Volatility (VIX): 15.90 (+0.7 on the week) -- elevated
Latest US data: inflation 3.4% (2026-08-01) | unemployment 4.1% (2026-08-01) | jobless claims 197k (2026-09-19)
Policy and expectations: Fed target 4.00% | market expects 2.4% inflation over 10 years
Rate path: 2-year Treasury 4.92% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score -0.20</summary>

```text
Last close 36.40 (bar of 2026-09-30), from 502 daily bars
Trend: vs 20d SMA 37.57 (-3.1%), 50d 37.78 (-3.7%), 200d 38.13 (-4.5%); 50d below 200d
Momentum: RSI(14) 27.7 | MACD -0.413 vs signal -0.272 (histogram -0.141)
Returns: 1d -0.0% | 5d -2.1% | 1m -6.2% | 3m -3.3%
52-week range: 35.83 - 41.03 (now 10.9% of the way up)
Volatility: ATR(14) 0.29 (0.8% of price) | annualised 20d 8.7%
Volume: 0.50x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.00</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score +0.00</summary>

```text
Fund type: Focused Region
What it holds: P/E 15.00 | P/B 1.81 | P/S 3.04 | 3y earnings growth n/a
Yield: 2.7%
Three-year record: +1.3% a year | beta to the market 0.18
Cost and size: expense ratio 0.75% | net assets 638.50M
What it is made of: Stocks 99.7%, Cash 0.3%
Largest holdings: Al Rajhi Bank 14.1%, Saudi Arabian Oil Co 11.1%, Saudi National Bank 8.8%, Saudi Telecom Co 6.0%, Saudi Arabian Mining Co 4.4%
Sector mix: Financial services 41.9%, Basic materials 12.7%, Energy 12.1%, Communication services 8.8%
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
Rolled up from the 5 largest holdings, 44.4% of the fund by weight
Ratings by weight: buy 90.0% | hold 10.0% | sell 0.0% (mean 2.08 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +18.1% above the current prices
Holdings read: 1120.SR, 2222.SR, 1180.SR, 7010.SR, 1211.SR
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
Direction: money coming in (1 week)
Share count change: 1 week: +1.4% (8.54M) over 7d
Shares outstanding: 17.25M | fund size: 627.97M
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### China (MCHI) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Neutral overall – no macro surprise, no decisive technical breakout, and only modest bullish signals from flows, fundamentals and analyst view.

**Main reasons it gave:**
- Modest net inflows (+0.7% share count increase) indicate slight bullish demand but limited magnitude
- Fundamentals show low valuation (P/E 11.9) and decent yield (2.0%) supporting a modestly positive view
- Analyst view covers only 32.2% of the fund, rating 100% buy with +56% price target, but limited coverage reduces impact
- Technical indicators show price below 20‑day, 50‑day, 200‑day SMAs and RSI 39.3 (oversold) without a decisive breakout

<details><summary><b>News</b> — score +0.00</summary>

- [ETFs Investing in Chongqing Rural Commercial Bank Co. Ltd. Class H Stocks](https://www.tradingview.com/symbols/HAN-C3B/etfs/)  
  <sub>TradingView, 22 hours ago</sub>  
  Explore funds investing in C3B in a single list with price, expense ratio, and more stats for an in-depth analysis of new opportunities.
- [ETFs Investing in Aluminum Corporation of China Limited Class H Stocks](https://www.tradingview.com/symbols/HAN-AOC/etfs/)  
  <sub>TradingView, 10 hours ago</sub>  
  Explore funds investing in AOC in a single list with price, expense ratio, and more stats for an in-depth analysis of new opportunities.
- [ETFs Investing in China Longyuan Power Group Corporation Ltd Class H Stocks](https://www.tradingview.com/symbols/HAN-6WX/etfs/)  
  <sub>TradingView, 15 hours ago</sub>  
  Explore funds investing in 6WX in a single list with price, expense ratio, and more stats for an in-depth analysis of new opportunities.
- [ETFs Investing in Yankuang Energy Group Company Limited Class H Stocks](https://www.tradingview.com/symbols/HAN-YZCA/etfs/)  
  <sub>TradingView, 16 hours ago</sub>  
  Explore funds investing in YZCA in a single list with price, expense ratio, and more stats for an in-depth analysis of new opportunities.
- [ETFs Investing in Shandong Gold Mining Co., Ltd. Class H Stocks](https://www.tradingview.com/symbols/HAN-188H/etfs/)  
  <sub>TradingView, 23 hours ago</sub>  
  Explore funds investing in 188H in a single list with price, expense ratio, and more stats for an in-depth analysis of new opportunities.
- [ETFs Investing in CMOC Group Limited Class H Stocks](https://www.tradingview.com/symbols/HAN-D7N/etfs/)  
  <sub>TradingView, 22 hours ago</sub>  
  Explore funds investing in D7N in a single list with price, expense ratio, and more stats for an in-depth analysis of new opportunities.
- [ETFs Investing in Ganfeng Lithium Group Co., Ltd. Class H Stocks](https://www.tradingview.com/symbols/HAN-39EA/etfs/)  
  <sub>TradingView, 22 hours ago</sub>  
  Explore funds investing in 39EA in a single list with price, expense ratio, and more stats for an in-depth analysis of new opportunities.
- [ETFs Investing in Sinopharm Group Co., Ltd. Class H Stocks](https://www.tradingview.com/symbols/HAN-X2S/etfs/)  
  <sub>TradingView, 22 hours ago</sub>  
  Explore funds investing in X2S in a single list with price, expense ratio, and more stats for an in-depth analysis of new opportunities.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.03% (+0.00 on the week) | 5-year 5.05% (+0.06 on the week) | 10-year 5.27% (+0.15 on the week) | 30-year 5.62% (+0.22 on the week)
Yield curve, 10-year minus 3-month: +1.24 points -- upward sloping (normal)
US dollar index: 101.27 (+0.17 on the week)
Volatility (VIX): 15.90 (+0.7 on the week) -- elevated
Latest US data: inflation 3.4% (2026-08-01) | unemployment 4.1% (2026-08-01) | jobless claims 197k (2026-09-19)
Policy and expectations: Fed target 4.00% | market expects 2.4% inflation over 10 years
Rate path: 2-year Treasury 4.92% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 52.32 (bar of 2026-09-30), from 502 daily bars
Trend: vs 20d SMA 53.25 (-1.7%), 50d 54.37 (-3.8%), 200d 56.90 (-8.1%); 50d below 200d
Momentum: RSI(14) 39.3 | MACD -0.535 vs signal -0.460 (histogram -0.075)
Returns: 1d +0.4% | 5d -1.6% | 1m -4.4% | 3m +1.5%
52-week range: 50.48 - 66.99 (now 11.1% of the way up)
Volatility: ATR(14) 0.59 (1.1% of price) | annualised 20d 15.4%
Volume: 0.55x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.40</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score +0.40</summary>

```text
Fund type: Greater China Region
What it holds: P/E 11.90 | P/B 1.39 | P/S 1.38 | 3y earnings growth n/a
Yield: 2.0%
Three-year record: +9.7% a year | beta to the market 0.44
Cost and size: expense ratio 0.59% | net assets 6.33B
What it is made of: Stocks 99.8%, Cash 0.2%
Largest holdings: Tencent Holdings Ltd 13.9%, Alibaba Group Holding Ltd Ordinary Shares 9.6%, China Construction Bank Corp Class H 4.0%, Industrial And Commercial Bank Of China Ltd Class H 2.5%, Xiaomi Corp Class B 2.4%
Sector mix: Consumer cyclical 23.4%, Financial services 20.0%, Communication services 18.2%, Technology 11.8%
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
Rolled up from the 5 largest holdings, 32.2% of the fund by weight
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 1.40 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +56.0% above the current prices
Holdings read: 0700.HK, 9988.HK, 00939, 01398, 1810.HK
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
Direction: money coming in (1 week)
Share count change: 1 week: +0.7% (43.11M) over 7d
Shares outstanding: 119.85M | fund size: 6.27B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Chip makers (SMH) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Neutral overall; no macro surprise, flat fund flows, bullish technicals with low volume, and strong analyst coverage but not enough to outweigh the lack of new catalyst.

**Main reasons it gave:**
- 10-year Treasury yield up 15 bps this week
- Fund flows flat (0% change) over 1 week
- RSI 62.2 and MACD positive but volume 0.22x 20‑day average
- Analyst coverage 49.2% of fund with 100% buy rating and +34.4% price target

<details><summary><b>News</b> — score +0.00</summary>

- [Is State Street SPDR S&P Semiconductor ETF (XSD) a Strong ETF Right Now?](https://finance.yahoo.com/markets/stocks/articles/state-street-spdr-p-semiconductor-092002347.html)  
  <sub>Yahoo Finance, 6 hours ago</sub>  
  Launched on 01/31/2006, the State Street SPDR S&P Semiconductor ETF (XSD) is a smart beta exchange traded fund offering broad exposure to the Technology...
- [Korea launches its own version of popular US fund Roundhill Memory ETF DRAM](https://www.kedglobal.com/stocks/newsView/ked202609290005)  
  <sub>KED Global, 20 hours ago</sub>  
  South Korean retail investors' appetite for US-listed memory semiconductor exchange traded funds (ETF) is prompting the launch of a local version aimed a.
- [30-Year Yield Hits 2002 High; Credit-Score Giant FICO Plunges 27%: Stock Market Today](https://www.tradingview.com/news/benzinga:0b9ed21e4094b:0-30-year-yield-hits-2002-high-credit-score-giant-fico-plunges-27-stock-market-today/)  
  <sub>TradingView, 22 hours ago</sub>  
  U.S. stocks were little changed by midday Tuesday, with small caps and the Dow lagging while tech held up, as the 10-year Treasury yield pushed to its...
- [Memory stocks face a new test as pricing momentum cools ahead of Micron (SMH:NASDAQ)](https://seekingalpha.com/news/4648405-memory-stocks-face-a-new-test-as-pricing-momentum-cools-ahead-of-micron)  
  <sub>Seeking Alpha, 4 hours ago</sub>  
  Memory stocks rally ahead of Micron (MU) earnings, but non-HBM pricing may be peaking.
- [Heavy Bond Pressure Continues to Hurt Stocks](https://pro.thestreet.com/market-commentary/heavy-bond-pressure-continues-to-hurt-stocks)  
  <sub>TheStreet Pro, 23 hours ago</sub>  
  Dismal market action continued on Tuesday morning. The most notable development was new lows in bonds despite oversold technical conditions.
- [S&P 500, Nasdaq, Dow End Higher On SpaceX Strong Debut And US-Iran Peace Signals — SPCX, SHEL, ROKU, XOM, HOOD In Focus](https://stocktwits.com/news-articles/markets/equity/s-and-p-500-nasdaq-dow-end-higher-on-space-x-strong-debut-and-us-iran-peace-signals-spcx-shel-roku-xom-hood-in-focus/cZKdaEuR75L)  
  <sub>Stocktwits, 17 hours ago</sub>  
  U.S. stock indices gained on Friday to end the week higher amid renewed hopes of diplomacy between the U.S. and Iran, while SpaceX's strong trading debut...
- [ETFs Investing in STMicroelectronics NV Sponsored ADR RegS Stocks](https://www.tradingview.com/symbols/HAN-SGMR/etfs/)  
  <sub>TradingView, 21 hours ago</sub>  
  Explore funds investing in SGMR in a single list with price, expense ratio, and more stats for an in-depth analysis of new opportunities.
- [Dow Hits Record High On Strong Banks And Industrial Stocks, Nasdaq And S&P 500 Slip On Tech Weakness — SPCX, YUM, HOOD, RIVN, AAPL, SNAP In Focus](https://stocktwits.com/news-articles/markets/equity/dow-hits-record-high-on-strong-banks-and-industrial-stocks-nasdaq-and-s-and-p-500-slip-on-tech-weakness-spcx-yum-hood-rivn-aapl-snap-in-focus/cZKhcEcR74o)  
  <sub>Stocktwits, 14 hours ago</sub>  
  The Dow Jones index gained on Tuesday, hitting fresh highs as cooling oil prices pushed industrials and materials stocks higher and calmed inflation worries...
- [S&P 500, Dow Extend Losses From Elevated Yield Pressure — SPCX, TGT, AAPL, MU, NTAP In Focus](https://stocktwits.com/news-articles/markets/equity/s-and-p-500-dow-extend-losses-from-elevated-yield-pressure-spcx-tgt-aapl-mu-ntap-in-focus/cZMZLlCRBW0)  
  <sub>Stocktwits, 16 hours ago</sub>  
  The S&P 500 ended Tuesday 0.2% lower, the Nasdaq 100 rose 0.2%, and the Dow Jones Industrial Average fell 0.3%.
- [Jonah Lupton: DRAM and SMH compared for ETF performance](https://tradersunion.com/news/market-voices/show/3568907-dram-smh-etf-comparison/)  
  <sub>Traders Union, 23 hours ago</sub>  
  Jonah Lupton compares DRAM and SMH ETFs, analyzing holdings like Micron, Samsung, and Seagate, and their forward earnings multiples.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.03% (+0.00 on the week) | 5-year 5.05% (+0.06 on the week) | 10-year 5.27% (+0.15 on the week) | 30-year 5.62% (+0.22 on the week)
Yield curve, 10-year minus 3-month: +1.24 points -- upward sloping (normal)
US dollar index: 101.27 (+0.17 on the week)
Volatility (VIX): 15.90 (+0.7 on the week) -- elevated
Latest US data: inflation 3.4% (2026-08-01) | unemployment 4.1% (2026-08-01) | jobless claims 197k (2026-09-19)
Policy and expectations: Fed target 4.00% | market expects 2.4% inflation over 10 years
Rate path: 2-year Treasury 4.92% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.20</summary>

```text
Last close 608.30 (bar of 2026-09-30), from 502 daily bars
Trend: vs 20d SMA 576.84 (+5.5%), 50d 568.21 (+7.1%), 200d 496.79 (+22.4%); 50d above 200d
Momentum: RSI(14) 62.2 | MACD 11.437 vs signal 6.866 (histogram 4.571)
Returns: 1d +0.2% | 5d +1.1% | 1m +9.3% | 3m -2.0%
52-week range: 325.10 - 668.91 (now 82.4% of the way up)
Volatility: ATR(14) 15.17 (2.5% of price) | annualised 20d 30.7%
Volume: 0.22x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score -0.20</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score -0.20</summary>

```text
Fund type: Technology
What it holds: P/E 37.78 | P/B 11.07 | P/S 13.20 | 3y earnings growth n/a
Yield: 0.2%
Three-year record: +61.5% a year | beta to the market 2.06
Cost and size: expense ratio 0.35% | net assets 67.79B
What it is made of: Stocks 99.9%, Cash 0.1%
Largest holdings: NVIDIA Corp 22.6%, Taiwan Semiconductor Manufacturing Co Ltd ADR 9.7%, Broadcom Inc 6.1%, Micron Technology Inc 5.5%, Advanced Micro Devices Inc 5.4%
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

<details><summary><b>What analysts and big funds say</b> — score +0.50</summary>

_Not available today._

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score +0.50</summary>

```text
Rolled up from the 5 largest holdings, 49.2% of the fund by weight
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 1.34 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +34.4% above the current prices
Holdings read: NVDA, TSM, AVGO, MU, AMD
Recent rating changes among them:
  - NVDA: 2026-09-29 Rosenblatt: main, Buy -> Buy
  - TSM: 2026-09-02 Stifel: init, ? -> Buy
  - AVGO: 2026-09-10 Piper Sandler: init, ? -> Overweight
  - MU: 2026-09-28 Wedbush: reit, Outperform -> Outperform
  - AMD: 2026-09-29 StoneX: reit, Buy -> Buy
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
Direction: flat (1 week)
Share count change: 1 week: +0.0% (0.00) over 12d
Shares outstanding: 11.67M | fund size: 7.10B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Turkey (TUR) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Neutral overall: technicals show a downtrend but no decisive break on volume; analyst view is bullish but only covers 39.5% of the fund; fund flows are flat; macro backdrop (rising US yields, stronger dollar) is not a surprise but modestly negative for emerging markets.

**Main reasons it gave:**
- Price below 20‑day, 50‑day and 200‑day SMAs with RSI 26.2 and negative MACD, indicating downtrend but no decisive break on volume
- Analyst ratings 100% buy for 39.5% of fund weight with +25.6% price target, but coverage is limited
- Fund flows flat over the week, showing no net inflows or outflows
- US Treasury yields rising and dollar index up, a modestly negative macro backdrop for emerging markets

<details><summary><b>News</b> — score +0.00</summary>

_No news found for this one today._

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.03% (+0.00 on the week) | 5-year 5.05% (+0.06 on the week) | 10-year 5.27% (+0.15 on the week) | 30-year 5.62% (+0.22 on the week)
Yield curve, 10-year minus 3-month: +1.24 points -- upward sloping (normal)
US dollar index: 101.27 (+0.17 on the week)
Volatility (VIX): 15.90 (+0.7 on the week) -- elevated
Latest US data: inflation 3.4% (2026-08-01) | unemployment 4.1% (2026-08-01) | jobless claims 197k (2026-09-19)
Policy and expectations: Fed target 4.00% | market expects 2.4% inflation over 10 years
Rate path: 2-year Treasury 4.92% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score -0.20</summary>

```text
Last close 33.97 (bar of 2026-09-30), from 502 daily bars
Trend: vs 20d SMA 37.95 (-10.5%), 50d 38.82 (-12.5%), 200d 39.33 (-13.6%); 50d below 200d
Momentum: RSI(14) 26.2 | MACD -1.209 vs signal -0.763 (histogram -0.446)
Returns: 1d -2.2% | 5d -9.4% | 1m -15.8% | 3m -13.3%
52-week range: 31.90 - 43.74 (now 17.5% of the way up)
Volatility: ATR(14) 0.76 (2.3% of price) | annualised 20d 36.2%
Volume: 0.98x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.00</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score +0.00</summary>

```text
Fund type: Focused Region
What it holds: P/E 13.81 | P/B 1.21 | P/S 0.66 | 3y earnings growth n/a
Yield: 2.1%
Three-year record: -0.2% a year | beta to the market 0.44
Cost and size: expense ratio 0.59% | net assets 225.08M
What it is made of: Stocks 100.4%, Cash -0.4%
Largest holdings: Aselsan Elektronik Sanayi Ve Ticaret AS 11.2%, Tupras-Turkiye Petrol Rafineleri AS 9.7%, Bim Birlesik Magazalar AS 8.7%, Akbank TAS 5.6%, Turk Hava Yollari AO 4.4%
Sector mix: Industrials 31.2%, Financial services 14.7%, Consumer defensive 11.9%, Basic materials 11.1%
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
Rolled up from the 5 largest holdings, 39.5% of the fund by weight
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 1.77 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +25.6% above the current prices
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
Direction: flat (1 week)
Share count change: 1 week: +0.0% (0.00) over 7d
Shares outstanding: 15.65M | fund size: 531.63M
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### US real estate (VNQ) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Neutral overall – analyst view is strongly bullish, but flat fund flows, high valuation metrics and modestly rising rates offset that optimism. Technicals show oversold momentum but low volume and negative MACD suggest weak upside.

**Main reasons it gave:**
- Analyst consensus 100% buy with weighted price target +20.2% (strong bullish signal)
- Fund flows flat over the past week (no net inflow/outflow, neutral insider sentiment)
- Fund fundamentals: high P/E 30.19 and yield 3.6% versus 10‑year Treasury 5.27% (valuation pressure in rising‑rate environment)
- Technical indicators: price below 20‑day, 50‑day, 200‑day SMAs; RSI 24 (oversold) but low volume and negative MACD (weak momentum)

<details><summary><b>News</b> — score +0.00</summary>

- [Panic In Real Estate CEFs: Trading NRO’s Historic Discount (Upgrade) (NYSE:NRO)](https://seekingalpha.com/article/4951018-panic-in-real-estate-cefs-trading-nros-historic-discount-upgrade)  
  <sub>Seeking Alpha, 1 hour ago</sub>  
  NRO (Neuberger Real Estate Secs) is a tactical buy after an 11% drop and extreme oversold discount to NAV.
- [ETFs Investing in Innovative Industrial Properties Inc Stocks](https://www.tradingview.com/symbols/HAN-1IK/etfs/)  
  <sub>TradingView, 21 hours ago</sub>  
  Explore funds investing in 1IK in a single list with price, expense ratio, and more stats for an in-depth analysis of new opportunities.
- [ETFs Investing in Medical Properties Trust, Inc. Stocks](https://www.tradingview.com/symbols/HAN-M3P/etfs/)  
  <sub>TradingView, 21 hours ago</sub>  
  Explore funds investing in M3P in a single list with price, expense ratio, and more stats for an in-depth analysis of new opportunities.
- [ETFs Investing in NNN REIT, Inc. Stocks](https://www.tradingview.com/symbols/HAN-CZ2/etfs/)  
  <sub>TradingView, 22 hours ago</sub>  
  Explore funds investing in CZ2 in a single list with price, expense ratio, and more stats for an in-depth analysis of new opportunities.
- [ETFs Investing in Gladstone Commercial Corporation Stocks](https://www.tradingview.com/symbols/HAN-GLE/etfs/)  
  <sub>TradingView, 22 hours ago</sub>  
  Explore funds investing in GLE in a single list with price, expense ratio, and more stats for an in-depth analysis of new opportunities.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.03% (+0.00 on the week) | 5-year 5.05% (+0.06 on the week) | 10-year 5.27% (+0.15 on the week) | 30-year 5.62% (+0.22 on the week)
Yield curve, 10-year minus 3-month: +1.24 points -- upward sloping (normal)
US dollar index: 101.27 (+0.17 on the week)
Volatility (VIX): 15.90 (+0.7 on the week) -- elevated
Latest US data: inflation 3.4% (2026-08-01) | unemployment 4.1% (2026-08-01) | jobless claims 197k (2026-09-19)
Policy and expectations: Fed target 4.00% | market expects 2.4% inflation over 10 years
Rate path: 2-year Treasury 4.92% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score -0.20</summary>

```text
Last close 90.09 (bar of 2026-09-30), from 502 daily bars
Trend: vs 20d SMA 93.46 (-3.6%), 50d 96.51 (-6.7%), 200d 94.37 (-4.5%); 50d above 200d
Momentum: RSI(14) 24.0 | MACD -1.756 vs signal -1.477 (histogram -0.279)
Returns: 1d -0.5% | 5d -1.5% | 1m -6.6% | 3m -6.9%
52-week range: 87.00 - 100.95 (now 22.2% of the way up)
Volatility: ATR(14) 1.12 (1.2% of price) | annualised 20d 11.8%
Volume: 0.31x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score -0.30</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score -0.30</summary>

```text
Fund type: Real Estate
What it holds: P/E 30.19 | P/B 2.59 | P/S 4.94 | 3y earnings growth n/a
Yield: 3.6%
Three-year record: +10.6% a year | beta to the market 0.98
Cost and size: expense ratio 0.13% | net assets 70.82B
What it is made of: Stocks 99.1%, Cash 0.7%, Other 0.2%
Largest holdings: Vanguard Real Estate II Index 14.5%, Welltower Inc 8.7%, Prologis Inc 6.9%, Equinix Inc 5.5%, American Tower Corp 4.3%
Sector mix: Real estate 99.4%, Communication services 0.4%, Energy 0.1%, Industrials 0.0%
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

<details><summary><b>What analysts and big funds say</b> — score +0.90</summary>

_Not available today._

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score +0.90</summary>

```text
Rolled up from the 5 largest holdings, 39.9% of the fund by weight
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 1.69 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +20.2% above the current prices
Holdings read: VRTPX, WELL, PLD, EQIX, AMT
Recent rating changes among them:
  - WELL: 2024-10-01 Wells Fargo: down, Overweight -> Equal-Weight
  - PLD: 2026-09-01 Wells Fargo: main, Overweight -> Overweight
  - EQIX: 2026-09-21 Rothschild & Co: init, ? -> Buy
  - AMT: 2026-08-20 Barclays: up, Equal-Weight -> Overweight
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
Direction: flat (1 week)
Share count change: 1 week: +0.0% (0.00) over 13d
Shares outstanding: 370.18M | fund size: 33.35B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Biotech (XBI) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Neutral overall – no macro surprise, technicals lack decisive break, mixed analyst view, modest inflows, positive fundamentals.

**Main reasons it gave:**
- Macro: yields modestly higher, VIX low (15.9), inflation stable (3.4%) – no surprise
- Technical: price above 20‑d SMA, RSI 50.6 (neutral), volume 0.25× 20‑d avg – no decisive break
- Analyst view: 43% buy/57% hold, weighted price target -18.3% (downside) – mixed sentiment
- Fund flows: share count +1.2% (133 M) over 7 d – modest inflow
- Fundamentals: low valuation (P/B 0.20, P/S 0.12) and strong 3‑yr record (+28.8%/yr) – positive fundamentals

<details><summary><b>News</b> — score +0.00</summary>

- [State Street SPDR S&P Biotech ETF (XBI) Stock Price, News, Quote & History](https://ca.finance.yahoo.com/quote/XBI/)  
  <sub>Yahoo! Finance Canada, 5 hours ago</sub>  
  State Street SPDR S&P Biotech ETF (XBI) · -3.13% · -3.43% · 31.12% · 28.61% · 57.76% · 24.82% · 850.36%. Key Events. Baseline. Advanced Chart.
- [GraniteShares Readies to Launch 2x Long Anthropic ETF (AIL)](https://stocktwits.com/news-articles/business/others/granite-shares-readies-to-launch-2x-long-anthropic-etf-ail/cZMFJQuRBhu)  
  <sub>Stocktwits, 1 hour ago</sub>  
  Proposed AIL ETF would provide 2x daily long exposure to Anthropic, pending its IPO and SEC effectiveness. NEW YORK, Sept. 29, 2026 (GLOBE NEWSWIRE)...
- [Is State Street SPDR S&P Semiconductor ETF (XSD) a Strong ETF Right Now?](https://finance.yahoo.com/markets/stocks/articles/state-street-spdr-p-semiconductor-092002347.html)  
  <sub>Yahoo Finance, 6 hours ago</sub>  
  Launched on 01/31/2006, the State Street SPDR S&P Semiconductor ETF (XSD) is a smart beta exchange traded fund offering broad exposure to the Technology...
- [ETFs Investing in REGENXBIO, Inc. Stocks](https://www.tradingview.com/symbols/HAN-RB0/etfs/)  
  <sub>TradingView, 20 hours ago</sub>  
  Explore funds investing in RB0 in a single list with price, expense ratio, and more stats for an in-depth analysis of new opportunities.
- [Biotech Lagged The Broader Market In September — Did Retail Favorites SLS, IBRX, VNDA And IOVA Dodge XBI’s Slump?](https://finance.yahoo.com/healthcare/articles/biotech-lagged-broader-market-september-034757461.html)  
  <sub>Yahoo Finance, 11 hours ago</sub>  
  Sellas reported preclinical pancreatic cancer findings for SLS009 as investors awaited the Phase 3 Regal leukemia readout for GPS.
- [New Grades, Price Targets for the Top-3 Stocks in Market’s Hottest Sector](https://pro.thestreet.com/trade-ideas/new-grades-price-targets-for-the-top-3-stocks-in-markets-hottest-sector)  
  <sub>TheStreet Pro, 23 hours ago</sub>  
  How hot are biotech stocks? One of the bellwethers for the industry, the iShares Biotechnology ETF (IBB) (left chart), has gained over 24% year to date.
- [Moderna stock slips as Citi cuts to Sell (MRNA:NASDAQ)](https://seekingalpha.com/news/4648418-moderna-stock-slips-citi-cuts-sell)  
  <sub>Seeking Alpha, 3 hours ago</sub>  
  Moderna (MRNA) stock falls as Citi downgrades the company to Sell, warning cancer vaccine hype has inflated valuation. Read more here.
- [ETFs Investing in Kura Oncology, Inc. Stocks](https://www.tradingview.com/symbols/HAN-KUR/etfs/)  
  <sub>TradingView, 18 hours ago</sub>  
  Explore funds investing in KUR in a single list with price, expense ratio, and more stats for an in-depth analysis of new opportunities.
- [Michael Burry Says His Puts Give Him 'Far More Upside' In A Crash As He Pulls His AI Bubble Timeline Forward](https://stocktwits.com/news-articles/markets/equity/michael-burry-puts-far-more-upside-crash-pulls-ai-bubble-timeline-forward/cZMnDzGRBWH)  
  <sub>Stocktwits, 6 hours ago</sub>  
  Fresh research accelerated Burry's bearish AI timeline from an earlier 2028 base case, prompting a shift toward more leveraged positions.
- [BofA Raises Odds Of Success For Immix Biopharma’s NXC-201 Therapy — Sees Over 190% Upside In IMMX Stock](https://stocktwits.com/news-articles/markets/equity/bofa-raises-immix-price-target-after-clinical-trial-result/cZMZ7RQRBWI)  
  <sub>Stocktwits, 21 hours ago</sub>  
  Immix Biopharma's latest clinical results showed strong patient responses to its lead CAR-T candidate as the biotech firm prepares for a planned regulatory...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.03% (+0.00 on the week) | 5-year 5.05% (+0.06 on the week) | 10-year 5.27% (+0.15 on the week) | 30-year 5.62% (+0.22 on the week)
Yield curve, 10-year minus 3-month: +1.24 points -- upward sloping (normal)
US dollar index: 101.27 (+0.17 on the week)
Volatility (VIX): 15.90 (+0.7 on the week) -- elevated
Latest US data: inflation 3.4% (2026-08-01) | unemployment 4.1% (2026-08-01) | jobless claims 197k (2026-09-19)
Policy and expectations: Fed target 4.00% | market expects 2.4% inflation over 10 years
Rate path: 2-year Treasury 4.92% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 158.53 (bar of 2026-09-30), from 502 daily bars
Trend: vs 20d SMA 158.35 (+0.1%), 50d 157.98 (+0.3%), 200d 138.52 (+14.4%); 50d above 200d
Momentum: RSI(14) 50.6 | MACD -0.752 vs signal -0.608 (histogram -0.144)
Returns: 1d +1.1% | 5d +2.1% | 1m -2.4% | 3m +1.3%
52-week range: 100.20 - 169.55 (now 84.1% of the way up)
Volatility: ATR(14) 4.01 (2.5% of price) | annualised 20d 25.3%
Volume: 0.25x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.30</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score +0.30</summary>

```text
Fund type: Health
What it holds: P/E n/a | P/B 0.20 | P/S 0.12 | 3y earnings growth n/a
Yield: 0.3%
Three-year record: +28.8% a year | beta to the market 1.12
Cost and size: expense ratio 0.35% | net assets 11.40B
What it is made of: Stocks 100.0%, Cash 0.0%
Largest holdings: Moderna Inc 2.8%, Twist Bioscience Corp 1.9%, Apogee Therapeutics Inc 1.5%, Kymera Therapeutics Inc Ordinary Shares 1.4%, Halozyme Therapeutics Inc 1.4%
Sector mix: Healthcare 99.3%, Financial services 0.7%
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

<details><summary><b>What analysts and big funds say</b> — score +0.00</summary>

_Not available today._

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score +0.00</summary>

```text
Rolled up from the 5 largest holdings, 9.0% of the fund by weight  -- thin, so read this as a fact about that slice rather than the fund
Ratings by weight: buy 43.2% | hold 56.8% | sell 0.0% (mean 2.28 on a 1=strong buy to 5=strong sell scale)
Weighted price target: -18.3% above the current prices
Holdings read: MRNA, TWST, APGE, KYMR, HALO
Recent rating changes among them:
  - MRNA: 2026-09-30 Citigroup: down, Neutral -> Sell
  - TWST: 2026-09-29 Leerink Partners: main, Outperform -> Outperform
  - APGE: 2026-08-13 Truist Securities: main, Hold -> Hold
  - KYMR: 2026-09-22 Stifel: main, Buy -> Buy
  - HALO: 2026-09-02 HC Wainwright & Co.: reit, Buy -> Buy
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
Direction: money coming in (1 week)
Share count change: 1 week: +1.2% (133.41M) over 7d
Shares outstanding: 73.61M | fund size: 11.67B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### US house builders (XHB) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Analyst view is bullish but thin, fund outflows are bearish, fundamentals are neutral; technicals and macro are also bearish, offsetting the analyst bullishness, leading to a neutral overall stance.

**Main reasons it gave:**
- Analyst coverage of top holdings (20.9% of fund) shows 74% buy rating and +22.6% price target
- Fund flows show 2% share count outflow over the week (‑2.0% share count, ‑$26.9M)
- Technical trend: price below 20‑day, 50‑day, 200‑day SMAs; RSI 39.2; volume 0.23x 20‑day average
- Macro: 10‑year Treasury yield rose 15 bps to 5.27% and 30‑year to 5.62%, indicating higher rates pressure on consumer cyclical sector
- News: housing stocks face downside as interest rates soar, 30‑year yields at 5.62% (Housing Stocks: More Downside Likely As Interest Rates Soar)

<details><summary><b>News</b> — score +0.00</summary>

- [Housing Stocks: More Downside Likely As Interest Rates Soar (NYSEARCA:XHB)](https://seekingalpha.com/article/4950812-housing-stocks-more-downside-likely-as-interest-rates-soar)  
  <sub>Seeking Alpha, 18 hours ago</sub>  
  Surging interest rates are pressuring the housing sector, with 30-year government bond yields hitting 5.6%, their highest since 2002. Housing ETFs like XHB...
- [Are Home Prices Rising 1.9 Percent While Real Values Fall for a 14th Straight Month?](https://kalkine.ca/news/real-estate/are-home-prices-rising-19-percent-while-real-values-fall-for-a-14th-straight-month)  
  <sub>kalkine.ca, 53 minutes ago</sub>  
  You are reading a free article with opinions that may differ from the recommendation given by Kalkine in its paid research reports.
- [Is the FHFA's 0.3 Percent July Gain Hiding a 6.3 Percent Versus 0.6 Percent Regional Split?](https://kalkine.ca/news/real-estate/is-the-fhfas-03-percent-july-gain-hiding-a-63-percent-versus-06-percent-regional-split)  
  <sub>kalkine.ca, 53 minutes ago</sub>  
  You are reading a free article with opinions that may differ from the recommendation given by Kalkine in its paid research reports. Become a Kalkine member...
- [Does a 12-Year Low in Consumer Confidence at 81.9 Mean the Economy Is Cracking Before the Jobs Report?](https://www.google.com/goto?url=CAESwgEB6zswFZePamH_oT0nrtrgX2U9AljjbyHTHupwOw8dwQ_nOh4CNvLV68hKLShpW4QbSgVvkjJUwY-NJ5I9U63uq4Ou0zUpqWhSxpswT3dX8OKKJ1KqHiU1TCnBCnpxry-WCv7AhkfXWRLqhZQE1FNBdTgf74UKhRjPbMHlFbWLHH8R2i62hahRSYQvM8wfPvd91E06oa56DfeBw1rOY_tbDpX87XHauVhACsI5I3RWIcZvYLnUXdgZHQCi8xiBIqpg3Q)  
  <sub>kalkine.ca, 53 minutes ago</sub>  
  You are reading a free article with opinions that may differ from the recommendation given by Kalkine in its paid research reports. Become a Kalkine member...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.03% (+0.00 on the week) | 5-year 5.05% (+0.06 on the week) | 10-year 5.27% (+0.15 on the week) | 30-year 5.62% (+0.22 on the week)
Yield curve, 10-year minus 3-month: +1.24 points -- upward sloping (normal)
US dollar index: 101.27 (+0.17 on the week)
Volatility (VIX): 15.90 (+0.7 on the week) -- elevated
Latest US data: inflation 3.4% (2026-08-01) | unemployment 4.1% (2026-08-01) | jobless claims 197k (2026-09-19)
Policy and expectations: Fed target 4.00% | market expects 2.4% inflation over 10 years
Rate path: 2-year Treasury 4.92% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score -0.20</summary>

```text
Last close 96.68 (bar of 2026-09-30), from 502 daily bars
Trend: vs 20d SMA 98.39 (-1.7%), 50d 103.58 (-6.7%), 200d 106.27 (-9.0%); 50d below 200d
Momentum: RSI(14) 39.2 | MACD -1.941 vs signal -2.152 (histogram 0.211)
Returns: 1d -0.3% | 5d -0.4% | 1m -6.0% | 3m -14.2%
52-week range: 94.86 - 121.36 (now 6.9% of the way up)
Volatility: ATR(14) 2.06 (2.1% of price) | annualised 20d 21.8%
Volume: 0.23x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.00</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score +0.00</summary>

```text
Fund type: Consumer Cyclical
What it holds: P/E 19.52 | P/B 2.34 | P/S 1.36 | 3y earnings growth n/a
Yield: 0.8%
Three-year record: +9.0% a year | beta to the market 1.46
Cost and size: expense ratio 0.35% | net assets 1.33B
What it is made of: Stocks 100.0%, Cash 0.1%
Largest holdings: Installed Building Products Inc 4.4%, Owens-Corning Inc 4.3%, Allegion PLC 4.3%, Champion Homes Inc 4.1%, Williams-Sonoma Inc 3.9%
Sector mix: Consumer cyclical 60.7%, Industrials 37.9%, Real estate 1.5%
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
Rolled up from the 5 largest holdings, 20.9% of the fund by weight  -- thin, so read this as a fact about that slice rather than the fund
Ratings by weight: buy 74.0% | hold 26.0% | sell 0.0% (mean 2.14 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +22.6% above the current prices
Holdings read: IBP, OC, ALLE, SKY, WSM
Recent rating changes among them:
  - IBP: 2026-09-25 Evercore ISI Group: main, In-Line -> In-Line
  - OC: 2026-09-11 Wells Fargo: main, Overweight -> Overweight
  - ALLE: 2026-08-10 Morgan Stanley: main, Equal-Weight -> Equal-Weight
  - SKY: 2026-09-30 Oppenheimer: init, ? -> Perform
  - WSM: 2026-09-09 Evercore ISI Group: main, In-Line -> In-Line
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
Direction: money going out (1 week)
Share count change: 1 week: -2.0% (-26.92M) over 7d
Shares outstanding: 13.54M | fund size: 1.31B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### US materials and chemicals (XLB) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> The fund shows no clear macro catalyst or decisive technical break. Analyst coverage is bullish but limited to 37% of the fund, flows are flat, and fundamentals are moderate, leading to a neutral stance.

**Main reasons it gave:**
- Analyst view: 100% buy rating for top holdings with +14.2% price target (covers 37% of fund)
- Technicals: Price below 20‑day, 50‑day, and 200‑day SMAs; RSI 34.2 (oversold) but no decisive break
- Fund flows: Share count flat (+0.0% over 7 days), indicating no net demand
- Macro: No major policy or data surprise; yields modestly higher, VIX low

<details><summary><b>News</b> — score +0.00</summary>

- [Ten materials stocks that fell the most over the past month (XLB:NYSEARCA)](https://seekingalpha.com/news/4648446-ten-materials-stocks-that-fell-the-most-over-the-past-month)  
  <sub>Seeking Alpha, 3 hours ago</sub>  
  September 2026 stock market update: see the 10 worst-performing materials stocks (AMR, CENX, ALB & more), key sector trends & ETFs—read now.
- [State Street Health Care Select Sector SPDR ETF (XLV) stock price, news, quote and history](https://au.finance.yahoo.com/quote/XLV/)  
  <sub>Yahoo Finance Australia, 5 hours ago</sub>  
  Find the latest State Street Health Care Select Sector SPDR ETF (XLV) stock quote, history, news and other vital information to help you with your stock...
- [30-Year Yield Hits 2002 High; Credit-Score Giant FICO Plunges 27%: Stock Market Today](https://www.tradingview.com/news/benzinga:0b9ed21e4094b:0-30-year-yield-hits-2002-high-credit-score-giant-fico-plunges-27-stock-market-today/)  
  <sub>TradingView, 22 hours ago</sub>  
  U.S. stocks were little changed by midday Tuesday, with small caps and the Dow lagging while tech held up, as the 10-year Treasury yield pushed to its...
- [Best Performing ETFs: Top Returns at a Glance](https://www.tradingkey.com/markets/etf/best-performing)  
  <sub>TradingKey, 19 hours ago</sub>  
  View TradingKey's list of the best performing ETFs, including price changes, trading volume, multi-period returns, and performance charts.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.03% (+0.00 on the week) | 5-year 5.05% (+0.06 on the week) | 10-year 5.27% (+0.15 on the week) | 30-year 5.62% (+0.22 on the week)
Yield curve, 10-year minus 3-month: +1.24 points -- upward sloping (normal)
US dollar index: 101.27 (+0.17 on the week)
Volatility (VIX): 15.90 (+0.7 on the week) -- elevated
Latest US data: inflation 3.4% (2026-08-01) | unemployment 4.1% (2026-08-01) | jobless claims 197k (2026-09-19)
Policy and expectations: Fed target 4.00% | market expects 2.4% inflation over 10 years
Rate path: 2-year Treasury 4.92% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score -0.10</summary>

```text
Last close 49.15 (bar of 2026-09-30), from 502 daily bars
Trend: vs 20d SMA 50.65 (-3.0%), 50d 51.64 (-4.8%), 200d 50.62 (-2.9%); 50d above 200d
Momentum: RSI(14) 34.2 | MACD -0.741 vs signal -0.601 (histogram -0.140)
Returns: 1d +0.1% | 5d -2.2% | 1m -6.7% | 3m -3.7%
52-week range: 42.23 - 53.67 (now 60.5% of the way up)
Volatility: ATR(14) 0.71 (1.4% of price) | annualised 20d 14.2%
Volume: 0.41x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.00</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score +0.00</summary>

```text
Fund type: Natural Resources
What it holds: P/E 24.59 | P/B 3.00 | P/S 2.01 | 3y earnings growth n/a
Yield: 1.6%
Three-year record: +10.0% a year | beta to the market 0.82
Cost and size: expense ratio 0.08% | net assets 8.75B
What it is made of: Stocks 99.9%, Cash 0.1%
Largest holdings: Linde PLC 13.1%, Newmont Corp 7.8%, Freeport-McMoRan Inc 6.3%, Corteva Inc 4.9%, Air Products and Chemicals Inc 4.8%
Sector mix: Basic materials 84.5%, Consumer cyclical 15.5%
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
Rolled up from the 5 largest holdings, 37.0% of the fund by weight
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 1.70 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +14.2% above the current prices
Holdings read: LIN, NEM, FCX, CTVA, APD
Recent rating changes among them:
  - LIN: 2026-09-28 Argus Research: main, Buy -> Buy
  - NEM: 2026-09-16 RBC Capital: main, Outperform -> Outperform
  - FCX: 2026-09-16 RBC Capital: main, Sector Perform -> Sector Perform
  - CTVA: 2026-09-18 Argus Research: reit, Buy -> Buy
  - APD: 2026-09-11 Keybanc: init, ? -> Sector Weight
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
Direction: flat (1 week)
Share count change: 1 week: +0.0% (0.00) over 7d
Shares outstanding: 71.92M | fund size: 3.54B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### US media and communication (XLC) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Neutral overall: bullish analyst view offset by modest outflows and slightly bearish technicals, with no macro surprise.

**Main reasons it gave:**
- Analyst consensus: 100% buy, weighted price target +16% above current price
- Fund flows: 1‑week share count down 1.8% ($412 M net redemption)
- Technical indicators: price below 20‑day SMA, MACD below signal, RSI 48.9
- Macro: no rate or inflation surprise; yields modestly up, VIX low

<details><summary><b>News</b> — score +0.00</summary>

- [These communication services stocks outperformed in September (XLC:NYSEARCA)](https://seekingalpha.com/news/4648166-these-communication-services-stocks-outperformed-in-september)  
  <sub>Seeking Alpha, 21 hours ago</sub>  
  Top communication services stocks for September 2026: 1-month winners led by AMC and Meta, plus Quant Ratings and ETF ideas—see the full list now.
- [Paramount Skydance Falls 3% as $44.4B Bond Sale for Warner Deal Reaches Investors; Netflix Ticks Up, Warner Bros. Discovery Holds Flat](https://247wallst.com/investing/2026/09/29/paramount-skydance-falls-3-as-44-4b-bond-sale-for-warner-deal-reaches-investors-netflix-ticks-up-warner-bros-discovery-holds-flat/)  
  <sub>24/7 Wall St., 21 hours ago</sub>  
  Paramount Skydance is hauling a mountain of debt into credit markets to finance its Warner Bros. Discovery takeover, and the split between a sinking...
- [ETFs Investing in Fox Corporation Class A Stocks](https://www.tradingview.com/symbols/HAN-FO5/etfs/)  
  <sub>TradingView, 23 hours ago</sub>  
  Explore funds investing in FO5 in a single list with price, expense ratio, and more stats for an in-depth analysis of new opportunities.
- [T Paid Holders $58 Billion While The Stock Trailed The Market](https://www.trefis.com/stock/t/articles/616906/t-paid-holders-58-billion-while-the-stock-trailed-the-market/2026-09-29)  
  <sub>Trefis, 23 hours ago</sub>  
  The telecom giant showered its owners with cash while its stock trailed the market, raising a sharp question about what all that money actually bought.
- [ETFs Investing in News Corporation Class A Stocks](https://www.tradingview.com/symbols/HAN-NC0/etfs/)  
  <sub>TradingView, 23 hours ago</sub>  
  Explore funds investing in NC0 in a single list with price, expense ratio, and more stats for an in-depth analysis of new opportunities.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.03% (+0.00 on the week) | 5-year 5.05% (+0.06 on the week) | 10-year 5.27% (+0.15 on the week) | 30-year 5.62% (+0.22 on the week)
Yield curve, 10-year minus 3-month: +1.24 points -- upward sloping (normal)
US dollar index: 101.27 (+0.17 on the week)
Volatility (VIX): 15.90 (+0.7 on the week) -- elevated
Latest US data: inflation 3.4% (2026-08-01) | unemployment 4.1% (2026-08-01) | jobless claims 197k (2026-09-19)
Policy and expectations: Fed target 4.00% | market expects 2.4% inflation over 10 years
Rate path: 2-year Treasury 4.92% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score -0.20</summary>

```text
Last close 111.94 (bar of 2026-09-30), from 502 daily bars
Trend: vs 20d SMA 112.60 (-0.6%), 50d 111.39 (+0.5%), 200d 113.86 (-1.7%); 50d below 200d
Momentum: RSI(14) 48.9 | MACD 0.135 vs signal 0.352 (histogram -0.217)
Returns: 1d +0.4% | 5d -0.6% | 1m +0.4% | 3m +2.0%
52-week range: 105.38 - 120.08 (now 44.6% of the way up)
Volatility: ATR(14) 1.73 (1.5% of price) | annualised 20d 21.3%
Volume: 0.35x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.20</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score +0.20</summary>

```text
Fund type: Communications
What it holds: P/E 15.38 | P/B 2.92 | P/S 2.06 | 3y earnings growth n/a
Yield: 1.3%
Three-year record: +20.4% a year | beta to the market 0.85
Cost and size: expense ratio 0.08% | net assets 22.43B
What it is made of: Stocks 99.8%, Cash 0.2%
Largest holdings: Meta Platforms Inc Class A 16.8%, Alphabet Inc Class A 10.3%, Alphabet Inc Class C 8.2%, AT&T Inc 5.3%, Verizon Communications Inc 5.0%
Sector mix: Communication services 100.0%
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
Rolled up from the 5 largest holdings, 45.5% of the fund by weight
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 1.56 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +16.0% above the current prices
Holdings read: META, GOOGL, GOOG, T, VZ
Recent rating changes among them:
  - META: 2024-09-30 Cantor Fitzgerald: reit, Overweight -> Overweight
  - GOOGL: 2026-09-28 Piper Sandler: reit, Overweight -> Overweight
  - GOOG: 2026-07-23 JP Morgan: main, Overweight -> Overweight
  - T: 2026-09-28 Morgan Stanley: main, Overweight -> Overweight
  - VZ: 2026-07-27 TD Cowen: main, Buy -> Buy
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
Direction: money going out (1 week)
Share count change: 1 week: -1.8% (-412.22M) over 7d
Shares outstanding: 198.62M | fund size: 22.23B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### US energy companies (XLE) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Most macro and technical signals are muted; no policy surprise or decisive technical break. Analyst coverage is bullish but fundamentals and inventory data point bearish, netting a neutral stance.

**Main reasons it gave:**
- Analyst view: 100% buy rating on top holdings with +6.1% price target
- Crude oil inventories built +3.0 MMbbl (58th percentile) – bearish supply pressure
- EIA forecast: WTI price down ~10% over six months
- Fund flows: share count flat (0% change) – neutral demand
- Technicals: RSI 44.1, MACD negative – weak bearish momentum

<details><summary><b>News</b> — score +0.00</summary>

- [Treasury Yields Lose Momentum as Energy ETF Retreats](https://www.forex.com/en-sg/news-and-analysis/treasury-yields-lose-momentum-as-energy-etf-retreats/)  
  <sub>FOREX.com, 5 hours ago</sub>  
  The 10-year Treasury yield is testing a resistance zone respected since the 1920s, as bearish RSI divergence signals fading upside momentum.
- [Oil Near $100, So Why Is XLE Falling? - State Street Energy Select Sector SPDR ETF (ARCA:XLE)](https://www.benzinga.com/etfs/sector-etfs/26/09/62056334/oil-near-100-should-lift-energy-instead-xle-etf-is-falling-heres-why)  
  <sub>Benzinga, 23 hours ago</sub>  
  Oil near $100 and Treasury yields above 5% are pressuring markets; XLK is rising while XLE falls. Here's what's driving the ETF split.
- [Nvidia Reverses After $150B Buyback News, But This NVDA-Tied ETF Is Still the Market’s Most Traded](https://www.tradingview.com/news/benzinga:695b16ccf094b:0-nvidia-reverses-after-150b-buyback-news-but-this-nvda-tied-etf-is-still-the-market-s-most-traded/)  
  <sub>TradingView, 18 hours ago</sub>  
  Nvidia Corp's NASDAQ:NVDA blockbuster $150 billion buyback announcement may have powered Monday's rally, but the AI chipmaker's reversal on Tuesday is...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.03% (+0.00 on the week) | 5-year 5.05% (+0.06 on the week) | 10-year 5.27% (+0.15 on the week) | 30-year 5.62% (+0.22 on the week)
Yield curve, 10-year minus 3-month: +1.24 points -- upward sloping (normal)
US dollar index: 101.27 (+0.17 on the week)
Volatility (VIX): 15.90 (+0.7 on the week) -- elevated
Latest US data: inflation 3.4% (2026-08-01) | unemployment 4.1% (2026-08-01) | jobless claims 197k (2026-09-19)
Policy and expectations: Fed target 4.00% | market expects 2.4% inflation over 10 years
Rate path: 2-year Treasury 4.92% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score -0.20</summary>

```text
Last close 61.84 (bar of 2026-09-30), from 502 daily bars
Trend: vs 20d SMA 63.70 (-2.9%), 50d 61.98 (-0.2%), 200d 56.38 (+9.7%); 50d above 200d
Momentum: RSI(14) 44.1 | MACD -0.144 vs signal 0.300 (histogram -0.444)
Returns: 1d +0.5% | 5d -0.8% | 1m -3.3% | 3m +17.1%
52-week range: 42.61 - 65.93 (now 82.5% of the way up)
Volatility: ATR(14) 1.19 (1.9% of price) | annualised 20d 19.9%
Volume: 0.25x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score -0.40</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score -0.40</summary>

```text
Fund type: Equity Energy
What it holds: P/E 17.74 | P/B 2.58 | P/S 1.68 | 3y earnings growth n/a
Yield: 2.4%
Three-year record: +13.9% a year | beta to the market -0.07
Cost and size: expense ratio 0.08% | net assets 41.44B
What it is made of: Stocks 99.8%, Cash 0.2%
Largest holdings: ExxonMobil Holdings Corp 19.9%, Chevron Corp 14.9%, ConocoPhillips 6.2%, Marathon Petroleum Corp 5.4%, Phillips 66 5.3%
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
US inventories, week ending 2026-09-18 (published the following Wednesday)
  Crude oil: 426.4 million barrels, +3.0 on the week (a build), 58% percentile over 52 weeks
  Petrol: 206.0 million barrels, -1.7 on the week (a draw), 8% percentile over 52 weeks -- low for the time of year
  Diesel: 107.4 million barrels, -0.4 on the week (a draw), 33% percentile over 52 weeks
  Natural gas: 3,351.0 billion cubic feet, +53.0 on the week (a build), 73% percentile over 52 weeks
A build is more supply than demand and a draw is the reverse, so a build reads bearish and a draw bullish -- as a rule of thumb, not a law. Weigh the change and how unusual the level is above the level itself, and remember the market has already seen this number.
```

</details>

<details><summary><b>How the crop is growing</b> — score -0.40</summary>

_Not available today._

</details>

<details><summary><b>What analysts and big funds say</b> — score +0.50</summary>

_Not available today._

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score +0.50</summary>

```text
Rolled up from the 5 largest holdings, 51.7% of the fund by weight
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 2.05 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +6.1% above the current prices
Holdings read: XOM, CVX, COP, MPC, PSX
Recent rating changes among them:
  - XOM: 2026-09-28 TD Cowen: main, Buy -> Buy
  - CVX: 2026-09-28 TD Cowen: main, Hold -> Hold
  - COP: 2026-09-14 UBS: main, Buy -> Buy
  - MPC: 2026-09-22 Jefferies: down, Buy -> Hold
  - PSX: 2026-09-30 TD Cowen: main, Buy -> Buy
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
Direction: flat (1 week)
Share count change: 1 week: +0.0% (0.00) over 7d
Shares outstanding: 186.42M | fund size: 11.53B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### US banks and finance (XLF) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Neutral overall as there is no macro surprise, technical weakness, flat fund flows, and mixed signals from bullish analyst view versus recent sector weakness.

**Main reasons it gave:**
- Financial stocks down 0.7% in afternoon trading (NYSE Financial Index)
- XLF price below 20‑day (56.05) and 50‑day (56.92) SMAs, RSI 27.1 (oversold) with low volume
- Analyst consensus 100% buy, weighted price target +14.5% above current (41.5% coverage)
- Fund flows flat: share count unchanged (+0.0% over 1 week)

<details><summary><b>News</b> — score +0.00</summary>

- [State Street SPDR S&P Biotech ETF (XBI) Stock Price, News, Quote & History](https://ca.finance.yahoo.com/quote/XBI/)  
  <sub>Yahoo! Finance Canada, 5 hours ago</sub>  
  Find the latest State Street SPDR S&P Biotech ETF (XBI) stock quote, history, news and other vital information to help you with your stock trading and...
- [Sector Update: Financial Stocks Lower in Afternoon Trading](https://www.bitget.com/amp/news/detail/12560605887645)  
  <sub>Bitget, 13 hours ago</sub>  
  01:59 PM EDT, 09/29/2026 (MT Newswires) -- Financial stocks declined in Tuesday afternoon trading, with the NYSE Financial Index decreasing 0.7% and the Sta...
- [Best Performing ETFs: Top Returns at a Glance](https://www.tradingkey.com/markets/etf/best-performing)  
  <sub>TradingKey, 19 hours ago</sub>  
  View TradingKey's list of the best performing ETFs, including price changes, trading volume, multi-period returns, and performance charts.
- [Sector Update: Financial](https://www.bitget.com/amp/news/detail/12560605887569)  
  <sub>Bitget, 13 hours ago</sub>  
  01:30 PM EDT, 09/29/2026 (MT Newswires) -- Financial stocks were lower in Tuesday afternoon trading, with the NYSE Financial Index decreasing 0.7% and the S...
- [Single-country ETFs surge as investors target AI, reform plays](https://www.investmentnews.com/etfs/single-country-etfs-surge-as-investors-target-ai-reform-plays/268410)  
  <sub>InvestmentNews, 3 hours ago</sub>  
  US-listed single-country ETFs have pulled in over $26 billion year-to-date, more than four times their full-year 2025 haul, TD Securities data shows.
- [30-Year Yield Hits 2002 High; Credit-Score Giant FICO Plunges 27%: Stock Market Today](https://www.tradingview.com/news/benzinga:0b9ed21e4094b:0-30-year-yield-hits-2002-high-credit-score-giant-fico-plunges-27-stock-market-today/)  
  <sub>TradingView, 22 hours ago</sub>  
  U.S. stocks were little changed by midday Tuesday, with small caps and the Dow lagging while tech held up, as the 10-year Treasury yield pushed to its...
- [Sector Update: Financial Stocks Decline Late Afternoon](https://finance.yahoo.com/markets/stocks/articles/sector-financial-stocks-decline-afternoon-200525147.html)  
  <sub>Yahoo Finance, 19 hours ago</sub>  
  Financial stocks declined in late Tuesday afternoon trading, with the NYSE Financial Index decreasing 0.4% and the State Street Financial Select Sector SPDR...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.03% (+0.00 on the week) | 5-year 5.05% (+0.06 on the week) | 10-year 5.27% (+0.15 on the week) | 30-year 5.62% (+0.22 on the week)
Yield curve, 10-year minus 3-month: +1.24 points -- upward sloping (normal)
US dollar index: 101.27 (+0.17 on the week)
Volatility (VIX): 15.90 (+0.7 on the week) -- elevated
Latest US data: inflation 3.4% (2026-08-01) | unemployment 4.1% (2026-08-01) | jobless claims 197k (2026-09-19)
Policy and expectations: Fed target 4.00% | market expects 2.4% inflation over 10 years
Rate path: 2-year Treasury 4.92% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score -0.20</summary>

```text
Last close 53.90 (bar of 2026-09-30), from 502 daily bars
Trend: vs 20d SMA 56.05 (-3.8%), 50d 56.92 (-5.3%), 200d 53.73 (+0.3%); 50d above 200d
Momentum: RSI(14) 27.1 | MACD -0.861 vs signal -0.606 (histogram -0.256)
Returns: 1d -0.2% | 5d -1.2% | 1m -6.6% | 3m -1.6%
52-week range: 47.81 - 58.56 (now 56.6% of the way up)
Volatility: ATR(14) 0.68 (1.3% of price) | annualised 20d 13.4%
Volume: 0.29x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.30</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score +0.30</summary>

```text
Fund type: Financial
What it holds: P/E 16.36 | P/B 2.42 | P/S 3.50 | 3y earnings growth n/a
Yield: 1.4%
Three-year record: +19.2% a year | beta to the market 0.71
Cost and size: expense ratio 0.08% | net assets 54.59B
What it is made of: Stocks 99.8%, Cash 0.2%
Largest holdings: JPMorgan Chase & Co 11.7%, Berkshire Hathaway Inc Class B 11.3%, Visa Inc Class A 7.7%, Mastercard Inc Class A 5.8%, Bank of America Corp 5.0%
Sector mix: Financial services 98.1%, Technology 1.6%, Industrials 0.3%
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
Rolled up from the 5 largest holdings, 41.5% of the fund by weight
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 1.78 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +14.5% above the current prices
Holdings read: JPM, BRK-B, V, MA, BAC
Recent rating changes among them:
  - JPM: 2026-09-28 HSBC: main, Hold -> Hold
  - BRK-B: 2026-08-10 UBS: main, Buy -> Buy
  - V: 2026-08-31 RBC Capital: main, Outperform -> Outperform
  - MA: 2026-08-31 RBC Capital: main, Outperform -> Outperform
  - BAC: 2026-08-03 UBS: main, Buy -> Buy
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
Direction: flat (1 week)
Share count change: 1 week: +0.0% (0.00) over 7d
Shares outstanding: 883.44M | fund size: 47.61B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### US industry (XLI) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Neutral overall – macro rates are rising, technicals show price below key SMAs and weak momentum, while analyst coverage is bullish but not enough to offset the macro/technical backdrop.

**Main reasons it gave:**
- 10‑year Treasury yield rose 15 bps this week, indicating higher rates pressure on industrials
- XLI price below 20‑day, 50‑day, and 200‑day SMAs, showing a downtrend
- RSI at 35.6 and volume at 0.27× 20‑day average suggest weak momentum
- Analyst coverage is bullish (100 % buy, +24 % price target) but macro and technicals are neutral/bearish, leading to an overall neutral stance

<details><summary><b>News</b> — score +0.00</summary>

- [Exchange-Traded Funds, Equity Futures Lower Pre-Bell Wednesday Amid Inflation Data Release](https://finance.yahoo.com/markets/stocks/articles/exchange-traded-funds-equity-futures-132034377.html)  
  <sub>Yahoo Finance, 2 hours ago</sub>  
  The broad market exchange-traded fund SPDR S&P 500 ETF Trust (SPY) was down 0.01% and the actively t.
- [State Street SPDR S&P Biotech ETF (XBI) Stock Price, News, Quote & History](https://ca.finance.yahoo.com/quote/XBI/)  
  <sub>Yahoo! Finance Canada, 5 hours ago</sub>  
  Find the latest State Street SPDR S&P Biotech ETF (XBI) stock quote, history, news and other vital information to help you with your stock trading and...
- [Exchange-Traded Funds Lower as US Equities Drop After Midday](https://finance.yahoo.com/markets/articles/exchange-traded-funds-lower-us-171654357.html)  
  <sub>Yahoo Finance, 22 hours ago</sub>  
  Broad Market Indicators Broad-market exchange-traded funds IWM and IVV fell. Actively traded Invesco QQQ Trust (QQQ) eased 0.1%.
- [Equity ETF flows slide as summer unwind takes hold](https://seekingalpha.com/news/4648503-equity-etf-flows-slide-as-summer-unwind-takes-hold)  
  <sub>Seeking Alpha, 2 hours ago</sub>  
  Equity ETF inflows have cooled from their mid-year peak, according to Baird Strategas. Average daily flows into equity exchange traded funds stood at $3.3...
- [Oil Near $100, So Why Is XLE Falling? - State Street Energy Select Sector SPDR ETF (ARCA:XLE)](https://www.benzinga.com/etfs/sector-etfs/26/09/62056334/oil-near-100-should-lift-energy-instead-xle-etf-is-falling-heres-why)  
  <sub>Benzinga, 23 hours ago</sub>  
  Oil near $100 and Treasury yields above 5% are pressuring markets; XLK is rising while XLE falls. Here's what's driving the ETF split.
- [How (XLK) Movements Inform Risk Allocation Models](https://news.stocktradersdaily.com/news_release/38/How_XLK_Movements_Inform_Risk_Allocation_Models_092926112402_1790738642.html)  
  <sub>Stock Traders Daily, 16 hours ago</sub>  
  Key findings for Technology Select Sector Spdr Etf (NYSE: XLK). Near-Term Neutral Sentiment Suggests a Stall Amid Mid and Long-Term Strength...
- [State Street Health Care Select Sector SPDR ETF (XLV) stock price, news, quote and history](https://au.finance.yahoo.com/quote/XLV/)  
  <sub>Yahoo Finance Australia, 5 hours ago</sub>  
  Find the latest State Street Health Care Select Sector SPDR ETF (XLV) stock quote, history, news and other vital information to help you with your stock...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.03% (+0.00 on the week) | 5-year 5.05% (+0.06 on the week) | 10-year 5.27% (+0.15 on the week) | 30-year 5.62% (+0.22 on the week)
Yield curve, 10-year minus 3-month: +1.24 points -- upward sloping (normal)
US dollar index: 101.27 (+0.17 on the week)
Volatility (VIX): 15.90 (+0.7 on the week) -- elevated
Latest US data: inflation 3.4% (2026-08-01) | unemployment 4.1% (2026-08-01) | jobless claims 197k (2026-09-19)
Policy and expectations: Fed target 4.00% | market expects 2.4% inflation over 10 years
Rate path: 2-year Treasury 4.92% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score -0.20</summary>

```text
Last close 168.48 (bar of 2026-09-30), from 502 daily bars
Trend: vs 20d SMA 170.70 (-1.3%), 50d 177.31 (-5.0%), 200d 172.23 (-2.2%); 50d above 200d
Momentum: RSI(14) 35.6 | MACD -2.371 vs signal -2.586 (histogram 0.215)
Returns: 1d -0.4% | 5d -1.0% | 1m -3.8% | 3m -8.1%
52-week range: 147.83 - 186.51 (now 53.4% of the way up)
Volatility: ATR(14) 2.27 (1.3% of price) | annualised 20d 11.7%
Volume: 0.27x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.00</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score +0.00</summary>

```text
Fund type: Industrials
What it holds: P/E 28.43 | P/B 6.75 | P/S 3.00 | 3y earnings growth n/a
Yield: 1.2%
Three-year record: +20.0% a year | beta to the market 1.02
Cost and size: expense ratio 0.08% | net assets 31.95B
What it is made of: Stocks 100.0%, Cash 0.1%
Largest holdings: Caterpillar Inc 6.7%, GE Aerospace 6.4%, RTX Corp 5.1%, GE Vernova Inc 4.4%, Union Pacific Corp 3.2%
Sector mix: Industrials 92.8%, Technology 6.7%, Basic materials 0.3%, Consumer cyclical 0.2%
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
Rolled up from the 5 largest holdings, 25.8% of the fund by weight
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 1.77 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +24.0% above the current prices
Holdings read: CAT, GE, RTX, GEV, UNP
Recent rating changes among them:
  - CAT: 2024-10-14 JP Morgan: main, Overweight -> Overweight
  - GE: 2026-09-23 Jefferies: main, Buy -> Buy
  - RTX: 2026-09-23 Bernstein: main, Market Perform -> Market Perform
  - GEV: 2026-09-15 Bernstein: reit, Outperform -> Outperform
  - UNP: 2026-09-16 UBS: up, Neutral -> Buy
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
Direction: flat (1 week)
Share count change: 1 week: +0.0% (0.00) over 7d
Shares outstanding: 136.63M | fund size: 23.02B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### US technology (XLK) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> No material macro surprise, technicals show a strong uptrend but price is near 52‑week high with low volume, analyst view is bullish but only covers ~45% of the fund, and fund flows are flat.

**Main reasons it gave:**
- Treasury yields rose modestly (10‑yr +0.15% on week) with no policy surprise
- Technicals: price 196.85 above 20‑day SMA 189.92, 50‑day SMA 185.55, 200‑day SMA 164.39, near 52‑week high and volume 0.41× 20‑day average
- Analyst view: 100% buy rating, weighted price target +23.7% above current, covering 45.7% of fund
- Fund flows flat: share count change +0.0% over 13 days, indicating no net demand

<details><summary><b>News</b> — score +0.00</summary>

- [Equity ETF flows slide as summer unwind takes hold](https://seekingalpha.com/news/4648503-equity-etf-flows-slide-as-summer-unwind-takes-hold)  
  <sub>Seeking Alpha, 2 hours ago</sub>  
  Equity ETF inflows have cooled from their mid-year peak, according to Baird Strategas. Average daily flows into equity exchange traded funds stood at $3.3...
- [How (XLK) Movements Inform Risk Allocation Models](https://news.stocktradersdaily.com/news_release/38/How_XLK_Movements_Inform_Risk_Allocation_Models_092926112402_1790738642.html)  
  <sub>Stock Traders Daily, 16 hours ago</sub>  
  Key findings for Technology Select Sector Spdr Etf (NYSE: XLK). Near-Term Neutral Sentiment Suggests a Stall Amid Mid and Long-Term Strength...
- [Oil Near $100, So Why Is XLE Falling? - State Street Energy Select Sector SPDR ETF (ARCA:XLE)](https://www.benzinga.com/etfs/sector-etfs/26/09/62056334/oil-near-100-should-lift-energy-instead-xle-etf-is-falling-heres-why)  
  <sub>Benzinga, 23 hours ago</sub>  
  Oil near $100 and Treasury yields above 5% are pressuring markets; XLK is rising while XLE falls. Here's what's driving the ETF split.
- [Vanguard Tech ETF (VGT) vs. iShares Tech ETF (IYW): Which Offers Better Value for Investors?](https://finance.yahoo.com/markets/stocks/articles/vanguard-tech-etf-vgt-vs-031031771.html)  
  <sub>Yahoo Finance, 12 hours ago</sub>  
  The Vanguard Information Technology ETF (NYSEMKT:VGT) and the iShares U.S. Technology ETF (NYSEMKT:IYW) both provide concentrated exposure to the U.S. tech...
- [Exchange-Traded Funds Lower as US Equities Drop After Midday](https://finance.yahoo.com/markets/articles/exchange-traded-funds-lower-us-171654357.html)  
  <sub>Yahoo Finance, 22 hours ago</sub>  
  Broad Market Indicators Broad-market exchange-traded funds IWM and IVV fell. Actively traded Invesco QQQ Trust (QQQ) eased 0.1%.
- [Sector Update: Tech](https://finance.yahoo.com/markets/stocks/articles/sector-tech-192625390.html)  
  <sub>Yahoo Finance, 20 hours ago</sub>  
  Tech stocks were higher late Tuesday afternoon, with the State Street Technology Select Sector SPDR ETF (XLK) increasing 0.1% and the State Street SPDR S&P...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.03% (+0.00 on the week) | 5-year 5.05% (+0.06 on the week) | 10-year 5.27% (+0.15 on the week) | 30-year 5.62% (+0.22 on the week)
Yield curve, 10-year minus 3-month: +1.24 points -- upward sloping (normal)
US dollar index: 101.27 (+0.17 on the week)
Volatility (VIX): 15.90 (+0.7 on the week) -- elevated
Latest US data: inflation 3.4% (2026-08-01) | unemployment 4.1% (2026-08-01) | jobless claims 197k (2026-09-19)
Policy and expectations: Fed target 4.00% | market expects 2.4% inflation over 10 years
Rate path: 2-year Treasury 4.92% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.20</summary>

```text
Last close 196.85 (bar of 2026-09-30), from 502 daily bars
Trend: vs 20d SMA 189.92 (+3.6%), 50d 185.55 (+6.1%), 200d 164.39 (+19.7%); 50d above 200d
Momentum: RSI(14) 64.6 | MACD 3.037 vs signal 2.413 (histogram 0.625)
Returns: 1d +1.2% | 5d +0.8% | 1m +5.5% | 3m +6.0%
52-week range: 127.50 - 198.21 (now 98.1% of the way up)
Volatility: ATR(14) 3.18 (1.6% of price) | annualised 20d 17.8%
Volume: 0.41x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.00</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score +0.00</summary>

```text
Fund type: Technology
What it holds: P/E 33.01 | P/B 11.41 | P/S 8.77 | 3y earnings growth n/a
Yield: 0.4%
Three-year record: +34.4% a year | beta to the market 1.50
Cost and size: expense ratio 0.08% | net assets 121.44B
What it is made of: Stocks 100.0%, Cash 0.0%
Largest holdings: NVIDIA Corp 14.4%, Apple Inc 12.5%, Microsoft Corp 10.1%, Broadcom Inc 4.7%, Micron Technology Inc 4.0%
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
Rolled up from the 5 largest holdings, 45.7% of the fund by weight
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 1.55 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +23.7% above the current prices
Holdings read: NVDA, AAPL, MSFT, AVGO, MU
Recent rating changes among them:
  - NVDA: 2026-09-29 Rosenblatt: main, Buy -> Buy
  - AAPL: 2026-09-29 Morgan Stanley: reit, Overweight -> Overweight
  - MSFT: 2026-09-30 Piper Sandler: main, Overweight -> Overweight
  - AVGO: 2026-09-10 Piper Sandler: init, ? -> Overweight
  - MU: 2026-09-28 Wedbush: reit, Outperform -> Outperform
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
Direction: flat (1 week)
Share count change: 1 week: +0.0% (0.00) over 13d
Shares outstanding: 272.06M | fund size: 53.55B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### US everyday goods (XLP) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Neutral overall: no macro surprise, technicals bearish, analyst view bullish, but flat fund flows and stable fundamentals keep the net view neutral.

**Main reasons it gave:**
- Technical: price below 20‑day SMA (83.16), 50‑day SMA (84.54), 200‑day SMA (83.72); RSI 36.8, MACD negative
- Analyst coverage of top 5 holdings (39.6% weight) shows 100% buy rating and weighted price target +12.9% above current
- Fund flows flat: share count unchanged (+0.0% week) indicating no net demand
- Macro: Treasury yields unchanged to modestly higher, curve normal (+1.24 points), no surprise data releases

<details><summary><b>News</b> — score +0.00</summary>

- [State Street Health Care Select Sector SPDR ETF (XLV) stock price, news, quote and history](https://au.finance.yahoo.com/quote/XLV/)  
  <sub>Yahoo Finance Australia, 5 hours ago</sub>  
  State Street Health Care Select Sector SPDR ETF (XLV) · 0.49% · -0.25% · 19.17% · 10.29% · 25.63% · 32.47% · 588.08%. Key events. Baseline. Advanced...
- [Sector Update: Consumer](https://finance.yahoo.com/markets/stocks/articles/sector-consumer-192328494.html)  
  <sub>Yahoo Finance, 20 hours ago</sub>  
  Consumer stocks were mixed late Tuesday afternoon, with the State Street Consumer Staples Select Sector SPDR ETF (XLP) shedding 0.7% and the State Street...
- [Sector Update: Consumer Stocks Retreat in Afternoon Trading](https://finance.yahoo.com/markets/stocks/articles/sector-consumer-stocks-retreat-afternoon-174653676.html)  
  <sub>Yahoo Finance, 21 hours ago</sub>  
  Consumer stocks were lower Tuesday afternoon, with the State Street Consumer Staples Select Sector SPDR ETF (XLP) shedding 0.7% and the State Street...
- [Exchange-Traded Funds Lower as US Equities Drop After Midday](https://finance.yahoo.com/markets/articles/exchange-traded-funds-lower-us-171654357.html)  
  <sub>Yahoo Finance, 22 hours ago</sub>  
  Broad Market Indicators Broad-market exchange-traded funds IWM and IVV fell. Actively traded Invesco QQQ Trust (QQQ) eased 0.1%.
- [30-Year Yield Hits 2002 High; Credit-Score Giant FICO Plunges 27%: Stock Market Today](https://www.tradingview.com/news/benzinga:0b9ed21e4094b:0-30-year-yield-hits-2002-high-credit-score-giant-fico-plunges-27-stock-market-today/)  
  <sub>TradingView, 22 hours ago</sub>  
  U.S. stocks were little changed by midday Tuesday, with small caps and the Dow lagging while tech held up, as the 10-year Treasury yield pushed to its...
- [Exchange-Traded Funds, Equity Futures Lower Pre-Bell Wednesday Amid Inflation Data Release](https://finance.yahoo.com/markets/stocks/articles/exchange-traded-funds-equity-futures-132034377.html)  
  <sub>Yahoo Finance, 2 hours ago</sub>  
  The broad market exchange-traded fund SPDR S&P 500 ETF Trust (SPY) was down 0.01% and the actively t.
- [How to Play the AI Trade With a Core-Satellite ETF Strategy](https://finance.yahoo.com/technology/ai/articles/play-ai-trade-core-satellite-131700200.html)  
  <sub>Yahoo Finance, 2 hours ago</sub>  
  Unsure whether AI is a bubble or a boom? A core-satellite ETF strategy can help investors pursue AI growth without making an all-or-nothing bet.
- [Sector Update: Consumer Stocks Mixed Late Afternoon](https://finance.yahoo.com/markets/stocks/articles/sector-consumer-stocks-mixed-afternoon-194916811.html)  
  <sub>Yahoo Finance, 19 hours ago</sub>  
  Consumer stocks were mixed late Tuesday afternoon, with the State Street Consumer Staples Select Sector SPDR ETF (XLP) shedding 0.6% and the State Street...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.03% (+0.00 on the week) | 5-year 5.05% (+0.06 on the week) | 10-year 5.27% (+0.15 on the week) | 30-year 5.62% (+0.22 on the week)
Yield curve, 10-year minus 3-month: +1.24 points -- upward sloping (normal)
US dollar index: 101.27 (+0.17 on the week)
Volatility (VIX): 15.90 (+0.7 on the week) -- elevated
Latest US data: inflation 3.4% (2026-08-01) | unemployment 4.1% (2026-08-01) | jobless claims 197k (2026-09-19)
Policy and expectations: Fed target 4.00% | market expects 2.4% inflation over 10 years
Rate path: 2-year Treasury 4.92% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score -0.40</summary>

```text
Last close 81.50 (bar of 2026-09-30), from 502 daily bars
Trend: vs 20d SMA 83.16 (-2.0%), 50d 84.54 (-3.6%), 200d 83.72 (-2.6%); 50d above 200d
Momentum: RSI(14) 36.8 | MACD -0.846 vs signal -0.724 (histogram -0.121)
Returns: 1d -0.4% | 5d -1.1% | 1m -4.1% | 3m -2.2%
52-week range: 75.60 - 90.01 (now 41.0% of the way up)
Volatility: ATR(14) 0.97 (1.2% of price) | annualised 20d 10.7%
Volume: 0.26x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.00</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score +0.00</summary>

```text
Fund type: Consumer Defensive
What it holds: P/E 25.14 | P/B 4.58 | P/S 1.36 | 3y earnings growth n/a
Yield: 2.6%
Three-year record: +8.9% a year | beta to the market 0.49
Cost and size: expense ratio 0.08% | net assets 14.52B
What it is made of: Stocks 99.9%, Cash 0.1%
Largest holdings: Walmart Inc 9.8%, Costco Wholesale Corp 8.9%, Coca-Cola Co 7.3%, Procter & Gamble Co 7.2%, Philip Morris International Inc 6.2%
Sector mix: Consumer defensive 98.2%, Consumer cyclical 1.8%
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
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 1.81 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +12.9% above the current prices
Holdings read: WMT, COST, KO, PG, PM
Recent rating changes among them:
  - WMT: 2026-09-29 Mizuho: main, Outperform -> Outperform
  - COST: 2026-09-28 Deutsche Bank: main, Buy -> Buy
  - KO: 2026-09-28 JP Morgan: main, Overweight -> Overweight
  - PG: 2026-09-30 TD Cowen: reit, Hold -> Hold
  - PM: 2026-09-23 UBS: main, Neutral -> Neutral
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
Direction: flat (1 week)
Share count change: 1 week: +0.0% (0.00) over 7d
Shares outstanding: 210.17M | fund size: 17.13B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### US electricity and water (XLU) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Neutral overall; bullish analyst view is limited in coverage, technicals show a downtrend with no decisive break, fund flows are flat, and macro data show no surprise.

**Main reasons it gave:**
- Analyst coverage of top holdings is 39.4% of fund with 80.9% buy rating and +25.8% price target
- Technical indicators show downtrend (price below 20‑day, 50‑day, 200‑day SMAs) and RSI 29, but no decisive break on volume
- Fund flows flat over past week, indicating no net demand for the ETF
- Macro data show no surprise: yields up modestly, inflation 3.4% and unemployment 4.1% near expectations

<details><summary><b>News</b> — score +0.00</summary>

- [4 ETFs Seeing Unusual Options Volume Today](https://www.schaeffersresearch.com/content/options/2026/09/29/4-etfs-seeing-unusual-options-volume-today)  
  <sub>Schaeffer's Investment Research, 22 hours ago</sub>  
  HYG, EWZ, LQD, and XLU are seeing elevated options volume today, even as all four ETFs stick close to the flatline.
- [Dividend Stocks Come Under Pressure. How to Fight Back.](https://www.barrons.com/articles/dividend-stocks-options-f817e87c)  
  <sub>Barron's, 10 hours ago</sub>  
  Dividend-reliant investors can sell calls on stocks, which creates what we call “conditional dividends” that often exceed common stock dividends.
- [CDL: Low Volatility Doesn't Make Up For Low Quality, Choose SCHD Instead (NASDAQ:CDL)](https://seekingalpha.com/article/4951008-cdl-low-volatility-doesnt-make-up-for-low-quality-choose-schd-instead?source=feed_tag_etf_analysis)  
  <sub>Seeking Alpha, 1 hour ago</sub>  
  CDL ETF remains a sell despite a 3.39% yield; downside risk and quality lag SCHD.
- [(XLU) Price Dynamics and Execution-Aware Positioning](https://news.stocktradersdaily.com/news_release/40/XLU_Price_Dynamics_and_Execution-Aware_Positioning_092926112802_1790738882.html)  
  <sub>Stock Traders Daily, 16 hours ago</sub>  
  Price-action only: Utilities Select Sector Spdr Etf (XLU) movements set the tone for institutional models. (XLU) Price Dynamics and Execution-Aware...
- [Best Performing ETFs: Top Returns at a Glance](https://www.tradingkey.com/markets/etf/best-performing)  
  <sub>TradingKey, 19 hours ago</sub>  
  View TradingKey's list of the best performing ETFs, including price changes, trading volume, multi-period returns, and performance charts.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.03% (+0.00 on the week) | 5-year 5.05% (+0.06 on the week) | 10-year 5.27% (+0.15 on the week) | 30-year 5.62% (+0.22 on the week)
Yield curve, 10-year minus 3-month: +1.24 points -- upward sloping (normal)
US dollar index: 101.27 (+0.17 on the week)
Volatility (VIX): 15.90 (+0.7 on the week) -- elevated
Latest US data: inflation 3.4% (2026-08-01) | unemployment 4.1% (2026-08-01) | jobless claims 197k (2026-09-19)
Policy and expectations: Fed target 4.00% | market expects 2.4% inflation over 10 years
Rate path: 2-year Treasury 4.92% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score -0.20</summary>

```text
Last close 39.56 (bar of 2026-09-30), from 502 daily bars
Trend: vs 20d SMA 41.28 (-4.2%), 50d 42.94 (-7.8%), 200d 44.42 (-10.9%); 50d below 200d
Momentum: RSI(14) 29.0 | MACD -1.046 vs signal -0.916 (histogram -0.130)
Returns: 1d -0.4% | 5d -0.5% | 1m -6.3% | 3m -11.6%
52-week range: 39.25 - 47.73 (now 3.7% of the way up)
Volatility: ATR(14) 0.60 (1.5% of price) | annualised 20d 14.3%
Volume: 0.75x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.00</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score +0.00</summary>

```text
Fund type: Utilities
What it holds: P/E 19.02 | P/B 2.14 | P/S 2.65 | 3y earnings growth n/a
Yield: 2.8%
Three-year record: +13.4% a year | beta to the market 0.43
Cost and size: expense ratio 0.08% | net assets 21.84B
What it is made of: Stocks 100.0%, Cash 0.1%
Largest holdings: NextEra Energy Inc 13.0%, Southern Co 7.5%, Duke Energy Corp 7.1%, Constellation Energy Corp 6.7%, American Electric Power Co Inc 5.1%
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

<details><summary><b>What analysts and big funds say</b> — score +0.45</summary>

_Not available today._

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score +0.45</summary>

```text
Rolled up from the 5 largest holdings, 39.4% of the fund by weight
Ratings by weight: buy 80.9% | hold 19.1% | sell 0.0% (mean 2.02 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +25.8% above the current prices
Holdings read: NEE, SO, DUK, CEG, AEP
Recent rating changes among them:
  - NEE: 2026-09-18 Morgan Stanley: main, Overweight -> Overweight
  - SO: 2026-09-25 Citigroup: main, Buy -> Buy
  - DUK: 2026-09-18 Morgan Stanley: main, Equal-Weight -> Equal-Weight
  - CEG: 2026-09-18 Morgan Stanley: main, Overweight -> Overweight
  - AEP: 2026-09-18 Morgan Stanley: main, Overweight -> Overweight
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
Direction: flat (1 week)
Share count change: 1 week: +0.0% (0.00) over 7d
Shares outstanding: 163.27M | fund size: 6.46B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### US health care (XLV) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Neutral overall – no material macro surprise, modest technicals, flat fund flows, and limited analyst coverage.

**Main reasons it gave:**
- Analyst coverage: 44.3% of fund, all buy with +10.7% price target
- Fund flows: flat, share count unchanged over 1 week
- Technicals: price above 20‑day, 50‑day, 200‑day SMAs, RSI 54, MACD positive but modest
- Healthcare sector index down 0.9% on the day
- Macro: yields up (10‑yr +0.15% week), VIX low (15.9), no data surprise

<details><summary><b>News</b> — score +0.00</summary>

- [State Street Health Care Select Sector SPDR ETF (XLV) stock price, news, quote and history](https://au.finance.yahoo.com/quote/XLV/)  
  <sub>Yahoo Finance Australia, 5 hours ago</sub>  
  State Street Health Care Select Sector SPDR ETF (XLV) · 0.49% · -0.25% · 19.17% · 10.29% · 25.63% · 32.47% · 588.08%. Key events. Baseline. Advanced...
- [30-Year Yield Hits 2002 High; Credit-Score Giant FICO Plunges 27%: Stock Market Today](https://www.tradingview.com/news/benzinga:0b9ed21e4094b:0-30-year-yield-hits-2002-high-credit-score-giant-fico-plunges-27-stock-market-today/)  
  <sub>TradingView, 22 hours ago</sub>  
  U.S. stocks were little changed by midday Tuesday, with small caps and the Dow lagging while tech held up, as the 10-year Treasury yield pushed to its...
- [Exchange-Traded Funds, Equity Futures Lower Pre-Bell Wednesday Amid Inflation Data Release](https://finance.yahoo.com/markets/stocks/articles/exchange-traded-funds-equity-futures-132034377.html)  
  <sub>Yahoo Finance, 2 hours ago</sub>  
  The broad market exchange-traded fund SPDR S&P 500 ETF Trust (SPY) was down 0.01% and the actively t.
- [Sector Update: Healthcare Stocks Decline Tuesday Afternoon](https://finance.yahoo.com/healthcare/articles/sector-healthcare-stocks-decline-tuesday-174048492.html)  
  <sub>Yahoo Finance, 21 hours ago</sub>  
  Healthcare stocks retreated Tuesday afternoon, with the NYSE Healthcare Index falling 0.9% and the State Street Health Care Select Sector SPDR ETF (XLV)...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.03% (+0.00 on the week) | 5-year 5.05% (+0.06 on the week) | 10-year 5.27% (+0.15 on the week) | 30-year 5.62% (+0.22 on the week)
Yield curve, 10-year minus 3-month: +1.24 points -- upward sloping (normal)
US dollar index: 101.27 (+0.17 on the week)
Volatility (VIX): 15.90 (+0.7 on the week) -- elevated
Latest US data: inflation 3.4% (2026-08-01) | unemployment 4.1% (2026-08-01) | jobless claims 197k (2026-09-19)
Policy and expectations: Fed target 4.00% | market expects 2.4% inflation over 10 years
Rate path: 2-year Treasury 4.92% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 170.31 (bar of 2026-09-30), from 502 daily bars
Trend: vs 20d SMA 169.17 (+0.7%), 50d 168.34 (+1.2%), 200d 156.60 (+8.8%); 50d above 200d
Momentum: RSI(14) 54.2 | MACD 0.535 vs signal 0.409 (histogram 0.126)
Returns: 1d -0.2% | 5d +0.9% | 1m -0.1% | 3m +6.8%
52-week range: 139.17 - 175.68 (now 85.3% of the way up)
Volatility: ATR(14) 2.35 (1.4% of price) | annualised 20d 13.0%
Volume: 0.64x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.00</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score +0.00</summary>

```text
Fund type: Health
What it holds: P/E 30.47 | P/B 4.77 | P/S 1.66 | 3y earnings growth n/a
Yield: 1.5%
Three-year record: +11.5% a year | beta to the market 0.52
Cost and size: expense ratio 0.08% | net assets 43.91B
What it is made of: Stocks 99.9%, Cash 0.1%
Largest holdings: Eli Lilly and Co 14.9%, Johnson & Johnson 10.4%, AbbVie Inc 7.4%, Merck & Co Inc 5.9%, UnitedHealth Group Inc 5.7%
Sector mix: Healthcare 100.0%
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
Rolled up from the 5 largest holdings, 44.3% of the fund by weight
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 1.72 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +10.7% above the current prices
Holdings read: LLY, JNJ, ABBV, MRK, UNH
Recent rating changes among them:
  - LLY: 2026-09-28 JP Morgan: main, Overweight -> Overweight
  - JNJ: 2026-09-29 JP Morgan: main, Neutral -> Neutral
  - ABBV: 2026-09-10 HSBC: main, Buy -> Buy
  - MRK: 2026-09-29 Scotiabank: main, Sector Outperform -> Sector Outperform
  - UNH: 2026-07-21 JP Morgan: main, Overweight -> Overweight
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
Direction: flat (1 week)
Share count change: 1 week: +0.0% (0.00) over 12d
Shares outstanding: 197.42M | fund size: 33.62B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Taiwan (EWT) · Sector or country — no answer, no confidence given

<details><summary><b>News</b> — score n/a</summary>

_No news found for this one today._

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score n/a</summary>

```text
US Treasury yields: 3-month 4.03% (+0.00 on the week) | 5-year 5.05% (+0.06 on the week) | 10-year 5.27% (+0.15 on the week) | 30-year 5.62% (+0.22 on the week)
Yield curve, 10-year minus 3-month: +1.24 points -- upward sloping (normal)
US dollar index: 101.27 (+0.17 on the week)
Volatility (VIX): 15.90 (+0.7 on the week) -- elevated
Latest US data: inflation 3.4% (2026-08-01) | unemployment 4.1% (2026-08-01) | jobless claims 197k (2026-09-19)
Policy and expectations: Fed target 4.00% | market expects 2.4% inflation over 10 years
Rate path: 2-year Treasury 4.92% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score n/a</summary>

```text
Last close 113.23 (bar of 2026-09-30), from 502 daily bars
Trend: vs 20d SMA 111.60 (+1.5%), 50d 106.24 (+6.6%), 200d 88.24 (+28.3%); 50d above 200d
Momentum: RSI(14) 57.4 | MACD 2.083 vs signal 2.081 (histogram 0.001)
Returns: 1d -0.8% | 5d +0.6% | 1m +4.8% | 3m +7.1%
52-week range: 60.03 - 115.64 (now 95.7% of the way up)
Volatility: ATR(14) 2.13 (1.9% of price) | annualised 20d 26.8%
Volume: 0.31x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score n/a</summary>

```text
Fund type: Greater China Region
What it holds: P/E 27.26 | P/B 4.29 | P/S 2.54 | 3y earnings growth n/a
Yield: 0.9%
Three-year record: +45.9% a year | beta to the market 1.30
Cost and size: expense ratio 0.59% | net assets 11.76B
What it is made of: Stocks 99.6%, Cash 0.4%
Largest holdings: Taiwan Semiconductor Manufacturing Co Ltd 22.1%, MediaTek Inc 6.0%, Delta Electronics Inc 4.0%, Hon Hai Precision Industry Co Ltd 3.3%, ASE Technology Holding Co Ltd 2.6%
Sector mix: Technology 73.9%, Financial services 14.0%, Basic materials 3.8%, Industrials 2.8%
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
Rolled up from the 5 largest holdings, 38.0% of the fund by weight
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 1.35 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +28.3% above the current prices
Holdings read: 2330.TW, 2454.TW, 2308.TW, 2317.TW, 3711.TW
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
Direction: flat (1 week)
Share count change: 1 week: +0.0% (0.00) over 12d
Shares outstanding: 85.00M | fund size: 9.62B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### US regional banks (KRE) · Sector or country — no answer, no confidence given

<details><summary><b>News</b> — score n/a</summary>

_No news found for this one today._

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score n/a</summary>

```text
US Treasury yields: 3-month 4.03% (+0.00 on the week) | 5-year 5.05% (+0.06 on the week) | 10-year 5.27% (+0.15 on the week) | 30-year 5.62% (+0.22 on the week)
Yield curve, 10-year minus 3-month: +1.24 points -- upward sloping (normal)
US dollar index: 101.27 (+0.17 on the week)
Volatility (VIX): 15.90 (+0.7 on the week) -- elevated
Latest US data: inflation 3.4% (2026-08-01) | unemployment 4.1% (2026-08-01) | jobless claims 197k (2026-09-19)
Policy and expectations: Fed target 4.00% | market expects 2.4% inflation over 10 years
Rate path: 2-year Treasury 4.92% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score n/a</summary>

```text
Last close 69.72 (bar of 2026-09-30), from 502 daily bars
Trend: vs 20d SMA 72.62 (-4.0%), 50d 74.55 (-6.5%), 200d 70.56 (-1.2%); 50d above 200d
Momentum: RSI(14) 29.9 | MACD -1.256 vs signal -1.000 (histogram -0.256)
Returns: 1d -0.2% | 5d -0.9% | 1m -5.2% | 3m -8.5%
52-week range: 58.14 - 77.93 (now 58.5% of the way up)
Volatility: ATR(14) 1.17 (1.7% of price) | annualised 20d 16.1%
Volume: 0.35x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score n/a</summary>

```text
Fund type: Financial
What it holds: P/E 12.60 | P/B 1.27 | P/S 3.77 | 3y earnings growth n/a
Yield: 2.2%
Three-year record: +22.8% a year | beta to the market 1.04
Cost and size: expense ratio 0.35% | net assets 4.01B
What it is made of: Stocks 99.9%, Cash 0.1%
Largest holdings: Cullen/Frost Bankers Inc 1.5%, SouthState Bank Corp 1.4%, Popular Inc 1.4%, Pinnacle Financial Partners Inc 1.4%, UMB Financial Corp 1.4%
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
Rolled up from the 5 largest holdings, 7.1% of the fund by weight  -- thin, so read this as a fact about that slice rather than the fund
Ratings by weight: buy 79.5% | hold 20.5% | sell 0.0% (mean 1.79 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +22.4% above the current prices
Holdings read: CFR, SSB, BPOP, PNFP, UMBF
Recent rating changes among them:
  - CFR: 2026-09-28 Morgan Stanley: main, Overweight -> Overweight
  - SSB: 2026-07-28 Citigroup: main, Buy -> Buy
  - BPOP: 2026-09-30 Wells Fargo: main, Overweight -> Overweight
  - PNFP: 2026-09-30 Wells Fargo: up, Equal-Weight -> Overweight
  - UMBF: 2026-09-28 Morgan Stanley: main, Overweight -> Overweight
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
Direction: money coming in (1 week)
Share count change: 1 week: +1.8% (67.84M) over 7d
Shares outstanding: 56.11M | fund size: 3.91B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### US shopping and leisure (XLY) · Sector or country — no answer, no confidence given

<details><summary><b>News</b> — score n/a</summary>

- [PEJ ETF: Worth Avoiding As Pressures From Higher Rates Mount (NYSEARCA:PEJ)](https://seekingalpha.com/article/4950850-pej-worth-avoiding-as-pressures-from-higher-rates-mount-maintain-hold?source=feed_tag_etf_analysis)  
  <sub>Seeking Alpha, 12 hours ago</sub>  
  Hold Invesco Leisure & Entertainment ETF (PEJ): August reconstitution weakened growth/quality. Read here for a detailed investment analysis.
- [Sector Update: Consumer Stocks Retreat in Afternoon Trading](https://finance.yahoo.com/markets/stocks/articles/sector-consumer-stocks-retreat-afternoon-174653676.html)  
  <sub>Yahoo Finance, 21 hours ago</sub>  
  Consumer stocks were lower Tuesday afternoon, with the State Street Consumer Staples Select Sector SPDR ETF (XLP) shedding 0.7% and the State Street...
- [Sector Update: Consumer](https://finance.yahoo.com/markets/stocks/articles/sector-consumer-192328494.html)  
  <sub>Yahoo Finance, 20 hours ago</sub>  
  Consumer stocks were mixed late Tuesday afternoon, with the State Street Consumer Staples Select Sector SPDR ETF (XLP) shedding 0.7% and the State Street...
- [Sector Update: Consumer Stocks Mixed Late Afternoon](https://finance.yahoo.com/markets/stocks/articles/sector-consumer-stocks-mixed-afternoon-194916811.html)  
  <sub>Yahoo Finance, 19 hours ago</sub>  
  Consumer stocks were mixed late Tuesday afternoon, with the State Street Consumer Staples Select Sector SPDR ETF (XLP) shedding 0.6% and the State Street...
- [Exchange-Traded Funds Lower as US Equities Drop After Midday](https://finance.yahoo.com/markets/articles/exchange-traded-funds-lower-us-171654357.html)  
  <sub>Yahoo Finance, 22 hours ago</sub>  
  Broad Market Indicators Broad-market exchange-traded funds IWM and IVV fell. Actively traded Invesco QQQ Trust (QQQ) eased 0.1%.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score n/a</summary>

```text
US Treasury yields: 3-month 4.03% (+0.00 on the week) | 5-year 5.05% (+0.06 on the week) | 10-year 5.27% (+0.15 on the week) | 30-year 5.62% (+0.22 on the week)
Yield curve, 10-year minus 3-month: +1.24 points -- upward sloping (normal)
US dollar index: 101.27 (+0.17 on the week)
Volatility (VIX): 15.90 (+0.7 on the week) -- elevated
Latest US data: inflation 3.4% (2026-08-01) | unemployment 4.1% (2026-08-01) | jobless claims 197k (2026-09-19)
Policy and expectations: Fed target 4.00% | market expects 2.4% inflation over 10 years
Rate path: 2-year Treasury 4.92% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score n/a</summary>

```text
Last close 109.37 (bar of 2026-09-30), from 502 daily bars
Trend: vs 20d SMA 111.88 (-2.2%), 50d 114.48 (-4.5%), 200d 116.50 (-6.1%); 50d below 200d
Momentum: RSI(14) 36.2 | MACD -1.628 vs signal -1.453 (histogram -0.175)
Returns: 1d +0.2% | 5d -1.2% | 1m -6.2% | 3m -7.4%
52-week range: 105.66 - 124.52 (now 19.7% of the way up)
Volatility: ATR(14) 1.51 (1.4% of price) | annualised 20d 14.8%
Volume: 0.25x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score n/a</summary>

```text
Fund type: Consumer Cyclical
What it holds: P/E 25.48 | P/B 5.89 | P/S 2.51 | 3y earnings growth n/a
Yield: 0.8%
Three-year record: +11.7% a year | beta to the market 1.16
Cost and size: expense ratio 0.08% | net assets 22.75B
What it is made of: Stocks 99.9%, Cash 0.1%
Largest holdings: Amazon.com Inc 24.4%, Tesla Inc 17.3%, The Home Depot Inc 5.4%, McDonald's Corp 4.1%, Booking Holdings Inc 3.9%
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
Rolled up from the 5 largest holdings, 55.0% of the fund by weight
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 1.76 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +26.3% above the current prices
Holdings read: AMZN, TSLA, HD, MCD, BKNG
Recent rating changes among them:
  - AMZN: 2026-09-30 Rosenblatt: main, Buy -> Buy
  - TSLA: 2026-09-28 JP Morgan: main, Neutral -> Neutral
  - HD: 2026-09-09 Bernstein: main, Market Perform -> Market Perform
  - MCD: 2026-09-29 JP Morgan: main, Overweight -> Overweight
  - BKNG: 2026-09-24 BTIG: reit, Buy -> Buy
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
Direction: flat (1 week)
Share count change: 1 week: +0.0% (0.00) over 12d
Shares outstanding: 120.25M | fund size: 13.15B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

## Commodities

### Sugar (CANE) · Commodity — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Neutral – no macro surprise, technicals mixed, heavy roll cost penalizes longs, modest outflows and extreme crowding but no decisive catalyst.

**Main reasons it gave:**
- Macro data unchanged: yields up modestly, inflation 3.4% in line with expectations
- Technical indicators mixed: RSI 54.4 (neutral), MACD histogram -0.042 (slightly bearish), low volume (0.34x 20‑day avg)
- Cost of holding heavy at -8.4% annual, penalizing long exposure
- Fund flows negative: share count down 1.5% over 7 days, indicating outflows
- Positioning crowded long (100% percentile) with a small weekly increase (+0.4% OI)

<details><summary><b>News</b> — score +0.00</summary>

_No news found for this one today._

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.03% (+0.00 on the week) | 5-year 5.05% (+0.06 on the week) | 10-year 5.27% (+0.15 on the week) | 30-year 5.62% (+0.22 on the week)
Yield curve, 10-year minus 3-month: +1.24 points -- upward sloping (normal)
US dollar index: 101.27 (+0.17 on the week)
Volatility (VIX): 15.90 (+0.7 on the week) -- elevated
Latest US data: inflation 3.4% (2026-08-01) | unemployment 4.1% (2026-08-01) | jobless claims 197k (2026-09-19)
Policy and expectations: Fed target 4.00% | market expects 2.4% inflation over 10 years
Rate path: 2-year Treasury 4.92% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 11.33 (bar of 2026-09-30), from 502 daily bars
Trend: vs 20d SMA 11.37 (-0.3%), 50d 10.87 (+4.2%), 200d 9.96 (+13.7%); 50d above 200d
Momentum: RSI(14) 54.4 | MACD 0.077 vs signal 0.119 (histogram -0.042)
Returns: 1d -0.3% | 5d -0.4% | 1m +0.1% | 3m +15.0%
52-week range: 9.02 - 11.82 (now 82.5% of the way up)
Volatility: ATR(14) 0.19 (1.7% of price) | annualised 20d 20.2%
Volume: 0.34x the 20-day average
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
Cost of holding this fund instead of sugar itself: -8.4% a year -- heavy: rolling contracts costs this fund real money
Measured: 3 months: fund +15.0%, commodity +24.6%, gap -9.6% | 6 months: fund +8.5%, commodity +20.4%, gap -11.8% | 12 months: fund +8.2%, commodity +16.6%, gap -8.4%
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

<details><summary><b>Buying and selling by company insiders</b> — score +0.20</summary>

_Not available today._

</details>

<details><summary><b>Who is positioned how</b> — score +0.20</summary>

```text
Contract: SUGAR NO. 11 - ICE FUTURES U.S. (positions as of 2026-09-22, published the following Friday)
Large speculators: net long 18.9% of open interest (1,147,767 contracts)
Change on the week: +0.4% of open interest
Crowding: 100% percentile over 52 weeks -- a crowded long by the standards of the past year
Read this as crowding, not as a forecast: an extreme is as often the end of a move as the middle of one.
```

</details>

<details><summary><b>Money going into and out of this fund</b> — score +0.20</summary>

```text
Direction: money going out (1 week)
Share count change: 1 week: -1.5% (-886.31K) over 7d
Shares outstanding: 5.18M | fund size: 58.74M
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Corn (CORN) · Commodity — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:** no explanation. It wrote only “NEUTRAL”, so the main reasons below are all it gave.

**Main reasons it gave:**
- Positioning: net long 21.8% of OI, crowding at 95th percentile, weekly change -0.7% (slight reduction)
- Cost of holding: -13% annual roll cost, heavy tailwind for short but not a directional signal
- Crop condition: 57% good/excellent, down 9 points YoY, trend flat over 3 weeks
- Macro: no rate or data surprise; yields modestly up, VIX low, no policy shift

<details><summary><b>News</b> — score +0.00</summary>

- [Inglis vs Sonmez | Prediction Markets](https://www.coinbase.com/en-it/predictions/event/KXWTAMATCH-26SEP29INGSON)  
  <sub>Coinbase, 8 hours ago</sub>  
  Make your prediction on Inglis vs Sonmez. Trade on the future with Coinbase Predictions.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.03% (+0.00 on the week) | 5-year 5.05% (+0.06 on the week) | 10-year 5.27% (+0.15 on the week) | 30-year 5.62% (+0.22 on the week)
Yield curve, 10-year minus 3-month: +1.24 points -- upward sloping (normal)
US dollar index: 101.27 (+0.17 on the week)
Volatility (VIX): 15.90 (+0.7 on the week) -- elevated
Latest US data: inflation 3.4% (2026-08-01) | unemployment 4.1% (2026-08-01) | jobless claims 197k (2026-09-19)
Policy and expectations: Fed target 4.00% | market expects 2.4% inflation over 10 years
Rate path: 2-year Treasury 4.92% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 19.55 (bar of 2026-09-30), from 502 daily bars
Trend: vs 20d SMA 19.89 (-1.7%), 50d 19.05 (+2.6%), 200d 18.13 (+7.8%); 50d above 200d
Momentum: RSI(14) 49.1 | MACD 0.120 vs signal 0.244 (histogram -0.124)
Returns: 1d +0.3% | 5d -1.1% | 1m -2.5% | 3m +15.3%
52-week range: 16.47 - 20.29 (now 80.6% of the way up)
Volatility: ATR(14) 0.29 (1.5% of price) | annualised 20d 14.5%
Volume: 0.10x the 20-day average
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
Cost of holding this fund instead of corn itself: -13.0% a year -- heavy: rolling contracts costs this fund real money
Measured: 3 months: fund +15.3%, commodity +24.0%, gap -8.7% | 6 months: fund +6.2%, commodity +14.1%, gap -7.8% | 12 months: fund +10.9%, commodity +23.9%, gap -13.0%
A commodity fund holds futures, not corn, and must sell each expiring contract to buy the next one. Where the next month costs more, that roll loses money every month. This gap is what the structure has actually cost, fees included -- it is history rather than a forecast, and it is not a direction: heavy carry is a reason to want a larger move to justify a long, and a tailwind for a short.
```

</details>

<details><summary><b>How much oil and gas is in storage</b> — score -0.10</summary>

_Not available today._

</details>

<details><summary><b>How the crop is growing</b> — score -0.10</summary>

```text
Corn rated good or excellent: 57% of the US crop (week 39 of 2026)
Direction over 3 weeks: steady, 0 points
Same week last year: 66% (-9 points)
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
Contract: CORN - CHICAGO BOARD OF TRADE (positions as of 2026-09-22, published the following Friday)
Large speculators: net long 21.8% of open interest (1,854,505 contracts)
Change on the week: -0.7% of open interest
Crowding: 95% percentile over 52 weeks -- a crowded long by the standards of the past year
Read this as crowding, not as a forecast: an extreme is as often the end of a move as the middle of one.
```

</details>

<details><summary><b>Money going into and out of this fund</b> — score -0.25</summary>

```text
Direction: flat (1 week)
Share count change: 1 week: -0.2% (-379.54K) over 7d
Shares outstanding: 8.36M | fund size: 163.36M
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Copper (CPER) · Commodity — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:** no explanation. It wrote only “NEUTRAL”, so the main reasons below are all it gave.

**Main reasons it gave:**
- Positioning: net long 27.4% of OI, up 4.9% week‑over‑week (small bullish bias)
- Fund flows: share count down 1.2% over 7 days (bearish bias)
- Cost of holding: -5.4% annual roll cost (heavy carry, tailwind for short)
- Macro: yields up across curve and dollar stronger, no surprise data (bearish for commodities)

<details><summary><b>News</b> — score +0.00</summary>

- [United States Commodity Index Funds Trust posts August net income of $34.93M; USCI NAV per share $106.42, CPER NAV per share $40.02](https://www.tradingview.com/news/tradingview:1ef08c1a542ab:0-united-states-commodity-index-funds-trust-posts-august-net-income-of-34-93m-usci-nav-per-share-106-42-cper-nav-per-share-40-02/)  
  <sub>TradingView, 23 hours ago</sub>  
  United States Commodity Index Funds Trust reported combined net income of $34926870 for August 2026 and series-level results including USCI NAV per share...
- [Simplify Raises the Stakes With Rival Bid for USCF](https://etfdb.com/alternatives-content-hub/simplify-ups-the-stakes-with-rival-bid-for-uscf/)  
  <sub>ETF Database, 16 hours ago</sub>  
  Simplify has now offered a competing bid for Marygold and USCF Investments, after Madison Dearborn announced a deal was struck last week.
- [United States Commodity Index Funds Trust releases monthly statements for USCI and CPER](https://www.investing.com/news/sec-filings/united-states-commodity-index-funds-trust-releases-monthly-statements-for-usci-and-cper-93CH-4923216)  
  <sub>Investing.com, 22 hours ago</sub>  
  United States Commodity Index Funds Trust (NYSE Arca:USCI, NYSE Arca:CPER) released monthly account statements for its United States Commodity Index Fund...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.03% (+0.00 on the week) | 5-year 5.05% (+0.06 on the week) | 10-year 5.27% (+0.15 on the week) | 30-year 5.62% (+0.22 on the week)
Yield curve, 10-year minus 3-month: +1.24 points -- upward sloping (normal)
US dollar index: 101.27 (+0.17 on the week)
Volatility (VIX): 15.90 (+0.7 on the week) -- elevated
Latest US data: inflation 3.4% (2026-08-01) | unemployment 4.1% (2026-08-01) | jobless claims 197k (2026-09-19)
Policy and expectations: Fed target 4.00% | market expects 2.4% inflation over 10 years
Rate path: 2-year Treasury 4.92% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 39.69 (bar of 2026-09-30), from 502 daily bars
Trend: vs 20d SMA 39.90 (-0.5%), 50d 39.75 (-0.1%), 200d 37.38 (+6.2%); 50d above 200d
Momentum: RSI(14) 48.4 | MACD 0.133 vs signal 0.156 (histogram -0.023)
Returns: 1d -0.6% | 5d -2.3% | 1m -0.8% | 3m +6.7%
52-week range: 30.00 - 41.43 (now 84.8% of the way up)
Volatility: ATR(14) 0.69 (1.7% of price) | annualised 20d 28.5%
Volume: 0.48x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score -0.35</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score -0.35</summary>

_Not available today._

</details>

<details><summary><b>Does this company beat its own forecasts</b> — score -0.35</summary>

_Not available today._

</details>

<details><summary><b>What holding this fund costs you</b> — score -0.35</summary>

```text
Cost of holding this fund instead of copper itself: -5.4% a year -- heavy: rolling contracts costs this fund real money
Measured: 3 months: fund +6.7%, commodity +7.9%, gap -1.2% | 6 months: fund +15.3%, commodity +18.2%, gap -2.9% | 12 months: fund +31.0%, commodity +36.4%, gap -5.4%
A commodity fund holds futures, not copper, and must sell each expiring contract to buy the next one. Where the next month costs more, that roll loses money every month. This gap is what the structure has actually cost, fees included -- it is history rather than a forecast, and it is not a direction: heavy carry is a reason to want a larger move to justify a long, and a tailwind for a short.
```

</details>

<details><summary><b>How much oil and gas is in storage</b> — score -0.35</summary>

_Not available today._

</details>

<details><summary><b>How the crop is growing</b> — score -0.35</summary>

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
Contract: COPPER- #1 - COMMODITY EXCHANGE INC. (positions as of 2026-09-22, published the following Friday)
Large speculators: net long 27.4% of open interest (301,657 contracts)
Change on the week: +4.9% of open interest
Crowding: 88% percentile over 52 weeks -- within its normal range
Read this as crowding, not as a forecast: an extreme is as often the end of a move as the middle of one.
```

</details>

<details><summary><b>Money going into and out of this fund</b> — score +0.10</summary>

```text
Direction: money going out (1 week)
Share count change: 1 week: -1.2% (-8.69M) over 7d
Shares outstanding: 18.49M | fund size: 733.79M
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Silver (SLV) · Commodity — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:** no explanation. It wrote only “NEUTRAL”, so the main reasons below are all it gave.

**Main reasons it gave:**
- Price below 20d, 50d, and 200d SMAs indicating bearish trend
- Rising Treasury yields (10y +0.15%) and stronger dollar (U.S. Dollar Index +0.17) increase opportunity cost for silver
- Cost of holding fund is -1.7% annual drag, a bearish factor for long positions
- Positioning shows net long 12.5% of OI with -0.2% weekly change, indicating no strong bullish crowding

<details><summary><b>News</b> — score +0.00</summary>

- [Silver Has Now Lost Nearly Half Its Value. Here’s What Broke the Metals Trade](https://247wallst.com/investing/2026/09/30/silver-has-now-lost-nearly-half-its-value-heres-what-broke-the-metals-trade/)  
  <sub>24/7 Wall St., 4 hours ago</sub>  
  Silver just recorded one of its worst stretches in decades, and the forces behind the selloff are still building pressure. Understanding what broke the...
- [SLVM ETF Holdings List — HAN:SLVM](https://www.tradingview.com/symbols/HAN-SLVM/holdings/)  
  <sub>TradingView, 7 hours ago</sub>  
  Explore HANetf ICAV - Sprott Silver Miners and Physical Silver UCITS ETF AccumUSD holdings with weight, market value, and other helpful data to make more...
- [Silver Miners (SIL) looking for a double correction](https://www.fxstreet.com/news/silver-miners-sil-looking-for-a-double-correction-202609301355)  
  <sub>FXStreet, 1 hour ago</sub>  
  Launched in 2010, the Global X Silver Miners ETF (SIL) provides investors with diversified exposure to leading silver mining companies worldwide.
- [Current price of silver as of Tuesday, Sept. 29, 2026](http://fortune.com/article/current-price-of-silver-9-29-2026/)  
  <sub>Fortune, 20 hours ago</sub>  
  If you're worried about increased inflation, adding precious metals like silver to your portfolio can be a smart choice.
- [Silver Price Today In The UK, 30 September 2026](https://www.forbes.com/advisor/uk/investing/silver-price/)  
  <sub>Forbes, 6 hours ago</sub>  
  The price of silver today, as of 9:10 a.m. GMT, is £46.24 per ounce.
- [3 Inflation-Proof Investments That Could Be Fantastic Buys in 2026](https://www.fool.com/investing/2026/09/29/x-inflation-proof-investments-that-could-be-fantas/)  
  <sub>The Motley Fool, 20 hours ago</sub>  
  Gold, silver, and Bitcoin could shield your portfolio from the inflationary headwinds.
- [Silver Elephant Mining Corp. (ELEF.TO) Stock Price, News, Quote & History](https://ca.finance.yahoo.com/quote/ELEF.TO/)  
  <sub>Yahoo! Finance Canada, 5 hours ago</sub>  
  Find the latest Silver Elephant Mining Corp. (ELEF.TO) stock quote, history, news and other vital information to help you with your stock trading and...
- [Planning to invest in equity mutual funds for 3 years? Check these 7 funds with over 40% gains](https://m.economictimes.com/mf/analysis/planning-to-invest-in-equity-mutual-funds-for-3-years-check-these-7-funds-with-over-40-gains/three-other-silver-etf-fofs/slideshow/134593124.cms)  
  <sub>The Economic Times, 3 hours ago</sub>  
  ICICI Prudential Silver ETF FoF, HDFC Silver ETF FoF, and Aditya Birla Sun Life ETF FoF delivered a CAGR of 43.13%, 43.04%, and 43% respectively in the last...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.03% (+0.00 on the week) | 5-year 5.05% (+0.06 on the week) | 10-year 5.27% (+0.15 on the week) | 30-year 5.62% (+0.22 on the week)
Yield curve, 10-year minus 3-month: +1.24 points -- upward sloping (normal)
US dollar index: 101.27 (+0.17 on the week)
Volatility (VIX): 15.90 (+0.7 on the week) -- elevated
Latest US data: inflation 3.4% (2026-08-01) | unemployment 4.1% (2026-08-01) | jobless claims 197k (2026-09-19)
Policy and expectations: Fed target 4.00% | market expects 2.4% inflation over 10 years
Rate path: 2-year Treasury 4.92% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score -0.30</summary>

```text
Last close 54.58 (bar of 2026-09-30), from 502 daily bars
Trend: vs 20d SMA 58.24 (-6.3%), 50d 57.67 (-5.4%), 200d 65.94 (-17.2%); 50d below 200d
Momentum: RSI(14) 39.2 | MACD -0.708 vs signal -0.166 (histogram -0.542)
Returns: 1d -1.6% | 5d -6.2% | 1m -9.2% | 3m +1.9%
52-week range: 42.37 - 105.60 (now 19.3% of the way up)
Volatility: ATR(14) 1.75 (3.2% of price) | annualised 20d 40.4%
Volume: 0.52x the 20-day average
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
Cost of holding this fund instead of silver itself: -1.7% a year -- a steady drag
Measured: 3 months: fund +1.9%, commodity +1.0%, gap +0.9% | 6 months: fund -19.9%, commodity -18.8%, gap -1.1% | 12 months: fund +28.4%, commodity +30.1%, gap -1.7%
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

<details><summary><b>Buying and selling by company insiders</b> — score -0.10</summary>

_Not available today._

</details>

<details><summary><b>Who is positioned how</b> — score -0.10</summary>

```text
Contract: SILVER - COMMODITY EXCHANGE INC. (positions as of 2026-09-22, published the following Friday)
Large speculators: net long 12.5% of open interest (106,474 contracts)
Change on the week: -0.2% of open interest
Crowding: 60% percentile over 52 weeks -- within its normal range
Read this as crowding, not as a forecast: an extreme is as often the end of a move as the middle of one.
```

</details>

<details><summary><b>Money going into and out of this fund</b> — score -0.10</summary>

```text
Direction: flat (1 week)
Share count change: 1 week: +0.0% (0.00) over 12d
Shares outstanding: 341.45M | fund size: 18.63B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Soybeans (SOYB) · Commodity — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> No macro surprise, technicals show no decisive break, positioning is crowded long with modest weekly increase, fund flows show outflows, cost of holding drags long positions.

**Main reasons it gave:**
- US inflation 3.4% and unemployment 4.1% in line with expectations (no macro surprise)
- Price 27.73 just below 20‑day SMA (27.80) and MACD histogram negative, no decisive technical break
- CFTC large speculators net long 23.8% of open interest, 97th percentile crowding, +1.9% weekly change
- Fund flows show outflows: share count down -0.9% (‑411.2K) over 7 days
- Cost of holding fund vs soybeans -1.2% per year, a drag on long positions

<details><summary><b>News</b> — score +0.00</summary>

_No news found for this one today._

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.03% (+0.00 on the week) | 5-year 5.05% (+0.06 on the week) | 10-year 5.27% (+0.15 on the week) | 30-year 5.62% (+0.22 on the week)
Yield curve, 10-year minus 3-month: +1.24 points -- upward sloping (normal)
US dollar index: 101.27 (+0.17 on the week)
Volatility (VIX): 15.90 (+0.7 on the week) -- elevated
Latest US data: inflation 3.4% (2026-08-01) | unemployment 4.1% (2026-08-01) | jobless claims 197k (2026-09-19)
Policy and expectations: Fed target 4.00% | market expects 2.4% inflation over 10 years
Rate path: 2-year Treasury 4.92% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 27.73 (bar of 2026-09-30), from 502 daily bars
Trend: vs 20d SMA 27.80 (-0.2%), 50d 26.61 (+4.2%), 200d 24.58 (+12.8%); 50d above 200d
Momentum: RSI(14) 56.1 | MACD 0.296 vs signal 0.415 (histogram -0.119)
Returns: 1d +0.5% | 5d -0.9% | 1m +1.8% | 3m +13.1%
52-week range: 21.46 - 28.14 (now 93.9% of the way up)
Volatility: ATR(14) 0.34 (1.2% of price) | annualised 20d 15.6%
Volume: 0.15x the 20-day average
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
Cost of holding this fund instead of soybeans itself: -1.2% a year -- a steady drag
Measured: 3 months: fund +13.1%, commodity +15.8%, gap -2.7% | 6 months: fund +13.7%, commodity +11.4%, gap +2.2% | 12 months: fund +27.9%, commodity +29.1%, gap -1.2%
A commodity fund holds futures, not soybeans, and must sell each expiring contract to buy the next one. Where the next month costs more, that roll loses money every month. This gap is what the structure has actually cost, fees included -- it is history rather than a forecast, and it is not a direction: heavy carry is a reason to want a larger move to justify a long, and a tailwind for a short.
```

</details>

<details><summary><b>How much oil and gas is in storage</b> — score +0.00</summary>

_Not available today._

</details>

<details><summary><b>How the crop is growing</b> — score +0.00</summary>

```text
Soybeans rated good or excellent: 58% of the US crop (week 39 of 2026)
Direction over 3 weeks: steady, 0 points
Same week last year: 62% (-4 points)
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
Contract: SOYBEANS - CHICAGO BOARD OF TRADE (positions as of 2026-09-22, published the following Friday)
Large speculators: net long 23.8% of open interest (1,114,328 contracts)
Change on the week: +1.9% of open interest
Crowding: 97% percentile over 52 weeks -- a crowded long by the standards of the past year
Read this as crowding, not as a forecast: an extreme is as often the end of a move as the middle of one.
```

</details>

<details><summary><b>Money going into and out of this fund</b> — score -0.20</summary>

```text
Direction: money going out (1 week)
Share count change: 1 week: -0.9% (-411.20K) over 7d
Shares outstanding: 1.66M | fund size: 46.06M
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

**Data that was missing** (counted as 0.00, never guessed):
- news unavailable: Bright Data returned an empty body with its 200; nothing to parse

### Natural gas (UNG) · Commodity — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:** no explanation. It wrote only “NEUTRAL”, so the main reasons below are all it gave.

**Main reasons it gave:**
- CFTC large speculators net short 3.6% of OI, increased by 1.9% week-over-week
- US natural gas inventories built 53 BCF, 73% percentile, bearish
- Cost of holding fund heavy at -11.4% annual, tailwind for short
- EIA price outlook expects Henry Hub to rise to $3.51 in 3 months, bullish

<details><summary><b>News</b> — score +0.00</summary>

- [Natural Gas Moves Toward its Peak Season with LNG Demand Rising](https://www.barchart.com/story/news/4863449/natural-gas-moves-toward-its-peak-season-with-lng-demand-rising)  
  <sub>Barchart.com, 20 hours ago</sub>  
  The natural gas injection season will end in mid-to-late November, and U.S. inventories will begin to decline as heating demand increases.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.03% (+0.00 on the week) | 5-year 5.05% (+0.06 on the week) | 10-year 5.27% (+0.15 on the week) | 30-year 5.62% (+0.22 on the week)
Yield curve, 10-year minus 3-month: +1.24 points -- upward sloping (normal)
US dollar index: 101.27 (+0.17 on the week)
Volatility (VIX): 15.90 (+0.7 on the week) -- elevated
Latest US data: inflation 3.4% (2026-08-01) | unemployment 4.1% (2026-08-01) | jobless claims 197k (2026-09-19)
Policy and expectations: Fed target 4.00% | market expects 2.4% inflation over 10 years
Rate path: 2-year Treasury 4.92% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 10.37 (bar of 2026-09-30), from 502 daily bars
Trend: vs 20d SMA 10.54 (-1.6%), 50d 10.29 (+0.8%), 200d 11.38 (-8.9%); 50d below 200d
Momentum: RSI(14) 47.3 | MACD 0.102 vs signal 0.111 (histogram -0.009)
Returns: 1d +0.2% | 5d -4.6% | 1m -1.6% | 3m -10.0%
52-week range: 9.63 - 16.90 (now 10.2% of the way up)
Volatility: ATR(14) 0.36 (3.5% of price) | annualised 20d 44.3%
Volume: 0.27x the 20-day average
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
Cost of holding this fund instead of natural gas itself: -11.4% a year -- heavy: rolling contracts costs this fund real money
Measured: 3 months: fund -10.0%, commodity -6.3%, gap -3.6% | 6 months: fund -11.6%, commodity +4.6%, gap -16.2% | 12 months: fund -19.1%, commodity -7.7%, gap -11.4%
A commodity fund holds futures, not natural gas, and must sell each expiring contract to buy the next one. Where the next month costs more, that roll loses money every month. This gap is what the structure has actually cost, fees included -- it is history rather than a forecast, and it is not a direction: heavy carry is a reason to want a larger move to justify a long, and a tailwind for a short.
```

</details>

<details><summary><b>How much oil and gas is in storage</b> — score -0.20</summary>

```text
US inventories, week ending 2026-09-18 (published the following Wednesday)
  Natural gas: 3,351.0 billion cubic feet, +53.0 on the week (a build), 73% percentile over 52 weeks
A build is more supply than demand and a draw is the reverse, so a build reads bearish and a draw bullish -- as a rule of thumb, not a law. Weigh the change and how unusual the level is above the level itself, and remember the market has already seen this number.
```

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
Contract: NAT GAS NYME - NEW YORK MERCANTILE EXCHANGE (positions as of 2026-09-22, published the following Friday)
Large speculators: net short 3.6% of open interest (1,837,146 contracts)
Change on the week: +1.9% of open interest
Crowding: 67% percentile over 52 weeks -- within its normal range
Read this as crowding, not as a forecast: an extreme is as often the end of a move as the middle of one.
```

</details>

<details><summary><b>Money going into and out of this fund</b> — score -0.20</summary>

```text
Direction: flat (1 week)
Share count change: 1 week: +0.0% (0.00) over 12d
Shares outstanding: 12.08M | fund size: 125.32M
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Oil (USO) · Commodity — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:** no explanation. It wrote only “NEUTRAL”, so the main reasons below are all it gave.

**Main reasons it gave:**
- EIA inventory report shows a 3.0M barrel crude build (bearish)
- EIA price outlook projects WTI falling to $84.5 in 3 months (bearish)
- CFTC positioning shows net long 5.5% with only +0.1% weekly change (neutral)
- Technical indicators show price above 200‑day SMA but RSI near 52 (neutral)

<details><summary><b>News</b> — score +0.00</summary>

- [Crude inventory rises by 0.9M barrels for the week ended September 25 – EIA](https://www.tradingview.com/news/seekingalpha:5dbfb91fa094b:0-crude-inventory-rises-by-0-9m-barrels-for-the-week-ended-september-25-eia/)  
  <sub>TradingView, 49 minutes ago</sub>  
  Content provided by Seeking Alpha is intended for information purposes only, and that Seeking Alpha does not offer any personalist investment advice and is...
- [States move to rein in fuel prices, from easing rules to tax relief](https://seekingalpha.com/news/4648340-states-move-to-rein-in-fuel-prices)  
  <sub>Seeking Alpha, 5 hours ago</sub>  
  State governments are moving to curb surging fuel prices, from easing regulations for dyed diesel to temporary tax relief, even as the White House is...
- [Trump Offers 40M Barrels From US Oil Reserve — But Buyers Aren’t Biting: Global Refining Capacity Is The](https://www.benzinga.com/markets/commodities/26/09/62071265/trump-offers-40m-barrels-from-us-oil-reserve-but-buyers-arent-biting-global-refining-capacity-is-the-problem-says-top-oil-analyst)  
  <sub>Benzinga, 7 hours ago</sub>  
  Trump's DOE offers 40M oil barrels, but weak buyer interest highlights global refining bottlenecks, this analyst says.
- [VLO Stock Heads For Best Year Since 1982 — Michael Burry Says It Has Become A ‘Huge Position’](https://stocktwits.com/news-articles/markets/equity/vlo-stock-best-year-1982-michael-burry-huge-position/cZtlx8lRBR0)  
  <sub>Stocktwits, 15 hours ago</sub>  
  Burry recovered his initial investment “and then some” for charity, while retaining a sizable stake that is “deep into house's money.”
- [U.S. to release 40M more barrels from oil reserve as fuel prices surge (USO:NYSEARCA)](https://seekingalpha.com/news/4648168-u-s-to-release-40m-more-barrels-from-oil-reserve-as-fuel-prices-surge)  
  <sub>Seeking Alpha, 22 hours ago</sub>  
  U.S. to release up to 40M SPR barrels to curb gasoline prices amid Iran conflict, urging Europe to meet IEA pledges.
- [Anthropic Warns Of Existential Risk And OpenAI Scraps New Model—Yet AI Stocks See Buying](https://www.benzinga.com/Opinion/26/09/62057861/anthropic-warns-of-existential-risk-and-openai-scraps-new-model-yet-ai-stocks-see-buying)  
  <sub>Benzinga, 23 hours ago</sub>  
  AI Existential Risk Please click here for an enlarged chart of Direxion Daily Semiconductor Bull 3X ETF (NYSE:SOXL). Note the following: Semiconductors...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.03% (+0.00 on the week) | 5-year 5.05% (+0.06 on the week) | 10-year 5.27% (+0.15 on the week) | 30-year 5.62% (+0.22 on the week)
Yield curve, 10-year minus 3-month: +1.24 points -- upward sloping (normal)
US dollar index: 101.27 (+0.17 on the week)
Volatility (VIX): 15.90 (+0.7 on the week) -- elevated
Latest US data: inflation 3.4% (2026-08-01) | unemployment 4.1% (2026-08-01) | jobless claims 197k (2026-09-19)
Policy and expectations: Fed target 4.00% | market expects 2.4% inflation over 10 years
Rate path: 2-year Treasury 4.92% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 147.41 (bar of 2026-09-30), from 502 daily bars
Trend: vs 20d SMA 150.08 (-1.8%), 50d 136.88 (+7.7%), 200d 114.38 (+28.9%); 50d above 200d
Momentum: RSI(14) 52.4 | MACD 3.248 vs signal 4.871 (histogram -1.624)
Returns: 1d +2.8% | 5d -1.0% | 1m +10.3% | 3m +42.7%
52-week range: 66.17 - 161.86 (now 84.9% of the way up)
Volatility: ATR(14) 5.41 (3.7% of price) | annualised 20d 45.4%
Volume: 0.31x the 20-day average
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

_Not available today._

</details>

<details><summary><b>How much oil and gas is in storage</b> — score -0.40</summary>

```text
US inventories, week ending 2026-09-18 (published the following Wednesday)
  Crude oil: 426.4 million barrels, +3.0 on the week (a build), 58% percentile over 52 weeks
  Petrol: 206.0 million barrels, -1.7 on the week (a draw), 8% percentile over 52 weeks -- low for the time of year
  Diesel: 107.4 million barrels, -0.4 on the week (a draw), 33% percentile over 52 weeks
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

```text
Contract: WTI-PHYSICAL - NEW YORK MERCANTILE EXCHANGE (positions as of 2026-09-22, published the following Friday)
Large speculators: net long 5.5% of open interest (1,841,811 contracts)
Change on the week: +0.1% of open interest
Crowding: 98% percentile over 52 weeks -- a crowded long by the standards of the past year
Read this as crowding, not as a forecast: an extreme is as often the end of a move as the middle of one.
```

</details>

<details><summary><b>Money going into and out of this fund</b> — score +0.00</summary>

```text
Direction: flat (1 week)
Share count change: 1 week: +0.0% (0.00) over 12d
Shares outstanding: 119.10M | fund size: 17.56B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Wheat (WEAT) · Commodity — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:** no explanation. It wrote only “NEUTRAL”, so the main reasons below are all it gave.

**Main reasons it gave:**
- No macro data surprise this week (inflation 3.4% and unemployment 4.1% in line with expectations)
- Positioning shows net short 2.5% of OI decreasing by 1.7% (reduction in bearishness)
- Fund flows positive: share count +1.6% over 7 days
- Cost of holding -13.3% annual drag on long positions

<details><summary><b>News</b> — score +0.00</summary>

_No news found for this one today._

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.03% (+0.00 on the week) | 5-year 5.05% (+0.06 on the week) | 10-year 5.27% (+0.15 on the week) | 30-year 5.62% (+0.22 on the week)
Yield curve, 10-year minus 3-month: +1.24 points -- upward sloping (normal)
US dollar index: 101.27 (+0.17 on the week)
Volatility (VIX): 15.90 (+0.7 on the week) -- elevated
Latest US data: inflation 3.4% (2026-08-01) | unemployment 4.1% (2026-08-01) | jobless claims 197k (2026-09-19)
Policy and expectations: Fed target 4.00% | market expects 2.4% inflation over 10 years
Rate path: 2-year Treasury 4.92% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 25.01 (bar of 2026-09-30), from 502 daily bars
Trend: vs 20d SMA 26.14 (-4.4%), 50d 25.56 (-2.2%), 200d 23.14 (+8.1%); 50d above 200d
Momentum: RSI(14) 39.8 | MACD -0.182 vs signal 0.046 (histogram -0.228)
Returns: 1d -0.2% | 5d -2.6% | 1m -10.1% | 3m +11.6%
52-week range: 19.88 - 28.00 (now 63.1% of the way up)
Volatility: ATR(14) 0.54 (2.1% of price) | annualised 20d 22.2%
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
Cost of holding this fund instead of wheat itself: -13.3% a year -- heavy: rolling contracts costs this fund real money
Measured: 3 months: fund +11.6%, commodity +16.4%, gap -4.8% | 6 months: fund +6.1%, commodity +11.8%, gap -5.7% | 12 months: fund +19.4%, commodity +32.6%, gap -13.3%
A commodity fund holds futures, not wheat, and must sell each expiring contract to buy the next one. Where the next month costs more, that roll loses money every month. This gap is what the structure has actually cost, fees included -- it is history rather than a forecast, and it is not a direction: heavy carry is a reason to want a larger move to justify a long, and a tailwind for a short.
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

<details><summary><b>Buying and selling by company insiders</b> — score +0.30</summary>

_Not available today._

</details>

<details><summary><b>Who is positioned how</b> — score +0.30</summary>

```text
Contract: WHEAT-SRW - CHICAGO BOARD OF TRADE (positions as of 2026-09-22, published the following Friday)
Large speculators: net short 2.5% of open interest (483,279 contracts)
Change on the week: -1.7% of open interest
Crowding: 78% percentile over 52 weeks -- within its normal range
Read this as crowding, not as a forecast: an extreme is as often the end of a move as the middle of one.
```

</details>

<details><summary><b>Money going into and out of this fund</b> — score +0.30</summary>

```text
Direction: money coming in (1 week)
Share count change: 1 week: +1.6% (5.62M) over 7d
Shares outstanding: 14.23M | fund size: 355.81M
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Gold (GLD) · Commodity — no answer, no confidence given

<details><summary><b>News</b> — score n/a</summary>

- [Gold Just Had Its Worst Day in Over Two Months. GLD Is Now 26% Off Its High](https://finance.yahoo.com/markets/commodities/articles/gold-just-had-worst-day-111554021.html)  
  <sub>Yahoo Finance, 4 hours ago</sub>  
  GLD dropped nearly 4% to sit 26% below its 52-week high; IAU tracks the same bullion at a 0.25% annual fee versus GLD's 0.40%.
- [Gold ETF GLD drops nearly 4%, hitting lowest in 2 months amid rising rates and oil price fears.](https://pluang.com/en/news-feed/emas-alami-penurunan-terburuk-dalam-2-bulan-gld-turun-26-persen)  
  <sub>Pluang, 4 hours ago</sub>  
  Gold experienced its largest single-day drop in over two months, with the SPDR Gold Trust (GLD) falling 3.94% and gold prices down 3.54%.
- [Equity ETF flows slide as summer unwind takes hold](https://seekingalpha.com/news/4648503-equity-etf-flows-slide-as-summer-unwind-takes-hold)  
  <sub>Seeking Alpha, 2 hours ago</sub>  
  Equity ETF inflows have cooled from their mid-year peak, according to Baird Strategas. Average daily flows into equity exchange traded funds stood at $3.3...
- [Global X Gold Explorers ETF (GOEX) Stock Price | Quotes & News](https://www.moomoo.com/stock/GOEX-US?chain_id=Name1K9-3FXPhg.1lbo660&global_content=%7B%22promote_id%22%3A13764%2C%22sub_promote_id%22%3A57%2C%22f%22%3A%22www.moomoo.com%2Fstock%2FWPM-US%22%7D)  
  <sub>Moomoo, 19 hours ago</sub>  
  $XAU/USD (XAUUSD.CFD)$ $SPDR Gold ETF (GLD.US)$ $Abrdn Gold ETF Trust (SGOL.US)$ $VanEck Gold Miners Equity ETF (GDX.US)$ $VanEck Junior Gold Miners ETF...
- [Silver Has Now Lost Nearly Half Its Value. Here’s What Broke the Metals Trade](https://247wallst.com/investing/2026/09/30/silver-has-now-lost-nearly-half-its-value-heres-what-broke-the-metals-trade/)  
  <sub>24/7 Wall St., 4 hours ago</sub>  
  Silver just recorded one of its worst stretches in decades, and the forces behind the selloff are still building pressure. Understanding what broke the...
- [GLD Sells Your Gold Every Month to Pay Itself, and the IRS Can Tax Those Sales at Up to 28%](https://finance.yahoo.com/markets/commodities/articles/gld-sells-gold-every-month-200137375.html)  
  <sub>Yahoo Finance, 19 hours ago</sub>  
  Every month you hold GLD, the trust quietly sells a piece of your gold to cover its own expenses, and the IRS considers you the seller.
- [Gold’s New Normal: State Street’s Aakash Doshi on Why GLD® Might Fit in Any Client Portfolio](https://www.thewealthadvisor.com/article/golds-new-normal-state-streets-aakash-doshi-why-gldr-might-fit-any-client-portfolio)  
  <sub>The Wealth Advisor, 23 hours ago</sub>  
  Content sponsored by State Street Investment Management. Gold returned 65% in 2025, in nominal terms, marking its strongest single year since 1979.
- [GLD ETF sells gold monthly to cover fees, trigg...](https://pluang.com/en/news-feed/gld-menjual-emas-setiap-bulan-untuk-membayar-biaya-dan-irs-dapat-mengenakan)  
  <sub>Pluang, 19 hours ago</sub>  
  The SPDR Gold Trust (GLD) ETF sells a small portion of its gold holdings every month to pay its 0.40% annual expenses, as it holds no cash or income.
- [The Inverse Correlation Between Gold And Interest Rates Is Breaking Down (NYSEARCA:GLD)](https://seekingalpha.com/article/4950785-inverse-correlation-between-gold-and-interest-rates-is-breaking-down)  
  <sub>Seeking Alpha, 20 hours ago</sub>  
  GLD remains a Buy as central bank gold buying (led by China) supports prices despite rising yields. Here's what investors need to consider.
- [There’s Nothing ‘Precious’ About the Charts of Gold and Silver Prices Here](https://www.inkl.com/news/theres-nothing-precious-about-the-charts-of-gold-and-silver-prices-here)  
  <sub>inkl, 20 hours ago</sub>  
  Gold has one of the worst charts I am seeing in the market right now.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score n/a</summary>

```text
US Treasury yields: 3-month 4.03% (+0.00 on the week) | 5-year 5.05% (+0.06 on the week) | 10-year 5.27% (+0.15 on the week) | 30-year 5.62% (+0.22 on the week)
Yield curve, 10-year minus 3-month: +1.24 points -- upward sloping (normal)
US dollar index: 101.27 (+0.17 on the week)
Volatility (VIX): 15.90 (+0.7 on the week) -- elevated
Latest US data: inflation 3.4% (2026-08-01) | unemployment 4.1% (2026-08-01) | jobless claims 197k (2026-09-19)
Policy and expectations: Fed target 4.00% | market expects 2.4% inflation over 10 years
Rate path: 2-year Treasury 4.92% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score n/a</summary>

```text
Last close 381.64 (bar of 2026-09-30), from 502 daily bars
Trend: vs 20d SMA 395.76 (-3.6%), 50d 396.06 (-3.6%), 200d 416.30 (-8.3%); 50d below 200d
Momentum: RSI(14) 39.1 | MACD -4.412 vs signal -2.180 (histogram -2.232)
Returns: 1d -0.3% | 5d -2.9% | 1m -6.6% | 3m +3.0%
52-week range: 354.79 - 495.90 (now 19.0% of the way up)
Volatility: ATR(14) 7.19 (1.9% of price) | annualised 20d 23.2%
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
Cost of holding this fund instead of gold itself: -0.6% a year -- close to nothing, as a physically backed fund should be
Measured: 3 months: fund +3.0%, commodity +2.8%, gap +0.2% | 6 months: fund -11.3%, commodity -9.7%, gap -1.6% | 12 months: fund +8.3%, commodity +8.9%, gap -0.6%
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
Contract: GOLD - COMMODITY EXCHANGE INC. (positions as of 2026-09-22, published the following Friday)
Large speculators: net long 30.9% of open interest (412,800 contracts)
Change on the week: -1.6% of open interest
Crowding: 63% percentile over 52 weeks -- within its normal range
Read this as crowding, not as a forecast: an extreme is as often the end of a move as the middle of one.
```

</details>

<details><summary><b>Money going into and out of this fund</b> — score n/a</summary>

```text
Direction: flat (1 week)
Share count change: 1 week: +0.0% (0.00) over 7d
Shares outstanding: 260.30M | fund size: 99.34B
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

