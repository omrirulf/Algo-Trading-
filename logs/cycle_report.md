# Daily report

**21 Oct 2026, 19:33 Israel time (16:33 UTC)** · 80 names checked · 4 traded · 0 with a problem

**Answers with no explanation:** 15 of 69 (the model wrote only a label, like “NEUTRAL”, where its reason should be). Their main reasons are still shown.

**Run:** started by the outside scheduler (via supabase-cron), on time (planned for 14:40 UTC).

| Group | Looked at | Took a side | No clear view | Problems |
| --- | --- | --- | --- | --- |
| Companies | 16 | 7 | 9 | 0 |
| Whole-market funds | 14 | 0 | 14 | 0 |
| Sector and country funds | 41 | 1 | 40 | 0 |
| Commodities | 9 | 0 | 9 | 0 |

## Open positions

Checked before any new trade. R is what the trade risked at entry; the ladder sells a third at +1R and another at +3R, the stop-loss follows the price up every day, and it only ever moves up.

| Position | What happened |
| --- | --- |
| Royal Bank of Canada (RY) · Company | **Stop raised.** At +0.85R, following the price. Stop-loss raised 192.77 → 194.88. |
| US materials and chemicals (XLB) · Sector or country | **Stop raised.** At +0.04R, following the price. Stop-loss raised 49.58 → 49.68. |
| Argentina (ARGT) · Sector or country | **Holding.** -0.27R, holding 80 shares. Stop-loss 86.01. |
| ASML (ASML) · Company | **Holding.** -0.24R, holding 3 shares. Stop-loss 1750.24. |
| United Kingdom (EWU) · Sector or country | **Holding.** +1.72R, holding 104 shares. Stop-loss 47.23. |
| Gold (GLD) · Commodity | **Holding.** +0.69R, holding 10 shares. Stop-loss 387.99. |
| US company bonds, riskier (HYG) · Index fund | **Holding.** -0.26R, holding 158 shares. Stop-loss 76.66. |
| Defence and aerospace (ITA) · Sector or country | **Holding.** -0.48R, holding 33 shares. Stop-loss 201.78. |
| Eli Lilly (LLY) · Company | **Holding.** +1.98R, holding 3 shares. Stop-loss 1224.49. |
| Nvidia (NVDA) · Company | **Holding.** -0.16R, holding 23 shares. Stop-loss 228.84. |
| Exxon Mobil (XOM) · Company | **Holding.** +2.17R, holding 9 shares. Stop-loss 170.88. |

## How to read this

Once a day the system looks at every name on the list. For each one it reads five kinds of evidence and gives each kind a score from -1.00 (bad) to +1.00 (good). Then it picks a side and says how sure it is, from 0.00 to 1.00.

The three sides: **BULLISH** = the model thinks the price will go up; **BEARISH** = the model thinks the price will go down; **NEUTRAL** = the model has no clear view.

Being sure is not enough on its own. A trade only happens when confidence reaches **0.30**. Below that the system writes down what it thought and does nothing. The size of a trade, the stop-loss and every limit are decided by plain code, not by the model.

Open positions are checked first, before any new trade. When a trade has earned back what it risked (+1R), a third of it is sold and the stop-loss moves up to the entry price, so it can no longer lose. At three times that (+3R) another third is sold and the stop moves up again. The last third stays open. Every day the stop-loss also follows the price up, so a position only ever closes when its stop is hit. The stop only ever moves up.

Under each name you will find the five scores. Click a grey line to open it and see the exact evidence behind that score. The words inside quotation marks are the model's own; nothing there has been rewritten.

## Companies

### Teva Pharmaceutical (TEVA) · Company — BULLISH, confidence 0.82

**Result:** REJECTED · no room under the sleeve budget limit

**In the model's own words:**

> Strong, ticker‑specific clinical trial data (Phase IIb IBD trial and 44‑week duvakitug data) provide a clear material catalyst, reinforced by a strong‑buy analyst consensus with a +16% price‑target gap and fresh upgrades. Technicals are neutral‑to‑slightly bearish (thin volume near 52‑week high), and fundamentals are mixed (high leverage, low margins, but forward P/E reasonable and 3 of 4 earnings beats). Insider activity shows routine net selling, offering no directional signal. Overall bullish signals dominate, justifying a BUY with high conviction.

**Main reasons it gave:**
- Phase IIb trial of Sanofi/Teva IBD drug shows long-term remission in ulcerative colitis and Crohn's disease (Yahoo Finance, 3h ago)
- 44-week duvakitug trial data shows 58% remission at 900 mg (AD HOC NEWS, 6h ago)
- Analyst consensus strong buy; mean price target $47.58 (+16% vs current price) (Analyst & Institutional View)
- Technicals: price near 52-week high with thin volume (0.33x 20‑day average) (Technicals)

<details><summary><b>News</b> — score +0.80</summary>

- [Sanofi & Teva’s IBD drug prompts long-term clinical remission in Phase IIb trial](https://finance.yahoo.com/news/sanofi-teva-ibd-drug-prompts-121920916.html)  
  <sub>Yahoo Finance, 3 hours ago</sub>  
  Sanofi and Teva Pharmaceuticals' inflammatory bowel disease (IBD) drug has shown benefit in patients with both ulcerative colitis (UC) and Crohn's disease.
- [TD Cowen raises Aurinia Pharmaceuticals price target on cost outlook](https://www.investing.com/news/analyst-ratings/td-cowen-raises-aurinia-pharmaceuticals-price-target-on-cost-outlook-93CH-4962389)  
  <sub>Investing.com, 4 hours ago</sub>  
  Investing.com - TD Cowen raised its price target on Aurinia Pharmaceuticals stock (NASDAQ:AUPH) to $18 from $17 while maintaining a Buy rating.
- [Teva reports 44-week duvakitug data and Barclays targets Teva stock at USD 47.00](https://www.ad-hoc-news.de/boerse/news/corporate-news/teva-reports-44-week-duvakitug-data-and-barclays-targets-teva-stock-at-usd-47-00/70381745)  
  <sub>AD HOC NEWS, 6 hours ago</sub>  
  Duvakitug data covered 130 responders through week 44, while Teva stock awaits November 3 results. The trial reached 58 percent remission at 900 mg.
- [Here Are Wednesday’s Top Wall Street Analyst Research Calls: Applied Digital, Chipotle Mexican Grill, Cirrus Logic, Costco, Digital Realty Trust, Intuitive Surgical, Netflix, Robinhood Markets, Zscaler, and More](https://finance.yahoo.com/markets/stocks/articles/wednesday-top-wall-street-analyst-120222779.html)  
  <sub>Yahoo Finance, 3 hours ago</sub>  
  Strong Q3 earnings pushed the Russell 2000 up 2% and the Dow up 1%, with an avalanche of results still scheduled this week. Fortinet was double-downgraded...
- [Study Shows GLP-1 Medications Might Aid in Prevention and Treatment of Substance Use Disorders](https://www.drugtopics.com/view/study-shows-glp-1-medications-might-aid-in-prevention-and-treatment-of-substance-use-disorders)  
  <sub>Drug Topics, 16 hours ago</sub>  
  GLP-1 diabetes drugs show promise in cutting addiction risk and overdose deaths, hinting at new options for substance use disorder prevention and care.
- [Alvotech's Manufacturing Progress, Simponi Launch Potential Support Recovery, UBS Says](https://www.moomoo.com/news/post/1001748210/alvotech-s-manufacturing-progress-simponi-launch-potential-support-recovery-ubs)  
  <sub>Moomoo, 22 hours ago</sub>  
  Alvotech(ALVO) has meaningful stock recovery potential as manufacturing progress boosts confidence and regulatory uncertainty eases, UBS Securities said in...
- [Alvotech (NASDAQ:ALVO) Shares Gap Up - What's Next?](https://www.marketbeat.com/instant-alerts/price-alvotech-nasdaq-alvo-shares-gap-up-whats-next-2026-10-20/)  
  <sub>MarketBeat, 24 hours ago</sub>  
  Alvotech (NASDAQ:ALVO - Get Free Report) shares gapped up prior to trading on Tuesday. The stock had previously closed at $5.03, but opened at $5.40.
- [Why We Must Boycott Teva](https://aontachtmedia.ie/why-we-must-boycott-teva/)  
  <sub>Aontacht Media, 21 hours ago</sub>  
  Teva has a track record of prioritising profit over the welfare of ordinary people, no matter their nationality. Omar Afzal. 20 Oct 2026 — 3 min read. Share.
- [FDA Approves Bepirovirsen Injection to Treat Chronic Hepatitis B](https://www.google.com/goto?url=CAESmwEB6zswFTPSuwX-HQiByCwlUrJb5OSkBVub7MbrPGX3sborQubr3P1DbYm8PPt-H1KojiZgWtD53fF8XFgevKChoP0sjqeGUOH3aq1HA5ZXOphq-Y3SyDEZtjH124OIozD54X5VJquwdbJbFw_20LGwylNHuqvbAW_fA3af0AzSQRrbQpRGOw65lBYRktzWAnpNYVQu5659ktWz7A)  
  <sub>Drug Topics, 1 hour ago</sub>  
  Approval was given to GSK, making its product the first antisense oligonucleotide established for the treatment of chronic hepatitis B.
- [Tue: Leumi lifts TASE](https://en.globes.co.il/en/article-tue-leumi-lifts-tase-1001560247)  
  <sub>Globes - Israel Business News, 22 hours ago</sub>  
  The Tel Aviv Stock Exchange rose today. The Tel Aviv 35 Index rose 0.20% to 4,214.13 points, the Tel Aviv 125 Index rose 0.48% to 4,091.46 points;...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.80</summary>

_Not available today._

</details>

<details><summary><b>Price and chart</b> — score -0.10</summary>

```text
Last close 40.87 (bar of 2026-10-21), from 502 daily bars
Trend: vs 20d SMA 40.18 (+1.7%), 50d 38.57 (+6.0%), 200d 34.30 (+19.1%); 50d above 200d
Momentum: RSI(14) 59.2 | MACD 0.802 vs signal 0.826 (histogram -0.024)
Returns: 1d +0.0% | 5d +0.4% | 1m +3.4% | 3m +31.1%
52-week range: 18.95 - 41.50 (now 97.2% of the way up)
Volatility: ATR(14) 1.13 (2.8% of price) | annualised 20d 26.2%
Volume: 0.33x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score -0.10</summary>

```text
Sector: Healthcare / Drug Manufacturers - Specialty & Generic | market cap 47.66B
Valuation: trailing P/E 68.11 | forward P/E 13.25 | P/B 6.14 | PEG n/a
Profitability: profit margin 4.1% | operating margin 4.0% | ROE 9.7%
Growth (YoY): revenue -0.8% | earnings n/a
Balance sheet: debt/equity 217.8% | free cash flow 2.22B
Risk: beta 0.82 | short interest 2.6% of float
Next earnings: 2026-11-03
```

</details>

<details><summary><b>What this fund holds</b> — score -0.10</summary>

_Not available today._

</details>

<details><summary><b>Does this company beat its own forecasts</b> — score -0.10</summary>

```text
Earnings record, last 4 quarters: 3 beats, 1 missed
  2026-06-30 missed by 92% | 2026-03-31 beat by 9% | 2025-12-31 beat by 39% | 2025-09-30 beat by 17%
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

<details><summary><b>What analysts and big funds say</b> — score +0.70</summary>

```text
Consensus: strong_buy (mean 1.46 on a 1=strong buy to 5=strong sell scale, 12 analysts)
Ratings: 4 strong buy, 8 buy, 1 hold, 0 sell, 0 strong sell
Price target: mean 47.58 (+16.4% vs last close), range 42.00 - 55.00
Recent rating changes:
  - 2026-10-15 Barclays: main, Overweight -> Overweight
  - 2026-10-12 JP Morgan: main, Overweight -> Overweight
  - 2026-10-01 TD Cowen: init, ? -> Buy
  - 2026-09-23 Oppenheimer: init, ? -> Outperform
  - 2026-09-09 Leerink Partners: init, ? -> Outperform
  - 2026-09-04 UBS: main, Buy -> Buy
Institutional ownership: 27.0%
Largest holders: Blackrock Inc. (5.5%), Harel Insurance Investments & Financial Services Ltd. (4.1%), Phoenix Financial Ltd. (3.7%), WCM Investment Management, LLC (3.5%), Clal Insurance Enterprises Holdings Ltd (3.5%)
```

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score +0.70</summary>

_Not available today._

</details>

<details><summary><b>Buying and selling by company insiders</b> — score +0.00</summary>

```text
Last 180 days: bought 43,476 shares in 3 transaction(s) | sold 194,459 shares in 6
Net: -150,983 shares (-2.3% of insider holdings) | insiders hold 6,525,658 shares
Distinct insiders: 0 buying, 10 selling
Sales — weak evidence on their own; often scheduled 10b5-1 plans, tax on vesting, or diversification:
  - 2026-09-18 SAVAGE BRIAN (Officer): 7,342 shares, 285.21K
  - 2026-09-18 MIGNONE ROBERTO A. (Director): 367,600 shares, 14.36M
  - 2026-08-21 WEISS AMIR (Officer): 9,445 shares, 355.30K
  - 2026-08-03 JOVER PLACID (Officer): 12,827 shares, 447.35K
(13 grant/option/gift transaction(s) excluded — compensation, not a view on the price)
```

</details>

<details><summary><b>Who is positioned how</b> — score +0.00</summary>

_Not available today._

</details>

<details><summary><b>Money going into and out of this fund</b> — score +0.00</summary>

_Not available today._

</details>

### Elbit Systems (ESLT) · Company — BULLISH, confidence 0.65

**Result:** REJECTED · no room under the sleeve budget limit

**In the model's own words:** no explanation. It wrote only “BUY”, so the main reasons below are all it gave.

**Main reasons it gave:**
- $235M contract win to supply EXTRA-MR rockets to European customer (news)
- Four consecutive earnings beats in last four quarters (earnings record)
- Revenue growth +15.9% YoY and earnings growth +34.2% YoY (fundamentals)
- Price above 20‑day and 50‑day SMA with bullish MACD (technical)

<details><summary><b>News</b> — score +0.80</summary>

- [Elbit Systems stock: November 17 results set the next test for Elbit Systems stock](https://www.ad-hoc-news.de/boerse/news/corporate-news/elbit-systems-stock-november-17-results-set-the-next-test-for-elbit-systems-stock/70385012)  
  <sub>AD HOC NEWS, 44 minutes ago</sub>  
  Six ratings average an ILS 880.88 target. Elbit Systems stock costs EUR 662.75 on October 21, 2026, 21.88 percent below its EUR 848.50 high.
- [Elbit Systems wins USD 235 million deal: Elbit Systems stock has USD 34.9 billion value](https://www.ad-hoc-news.de/boerse/news/corporate-news/elbit-systems-wins-usd-235-million-deal-elbit-systems-stock-has-usd-34-9-billion-value/70381012)  
  <sub>AD HOC NEWS, 7 hours ago</sub>  
  Elbit Systems won a USD 235.00 million deal on October 19, 2026, under a three-year contract. Elbit Systems stock costs EUR 665.75 on October 21, 2026.
- [Elbit Systems Wins $235M Contract To Supply Rocket Artillery Systems To European Customer: What Investors Need To Know](https://stocktwits.com/news-articles/markets/equity/elbit-systems-wins-235-m-contract-to-supply-rocket-artillery-systems-to-european-customer-what-investors-need-to-know/cZx8ZAKRBMS)  
  <sub>Stocktwits, 14 hours ago</sub>  
  Elbit Systems (ESLT) drew investor attention on Monday after the defense technology company announced a $235 million contract to supply EXTRA-MR rockets and...
- [Kratos Defense & Security Solutions, Inc. (KTOS) stock price, news, quote and history - Yahoo Finance](https://sg.finance.yahoo.com/quote/KTOS/latest-news/)  
  <sub>Yahoo Finance Singapore, 12 hours ago</sub>  
  Find the latest Kratos Defense & Security Solutions, Inc. (KTOS) stock quote, history, news and other vital information to help you with your stock trading...
- [Cathie Wood Sells $5.4 Million Worth of Palantir Stock as Ark Continues to Dump PLTR, Analyst Warns Valua](https://www.benzinga.com/etfs/broad-u-s-equity-etfs/26/10/62485690/cathie-wood-ark-invest-sells-5-million-palantir-stock-valuation-warning)  
  <sub>Benzinga, 13 hours ago</sub>  
  Cathie Wood's Ark sold Palantir shares and bought Oklo and X-Energy shares on Tuesday, Oct. 20, 2026.
- [Red Cat Holdings, Inc. (RCAT) stock price, news, quote and history - Yahoo Finance](https://sg.finance.yahoo.com/quote/RCAT/latest-news/)  
  <sub>Yahoo Finance Singapore, 12 hours ago</sub>  
  Find the latest Red Cat Holdings, Inc. (RCAT) stock quote, history, news and other vital information to help you with your stock trading and investing.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.80</summary>

_Not available today._

</details>

<details><summary><b>Price and chart</b> — score +0.20</summary>

```text
Last close 740.00 (bar of 2026-10-21), from 502 daily bars
Trend: vs 20d SMA 705.52 (+4.9%), 50d 723.88 (+2.2%), 200d 782.41 (-5.4%); 50d below 200d
Momentum: RSI(14) 56.9 | MACD 3.351 vs signal -6.120 (histogram 9.472)
Returns: 1d -0.6% | 5d +5.5% | 1m -0.6% | 3m -8.5%
52-week range: 454.95 - 1,014.33 (now 51.0% of the way up)
Volatility: ATR(14) 19.33 (2.6% of price) | annualised 20d 40.7%
Volume: 0.22x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.30</summary>

```text
Sector: Industrials / Aerospace & Defense | market cap 34.68B
Valuation: trailing P/E 55.68 | forward P/E 39.76 | P/B 7.85 | PEG n/a
Profitability: profit margin 7.4% | operating margin 9.6% | ROE 15.2%
Growth (YoY): revenue +15.9% | earnings +34.2%
Balance sheet: debt/equity 19.3% | free cash flow -38.48M
Risk: beta -0.30 | short interest 0.8% of float
Next earnings: 2026-11-24
```

</details>

<details><summary><b>What this fund holds</b> — score +0.30</summary>

_Not available today._

</details>

<details><summary><b>Does this company beat its own forecasts</b> — score +0.30</summary>

```text
Earnings record, last 4 quarters: 4 beats
  2026-06-30 beat by 10% | 2026-03-31 beat by 16% | 2025-12-31 beat by 16% | 2025-09-30 beat by 21%
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

<details><summary><b>What analysts and big funds say</b> — score +0.00</summary>

```text
Consensus: hold (mean 2.67 on a 1=strong buy to 5=strong sell scale, 6 analysts)
Ratings: 0 strong buy, 1 buy, 5 hold, 0 sell, 0 strong sell
Price target: mean 802.17 (+8.4% vs last close), range 518.00 - 960.00
Recent rating changes:
  - 2026-10-05 Jefferies: main, Hold -> Hold
  - 2026-08-19 JP Morgan: main, Neutral -> Neutral
  - 2026-06-24 Jefferies: main, Hold -> Hold
  - 2026-05-27 Jefferies: main, Hold -> Hold
  - 2026-05-27 JP Morgan: main, Neutral -> Neutral
  - 2026-04-13 JP Morgan: main, Neutral -> Neutral
Institutional ownership: 23.0%
Largest holders: Clal Insurance Enterprises Holdings Ltd (3.5%), Vanguard Capital Management LLC (1.6%), Van Eck Associates Corporation (1.2%), Y.D. More Investments Ltd (1.0%), Altshuler Shaham Ltd (1.0%)
```

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score +0.00</summary>

_Not available today._

</details>

<details><summary><b>Buying and selling by company insiders</b> — score +0.00</summary>

```text
Last 180 days: bought 0 shares in 0 transaction(s) | sold n/a shares in 0
Net: +0 shares | insiders hold 19,278,816 shares
Distinct insiders: 0 buying, 0 selling
```

</details>

<details><summary><b>Who is positioned how</b> — score +0.00</summary>

_Not available today._

</details>

<details><summary><b>Money going into and out of this fund</b> — score +0.00</summary>

_Not available today._

</details>

### Caterpillar (CAT) · Company — BULLISH, confidence 0.62

**Result:** REJECTED · no room under the sleeve budget limit

**In the model's own words:** no explanation. It wrote only “BUY”, so the main reasons below are all it gave.

**Main reasons it gave:**
- Earnings beat record: 4 consecutive beats (31%, 19%, 9%, 8%)
- Analyst price target +28.7% above current price
- Net insider buying (+4.2% of holdings) despite executive sales
- Technical downtrend: price below 20d/50d/200d SMAs, RSI 33.9
- North Carolina expansion: $1B investment

<details><summary><b>News</b> — score +0.20</summary>

- [CAT Keeps Dividend Unchanged: Is Another Hike on the Horizon?](https://finance.yahoo.com/markets/stocks/articles/cat-keeps-dividend-unchanged-another-130900328.html)  
  <sub>Yahoo Finance, 2 hours ago</sub>  
  Caterpillar Inc. CAT continues to demonstrate its commitment to shareholder returns, supported by consistent dividend payments, robust cash flow generation...
- [CAT 261023 555.00C (CAT261023C555000) Stock Options Chain | Quotes & News](https://www.moomoo.com/options/CAT261023C555000-US)  
  <sub>Moomoo, 5 hours ago</sub>  
  Track real-time CAT 261023 555.00C (CAT261023C555000) stock options chain data and pricing information and news on moomoo App for your options trading and...
- [Red Cat: Steyr Acquisition Raises Dilution Risk (NASDAQ:RCAT)](https://seekingalpha.com/article/4955796-red-cat-steyr-acquisition-raises-dilution-risk-rating-downgrade)  
  <sub>Seeking Alpha, 5 hours ago</sub>  
  Red Cat's multi-domain unmanned capabilities are expanding, notably with Steyr's propulsion expertise and European defense relationships.
- [Caterpillar (CAT) Expands In North Carolina As Investors Ask If The Stock Is A Bargain](https://simplywall.st/stocks/us/capital-goods/nyse-cat/caterpillar/news/caterpillar-cat-expands-in-north-carolina-as-investors-ask-i)  
  <sub>Simply Wall Street, 17 hours ago</sub>  
  Caterpillar (CAT) is back in focus after committing about US$1b to expand its Cat Compact manufacturing footprint in North Carolina, including a new Sanford...
- [ETFs Are Net Sellers of Caterpillar (CAT) on Oct. 19](https://finance.yahoo.com/markets/stocks/articles/etfs-net-sellers-caterpillar-cat-110234932.html)  
  <sub>Yahoo Finance, 4 hours ago</sub>  
  ETFs sold $31.8 million of Caterpillar stock on a net basis, with 26 funds buying and 19 selling.
- [Caterpillar (CAT) Formally Objects To Tokenized Trading Of Its Shares](https://finance.yahoo.com/markets/crypto/articles/caterpillar-cat-formally-objects-tokenized-210914768.html)  
  <sub>Yahoo Finance, 18 hours ago</sub>  
  Caterpillar (NYSE:CAT) has formally objected to its shares being traded on the OKX-ICE Tokenized Stock Venue. The company states it did not authorize any...
- [Red Cat Holdings, Inc. (RCAT) stock price, news, quote and history - Yahoo Finance](https://sg.finance.yahoo.com/quote/RCAT/latest-news/)  
  <sub>Yahoo Finance Singapore, 12 hours ago</sub>  
  Red Cat Holdings, Inc. (RCAT) · 3 Drone Defense Stocks With Revenue Growth Up To 44% · 3 Drone Defense Stocks To Watch With Up To 44% Revenue Growth · 3 Drone...
- [Caterpillar Inc. (CAT) stock price, news, quote and history](https://au.finance.yahoo.com/quote/CAT/latest-news/)  
  <sub>Yahoo Finance Australia, 21 hours ago</sub>  
  Find the latest Caterpillar Inc. (CAT) stock quote, history, news and other vital information to help you with your stock trading and investing.
- [CAT280616C00620000 Interactive Stock Chart | CAT Jun 2028 620.000 call Stock](https://finance.yahoo.com/chart/CAT280616C00620000)  
  <sub>Yahoo Finance, 13 hours ago</sub>  
  At Yahoo Finance, you get free stock quotes, up-to-date news, portfolio management resources, international market data, social interaction and mortgage...
- [CAT 261023 590.00C (CAT261023C590000) Stock Options Chain | Quotes & News](https://www.moomoo.com/options/CAT261023C590000-US)  
  <sub>Moomoo, 21 hours ago</sub>  
  Track real-time CAT 261023 590.00C (CAT261023C590000) stock options chain data and pricing information and news on moomoo App for your options trading and...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.20</summary>

_Not available today._

</details>

<details><summary><b>Price and chart</b> — score -0.50</summary>

```text
Last close 735.13 (bar of 2026-10-21), from 502 daily bars
Trend: vs 20d SMA 792.59 (-7.2%), 50d 806.02 (-8.8%), 200d 807.73 (-9.0%); 50d below 200d
Momentum: RSI(14) 33.9 | MACD -23.731 vs signal -14.984 (histogram -8.747)
Returns: 1d +1.4% | 5d -1.8% | 1m -9.0% | 3m -17.8%
52-week range: 513.91 - 1,064.90 (now 40.1% of the way up)
Volatility: ATR(14) 26.19 (3.6% of price) | annualised 20d 32.9%
Volume: 0.22x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.30</summary>

```text
Sector: Industrials / Farm & Heavy Construction Machinery | market cap 337.92B
Valuation: trailing P/E 31.65 | forward P/E 22.56 | P/B 17.42 | PEG 1.42
Profitability: profit margin 14.5% | operating margin 22.2% | ROE 57.0%
Growth (YoY): revenue +24.0% | earnings +68.2%
Balance sheet: debt/equity 232.8% | free cash flow 5.05B
Risk: beta 1.58 | short interest 1.9% of float
Next earnings: 2026-10-29
```

</details>

<details><summary><b>What this fund holds</b> — score +0.30</summary>

_Not available today._

</details>

<details><summary><b>Does this company beat its own forecasts</b> — score +0.30</summary>

```text
Earnings record, last 4 quarters: 4 beats
  2026-06-30 beat by 31% | 2026-03-31 beat by 19% | 2025-12-31 beat by 9% | 2025-09-30 beat by 8%
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
Consensus: buy (mean 2.00 on a 1=strong buy to 5=strong sell scale, 26 analysts)
Ratings: 1 strong buy, 15 buy, 12 hold, 1 sell, 0 strong sell
Price target: mean 945.76 (+28.7% vs last close), range 575.00 - 1,155.00
Recent rating changes:
  - 2026-10-14 Oppenheimer: main, Outperform -> Outperform
  - 2026-10-12 Citigroup: main, Buy -> Buy
  - 2026-10-05 Truist Securities: main, Buy -> Buy
  - 2026-09-10 Freedom Broker: up, Hold -> Buy
  - 2026-08-11 Evercore ISI Group: main, Outperform -> Outperform
  - 2026-08-06 DA Davidson: main, Neutral -> Neutral
Institutional ownership: 73.5%
Largest holders: Blackrock Inc. (8.3%), State Street Corporation (7.5%), Vanguard Capital Management LLC (6.5%), State Farm Mutual Automobile Insurance Co (3.2%), Vanguard Portfolio Management LLC (2.6%)
```

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score +0.50</summary>

_Not available today._

</details>

<details><summary><b>Buying and selling by company insiders</b> — score +0.10</summary>

```text
Last 180 days: bought 169,246 shares in 20 transaction(s) | sold 128,174 shares in 10
Net: +41,072 shares (+4.2% of insider holdings) | insiders hold 1,006,687 shares
Distinct insiders: 1 buying, 8 selling
Open-market purchases — insiders spending their own money:
  - 2026-05-04 MACLENNAN DAVID W (Director): 250 shares, 219.21K
Sales — weak evidence on their own; often scheduled 10b5-1 plans, tax on vesting, or diversification:
  - 2026-08-28 CREED JOSEPH E (Chief Executive Officer): 32,401 shares, 26.21M
  - 2026-05-14 JOHNSON DENISE C. (Officer): 12,605 shares, 11.44M
  - 2026-05-13 SCHAUPP WILLIAM E (Officer): 360 shares, 326.16K
  - 2026-05-13 JOHNSON DENISE C. (Officer): 6,196 shares, 5.64M
(19 grant/option/gift transaction(s) excluded — compensation, not a view on the price)
```

</details>

<details><summary><b>Who is positioned how</b> — score +0.10</summary>

_Not available today._

</details>

<details><summary><b>Money going into and out of this fund</b> — score +0.10</summary>

_Not available today._

</details>

### Microsoft (MSFT) · Company — BULLISH, confidence 0.55

**Result:** ACCEPTED · 9 shares · submitted buy 9 MSFT @ ~532.09, stop 509.74

**In the model's own words:**

> Strong fundamentals, consistent earnings beats, and bullish analyst consensus outweigh slightly negative technical signals and neutral insider activity.

**Main reasons it gave:**
- Four consecutive earnings beats (10%, 3%, 6%, 5% beats)
- Strong fundamentals: profit margin 40.3%, ROE 34%, revenue growth 17.7% YoY
- Analyst consensus strong buy, mean price target $600.9 (+13.5% above current price)
- Technical indicators: MACD below signal, thin volume (0.17x 20‑day avg) suggest weak short‑term momentum
- Insider activity: net buy of 263,995 shares (+4.7% holdings) but no distinct insider purchases, sales by CFO/CEO

<details><summary><b>News</b> — score +0.00</summary>

_No news found for this one today._

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

_Not available today._

</details>

<details><summary><b>Price and chart</b> — score -0.30</summary>

```text
Last close 529.29 (bar of 2026-10-21), from 502 daily bars
Trend: vs 20d SMA 524.94 (+0.8%), 50d 507.23 (+4.3%), 200d 436.08 (+21.4%); 50d above 200d
Momentum: RSI(14) 56.4 | MACD 9.293 vs signal 10.446 (histogram -1.153)
Returns: 1d -0.5% | 5d -0.8% | 1m +6.3% | 3m +38.7%
52-week range: 352.83 - 543.45 (now 92.6% of the way up)
Volatility: ATR(14) 11.12 (2.1% of price) | annualised 20d 21.9%
Volume: 0.17x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.60</summary>

```text
Sector: Technology / Software - Infrastructure | market cap 3.93T
Valuation: trailing P/E 29.48 | forward P/E 22.33 | P/B 8.89 | PEG 1.62
Profitability: profit margin 40.3% | operating margin 45.1% | ROE 34.0%
Growth (YoY): revenue +17.7% | earnings +31.7%
Balance sheet: debt/equity 29.1% | free cash flow 16.55B
Risk: beta 1.10 | short interest 0.8% of float
Next earnings: 2026-10-28
```

</details>

<details><summary><b>What this fund holds</b> — score +0.60</summary>

_Not available today._

</details>

<details><summary><b>Does this company beat its own forecasts</b> — score +0.60</summary>

```text
Earnings record, last 4 quarters: 4 beats
  2026-06-30 beat by 10% | 2026-03-31 beat by 3% | 2025-06-30 beat by 6% | 2025-03-31 beat by 5%
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
Consensus: strong_buy (mean 1.33 on a 1=strong buy to 5=strong sell scale, 53 analysts)
Ratings: 13 strong buy, 41 buy, 3 hold, 0 sell, 0 strong sell
Price target: mean 600.88 (+13.5% vs last close), range 440.00 - 870.00
Recent rating changes:
  - 2026-10-21 Guggenheim: reit, Buy -> Buy
  - 2026-10-20 BMO Capital: main, Outperform -> Outperform
  - 2026-10-19 Bernstein: main, Outperform -> Outperform
  - 2026-10-16 StoneX: main, Buy -> Buy
  - 2026-10-15 UBS: main, Buy -> Buy
  - 2026-10-15 Citigroup: main, Buy -> Buy
Institutional ownership: 75.8%
Largest holders: Blackrock Inc. (8.2%), Vanguard Capital Management LLC (6.5%), State Street Corporation (4.2%), Geode Capital Management, LLC (2.5%), FMR, LLC (2.5%)
```

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score +0.30</summary>

_Not available today._

</details>

<details><summary><b>Buying and selling by company insiders</b> — score +0.00</summary>

```text
Last 180 days: bought 513,644 shares in 16 transaction(s) | sold 249,649 shares in 10
Net: +263,995 shares (+4.7% of insider holdings) | insiders hold 5,866,181 shares
Distinct insiders: 0 buying, 5 selling
Sales — weak evidence on their own; often scheduled 10b5-1 plans, tax on vesting, or diversification:
  - 2026-10-13 HOOD AMY E (Chief Financial Officer): 7,305 shares, 3.98M
  - 2026-09-14 HOOD AMY E (Chief Financial Officer): 41,674 shares, 20.76M
  - 2026-09-01 NADELLA SATYA (Chief Executive Officer): 86,525 shares, 43.39M
  - 2026-08-05 ALTHOFF JUDSON (Officer): 10,000 shares, 4.88M
(15 grant/option/gift transaction(s) excluded — compensation, not a view on the price)
```

</details>

<details><summary><b>Who is positioned how</b> — score +0.00</summary>

_Not available today._

</details>

<details><summary><b>Money going into and out of this fund</b> — score +0.00</summary>

_Not available today._

</details>

**Data that was missing** (counted as 0.00, never guessed):
- news unavailable: Bright Data unreachable: The read operation timed out

### Novo Nordisk (NVO) · Company — BULLISH, confidence 0.55

**Result:** REJECTED · no room under the sleeve budget limit

**In the model's own words:**

> Positive CagriSema weight‑loss data provides a material, ticker‑specific catalyst that has already moved the stock up ~2%. Technicals show the price above the 20‑day SMA but still below the 50‑day and 200‑day SMAs, with very low volume, indicating a modestly bearish backdrop. Fundamentals are solid with a cheap trailing P/E of 9.23 and strong profitability, though growth is weak. Analyst consensus is neutral with mixed recent rating changes, and there is no insider activity. Earnings record shows 2 misses, 1 beat, and 1 in‑line, adding slight bearish pressure. Overall, the bullish news outweighs the modest technical and earnings concerns, leading to a BUY signal with moderate conviction.

**Main reasons it gave:**
- CagriSema weight‑loss data showed 25% loss in women, shares rose ~2%
- Price above 20‑day SMA (+2.3%) but below 50‑day and 200‑day SMAs, indicating downtrend
- Volume at 0.17× 20‑day average, indicating weak participation
- Trailing P/E 9.23, cheap relative to peers despite earnings decline
- Earnings record: 2 misses, 1 beat, 1 in‑line over last 4 quarters

<details><summary><b>News</b> — score +0.60</summary>

- [BIOA, GLUE Stocks Clock Worst Day In Years— What’s The NVO Connection?](https://stocktwits.com/news-articles/markets/equity/bioa-glue-stocks-clock-worst-day-in-years-what-s-the-nvo-connection/cZN4NtDRJ5G)  
  <sub>Stocktwits, 14 hours ago</sub>  
  Citi noted BIOA's greater-than-60% drop and agreed the data is a negative for BioAge's heart-disease thesis, yet argued the size of the move “seems overdone”...
- [Eli Lilly Rises 4% While Foundayo Nears European Approval; Amgen and Novo Nordisk Edge Higher](https://247wallst.com/investing/2026/10/20/eli-lilly-rises-4-while-foundayo-nears-european-approval-amgen-and-novo-nordisk-edge-higher/)  
  <sub>24/7 Wall St., 22 hours ago</sub>  
  Eli Lilly surged 4% after Europe's medicines committee recommended Foundayo for both obesity and diabetes, a wider label than any rival oral pill holds.
- [NVO Nov 2026 28.000 put (NVO261113P00028000) Stock Price, News, Quote & History](https://ca.finance.yahoo.com/quote/NVO261113P00028000/)  
  <sub>Yahoo! Finance Canada, 23 hours ago</sub>  
  Find the latest NVO Nov 2026 28.000 put (NVO261113P00028000) stock quote, history, news and other vital information to help you with your stock trading and...
- [Hims & Hers gains after German launch](https://seekingalpha.com/news/4654744-hims-hers-stock-gains-german-launch)  
  <sub>Seeking Alpha, 23 hours ago</sub>  
  Shares of Hims & Hers Health (HIMS) rose on Tuesday after the telehealth platform launched in Germany, expanding its European market presence further...
- [OMER Stock Surges 5% After Hours On Novo Nordisk Deal Windfall And Drug Launch Optimism](https://stocktwits.com/news-articles/markets/equity/omer-stock-surges-after-hours-on-novo-nordisk-deal-windfall-drug-launch-optimism/cZE5fIyRIVy)  
  <sub>Stocktwits, 14 hours ago</sub>  
  Omeros reported net income for the fourth quarter of $86.5 million, compared to a net loss of $31.4 million in the corresponding quarter of 2024.
- [SOFI Stock Got Hit With Price-Target Cuts After Q2 Earnings, But One Contrarian Says Market Is Missing Bigger Story](https://stocktwits.com/news-articles/markets/equity/sofi-stock-got-hit-with-price-target-cuts-after-q2-earnings-but-one-contrarian-says-market-is-missing-bigger-story/cZoRwebRJ5l)  
  <sub>Stocktwits, 15 hours ago</sub>  
  Shay Boloor, chief market strategist at Futrum Equities, said in a post on X that the market is overpricing credit risk and underpricing the platform even...
- [Novo Resources schedules November 5 results: what it means for Novo Resources stock](https://www.ad-hoc-news.de/boerse/news/nebenwerte/novo-resources-schedules-november-5-results-what-it-means-for-novo-resources-stock/70377258)  
  <sub>AD HOC NEWS, 20 hours ago</sub>  
  Novo Resources posted a CAD 3.25 million second-quarter loss. Novo Resources stock costs CAD 0.06 on TSX on October 20, 2026 at 1:52 p.m. ET.
- [AXTI Stock Skyrockets As Investors Cheer Blowout Guidance, Record Quarterly Revenue — Needham Spots A 'Real' AI Networking Opportunity](https://stocktwits.com/news-articles/markets/equity/axti-stock-skyrockets-blowout-guidance-record-revenue-ai-oppurtunity/cZN4aMRRJPK)  
  <sub>Stocktwits, 14 hours ago</sub>  
  Needham upgraded AXT to 'Buy' from 'Hold' with a $90 price target, implying an upside of 61% from current levels.
- [Novo Nordisk Stock (NVO) Climbs 2% Today on Positive CagriSema Weight-Loss Data](https://www.tipranks.com/news/novo-nordisk-stock-nvo-climbs-2-today-on-positive-cagrisema-weight-loss-data)  
  <sub>TipRanks, 20 hours ago</sub>  
  Novo Nordisk NVO -1.06% ▽ stock scored an almost 2% rise on Tuesday after the pharmaceutical firm announced new data from its CagriSema weight-loss drug.
- [Novo Nordisk stock rises as CagriSema delivers 25% weight loss in women](https://invezz.com/ng/news/2026/10/20/novo-nordisk-stock-rises-as-cagrisema-delivers-25percent-weight-loss-in-women/)  
  <sub>Invezz, 21 hours ago</sub>  
  Novo Nordisk shares NVO rose on Tuesday after the Danish drugmaker reported that its experimental weight-loss drug CagriSema helped women with obesity or...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.60</summary>

_Not available today._

</details>

<details><summary><b>Price and chart</b> — score -0.25</summary>

```text
Last close 39.22 (bar of 2026-10-21), from 502 daily bars
Trend: vs 20d SMA 38.35 (+2.3%), 50d 42.20 (-7.1%), 200d 44.86 (-12.6%); 50d below 200d
Momentum: RSI(14) 46.5 | MACD -0.849 vs signal -1.262 (histogram 0.414)
Returns: 1d -0.3% | 5d +2.9% | 1m -0.4% | 3m -18.6%
52-week range: 35.29 - 63.98 (now 13.7% of the way up)
Volatility: ATR(14) 0.88 (2.2% of price) | annualised 20d 19.7%
Volume: 0.17x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.10</summary>

```text
Sector: Healthcare / Drug Manufacturers - General | market cap 173.10B
Valuation: trailing P/E 9.23 | forward P/E 11.44 | P/B 5.24 | PEG 4.32
Profitability: profit margin 35.3% | operating margin 42.5% | ROE 59.8%
Growth (YoY): revenue +2.1% | earnings -20.6%
Balance sheet: debt/equity 63.3% | free cash flow 37.67B
Risk: beta 0.38 | short interest 1.0% of float
Next earnings: 2026-11-04
```

</details>

<details><summary><b>What this fund holds</b> — score +0.10</summary>

_Not available today._

</details>

<details><summary><b>Does this company beat its own forecasts</b> — score +0.10</summary>

```text
Earnings record, last 4 quarters: 1 beat, 1 in line, 2 missed
  2026-06-30 missed by 6% | 2026-03-31 beat by 23% | 2025-12-31 in line | 2025-09-30 missed by 7%
```

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

```text
Consensus: hold (mean 2.71 on a 1=strong buy to 5=strong sell scale, 12 analysts)
Ratings: 0 strong buy, 3 buy, 10 hold, 1 sell, 0 strong sell
Price target: mean 45.22 (+15.3% vs last close), range 39.86 - 61.96
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

<details><summary><b>What analysts say about what this fund holds</b> — score +0.00</summary>

_Not available today._

</details>

<details><summary><b>Buying and selling by company insiders</b> — score +0.00</summary>

```text
Last 180 days: bought 0 shares in 0 transaction(s) | sold n/a shares in 0
Net: +0 shares | insiders hold 132,841 shares
Distinct insiders: 0 buying, 0 selling
```

</details>

<details><summary><b>Who is positioned how</b> — score +0.00</summary>

_Not available today._

</details>

<details><summary><b>Money going into and out of this fund</b> — score +0.00</summary>

_Not available today._

</details>

### JPMorgan Chase (JPM) · Company — BULLISH, confidence 0.50

**Result:** ACCEPTED · 15 shares · submitted buy 15 JPM @ ~334.19, stop 321.20

**In the model's own words:**

> moderate bullish view based on solid fundamentals, analyst buy consensus, and recent institutional buying, tempered by weak technicals and a recent earnings miss

**Main reasons it gave:**
- Analyst consensus buy with mean rating 2.04 and +11.5% price target
- Trailing P/E 14.0 and forward P/E 13.1 indicate reasonable valuation
- SteelPeak Wealth increased stake by 57.7% (institutional buying)
- Technical weakness: price below 20‑day SMA, low volume (0.14× 20‑day avg) and RSI 44

<details><summary><b>News</b> — score +0.10</summary>

- [JPMorgan Chase & Co. (JPM) stock price, news, quote and history](https://sg.finance.yahoo.com/quote/JPM/)  
  <sub>Yahoo Finance Singapore, 8 hours ago</sub>  
  JPMorgan Chase & Co. (JPM) · 1.16% · -4.12% · 5.76% · 4.05% · 10.88% · 96.24% · 6,580.46%. Key events. Baseline. Advanced chart. Loading chart...
- [JPMorgan Chase & Co. $JPM Stock: SteelPeak Wealth LLC Boosts Holdings](https://www.marketbeat.com/instant-alerts/filing-jpmorgan-chase-co-jpm-stock-steelpeak-wealth-llc-boosts-holdings-2026-10-21/)  
  <sub>MarketBeat, 6 hours ago</sub>  
  SteelPeak Wealth LLC raised its position in JPMorgan Chase & Co. (NYSE:JPM - Free Report) by 57.7% during the third quarter, according to the company in its...
- [Intel Stock Still Trades at 84 Times Earnings After a 35% Drop. I'm Not Buying Yet.](https://www.theglobeandmail.com/investing/markets/stocks/JPM/pressreleases/8275623/intel-stock-still-trades-at-84-times-earnings-after-a-35-drop-im-not-buying-yet/)  
  <sub>The Globe and Mail, 2 hours ago</sub>  
  Detailed price information for JP Morgan Chase & Company (JPM-N) from The Globe and Mail including charting and trades.
- [JPMorgan Chase & Co. $JPM Stock: BDF Gestion Reduces Holdings](https://www.marketbeat.com/instant-alerts/filing-jpmorgan-chase-co-jpm-stock-bdf-gestion-reduces-holdings-2026-10-21/)  
  <sub>MarketBeat, 7 hours ago</sub>  
  BDF Gestion cut its stake in shares of JPMorgan Chase & Co. (NYSE:JPM - Free Report) by 11.3% during the 3rd quarter, according to the company in its most...
- [JPM261016C00380000 Interactive Stock Chart | JPM Oct 2026 380.000 call Stock](https://finance.yahoo.com/chart/JPM261016C00380000)  
  <sub>Yahoo Finance, 4 hours ago</sub>  
  At Yahoo Finance, you get free stock quotes, up-to-date news, portfolio management resources, international market data, social interaction and mortgage...
- [JP Morgan and SIFMA flag gaps in SEC tokenized stock exemption](https://www.ledgerinsights.com/jp-morgan-and-sifma-flag-gaps-in-sec-tokenized-stock-exemption/)  
  <sub>Ledger Insights, 23 hours ago</sub>  
  The topic of the SEC Innovation Exemption for tokenized securities venues (TSVs) came up during SIFMA's annual conference today. JP Morgan's Eddie Wen.
- [JPMorgan Says One Big Headwind for Stocks May Be Fading](https://www.tradingview.com/news/gurufocus:59c44d176094b:0-jpmorgan-says-one-big-headwind-for-stocks-may-be-fading/)  
  <sub>TradingView, 23 hours ago</sub>  
  JPMorgan NYSE:JPM says the stock-market recovery could extend into year-end if global bond yields begin to stabilize, potentially easing the valuation...
- [JPMorgan Chase (NYSE:JPM) Share Price, Forecast & Analysis](https://stocksdownunder.com/company/jpmorgan-chase/)  
  <sub>Stocks Down Under, 19 hours ago</sub>  
  Explore JPMorgan Chase (NYSE:JPM) share price, stock analysis, financial performance, valuation and analyst price targets on Stocks Down Under.
- [JPMorgan Stocks Fall Although Its Security Initiative Reaches $2](https://www.gurufocus.com/news/9129937/jpmorgan-stocks-fall-although-its-security-initiative-reaches-230-billion)  
  <sub>GuruFocus, 23 hours ago</sub>  
  Diversified banking group JPMorgan (JPM) reported progress on its national-security investment push, while shares traded at $337.20, down approximately...
- [J.P. Morgan upgrades Luxshare: Buy target reaches RMB 97 for Luxshare stock](https://www.ad-hoc-news.de/boerse/news/corporate-news/j-p-morgan-upgrades-luxshare-buy-target-reaches-rmb-97-for-luxshare-stock/70380622)  
  <sub>AD HOC NEWS, 8 hours ago</sub>  
  First-half revenue rose 40.20 percent to CNY 174.50 billion. Luxshare stock reports results October 27 after CNY 7.84 billion profit.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.10</summary>

_Not available today._

</details>

<details><summary><b>Price and chart</b> — score -0.50</summary>

```text
Last close 334.02 (bar of 2026-10-21), from 502 daily bars
Trend: vs 20d SMA 334.31 (-0.1%), 50d 346.59 (-3.6%), 200d 322.47 (+3.6%); 50d above 200d
Momentum: RSI(14) 44.0 | MACD -2.969 vs signal -3.891 (histogram 0.922)
Returns: 1d -0.4% | 5d -0.4% | 1m -1.8% | 3m -4.5%
52-week range: 282.84 - 365.18 (now 62.2% of the way up)
Volatility: ATR(14) 6.49 (1.9% of price) | annualised 20d 14.6%
Volume: 0.14x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.30</summary>

```text
Sector: Financial Services / Banks - Diversified | market cap 887.02B
Valuation: trailing P/E 14.01 | forward P/E 13.08 | P/B 2.52 | PEG 1.57
Profitability: profit margin 34.6% | operating margin 42.6% | ROE 18.0%
Growth (YoY): revenue +10.2% | earnings +9.9%
Balance sheet: debt/equity n/a | free cash flow n/a
Risk: beta 1.01 | short interest 0.9% of float
Next earnings: 2027-01-14
```

</details>

<details><summary><b>What this fund holds</b> — score +0.30</summary>

_Not available today._

</details>

<details><summary><b>Does this company beat its own forecasts</b> — score +0.30</summary>

```text
Earnings record, last 4 quarters: 3 beats, 1 missed
  2026-09-30 missed by 7% | 2026-06-30 beat by 4% | 2026-03-31 beat by 8% | 2025-12-31 beat by 3%
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
Consensus: buy (mean 2.04 on a 1=strong buy to 5=strong sell scale, 23 analysts)
Ratings: 5 strong buy, 10 buy, 11 hold, 0 sell, 0 strong sell
Price target: mean 372.57 (+11.5% vs last close), range 312.00 - 425.00
Recent rating changes:
  - 2026-10-15 Citigroup: main, Neutral -> Neutral
  - 2026-10-14 Truist Securities: main, Hold -> Hold
  - 2026-10-14 Barclays: main, Overweight -> Overweight
  - 2026-10-14 RBC Capital: reit, Outperform -> Outperform
  - 2026-10-14 Morgan Stanley: main, Equal-Weight -> Equal-Weight
  - 2026-10-14 Baird: main, Neutral -> Neutral
Institutional ownership: 75.6%
Largest holders: Blackrock Inc. (7.8%), Vanguard Capital Management LLC (6.1%), State Street Corporation (4.7%), Bank of America Corporation (2.6%), Morgan Stanley (2.5%)
```

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score +0.50</summary>

_Not available today._

</details>

<details><summary><b>Buying and selling by company insiders</b> — score +0.00</summary>

```text
Last 180 days: bought 136,610 shares in 7 transaction(s) | sold 49,845 shares in 11
Net: +86,765 shares (+0.8% of insider holdings) | insiders hold 10,356,840 shares
Distinct insiders: 0 buying, 9 selling
Sales — weak evidence on their own; often scheduled 10b5-1 plans, tax on vesting, or diversification:
  - 2026-09-10 LEOPOLD ROBIN (Officer): 2,500 shares, 882.03K
  - 2026-08-11 LEOPOLD ROBIN (Officer): 2,500 shares, 903.52K
  - 2026-06-22 FRIEDMAN STACEY R. (General Counsel): 5,467 shares, 1.81M
  - 2026-05-20 FRIEDMAN STACEY R. (General Counsel): 5,468 shares, 1.64M
(7 grant/option/gift transaction(s) excluded — compensation, not a view on the price)
```

</details>

<details><summary><b>Who is positioned how</b> — score +0.00</summary>

_Not available today._

</details>

<details><summary><b>Money going into and out of this fund</b> — score +0.00</summary>

_Not available today._

</details>

### HDFC Bank (HDB) · Company — BULLISH, confidence 0.45

**Result:** ACCEPTED · 60 shares · submitted buy 60 HDB @ ~22.79, stop 21.65

**In the model's own words:**

> Mixed but slightly positive outlook: institutional buying and strong Q2 fundamentals offset weak technicals and high valuation.

**Main reasons it gave:**
- Robeco Institutional Asset Management increased its HDB stake by 13.1% (institutional purchase).
- HDFC Bank Q2 asset quality improved to 1.11% and net interest income rose 9.7% (positive earnings news).
- Technicals show low volume (0.18x 20‑day average) and price near 52‑week low, limiting downside risk.
- Fundamentals show strong YoY revenue growth (+80.8%) and earnings growth (+21.3%) with low beta (0.41).
- Analyst consensus remains Buy with a 33% price target upside.

<details><summary><b>News</b> — score +0.40</summary>

- [1,918,221 HDFC Bank Limited $HDB Shares Bought by Robeco Institutional Asset Management B.V.](https://www.marketbeat.com/instant-alerts/filing-1918221-hdfc-bank-limited-hdb-shares-bought-by-robeco-institutional-asset-management-bv-2026-10-21/)  
  <sub>MarketBeat, 5 hours ago</sub>  
  Robeco Institutional Asset Management B.V. boosted its position in HDFC Bank Limited (NYSE:HDB - Free Report) by 13.1% in the 3rd quarter, according to its...
- [Taking Stock: Nifty ends above 22,800 on late buying; Sensex sheds 143 points](https://www.tradingview.com/news/moneycontrol:c0840bbbc094b:0-taking-stock-nifty-ends-above-22-800-on-late-buying-sensex-sheds-143-points/)  
  <sub>TradingView, 4 hours ago</sub>  
  Indian benchmark indices remained under pressure for the second consecutive session on Wednesday, October 21, as selling across most sectors weighed on...
- [HDFC Bank stock: Asset quality improves to 1.11 percent in Q2 results](https://www.ad-hoc-news.de/boerse/news/corporate-news/hdfc-bank-stock-asset-quality-improves-to-1-11-percent-in-q2-results/70384938)  
  <sub>AD HOC NEWS, 45 minutes ago</sub>  
  Net interest income rose 9.70 percent in the September quarter. HDFC Bank stock costs EUR 20.30 on October 21, 2026 at 3:41 p.m. CEST.
- [Prologis (PLD) Stock Price Today, Live Chart & News](https://techgraph.co/stock-market/quote/pld/)  
  <sub>TechGraph, 6 hours ago</sub>  
  Prologis (PLD) stock price today: latest $127.47 (+3.04%) on NYSE. PLD share price, live chart, market cap, 52-week range, dividends and news on TechGraph.
- [Momentum Stocks: Transworld Shipping, Jeyyam Global Foods, Phantom Digital Effects jump up to 18% on sheer...](https://www.moneycontrol.com/news/business/markets/momentum-stocks-transworld-shipping-jeyyam-global-foods-phantom-digital-effects-jump-up-to-18-on-sheer-momentum-14056274.html)  
  <sub>Moneycontrol.com, 10 hours ago</sub>  
  Sobha, Muthoot Finance, PI Industries, Yes Bank, SJVN, GMDC, Jupiter Wagons, Trident, Swiggy, Reliance Power, Tube Investment, TVS Holdings,...
- [HDBank completes 1,501,582,896-share issue: what it means for HDBank stock](https://www.ad-hoc-news.de/boerse/news/corporate-news/hdbank-completes-1-501-582-896-share-issue-what-it-means-for-hdbank-stock/70382888)  
  <sub>AD HOC NEWS, 4 hours ago</sub>  
  Capital and earnings milestones. HDBank distributed 1,501,582,896 shares in a report dated October 19, 2026. First-half 2026 pretax profit reached VND...
- [Even The Cheapest 4-Room HDB Flats Aren't Cheap Anymore — One Statistic Reveals Just How Rare $500K Flats Are](https://stackedhomes.com/only-7-4-room-hdb-resale/)  
  <sub>Stacked Homes, 13 hours ago</sub>  
  Five years ago, two in three 4-room HDB resale flats sold under $500K. Now it's one in 15. We looked at what these flats are, where they are and the catch.
- [Jio Platforms IPO fully subscribed in 100 minutes; here's how top mega IPOs fared on Day 1](https://www.dtnext.in/news/business/jio-platforms-ipo-fully-subscribed-in-100-minutes-heres-how-top-mega-ipos-fared-on-day-1)  
  <sub>DT Next, 2 hours ago</sub>  
  Reliance Power, however, remains a notable exception -- having achieved full subscription within a minute of opening in 2008.
- [Piramal Finance shares jump 4% as Q2 profit rises 67% YoY to Rs 545 crore, NII jumps 35% YoY](https://m.economictimes.com/markets/stocks/news/piramal-finance-shares-jump-4-as-q2-profit-rises-67-yoy-to-rs-545-crore-nii-jumps-35-yoy/articleshow/135084284.cms)  
  <sub>The Economic Times, 8 hours ago</sub>  
  Piramal Finance shares rose nearly 4% after Q2 FY27 net profit surged 67% year-on-year to Rs 545 crore. Assets under management grew 24%, while retail...
- [Stock markets remain under pressure amid sellin…](https://www.uniindia.com/business-economy/stock-markets-remain-under-pressure-amid-selling-across-sectors/221020)  
  <sub>www.uniindia.com, 14 hours ago</sub>  
  New Delhi, Oct 21 (UNI) Indian stock markets on Wednesday remained under pressure throughout the session amid selling across most sectors.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.40</summary>

_Not available today._

</details>

<details><summary><b>Price and chart</b> — score -0.40</summary>

```text
Last close 22.74 (bar of 2026-10-21), from 502 daily bars
Trend: vs 20d SMA 22.68 (+0.2%), 50d 22.88 (-0.6%), 200d 26.21 (-13.2%); 50d below 200d
Momentum: RSI(14) 48.8 | MACD 0.045 vs signal -0.038 (histogram 0.083)
Returns: 1d -1.4% | 5d +0.5% | 1m -2.9% | 3m -1.7%
52-week range: 21.84 - 37.18 (now 5.8% of the way up)
Volatility: ATR(14) 0.57 (2.5% of price) | annualised 20d 29.1%
Volume: 0.18x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.30</summary>

```text
Sector: Financial Services / Banks - Regional | market cap 116.85B
Valuation: trailing P/E 14.67 | forward P/E 16.46 | P/B 9.12 | PEG n/a
Profitability: profit margin 26.5% | operating margin 38.5% | ROE 11.0%
Growth (YoY): revenue +80.8% | earnings +21.3%
Balance sheet: debt/equity n/a | free cash flow n/a
Risk: beta 0.41 | short interest 0.7% of float
Next earnings: 2027-01-16
```

</details>

<details><summary><b>What this fund holds</b> — score +0.30</summary>

_Not available today._

</details>

<details><summary><b>Does this company beat its own forecasts</b> — score +0.30</summary>

```text
Earnings record, last 4 quarters: 2 beats, 2 in line
  2026-06-30 in line | 2026-03-31 in line | 2025-12-31 beat by 61% | 2025-09-30 beat by 10%
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
Consensus: buy (mean 1.75 on a 1=strong buy to 5=strong sell scale, 4 analysts)
Ratings: 1 strong buy, 2 buy, 1 hold, 0 sell, 0 strong sell
Price target: mean 30.30 (+33.3% vs last close), range 26.20 - 33.00
Recent rating changes:
  - 2024-07-22 JP Morgan: down, Overweight -> Neutral
  - 2019-09-09 Bernstein: down, Outperform -> Market Perform
  - 2019-06-11 Nomura: down, Buy -> Neutral
  - 2017-03-21 Morgan Stanley: down, Overweight -> Equal-Weight
  - 2016-09-14 Goldman Sachs: main, ? -> Buy
  - 2015-03-11 Societe Generale: init, ? -> Buy
Institutional ownership: 13.8%
Largest holders: Morgan Stanley (1.0%), Royal Bank of Canada (0.8%), Schroder Investment Management Group (0.4%), JPMORGAN CHASE & CO (0.4%), Bank of America Corporation (0.3%)
```

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score +0.30</summary>

_Not available today._

</details>

<details><summary><b>Buying and selling by company insiders</b> — score +0.00</summary>

```text
Last 180 days: bought 0 shares in 0 transaction(s) | sold n/a shares in 0
Net: +0 shares | insiders hold 0 shares
Distinct insiders: 0 buying, 0 selling
```

</details>

<details><summary><b>Who is positioned how</b> — score +0.00</summary>

_Not available today._

</details>

<details><summary><b>Money going into and out of this fund</b> — score +0.00</summary>

_Not available today._

</details>

### MercadoLibre (MELI) · Company — NEUTRAL, confidence 0.40

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Mixed signals: bullish technicals and analyst view are offset by a weak earnings record, high valuation and modest insider buying, leading to a neutral stance with low conviction.

**Main reasons it gave:**
- Earnings record: 3 of last 4 quarters missed consensus
- Technical: price above 20d/50d/200d SMAs but volume only 0.14x 20‑day average
- Fundamentals: high valuation (trailing P/E 51.4) despite strong revenue growth (+49.8% YoY)
- Insider activity: small purchases (124 shares by officer, 600 shares by director) indicate mild confidence

<details><summary><b>News</b> — score +0.00</summary>

_No news found for this one today._

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

_Not available today._

</details>

<details><summary><b>Price and chart</b> — score +0.25</summary>

```text
Last close 1,889.53 (bar of 2026-10-21), from 502 daily bars
Trend: vs 20d SMA 1,814.97 (+4.1%), 50d 1,860.45 (+1.6%), 200d 1,828.95 (+3.3%); 50d above 200d
Momentum: RSI(14) 56.8 | MACD 9.236 vs signal 0.490 (histogram 8.746)
Returns: 1d +0.5% | 5d +2.7% | 1m +3.4% | 3m +5.0%
52-week range: 1,546.81 - 2,360.76 (now 42.1% of the way up)
Volatility: ATR(14) 53.60 (2.8% of price) | annualised 20d 41.1%
Volume: 0.14x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.10</summary>

```text
Sector: Consumer Cyclical / Internet Retail | market cap 95.79B
Valuation: trailing P/E 51.39 | forward P/E 33.60 | P/B 12.23 | PEG 1.00
Profitability: profit margin 5.3% | operating margin 6.7% | ROE 27.5%
Growth (YoY): revenue +49.8% | earnings -10.9%
Balance sheet: debt/equity 168.6% | free cash flow 353.38M
Risk: beta 1.31 | short interest 1.8% of float
Next earnings: 2026-11-04
```

</details>

<details><summary><b>What this fund holds</b> — score +0.10</summary>

_Not available today._

</details>

<details><summary><b>Does this company beat its own forecasts</b> — score +0.10</summary>

```text
Earnings record, last 4 quarters: 1 beat, 3 missed
  2026-06-30 beat by 4% | 2026-03-31 missed by 7% | 2025-12-31 missed by 6% | 2025-09-30 missed by 13%
```

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

```text
Consensus: buy (mean 1.62 on a 1=strong buy to 5=strong sell scale, 26 analysts)
Ratings: 4 strong buy, 16 buy, 6 hold, 0 sell, 0 strong sell
Price target: mean 2,270.01 (+20.1% vs last close), range 1,750.00 - 2,800.00
Recent rating changes:
  - 2026-10-13 Citigroup: main, Neutral -> Neutral
  - 2026-10-12 Cantor Fitzgerald: main, Overweight -> Overweight
  - 2026-10-06 Susquehanna: main, Positive -> Positive
  - 2026-09-03 BTIG: reit, Buy -> Buy
  - 2026-08-11 JP Morgan: main, Neutral -> Neutral
  - 2026-08-06 Cantor Fitzgerald: main, Overweight -> Overweight
Institutional ownership: 80.0%
Largest holders: Capital Research Global Investors (6.2%), BAILLIE GIFFORD & CO (6.0%), Capital International Investors (3.7%), Capital World Investors (3.5%), Morgan Stanley (2.9%)
```

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score +0.30</summary>

_Not available today._

</details>

<details><summary><b>Buying and selling by company insiders</b> — score +0.15</summary>

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

<details><summary><b>Who is positioned how</b> — score +0.15</summary>

_Not available today._

</details>

<details><summary><b>Money going into and out of this fund</b> — score +0.15</summary>

_Not available today._

</details>

**Data that was missing** (counted as 0.00, never guessed):
- news unavailable: Bright Data unreachable: The read operation timed out

### Procter & Gamble (PG) · Company — NEUTRAL, confidence 0.36

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Mixed signals: bullish technicals and analyst consensus offset by bearish fundamentals and neutral news. No material catalyst, so maintain a neutral stance with low conviction.

**Main reasons it gave:**
- Institutional investors (Quadrant Capital, Bank Pictet, Nisa Investment Advisors, Bell Bank) cut holdings – bearish sentiment but no material catalyst
- Price above 20‑day, 50‑day, 200‑day SMAs; RSI 68.2; MACD positive – bullish technicals
- High valuation (PEG 3.79) and YoY earnings decline (-15.5%) – bearish fundamentals
- Analyst consensus buy with modest +2.4% price target and recent upgrades – slight bullish

<details><summary><b>News</b> — score +0.00</summary>

- [What To Expect From Procter & Gamble’s (PG) Q3 Earnings](https://finance.yahoo.com/markets/stocks/articles/expect-procter-gamble-pg-q3-080639288.html)  
  <sub>Yahoo Finance, 7 hours ago</sub>  
  Consumer products behemoth Procter & Gamble (NYSE:PG) will be announcing earnings results this Thursday morning. Here's what to look for.
- [Procter & Gamble Company (The) $PG Stock Position Cut by Quadrant Capital Group LLC](https://www.marketbeat.com/instant-alerts/filing-procter-gamble-company-the-pg-stock-position-cut-by-quadrant-capital-group-llc-2026-10-21/)  
  <sub>MarketBeat, 3 hours ago</sub>  
  Quadrant Capital Group LLC lowered its holdings in shares of Procter & Gamble Company (The) (NYSE:PG - Free Report) by 5.0% in the 3rd quarter, according to...
- [P&G Q1 earnings on deck: Eyes on sales growth (PG:NYSE)](https://seekingalpha.com/news/4655172-pg-q1-earnings-on-deck-eyes-on-sales-growth)  
  <sub>Seeking Alpha, 17 minutes ago</sub>  
  P&G (PG) reports Q1 earnings Thursday—see EPS/revenue expectations, inflation and margin pressures, and analyst outlook.
- [The All-In Hosts Asked If the AI Trade Is Cracking. Here’s What Income Investors Should Do](https://247wallst.com/investing/2026/10/21/the-all-in-hosts-asked-if-the-ai-trade-is-cracking-heres-what-income-investors-should-do/)  
  <sub>24/7 Wall St., 2 hours ago</sub>  
  CoreWeave's bonds and stock are cratering, and the All-In hosts are asking out loud whether the entire AI trade is starting to crack.
- [2 Dividend Stocks to Buy and Hold Forever](https://www.theglobeandmail.com/investing/markets/stocks/PG/pressreleases/8275261/2-dividend-stocks-to-buy-and-hold-forever/)  
  <sub>The Globe and Mail, 2 hours ago</sub>  
  Multinational consumer goods manufacturer Procter & Gamble (NYSE: PG) has increased its dividend annually for 70 consecutive years.
- [Procter & Gamble Company (The) $PG Stock Position Lessened by Bank Pictet & Cie Europe AG](https://www.marketbeat.com/instant-alerts/filing-procter-gamble-company-the-pg-stock-position-lessened-by-bank-pictet-cie-europe-ag-2026-10-21/)  
  <sub>MarketBeat, 8 hours ago</sub>  
  Bank Pictet & Cie Europe AG lessened its position in shares of Procter & Gamble Company (The) (NYSE:PG - Free Report) by 33.1% in the third quarter,...
- [PG Oct 2026 167.500 call (PG261023C00167500) Stock Price, News, Quote & History](https://ca.finance.yahoo.com/quote/PG261023C00167500/)  
  <sub>Yahoo! Finance Canada, 4 hours ago</sub>  
  Find the latest PG Oct 2026 167.500 call (PG261023C00167500) stock quote, history, news and other vital information to help you with your stock trading and...
- [33,559 Procter & Gamble Company (The) $PG Shares Sold by Nisa Investment Advisors LLC](https://www.marketbeat.com/instant-alerts/filing-33559-procter-gamble-company-the-pg-shares-sold-by-nisa-investment-advisors-llc-2026-10-21/)  
  <sub>MarketBeat, 6 hours ago</sub>  
  Nisa Investment Advisors LLC decreased its position in Procter & Gamble Company (The) (NYSE:PG - Free Report) by 6.0% in the third quarter, according to its...
- [Procter & Gamble Company (The) $PG Holdings Cut by Bell Bank](https://www.marketbeat.com/instant-alerts/filing-procter-gamble-company-the-pg-holdings-cut-by-bell-bank-2026-10-21/)  
  <sub>MarketBeat, 4 hours ago</sub>  
  Bell Bank reduced its holdings in Procter & Gamble Company (The) (NYSE:PG - Free Report) by 28.8% during the third quarter, according to its most recent 13F...
- [Raymond James Names Top Household and Personal Care Stocks](https://finance.yahoo.com/markets/stocks/articles/raymond-james-names-top-household-070906312.html)  
  <sub>Yahoo Finance, 8 hours ago</sub>  
  Investing.com -- Raymond James has identified leading stocks in the household and personal care sector, which encompasses companies that manufacture and...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

_Not available today._

</details>

<details><summary><b>Price and chart</b> — score +0.30</summary>

```text
Last close 158.36 (bar of 2026-10-21), from 502 daily bars
Trend: vs 20d SMA 151.10 (+4.8%), 50d 147.63 (+7.3%), 200d 148.28 (+6.8%); 50d below 200d
Momentum: RSI(14) 68.2 | MACD 3.302 vs signal 2.356 (histogram 0.946)
Returns: 1d -0.6% | 5d +1.2% | 1m +6.8% | 3m +7.7%
52-week range: 138.04 - 167.20 (now 69.7% of the way up)
Volatility: ATR(14) 2.45 (1.5% of price) | annualised 20d 18.9%
Volume: 0.28x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score -0.20</summary>

```text
Sector: Consumer Defensive / Household & Personal Products | market cap 368.10B
Valuation: trailing P/E 23.92 | forward P/E 21.42 | P/B 6.90 | PEG 3.79
Profitability: profit margin 18.4% | operating margin 22.1% | ROE 30.3%
Growth (YoY): revenue +1.5% | earnings -15.5%
Balance sheet: debt/equity 64.5% | free cash flow 13.28B
Risk: beta 0.38 | short interest 1.1% of float
Next earnings: 2026-10-22
```

</details>

<details><summary><b>What this fund holds</b> — score -0.20</summary>

_Not available today._

</details>

<details><summary><b>Does this company beat its own forecasts</b> — score -0.20</summary>

```text
Earnings record, last 4 quarters: 4 in line
  2026-06-30 in line | 2026-03-31 in line | 2025-06-30 in line | 2025-03-31 in line
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

<details><summary><b>What analysts and big funds say</b> — score +0.20</summary>

```text
Consensus: buy (mean 2.16 on a 1=strong buy to 5=strong sell scale, 23 analysts)
Ratings: 5 strong buy, 8 buy, 12 hold, 0 sell, 0 strong sell
Price target: mean 162.13 (+2.4% vs last close), range 143.00 - 186.00
Recent rating changes:
  - 2026-10-20 RBC Capital: reit, Outperform -> Outperform
  - 2026-10-14 Citigroup: main, Buy -> Buy
  - 2026-10-06 Evercore ISI Group: up, In-Line -> Outperform
  - 2026-10-06 RBC Capital: main, Outperform -> Outperform
  - 2026-09-30 TD Cowen: reit, Hold -> Hold
  - 2026-08-07 Argus Research: down, Buy -> Hold
Institutional ownership: 71.9%
Largest holders: Blackrock Inc. (8.2%), Vanguard Capital Management LLC (6.6%), State Street Corporation (4.4%), Geode Capital Management, LLC (2.9%), Vanguard Portfolio Management LLC (2.7%)
```

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score +0.20</summary>

_Not available today._

</details>

<details><summary><b>Buying and selling by company insiders</b> — score +0.00</summary>

```text
Last 180 days: bought 156,293 shares in 42 transaction(s) | sold 48,751 shares in 16
Net: +107,542 shares (+5.3% of insider holdings) | insiders hold 2,138,478 shares
Distinct insiders: 0 buying, 10 selling
Sales — weak evidence on their own; often scheduled 10b5-1 plans, tax on vesting, or diversification:
  - 2026-10-05 GAMA PAUL (Officer): 2,225 shares, 323.38K
  - 2026-10-05 WHALEY SUSAN STREET (Officer): 2,369 shares, 344.31K
  - 2026-10-05 SCHULTEN ANDRE (Chief Financial Officer): 3,914 shares, 568.86K
  - 2026-08-24 JANZARUK MATTHEW W. (Officer): 359 shares, 52.14K
(40 grant/option/gift transaction(s) excluded — compensation, not a view on the price)
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

> Mixed signals: strong fundamentals and modestly bullish news are offset by bearish technicals, recent earnings misses, and no concrete catalyst. Overall view is neutral with low conviction.

**Main reasons it gave:**
- Price below 20‑day, 50‑day and 200‑day SMAs; RSI 38.4 (bearish technical)
- Trailing P/E 16.7, profit margin 54.8% and revenue growth 24% YoY (strong fundamentals)
- Earnings record: 2 beats, 2 misses; recent two quarters missed (mixed earnings)
- News: speculative AI leadership and earnings preview, no concrete catalyst (generic news)

<details><summary><b>News</b> — score +0.20</summary>

- [If Alphabet Does This on Oct. 28, the Stock Could Skyrocket](https://finance.yahoo.com/markets/stocks/articles/alphabet-does-oct-28-stock-111300411.html)  
  <sub>Yahoo Finance, 4 hours ago</sub>  
  Like many big tech companies, Alphabet (NASDAQ: GOOG) (NASDAQ: GOOGL) has had a lackluster year. It's only up about 7% for the year, but that figure was...
- [Fund Update: 34,907 GOOGLE (GOOGL) shares added to Quilter Plc portfolio](https://www.quiverquant.com/news/Fund+Update%3A+34%2C907+GOOGLE+%28GOOGL%29+shares+added+to+Quilter+Plc+portfolio)  
  <sub>Quiver Quantitative, 4 hours ago</sub>  
  Quilter Plc has added 34907 shares of $GOOGL to their portfolio, per a new SEC 13F filing. This dis.
- [Alphabet Deadline Alert: Levi & Korsinsky Reminds Alphabet Inc. (GOOGL/GOOG) Investors of Securities Class Action Deadline on December 1, 2026](https://www.morningstar.com/news/pr-newswire/20261021ny77197/alphabet-deadline-alert-levi-korsinsky-reminds-alphabet-inc-googlgoog-investors-of-securities-class-action-deadline-on-december-1-2026)  
  <sub>Morningstar, 33 minutes ago</sub>  
  Alphabet Deadline Alert: Levi & Korsinsky Reminds Alphabet Inc. (GOOGL/GOOG) Investors of Securities Class Action Deadline on December 1, 2026...
- [GOOGL Stock Rises After Gemini 4 Argon Launch, But JPMorgan Says Google Must Reclaim AI Leadership](https://stocktwits.com/news-articles/markets/equity/googl-stock-gemini-4-argon-launch-reclaim-leadership/cZD05VWRBip)  
  <sub>Stocktwits, 15 hours ago</sub>  
  GOOGL Stock Rises After Gemini 4 Argon Launch, But JPMorgan Says Google Must Reclaim AI Leadership · Nvidia-Backed Nebius Acquires Inferize To Reduce Idle GPU...
- [Alphabet: Q3 Is About Earning A Higher Multiple (NASDAQ:GOOGL)](https://seekingalpha.com/article/4955820-alphabet-q3-is-about-earning-a-higher-multiple)  
  <sub>Seeking Alpha, 4 hours ago</sub>  
  Alphabet shares have fallen nearly 16% from their May highs, even as Wall Street has raised its 2028 EPS estimates by almost 10%. I rate GOOGL stock as a...
- [GOOGL 261021 265.00C (GOOGL261021C265000) Stock Options Chain | Quotes & News](https://www.moomoo.com/options/GOOGL261021C265000-US)  
  <sub>Moomoo, 5 hours ago</sub>  
  Track real-time GOOGL 261021 265.00C (GOOGL261021C265000) stock options chain data and pricing information and news on moomoo App for your options trading...
- [Alphabet (GOOGL): Does Its Valuation Account for Waymo’s Potential?](https://finance.yahoo.com/markets/stocks/articles/alphabet-googl-does-valuation-account-134949535.html)  
  <sub>Yahoo Finance, 56 minutes ago</sub>  
  Alphabet Inc. (NASDAQ:GOOGL) can finance Waymo from a much larger advertising and cloud business. That gives it room to build autonomous transportation,...
- [GOOG, GOOGL Loss Notice: Alphabet Investors are Reminded of](https://www.globenewswire.com/news-release/2026/10/21/3385292/0/en/goog-googl-loss-notice-alphabet-investors-are-reminded-of-the-december-1-court-deadline-contact-bfa-law-if-you-lost-money.html)  
  <sub>GlobeNewswire, 5 hours ago</sub>  
  NEW YORK, Oct. 21, 2026 (GLOBE NEWSWIRE) -- Leading securities law firm Bleichmar Fonti & Auld LLP announces that a class action lawsuit has been filed...
- [The Stock Market is Flashing Several Warning Signs at Once. Does That Mean a Crash is Imminent?](https://www.theglobeandmail.com/investing/markets/stocks/GOOGL-Q/pressreleases/8279176/the-stock-market-is-flashing-several-warning-signs-at-once-does-that-mean-a-crash-is-imminent/)  
  <sub>The Globe and Mail, 11 minutes ago</sub>  
  Detailed price information for Alphabet Cl A (GOOGL-Q) from The Globe and Mail including charting and trades.
- [Alphabet Q3 Preview: Full-Stack AI Platform Positions Google Cloud For Solid Growth (GOOG)](https://seekingalpha.com/article/4955830-alphabet-q3-preview-full-stack-ai-platform-positions-google-cloud-for-solid-growth)  
  <sub>Seeking Alpha, 3 hours ago</sub>  
  Alphabet Inc. Strong Buy: full-stack AI + Google Cloud edge, $487 target. Click for this updated look at GOOG ahead of its Q3 earnings release.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.20</summary>

_Not available today._

</details>

<details><summary><b>Price and chart</b> — score -0.50</summary>

```text
Last close 332.01 (bar of 2026-10-21), from 502 daily bars
Trend: vs 20d SMA 345.04 (-3.8%), 50d 343.80 (-3.4%), 200d 341.26 (-2.7%); 50d above 200d
Momentum: RSI(14) 38.4 | MACD -0.994 vs signal 0.505 (histogram -1.498)
Returns: 1d -2.4% | 5d -4.5% | 1m -5.5% | 3m +4.5%
52-week range: 250.46 - 402.62 (now 53.6% of the way up)
Volatility: ATR(14) 8.63 (2.6% of price) | annualised 20d 19.6%
Volume: 0.51x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.60</summary>

```text
Sector: Communication Services / Internet Content & Information | market cap 4.06T
Valuation: trailing P/E 16.66 | forward P/E 21.63 | P/B 6.52 | PEG 1.25
Profitability: profit margin 54.8% | operating margin 34.0% | ROE 48.7%
Growth (YoY): revenue +24.2% | earnings +294.0%
Balance sheet: debt/equity 18.9% | free cash flow 22.67B
Risk: beta 1.21 | short interest 1.4% of float
Next earnings: 2026-10-28
```

</details>

<details><summary><b>What this fund holds</b> — score +0.60</summary>

_Not available today._

</details>

<details><summary><b>Does this company beat its own forecasts</b> — score +0.60</summary>

```text
Earnings record, last 4 quarters: 2 beats, 2 missed
  2026-06-30 missed by 4% | 2026-03-31 missed by 3% | 2025-12-31 beat by 4% | 2025-09-30 beat by 29%
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

<details><summary><b>What analysts and big funds say</b> — score +0.10</summary>

```text
Consensus: strong_buy (mean 1.38 on a 1=strong buy to 5=strong sell scale, 54 analysts)
Ratings: 13 strong buy, 43 buy, 5 hold, 0 sell, 0 strong sell
Price target: mean 430.33 (+29.6% vs last close), range 340.00 - 515.00
Recent rating changes:
  - 2026-10-20 BMO Capital: main, Outperform -> Outperform
  - 2026-10-19 Keybanc: main, Overweight -> Overweight
  - 2026-10-15 JP Morgan: main, Overweight -> Overweight
  - 2026-10-14 UBS: main, Neutral -> Neutral
  - 2026-10-12 Cantor Fitzgerald: reit, Overweight -> Overweight
  - 2026-10-08 Needham: reit, Buy -> Buy
Institutional ownership: 81.1%
Largest holders: Blackrock Inc. (7.9%), Vanguard Capital Management LLC (6.5%), FMR, LLC (4.3%), State Street Corporation (4.1%), Geode Capital Management, LLC (2.6%)
```

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score +0.10</summary>

_Not available today._

</details>

<details><summary><b>Buying and selling by company insiders</b> — score +0.00</summary>

```text
Last 180 days: bought 0 shares in 0 transaction(s) | sold n/a shares in 0
Net: +0 shares | insiders hold 195,313,088 shares
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

### Toyota (TM) · Company — NEUTRAL, confidence 0.35

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Mixed signals: negative news (recall, tariff‑related profit drop) offset by cheap valuation, bullish analyst consensus, and modest fundamentals; thin trading reduces confidence, leading to a neutral stance with low conviction.

**Main reasons it gave:**
- Recall of ~105,800 US vehicles over fire risk (negative news)
- Profit drop due to JPY 1.38 trillion tariff hit (negative news)
- Trailing P/E 8.60 indicates cheap valuation (positive fundamentals)
- Analyst consensus: 2 strong buy, 2 buy; mean price target +19.7% (positive analyst view)
- Daily volume at 0.12x 20‑day average (thin trading, technical caution)

<details><summary><b>News</b> — score -0.50</summary>

- [20,218 Toyota Motor Corporation $TM Shares Acquired by Quadrant Capital Group LLC](https://www.marketbeat.com/instant-alerts/filing-20218-toyota-motor-corporation-tm-shares-acquired-by-quadrant-capital-group-llc-2026-10-21/)  
  <sub>MarketBeat, 3 hours ago</sub>  
  Quadrant Capital Group LLC raised its position in shares of Toyota Motor Corporation (NYSE:TM - Free Report) by 87.6% during the 3rd quarter, according to...
- [A production line for mouth-dissolving strips has shipped to Texas; manufacturing has not begun.](https://www.stocktitan.net/news/RDTCF/rapid-dose-therapeutics-ships-quick-strip-tm-production-line-to-y2r8tcas30k6.html)  
  <sub>Stock Titan, 2 hours ago</sub>  
  Definitive operational arrangements and equipment qualification remain ahead; the global oral thin films market is projected to reach $7.95B by 2034.
- [Toyota to start Thai hydrogen Hilux production in 2027](https://finance.yahoo.com/energy/articles/toyota-start-thai-hydrogen-hilux-134010713.html)  
  <sub>Yahoo Finance, 1 hour ago</sub>  
  Toyota Motor plans to begin Thai manufacturing of a hydrogen fuel cell Hilux pickup in December 2027, with initial output intended for export.
- [Will Toyota Return To Earnings Growth In FY2027?](https://www.benzinga.com/Opinion/26/10/62483434/will-toyota-return-to-earnings-growth-in-fy2027)  
  <sub>Benzinga, 18 hours ago</sub>  
  Toyota Motor Corporation (NYSE:TM) (TYO:7203) delivered higher revenue in fiscal 2026, supported by increased vehicle sales and its extensive global...
- [Toyota to recall about 105,800 US vehicles over fire risk, NHTSA says By Reuters](https://www.investing.com/news/stock-market-news/toyota-to-recall-about-105800-us-vehicles-over-fire-risknhtsa-says-4961860)  
  <sub>Investing.com, 7 hours ago</sub>  
  Oct 21 (Reuters) - Toyota is recalling 105,794 vehicles in the US over a potential fuel leak that could raise the risk of fire if it reaches an ignition...
- [Joint drone demos and proposals are planned in the U.S. and Europe; projects remain subject to separate agreements.](https://www.stocktitan.net/news/CYCA/cytta-air-expands-growth-opportunities-with-qognifly-alliance-5w2yspsesegw.html)  
  <sub>Stock Titan, 12 minutes ago</sub>  
  Cytta Air (CYCA) announced a teaming agreement with Romania-based Qognifly Systems to pursue government and commercial opportunities in the United States...
- [(HBND) Trading Performance and Risk Management (HBND:CA)](https://news.stocktradersdaily.com/canada/hbnd-trading-performance-and-risk-management_20261020_5bc697)  
  <sub>Stock Traders Daily, 16 hours ago</sub>  
  Trading Performance Report for Hamilton U.S. Bond YIELD MAXIMIZER TM ETF (HBND) with Risk Management Strategies.
- [Toyota reports profit drop: JPY 1.38 trillion tariff hit weighs on Toyota Motor Corporation stock](https://www.ad-hoc-news.de/boerse/news/corporate-news/toyota-reports-profit-drop-jpy-1-38-trillion-tariff-hit-weighs-on-toyota/70380599)  
  <sub>AD HOC NEWS, 8 hours ago</sub>  
  Toyota revenue rose 5.5 percent to JPY 50.68 trillion in fiscal 2026. TM stock costs EUR 174.00 on October 21, 2026; fiscal 2027 guidance is JPY 51...
- [A treatment for children with a skin disease could gain UK approval about six weeks sooner.](https://www.stocktitan.net/news/INMB/i-nmune-bio-advances-ebstrocel-tm-toward-potential-uk-approval-in-vafqgqkg5pdc.html)  
  <sub>Stock Titan, 4 hours ago</sub>  
  INmune Bio submitted its final UK pre-application package Oct. 20; a U.S. license application is planned for Q2 2027, subject to FDA meeting feedback.
- [When the Price of (FMAX) Talks, People Listen (FMAX:CA)](https://news.stocktradersdaily.com/canada/when-the-price-of-fmax-talks,-people-listen_20261020_e81100)  
  <sub>Stock Traders Daily, 16 hours ago</sub>  
  Check the time stamp on this data. Updated Proprietary Signals for Hamilton U.S. Financials YIELD MAXIMIZER TM ETF (FMAX:CA) available here.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score -0.50</summary>

_Not available today._

</details>

<details><summary><b>Price and chart</b> — score -0.10</summary>

```text
Last close 195.63 (bar of 2026-10-21), from 502 daily bars
Trend: vs 20d SMA 187.94 (+4.1%), 50d 191.12 (+2.4%), 200d 199.59 (-2.0%); 50d below 200d
Momentum: RSI(14) 60.9 | MACD 1.187 vs signal -0.216 (histogram 1.402)
Returns: 1d -0.5% | 5d +3.7% | 1m +1.9% | 3m +10.7%
52-week range: 166.50 - 248.29 (now 35.6% of the way up)
Volatility: ATR(14) 3.00 (1.5% of price) | annualised 20d 21.0%
Volume: 0.12x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.20</summary>

```text
Sector: Consumer Cyclical / Auto Manufacturers | market cap 230.41B
Valuation: trailing P/E 8.60 | forward P/E 12.40 | P/B 15.75 | PEG n/a
Profitability: profit margin 8.6% | operating margin 7.9% | ROE 12.4%
Growth (YoY): revenue +10.4% | earnings +86.9%
Balance sheet: debt/equity 115.0% | free cash flow -3.60T
Risk: beta 0.38 | short interest 0.1% of float
Next earnings: 2026-11-05
```

</details>

<details><summary><b>What this fund holds</b> — score +0.20</summary>

_Not available today._

</details>

<details><summary><b>Does this company beat its own forecasts</b> — score +0.20</summary>

```text
Earnings record, last 4 quarters: 4 beats
  2026-06-30 beat by 44% | 2026-03-31 beat by 12% | 2025-12-31 beat by 27% | 2025-09-30 beat by 24%
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

<details><summary><b>What analysts and big funds say</b> — score +0.50</summary>

```text
Consensus: none (mean n/a on a 1=strong buy to 5=strong sell scale, 4 analysts)
Ratings: 2 strong buy, 2 buy, 0 hold, 0 sell, 0 strong sell
Price target: mean 234.08 (+19.7% vs last close), range 230.00 - 239.31
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

_No news found for this one today._

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>Price and chart</b> — score n/a</summary>

```text
Last close 1,669.29 (bar of 2026-10-21), from 502 daily bars
Trend: vs 20d SMA 1,748.65 (-4.5%), 50d 1,733.10 (-3.7%), 200d 1,584.64 (+5.3%); 50d above 200d
Momentum: RSI(14) 43.1 | MACD -23.123 vs signal -6.054 (histogram -17.069)
Returns: 1d +2.4% | 5d +1.2% | 1m -4.5% | 3m -7.4%
52-week range: 966.57 - 1,989.44 (now 68.7% of the way up)
Volatility: ATR(14) 52.77 (3.2% of price) | annualised 20d 30.0%
Volume: 0.37x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score n/a</summary>

```text
Sector: Technology / Semiconductor Equipment & Materials | market cap 643.37B
Valuation: trailing P/E 41.07 | forward P/E 26.62 | P/B 1,435.94 | PEG 1.58
Profitability: profit margin 34.1% | operating margin 44.4% | ROE 65.6%
Growth (YoY): revenue +55.2% | earnings +135.9%
Balance sheet: debt/equity 8.9% | free cash flow 10.37B
Risk: beta 1.30 | short interest 0.4% of float
Next earnings: 2026-10-14
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
Price target: mean 2,147.99 (+28.7% vs last close), range 868.67 - 2,853.54
Recent rating changes:
  - 2026-10-15 JP Morgan: main, Overweight -> Overweight
  - 2026-07-16 JP Morgan: main, Overweight -> Overweight
  - 2026-07-16 Wells Fargo: main, Overweight -> Overweight
  - 2026-07-16 RBC Capital: main, Outperform -> Outperform
  - 2026-07-14 RBC Capital: main, Outperform -> Outperform
  - 2026-07-06 Bernstein: main, Outperform -> Outperform
Institutional ownership: 20.3%
Largest holders: FMR, LLC (1.4%), Fisher Asset Management, LLC (1.2%), Capital World Investors (1.0%), Invesco Ltd. (0.8%), State Farm Mutual Automobile Insurance Co (0.7%)
```

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>Buying and selling by company insiders</b> — score n/a</summary>

```text
Last 180 days: bought 0 shares in 0 transaction(s) | sold n/a shares in 0
Net: +0 shares | insiders hold 1,702,666 shares
Distinct insiders: 0 buying, 0 selling
```

</details>

<details><summary><b>Who is positioned how</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>Money going into and out of this fund</b> — score n/a</summary>

_Not available today._

</details>

**Data that was missing** (counted as 0.00, never guessed):
- news unavailable: Bright Data unreachable: The read operation timed out

### Eli Lilly (LLY) · Company — no answer, no confidence given

<details><summary><b>News</b> — score n/a</summary>

- [LLY Stock Alert: What to Know as Eli Lilly Hits a New All-Time High](https://www.barchart.com/story/news/8276804/lly-stock-alert-what-to-know-as-eli-lilly-hits-a-new-all-time-high)  
  <sub>Barchart.com, 1 hour ago</sub>  
  Eli Lilly stock printed a new all-time high yesterday. Here's what has driven LLY shares higher and what comes next.
- [Investors Heavily Search Eli Lilly and Company (LLY): Here is What You Need to Know](https://finance.yahoo.com/markets/stocks/articles/investors-heavily-search-eli-lilly-120006393.html)  
  <sub>Yahoo Finance, 3 hours ago</sub>  
  Recently, Zacks.com users have been paying close attention to Lilly (LLY). This makes it worthwhile to examine what the stock has in store.
- [LLY Stock Hits All-Time High After Goldman Sachs Raises Price Target Ahead Of Q3 Earnings](https://stocktwits.com/news-articles/markets/equity/lly-stock-hits-new-record-eli-lilly-valuation-pushes-past-berkshire-hathaway-ahead-of-q3-earnings/cZxAGvFRBHP)  
  <sub>Stocktwits, 10 hours ago</sub>  
  Eli Lilly and Company (LLY) shares climbed to a record high in midday trade on Tuesday, pushing its market capitalization above Berkshire Hathaway's (BRK.
- [LLY Stock Hits New Record, Eli Lilly Valuation Pushes Past Berkshire Hathaway Ahead Of Q3 Earnings](https://es.tradingview.com/news/stocktwits:e68ed0d59094b:0-lly-stock-hits-new-record-eli-lilly-valuation-pushes-past-berkshire-hathaway-ahead-of-q3-earnings/)  
  <sub>TradingView, 22 hours ago</sub>  
  Eli Lilly and Company (LLY) shares climbed to a record high in midday trade on Tuesday, pushing its market capitalization above Berkshire Hathaway's (BRK.
- [SPY is up 0.5% today, on LLY stock price movement](https://www.quiverquant.com/news/SPY+is+up+0.5%25+today%2C+on+LLY+stock+price+movement)  
  <sub>Quiver Quantitative, 23 hours ago</sub>  
  $SPY stock has risen 0.5% today, according to our price data from Polygon. It has been bolstered by LLY stock rising 4.9%.
- [ETFs Are Net Sellers of Lilly (LLY) on Monday](https://finance.yahoo.com/markets/stocks/articles/etfs-net-sellers-lilly-lly-110320159.html)  
  <sub>Yahoo Finance, 4 hours ago</sub>  
  ETFs sold a net $15.5 million of Eli Lilly (LLY) on Oct. 19, with 15 sellers against 36 buyers.
- [Eli Lilly (LLY) Stock Hits New High at $1311.21 Ahead of Q3 Earnings](https://www.gurufocus.com/news/9132132/eli-lilly-lly-stock-hits-new-high-at-131121-ahead-of-q3-earnings)  
  <sub>GuruFocus, 23 hours ago</sub>  
  On October 20, 2026, Eli Lilly and Co (NYSE: LLY) shares surged to a fresh all-time high of $1311.21 during morning trading, surpassing the previous record...
- [Eli Lilly Gains 4.6% as Goldman Sachs Lifts Price Target to $1,413](https://www.tikr.com/blog/eli-lilly-gains-4-6-as-goldman-sachs-lifts-price-target-to-1413)  
  <sub>TIKR.com, 22 hours ago</sub>  
  Eli Lilly shares rose 4.6% today to a record high after Goldman Sachs raised its price target to $1,413 from $1,371 and kept its Buy rating.
- [Eli Lilly Rises 4% While Foundayo Nears European Approval; Amgen and Novo Nordisk Edge Higher](https://247wallst.com/investing/2026/10/20/eli-lilly-rises-4-while-foundayo-nears-european-approval-amgen-and-novo-nordisk-edge-higher/)  
  <sub>24/7 Wall St., 22 hours ago</sub>  
  Eli Lilly surged 4% after Europe's medicines committee recommended Foundayo for both obesity and diabetes, a wider label than any rival oral pill holds.
- [Is Eli Lilly (NYSE:LLY) Maintaining Its Presence in the Healthcare Sector?](https://kalkinemedia.com/us/stocks/healthcare/is-eli-lilly-nyselly-maintaining-its-presence-in-the-healthcare-sector)  
  <sub>Kalkine Media, 7 hours ago</sub>  
  Eli Lilly (NYSE:LLY) remains in focus as healthcare innovation and pharmaceutical research continue shaping the industry.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>Price and chart</b> — score n/a</summary>

```text
Last close 1,268.21 (bar of 2026-10-21), from 502 daily bars
Trend: vs 20d SMA 1,194.07 (+6.2%), 50d 1,183.54 (+7.2%), 200d 1,082.89 (+17.1%); 50d above 200d
Momentum: RSI(14) 65.4 | MACD 25.265 vs signal 13.571 (histogram 11.694)
Returns: 1d -1.2% | 5d +4.9% | 1m +8.4% | 3m +6.9%
52-week range: 799.57 - 1,283.66 (now 96.8% of the way up)
Volatility: ATR(14) 36.24 (2.9% of price) | annualised 20d 29.1%
Volume: 0.25x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score n/a</summary>

```text
Sector: Healthcare / Drug Manufacturers - General | market cap 1.13T
Valuation: trailing P/E 42.57 | forward P/E 26.86 | P/B 33.37 | PEG 1.14
Profitability: profit margin 33.5% | operating margin 54.2% | ROE 102.3%
Growth (YoY): revenue +47.7% | earnings +26.2%
Balance sheet: debt/equity 162.1% | free cash flow 11.07B
Risk: beta 0.45 | short interest 0.8% of float
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
Consensus: buy (mean 1.61 on a 1=strong buy to 5=strong sell scale, 30 analysts)
Ratings: 6 strong buy, 20 buy, 3 hold, 1 sell, 1 strong sell
Price target: mean 1,331.32 (+5.0% vs last close), range 930.00 - 1,600.00
Recent rating changes:
  - 2026-10-12 RBC Capital: reit, Outperform -> Outperform
  - 2026-10-08 Cantor Fitzgerald: main, Overweight -> Overweight
  - 2026-10-07 Morgan Stanley: main, Overweight -> Overweight
  - 2026-09-28 JP Morgan: main, Overweight -> Overweight
  - 2026-09-22 TD Cowen: reit, Buy -> Buy
  - 2026-09-18 Guggenheim: main, Buy -> Buy
Institutional ownership: 85.3%
Largest holders: Lilly Endowment, Inc (9.6%), Blackrock Inc. (7.2%), Vanguard Capital Management LLC (5.7%), PNC Financial Services Group, Inc. (5.5%), State Street Corporation (3.9%)
```

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>Buying and selling by company insiders</b> — score n/a</summary>

```text
Last 180 days: bought 1,467 shares in 28 transaction(s) | sold 308,215 shares in 8
Net: -306,748 shares (-18.0% of insider holdings) | insiders hold 1,390,517 shares
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

### Nvidia (NVDA) · Company — no answer, no confidence given

<details><summary><b>News</b> — score n/a</summary>

- [NVIDIA (NVDA) is Strengthening AI Conviction Balanced Against Evolving Competitive Risks](https://finance.yahoo.com/technology/ai/articles/nvidia-nvda-strengthening-ai-conviction-135925966.html)  
  <sub>Yahoo Finance, 44 minutes ago</sub>  
  L1 Capital, an investment management firm, released its “L1 Capital International Fund” (unhedged) third-quarter 2026 investor letter.
- [Nvidia Launches Containerized DSX Pod System To Accelerate AI Factory Deployments](https://www.tikr.com/blog/nvidia-nvda-stock-dsx-pod-ai-factory-containerized-system)  
  <sub>TIKR.com, 1 hour ago</sub>  
  Now Live: Discover how much upside your favorite stocks could have using TIKR's new Valuation Model (It's free)>>>. What Happened? Nvidia (NVDA)...
- [Dan Ives Calls the Selloff in NVDA Stock a Buying Opportunity as Analysts See 53% Upside](https://www.barchart.com/story/news/8270928/dan-ives-calls-the-selloff-in-nvda-stock-a-buying-opportunity-as-analysts-see-53-upside)  
  <sub>Barchart.com, 3 hours ago</sub>  
  Nvidia (NVDA) stock just took a hit. The share price fell approximately 5% in two trading sessions in mid-October. Risk of AI debt and rising borrowing...
- [Nine telecom operators are building or expanding NVIDIA-powered computing in Europe, the Middle East and Africa.](https://www.stocktitan.net/news/NVDA/nvidia-nokia-and-leading-telecom-operators-turn-networks-into-gnxh4cnobf67.html)  
  <sub>Stock Titan, 5 hours ago</sub>  
  NVIDIA (NVDA) announced expanded telecom adoption of its computing platforms, including infrastructure projects across nine operators in Europe,...
- [NVDA Stock Rides Massive AI Chip Orders And Global Partnerships](https://www.timothysykes.com/news/nvidia-corporation-nvda-news-2026_10_21/)  
  <sub>Timothy Sykes, 3 hours ago</sub>  
  NVIDIA Corporation stocks have been trading up by 2.02 percent amid bullish sentiment on accelerating AI chip demand. Key Takeaways For NVDA Traders SpaceX...
- [NVDA Stock Eyes ‘Beat-And-Raise’ Quarter Next Week As Microsoft, Amazon, SpaceX Fuel ‘Rock-Solid’ AI Demand](https://stocktwits.com/news-articles/markets/equity/nvda-earnings-rock-solid-ai-demand-bar-beat-and-raise-higher/cZYI0BfRJmL)  
  <sub>Stocktwits, 14 hours ago</sub>  
  The company expects comparable revenue to fall by a low-to-mid-single-digit percentage in the first quarter. Adjusted EBITDA is projected to decline by a low-...
- [NVIDIA Corporation $NVDA Stock: Angeles Wealth Management LLC Grows Stake](https://www.marketbeat.com/instant-alerts/filing-nvidia-corporation-nvda-stock-angeles-wealth-management-llc-grows-stake-2026-10-21/)  
  <sub>MarketBeat, 7 hours ago</sub>  
  Angeles Wealth Management LLC lifted its holdings in NVIDIA Corporation (NASDAQ:NVDA - Free Report) by 4.4% in the 2nd quarter, according to the company in...
- [Prediction: Nvidia’s Road to $1 Trillion in Annual Revenue Could Transform Its Stock](https://247wallst.com/investing/2026/10/21/prediction-nvidias-road-to-1-trillion-in-annual-revenue-could-transform-its-stock/)  
  <sub>24/7 Wall St., 13 minutes ago</sub>  
  NVIDIA's $108B quarterly guidance implies a $432B run rate, yet shares trade at just 16x forward earnings despite 105% revenue growth.
- [NVDA, ZM, SPCX Stocks Rise Premarket: Nvidia Announces AI Factory Pods, Zoom Gets Upgrade, SpaceX Target Rises](https://finance.yahoo.com/markets/stocks/articles/nvda-zm-spcx-stocks-rise-113149385.html)  
  <sub>Yahoo Finance, 3 hours ago</sub>  
  NVDA shares gain as its new DSX POD design aims to cut AI factory deployment times from six months to as little as 14 days. ZM stock rallies after...
- [NVIDIA says Vera Rubin systems handle 30 times more AI work per unit of power.](https://www.stocktitan.net/news/NVDA/nvidia-launches-open-shell-reference-architecture-for-safe-ai-kjnmhld3rvcd.html)  
  <sub>Stock Titan, 5 hours ago</sub>  
  NVIDIA (NVDA) launched the OpenShell Reference Architecture for building and governing AI agents across enterprise infrastructure and edge systems.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>Price and chart</b> — score n/a</summary>

```text
Last close 219.23 (bar of 2026-10-21), from 502 daily bars
Trend: vs 20d SMA 226.73 (-3.3%), 50d 222.95 (-1.7%), 200d 203.42 (+7.8%); 50d above 200d
Momentum: RSI(14) 44.6 | MACD -1.490 vs signal 0.507 (histogram -1.997)
Returns: 1d +1.3% | 5d -0.9% | 1m -4.2% | 3m +5.0%
52-week range: 165.17 - 239.24 (now 73.0% of the way up)
Volatility: ATR(14) 5.90 (2.7% of price) | annualised 20d 23.6%
Volume: 0.28x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score n/a</summary>

```text
Sector: Technology / Semiconductors | market cap 5.29T
Valuation: trailing P/E 27.72 | forward P/E 13.78 | P/B 23.12 | PEG 0.48
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
Earnings record, last 4 quarters: 4 beats
  2026-09-30 beat by 4% | 2026-09-30 beat by 4% | 2026-06-30 beat by 4% | 2026-06-30 beat by 4%
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
Consensus: strong_buy (mean 1.29 on a 1=strong buy to 5=strong sell scale, 59 analysts)
Ratings: 10 strong buy, 49 buy, 2 hold, 1 sell, 0 strong sell
Price target: mean 328.72 (+49.9% vs last close), range 180.00 - 515.00
Recent rating changes:
  - 2026-10-01 Cantor Fitzgerald: reit, Overweight -> Overweight
  - 2026-09-29 Rosenblatt: main, Buy -> Buy
  - 2026-09-10 Piper Sandler: init, ? -> Overweight
  - 2026-09-04 Rosenblatt: main, Buy -> Buy
  - 2026-09-04 Needham: reit, Buy -> Buy
  - 2026-08-27 Citigroup: main, Buy -> Buy
Institutional ownership: 71.4%
Largest holders: Blackrock Inc. (8.1%), Vanguard Capital Management LLC (6.4%), FMR, LLC (4.3%), State Street Corporation (4.2%), Geode Capital Management, LLC (2.5%)
```

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>Buying and selling by company insiders</b> — score n/a</summary>

```text
Last 180 days: bought 2,613,243 shares in 18 transaction(s) | sold 6,198,325 shares in 9
Net: -3,585,082 shares (-0.4% of insider holdings) | insiders hold 965,687,040 shares
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

### Royal Bank of Canada (RY) · Company — no answer, no confidence given

<details><summary><b>News</b> — score n/a</summary>

- [Royal Bank Of Canada $RY Stock Sold by QV Investors Inc.](https://www.marketbeat.com/instant-alerts/filing-royal-bank-of-canada-ry-stock-sold-by-qv-investors-inc-2026-10-21/)  
  <sub>MarketBeat, 5 hours ago</sub>  
  QV Investors Inc. cut its position in Royal Bank Of Canada (NYSE:RY - Free Report) (TSE:RY) by 13.2% in the 3rd quarter, according to its most recent...
- [AT&T (T) stock trades down, here is why](https://www.theglobeandmail.com/investing/markets/stocks/T/pressreleases/8279116/att-t-stock-trades-down-here-is-why/)  
  <sub>The Globe and Mail, 35 minutes ago</sub>  
  Shares of telecommunications conglomerate AT&T (NYSE:T) fell 6.6% in the pre-market session after the company reported third quarter results, with earnings...
- [Royal Bank of Canada stock rises Tuesday, outperforms market](https://www.marketwatch.com/data-news/royal-bank-of-canada-stock-rises-tuesday-outperforms-market-19b0517c-c1daeb289012?mod=mw_quote_news)  
  <sub>MarketWatch, 18 hours ago</sub>  
  Trading volume of 4.5 M shares eclipsed its 50-day average volume of 2.9 M. Editor's Note: This story was auto-generated by Automated Insights,...
- [RY Nov 2026 175.000 call (RY261120C00175000) Stock Price, News, Quote & History](https://ca.finance.yahoo.com/quote/RY261120C00175000/)  
  <sub>Yahoo! Finance Canada, 23 hours ago</sub>  
  Find the latest RY Nov 2026 175.000 call (RY261120C00175000) stock quote, history, news and other vital information to help you with your stock trading and...
- [Royal Bank of Canada (TSX:RY): High Net Income, Strong Profitability and Operational Efficiency Reinforce Long-Term Investment Potential](https://kalkine.ca/news/financial/royal-bank-of-canada-tsxry-high-net-income-strong-profitability-and-operational-efficiency-reinforce-long-term-investment-potential)  
  <sub>kalkine.ca, 6 hours ago</sub>  
  Royal Bank of Canada (TSX:RY): High Net Income, Strong Profitability and Operational Efficiency Reinforce Long-Term Investment Potential.
- [Royal Bank of Canada commits CAD 70 million while Royal Bank of Canada stock trades at EUR 178.18](https://www.ad-hoc-news.de/boerse/news/corporate-news/royal-bank-of-canada-commits-cad-70-million-while-royal-bank-of-canada-stock-trades-at-eur-178-18/70381998)  
  <sub>AD HOC NEWS, 6 hours ago</sub>  
  RBC targets 25000 entrepreneurs. Royal Bank of Canada stock costs EUR 178.18 on October 21, 2026 at a USD 276.0 billion valuation.
- [This Dividend Giant Just Hiked Its Payout By 7%](https://www.fool.ca/2026/10/20/this-dividend-giant-just-hiked-its-payout-by-7/)  
  <sub>The Motley Fool Canada, 15 hours ago</sub>  
  Royal Bank of Canada (TSX:RY) just keeps rewarding shareholders with generous dividend hikes.
- [Why Did Royal Bank of Canada (TSX:RY) Rise 0.959% on October 20, 2026?](https://kalkine.ca/news/financial/why-did-royal-bank-of-canada-tsxry-rise-0959-on-october-20-2026)  
  <sub>kalkine.ca, 53 minutes ago</sub>  
  You are reading a free article with opinions that may differ from the recommendation given by Kalkine in its paid research reports.
- [Why 3M Stock Jumped Today](https://www.theglobeandmail.com/investing/markets/stocks/NFLX/pressreleases/8238616/why-3m-stock-jumped-today/)  
  <sub>The Globe and Mail, 23 hours ago</sub>  
  Diversified industrial and materials-science company 3M(NYSE:MMM) is expanding its data center business, and that is helping its shares jump today.
- [History Says Micron Stock Gains 28% During the Fourth Quarter. Here's Why I Think Shares Will Surge Even More Before 2026 Is Over.](https://www.theglobeandmail.com/investing/markets/stocks/MU/pressreleases/8236983/history-says-micron-stock-gains-28-during-the-fourth-quarter-heres-why-i-think-shares-will-surge-even-more-before-2026-is-over/)  
  <sub>The Globe and Mail, 23 hours ago</sub>  
  Detailed price information for Micron Technology (MU-Q) from The Globe and Mail including charting and trades.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>Price and chart</b> — score n/a</summary>

```text
Last close 201.01 (bar of 2026-10-21), from 502 daily bars
Trend: vs 20d SMA 196.33 (+2.4%), 50d 202.80 (-0.9%), 200d 188.03 (+6.9%); 50d above 200d
Momentum: RSI(14) 55.6 | MACD -1.344 vs signal -2.428 (histogram 1.084)
Returns: 1d +1.0% | 5d +3.7% | 1m -1.4% | 3m -3.6%
52-week range: 145.41 - 217.87 (now 76.7% of the way up)
Volatility: ATR(14) 2.96 (1.5% of price) | annualised 20d 16.7%
Volume: 0.16x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score n/a</summary>

```text
Sector: Financial Services / Banks - Diversified | market cap 278.28B
Valuation: trailing P/E 17.57 | forward P/E 15.85 | P/B 2.93 | PEG 2.26
Profitability: profit margin 33.9% | operating margin 46.4% | ROE 16.2%
Growth (YoY): revenue +8.9% | earnings +12.8%
Balance sheet: debt/equity n/a | free cash flow n/a
Risk: beta 0.91 | short interest n/a of float
Next earnings: 2026-12-03
```

</details>

<details><summary><b>What this fund holds</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>Does this company beat its own forecasts</b> — score n/a</summary>

```text
Earnings record, last 4 quarters: 2 beats, 2 in line
  2026-09-30 in line | 2026-06-30 in line | 2026-03-31 beat by 3% | 2025-12-31 beat by 6%
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
Price target: mean 212.00 (+5.5% vs last close), range 185.04 - 233.18
Recent rating changes:
  - 2025-08-29 Argus Research: main, Buy -> Buy
  - 2024-12-05 BMO Capital: main, Outperform -> Outperform
  - 2024-08-29 BMO Capital: main, Outperform -> Outperform
  - 2024-06-06 Argus Research: main, Buy -> Buy
  - 2024-04-05 BMO Capital: up, Market Perform -> Outperform
  - 2023-12-18 B of A Securities: up, Neutral -> Buy
Institutional ownership: 49.4%
Largest holders: Royal Bank of Canada (5.1%), Bank of Montreal /CAN/ (4.4%), Vanguard Capital Management LLC (3.1%), FIL LTD (1.7%), TD Asset Management, Inc (1.7%)
```

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>Buying and selling by company insiders</b> — score n/a</summary>

```text
Last 180 days: bought 0 shares in 0 transaction(s) | sold n/a shares in 0
Net: +0 shares | insiders hold 373,796 shares
Distinct insiders: 1 buying, 0 selling
Open-market purchases — insiders spending their own money:
  - 2026-09-29 Royal Bank of Canada (Issuer): 200,000 shares, 39.94M
  - 2026-09-28 Royal Bank of Canada (Issuer): 200,000 shares, 40.29M
  - 2026-09-25 Royal Bank of Canada (Issuer): 200,000 shares, 40.24M
  - 2026-09-24 Royal Bank of Canada (Issuer): 200,000 shares, 39.86M
(101 grant/option/gift transaction(s) excluded — compensation, not a view on the price)
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

- [ExxonMobil (NYSE:XOM) Stock Rating Raised to "Strong-Buy" at Zacks Research](https://www.marketbeat.com/instant-alerts/analyst-exxonmobil-nyse-xom-stock-rating-raised-to-strong-buy-at-zacks-research-2026-10-21/)  
  <sub>MarketBeat, 4 hours ago</sub>  
  Zacks Research upgraded ExxonMobil from a "hold" rating to a "strong-buy" rating in a research report on Monday.
- [Which Dates Could Move Exxon Mobil Stock Most?](https://www.trefis.com/stock/xom/articles/619375/which-dates-could-move-exxon-mobil-stock-most/2026-10-20)  
  <sub>Trefis, 13 hours ago</sub>  
  Exxon Mobil (XOM) stock returned 65.8% over the past year, against 17.4% for the S&P 500, with the company drawing help from its markets.
- [Fund Update: New $14.0M $XOM stock position opened by Carnegie Investment Counsel](https://www.quiverquant.com/news/Fund+Update%3A+New+%2414.0M+%24XOM+stock+position+opened+by+Carnegie+Investment+Counsel)  
  <sub>Quiver Quantitative, 18 hours ago</sub>  
  Carnegie Investment Counsel has opened a new $14.0M position in $XOM, per a new SEC 13F filing. This.
- [What ExxonMobil Doubters Got Wrong](https://simplywall.st/stocks/us/energy/nyse-xom/exxonmobil-holdings/news/what-exxonmobil-doubters-got-wrong/amp)  
  <sub>Simply Wall Street, 15 hours ago</sub>  
  If ExxonMobil was on your watchlist rather than in your portfolio, the payoff over the last 12 months may feel like a near miss. Holding ExxonMobil over the...
- [ExxonMobil Corporation $XOM Stock: Prime Capital Investment Advisors LLC Increases Position](https://www.marketbeat.com/instant-alerts/filing-exxonmobil-corporation-xom-stock-prime-capital-investment-advisors-llc-increases-position-2026-10-21/)  
  <sub>MarketBeat, 6 hours ago</sub>  
  Prime Capital Investment Advisors LLC boosted its holdings in shares of ExxonMobil Corporation (NYSE:XOM - Free Report) by 4.0% during the 3rd quarter,...
- [Exxon Mobil (XOM) Shares Slip Amid Light Options Trading Ahead o](https://www.gurufocus.com/news/9132294/exxon-mobil-xom-shares-slip-amid-light-options-trading-ahead-of-earnings)  
  <sub>GuruFocus, 21 hours ago</sub>  
  On October 20, 2026, Exxon Mobil (XOM) saw its stock price decline by $1.21 to approximately $177.07, with subdued options activity signaling cautious...
- [ExxonMobil Hits a New All-Time High. Is It Too Late to Buy the Stock?](https://www.fool.com/investing/2026/10/20/exxonmobil-hits-a-new-all-time-high-is-it-too-late-to-buy-the-stock/)  
  <sub>The Motley Fool, 23 hours ago</sub>  
  Commodity prices are high, and so too are the valuations of many top oil and gas stocks. ExxonMobil (XOM -0.24%), which is a leading oil producer,...
- [Is Climbing Crude Drawing Focus to Exxon Mobil (NYSE:XOM)?](https://kalkinemedia.com/us/stocks/oil-gas/is-climbing-crude-drawing-focus-to-exxon-mobil-nysexom)  
  <sub>Kalkine Media, 10 hours ago</sub>  
  Exxon Mobil (NYSE:XOM) firmed as crude climbed on supply concerns, with its integrated model, Guyana output and Permian reach drawing eyes during earnings...
- [6,066 ExxonMobil Corporation $XOM Shares Sold by Provident Wealth Management LLC](https://www.marketbeat.com/instant-alerts/filing-6066-exxonmobil-corporation-xom-shares-sold-by-provident-wealth-management-llc-2026-10-21/)  
  <sub>MarketBeat, 5 hours ago</sub>  
  Provident Wealth Management LLC trimmed its position in shares of ExxonMobil Corporation (NYSE:XOM - Free Report) by 70.9% in the 3rd quarter, according to...
- [ExxonMobil (NYSE:XOM) Share Price, Forecast & Analysis](https://stocksdownunder.com/company/exxonmobil/)  
  <sub>Stocks Down Under, 20 hours ago</sub>  
  Explore ExxonMobil (NYSE:XOM) share price, stock analysis, financial performance, valuation and analyst price targets on Stocks Down Under.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>Price and chart</b> — score n/a</summary>

```text
Last close 178.03 (bar of 2026-10-21), from 502 daily bars
Trend: vs 20d SMA 168.91 (+5.4%), 50d 164.92 (+7.9%), 200d 152.55 (+16.7%); 50d above 200d
Momentum: RSI(14) 70.1 | MACD 4.368 vs signal 3.345 (histogram 1.023)
Returns: 1d +0.1% | 5d +0.6% | 1m +12.2% | 3m +13.5%
52-week range: 112.71 - 178.98 (now 98.6% of the way up)
Volatility: ATR(14) 3.54 (2.0% of price) | annualised 20d 17.3%
Volume: 0.21x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score n/a</summary>

```text
Sector: Energy / Oil & Gas Integrated | market cap 732.04B
Valuation: trailing P/E 22.91 | forward P/E 14.56 | P/B 2.82 | PEG 1.38
Profitability: profit margin 9.1% | operating margin 15.9% | ROE 12.6%
Growth (YoY): revenue +44.1% | earnings +112.8%
Balance sheet: debt/equity 15.9% | free cash flow 20.67B
Risk: beta 0.21 | short interest 1.1% of float
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
Consensus: buy (mean 2.40 on a 1=strong buy to 5=strong sell scale, 22 analysts)
Ratings: 3 strong buy, 6 buy, 16 hold, 0 sell, 0 strong sell
Price target: mean 179.41 (+0.8% vs last close), range 142.00 - 206.00
Recent rating changes:
  - 2026-10-19 Barclays: main, Overweight -> Overweight
  - 2026-10-15 Morgan Stanley: main, Overweight -> Overweight
  - 2026-10-01 Wells Fargo: down, Overweight -> Equal-Weight
  - 2026-09-28 TD Cowen: main, Buy -> Buy
  - 2026-09-03 Piper Sandler: main, Neutral -> Neutral
  - 2026-08-19 Morgan Stanley: main, Overweight -> Overweight
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

> Neutral overall – no macro surprise, technicals lack decisive break, flows flat, fundamentals mixed.

**Main reasons it gave:**
- Flat fund flows: 0% change in share count over week and month
- Technical: price below 20‑day SMA (28.12 vs 28.33) and 50‑day SMA (28.12 vs 28.51), RSI 41.9, MACD slightly negative
- Macro: Treasury yields down modestly, dollar index down 0.78%, VIX unchanged – no surprise
- Fund basics: 3.2% yield, 3‑year return +13.1% p.a., expense ratio 0.85% – mixed fundamentals

<details><summary><b>News</b> — score +0.00</summary>

- [Trump promises farmer bailout, cash payments ahead of midterms](https://seekingalpha.com/news/4654997-trump-farmer-relief-program-cash-payments-midterms)  
  <sub>Seeking Alpha, 8 hours ago</sub>  
  Trump promises voter relief before midterms: $8B farmer payments, $5K checks, Medicare support & fraud rewards.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.06% (-0.03 on the week) | 5-year 4.93% (-0.07 on the week) | 10-year 5.10% (-0.09 on the week) | 30-year 5.41% (-0.11 on the week)
Yield curve, 10-year minus 3-month: +1.04 points -- upward sloping (normal)
US dollar index: 101.77 (-0.78 on the week)
Volatility (VIX): 17.03 (+0.2 on the week) -- elevated
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 28.12 (bar of 2026-10-21), from 502 daily bars
Trend: vs 20d SMA 28.33 (-0.8%), 50d 28.51 (-1.4%), 200d 27.31 (+3.0%); 50d above 200d
Momentum: RSI(14) 41.9 | MACD -0.088 vs signal -0.061 (histogram -0.027)
Returns: 1d -0.2% | 5d -0.5% | 1m -1.5% | 3m -0.4%
52-week range: 25.44 - 29.49 (now 66.2% of the way up)
Volatility: ATR(14) 0.25 (0.9% of price) | annualised 20d 9.1%
Volume: 0.79x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.20</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score +0.20</summary>

```text
Fund type: Commodities Focused
What it holds: P/E n/a | P/B 0.00 | P/S 0.00 | 3y earnings growth n/a
Yield: 3.2%
Three-year record: +13.1% a year | beta to the market 0.35
Cost and size: expense ratio 0.85% | net assets 1.36B
What it is made of: Other 51.0%, Cash 47.0%, Bonds 2.0%
Largest holdings: Invesco Shrt-Trm Inv Gov&Agcy Instl 42.3%, Invesco Short Term Treasury ETF 4.6%
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
Rolled up from the 2 largest holdings, 46.9% of the fund by weight
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
Shares outstanding: 27.60M | fund size: 776.11M
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Commodities basket (DBC) · Index fund — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:** no explanation. It wrote only “NEUTRAL”, so the main reasons below are all it gave.

**Main reasons it gave:**
- Flat fund flows (0.0% change) indicating no net demand shift
- Technical trend above 20d, 50d, 200d SMAs but low volume (0.17x 20‑day average)
- Crude oil inventories draw of 8.6 million barrels (15th percentile) bullish for oil
- EIA forecast WTI price falling to $86 in six months, bearish outlook

<details><summary><b>News</b> — score +0.00</summary>

- [Commodity markets diverge as oil outpaces cracks in copper, gold - BofA (DBC:NYSEARCA)](https://seekingalpha.com/news/4654758-commodity-markets-diverge-as-oil-outpaces-cracks-in-copper-gold---bofa)  
  <sub>Seeking Alpha, 23 hours ago</sub>  
  Commodity markets (DBC) are splintering as surging Brent crude oil (BNO) (CO1:COM) targets multi-year highs, while copper (CPER) and gold (GLD) (XAUUSD:CUR)...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.06% (-0.03 on the week) | 5-year 4.93% (-0.07 on the week) | 10-year 5.10% (-0.09 on the week) | 30-year 5.41% (-0.11 on the week)
Yield curve, 10-year minus 3-month: +1.04 points -- upward sloping (normal)
US dollar index: 101.77 (-0.78 on the week)
Volatility (VIX): 17.03 (+0.2 on the week) -- elevated
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 33.49 (bar of 2026-10-21), from 502 daily bars
Trend: vs 20d SMA 32.96 (+1.6%), 50d 32.24 (+3.9%), 200d 28.86 (+16.0%); 50d above 200d
Momentum: RSI(14) 60.0 | MACD 0.392 vs signal 0.377 (histogram 0.015)
Returns: 1d -0.3% | 5d +0.5% | 1m +3.2% | 3m +10.5%
52-week range: 22.11 - 33.74 (now 97.8% of the way up)
Volatility: ATR(14) 0.47 (1.4% of price) | annualised 20d 14.4%
Volume: 0.17x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score -0.20</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score -0.20</summary>

```text
Fund type: Commodities Broad Basket
What it holds: P/E n/a | P/B 0.00 | P/S 0.00 | 3y earnings growth n/a
Yield: 2.3%
Three-year record: +14.9% a year | beta to the market 1.05
Cost and size: expense ratio 0.85% | net assets 1.92B
What it is made of: Other 50.4%, Cash 45.1%, Bonds 2.5%, Stocks 2.0%
Largest holdings: Invesco Shrt-Trm Inv Gov&Agcy Instl 41.5%, Brent Crude Future Dec 26 9.7%, Invesco Short Term Treasury ETF 5.8%, Mini Ibovespa Future Dec 26 2.0%
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
US inventories, week ending 2026-10-09 (published the following Wednesday)
  Crude oil: 415.6 million barrels, -8.6 on the week (a draw), 15% percentile over 52 weeks
  Natural gas: 3,567.0 billion cubic feet, +67.0 on the week (a build), 83% percentile over 52 weeks
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
Rolled up from the 4 largest holdings, 59.1% of the fund by weight
Ratings by weight: buy n/a | hold n/a | sell n/a (mean n/a on a 1=strong buy to 5=strong sell scale)
Weighted price target: n/a above the current prices
Holdings read: AGPXX, BRNG6, TBLL, WINZ26
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
Share count change: 1 week: +0.0% (0.00) over 7d | 1 month: +0.0% (0.00) over 33d
Shares outstanding: 111.40M | fund size: 3.73B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Developing country bonds (EMB) · Index fund — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Neutral overall; no macro surprise, mixed technicals, negative fund flows, moderate fundamentals.

**Main reasons it gave:**
- Fund flows negative: share count down -0.3% in a week and -11.5% in a month
- Technical indicators mixed: price below 50‑day and 200‑day SMA, RSI 44, MACD line above signal but low volume
- No macro surprise this week: yields down slightly, dollar down 0.78%, VIX stable
- Fund basics: yield 5.4% with credit quality spread across BBB (33.5%), BB (25.3%), B (19.5%)

<details><summary><b>News</b> — score +0.00</summary>

_No news found for this one today._

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.06% (-0.03 on the week) | 5-year 4.93% (-0.07 on the week) | 10-year 5.10% (-0.09 on the week) | 30-year 5.41% (-0.11 on the week)
Yield curve, 10-year minus 3-month: +1.04 points -- upward sloping (normal)
US dollar index: 101.77 (-0.78 on the week)
Volatility (VIX): 17.03 (+0.2 on the week) -- elevated
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 91.38 (bar of 2026-10-21), from 502 daily bars
Trend: vs 20d SMA 91.15 (+0.3%), 50d 93.03 (-1.8%), 200d 95.11 (-3.9%); 50d below 200d
Momentum: RSI(14) 44.0 | MACD -0.467 vs signal -0.629 (histogram 0.163)
Returns: 1d +0.2% | 5d +0.2% | 1m -2.5% | 3m -3.3%
52-week range: 90.14 - 97.74 (now 16.3% of the way up)
Volatility: ATR(14) 0.52 (0.6% of price) | annualised 20d 6.5%
Volume: 0.43x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.20</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score +0.20</summary>

```text
Fund type: Emerging Markets Bond
Yield: 5.4%
Credit quality: BBB 33.5%, BB 25.3%, B 19.5%, A 17.7% | US government debt 88.0%
Three-year record: +10.2% a year | beta to the market 1.10
Cost and size: expense ratio 0.39% | net assets 12.93B
What it is made of: Bonds 99.1%, Cash 0.9%
Largest holdings: BlackRock Cash Funds Treasury SL Agency 0.7%
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

<details><summary><b>Buying and selling by company insiders</b> — score -0.50</summary>

_Not available today._

</details>

<details><summary><b>Who is positioned how</b> — score -0.50</summary>

_Not available today._

</details>

<details><summary><b>Money going into and out of this fund</b> — score -0.50</summary>

```text
Direction: money going out (1 month)
Share count change: 1 week: -0.3% (-43.69M) over 7d | 1 month: -11.5% (-1.69B) over 32d
Shares outstanding: 141.80M | fund size: 12.96B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### US government bonds, 7-10 years (IEF) · Index fund — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> No strong macro surprise, technicals lack decisive break, fundamentals stable; slight bullish tilt from reduced short positioning and flight‑to‑quality news, but overall view remains neutral.

**Main reasons it gave:**
- 10-year Treasury yield down 9 bps this week
- CFTC data: net short on 10-year note fell 0.6% of open interest
- High‑yield vs investment‑grade spreads widened, indicating flight to quality
- IEF price above 20‑day SMA but below 50‑day and 200‑day SMA, low volume

<details><summary><b>News</b> — score +0.00</summary>

- [Investors are preferring high-yield bonds over riskier investment-grade](https://seekingalpha.com/news/4655189-investors-are-preferring-high-yield-bonds-over-riskier-investment-grade)  
  <sub>Seeking Alpha, 31 minutes ago</sub>  
  High-yield vs investment-grade bond spreads hit the widest since May 2025, signaling a flight to quality.
- [Daily ETF Flows: Chip ETFs Top the List](https://finance.yahoo.com/markets/options/articles/daily-etf-flows-chip-etfs-210004293.html)  
  <sub>Yahoo Finance, 18 hours ago</sub>  
  Here are the daily ETF fund flows for October 19, 2026.
- [TLT: The Refunding Could Break The Bond Bear, Again (NASDAQ:TLT)](https://seekingalpha.com/article/4955765-tlt-the-refunding-could-break-the-bond-bear-again)  
  <sub>Seeking Alpha, 6 hours ago</sub>  
  TLT's sell-off is driven by real yields and uncertainty, not inflation expectations, with the term premium at its highest since 2010. Read why TLT ETF is a...
- [Nomura's McElligott sees bond squeeze and AI jitters driving reversals (SHY:NASDAQ)](https://seekingalpha.com/news/4654821-nomuras-mcelligott-sees-bond-squeeze-and-ai-jitters-driving-reversals)  
  <sub>Seeking Alpha, 21 hours ago</sub>  
  Momentum unwind is sparking a “reverse dispersion” rally: bond-short squeeze + AI headwinds rotate flows into value (VTV) and small caps (IWM).

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.06% (-0.03 on the week) | 5-year 4.93% (-0.07 on the week) | 10-year 5.10% (-0.09 on the week) | 30-year 5.41% (-0.11 on the week)
Yield curve, 10-year minus 3-month: +1.04 points -- upward sloping (normal)
US dollar index: 101.77 (-0.78 on the week)
Volatility (VIX): 17.03 (+0.2 on the week) -- elevated
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 90.24 (bar of 2026-10-21), from 502 daily bars
Trend: vs 20d SMA 89.62 (+0.7%), 50d 91.15 (-1.0%), 200d 94.04 (-4.0%); 50d below 200d
Momentum: RSI(14) 50.5 | MACD -0.228 vs signal -0.445 (histogram 0.217)
Returns: 1d -0.0% | 5d +0.6% | 1m -1.0% | 3m -2.8%
52-week range: 88.92 - 97.99 (now 14.6% of the way up)
Volatility: ATR(14) 0.47 (0.5% of price) | annualised 20d 4.9%
Volume: 0.16x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.00</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score +0.00</summary>

```text
Fund type: Long Government
Yield: 4.1%
Credit quality: AA 100.0% | US government debt 99.7%
Three-year record: +4.2% a year | beta to the market 1.16
Cost and size: expense ratio 0.15% | net assets 41.56B
What it is made of: Bonds 99.7%, Cash 0.3%
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
Contract: UST 10Y NOTE - CHICAGO BOARD OF TRADE (positions as of 2026-10-13, published the following Friday)
Large speculators: net short 37.9% of open interest (5,819,512 contracts)
Change on the week: -0.6% of open interest
Crowding: 60% percentile over 52 weeks -- within its normal range
Read this as crowding, not as a forecast: an extreme is as often the end of a move as the middle of one.
```

</details>

<details><summary><b>Money going into and out of this fund</b> — score +0.00</summary>

```text
Direction: flat (1 month)
Share count change: 1 week: +0.0% (0.00) over 7d | 1 month: +0.0% (0.00) over 33d
Shares outstanding: 146.00M | fund size: 13.18B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### US small companies (IWM) · Index fund — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Neutral overall as no material macro surprise, modest analyst optimism offset by thin coverage and slight bearish positioning, fundamentals are unremarkable

**Main reasons it gave:**
- Analyst view: 100% buy rating on 2% of fund, price target +12% above current price
- CFTC positioning: net short 20.6% of open interest, increased 4.2% week over week
- Price below 20‑day, 50‑day, and 200‑day SMAs (276.51 vs 277.75, 287.49, 278.03)
- Macro yields unchanged, VIX stable at 17.03 (no surprise)

<details><summary><b>News</b> — score +0.00</summary>

_No news found for this one today._

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.06% (-0.03 on the week) | 5-year 4.93% (-0.07 on the week) | 10-year 5.10% (-0.09 on the week) | 30-year 5.41% (-0.11 on the week)
Yield curve, 10-year minus 3-month: +1.04 points -- upward sloping (normal)
US dollar index: 101.77 (-0.78 on the week)
Volatility (VIX): 17.03 (+0.2 on the week) -- elevated
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 276.51 (bar of 2026-10-21), from 502 daily bars
Trend: vs 20d SMA 277.75 (-0.4%), 50d 287.49 (-3.8%), 200d 278.03 (-0.5%); 50d above 200d
Momentum: RSI(14) 44.2 | MACD -3.620 vs signal -3.824 (histogram 0.204)
Returns: 1d +0.3% | 5d +1.9% | 1m -3.7% | 3m -5.3%
52-week range: 229.11 - 305.09 (now 62.4% of the way up)
Volatility: ATR(14) 3.74 (1.4% of price) | annualised 20d 14.6%
Volume: 0.19x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.00</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score +0.00</summary>

```text
Fund type: Small Blend
What it holds: P/E 16.35 | P/B 2.02 | P/S 1.25 | 3y earnings growth n/a
Yield: 1.0%
Three-year record: +18.5% a year | beta to the market 1.27
Cost and size: expense ratio 0.19% | net assets 78.04B
What it is made of: Stocks 99.7%, Cash 0.3%
Largest holdings: BlackRock Cash Funds Treasury SL Agency 0.5%, Twist Bioscience Corp 0.4%, Moog Inc Class A 0.4%, JFrog Ltd Ordinary Shares 0.4%, 10x Genomics Inc Ordinary Shares - Class A 0.4%
Sector mix: Healthcare 20.9%, Financial services 18.0%, Technology 14.5%, Industrials 13.3%
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
Rolled up from the 5 largest holdings, 2.0% of the fund by weight  -- thin, so read this as a fact about that slice rather than the fund
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 1.87 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +12.0% above the current prices
Holdings read: XTSLA, TWST, MOG-A, FROG, TXG
Recent rating changes among them:
  - TWST: 2026-10-13 TD Cowen: main, Buy -> Buy
  - MOG-A: 2026-10-13 JP Morgan: main, Overweight -> Overweight
  - FROG: 2026-10-21 Truist Securities: main, Buy -> Buy
  - TXG: 2026-10-13 TD Cowen: main, Hold -> Hold
```

</details>

<details><summary><b>Buying and selling by company insiders</b> — score -0.20</summary>

_Not available today._

</details>

<details><summary><b>Who is positioned how</b> — score -0.20</summary>

```text
Contract: RUSSELL E-MINI - CHICAGO MERCANTILE EXCHANGE (positions as of 2026-10-13, published the following Friday)
Large speculators: net short 20.6% of open interest (444,784 contracts)
Change on the week: +4.2% of open interest
Crowding: 22% percentile over 52 weeks -- within its normal range
Read this as crowding, not as a forecast: an extreme is as often the end of a move as the middle of one.
```

</details>

<details><summary><b>Money going into and out of this fund</b> — score -0.20</summary>

```text
Direction: flat (1 month)
Share count change: 1 week: +0.0% (0.00) over 7d | 1 month: +0.0% (0.00) over 32d
Shares outstanding: 281.05M | fund size: 77.71B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

**Data that was missing** (counted as 0.00, never guessed):
- news unavailable: Bright Data unreachable: The read operation timed out

### US company bonds, safer (LQD) · Index fund — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> No material macro surprise, policy shift, or decisive technical breakout observed. Treasury yields slipped modestly, high‑yield spreads widened (flight‑to‑quality signal), but fund flows are flat and technicals are mixed (price above short‑term SMA but below medium/long‑term SMAs, MACD line above signal on low volume). Overall evidence does not justify a bullish or bearish stance.

**Main reasons it gave:**
- 10‑year Treasury yield down 0.09% on the week to 5.10%
- High‑yield vs investment‑grade spreads widened to widest since May 2025
- Fund flows flat (share count unchanged) over past week and month
- Price above 20‑day SMA (+0.5%) but below 50‑day and 200‑day SMAs
- MACD line above signal (‑0.335 > ‑0.549) with low volume (0.26× 20‑day avg)

<details><summary><b>News</b> — score +0.00</summary>

- [Daily ETF Flows: Chip ETFs Top the List](https://finance.yahoo.com/markets/options/articles/daily-etf-flows-chip-etfs-210004293.html)  
  <sub>Yahoo Finance, 18 hours ago</sub>  
  Here are the daily ETF fund flows for October 19, 2026.
- [Investors are preferring high-yield bonds over riskier investment-grade](https://seekingalpha.com/news/4655189-investors-are-preferring-high-yield-bonds-over-riskier-investment-grade)  
  <sub>Seeking Alpha, 35 minutes ago</sub>  
  High-yield vs investment-grade bond spreads hit the widest since May 2025, signaling a flight to quality.
- [U.S. ETF Express | T-REX 2x Long BMNR Daily Target ETF Was the Top Gainer, Rising 11.78%](https://www.moomoo.com/news/post/1001768745/us-etf-express-t-rex-2x-long-bmnr-daily-target)  
  <sub>Moomoo, 18 hours ago</sub>  
  TopGainers/Losers4480 U.S. ETFs rose and 1610 fell today.The top gainer was $T-REX 2x Long BMNR Daily Target ETF(BMNU.US)$, climbing 11.78% to close at...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.06% (-0.03 on the week) | 5-year 4.93% (-0.07 on the week) | 10-year 5.10% (-0.09 on the week) | 30-year 5.41% (-0.11 on the week)
Yield curve, 10-year minus 3-month: +1.04 points -- upward sloping (normal)
US dollar index: 101.77 (-0.78 on the week)
Volatility (VIX): 17.03 (+0.2 on the week) -- elevated
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 103.11 (bar of 2026-10-21), from 502 daily bars
Trend: vs 20d SMA 102.61 (+0.5%), 50d 104.36 (-1.2%), 200d 107.91 (-4.5%); 50d below 200d
Momentum: RSI(14) 47.2 | MACD -0.335 vs signal -0.549 (histogram 0.214)
Returns: 1d -0.1% | 5d +0.4% | 1m -1.9% | 3m -3.0%
52-week range: 101.83 - 112.92 (now 11.5% of the way up)
Volatility: ATR(14) 0.61 (0.6% of price) | annualised 20d 5.7%
Volume: 0.26x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.00</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score +0.00</summary>

```text
Fund type: Corporate Bond
Yield: 4.9%
Credit quality: A 46.7%, BBB 40.5%, AA 11.9%, AAA 0.9%
Three-year record: +6.2% a year | beta to the market 1.35
Cost and size: expense ratio 0.14% | net assets 28.27B
What it is made of: Bonds 98.7%, Cash 1.3%, Convertible 0.0%
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
Direction: flat (1 month)
Share count change: 1 week: +0.0% (0.00) over 7d | 1 month: +0.0% (0.00) over 33d
Shares outstanding: 293.50M | fund size: 30.26B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### S&P 500, equal weight (RSP) · Index fund — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:** no explanation. It wrote only “NEUTRAL”, so the main reasons below are all it gave.

**Main reasons it gave:**
- Analyst coverage thin (1.4% of fund) but 78.5% buy rating, giving modest bullish bias
- CFTC data shows net short 21.2% with a small weekly increase, indicating slight bearish sentiment
- Technicals: price above 20‑, 50‑ and 200‑day SMAs and positive MACD, but volume at 0.29× 20‑day average
- Macro data: yields slipped slightly, dollar down, VIX unchanged; no surprise policy or data release

<details><summary><b>News</b> — score +0.00</summary>

- [Invesco S&P 500 Equal Weight (RSP) Sells $1.1 Million of Moderna on Monday](https://finance.yahoo.com/markets/stocks/articles/invesco-p-500-equal-weight-110430683.html)  
  <sub>Yahoo Finance, 4 hours ago</sub>  
  This article first appeared on GuruFocus. No ETFs were buying versus selling in the latest filing Invesco S&P 500 Equal Weight ETF (RSP) was a pure seller...
- [3 Great Broad-Market ETFs That Are Not Market-Weighted](https://www.morningstar.com/funds/3-great-broad-market-etfs-that-are-not-market-weighted-2)  
  <sub>Morningstar, 5 hours ago</sub>  
  As mega-cap tech stocks play a growing role in broad-market indexes, investors may consider alternative sources to diversify better.
- [The Semiconductor Selloff May Be About To Accelerate](https://mottcapitalmanagement.com/the-semiconductor-selloff-may-be-about-to-accelerate/)  
  <sub>Mott Capital Management, 17 hours ago</sub>  
  Markets were fairly boring again today, with little happening on the surface but plenty happening beneath. The RSP outperformed the SPY, pushing the...
- [Michael Burry Sees a 2000-Style Rotation Out of the Market's Winners](https://www.tradingview.com/news/benzinga:e4af189c7094b:0-michael-burry-sees-a-2000-style-rotation-out-of-the-market-s-winners/)  
  <sub>TradingView, 23 hours ago</sub>  
  Michael Burry expects the next phase of the stock market to resemble the months after the dot-com peak in 2000, when the biggest winners fell hard and the...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.06% (-0.03 on the week) | 5-year 4.93% (-0.07 on the week) | 10-year 5.10% (-0.09 on the week) | 30-year 5.41% (-0.11 on the week)
Yield curve, 10-year minus 3-month: +1.04 points -- upward sloping (normal)
US dollar index: 101.77 (-0.78 on the week)
Volatility (VIX): 17.03 (+0.2 on the week) -- elevated
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 216.32 (bar of 2026-10-21), from 502 daily bars
Trend: vs 20d SMA 211.98 (+2.1%), 50d 215.53 (+0.4%), 200d 207.06 (+4.5%); 50d above 200d
Momentum: RSI(14) 59.5 | MACD 0.284 vs signal -0.458 (histogram 0.742)
Returns: 1d +0.2% | 5d +2.0% | 1m +1.7% | 3m +2.1%
52-week range: 182.18 - 222.77 (now 84.1% of the way up)
Volatility: ATR(14) 1.95 (0.9% of price) | annualised 20d 9.9%
Volume: 0.29x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.00</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score +0.00</summary>

```text
Fund type: Large Blend
What it holds: P/E 20.26 | P/B 2.97 | P/S 1.87 | 3y earnings growth n/a
Yield: 1.5%
Three-year record: +17.3% a year | beta to the market 0.84
Cost and size: expense ratio 0.20% | net assets 96.06B
What it is made of: Stocks 99.9%, Cash 0.1%
Largest holdings: Moderna Inc 0.3%, Everpure Inc Class A 0.3%, Illumina Inc 0.3%, CrowdStrike Holdings Inc Class A 0.3%, Revvity Inc 0.3%
Sector mix: Technology 18.0%, Industrials 15.2%, Financial services 13.5%, Healthcare 12.6%
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
Rolled up from the 5 largest holdings, 1.4% of the fund by weight  -- thin, so read this as a fact about that slice rather than the fund
Ratings by weight: buy 78.5% | hold 21.5% | sell 0.0% (mean 2.20 on a 1=strong buy to 5=strong sell scale)
Weighted price target: -10.2% above the current prices
Holdings read: MRNA, P, ILMN, CRWD, RVTY
Recent rating changes among them:
  - MRNA: 2026-10-15 Goldman Sachs: main, Neutral -> Neutral
  - P: 2026-10-12 Guggenheim: main, Buy -> Buy
  - ILMN: 2026-10-19 Canaccord Genuity: main, Hold -> Hold
  - CRWD: 2026-10-16 Keybanc: main, Overweight -> Overweight
  - RVTY: 2026-10-13 TD Cowen: main, Buy -> Buy
```

</details>

<details><summary><b>Buying and selling by company insiders</b> — score -0.10</summary>

_Not available today._

</details>

<details><summary><b>Who is positioned how</b> — score -0.10</summary>

```text
Contract: E-MINI S&P 500 - CHICAGO MERCANTILE EXCHANGE (positions as of 2026-10-13, published the following Friday)
Large speculators: net short 21.2% of open interest (1,931,607 contracts)
Change on the week: +0.3% of open interest
Crowding: 35% percentile over 52 weeks -- within its normal range
Read this as crowding, not as a forecast: an extreme is as often the end of a move as the middle of one.
```

</details>

<details><summary><b>Money going into and out of this fund</b> — score -0.10</summary>

```text
Direction: flat (1 month)
Share count change: 1 week: +0.0% (0.00) over 7d | 1 month: +0.0% (0.00) over 33d
Shares outstanding: 155.55M | fund size: 33.65B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### US government bonds, 1-3 years (SHY) · Index fund — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> No macro surprise, no decisive technical break, modest bullish shift in positioning, fundamentals unchanged

**Main reasons it gave:**
- Treasury yields slipped modestly across the curve (3‑month -0.03, 10‑year -0.09) with no surprise
- Price $81.30 is just above 20‑day SMA (+0.1%) but below 50‑day and 200‑day SMAs; RSI 50.4, low volume
- CFTC shows net short 30% of OI, but short position decreased 2% of OI this week
- Fund basics unchanged: yield 3.6%, AA credit quality, 3‑year return +4% per year

<details><summary><b>News</b> — score +0.00</summary>

- [Yardeni’s Meter Sees AI Bubble, But No Burst Yet — Only 9% Of Similar Cases Saw A Bear Market Within 2 Years](https://www.tradingview.com/news/stocktwits:218a1eab1094b:0-yardeni-s-meter-sees-ai-bubble-but-no-burst-yet-only-9-of-similar-cases-saw-a-bear-market-within-2-years/)  
  <sub>TradingView, 1 hour ago</sub>  
  Yardeni Research's new artificial intelligence (AI) Bubble Meter suggests an AI stock market bubble exists, but the forces that historically ended major...
- [XRP Price Analysis: XRP Just Bounced 4% Off Its Low. Can It Break Back Above $1.40?](https://247wallst.com/investing/cryptocurrency/2026/10/21/xrp-price-analysis-xrp-just-bounced-4-off-its-low-can-it-break-back-above-1-40/)  
  <sub>24/7 Wall St., 5 minutes ago</sub>  
  XRP just posted its biggest single-day gain among major cryptocurrencies, but a stubborn ceiling has crushed every rally attempt in 2026 and institutional...
- [Paying a Grandchild’s Tuition at 71? Every Payment Comes Out of a Portfolio That Still Has to Last. These 3 ETFs Fund It on a Schedule](https://finance.yahoo.com/markets/options/articles/paying-grandchild-tuition-71-every-210323093.html)  
  <sub>Yahoo Finance, 18 hours ago</sub>  
  SHY, SPYM, and SPMD each hold tuition money based on when the bill comes due, moving funds from growth to safety as dates near. Paying tuition directly to...
- [Oil Prices Hit $110 Amid Fiscal Gridlock! French Debt Risk Premium Hits 15-Year High, Is a New "European Debt Crisis" Looming?](https://news.futunn.com/en/post/1001802794/oil-prices-hit-110-amid-fiscal-gridlock-french-debt-risk)  
  <sub>富途牛牛, 4 hours ago</sub>  
  Asrising energy prices have intensified pessimistic concerns about France's fiscal outlook, the gauge of risk for French government bonds has reached a...
- [Nomura's McElligott sees bond squeeze and AI jitters driving reversals (SHY:NASDAQ)](https://seekingalpha.com/news/4654821-nomuras-mcelligott-sees-bond-squeeze-and-ai-jitters-driving-reversals)  
  <sub>Seeking Alpha, 21 hours ago</sub>  
  A loss of legacy cross-asset momentum is driving a “reverse dispersion” rally across global markets, as a squeeze in short bond (SHY) (TLT) positions and AI...
- [Vanguard's All-World ETF Grinds Higher as Tokyo Exports and Wall Street Calm Override AI Jitters](https://www.ad-hoc-news.de/boerse/news/unternehmensnachrichten/vanguard-s-all-world-etf-grinds-higher-as-tokyo-exports-and-wall-street-calm-override-ai-jitters/70382884)  
  <sub>AD HOC NEWS, 5 hours ago</sub>  
  Vanguard FTSE All-World ETF edged up 0.3% to 170.94 euros as a 16.7% jump in Japanese exports and a 3.3% Kospi gain steadied the fund after a tech selloff.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.06% (-0.03 on the week) | 5-year 4.93% (-0.07 on the week) | 10-year 5.10% (-0.09 on the week) | 30-year 5.41% (-0.11 on the week)
Yield curve, 10-year minus 3-month: +1.04 points -- upward sloping (normal)
US dollar index: 101.77 (-0.78 on the week)
Volatility (VIX): 17.03 (+0.2 on the week) -- elevated
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 81.30 (bar of 2026-10-21), from 502 daily bars
Trend: vs 20d SMA 81.19 (+0.1%), 50d 81.49 (-0.2%), 200d 82.16 (-1.0%); 50d below 200d
Momentum: RSI(14) 50.4 | MACD -0.036 vs signal -0.077 (histogram 0.041)
Returns: 1d +0.0% | 5d +0.2% | 1m -0.0% | 3m -0.6%
52-week range: 81.05 - 83.18 (now 11.7% of the way up)
Volatility: ATR(14) 0.11 (0.1% of price) | annualised 20d 1.2%
Volume: 0.12x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.00</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score +0.00</summary>

```text
Fund type: Short Government
Yield: 3.6%
Credit quality: AA 100.0% | US government debt 99.5%
Three-year record: +4.0% a year | beta to the market 0.24
Cost and size: expense ratio 0.15% | net assets 26.28B
What it is made of: Bonds 99.5%, Cash 0.5%
Largest holdings: BlackRock Cash Funds Treasury SL Agency 1.4%
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
Contract: UST 2Y NOTE - CHICAGO BOARD OF TRADE (positions as of 2026-10-13, published the following Friday)
Large speculators: net short 30.0% of open interest (4,554,153 contracts)
Change on the week: -2.0% of open interest
Crowding: 87% percentile over 52 weeks -- within its normal range
Read this as crowding, not as a forecast: an extreme is as often the end of a move as the middle of one.
```

</details>

<details><summary><b>Money going into and out of this fund</b> — score +0.10</summary>

```text
Direction: flat (1 month)
Share count change: 1 week: +0.0% (0.00) over 7d | 1 month: +0.0% (0.00) over 33d
Shares outstanding: 209.30M | fund size: 17.02B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### US inflation-linked bonds (TIP) · Index fund — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Neutral stance based on mixed macro, technical, and positioning signals with no material catalyst.

**Main reasons it gave:**
- US Treasury yields fell slightly across the curve (no surprise)
- High-yield vs investment-grade spreads widened, indicating flight to quality
- Technicals show mixed signals: price near lower 52‑week range, MACD bullish but price below 200‑day SMA
- Positioning shows net short 37.9% with minimal weekly change, indicating moderate bearish sentiment but no shift

<details><summary><b>News</b> — score +0.00</summary>

- [Investors are preferring high-yield bonds over riskier investment-grade](https://seekingalpha.com/news/4655189-investors-are-preferring-high-yield-bonds-over-riskier-investment-grade)  
  <sub>Seeking Alpha, 33 minutes ago</sub>  
  High-yield vs investment-grade bond spreads hit the widest since May 2025, signaling a flight to quality.
- [FMPG ETF Holdings List — TSX:FMPG](https://www.tradingview.com/symbols/TSX-FMPG/holdings/)  
  <sub>TradingView, 17 hours ago</sub>  
  Explore Fidelity Global Growth Portfolio ETF Series units Trust Units holdings with weight, market value, and other helpful data to make more informed...
- [2 High-Yield Goldman Sachs ETFs Paying over 8% in Passive Income](https://www.tipranks.com/news/2-high-yield-goldman-sachs-etfs-paying-over-8-in-passive-income)  
  <sub>TipRanks, 1 hour ago</sub>  
  For investors seeking regular income, Goldman Sachs ($GS) offers two premium income ETFs: the Goldman Sachs Nasdaq 100 Core Premium Income ETF ($GPIQ) and...
- [‘It’s definitely a bubble’: Paul Musson warns AI investors on ‘Zero Sum’](https://invezz.com/uk/news/2026/10/21/its-definitely-a-bubble-paul-musson-warns-ai-investors-on-zero-sum/)  
  <sub>Invezz, 3 hours ago</sub>  
  The US national debt has climbed to $40 trillion, but the bigger question is what decades of borrowing, low interest rates, and rising asset prices have...
- [These 3 ETFs Could Deliver 11%+ Gains, AI Analyst Says](https://www.tipranks.com/news/these-3-etfs-could-deliver-11-gains-ai-analyst-says)  
  <sub>TipRanks, 21 hours ago</sub>  
  Exchange-traded funds (ETFs) remain an important way to gain exposure to big companies' growth potential. For investors looking for an entry point,...
- [3 Best Vanguard ETFs with Low Fees and 21%+ Upside Potential](https://www.tipranks.com/news/3-best-vanguard-etfs-with-low-fees-and-21-upside-potential)  
  <sub>TipRanks, 23 hours ago</sub>  
  Low-cost ETFs can help investors build wealth over time, but some offer more upside potential than others. According to TipRanks' Vanguard ETFs tool,...
- [Institutional Nudge: Fidelity’s Ethereum ETF Draws Fresh Inflows as Price Rally Holds](https://www.tipranks.com/news/cryptocurrencies/institutional-nudge-fidelitys-ethereum-etf-draws-fresh-inflows-as-price-rally-holds)  
  <sub>TipRanks, 23 hours ago</sub>  
  Fidelity's Ethereum vehicle quietly pulled in fresh cash this week, underscoring growing institutional conviction in the sector. The Fidelity Ethereum Fund...
- [Thirteen option delistings on October 20th](https://www.tipranks.com/news/the-fly/thirteen-option-delistings-on-october-20th-thefly-news-2)  
  <sub>TipRanks, 23 hours ago</sub>  
  Option delistings effective October 20th include Themes Lithium & Battery Metal Miners ETF (LIMI), KEJPM Stock (KEJPM), KDJPM Stock (KDJPM),...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.06% (-0.03 on the week) | 5-year 4.93% (-0.07 on the week) | 10-year 5.10% (-0.09 on the week) | 30-year 5.41% (-0.11 on the week)
Yield curve, 10-year minus 3-month: +1.04 points -- upward sloping (normal)
US dollar index: 101.77 (-0.78 on the week)
Volatility (VIX): 17.03 (+0.2 on the week) -- elevated
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 105.54 (bar of 2026-10-21), from 502 daily bars
Trend: vs 20d SMA 104.59 (+0.9%), 50d 105.80 (-0.2%), 200d 108.99 (-3.2%); 50d below 200d
Momentum: RSI(14) 57.0 | MACD -0.074 vs signal -0.305 (histogram 0.231)
Returns: 1d +0.1% | 5d +0.7% | 1m -0.0% | 3m -1.8%
52-week range: 103.98 - 112.20 (now 19.0% of the way up)
Volatility: ATR(14) 0.39 (0.4% of price) | annualised 20d 3.9%
Volume: 0.23x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.00</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score +0.00</summary>

```text
Fund type: Inflation-Protected Bond
Yield: 4.7%
Credit quality: AA 100.0% | US government debt 100.0%
Three-year record: +4.3% a year | beta to the market 0.71
Cost and size: expense ratio 0.18% | net assets 14.23B
What it is made of: Bonds 100.0%
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
Contract: UST 10Y NOTE - CHICAGO BOARD OF TRADE (positions as of 2026-10-13, published the following Friday)
Large speculators: net short 37.9% of open interest (5,819,512 contracts)
Change on the week: -0.6% of open interest
Crowding: 60% percentile over 52 weeks -- within its normal range
Read this as crowding, not as a forecast: an extreme is as often the end of a move as the middle of one.
```

</details>

<details><summary><b>Money going into and out of this fund</b> — score +0.00</summary>

```text
Direction: flat (1 month)
Share count change: 1 week: +0.0% (0.00) over 7d | 1 month: +0.0% (0.00) over 33d
Shares outstanding: 177.70M | fund size: 18.75B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### US government bonds, 20+ years (TLT) · Index fund — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> No material macro surprise, technicals mixed, speculator positioning modestly bearish, fundamentals stable.

**Main reasons it gave:**
- News cites rising real yields and highest term premium since 2010, pressuring TLT
- 10-year Treasury yield fell 9 bps this week, supporting bond prices
- Large speculators net short 29.8% of open interest, indicating bearish sentiment but change only +0.4%
- Technical indicators mixed: price above 20‑day SMA but below 50‑day and 200‑day SMA; MACD bullish but low volume
- Fund fundamentals stable: AA‑rated US Treasuries, 5% yield, 99.6% bond holdings

<details><summary><b>News</b> — score +0.00</summary>

- [TLT: The Refunding Could Break The Bond Bear, Again (NASDAQ:TLT)](https://seekingalpha.com/article/4955765-tlt-the-refunding-could-break-the-bond-bear-again)  
  <sub>Seeking Alpha, 6 hours ago</sub>  
  TLT's sell-off is driven by real yields and uncertainty, not inflation expectations, with the term premium at its highest since 2010. Read why TLT ETF is a...
- [iShares 20+ Year Treasury Bond ETF (TLT)](https://ca.finance.yahoo.com/quote/TLT/options/?date=1793145600&straddle=false&type=all)  
  <sub>Yahoo! Finance Canada, 15 hours ago</sub>  
  View the basic TLT option chain and compare options of iShares 20+ Year Treasury Bond ETF on Yahoo Finance.
- [iShares 20+ Year Treasury Bond ETF seen as a bu...](https://pluang.com/en/news-feed/tlt-refunding-bisa-membalikkan-tren-bear-obligasi)  
  <sub>Pluang, 6 hours ago</sub>  
  The iShares 20+ Year Treasury Bond ETF (TLT) has declined about 5% in 2026, pressured by rising real yields and uncertainty rather than inflation fears.
- [iShares 20+ Year Treasury Bond ETF (TLT) Profile, Company FAQs & Facts, Industry, Sector, Employee Strength](https://stocktwits.com/symbol/TLT/about)  
  <sub>Stocktwits, 21 hours ago</sub>  
  About TLT. About. The iShares 20+ Year Treasury Bond ETF seeks to track an index that includes U.S. Treasury bonds with remaining maturities greater than twenty...
- [TLT 261021 71.00C (TLT261021C71000) Stock Options Chain | Quotes & News](https://www.moomoo.com/options/TLT261021C71000-US?chain_id=Name1K9-3FXPhg.1kgajc0)  
  <sub>Moomoo, 5 hours ago</sub>  
  Track real-time TLT 261021 71.00C (TLT261021C71000) stock options chain data and pricing information and news on moomoo App for your options trading and...
- [iShares 20+ Year Treasury Bond Tokenized ETF (Ondo) price today, TLTon to USD chart, marketcap and volume](https://cryptoslate.com/coins/ishares-20-year-treasury-bond-tokenized-etf-ondo/)  
  <sub>CryptoSlate, 2 hours ago</sub>  
  iShares 20+ Year Treasury Bond Tokenized ETF (Ondo) price is $80.34 on Oct 21, 2026. Market cap $17.93M; 24h volume $744.85K.
- [TLT 261021 92.00C (TLT261021C92000) Stock Options Chain | Quotes & News](https://www.moomoo.com/options/TLT261021C92000-US)  
  <sub>Moomoo, 5 hours ago</sub>  
  Track real-time TLT 261021 92.00C (TLT261021C92000) stock options chain data and pricing information and news on moomoo App for your options trading and...
- [S&P 500, Nasdaq Futures Pull Back After Trump Wants 'Couple Days To Think' About Iran Ceasefire Deal: ASTS, DELL, BB, SMCI In Focus](https://stocktwits.com/news-articles/markets/equity/sp500-nasdaq-futures-pull-back-after-trump-wants-couple-days-to-think-about-iran-ceasefire-deal/cZgS7tGRet0)  
  <sub>Stocktwits, 14 hours ago</sub>  
  According to a report from Axios, the U.S. and Iran have reached a tentative deal to extend the ceasefire between the two nations by 60 days and are on...
- [Daily ETF Flows: Chip ETFs Top the List](https://finance.yahoo.com/markets/options/articles/daily-etf-flows-chip-etfs-210004293.html)  
  <sub>Yahoo Finance, 18 hours ago</sub>  
  Here are the daily ETF fund flows for October 19, 2026.
- [The Bond ETFs That Belong in Your Portfolio, and Which Ones Require Extra Caution](https://www.morningstar.com/bonds/bond-etfs-that-belong-your-portfolio-which-ones-require-extra-caution)  
  <sub>Morningstar, 4 hours ago</sub>  
  Certain types of bond ETFs are better options to preserve wealth and generate income, while others are situationally useful, but investors need to be aware...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.06% (-0.03 on the week) | 5-year 4.93% (-0.07 on the week) | 10-year 5.10% (-0.09 on the week) | 30-year 5.41% (-0.11 on the week)
Yield curve, 10-year minus 3-month: +1.04 points -- upward sloping (normal)
US dollar index: 101.77 (-0.78 on the week)
Volatility (VIX): 17.03 (+0.2 on the week) -- elevated
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 80.13 (bar of 2026-10-21), from 502 daily bars
Trend: vs 20d SMA 78.55 (+2.0%), 50d 80.59 (-0.6%), 200d 84.84 (-5.5%); 50d below 200d
Momentum: RSI(14) 56.1 | MACD -0.202 vs signal -0.602 (histogram 0.400)
Returns: 1d +0.0% | 5d +1.6% | 1m -2.0% | 3m -3.7%
52-week range: 77.11 - 92.06 (now 20.2% of the way up)
Volatility: ATR(14) 0.79 (1.0% of price) | annualised 20d 10.4%
Volume: 0.16x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.00</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score +0.00</summary>

```text
Fund type: Long Government
Yield: 5.0%
Credit quality: AA 100.0% | US government debt 99.6%
Three-year record: +2.9% a year | beta to the market 2.31
Cost and size: expense ratio 0.15% | net assets 46.23B
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
Contract: ULTRA UST BOND - CHICAGO BOARD OF TRADE (positions as of 2026-10-13, published the following Friday)
Large speculators: net short 29.8% of open interest (2,397,995 contracts)
Change on the week: +0.4% of open interest
Crowding: 87% percentile over 52 weeks -- within its normal range
Read this as crowding, not as a forecast: an extreme is as often the end of a move as the middle of one.
```

</details>

<details><summary><b>Money going into and out of this fund</b> — score -0.10</summary>

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

> Neutral overall; no clear macro surprise, no decisive technical break, and mixed behavioural signals.

**Main reasons it gave:**
- Dollar index down 0.78% on the week (macro bearish for USD)
- UUP price near 52‑week high (92.9% of range) with low volume (0.08× 20‑day average)
- CFTC positioning shows modest net long increase (+2.3% OI) but high crowding (85th percentile)
- Fund inflows strong (+41.4% month) but technicals show limited upside

<details><summary><b>News</b> — score +0.00</summary>

_No news found for this one today._

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.06% (-0.03 on the week) | 5-year 4.93% (-0.07 on the week) | 10-year 5.10% (-0.09 on the week) | 30-year 5.41% (-0.11 on the week)
Yield curve, 10-year minus 3-month: +1.04 points -- upward sloping (normal)
US dollar index: 101.77 (-0.78 on the week)
Volatility (VIX): 17.03 (+0.2 on the week) -- elevated
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 28.94 (bar of 2026-10-21), from 502 daily bars
Trend: vs 20d SMA 28.92 (+0.1%), 50d 28.45 (+1.7%), 200d 27.86 (+3.9%); 50d above 200d
Momentum: RSI(14) 57.1 | MACD 0.147 vs signal 0.179 (histogram -0.032)
Returns: 1d +0.1% | 5d -0.6% | 1m +1.6% | 3m +1.3%
52-week range: 26.47 - 29.13 (now 92.9% of the way up)
Volatility: ATR(14) 0.12 (0.4% of price) | annualised 20d 5.2%
Volume: 0.08x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.10</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score +0.10</summary>

```text
Fund type: Trading--Miscellaneous
What it holds: P/E n/a | P/B 0.00 | P/S 0.00 | 3y earnings growth n/a
Yield: 3.2%
Three-year record: +3.8% a year | beta to the market -11.39
Cost and size: expense ratio 0.75% | net assets 431.14M
What it is made of: Cash 100.0%
Largest holdings: Invesco Shrt-Trm Inv Gov&Agcy Instl 49.4%
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
Rolled up from the 1 largest holdings, 49.4% of the fund by weight
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
Contract: USD INDEX - ICE FUTURES U.S. (positions as of 2026-10-13, published the following Friday)
Large speculators: net long 4.0% of open interest (51,816 contracts)
Change on the week: +2.3% of open interest
Crowding: 85% percentile over 52 weeks -- within its normal range
Read this as crowding, not as a forecast: an extreme is as often the end of a move as the middle of one.
```

</details>

<details><summary><b>Money going into and out of this fund</b> — score +0.20</summary>

```text
Direction: money coming in (1 month)
Share count change: 1 week: +0.2% (741.55K) over 7d | 1 month: +41.4% (126.05M) over 32d
Shares outstanding: 14.88M | fund size: 430.54M
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Europe (VGK) · Index fund — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Neutral overall; no macro surprise, modest analyst bias on a thin slice, minimal net short decreasing, technicals mixed, fundamentals stable.

**Main reasons it gave:**
- US Treasury yields fell modestly across the curve this week
- Net short in MSCI EAFE futures is only 0.3% and decreased by 0.4% week‑over‑week
- Analyst coverage of top holdings is thin (12.1% of fund) with modest buy bias
- Technical indicators show price near 20‑day SMA, RSI neutral, MACD slightly bullish but no decisive break
- Fund fundamentals (P/E 17.26, 3% yield) remain average with no major change

<details><summary><b>News</b> — score +0.00</summary>

_No news found for this one today._

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.06% (-0.03 on the week) | 5-year 4.93% (-0.07 on the week) | 10-year 5.10% (-0.09 on the week) | 30-year 5.41% (-0.11 on the week)
Yield curve, 10-year minus 3-month: +1.04 points -- upward sloping (normal)
US dollar index: 101.77 (-0.78 on the week)
Volatility (VIX): 17.03 (+0.2 on the week) -- elevated
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 87.55 (bar of 2026-10-21), from 502 daily bars
Trend: vs 20d SMA 86.76 (+0.9%), 50d 89.29 (-1.9%), 200d 87.81 (-0.3%); 50d above 200d
Momentum: RSI(14) 50.5 | MACD -0.573 vs signal -0.855 (histogram 0.282)
Returns: 1d +0.4% | 5d +1.8% | 1m -2.1% | 3m -0.3%
52-week range: 77.90 - 93.19 (now 63.1% of the way up)
Volatility: ATR(14) 0.91 (1.0% of price) | annualised 20d 12.7%
Volume: 0.12x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.10</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score +0.10</summary>

```text
Fund type: Europe Stock
What it holds: P/E 17.26 | P/B 2.24 | P/S 1.59 | 3y earnings growth n/a
Yield: 3.0%
Three-year record: +18.9% a year | beta to the market 0.90
Cost and size: expense ratio 0.06% | net assets 37.17B
What it is made of: Stocks 99.0%, Cash 0.7%, Other 0.3%
Largest holdings: ASML Holding NV 4.5%, HSBC Holdings PLC 2.2%, Roche Holding AG Ordinary Shares new 1.9%, Shell PLC 1.8%, Novartis AG Registered Shares 1.7%
Sector mix: Financial services 25.4%, Industrials 19.5%, Healthcare 12.1%, Technology 9.4%
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
Rolled up from the 5 largest holdings, 12.1% of the fund by weight  -- thin, so read this as a fact about that slice rather than the fund
Ratings by weight: buy 67.6% | hold 32.4% | sell 0.0% (mean 2.02 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +16.5% above the current prices
Holdings read: ASML.AS, HSBA.L, ROP.SW, SHEL.L, NOVN.SW
Recent rating changes among them: none reported
```

</details>

<details><summary><b>Buying and selling by company insiders</b> — score +0.05</summary>

_Not available today._

</details>

<details><summary><b>Who is positioned how</b> — score +0.05</summary>

```text
Contract: MSCI EAFE  - ICE FUTURES U.S. (positions as of 2026-10-13, published the following Friday)
Large speculators: net short 0.3% of open interest (480,891 contracts)
Change on the week: -0.4% of open interest
Crowding: 65% percentile over 52 weeks -- within its normal range
Read this as crowding, not as a forecast: an extreme is as often the end of a move as the middle of one.
```

</details>

<details><summary><b>Money going into and out of this fund</b> — score +0.05</summary>

```text
Direction: flat (1 month)
Share count change: 1 week: +0.0% (0.00) over 7d | 1 month: +0.0% (0.00) over 33d
Shares outstanding: 282.09M | fund size: 24.70B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

**Data that was missing** (counted as 0.00, never guessed):
- news unavailable: Bright Data unreachable: The read operation timed out

### Emerging markets (VWO) · Index fund — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> No macro surprise, technicals lack decisive break, analyst view bullish but thin, positioning slightly bearish

**Main reasons it gave:**
- Analyst coverage thin (23.5% of fund) but shows 100% buy and +46.9% price target
- CFTC positioning net long decreased by 1.5% of open interest, indicating slight bearish shift
- Technical indicators: price below 20‑day and 50‑day SMA, RSI 36.7, no decisive break on volume
- Macro: Treasury yields up slightly, dollar down, VIX unchanged – no surprise data

<details><summary><b>News</b> — score +0.00</summary>

- [ETFs Investing in MOL Hungarian Oil & Gas Plc Class A Stocks](https://www.tradingview.com/symbols/HAM-MOGB/etfs/)  
  <sub>TradingView, 23 hours ago</sub>  
  Explore funds investing in MOGB in a single list with price, expense ratio, and more stats for an in-depth analysis of new opportunities.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.06% (-0.03 on the week) | 5-year 4.93% (-0.07 on the week) | 10-year 5.10% (-0.09 on the week) | 30-year 5.41% (-0.11 on the week)
Yield curve, 10-year minus 3-month: +1.04 points -- upward sloping (normal)
US dollar index: 101.77 (-0.78 on the week)
Volatility (VIX): 17.03 (+0.2 on the week) -- elevated
```

</details>

<details><summary><b>Price and chart</b> — score -0.20</summary>

```text
Last close 58.01 (bar of 2026-10-21), from 502 daily bars
Trend: vs 20d SMA 59.33 (-2.2%), 50d 59.96 (-3.3%), 200d 58.30 (-0.5%); 50d above 200d
Momentum: RSI(14) 36.7 | MACD -0.497 vs signal -0.317 (histogram -0.180)
Returns: 1d -0.4% | 5d -1.5% | 1m -5.1% | 3m -0.2%
52-week range: 52.42 - 61.44 (now 61.9% of the way up)
Volatility: ATR(14) 0.62 (1.1% of price) | annualised 20d 13.1%
Volume: 0.26x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.35</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score +0.35</summary>

```text
Fund type: Diversified Emerging Mkts
What it holds: P/E 16.13 | P/B 2.13 | P/S 1.85 | 3y earnings growth n/a
Yield: 2.0%
Three-year record: +18.1% a year | beta to the market 0.75
Cost and size: expense ratio 0.06% | net assets 164.66B
What it is made of: Stocks 95.8%, Cash 4.0%, Other 0.1%, Preferred 0.0%
Largest holdings: Taiwan Semiconductor Manufacturing Co Ltd 15.7%, Tencent Holdings Ltd 2.8%, Alibaba Group Holding Ltd Ordinary Shares 2.1%, MediaTek Inc 1.9%, Delta Electronics Inc 0.9%
Sector mix: Technology 33.8%, Financial services 19.5%, Consumer cyclical 9.3%, Industrials 7.5%
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
Rolled up from the 5 largest holdings, 23.5% of the fund by weight  -- thin, so read this as a fact about that slice rather than the fund
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 1.33 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +46.9% above the current prices
Holdings read: 2330.TW, 0700.HK, 9988.HK, 2454.TW, 2308.TW
Recent rating changes among them: none reported
```

</details>

<details><summary><b>Buying and selling by company insiders</b> — score -0.25</summary>

_Not available today._

</details>

<details><summary><b>Who is positioned how</b> — score -0.25</summary>

```text
Contract: MSCI EM INDEX - ICE FUTURES U.S. (positions as of 2026-10-13, published the following Friday)
Large speculators: net long 2.8% of open interest (1,042,945 contracts)
Change on the week: -1.5% of open interest
Crowding: 33% percentile over 52 weeks -- within its normal range
Read this as crowding, not as a forecast: an extreme is as often the end of a move as the middle of one.
```

</details>

<details><summary><b>Money going into and out of this fund</b> — score -0.25</summary>

```text
Direction: flat (1 month)
Share count change: 1 week: +0.0% (0.00) over 7d | 1 month: +0.0% (0.00) over 32d
Shares outstanding: 1.42B | fund size: 82.26B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### US company bonds, riskier (HYG) · Index fund — no answer, no confidence given

<details><summary><b>News</b> — score n/a</summary>

- [Investors are preferring high-yield bonds over riskier investment-grade](https://seekingalpha.com/news/4655189-investors-are-preferring-high-yield-bonds-over-riskier-investment-grade)  
  <sub>Seeking Alpha, 35 minutes ago</sub>  
  High-yield vs investment-grade bond spreads hit the widest since May 2025, signaling a flight to quality.
- [Options Flow Leaderboard | Bradesco Call Roll Fuels Earnings Bet; GME Sees 8.8-to-1 Call Skew on CEO's Buying Spree](https://www.moomoo.com/community/feed/options-flow-leaderboard-bradesco-call-roll-fuels-earnings-bet-gme-117476797644806)  
  <sub>Moomoo, 12 hours ago</sub>  
  Call/Put Volume Board $Bank Bradesco SA(prefer share ADS) (BBD.US)$ reports Q3 earnings Thursday pre-market; shares have run ~35% since late September...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score n/a</summary>

```text
US Treasury yields: 3-month 4.06% (-0.03 on the week) | 5-year 4.93% (-0.07 on the week) | 10-year 5.10% (-0.09 on the week) | 30-year 5.41% (-0.11 on the week)
Yield curve, 10-year minus 3-month: +1.04 points -- upward sloping (normal)
US dollar index: 101.77 (-0.78 on the week)
Volatility (VIX): 17.03 (+0.2 on the week) -- elevated
```

</details>

<details><summary><b>Price and chart</b> — score n/a</summary>

```text
Last close 76.89 (bar of 2026-10-21), from 502 daily bars
Trend: vs 20d SMA 77.16 (-0.3%), 50d 78.38 (-1.9%), 200d 79.65 (-3.5%); 50d below 200d
Momentum: RSI(14) 34.1 | MACD -0.422 vs signal -0.461 (histogram 0.039)
Returns: 1d +0.1% | 5d +0.1% | 1m -2.3% | 3m -2.9%
52-week range: 76.81 - 81.28 (now 1.9% of the way up)
Volatility: ATR(14) 0.30 (0.4% of price) | annualised 20d 3.8%
Volume: 0.11x the 20-day average
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
Three-year record: +8.5% a year | beta to the market 0.70
Cost and size: expense ratio 0.49% | net assets 16.78B
What it is made of: Bonds 99.5%, Cash 0.3%, Preferred 0.2%
Largest holdings: BlackRock Cash Funds Treasury SL Agency 1.0%
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
Direction: flat (1 month)
Share count change: 1 week: +0.0% (0.00) over 7d | 1 month: +0.0% (0.00) over 33d
Shares outstanding: 195.60M | fund size: 15.04B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

## Sector and country funds

### Israel (EIS) · Sector or country — BULLISH, confidence 0.35

**Result:** ACCEPTED · 57 shares · submitted buy 57 EIS @ ~122.04, stop 118.59

**In the model's own words:**

> Analyst view is strongly positive, fundamentals are solid, technicals show modest bullish signs, but low volume tempers confidence; macro shows no surprise.

**Main reasons it gave:**
- Analyst: 100% buy rating covering 37.6% of fund with +20.5% price target
- Fundamentals: 3‑year record +38.2%/yr and moderate valuation (P/E 17.9)
- Technical: price above 20‑day SMA and MACD histogram positive
- Technical: volume 0.15× 20‑day average (low activity)
- Macro: yields down, dollar down, VIX stable (no surprise)

<details><summary><b>News</b> — score +0.00</summary>

_No news found for this one today._

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.06% (-0.03 on the week) | 5-year 4.93% (-0.07 on the week) | 10-year 5.10% (-0.09 on the week) | 30-year 5.41% (-0.11 on the week)
Yield curve, 10-year minus 3-month: +1.04 points -- upward sloping (normal)
US dollar index: 101.77 (-0.78 on the week)
Volatility (VIX): 17.03 (+0.2 on the week) -- elevated
```

</details>

<details><summary><b>Price and chart</b> — score +0.20</summary>

```text
Last close 121.90 (bar of 2026-10-21), from 502 daily bars
Trend: vs 20d SMA 120.28 (+1.4%), 50d 122.42 (-0.4%), 200d 123.13 (-1.0%); 50d below 200d
Momentum: RSI(14) 53.5 | MACD -0.705 vs signal -1.006 (histogram 0.301)
Returns: 1d +0.8% | 5d +3.3% | 1m -3.9% | 3m +2.2%
52-week range: 98.34 - 137.69 (now 59.9% of the way up)
Volatility: ATR(14) 1.71 (1.4% of price) | annualised 20d 16.4%
Volume: 0.15x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.35</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score +0.35</summary>

```text
Fund type: Focused Region
What it holds: P/E 17.89 | P/B 2.43 | P/S 2.45 | 3y earnings growth n/a
Yield: 1.5%
Three-year record: +38.2% a year | beta to the market 1.09
Cost and size: expense ratio 0.59% | net assets 874.00M
What it is made of: Stocks 99.5%, Cash 0.5%
Largest holdings: Teva Pharmaceutical Industries Ltd ADR 10.1%, Bank Leumi Le-Israel BM 9.0%, Bank Hapoalim BM 8.1%, Tower Semiconductor Ltd 5.5%, Elbit Systems Ltd 4.8%
Sector mix: Financial services 36.1%, Technology 18.1%, Healthcare 10.7%, Industrials 10.0%
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

<details><summary><b>What analysts and big funds say</b> — score +0.55</summary>

_Not available today._

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score +0.55</summary>

```text
Rolled up from the 5 largest holdings, 37.6% of the fund by weight
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 1.17 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +20.5% above the current prices
Holdings read: TEVA, LUMI.TA, POLI.TA, TSEM.TA, ESLT.TA
Recent rating changes among them:
  - TEVA: 2026-10-15 Barclays: main, Overweight -> Overweight
  - TSEM.TA: 2026-09-25 Mizuho: init, ? -> Outperform
  - ESLT.TA: 2026-10-05 Jefferies: main, Hold -> Hold
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
Shares outstanding: 2.55M | fund size: 310.86M
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Turkey (TUR) · Sector or country — NEUTRAL, confidence 0.30

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Analyst consensus 100% buy with +30.6% price target; flat fund flows over the past week and month; low valuation metrics (P/E 11.69, P/B 1.02, P/S 0.63); RSI 30.5 indicating oversold conditions

**Main reasons it gave:**
- Analyst consensus 100% buy with +30.6% price target
- Fund flows flat over the past week and month
- Fund valuation: P/E 11.69, P/B 1.02, P/S 0.63
- RSI 30.5 indicating oversold conditions

<details><summary><b>News</b> — score +0.00</summary>

- [Direxion Daily Semiconductor Bull 3X Shares (SOXL) Stock Price, News, Quote & History](https://ca.finance.yahoo.com/quote/SOXL/)  
  <sub>Yahoo! Finance Canada, 5 hours ago</sub>  
  Find the latest Direxion Daily Semiconductor Bull 3X Shares (SOXL) stock quote, history, news and other vital information to help you with your stock...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.06% (-0.03 on the week) | 5-year 4.93% (-0.07 on the week) | 10-year 5.10% (-0.09 on the week) | 30-year 5.41% (-0.11 on the week)
Yield curve, 10-year minus 3-month: +1.04 points -- upward sloping (normal)
US dollar index: 101.77 (-0.78 on the week)
Volatility (VIX): 17.03 (+0.2 on the week) -- elevated
```

</details>

<details><summary><b>Price and chart</b> — score -0.10</summary>

```text
Last close 32.15 (bar of 2026-10-21), from 502 daily bars
Trend: vs 20d SMA 34.04 (-5.6%), 50d 37.29 (-13.8%), 200d 39.23 (-18.1%); 50d below 200d
Momentum: RSI(14) 30.5 | MACD -1.392 vs signal -1.332 (histogram -0.060)
Returns: 1d -1.4% | 5d -4.4% | 1m -13.9% | 3m -18.5%
52-week range: 31.80 - 43.74 (now 2.9% of the way up)
Volatility: ATR(14) 0.65 (2.0% of price) | annualised 20d 25.3%
Volume: 0.13x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.10</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score +0.10</summary>

```text
Fund type: Focused Region
What it holds: P/E 11.69 | P/B 1.02 | P/S 0.63 | 3y earnings growth n/a
Yield: 2.5%
Three-year record: -1.1% a year | beta to the market 0.61
Cost and size: expense ratio 0.59% | net assets 163.33M
What it is made of: Stocks 99.7%, Cash 0.3%
Largest holdings: Aselsan Elektronik Sanayi Ve Ticaret AS 11.4%, Tupras-Turkiye Petrol Rafineleri AS 10.6%, Bim Birlesik Magazalar AS 10.4%, Akbank TAS 6.1%, Turk Hava Yollari AO 4.8%
Sector mix: Industrials 29.2%, Financial services 16.1%, Consumer defensive 13.9%, Basic materials 11.4%
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
Rolled up from the 5 largest holdings, 43.2% of the fund by weight
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 1.69 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +30.6% above the current prices
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
Shares outstanding: 15.65M | fund size: 503.15M
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### US regional banks (KRE) · Sector or country — NEUTRAL, confidence 0.10

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> The fund shows modestly bullish fundamentals and analyst sentiment, but net outflows indicate bearish investor behavior. Technicals are mixed with price above the 20‑day SMA but below the 50‑day SMA and low volume, while macro conditions are unchanged and not surprising.

**Main reasons it gave:**
- Fund flows: net outflows of -2.3% over the past month and -0.3% over the past week
- Analyst coverage: thin (5.7% of fund weight) but 59.8% buy rating and +12.5% price target for top holdings
- Technicals: price above 20‑day SMA but below 50‑day SMA, RSI 48.2 (neutral), low volume (0.31× 20‑day average)
- Macro: yields high but unchanged, normal upward‑sloping yield curve, VIX modestly elevated

<details><summary><b>News</b> — score +0.00</summary>

- [Form 4 State Street® Utilities Select Sector SPDR® ETF For: 20 October](https://uk.investing.com/news/stock-market-news/form-4-state-street-utilities-select-sector-spdr-etf-for-20-october-93CH-4920758)  
  <sub>Investing.com UK, 20 hours ago</sub>  
  Registration Statement No.333-285508. Filed Pursuant to Rule 424(b)(2). Pricing Supplement dated October 16, 2026 to the Prospectus dated March 25, 2025,
- [Is CoreWeave's Credit Crisis More Like the 2023 SVB Panic Than the 2008 Subprime Mortgage Crisis?](https://eu.36kr.com/en/p/4034051208025220)  
  <sub>36Kr, 23 hours ago</sub>  
  Recent Wall Street market discussions have widely argued that the widespread market panic surrounding specialized cloud provider CoreWeave is largely...
- [Form 4 iShares Semiconductor ETF For: 21 October By Investing.com](https://ca.investing.com/news/stock-market-news/form-4-ishares-semiconductor-etf-for-21-october-93CH-4892248)  
  <sub>Investing.com Canada, 9 hours ago</sub>  
  This pricing supplement, which is not complete and may be changed, relates to an effective Registration Statement under the Securities Act of 1933.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.06% (-0.03 on the week) | 5-year 4.93% (-0.07 on the week) | 10-year 5.10% (-0.09 on the week) | 30-year 5.41% (-0.11 on the week)
Yield curve, 10-year minus 3-month: +1.04 points -- upward sloping (normal)
US dollar index: 101.77 (-0.78 on the week)
Volatility (VIX): 17.03 (+0.2 on the week) -- elevated
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 70.39 (bar of 2026-10-21), from 502 daily bars
Trend: vs 20d SMA 69.90 (+0.7%), 50d 72.56 (-3.0%), 200d 70.80 (-0.6%); 50d above 200d
Momentum: RSI(14) 48.2 | MACD -0.728 vs signal -0.991 (histogram 0.263)
Returns: 1d -0.3% | 5d +2.7% | 1m -1.1% | 3m -6.3%
52-week range: 58.63 - 77.93 (now 60.9% of the way up)
Volatility: ATR(14) 1.24 (1.8% of price) | annualised 20d 16.7%
Volume: 0.31x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.20</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score +0.20</summary>

```text
Fund type: Financial
What it holds: P/E 12.02 | P/B 1.21 | P/S 3.59 | 3y earnings growth n/a
Yield: 2.3%
Three-year record: +22.6% a year | beta to the market 1.04
Cost and size: expense ratio 0.35% | net assets 3.73B
What it is made of: Stocks 99.8%, Cash 0.2%
Largest holdings: United Bankshares Inc 1.1%, First Interstate BancSystem Inc 1.1%, Old National Bancorp 1.1%, Hancock Whitney Corp 1.1%, East West Bancorp Inc 1.1%
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
Rolled up from the 5 largest holdings, 5.7% of the fund by weight  -- thin, so read this as a fact about that slice rather than the fund
Ratings by weight: buy 59.8% | hold 40.2% | sell 0.0% (mean 2.24 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +12.5% above the current prices
Holdings read: UBSI, FIBK, ONB, HWC, EWBC
Recent rating changes among them:
  - UBSI: 2026-07-27 Keefe, Bruyette & Woods: main, Market Perform -> Market Perform
  - FIBK: 2026-10-05 Barclays: main, Underweight -> Underweight
  - ONB: 2026-10-09 RBC Capital: main, Sector Perform -> Sector Perform
  - HWC: 2026-10-21 Piper Sandler: main, Overweight -> Overweight
  - EWBC: 2026-10-21 TD Cowen: main, Buy -> Buy
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
Share count change: 1 week: -0.3% (-11.68M) over 7d | 1 month: -2.3% (-91.06M) over 32d
Shares outstanding: 53.82M | fund size: 3.79B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Poland (EPOL) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Neutral overall due to mixed signals: bullish analyst consensus, modest outflows, technicals near 52‑week high but low volume, and neutral macro backdrop.

**Main reasons it gave:**
- Analyst consensus: 100% buy rating with +1.2% price target
- Fund flows: 1.7% share count decline over past month (net outflows)
- Technicals: price near 52‑week high, above 20‑, 50‑, 200‑day SMAs, but volume at 15% of 20‑day average
- Macro: Treasury yields slipped modestly, no surprise data; VIX 17.0 (moderate volatility)

<details><summary><b>News</b> — score +0.00</summary>

_No news found for this one today._

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.06% (-0.03 on the week) | 5-year 4.93% (-0.07 on the week) | 10-year 5.10% (-0.09 on the week) | 30-year 5.41% (-0.11 on the week)
Yield curve, 10-year minus 3-month: +1.04 points -- upward sloping (normal)
US dollar index: 101.77 (-0.78 on the week)
Volatility (VIX): 17.03 (+0.2 on the week) -- elevated
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 45.03 (bar of 2026-10-21), from 502 daily bars
Trend: vs 20d SMA 44.13 (+2.0%), 50d 44.41 (+1.4%), 200d 40.10 (+12.3%); 50d above 200d
Momentum: RSI(14) 56.8 | MACD 0.045 vs signal -0.036 (histogram 0.081)
Returns: 1d +1.9% | 5d +2.3% | 1m -1.2% | 3m +10.4%
52-week range: 32.56 - 45.76 (now 94.5% of the way up)
Volatility: ATR(14) 0.65 (1.4% of price) | annualised 20d 19.1%
Volume: 0.15x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.15</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score +0.15</summary>

```text
Fund type: Focused Region
What it holds: P/E 13.22 | P/B 2.06 | P/S 1.40 | 3y earnings growth n/a
Yield: 3.3%
Three-year record: +39.0% a year | beta to the market 0.64
Cost and size: expense ratio 0.59% | net assets 833.96M
What it is made of: Stocks 99.1%, Cash 0.9%
Largest holdings: PKO Bank Polski SA 16.2%, Orlen SA 12.7%, Bank Polska Kasa Opieki SA 7.4%, Powszechny Zaklad Ubezpieczen SA 6.0%, Allegro.EU SA Ordinary Shares 4.9%
Sector mix: Financial services 46.9%, Energy 13.3%, Consumer cyclical 13.2%, Basic materials 6.2%
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

<details><summary><b>What analysts and big funds say</b> — score +0.35</summary>

_Not available today._

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score +0.35</summary>

```text
Rolled up from the 5 largest holdings, 47.1% of the fund by weight
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 2.18 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +1.2% above the current prices
Holdings read: PKO.WA, PKN.WA, PEO.WA, PZU.WA, ALE.WA
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
Share count change: 1 week: -0.6% (-4.81M) over 7d | 1 month: -1.7% (-14.89M) over 32d
Shares outstanding: 18.91M | fund size: 851.52M
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

**Data that was missing** (counted as 0.00, never guessed):
- news unavailable: Bright Data unreachable: The read operation timed out

### Australia (EWA) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Neutral overall; analyst view modestly bearish, fundamentals modestly bullish, and flows flat.

**Main reasons it gave:**
- Flat fund flows: share count unchanged (+0.0% week, +0.0% month)
- Analyst rating: 59.5% hold, 40.5% sell, mean rating 3.41 (sell‑leaning)
- Technical trend: price above 20‑day (+2.5%), 50‑day (+0.3%), 200‑day (+1.6%) SMAs but volume at 0.26× 20‑day average
- Macro: Treasury yields unchanged (3‑month -0.03, 5‑year -0.07, 10‑year -0.09) and no policy surprise

<details><summary><b>News</b> — score +0.00</summary>

_No news found for this one today._

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.06% (-0.03 on the week) | 5-year 4.93% (-0.07 on the week) | 10-year 5.10% (-0.09 on the week) | 30-year 5.41% (-0.11 on the week)
Yield curve, 10-year minus 3-month: +1.04 points -- upward sloping (normal)
US dollar index: 101.77 (-0.78 on the week)
Volatility (VIX): 17.03 (+0.2 on the week) -- elevated
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 29.26 (bar of 2026-10-21), from 502 daily bars
Trend: vs 20d SMA 28.55 (+2.5%), 50d 29.18 (+0.3%), 200d 28.79 (+1.6%); 50d above 200d
Momentum: RSI(14) 58.6 | MACD -0.006 vs signal -0.133 (histogram 0.127)
Returns: 1d +0.4% | 5d +2.5% | 1m +0.6% | 3m +2.7%
52-week range: 24.95 - 30.43 (now 78.6% of the way up)
Volatility: ATR(14) 0.32 (1.1% of price) | annualised 20d 11.2%
Volume: 0.26x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.20</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score +0.20</summary>

```text
Fund type: Focused Region
What it holds: P/E 20.31 | P/B 2.65 | P/S 3.31 | 3y earnings growth n/a
Yield: 3.0%
Three-year record: +15.0% a year | beta to the market 0.98
Cost and size: expense ratio 0.50% | net assets 1.21B
What it is made of: Stocks 99.2%, Cash 0.8%
Largest holdings: BHP Group Ltd 15.4%, Commonwealth Bank of Australia 12.6%, National Australia Bank Ltd 6.1%, Westpac Banking Corp 6.0%, ANZ Group Holdings Ltd 5.8%
Sector mix: Financial services 42.0%, Basic materials 25.4%, Consumer cyclical 6.5%, Healthcare 5.6%
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
Rolled up from the 5 largest holdings, 45.9% of the fund by weight
Ratings by weight: buy 0.0% | hold 59.5% | sell 40.5% (mean 3.41 on a 1=strong buy to 5=strong sell scale)
Weighted price target: -6.7% above the current prices
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
Share count change: 1 week: +0.0% (0.00) over 7d | 1 month: +0.0% (0.00) over 33d
Shares outstanding: 63.60M | fund size: 1.86B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Canada (EWC) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Neutral call – no macro surprise, flat fund flows, modest technicals without decisive break, limited analyst coverage with only modest upside, and solid but not catalytic fundamentals.

**Main reasons it gave:**
- No macro surprise or data release outside expectations
- Fund flows flat (0% change) indicating no net demand
- Technicals show modest uptrend but low volume and price near 52‑week high
- Analyst coverage only 29.3% of fund with modest +1.7% price target

<details><summary><b>News</b> — score +0.00</summary>

_No news found for this one today._

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.06% (-0.03 on the week) | 5-year 4.93% (-0.07 on the week) | 10-year 5.10% (-0.09 on the week) | 30-year 5.41% (-0.11 on the week)
Yield curve, 10-year minus 3-month: +1.04 points -- upward sloping (normal)
US dollar index: 101.77 (-0.78 on the week)
Volatility (VIX): 17.03 (+0.2 on the week) -- elevated
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 61.37 (bar of 2026-10-21), from 502 daily bars
Trend: vs 20d SMA 59.39 (+3.3%), 50d 60.56 (+1.3%), 200d 58.09 (+5.7%); 50d above 200d
Momentum: RSI(14) 61.5 | MACD 0.155 vs signal -0.170 (histogram 0.325)
Returns: 1d +0.8% | 5d +3.6% | 1m +1.0% | 3m +4.3%
52-week range: 49.72 - 62.64 (now 90.2% of the way up)
Volatility: ATR(14) 0.70 (1.1% of price) | annualised 20d 14.8%
Volume: 0.18x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.25</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score +0.25</summary>

```text
Fund type: Focused Region
What it holds: P/E 18.94 | P/B 2.75 | P/S 2.69 | 3y earnings growth n/a
Yield: 1.3%
Three-year record: +24.7% a year | beta to the market 0.80
Cost and size: expense ratio 0.50% | net assets 7.02B
What it is made of: Stocks 99.6%, Cash 0.4%
Largest holdings: Royal Bank of Canada 9.1%, The Toronto-Dominion Bank 6.5%, Shopify Inc Registered Shs -A- Subord Vtg 6.0%, Bank of Montreal 3.8%, Bank of Nova Scotia 3.7%
Sector mix: Financial services 39.9%, Energy 17.3%, Basic materials 15.2%, Technology 9.3%
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

<details><summary><b>What analysts and big funds say</b> — score +0.35</summary>

_Not available today._

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score +0.35</summary>

```text
Rolled up from the 5 largest holdings, 29.3% of the fund by weight
Ratings by weight: buy 79.8% | hold 20.2% | sell 0.0% (mean 2.11 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +1.7% above the current prices
Holdings read: RY, TD, SHOP, BMO.TO, BNS.TO
Recent rating changes among them:
  - RY: 2025-08-29 Argus Research: main, Buy -> Buy
  - TD: 2026-06-01 RBC Capital: main, Outperform -> Outperform
  - SHOP: 2026-10-16 RBC Capital: main, Outperform -> Outperform
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
Direction: flat (1 month)
Share count change: 1 week: +0.0% (0.00) over 7d | 1 month: +0.0% (0.00) over 33d
Shares outstanding: 94.80M | fund size: 5.82B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Sweden (EWD) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Neutral overall as there is no material macro surprise, fund flows are flat, technicals are mixed, and analyst coverage is limited despite a bullish tilt.

**Main reasons it gave:**
- Analyst coverage limited to 28.9% of fund, with 81.7% buy rating and +13.6% price target
- Fund flows flat with no net inflows or outflows
- Technical indicators mixed: price above 20‑day SMA but below 50‑day and 200‑day SMA, RSI 50.8, low volume
- Macro unchanged: yields down slightly, dollar down, VIX stable

<details><summary><b>News</b> — score +0.00</summary>

_No news found for this one today._

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.06% (-0.03 on the week) | 5-year 4.93% (-0.07 on the week) | 10-year 5.10% (-0.09 on the week) | 30-year 5.41% (-0.11 on the week)
Yield curve, 10-year minus 3-month: +1.04 points -- upward sloping (normal)
US dollar index: 101.77 (-0.78 on the week)
Volatility (VIX): 17.03 (+0.2 on the week) -- elevated
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 51.11 (bar of 2026-10-21), from 502 daily bars
Trend: vs 20d SMA 50.62 (+1.0%), 50d 51.79 (-1.3%), 200d 51.49 (-0.7%); 50d above 200d
Momentum: RSI(14) 50.8 | MACD -0.146 vs signal -0.298 (histogram 0.152)
Returns: 1d +0.1% | 5d +0.9% | 1m -2.1% | 3m +2.8%
52-week range: 45.38 - 54.72 (now 61.3% of the way up)
Volatility: ATR(14) 0.67 (1.3% of price) | annualised 20d 13.7%
Volume: 0.09x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.15</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score +0.15</summary>

```text
Fund type: Focused Region
What it holds: P/E 14.64 | P/B 2.82 | P/S 2.83 | 3y earnings growth n/a
Yield: 3.6%
Three-year record: +20.2% a year | beta to the market 1.25
Cost and size: expense ratio 0.51% | net assets 947.21M
What it is made of: Stocks 99.1%, Cash 0.9%
Largest holdings: Spotify Technology SA 9.7%, Investor AB Class B 9.6%, Atlas Copco AB Class A 7.1%, Volvo AB Class B 6.8%, Sandvik AB 5.3%
Sector mix: Industrials 46.3%, Financial services 25.6%, Communication services 13.5%, Technology 6.1%
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

<details><summary><b>What analysts and big funds say</b> — score +0.45</summary>

_Not available today._

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score +0.45</summary>

```text
Rolled up from the 4 largest holdings, 28.9% of the fund by weight
Ratings by weight: buy 81.7% | hold 18.3% | sell 0.0% (mean 2.01 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +13.6% above the current prices
Holdings read: SPOT, ATCO-A.ST, VOLV-B.ST, SAND.ST
Recent rating changes among them:
  - SPOT: 2026-10-20 Rosenblatt: main, Neutral -> Neutral
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
Share count change: 1 week: +0.0% (0.00) over 7d | 1 month: +0.0% (0.00) over 33d
Shares outstanding: 7.65M | fund size: 390.99M
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Germany (EWG) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Most dimensions point to a neutral stance: no macro surprise, flat fund flows, technicals lack a decisive break, and while analyst coverage is bullish, it does not outweigh the neutral macro/technical context.

**Main reasons it gave:**
- US Treasury yields up slightly across the curve, no rate surprise
- Fund flows flat over the past week and month, indicating no net demand
- Technicals show price just above 20‑day SMA but below 50‑day SMA, RSI 51, no decisive break
- Analyst coverage of top holdings (45.4% of fund) is 78.7% buy, but macro and technical context remain neutral

<details><summary><b>News</b> — score +0.00</summary>

_No news found for this one today._

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.06% (-0.03 on the week) | 5-year 4.93% (-0.07 on the week) | 10-year 5.10% (-0.09 on the week) | 30-year 5.41% (-0.11 on the week)
Yield curve, 10-year minus 3-month: +1.04 points -- upward sloping (normal)
US dollar index: 101.77 (-0.78 on the week)
Volatility (VIX): 17.03 (+0.2 on the week) -- elevated
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 41.79 (bar of 2026-10-21), from 502 daily bars
Trend: vs 20d SMA 41.37 (+1.0%), 50d 42.64 (-2.0%), 200d 42.30 (-1.2%); 50d above 200d
Momentum: RSI(14) 51.0 | MACD -0.299 vs signal -0.424 (histogram 0.124)
Returns: 1d +0.9% | 5d +2.1% | 1m -2.0% | 3m +3.0%
52-week range: 38.08 - 44.59 (now 57.0% of the way up)
Volatility: ATR(14) 0.50 (1.2% of price) | annualised 20d 14.3%
Volume: 0.14x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.30</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score +0.30</summary>

```text
Fund type: Focused Region
What it holds: P/E 17.64 | P/B 1.86 | P/S 1.23 | 3y earnings growth n/a
Yield: 2.0%
Three-year record: +19.6% a year | beta to the market 0.98
Cost and size: expense ratio 0.49% | net assets 1.47B
What it is made of: Stocks 99.9%, Cash 0.1%
Largest holdings: Siemens AG 12.1%, SAP SE 11.5%, Allianz SE 9.6%, Siemens Energy AG Ordinary Shares 6.7%, Deutsche Telekom AG 5.4%
Sector mix: Industrials 28.9%, Financial services 22.9%, Technology 16.4%, Healthcare 7.2%
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
Ratings by weight: buy 78.7% | hold 21.3% | sell 0.0% (mean 1.94 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +17.3% above the current prices
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
Direction: flat (1 month)
Share count change: 1 week: +0.0% (0.00) over 7d | 1 month: +0.0% (0.00) over 32d
Shares outstanding: 79.50M | fund size: 3.32B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Italy (EWI) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> The fund shows a strong bullish analyst rating (+20.6% price target) but flat fund flows and a down‑trend technical picture (price below 20‑, 50‑ and 200‑day SMAs, RSI 39.1) offset the upside. Fundamentals are solid (P/E 14.42, 3‑year return +27.3%/yr, yield 3.2%) but not enough to overcome the mixed signals, leading to a neutral overall stance.

**Main reasons it gave:**
- Analyst view: 100% buy rating with +20.6% price target
- Fund flows: flat (0% change) over the past month
- Technical: price below 20‑day, 50‑day, and 200‑day SMAs; RSI 39.1 indicating weak momentum
- Fundamentals: P/E 14.42, three‑year return +27.3% per year, yield 3.2%

<details><summary><b>News</b> — score +0.00</summary>

_No news found for this one today._

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.06% (-0.03 on the week) | 5-year 4.93% (-0.07 on the week) | 10-year 5.10% (-0.09 on the week) | 30-year 5.41% (-0.11 on the week)
Yield curve, 10-year minus 3-month: +1.04 points -- upward sloping (normal)
US dollar index: 101.77 (-0.78 on the week)
Volatility (VIX): 17.03 (+0.2 on the week) -- elevated
```

</details>

<details><summary><b>Price and chart</b> — score -0.30</summary>

```text
Last close 56.43 (bar of 2026-10-21), from 502 daily bars
Trend: vs 20d SMA 57.36 (-1.6%), 50d 60.08 (-6.1%), 200d 58.13 (-2.9%); 50d above 200d
Momentum: RSI(14) 39.1 | MACD -1.190 vs signal -1.229 (histogram 0.039)
Returns: 1d +0.7% | 5d +0.6% | 1m -7.1% | 3m -5.5%
52-week range: 50.66 - 63.35 (now 45.5% of the way up)
Volatility: ATR(14) 0.79 (1.4% of price) | annualised 20d 18.0%
Volume: 0.10x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.20</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score +0.20</summary>

```text
Fund type: Focused Region
What it holds: P/E 14.42 | P/B 1.77 | P/S 1.50 | 3y earnings growth n/a
Yield: 3.2%
Three-year record: +27.3% a year | beta to the market 0.88
Cost and size: expense ratio 0.50% | net assets 1.17B
What it is made of: Stocks 99.9%, Cash 0.1%
Largest holdings: UniCredit SpA 18.0%, Intesa Sanpaolo 15.0%, Enel SpA 10.6%, Eni SpA 4.7%, Prysmian SpA 4.7%
Sector mix: Financial services 54.1%, Utilities 16.5%, Industrials 12.0%, Consumer cyclical 8.0%
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
Rolled up from the 5 largest holdings, 53.0% of the fund by weight
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 2.03 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +20.6% above the current prices
Holdings read: UCG.MI, ISP.MI, ENEL.MI, ENI.MI, PRY.MI
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
Share count change: 1 week: +0.0% (0.00) over 7d | 1 month: +0.0% (0.00) over 33d
Shares outstanding: 8.55M | fund size: 482.48M
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

**Data that was missing** (counted as 0.00, never guessed):
- news unavailable: Bright Data HTTP 502: <html>
<head><title>502 Bad Gateway</title></head>
<body>
<center><h1>502 Bad Gateway</h1></center>
</body>
</html>


### Japan (EWJ) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Neutral overall as no material macro surprise, no decisive technical break, and mixed signals from fundamentals, analyst view, and positioning.

**Main reasons it gave:**
- Japan trade deficit widened to JPY 536.6B, worse than expectations
- Analyst coverage of top holdings is 100% buy with +23.3% price target, but only covers 17% of fund
- CFTC data shows net short 2.4% of open interest, up 5.8% week, indicating slight bearish positioning
- Technical indicators: price below 20‑day and 50‑day SMAs, negative MACD, RSI 45.2, no decisive break

<details><summary><b>News</b> — score +0.00</summary>

- [Japan’s trade gap widens despite 13-month export growth streak (EWJ:NYSEARCA)](https://seekingalpha.com/news/4654985-japans-trade-gap-widens-despite-13-month-export-growth-streak)  
  <sub>Seeking Alpha, 11 hours ago</sub>  
  Japan's trade deficit widened to JPY 536.6B in September 2026 from JPY 277.7B a year earlier, exceeding market expectations of a JPY 181B.
- [iShares MSCI EAFE ETF (EFA) Stock Price, News, Quote & History](https://ca.finance.yahoo.com/quote/EFA/)  
  <sub>Yahoo! Finance Canada, 21 hours ago</sub>  
  Find the latest iShares MSCI EAFE ETF (EFA) stock quote, history, news and other vital information to help you with your stock trading and investing.
- [Where the AI Trade Is Still Ripping](https://investorplace.com/2026/10/where-the-ai-trade-is-still-ripping/)  
  <sub>InvestorPlace, 10 hours ago</sub>  
  An ugly week for the AI trade… Eric Fry on why “familiar isn't safe”… Brian Hunt's Brazil call keeps paying… Jonathan Rose eyes AI at a discount.
- [Asian markets recover as earnings optimism offsets AI concerns (EWJ:NYSEARCA)](https://seekingalpha.com/news/4654984-asian-markets-recover-as-earnings-optimism-offsets-ai-concerns)  
  <sub>Seeking Alpha, 11 hours ago</sub>  
  Asian stock market update: Nikkei and Kospi rally on strong U.S. earnings, while oil hits $110 and tech volatility persists.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.06% (-0.03 on the week) | 5-year 4.93% (-0.07 on the week) | 10-year 5.10% (-0.09 on the week) | 30-year 5.41% (-0.11 on the week)
Yield curve, 10-year minus 3-month: +1.04 points -- upward sloping (normal)
US dollar index: 101.77 (-0.78 on the week)
Volatility (VIX): 17.03 (+0.2 on the week) -- elevated
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 95.83 (bar of 2026-10-21), from 502 daily bars
Trend: vs 20d SMA 97.00 (-1.2%), 50d 96.87 (-1.1%), 200d 91.42 (+4.8%); 50d above 200d
Momentum: RSI(14) 45.2 | MACD -0.407 vs signal -0.080 (histogram -0.327)
Returns: 1d +0.4% | 5d -0.0% | 1m -3.0% | 3m +5.2%
52-week range: 79.49 - 99.32 (now 82.4% of the way up)
Volatility: ATR(14) 1.25 (1.3% of price) | annualised 20d 15.2%
Volume: 0.47x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.20</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score +0.20</summary>

```text
Fund type: Japan Stock
What it holds: P/E 15.27 | P/B 1.98 | P/S 1.37 | 3y earnings growth n/a
Yield: 3.7%
Three-year record: +21.0% a year | beta to the market 0.83
Cost and size: expense ratio 0.49% | net assets 23.53B
What it is made of: Stocks 99.1%, Cash 0.9%
Largest holdings: Mitsubishi UFJ Financial Group Inc 4.7%, Toyota Motor Corp 3.3%, Tokyo Electron Ltd 3.1%, Sumitomo Mitsui Financial Group Inc 3.0%, Advantest Corp 3.0%
Sector mix: Industrials 22.8%, Technology 22.0%, Financial services 19.3%, Consumer cyclical 11.1%
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
Rolled up from the 5 largest holdings, 17.0% of the fund by weight  -- thin, so read this as a fact about that slice rather than the fund
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 1.69 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +23.3% above the current prices
Holdings read: 8306.T, 7203.T, 8035.T, 8316.T, 6857.T
Recent rating changes among them: none reported
```

</details>

<details><summary><b>Buying and selling by company insiders</b> — score -0.20</summary>

_Not available today._

</details>

<details><summary><b>Who is positioned how</b> — score -0.20</summary>

```text
Contract: NIKKEI STOCK AVERAGE YEN DENOM - CHICAGO MERCANTILE EXCHANGE (positions as of 2026-10-13, published the following Friday)
Large speculators: net short 2.4% of open interest (23,701 contracts)
Change on the week: +5.8% of open interest
Crowding: 15% percentile over 52 weeks -- within its normal range
Read this as crowding, not as a forecast: an extreme is as often the end of a move as the middle of one.
```

</details>

<details><summary><b>Money going into and out of this fund</b> — score -0.20</summary>

```text
Direction: flat (1 month)
Share count change: 1 week: +0.0% (0.00) over 7d | 1 month: +0.0% (0.00) over 33d
Shares outstanding: 227.85M | fund size: 21.84B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Switzerland (EWL) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Neutral overall; no material macro surprise, flat fund flows, modestly bullish analyst view, stable fundamentals, mixed technical signals.

**Main reasons it gave:**
- Flat fund flows (no net inflows/outflows) over the past week and month
- Analyst ratings mixed: 64.8% buy, 35.2% hold, weighted price target +3.6% above current price
- Technical indicators: price above 20‑day, 50‑day, and 200‑day SMAs, but RSI high at 68.9 and volume low at 0.42× average
- Macro environment unchanged: yields down slightly across the curve, dollar index down 0.78, VIX stable at 17.03

<details><summary><b>News</b> — score +0.00</summary>

- [ETFs Investing in Swatch Group Ltd. Bearer Stocks](https://www.tradingview.com/symbols/XETR-UHR/etfs/)  
  <sub>TradingView, 6 hours ago</sub>  
  Explore funds investing in UHR in a single list with price, expense ratio, and more stats for an in-depth analysis of new opportunities.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.06% (-0.03 on the week) | 5-year 4.93% (-0.07 on the week) | 10-year 5.10% (-0.09 on the week) | 30-year 5.41% (-0.11 on the week)
Yield curve, 10-year minus 3-month: +1.04 points -- upward sloping (normal)
US dollar index: 101.77 (-0.78 on the week)
Volatility (VIX): 17.03 (+0.2 on the week) -- elevated
```

</details>

<details><summary><b>Price and chart</b> — score +0.20</summary>

```text
Last close 63.22 (bar of 2026-10-21), from 502 daily bars
Trend: vs 20d SMA 60.40 (+4.7%), 50d 61.57 (+2.7%), 200d 61.67 (+2.5%); 50d below 200d
Momentum: RSI(14) 68.9 | MACD 0.372 vs signal -0.143 (histogram 0.515)
Returns: 1d +0.3% | 5d +4.5% | 1m +3.3% | 3m +2.2%
52-week range: 55.06 - 65.08 (now 81.4% of the way up)
Volatility: ATR(14) 0.66 (1.0% of price) | annualised 20d 13.7%
Volume: 0.42x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.20</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score +0.20</summary>

```text
Fund type: Focused Region
What it holds: P/E 24.08 | P/B 4.13 | P/S 2.67 | 3y earnings growth n/a
Yield: 1.8%
Three-year record: +15.5% a year | beta to the market 0.91
Cost and size: expense ratio 0.50% | net assets 2.67B
What it is made of: Stocks 99.0%, Cash 1.0%
Largest holdings: Roche Holding AG Ordinary Shares new 13.9%, Novartis AG Registered Shares 12.4%, Nestle SA 11.0%, UBS Group AG Registered Shares 6.4%, ABB Ltd 4.6%
Sector mix: Healthcare 38.0%, Financial services 19.6%, Consumer defensive 13.1%, Industrials 12.3%
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
Rolled up from the 5 largest holdings, 48.2% of the fund by weight
Ratings by weight: buy 64.8% | hold 35.2% | sell 0.0% (mean 2.40 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +3.6% above the current prices
Holdings read: ROP.SW, NOVN.SW, NESN.SW, UBSG.SW, ABBN.SW
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
Direction: flat (1 month)
Share count change: 1 week: +0.0% (0.00) over 7d | 1 month: +0.0% (0.00) over 32d
Shares outstanding: 28.62M | fund size: 1.81B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Netherlands (EWN) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Neutral overall; no macro surprise, flat fund flows, mixed technicals, but bullish analyst view limited to top holdings.

**Main reasons it gave:**
- Analyst consensus 100% buy for top holdings with +42.9% price target
- Technical momentum bearish: RSI 43, MACD below signal, price below 20‑day/50‑day SMA
- Fund flows flat over past week and month, indicating no net demand shift
- Macro environment neutral: yields down slightly, dollar down, VIX unchanged

<details><summary><b>News</b> — score +0.00</summary>

_No news found for this one today._

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.06% (-0.03 on the week) | 5-year 4.93% (-0.07 on the week) | 10-year 5.10% (-0.09 on the week) | 30-year 5.41% (-0.11 on the week)
Yield curve, 10-year minus 3-month: +1.04 points -- upward sloping (normal)
US dollar index: 101.77 (-0.78 on the week)
Volatility (VIX): 17.03 (+0.2 on the week) -- elevated
```

</details>

<details><summary><b>Price and chart</b> — score -0.20</summary>

```text
Last close 65.58 (bar of 2026-10-21), from 502 daily bars
Trend: vs 20d SMA 66.61 (-1.5%), 50d 67.81 (-3.3%), 200d 64.89 (+1.1%); 50d above 200d
Momentum: RSI(14) 43.0 | MACD -0.754 vs signal -0.623 (histogram -0.131)
Returns: 1d +0.9% | 5d +1.0% | 1m -4.4% | 3m -2.3%
52-week range: 55.33 - 71.61 (now 63.0% of the way up)
Volatility: ATR(14) 0.91 (1.4% of price) | annualised 20d 16.0%
Volume: 0.03x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.30</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score +0.30</summary>

```text
Fund type: Focused Region
What it holds: P/E 18.85 | P/B 2.55 | P/S 1.87 | 3y earnings growth n/a
Yield: 4.2%
Three-year record: +24.1% a year | beta to the market 1.09
Cost and size: expense ratio 0.50% | net assets 710.44M
What it is made of: Stocks 98.9%, Cash 1.1%
Largest holdings: ASML Holding NV 23.6%, ING Groep NV 9.1%, Nebius Group NV Shs Class-A- 4.9%, Prosus NV Ordinary Shares - Class N 4.6%, ASM International NV 4.4%
Sector mix: Technology 33.4%, Financial services 21.5%, Consumer defensive 10.4%, Industrials 9.6%
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
Rolled up from the 5 largest holdings, 46.7% of the fund by weight
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 1.58 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +42.9% above the current prices
Holdings read: ASML.AS, INGA.AS, NBIS, PRX.AS, ASM.AS
Recent rating changes among them:
  - NBIS: 2026-10-21 Piper Sandler: main, Neutral -> Neutral
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
Shares outstanding: 5.55M | fund size: 364.00M
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Spain (EWP) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> No material macro surprise, flat fund flows, technicals not decisive, analyst view modestly bullish but not enough to tilt.

**Main reasons it gave:**
- Analyst coverage of 55.8% of fund shows 51.5% buy rating and +7.2% price target
- Fund flows flat over past month indicating no net demand
- Technical indicators: price above 200‑day SMA but below 20‑day and 50‑day SMAs, RSI 44.9, low volume
- Macro yields slightly down, curve normal, VIX modestly elevated – no surprise

<details><summary><b>News</b> — score +0.00</summary>

_No news found for this one today._

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.06% (-0.03 on the week) | 5-year 4.93% (-0.07 on the week) | 10-year 5.10% (-0.09 on the week) | 30-year 5.41% (-0.11 on the week)
Yield curve, 10-year minus 3-month: +1.04 points -- upward sloping (normal)
US dollar index: 101.77 (-0.78 on the week)
Volatility (VIX): 17.03 (+0.2 on the week) -- elevated
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 58.47 (bar of 2026-10-21), from 502 daily bars
Trend: vs 20d SMA 58.69 (-0.4%), 50d 60.71 (-3.7%), 200d 57.88 (+1.0%); 50d above 200d
Momentum: RSI(14) 44.9 | MACD -0.757 vs signal -0.834 (histogram 0.077)
Returns: 1d +0.7% | 5d +1.0% | 1m -5.0% | 3m -0.9%
52-week range: 49.21 - 63.23 (now 66.0% of the way up)
Volatility: ATR(14) 0.80 (1.4% of price) | annualised 20d 16.2%
Volume: 0.11x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.20</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score +0.20</summary>

```text
Fund type: Focused Region
What it holds: P/E 15.94 | P/B 2.15 | P/S 1.78 | 3y earnings growth n/a
Yield: 2.8%
Three-year record: +33.1% a year | beta to the market 0.88
Cost and size: expense ratio 0.50% | net assets 2.38B
What it is made of: Stocks 99.8%, Cash 0.2%
Largest holdings: Banco Santander SA 19.2%, Banco Bilbao Vizcaya Argentaria SA 14.3%, Iberdrola SA 12.8%, Repsol SA 5.0%, CaixaBank SA 4.5%
Sector mix: Financial services 45.6%, Utilities 20.7%, Industrials 14.1%, Technology 5.5%
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
Rolled up from the 5 largest holdings, 55.8% of the fund by weight
Ratings by weight: buy 51.5% | hold 48.5% | sell 0.0% (mean 2.30 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +7.2% above the current prices
Holdings read: SAN.MC, BBVA.MC, IBE.MC, REP.MC, CABK.MC
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
Shares outstanding: 37.35M | fund size: 2.18B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Taiwan (EWT) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> No macro surprise, technicals lack decisive break, fund flows flat, analyst view bullish but limited coverage, fundamentals mixed.

**Main reasons it gave:**
- Analyst coverage 100% buy with +40.2% price target covering 39.1% of fund
- Fund flows flat over past week and month (share count unchanged)
- Technicals: price below 20‑day SMA, MACD negative, RSI 44.3, volume 0.25× 20‑day average
- Macro: yields up modestly, dollar down, VIX low – no surprise data

<details><summary><b>News</b> — score +0.00</summary>

_No news found for this one today._

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.06% (-0.03 on the week) | 5-year 4.93% (-0.07 on the week) | 10-year 5.10% (-0.09 on the week) | 30-year 5.41% (-0.11 on the week)
Yield curve, 10-year minus 3-month: +1.04 points -- upward sloping (normal)
US dollar index: 101.77 (-0.78 on the week)
Volatility (VIX): 17.03 (+0.2 on the week) -- elevated
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 108.99 (bar of 2026-10-21), from 502 daily bars
Trend: vs 20d SMA 112.76 (-3.3%), 50d 110.27 (-1.2%), 200d 91.96 (+18.5%); 50d above 200d
Momentum: RSI(14) 44.3 | MACD -0.690 vs signal 0.374 (histogram -1.064)
Returns: 1d +1.5% | 5d -1.8% | 1m -5.3% | 3m +9.2%
52-week range: 60.03 - 118.00 (now 84.5% of the way up)
Volatility: ATR(14) 2.30 (2.1% of price) | annualised 20d 23.7%
Volume: 0.25x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.00</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score +0.00</summary>

```text
Fund type: Greater China Region
What it holds: P/E 28.15 | P/B 4.48 | P/S 2.64 | 3y earnings growth n/a
Yield: 0.9%
Three-year record: +42.9% a year | beta to the market 1.26
Cost and size: expense ratio 0.59% | net assets 12.34B
What it is made of: Stocks 99.8%, Cash 0.2%
Largest holdings: Taiwan Semiconductor Manufacturing Co Ltd 21.9%, MediaTek Inc 7.2%, Delta Electronics Inc 3.9%, Hon Hai Precision Industry Co Ltd 3.2%, ASE Technology Holding Co Ltd 3.0%
Sector mix: Technology 74.2%, Financial services 14.3%, Basic materials 3.8%, Industrials 2.8%
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
Rolled up from the 5 largest holdings, 39.1% of the fund by weight
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 1.35 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +40.2% above the current prices
Holdings read: 2330.TW, 2454.TW, 2308.TW, 2317.TW, 3711.TW
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
Share count change: 1 week: +0.0% (0.00) over 7d | 1 month: +0.0% (0.00) over 33d
Shares outstanding: 85.00M | fund size: 9.26B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Mexico (EWW) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Overall neutral as no macro surprise, no decisive technical break, and flat fund flows. Analyst view is bullish (+6.3% price target) and fundamentals are positive (low P/E, 3.5% yield, strong 3‑year return), but these are not enough to outweigh the lack of a clear catalyst.

**Main reasons it gave:**
- Analyst consensus: 90.9% buy, weighted price target +6.3% above current price
- Technical indicators: price above 20‑day and 50‑day SMAs, MACD bullish
- Fund flows: flat share count, indicating neutral demand
- Macro: US Treasury yields slipped slightly and dollar index fell 0.78% on the week

<details><summary><b>News</b> — score +0.00</summary>

_No news found for this one today._

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.06% (-0.03 on the week) | 5-year 4.93% (-0.07 on the week) | 10-year 5.10% (-0.09 on the week) | 30-year 5.41% (-0.11 on the week)
Yield curve, 10-year minus 3-month: +1.04 points -- upward sloping (normal)
US dollar index: 101.77 (-0.78 on the week)
Volatility (VIX): 17.03 (+0.2 on the week) -- elevated
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 75.24 (bar of 2026-10-21), from 502 daily bars
Trend: vs 20d SMA 72.82 (+3.3%), 50d 74.48 (+1.0%), 200d 76.03 (-1.0%); 50d below 200d
Momentum: RSI(14) 58.6 | MACD 0.232 vs signal -0.290 (histogram 0.522)
Returns: 1d -0.3% | 5d +3.5% | 1m +1.0% | 3m +0.3%
52-week range: 65.07 - 81.23 (now 62.9% of the way up)
Volatility: ATR(14) 1.23 (1.6% of price) | annualised 20d 18.7%
Volume: 0.31x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.35</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score +0.35</summary>

```text
Fund type: Focused Region
What it holds: P/E 12.17 | P/B 1.90 | P/S 1.42 | 3y earnings growth n/a
Yield: 3.5%
Three-year record: +16.0% a year | beta to the market 1.07
Cost and size: expense ratio 0.50% | net assets 1.49B
What it is made of: Stocks 99.4%, Cash 0.6%
Largest holdings: Grupo Mexico SAB de CV Class B 16.4%, Grupo Financiero Banorte SAB de CV Class O 11.1%, Fomento Economico Mexicano SAB de CV Units Cons. Of 1 Shs-B- And 4 Shs-D- 8.8%, America Movil SAB de CV Ordinary Shares - Class B 7.2%, Wal - Mart de Mexico SAB de CV 4.4%
Sector mix: Basic materials 26.8%, Consumer defensive 24.8%, Financial services 19.5%, Industrials 12.1%
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
Rolled up from the 5 largest holdings, 47.8% of the fund by weight
Ratings by weight: buy 90.9% | hold 9.1% | sell 0.0% (mean 2.15 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +6.3% above the current prices
Holdings read: GMEXICOB.MX, GFNORTEO.MX, FEMSAUBD.MX, AMXB.MX, WALMEX.MX
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
Shares outstanding: 18.90M | fund size: 1.42B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### South Korea (EWY) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> No macro surprise, technicals show bearish momentum, fund flows flat, analyst view neutral, fundamentals modest but not decisive.

**Main reasons it gave:**
- US Treasury yields fell slightly across the curve this week
- EWY price is below 20‑day, 50‑day and 200‑day SMAs with RSI 36.5 and negative MACD
- Fund flows flat over the past week and month, indicating no net demand
- Analyst coverage of top holdings provides no rating guidance

<details><summary><b>News</b> — score +0.00</summary>

- [Ishares Msci South Korea ETF (Derivatives) Price (EWY/USD) Today | Live Price, Market Cap & Chart](https://www.binance.com/en/price/ishares-msci-south-korea-etf-derivatives)  
  <sub>Binance, 16 hours ago</sub>  
  The current price of Ishares Msci South Korea ETF (Derivatives) (EWY) is $157.32. Top cryptocurrency prices are updated in real-time on Binance's price...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.06% (-0.03 on the week) | 5-year 4.93% (-0.07 on the week) | 10-year 5.10% (-0.09 on the week) | 30-year 5.41% (-0.11 on the week)
Yield curve, 10-year minus 3-month: +1.04 points -- upward sloping (normal)
US dollar index: 101.77 (-0.78 on the week)
Volatility (VIX): 17.03 (+0.2 on the week) -- elevated
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 156.66 (bar of 2026-10-21), from 502 daily bars
Trend: vs 20d SMA 174.33 (-10.1%), 50d 178.38 (-12.2%), 200d 160.99 (-2.7%); 50d above 200d
Momentum: RSI(14) 36.5 | MACD -7.417 vs signal -4.545 (histogram -2.872)
Returns: 1d +1.7% | 5d -2.0% | 1m -18.7% | 3m -9.9%
52-week range: 88.53 - 219.20 (now 52.1% of the way up)
Volatility: ATR(14) 6.31 (4.0% of price) | annualised 20d 40.8%
Volume: 0.54x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.00</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score +0.00</summary>

```text
Fund type: Focused Region
What it holds: P/E 10.41 | P/B 1.79 | P/S 1.66 | 3y earnings growth n/a
Yield: 1.1%
Three-year record: +42.9% a year | beta to the market 2.48
Cost and size: expense ratio 0.59% | net assets 26.21B
What it is made of: Stocks 96.8%, Cash 3.2%
Largest holdings: SK hynix Inc 23.7%, Samsung Electronics Co Ltd 22.8%, SK Square 3.1%, Samsung Electro-Mechanics Co Ltd 2.7%, KB Financial Group Inc 1.9%
Sector mix: Technology 56.9%, Industrials 16.4%, Financial services 10.9%, Consumer cyclical 4.5%
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
Rolled up from the 5 largest holdings, 54.3% of the fund by weight
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
Direction: flat (1 month)
Share count change: 1 week: +0.0% (0.00) over 7d | 1 month: +0.0% (0.00) over 33d
Shares outstanding: 75.60M | fund size: 11.84B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Brazil (EWZ) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> No material macro surprise, flat fund flows, limited analyst coverage, price near 52‑week high with low volume.

**Main reasons it gave:**
- Fund flows flat: 0% share count change over week and month
- Analyst coverage only 39.9% of fund, though all ratings are buy with +18.3% price target
- Price near 52‑week high (94.5% of range) with volume at 0.48× 20‑day average
- No macro surprise: US yields unchanged, dollar down modestly, VIX stable

<details><summary><b>News</b> — score +0.00</summary>

- [Brazil ETF EWZ Options Surge on Brazil Election Trade | Options Income Daily](http://www.moomoo.com/community/feed/brazil-etf-ewz-options-surge-on-brazil-election-trade-options-117476372774918)  
  <sub>Moomoo, 14 hours ago</sub>  
  by Monta HONG, CFA | Options Strategist Options activity in the $iShares MSCI Brazil ETF (EWZ.US)$ has intensified as traders prepare for political vo...
- [EWZ 261023 30.00C (EWZ261023C30000) Stock Community & Discussion](https://www.moomoo.com/options/EWZ261023C30000-US/community)  
  <sub>Moomoo, 15 hours ago</sub>  
  Find the latest EWZ 261023 30.00C (EWZ261023C30000)stock discussion in moomoo's forum, a popular stock community. Get stock reviews, comments and analysis...
- [MBGA: Make Brazil Great Again](https://dailyreckoning.com/post/mbga-make-brazil-great-again)  
  <sub>The Daily Reckoning, 5 hours ago</sub>  
  It's rare to see a nation's stock market jump more than 10% in a day. But that's exactly what happened in Brazil today. The EWZ Brazil ETF popped 13.67%...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.06% (-0.03 on the week) | 5-year 4.93% (-0.07 on the week) | 10-year 5.10% (-0.09 on the week) | 30-year 5.41% (-0.11 on the week)
Yield curve, 10-year minus 3-month: +1.04 points -- upward sloping (normal)
US dollar index: 101.77 (-0.78 on the week)
Volatility (VIX): 17.03 (+0.2 on the week) -- elevated
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 42.79 (bar of 2026-10-21), from 502 daily bars
Trend: vs 20d SMA 40.68 (+5.2%), 50d 38.13 (+12.2%), 200d 37.09 (+15.4%); 50d above 200d
Momentum: RSI(14) 65.4 | MACD 1.383 vs signal 1.391 (histogram -0.008)
Returns: 1d -0.3% | 5d +0.4% | 1m +11.8% | 3m +18.3%
52-week range: 29.94 - 43.54 (now 94.5% of the way up)
Volatility: ATR(14) 0.97 (2.3% of price) | annualised 20d 49.7%
Volume: 0.48x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.20</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score +0.20</summary>

```text
Fund type: Focused Region
What it holds: P/E 10.73 | P/B 1.84 | P/S 1.40 | 3y earnings growth n/a
Yield: 3.9%
Three-year record: +18.4% a year | beta to the market 0.83
Cost and size: expense ratio 0.59% | net assets 8.64B
What it is made of: Stocks 97.5%, Cash 2.0%, Preferred 0.5%
Largest holdings: Vale SA 8.9%, Itau Unibanco Holding SA Participating Preferred 8.4%, Nu Holdings Ltd Ordinary Shares Class A 8.1%, Petroleo Brasileiro SA Petrobras Participating Preferred 7.5%, Petroleo Brasileiro SA Petrobras 7.0%
Sector mix: Financial services 34.4%, Energy 18.1%, Basic materials 13.0%, Utilities 12.8%
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
Rolled up from the 5 largest holdings, 39.9% of the fund by weight
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 1.83 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +18.3% above the current prices
Holdings read: VALE3.SA, ITUB4, NU, PETR4, PETR3.SA
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
Share count change: 1 week: +0.0% (0.00) over 7d | 1 month: +0.0% (0.00) over 32d
Shares outstanding: 200.55M | fund size: 8.58B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### South Africa (EZA) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Mixed signals: bullish analyst consensus and fundamentals offset by bearish technicals and flat flows.

**Main reasons it gave:**
- Analyst consensus: 100% buy with weighted price target +33% above current price
- Fund fundamentals: low P/E 10.44 and high dividend yield 7.9%
- Technicals: price below 50‑day and 200‑day SMAs, near 52‑week low
- Fund flows: flat share count over past month

<details><summary><b>News</b> — score +0.00</summary>

_No news found for this one today._

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.06% (-0.03 on the week) | 5-year 4.93% (-0.07 on the week) | 10-year 5.10% (-0.09 on the week) | 30-year 5.41% (-0.11 on the week)
Yield curve, 10-year minus 3-month: +1.04 points -- upward sloping (normal)
US dollar index: 101.77 (-0.78 on the week)
Volatility (VIX): 17.03 (+0.2 on the week) -- elevated
```

</details>

<details><summary><b>Price and chart</b> — score -0.20</summary>

```text
Last close 65.38 (bar of 2026-10-21), from 502 daily bars
Trend: vs 20d SMA 64.22 (+1.8%), 50d 67.51 (-3.2%), 200d 68.84 (-5.0%); 50d below 200d
Momentum: RSI(14) 50.2 | MACD -0.620 vs signal -0.996 (histogram 0.376)
Returns: 1d -0.1% | 5d +3.3% | 1m -5.5% | 3m +8.2%
52-week range: 60.43 - 81.60 (now 23.4% of the way up)
Volatility: ATR(14) 1.17 (1.8% of price) | annualised 20d 22.6%
Volume: 0.47x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.30</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score +0.30</summary>

```text
Fund type: Focused Region
What it holds: P/E 10.44 | P/B 2.00 | P/S 1.73 | 3y earnings growth n/a
Yield: 7.9%
Three-year record: +26.5% a year | beta to the market 1.07
Cost and size: expense ratio 0.59% | net assets 473.79M
What it is made of: Stocks 99.7%, Cash 0.3%
Largest holdings: Anglogold Ashanti PLC 12.7%, Gold Fields Ltd 8.7%, Naspers Ltd Class N 8.4%, Firstrand Ltd 7.4%, Standard Bank Group Ltd 6.2%
Sector mix: Basic materials 39.1%, Financial services 34.4%, Consumer cyclical 12.8%, Communication services 6.4%
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
Rolled up from the 5 largest holdings, 43.4% of the fund by weight
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 2.00 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +33.0% above the current prices
Holdings read: AU, GFI.JO, NPN.JO, FSR.JO, SBK.JO
Recent rating changes among them:
  - AU: 2026-10-15 Goldman Sachs: init, ? -> Buy
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
Shares outstanding: 7.90M | fund size: 516.50M
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Gold mining companies (GDX) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> No macro surprise, technicals show price below key moving averages with low volume, analyst view is bullish but covers only 40.8% of the fund, and recent fund flows show a net outflow of -7.8% over the month. The mix of signals leads to a neutral stance.

**Main reasons it gave:**
- Analyst consensus: 100% buy with +16.1% price target (covers 40.8% of fund)
- Fund flows: net outflow of -7.8% over past month despite recent 2.7% weekly inflow
- Technicals: price below 20‑day, 50‑day, 200‑day SMAs and volume at 0.21× 20‑day average
- Macro: yields down slightly, dollar down, VIX unchanged (no surprise)

<details><summary><b>News</b> — score +0.00</summary>

- [VanEck Gold Miners ETF (GDX) Stock Price, News, Quote & History](https://ca.finance.yahoo.com/quote/GDX/)  
  <sub>Yahoo! Finance Canada, 20 hours ago</sub>  
  VanEck Gold Miners ETF (GDX) · -1.31% · -9.82% · -13.14% · -0.85% · 7.14% · 162.02% · 135.76%. Key Events. Baseline. Advanced Chart.
- [YieldMax® ETFs Announces Weekly Distributions for Group 2 ETFs](https://www.globenewswire.com/news-release/2026/10/21/3385351/0/en/yieldmax-etfs-announces-weekly-distributions-for-group-2-etfs.html)  
  <sub>GlobeNewswire, 5 hours ago</sub>  
  CHICAGO and MILWAUKEE and NEW YORK, Oct. 21, 2026 (GLOBE NEWSWIRE) -- YieldMax® ETFs today announced distributions for the YieldMax® Group 2 weekly pay ETFs...
- [The Pivot: CoinShares Survey Suggests Crypto Investing No Longer for Speculation...It's Strategic!](https://www.advisorperspectives.com/webinars/2026/11/17/the-pivot-coinshares-survey-suggests-crypto-investing-no-longer-for-speculation-its-strategic?partnerref=APSidebar)  
  <sub>Advisor Perspectives, 23 hours ago</sub>  
  Crypto is pivoting from a speculative asset into a strategic allocation. A recent CoinShares survey shows that cryptocurrency is increasingly viewed as a...
- [ETFs Investing in Eldorado Gold Corporation Stocks](https://www.tradingview.com/symbols/XETR-ELO1/etfs/)  
  <sub>TradingView, 23 hours ago</sub>  
  Explore funds investing in ELO1 in a single list with price, expense ratio, and more stats for an in-depth analysis of new opportunities.
- [Form 4 VanEck Gold Miners ETF For: 20 October By Investing.com](https://ca.investing.com/news/stock-market-news/form-4-vaneck-gold-miners-etf-for-20-october-93CH-4892191)  
  <sub>Investing.com Canada, 12 hours ago</sub>  
  The information in this preliminary pricing supplement is not complete and may be changed. We may not sell these Notes until the pricing supplement,...
- [CIBC cuts Q4 gold price forecast to $4,500, then sees bounce to $5,200 in 2027 (GLD:NYSEARCA)](https://seekingalpha.com/news/4654945-cibc-cuts-q4-gold-price-forecast-to-4500-then-sees-bounce-to-5200-in-2027)  
  <sub>Seeking Alpha, 18 hours ago</sub>  
  Commodity analysts at CIBC Capital remain bullish on gold over the longer term even as the bank significantly lowers its price forecast for this year.
- [VanEck UCITS ETFs Plc - Net Asset Value(s)](https://uk.finance.yahoo.com/news/vaneck-ucits-etfs-plc-net-060000272.html)  
  <sub>Yahoo Finance UK, 9 hours ago</sub>  
  Fund Name. NAV Date. Ticker Symbol. ISIN. Shares in Issue. Net Asset Value. NAV per Share. VanEck Emerging Markets High Yield Bond UCITS ETF. 2026-10-20.
- [ETFs investiert in Kinross Gold Corporation-Aktien](https://de.tradingview.com/symbols/BX-KIN2/etfs/)  
  <sub>TradingView, 23 hours ago</sub>  
  Entdecken Sie Fonds, die in KIN2 investiert sind. Dargestellt auf einer Liste zusammen mit dem Preis, der Kostenquote und weiteren nützlichen Daten für eine...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.06% (-0.03 on the week) | 5-year 4.93% (-0.07 on the week) | 10-year 5.10% (-0.09 on the week) | 30-year 5.41% (-0.11 on the week)
Yield curve, 10-year minus 3-month: +1.04 points -- upward sloping (normal)
US dollar index: 101.77 (-0.78 on the week)
Volatility (VIX): 17.03 (+0.2 on the week) -- elevated
```

</details>

<details><summary><b>Price and chart</b> — score -0.20</summary>

```text
Last close 86.62 (bar of 2026-10-21), from 502 daily bars
Trend: vs 20d SMA 87.73 (-1.3%), 50d 93.21 (-7.1%), 200d 91.05 (-4.9%); 50d above 200d
Momentum: RSI(14) 44.7 | MACD -1.688 vs signal -1.729 (histogram 0.041)
Returns: 1d +0.6% | 5d +3.9% | 1m -11.5% | 3m +15.5%
52-week range: 68.28 - 115.84 (now 38.6% of the way up)
Volatility: ATR(14) 2.82 (3.3% of price) | annualised 20d 36.6%
Volume: 0.21x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.20</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score +0.20</summary>

```text
Fund type: Equity Precious Metals
What it holds: P/E 13.93 | P/B 3.18 | P/S 4.54 | 3y earnings growth n/a
Yield: 0.7%
Three-year record: +44.8% a year | beta to the market 0.81
Cost and size: expense ratio 0.51% | net assets 26.25B
What it is made of: Stocks 100.0%, Cash 0.0%
Largest holdings: Newmont Corp 11.1%, Agnico Eagle Mines Ltd 11.0%, Barrick Mining Corp 7.9%, Wheaton Precious Metals Corp 5.5%, Franco-Nevada Corp 5.2%
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
Rolled up from the 5 largest holdings, 40.8% of the fund by weight
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 1.65 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +16.1% above the current prices
Holdings read: NEM, AEM.TO, ABX.TO, WPM.TO, FNV.TO
Recent rating changes among them:
  - NEM: 2026-10-20 Citigroup: main, Buy -> Buy
  - AEM.TO: 2026-10-21 JP Morgan: main, Neutral -> Neutral
  - ABX.TO: 2026-10-21 JP Morgan: main, Overweight -> Overweight
  - WPM.TO: 2026-10-08 UBS: main, Buy -> Buy
  - FNV.TO: 2026-09-16 RBC Capital: main, Outperform -> Outperform
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
Share count change: 1 week: +2.7% (696.19M) over 7d | 1 month: -7.8% (-2.23B) over 32d
Shares outstanding: 303.07M | fund size: 26.25B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Software (IGV) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Neutral overall; no macro surprise, technicals lack decisive break, fund flows flat, fundamentals neutral despite high valuations, analyst view bullish but not enough to shift overall stance.

**Main reasons it gave:**
- Analyst view: 100% buy rating, weighted price target +20.9% above current price
- Technicals: price above 20d, 50d, 200d SMAs; MACD below signal; volume 0.24x 20‑day average
- Macro: Treasury yields down slightly, normal upward yield curve, VIX 17.0, no surprise data
- Fund flows: flat share count, no net creations/redemptions

<details><summary><b>News</b> — score +0.00</summary>

- [How Vulnerable Is IGV After Palantir and ServiceNow Lost 5%?](https://kalkine.ca/news/general-news/how-vulnerable-is-igv-after-palantir-and-servicenow-lost-5)  
  <sub>kalkine.ca, 3 hours ago</sub>  
  You are reading a free article with opinions that may differ from the recommendation given by Kalkine in its paid research reports. Become a Kalkine member...
- [Braze leads software sector higher, while chip stocks mostly hold steady](https://www.tradingview.com/news/seekingalpha:79d114cdb094b:0-braze-leads-software-sector-higher-while-chip-stocks-mostly-hold-steady/)  
  <sub>TradingView, 20 hours ago</sub>  
  Braze NASDAQ:BRZE shares catapulted more than 50% on Tuesday after Salesforce NYSE:CRM agreed to buy the AI-powered marketing platform for $5.66B in...
- [Form 4 iShares Expanded Tech-Software Sector ETF For: 20 October By Investing.com](https://za.investing.com/news/stock-market-news/form-4-ishares-expanded-techsoftware-sector-etf-for-20-october-93CH-4515300)  
  <sub>Investing.com South Africa, 14 hours ago</sub>  
  Pricing Supplement dated October 16, 2026. (To the Prospectus dated May 15, 2025, the Prospectus Supplement dated May 15, 2025

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.06% (-0.03 on the week) | 5-year 4.93% (-0.07 on the week) | 10-year 5.10% (-0.09 on the week) | 30-year 5.41% (-0.11 on the week)
Yield curve, 10-year minus 3-month: +1.04 points -- upward sloping (normal)
US dollar index: 101.77 (-0.78 on the week)
Volatility (VIX): 17.03 (+0.2 on the week) -- elevated
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 108.74 (bar of 2026-10-21), from 502 daily bars
Trend: vs 20d SMA 108.27 (+0.4%), 50d 106.10 (+2.5%), 200d 93.78 (+15.9%); 50d above 200d
Momentum: RSI(14) 53.0 | MACD 0.618 vs signal 1.098 (histogram -0.479)
Returns: 1d +1.7% | 5d +1.0% | 1m +1.9% | 3m +24.8%
52-week range: 74.67 - 117.08 (now 80.3% of the way up)
Volatility: ATR(14) 2.75 (2.5% of price) | annualised 20d 28.7%
Volume: 0.24x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.00</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score +0.00</summary>

```text
Fund type: Technology
What it holds: P/E 31.87 | P/B 7.50 | P/S 8.53 | 3y earnings growth n/a
Yield: 0.0%
Three-year record: +15.1% a year | beta to the market 1.22
Cost and size: expense ratio 0.38% | net assets 13.91B
What it is made of: Stocks 100.0%, Cash 0.0%
Largest holdings: Palo Alto Networks Inc 9.7%, Palantir Technologies Inc Ordinary Shares - Class A 9.0%, CrowdStrike Holdings Inc Class A 8.9%, Microsoft Corp 8.5%, Oracle Corp 6.9%
Sector mix: Technology 93.2%, Communication services 4.2%, Financial services 2.2%, Consumer cyclical 0.3%
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
Rolled up from the 5 largest holdings, 42.9% of the fund by weight
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 1.64 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +20.9% above the current prices
Holdings read: PANW, PLTR, CRWD, MSFT, ORCL
Recent rating changes among them:
  - PANW: 2026-10-15 Citigroup: main, Buy -> Buy
  - PLTR: 2026-10-15 Mizuho: main, Outperform -> Outperform
  - CRWD: 2026-10-16 Keybanc: main, Overweight -> Overweight
  - MSFT: 2026-10-21 Guggenheim: reit, Buy -> Buy
  - ORCL: 2026-10-02 Citizens: reit, Market Outperform -> Market Outperform
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
Shares outstanding: 12.50M | fund size: 1.36B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### India (INDA) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:** no explanation. It wrote only “NEUTRAL”, so the main reasons below are all it gave.

**Main reasons it gave:**
- Outflows: -13.1% share count decline over 1 month
- Analyst consensus: 100% buy on top holdings (23.7% of fund) with +28.6% price target
- Technicals: price above 20‑day SMA, MACD above signal, but volume at 0.35× 20‑day average
- Macro: US dollar down 0.78% on week, yields down modestly, no policy surprise

<details><summary><b>News</b> — score +0.00</summary>

_No news found for this one today._

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.06% (-0.03 on the week) | 5-year 4.93% (-0.07 on the week) | 10-year 5.10% (-0.09 on the week) | 30-year 5.41% (-0.11 on the week)
Yield curve, 10-year minus 3-month: +1.04 points -- upward sloping (normal)
US dollar index: 101.77 (-0.78 on the week)
Volatility (VIX): 17.03 (+0.2 on the week) -- elevated
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 47.40 (bar of 2026-10-21), from 502 daily bars
Trend: vs 20d SMA 46.94 (+1.0%), 50d 48.25 (-1.8%), 200d 49.40 (-4.1%); 50d below 200d
Momentum: RSI(14) 49.7 | MACD -0.175 vs signal -0.386 (histogram 0.211)
Returns: 1d -0.8% | 5d +0.8% | 1m -1.8% | 3m -0.5%
52-week range: 45.42 - 55.29 (now 20.1% of the way up)
Volatility: ATR(14) 0.52 (1.1% of price) | annualised 20d 16.0%
Volume: 0.35x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.00</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score +0.00</summary>

```text
Fund type: India Equity
What it holds: P/E 21.36 | P/B 2.96 | P/S 2.56 | 3y earnings growth n/a
Yield: n/a
Three-year record: +2.5% a year | beta to the market 0.62
Cost and size: expense ratio 0.61% | net assets 5.83B
What it is made of: Stocks 99.3%, Cash 0.7%
Largest holdings: HDFC Bank Ltd 6.4%, ICICI Bank Ltd 5.6%, Reliance Industries Ltd 5.4%, Bharti Airtel Ltd 3.9%, Infosys Ltd 2.4%
Sector mix: Financial services 29.7%, Consumer cyclical 12.3%, Industrials 10.2%, Basic materials 8.5%
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
Rolled up from the 5 largest holdings, 23.7% of the fund by weight  -- thin, so read this as a fact about that slice rather than the fund
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 1.35 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +28.6% above the current prices
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
Share count change: 1 week: -2.5% (-152.20M) over 7d | 1 month: -13.1% (-877.61M) over 32d
Shares outstanding: 123.14M | fund size: 5.84B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

**Data that was missing** (counted as 0.00, never guessed):
- news unavailable: Bright Data HTTP 502: <html>
<head><title>502 Bad Gateway</title></head>
<body>
<center><h1>502 Bad Gateway</h1></center>
</body>
</html>


### Transport and delivery (IYT) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:** no explanation. It wrote only “Neutral”, so the main reasons below are all it gave.

**Main reasons it gave:**
- Analyst coverage of top holdings shows 100% buy rating and +27.9% price target
- Fund flows flat over past week and month (0% share count change)
- Macro data unchanged: Treasury yields down slightly, VIX stable, no surprise
- Technical indicators: price below 50‑day and 200‑day SMA, RSI 47.5, low volume

<details><summary><b>News</b> — score +0.00</summary>

- [Hertz Soars 12% as Oro Mobility Lands $80M Investment; Ryder and Avis Tick Up](https://247wallst.com/investing/2026/10/20/hertz-soars-12-as-oro-mobility-lands-80m-investment-ryder-and-avis-tick-up/)  
  <sub>24/7 Wall St., 24 hours ago</sub>  
  Hertz surged 12% after Oro Mobility secured an $80M equity investment from Cohen Private Ventures, Certares, and Knighthead, while Hertz retains majority...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.06% (-0.03 on the week) | 5-year 4.93% (-0.07 on the week) | 10-year 5.10% (-0.09 on the week) | 30-year 5.41% (-0.11 on the week)
Yield curve, 10-year minus 3-month: +1.04 points -- upward sloping (normal)
US dollar index: 101.77 (-0.78 on the week)
Volatility (VIX): 17.03 (+0.2 on the week) -- elevated
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 80.11 (bar of 2026-10-21), from 502 daily bars
Trend: vs 20d SMA 79.64 (+0.6%), 50d 82.33 (-2.7%), 200d 81.57 (-1.8%); 50d above 200d
Momentum: RSI(14) 47.5 | MACD -0.523 vs signal -0.759 (histogram 0.237)
Returns: 1d +0.3% | 5d +0.7% | 1m -0.0% | 3m -9.2%
52-week range: 68.14 - 90.01 (now 54.8% of the way up)
Volatility: ATR(14) 1.16 (1.4% of price) | annualised 20d 13.8%
Volume: 0.09x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.00</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score +0.00</summary>

```text
Fund type: Industrials
What it holds: P/E 18.90 | P/B 3.94 | P/S 1.34 | 3y earnings growth n/a
Yield: 1.0%
Three-year record: +13.4% a year | beta to the market 1.32
Cost and size: expense ratio 0.37% | net assets 1.88B
What it is made of: Stocks 99.9%, Cash 0.1%
Largest holdings: Union Pacific Corp 17.4%, Uber Technologies Inc 15.1%, CSX Corp 9.3%, Delta Air Lines Inc 4.9%, United Airlines Holdings Inc 4.8%
Sector mix: Industrials 84.1%, Technology 15.9%
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
Rolled up from the 5 largest holdings, 51.6% of the fund by weight
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 1.64 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +27.9% above the current prices
Holdings read: UNP, UBER, CSX, DAL, UAL
Recent rating changes among them:
  - UNP: 2026-10-07 Citigroup: main, Buy -> Buy
  - UBER: 2026-10-16 Guggenheim: reit, Buy -> Buy
  - CSX: 2026-10-07 Citigroup: main, Neutral -> Neutral
  - DAL: 2026-10-12 UBS: main, Buy -> Buy
  - UAL: 2026-10-16 UBS: main, Buy -> Buy
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
Share count change: 1 week: +0.0% (0.00) over 7d | 1 month: +0.0% (0.00) over 33d
Shares outstanding: 2.80M | fund size: 224.32M
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Saudi Arabia (KSA) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Neutral overall; analyst view is bullish but modest, fund flows show net outflow, fundamentals are slightly bearish, and technicals show no decisive break.

**Main reasons it gave:**
- Analyst view: 90% buy rating and +21.5% price target
- Fund flows: net outflow of -2.1% over past month
- Technicals: price below 20‑day, 50‑day, 200‑day SMAs and RSI 22.7 (oversold)
- Macro: US yields up slightly, dollar down, VIX moderate

<details><summary><b>News</b> — score +0.00</summary>

- [Financial Results : SAB 9M 2026 net profit rises to SAR 6.58B; Q3 at SAR 2.17B](https://www.argaam.com/en/financial-reports/company-report/48/2026/72?preview=true)  
  <sub>ارقام : اخبار ومعلومات سوق الأسهم السعودي - تاسي, 3 hours ago</sub>  
  Loading data... Comments Analysis: Positive: 0%. Neutral: 0%. Negative: 0%. Comments Summary:Loading data... Please note that this news summary has been...
- [Financial Results : Saudi Kayan losses narrow to SAR 1.4B in 9M 2026, SAR 94.2M in Q3](https://www.argaam.com/en/financial-reports/company-report/598/2026/72?preview=true)  
  <sub>ارقام : اخبار ومعلومات سوق الأسهم السعودي - تاسي, 3 hours ago</sub>  
  Loading data... Comments Analysis: Positive: 0%. Neutral: 0%. Negative: 0%. Comments Summary:Loading data... Please note that this news summary has been...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.06% (-0.03 on the week) | 5-year 4.93% (-0.07 on the week) | 10-year 5.10% (-0.09 on the week) | 30-year 5.41% (-0.11 on the week)
Yield curve, 10-year minus 3-month: +1.04 points -- upward sloping (normal)
US dollar index: 101.77 (-0.78 on the week)
Volatility (VIX): 17.03 (+0.2 on the week) -- elevated
```

</details>

<details><summary><b>Price and chart</b> — score -0.20</summary>

```text
Last close 34.60 (bar of 2026-10-21), from 502 daily bars
Trend: vs 20d SMA 35.98 (-3.8%), 50d 37.31 (-7.2%), 200d 38.07 (-9.1%); 50d below 200d
Momentum: RSI(14) 22.7 | MACD -0.699 vs signal -0.594 (histogram -0.105)
Returns: 1d -0.5% | 5d -1.6% | 1m -7.3% | 3m -6.8%
52-week range: 34.60 - 41.03 (now 0.0% of the way up)
Volatility: ATR(14) 0.33 (0.9% of price) | annualised 20d 12.6%
Volume: 0.47x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score -0.10</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score -0.10</summary>

```text
Fund type: Focused Region
What it holds: P/E 14.08 | P/B 1.70 | P/S 2.84 | 3y earnings growth n/a
Yield: 2.8%
Three-year record: +0.9% a year | beta to the market 0.19
Cost and size: expense ratio 0.75% | net assets 588.43M
What it is made of: Stocks 99.6%, Cash 0.4%
Largest holdings: Al Rajhi Bank 14.1%, Saudi Arabian Oil Co 11.5%, Saudi National Bank 8.6%, Saudi Telecom Co 6.1%, Saudi Arabian Mining Co 4.3%
Sector mix: Financial services 42.2%, Energy 12.5%, Basic materials 12.4%, Communication services 9.0%
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
Rolled up from the 5 largest holdings, 44.6% of the fund by weight
Ratings by weight: buy 90.3% | hold 9.7% | sell 0.0% (mean 2.06 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +21.5% above the current prices
Holdings read: 1120.SR, 2222.SR, 1180.SR, 7010.SR, 1211.SR
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
Share count change: 1 week: +2.3% (13.02M) over 7d | 1 month: -2.1% (-12.51M) over 32d
Shares outstanding: 16.67M | fund size: 576.91M
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### China (MCHI) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Neutral overall as no macro surprise or decisive technical break; bullish analyst view offset by bearish technicals and net outflows

**Main reasons it gave:**
- Technical indicators show bearish momentum (RSI 32.5, MACD negative) with low volume
- Analyst view of top holdings is 100% buy with price target +64% above current
- Fund flows show net outflows over the past month (-2.7%) indicating bearish sentiment

<details><summary><b>News</b> — score +0.00</summary>

_No news found for this one today._

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.06% (-0.03 on the week) | 5-year 4.93% (-0.07 on the week) | 10-year 5.10% (-0.09 on the week) | 30-year 5.41% (-0.11 on the week)
Yield curve, 10-year minus 3-month: +1.04 points -- upward sloping (normal)
US dollar index: 101.77 (-0.78 on the week)
Volatility (VIX): 17.03 (+0.2 on the week) -- elevated
```

</details>

<details><summary><b>Price and chart</b> — score -0.40</summary>

```text
Last close 50.05 (bar of 2026-10-21), from 502 daily bars
Trend: vs 20d SMA 51.81 (-3.4%), 50d 53.28 (-6.1%), 200d 56.21 (-11.0%); 50d below 200d
Momentum: RSI(14) 32.5 | MACD -0.687 vs signal -0.587 (histogram -0.099)
Returns: 1d -1.8% | 5d -2.7% | 1m -7.7% | 3m -6.2%
52-week range: 50.05 - 65.59 (now 0.0% of the way up)
Volatility: ATR(14) 0.67 (1.3% of price) | annualised 20d 16.5%
Volume: 0.42x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.30</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score +0.30</summary>

```text
Fund type: Greater China Region
What it holds: P/E 11.39 | P/B 1.33 | P/S 1.31 | 3y earnings growth n/a
Yield: 2.1%
Three-year record: +9.6% a year | beta to the market 0.45
Cost and size: expense ratio 0.59% | net assets 5.99B
What it is made of: Stocks 99.5%, Cash 0.5%
Largest holdings: Tencent Holdings Ltd 13.8%, Alibaba Group Holding Ltd Ordinary Shares 9.3%, China Construction Bank Corp Class H 4.3%, Industrial And Commercial Bank Of China Ltd Class H 2.6%, Xiaomi Corp Class B 2.2%
Sector mix: Consumer cyclical 22.5%, Financial services 21.0%, Communication services 18.1%, Technology 11.6%
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
Rolled up from the 5 largest holdings, 32.3% of the fund by weight
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 1.41 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +64.3% above the current prices
Holdings read: 0700.HK, 9988.HK, 00939, 01398, 1810.HK
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
Share count change: 1 week: +3.1% (178.42M) over 7d | 1 month: -2.7% (-164.17M) over 32d
Shares outstanding: 117.22M | fund size: 5.87B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

**Data that was missing** (counted as 0.00, never guessed):
- news unavailable: Bright Data unreachable: The read operation timed out

### Chip makers (SMH) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Neutral overall; no macro surprise, technicals show short‑term bearish momentum but no decisive break, flat fund flows, and analyst bullishness limited to 44% coverage.

**Main reasons it gave:**
- Flat fund flows (0% change week/month) indicate no net demand
- Technical momentum bearish (RSI 38.7, MACD -9.033) but no decisive break on volume
- Macro data unchanged (yields down ~0.1% week, dollar -0.78, VIX 17.03)
- Analyst coverage 44.3% all buy, price target +46% above current but limited coverage

<details><summary><b>News</b> — score +0.00</summary>

- [Semiconductor Stocks May Face An Explosive Move This Week (NASDAQ:SMH)](https://seekingalpha.com/article/4955914-semiconductor-stocks-may-face-an-explosive-move-this-week)  
  <sub>Seeking Alpha, 9 minutes ago</sub>  
  The VanEck Semiconductor ETF sits at critical technical support, with upcoming Bank of Korea rate decisions likely to drive the next major SMH move.
- [Forget SMH. Invesco’s Chip Fund Returned 67.69% Over the Past Year Against SMH’s 61.32%.](https://finance.yahoo.com/markets/stocks/articles/forget-smh-invesco-chip-fund-220302614.html)  
  <sub>Yahoo Finance, 17 hours ago</sub>  
  Invesco's semiconductor fund quietly beat the industry's most popular chip ETF over the past year, but the five-year scoreboard tells a very different story...
- [Forget SMH. Invesco's Chip Fund Returned 67.69% Over the Past Year Against SMH's 61.32%.](https://247wallst.com/investing/etf/2026/10/20/forget-smh-invescos-chip-fund-returned-67-69-over-the-past-year-against-smhs-61-32/)  
  <sub>24/7 Wall St., 17 hours ago</sub>  
  Invesco's semiconductor fund quietly beat the industry's most popular chip ETF over the past year, but the five-year scoreboard tells a very different story...
- [Invesco's chip ETF outperformed SMH with 67.69% return in one year but lags over five years.](https://pluang.com/en/news-feed/invesco-chip-fund-lebih-baik-dari-smh)  
  <sub>Pluang, 17 hours ago</sub>  
  Invesco's semiconductor ETF (SOXQ) returned 67.69% over the past year, beating the popular VanEck's SMH fund, which returned 61.32%.
- [DRAM ETF Heads For Longest Weekly Losing Streak Since Inception, Roundhill CEO Says ‘Investor Sentiment Has Turned’](https://stocktwits.com/news-articles/markets/equity/dram-etf-record-weekly-losing-streak-roundhill-ceo-investor-sentiment-has-turned/cZxhcl7RBrQ)  
  <sub>Stocktwits, 14 hours ago</sub>  
  The Roundhill Memory ETF (DRAM) was on track for its longest losing streak since inception on Thursday, even as Round Hill Investments CEO Dave Maza said...
- [VanEck Semiconductor ETF Options Spot-On: On October 20th, 135.97K Contracts Were Traded, With 1.83 Million Open Interest](https://news.futunn.com/en/post/1001710442/vaneck-semiconductor-etf-options-spot-on-on-october-20th-135)  
  <sub>富途牛牛, 18 hours ago</sub>  
  OnOctober 20th ET, $VanEck Semiconductor ETF(SMH.US)$ had active options trading, with a total trading volume of 135.97K options for the day,...
- [SMH 261023 530.00C (SMH261023C530000) Stock Options Chain | Quotes & News](https://www.moomoo.com/options/SMH261023C530000-US)  
  <sub>Moomoo, 4 hours ago</sub>  
  Track real-time SMH 261023 530.00C (SMH261023C530000) stock options chain data and pricing information and news on moomoo App for your options trading and...
- [S&P 500, Dow Gain As Earnings Season Sets In, While SpaceX Aids Nasdaq After-Hours — SPCX, BA, MMM, NFLX, QCOM In Focus](https://www.google.com/goto?url=CAES5wEB6zswFYB3O3-T0EQiGSdzvvkZJUwcoOCCD32PBMCsd-43LkqGOs4pG3KFb5DajrJniX4BMk5FRsf5bMm8_OsCfpwT0xhp8-E9qq1hdH7B75ucZtZ76Itw4d3GThZ_CW_6AwAaxtbEDMOxG15o4mg23yaClCpcAY5VQLycQZlEwsTA1XMmCWZvFnQdWmSM43eGJGcHy9A4Cn1YFvHnoNTnAy6vSdjyO_exPLOIbO9FBiArTU-54wDLX2tHJhvR-FmKDCmdyohU2gYD8LnuBJ1LQZwVh1tKiIDwKbCcsaghWGYCCgFTufk)  
  <sub>TradingView, 16 hours ago</sub>  
  The S&P 500 and Dow Jones index ended higher on Tuesday as investors braced for the start of earnings season, with 3M shares helping the Dow and strong...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.06% (-0.03 on the week) | 5-year 4.93% (-0.07 on the week) | 10-year 5.10% (-0.09 on the week) | 30-year 5.41% (-0.11 on the week)
Yield curve, 10-year minus 3-month: +1.04 points -- upward sloping (normal)
US dollar index: 101.77 (-0.78 on the week)
Volatility (VIX): 17.03 (+0.2 on the week) -- elevated
```

</details>

<details><summary><b>Price and chart</b> — score -0.20</summary>

```text
Last close 553.21 (bar of 2026-10-21), from 502 daily bars
Trend: vs 20d SMA 593.20 (-6.7%), 50d 577.49 (-4.2%), 200d 514.03 (+7.6%); 50d above 200d
Momentum: RSI(14) 38.7 | MACD -9.033 vs signal -0.654 (histogram -8.379)
Returns: 1d +1.3% | 5d -2.0% | 1m -8.9% | 3m -4.6%
52-week range: 325.10 - 668.91 (now 66.3% of the way up)
Volatility: ATR(14) 16.44 (3.0% of price) | annualised 20d 26.8%
Volume: 0.42x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.00</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score +0.00</summary>

```text
Fund type: Technology
What it holds: P/E 32.50 | P/B 11.65 | P/S 13.32 | 3y earnings growth n/a
Yield: 0.2%
Three-year record: +56.7% a year | beta to the market 2.00
Cost and size: expense ratio 0.35% | net assets 74.88B
What it is made of: Stocks 100.0%, Cash 0.0%
Largest holdings: NVIDIA Corp 19.3%, Taiwan Semiconductor Manufacturing Co Ltd ADR 9.3%, Advanced Micro Devices Inc 5.5%, Broadcom Inc 5.3%, Micron Technology Inc 4.9%
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
Rolled up from the 5 largest holdings, 44.3% of the fund by weight
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 1.34 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +46.2% above the current prices
Holdings read: NVDA, TSM, AMD, AVGO, MU
Recent rating changes among them:
  - NVDA: 2026-10-01 Cantor Fitzgerald: reit, Overweight -> Overweight
  - TSM: 2026-10-16 Barclays: main, Overweight -> Overweight
  - AMD: 2026-10-21 Susquehanna: main, Positive -> Positive
  - AVGO: 2026-09-10 Piper Sandler: init, ? -> Overweight
  - MU: 2026-10-13 Rosenblatt: main, Buy -> Buy
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
Share count change: 1 week: +0.0% (0.00) over 7d | 1 month: +0.0% (0.00) over 33d
Shares outstanding: 11.67M | fund size: 6.46B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### US real estate (VNQ) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Neutral overall: no macro surprise, technicals lack decisive break, flat fund flows, analyst bullish view limited to 40.5% of fund.

**Main reasons it gave:**
- Flat fund flows: share count unchanged (+0% week, +0% month)
- Technical: price below 50‑day (93.93) and 200‑day (94.49) SMAs, RSI 49.7, no decisive break
- Macro: yields down modestly across curve, normal upward slope (+1.04), no surprise data
- Analyst coverage: 100% buy rating, price target +17.6% above current, covering 40.5% of fund weight

<details><summary><b>News</b> — score +0.00</summary>

- [ETFs Investing in Zillow Group, Inc. Class A Stocks](https://www.tradingview.com/symbols/DUS-0ZG/etfs/)  
  <sub>TradingView, 3 hours ago</sub>  
  Explore funds investing in 0ZG in a single list with price, expense ratio, and more stats for an in-depth analysis of new opportunities.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.06% (-0.03 on the week) | 5-year 4.93% (-0.07 on the week) | 10-year 5.10% (-0.09 on the week) | 30-year 5.41% (-0.11 on the week)
Yield curve, 10-year minus 3-month: +1.04 points -- upward sloping (normal)
US dollar index: 101.77 (-0.78 on the week)
Volatility (VIX): 17.03 (+0.2 on the week) -- elevated
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 91.74 (bar of 2026-10-21), from 502 daily bars
Trend: vs 20d SMA 90.51 (+1.4%), 50d 93.93 (-2.3%), 200d 94.49 (-2.9%); 50d below 200d
Momentum: RSI(14) 49.7 | MACD -0.564 vs signal -1.012 (histogram 0.449)
Returns: 1d -0.6% | 5d +1.5% | 1m -2.0% | 3m -7.0%
52-week range: 87.00 - 100.95 (now 34.0% of the way up)
Volatility: ATR(14) 1.25 (1.4% of price) | annualised 20d 14.0%
Volume: 0.29x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.00</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score +0.00</summary>

```text
Fund type: Real Estate
What it holds: P/E 28.36 | P/B 2.42 | P/S 4.59 | 3y earnings growth n/a
Yield: 3.8%
Three-year record: +11.9% a year | beta to the market 0.98
Cost and size: expense ratio 0.13% | net assets 66.42B
What it is made of: Stocks 99.0%, Cash 0.7%, Other 0.3%
Largest holdings: Vanguard Real Estate II Index 14.5%, Welltower Inc 9.1%, Prologis Inc 6.9%, Equinix Inc 5.7%, American Tower Corp 4.3%
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

<details><summary><b>What analysts and big funds say</b> — score +0.40</summary>

_Not available today._

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score +0.40</summary>

```text
Rolled up from the 5 largest holdings, 40.5% of the fund by weight
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 1.64 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +17.6% above the current prices
Holdings read: VRTPX, WELL, PLD, EQIX, AMT
Recent rating changes among them:
  - WELL: 2026-10-19 Wells Fargo: main, Overweight -> Overweight
  - PLD: 2026-10-21 Raymond James: up, Market Perform -> Outperform
  - EQIX: 2026-10-21 CIBC: init, ? -> Outperformer
  - AMT: 2026-10-20 Bernstein: main, Outperform -> Outperform
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
Share count change: 1 week: +0.0% (0.00) over 7d | 1 month: +0.0% (0.00) over 34d
Shares outstanding: 370.18M | fund size: 33.96B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Biotech (XBI) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Overall neutral view after weighing analyst coverage, fund flows, fundamentals and technicals.

**Main reasons it gave:**
- Fund flows: -5.3% share count over past month (net outflow)
- Analyst coverage thin (9.2% weight) with 61% buy rating and +11.1% price target above current price
- Technicals: price above 20‑day SMA (+1.3%) and MACD histogram positive, but volume at 0.34× 20‑day average
- Macro: yields down slightly, curve upward sloping, VIX at 17.03 (no surprise)

<details><summary><b>News</b> — score +0.00</summary>

- [Biotech ETF (BBH) Hits New 52-Week High](https://finance.yahoo.com/healthcare/articles/biotech-etf-bbh-hits-52-090000473.html)  
  <sub>Yahoo Finance, 6 hours ago</sub>  
  BBH hits a 52-week high as positive Amgen news and strong momentum fuel gains. Can the biotech ETF rally further?
- [Gap Between Market’s 2 Tiers Starts to Close](https://pro.thestreet.com/market-commentary/gap-between-markets-2-tiers-starts-to-close)  
  <sub>TheStreet Pro, 19 hours ago</sub>  
  SpaceX saw beats on both the top and bottom line but is trading flat in front of the conference call.
- [Form 4 iShares Biotechnology ETF For: 20 October By Investing.com](https://za.investing.com/news/stock-market-news/form-4-ishares-biotechnology-etf-for-20-october-93CH-4513569)  
  <sub>Investing.com South Africa, 14 hours ago</sub>  
  The information in this preliminary pricing supplement is not complete and may be changed. This preliminary pricing supplement and the accompanying...
- [I’m Bottom Fishing This Data Center Play the Right Way](https://pro.thestreet.com/trade-ideas/im-bottom-fishing-this-data-center-play-the-right-way)  
  <sub>TheStreet Pro, 20 minutes ago</sub>  
  Market breadth isn't as strong on Wednesday morning as it was on Tuesday, but it is still healthy at about 58% positive. Notably, the number of new 12-month...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.06% (-0.03 on the week) | 5-year 4.93% (-0.07 on the week) | 10-year 5.10% (-0.09 on the week) | 30-year 5.41% (-0.11 on the week)
Yield curve, 10-year minus 3-month: +1.04 points -- upward sloping (normal)
US dollar index: 101.77 (-0.78 on the week)
Volatility (VIX): 17.03 (+0.2 on the week) -- elevated
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 154.28 (bar of 2026-10-21), from 502 daily bars
Trend: vs 20d SMA 152.30 (+1.3%), 50d 157.60 (-2.1%), 200d 140.62 (+9.7%); 50d above 200d
Momentum: RSI(14) 51.8 | MACD -1.960 vs signal -2.296 (histogram 0.336)
Returns: 1d +0.7% | 5d +5.1% | 1m -4.7% | 3m +1.3%
52-week range: 107.32 - 169.55 (now 75.5% of the way up)
Volatility: ATR(14) 4.39 (2.8% of price) | annualised 20d 32.0%
Volume: 0.34x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.10</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score +0.10</summary>

```text
Fund type: Health
What it holds: P/E n/a | P/B 0.21 | P/S 0.12 | 3y earnings growth n/a
Yield: 0.3%
Three-year record: +30.4% a year | beta to the market 1.09
Cost and size: expense ratio 0.35% | net assets 10.36B
What it is made of: Stocks 100.0%, Cash 0.0%
Largest holdings: Twist Bioscience Corp 2.2%, Moderna Inc 2.0%, Natera Inc 1.8%, Iovance Biotherapeutics Inc 1.6%, Amgen Inc 1.5%
Sector mix: Healthcare 99.3%, Financial services 0.7%
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

<details><summary><b>What analysts and big funds say</b> — score +0.25</summary>

_Not available today._

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score +0.25</summary>

```text
Rolled up from the 5 largest holdings, 9.2% of the fund by weight  -- thin, so read this as a fact about that slice rather than the fund
Ratings by weight: buy 61.1% | hold 38.9% | sell 0.0% (mean 2.09 on a 1=strong buy to 5=strong sell scale)
Weighted price target: -11.1% above the current prices
Holdings read: TWST, MRNA, NTRA, IOVA, AMGN
Recent rating changes among them:
  - TWST: 2026-10-13 TD Cowen: main, Buy -> Buy
  - MRNA: 2026-10-15 Goldman Sachs: main, Neutral -> Neutral
  - NTRA: 2026-10-19 Canaccord Genuity: main, Buy -> Buy
  - IOVA: 2026-10-13 Barclays: main, Overweight -> Overweight
  - AMGN: 2026-10-21 Barclays: main, Equal-Weight -> Equal-Weight
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
Share count change: 1 week: +4.0% (414.30M) over 7d | 1 month: -5.3% (-605.61M) over 32d
Shares outstanding: 70.06M | fund size: 10.81B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### US house builders (XHB) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Neutral overall as housing sector weakness, technical downside, but positive inflows and bullish analyst view (thin coverage) offset each other

**Main reasons it gave:**
- Weak housing starts and pending home sales this week indicating sector pressure
- ETF price 95.89 below 50‑day SMA 99.81 and 200‑day SMA 105.52, low volume
- Share count up +10.4% over past month (137.49M) showing net inflows
- Analyst coverage of top holdings (17% weight) shows 100% buy and +17.9% price target (bullish but thin)

<details><summary><b>News</b> — score +0.00</summary>

- [My Research](https://www.bespokepremium.com/interactive/posts/think-big-blog/builders-firstsource-bldr-dream-finders-homes-dfh-highlight-pain-for-homebuilders)  
  <sub>Bespoke Investment Group, 18 hours ago</sub>  
  The housing industry continues to struggle from the weight of high interest rates as data like Housing Starts and Pending Home Sales have shown this week.
- [Builders FirstSource, Dream Finders Homes Highlight Pain For Homebuilders](https://seekingalpha.com/article/4955715-builders-firstsource-dream-finders-homes-highlight-pain-for-homebuilders)  
  <sub>Seeking Alpha, 12 hours ago</sub>  
  The S&P Homebuilders ETF, which contains homebuilders, building products, home improvement, and home furnishing and appliance companies, just made new...
- [Direxion Daily Semiconductor Bull 3X Shares (SOXL) Stock Price, News, Quote & History](https://ca.finance.yahoo.com/quote/SOXL/)  
  <sub>Yahoo! Finance Canada, 4 hours ago</sub>  
  Find the latest Direxion Daily Semiconductor Bull 3X Shares (SOXL) stock quote, history, news and other vital information to help you with your stock...
- [Housing Is Weak, but Its Impact on the Business Cycle Is Muted](https://au.investing.com/analysis/housing-is-weak-but-its-impact-on-the-business-cycle-is-muted-200617771)  
  <sub>Investing.com Australia, 3 hours ago</sub>  
  Market Analysis by covering: State Street® SPDR® S&P® Homebuilders ETF, Federal Home Loan Mortgage Corp. Read 's Market Analysis on Investing.com AU.
- [Builders FirstSource, Dream Finders Homes Highlight Pain For Homebuilders - TalkMarkets](https://t.co/Iv57SrTIrk)  
  <sub>Howl.link, 18 hours ago</sub>  
  XHB hit 52-week lows as high interest rates batter the housing sector.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.06% (-0.03 on the week) | 5-year 4.93% (-0.07 on the week) | 10-year 5.10% (-0.09 on the week) | 30-year 5.41% (-0.11 on the week)
Yield curve, 10-year minus 3-month: +1.04 points -- upward sloping (normal)
US dollar index: 101.77 (-0.78 on the week)
Volatility (VIX): 17.03 (+0.2 on the week) -- elevated
```

</details>

<details><summary><b>Price and chart</b> — score -0.30</summary>

```text
Last close 95.89 (bar of 2026-10-21), from 502 daily bars
Trend: vs 20d SMA 95.82 (+0.1%), 50d 99.81 (-3.9%), 200d 105.52 (-9.1%); 50d below 200d
Momentum: RSI(14) 47.2 | MACD -1.233 vs signal -1.565 (histogram 0.333)
Returns: 1d -0.3% | 5d +3.3% | 1m -3.5% | 3m -10.1%
52-week range: 92.84 - 121.36 (now 10.7% of the way up)
Volatility: ATR(14) 2.13 (2.2% of price) | annualised 20d 21.7%
Volume: 0.22x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score -0.10</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score -0.10</summary>

```text
Fund type: Consumer Cyclical
What it holds: P/E 18.56 | P/B 2.09 | P/S 1.23 | 3y earnings growth n/a
Yield: 1.2%
Three-year record: +10.5% a year | beta to the market 1.48
Cost and size: expense ratio 0.35% | net assets 1.43B
What it is made of: Stocks 99.9%, Cash 0.1%
Largest holdings: SharkNinja Inc 3.5%, Cavco Industries Inc 3.4%, Champion Homes Inc 3.4%, Johnson Controls International PLC Registered Shares 3.4%, Wayfair Inc Class A 3.4%
Sector mix: Consumer cyclical 63.4%, Industrials 31.7%, Basic materials 3.2%, Real estate 1.8%
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

<details><summary><b>What analysts and big funds say</b> — score +0.30</summary>

_Not available today._

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score +0.30</summary>

```text
Rolled up from the 5 largest holdings, 17.0% of the fund by weight  -- thin, so read this as a fact about that slice rather than the fund
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 1.79 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +17.9% above the current prices
Holdings read: SN, CVCO, SKY, JCI, W
Recent rating changes among them:
  - SN: 2026-10-19 JP Morgan: main, Overweight -> Overweight
  - CVCO: 2026-09-30 Oppenheimer: init, ? -> Outperform
  - SKY: 2026-10-15 RBC Capital: main, Outperform -> Outperform
  - JCI: 2026-10-15 Mizuho: main, Neutral -> Neutral
  - W: 2026-10-20 Piper Sandler: main, Overweight -> Overweight
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
Share count change: 1 week: +0.7% (9.76M) over 7d | 1 month: +10.4% (137.49M) over 32d
Shares outstanding: 15.19M | fund size: 1.46B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### US media and communication (XLC) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Neutral overall – no macro surprise, technicals are weak but not decisive, modest inflows, and bullish analyst view not enough to outweigh lack of catalyst.

**Main reasons it gave:**
- Macro: yields down slightly, normal upward curve, no surprise data
- Technical: price below 20d/50d/200d SMAs, RSI 42.2, MACD negative, low volume
- Fund flows: modest net inflows (+0.2% week, +3.0% month) indicating limited demand
- Analyst view: 90.6% buy, weighted price target +19.3% above price but no macro catalyst

<details><summary><b>News</b> — score +0.00</summary>

- [Netflix Sinks 7% as Soft Q4 Outlook Sparks Wave of Price Target Cuts; Spotify Slips, Disney Holds Steady](https://247wallst.com/investing/2026/10/21/netflix-sinks-7-as-soft-q4-outlook-sparks-wave-of-price-target-cuts-spotify-slips-disney-holds-steady/)  
  <sub>24/7 Wall St., 2 hours ago</sub>  
  A Q4 2026 revenue forecast that fell short of Wall Street's expectations is overshadowing an earnings beat at Netflix (NASDAQ:NFLX | NFLX Price Prediction),...
- [Skydance Rises 5% as Steep Post-Merger Slide Pauses; Disney Gains 2%, Netflix Slips](https://finance.yahoo.com/markets/stocks/articles/skydance-rises-5-steep-post-180340100.html)  
  <sub>Yahoo Finance, 21 hours ago</sub>  
  Skydance (SKYD) surged 5% to $7.15, pausing a steep post-merger slide, while Disney (DIS) added a softer 2% to $111.41. XLC gained just 0.1% and SPY rose...
- [Defensive rotation: Quality over sector labels in healthcare, banks, and consumer staples (XLV:NYSEARCA)](https://seekingalpha.com/news/4654645-defensive-rotation-quality-over-sector-labels-in-healthcare-banks-and-consumer-staples)  
  <sub>Seeking Alpha, 20 hours ago</sub>  
  Defensive sector rotation is underway—focus on quality healthcare, banks & staples with cash flow, valuation and earnings support.
- [Health Care Stocks Hit Record Highs, GM Drops Nearly 8%: Stock Market Today](https://www.tradingview.com/news/benzinga:1285d9920094b:0-health-care-stocks-hit-record-highs-gm-drops-nearly-8-stock-market-today/)  
  <sub>TradingView, 22 hours ago</sub>  
  Health care stocks climbed to record highs by midday Tuesday, with defensives and small caps leading a recovery from an early dip as the Nasdaq 100 stalled.
- [AT&T Sinks 5% Despite Q3 Beat and Raised Outlook; Verizon and T-Mobile Drop 3%](https://247wallst.com/investing/2026/10/21/att-sinks-5-despite-q3-beat-and-raised-outlook-verizon-and-t-mobile-drop-3/)  
  <sub>24/7 Wall St., 2 hours ago</sub>  
  AT&T sank 7% despite beating Q3 revenue and raising its full-year profit outlook, while Verizon and T-Mobile each fell 3%. SpaceX agreed to buy a nationwide...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.06% (-0.03 on the week) | 5-year 4.93% (-0.07 on the week) | 10-year 5.10% (-0.09 on the week) | 30-year 5.41% (-0.11 on the week)
Yield curve, 10-year minus 3-month: +1.04 points -- upward sloping (normal)
US dollar index: 101.77 (-0.78 on the week)
Volatility (VIX): 17.03 (+0.2 on the week) -- elevated
```

</details>

<details><summary><b>Price and chart</b> — score -0.20</summary>

```text
Last close 109.19 (bar of 2026-10-21), from 502 daily bars
Trend: vs 20d SMA 111.23 (-1.8%), 50d 111.81 (-2.3%), 200d 113.39 (-3.7%); 50d below 200d
Momentum: RSI(14) 42.2 | MACD -0.490 vs signal -0.281 (histogram -0.209)
Returns: 1d -0.9% | 5d -1.5% | 1m -3.8% | 3m +3.6%
52-week range: 105.38 - 120.08 (now 26.0% of the way up)
Volatility: ATR(14) 1.70 (1.6% of price) | annualised 20d 16.2%
Volume: 0.41x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.30</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score +0.30</summary>

```text
Fund type: Communications
What it holds: P/E 16.28 | P/B 3.24 | P/S 2.42 | 3y earnings growth n/a
Yield: 1.2%
Three-year record: +19.3% a year | beta to the market 0.85
Cost and size: expense ratio 0.08% | net assets 22.53B
What it is made of: Stocks 99.8%, Cash 0.2%
Largest holdings: Meta Platforms Inc Class A 22.2%, Alphabet Inc Class A 11.6%, Alphabet Inc Class C 9.3%, Warner Bros. Discovery Inc Ordinary Shares - Class A 4.9%, The Walt Disney Co 4.5%
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
Ratings by weight: buy 90.6% | hold 9.4% | sell 0.0% (mean 1.52 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +19.3% above the current prices
Holdings read: META, GOOGL, GOOG, WBD, DIS
Recent rating changes among them:
  - META: 2026-10-20 Rosenblatt: main, Buy -> Buy
  - GOOGL: 2026-10-20 BMO Capital: main, Outperform -> Outperform
  - GOOG: 2026-10-15 JP Morgan: main, Overweight -> Overweight
  - WBD: 2026-09-29 Argus Research: down, Hold -> Sell
  - DIS: 2026-10-16 Citigroup: main, Buy -> Buy
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
Share count change: 1 week: +0.2% (50.73M) over 7d | 1 month: +3.0% (658.80M) over 32d
Shares outstanding: 204.57M | fund size: 22.34B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### US energy companies (XLE) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:** no explanation. It wrote only “NEUTRAL”, so the main reasons below are all it gave.

**Main reasons it gave:**
- Analyst view: 100% buy, weighted price target +0.8% above current price
- Fund flows: share count unchanged (+0.0% week, +0.0% month)
- EIA price outlook: WTI forecast down 14% over six months, indicating bearish pressure
- Technicals: price near 52‑week high (99.7% of range) with low volume (0.30x 20‑day avg), no decisive breakout

<details><summary><b>News</b> — score +0.00</summary>

- [Energy ETFs: How to Play the Sector's Surge](https://es.tradingview.com/news/zacks:4d0ab9783094b:0-energy-etfs-how-to-play-the-sector-s-surge/)  
  <sub>TradingView, 21 hours ago</sub>  
  Energy is the best-performing sector this year, up about 53%, significantly ahead of the second-best performer, information technology, which has gained...
- [Cruise Stocks Rally While Energy Shares Slip: Norwegian, Royal Caribbean and Carnival Rise 3%](https://247wallst.com/investing/2026/10/20/cruise-stocks-rally-while-energy-shares-slip-norwegian-royal-caribbean-and-carnival-rise-3/)  
  <sub>24/7 Wall St., 21 hours ago</sub>  
  Cruise stocks are surging together while energy shares slip, and the gap between those two moves tells a story about what it actually costs to sail a...
- [What State Street Energy SPDR (XLE) Bought: Exxon Mobil Leads on Oct. 19](https://finance.yahoo.com/energy/articles/state-street-energy-spdr-xle-110444973.html)  
  <sub>Yahoo Finance, 4 hours ago</sub>  
  This article first appeared on GuruFocus. State Street Energy Select Sector SPDR ETF (XLE) added to every one of its holdings on Monday, with no positions...
- [Two Tactical ETFs For Collecting High Income From High Oil And Commodity Prices](https://seekingalpha.com/article/4955873-two-tactical-etfs-for-collecting-high-income-from-high-oil-and-commodity-prices)  
  <sub>Seeking Alpha, 2 hours ago</sub>  
  I focus on high-yield income ETFs XLEI and FTGC for tactical portfolio allocation amid rising energy and commodity prices.
- [IYE: The iShares U.S. Energy ETF Offers Broad Sector Exposure (NYSEARCA:IYE)](https://seekingalpha.com/article/4955621-iye-ishares-us-energy-etf-offers-broad-sector-exposure)  
  <sub>Seeking Alpha, 20 hours ago</sub>  
  Explore iShares IYE ETF: Russell 1000 Energy exposure, Exxon/Chevron weight, refiners growth, returns vs SPY and tax perks.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.06% (-0.03 on the week) | 5-year 4.93% (-0.07 on the week) | 10-year 5.10% (-0.09 on the week) | 30-year 5.41% (-0.11 on the week)
Yield curve, 10-year minus 3-month: +1.04 points -- upward sloping (normal)
US dollar index: 101.77 (-0.78 on the week)
Volatility (VIX): 17.03 (+0.2 on the week) -- elevated
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 68.17 (bar of 2026-10-21), from 502 daily bars
Trend: vs 20d SMA 64.79 (+5.2%), 50d 64.04 (+6.4%), 200d 57.95 (+17.6%); 50d above 200d
Momentum: RSI(14) 67.4 | MACD 1.366 vs signal 0.995 (histogram 0.371)
Returns: 1d +0.3% | 5d +0.8% | 1m +10.3% | 3m +14.8%
52-week range: 43.35 - 68.24 (now 99.7% of the way up)
Volatility: ATR(14) 1.28 (1.9% of price) | annualised 20d 19.0%
Volume: 0.30x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score -0.30</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score -0.30</summary>

```text
Fund type: Equity Energy
What it holds: P/E 17.51 | P/B 2.47 | P/S 1.70 | 3y earnings growth n/a
Yield: 2.5%
Three-year record: +17.5% a year | beta to the market -0.03
Cost and size: expense ratio 0.08% | net assets 39.13B
What it is made of: Stocks 99.8%, Cash 0.2%
Largest holdings: ExxonMobil Holdings Corp 24.0%, Chevron Corp 18.1%, ConocoPhillips 6.7%, Valero Energy Corp 4.7%, Marathon Petroleum Corp 4.7%
Sector mix: Energy 100.0%
```

</details>

<details><summary><b>Does this company beat its own forecasts</b> — score -0.30</summary>

_Not available today._

</details>

<details><summary><b>What holding this fund costs you</b> — score -0.30</summary>

_Not available today._

</details>

<details><summary><b>How much oil and gas is in storage</b> — score -0.30</summary>

```text
US inventories, week ending 2026-10-09 (published the following Wednesday)
  Crude oil: 415.6 million barrels, -8.6 on the week (a draw), 15% percentile over 52 weeks
  Petrol: 208.3 million barrels, +3.5 on the week (a build), 21% percentile over 52 weeks
  Diesel: 102.6 million barrels, -2.5 on the week (a draw), 12% percentile over 52 weeks -- low for the time of year
  Natural gas: 3,567.0 billion cubic feet, +67.0 on the week (a build), 83% percentile over 52 weeks
A build is more supply than demand and a draw is the reverse, so a build reads bearish and a draw bullish -- as a rule of thumb, not a law. Weigh the change and how unusual the level is above the level itself, and remember the market has already seen this number.
```

</details>

<details><summary><b>How the crop is growing</b> — score -0.30</summary>

_Not available today._

</details>

<details><summary><b>What analysts and big funds say</b> — score +0.30</summary>

_Not available today._

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score +0.30</summary>

```text
Rolled up from the 5 largest holdings, 58.2% of the fund by weight
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 2.12 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +0.8% above the current prices
Holdings read: XOM, CVX, COP, VLO, MPC
Recent rating changes among them:
  - XOM: 2026-10-19 Barclays: main, Overweight -> Overweight
  - CVX: 2026-10-15 Morgan Stanley: main, Overweight -> Overweight
  - COP: 2026-10-20 Susquehanna: main, Positive -> Positive
  - VLO: 2026-10-14 Wells Fargo: main, Overweight -> Overweight
  - MPC: 2026-10-14 Wells Fargo: main, Overweight -> Overweight
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
Shares outstanding: 186.42M | fund size: 12.71B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### US banks and finance (XLF) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:** no explanation. It wrote only “NEUTRAL”, so the main reasons below are all it gave.

**Main reasons it gave:**
- Flat fund flows (0% change) indicating no net demand
- No macro surprise in yields, inflation, or policy data
- Technical indicators modestly bullish but low volume and no decisive break
- Analyst view bullish but only covers 42.7% of the fund

<details><summary><b>News</b> — score +0.00</summary>

- [Financial Select Sector SPDR (XLF) Sells Berkshire and JPMorgan on Monday](https://finance.yahoo.com/markets/stocks/articles/financial-select-sector-spdr-xlf-110404112.html)  
  <sub>Yahoo Finance, 4 hours ago</sub>  
  This article first appeared on GuruFocus. Financial Select Sector SPDR ETF (XLF) was the sole mover in Monday's session, with ETF activity showing $446.0...
- [Exchange-Traded Funds, Equity Futures Higher Pre-Bell Wednesday as AI Stocks Rebound Amid Corporate Earnings](https://finance.yahoo.com/markets/stocks/articles/exchange-traded-funds-equity-futures-131151383.html)  
  <sub>Yahoo Finance, 2 hours ago</sub>  
  The broad market exchange-traded fund SPDR S&P 500 ETF Trust (SPY) was up 0.2% and the actively trad.
- [ETFs Are Net Sellers of Wells Fargo (WFC) on Oct. 19](https://www.gurufocus.com/news/9133578/etfs-are-net-sellers-of-wells-fargo-wfc-on-oct-19)  
  <sub>GuruFocus, 4 hours ago</sub>  
  XLF led the move as ETF activity turned negative on Wells Fargo (WFC) in Monday's session, with a net $15.4 million sold. More funds traded the other way,...
- [The Pivot: CoinShares Survey Suggests Crypto Investing No Longer for Speculation...It's Strategic!](https://www.advisorperspectives.com/webinars/2026/11/17/the-pivot-coinshares-survey-suggests-crypto-investing-no-longer-for-speculation-its-strategic?partnerref=APSidebar)  
  <sub>Advisor Perspectives, 23 hours ago</sub>  
  Crypto is pivoting from a speculative asset into a strategic allocation. A recent CoinShares survey shows that cryptocurrency is increasingly viewed as a...
- [Defensive rotation: Quality over sector labels in healthcare, banks, and consumer staples (XLV:NYSEARCA)](https://seekingalpha.com/news/4654645-defensive-rotation-quality-over-sector-labels-in-healthcare-banks-and-consumer-staples)  
  <sub>Seeking Alpha, 20 hours ago</sub>  
  Defensive sector rotation is underway—focus on quality healthcare, banks & staples with cash flow, valuation and earnings support.
- [ETFs Are Net Sellers of Mastercard (MA) on Monday](https://www.gurufocus.com/news/9133564/etfs-are-net-sellers-of-mastercard-ma-on-monday)  
  <sub>GuruFocus, 4 hours ago</sub>  
  XLF led the move, cutting its Mastercard (MA) position by $28.7 million on Monday as ETF activity turned negative. Eighteen ETFs sold shares while 28 bought...
- [Bank Stocks Fell 13% to 14% in the Month Before Q3 Earnings](https://www.openingbelldailynews.com/p/bank-stocks-fall-before-q3-2026-earnings-chart)  
  <sub>Opening Bell Daily, 3 hours ago</sub>  
  Every big bank stock fell in the month before Q3 2026 earnings, with Bank of America, Goldman and Morgan Stanley down 13% to 14% as the S&P 500 rose.
- [Health Care Stocks Hit Record Highs, GM Drops Nearly 8%: Stock Market Today](https://www.tradingview.com/news/benzinga:1285d9920094b:0-health-care-stocks-hit-record-highs-gm-drops-nearly-8-stock-market-today/)  
  <sub>TradingView, 22 hours ago</sub>  
  Health care stocks climbed to record highs by midday Tuesday, with defensives and small caps leading a recovery from an early dip as the Nasdaq 100 stalled.
- [Product Due Diligence Session: How Midstream/MLPs Benefit from Booming LNG Exports | ETF Trends](https://www.advisorperspectives.com/webinars/2026/11/10/how-midstream-mlps-benefit-from-booming-lng-exports?partnerref=APSidebar)  
  <sub>Advisor Perspectives, 24 hours ago</sub>  
  Interruptions to energy flows from the Middle East have reinforced the importance of North American energy exports, particularly liquefied natural gas (LNG)...
- [Sector Update: Financial Stocks Higher Late Afternoon](https://finance.yahoo.com/markets/stocks/articles/sector-financial-stocks-higher-afternoon-195815872.html)  
  <sub>Yahoo Finance, 19 hours ago</sub>  
  Financial stocks were advancing in late Tuesday trading, with the NYSE Financial Index rising 1% and the State Street Financial Select Sector SPDR ETF (XLF)...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.06% (-0.03 on the week) | 5-year 4.93% (-0.07 on the week) | 10-year 5.10% (-0.09 on the week) | 30-year 5.41% (-0.11 on the week)
Yield curve, 10-year minus 3-month: +1.04 points -- upward sloping (normal)
US dollar index: 101.77 (-0.78 on the week)
Volatility (VIX): 17.03 (+0.2 on the week) -- elevated
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 56.01 (bar of 2026-10-21), from 502 daily bars
Trend: vs 20d SMA 54.52 (+2.7%), 50d 56.15 (-0.3%), 200d 53.69 (+4.3%); 50d above 200d
Momentum: RSI(14) 58.3 | MACD -0.074 vs signal -0.366 (histogram 0.293)
Returns: 1d +0.5% | 5d +2.7% | 1m +2.2% | 3m +0.3%
52-week range: 47.81 - 58.56 (now 76.2% of the way up)
Volatility: ATR(14) 0.69 (1.2% of price) | annualised 20d 11.8%
Volume: 0.25x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.25</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score +0.25</summary>

```text
Fund type: Financial
What it holds: P/E 15.21 | P/B 2.25 | P/S 3.26 | 3y earnings growth n/a
Yield: 1.6%
Three-year record: +20.8% a year | beta to the market 0.75
Cost and size: expense ratio 0.08% | net assets 50.97B
What it is made of: Stocks 99.9%, Cash 0.1%
Largest holdings: Berkshire Hathaway Inc Class B 12.3%, JPMorgan Chase & Co 11.7%, Visa Inc Class A 8.1%, Mastercard Inc Class A 5.9%, Bank of America Corp 4.7%
Sector mix: Financial services 98.2%, Technology 1.6%, Industrials 0.2%
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
Rolled up from the 5 largest holdings, 42.7% of the fund by weight
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 1.77 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +7.9% above the current prices
Holdings read: BRK-B, JPM, V, MA, BAC
Recent rating changes among them:
  - BRK-B: 2026-08-10 UBS: main, Buy -> Buy
  - JPM: 2026-10-15 Citigroup: main, Neutral -> Neutral
  - V: 2026-10-12 Baird: main, Outperform -> Outperform
  - MA: 2026-10-09 Baird: main, Outperform -> Outperform
  - BAC: 2026-10-15 Citigroup: main, Buy -> Buy
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
Shares outstanding: 883.44M | fund size: 49.48B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### US industry (XLI) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Neutral overall: analyst view is strongly bullish (+25.5% price target) but technicals show price below key moving averages and modest RSI, fund flows are flat indicating no net demand shift, macro data show only slight yield uptick and no surprise, and fundamentals are mixed with high valuation offset by strong recent performance. No material macro surprise or decisive technical break justifies a directional bias.

**Main reasons it gave:**
- Analyst view: 100% buy rating with +25.5% price target (bullish)
- Technicals: price below 20‑day, 50‑day, 200‑day SMAs; RSI 43.5 (slightly bearish)
- Fund flows: flat, no net creations/redemptions (neutral demand)
- Macro: yields up slightly, upward sloping curve, VIX moderate (no surprise)
- Fundamentals: high valuation (P/E 27.4) but strong 3‑year performance (+20.3%/yr) (mixed)

<details><summary><b>News</b> — score +0.00</summary>

- [Exchange-Traded Funds, Equity Futures Higher Pre-Bell Wednesday as AI Stocks Rebound Amid Corporate Earnings](https://finance.yahoo.com/markets/stocks/articles/exchange-traded-funds-equity-futures-131151383.html)  
  <sub>Yahoo Finance, 2 hours ago</sub>  
  The broad market exchange-traded fund SPDR S&P 500 ETF Trust (SPY) was up 0.2% and the actively trad.
- [Cyclicals Top Sectors In Wednesday Trading As Defensives Trail](https://www.benzinga.com/etfs/sector-etfs/26/10/62499965/cyclicals-top-sectors-in-wednesday-trading-as-defensives-trail)  
  <sub>Benzinga, 22 minutes ago</sub>  
  Five sectors are higher and six are lower in Wednesday's regular session, with cyclical sectors holding two of the top three positions alongside Technology.
- [American Airlines, Alaska Air lead list of undervalued industrial stocks (XLI:NYSEARCA)](https://seekingalpha.com/news/4655108-american-airlines-alaska-air-lead-list-of-undervalued-industrial-stocks)  
  <sub>Seeking Alpha, 3 hours ago</sub>  
  Q3 2026 industrials earnings: screen 14 undervalued stocks (AAL, ALK, SARO, UPS) with Seeking Alpha valuation grades—see the list and act now.
- [State Street Technology Select Sector SPDR ETF (XLK) Stock Price Today: $187.25](https://pluang.com/en/asset/usstock/XLK/10985)  
  <sub>Pluang, 22 hours ago</sub>  
  About State Street Technology Select Sector SPDR ETF ... XLK tracks the Technology Select Sector Index, providing targeted exposure to the largest and most...
- [State Street Utilities Select Sector SPDR ETF (XLU) Stock Price, News, Quote & History](https://ca.finance.yahoo.com/quote/XLU/)  
  <sub>Yahoo! Finance Canada, 17 hours ago</sub>  
  Find the latest State Street Utilities Select Sector SPDR ETF (XLU) stock quote, history, news and other vital information to help you with your stock...
- [Backlogs For Industrials Are Rising Going Into Earnings (NYSEARCA:XLI)](https://seekingalpha.com/article/4955544-backlogs-for-industrials-are-rising-going-into-earnings)  
  <sub>Seeking Alpha, 23 hours ago</sub>  
  Industrials (XLI) show strong demand, rising backlogs, and improving factory data ahead of earnings.
- [Bank of Nova Scotia Launches Auto-Callable Notes Linked to DJIA, Russell 2000, and XLK ETF with Maturity in 2030](https://kalkinemedia.com/us/news/announcements/bank-of-nova-scotia-launches-auto-callable-notes-linked-to-djia-russell-2000-and-xlk-etf-with-maturity-in-2030)  
  <sub>Kalkine Media, 18 hours ago</sub>  
  On October 20, 2026, the Bank of Nova Scotia filed a free writing prospectus for a term sheet featuring principal-at-risk, auto-callable securities tied to...
- [Exchange-Traded Funds Gain as US Equities Advance After Midday](https://finance.yahoo.com/markets/stocks/articles/exchange-traded-funds-gain-us-171124946.html)  
  <sub>Yahoo Finance, 22 hours ago</sub>  
  Broad Market Indicators Broad-market exchange-traded funds IWM and IVV rose. Actively traded Invesco QQQ Trust (QQQ) was little changed, erasing earlier...
- [Another Sentiment Indicator Shows a Bearish Turn](https://realmoney.thestreet.com/trade-ideas/another-sentiment-indicator-shows-a-bearish-turn)  
  <sub>RealMoney Pro, 17 hours ago</sub>  
  The tech stocks are due for an oversold rally. Sentiment remains complacent, but more bears are joining the fray.
- [The Pivot: CoinShares Survey Suggests Crypto Investing No Longer for Speculation...It's Strategic!](https://www.advisorperspectives.com/webinars/2026/11/17/the-pivot-coinshares-survey-suggests-crypto-investing-no-longer-for-speculation-its-strategic?partnerref=APSidebar)  
  <sub>Advisor Perspectives, 23 hours ago</sub>  
  Crypto is pivoting from a speculative asset into a strategic allocation. A recent CoinShares survey shows that cryptocurrency is increasingly viewed as a...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.06% (-0.03 on the week) | 5-year 4.93% (-0.07 on the week) | 10-year 5.10% (-0.09 on the week) | 30-year 5.41% (-0.11 on the week)
Yield curve, 10-year minus 3-month: +1.04 points -- upward sloping (normal)
US dollar index: 101.77 (-0.78 on the week)
Volatility (VIX): 17.03 (+0.2 on the week) -- elevated
```

</details>

<details><summary><b>Price and chart</b> — score -0.20</summary>

```text
Last close 167.87 (bar of 2026-10-21), from 502 daily bars
Trend: vs 20d SMA 168.59 (-0.4%), 50d 173.03 (-3.0%), 200d 173.11 (-3.0%); 50d below 200d
Momentum: RSI(14) 43.5 | MACD -1.406 vs signal -1.544 (histogram 0.138)
Returns: 1d +0.6% | 5d +0.5% | 1m -1.4% | 3m -7.7%
52-week range: 147.83 - 186.51 (now 51.8% of the way up)
Volatility: ATR(14) 2.47 (1.5% of price) | annualised 20d 13.4%
Volume: 0.39x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.00</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score +0.00</summary>

```text
Fund type: Industrials
What it holds: P/E 27.43 | P/B 6.56 | P/S 2.92 | 3y earnings growth n/a
Yield: 1.1%
Three-year record: +20.3% a year | beta to the market 1.01
Cost and size: expense ratio 0.08% | net assets 29.83B
What it is made of: Stocks 99.9%, Cash 0.1%
Largest holdings: Caterpillar Inc 7.0%, GE Aerospace 6.1%, GE Vernova Inc 4.8%, RTX Corp 4.7%, Deere & Co 3.2%
Sector mix: Industrials 93.4%, Technology 6.1%, Basic materials 0.3%, Consumer cyclical 0.2%
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
Rolled up from the 5 largest holdings, 25.7% of the fund by weight
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 1.76 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +25.5% above the current prices
Holdings read: CAT, GE, GEV, RTX, DE
Recent rating changes among them:
  - CAT: 2026-10-14 Oppenheimer: main, Outperform -> Outperform
  - GE: 2026-10-21 Susquehanna: main, Positive -> Positive
  - GEV: 2026-10-14 Susquehanna: main, Positive -> Positive
  - RTX: 2026-10-21 Barclays: main, Overweight -> Overweight
  - DE: 2026-10-08 JP Morgan: main, Neutral -> Neutral
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
Shares outstanding: 136.63M | fund size: 22.94B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### US technology (XLK) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Neutral overall: no macro surprise, flat fund flows, mixed technical signals, and bullish analyst view not enough to shift direction.

**Main reasons it gave:**
- Flat fund flows: share count unchanged (+0.0% week, +0.0% month)
- Analyst view: 100% buy rating, weighted price target +24.2% above price
- Technical: price below 20‑day SMA (194.46) and 50‑day SMA (189.91), MACD negative, RSI 42.9, low volume
- Macro: yields down across curve, dollar index -0.78, VIX stable at 17.03

<details><summary><b>News</b> — score +0.00</summary>

- [State Street Tech Select SPDR (XLK) Adds NVIDIA and Apple on Oct. 19](https://finance.yahoo.com/markets/stocks/articles/state-street-tech-select-spdr-110359928.html)  
  <sub>Yahoo Finance, 4 hours ago</sub>  
  This article first appeared on GuruFocus. State Street Technology Select Sector SPDR ETF (XLK) recorded net buying of $474.0 million on Monday,...
- [Cyclicals Top Sectors In Wednesday Trading As Defensives Trail](https://www.benzinga.com/etfs/sector-etfs/26/10/62499965/cyclicals-top-sectors-in-wednesday-trading-as-defensives-trail)  
  <sub>Benzinga, 19 minutes ago</sub>  
  Five sectors are higher and six are lower in Wednesday's regular session, with cyclical sectors holding two of the top three positions alongside Technology.
- [DRAM ETF Heads For Longest Weekly Losing Streak Since Inception, Roundhill CEO Says ‘Investor Sentiment Has Turned’](https://stocktwits.com/news-articles/markets/equity/dram-etf-record-weekly-losing-streak-roundhill-ceo-investor-sentiment-has-turned/cZxhcl7RBrQ)  
  <sub>Stocktwits, 14 hours ago</sub>  
  The Roundhill Memory ETF (DRAM) was on track for its longest losing streak since inception on Thursday, even as Round Hill Investments CEO Dave Maza said...
- [State Street Technology Select Sector SPDR ETF (XLK) Stock Price Today: $187.25](https://pluang.com/en/asset/usstock/XLK/10985)  
  <sub>Pluang, 22 hours ago</sub>  
  About State Street Technology Select Sector SPDR ETF ... XLK tracks the Technology Select Sector Index, providing targeted exposure to the largest and most...
- [Bank of Nova Scotia Launches Auto-Callable Notes Linked to DJIA, Russell 2000, and XLK ETF with Maturity in 2030](https://kalkinemedia.com/us/news/announcements/bank-of-nova-scotia-launches-auto-callable-notes-linked-to-djia-russell-2000-and-xlk-etf-with-maturity-in-2030)  
  <sub>Kalkine Media, 18 hours ago</sub>  
  On October 20, 2026, the Bank of Nova Scotia filed a free writing prospectus for a term sheet featuring principal-at-risk, auto-callable securities tied to...
- [(XLK) Price Dynamics and Execution-Aware Positioning](https://news.stocktradersdaily.com/news_release/150/XLK_Price_Dynamics_and_Execution-Aware_Positioning_102026032601_1792524361.html)  
  <sub>Stock Traders Daily, 24 hours ago</sub>  
  Price-action only: Technology Select Sector Spdr Etf (XLK) movements set the tone for institutional models. (XLK) Price Dynamics and Execution-Aware...
- [Sector Update: Tech Stocks Mixed Late Afternoon](https://ca.finance.yahoo.com/news/sector-tech-stocks-mixed-afternoon-194226083.html)  
  <sub>Yahoo! Finance Canada, 20 hours ago</sub>  
  Tech stocks were mixed late Tuesday afternoon, with the State Street Technology Select Sector SPDR ETF (XLK) fractionally lower and the State Street SPDR...
- [VOOV: A Solid Value ETF, But Choose MGV Instead For Greater Returns And Stability](https://seekingalpha.com/article/4955602-voov-a-solid-value-etf-but-choose-mgv-instead-for-greater-returns-and-stability)  
  <sub>Seeking Alpha, 21 hours ago</sub>  
  MGV vs VOOV: why Vanguard Mega Cap Value ETF may be the better value pick—cheaper P/E and higher yield with less reconstitution risk.
- [Health Care Stocks Hit Record Highs, GM Drops Nearly 8%: Stock Market Today](https://www.benzinga.com/markets/equities/26/10/62475717/health-care-stocks-hit-record-highs-gm-drops-nearly-8-stock-market-today)  
  <sub>Benzinga, 22 hours ago</sub>  
  Health care stocks climbed to record highs by midday Tuesday, with defensives and small caps leading a recovery from an early dip.
- [Defensive rotation: Quality over sector labels in healthcare, banks, and consumer staples (XLV:NYSEARCA)](https://seekingalpha.com/news/4654645-defensive-rotation-quality-over-sector-labels-in-healthcare-banks-and-consumer-staples)  
  <sub>Seeking Alpha, 20 hours ago</sub>  
  Defensive sector rotation is underway—focus on quality healthcare, banks & staples with cash flow, valuation and earnings support.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.06% (-0.03 on the week) | 5-year 4.93% (-0.07 on the week) | 10-year 5.10% (-0.09 on the week) | 30-year 5.41% (-0.11 on the week)
Yield curve, 10-year minus 3-month: +1.04 points -- upward sloping (normal)
US dollar index: 101.77 (-0.78 on the week)
Volatility (VIX): 17.03 (+0.2 on the week) -- elevated
```

</details>

<details><summary><b>Price and chart</b> — score -0.20</summary>

```text
Last close 187.72 (bar of 2026-10-21), from 502 daily bars
Trend: vs 20d SMA 194.46 (-3.5%), 50d 189.91 (-1.2%), 200d 168.14 (+11.6%); 50d above 200d
Momentum: RSI(14) 42.9 | MACD -0.983 vs signal 0.795 (histogram -1.778)
Returns: 1d +1.2% | 5d -1.4% | 1m -4.4% | 3m +5.2%
52-week range: 127.50 - 202.00 (now 80.8% of the way up)
Volatility: ATR(14) 3.65 (1.9% of price) | annualised 20d 20.2%
Volume: 0.39x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.00</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score +0.00</summary>

```text
Fund type: Technology
What it holds: P/E 32.04 | P/B 11.88 | P/S 9.26 | 3y earnings growth n/a
Yield: 0.4%
Three-year record: +31.5% a year | beta to the market 1.45
Cost and size: expense ratio 0.08% | net assets 127.30B
What it is made of: Stocks 100.0%, Cash 0.0%
Largest holdings: NVIDIA Corp 15.5%, Apple Inc 13.6%, Microsoft Corp 10.7%, Advanced Micro Devices Inc 5.1%, Broadcom Inc 4.7%
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
Rolled up from the 5 largest holdings, 49.5% of the fund by weight
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 1.58 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +24.2% above the current prices
Holdings read: NVDA, AAPL, MSFT, AMD, AVGO
Recent rating changes among them:
  - NVDA: 2026-10-01 Cantor Fitzgerald: reit, Overweight -> Overweight
  - AAPL: 2026-10-20 MoffettNathanson: main, Neutral -> Neutral
  - MSFT: 2026-10-21 Guggenheim: reit, Buy -> Buy
  - AMD: 2026-10-21 Susquehanna: main, Positive -> Positive
  - AVGO: 2026-09-10 Piper Sandler: init, ? -> Overweight
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
Share count change: 1 week: +0.0% (0.00) over 7d | 1 month: +0.0% (0.00) over 34d
Shares outstanding: 272.06M | fund size: 51.07B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### US everyday goods (XLP) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Neutral overall as there is no material macro surprise, technicals show an uptrend but low volume, analyst view is bullish but covers <50% of the fund, and fund flows are flat.

**Main reasons it gave:**
- 10‑yr Treasury yield down 9 bps this week, no rate surprise
- XLP price above 20‑day, 50‑day, 200‑day SMAs but volume only 0.37× 20‑day average
- Analyst coverage 100% buy for top holdings, weighted price target +5.4% above current
- Fund flows flat over past month, share count unchanged

<details><summary><b>News</b> — score +0.00</summary>

- [State Street Consumer Staples SPDR (XLP) Adds Walmart and Costco on Monday](https://finance.yahoo.com/markets/stocks/articles/state-street-consumer-staples-spdr-110500347.html)  
  <sub>Yahoo Finance, 4 hours ago</sub>  
  This article first appeared on GuruFocus. State Street Consumer Staples Select Sector SPDR ETF (XLP) was the only ETF buying on Monday, Oct. 19,...
- [Should You Invest in the iShares U.S. Consumer Staples ETF (IYK)?](https://www.google.com/goto?url=CAESnQEB6zswFSX53AoJJrFe6H22_DhDRvAnpEIrK14AJM7wUgSpYW3Abp9Mt1s1GfNztGso718-MxuC9oykYUa5b5dAQjcag4q1yJh-Xi4KTAKSKIPcLrPKssDghMU0egAq3HZBZk6i6v16DOJXP78yB8ncxiw3mBZk_O_ERsSP5cVfS8SnKJs-76_XTcf47tk5QTHZ1H-idxZ41cGW1RSg)  
  <sub>Yahoo Finance, 6 hours ago</sub>  
  Launched on June 12, 2000, the iShares U.S. Consumer Staples ETF (IYK) is a passively managed exchange traded fund designed to provide a broad exposure to...
- [Defensive rotation: Quality over sector labels in healthcare, banks, and consumer staples (XLV:NYSEARCA)](https://seekingalpha.com/news/4654645-defensive-rotation-quality-over-sector-labels-in-healthcare-banks-and-consumer-staples)  
  <sub>Seeking Alpha, 20 hours ago</sub>  
  Defensive sector rotation is underway—focus on quality healthcare, banks & staples with cash flow, valuation and earnings support.
- [Investors Shift to Defensive Healthcare ETF XLV Amid Market Vola](https://www.gurufocus.com/news/9132461/investors-shift-to-defensive-healthcare-etf-xlv-amid-market-volatility)  
  <sub>GuruFocus, 19 hours ago</sub>  
  On October 20, 2026, a notable rotation into defensive sectors is underway, with healthcare-focused ETFs like State Street Health Care Select Sector SPDR...
- [Exchange-Traded Funds, Equity Futures Higher Pre-Bell Wednesday as AI Stocks Rebound Amid Corporate Earnings](https://www.google.com/goto?url=CAESoAEB6zswFQYOKZxZy0PwIKhe8Vt2lSx_iQaNmfUGMyMOLuPQUj9oGI3WKFRD1ObPbnm4HrB-UBCa1pskeeAS8jImRuE8ictkbtMSakEOC6mMOdWhRY1PbvLnZmc6e7lOUYNdTAvJ1nLW74yQQmxlK5Z19cJoGvISc8gLz7VCNl9GNwdEbWeI9i8DH0kxzBgaQ-633yNQUow6_55bSAOYZ08Z)  
  <sub>Yahoo Finance, 2 hours ago</sub>  
  The broad market exchange-traded fund SPDR S&P 500 ETF Trust (SPY) was up 0.2% and the actively trad.
- [Health Care Stocks Hit Record Highs, GM Drops Nearly 8%: Stock Market Today](https://www.tradingview.com/news/benzinga:1285d9920094b:0-health-care-stocks-hit-record-highs-gm-drops-nearly-8-stock-market-today/)  
  <sub>TradingView, 22 hours ago</sub>  
  Health care stocks climbed to record highs by midday Tuesday, with defensives and small caps leading a recovery from an early dip as the Nasdaq 100 stalled.
- [State Street Consumer Discretionary Select Sector SPDR ETF (XLY:UN): Stock Price, Quote and News](https://www.bnnbloomberg.ca/stock/XLY:UN/)  
  <sub>BNN Bloomberg, 19 hours ago</sub>  
  Real-time stock price, in-depth analysis, and the latest news for State Street Consumer Discretionary Select Sector SPDR ETF (XLY:UN).
- [State Street Health Care Select Sector SPDR ETF (XLV) stock price, news, quote and history](https://uk.finance.yahoo.com/quote/XLV/)  
  <sub>Yahoo Finance UK, 13 hours ago</sub>  
  State Street Health Care Select Sector SPDR ETF (XLV) · 2.25% · 5.24% · 21.90% · 14.90% · 22.56% · 35.63% · 616.86%. Key events. Baseline. Advanced chart.
- [Sector Update: Consumer Stocks Rise Late Afternoon](https://finance.yahoo.com/markets/stocks/articles/sector-consumer-stocks-rise-afternoon-194829440.html)  
  <sub>Yahoo Finance, 20 hours ago</sub>  
  Consumer stocks were higher late Tuesday afternoon, with the State Street Consumer Staples Select Sector SPDR ETF (XLP) increasing 0.5% and the State Street...
- [The Pivot: CoinShares Survey Suggests Crypto Investing No Longer for Speculation...It's Strategic!](https://www.advisorperspectives.com/webinars/2026/11/17/the-pivot-coinshares-survey-suggests-crypto-investing-no-longer-for-speculation-its-strategic?partnerref=APSidebar)  
  <sub>Advisor Perspectives, 23 hours ago</sub>  
  Crypto is pivoting from a speculative asset into a strategic allocation. A recent CoinShares survey shows that cryptocurrency is increasingly viewed as a...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.06% (-0.03 on the week) | 5-year 4.93% (-0.07 on the week) | 10-year 5.10% (-0.09 on the week) | 30-year 5.41% (-0.11 on the week)
Yield curve, 10-year minus 3-month: +1.04 points -- upward sloping (normal)
US dollar index: 101.77 (-0.78 on the week)
Volatility (VIX): 17.03 (+0.2 on the week) -- elevated
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 87.23 (bar of 2026-10-21), from 502 daily bars
Trend: vs 20d SMA 83.59 (+4.3%), 50d 84.24 (+3.6%), 200d 84.15 (+3.7%); 50d above 200d
Momentum: RSI(14) 66.5 | MACD 1.093 vs signal 0.447 (histogram 0.647)
Returns: 1d -0.6% | 5d +1.4% | 1m +5.4% | 3m +4.8%
52-week range: 75.60 - 90.01 (now 80.7% of the way up)
Volatility: ATR(14) 1.11 (1.3% of price) | annualised 20d 15.0%
Volume: 0.37x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.20</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score +0.20</summary>

```text
Fund type: Consumer Defensive
What it holds: P/E 23.91 | P/B 4.44 | P/S 1.29 | 3y earnings growth n/a
Yield: 2.7%
Three-year record: +11.9% a year | beta to the market 0.48
Cost and size: expense ratio 0.08% | net assets 13.45B
What it is made of: Stocks 99.9%, Cash 0.1%
Largest holdings: Walmart Inc 10.5%, Costco Wholesale Corp 9.2%, Procter & Gamble Co 7.7%, Coca-Cola Co 7.6%, Philip Morris International Inc 6.8%
Sector mix: Consumer defensive 98.5%, Consumer cyclical 1.5%
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
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 1.80 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +5.4% above the current prices
Holdings read: WMT, COST, PG, KO, PM
Recent rating changes among them:
  - WMT: 2026-10-20 Evercore ISI Group: main, Outperform -> Outperform
  - COST: 2026-10-21 CICC: init, ? -> Outperform
  - PG: 2026-10-20 RBC Capital: reit, Outperform -> Outperform
  - KO: 2026-10-16 Barclays: main, Overweight -> Overweight
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
Direction: flat (1 month)
Share count change: 1 week: +0.0% (0.00) over 7d | 1 month: +0.0% (0.00) over 32d
Shares outstanding: 210.17M | fund size: 18.33B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### US electricity and water (XLU) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Neutral overall due to lack of macro surprise, flat fund flows, mixed technicals, and limited analyst coverage despite bullish ratings.

**Main reasons it gave:**
- Analyst coverage only 39.5% of fund despite 80.6% buy rating and +16% price target
- Fund flows flat with no net creations or redemptions over the past week
- Technical indicators mixed: price above short-term SMAs but below 200‑day SMA, MACD positive but no decisive break
- Macro environment unchanged: yields down slightly, VIX stable, no surprise data releases

<details><summary><b>News</b> — score +0.00</summary>

- [State Street Utilities Select Sector SPDR ETF (XLU) Stock Price, News, Quote & History](https://ca.finance.yahoo.com/quote/XLU/)  
  <sub>Yahoo! Finance Canada, 18 hours ago</sub>  
  State Street Utilities Select Sector SPDR ETF (XLU) · 0.02% · 1.90% · -8.46% · -1.90% · -8.50% · 25.18% · 176.89%. Key Events. Baseline.
- [Trading Systems Reacting to (XLU) Volatility](https://news.stocktradersdaily.com/news_release/1/Trading_Systems_Reacting_to_XLU_Volatility_102026033002_1792524602.html)  
  <sub>Stock Traders Daily, 24 hours ago</sub>  
  Price-action only: Utilities Select Sector Spdr Etf (XLU) movements set the tone for institutional models. Trading Systems Reacting to (XLU) Volatility.
- [The Pivot: CoinShares Survey Suggests Crypto Investing No Longer for Speculation...It's Strategic!](https://www.advisorperspectives.com/webinars/2026/11/17/the-pivot-coinshares-survey-suggests-crypto-investing-no-longer-for-speculation-its-strategic?partnerref=APSidebar)  
  <sub>Advisor Perspectives, 23 hours ago</sub>  
  Crypto is pivoting from a speculative asset into a strategic allocation. A recent CoinShares survey shows that cryptocurrency is increasingly viewed as a...
- [Form 4 State Street® Utilities Select Sector SPDR® ETF For: 20 October](https://uk.investing.com/news/stock-market-news/form-4-state-street-utilities-select-sector-spdr-etf-for-20-october-93CH-4920758)  
  <sub>Investing.com UK, 20 hours ago</sub>  
  Registration Statement No.333-285508. Filed Pursuant to Rule 424(b)(2). Pricing Supplement dated October 16, 2026 to the Prospectus dated March 25, 2025,
- [Health Care Stocks Hit Record Highs, GM Drops Nearly 8%: Stock Market Today](https://www.tradingview.com/news/benzinga:1285d9920094b:0-health-care-stocks-hit-record-highs-gm-drops-nearly-8-stock-market-today/)  
  <sub>TradingView, 22 hours ago</sub>  
  Health care stocks climbed to record highs by midday Tuesday, with defensives and small caps leading a recovery from an early dip as the Nasdaq 100 stalled.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.06% (-0.03 on the week) | 5-year 4.93% (-0.07 on the week) | 10-year 5.10% (-0.09 on the week) | 30-year 5.41% (-0.11 on the week)
Yield curve, 10-year minus 3-month: +1.04 points -- upward sloping (normal)
US dollar index: 101.77 (-0.78 on the week)
Volatility (VIX): 17.03 (+0.2 on the week) -- elevated
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 41.99 (bar of 2026-10-21), from 502 daily bars
Trend: vs 20d SMA 40.79 (+2.9%), 50d 41.92 (+0.2%), 200d 44.29 (-5.2%); 50d below 200d
Momentum: RSI(14) 56.4 | MACD 0.097 vs signal -0.129 (histogram 0.226)
Returns: 1d +0.3% | 5d +0.7% | 1m +3.6% | 3m -9.1%
52-week range: 39.25 - 47.73 (now 32.4% of the way up)
Volatility: ATR(14) 0.64 (1.5% of price) | annualised 20d 16.4%
Volume: 0.33x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.30</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score +0.30</summary>

```text
Fund type: Utilities
What it holds: P/E 17.86 | P/B 2.04 | P/S 2.49 | 3y earnings growth n/a
Yield: 3.1%
Three-year record: +15.5% a year | beta to the market 0.40
Cost and size: expense ratio 0.08% | net assets 21.33B
What it is made of: Stocks 99.8%, Cash 0.2%
Largest holdings: NextEra Energy Inc 12.7%, Southern Co 7.7%, Duke Energy Corp 7.2%, Constellation Energy Corp 6.7%, American Electric Power Co Inc 5.2%
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

<details><summary><b>What analysts and big funds say</b> — score +0.45</summary>

_Not available today._

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score +0.45</summary>

```text
Rolled up from the 5 largest holdings, 39.5% of the fund by weight
Ratings by weight: buy 80.6% | hold 19.4% | sell 0.0% (mean 2.00 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +16.0% above the current prices
Holdings read: NEE, SO, DUK, CEG, AEP
Recent rating changes among them:
  - NEE: 2026-10-21 Bernstein: reit, Outperform -> Outperform
  - SO: 2026-10-20 Jefferies: main, Hold -> Hold
  - DUK: 2026-10-13 JP Morgan: main, Neutral -> Neutral
  - CEG: 2026-10-16 CIBC: init, ? -> Outperformer
  - AEP: 2026-10-20 BTIG: up, Neutral -> Buy
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
Shares outstanding: 163.27M | fund size: 6.86B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### US health care (XLV) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:** no explanation. It wrote only “Neutral”, so the main reasons below are all it gave.

**Main reasons it gave:**
- Flat fund flows indicate no net demand
- All analyst ratings are buy with modest +6.4% price target, but no macro catalyst
- Technical indicators show price near all‑time high with low volume and no decisive break
- Macro yields unchanged and no surprise data, VIX stable

<details><summary><b>News</b> — score +0.00</summary>

- [What State Street Health Care SPDR (XLV) Bought: Eli Lilly Leads on Monday](https://finance.yahoo.com/healthcare/articles/state-street-health-care-spdr-110414633.html)  
  <sub>Yahoo Finance, 4 hours ago</sub>  
  This article first appeared on GuruFocus. State Street Health Care Select Sector SPDR ETF (XLV) was the sole mover in Monday's session, with ETF activity...
- [Investors Shift to Defensive Healthcare ETF XLV Amid Market Vola](https://www.gurufocus.com/news/9132461/investors-shift-to-defensive-healthcare-etf-xlv-amid-market-volatility)  
  <sub>GuruFocus, 19 hours ago</sub>  
  On October 20, 2026, a notable rotation into defensive sectors is underway, with healthcare-focused ETFs like State Street Health Care Select Sector SPDR...
- [Should You Invest in the Vanguard Health Care Index Fund ETF Shares (VHT)?](https://finance.yahoo.com/healthcare/articles/invest-vanguard-health-care-index-092002890.html)  
  <sub>Yahoo Finance, 6 hours ago</sub>  
  Designed to provide broad exposure to the Healthcare - Broad segment of the equity market, the Vanguard Health Care Index Fund ETF Shares (VHT) is a...
- [Healthcare Just Broke Out to an All-Time High... And Nobody’s Talking About It by John Salama, CMT](https://www.theglobeandmail.com/investing/markets/stocks/IWM-A/pressreleases/8243728/healthcare-just-broke-out-to-an-all-time-high-and-nobodys-talking-about-it-by-john-salama-cmt/)  
  <sub>The Globe and Mail, 20 hours ago</sub>  
  Detailed price information for Ishares Russell 2000 ETF (IWM-A) from The Globe and Mail including charting and trades.
- [XLV touches a new high, hitting overbought territory](https://www.tradingview.com/news/seekingalpha:8a23c3211094b:0-xlv-touches-a-new-high-hitting-overbought-territory/)  
  <sub>TradingView, 22 hours ago</sub>  
  The Health Care Select Sector SPDR ETF AMEX:XLV reached a new record high at $179.86, up 2.26% on Tuesday.Its relative strength index also hit overbought...
- [Defensive rotation: Quality over sector labels in healthcare, banks, and consumer staples (XLV:NYSEARCA)](https://seekingalpha.com/news/4654645-defensive-rotation-quality-over-sector-labels-in-healthcare-banks-and-consumer-staples)  
  <sub>Seeking Alpha, 20 hours ago</sub>  
  Defensive sector rotation is underway—focus on quality healthcare, banks & staples with cash flow, valuation and earnings support.
- [Moderna Jumps 7% While Melanoma Vaccine Data Looms; Bristol Myers Squibb Rises 5%, Pfizer Advances 2%](https://247wallst.com/investing/2026/10/20/moderna-jumps-7-while-melanoma-vaccine-data-looms-bristol-myers-squibb-rises-5-pfizer-inches-higher/)  
  <sub>24/7 Wall St., 21 hours ago</sub>  
  Moderna shares are surging ahead of a closely watched cancer data presentation in Madrid, but the company's razor-thin revenue base means a single readout...
- [Exchange-Traded Funds, Equity Futures Higher Pre-Bell Wednesday as AI Stocks Rebound Amid Corporate Earnings](https://finance.yahoo.com/markets/stocks/articles/exchange-traded-funds-equity-futures-131151383.html)  
  <sub>Yahoo Finance, 2 hours ago</sub>  
  The broad market exchange-traded fund SPDR S&P 500 ETF Trust (SPY) was up 0.2% and the actively trad.
- [Health Care Stocks Hit Record Highs, GM Drops Nearly 8%: Stock Market Today](https://www.tradingview.com/news/benzinga:1285d9920094b:0-health-care-stocks-hit-record-highs-gm-drops-nearly-8-stock-market-today/)  
  <sub>TradingView, 22 hours ago</sub>  
  Health care stocks climbed to record highs by midday Tuesday, with defensives and small caps leading a recovery from an early dip as the Nasdaq 100 stalled.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.06% (-0.03 on the week) | 5-year 4.93% (-0.07 on the week) | 10-year 5.10% (-0.09 on the week) | 30-year 5.41% (-0.11 on the week)
Yield curve, 10-year minus 3-month: +1.04 points -- upward sloping (normal)
US dollar index: 101.77 (-0.78 on the week)
Volatility (VIX): 17.03 (+0.2 on the week) -- elevated
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 178.49 (bar of 2026-10-21), from 502 daily bars
Trend: vs 20d SMA 171.45 (+4.1%), 50d 170.63 (+4.6%), 200d 157.85 (+13.1%); 50d above 200d
Momentum: RSI(14) 65.3 | MACD 2.387 vs signal 1.350 (histogram 1.037)
Returns: 1d -0.7% | 5d +2.6% | 1m +5.1% | 3m +10.6%
52-week range: 142.84 - 179.82 (now 96.4% of the way up)
Volatility: ATR(14) 2.83 (1.6% of price) | annualised 20d 18.5%
Volume: 0.50x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.30</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score +0.30</summary>

```text
Fund type: Health
What it holds: P/E 30.01 | P/B 4.74 | P/S 1.66 | 3y earnings growth n/a
Yield: 1.5%
Three-year record: +12.8% a year | beta to the market 0.52
Cost and size: expense ratio 0.08% | net assets 43.39B
What it is made of: Stocks 99.8%, Cash 0.2%
Largest holdings: Eli Lilly and Co 15.1%, Johnson & Johnson 10.4%, AbbVie Inc 7.5%, Merck & Co Inc 5.8%, UnitedHealth Group Inc 5.4%
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
Rolled up from the 5 largest holdings, 44.3% of the fund by weight
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 1.72 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +6.4% above the current prices
Holdings read: LLY, JNJ, ABBV, MRK, UNH
Recent rating changes among them:
  - LLY: 2026-10-12 RBC Capital: reit, Outperform -> Outperform
  - JNJ: 2026-10-16 Wells Fargo: main, Overweight -> Overweight
  - ABBV: 2026-10-21 Barclays: main, Overweight -> Overweight
  - MRK: 2026-10-12 Citigroup: main, Neutral -> Neutral
  - UNH: 2026-10-20 RBC Capital: main, Outperform -> Outperform
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
Share count change: 1 week: +0.0% (0.00) over 7d | 1 month: +0.0% (0.00) over 33d
Shares outstanding: 197.42M | fund size: 35.24B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### US shopping and leisure (XLY) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Neutral overall; no macro surprise, technicals lack decisive break, and fund flows are flat despite bullish analyst coverage.

**Main reasons it gave:**
- Treasury yields fell modestly across the curve with no rate surprise
- Price just below 200‑day SMA and volume at 0.31× 20‑day average, no decisive technical break
- Fund flows flat over the past week and month, indicating neutral investor demand
- Analyst coverage of top holdings 100% buy with +17% price target, but no macro catalyst

<details><summary><b>News</b> — score +0.00</summary>

- [State Street Consumer Discretionary (XLY) Sells $45.7 Million of Amazon on Oct. 19](https://finance.yahoo.com/markets/stocks/articles/state-street-consumer-discretionary-xly-110457691.html)  
  <sub>Yahoo Finance, 4 hours ago</sub>  
  This article first appeared on GuruFocus. State Street Consumer Discretionary Select Sector SPDR ETF (XLY) extended a one-day streak of one-sided ETF...
- [State Street Consumer Discretionary Select Sector SPDR ETF (XLY:UN): Stock Price, Quote and News](https://www.bnnbloomberg.ca/stock/XLY:UN/)  
  <sub>BNN Bloomberg, 19 hours ago</sub>  
  Real-time stock price, in-depth analysis, and the latest news for State Street Consumer Discretionary Select Sector SPDR ETF (XLY:UN).
- [Undervalued consumer discretionary stocks to watch as Q3 earnings season gears up (XLY:NYSEARCA)](https://seekingalpha.com/news/4655167-undervalued-consumer-discretionary-stocks-to-watch-as-q3-earnings-season-gears-up)  
  <sub>Seeking Alpha, 2 hours ago</sub>  
  Screening Q3 2026 earnings reveals 7 undervalued consumer discretionary stocks—CALY, DAN, F and more—plus ETF ideas.
- [Sector Update: Consumer Stocks Rise Late Afternoon](https://finance.yahoo.com/markets/stocks/articles/sector-consumer-stocks-rise-afternoon-194829440.html)  
  <sub>Yahoo Finance, 20 hours ago</sub>  
  Consumer stocks were higher late Tuesday afternoon, with the State Street Consumer Staples Select Sector SPDR ETF (XLP) increasing 0.5% and the State Street...
- [Exchange-Traded Funds Gain as US Equities Advance After Midday](https://finance.yahoo.com/markets/stocks/articles/exchange-traded-funds-gain-us-171124946.html)  
  <sub>Yahoo Finance, 22 hours ago</sub>  
  Broad Market Indicators Broad-market exchange-traded funds IWM and IVV rose. Actively traded Invesco QQQ Trust (QQQ) was little changed, erasing earlier...
- [Keith Richards’ Top Picks for Oct. 20, 2026](https://www.bnnbloomberg.ca/markets/2026/10/20/keith-richards-top-picks-for-oct-20-2026/)  
  <sub>BNN Bloomberg, 22 hours ago</sub>  
  Top Picks from Keith Richards, President, Chief Portfolio Manager, ValueTrend Wealth Management.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.06% (-0.03 on the week) | 5-year 4.93% (-0.07 on the week) | 10-year 5.10% (-0.09 on the week) | 30-year 5.41% (-0.11 on the week)
Yield curve, 10-year minus 3-month: +1.04 points -- upward sloping (normal)
US dollar index: 101.77 (-0.78 on the week)
Volatility (VIX): 17.03 (+0.2 on the week) -- elevated
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 115.59 (bar of 2026-10-21), from 502 daily bars
Trend: vs 20d SMA 111.62 (+3.6%), 50d 113.60 (+1.8%), 200d 115.83 (-0.2%); 50d below 200d
Momentum: RSI(14) 62.9 | MACD 0.524 vs signal -0.136 (histogram 0.660)
Returns: 1d +0.1% | 5d +3.7% | 1m +2.9% | 3m +6.3%
52-week range: 105.66 - 124.52 (now 52.7% of the way up)
Volatility: ATR(14) 1.52 (1.3% of price) | annualised 20d 13.5%
Volume: 0.31x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.00</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score +0.00</summary>

```text
Fund type: Consumer Cyclical
What it holds: P/E 24.00 | P/B 5.56 | P/S 2.32 | 3y earnings growth n/a
Yield: 0.9%
Three-year record: +15.0% a year | beta to the market 1.18
Cost and size: expense ratio 0.08% | net assets 21.27B
What it is made of: Stocks 99.9%, Cash 0.1%
Largest holdings: Amazon.com Inc 23.4%, Tesla Inc 17.7%, The Home Depot Inc 5.0%, McDonald's Corp 4.2%, TJX Companies Inc 4.1%
Sector mix: Consumer cyclical 98.7%, Technology 1.3%
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
Rolled up from the 5 largest holdings, 54.4% of the fund by weight
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 1.79 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +17.1% above the current prices
Holdings read: AMZN, TSLA, HD, MCD, TJX
Recent rating changes among them:
  - AMZN: 2026-10-19 Morgan Stanley: main, Overweight -> Overweight
  - TSLA: 2026-10-20 Cantor Fitzgerald: reit, Overweight -> Overweight
  - HD: 2026-09-09 Bernstein: main, Market Perform -> Market Perform
  - MCD: 2026-10-20 Citigroup: main, Buy -> Buy
  - TJX: 2026-08-26 Jefferies: down, Buy -> Hold
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
Share count change: 1 week: +0.0% (0.00) over 7d | 1 month: +0.0% (0.00) over 33d
Shares outstanding: 120.25M | fund size: 13.90B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Argentina (ARGT) · Sector or country — no answer, no confidence given

<details><summary><b>News</b> — score n/a</summary>

- [(ARGT) Risk Channels and Responsive Allocation](https://news.stocktradersdaily.com/news_release/20/ARGT_Risk_Channels_and_Responsive_Allocation_102026095002_1792547402.html)  
  <sub>Stock Traders Daily, 18 hours ago</sub>  
  Key findings for Global X Msci Argentina Etf (NASDAQ: ARGT). Weak Near-Term Sentiment Could Catalyze Bearish Positioning; No clear price positioning signal...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score n/a</summary>

```text
US Treasury yields: 3-month 4.06% (-0.03 on the week) | 5-year 4.93% (-0.07 on the week) | 10-year 5.10% (-0.09 on the week) | 30-year 5.41% (-0.11 on the week)
Yield curve, 10-year minus 3-month: +1.04 points -- upward sloping (normal)
US dollar index: 101.77 (-0.78 on the week)
Volatility (VIX): 17.03 (+0.2 on the week) -- elevated
```

</details>

<details><summary><b>Price and chart</b> — score n/a</summary>

```text
Last close 87.77 (bar of 2026-10-21), from 502 daily bars
Trend: vs 20d SMA 87.62 (+0.2%), 50d 91.33 (-3.9%), 200d 92.36 (-5.0%); 50d below 200d
Momentum: RSI(14) 44.3 | MACD -1.118 vs signal -1.291 (histogram 0.173)
Returns: 1d +0.6% | 5d +0.9% | 1m -5.5% | 3m -6.7%
52-week range: 70.49 - 102.94 (now 53.3% of the way up)
Volatility: ATR(14) 1.68 (1.9% of price) | annualised 20d 28.5%
Volume: 0.25x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score n/a</summary>

```text
Fund type: Focused Region
What it holds: P/E 13.92 | P/B 1.57 | P/S 1.21 | 3y earnings growth n/a
Yield: 1.2%
Three-year record: +30.6% a year | beta to the market 0.45
Cost and size: expense ratio 0.59% | net assets 718.85M
What it is made of: Stocks 99.9%, Cash 0.1%
Largest holdings: MercadoLibre Inc 21.7%, YPF SA ADR 10.4%, Vista Energy SAB de CV ADR 7.0%, Grupo Financiero Galicia SA ADR 5.7%, Pampa Energia SA ADR 4.7%
Sector mix: Consumer cyclical 27.8%, Energy 21.2%, Financial services 14.2%, Basic materials 11.8%
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
Rolled up from the 5 largest holdings, 49.4% of the fund by weight
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 1.66 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +31.1% above the current prices
Holdings read: MELI, YPF, VIST, GGAL, PAM
Recent rating changes among them:
  - MELI: 2026-10-13 Citigroup: main, Neutral -> Neutral
  - YPF: 2026-09-01 JP Morgan: main, Overweight -> Overweight
  - VIST: 2026-09-01 JP Morgan: main, Overweight -> Overweight
  - GGAL: 2026-10-13 UBS: main, Neutral -> Neutral
  - PAM: 2026-09-01 JP Morgan: main, Neutral -> Neutral
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
Share count change: 1 week: +1.5% (10.41M) over 7d | 1 month: -5.4% (-41.48M) over 32d
Shares outstanding: 8.25M | fund size: 724.21M
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### United Kingdom (EWU) · Sector or country — no answer, no confidence given

<details><summary><b>News</b> — score n/a</summary>

- [Inflation at 3.5% Puts These UK ETFs in Focus as BOE Hike Bets Mount](https://www.zacks.com/stock/news/3011748/inflation-at-35-puts-these-uk-etfs-in-focus-as-boe-hike-bets-mount)  
  <sub>Zacks Investment Research, 3 hours ago</sub>  
  UK inflation hit 3.5% in September, fueling BOE rate-hike bets. Explore three ETFs positioned for shifting opportunities across UK equities.
- [UK inflation rises to 3.1% in August, highest in five months (FXB:NYSEARCA)](https://seekingalpha.com/news/4654995-uk-inflation-rises-to-3_1-percent-in-august-highest-in-five-months)  
  <sub>Seeking Alpha, 9 hours ago</sub>  
  The UK's annual inflation rate rose to 3.1% in August 2026, its highest level in five months, from 2.9% in July, in line with market expectations.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score n/a</summary>

```text
US Treasury yields: 3-month 4.06% (-0.03 on the week) | 5-year 4.93% (-0.07 on the week) | 10-year 5.10% (-0.09 on the week) | 30-year 5.41% (-0.11 on the week)
Yield curve, 10-year minus 3-month: +1.04 points -- upward sloping (normal)
US dollar index: 101.77 (-0.78 on the week)
Volatility (VIX): 17.03 (+0.2 on the week) -- elevated
```

</details>

<details><summary><b>Price and chart</b> — score n/a</summary>

```text
Last close 47.84 (bar of 2026-10-21), from 502 daily bars
Trend: vs 20d SMA 46.88 (+2.0%), 50d 47.68 (+0.3%), 200d 46.88 (+2.1%); 50d above 200d
Momentum: RSI(14) 57.5 | MACD 0.044 vs signal -0.162 (histogram 0.206)
Returns: 1d +0.2% | 5d +2.0% | 1m +0.4% | 3m +2.4%
52-week range: 41.34 - 49.39 (now 80.7% of the way up)
Volatility: ATR(14) 0.49 (1.0% of price) | annualised 20d 12.6%
Volume: 0.17x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score n/a</summary>

```text
Fund type: Focused Region
What it holds: P/E 16.50 | P/B 2.22 | P/S 1.46 | 3y earnings growth n/a
Yield: 3.2%
Three-year record: +19.5% a year | beta to the market 0.71
Cost and size: expense ratio 0.50% | net assets 3.67B
What it is made of: Stocks 98.6%, Other 1.1%, Cash 0.4%
Largest holdings: HSBC Holdings PLC 11.0%, Shell PLC 8.9%, AstraZeneca PLC 8.0%, Rolls-Royce Holdings PLC 5.2%, Unilever PLC 4.3%
Sector mix: Financial services 26.1%, Consumer defensive 14.1%, Industrials 13.3%, Healthcare 13.0%
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
Rolled up from the 5 largest holdings, 37.4% of the fund by weight
Ratings by weight: buy 59.1% | hold 40.9% | sell 0.0% (mean 2.13 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +13.0% above the current prices
Holdings read: HSBA.L, SHEL.L, AZN.L, RR.L, ULVR.L
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
Direction: flat (1 month)
Share count change: 1 week: +0.0% (0.00) over 7d | 1 month: +0.0% (0.00) over 33d
Shares outstanding: 67.80M | fund size: 3.24B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Defence and aerospace (ITA) · Sector or country — no answer, no confidence given

<details><summary><b>News</b> — score n/a</summary>

- [Should You Invest in the Select STOXX Europe Aerospace & Defense ETF (EUAD)?](https://finance.yahoo.com/markets/stocks/articles/invest-select-stoxx-europe-aerospace-092003425.html)  
  <sub>Yahoo Finance, 6 hours ago</sub>
- [ITA ETF Holdings: GE Aerospace, RTX, Boeing and Top Stocks](https://www.ebc.com/forex/ita-etf-holdings-top-stocks)  
  <sub>EBC Financial Group, 8 hours ago</sub>  
  Explore ITA ETF holdings, including GE Aerospace, RTX and Boeing, and learn how its top stocks shape exposure to commercial aviation and US defense.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score n/a</summary>

```text
US Treasury yields: 3-month 4.06% (-0.03 on the week) | 5-year 4.93% (-0.07 on the week) | 10-year 5.10% (-0.09 on the week) | 30-year 5.41% (-0.11 on the week)
Yield curve, 10-year minus 3-month: +1.04 points -- upward sloping (normal)
US dollar index: 101.77 (-0.78 on the week)
Volatility (VIX): 17.03 (+0.2 on the week) -- elevated
```

</details>

<details><summary><b>Price and chart</b> — score n/a</summary>

```text
Last close 206.54 (bar of 2026-10-21), from 502 daily bars
Trend: vs 20d SMA 207.46 (-0.4%), 50d 220.52 (-6.3%), 200d 229.83 (-10.1%); 50d below 200d
Momentum: RSI(14) 39.6 | MACD -3.525 vs signal -4.507 (histogram 0.982)
Returns: 1d +0.2% | 5d +1.1% | 1m -3.5% | 3m -13.3%
52-week range: 198.23 - 253.22 (now 15.1% of the way up)
Volatility: ATR(14) 3.69 (1.8% of price) | annualised 20d 15.1%
Volume: 0.39x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score n/a</summary>

```text
Fund type: Industrials
What it holds: P/E 31.87 | P/B 5.88 | P/S 2.95 | 3y earnings growth n/a
Yield: 0.3%
Three-year record: +25.1% a year | beta to the market 0.98
Cost and size: expense ratio 0.37% | net assets 12.14B
What it is made of: Stocks 100.0%, Cash 0.0%
Largest holdings: GE Aerospace 21.0%, RTX Corp 16.2%, Boeing Co 7.5%, Howmet Aerospace Inc 4.6%, Lockheed Martin Corp 4.6%
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
Rolled up from the 5 largest holdings, 53.9% of the fund by weight
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 1.68 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +28.3% above the current prices
Holdings read: GE, RTX, BA, HWM, LMT
Recent rating changes among them:
  - GE: 2026-10-21 Susquehanna: main, Positive -> Positive
  - RTX: 2026-10-21 Barclays: main, Overweight -> Overweight
  - BA: 2026-10-19 Morgan Stanley: main, Equal-Weight -> Equal-Weight
  - HWM: 2026-10-15 RBC Capital: main, Outperform -> Outperform
  - LMT: 2026-10-15 RBC Capital: main, Sector Perform -> Sector Perform
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
Share count change: 1 week: -0.5% (-56.45M) over 7d | 1 month: -7.7% (-1.01B) over 32d
Shares outstanding: 58.44M | fund size: 12.07B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### US materials and chemicals (XLB) · Sector or country — no answer, no confidence given

<details><summary><b>News</b> — score n/a</summary>

- [State Street Consumer Discretionary (XLY) Sells $45.7 Million of Amazon on Oct. 19](https://finance.yahoo.com/markets/stocks/articles/state-street-consumer-discretionary-xly-110457691.html)  
  <sub>Yahoo Finance, 4 hours ago</sub>  
  This article first appeared on GuruFocus. State Street Consumer Discretionary Select Sector SPDR ETF (XLY) extended a one-day streak of one-sided ETF...
- [These six materials stocks look undervalued as Q3 earnings season begins (XLB:NYSEARCA)](https://seekingalpha.com/news/4655100-these-six-materials-stocks-look-undervalued-as-q3-earnings-season-begins)  
  <sub>Seeking Alpha, 4 hours ago</sub>  
  Q3 2026 earnings season: screen U.S. materials stocks with top valuation grades—LYB, GPK, IP, MOS, DOW, EMN—and key ETFs.
- [(XLB) Stock Trading Blueprint (XLB:CA)](https://news.stocktradersdaily.com/canada/xlb-stock-trading-blueprint_20261020_12e742)  
  <sub>Stock Traders Daily, 23 hours ago</sub>  
  Stock Trading Blueprint for iShares Core Canadian Long Term Bond Index ETF (XLB) with Key Buy and Sell Indicators.
- [Health Care Stocks Hit Record Highs, GM Drops Nearly 8%: Stock Market Today](https://www.tradingview.com/news/benzinga:1285d9920094b:0-health-care-stocks-hit-record-highs-gm-drops-nearly-8-stock-market-today/)  
  <sub>TradingView, 22 hours ago</sub>  
  Health care stocks climbed to record highs by midday Tuesday, with defensives and small caps leading a recovery from an early dip as the Nasdaq 100 stalled.
- [State Street Consumer Discretionary Select Sector SPDR ETF (XLY:UN): Stock Price, Quote and News](https://www.bnnbloomberg.ca/stock/XLY:UN/)  
  <sub>BNN Bloomberg, 19 hours ago</sub>  
  Real-time stock price, in-depth analysis, and the latest news for State Street Consumer Discretionary Select Sector SPDR ETF (XLY:UN).
- [Cyclicals Top Sectors In Wednesday Trading As Defensives Trail](https://www.benzinga.com/etfs/sector-etfs/26/10/62499965/cyclicals-top-sectors-in-wednesday-trading-as-defensives-trail)  
  <sub>Benzinga, 27 minutes ago</sub>  
  Five sectors are higher and six are lower in Wednesday's regular session, with cyclical sectors holding two of the top three positions alongside Technology.
- [The Pivot: CoinShares Survey Suggests Crypto Investing No Longer for Speculation...It's Strategic!](https://www.advisorperspectives.com/webinars/2026/11/17/the-pivot-coinshares-survey-suggests-crypto-investing-no-longer-for-speculation-its-strategic?partnerref=APSidebar)  
  <sub>Advisor Perspectives, 23 hours ago</sub>  
  Crypto is pivoting from a speculative asset into a strategic allocation. A recent CoinShares survey shows that cryptocurrency is increasingly viewed as a...
- [State Street Utilities Select Sector SPDR ETF (XLU) Stock Price, News, Quote & History](https://ca.finance.yahoo.com/quote/XLU/)  
  <sub>Yahoo! Finance Canada, 18 hours ago</sub>  
  Find the latest State Street Utilities Select Sector SPDR ETF (XLU) stock quote, history, news and other vital information to help you with your stock...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score n/a</summary>

```text
US Treasury yields: 3-month 4.06% (-0.03 on the week) | 5-year 4.93% (-0.07 on the week) | 10-year 5.10% (-0.09 on the week) | 30-year 5.41% (-0.11 on the week)
Yield curve, 10-year minus 3-month: +1.04 points -- upward sloping (normal)
US dollar index: 101.77 (-0.78 on the week)
Volatility (VIX): 17.03 (+0.2 on the week) -- elevated
```

</details>

<details><summary><b>Price and chart</b> — score n/a</summary>

```text
Last close 51.03 (bar of 2026-10-21), from 502 daily bars
Trend: vs 20d SMA 49.73 (+2.6%), 50d 51.05 (-0.0%), 200d 50.94 (+0.2%); 50d above 200d
Momentum: RSI(14) 58.3 | MACD 0.054 vs signal -0.251 (histogram 0.305)
Returns: 1d -0.4% | 5d +2.7% | 1m +1.0% | 3m +1.5%
52-week range: 42.23 - 53.67 (now 76.9% of the way up)
Volatility: ATR(14) 0.69 (1.4% of price) | annualised 20d 13.0%
Volume: 0.24x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score n/a</summary>

```text
Fund type: Natural Resources
What it holds: P/E 22.69 | P/B 2.70 | P/S 1.78 | 3y earnings growth n/a
Yield: 1.8%
Three-year record: +12.3% a year | beta to the market 0.85
Cost and size: expense ratio 0.08% | net assets 7.78B
What it is made of: Stocks 99.8%, Cash 0.2%
Largest holdings: Linde PLC 12.2%, Newmont Corp 6.8%, Freeport-McMoRan Inc 5.6%, Ecolab Inc 4.7%, Sherwin-Williams Co 4.7%
Sector mix: Basic materials 83.2%, Consumer cyclical 16.8%
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
Rolled up from the 5 largest holdings, 34.1% of the fund by weight
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 1.71 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +13.0% above the current prices
Holdings read: LIN, NEM, FCX, ECL, SHW
Recent rating changes among them:
  - LIN: 2026-10-15 RBC Capital: main, Outperform -> Outperform
  - NEM: 2026-10-20 Citigroup: main, Buy -> Buy
  - FCX: 2026-10-19 Barclays: main, Overweight -> Overweight
  - ECL: 2026-10-05 UBS: main, Buy -> Buy
  - SHW: 2026-10-13 Barclays: init, ? -> Equal-Weight
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
Shares outstanding: 71.92M | fund size: 3.67B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

## Commodities

### Sugar (CANE) · Commodity — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> No macro surprise or decisive technical break; technicals show strong uptrend but low volume; positioning is crowded long with minimal change; fund outflows are sizable but not decisive; heavy roll cost is a bearish tailwind but not enough to tip the call.

**Main reasons it gave:**
- US Treasury yields fell slightly across the curve (10‑year -0.09% week)
- SUGAR NO. 11 net long 22% of OI, crowding at 100th percentile, change +0.2% week
- Fund outflows: -15.2% share count over past month
- Cost of holding: -8.2% annual roll cost (heavy)

<details><summary><b>News</b> — score +0.00</summary>

_No news found for this one today._

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.06% (-0.03 on the week) | 5-year 4.93% (-0.07 on the week) | 10-year 5.10% (-0.09 on the week) | 30-year 5.41% (-0.11 on the week)
Yield curve, 10-year minus 3-month: +1.04 points -- upward sloping (normal)
US dollar index: 101.77 (-0.78 on the week)
Volatility (VIX): 17.03 (+0.2 on the week) -- elevated
```

</details>

<details><summary><b>Price and chart</b> — score +0.20</summary>

```text
Last close 12.22 (bar of 2026-10-21), from 502 daily bars
Trend: vs 20d SMA 11.94 (+2.3%), 50d 11.54 (+5.9%), 200d 10.15 (+20.4%); 50d above 200d
Momentum: RSI(14) 60.8 | MACD 0.271 vs signal 0.277 (histogram -0.006)
Returns: 1d -0.3% | 5d -0.9% | 1m +9.0% | 3m +26.5%
52-week range: 9.02 - 12.47 (now 92.8% of the way up)
Volatility: ATR(14) 0.19 (1.6% of price) | annualised 20d 22.4%
Volume: 0.39x the 20-day average
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
Measured: 3 months: fund +26.5%, commodity +39.1%, gap -12.6% | 6 months: fund +31.7%, commodity +50.6%, gap -18.9% | 12 months: fund +21.8%, commodity +30.0%, gap -8.2%
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

<details><summary><b>Buying and selling by company insiders</b> — score +0.00</summary>

_Not available today._

</details>

<details><summary><b>Who is positioned how</b> — score +0.00</summary>

```text
Contract: SUGAR NO. 11 - ICE FUTURES U.S. (positions as of 2026-10-13, published the following Friday)
Large speculators: net long 22.0% of open interest (1,179,144 contracts)
Change on the week: +0.2% of open interest
Crowding: 100% percentile over 52 weeks -- a crowded long by the standards of the past year
Read this as crowding, not as a forecast: an extreme is as often the end of a move as the middle of one.
```

</details>

<details><summary><b>Money going into and out of this fund</b> — score +0.00</summary>

```text
Direction: money going out (1 month)
Share count change: 1 week: -1.8% (-983.76K) over 7d | 1 month: -15.2% (-9.49M) over 32d
Shares outstanding: 4.34M | fund size: 53.01M
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Corn (CORN) · Commodity — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:** no explanation. It wrote only “NEUTRAL”, so the main reasons below are all it gave.

**Main reasons it gave:**
- Speculators net long fell 4.4% of open interest this week
- Fund's cost of holding is -7.4% annualized, heavy negative roll
- US crop condition improved by 2 points over 3 weeks, indicating more supply
- Treasury yields fell modestly, no macro policy surprise

<details><summary><b>News</b> — score +0.00</summary>

- [Corn Selling Continues on Tuesday](https://www.barchart.com/story/news/8250577/corn-selling-continues-on-tuesday)  
  <sub>Barchart.com, 18 hours ago</sub>  
  Corn futures posted losses of a penny to 5 cents across the board on Tuesday, as the fund selling continues. The CmdtyView national average Cash Corn price...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.06% (-0.03 on the week) | 5-year 4.93% (-0.07 on the week) | 10-year 5.10% (-0.09 on the week) | 30-year 5.41% (-0.11 on the week)
Yield curve, 10-year minus 3-month: +1.04 points -- upward sloping (normal)
US dollar index: 101.77 (-0.78 on the week)
Volatility (VIX): 17.03 (+0.2 on the week) -- elevated
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 17.86 (bar of 2026-10-21), from 502 daily bars
Trend: vs 20d SMA 18.78 (-4.9%), 50d 19.24 (-7.2%), 200d 18.18 (-1.8%); 50d above 200d
Momentum: RSI(14) 26.5 | MACD -0.393 vs signal -0.280 (histogram -0.114)
Returns: 1d +0.0% | 5d -3.0% | 1m -10.6% | 3m -2.5%
52-week range: 16.47 - 20.29 (now 36.4% of the way up)
Volatility: ATR(14) 0.29 (1.6% of price) | annualised 20d 16.0%
Volume: 1.16x the 20-day average
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
Cost of holding this fund instead of corn itself: -7.4% a year -- heavy: rolling contracts costs this fund real money
Measured: 3 months: fund -2.5%, commodity -0.5%, gap -2.0% | 6 months: fund -1.9%, commodity +1.7%, gap -3.6% | 12 months: fund +1.7%, commodity +9.1%, gap -7.4%
A commodity fund holds futures, not corn, and must sell each expiring contract to buy the next one. Where the next month costs more, that roll loses money every month. This gap is what the structure has actually cost, fees included -- it is history rather than a forecast, and it is not a direction: heavy carry is a reason to want a larger move to justify a long, and a tailwind for a short.
```

</details>

<details><summary><b>How much oil and gas is in storage</b> — score -0.40</summary>

_Not available today._

</details>

<details><summary><b>How the crop is growing</b> — score -0.40</summary>

```text
Corn rated good or excellent: 56% of the US crop (week 42 of 2026)
Direction over 3 weeks: steady, +2 points
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
Contract: CORN - CHICAGO BOARD OF TRADE (positions as of 2026-10-13, published the following Friday)
Large speculators: net long 13.4% of open interest (1,845,260 contracts)
Change on the week: -4.4% of open interest
Crowding: 78% percentile over 52 weeks -- within its normal range
Read this as crowding, not as a forecast: an extreme is as often the end of a move as the middle of one.
```

</details>

<details><summary><b>Money going into and out of this fund</b> — score -0.30</summary>

```text
Direction: money going out (1 month)
Share count change: 1 week: +2.3% (2.91M) over 7d | 1 month: -12.6% (-18.57M) over 32d
Shares outstanding: 7.22M | fund size: 129.01M
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Copper (CPER) · Commodity — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:** no explanation. It wrote only “NEUTRAL”, so the main reasons below are all it gave.

**Main reasons it gave:**
- Macro data stable: yields down slightly, dollar down, VIX unchanged
- Technical indicators mixed: price near 52‑week high, RSI 46.9, MACD negative, low volume
- Cost of holding drag of -4.9% per year reduces long attractiveness
- Positioning shows net long decreasing by -0.7% of open interest
- Fund flows show net outflows of -6.2% over the past month

<details><summary><b>News</b> — score +0.00</summary>

- [Commodity markets diverge as oil outpaces cracks in copper, gold - BofA (DBC:NYSEARCA)](https://seekingalpha.com/news/4654758-commodity-markets-diverge-as-oil-outpaces-cracks-in-copper-gold---bofa)  
  <sub>Seeking Alpha, 24 hours ago</sub>  
  Commodity markets (DBC) are splintering as surging Brent crude oil (BNO) (CO1:COM) targets multi-year highs, while copper (CPER) and gold (GLD) (XAUUSD:CUR)...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.06% (-0.03 on the week) | 5-year 4.93% (-0.07 on the week) | 10-year 5.10% (-0.09 on the week) | 30-year 5.41% (-0.11 on the week)
Yield curve, 10-year minus 3-month: +1.04 points -- upward sloping (normal)
US dollar index: 101.77 (-0.78 on the week)
Volatility (VIX): 17.03 (+0.2 on the week) -- elevated
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 39.54 (bar of 2026-10-21), from 502 daily bars
Trend: vs 20d SMA 39.89 (-0.9%), 50d 39.85 (-0.8%), 200d 37.80 (+4.6%); 50d above 200d
Momentum: RSI(14) 46.9 | MACD -0.055 vs signal 0.005 (histogram -0.060)
Returns: 1d -0.5% | 5d -0.3% | 1m -4.5% | 3m +3.4%
52-week range: 30.53 - 41.43 (now 82.7% of the way up)
Volatility: ATR(14) 0.55 (1.4% of price) | annualised 20d 15.5%
Volume: 0.22x the 20-day average
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
Cost of holding this fund instead of copper itself: -4.9% a year -- a steady drag
Measured: 3 months: fund +3.4%, commodity +4.3%, gap -0.8% | 6 months: fund +5.2%, commodity +7.4%, gap -2.2% | 12 months: fund +26.6%, commodity +31.5%, gap -4.9%
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

<details><summary><b>Buying and selling by company insiders</b> — score -0.10</summary>

_Not available today._

</details>

<details><summary><b>Who is positioned how</b> — score -0.10</summary>

```text
Contract: COPPER- #1 - COMMODITY EXCHANGE INC. (positions as of 2026-10-13, published the following Friday)
Large speculators: net long 19.5% of open interest (313,832 contracts)
Change on the week: -0.7% of open interest
Crowding: 15% percentile over 52 weeks -- within its normal range
Read this as crowding, not as a forecast: an extreme is as often the end of a move as the middle of one.
```

</details>

<details><summary><b>Money going into and out of this fund</b> — score -0.10</summary>

```text
Direction: money going out (1 month)
Share count change: 1 week: +1.7% (11.82M) over 7d | 1 month: -6.2% (-47.18M) over 32d
Shares outstanding: 18.04M | fund size: 713.50M
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Silver (SLV) · Commodity — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:** no explanation. It wrote only “NEUTRAL”, so the main reasons below are all it gave.

**Main reasons it gave:**
- US 10-year Treasury yield up 0.09% week, no surprise
- SLV price below 20d, 50d, 200d SMAs; RSI 39.5 (oversold) and volume 0.29x 20‑day avg
- CFTC large speculators net long 5.2% down 2% week; crowded short (8% percentile)
- Cost of holding -4.2% annual drag versus spot silver

<details><summary><b>News</b> — score +0.00</summary>

- [Current price of silver as of Wednesday, Oct. 21, 2026](https://fortune.com/article/current-price-of-silver-10-21-2026/)  
  <sub>Fortune, 3 hours ago</sub>  
  If you're worried about increased inflation, adding precious metals like silver to your portfolio can be a smart choice.
- [Silver Price Forecast: Recovery Stalls as Treasury Yields Rise](https://www.fxempire.com/forecasts/article/silver-price-forecast-recovery-stalls-as-treasury-yields-rise-1639418)  
  <sub>FXEmpire, 7 hours ago</sub>  
  Silver is under pressure as firmer yields, a stronger dollar and December Fed expectations keep buyers from extending the recovery.
- [A Sterling Thesis: The Long-Term Silver Investment Case](https://www.etftrends.com/gold-silver-investing-content-hub/sterling-thesis-silvers-long-term-investment-case/)  
  <sub>ETF Trends, 20 hours ago</sub>  
  The price of silver may have stumbled in September, but the metal's potent industrial applications have kept its price up across Q3.
- [Gold & Silver ETFs Fall Together; IT ETFs Rally on Oct 21](https://hdfcsky.com/news/gold-silver-etfs-fall-it-etfs-rally-banks-defence-down)  
  <sub>HDFC Sky, 9 hours ago</sub>  
  All 26 gold ETFs and 19 silver ETFs declined on Oct 21, with silver weaker over 30 days. IT ETFs rallied up to 2.74%, while bank and defence ETFs slipped as...
- [VanEck Gold Miners ETF (GDX) Stock Price, News, Quote & History](https://ca.finance.yahoo.com/quote/GDX/)  
  <sub>Yahoo! Finance Canada, 20 hours ago</sub>  
  Find the latest VanEck Gold Miners ETF (GDX) stock quote, history, news and other vital information to help you with your stock trading and investing.
- [Gold (XAUUSD) & Silver Price Forecast: ETF Holdings Hit Record, Can Gold Hold $4,083?](https://www.fxempire.com/forecasts/article/gold-xauusd-silver-price-forecast-etf-holdings-hit-record-can-gold-hold-4083-1639397)  
  <sub>FXEmpire, 9 hours ago</sub>  
  Gold (XAUUSD) and silver price forecast: record ETF holdings clash with 94% December hike odds as gold eyes $4083 support and silver tests $57.39.
- [408x Oversubscribed AI IPO Crashes 32%—Democratic Sweep Prospects Trigger Selling in Data Center Stocks](https://www.benzinga.com/Opinion/26/10/62474366/408x-oversubscribed-ai-ipo-crashes-32-democratic-sweep-prospects-trigger-selling-in-data-center-stocks)  
  <sub>Benzinga, 24 hours ago</sub>  
  AI Boom Warning Please click here for an enlarged chart of Direxion Daily Semiconductor Bull 3X ETF (NYSE:SOXL). Note the following: Semiconductors reflect...
- [Silver Rate Today Live, Latest Silver Price In India](https://www.ndtvprofit.com/silver-rates)  
  <sub>NDTV Profit, 8 hours ago</sub>  
  Track the silver rates today in India with live updates. Check the latest silver prices, daily movements, historical trends, news and key market insights on...
- [Gold, Silver rates today, October 21: Gold gets costlier or cheaper? Check 24K, 22K gold prices in 10 cities](https://upstox.com/news/personal-finance/commodities/gold-silver-rates-today-october-21-gold-gets-costlier-or-cheaper-check-24-k-22-k-gold-prices-in-10-cities/article-202152/)  
  <sub>Upstox, 8 hours ago</sub>  
  Gold and silver rates today, October 21, 2026: Check 24K, 22K and 18K gold prices and silver rates in Delhi, Mumbai, Chennai and 7 other cities ahead of...
- [Silver Rate Today in Gulbarga 21st October 2026 : 1 KG, Todays Silver Price in Gulbarga](https://www.businesstoday.in/commodity/silver-rate-in-gulbarga-today)  
  <sub>Business Today, 8 hours ago</sub>  
  Silver Price in Gulbarga Today 21st October 2026: Find updated 1 KG Silver rate today in Gulbarga 21st October 2026. Also check latest gold price related...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.06% (-0.03 on the week) | 5-year 4.93% (-0.07 on the week) | 10-year 5.10% (-0.09 on the week) | 30-year 5.41% (-0.11 on the week)
Yield curve, 10-year minus 3-month: +1.04 points -- upward sloping (normal)
US dollar index: 101.77 (-0.78 on the week)
Volatility (VIX): 17.03 (+0.2 on the week) -- elevated
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 51.99 (bar of 2026-10-21), from 502 daily bars
Trend: vs 20d SMA 54.01 (-3.7%), 50d 57.37 (-9.4%), 200d 65.18 (-20.2%); 50d below 200d
Momentum: RSI(14) 39.5 | MACD -1.607 vs signal -1.461 (histogram -0.146)
Returns: 1d -0.2% | 5d +3.5% | 1m -14.4% | 3m -0.1%
52-week range: 42.40 - 105.60 (now 15.2% of the way up)
Volatility: ATR(14) 1.41 (2.7% of price) | annualised 20d 36.6%
Volume: 0.29x the 20-day average
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
Cost of holding this fund instead of silver itself: -4.2% a year -- a steady drag
Measured: 3 months: fund -0.1%, commodity +0.1%, gap -0.2% | 6 months: fund -26.1%, commodity -25.8%, gap -0.4% | 12 months: fund +8.9%, commodity +13.1%, gap -4.2%
A commodity fund holds futures, not silver, and must sell each expiring contract to buy the next one. Where the next month costs more, that roll loses money every month. This gap is what the structure has actually cost, fees included -- it is history rather than a forecast, and it is not a direction: heavy carry is a reason to want a larger move to justify a long, and a tailwind for a short.
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
Contract: SILVER - COMMODITY EXCHANGE INC. (positions as of 2026-10-13, published the following Friday)
Large speculators: net long 5.2% of open interest (108,433 contracts)
Change on the week: -2.0% of open interest
Crowding: 8% percentile over 52 weeks -- a crowded short by the standards of the past year
Read this as crowding, not as a forecast: an extreme is as often the end of a move as the middle of one.
```

</details>

<details><summary><b>Money going into and out of this fund</b> — score -0.20</summary>

```text
Direction: flat (1 month)
Share count change: 1 week: +0.0% (0.00) over 7d | 1 month: +0.0% (0.00) over 33d
Shares outstanding: 341.45M | fund size: 17.75B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Soybeans (SOYB) · Commodity — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:** no explanation. It wrote only “NEUTRAL”, so the main reasons below are all it gave.

**Main reasons it gave:**
- No macro surprise: yields and dollar moved modestly, VIX stable
- Technicals: price below 20‑day and 50‑day SMA, RSI 35.8, no decisive break
- Positioning: net long 23.3% of OI, crowding 92% percentile, change +0.3% OI
- Crop condition: US soybeans rating steady, slight 1‑point decline over 3 weeks
- Cost of holding near zero (-0.1% per year), indicating physically backed fund

<details><summary><b>News</b> — score +0.00</summary>

_No news found for this one today._

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.06% (-0.03 on the week) | 5-year 4.93% (-0.07 on the week) | 10-year 5.10% (-0.09 on the week) | 30-year 5.41% (-0.11 on the week)
Yield curve, 10-year minus 3-month: +1.04 points -- upward sloping (normal)
US dollar index: 101.77 (-0.78 on the week)
Volatility (VIX): 17.03 (+0.2 on the week) -- elevated
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 26.60 (bar of 2026-10-21), from 502 daily bars
Trend: vs 20d SMA 27.30 (-2.6%), 50d 27.15 (-2.0%), 200d 24.95 (+6.6%); 50d above 200d
Momentum: RSI(14) 35.8 | MACD -0.146 vs signal -0.018 (histogram -0.129)
Returns: 1d -0.4% | 5d -2.2% | 1m -5.3% | 3m +2.0%
52-week range: 21.71 - 28.14 (now 76.0% of the way up)
Volatility: ATR(14) 0.28 (1.1% of price) | annualised 20d 10.6%
Volume: 1.23x the 20-day average
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
Cost of holding this fund instead of soybeans itself: -0.1% a year -- close to nothing, as a physically backed fund should be
Measured: 3 months: fund +2.0%, commodity +0.6%, gap +1.3% | 6 months: fund +8.5%, commodity +6.9%, gap +1.6% | 12 months: fund +20.6%, commodity +20.7%, gap -0.1%
A commodity fund holds futures, not soybeans, and must sell each expiring contract to buy the next one. Where the next month costs more, that roll loses money every month. This gap is what the structure has actually cost, fees included -- it is history rather than a forecast, and it is not a direction: heavy carry is a reason to want a larger move to justify a long, and a tailwind for a short.
```

</details>

<details><summary><b>How much oil and gas is in storage</b> — score +0.20</summary>

_Not available today._

</details>

<details><summary><b>How the crop is growing</b> — score +0.20</summary>

```text
Soybeans rated good or excellent: 57% of the US crop (week 41 of 2026)
Direction over 3 weeks: steady, -1 points
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
Contract: SOYBEANS - CHICAGO BOARD OF TRADE (positions as of 2026-10-13, published the following Friday)
Large speculators: net long 23.3% of open interest (1,072,235 contracts)
Change on the week: +0.3% of open interest
Crowding: 92% percentile over 52 weeks -- a crowded long by the standards of the past year
Read this as crowding, not as a forecast: an extreme is as often the end of a move as the middle of one.
```

</details>

<details><summary><b>Money going into and out of this fund</b> — score +0.00</summary>

```text
Direction: money coming in (1 month)
Share count change: 1 week: +2.7% (1.18M) over 7d | 1 month: +2.1% (927.30K) over 32d
Shares outstanding: 1.69M | fund size: 45.01M
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Natural gas (UNG) · Commodity — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Neutral overall; no material macro surprise, technicals show downtrend but no decisive break on volume, fundamentals are bearish but not decisive enough to tilt direction.

**Main reasons it gave:**
- Technical: price below 20‑day, 50‑day, 200‑day SMAs; RSI 40.5; low volume (no decisive break)
- Energy inventories: 67 BCF build, 83% percentile (bearish supply)
- EIA price outlook: forecast 18% price decline over six months
- Cost of holding: -5.2% annual roll cost (tailwind for short)

<details><summary><b>News</b> — score +0.00</summary>

- [Healthcare Just Broke Out to an All-Time High... And Nobody’s Talking About It by John Salama, CMT](https://www.theglobeandmail.com/investing/markets/stocks/IWM-A/pressreleases/8243728/healthcare-just-broke-out-to-an-all-time-high-and-nobodys-talking-about-it-by-john-salama-cmt/)  
  <sub>The Globe and Mail, 21 hours ago</sub>  
  Detailed price information for Ishares Russell 2000 ETF (IWM-A) from The Globe and Mail including charting and trades.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.06% (-0.03 on the week) | 5-year 4.93% (-0.07 on the week) | 10-year 5.10% (-0.09 on the week) | 30-year 5.41% (-0.11 on the week)
Yield curve, 10-year minus 3-month: +1.04 points -- upward sloping (normal)
US dollar index: 101.77 (-0.78 on the week)
Volatility (VIX): 17.03 (+0.2 on the week) -- elevated
```

</details>

<details><summary><b>Price and chart</b> — score -0.20</summary>

```text
Last close 10.09 (bar of 2026-10-21), from 502 daily bars
Trend: vs 20d SMA 10.77 (-6.3%), 50d 10.49 (-3.8%), 200d 11.25 (-10.3%); 50d below 200d
Momentum: RSI(14) 40.5 | MACD 0.008 vs signal 0.096 (histogram -0.088)
Returns: 1d -3.9% | 5d -10.1% | 1m -7.1% | 3m -4.9%
52-week range: 9.63 - 16.90 (now 6.3% of the way up)
Volatility: ATR(14) 0.38 (3.8% of price) | annualised 20d 47.1%
Volume: 0.41x the 20-day average
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
Cost of holding this fund instead of natural gas itself: -5.2% a year -- heavy: rolling contracts costs this fund real money
Measured: 3 months: fund -4.9%, commodity -3.1%, gap -1.8% | 6 months: fund -7.9%, commodity +3.9%, gap -11.7% | 12 months: fund -22.0%, commodity -16.8%, gap -5.2%
A commodity fund holds futures, not natural gas, and must sell each expiring contract to buy the next one. Where the next month costs more, that roll loses money every month. This gap is what the structure has actually cost, fees included -- it is history rather than a forecast, and it is not a direction: heavy carry is a reason to want a larger move to justify a long, and a tailwind for a short.
```

</details>

<details><summary><b>How much oil and gas is in storage</b> — score -0.60</summary>

```text
US inventories, week ending 2026-10-09 (published the following Wednesday)
  Natural gas: 3,567.0 billion cubic feet, +67.0 on the week (a build), 83% percentile over 52 weeks
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

<details><summary><b>Buying and selling by company insiders</b> — score -0.10</summary>

_Not available today._

</details>

<details><summary><b>Who is positioned how</b> — score -0.10</summary>

```text
Contract: NAT GAS NYME - NEW YORK MERCANTILE EXCHANGE (positions as of 2026-10-13, published the following Friday)
Large speculators: net short 7.3% of open interest (1,741,163 contracts)
Change on the week: +0.7% of open interest
Crowding: 12% percentile over 52 weeks -- within its normal range
Read this as crowding, not as a forecast: an extreme is as often the end of a move as the middle of one.
```

</details>

<details><summary><b>Money going into and out of this fund</b> — score -0.10</summary>

```text
Direction: flat (1 month)
Share count change: 1 week: +0.0% (0.00) over 7d | 1 month: +0.0% (0.00) over 33d
Shares outstanding: 12.08M | fund size: 121.93M
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Oil (USO) · Commodity — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:** no explanation. It wrote only “NEUTRAL”, so the main reasons below are all it gave.

**Main reasons it gave:**
- CFTC net long 2.1% of OI, down 0.7% week over week
- EIA weekly crude inventories draw 8.6M barrels, 15th percentile (bullish)
- EIA price outlook forecasts WTI falling to $86 in six months (bearish)
- Technicals: price above 20d/50d/200d SMAs, RSI 61, MACD positive, low volume

<details><summary><b>News</b> — score +0.00</summary>

- [Energy ETFs: How to Play the Sector's Surge](https://es.tradingview.com/news/zacks:4d0ab9783094b:0-energy-etfs-how-to-play-the-sector-s-surge/)  
  <sub>TradingView, 22 hours ago</sub>  
  Energy is the best-performing sector this year, up about 53%, significantly ahead of the second-best performer, information technology, which has gained...
- [VTI: Vanguard Total Stock Market ETF Latest Stock Price, Analysis, News and Trading Ideas](https://stocktwits.com/symbol/VTI)  
  <sub>Stocktwits, 8 hours ago</sub>  
  Get real-time Vanguard Total Stock Market ETF (VTI) stock price, news, financials, community insights, and trading ideas. Join 10 million+ investors and...
- [Oil prices end lower in volatile session amid reports of U.S.-Iran diplomacy (USO:NYSEARCA)](https://seekingalpha.com/news/4654972-oil-prices-end-lower-in-volatile-session-amid-reports-of-us-iran-diplomacy)  
  <sub>Seeking Alpha, 16 hours ago</sub>  
  Crude oil futures fell as traders weighed a reported meeting between Iran president and Pakistan's army ‌chief vs. continued Houthi attacks and reports of...
- [Exchange-Traded Funds Gain as US Equities Advance After Midday](https://finance.yahoo.com/markets/stocks/articles/exchange-traded-funds-gain-us-171124946.html)  
  <sub>Yahoo Finance, 23 hours ago</sub>  
  Broad Market Indicators Broad-market exchange-traded funds IWM and IVV rose. Actively traded Invesco QQQ Trust (QQQ) was little changed, erasing earlier...
- [Healthcare Just Broke Out to an All-Time High... And Nobody’s Talking About It by John Salama, CMT](https://www.theglobeandmail.com/investing/markets/stocks/IWM-A/pressreleases/8243728/healthcare-just-broke-out-to-an-all-time-high-and-nobodys-talking-about-it-by-john-salama-cmt/)  
  <sub>The Globe and Mail, 21 hours ago</sub>  
  Detailed price information for Ishares Russell 2000 ETF (IWM-A) from The Globe and Mail including charting and trades.
- [U.S. crude stockpiles fell 4.9M barrels last week, API says (USO:NYSEARCA)](https://seekingalpha.com/news/4654966-u-s-crude-stockpiles-fell-4_9m-barrels-last-week-api-says)  
  <sub>Seeking Alpha, 18 hours ago</sub>  
  The American Petroleum Institute reportedly shows a draw of 4.93M barrels of oil in US commercial stockpiles for the week ending October 16.
- [408x Oversubscribed AI IPO Crashes 32%—Democratic Sweep Prospects Trigger Selling in Data Center Stocks](https://www.benzinga.com/Opinion/26/10/62474366/408x-oversubscribed-ai-ipo-crashes-32-democratic-sweep-prospects-trigger-selling-in-data-center-stocks)  
  <sub>Benzinga, 24 hours ago</sub>  
  AI Boom Warning Please click here for an enlarged chart of Direxion Daily Semiconductor Bull 3X ETF (NYSE:SOXL). Note the following: Semiconductors reflect...
- [Rubio Says Trump Will Take Up To 60 Days To Assess Impact Of Russia-Related Sanctions And Tariffs: Report](https://stocktwits.com/news-articles/markets/equity/rubio-trump-60-days-russia-sanctions-tariffs-waiver-evaluate/cZxNOESRBtZ)  
  <sub>Stocktwits, 15 hours ago</sub>  
  Rubio's comments came a day after Trump waived key measures targeting Russian exports and countries that buy Russian energy.
- [Traders Are Heading to the Polls Early. Incumbent Mega-Cap Tech Stocks Are Still Winning the Race.](https://www.barchart.com/story/news/8247147/traders-are-heading-to-the-polls-early-incumbent-mega-cap-tech-stocks-are-still-winning-the-race)  
  <sub>Barchart.com, 19 hours ago</sub>  
  While political polls dominate the evening news, another set of ballots was just cast that tells us far more about our economic reality.
- [Middle East oil flows now surpass levels before U.S.-Iran war, Kpler says (CL1:COM:Commodity)](https://seekingalpha.com/news/4655180-middle-east-oil-flows-now-surpass-levels-before-us-iran-war-kpler-says)  
  <sub>Seeking Alpha, 1 hour ago</sub>  
  Middle East oil exports, including shipments through the Strait of Hormuz and alternative routes, surpassed pre-war levels despite escalating violence...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.06% (-0.03 on the week) | 5-year 4.93% (-0.07 on the week) | 10-year 5.10% (-0.09 on the week) | 30-year 5.41% (-0.11 on the week)
Yield curve, 10-year minus 3-month: +1.04 points -- upward sloping (normal)
US dollar index: 101.77 (-0.78 on the week)
Volatility (VIX): 17.03 (+0.2 on the week) -- elevated
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 158.46 (bar of 2026-10-21), from 502 daily bars
Trend: vs 20d SMA 151.15 (+4.8%), 50d 144.85 (+9.4%), 200d 120.62 (+31.4%); 50d above 200d
Momentum: RSI(14) 61.1 | MACD 4.034 vs signal 3.180 (histogram 0.853)
Returns: 1d -1.3% | 5d +3.2% | 1m +10.0% | 3m +13.6%
52-week range: 66.17 - 161.86 (now 96.4% of the way up)
Volatility: ATR(14) 4.84 (3.1% of price) | annualised 20d 33.7%
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

_Not available today._

</details>

<details><summary><b>How much oil and gas is in storage</b> — score +0.00</summary>

```text
US inventories, week ending 2026-10-09 (published the following Wednesday)
  Crude oil: 415.6 million barrels, -8.6 on the week (a draw), 15% percentile over 52 weeks
  Petrol: 208.3 million barrels, +3.5 on the week (a build), 21% percentile over 52 weeks
  Diesel: 102.6 million barrels, -2.5 on the week (a draw), 12% percentile over 52 weeks -- low for the time of year
A build is more supply than demand and a draw is the reverse, so a build reads bearish and a draw bullish -- as a rule of thumb, not a law. Weigh the change and how unusual the level is above the level itself, and remember the market has already seen this number.
```

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
Contract: WTI-PHYSICAL - NEW YORK MERCANTILE EXCHANGE (positions as of 2026-10-13, published the following Friday)
Large speculators: net long 2.1% of open interest (1,900,179 contracts)
Change on the week: -0.7% of open interest
Crowding: 35% percentile over 52 weeks -- within its normal range
Read this as crowding, not as a forecast: an extreme is as often the end of a move as the middle of one.
```

</details>

<details><summary><b>Money going into and out of this fund</b> — score -0.20</summary>

```text
Direction: flat (1 month)
Share count change: 1 week: +0.0% (0.00) over 7d | 1 month: +0.0% (0.00) over 33d
Shares outstanding: 119.10M | fund size: 18.87B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Wheat (WEAT) · Commodity — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:** no explanation. It wrote only “NEUTRAL”, so the main reasons below are all it gave.

**Main reasons it gave:**
- No macro surprise or data release outside expectations this week
- Technical indicators show price below 20‑day and 50‑day SMAs, low RSI (26.8) and negative MACD, but no decisive break on heavy volume
- Large speculators net short 6.4% of open interest, change -0.6% (moderate bearish sentiment)
- Fund flows show net outflows over the past month (-13.3% share count change)

<details><summary><b>News</b> — score +0.00</summary>

_No news found for this one today._

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.06% (-0.03 on the week) | 5-year 4.93% (-0.07 on the week) | 10-year 5.10% (-0.09 on the week) | 30-year 5.41% (-0.11 on the week)
Yield curve, 10-year minus 3-month: +1.04 points -- upward sloping (normal)
US dollar index: 101.77 (-0.78 on the week)
Volatility (VIX): 17.03 (+0.2 on the week) -- elevated
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 23.06 (bar of 2026-10-21), from 502 daily bars
Trend: vs 20d SMA 24.58 (-6.2%), 50d 25.54 (-9.7%), 200d 23.46 (-1.7%); 50d above 200d
Momentum: RSI(14) 26.8 | MACD -0.564 vs signal -0.427 (histogram -0.137)
Returns: 1d -2.1% | 5d -5.5% | 1m -11.3% | 3m -10.0%
52-week range: 19.88 - 28.00 (now 39.2% of the way up)
Volatility: ATR(14) 0.48 (2.1% of price) | annualised 20d 17.9%
Volume: 1.69x the 20-day average
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
Cost of holding this fund instead of wheat itself: -11.3% a year -- heavy: rolling contracts costs this fund real money
Measured: 3 months: fund -10.0%, commodity -9.9%, gap -0.2% | 6 months: fund +0.9%, commodity +4.7%, gap -3.8% | 12 months: fund +13.0%, commodity +24.3%, gap -11.3%
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

<details><summary><b>Buying and selling by company insiders</b> — score -0.20</summary>

_Not available today._

</details>

<details><summary><b>Who is positioned how</b> — score -0.20</summary>

```text
Contract: WHEAT-SRW - CHICAGO BOARD OF TRADE (positions as of 2026-10-13, published the following Friday)
Large speculators: net short 6.4% of open interest (506,774 contracts)
Change on the week: -0.6% of open interest
Crowding: 58% percentile over 52 weeks -- within its normal range
Read this as crowding, not as a forecast: an extreme is as often the end of a move as the middle of one.
```

</details>

<details><summary><b>Money going into and out of this fund</b> — score -0.20</summary>

```text
Direction: money going out (1 month)
Share count change: 1 week: +2.3% (6.09M) over 7d | 1 month: -13.3% (-41.94M) over 32d
Shares outstanding: 11.90M | fund size: 274.48M
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Gold (GLD) · Commodity — no answer, no confidence given

<details><summary><b>News</b> — score n/a</summary>

- [These Factors Could Make This Gold ETF Shine](https://etfdb.com/leveraged-inverse-content-hub/factors-could-make-gold-etf-gld-shine/)  
  <sub>ETF Database, 56 minutes ago</sub>  
  Although it may be of little comfort to jilted investors, gold's 2026 slump is actually easily explainable.
- [Options Whale Alert: $28.10M Bearish Long Put Opened on $GLD](https://www.moomoo.com/news/post/1001832843/options-whale-alert-28-10m-bearish-long-put-opened-on)  
  <sub>Moomoo, 7 hours ago</sub>  
  SPDRGold ETF(GLD.US)$ closed down 0.54% at $377.65. A trader bought 3900 Jan 15, 2027 $450.00 puts to open a Long Put. The position carries a net debit of $
- [Gold: Relief On The Horizon](https://seekingalpha.com/article/4955814-gold-relief-on-the-horizon)  
  <sub>Seeking Alpha, 5 hours ago</sub>  
  Gold has faced headwinds from rising Treasury yields, but I see potential for a near-term reversal in yields, supporting gold prices.
- [VanEck Gold Miners ETF (GDX) Stock Price, News, Quote & History](https://ca.finance.yahoo.com/quote/GDX/)  
  <sub>Yahoo! Finance Canada, 20 hours ago</sub>  
  Find the latest VanEck Gold Miners ETF (GDX) stock quote, history, news and other vital information to help you with your stock trading and investing.
- [Gold ETFs to Watch Amid Fed Rate Hike & Oil Risks](https://www.zacks.com/stock/news/3012037/gold-etfs-to-watch-amid-fed-rate-hike-oil-risks)  
  <sub>Zacks Investment Research, 1 hour ago</sub>  
  Gold ETFs GLD, IAU and GLDM could regain momentum if easing rate expectations and geopolitical risks outweigh inflationary pressures.
- [GLD NTA 20-10-2026 $3.86172](https://www.businessdesk.co.nz/nzx-announcements/gld-etf-units/482146)  
  <sub>BusinessDesk | NZ, 17 hours ago</sub>  
  View the full NZX announcement for Smart Gold ETF (GLD): GLD NTA 20-10-2026 $3.86172. Financial updates and company disclosures on BusinessDesk.
- [Jim Cramer Prefers Gold to Bitcoin for Portfolio Insurance, but Backs 2 ‘Vetted’ Cryptos](https://www.bitget.com/amp/news/detail/12560605991485)  
  <sub>Bitget, 14 hours ago</sub>  
  CNBC host Jim Cramer told a young investor he prefers gold bullion to Bitcoin (BTC) for insuring a portfolio. However, he did not dismiss Bitcoin entirely a...
- [CIBC cuts Q4 gold price forecast to $4,500, then sees bounce to $5,200 in 2027 (GLD:NYSEARCA)](https://seekingalpha.com/news/4654945-cibc-cuts-q4-gold-price-forecast-to-4500-then-sees-bounce-to-5200-in-2027)  
  <sub>Seeking Alpha, 18 hours ago</sub>  
  Commodity analysts at CIBC Capital remain bullish on gold over the longer term even as the bank significantly lowers its price forecast for this year.
- [The Pivot: CoinShares Survey Suggests Crypto Investing No Longer for Speculation...It's Strategic!](https://www.advisorperspectives.com/webinars/2026/11/17/the-pivot-coinshares-survey-suggests-crypto-investing-no-longer-for-speculation-its-strategic?partnerref=APSidebar)  
  <sub>Advisor Perspectives, 23 hours ago</sub>  
  Crypto is pivoting from a speculative asset into a strategic allocation. A recent CoinShares survey shows that cryptocurrency is increasingly viewed as a...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score n/a</summary>

```text
US Treasury yields: 3-month 4.06% (-0.03 on the week) | 5-year 4.93% (-0.07 on the week) | 10-year 5.10% (-0.09 on the week) | 30-year 5.41% (-0.11 on the week)
Yield curve, 10-year minus 3-month: +1.04 points -- upward sloping (normal)
US dollar index: 101.77 (-0.78 on the week)
Volatility (VIX): 17.03 (+0.2 on the week) -- elevated
```

</details>

<details><summary><b>Price and chart</b> — score n/a</summary>

```text
Last close 378.79 (bar of 2026-10-21), from 502 daily bars
Trend: vs 20d SMA 381.56 (-0.7%), 50d 395.87 (-4.3%), 200d 414.64 (-8.6%); 50d below 200d
Momentum: RSI(14) 43.2 | MACD -4.041 vs signal -4.407 (histogram 0.366)
Returns: 1d +0.3% | 5d +0.7% | 1m -5.3% | 3m +2.0%
52-week range: 362.32 - 495.90 (now 12.3% of the way up)
Volatility: ATR(14) 5.44 (1.4% of price) | annualised 20d 20.2%
Volume: 0.36x the 20-day average
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
Cost of holding this fund instead of gold itself: -1.3% a year -- a steady drag
Measured: 3 months: fund +2.0%, commodity +2.6%, gap -0.6% | 6 months: fund -13.0%, commodity -12.6%, gap -0.4% | 12 months: fund -6.0%, commodity -4.7%, gap -1.3%
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
Contract: GOLD - COMMODITY EXCHANGE INC. (positions as of 2026-10-13, published the following Friday)
Large speculators: net long 27.0% of open interest (396,345 contracts)
Change on the week: -1.0% of open interest
Crowding: 50% percentile over 52 weeks -- within its normal range
Read this as crowding, not as a forecast: an extreme is as often the end of a move as the middle of one.
```

</details>

<details><summary><b>Money going into and out of this fund</b> — score n/a</summary>

```text
Direction: flat (1 month)
Share count change: 1 week: +0.0% (0.00) over 7d | 1 month: +0.0% (0.00) over 32d
Shares outstanding: 260.30M | fund size: 98.60B
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

