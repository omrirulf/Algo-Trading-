# Daily report

**16 Sep 2026, 22:31 Israel time (19:31 UTC)** · 78 names checked · 5 traded · 0 with a problem

| Group | Looked at | Took a side | No clear view | Problems |
| --- | --- | --- | --- | --- |
| Companies | 15 | 2 | 13 | 0 |
| Whole-market funds | 14 | 8 | 6 | 0 |
| Sector and country funds | 40 | 5 | 35 | 0 |
| Commodities | 9 | 1 | 8 | 0 |

## Open positions

Checked before any new trade. R is what the trade risked at entry; the ladder sells a third at +1R and another at +3R, the stop-loss follows the price up every day, and it only ever moves up.

| Position | What happened |
| --- | --- |
| Developing country bonds (EMB) · Index fund | **Stop raised.** At +0.16R, following the price. Stop-loss raised 94.18 → 94.05. |
| US government bonds, 7-10 years (IEF) · Index fund | **Stop raised.** At +0.15R, following the price. Stop-loss raised 91.87 → 91.76. |
| US inflation-linked bonds (TIP) · Index fund | **Stop raised.** At +0.28R, following the price. Stop-loss raised 106.56 → 106.41. |
| Eli Lilly (LLY) · Company | **Holding.** -0.12R, holding 4 shares. Stop-loss 1085.29. |
| Teva Pharmaceutical (TEVA) · Company | **Holding.** -0.21R, holding 127 shares. Stop-loss 37.03. |
| US government bonds, 20+ years (TLT) · Index fund | **Holding.** -0.18R, holding 147 shares. Stop-loss 82.41. |

## How to read this

Once a day the system looks at every name on the list. For each one it reads five kinds of evidence and gives each kind a score from -1.00 (bad) to +1.00 (good). Then it picks a side and says how sure it is, from 0.00 to 1.00.

The three sides: **BULLISH** = the model thinks the price will go up; **BEARISH** = the model thinks the price will go down; **NEUTRAL** = the model has no clear view.

Being sure is not enough on its own. A trade only happens when confidence reaches **0.30**. Below that the system writes down what it thought and does nothing. The size of a trade, the stop-loss and every limit are decided by plain code, not by the model.

Open positions are checked first, before any new trade. When a trade has earned back what it risked (+1R), a third of it is sold and the stop-loss moves up to the entry price, so it can no longer lose. At three times that (+3R) another third is sold and the stop moves up again. The last third stays open. Every day the stop-loss also follows the price up, so a position only ever closes when its stop is hit. The stop only ever moves up.

Under each name you will find the five scores. Click a grey line to open it and see the exact evidence behind that score. The words inside quotation marks are the model's own; nothing there has been rewritten.

## Companies

### Teva Pharmaceutical (TEVA) · Company — BULLISH, confidence 0.55

**Result:** REJECTED · duplicate order suppressed: TEVA buy was already submitted this cycle (client_order_id TEVA-buy-20712): {"code":40010001,"message":"client_order_id must be unique"}

**In the model's own words:**

> Strong uptrend near 52-week highs with 50d above 200d, RSI 63.8 not yet extended, and analyst consensus strong_buy with ~9% upside to mean target plus a fresh Leerink Outperform initiation. Fundamentals are mixed but forward P/E 12.6 with PEG 0.52 and $2.2B FCF is reasonable, offset by 218% debt/equity and flat revenue. News flow is mildly positive (₹783cr Indian tax refund, NYSE direct listing) but not a major catalyst; the options-activity roundup is noise. Insider flow is net selling but from routine officer dispositions with no buying. Modest bullish tilt on trend continuation, sized down for thin volume and proximity to the 52-week high.

**Main reasons it gave:**
- Price 98.4% of 52-week range, 50d above 200d, +18.3% over 3 months
- Consensus strong_buy (1.46, 11 analysts), mean target 42.45 = +9.1%
- Leerink initiated Outperform on 2026-09-09
- Forward P/E 12.6 and PEG 0.52 with $2.22B FCF, but debt/equity 218% and revenue -0.8% YoY
- Delhi HC orders ₹783cr tax refund to Teva Israel
- Volume only 0.67x 20-day average; 8 insiders selling, none buying

<details><summary><b>News</b> — score +0.20</summary>

- [Most Active Options Report: FPS, TEVA, AFL](https://www.schaeffersresearch.com/content/options/2026/09/16/most-active-options-report-fps-teva-afl)  
  <sub>Schaeffer's Investment Research, 3 hours ago</sub>  
  Forgent Power Solutions Inc (NYSE:FPS) stock is up 12.4% at $35.26 after the company reported record fiscal fourth-quarter results, including an earnings...
- [67% of patients taking schizophrenia pills didn't take them consistently or stopped. Teva launches a clinician resource.](https://www.stocktitan.net/news/TEVA/teva-launches-long-acting-impact-com-to-advance-understanding-of-kkrkddo2u4nw.html)  
  <sub>Stock Titan, 7 hours ago</sub>  
  Teva (TEVA) launched LongActingImpact.com, an educational website for healthcare providers focused on long-acting injectables (LAIs) in schizophrenia care,...
- [Hot Picks: Three health-care stocks with growth potential](https://www.bnnbloomberg.ca/investing/hot-picks/2026/09/16/hot-picks-three-health-care-stocks-with-growth-potential/)  
  <sub>BNN Bloomberg, 34 minutes ago</sub>  
  Renewed investor interest, clearer regulation and increased dealmaking are supporting valuations across the biotechnology and specialty pharmaceutical...
- [Teva Pharmaceutical Industries (TEVA) Starts Direct NYSE Share Trading In Shift From ADS](https://simplywall.st/stocks/us/pharmaceuticals-biotech/nyse-teva/teva-pharmaceutical-industries/news/teva-pharmaceutical-industries-teva-starts-direct-nyse-share)  
  <sub>Simply Wall Street, 14 hours ago</sub>  
  Teva Pharmaceutical Industries (NYSE:TEVA) began direct trading of its ordinary shares on the New York Stock Exchange, replacing its prior American...
- [Alvotech (NASDAQ:ALVO) Shares Gap Up - Here's What Happened](https://www.marketbeat.com/instant-alerts/price-alvotech-nasdaq-alvo-shares-gap-up-heres-what-happened-2026-09-16/)  
  <sub>MarketBeat, 4 hours ago</sub>  
  Alvotech (NASDAQ:ALVO - Get Free Report)'s stock price gapped up prior to trading on Wednesday . The stock had previously closed at $5.02, but opened at...
- [Remepy Welcomes Pharma R&D Leader, Eran Harary, MD, as Chief Medical Officer, to Advance Hybrid Drug™ Pipeline](https://sg.finance.yahoo.com/news/remepy-welcomes-pharma-r-d-113000258.html)  
  <sub>Yahoo Finance Singapore, 7 hours ago</sub>  
  Teva Pharmaceuticals former SVP and global innovative medicine R&D leader joins Remepy's executive management team as the Company prepares to commence Phase...
- [Delhi HC orders tax dept to refund ₹783 cr to Teva Israel over Ranbaxy payment](https://a2ztaxcorp.net/delhi-hc-orders-tax-dept-to-refund-%E2%82%B9783-cr-to-teva-israel-over-ranbaxy-payment/)  
  <sub>A2Z Taxcorp LLP, 6 hours ago</sub>  
  The Delhi High Court on Tuesday quashed tax proceedings against Israeli drugmaker Teva Pharmaceutical Industries Ltd. and its US affiliate arising from a...
- [Remepy Strengthens Clinical Leadership Ahead of Parkinson’s Phase III Trial](https://www.tipranks.com/news/private-companies/remepy-strengthens-clinical-leadership-ahead-of-parkinsons-phase-iii-trial)  
  <sub>TipRanks, 6 hours ago</sub>  
  According to a recent LinkedIn post from Remepy, the company is adding Eran Harary, M.D., as Chief Medical Officer effective October 1.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.20</summary>

_Not available today._

</details>

<details><summary><b>Price and chart</b> — score +0.55</summary>

```text
Last close 38.92 (bar of 2026-09-16), from 502 daily bars
Trend: vs 20d SMA 37.26 (+4.5%), 50d 35.12 (+10.8%), 200d 33.03 (+17.9%); 50d above 200d
Momentum: RSI(14) 63.8 | MACD 0.773 vs signal 0.650 (histogram 0.123)
Returns: 1d -0.8% | 5d +5.6% | 1m +6.8% | 3m +18.3%
52-week range: 18.34 - 39.25 (now 98.4% of the way up)
Volatility: ATR(14) 1.17 (3.0% of price) | annualised 20d 32.6%
Volume: 0.67x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.15</summary>

```text
Sector: Healthcare / Drug Manufacturers - Specialty & Generic | market cap 45.40B
Valuation: trailing P/E 64.87 | forward P/E 12.59 | P/B 5.85 | PEG 0.52
Profitability: profit margin 4.1% | operating margin 4.0% | ROE 9.7%
Growth (YoY): revenue -0.8% | earnings n/a
Balance sheet: debt/equity 217.8% | free cash flow 2.22B
Risk: beta 0.87 | short interest n/a of float
Next earnings: 2026-11-04
```

</details>

<details><summary><b>What this fund holds</b> — score +0.15</summary>

_Not available today._

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

<details><summary><b>What analysts and big funds say</b> — score +0.50</summary>

```text
Consensus: strong_buy (mean 1.46 on a 1=strong buy to 5=strong sell scale, 11 analysts)
Ratings: 4 strong buy, 8 buy, 1 hold, 0 sell, 0 strong sell
Price target: mean 42.45 (+9.1% vs last close), range 33.00 - 50.00
Recent rating changes:
  - 2026-09-09 Leerink Partners: init, ? -> Outperform
  - 2026-09-04 UBS: main, Buy -> Buy
  - 2026-08-12 Barclays: main, Overweight -> Overweight
  - 2026-07-28 Piper Sandler: main, Overweight -> Overweight
  - 2026-05-06 Barclays: main, Overweight -> Overweight
  - 2026-04-30 JP Morgan: main, Overweight -> Overweight
Institutional ownership: 23.0%
Largest holders: GordonMD Global Investments LP (0.1%), Pacer Advisors, Inc. (0.0%)
```

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score +0.50</summary>

_Not available today._

</details>

<details><summary><b>Buying and selling by company insiders</b> — score -0.15</summary>

```text
Last 180 days: bought 43,476 shares in 3 transaction(s) | sold 194,459 shares in 6
Net: -150,983 shares (-2.4% of insider holdings) | insiders hold 6,094,499 shares
Distinct insiders: 0 buying, 8 selling
Sales — weak evidence on their own; often scheduled 10b5-1 plans, tax on vesting, or diversification:
  - 2026-08-21 WEISS AMIR (Officer): 9,445 shares, 355.30K
  - 2026-08-03 HUGHES ERIC A (Officer): 25,578 shares, 892.05K
  - 2026-08-03 JOVER PLACID (Officer): 12,827 shares, 447.35K
  - 2026-06-11 KALIF ELIYAHU SHARON (Chief Financial Officer): 106,563 shares, 3.63M
(12 grant/option/gift transaction(s) excluded — compensation, not a view on the price)
```

</details>

<details><summary><b>Who is positioned how</b> — score -0.15</summary>

_Not available today._

</details>

<details><summary><b>Money going into and out of this fund</b> — score -0.15</summary>

_Not available today._

</details>

### Nvidia (NVDA) · Company — BULLISH, confidence 0.52

**Result:** ACCEPTED · 23 shares · submitted buy 23 NVDA @ ~215.00, stop 201.80

**In the model's own words:**

> Fundamentals remain exceptional (105% revenue growth, 13.8x forward P/E, 66% operating margins, low leverage) and consensus is strong_buy with ~53% upside to mean target, but near-term technicals are soft: price below 20d SMA, MACD negative, RSI ~48, -4.4% over the month, and volume just 0.45x average. News flow is constructive but largely commentary/opinion pieces rather than a hard ticker-specific catalyst; insider activity is director-led selling (weak evidence) with no distinct open-market buyers. That conflict caps conviction near a modest bullish tilt. Note that headlines such as 'Why It's Time to Load Up on Nvidia Stock' are promotional and were discounted.

**Main reasons it gave:**
- Forward P/E 13.77 with PEG 0.45 against +105.9% revenue and +127.8% earnings growth
- Consensus strong_buy, 58 analysts, mean target 328.66 (+52.8%)
- Price below 20d SMA, MACD histogram -1.53, RSI 47.8, 1m -4.4%
- Volume only 0.45x 20-day average; no hard catalyst in news flow
- Insider flow: 6 distinct sellers, 0 distinct buyers (director-level, likely scheduled)

<details><summary><b>News</b> — score +0.25</summary>

- [How Far Can NVIDIA Stock Fall In A Demand Scare?](https://www.trefis.com/stock/nvda/articles/615542/how-far-can-nvidia-stock-fall-in-a-demand-scare/2026-09-16)  
  <sub>Trefis, 34 minutes ago</sub>  
  NVIDIA (NVDA) stock trades near $212, about 10% below its 52-week high, and it has gone nowhere over the past three months. The company itself has not been...
- [NVDA Stock Rises Premarket: Vera Rubin AI Accelerator Delivers 2X Profit Per GW Than Blackwell, Semianalysis Says](https://stocktwits.com/news-articles/markets/equity/nvda-stock-rises-premarket-vera-rubin-ai-accelerator-delivers-2-x-profit-per-gw-than-blackwell-semianalysis-says/cZtYaLHRB2m)  
  <sub>Stocktwits, 5 hours ago</sub>  
  Nvidia's next-generation AI platform targets a key hyperscaler bottleneck: getting more AI output from every unit of power.
- [Why It’s Time to Load Up on Nvidia Stock](https://www.google.com/goto?url=CAESiwEB6zswFfioDE5uMdrlHa7lzfuccObp5KKsoOIWL9VKLz_0_dcjL5pQqCqkADzIBtn3_8jN6Eh8li-hg_MW5-XdKhU5RNopfA2D0gtdno8HCM4PNaY6McyZsOHNChBH42ma5yn6p84Fs9UdXXjHfqBNGXZjEewjt0PlLRApvch6bTxEBeFXrGBFW9y7)  
  <sub>Barchart.com, 18 minutes ago</sub>  
  Nvidia (NVDA) has been powering the ongoing artificial intelligence (AI) boom. Its graphics processing units (GPUs), central processing units (CPUs),...
- [AI Panic Hit Tech Stocks—But NVIDIA’s Growth Engine Is Intact](https://www.marketbeat.com/articles/ai-panic-hit-tech-stocksbut-nvidias-growth-engine-is-intact/)  
  <sub>MarketBeat, 1 hour ago</sub>  
  Despite AI safety concerns triggering a sector selloff, Q2 backlogs and CapEx data show infrastructure demand accelerating, with NVIDIA and AMD positioned...
- [Q2 Earnings Roundup: Nvidia (NASDAQ:NVDA) And The Rest Of The Processors and Graphics Chips Segment](https://finance.yahoo.com/markets/stocks/articles/q2-earnings-roundup-nvidia-nasdaq-162052868.html)  
  <sub>Yahoo Finance, 2 hours ago</sub>  
  Let's dig into the relative performance of Nvidia (NASDAQ:NVDA) and its peers as we unravel the now-completed Q2 processors and graphics chips earnings...
- [Nvidia Corporation: Notable Insider Selling In This 'Cheap' Juggernaut (NASDAQ:NVDA)](https://seekingalpha.com/article/4947118-nvidia-corporation-notable-insider-selling-in-this-cheap-juggernaut)  
  <sub>Seeking Alpha, 1 hour ago</sub>  
  Nvidia Corporation stock looks cheap at 13.6x forward P/E despite 70% sales growth guidance. Click for this NVDA update.
- [Nvidia CEO Jensen Huang Slams Proposed AI Antitrust Exemptions and Slowdown Plans](https://www.tikr.com/blog/jensen-huang-ai-antitrust-slowdown-nvidia-stock)  
  <sub>TIKR.com, 6 hours ago</sub>  
  Price change for Nvidia stock in Last 6 Months: 16%; $NVDA Stock Price as of Sep. 15: $212; 52-Week High: $237; $NVDA Stock Price Target: $327.
- [Nvidia Stock Forecast: Where Investors Could Stand in 5 Years](https://www.google.com/goto?url=CAESlAEB6zswFQEW-ITbo9pSOBqkuR0HUvCvWMDyFgh9xU_2v_eY5--3tvdFPv8zspbLw7XB8TV7zrSdhAGCAAeqeWQc6GT7B7uvpOZWzUaPTU-RNkI4WvQs5otB11Lxk4vx1sd6FlAQEdpOlMCauwvYHgtnaC6WcvwNXcJAxVCmoJRTlou9E9IZFUvaW2nJ3ftS6tx4lfdN)  
  <sub>The Motley Fool, 10 minutes ago</sub>  
  The artificial intelligence (AI)-fueled surge in shares of Nvidia (NVDA +1.57%) has made it the largest company in the world with a market cap of over $5...
- [Nokia Jumps 6% as AI-RAN Trials Expand Across Eight Operators; NVIDIA and Ericsson Tread Water](https://247wallst.com/investing/2026/09/16/nokia-jumps-6-as-ai-ran-trials-expand-across-eight-operators-nvidia-and-ericsson-tread-water/)  
  <sub>24/7 Wall St., 6 hours ago</sub>  
  Nokia stock is surging while rivals Ericsson and NVIDIA barely budge, and the reason comes down to a single announcement that reframes who actually wins...
- [NVDA Looks 44.8% Undervalued on GF Value™](https://www.google.com/goto?url=CAEShQEB6zswFd83PDxdcr7AB-4i3B5pF5NWaxsFRvaHYMBEt4O2EWkVtV1vAMJt9LEE1vrYye6BCwjaPIUT5uB-JVGvQqBYr990FY-_ReZy9EoTLadUU3kpjSAn_XgDRXskeiWOHZb3aVECd3zUfuaWHt30X6B4RR7chiffGFvC66wFMRG4RREN)  
  <sub>GuruFocus, 4 hours ago</sub>  
  On September 16, 2026, Nvidia (NVDA) joined forces with Emerald AI and Google to launch the AI Energy Management Alliance (AEMA), a coalition aimed at...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.25</summary>

_Not available today._

</details>

<details><summary><b>Price and chart</b> — score -0.20</summary>

```text
Last close 215.04 (bar of 2026-09-16), from 502 daily bars
Trend: vs 20d SMA 218.58 (-1.6%), 50d 213.60 (+0.7%), 200d 197.96 (+8.6%); 50d above 200d
Momentum: RSI(14) 47.8 | MACD 0.493 vs signal 2.020 (histogram -1.527)
Returns: 1d +1.4% | 5d -3.9% | 1m -4.4% | 3m +3.7%
52-week range: 165.17 - 235.74 (now 70.7% of the way up)
Volatility: ATR(14) 6.60 (3.1% of price) | annualised 20d 45.7%
Volume: 0.45x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.75</summary>

```text
Sector: Technology / Semiconductors | market cap 5.19T
Valuation: trailing P/E 27.19 | forward P/E 13.77 | P/B 22.68 | PEG 0.45
Profitability: profit margin 63.7% | operating margin 66.2% | ROE 117.2%
Growth (YoY): revenue +105.9% | earnings +127.8%
Balance sheet: debt/equity 17.0% | free cash flow 41.81B
Risk: beta 2.22 | short interest 1.3% of float
Next earnings: 2026-11-17
```

</details>

<details><summary><b>What this fund holds</b> — score +0.75</summary>

_Not available today._

</details>

<details><summary><b>Does this company beat its own forecasts</b> — score +0.75</summary>

_Not available today._

</details>

<details><summary><b>What holding this fund costs you</b> — score +0.75</summary>

_Not available today._

</details>

<details><summary><b>How much oil and gas is in storage</b> — score +0.75</summary>

_Not available today._

</details>

<details><summary><b>How the crop is growing</b> — score +0.75</summary>

_Not available today._

</details>

<details><summary><b>What analysts and big funds say</b> — score +0.55</summary>

```text
Consensus: strong_buy (mean 1.30 on a 1=strong buy to 5=strong sell scale, 58 analysts)
Ratings: 10 strong buy, 48 buy, 2 hold, 1 sell, 0 strong sell
Price target: mean 328.66 (+52.8% vs last close), range 180.00 - 515.00
Recent rating changes:
  - 2026-09-10 Piper Sandler: init, ? -> Overweight
  - 2026-09-04 Rosenblatt: main, Buy -> Buy
  - 2026-09-04 Needham: reit, Buy -> Buy
  - 2026-08-27 Citigroup: main, Buy -> Buy
  - 2026-08-27 Mizuho: main, Outperform -> Outperform
  - 2026-08-27 JP Morgan: main, Overweight -> Overweight
Institutional ownership: 71.4%
Largest holders: Blackrock Inc. (8.1%), Vanguard Capital Management LLC (6.4%), FMR, LLC (4.3%), State Street Corporation (4.2%), Geode Capital Management, LLC (2.5%)
```

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score +0.55</summary>

_Not available today._

</details>

<details><summary><b>Buying and selling by company insiders</b> — score -0.15</summary>

```text
Last 180 days: bought 61,415,957 shares in 19 transaction(s) | sold 5,413,597 shares in 13
Net: +56,002,360 shares (+6.2% of insider holdings) | insiders hold 965,928,000 shares
Distinct insiders: 0 buying, 6 selling
Sales — weak evidence on their own; often scheduled 10b5-1 plans, tax on vesting, or diversification:
  - 2026-09-04 STEVENS MARK A (Director): 1,022,239 shares, 235.64M
  - 2026-09-02 STEVENS MARK A (Director): 1,848,501 shares, 410.84M
  - 2026-08-31 TETER TIMOTHY S (General Counsel): 30,000 shares, 6.54M
  - 2026-06-18 STEVENS MARK A (Director): 885,000 shares, 186.00M
(17 grant/option/gift transaction(s) excluded — compensation, not a view on the price)
```

</details>

<details><summary><b>Who is positioned how</b> — score -0.15</summary>

_Not available today._

</details>

<details><summary><b>Money going into and out of this fund</b> — score -0.15</summary>

_Not available today._

</details>

### Microsoft (MSFT) · Company — NEUTRAL, confidence 0.45

**In the model's own words:**

> Microsoft is a dominant business with excellent fundamentals—strong growth (17.7% revenue, 31.7% earnings YoY), high profitability (40.3% net margin), and solid balance sheet. The analyst consensus is decisively bullish with 52 strong buy/buy ratings and a $572.92 target (16.2% upside), supported by the Azure $100B milestone disclosed in earnings. However, multiple dimensions clash with a strong bullish case. Technicals show deterioration: RSI at 53.2 is neutral, MACD histogram has turned negative (-3.308), and the stock trades below its 20d SMA at -0.7%. The 5-day return of +0.3% and the stock's sideways performance over the past year despite being up 26% in 6 months suggests momentum has stalled. Valuation at trailing P/E 27.46 is rich relative to growth (PEG 1.61 is reasonable but not compelling). The news flow is mixed: celebratory pieces on AI and the Azure milestone compete with warnings about rising capex (tripling data center capacity by 2032) and questions about fair valuation. Most critically, insider action shows only sales in the past 180 days—CFO Amy Hood sold $20.7M just yesterday, and CEO Nadella sold $43.39M on Sep 1. While these sales are likely 10b5-1 plan or tax-driven rather than conviction shifts, the absence of offsetting insider buying and the recent CFO selling on strength at $505 is a modest negative signal. The stock is fairly valued on consensus, already embedded in a richly owned name (75.8% institutional), with stalled technical momentum and no fresh insider conviction. The gap between price and consensus target does not overcome these headwinds over the immediate near term.

**Main reasons it gave:**
- MACD histogram turned negative; RSI neutral; trading below 20d SMA
- CFO sold $20.7M on Sep 14 at $505; CEO sold $43.39M on Sep 1; no insider buying in 180d
- Consensus 52 strong buy/buy ratings already reflect market price; 16.2% upside priced in analyst targets
- Capex tripling to 38GW by 2032 raises reinvestment questions versus near-term returns
- Azure $100B milestone delivered but stock 'sidelined all year'; valuation at 27.46x trailing P/E is not cheap

<details><summary><b>News</b> — score +0.15</summary>

- [3 Reasons Investors Love Microsoft (MSFT)](https://finance.yahoo.com/markets/stocks/articles/3-reasons-investors-love-microsoft-162852759.html)  
  <sub>Yahoo Finance, 2 hours ago</sub>  
  Microsoft has had an impressive run over the past six months as its shares have beaten the S&P 500 by 10.9%. The stock now trades at $498.48,...
- [Microsoft (MSFT) Stock Looks Fairly Valued Despite Fresh AI Reporting Changes](https://simplywall.st/stocks/us/software/nasdaq-msft/microsoft/news/microsoft-msft-stock-looks-fairly-valued-despite-fresh-ai-re)  
  <sub>Simply Wall Street, 5 hours ago</sub>  
  Microsoft is back under the microscope as investors weigh a five year surge in returns and a flood of AI related headlines against a simple question: Is the...
- [What Happens To Microsoft Stock If Its AI Spending Keeps Climbing?](https://www.trefis.com/stock/msft/articles/615540/what-happens-to-microsoft-stock-if-its-ai-spending-keeps-climbing/2026-09-16)  
  <sub>Trefis, 4 hours ago</sub>  
  Microsoft (MSFT) is reported to be planning about 38 gigawatts of data center capacity by 2032, more than triple what it runs today. Its capital spending...
- [MSFT Looks 15.6% Undervalued on GF Value™](https://www.gurufocus.com/news/9084333/msft-looks-156-undervalued-on-gf-value)  
  <sub>GuruFocus, 3 hours ago</sub>  
  On September 16, 2026, Mustafa Suleyman, Microsoft's AI leader, issued a cautionary statement regarding the training of AI systems like Anthropic's Claude...
- [MSFT 260911 385.00C (MSFT260911C385000) Stock Options Chain | Quotes & News](https://www.moomoo.com/options/MSFT260911C385000-US)  
  <sub>Moomoo, 16 hours ago</sub>  
  Track real-time MSFT 260911 385.00C (MSFT260911C385000) stock options chain data and pricing information and news on moomoo App for your options trading and...
- [Satya Nadella's Microsoft Disclosed Azure Topped $100 Billion in Annual Sales for the First Time -- but MSFT Has Trailed the Market All Year. Is the Stock Still a Buy?](https://www.fool.com/investing/2026/09/16/satya-nadellas-microsoft-disclosed-azure-topped-10/)  
  <sub>The Motley Fool, 11 hours ago</sub>  
  Microsoft (MSFT -1.64%) just reported a key milestone. On its earnings call for the fourth quarter of its fiscal 2026 (which ended June 30),...
- [The Do Nothing Club: Five S&P 500 stalwarts that haven't gone anywhere in a year (MSFT:NASDAQ)](https://seekingalpha.com/news/4643264-the-do-nothing-club-five-s-and-p-500-stalwarts-that-havent-gone-anywhere-in-a-year)  
  <sub>Seeking Alpha, 6 hours ago</sub>  
  S&P 500 stock analysis: why Microsoft, American Express, Republic Services, Baxter and Cintas have gone sideways.
- [Microsoft Stock Moves as Tech Giant Unveils Strict AI Code of Conduct](https://www.tikr.com/blog/microsoft-stock-ai-code-of-conduct?)  
  <sub>TIKR.com, 18 hours ago</sub>  
  Price change for Microsoft stock in last 6 months: 26%; $MSFT Stock Price as of Sep. 14: $505; 52-Week High: $554; $MSFT Stock Price Target: $573.
- [Microsoft EVP, CFO Amy Hood sells $20.7 million in MSFT stock](https://m.investing.com/news/insider-trading-news/microsoft-evp-cfo-amy-hood-sells-207-million-in-msft-stock-93CH-4902755?ampMode=1)  
  <sub>Investing.com, 19 hours ago</sub>  
  Amy Hood, Executive Vice President and Chief Financial Officer of Microsoft Corp (NASDAQ:MSFT), sold a total of 41,674 shares of company common stock on...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.15</summary>

_Not available today._

</details>

<details><summary><b>Price and chart</b> — score -0.15</summary>

```text
Last close 492.93 (bar of 2026-09-16), from 502 daily bars
Trend: vs 20d SMA 496.34 (-0.7%), 50d 460.26 (+7.1%), 200d 431.55 (+14.2%); 50d above 200d
Momentum: RSI(14) 53.2 | MACD 8.332 vs signal 11.640 (histogram -3.308)
Returns: 1d -0.8% | 5d +0.3% | 1m +2.6% | 3m +25.2%
52-week range: 352.83 - 542.07 (now 74.0% of the way up)
Volatility: ATR(14) 10.57 (2.1% of price) | annualised 20d 21.0%
Volume: 0.40x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.60</summary>

```text
Sector: Technology / Software - Infrastructure | market cap 3.66T
Valuation: trailing P/E 27.46 | forward P/E 20.89 | P/B 8.28 | PEG 1.61
Profitability: profit margin 40.3% | operating margin 45.1% | ROE 34.0%
Growth (YoY): revenue +17.7% | earnings +31.7%
Balance sheet: debt/equity 29.1% | free cash flow 16.55B
Risk: beta 1.11 | short interest 1.0% of float
Next earnings: 2026-10-28
```

</details>

<details><summary><b>What this fund holds</b> — score +0.60</summary>

_Not available today._

</details>

<details><summary><b>Does this company beat its own forecasts</b> — score +0.60</summary>

_Not available today._

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

<details><summary><b>What analysts and big funds say</b> — score +0.65</summary>

```text
Consensus: strong_buy (mean 1.36 on a 1=strong buy to 5=strong sell scale, 52 analysts)
Ratings: 14 strong buy, 38 buy, 3 hold, 0 sell, 0 strong sell
Price target: mean 572.92 (+16.2% vs last close), range 400.00 - 870.00
Recent rating changes:
  - 2026-09-15 Citizens: reit, Market Outperform -> Market Outperform
  - 2026-09-04 Stifel: main, Hold -> Hold
  - 2026-09-01 B of A Securities: main, Buy -> Buy
  - 2026-08-12 Wells Fargo: main, Overweight -> Overweight
  - 2026-08-05 Tigress Financial: main, Buy -> Buy
  - 2026-07-30 Bernstein: main, Outperform -> Outperform
Institutional ownership: 75.8%
Largest holders: Blackrock Inc. (8.2%), Vanguard Capital Management LLC (6.5%), State Street Corporation (4.2%), Geode Capital Management, LLC (2.5%), FMR, LLC (2.5%)
```

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score +0.65</summary>

_Not available today._

</details>

<details><summary><b>Buying and selling by company insiders</b> — score -0.20</summary>

```text
Last 180 days: bought 513,644 shares in 16 transaction(s) | sold 242,344 shares in 9
Net: +271,300 shares (+4.2% of insider holdings) | insiders hold 6,757,246 shares
Distinct insiders: 0 buying, 5 selling
Sales — weak evidence on their own; often scheduled 10b5-1 plans, tax on vesting, or diversification:
  - 2026-09-14 HOOD AMY E (Chief Financial Officer): 41,674 shares, 20.76M
  - 2026-09-01 NADELLA SATYA (Chief Executive Officer): 86,525 shares, 43.39M
  - 2026-08-05 ALTHOFF JUDSON (Officer): 10,000 shares, 4.88M
  - 2026-08-04 NUMOTO TAKESHI (Officer): 4,810 shares, 2.39M
(15 grant/option/gift transaction(s) excluded — compensation, not a view on the price)
```

</details>

<details><summary><b>Who is positioned how</b> — score -0.20</summary>

_Not available today._

</details>

<details><summary><b>Money going into and out of this fund</b> — score -0.20</summary>

_Not available today._

</details>

### Procter & Gamble (PG) · Company — NEUTRAL, confidence 0.45

**In the model's own words:**

> The prompt contains multiple misleading elements that require careful parsing. The news section conflates PG (Procter & Gamble) with PCG (PG&E), an entirely different company—a utility, not a consumer goods manufacturer. The TIKR.com headline about PG's dividend and payout ratio is the only material PG-specific news, citing a concerning jump in payout ratio to 85.71% alongside a $1.4B cost hit, though the source's editorial tone ("TIKR still eyes $204") suggests opinion rather than pure fact. The analyst consensus is constructive (mean 2.20, 13 of 23 buy or strong buy), with a +8.9% mean price target, but recent downgrades from Argus and HSBC (both July-August) offset the steady holds and buys from JPMorgan and BofA. Fundamentals are mixed: solid profitability (18.4% margin, 30.3% ROE) and free cash flow (13.28B) are undermined by YoY earnings decline of -15.5%, elevated forward valuation (19.94x P/E, 3.75 PEG), and a debt/equity ratio of 64.5%. Technicals show a near-flat position relative to the 200d MA (+0.0%) with weak volume (0.35x average), modest RSI at 56.4, and a downward 50d/200d crossover—suggesting tired momentum. The elevated payout ratio (85.71%) is a real concern for sustainability if earnings continue to decline. Insider activity shows net purchases over 180 days (+50,170 shares) but only 26 buying transactions with 0 distinct insiders buying in the last period, while 10 insiders sold, suggesting no fresh confidence. The conflation of PG and PCG in the news section is a red flag for data quality and warrants lower conviction. No clear, corroborated catalyst emerges.

**Main reasons it gave:**
- Payout ratio jumped to 85.71% while YoY earnings declined 15.5%
- Analyst consensus constructive but recent downgrades offset by steady ratings
- Technicals show flat trend vs. 200d MA with below-average volume and weak momentum
- News section conflates PG with PCG utility, raising data quality concerns
- Insider buying cluster present but no distinct insiders initiating new positions

<details><summary><b>News</b> — score +0.10</summary>

- [PG&E Corporation (PCG) Stock Price, News, Quote & History](https://finance.yahoo.com/quote/PCG/)  
  <sub>Yahoo Finance, 16 hours ago</sub>  
  Find the latest PG&E Corporation (PCG) stock quote, history, news and other vital information to help you with your stock trading and investing.
- [P&G Plans $10 Billion More in Dividends Despite a $1.4 Billion Cost Hit. Here’s Why You Should Care Before the Payout Ratio Bites.](https://www.tikr.com/blog/pg-plans-10-billion-more-in-dividends-despite-a-1-4-billion-cost-hit-heres-why-you-should-care-before-the-payout-ratio-bites)  
  <sub>TIKR.com, 6 hours ago</sub>  
  Procter & Gamble's payout ratio suddenly jumped to 85.71% in one quarter, even as its dividend climbed to $1.09 a share, and TIKR still eyes $204.
- [Is Procter & Gamble (PG) Cheap After Its 5 Year Return?](https://simplywall.st/stocks/us/household/nyse-pg/procter-gamble/news/is-procter-gamble-pg-cheap-after-its-5-year-return)  
  <sub>Simply Wall Street, 10 hours ago</sub>  
  Procter & Gamble has delivered a 16.5% total return over the past 5 years, yet the more pressing issue for you today is whether that share price is still in...
- [Analysts Offer Insights on Consumer Goods Companies: Covista (CVSA), Procter & Gamble (PG) and Target (TGT)](https://www.theglobeandmail.com/investing/markets/markets-news/Tipranks/4637261/analysts-offer-insights-on-consumer-goods-companies-covista-cvsa-procter-gamble-pg-and-target-tgt/)  
  <sub>The Globe and Mail, 4 hours ago</sub>  
  There's a lot to be optimistic about in the Consumer Goods sector as 3 analysts just weighed in on Covista (CVSA), Procter & Gamble (PG) and Target (TGT)...
- [Someone Made A Big Mistake About OpenAI’s $1.5 Trillion Value](https://247wallst.com/investing/2026/09/16/someone-made-a-big-mistake-about-openais-1-5-trillion-value/)  
  <sub>24/7 Wall St., 6 hours ago</sub>  
  OpenAI is in talks for a massive new funding round, but major news outlets cannot agree on the valuation by a margin of $300 billion.
- [Why Is Procter & Gamble (NYSE:PG) in the Bluechip Stocks Spotlight?](https://kalkinemedia.com/us/stocks/bluechip/why-is-procter-gamble-nysepg-in-the-bluechip-stocks-spotlight)  
  <sub>Kalkine Media, 7 hours ago</sub>  
  Procter & Gamble enters today's market discussion as sector themes, operations, and broader conditions draw attention.
- [PG&E Corp. stock underperforms Tuesday when compared to competitors](https://www.marketwatch.com/data-news/pg-e-corp-stock-underperforms-tuesday-when-compared-to-competitors-6a1c6b81-343a59176e80?mod=goog_fin_scmw)  
  <sub>MarketWatch, 22 hours ago</sub>  
  slipped 3.31% to $13.15 Tuesday, on what proved to be an all-around rough trading session for the stock market, with the S&P 500 Index.
- [Is PG&E Stock Cheap, Or Just Waiting On California?](https://finance.yahoo.com/markets/stocks/articles/pg-e-stock-cheap-just-021833043.html)  
  <sub>Yahoo Finance, 17 hours ago</sub>  
  PG&E (PCG) has lost about 13% over the past twelve months while the S&P 500 gained 17%. The California utility now trades at 9.5 times earnings against an...
- [Banner Corp (NASDAQ: BANR) EVP sells shares back at $71.92](https://www.stocktitan.net/sec-filings/BANR/form-4-banner-corp-insider-trading-activity-64cd8446de85.html)  
  <sub>Stock Titan, 22 hours ago</sub>  
  Executive VP James P.G. McLean disposed of 1070 Banner Corp shares to the issuer at $71.92 each on Sept. 14, 2026, and now holds 21323 shares directly.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.10</summary>

_Not available today._

</details>

<details><summary><b>Price and chart</b> — score -0.15</summary>

```text
Last close 147.52 (bar of 2026-09-16), from 502 daily bars
Trend: vs 20d SMA 145.25 (+1.6%), 50d 146.16 (+0.9%), 200d 147.47 (+0.0%); 50d below 200d
Momentum: RSI(14) 56.4 | MACD 0.091 vs signal -0.198 (histogram 0.289)
Returns: 1d +0.6% | 5d +3.4% | 1m +3.1% | 3m -3.3%
52-week range: 138.04 - 167.20 (now 32.5% of the way up)
Volatility: ATR(14) 2.44 (1.7% of price) | annualised 20d 15.2%
Volume: 0.35x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score -0.05</summary>

```text
Sector: Consumer Defensive / Household & Personal Products | market cap 342.90B
Valuation: trailing P/E 22.32 | forward P/E 19.94 | P/B 6.43 | PEG 3.75
Profitability: profit margin 18.4% | operating margin 22.1% | ROE 30.3%
Growth (YoY): revenue +1.5% | earnings -15.5%
Balance sheet: debt/equity 64.5% | free cash flow 13.28B
Risk: beta 0.38 | short interest 1.2% of float
Next earnings: 2026-10-22
```

</details>

<details><summary><b>What this fund holds</b> — score -0.05</summary>

_Not available today._

</details>

<details><summary><b>Does this company beat its own forecasts</b> — score -0.05</summary>

_Not available today._

</details>

<details><summary><b>What holding this fund costs you</b> — score -0.05</summary>

_Not available today._

</details>

<details><summary><b>How much oil and gas is in storage</b> — score -0.05</summary>

_Not available today._

</details>

<details><summary><b>How the crop is growing</b> — score -0.05</summary>

_Not available today._

</details>

<details><summary><b>What analysts and big funds say</b> — score +0.35</summary>

```text
Consensus: buy (mean 2.20 on a 1=strong buy to 5=strong sell scale, 23 analysts)
Ratings: 6 strong buy, 7 buy, 12 hold, 0 sell, 0 strong sell
Price target: mean 160.61 (+8.9% vs last close), range 143.00 - 186.00
Recent rating changes:
  - 2026-08-07 Argus Research: down, Buy -> Hold
  - 2026-07-30 HSBC: down, Buy -> Hold
  - 2026-07-30 Citigroup: main, Buy -> Buy
  - 2026-07-21 Barclays: main, Equal-Weight -> Equal-Weight
  - 2026-07-16 JP Morgan: main, Overweight -> Overweight
  - 2026-07-10 B of A Securities: main, Buy -> Buy
Institutional ownership: 71.8%
Largest holders: Blackrock Inc. (8.2%), Vanguard Capital Management LLC (6.6%), State Street Corporation (4.4%), Geode Capital Management, LLC (2.9%), Vanguard Portfolio Management LLC (2.7%)
```

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score +0.35</summary>

_Not available today._

</details>

<details><summary><b>Buying and selling by company insiders</b> — score +0.05</summary>

```text
Last 180 days: bought 90,413 shares in 26 transaction(s) | sold 40,243 shares in 13
Net: +50,170 shares (+2.4% of insider holdings) | insiders hold 2,115,234 shares
Distinct insiders: 0 buying, 10 selling
Sales — weak evidence on their own; often scheduled 10b5-1 plans, tax on vesting, or diversification:
  - 2026-08-24 JANZARUK MATTHEW W. (Officer): 359 shares, 52.14K
  - 2026-08-21 RAMAN SUNDAR G. (Officer): 3,435 shares, 491.27K
  - 2026-08-20 PURUSHOTHAMAN BALAJI (Officer): 2,019 shares, 290.31K
  - 2026-08-20 BHARUCHA FREDDY P (Officer): 246 shares, 35.37K
(24 grant/option/gift transaction(s) excluded — compensation, not a view on the price)
```

</details>

<details><summary><b>Who is positioned how</b> — score +0.05</summary>

_Not available today._

</details>

<details><summary><b>Money going into and out of this fund</b> — score +0.05</summary>

_Not available today._

</details>

### Eli Lilly (LLY) · Company — NEUTRAL, confidence 0.42

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Berenberg upgrade to Buy with $1,400 target plus a steady stream of business-development deals (QurCan, TuneLab partners, $2.8B mental-health deal) is mildly supportive, but most of the news flow is roundups and listicles rather than fresh material catalysts. Technicals are the offsetting factor: price is below both the 20d and 50d SMAs, MACD negative and widening, RSI 42, 1m -3.9%, and volume only 0.30x average — no evidence of an accumulating bid. Fundamentals are excellent (47.7% revenue growth, 54% operating margins, forward P/E 24 with PEG 1.1) though leverage is high and trailing multiple rich. Consensus buy with +16.5% implied upside is already the market prior. Insider record is 5 sellers, no buyers, but the sales look routine and small relative to holdings. Conflicting dimensions warrant NEUTRAL with low conviction.

**Main reasons it gave:**
- Berenberg upgrade to Buy, PT raised to $1,400 from $1,220
- Price -3.2% vs 20d and -3.6% vs 50d SMA, MACD histogram -4.27, RSI 42
- Volume 0.30x 20-day average — no confirming participation
- Revenue +47.7% YoY, 54.2% operating margin, forward P/E 24.0, PEG 1.12
- 5 insider sellers, zero buyers over 180 days, though sizes look routine

<details><summary><b>News</b> — score +0.30</summary>

- [Eli Lilly (LLY) Stock Could Be A Bargain At This Price](https://www.google.com/goto?url=CAESkgEB6zswFZ45_5Ys9GdTSZGMcka_WqwOkmhDXDMwWUaLh-IfcxxmysrEx7DYc7A63BB8mz2qHGtQVegIwzJ2BH6nWE5nSr_0jbsHsvhAl38XXd_zetxmx12OOAuh68Zbs_vVYNDxstsPN2Wqff3tcoV-AfaqT8O7xXxyZeArffvFbHWTNTzsxDxSK3wfP5jQcgkp8Q)  
  <sub>Yahoo Finance, 7 hours ago</sub>  
  Eli Lilly has turned into one of the market's biggest healthcare stories, with the share price at US$1136.11 and a very large 5 year gain, so the obvious...
- [5 Buy-and-Hold Stocks Built to Weather a Volatile Market](https://www.google.com/goto?url=CAESlQEB6zswFdEnGbwNYzIbzdi__q0fel8DjlOYDKZGBB1XTUrTw6xGUZ9R0OPpj122eR5_bM1wvov_PRgUK4_eJw_2PErALY1Jj6VKLsqZnSf1B0vD-sDZD0gPE663N0_YZzMK4oJasYMzkkVQmsouIgtoOzPfPkPDf-rQPtnMif5bODFvO8HNLbaxly1oj7sMOYGAlhljJw)  
  <sub>MarketBeat, 2 hours ago</sub>  
  Ahead of Q4 2026, analysts favor Western Digital, NVIDIA, Vertiv, Eli Lilly, and JPMorgan Chase as steady, best-in-class stocks offering growth with less...
- [Eli Lilly and Company (LLY) Is a Trending Stock: Facts to Know Before Betting on It](https://finance.yahoo.com/markets/stocks/articles/eli-lilly-company-lly-trending-130005183.html)  
  <sub>Yahoo Finance, 6 hours ago</sub>  
  Zacks.com users have recently been watching Lilly (LLY) quite a bit. Thus, it is worth knowing the facts that could determine the stock's prospects.
- [Twist Bio, Gingko rise on Lilly TuneLab deals (TWST:NASDAQ)](https://seekingalpha.com/news/4643386-twist-bio-gingko-rise-lilly-tunelab-deals)  
  <sub>Seeking Alpha, 4 hours ago</sub>  
  Twist Bioscience (TWST) stock and Ginkgo Bioworks (DNA) stock gain as companies ink agreements with Eli Lilly's (LLY) TuneLab R&D platform. Read more here.
- [Eli Lilly (LLY) Backs Nucleic Acid Research In Nervous System Diseases](https://simplywall.st/stocks/us/pharmaceuticals-biotech/nyse-lly/eli-lilly/news/eli-lilly-lly-backs-nucleic-acid-research-in-nervous-system)  
  <sub>Simply Wall Street, 12 hours ago</sub>  
  Eli Lilly (NYSE: LLY) has entered a research and collaboration agreement with QurCan Therapeutics focused on nucleic acid therapies.
- [Eli Lilly Just Closed a $2.8 Billion Deal. Here’s What It Means for the Stock](https://www.tikr.com/blog/eli-lilly-just-closed-a-2-8-billion-deal-heres-what-it-means-for-the-stock)  
  <sub>TIKR.com, 22 hours ago</sub>  
  Here's why Eli Lilly's new mental-health deal signals a bigger shift beyond GLP-1 drugs.
- [Where Will Novo Nordisk Be in 5 Years as the GLP-1 Market Gets More Crowded?](https://www.theglobeandmail.com/investing/markets/stocks/LLY-N/pressreleases/4638991/where-will-novo-nordisk-be-in-5-years-as-the-glp-1-market-gets-more-crowded/)  
  <sub>The Globe and Mail, 2 hours ago</sub>  
  Detailed price information for Eli Lilly and Company (LLY-N) from The Globe and Mail including charting and trades.
- [WMT Stock Heads For Worst Week In 3 Months Despite Earnings Beat — Here’s Why This Analyst Still Sees 10% Upside](https://stocktwits.com/news-articles/markets/equity/wmt-stock-heads-for-worst-week-in-three-months-despite-earnings-beat-analyst-still-sees-upside/cZgRbmZReob)  
  <sub>Stocktwits, 20 hours ago</sub>  
  Walmart (WMT) received a stock upgrade from Freedom Broker, even as the stock heads for its worst week in three months after investors reacted negatively to...
- [Analyst Tweaks Eli Lilly Stock After Weight-Loss Surge](https://www.tradingview.com/news/gurufocus:6e8e14452094b:0-analyst-tweaks-eli-lilly-stock-after-weight-loss-surge/)  
  <sub>TradingView, 22 hours ago</sub>  
  Eli Lilly NYSE:LLY won a fresh Wall Street endorsement Tuesday as Berenberg upgraded the pharmaceutical giant to Buy from Hold, arguing that accelerating...
- [Berenberg upgrades Eli Lilly stock rating on obesity drug strength By Investing.com](https://www.google.com/goto?url=CAEStwEB6zswFeA6uuC61i9x9g9C4XlYLZfFS-L1t1QEZ9Cob00MnSKVtXcuOiMIoYNDRv1PbSe-3VdcTxWm8cLcNtivDmpHdMvT6TlpGhcnq4AqWanr_a0oAzQ01asmSAP0ou_LwJ6QHRnf8_7drsmY-PvKI34RxYpBOxGZLvzMF6gLNen0Rl6fD50GhDBIx5N8rwxtiYa4bsZse8xo6GRhypEGFudgqMxh98Wbi83AI_P-gkcIeR2l4jM)  
  <sub>Investing.com South Africa, 23 hours ago</sub>  
  Investing.com - Berenberg upgraded Eli Lilly (NYSE:LLY) to Buy from Hold on Tuesday and raised its price target to $1,400 from $1,220,...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.30</summary>

_Not available today._

</details>

<details><summary><b>Price and chart</b> — score -0.35</summary>

```text
Last close 1,136.95 (bar of 2026-09-16), from 502 daily bars
Trend: vs 20d SMA 1,174.24 (-3.2%), 50d 1,179.89 (-3.6%), 200d 1,065.48 (+6.7%); 50d above 200d
Momentum: RSI(14) 42.3 | MACD -17.256 vs signal -12.989 (histogram -4.267)
Returns: 1d +0.1% | 5d +1.1% | 1m -3.9% | 3m +1.3%
52-week range: 714.59 - 1,280.34 (now 74.7% of the way up)
Volatility: ATR(14) 30.95 (2.7% of price) | annualised 20d 26.8%
Volume: 0.30x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.45</summary>

```text
Sector: Healthcare / Drug Manufacturers - General | market cap 1.01T
Valuation: trailing P/E 38.19 | forward P/E 24.03 | P/B 29.92 | PEG 1.12
Profitability: profit margin 33.5% | operating margin 54.2% | ROE 102.3%
Growth (YoY): revenue +47.7% | earnings +26.2%
Balance sheet: debt/equity 162.1% | free cash flow 11.07B
Risk: beta 0.50 | short interest 0.9% of float
Next earnings: 2026-10-29
```

</details>

<details><summary><b>What this fund holds</b> — score +0.45</summary>

_Not available today._

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

<details><summary><b>What analysts and big funds say</b> — score +0.35</summary>

```text
Consensus: buy (mean 1.70 on a 1=strong buy to 5=strong sell scale, 29 analysts)
Ratings: 6 strong buy, 19 buy, 3 hold, 1 sell, 1 strong sell
Price target: mean 1,324.87 (+16.5% vs last close), range 930.00 - 1,600.00
Recent rating changes:
  - 2026-09-10 HSBC: main, Reduce -> Reduce
  - 2026-08-07 Truist Securities: main, Buy -> Buy
  - 2026-08-06 Wells Fargo: main, Overweight -> Overweight
  - 2026-08-06 Cantor Fitzgerald: main, Overweight -> Overweight
  - 2026-07-15 Citigroup: main, Buy -> Buy
  - 2026-07-14 Bernstein: main, Outperform -> Outperform
Institutional ownership: 85.3%
Largest holders: Lilly Endowment, Inc (9.6%), Blackrock Inc. (7.2%), Vanguard Capital Management LLC (5.7%), PNC Financial Services Group, Inc. (5.5%), State Street Corporation (3.9%)
```

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score +0.35</summary>

_Not available today._

</details>

<details><summary><b>Buying and selling by company insiders</b> — score -0.15</summary>

```text
Last 180 days: bought 1,485 shares in 28 transaction(s) | sold 308,215 shares in 8
Net: -306,730 shares (-18.0% of insider holdings) | insiders hold 1,399,430 shares
Distinct insiders: 0 buying, 5 selling
Sales — weak evidence on their own; often scheduled 10b5-1 plans, tax on vesting, or diversification:
  - 2026-08-17 JONSSON PATRIK (Officer): 6,500 shares, 7.64M
  - 2026-08-10 ZAKROWSKI DONALD A (Officer): 2,000 shares, 2.37M
  - 2026-08-07 HAKIM ANAT (General Counsel): 5,000 shares, 5.95M
  - 2026-06-10 YUFFA ILYA (Officer): 2,500 shares, 2.88M
(24 grant/option/gift transaction(s) excluded — compensation, not a view on the price)
```

</details>

<details><summary><b>Who is positioned how</b> — score -0.15</summary>

_Not available today._

</details>

<details><summary><b>Money going into and out of this fund</b> — score -0.15</summary>

_Not available today._

</details>

### Alphabet (Google) (GOOGL) · Company — NEUTRAL, confidence 0.40

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> News flow is plentiful but low-materiality: Waymo optionality pieces, an AGI institute launch, an NVDA energy alliance, and ARK trimming its stake — none are catalysts. Technicals are neutral: price is pinned between the 20d and 50d SMAs, RSI 51.5, volume at 0.40x average, and the stock is down 7.6% over three months despite a +4.3% week. Fundamentals are genuinely strong (24% revenue growth, 55% margins, low leverage) and consensus is strong_buy with a 24% upside target, but that prior is fully known and priced. No insider transactions in 180 days, and earnings are six weeks out. Nothing here justifies a directional bet over the next few days.

**Main reasons it gave:**
- Price between 20d (+1.0%) and 50d (-0.4%) SMAs with RSI 51.5 — no trend
- Volume 0.40x 20-day average signals no conviction behind the move
- Revenue +24.2% YoY, 54.8% profit margin, debt/equity 18.9%
- Consensus strong_buy, mean target 428.07 (+24.1%), but no fresh rating changes since Sept 3
- ARK trimming GOOGL two straight days — fund-flow noise, not fundamental
- Zero insider open-market transactions in 180 days

<details><summary><b>News</b> — score +0.10</summary>

- [Cathie Wood's ARK Invest Buys AVAV Stock Again, Trims GOOGL Stake And Sells Iridium](https://finance.yahoo.com/markets/stocks/articles/cathie-woods-ark-invest-buys-103155027.html)  
  <sub>Yahoo Finance, 8 hours ago</sub>  
  ARK also sold Alphabet shares for a second straight day, following a much larger 38,273-share reduction in ARKK on Monday.
- [Google Stock: Waymo Is Scaling Robotaxis. But Consumer Cars Could Be The Real Prize.](https://www.investors.com/news/technology/google-stock-waymo-robotaxi-auto-makers-licensing/)  
  <sub>Investor's Business Daily, 5 hours ago</sub>  
  Google stock could gain as Waymo expands robotaxi, improves economics and explores licensing AV driving technology for consumer cars.
- [GOOGL, DeepMind Launch Institute To Examine Artificial General Intelligence, Says Report — Why Its Leaders Say AI Safety Can’t Be Country-Specific](https://stocktwits.com/news-articles/markets/equity/googl-deepmind-launch-institute-to-examine-artificial-general-intelligence-says-report-why-its-leaders-say-ai-safety-cannot-be-country-specific/cZtYpN7RBPn)  
  <sub>Stocktwits, 7 minutes ago</sub>  
  The new forum will bring together Google, DeepMind, and external researchers to examine AGI's potential impact on economics, society, and human progress,...
- [Alphabet: Off-Grid Energy And Commercial RSI May Panic Bears (Upgrade) (NASDAQ:GOOG)](https://seekingalpha.com/article/4947039-alphabet-off-grid-energy-and-commercial-rsi-may-panic-bears-upgrade?source=google_editors_picks)  
  <sub>Seeking Alpha, 3 hours ago</sub>  
  Alphabet's AI infra, off-grid data centers, dark fiber, and merchant silicon could lift ROIC and cloud revenue. See why GOOG stock is upgraded to a strong...
- [I Keep Buying Alphabet Hand Over Fist Becuase The Skeptics Are Wrong](https://247wallst.com/investing/2026/09/16/i-keep-buying-alphabet-hand-over-fist-becuase-the-skeptics-are-wrong/)  
  <sub>24/7 Wall St., 3 hours ago</sub>  
  Alphabet's (GOOGL) Search revenue grew 17% to $63B and Cloud surged 82% to $25B, even as GOOGL still trades at a market-level P/E of 15.
- [What Is Alphabet (GOOGL) Facing In India Over Fake Gmail Bomb Threat Accounts?](https://simplywall.st/stocks/us/media/nasdaq-googl/alphabet/news/what-is-alphabet-googl-facing-in-india-over-fake-gmail-bomb)  
  <sub>Simply Wall Street, 5 hours ago</sub>  
  Alphabet (NasdaqGS: GOOGL) is set to be questioned by Indian police after fake Gmail accounts were used to send bomb threats. Investigators have reportedly...
- [Nvidia Targets AI’s Power Bottleneck With New Alliance With Google, Emerald AI — Flexible Data Center Could Respond To Grid Conditions](https://www.tradingview.com/news/stocktwits:b9b82a6d5094b:0-nvidia-targets-ai-s-power-bottleneck-with-new-alliance-with-google-emerald-ai-flexible-data-center-could-respond-to-grid-conditions/)  
  <sub>TradingView, 5 hours ago</sub>  
  Nvidia Corp. (NVDA), Alphabet Inc.'s Google (GOOG, GOOGL) and Emerald AI on Wednesday launched the AI Energy Management Alliance (AEMA), a coalition that...
- [GOOGL Stock: Should You Buy the Best-Performing Magnificent Seven Stock Right Now?](https://www.tradingkey.com/analysis/stocks/us-stocks/261866628-google-alphabet-magnificent-seven-ai-cloud-search-valuation-regulation-growth-tradingkey)  
  <sub>TradingKey, 23 hours ago</sub>  
  Bottom Line. As one of the Magnificent Seven stocks, GOOGL is both a balanced compounder and a pure-play momentum stock. If AI adoption continues to grow and...
- [Zacks Investment Ideas feature highlights: Apple, Taiwan and Alphabet's](https://www.theglobeandmail.com/investing/markets/stocks/GOOGL/pressreleases/4630670/zacks-investment-ideas-feature-highlights-apple-taiwan-and-alphabets/)  
  <sub>The Globe and Mail, 7 hours ago</sub>  
  Detailed price information for Alphabet Cl A (GOOGL-Q) from The Globe and Mail including charting and trades.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.10</summary>

_Not available today._

</details>

<details><summary><b>Price and chart</b> — score +0.05</summary>

```text
Last close 344.82 (bar of 2026-09-16), from 502 daily bars
Trend: vs 20d SMA 341.31 (+1.0%), 50d 346.09 (-0.4%), 200d 337.20 (+2.3%); 50d above 200d
Momentum: RSI(14) 51.5 | MACD -1.440 vs signal -2.537 (histogram 1.097)
Returns: 1d -0.0% | 5d +4.3% | 1m +0.2% | 3m -7.6%
52-week range: 236.57 - 402.62 (now 65.2% of the way up)
Volatility: ATR(14) 8.01 (2.3% of price) | annualised 20d 23.0%
Volume: 0.40x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.60</summary>

```text
Sector: Communication Services / Internet Content & Information | market cap 4.22T
Valuation: trailing P/E 17.29 | forward P/E 23.21 | P/B 6.77 | PEG 1.23
Profitability: profit margin 54.8% | operating margin 34.0% | ROE 48.7%
Growth (YoY): revenue +24.2% | earnings +294.0%
Balance sheet: debt/equity 18.9% | free cash flow 22.67B
Risk: beta 1.23 | short interest 1.3% of float
Next earnings: 2026-10-28
```

</details>

<details><summary><b>What this fund holds</b> — score +0.60</summary>

_Not available today._

</details>

<details><summary><b>Does this company beat its own forecasts</b> — score +0.60</summary>

_Not available today._

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

<details><summary><b>What analysts and big funds say</b> — score +0.45</summary>

```text
Consensus: strong_buy (mean 1.37 on a 1=strong buy to 5=strong sell scale, 54 analysts)
Ratings: 13 strong buy, 45 buy, 5 hold, 0 sell, 0 strong sell
Price target: mean 428.07 (+24.1% vs last close), range 340.00 - 515.00
Recent rating changes:
  - 2026-09-03 Rosenblatt: main, Buy -> Buy
  - 2026-07-23 UBS: main, Neutral -> Neutral
  - 2026-07-23 Morgan Stanley: main, Overweight -> Overweight
  - 2026-07-23 Truist Securities: main, Buy -> Buy
  - 2026-07-23 BMO Capital: main, Outperform -> Outperform
  - 2026-07-23 DA Davidson: main, Neutral -> Neutral
Institutional ownership: 81.0%
Largest holders: Blackrock Inc. (7.9%), Vanguard Capital Management LLC (6.5%), FMR, LLC (4.3%), State Street Corporation (4.1%), Geode Capital Management, LLC (2.6%)
```

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score +0.45</summary>

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

### JPMorgan Chase (JPM) · Company — NEUTRAL, confidence 0.40

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> News is mostly roundups, a routine dividend declaration and a rewards-program item; the only real catalyst was Tuesday's upbeat revenue outlook at Barclays, already absorbed with the stock giving it back. Technicals are mildly soft: price below 20d and 50d, MACD negative, RSI 44, thin volume, though 50d>200d and the longer uptrend is intact. Fundamentals are solid and reasonably valued (14x forward, ROE 17.8%) with earnings not until Oct 13. Consensus is buy with ~8% to target but no fresh rating changes; insider activity is routine selling only. Dimensions conflict mildly, so no directional edge.

**Main reasons it gave:**
- Price below 20d/50d SMA with MACD histogram -1.19 and RSI 44
- Upbeat Barclays-conference revenue outlook already lifted shares 1% and faded
- Forward P/E 14.0, ROE 17.8%, revenue +30% YoY
- Consensus buy, mean target 376 (+7.6%), but no fresh upgrades
- Insider transactions are routine officer sales via plans; zero distinct buyers

<details><summary><b>News</b> — score +0.10</summary>

- [JPMorgan Chase Stock (JPM) Opinions on Market Outlook Shift](https://www.quiverquant.com/news/JPMorgan+Chase+Stock+%28JPM%29+Opinions+on+Market+Outlook+Shift)  
  <sub>Quiver Quantitative, 5 hours ago</sub>  
  Q3 Revenue Outlook: Social media chatter highlights JPMorgan Chase's Co-President noting that third-
- [Eligible Chase cardholders can turn points into investment cash](https://www.stocktitan.net/news/JPM/chase-expands-ultimate-rewards-with-new-invest-your-points-ui4pzb9z87y7.html)  
  <sub>Stock Titan, 5 hours ago</sub>  
  Points can be redeemed through the Chase Mobile app, Chase.com or a J.P. Morgan advisor; new customers may earn up to $1000 with qualifying new money.
- [JPMorgan Chase (JPM) Stock Looks Undervalued Following Its 161% 5 Year Run](https://simplywall.st/stocks/us/banks/nyse-jpm/jpmorgan-chase/news/jpmorgan-chase-jpm-stock-looks-undervalued-following-its-161)  
  <sub>Simply Wall Street, 10 hours ago</sub>  
  JPMorgan Chase has delivered strong long term share price gains, and the current level now raises a clear question for investors about whether those gains...
- [5 Buy-and-Hold Stocks Built to Weather a Volatile Market](https://www.marketbeat.com/articles/5-buy-and-hold-stocks-built-to-weather-a-volatile-market/)  
  <sub>MarketBeat, 2 hours ago</sub>  
  Ahead of Q4 2026, analysts favor Western Digital, NVIDIA, Vertiv, Eli Lilly, and JPMorgan Chase as steady, best-in-class stocks offering growth with less...
- [JPMorgan vs. Wells Fargo: Which Bank Stock Has More Upside Potential?](https://www.theglobeandmail.com/investing/markets/stocks/JPM/pressreleases/4638893/jpmorgan-vs-wells-fargo-which-bank-stock-has-more-upside-potential/)  
  <sub>The Globe and Mail, 2 hours ago</sub>  
  Detailed price information for JP Morgan Chase & Company (JPM-N) from The Globe and Mail including charting and trades.
- [Credit card delinquencies, charge-offs tick up: August Credit Pulse (AXP:NYSE)](https://seekingalpha.com/news/4643387-credit-card-delinquencies-charge-offs-tick-up-august-credit-pulse)  
  <sub>Seeking Alpha, 3 hours ago</sub>  
  Credit card delinquencies and charge-offs ticked up in August compared to the prior month, according to Seeking Alpha's latest edition of Credit Pulse.
- [JPMorganChase Declares Common Stock Dividend](https://www.businesswire.com/news/home/20260915522805/en/JPMorganChase-Declares-Common-Stock-Dividend)  
  <sub>Business Wire, 22 hours ago</sub>  
  JPMorgan Chase & Co. (NYSE: JPM) (“JPMorganChase” or the “Firm”) declared a quarterly dividend on the outstanding shares of the common stock of...
- [JPMorgan Chase stock rises after upbeat revenue outlook](https://www.investing.com/news/stock-market-news/jpmorgan-chase-stock-rises-after-upbeat-revenue-outlook-4902445)  
  <sub>Investing.com, 23 hours ago</sub>  
  Investing.com -- JPMorgan Chase (NYSE:JPM) shares rose 1% on Tuesday after the bank provided an upbeat revenue outlook at a Barclays conference,...
- [JPM Looks 11.1% Overvalued on GF Value™ as Dividend Sustainabili](https://www.gurufocus.com/news/9084076/jpm-looks-111-overvalued-on-gf-value-as-dividend-sustainability-remains-key)  
  <sub>GuruFocus, 5 hours ago</sub>  
  On September 16, 2026, JPMorgan Chase & Co (NYSE: JPM) announced an enhancement to its Ultimate Rewards program, launching the "Invest Your Points" feature.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.10</summary>

_Not available today._

</details>

<details><summary><b>Price and chart</b> — score -0.25</summary>

```text
Last close 349.59 (bar of 2026-09-16), from 502 daily bars
Trend: vs 20d SMA 355.00 (-1.5%), 50d 352.55 (-0.8%), 200d 320.15 (+9.2%); 50d above 200d
Momentum: RSI(14) 44.0 | MACD -0.257 vs signal 0.934 (histogram -1.191)
Returns: 1d -0.8% | 5d -1.4% | 1m -3.1% | 3m +5.6%
52-week range: 282.84 - 365.18 (now 81.1% of the way up)
Volatility: ATR(14) 6.54 (1.9% of price) | annualised 20d 15.7%
Volume: 0.64x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.40</summary>

```text
Sector: Financial Services / Banks - Diversified | market cap 929.28B
Valuation: trailing P/E 14.98 | forward P/E 13.99 | P/B 2.63 | PEG 1.64
Profitability: profit margin 34.9% | operating margin 50.4% | ROE 17.8%
Growth (YoY): revenue +30.4% | earnings +46.9%
Balance sheet: debt/equity n/a | free cash flow n/a
Risk: beta 0.97 | short interest 1.0% of float
Next earnings: 2026-10-13
```

</details>

<details><summary><b>What this fund holds</b> — score +0.40</summary>

_Not available today._

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

<details><summary><b>What analysts and big funds say</b> — score +0.20</summary>

```text
Consensus: buy (mean 2.12 on a 1=strong buy to 5=strong sell scale, 21 analysts)
Ratings: 4 strong buy, 9 buy, 10 hold, 0 sell, 1 strong sell
Price target: mean 376.14 (+7.6% vs last close), range 305.00 - 452.00
Recent rating changes:
  - 2026-08-14 Wells Fargo: main, Overweight -> Overweight
  - 2026-08-03 UBS: main, Buy -> Buy
  - 2026-07-20 Citigroup: main, Neutral -> Neutral
  - 2026-07-17 Evercore ISI Group: main, Outperform -> Outperform
  - 2026-07-16 B of A Securities: main, Buy -> Buy
  - 2026-07-15 Baird: main, Neutral -> Neutral
Institutional ownership: 75.7%
Largest holders: Blackrock Inc. (7.8%), Vanguard Capital Management LLC (6.1%), State Street Corporation (4.7%), Bank of America Corporation (2.6%), Morgan Stanley (2.5%)
```

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score +0.20</summary>

_Not available today._

</details>

<details><summary><b>Buying and selling by company insiders</b> — score -0.05</summary>

```text
Last 180 days: bought 969,320 shares in 22 transaction(s) | sold 230,669 shares in 20
Net: +738,651 shares (+7.7% of insider holdings) | insiders hold 10,393,508 shares
Distinct insiders: 0 buying, 10 selling
Sales — weak evidence on their own; often scheduled 10b5-1 plans, tax on vesting, or diversification:
  - 2026-09-10 LEOPOLD ROBIN (Officer): 2,500 shares, 882.03K
  - 2026-08-11 LEOPOLD ROBIN (Officer): 2,500 shares, 903.52K
  - 2026-06-22 FRIEDMAN STACEY R. (General Counsel): 5,467 shares, 1.81M
  - 2026-05-20 FRIEDMAN STACEY R. (General Counsel): 5,468 shares, 1.64M
(22 grant/option/gift transaction(s) excluded — compensation, not a view on the price)
```

</details>

<details><summary><b>Who is positioned how</b> — score -0.05</summary>

_Not available today._

</details>

<details><summary><b>Money going into and out of this fund</b> — score -0.05</summary>

_Not available today._

</details>

### Novo Nordisk (NVO) · Company — NEUTRAL, confidence 0.40

**In the model's own words:**

> NVO faces conflicting signals across dimensions. News is positive on two fronts: the Anthropic AI partnership for drug discovery and upcoming Wegovy pill data at EASD, both substantive catalysts for a company competing in the increasingly crowded GLP-1 obesity market. However, technicals paint a deteriorating picture—the stock is down 6.2% over five days and 11.4% below its 50-day moving average, with RSI at 33 suggesting oversold conditions but momentum (MACD histogram negative) confirming weakness. Volume is 24% below average, indicating weak conviction behind any move. Fundamentals are mixed: trailing P/E of 10.26 is attractive and free cash flow is strong at $37.67B, but earnings fell 20.6% YoY and forward growth appears muted. The analyst consensus is "hold" with a mean target 11.8% above the current price, but recent downgrades from major firms (Morgan Stanley to Underweight, Goldman and JP Morgan to Neutral) suggest momentum in analyst sentiment is negative. No insider buying or selling in the past 180 days provides no signal either way. The Anthropic partnership and EASD data presentation are real developments, but they arrive into a stock that has been hammered and may already price in some recovery. The absence of insider conviction and the recent analyst downgrades offset the news catalysts. This is a stock with upcoming newsflow but deteriorating technicals and analyst sentiment, warranting a hold view with modest conviction until clearer directional signals emerge.

**Main reasons it gave:**
- Anthropic partnership to accelerate drug discovery using Claude models
- Wegovy pill data presentation at EASD conference later this month
- Stock down 11.4% vs 50-day MA with RSI 33, momentum waning
- Recent analyst downgrades from Morgan Stanley and Goldman Sachs
- Earnings declined 20.6% YoY despite attractive trailing valuation

<details><summary><b>News</b> — score +0.55</summary>

- [Novo will test AI on drug research problems](https://www.stocktitan.net/news/NVO/novo-and-anthropic-will-collaborate-to-advance-drug-discovery-with-m5lydsg3kvyz.html)  
  <sub>Stock Titan, 7 hours ago</sub>  
  Novo Nordisk (NVO) and Anthropic announced a collaboration to apply Anthropic's Claude models, including Claude Science, to Novo's R&D and software...
- [Novo teams up with Anthropic for R&D (NVO:NYSE)](https://seekingalpha.com/news/4643348-novo-collaborate-with-anthropic-rd)  
  <sub>Seeking Alpha, 6 hours ago</sub>  
  Novo Nordisk (NVO) partners with Anthropic (ANTHRO) to speed drug discovery and advance AI-driven software development. Read more here..
- [NVO Looks 59.5% Undervalued on GF Value™ as Dividend Sustainabil](https://www.gurufocus.com/news/9084079/nvo-looks-595-undervalued-on-gf-value-as-dividend-sustainability-shines)  
  <sub>GuruFocus, 5 hours ago</sub>  
  On September 16, 2026, Novo Nordisk (NVO) announced a strategic collaboration with Anthropic to enhance its drug discovery and AI capabilities,...
- [NVO To Present Fresh Data From Blockbuster Wegovy Pill At European Conference As Rival Eli Lilly Readies Its Own Obesity Updates](https://finance.yahoo.com/healthcare/articles/nvo-present-fresh-data-blockbuster-104404960.html)  
  <sub>Yahoo Finance, 8 hours ago</sub>  
  Novo said it will present 44 abstracts at the European Association for the Study of Diabetes symposium later this month.
- [Novo Nordisk Taps Anthropic’s Claude Science To Speed Up Drug Discovery — Here’s Everything Investors Need To Know](https://stocktwits.com/news-articles/markets/equity/novo-nordisk-taps-anthropic-s-claude-science-to-speed-up-drug-discovery-here-s-everything-investors-need-to-know/cZtY1NqRB2z)  
  <sub>Stocktwits, 6 hours ago</sub>  
  Novo will use Anthropic's Claude Science in R&D to tackle scientific and drug discovery challenges, aiming to develop new medicines faster.
- [Where Will Novo Nordisk Be in 5 Years as the GLP-1 Market Gets More Crowded?](https://www.theglobeandmail.com/investing/markets/stocks/NVO/pressreleases/4638991/where-will-novo-nordisk-be-in-5-years-as-the-glp-1-market-gets-more-crowded/)  
  <sub>The Globe and Mail, 2 hours ago</sub>  
  Detailed price information for Novo Nordisk A/S ADR (NVO-N) from The Globe and Mail including charting and trades.
- [Novo Nordisk Turns to Anthropic's Claude to Accelerate Drug Discovery](https://finance.biggo.com/news/6de6b53b-d8ec-4fab-bb21-bdf234d4aa24)  
  <sub>BigGo Finance, 5 hours ago</sub>  
  Novo Nordisk announced a partnership with AI company Anthropic to accelerate drug discovery and development using the Claude model family and the new…
- [Data on a Wegovy pill is among 44 research presentations Novo Nordisk will make](https://www.stocktitan.net/news/NVO/novo-to-share-real-world-and-clinical-data-including-wegovy-pill-and-wywwg1o5wek2.html)  
  <sub>Stock Titan, 12 hours ago</sub>  
  Novo Nordisk (NVO) will present new real-world and clinical data from its cardiometabolic portfolio and pipeline at the 62nd EASD Annual Meeting in Milan,...
- [NVO Looks 59.5% Undervalued on GF Value™ with Strong Dividend Ap](https://www.gurufocus.com/news/9083892/nvo-looks-595-undervalued-on-gf-value-with-strong-dividend-appeal)  
  <sub>GuruFocus, 6 hours ago</sub>  
  On September 16, 2026, Novo Nordisk (NVO) announced a strategic partnership with Anthropic to accelerate innovative medicine development and advance AI...
- [LLY|Eli Lilly and Co|Price:1139.280|Chg%:+3.170](https://www.tradingkey.com/markets/stocks/lly)  
  <sub>TradingKey, 7 hours ago</sub>  
  Track the Eli Lilly and Co stock with the latest LLY price, chart, market news, key financials, analyst forecasts, and company overview on TradingKey.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.55</summary>

_Not available today._

</details>

<details><summary><b>Price and chart</b> — score -0.45</summary>

```text
Last close 41.78 (bar of 2026-09-16), from 502 daily bars
Trend: vs 20d SMA 45.49 (-8.2%), 50d 47.13 (-11.4%), 200d 46.21 (-9.6%); 50d above 200d
Momentum: RSI(14) 33.1 | MACD -1.142 vs signal -0.742 (histogram -0.400)
Returns: 1d -1.8% | 5d -6.2% | 1m -6.9% | 3m -4.1%
52-week range: 35.29 - 63.98 (now 22.6% of the way up)
Volatility: ATR(14) 1.22 (2.9% of price) | annualised 20d 31.8%
Volume: 0.76x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.10</summary>

```text
Sector: Healthcare / Drug Manufacturers - General | market cap 184.57B
Valuation: trailing P/E 10.26 | forward P/E 12.34 | P/B 5.41 | PEG 3.01
Profitability: profit margin 35.3% | operating margin 42.5% | ROE 59.8%
Growth (YoY): revenue +2.1% | earnings -20.6%
Balance sheet: debt/equity 63.3% | free cash flow 37.67B
Risk: beta 0.34 | short interest 1.0% of float
Next earnings: 2026-11-04
```

</details>

<details><summary><b>What this fund holds</b> — score +0.10</summary>

_Not available today._

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

<details><summary><b>What analysts and big funds say</b> — score -0.25</summary>

```text
Consensus: hold (mean 2.71 on a 1=strong buy to 5=strong sell scale, 12 analysts)
Ratings: 0 strong buy, 3 buy, 10 hold, 1 sell, 0 strong sell
Price target: mean 46.72 (+11.8% vs last close), range 39.54 - 63.33
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

<details><summary><b>What analysts say about what this fund holds</b> — score -0.25</summary>

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

### Caterpillar (CAT) · Company — NEUTRAL, confidence 0.36

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> News flow is mostly noise — several items are about Red Cat (RCAT), not Caterpillar, plus a valuation listicle and an analyst-consensus rehash; the only CAT-specific item is a second-tier Freedom Broker upgrade to Buy with a $980 target, which is unlikely to move a $360B name. Technicals are in a corrective downtrend: price below 20d and 50d, -11% over a month, RSI 39.6, but sitting right on the 200d SMA with a flattening MACD histogram and very thin volume (0.49x), so a bounce is as plausible as continuation. Fundamentals show strong growth (+24% revenue, +68% earnings, 57% ROE) but rich multiples (P/B 18.6, trailing P/E 34) and high leverage. Consensus is buy with a 24% target gap, though rating changes are stale. Insiders net-bought in share count but that is driven by option-related flow; the only genuine open-market buy was a token 250 shares while the CEO sold $26M. No corroborated catalyst, so no directional edge.

**Main reasons it gave:**
- Most headlines refer to Red Cat (RCAT), not Caterpillar — irrelevant to CAT
- Only CAT-specific news is a Freedom Broker upgrade to Buy, $980 target (second-tier, low impact)
- Price 7.3% below 50d SMA, -11.1% 1m, RSI 39.6, but holding 200d SMA at 781.80
- Volume 0.49x 20-day average — no conviction behind the move
- Revenue +24% / earnings +68% YoY against trailing P/E 33.8 and D/E 233%
- CEO sold $26M in Aug; sole open-market buy was a 250-share director purchase

<details><summary><b>News</b> — score +0.05</summary>

- [Is CAT Stock Safe At $780? Sizing Caterpillar’s Next Move](https://www.trefis.com/stock/cat/articles/615517/is-cat-stock-safe-at-780-sizing-caterpillars-next-move/2026-09-16)  
  <sub>Trefis, 2 hours ago</sub>  
  Caterpillar (CAT) trades around $780. The market puts roughly a two-in-three chance that the stock finishes somewhere between about $525 and about $1170 a...
- [Caterpillar Stock (CAT) Opinions on Analyst Upgrade to Buy](https://www.quiverquant.com/news/Caterpillar+Stock+%28CAT%29+Opinions+on+Analyst+Upgrade+to+Buy)  
  <sub>Quiver Quantitative, 1 hour ago</sub>  
  Analyst Upgrade Sparks Interest: Recent social media chatter highlights an upgrade from Freedom Broker, shifting Caterpillar to a Buy rating with a $980...
- [Red Cat Sinks 6% as Speculative Drone Names Extend Month-Long Slide; Unusual Machines Drops 4%, AeroVironment Barely Budges](https://247wallst.com/investing/2026/09/16/red-cat-sinks-6-as-speculative-drone-names-extend-month-long-slide-unusual-machines-drops-4-aerovironment-barely-budges/)  
  <sub>24/7 Wall St., 3 hours ago</sub>  
  Something is breaking down inside the drone trade, and it is not hitting every name the same way. The split forming across the group this session points to...
- [Is It Worth Investing in Caterpillar (CAT) Based on Wall Street's Bullish Views?](https://finance.yahoo.com/markets/stocks/articles/worth-investing-caterpillar-cat-based-133002153.html)  
  <sub>Yahoo Finance, 5 hours ago</sub>  
  The recommendations of Wall Street analysts are often relied on by investors when deciding whether to buy, sell, or hold a stock. Media reports about these...
- [Red Cat Holdings: Defense Tailwinds Offset By Execution Risk (NASDAQ:RCAT)](https://seekingalpha.com/article/4947129-red-cat-holdings-defense-tailwinds-offset-by-execution-risk)  
  <sub>Seeking Alpha, 55 minutes ago</sub>  
  Red Cat scales domestic UAV/USV production for defense demand—yet competition, capacity gaps, and valuation risks loom. Click for more on RCAT stock.
- [RCAT Stock Slips As CEO Jeffrey Thompson Unloads Shares](https://stockstotrade.com/news/red-cat-holdings-inc-rcat-news-2026_09_16/)  
  <sub>StocksToTrade, 2 hours ago</sub>  
  Red Cat Holdings Inc. stocks have been trading down by -7.78 percent after bearish sentiment from recent drone-sector news. Key Takeaways Red Cat Holdings'...
- [RCAT Stock Under Pressure After CEO Insider Sale](https://www.timothysykes.com/news/red-cat-holdings-inc-rcat-news-2026_09_16/)  
  <sub>Timothy Sykes, 2 hours ago</sub>  
  Red Cat Holdings Inc. stocks have been trading down by -7.78 percent amid bearish sentiment over its drone technology outlook. Key Takeaways RCAT is...
- [Can I get hantavirus from my pet? Here's what pet owners should know](https://abcnews.com/GMA/News/hantavirus-pet-pet-owners/story?id=132977531)  
  <sub>ABC News - Breaking News, Latest News and Videos, 12 hours ago</sub>  
  The recent headlines about illnesses and deaths tied to possible hantavirus exposure have left some pet owners wondering whether the virus can be spread...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.05</summary>

_Not available today._

</details>

<details><summary><b>Price and chart</b> — score -0.35</summary>

```text
Last close 784.14 (bar of 2026-09-16), from 502 daily bars
Trend: vs 20d SMA 805.86 (-2.7%), 50d 845.75 (-7.3%), 200d 781.80 (+0.3%); 50d above 200d
Momentum: RSI(14) 39.6 | MACD -15.622 vs signal -15.919 (histogram 0.298)
Returns: 1d +0.1% | 5d -3.9% | 1m -11.1% | 3m -17.1%
52-week range: 440.67 - 1,064.90 (now 55.0% of the way up)
Volatility: ATR(14) 25.03 (3.2% of price) | annualised 20d 27.1%
Volume: 0.49x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.20</summary>

```text
Sector: Industrials / Farm & Heavy Construction Machinery | market cap 360.45B
Valuation: trailing P/E 33.81 | forward P/E 24.22 | P/B 18.58 | PEG 1.37
Profitability: profit margin 14.5% | operating margin 22.2% | ROE 57.0%
Growth (YoY): revenue +24.0% | earnings +68.2%
Balance sheet: debt/equity 232.8% | free cash flow 5.05B
Risk: beta 1.59 | short interest 1.8% of float
Next earnings: 2026-10-29
```

</details>

<details><summary><b>What this fund holds</b> — score +0.20</summary>

_Not available today._

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

```text
Consensus: buy (mean 2.14 on a 1=strong buy to 5=strong sell scale, 26 analysts)
Ratings: 1 strong buy, 13 buy, 12 hold, 1 sell, 1 strong sell
Price target: mean 975.61 (+24.4% vs last close), range 575.00 - 1,225.00
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

<details><summary><b>What analysts say about what this fund holds</b> — score +0.30</summary>

_Not available today._

</details>

<details><summary><b>Buying and selling by company insiders</b> — score -0.10</summary>

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

<details><summary><b>Who is positioned how</b> — score -0.10</summary>

_Not available today._

</details>

<details><summary><b>Money going into and out of this fund</b> — score -0.10</summary>

_Not available today._

</details>

### ASML (ASML) · Company — NEUTRAL, confidence 0.35

**In the model's own words:**

> ASML faces cross-cutting signals that leave directionality unclear over the near term. On the positive side: analysts maintain strong consensus (mean 1.4 strong buy, 33 buy vs 1 sell; 16 analysts), the forward P/E of 26.69 is reasonable for a company growing earnings 28.5% YoY, TSMC/Samsung commitments for High NA EUV show concrete demand, and the 200-day trend remains positive (+6.4%). Cantor named it top semiconductor equipment pick. Fundamentals are robust—30% profit margin, 53.9% ROE, 8.4B free cash flow. Against this: the stock has fallen 17.4% in three months and 15% in one month; it trades 5.8% below its 20-day MA and 7.3% below its 50-day MA. RSI at 39.2 and MACD histogram deeply negative signal oversold conditions but also confirm momentum has broken. Most critically, the AI slowdown narrative—referenced in four separate headlines within hours—creates near-term headline risk even if it does not threaten the long-term secular story. Volume is 15% below average, suggesting weak conviction either direction. Insider activity is absent entirely (zero transactions in 180 days), providing no tiebreaker. The stock may be attractive to long-term buyers at current weakness, but the AI demand question and technical deterioration create too much near-term uncertainty to justify a bullish lean with confidence. Analysts' 33% upside target assumes the demand thesis holds; that thesis is now under public scrutiny.

**Main reasons it gave:**
- AI researcher calls for frontier model slowdown creating near-term headline risk despite long-term EUV monopoly
- Stock down 15% in one month and 5.8% below 20-day MA; RSI 39.2 and negative MACD confirm momentum break
- Forward P/E 26.69 and 28.5% earnings growth support analyst consensus, but valuation vulnerable if demand softens
- TSMC/Samsung High NA EUV commitments confirm near-term pipeline, but insufficient to overcome AI uncertainty in headlines
- Zero insider transactions in 180 days provide no conviction signal either direction

<details><summary><b>News</b> — score -0.25</summary>

- [ASML Holding (ASML) Faces Fresh Questions Over Future AI Demand](https://finance.yahoo.com/technology/ai/articles/asml-holding-asml-faces-fresh-151100256.html)  
  <sub>Yahoo Finance, 4 hours ago</sub>  
  ASML Holding (NasdaqGS:ASML) faces fresh scrutiny as leading AI researchers urge a slowdown in frontier model development in 2026. Several high profile AI...
- [Weakness Is an Opportunity for Long-Term ASML Stock Investors](https://www.barchart.com/story/news/4637629/weakness-is-an-opportunity-for-long-term-asml-stock-investors)  
  <sub>Barchart.com, 3 hours ago</sub>  
  ASML wins commitments from Samsung, TSMC for new chipmaking.
- [ASML vs. Taiwan Semiconductor Manufacturing: Which Tech Stock Is a Better Buy in 2026?](https://www.fool.com/coverage/better-buy/2026/09/16/asml-vs-taiwan-semiconductor-manufacturing-which-tech-stock-is-a-better-buy-in-2026/)  
  <sub>The Motley Fool, 6 hours ago</sub>  
  One builds the machines; the other builds the chips. Their vastly different margins and valuations reveal which supply-chain player offers better returns.
- [Can ASML's Tie-Up With TSM to Advance High NA EUV Drive Growth?](https://qz.com/can-asml-s-tie-up-with-tsm-to-advance-high-na-euv-drive-growth)  
  <sub>qz.com, 4 hours ago</sub>  
  ASML and TSM are collaborating on a 12-inch photomask pilot line to advance High NA EUV and boost semiconductor manufacturing efficiency.
- [ASML Holding (ENXTAM:ASML) Shares Fell On Calls To Slow AI Development](https://simplywall.st/stocks/nl/semiconductors/ams-asml/asml-holding-shares/news/asml-holding-enxtamasml-shares-fell-on-calls-to-slow-ai-deve)  
  <sub>Simply Wall Street, 10 hours ago</sub>  
  ASML Holding (ENXTAM:ASML) shares sold off after leading AI executives publicly urged a slowdown in advanced AI development.
- [There Is One Thing ASML's $400 Million Machine Still Cannot Do. AI Chips Keep Making It Worse.](https://247wallst.com/investing/2026/09/15/there-is-one-thing-asmls-400-million-machine-still-cannot-do-ai-chips-keep-making-it-worse/)  
  <sub>24/7 Wall St., 23 hours ago</sub>  
  ASML's $400 million lithography machine powers every cutting-edge AI chip on the planet, yet one stubborn physical constraint keeps chipmakers stitching...
- [Cantor Names Top Semiconductor Equipment Stock](https://www.investing.com/news/stock-market-news/cantor-names-top-semiconductor-equipment-stock-93CH-4902671)  
  <sub>Investing.com, 21 hours ago</sub>  
  Investing.com -- Cantor has identified its top pick in the semiconductor equipment sector, highlighting ASML Holding NV as a standout opportunity amid what...
- [ASML Holding stock steadies after sharp pullback as Q2 2026 guidance raises the stakes](https://www.ad-hoc-news.de/boerse/news/corporate-news/asml-holding-stock-steadies-after-sharp-pullback-as-q2-2026-guidance/70111109)  
  <sub>ad-hoc-news.de, 6 hours ago</sub>  
  ASML Holding stock is trading around USD 1591.48 as of September 16, 2026, after a recent pullback of about 17.4 percent over three months.
- [Taiwan Semiconductor Vs. ASML: There’s Actually One True Dominant Picks-and-Shovels Play](https://finance.yahoo.com/technology/articles/taiwan-semiconductor-vs-asml-actually-110540607.html)  
  <sub>Yahoo Finance, 8 hours ago</sub>  
  TSMC (TSM) posted $40B in revenue up 36%, while ASML's EUV monopoly ensures every leading-edge chipmaker, including TSMC, Intel, and Samsung, must buy from...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score -0.25</summary>

_Not available today._

</details>

<details><summary><b>Price and chart</b> — score -0.45</summary>

```text
Last close 1,600.62 (bar of 2026-09-16), from 502 daily bars
Trend: vs 20d SMA 1,698.94 (-5.8%), 50d 1,727.38 (-7.3%), 200d 1,503.65 (+6.4%); 50d above 200d
Momentum: RSI(14) 39.2 | MACD -32.906 vs signal -19.474 (histogram -13.432)
Returns: 1d +0.6% | 5d -7.5% | 1m -15.0% | 3m -11.3%
52-week range: 872.27 - 1,989.44 (now 65.2% of the way up)
Volatility: ATR(14) 56.77 (3.5% of price) | annualised 20d 38.0%
Volume: 0.85x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.60</summary>

```text
Sector: Technology / Semiconductor Equipment & Materials | market cap 614.80B
Valuation: trailing P/E 54.37 | forward P/E 26.69 | P/B 1,349.86 | PEG 1.42
Profitability: profit margin 30.1% | operating margin 37.1% | ROE 53.9%
Growth (YoY): revenue +21.3% | earnings +28.5%
Balance sheet: debt/equity 9.1% | free cash flow 8.44B
Risk: beta 1.36 | short interest 0.4% of float
Next earnings: 2026-10-14
```

</details>

<details><summary><b>What this fund holds</b> — score +0.60</summary>

_Not available today._

</details>

<details><summary><b>Does this company beat its own forecasts</b> — score +0.60</summary>

_Not available today._

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

<details><summary><b>What analysts and big funds say</b> — score +0.75</summary>

```text
Consensus: strong_buy (mean 1.40 on a 1=strong buy to 5=strong sell scale, 16 analysts)
Ratings: 7 strong buy, 32 buy, 3 hold, 1 sell, 0 strong sell
Price target: mean 2,137.39 (+33.5% vs last close), range 888.83 - 2,846.19
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

<details><summary><b>What analysts say about what this fund holds</b> — score +0.75</summary>

_Not available today._

</details>

<details><summary><b>Buying and selling by company insiders</b> — score +0.00</summary>

```text
Last 180 days: bought 0 shares in 0 transaction(s) | sold n/a shares in 0
Net: +0 shares | insiders hold 3,414,222 shares
Distinct insiders: 0 buying, 0 selling
```

</details>

<details><summary><b>Who is positioned how</b> — score +0.00</summary>

_Not available today._

</details>

<details><summary><b>Money going into and out of this fund</b> — score +0.00</summary>

_Not available today._

</details>

### Elbit Systems (ESLT) · Company — NEUTRAL, confidence 0.35

**In the model's own words:**

> Elbit Systems presents a mixed picture across dimensions. The company shows solid fundamental growth (+15.9% revenue, +34.2% earnings YoY) and maintains reasonable profitability, but faces a stretched valuation at 55x trailing P/E and 40x forward P/E for a defense contractor. Technically, the stock is down 4% from its 50-day and 3.5% from its 200-day moving average after a recent 10.9% decline over 3 months; momentum is neutral (RSI 47.2, MACD slightly positive) and volume is thin at 0.45x average. Analyst consensus is a soft 'hold' with price targets implying 11.4% upside but wide dispersion (518-960), indicating low conviction. The recent insider activity shows balanced buying and selling with no clear directional signal—sales in April from the CEO and officers appear routine (clustered around compensation events), while recent institutional buying (Engineers Gate 542.8% increase) is notable but the underlying context is unclear and could reflect index or sector positioning rather than fundamental conviction. The near-term catalyst is earnings on 2026-11-24, over two months away. No material ticker-specific news catalyst in the past 24 hours. The stock sits 49.7% through its 52-week range with modest negative momentum, suggesting it is neither oversold nor particularly attractive at current levels.

**Main reasons it gave:**
- Valuation stretched at 55x trailing P/E despite revenue growth
- Consensus rating soft hold with wide analyst price target dispersion
- Stock down 4% from 50-day MA with thin volume
- Insider sales in April clustered around CEO and officers, consistent with compensation
- Earnings catalyst 69 days away

<details><summary><b>News</b> — score +0.00</summary>

- [Elbit Systems Ltd. $ESLT Shares Purchased by Engineers Gate Manager LP](https://www.marketbeat.com/instant-alerts/filing-elbit-systems-ltd-eslt-shares-purchased-by-engineers-gate-manager-lp-2026-09-16/)  
  <sub>MarketBeat, 11 hours ago</sub>  
  Engineers Gate Manager LP boosted its position in shares of Elbit Systems Ltd. (NASDAQ:ESLT - Free Report) by 542.8% during the second quarter, according to...
- [Wed: Tower leads TASE rebound](https://en.globes.co.il/en/article-wed-tower-leads-tase-rebound-1001556734)  
  <sub>Globes - Israel Business News, 2 hours ago</sub>  
  The Tel Aviv Stock Exchange rose today. The Tel Aviv 35 Index rose 1.32% to 4,246.84 points, the Tel Aviv 125 Index rose 1.04% to 4,125.35 points;...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

_Not available today._

</details>

<details><summary><b>Price and chart</b> — score -0.15</summary>

```text
Last close 732.72 (bar of 2026-09-16), from 502 daily bars
Trend: vs 20d SMA 721.35 (+1.6%), 50d 763.04 (-4.0%), 200d 759.58 (-3.5%); 50d above 200d
Momentum: RSI(14) 47.2 | MACD -12.871 vs signal -17.711 (histogram 4.840)
Returns: 1d +0.1% | 5d +2.6% | 1m -6.4% | 3m -10.9%
52-week range: 454.95 - 1,014.33 (now 49.7% of the way up)
Volatility: ATR(14) 17.06 (2.3% of price) | annualised 20d 23.6%
Volume: 0.45x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.35</summary>

```text
Sector: Industrials / Aerospace & Defense | market cap 34.34B
Valuation: trailing P/E 55.05 | forward P/E 39.90 | P/B 7.77 | PEG n/a
Profitability: profit margin 7.4% | operating margin 9.6% | ROE 15.2%
Growth (YoY): revenue +15.9% | earnings +34.2%
Balance sheet: debt/equity 19.3% | free cash flow -38.48M
Risk: beta -0.30 | short interest 0.8% of float
Next earnings: 2026-11-24
```

</details>

<details><summary><b>What this fund holds</b> — score +0.35</summary>

_Not available today._

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

<details><summary><b>What analysts and big funds say</b> — score +0.05</summary>

```text
Consensus: hold (mean 2.67 on a 1=strong buy to 5=strong sell scale, 6 analysts)
Ratings: 0 strong buy, 1 buy, 5 hold, 0 sell, 0 strong sell
Price target: mean 816.33 (+11.4% vs last close), range 518.00 - 960.00
Recent rating changes:
  - 2026-08-19 JP Morgan: main, Neutral -> Neutral
  - 2026-06-24 Jefferies: main, Hold -> Hold
  - 2026-05-27 JP Morgan: main, Neutral -> Neutral
  - 2026-04-13 JP Morgan: main, Neutral -> Neutral
  - 2025-12-19 JP Morgan: main, Neutral -> Neutral
  - 2025-12-11 Morgan Stanley: init, ? -> Equal-Weight
Institutional ownership: 23.0%
Largest holders: Clal Insurance Enterprises Holdings Ltd (3.5%), Vanguard Capital Management LLC (1.6%), Van Eck Associates Corporation (1.2%), Y.D. More Investments Ltd (1.0%), Altshuler Shaham Ltd (1.0%)
```

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score +0.05</summary>

_Not available today._

</details>

<details><summary><b>Buying and selling by company insiders</b> — score +0.00</summary>

```text
Last 180 days: bought 82,000 shares in 7 transaction(s) | sold 69,736 shares in 7
Net: +12,264 shares (+0.1% of insider holdings) | insiders hold 19,279,282 shares
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

### MercadoLibre (MELI) · Company — NEUTRAL, confidence 0.35

**In the model's own words:**

> MELI presents a conflicted picture with no clear catalyst emerging in the past 24 hours. News is generic sector commentary rather than company-specific catalysts (one headline conflates MELI with a roundup of digital trade platforms; another discusses Intel's foundry strategy, irrelevant to MELI). Technicals show concerning momentum divergence: RSI at 43.5 is cooling, MACD histogram deeply negative at -17.459, and the stock is now 4.5% below its 20-day SMA despite being only 0.7% below its 200-day, suggesting loss of upside momentum. A recent 3.8% drop and 1-month flat performance (3.1%) against a 10% 3-month gain indicate consolidation or mild weakness after a run. Fundamentals are mixed: strong 49.8% revenue growth and 27.5% ROE are offset by a 10.9% earnings decline YoY and an elevated trailing P/E of 50.1x, though forward P/E of 32.65 and PEG of 0.92 suggest reasonable growth pricing. Analyst consensus is solidly bullish with a 22.9% mean price target upside, but this is already well-known market consensus and offers limited edge; no fresh rating changes in the past month. Insider activity from June and May (two small open-market buys by officers totaling ~$1.2M) is positive in isolation but stale—no recent activity to confirm conviction. The stock sits at the lower end of its 52-week range (30.7% of the way up) and volume is only 1.23x average, suggesting neither strong accumulation nor distribution. The earnings date of Nov 4 is 6.5 weeks away, too far to dominate the next few trading days. With positive analyst consensus, reasonable growth metrics, and some prior insider support, but negative momentum, stale insider data, and no fresh tick-specific catalyst, the risk-reward is balanced without clear directional force.

**Main reasons it gave:**
- MACD histogram deeply negative at -17.459 with RSI cooling to 43.5
- Recent 3.8% drop and stock 4.5% below 20-day SMA suggests momentum loss
- Analyst consensus bullish but already priced in with no fresh rating changes in past month
- Revenue growth strong at 49.8% YoY but earnings declined 10.9% YoY
- No recent insider buying activity; prior two buys from June-May are stale

<details><summary><b>News</b> — score -0.10</summary>

- [MU: Micron Technology Inc Latest Stock Price, Analysis, News and Trading Ideas](https://stocktwits.com/symbol/MU)  
  <sub>Stocktwits, 4 hours ago</sub>  
  Get real-time Micron Technology Inc (MU) stock price, news, financials, community insights, and trading ideas. Join 10 million+ investors and traders...
- [MercadoLibre Stock And 2 Digital Trade Platforms Worth Watching](https://simplywall.st/stocks/us/diversified-financials/nyse-psfe/paysafe/news/mercadolibre-stock-and-2-digital-trade-platforms-worth-watch)  
  <sub>Simply Wall Street, 2 hours ago</sub>  
  Global trade is being quietly rewired as policymakers debate whether to strengthen or fragment the system, and that tug of war matters for every investor...
- [Is MercadoLibre Inc (MELI) a Bargain After 3.8% Drop? GF Value S](https://www.gurufocus.com/news/9082719/is-mercadolibre-inc-meli-a-bargain-after-38-drop-gf-value-says-undervalued)  
  <sub>GuruFocus, 21 hours ago</sub>  
  On September 15, 2026, MercadoLibre Inc (MELI) shares fell 3.8% to a current price of $1828.94. This decline is part of a broader trend, with the stock...
- [MercadoLibre (NASDAQ:MELI) Draws A Closer Look As Themes Reshuffle](https://kalkinemedia.com/us/stocks/growth/mercadolibre-nasdaqmeli-draws-a-closer-look-as-themes-reshuffle)  
  <sub>Kalkine Media, 20 hours ago</sub>  
  MercadoLibre is being tracked as a widening split between software demand and semiconductor sentiment changes the tone across the broader market.
- [Intel CEO Lip-Bu Tan Reportedly Says ‘Multiple Customers’ Eyeing Foundry Tie-Up](https://stocktwits.com/news-articles/markets/equity/intel-ceo-lip-bu-tan-reportedly-says-multiple-customers-eyeing-foundry-tie-up/cZXuiDuReZa)  
  <sub>Stocktwits, 21 hours ago</sub>  
  Tan said improvement in Intel's 18A and 14A chip processes has drawn interest from potential customers.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score -0.10</summary>

_Not available today._

</details>

<details><summary><b>Price and chart</b> — score -0.35</summary>

```text
Last close 1,843.00 (bar of 2026-09-16), from 502 daily bars
Trend: vs 20d SMA 1,929.99 (-4.5%), 50d 1,877.63 (-1.8%), 200d 1,855.64 (-0.7%); 50d above 200d
Momentum: RSI(14) 43.5 | MACD 0.466 vs signal 17.925 (histogram -17.459)
Returns: 1d +0.8% | 5d -1.8% | 1m +3.1% | 3m +10.1%
52-week range: 1,546.81 - 2,510.97 (now 30.7% of the way up)
Volatility: ATR(14) 63.66 (3.5% of price) | annualised 20d 38.5%
Volume: 1.23x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.25</summary>

```text
Sector: Consumer Cyclical / Internet Retail | market cap 93.43B
Valuation: trailing P/E 50.14 | forward P/E 32.65 | P/B 11.93 | PEG 0.92
Profitability: profit margin 5.3% | operating margin 6.7% | ROE 27.5%
Growth (YoY): revenue +49.8% | earnings -10.9%
Balance sheet: debt/equity 168.6% | free cash flow 353.38M
Risk: beta 1.31 | short interest 1.6% of float
Next earnings: 2026-11-04
```

</details>

<details><summary><b>What this fund holds</b> — score +0.25</summary>

_Not available today._

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

<details><summary><b>What analysts and big funds say</b> — score +0.50</summary>

```text
Consensus: buy (mean 1.54 on a 1=strong buy to 5=strong sell scale, 24 analysts)
Ratings: 5 strong buy, 15 buy, 4 hold, 0 sell, 0 strong sell
Price target: mean 2,264.88 (+22.9% vs last close), range 1,750.00 - 2,800.00
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

<details><summary><b>What analysts say about what this fund holds</b> — score +0.50</summary>

_Not available today._

</details>

<details><summary><b>Buying and selling by company insiders</b> — score +0.20</summary>

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

<details><summary><b>Who is positioned how</b> — score +0.20</summary>

_Not available today._

</details>

<details><summary><b>Money going into and out of this fund</b> — score +0.20</summary>

_Not available today._

</details>

### Royal Bank of Canada (RY) · Company — NEUTRAL, confidence 0.35

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> News flow is mostly valuation opinion pieces, a covered bond listing (routine funding), and a conference reiteration of strategy — no material ticker-specific catalyst. Technicals are soft: price below 20d and 50d, RSI ~40, MACD negative, -6% over a month, though still well above the 200d. Fundamentals are solid (ROE 16%, +9% revenue, +13% earnings, forward P/E 15.8) but earnings are not until December. Analyst consensus is a stale buy with only +3.4% to target. The 'insider' buys are issuer buyback activity, not individual insiders spending their own money, so they carry little informational weight. Mixed inputs argue for no directional view.

**Main reasons it gave:**
- Price below 20d (-1.5%) and 50d (-3.0%) SMAs, MACD histogram -0.383, RSI 39.9
- -6.1% over past month on 0.32x average volume
- News is valuation commentary plus routine €3bn covered bond LSE listing, no hard catalyst
- Forward P/E 15.79 with ROE 16.2%, revenue +8.9%, earnings +12.8%
- Analyst mean target 210.02, only +3.4% upside; no rating changes since Aug 2025
- Reported 'insider' purchases are issuer buyback blocks, not individual executives

<details><summary><b>News</b> — score +0.10</summary>

- [Royal Bank Of Canada (TSX:RY) Stock Looks 22% Undervalued On Equity Returns](https://simplywall.st/stocks/ca/banks/tsx-ry/royal-bank-of-canada-shares/news/royal-bank-of-canada-tsxry-stock-looks-22-undervalued-on-equ)  
  <sub>Simply Wall Street, 15 hours ago</sub>  
  Royal Bank of Canada has delivered strong share-price gains over the past few years, and that kind of run naturally raises a question for anyone looking at...
- [RY: Strong growth, efficiency gains, and strategic initiatives drive robust performance and outlook](https://www.tradingview.com/news/urn:summary_document_transcript:quartr.com:4176242:0-ry-strong-growth-efficiency-gains-and-strategic-initiatives-drive-robust-performance-and-outlook/)  
  <sub>TradingView, 2 hours ago</sub>  
  Progress on strategic goals includes strong Canadian and global business growth, improved ROE, and efficiency gains. Capital priorities remain focused on...
- [Royal Bank Of Canada (TSX:RY): Is The Stock Still Undervalued Today?](https://kalkinemedia.com/ca/stocks/financial/royal-bank-of-canada-tsxry-is-the-stock-still-undervalued-today)  
  <sub>Kalkine Media, 4 hours ago</sub>  
  Royal Bank of Canada has delivered a strong long term run. Explore whether its equity returns and intrinsic value still justify todays share price.
- [Royal Bank of Canada at Barclays conference: growth, costs and capital](https://ca.investing.com/news/stock-market-news/royal-bank-of-canada-at-barclays-conference-growth-costs-and-capital-93CH-4842143)  
  <sub>Investing.com Canada, 2 hours ago</sub>  
  On Wednesday, 16 September 2026, Royal Bank of Canada (RY) used the Barclays 24th Annual Global Financial Services Conference to show that its strategy is...
- [Here’s How Much You Would Have Made Owning Royal Bank of Canada Stock In The Last 5 Years](https://www.benzinga.com/news/26/09/61806602/here-s-how-much-you-would-have-made-owning-royal-bank-canada-stock-last-5-years)  
  <sub>Benzinga, 19 hours ago</sub>  
  Royal Bank of Canada (NYSE:RY) has outperformed the market over the past 5 years by 3.97% on an annualized basis producing an average annual return of...
- [Publication of Final Terms](https://www.marketscreener.com/news/publication-of-final-terms-ce785bd2de8af424)  
  <sub>www.marketscreener.com, 2 hours ago</sub>  
  Regulatory Announcement Royal Bank of Canada September 16, 2026 Publication of Final Terms Not for release, publication or distribution,...
- [Why Royal Bank of Canada (TSX:RY) Remains at the Centre of Canada's Banking Story](https://kalkine.ca/news/financial/why-royal-bank-of-canada-tsxry-remains-at-the-centre-of-canadas-banking-story)  
  <sub>kalkine.ca, 7 hours ago</sub>  
  You are reading a free article with opinions that may differ from the recommendation given by Kalkine in its paid research reports.
- [Royal Bank of Canada admits €3bn covered bonds to LSE](https://ca.investing.com/news/stock-market-news/royal-bank-of-canada-admits-3bn-covered-bonds-to-lse-93CH-4842116)  
  <sub>Investing.com Canada, 3 hours ago</sub>  
  LONDON - Royal Bank of Canada announced today the admission to trading of €3 billion in covered bonds on the London Stock Exchange's main market.
- [Royal Bank of Canada (TSX:RY) Faces a New Market Test](https://kalkinemedia.com/ca/stocks/financial/royal-bank-of-canada-tsxry-faces-a-new-market-test)  
  <sub>Kalkine Media, 11 hours ago</sub>  
  Royal Bank of Canada coverage examines the rates-heavy Canadian market backdrop ahead of the Federal Reserve decision, company operations, sector conditions...
- [Royal Bank of Canada admits €3bn covered bonds to LSE By Investing.com](https://uk.investing.com/news/stock-market-news/royal-bank-of-canada-admits-3bn-covered-bonds-to-lse-93CH-4871858)  
  <sub>Investing.com UK, 3 hours ago</sub>  
  LONDON - Royal Bank of Canada announced today the admission to trading of €3 billion in covered bonds on the London Stock Exchange's main market.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.10</summary>

_Not available today._

</details>

<details><summary><b>Price and chart</b> — score -0.35</summary>

```text
Last close 203.08 (bar of 2026-09-16), from 502 daily bars
Trend: vs 20d SMA 206.17 (-1.5%), 50d 209.39 (-3.0%), 200d 184.03 (+10.4%); 50d above 200d
Momentum: RSI(14) 39.9 | MACD -1.083 vs signal -0.700 (histogram -0.383)
Returns: 1d -0.6% | 5d -1.8% | 1m -6.1% | 3m +1.0%
52-week range: 143.64 - 217.87 (now 80.1% of the way up)
Volatility: ATR(14) 3.20 (1.6% of price) | annualised 20d 17.4%
Volume: 0.32x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.30</summary>

```text
Sector: Financial Services / Banks - Diversified | market cap 281.15B
Valuation: trailing P/E 17.75 | forward P/E 15.79 | P/B 2.91 | PEG 2.26
Profitability: profit margin 33.9% | operating margin 46.4% | ROE 16.2%
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

```text
Consensus: buy (mean 2.13 on a 1=strong buy to 5=strong sell scale, 3 analysts)
Ratings: 4 strong buy, 5 buy, 5 hold, 0 sell, 1 strong sell
Price target: mean 210.02 (+3.4% vs last close), range 182.28 - 229.04
Recent rating changes:
  - 2025-08-29 Argus Research: main, Buy -> Buy
  - 2024-12-05 BMO Capital: main, Outperform -> Outperform
  - 2024-08-29 BMO Capital: main, Outperform -> Outperform
  - 2024-06-06 Argus Research: main, Buy -> Buy
  - 2024-04-05 BMO Capital: up, Market Perform -> Outperform
  - 2023-12-18 B of A Securities: up, Neutral -> Buy
Institutional ownership: 49.6%
Largest holders: Royal Bank of Canada (5.1%), Bank of Montreal /CAN/ (4.4%), Vanguard Capital Management LLC (3.1%), FIL LTD (1.7%), TD Asset Management, Inc (1.7%)
```

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score +0.10</summary>

_Not available today._

</details>

<details><summary><b>Buying and selling by company insiders</b> — score +0.10</summary>

```text
Last 180 days: bought 0 shares in 0 transaction(s) | sold n/a shares in 0
Net: +0 shares | insiders hold 387,640 shares
Distinct insiders: 1 buying, 0 selling
Open-market purchases — insiders spending their own money:
  - 2026-08-31 Royal Bank of Canada (Issuer): 350,000 shares, 69.76M
  - 2026-08-28 Royal Bank of Canada (Issuer): 350,000 shares, 70.00M
  - 2026-07-31 Royal Bank of Canada (Issuer): 211 shares, 43.82K
  - 2026-07-31 Royal Bank of Canada (Issuer): 140 shares, 29.09K
(105 grant/option/gift transaction(s) excluded — compensation, not a view on the price)
```

</details>

<details><summary><b>Who is positioned how</b> — score +0.10</summary>

_Not available today._

</details>

<details><summary><b>Money going into and out of this fund</b> — score +0.10</summary>

_Not available today._

</details>

### Toyota (TM) · Company — NEUTRAL, confidence 0.35

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> News flow is almost entirely irrelevant noise (ETF tickers containing 'TM', grocery and mining items); the only relevant item is a generic hybrid-demand sector ETF piece, not a ticker-specific catalyst. Technicals are mixed: price sits below 20d and 200d SMAs with 50d under 200d and a negative MACD histogram, RSI neutral at 50.7, volume only half normal. Fundamentals are cheap (8.4x trailing) with strong reported growth but negative FCF and high leverage; earnings are far off (Nov 2026). Small analyst coverage is positive with ~20% upside but stale. No insider transactions. Nothing corroborated enough to take a side.

**Main reasons it gave:**
- News set dominated by unrelated items matching 'TM' string; no company-specific catalyst
- Price below 20d and 200d SMA, 50d under 200d, MACD histogram -0.53
- Trailing P/E 8.4 with revenue +10.4% and earnings +86.9% YoY
- Analyst mean target 231.58 (+19.9%) but only 4 analysts and stale changes
- Zero insider open-market transactions in 180 days

<details><summary><b>News</b> — score +0.05</summary>

- [Data center power use may nearly double by 2030. PRF Technologies is exploring how to manage it.](https://www.stocktitan.net/news/PRFX/prf-technologies-grid-feed-tm-to-explore-strategic-growth-ugtm7bimrmso.html)  
  <sub>Stock Titan, 6 hours ago</sub>  
  AI data center electricity use is expected to triple; global use is projected at 950 TWh in 2030. GridFeed could weigh workloads, batteries and grid...
- [Automotive ETFs in Spotlight as Hybrid Cars Take Center Stage](https://finance.yahoo.com/markets/stocks/articles/automotive-etfs-spotlight-hybrid-cars-161700235.html)  
  <sub>Yahoo Finance, 3 hours ago</sub>  
  Hybrid cars are gaining ground as EV challenges mount, putting Toyota, Honda and Hyundai in focus and boosting the outlook for auto ETFs.
- [Long Term Trading Analysis for (SWIN) (SWIN:CA)](https://news.stocktradersdaily.com/canada/long-term-trading-analysis-for-swin-_20260915_dff56f)  
  <sub>Stock Traders Daily, 17 hours ago</sub>  
  Trading Report for HAMILTON CHAMPIONS TM Enhanced U.S. Dividend ETF SWIN With Buy and Sell Signals.
- [Pumpkin turns up in coffee, popcorn and muffins at Kroger](https://www.stocktitan.net/news/KR/kroger-ushers-in-fall-with-new-limited-time-private-selection-tm-21h68xvun825.html)  
  <sub>Stock Titan, 6 hours ago</sub>  
  Coffee, popcorn, chai, muffins and cookies join Kroger's seasonal lineup. Kroger.com offers pickup or delivery in as little as 30 minutes.
- [When the Price of (SMVP) Talks, People Listen (SMVP:CA)](https://news.stocktradersdaily.com/canada/when-the-price-of-smvp-talks,-people-listen_20260915_0ef2e5)  
  <sub>Stock Traders Daily, 17 hours ago</sub>  
  When the Price of HAMILTON CHAMPIONS TM U.S. Dividend Index ETF SMVP Talks, People Listen.
- [Old El Paso™ is Bringing More Tex-Mex Flavor to the Soup Aisle with its First Broth Varieties and Two New Soups](https://www.stocktitan.net/news/GIS/old-el-paso-tm-is-bringing-more-tex-mex-flavor-to-the-soup-aisle-9xvrrw9abbqw.html)  
  <sub>Stock Titan, 6 hours ago</sub>  
  The 32-ounce broths work in ramen, pasta, sauces and stews, while the soups offer 12–16 grams of protein per can and are available nationwide.
- [Sensex Today Ends 333 Points Higher | Nifty Above 23,200 | Paytm Up 3%](https://www.equitymaster.com/indian-share-markets/09/16/2026/Sensex-Today-Ends-333-Points-Higher--Nifty-Above-23200--Paytm-Up-3?utm_source=todays-market-plug&utm_medium=website&utm_campaign=content&utm_content=TM)  
  <sub>Equitymaster, 8 hours ago</sub>  
  Although the benchmark indices opened higher, they traded positive throughout the session and ultimately closed green. Indian equity benchmarks indices,...
- [Morocco Strategic Minerals Reports New Gold Hits at Tamdghoust and Grants 4.92 Million Stock Options](https://kalkine.ca/news/announcements/morocco-strategic-minerals-reports-new-gold-hits-at-tamdghoust-and-grants-492-million-stock-options)  
  <sub>kalkine.ca, 23 hours ago</sub>  
  Morocco Strategic Minerals Corporation (TSXV: MCC) announced new surface sampling results from its Tamdghoust research permit in Morocco's western High...
- [A human gut model detected drug toxicity before cells were harmed](https://www.stocktitan.net/news/VIVS/vivo-sim-labs-unveils-new-na-mkind-tm-drug-toxicity-data-at-eurotox-exqphmy6jpnd.html)  
  <sub>Stock Titan, 7 hours ago</sub>  
  VivoSim's data ranked trastuzumab deruxtecan as significantly more hepatotoxic than trastuzumab emtansine; liver spheroids supported testing for up to 28...
- [Hero Motors IPO Opens Today | Rupee Sees Sharpest Single-Day Drop| Top Buzzing Stocks Today](https://www.equitymaster.com/tm/tm.asp?date=9/16/2026&title=Hero-Motors-IPO-Opens-Today--Rupee-Sees-Sharpest-Single-Day-Drop-Top-Buzzing-Stocks-Today)  
  <sub>Equitymaster, 18 hours ago</sub>  
  Top cues to track in today's stock market session.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.05</summary>

_Not available today._

</details>

<details><summary><b>Price and chart</b> — score -0.15</summary>

```text
Last close 193.17 (bar of 2026-09-16), from 502 daily bars
Trend: vs 20d SMA 194.63 (-0.8%), 50d 188.07 (+2.7%), 200d 202.13 (-4.4%); 50d below 200d
Momentum: RSI(14) 50.7 | MACD 1.870 vs signal 2.396 (histogram -0.526)
Returns: 1d -1.2% | 5d +1.2% | 1m +2.1% | 3m +8.4%
52-week range: 166.50 - 248.29 (now 32.6% of the way up)
Volatility: ATR(14) 3.34 (1.7% of price) | annualised 20d 23.1%
Volume: 0.52x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.25</summary>

```text
Sector: Consumer Cyclical / Auto Manufacturers | market cap 228.75B
Valuation: trailing P/E 8.43 | forward P/E 12.24 | P/B 15.32 | PEG n/a
Profitability: profit margin 8.6% | operating margin 7.9% | ROE 12.4%
Growth (YoY): revenue +10.4% | earnings +86.9%
Balance sheet: debt/equity 115.0% | free cash flow -3.60T
Risk: beta 0.34 | short interest 0.1% of float
Next earnings: 2026-11-05
```

</details>

<details><summary><b>What this fund holds</b> — score +0.25</summary>

_Not available today._

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

<details><summary><b>What analysts and big funds say</b> — score +0.20</summary>

```text
Consensus: none (mean n/a on a 1=strong buy to 5=strong sell scale, 4 analysts)
Ratings: 2 strong buy, 2 buy, 0 hold, 0 sell, 0 strong sell
Price target: mean 231.58 (+19.9% vs last close), range 220.00 - 239.31
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

<details><summary><b>What analysts say about what this fund holds</b> — score +0.20</summary>

_Not available today._

</details>

<details><summary><b>Buying and selling by company insiders</b> — score +0.00</summary>

```text
Last 180 days: bought 0 shares in 0 transaction(s) | sold n/a shares in 0
Net: +0 shares | insiders hold 757,877 shares
Distinct insiders: 0 buying, 0 selling
(1 grant/option/gift transaction(s) excluded — compensation, not a view on the price)
```

</details>

<details><summary><b>Who is positioned how</b> — score +0.00</summary>

_Not available today._

</details>

<details><summary><b>Money going into and out of this fund</b> — score +0.00</summary>

_Not available today._

</details>

### Exxon Mobil (XOM) · Company — NEUTRAL, confidence 0.35

**In the model's own words:**

> XOM trades near 52-week highs on strong fundamentals and an upbeat analyst consensus, but today's price action is decidedly negative (-3.4% on the day, -4.43% in one source) amid sector-wide energy weakness tied to crude oil pullbacks and Fed policy uncertainty. The recent news mix includes both positives (Guyana investment recovery, Rose carbon capture approval, higher LNG targets) and negatives (Guyana production concerns, general energy sector underperformance). Technicals show the stock is at the upper end of its range with moderating momentum (RSI 53.6, MACD barely positive) and below-average volume, suggesting weak conviction behind the current price level. The forward P/E of 15.15 is reasonable for an energy major with 112.8% YoY earnings growth and 9.1% profit margins, but the elevated 21.05 trailing P/E reflects recent outperformance already priced in. Analyst consensus is constructively bullish (mean 2.32, +4.5% upside to target), but this is not a fresh catalyst—recent rating changes show no upgrades and one downgrade (BofA). Insider activity is ambiguous: buying has outweighed selling on a net basis, but with zero distinct insiders buying or selling in recent activity (despite 251 transactions), the granularity of the signal is unclear and does not provide independent corroboration. The combination of negative momentum, sector headwinds, moderating volume, and lack of a single material fresh catalyst argues for a neutral bias pending clarity on Fed policy and crude direction.

**Main reasons it gave:**
- Stock down 3.4% on the day amid crude oil pullback and sector weakness
- RSI 53.6 with MACD near signal line, momentum moderating
- Below-average volume and price near 52-week highs limit upside conviction
- Analyst consensus bullish but no recent upgrades; +4.5% upside already reflected
- Forward P/E 15.15 and 112.8% YoY earnings growth support fundamentals despite recent outperformance

<details><summary><b>News</b> — score -0.15</summary>

- [ExxonMobil Holdings (XOM) Shares Moved, What Is Drawing Fresh Attention?](https://www.google.com/goto?url=CAESlQEB6zswFfKBKDfuIGdnF8Vm23I93HW2p331VA-mEGYKAlNWrrWMa_5YUrO-k1B-KJk7iDo3vOPQWrZx0qaFm1c1j3oil28OVW_EZBlt9b8GfsA4YFT16wbBUTocyH7LqI9wPYvCGj4bfjMlClT1kcAE3aoqLVFmHrPf0cVvfEzStE-NLz7Q0QZ9GoHsQs66xo7bxwxE2A)  
  <sub>Yahoo Finance, 9 hours ago</sub>  
  ExxonMobil Holdings (XOM) moved back into focus after management outlined higher long term LNG sales targets, while rising crude prices and upbeat earnings...
- [XOM|Exxon Mobil Corp|Price:164.890|Chg%:-4.430](https://www.tradingkey.com/markets/stocks/xom)  
  <sub>TradingKey, 2 hours ago</sub>  
  Exxon Mobil Corp News · EOG Resources Inc Stock (EOG) Moved Down by 5.13% on Sep 16: Drivers Behind the Movement · Diamondback Energy Inc Stock (FANG) Moved...
- [ExxonMobil: Lower Production From Guyana Looming? (NYSE:XOM)](https://seekingalpha.com/article/4947066-exxonmobil-lower-production-from-guyana-looming)  
  <sub>Seeking Alpha, 3 hours ago</sub>  
  ExxonMobil has recovered its investment in Guyana's Stabroek Block, accelerating the transition in its production-sharing agreement.
- [Chevron Doesn’t Need Oil to Hit New Highs. Here’s What Could Drive the Stock Instead](https://247wallst.com/investing/2026/09/16/chevron-doesnt-need-oil-to-hit-new-highs-heres-what-could-drive-the-stock-instead/)  
  <sub>24/7 Wall St., 1 hour ago</sub>
- [Exxon Looks to Ditch New Jersey Incorporation for Texas Homecoming](https://www.google.com/goto?url=CAESmQEB6zswFRyhu74gmmPRj3MiRBV_M0xaZQ1FJGJdqfU3njbCADRVOd_P7aHKTtj0TnG014GSeA8oQQ4buYdWH4sO0og4qGYR66_NJbEaKg4gjTfeS8YvETK8X5yZcjbpSaY6t8gRtogCr466hLIsi7xkQlXLFBh1_uhcC1PN33U9-u8z-P9r4929gvTT7rwPfhGExhTfcfQqvmo)  
  <sub>EnergyNow.com, 6 hours ago</sub>  
  Summary Exxon is latest high-profile company moving to Texas for business-friendly environment New Jersey sued…
- [ExxonMobil (XOM) Wins Approval For Rose Carbon Capture Project In Texas](https://www.google.com/goto?url=CAESvgEB6zswFfomqbUbxOuaIqXZWn6x4g0l2oJrrwXZCNm6zMH_rrzwmEY3MDKhitPoLQ0O8_sFocDECSjsxiYX3Y0PBzu-xDH8ant83kCJsa2QCLQNUX9tfAIqEucBNyVab_DEZ5mp3BmbX8cq8ZV18obS72cCGUMv0S8ukOpLKHHPJ-giIP7wDkDd8IQ6phhTCzwumT8eDkRjcQeMkYMsVV1JBJTTtvO2nFa9wqmmW0tG2FXW35bflJXdLKi-qqeD)  
  <sub>Simply Wall Street, 11 hours ago</sub>  
  ExxonMobil Holdings (NYSE:XOM) has received regulatory approval for its Rose carbon capture project in Texas. The Rose facility is designed to capture and...
- [Energy Stocks Sink as Oil Prices Edge Lower](https://www.google.com/goto?url=CAESmAEB6zswFb5Ynr4zwxA6uVVlokEupYJCSWrsaWb2oGEzkaMdpwWc7UL79pA6Vs_lpTZnFHMjOq9UEtI70mGEAr6o0BTb_Ih4nT6HR_P9kDz1kwaK25juvH-Wa8opsaKBDaRAzypDjG3n10a0IUbAj6u5D7-sQ77t3swwgAv6tnvjCT9Q9zz4R5qf4r66TSAXMcVbuGUj5P6R2w)  
  <sub>marketscreener.com, 3 hours ago</sub>  
  By Connor Hart Energy stocks were trading lower on Wednesday, as oil prices edged down ahead of the Federal Reserve's interest-rate decision and as...
- [AMD, SpaceX among market cap stock movers on Wednesday](https://www.google.com/goto?url=CAESqwEB6zswFeflkmZRKHcf2ROenpmeqXdkZ4EO9IXzO2dINWEdZf3Hx3KOlRmW2XD83UiUxxl2Wuuzmumc27q0skOt_K68yZvRdelOD28eNPXaJJbbA3yL-XwuMLTXoII8_-vNwASCgYB5Uu6iScSqQ-LvkAiFGKQ3YDXT_x7lVmgIU8Z__nYBHS1xUZQ6qVa7hyV_InO4VsWreIefImeIKgXlWpTHtQIQNSdMTTU)  
  <sub>Investing.com, 47 minutes ago</sub>  
  Wednesday's market has seen swings in various stocks based on news and other factors. Today, stocks like AMD and SpaceX are rallying, while stocks like...
- [Exxon Mobil Corp Stock (XOM) Moved Down by 3.30% on Sep 16: A Full Analysis](https://www.tradingkey.com/news/market-movers/262171226-market-movers-xom-20260916)  
  <sub>TradingKey, 4 hours ago</sub>  
  Crude oil price pullbacks and inventory builds created downward pressure on ExxonMobil.ExxonMobil maintains strong fundamentals, including record Permian...
- [16 S&P 500 Stocks Hit 52-Week Highs On Tuesday](https://www.trefis.com/stock/spy/articles/615495/16-sp-500-stocks-hit-52-week-highs-on-tuesday/2026-09-16)  
  <sub>Trefis, 9 hours ago</sub>  
  A list of stocks at yearly highs is dominated by one part of the market, raising questions about the quality of the run. The Oil & Gas Exploration...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score -0.15</summary>

_Not available today._

</details>

<details><summary><b>Price and chart</b> — score -0.20</summary>

```text
Last close 163.52 (bar of 2026-09-16), from 502 daily bars
Trend: vs 20d SMA 162.87 (+0.4%), 50d 156.82 (+4.3%), 200d 146.43 (+11.7%); 50d above 200d
Momentum: RSI(14) 53.6 | MACD 2.350 vs signal 2.313 (histogram 0.037)
Returns: 1d -3.4% | 5d -0.4% | 1m +1.3% | 3m +15.3%
52-week range: 110.64 - 171.47 (now 86.9% of the way up)
Volatility: ATR(14) 3.92 (2.4% of price) | annualised 20d 26.0%
Volume: 0.53x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.55</summary>

```text
Sector: Energy / Oil & Gas Integrated | market cap 672.38B
Valuation: trailing P/E 21.05 | forward P/E 15.15 | P/B 2.59 | PEG 1.45
Profitability: profit margin 9.1% | operating margin 15.9% | ROE 12.6%
Growth (YoY): revenue +44.1% | earnings +112.8%
Balance sheet: debt/equity 15.9% | free cash flow 20.67B
Risk: beta 0.17 | short interest 1.1% of float
Next earnings: 2026-10-30
```

</details>

<details><summary><b>What this fund holds</b> — score +0.55</summary>

_Not available today._

</details>

<details><summary><b>Does this company beat its own forecasts</b> — score +0.55</summary>

_Not available today._

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

<details><summary><b>What analysts and big funds say</b> — score +0.25</summary>

```text
Consensus: buy (mean 2.32 on a 1=strong buy to 5=strong sell scale, 22 analysts)
Ratings: 3 strong buy, 7 buy, 15 hold, 0 sell, 0 strong sell
Price target: mean 170.91 (+4.5% vs last close), range 142.00 - 200.00
Recent rating changes:
  - 2026-09-03 Piper Sandler: main, Neutral -> Neutral
  - 2026-08-19 Morgan Stanley: main, Overweight -> Overweight
  - 2026-08-17 Barclays: main, Overweight -> Overweight
  - 2026-08-07 TD Cowen: main, Buy -> Buy
  - 2026-08-04 Freedom Broker: up, Sell -> Hold
  - 2026-07-28 B of A Securities: down, Buy -> Neutral
Institutional ownership: 67.1%
Largest holders: Blackrock Inc. (8.1%), Vanguard Capital Management LLC (6.5%), State Street Corporation (5.0%), FMR, LLC (3.3%), Vanguard Portfolio Management LLC (2.8%)
```

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score +0.25</summary>

_Not available today._

</details>

<details><summary><b>Buying and selling by company insiders</b> — score +0.00</summary>

```text
Last 180 days: bought 10,818,651 shares in 251 transaction(s) | sold 3,904,152 shares in 49
Net: +6,914,499 shares (-194.8% of insider holdings) | insiders hold 3,371,767 shares
Distinct insiders: 0 buying, 0 selling
```

</details>

<details><summary><b>Who is positioned how</b> — score +0.00</summary>

_Not available today._

</details>

<details><summary><b>Money going into and out of this fund</b> — score +0.00</summary>

_Not available today._

</details>

## Whole-market funds

### Developing country bonds (EMB) · Index fund — BEARISH, confidence 0.35

**Result:** REJECTED · no room for broad fund EMB under its 12% cap or the 'Credit' group limit: equity 99950.70, price 93.14, existing exposure 11921.92, headroom 13065.75

**In the model's own words:**

> Rates are the whole story for EM hard-currency debt and the week's move is hostile: 5y +21bp, 10y +14bp, 3m +16bp, with the dollar index up 1.34 — a rising-rate, strong-dollar combination that pressures both the duration and spread legs of EMB. Technicals corroborate rather than contradict: price at 93.14 sits 4% off the 52-week low, below 20/50/200d SMAs with 50d under 200d, MACD negative and widening, RSI 31. Fund basics are unremarkable (5.1% yield, mostly BBB/BB, 0.39% fee) and offer a cushion but no offset to a further rate leg higher. The single news item is a TLT flow/listicle story referencing a Fed 'rate hike' with no verifiable detail — treated as low-reliability noise and not scored as a catalyst. No analyst roll-up or CFTC positioning for this instrument; share-count flows not provided, so insider_score is null. Conviction kept modest: this is a macro drift call, not a discrete surprise.

**Main reasons it gave:**
- 5-year yield +21bp and 10-year +14bp on the week
- Dollar index +1.34 to 100.11, a headwind for EM debt
- Price below 20/50/200d SMAs with 50d under 200d, RSI 31, MACD histogram -0.147
- Only 4% of the way up the 52-week range, near lows
- Sole news item is a low-quality TLT flow story, not EM-specific

<details><summary><b>News</b> — score -0.10</summary>

- ['Jackpot Mode': Bloomberg's Eric Balchunas Says Traders Are Betting $7 Billion on TLT In Hopes Of Rare Bond Market Move](https://247wallst.com/investing/etf/2026/09/16/jackpot-mode-bloombergs-eric-balchunas-says-traders-are-betting-7-billion-on-tlt-in-hopes-of-rare-bond-market-move/)  
  <sub>24/7 Wall St., 5 hours ago</sub>  
  On the morning of a Federal Reserve decision Wall Street has priced as a near-certain rate hike, $7 billion rushed into the iShares 20+ Year Treasury Bond...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score -0.10</summary>

```text
US Treasury yields: 3-month 3.96% (+0.16 on the week) | 5-year 4.83% (+0.21 on the week) | 10-year 4.97% (+0.14 on the week) | 30-year 5.32% (+0.03 on the week)
Yield curve, 10-year minus 3-month: +1.01 points -- upward sloping (normal)
US dollar index: 100.11 (+1.34 on the week)
Volatility (VIX): 16.79 (+0.3 on the week) -- elevated
```

</details>

<details><summary><b>Price and chart</b> — score -0.55</summary>

```text
Last close 93.14 (bar of 2026-09-16), from 502 daily bars
Trend: vs 20d SMA 94.33 (-1.3%), 50d 94.82 (-1.8%), 200d 95.71 (-2.7%); 50d below 200d
Momentum: RSI(14) 31.2 | MACD -0.493 vs signal -0.346 (histogram -0.147)
Returns: 1d +0.2% | 5d -1.1% | 1m -1.6% | 3m -3.7%
52-week range: 92.95 - 97.74 (now 4.0% of the way up)
Volatility: ATR(14) 0.39 (0.4% of price) | annualised 20d 5.4%
Volume: 0.78x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score -0.10</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score -0.10</summary>

```text
Fund type: Emerging Markets Bond
Yield: 5.1%
Credit quality: BBB 33.9%, BB 25.2%, B 19.3%, A 17.6% | US government debt 87.3%
Three-year record: +8.8% a year | beta to the market 1.08
Cost and size: expense ratio 0.39% | net assets 14.92B
What it is made of: Bonds 98.4%, Cash 1.6%
Largest holdings: BlackRock Cash Funds Treasury SL Agency 1.5%
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

<details><summary><b>Buying and selling by company insiders</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>Who is positioned how</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>Money going into and out of this fund</b> — score n/a</summary>

_Not available today._

</details>

### US company bonds, riskier (HYG) · Index fund — BEARISH, confidence 0.35

**Result:** ERROR · BrokerError: submit_order failed for HYG: {"code":42210000,"message":"asset \"HYG\" cannot be sold short"}

**In the model's own words:**

> Rates are the driver: yields rose across the curve this week (5y +21bp, 10y +14bp) with the dollar up 1.34, and HYG is sitting at the bottom of its 52-week range, below its 20/50/200d averages with 50d under 200d and MACD negative. Duration pressure plus a mild risk-off tone in a fund yielding only 5.9% with 40% of holdings at B or below justifies a modest bearish lean, tempered by RSI 27.6 (oversold, low ATR) which argues against pressing it. News items are generic HYG-vs-JNK fee comparisons and an income listicle -- no macro content, so news is scored near neutral. No analyst roll-up or CFTC positioning exists for this instrument, and no share-count flow data was given, so those scores are left null.

**Main reasons it gave:**
- 5-year yield +21bp and 10-year +14bp on the week, pressuring credit duration
- Close 78.44 at the very bottom of the 52-week range (78.38-81.32), 2% below 200d SMA
- 50d SMA below 200d, MACD -0.299 under signal -- established downtrend
- RSI(14) 27.6 oversold, arguing against high conviction on the short side
- Credit mix 40% B-or-below against only a 5.9% yield offers thin cushion if spreads widen

<details><summary><b>News</b> — score +0.00</summary>

- [HYG vs JNK: The Two Biggest Junk Bond ETFs Look Identical, but the Cheaper One Pays More](https://247wallst.com/investing/etf/2026/09/15/hyg-vs-jnk-the-two-biggest-junk-bond-etfs-look-identical-but-the-cheaper-one-pays-more/)  
  <sub>24/7 Wall St., 21 hours ago</sub>  
  HYG and JNK offer similar high-yield bond exposure, but differences in fees and distributions give the cheaper fund an income edge investors should...
- [JNK offers higher yield and lower fees than HYG in junk bond ETFs, ideal for income-focused investors.](https://pluang.com/en/news-feed/perbandingan-etf-hyg-vs-jnk-pilihan-terbaik-untuk-investor-pendapatan)  
  <sub>Pluang, 20 hours ago</sub>  
  The two largest junk bond ETFs, iShares HYG and SPDR JNK, hold similar bonds and pay monthly, but JNK offers a higher distribution yield and lower fees...
- [Bonds Offer Historically High Income - That Is Your Opportunity](https://seekingalpha.com/article/4946734-bonds-offer-historically-high-income-that-is-your-opportunity)  
  <sub>Seeking Alpha, 7 hours ago</sub>  
  Municipal bonds remain a core preference for tax savings and portfolio safety. Read why high yield corporates suit risk-seeking investors in lower tax...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 3.96% (+0.16 on the week) | 5-year 4.83% (+0.21 on the week) | 10-year 4.97% (+0.14 on the week) | 30-year 5.32% (+0.03 on the week)
Yield curve, 10-year minus 3-month: +1.01 points -- upward sloping (normal)
US dollar index: 100.11 (+1.34 on the week)
Volatility (VIX): 16.79 (+0.3 on the week) -- elevated
```

</details>

<details><summary><b>Price and chart</b> — score -0.45</summary>

```text
Last close 78.44 (bar of 2026-09-16), from 502 daily bars
Trend: vs 20d SMA 79.25 (-1.0%), 50d 79.43 (-1.2%), 200d 80.05 (-2.0%); 50d below 200d
Momentum: RSI(14) 27.6 | MACD -0.299 vs signal -0.189 (histogram -0.109)
Returns: 1d +0.1% | 5d -0.7% | 1m -1.5% | 3m -2.0%
52-week range: 78.38 - 81.32 (now 2.0% of the way up)
Volatility: ATR(14) 0.22 (0.3% of price) | annualised 20d 4.0%
Volume: 0.97x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score -0.15</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score -0.15</summary>

```text
Fund type: High Yield Bond
Yield: 5.9%
Credit quality: BB 57.9%, B 32.2%, Below B 8.3%, BBB 1.1%
Three-year record: +7.8% a year | beta to the market 0.67
Cost and size: expense ratio 0.49% | net assets 16.19B
What it is made of: Bonds 98.6%, Cash 1.2%, Preferred 0.2%
Largest holdings: BlackRock Cash Funds Treasury SL Agency 1.3%
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

_Not available today._

</details>

### US government bonds, 7-10 years (IEF) · Index fund — BEARISH, confidence 0.35

**Result:** REJECTED · duplicate order suppressed: IEF sell was already submitted this cycle (client_order_id IEF-sell-20712): {"code":40010001,"message":"client_order_id must be unique"}

**In the model's own words:**

> Yields are breaking to multi-decade highs with the 10-year above 5% intraday and +14bp on the week, 5-year +21bp, while the dollar is up 1.34 and a Fed decision priced as a hike sits in front of the market. IEF is at a fresh 52-week low, below all major moving averages with 50d under 200d, MACD negative and expanding, on 1.36x volume -- a decisive break rather than a stretched oversold bounce setup, though RSI 24.8 argues for modest conviction only. Short interest rotating specifically into the 7-10y belly corroborates the pressure point. No analyst roll-up or CFTC positioning for this instrument; flows data not provided, so insider_score is null. Headlines about TLT dip-buying are one-holding/roundup noise and were discounted.

**Main reasons it gave:**
- 10-year yield 4.97%, +14bp on week, breached 5% intraday
- 5-year +21bp on week -- belly of curve hit hardest, where IEF sits
- Fresh 52-week low at 90.80, below 20/50/200d SMAs with 50d<200d
- Short sellers rotating Treasury ETF shorts from TLT into IEF/IEI ahead of Fed
- Dollar index +1.34 on week, consistent with tighter policy expectations

<details><summary><b>News</b> — score -0.40</summary>

- ['Jackpot Mode': Bloomberg's Eric Balchunas Says Traders Are Betting $7 Billion on TLT In Hopes Of Rare Bond Market Move](https://247wallst.com/investing/etf/2026/09/16/jackpot-mode-bloombergs-eric-balchunas-says-traders-are-betting-7-billion-on-tlt-in-hopes-of-rare-bond-market-move/)  
  <sub>24/7 Wall St., 5 hours ago</sub>  
  On the morning of a Federal Reserve decision Wall Street has priced as a near-certain rate hike, $7 billion rushed into the iShares 20+ Year Treasury Bond...
- [Treasury ETF shorts shift toward belly ahead of Fed decision (TLT:NASDAQ)](https://seekingalpha.com/news/4643261-treasury-etf-shorts-shift-toward-belly-ahead-of-fed-decision)  
  <sub>Seeking Alpha, 10 hours ago</sub>  
  Short sellers rotate Treasury ETF shorts from TLT to IEF/IEI ahead of the Fed decision.
- [Global Bond Yields Hit Multi-Decade Highs Except in China - iShares 7-10 Year Treasury Bond ETF (NASDAQ:I](https://www.benzinga.com/markets/bonds/26/09/61811278/global-bond-yields-surge-everywhere-except-china)  
  <sub>Benzinga, 8 hours ago</sub>  
  A global bond yield crisis has pushed borrowing costs to multi-decade highs in the U.S., UK, and Japan, while China's yields near record lows.
- [While the U.S. 10-year Treasury bond rate exceeded 5% during the day, the investment performance of](https://www.mk.co.kr/en/economy/12154669)  
  <sub>매일경제, 8 hours ago</sub>  
  While the U.S. 10-year Treasury bond rate exceeded 5% during the day, the investment performance of the U.S. bond exchange-traded fund (ETF) was mixed...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score -0.40</summary>

```text
US Treasury yields: 3-month 3.96% (+0.16 on the week) | 5-year 4.83% (+0.21 on the week) | 10-year 4.97% (+0.14 on the week) | 30-year 5.32% (+0.03 on the week)
Yield curve, 10-year minus 3-month: +1.01 points -- upward sloping (normal)
US dollar index: 100.11 (+1.34 on the week)
Volatility (VIX): 16.79 (+0.3 on the week) -- elevated
```

</details>

<details><summary><b>Price and chart</b> — score -0.60</summary>

```text
Last close 90.80 (bar of 2026-09-16), from 502 daily bars
Trend: vs 20d SMA 92.27 (-1.6%), 50d 92.85 (-2.2%), 200d 94.87 (-4.3%); 50d below 200d
Momentum: RSI(14) 24.8 | MACD -0.599 vs signal -0.430 (histogram -0.170)
Returns: 1d -0.0% | 5d -1.2% | 1m -2.2% | 3m -3.9%
52-week range: 90.80 - 97.99 (now 0.0% of the way up)
Volatility: ATR(14) 0.38 (0.4% of price) | annualised 20d 5.1%
Volume: 1.36x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score -0.10</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score -0.10</summary>

```text
Fund type: Long Government
Yield: 4.0%
Credit quality: AA 100.0% | US government debt 99.6%
Three-year record: +2.8% a year | beta to the market 1.16
Cost and size: expense ratio 0.15% | net assets 41.82B
What it is made of: Bonds 99.6%, Cash 0.4%
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

<details><summary><b>Buying and selling by company insiders</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>Who is positioned how</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>Money going into and out of this fund</b> — score n/a</summary>

_Not available today._

</details>

### US company bonds, safer (LQD) · Index fund — BEARISH, confidence 0.35

**Result:** ERROR · BrokerError: submit_order failed for LQD: {"code":42210000,"message":"asset \"LQD\" cannot be sold short"}

**In the model's own words:**

> Yields rose sharply across the belly of the curve this week (5y +21bp, 10y +14bp), which is a direct headwind for a long-duration investment-grade credit fund. Price confirms: LQD sits at 104.62, essentially at the 52-week low, below its 20/50/200d averages with 50d under 200d, RSI 36 and MACD negative. Dollar strength (+1.34) and a firm front end argue rates pressure persists near term. Fundamentals are unremarkable-to-mildly supportive: 4.7% yield, solid A/BBB credit quality, cheap 0.14% fee, so carry cushions but does not offset duration. No analyst roll-up or CFTC positioning for this instrument; the only flow datum in the news is an unrelated single-fund item, so insider read is left null. News items are noise (ETF listicles), scored neutral. Conviction kept modest because a rate move of this size is not an outsized policy surprise and the fund is already near lows where mean-reversion risk is real.

**Main reasons it gave:**
- 5-year yield +21bp and 10-year +14bp on the week, direct duration headwind
- Close 104.62 within 0.3% of the 52-week low, 4% of the way up the range
- 50d SMA below 200d, RSI 36, MACD below signal
- 4.7% yield and 0.14% fee provide carry cushion; credit quality skewed A/BBB
- Dollar index +1.34 on the week, VIX 16.8 and slightly higher

<details><summary><b>News</b> — score +0.00</summary>

- [Daily ETF Flows: BOTZ Loses $187M](https://finance.yahoo.com/markets/options/articles/daily-etf-flows-botz-loses-210004282.html)  
  <sub>Yahoo Finance, 22 hours ago</sub>  
  Here are the daily ETF fund flows for September 14, 2026.
- [HYG vs JNK: The Two Biggest Junk Bond ETFs Look Identical, but the Cheaper One Pays More](https://247wallst.com/investing/etf/2026/09/15/hyg-vs-jnk-the-two-biggest-junk-bond-etfs-look-identical-but-the-cheaper-one-pays-more/)  
  <sub>24/7 Wall St., 21 hours ago</sub>  
  HYG and JNK offer similar high-yield bond exposure, but differences in fees and distributions give the cheaper fund an income edge investors should...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 3.96% (+0.16 on the week) | 5-year 4.83% (+0.21 on the week) | 10-year 4.97% (+0.14 on the week) | 30-year 5.32% (+0.03 on the week)
Yield curve, 10-year minus 3-month: +1.01 points -- upward sloping (normal)
US dollar index: 100.11 (+1.34 on the week)
Volatility (VIX): 16.79 (+0.3 on the week) -- elevated
```

</details>

<details><summary><b>Price and chart</b> — score -0.50</summary>

```text
Last close 104.62 (bar of 2026-09-16), from 502 daily bars
Trend: vs 20d SMA 105.59 (-0.9%), 50d 106.23 (-1.5%), 200d 108.86 (-3.9%); 50d below 200d
Momentum: RSI(14) 36.1 | MACD -0.568 vs signal -0.457 (histogram -0.111)
Returns: 1d +0.3% | 5d -0.7% | 1m -1.0% | 3m -4.1%
52-week range: 104.28 - 112.92 (now 4.0% of the way up)
Volatility: ATR(14) 0.50 (0.5% of price) | annualised 20d 6.4%
Volume: 1.14x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.10</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score +0.10</summary>

```text
Fund type: Corporate Bond
Yield: 4.7%
Credit quality: A 46.6%, BBB 40.2%, AA 12.3%, AAA 1.0%
Three-year record: +4.5% a year | beta to the market 1.35
Cost and size: expense ratio 0.14% | net assets 32.04B
What it is made of: Bonds 98.9%, Cash 1.1%, Convertible 0.0%
Largest holdings: BlackRock Cash Funds Treasury SL Agency 1.0%
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

<details><summary><b>Buying and selling by company insiders</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>Who is positioned how</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>Money going into and out of this fund</b> — score n/a</summary>

_Not available today._

</details>

### US government bonds, 1-3 years (SHY) · Index fund — BEARISH, confidence 0.35

**Result:** REJECTED · ATR 0.1001 is below 0.20% of price 81.26

**In the model's own words:**

> Short-duration Treasuries face a live rate-hike decision with the 5-year yield up 21bp on the week and the 3-month up 16bp, the part of the curve SHY actually owns. Price is at a fresh 52-week low, below all major moving averages with 50d under 200d and negative MACD. RSI at 23.5 is deeply oversold, which caps conviction and argues against pressing, and duration is short so downside in price terms is small while a 3.6% yield cushions. Headlines about TLT flows and an app builder are noise; the Citi hike call and the curve move are the substance.

**Main reasons it gave:**
- 5-year yield +21bp on the week, 3-month +16bp; front-end repricing hits SHY directly
- Fed decision priced as near-certain hike per Citi 'calibration' call
- Close at 81.26, the 52-week low, below 20/50/200d with 50d under 200d
- RSI(14) 23.5 deeply oversold and ATR just 0.1% of price - limited further downside
- 3.6% yield and AA/US-government-only credit cushion total return

<details><summary><b>News</b> — score -0.30</summary>

- ['Jackpot Mode': Bloomberg's Eric Balchunas Says Traders Are Betting $7 Billion on TLT In Hopes Of Rare Bond Market Move](https://247wallst.com/investing/etf/2026/09/16/jackpot-mode-bloombergs-eric-balchunas-says-traders-are-betting-7-billion-on-tlt-in-hopes-of-rare-bond-market-move/)  
  <sub>24/7 Wall St., 5 hours ago</sub>  
  On the morning of a Federal Reserve decision Wall Street has priced as a near-certain rate hike, $7 billion rushed into the iShares 20+ Year Treasury Bond...
- [Citi: Fed to hike this week — calls it a ‘calibration,’ not a new cycle](https://seekingalpha.com/news/4643450-citi-fed-to-hike-this-week-calls-it-a-calibration-not-a-new-cycle)  
  <sub>Seeking Alpha, 3 hours ago</sub>  
  Nearly two years after the Federal Reserve delivered the first rate cut of the last easing cycle, Citi economists now expect U.S. policymakers to raise the...
- [Ex-Fed Economist Warns About ‘Inflation Trap’ As Central Bank Prepares to Vote](https://www.benzinga.com/markets/macro-economic-events/26/09/61809965/ex-fed-economist-warns-about-inflation-trap-as-central-bank-prepares-to-vote)  
  <sub>Benzinga, 9 hours ago</sub>  
  Former Fed economist Marvin Barth debunks debt panic, blaming primary deficits—not nominal debt or bond yields—for U.S. budget risks.
- [Brian Kimathi: Businessman builds app that gives Kenyans access to US stocks and ETFs](https://biznakenya.com/brian-kimathi-businessman-behind-pandapanda-app/)  
  <sub>Bizna Kenya, 9 hours ago</sub>  
  It was this gap that Brian Kimathi set out to address when he began building PandaPanda in 2025.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score -0.30</summary>

```text
US Treasury yields: 3-month 3.96% (+0.16 on the week) | 5-year 4.83% (+0.21 on the week) | 10-year 4.97% (+0.14 on the week) | 30-year 5.32% (+0.03 on the week)
Yield curve, 10-year minus 3-month: +1.01 points -- upward sloping (normal)
US dollar index: 100.11 (+1.34 on the week)
Volatility (VIX): 16.79 (+0.3 on the week) -- elevated
```

</details>

<details><summary><b>Price and chart</b> — score -0.45</summary>

```text
Last close 81.26 (bar of 2026-09-16), from 502 daily bars
Trend: vs 20d SMA 81.73 (-0.6%), 50d 81.84 (-0.7%), 200d 82.36 (-1.3%); 50d below 200d
Momentum: RSI(14) 23.5 | MACD -0.165 vs signal -0.109 (histogram -0.056)
Returns: 1d -0.1% | 5d -0.4% | 1m -0.9% | 3m -1.1%
52-week range: 81.26 - 83.18 (now 0.0% of the way up)
Volatility: ATR(14) 0.10 (0.1% of price) | annualised 20d 1.8%
Volume: 0.52x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.10</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score +0.10</summary>

```text
Fund type: Short Government
Yield: 3.6%
Credit quality: AA 100.0% | US government debt 99.2%
Three-year record: +4.0% a year | beta to the market 0.22
Cost and size: expense ratio 0.15% | net assets 25.91B
What it is made of: Bonds 99.2%, Cash 0.8%
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

<details><summary><b>Buying and selling by company insiders</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>Who is positioned how</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>Money going into and out of this fund</b> — score n/a</summary>

_Not available today._

</details>

### US inflation-linked bonds (TIP) · Index fund — BEARISH, confidence 0.35

**Result:** REJECTED · no room for broad fund TIP under its 12% cap or the 'Duration' group limit: equity 99945.47, price 105.54, existing exposure 1055.35, headroom 98.73

**In the model's own words:**

> Real yields are rising hard: 5-year +21bp and 10-year +14bp on the week, with the dollar up 1.34 points. TIP is a duration instrument and is printing 52-week lows with RSI 25, 50d below 200d, MACD negative. That is a rate move corroborated by a decisive technical breakdown, though the oversold reading and low volume argue against a large view. News flow is noise (ETF listicles, Ethereum flows, one item addressing traders directly via a price-action promo -- disregarded). No POSITIONING or FUND FLOWS section and no analyst roll-up for a Treasury fund, so those stay null.

**Main reasons it gave:**
- 5-year yield +21bp and 10-year +14bp on the week
- Close 105.51 at the bottom of the 52-week range, 0% of the way up
- 50d SMA below 200d, MACD histogram -0.131
- RSI(14) 25.1 signals stretched downside, limiting conviction
- Dollar index +1.34 on the week; VIX 16.79 modestly elevated

<details><summary><b>News</b> — score +0.00</summary>

- [Don’t Miss Out on These ETFs](https://www.google.com/goto?url=CAESdAHrOzAV82j3qc_M6YkuEGMkAddIUNEDovfBNkZnNq-i-HfHZoZ5xgSL6H_0FEGve-zrSUQLD-TlRFtUNlhjc3WDLCG2Ba8CvSD0sq-BK5Vk_x89At5PBlOW5zehf5uZ2M287z9yYjLozjejtIcKeaRj_cMR)  
  <sub>Morningstar, 9 hours ago</sub>  
  Russel Kinnel: You probably don't need me to tell you about Vanguard Total Stock Market VTI. or the other giant exchange-traded funds.
- [Precision Trading with Spdr Bloomberg 1-10 Year Tips Etf (TIPX) Risk Zones](https://www.google.com/goto?url=CAES0QEB6zswFaoSgaOUTue1tSq6gGXrUX5mi6Js3FUOxZM9Rc1sosxDxQYUGirzpY3RQTg636nayIKaPKTvJcjDL_2OmavjVqPJgtMRF3aQwGgaJ4IJw88j1FHlJjn-WBuZ7M5PgdS9z1yQc-uqaXgsDcC4vhWZ0MEgJ_xt-_JNU5nhyYos3T1palA_KqZSHhMRTNn0yqk_mfJnROWe15WIHiGF1bpxb0naqhXFcmD3DQKAWV0KN1b_Vxxt9OM7wWaEUJKomJV1pEKykSUtrNWRuxCn4Q)  
  <sub>Stock Traders Daily, 10 hours ago</sub>  
  Price-action only: Spdr Bloomberg 1-10 Year Tips Etf (TIPX) movements set the tone for institutional models. Precision Trading with Spdr Bloomberg 1-10 Year...
- [The Global Bond Comeback: Why Higher Yields Are Opening a New Opportunity for Investors-Expert View by Spherical Insights](https://www.sphericalinsights.com/blogs/the-global-bond-comeback-why-higher-yields-are-opening-a-new-opportunity-for-investors)  
  <sub>Spherical Insights, 6 hours ago</sub>  
  Bond market size was valued at USD 120.58 trillion in 2025 and is estimated to grow to approximately USD 201.13 trillion by 2035, at a CAGR of 5.32%
- [Ex-Fed Economist Warns About ‘Inflation Trap’ As Central Bank Prepares to Vote](https://www.benzinga.com/markets/macro-economic-events/26/09/61809965/ex-fed-economist-warns-about-inflation-trap-as-central-bank-prepares-to-vote)  
  <sub>Benzinga, 9 hours ago</sub>  
  Former Fed economist Marvin Barth debunks debt panic, blaming primary deficits—not nominal debt or bond yields—for U.S. budget risks.
- [These 3 ETFs Could Deliver Double-Digit Returns, Says the AI Analyst](https://www.tipranks.com/news/these-3-etfs-could-deliver-double-digit-returns-says-the-ai-analyst)  
  <sub>TipRanks, 2 hours ago</sub>  
  TipRanks' ETF AI Analyst has an Outperform rating on the State Street SPDR Portfolio SP 500 ETF ($SPYM), Vanguard High Dividend Yield Index ETF ($VYM),...
- [Micron Stock Price Target Signals 69%+ Upside Ahead of Earnings — 3 ETFs That Could Benefit](https://www.tipranks.com/news/micron-stock-price-target-signals-69-upside-ahead-of-earnings-3-etfs-that-could-benefit)  
  <sub>TipRanks, 5 hours ago</sub>  
  Memory chip company Micron ($MU) will announce its fiscal fourth-quarter earnings on September 30. The stock has been one of the standout performers in the...
- [Unlock Deeper ETF Research](https://www.tipranks.com/news/labs/unlock-deeper-etf-research)  
  <sub>TipRanks, 5 hours ago</sub>  
  ETFs give investors a simple way to spread risk and reach new parts of the market. Yet each ETF may hold dozens or even hundreds of stocks. This can make <.
- [Ethereum ETF Sees Nearly Quarter of Assets Exit in a Day as Rally Pauses](https://www.tipranks.com/news/cryptocurrencies/ethereum-etf-sees-nearly-quarter-of-assets-exit-in-a-day-as-rally-pauses)  
  <sub>TipRanks, 4 hours ago</sub>  
  Ethereum ETF sees sharp outflow as traders lock in gains The Invesco Galaxy Ethereum ETF, QETH, recorded a sizeable outflow of $5.43 million on September 14...
- [Ethereum ETF Pulls Fresh Cash as Token Rally Stays in ‘Hold’ Mode](https://www.google.com/goto?url=CAESpgEB6zswFeczW5ZUOiktbpsfNyKHse6S32zIg9m2pJWEJ1kmHxLhFXQCbFEZLhiTp6NrEEsXlDzEqhP3jgytSpRTXcUfgfZ6Nyny65izEGxtf83tiKsJNcR1LE9mWTI_BLGxMnPjkTFLDN3DDbGhykf-n0Nmr1KZuVIrNaLEyIWEay-QyghISrORiYHUKKq8l7WwGYnHb4yahfsKdJqtXkSiHo-9p268)  
  <sub>TipRanks, 4 hours ago</sub>  
  Ethereum ETF Pulls Fresh Cash as Token Rally Stays in 'Hold' Mode iShares Ethereum Trust ETF ETHA drew a sizeable $80.5 million of net inflows on September...
- [San Francisco Tribune Releases Top 5 ETFs to Check Out in 2026](https://www.google.com/goto?url=CAESnQEB6zswFSdhax3WkdXp7GzQY8LWflwdVEC-5k4VWlAnaWOk8Ti44uIE8Ho3b7enY1WQussqQx70B5mPRkCVX1G8yJXB-JHUJRVRO7wEdSoy35BMqFB2y8hEuI7S57bIu1awZTk7HwReYlB9hJTtK1PWCtgDJx2IPAm9Y9nkpqwVv-GQZua3Li9-usqFKDt-B_yqZ7pjY3iNzq6Myc4z)  
  <sub>TipRanks, 6 hours ago</sub>  
  New York, United States, September 16th, 2026, FinanceWire Exchange-traded funds have become a central part of modern investing, giving investors access to...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 3.96% (+0.16 on the week) | 5-year 4.83% (+0.21 on the week) | 10-year 4.97% (+0.14 on the week) | 30-year 5.32% (+0.03 on the week)
Yield curve, 10-year minus 3-month: +1.01 points -- upward sloping (normal)
US dollar index: 100.11 (+1.34 on the week)
Volatility (VIX): 16.79 (+0.3 on the week) -- elevated
```

</details>

<details><summary><b>Price and chart</b> — score -0.60</summary>

```text
Last close 105.51 (bar of 2026-09-16), from 502 daily bars
Trend: vs 20d SMA 106.83 (-1.2%), 50d 107.23 (-1.6%), 200d 109.68 (-3.8%); 50d below 200d
Momentum: RSI(14) 25.1 | MACD -0.428 vs signal -0.297 (histogram -0.131)
Returns: 1d -0.3% | 5d -1.2% | 1m -1.2% | 3m -3.9%
52-week range: 105.51 - 112.20 (now 0.0% of the way up)
Volatility: ATR(14) 0.35 (0.3% of price) | annualised 20d 4.0%
Volume: 0.71x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score -0.10</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score -0.10</summary>

```text
Fund type: Inflation-Protected Bond
Yield: 5.0%
Credit quality: AA 99.9% | US government debt 99.9%
Three-year record: +3.6% a year | beta to the market 0.68
Cost and size: expense ratio 0.18% | net assets 15.01B
What it is made of: Bonds 99.9%, Cash 0.1%
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

<details><summary><b>Buying and selling by company insiders</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>Who is positioned how</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>Money going into and out of this fund</b> — score n/a</summary>

_Not available today._

</details>

### US government bonds, 20+ years (TLT) · Index fund — BEARISH, confidence 0.35

**Result:** REJECTED · no room for broad fund TLT under its 12% cap or the 'Duration' group limit: equity 99951.23, price 81.07, existing exposure 11917.58, headroom 116.49

**In the model's own words:**

> Yields are breaking higher across the curve into a Fed decision the market has priced as a hike: 5y +21bp, 10y +14bp on the week, 10y through 5% for the first time since 2007, and the dollar up 1.34. TLT is at the very bottom of its 52-week range (2.4% of the way up), below its 20/50/200d averages with 50d under 200d, RSI 38 and MACD negative -- a downtrend confirming the rate move rather than a washed-out bounce setup. The $7bn inflow story is real behavioural data but reads as retail dip-buying/crowding into a falling knife rather than a bullish tell, and short sellers rotating from TLT to the belly cuts both ways. Headline framing of a 'jackpot' trade is promotional and not treated as evidence. Modest conviction: the setup is oversold and a dovish surprise would snap it hard.

**Main reasons it gave:**
- 10-year Treasury yield above 5%, highest since 2007; 5y +21bp and 10y +14bp on the week
- Close 80.98 near 52-week low, below 20/50/200d SMAs with 50d under 200d
- RSI 38 and negative MACD histogram, 3-month return -6.0%
- Dollar index +1.34 on the week into a Fed decision priced for a hike
- $7bn of inflows into TLT reads as crowded dip-buying rather than confirmation

<details><summary><b>News</b> — score -0.40</summary>

- ['Jackpot Mode': Bloomberg's Eric Balchunas Says Traders Are Betting $7 Billion on TLT In Hopes Of Rare Bond Market Move](https://247wallst.com/investing/etf/2026/09/16/jackpot-mode-bloombergs-eric-balchunas-says-traders-are-betting-7-billion-on-tlt-in-hopes-of-rare-bond-market-move/)  
  <sub>24/7 Wall St., 5 hours ago</sub>  
  On the morning of a Federal Reserve decision Wall Street has priced as a near-certain rate hike, $7 billion rushed into the iShares 20+ Year Treasury Bond...
- [‘Jackpot Mode’: Bloomberg’s Eric Balchunas Says Traders Are Betting $7 Billion on TLT In Hopes Of Rare Bond Market Move](https://finance.yahoo.com/markets/options/articles/jackpot-mode-bloomberg-eric-balchunas-135303436.html)  
  <sub>Yahoo Finance, 5 hours ago</sub>  
  A $7 billion flood into a Treasury bond fund that has lost a third of its value sounds like a mistake, but Bloomberg ETF analyst Eric Balchunas sees...
- [Treasury ETF shorts shift toward belly ahead of Fed decision (TLT:NASDAQ)](https://seekingalpha.com/news/4643261-treasury-etf-shorts-shift-toward-belly-ahead-of-fed-decision)  
  <sub>Seeking Alpha, 10 hours ago</sub>  
  Short sellers rotate Treasury ETF shorts from TLT to IEF/IEI ahead of the Fed decision.
- [Traders bet $7 billion on TLT, a long-term Trea...](https://pluang.com/en/news-feed/mode-jackpot-trader-bertaruh-7-miliar-dolar-pada-tlt-untuk-bergerak-pasar)  
  <sub>Pluang, 5 hours ago</sub>  
  Traders have invested $7 billion into the iShares 20+ Year Treasury Bond ETF (TLT) ahead of a Federal Reserve rate hike decision, hoping for a "jackpot...
- [While the U.S. 10-year Treasury bond rate exceeded 5% during the day, the investment performance of](https://www.mk.co.kr/en/economy/12154669)  
  <sub>매일경제, 8 hours ago</sub>  
  While the U.S. 10-year Treasury bond rate exceeded 5% during the day, the investment performance of the U.S. bond exchange-traded fund (ETF) was mixed...
- [The 10-Year Treasury Broke 5% and Long Bond Holders Are Not Getting Rescued](https://247wallst.com/investing/2026/09/16/the-10-year-treasury-broke-5-and-long-bond-holders-are-not-getting-rescued/)  
  <sub>24/7 Wall St., 6 hours ago</sub>  
  Long Treasury yields just hit levels not seen since 2007, and the usual rescue plan from the Fed is nowhere on the horizon. Understanding why this time is...
- [Inflation Fears and Oil Surge Rattle Markets](https://www.etf.com/sections/bonds/inflation-fears-and-oil-surge-rattle-markets)  
  <sub>ETF.com, 22 hours ago</sub>  
  The summer months may have ended, but the dog days appear to be sticking around, at least for markets. With the Fed rate decision due Wednesday and new...
- [BlackRock’s Rick Rieder Turns Cautious on US Stocks, Warns $40 Trillion Debt Is Becoming a ‘Compounding…Problem’](https://www.tradingview.com/news/benzinga:bf78b3700094b:0-blackrock-s-rick-rieder-turns-cautious-on-us-stocks-warns-40-trillion-debt-is-becoming-a-compounding-problem/)  
  <sub>TradingView, 7 hours ago</sub>  
  BlackRock Chief Investment Officer Rick Rieder warns that the $40 trillion national debt is a mounting fiscal burden, yet he views a 5% yield on 10-year...
- [IWM News | ISHARES RUSSELL 2000 ETF (NYSEARCA:IWM)](https://www.chartmill.com/stock/quote/IWM/news)  
  <sub>ChartMill, 22 hours ago</sub>  
  Latest news and press releases for ISHARES RUSSELL 2000 ETF (NYSEARCA:IWM).
- [S&P 500, Nasdaq, Dow End Lower As Investors Price In Rate Hike Ahead Of Fed Meeting — AMZN, META, MU, TSLA, PLTR In Focus](https://stocktwits.com/news-articles/markets/equity/s-and-p-500-nasdaq-dow-end-lower-as-investors-price-in-rate-hike-ahead-of-fed-meeting-amzn-meta-mu-tsla-pltr-in-focus/cZtn8vQRBcx)  
  <sub>Stocktwits, 22 hours ago</sub>  
  The S&P 500 ended Tuesday 0.5% lower, while the Nasdaq 100 slipped 0.7% and the Dow Jones Industrial Average eased 0.6%. Benchmark 10-year yields hit 5%,...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score -0.40</summary>

```text
US Treasury yields: 3-month 3.96% (+0.16 on the week) | 5-year 4.83% (+0.21 on the week) | 10-year 4.97% (+0.14 on the week) | 30-year 5.32% (+0.03 on the week)
Yield curve, 10-year minus 3-month: +1.01 points -- upward sloping (normal)
US dollar index: 100.11 (+1.34 on the week)
Volatility (VIX): 16.79 (+0.3 on the week) -- elevated
```

</details>

<details><summary><b>Price and chart</b> — score -0.50</summary>

```text
Last close 80.98 (bar of 2026-09-16), from 502 daily bars
Trend: vs 20d SMA 82.08 (-1.3%), 50d 82.73 (-2.1%), 200d 85.95 (-5.8%); 50d below 200d
Momentum: RSI(14) 38.0 | MACD -0.549 vs signal -0.437 (histogram -0.113)
Returns: 1d +0.3% | 5d -0.9% | 1m -0.5% | 3m -6.0%
52-week range: 80.71 - 92.06 (now 2.4% of the way up)
Volatility: ATR(14) 0.68 (0.8% of price) | annualised 20d 10.3%
Volume: 1.30x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score -0.10</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score -0.10</summary>

```text
Fund type: Long Government
Yield: 4.7%
Credit quality: AA 100.0% | US government debt 99.6%
Three-year record: -0.6% a year | beta to the market 2.39
Cost and size: expense ratio 0.15% | net assets 47.05B
What it is made of: Bonds 99.6%, Cash 0.4%
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

<details><summary><b>Buying and selling by company insiders</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>Who is positioned how</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>Money going into and out of this fund</b> — score n/a</summary>

_Not available today._

</details>

### US dollar (UUP) · Index fund — BULLISH, confidence 0.35

**Result:** ACCEPTED · 422 shares · submitted buy 422 UUP @ ~28.38, stop 28.16

**In the model's own words:**

> Dollar index up 1.34 on the week alongside a broad rise in US yields (5y +21bp, 10y +14bp), a rate-differential move that directly drives this fund. UUP is near the top of its 52-week range (89%), above 20/50/200d SMAs with 50d over 200d, RSI 63 and MACD crossing positive. The move is real but modest in absolute terms and volume is below average, so this is a trend-continuation call rather than a catalyst. Analyst roll-up covers only a cash money-market holding and carries no information; no positioning or flow data available. The single news item is generic commentary and was not weighted.

**Main reasons it gave:**
- DXY 100.11, +1.34 on the week
- 5y yield +21bp, 10y +14bp week over week, supporting rate differentials
- Price 89% of 52-week range, above 20/50/200d SMAs with 50d>200d
- MACD histogram +0.037 turning positive, RSI 63
- Volume 0.92x average -- no decisive breakout confirmation

<details><summary><b>News</b> — score +0.00</summary>

- [Ex-Fed Economist Warns About ‘Inflation Trap’ As Central Bank Prepares to Vote](https://www.benzinga.com/markets/macro-economic-events/26/09/61809965/ex-fed-economist-warns-about-inflation-trap-as-central-bank-prepares-to-vote)  
  <sub>Benzinga, 9 hours ago</sub>  
  Former Fed economist Marvin Barth debunks debt panic, blaming primary deficits—not nominal debt or bond yields—for U.S. budget risks.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 3.96% (+0.16 on the week) | 5-year 4.83% (+0.21 on the week) | 10-year 4.97% (+0.14 on the week) | 30-year 5.32% (+0.03 on the week)
Yield curve, 10-year minus 3-month: +1.01 points -- upward sloping (normal)
US dollar index: 100.11 (+1.34 on the week)
Volatility (VIX): 16.79 (+0.3 on the week) -- elevated
```

</details>

<details><summary><b>Price and chart</b> — score +0.45</summary>

```text
Last close 28.38 (bar of 2026-09-16), from 502 daily bars
Trend: vs 20d SMA 28.06 (+1.1%), 50d 28.20 (+0.6%), 200d 27.72 (+2.4%); 50d above 200d
Momentum: RSI(14) 63.1 | MACD 0.013 vs signal -0.024 (histogram 0.037)
Returns: 1d +0.5% | 5d +1.4% | 1m +1.0% | 3m +1.6%
52-week range: 26.47 - 28.60 (now 89.4% of the way up)
Volatility: ATR(14) 0.11 (0.4% of price) | annualised 20d 5.7%
Volume: 0.92x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.00</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score +0.00</summary>

```text
Fund type: Trading--Miscellaneous
What it holds: P/E n/a | P/B 0.00 | P/S 0.00 | 3y earnings growth n/a
Yield: 3.3%
Three-year record: +3.2% a year | beta to the market -9.48
Cost and size: expense ratio 0.75% | net assets 298.71M
What it is made of: Cash 100.0%
Largest holdings: Invesco Shrt-Trm Inv Gov&Agcy Instl 48.8%
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

_Not available today._

</details>

<details><summary><b>Money going into and out of this fund</b> — score n/a</summary>

_Not available today._

</details>

### Commodities basket (DBC) · Index fund — NEUTRAL, confidence 0.25

**In the model's own words:**

> DBC is a broad commodity basket with 50.6% in 'Other' and 44.8% in cash, so its composition is opaque and difficult to assess directionally. Technicals show the fund near 52-week highs (96.6th percentile) with RSI at 68.5 indicating overbought conditions, while momentum remains positive but momentum histogram is modest. The trend is upward across all timeframes -- 20d, 50d, and 200d SMAs all in bullish alignment -- and the fund has delivered +19.3% over three months. However, recent volume is weak at 0.69x average, and the latest daily bar closed down 1.2%, raising questions about the durability of the move. Macro backdrop shows rising Treasury yields across the curve (10y +14bp, 5y +21bp on the week) and a strengthening dollar (+1.34 this week), both headwinds for commodity-denominated wealth. The VIX at 16.79 is elevated but not alarming. With no news catalyst, no analyst coverage of the holdings, and the fund already priced at the top of its range after a large rally, the risk-reward appears balanced rather than tilted. The combination of overbought technicals, weak volume, elevated rates, and strong dollar argues against adding exposure here despite the uptrend. A modest pullback would be required to justify fresh commitment.

**Main reasons it gave:**
- RSI 68.5 signals overbought conditions near 52-week highs
- Volume 0.69x average indicates weakening conviction on the rally
- Rising US yields and strengthening dollar headwinds for commodities
- Uptrend intact across 20d/50d/200d but momentum histogram modest at 0.112

<details><summary><b>News</b> — score +0.00</summary>

_No news found for this one today._

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 3.96% (+0.16 on the week) | 5-year 4.83% (+0.21 on the week) | 10-year 4.97% (+0.14 on the week) | 30-year 5.32% (+0.03 on the week)
Yield curve, 10-year minus 3-month: +1.01 points -- upward sloping (normal)
US dollar index: 100.11 (+1.34 on the week)
Volatility (VIX): 16.79 (+0.3 on the week) -- elevated
```

</details>

<details><summary><b>Price and chart</b> — score +0.35</summary>

```text
Last close 33.28 (bar of 2026-09-16), from 502 daily bars
Trend: vs 20d SMA 31.89 (+4.4%), 50d 30.26 (+10.0%), 200d 27.60 (+20.6%); 50d above 200d
Momentum: RSI(14) 68.5 | MACD 0.949 vs signal 0.837 (histogram 0.112)
Returns: 1d -1.2% | 5d +1.3% | 1m +8.9% | 3m +19.3%
52-week range: 22.07 - 33.68 (now 96.6% of the way up)
Volatility: ATR(14) 0.50 (1.5% of price) | annualised 20d 18.6%
Volume: 0.69x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.10</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score +0.10</summary>

```text
Fund type: Commodities Broad Basket
What it holds: P/E n/a | P/B 0.00 | P/S 0.00 | 3y earnings growth n/a
Yield: 2.4%
Three-year record: +13.9% a year | beta to the market 1.05
Cost and size: expense ratio 0.85% | net assets 1.80B
What it is made of: Other 50.6%, Cash 44.8%, Bonds 2.7%, Stocks 1.9%
Largest holdings: Invesco Shrt-Trm Inv Gov&Agcy Instl 40.8%, Brent Crude Future Nov 26 8.9%, Invesco Short Term Treasury ETF 6.2%, Mini Ibovespa Future Dec 26 1.9%
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
Rolled up from the 4 largest holdings, 57.7% of the fund by weight
Ratings by weight: buy n/a | hold n/a | sell n/a (mean n/a on a 1=strong buy to 5=strong sell scale)
Weighted price target: n/a above the current prices
Holdings read: AGPXX, BRNF6, TBLL, WINZ26
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

_Not available today._

</details>

### US small companies (IWM) · Index fund — NEUTRAL, confidence 0.25

**In the model's own words:**

> IWM is trading 4.1% below its 50-day MA and 3.6% below its 20-day MA, with RSI at 32 suggesting oversold conditions in the near term. The technical picture shows a fund that has pulled back 6.8% over the month but remains 3.3% above its 200-day MA, maintaining an uptrend structure. However, several headwinds temper any bullish read. The fund is valued at a P/E of 17.30 and P/B of 2.13, which GuruFocus characterizes as overvalued. Most critically, large speculators hold a net short of 25.5% of open interest in Russell E-Mini contracts—at the 7th percentile of crowding over the past year, this indicates a historically crowded short position. Crowded extremes often mark exhaustion rather than direction, but the positioning is too recent and the short too pronounced to ignore. Macro backdrop is mixed: Treasury yields have moved higher across the curve this week, the dollar has strengthened 1.34% on the week, and the Fed is signaling potential rate hikes after a 3-year pause. Small caps like those in IWM are rate-sensitive and tend to underperform in a rising-rate environment. Volume is light at 0.81x the 20-day average, suggesting weak conviction on either side. Analyst coverage on the five largest holdings (1.7% of fund) is thin, shows 100% buy ratings with +22.9% upside targets, but this slice is too small to drive a conviction signal. The oversold technicals could attract mean-reversion buyers, but absent a specific catalyst—a Fed pivot, a data surprise favoring risk, or a break of the 200-day support—this appears to be a fade of recent weakness rather than a new trend. A NEUTRAL stance respects both the technical extremes and the macro headwinds.

**Main reasons it gave:**
- Large speculators short 25.5% of open interest at the 7th percentile of crowding, an extreme that often marks exhaustion
- Treasury yields up 14-21bp across the curve this week and Fed signaling likely rate hikes, headwind for rate-sensitive small caps
- Fund trading 4.1% below 50-day MA and RSI 32, oversold but lacks volume conviction
- P/E 17.30 and P/B 2.13 characterized as overvalued by fundamental metrics
- Analyst view on top 1.7% of holdings is bullish but too thin a sample to drive fund signal

<details><summary><b>News</b> — score +0.00</summary>

- [PRFZ Is Turning 20: A Battle-Tested SMID-Cap ETF](https://www.etftrends.com/smart-beta-content-hub/prfz-turning-20-battle-tested-smid-cap-etf/)  
  <sub>ETF Trends, 3 hours ago</sub>  
  PRFZ marks 20 years of fundamental indexing, selecting SMID-cap equities by economic footprint to outperform traditional benchmarks.
- [IWM News | ISHARES RUSSELL 2000 ETF (NYSEARCA:IWM)](https://www.chartmill.com/stock/quote/IWM/news)  
  <sub>ChartMill, 22 hours ago</sub>  
  Latest news and press releases for ISHARES RUSSELL 2000 ETF (NYSEARCA:IWM).
- [Fed Most Likely to Hike Rates After 3 Years: ETFs to Win/Lose](https://www.zacks.com/stock/news/2990405/fed-most-likely-to-hike-rates-after-3-years-etfs-to-winlose)  
  <sub>Zacks Investment Research, 7 hours ago</sub>  
  The Fed's likely rate hike could create opportunities and risks across ETFs, with value, technology and energy in focus while homebuilders,...
- [IWM Looks 46.9% Overvalued on GF Value™](https://www.gurufocus.com/news/9082166/iwm-looks-469-overvalued-on-gf-value)  
  <sub>GuruFocus, 24 hours ago</sub>  
  On September 15, 2026, the iShares Russell 2000 ETF (IWM) announced a dividend payment of $0.7504 per share, payable on September 18 to shareholders of...
- [ITWO: Downgrading To Hold As The High Volatility Tailwind Fades (BATS:ITWO)](https://seekingalpha.com/article/4947112-itwo-downgrading-to-hold-as-the-high-volatility-tailwind-fades)  
  <sub>Seeking Alpha, 1 hour ago</sub>  
  ProShares Russell 2000 High Income ETF is downgraded to Hold as the volatile regime that fueled recent outperformance is fading. Click for more on ITWO.
- [S&P 500 Gains, Crude Falls Ahead Of Fed's Expected First Hike Since 2023: Stock Market Today](https://www.tradingview.com/news/benzinga:7cee8586a094b:0-s-p-500-gains-crude-falls-ahead-of-fed-s-expected-first-hike-since-2023-stock-market-today/)  
  <sub>TradingView, 2 hours ago</sub>  
  A sharp reversal in crude oil handed U.S. equities a reprieve on Wednesday, with stocks grinding higher off six-week lows just hours before the Federal...
- [Daily ETF Flows: BOTZ Loses $187M](https://www.etf.com/sections/daily-etf-flows/daily-etf-flows-botz-loses-187m)  
  <sub>ETF.com, 17 hours ago</sub>  
  Here are the daily ETF fund flows for September 14, 2026.
- [5 Best International ETFs to Buy in 2026](https://www.fool.com/investing/how-to-invest/etfs/international-etfs/)  
  <sub>The Motley Fool, 21 hours ago</sub>  
  International exchange-traded funds (ETFs) are listed investment vehicles that hold stocks from countries outside the U.S. They offer a simple way to gain...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 3.96% (+0.16 on the week) | 5-year 4.83% (+0.21 on the week) | 10-year 4.97% (+0.14 on the week) | 30-year 5.32% (+0.03 on the week)
Yield curve, 10-year minus 3-month: +1.01 points -- upward sloping (normal)
US dollar index: 100.11 (+1.34 on the week)
Volatility (VIX): 16.79 (+0.3 on the week) -- elevated
```

</details>

<details><summary><b>Price and chart</b> — score -0.15</summary>

```text
Last close 283.43 (bar of 2026-09-16), from 502 daily bars
Trend: vs 20d SMA 293.96 (-3.6%), 50d 295.56 (-4.1%), 200d 274.45 (+3.3%); 50d above 200d
Momentum: RSI(14) 32.0 | MACD -3.099 vs signal -1.772 (histogram -1.327)
Returns: 1d -0.6% | 5d -2.5% | 1m -6.8% | 3m -3.0%
52-week range: 229.11 - 305.09 (now 71.5% of the way up)
Volatility: ATR(14) 3.34 (1.2% of price) | annualised 20d 12.4%
Volume: 0.81x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score -0.20</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score -0.20</summary>

```text
Fund type: Small Blend
What it holds: P/E 17.30 | P/B 2.13 | P/S 1.31 | 3y earnings growth n/a
Yield: 0.9%
Three-year record: +17.2% a year | beta to the market 1.24
Cost and size: expense ratio 0.19% | net assets 80.46B
What it is made of: Stocks 99.5%, Cash 0.5%
Largest holdings: JFrog Ltd Ordinary Shares 0.3%, Moog Inc Class A 0.3%, BlackRock Cash Funds Treasury SL Agency 0.3%, UMB Financial Corp 0.3%, Glaukos Corp 0.3%
Sector mix: Healthcare 21.0%, Financial services 18.1%, Technology 13.8%, Industrials 13.2%
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

<details><summary><b>What analysts and big funds say</b> — score +0.35</summary>

_Not available today._

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score +0.35</summary>

```text
Rolled up from the 5 largest holdings, 1.7% of the fund by weight  -- thin, so read this as a fact about that slice rather than the fund
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 1.64 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +22.9% above the current prices
Holdings read: FROG, MOG-A, XTSLA, UMBF, GKOS
Recent rating changes among them:
  - FROG: 2026-09-04 DA Davidson: main, Buy -> Buy
  - MOG-A: 2026-09-15 Guggenheim: init, ? -> Neutral
  - UMBF: 2026-09-14 UBS: init, ? -> Neutral
  - GKOS: 2026-08-20 BTIG: main, Buy -> Buy
```

</details>

<details><summary><b>Buying and selling by company insiders</b> — score -0.35</summary>

_Not available today._

</details>

<details><summary><b>Who is positioned how</b> — score -0.35</summary>

```text
Contract: RUSSELL E-MINI (positions as of 2026-09-08, published the following Friday)
Large speculators: net short 25.5% of open interest (431,147 contracts)
Change on the week: +0.2% of open interest
Crowding: 7% percentile over 52 weeks -- a crowded short by the standards of the past year
Read this as crowding, not as a forecast: an extreme is as often the end of a move as the middle of one.
```

</details>

<details><summary><b>Money going into and out of this fund</b> — score -0.35</summary>

_Not available today._

</details>

### S&P 500, equal weight (RSP) · Index fund — NEUTRAL, confidence 0.25

**In the model's own words:**

> RSP is a large-blend equal-weight fund holding diversified US equities. Technicals show a deteriorating near-term picture: price is 2.7% below the 20-day SMA, RSI at 35 signals oversold conditions, MACD histogram deeply negative at -0.892, and volume is light at 0.82x average. The fund has declined 3.8% over one month despite remaining 3.8% above its 200-day MA. Macro backdrop is mixed: Treasury yields moved higher across the curve this week (3-month +16bp, 5-year +21bp, 10-year +14bp), the curve remains normally upward-sloping at +1.01, and the dollar strengthened 1.34% on the week. VIX sits at 16.79, modestly elevated but not alarming. Fund fundamentals show a P/E of 21.39 with 1.5% yield and a three-year track record of +14.9% annually (beta 0.83). The analyst view is thin—covering only 1.8% of holdings via the top 5 positions—showing buy ratings at 67.9% but with a downgrade in MRNA (Rothschild downgrade to Sell on Sept 3) offsetting modest positive targets at +5.2%. CFTC positioning data from Sept 8 shows large speculators net short 16.5% of open interest, a significant shift (+42.3% on the week), but at only the 58th percentile historically, indicating this is not yet an extreme crowding signal. The combination of weakening momentum, rising rates, and heavy short positioning in the E-mini S&P 500 futures creates near-term pressure, but no decisive macro catalyst or technical break has materialized to justify a strong directional call. The fund's diversified composition and stable long-term beta argue against conviction in either direction at this juncture.

**Main reasons it gave:**
- Price 2.7% below 20-day SMA with RSI at 35 (oversold)
- MACD histogram at -0.892 with histogram deeply negative
- Treasury yields +14 to +21bp this week across curve
- Large speculators shifted to 16.5% net short, +42.3% positioning change week-over-week
- Analyst roll-up thin at 1.8% coverage; top holding MRNA downgraded to Sell by Rothschild

<details><summary><b>News</b> — score -0.15</summary>

- [Is Invesco S&P 500 Pure Value ETF (RPV) a Strong ETF Right Now?](https://finance.yahoo.com/markets/stocks/articles/invesco-p-500-pure-value-102002995.html)  
  <sub>Yahoo Finance, 9 hours ago</sub>  
  The Invesco S&P 500 Pure Value ETF (RPV) made its debut on 03/01/2006, and is a smart beta exchange traded fund that provides broad exposure to the Style...
- [2 Closed-End Fund Buys In The Month Of August 2026](https://seekingalpha.com/article/4946766-2-closed-end-fund-buys-in-the-month-of-august-2026)  
  <sub>Seeking Alpha, 20 hours ago</sub>  
  Every month I add to positions in my CEF portfolio, which helps to compound my distribution growth over the long term. Click for this month's additions.
- [Equity Futures Climb Into FOMC as Oil Cools](https://www.moomoo.com/community/feed/equity-futures-climb-into-fomc-as-oil-cools-117280613662726?chain_id=Name1K9-3FXPhg.1lal160&global_content=%7B%22promote_id%22%3A13764%2C%22sub_promote_id%22%3A107%2C%22f%22%3A%22www.moomoo.com%2Fetfs%2FIAUM-US%22%7D)  
  <sub>Moomoo, 7 hours ago</sub>  
  Tap the related stocks on the image above to add them to your Watchlist. Market Overview $E-mini S&P 500 Futures (DEC6) (ESmain.US)$ +0.36% at 7683.2...
- [ETFs Investing in F5, Inc. Stocks](https://www.tradingview.com/symbols/BIVA-FFIV/etfs/)  
  <sub>TradingView, 24 hours ago</sub>  
  Explore funds investing in FFIV in a single list with price, expense ratio, and more stats for an in-depth analysis of new opportunities.
- [Fidelity Just Warned 500-Stock Fund Owners. 35% to 40% of Your S&P 500 Moves Come From 7 Mega-Cap Stocks](https://www.aol.com/articles/fidelity-just-warned-500-stock-150400000.html)  
  <sub>AOL.com, 19 hours ago</sub>  
  Fidelity sent a warning letter to S&P 500 fund holders, and a financial advisor on a major podcast confirmed what the fine print actually means for your...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score -0.15</summary>

```text
US Treasury yields: 3-month 3.96% (+0.16 on the week) | 5-year 4.83% (+0.21 on the week) | 10-year 4.97% (+0.14 on the week) | 30-year 5.32% (+0.03 on the week)
Yield curve, 10-year minus 3-month: +1.01 points -- upward sloping (normal)
US dollar index: 100.11 (+1.34 on the week)
Volatility (VIX): 16.79 (+0.3 on the week) -- elevated
```

</details>

<details><summary><b>Price and chart</b> — score -0.35</summary>

```text
Last close 212.46 (bar of 2026-09-16), from 502 daily bars
Trend: vs 20d SMA 218.37 (-2.7%), 50d 217.25 (-2.2%), 200d 204.61 (+3.8%); 50d above 200d
Momentum: RSI(14) 35.1 | MACD -1.288 vs signal -0.396 (histogram -0.892)
Returns: 1d -0.7% | 5d -1.0% | 1m -3.8% | 3m +0.1%
52-week range: 182.18 - 222.77 (now 74.6% of the way up)
Volatility: ATR(14) 1.82 (0.9% of price) | annualised 20d 10.0%
Volume: 0.82x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score -0.10</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score -0.10</summary>

```text
Fund type: Large Blend
What it holds: P/E 21.39 | P/B 3.11 | P/S 1.95 | 3y earnings growth n/a
Yield: 1.5%
Three-year record: +14.9% a year | beta to the market 0.83
Cost and size: expense ratio 0.20% | net assets 100.87B
What it is made of: Stocks 99.9%, Cash 0.1%
Largest holdings: Moderna Inc 0.6%, Veeva Systems Inc Class A 0.3%, Zebra Technologies Corp Ordinary Shares - Class A 0.3%, Charles River Laboratories International Inc 0.3%, DoorDash Inc Ordinary Shares - Class A 0.3%
Sector mix: Technology 17.3%, Industrials 14.7%, Financial services 14.6%, Healthcare 13.1%
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

<details><summary><b>What analysts and big funds say</b> — score +0.05</summary>

_Not available today._

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score +0.05</summary>

```text
Rolled up from the 5 largest holdings, 1.8% of the fund by weight  -- thin, so read this as a fact about that slice rather than the fund
Ratings by weight: buy 67.9% | hold 32.1% | sell 0.0% (mean 2.12 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +5.2% above the current prices
Holdings read: MRNA, VEEV, ZBRA, CRL, DASH
Recent rating changes among them:
  - MRNA: 2026-09-03 Rothschild & Co: down, Neutral -> Sell
  - VEEV: 2026-08-28 Citigroup: main, Neutral -> Neutral
  - ZBRA: 2026-09-15 Needham: main, Buy -> Buy
  - CRL: 2026-09-11 Evercore ISI Group: main, Outperform -> Outperform
  - DASH: 2026-09-09 Scotiabank: init, ? -> Sector Outperform
```

</details>

<details><summary><b>Buying and selling by company insiders</b> — score -0.20</summary>

_Not available today._

</details>

<details><summary><b>Who is positioned how</b> — score -0.20</summary>

```text
Contract: E-MINI S&P 500 (positions as of 2026-09-08, published the following Friday)
Large speculators: net short 16.5% of open interest (2,071,836 contracts)
Change on the week: +42.3% of open interest
Crowding: 58% percentile over 52 weeks -- within its normal range
Read this as crowding, not as a forecast: an extreme is as often the end of a move as the middle of one.
```

</details>

<details><summary><b>Money going into and out of this fund</b> — score -0.20</summary>

_Not available today._

</details>

### Europe (VGK) · Index fund — NEUTRAL, confidence 0.25

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Europe equities are pulling back below 20d and 50d SMAs with negative MACD and RSI 33.7, while the dollar jumped 1.34 on the week and US yields rose across the curve (5y +21bp) — a mildly bearish mix for a dollar-denominated European fund. Offsetting that, 50d remains above 200d, valuation is reasonable (P/E 17.7, 2.8% yield) and speculative EAFE positioning is at a 98th-percentile crowded long, which cuts both ways. No policy or data surprise specific to Europe; the news items are constituent-level listicles and carry no information. Default to NEUTRAL with a slight downside tilt.

**Main reasons it gave:**
- Close 88.51 below 20d (-3.0%) and 50d (-2.2%) SMA, MACD histogram -0.423, RSI 33.7
- Dollar index +1.34 on the week to 100.11, a headwind for unhedged European equity exposure
- US 5y yield +21bp, 10y +14bp on the week
- EAFE spec net long at 98th percentile of 52 weeks — crowded positioning
- Analyst roll-up +19.5% target but covers only 11.5% of fund weight

<details><summary><b>News</b> — score +0.00</summary>

- [ETFs Investing in Adyen NV Stocks](https://www.tradingview.com/symbols/OTC-ADYYF/etfs/)  
  <sub>TradingView, 11 hours ago</sub>  
  Explore funds investing in ADYYF in a single list with price, expense ratio, and more stats for an in-depth analysis of new opportunities.
- [ETFs Investing in Genmab A/S Stocks](https://www.tradingview.com/symbols/FWB-GE9/etfs/)  
  <sub>TradingView, 17 hours ago</sub>  
  Explore funds investing in GE9 in a single list with price, expense ratio, and more stats for an in-depth analysis of new opportunities.
- [ETFs Investing in Sacyr SA Stocks](https://www.tradingview.com/symbols/TRADEGATE-VHM/etfs/)  
  <sub>TradingView, 21 hours ago</sub>  
  Explore funds investing in VHM in a single list with price, expense ratio, and more stats for an in-depth analysis of new opportunities.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 3.96% (+0.16 on the week) | 5-year 4.83% (+0.21 on the week) | 10-year 4.97% (+0.14 on the week) | 30-year 5.32% (+0.03 on the week)
Yield curve, 10-year minus 3-month: +1.01 points -- upward sloping (normal)
US dollar index: 100.11 (+1.34 on the week)
Volatility (VIX): 16.79 (+0.3 on the week) -- elevated
```

</details>

<details><summary><b>Price and chart</b> — score -0.35</summary>

```text
Last close 88.51 (bar of 2026-09-16), from 502 daily bars
Trend: vs 20d SMA 91.20 (-3.0%), 50d 90.53 (-2.2%), 200d 87.28 (+1.4%); 50d above 200d
Momentum: RSI(14) 33.7 | MACD -0.541 vs signal -0.118 (histogram -0.423)
Returns: 1d -0.5% | 5d -1.9% | 1m -3.9% | 3m -1.7%
52-week range: 77.90 - 93.19 (now 69.4% of the way up)
Volatility: ATR(14) 0.79 (0.9% of price) | annualised 20d 10.0%
Volume: 0.71x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.10</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score +0.10</summary>

```text
Fund type: Europe Stock
What it holds: P/E 17.67 | P/B 2.30 | P/S 1.67 | 3y earnings growth n/a
Yield: 2.8%
Three-year record: +17.6% a year | beta to the market 0.90
Cost and size: expense ratio 0.06% | net assets 39.06B
What it is made of: Stocks 98.9%, Cash 0.8%, Other 0.3%
Largest holdings: ASML Holding NV 3.9%, HSBC Holdings PLC 2.3%, Roche Holding AG Ordinary Shares new 1.9%, Novartis AG Registered Shares 1.8%, Nestle SA 1.6%
Sector mix: Financial services 25.2%, Industrials 19.9%, Healthcare 12.3%, Technology 8.6%
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
Rolled up from the 5 largest holdings, 11.5% of the fund by weight  -- thin, so read this as a fact about that slice rather than the fund
Ratings by weight: buy 64.6% | hold 35.4% | sell 0.0% (mean 2.12 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +19.5% above the current prices
Holdings read: ASML.AS, HSBA.L, ROP.SW, NOVN.SW, NESN.SW
Recent rating changes among them: none reported
```

</details>

<details><summary><b>Buying and selling by company insiders</b> — score -0.30</summary>

_Not available today._

</details>

<details><summary><b>Who is positioned how</b> — score -0.30</summary>

```text
Contract: MSCI EAFE (positions as of 2026-09-08, published the following Friday)
Large speculators: net long 5.1% of open interest (477,461 contracts)
Change on the week: -0.6% of open interest
Crowding: 98% percentile over 52 weeks -- a crowded long by the standards of the past year
Read this as crowding, not as a forecast: an extreme is as often the end of a move as the middle of one.
```

</details>

<details><summary><b>Money going into and out of this fund</b> — score -0.30</summary>

_Not available today._

</details>

### Emerging markets (VWO) · Index fund — NEUTRAL, confidence 0.25

**In the model's own words:**

> VWO is caught between conflicting signals that cancel to near-neutral. Technicals are weak: price sits 2.2% below its 20-day moving average, RSI is depressed at 39.5, MACD is negative with a bearish histogram, and the fund has declined 3% over five days on below-average volume. The 52-week positioning at 73.7% of range offers no edge. Macro headwinds are material: Treasury yields have risen across the curve this week (10-year +14bp, 5-year +21bp), the dollar has spiked 1.34% to a two-year high, and volatility sits elevated at 16.79 VIX. These moves are bearish for emerging markets, which typically suffer when the dollar strengthens and dollar-denominated funding costs rise. However, fundamental data tempers the downside. The fund's valuation is reasonable at 16.5x earnings and 2.11x book, yielding 2.3%, and three-year returns of +17% annually suggest underlying business quality. Analyst coverage of the top 22.7% of holdings shows 100% buy ratings with +41.2% price target upside, though this thin roll-up does not speak to the full fund. CFTC positioning in EM futures is at the 55th percentile with no significant crowding, and the +0.1% weekly change shows no conviction shift. The mismatch between strong fundamental ratings and weak technical/macro setup leaves no clear directional edge. Recent headlines are generic list-making, not actionable news.

**Main reasons it gave:**
- Dollar index +1.34% to 100.11 on the week weighs on EM competitiveness
- RSI 39.5 and MACD negative with bearish histogram confirm weakening momentum
- Treasury yields up across curve (+21bp at 5y) raises dollar funding costs
- Analyst roll-up 100% buy with +41.2% price target offset by thin 22.7% coverage
- CFTC EM futures at 55th percentile crowding with minimal weekly flow change

<details><summary><b>News</b> — score +0.00</summary>

- [5 Best Emerging Markets ETFs for 2026 and How to Invest](https://www.fool.com/investing/how-to-invest/etfs/emerging-markets-etfs/)  
  <sub>The Motley Fool, 20 hours ago</sub>  
  An emerging markets ETF (exchange-traded fund) is a listed investment vehicle that invests in stocks from developing nations. They can offer investors...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 3.96% (+0.16 on the week) | 5-year 4.83% (+0.21 on the week) | 10-year 4.97% (+0.14 on the week) | 30-year 5.32% (+0.03 on the week)
Yield curve, 10-year minus 3-month: +1.01 points -- upward sloping (normal)
US dollar index: 100.11 (+1.34 on the week)
Volatility (VIX): 16.79 (+0.3 on the week) -- elevated
```

</details>

<details><summary><b>Price and chart</b> — score -0.35</summary>

```text
Last close 59.06 (bar of 2026-09-16), from 502 daily bars
Trend: vs 20d SMA 60.41 (-2.2%), 50d 59.66 (-1.0%), 200d 57.61 (+2.5%); 50d above 200d
Momentum: RSI(14) 39.5 | MACD -0.043 vs signal 0.208 (histogram -0.251)
Returns: 1d -0.3% | 5d -3.0% | 1m -2.2% | 3m -1.8%
52-week range: 52.42 - 61.44 (now 73.7% of the way up)
Volatility: ATR(14) 0.61 (1.0% of price) | annualised 20d 11.2%
Volume: 0.93x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.25</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score +0.25</summary>

```text
Fund type: Diversified Emerging Mkts
What it holds: P/E 16.50 | P/B 2.11 | P/S 1.85 | 3y earnings growth n/a
Yield: 2.3%
Three-year record: +17.0% a year | beta to the market 0.75
Cost and size: expense ratio 0.06% | net assets 168.36B
What it is made of: Stocks 95.5%, Cash 4.3%, Other 0.1%, Preferred 0.0%
Largest holdings: Taiwan Semiconductor Manufacturing Co Ltd 15.0%, Tencent Holdings Ltd 3.2%, Alibaba Group Holding Ltd Ordinary Shares 2.3%, MediaTek Inc 1.3%, China Construction Bank Corp Class H 0.9%
Sector mix: Technology 30.3%, Financial services 20.6%, Consumer cyclical 10.5%, Industrials 7.6%
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
Rolled up from the 5 largest holdings, 22.7% of the fund by weight  -- thin, so read this as a fact about that slice rather than the fund
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 1.34 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +41.2% above the current prices
Holdings read: 2330.TW, 0700.HK, 9988.HK, 2454.TW, 00939
Recent rating changes among them: none reported
```

</details>

<details><summary><b>Buying and selling by company insiders</b> — score +0.05</summary>

_Not available today._

</details>

<details><summary><b>Who is positioned how</b> — score +0.05</summary>

```text
Contract: MSCI EM INDEX (positions as of 2026-09-08, published the following Friday)
Large speculators: net long 4.2% of open interest (1,068,575 contracts)
Change on the week: +0.1% of open interest
Crowding: 55% percentile over 52 weeks -- within its normal range
Read this as crowding, not as a forecast: an extreme is as often the end of a move as the middle of one.
```

</details>

<details><summary><b>Money going into and out of this fund</b> — score +0.05</summary>

_Not available today._

</details>

### Farm goods basket (DBA) · Index fund — NEUTRAL, confidence 0.15

**In the model's own words:**

> DBA is positioned as an agricultural commodities fund but the holdings composition reveals it is predominantly a cash and short-duration Treasury vehicle (46.2% cash, 43.1% in short-term government bonds), with only 2% bonds and a stated 51.8% 'Other' category that likely reflects agricultural futures positions. Technicals show the fund near 52-week highs (82.8% of range), trading above its 50d and 200d SMAs with positive returns over 1m (+2.3%) and 3m (+8.0%), but momentum has rolled over slightly (MACD histogram negative at -0.064, RSI at 53.0 is neutral). Volume is well below average at 0.39x the 20d mean, indicating weak conviction behind the move. Macro conditions show Treasury yields rising across the curve this week (3m +16bp, 5y +21bp, 10y +14bp), a stronger US dollar (+1.34 on the week to 100.11), and VIX elevated at 16.79, which typically pressures commodities when the dollar strengthens and risk appetite wanes. The fund's heavy weighting to cash and short-term Treasuries (89.2% combined) and low expense ratio (0.85%) suggest it is being used as a defensive, liquidity-focused position rather than as a commodity exposure play. The lack of news, thin volume, and absence of fresh catalysts, combined with rising rates and dollar strength headwinds for commodities, argue against initiating or adding exposure. A neutral stance is warranted pending clearer directional conviction or a material change in the macro backdrop.

**Main reasons it gave:**
- Fund composition is 89.2% cash and short-term Treasuries, not commodity futures as ticker suggests
- MACD histogram rolled negative and volume 39% of average indicates weakening momentum
- US dollar index +1.34 on the week typically pressures agricultural commodities
- Treasury yields rising across curve this week with 5y +21bp suggests commodity headwinds

<details><summary><b>News</b> — score +0.00</summary>

_No news found for this one today._

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 3.96% (+0.16 on the week) | 5-year 4.83% (+0.21 on the week) | 10-year 4.97% (+0.14 on the week) | 30-year 5.32% (+0.03 on the week)
Yield curve, 10-year minus 3-month: +1.01 points -- upward sloping (normal)
US dollar index: 100.11 (+1.34 on the week)
Volatility (VIX): 16.79 (+0.3 on the week) -- elevated
```

</details>

<details><summary><b>Price and chart</b> — score +0.25</summary>

```text
Last close 28.80 (bar of 2026-09-16), from 502 daily bars
Trend: vs 20d SMA 28.86 (-0.2%), 50d 28.22 (+2.1%), 200d 27.02 (+6.6%); 50d above 200d
Momentum: RSI(14) 53.0 | MACD 0.253 vs signal 0.317 (histogram -0.064)
Returns: 1d -0.3% | 5d -0.7% | 1m +2.3% | 3m +8.0%
52-week range: 25.44 - 29.49 (now 82.8% of the way up)
Volatility: ATR(14) 0.29 (1.0% of price) | annualised 20d 11.9%
Volume: 0.39x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score -0.15</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score -0.15</summary>

```text
Fund type: Commodities Focused
What it holds: P/E n/a | P/B 0.00 | P/S 0.00 | 3y earnings growth n/a
Yield: 3.1%
Three-year record: +13.7% a year | beta to the market 0.35
Cost and size: expense ratio 0.85% | net assets 1.33B
What it is made of: Other 51.8%, Cash 46.2%, Bonds 2.0%
Largest holdings: Invesco Shrt-Trm Inv Gov&Agcy Instl 43.1%, Invesco Short Term Treasury ETF 4.4%
Sector mix: Healthcare 16.8%, Industrials 15.2%, Financial services 13.7%, Consumer cyclical 11.8%
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

_Not available today._

</details>

## Sector and country funds

### US house builders (XHB) · Sector or country — BEARISH, confidence 0.40

**Result:** ERROR · BrokerError: submit_order failed for XHB: {"code":42210000,"message":"asset \"XHB\" cannot be sold short"}

**In the model's own words:**

> Rate-sensitive housing basket facing a genuine macro headwind: yields rose across the curve this week (5y +21bp, 10y +14bp to 4.97%) alongside a stronger dollar, which is the single most direct driver of homebuilder and building-products earnings. The technical picture corroborates -- price 9.8% below the 200d SMA with 50d below 200d, MACD negative and widening, 1m -11%, and the fund sitting just 5.5% off its 52-week low. Fundamentals are not stretched (P/E 19.5) and the analyst roll-up on the top five names is constructive (+22% weighted target, 74% buys), but that covers only 20.9% of the fund and analyst targets lag rate shocks. Flows and positioning data absent, so no behavioural read. Modest conviction: this is a continuation call on a rate move rather than a fresh catalyst, and RSI 31.9 leaves bounce risk.

**Main reasons it gave:**
- 10y yield +14bp to 4.97% and 5y +21bp on the week, directly adverse for housing-linked equities
- Price 9.8% below 200d SMA, 50d below 200d, MACD histogram -0.52
- Trading 5.5% off the 52-week low after -11% in one month
- Dollar index +1.34 on the week, beta to market 1.46 amplifies macro drag
- Analyst roll-up bullish (+22.3% target) but covers only 20.9% of fund weight

<details><summary><b>News</b> — score +0.00</summary>

_No news found for this one today._

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 3.96% (+0.16 on the week) | 5-year 4.83% (+0.21 on the week) | 10-year 4.97% (+0.14 on the week) | 30-year 5.32% (+0.03 on the week)
Yield curve, 10-year minus 3-month: +1.01 points -- upward sloping (normal)
US dollar index: 100.11 (+1.34 on the week)
Volatility (VIX): 16.79 (+0.3 on the week) -- elevated
```

</details>

<details><summary><b>Price and chart</b> — score -0.65</summary>

```text
Last close 96.31 (bar of 2026-09-16), from 502 daily bars
Trend: vs 20d SMA 102.29 (-5.9%), 50d 105.66 (-8.9%), 200d 106.79 (-9.8%); 50d below 200d
Momentum: RSI(14) 31.9 | MACD -2.643 vs signal -2.119 (histogram -0.524)
Returns: 1d -1.5% | 5d -2.9% | 1m -11.0% | 3m -12.3%
52-week range: 94.86 - 121.36 (now 5.5% of the way up)
Volatility: ATR(14) 2.22 (2.3% of price) | annualised 20d 22.4%
Volume: 0.93x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score -0.10</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score -0.10</summary>

```text
Fund type: Consumer Cyclical
What it holds: P/E 19.52 | P/B 2.34 | P/S 1.36 | 3y earnings growth n/a
Yield: 0.8%
Three-year record: +7.6% a year | beta to the market 1.46
Cost and size: expense ratio 0.35% | net assets 1.33B
What it is made of: Stocks 100.0%, Cash 0.1%
Largest holdings: Installed Building Products Inc 4.4%, Owens-Corning Inc 4.3%, Allegion PLC 4.3%, Champion Homes Inc 4.1%, Williams-Sonoma Inc 3.9%
Sector mix: Consumer cyclical 60.7%, Industrials 37.9%, Real estate 1.5%
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
Rolled up from the 5 largest holdings, 20.9% of the fund by weight  -- thin, so read this as a fact about that slice rather than the fund
Ratings by weight: buy 73.8% | hold 26.2% | sell 0.0% (mean 2.22 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +22.3% above the current prices
Holdings read: IBP, OC, ALLE, SKY, WSM
Recent rating changes among them:
  - IBP: 2026-09-15 Stifel: init, ? -> Buy
  - OC: 2026-09-11 Wells Fargo: main, Overweight -> Overweight
  - ALLE: 2026-08-10 Morgan Stanley: main, Equal-Weight -> Equal-Weight
  - SKY: 2026-08-06 UBS: main, Buy -> Buy
  - WSM: 2026-09-09 Evercore ISI Group: main, In-Line -> In-Line
```

</details>

<details><summary><b>Buying and selling by company insiders</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>Who is positioned how</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>Money going into and out of this fund</b> — score n/a</summary>

_Not available today._

</details>

### Australia (EWA) · Sector or country — BEARISH, confidence 0.35

**Result:** ERROR · BrokerError: submit_order failed for EWA: {"code":42210000,"message":"asset \"EWA\" cannot be sold short"}

**In the model's own words:**

> Rates and FX moved against a commodity/bank-heavy Australia fund this week: 5y +21bp, 10y +14bp, dollar index +1.34, all of which pressure AUD-denominated equities on translation. Price broke below the 20d and 50d SMAs and is sitting near the 200d at 28.50 with MACD negative and volume 1.45x average, a decisive-looking break rather than drift. Analyst roll-up over 46% of the fund is unusually weighted (zero buys, 40% sells, mean 3.49) with a weighted target 5.4% BELOW spot, which is a rare negative read even allowing for the narrow coverage. Offsetting: RSI 32.5 is near oversold, 50d still above 200d, and there is no macro catalyst specific to Australia, so conviction stays modest rather than high. No fund flow or positioning data available, so insider dimension is left null.

**Main reasons it gave:**
- Analyst roll-up over 46.4% of fund: 0% buys, 40.4% sells, weighted target 5.4% below spot
- Close 28.34 below both 20d (29.76) and 50d (29.43) SMAs, resting on 200d at 28.50
- US dollar index +1.34 on the week and 5y yield +21bp, both headwinds for AUD-linked equities
- Volume 1.45x 20-day average on a -1.9% day, MACD histogram -0.204
- RSI 32.5 near oversold and 50d still above 200d, capping downside conviction

<details><summary><b>News</b> — score +0.00</summary>

_No news found for this one today._

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 3.96% (+0.16 on the week) | 5-year 4.83% (+0.21 on the week) | 10-year 4.97% (+0.14 on the week) | 30-year 5.32% (+0.03 on the week)
Yield curve, 10-year minus 3-month: +1.01 points -- upward sloping (normal)
US dollar index: 100.11 (+1.34 on the week)
Volatility (VIX): 16.79 (+0.3 on the week) -- elevated
```

</details>

<details><summary><b>Price and chart</b> — score -0.45</summary>

```text
Last close 28.34 (bar of 2026-09-16), from 502 daily bars
Trend: vs 20d SMA 29.76 (-4.8%), 50d 29.43 (-3.7%), 200d 28.50 (-0.5%); 50d above 200d
Momentum: RSI(14) 32.5 | MACD -0.189 vs signal 0.015 (histogram -0.204)
Returns: 1d -1.9% | 5d -4.3% | 1m -4.1% | 3m -2.2%
52-week range: 24.95 - 30.43 (now 62.0% of the way up)
Volatility: ATR(14) 0.35 (1.2% of price) | annualised 20d 16.3%
Volume: 1.45x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score -0.10</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score -0.10</summary>

```text
Fund type: Focused Region
What it holds: P/E 21.06 | P/B 2.81 | P/S 3.39 | 3y earnings growth n/a
Yield: 2.8%
Three-year record: +13.0% a year | beta to the market 0.96
Cost and size: expense ratio 0.50% | net assets 1.33B
What it is made of: Stocks 99.5%, Cash 0.5%
Largest holdings: BHP Group Ltd 16.3%, Commonwealth Bank of Australia 13.0%, National Australia Bank Ltd 5.9%, Westpac Banking Corp 5.7%, ANZ Group Holdings Ltd 5.5%
Sector mix: Financial services 41.1%, Basic materials 26.7%, Consumer cyclical 6.5%, Healthcare 5.2%
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

<details><summary><b>What analysts and big funds say</b> — score -0.50</summary>

_Not available today._

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score -0.50</summary>

```text
Rolled up from the 5 largest holdings, 46.4% of the fund by weight
Ratings by weight: buy 0.0% | hold 59.6% | sell 40.4% (mean 3.49 on a 1=strong buy to 5=strong sell scale)
Weighted price target: -5.4% above the current prices
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

_Not available today._

</details>

### Turkey (TUR) · Sector or country — BEARISH, confidence 0.35

**Result:** ERROR · BrokerError: submit_order failed for TUR: {"code":42210000,"message":"asset \"TUR\" cannot be sold short"}

**In the model's own words:**

> No macro news for Turkey in the window, but the tape shows a decisive break: -6.8% in one day on 3.45x average volume, -11.5% over five sessions, price 8-10% below the 20/50/200-day averages with MACD below signal. That is the kind of high-volume technical break this instrument's signal set can act on. The macro backdrop corroborates: US 5y +21bp and 10y +14bp on the week with the dollar index +1.34, a tightening-liquidity, strong-dollar mix that is historically hostile to a single-country EM equity fund. Offsets keep conviction modest: RSI 28.6 is oversold and prone to reflex bounces, valuation is cheap (P/E 13.8, P/B 1.21), and the holdings roll-up is unanimously buy-rated with +23% implied upside, though it covers only 39.5% of the fund and reflects lira-denominated local targets. Not a high-conviction macro catalyst, so sized as a lean.

**Main reasons it gave:**
- -6.8% single-day drop on 3.45x 20-day average volume
- Price 9.6% below 20d and 7.9% below 200d SMA; MACD histogram -0.347
- US 5y yield +21bp and dollar index +1.34 on the week, hostile to single-country EM
- Holdings P/E 13.81, P/B 1.21 and 2.1% yield limit downside case
- Analyst roll-up 100% buy with +23.1% target upside, but only 39.5% fund coverage

<details><summary><b>News</b> — score +0.00</summary>

_No news found for this one today._

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 3.96% (+0.16 on the week) | 5-year 4.83% (+0.21 on the week) | 10-year 4.97% (+0.14 on the week) | 30-year 5.32% (+0.03 on the week)
Yield curve, 10-year minus 3-month: +1.01 points -- upward sloping (normal)
US dollar index: 100.11 (+1.34 on the week)
Volatility (VIX): 16.79 (+0.3 on the week) -- elevated
```

</details>

<details><summary><b>Price and chart</b> — score -0.65</summary>

```text
Last close 36.10 (bar of 2026-09-16), from 502 daily bars
Trend: vs 20d SMA 39.95 (-9.6%), 50d 39.30 (-8.2%), 200d 39.21 (-7.9%); 50d above 200d
Momentum: RSI(14) 28.6 | MACD -0.232 vs signal 0.115 (histogram -0.347)
Returns: 1d -6.8% | 5d -11.5% | 1m -8.5% | 3m -10.5%
52-week range: 31.90 - 43.74 (now 35.4% of the way up)
Volatility: ATR(14) 0.75 (2.1% of price) | annualised 20d 32.8%
Volume: 3.45x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.20</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score +0.20</summary>

```text
Fund type: Focused Region
What it holds: P/E 13.81 | P/B 1.21 | P/S 0.66 | 3y earnings growth n/a
Yield: 2.1%
Three-year record: +3.5% a year | beta to the market 0.44
Cost and size: expense ratio 0.59% | net assets 225.08M
What it is made of: Stocks 100.4%, Cash -0.4%
Largest holdings: Aselsan Elektronik Sanayi Ve Ticaret AS 11.2%, Tupras-Turkiye Petrol Rafineleri AS 9.7%, Bim Birlesik Magazalar AS 8.7%, Akbank TAS 5.6%, Turk Hava Yollari AO 4.4%
Sector mix: Industrials 31.2%, Financial services 14.7%, Consumer defensive 11.9%, Basic materials 11.1%
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
Rolled up from the 5 largest holdings, 39.5% of the fund by weight
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 1.58 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +23.1% above the current prices
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

_Not available today._

</details>

### Biotech (XBI) · Sector or country — BEARISH, confidence 0.35

**Result:** ACCEPTED · 45 shares · submitted sell 45 XBI @ ~153.34, stop 161.15

**In the model's own words:**

> Yields jumped across the curve this week (5y +21bp, 10y +14bp) with the dollar up 1.34 and the market pricing a ~92% chance of a 25bp Fed hike -- a genuinely hostile backdrop for long-duration, cash-burning small-cap biotech. Technicals corroborate: price 5.5% below the 20d and 2.7% below the 50d, MACD crossed negative with a -1.6 histogram, RSI 39, five-day return -3.7% after a +13.4% three-month run. Offsetting this is an intact longer-term uptrend (50d>200d, +12% over 200d) and a still-mild VIX, so this is a pullback-within-uptrend call rather than a regime break. Analyst roll-up covers only 9% of the fund and carries a negative weighted target with two recent downgrades to Sell, which is a fact about that thin slice. Promotional headlines telling readers to 'stay bullish' are marketing, not evidence, and are discounted.

**Main reasons it gave:**
- 5-year yield +21bp and 10-year +14bp on the week; dollar index +1.34
- CME pricing ~92% odds of a 25bp hike to 3.75% -- rate-sensitive small-cap biotech most exposed
- Price 5.5% below 20d SMA, MACD histogram -1.623, RSI 38.9 after +13.4% 3-month run
- Analyst roll-up on 9% of fund weight shows -8.7% weighted target and recent MRNA/TWST Sell actions
- Longer-term uptrend intact (50d>200d, +12.2% vs 200d), capping bearish conviction

<details><summary><b>News</b> — score -0.15</summary>

- [Biotech Midweek Pulse: XBI Loses Steam After Hot 2026 Run — Here Are The Stocks And Catalysts To Watch Next](https://www.tradingview.com/news/stocktwits:ee8d9b8aa094b:0-biotech-midweek-pulse-xbi-loses-steam-after-hot-2026-run-here-are-the-stocks-and-catalysts-to-watch-next/)  
  <sub>TradingView, 17 hours ago</sub>  
  Biotech's 2026 rally cooled this week even as drug developers delivered major clinical updates. Definium Therapeutics (DFTX), Vera Therapeutics (VERA) and...
- [Our Biotech ETF Pick Is on a Roll. There’s Plenty of Reasons to Stay Bullish.](https://www.barrons.com/articles/spdr-biotech-etf-stock-pick-1a4560d9)  
  <sub>Barron's, 24 hours ago</sub>  
  Biotech stocks have been a bright spot in the market this year, and should continue to reward investors. Our State Street SPDR S&P Biotech ETF · XBI.
- [Dow, S&P 500, Nasdaq Futures Edge Higher Ahead Of Fed Rate Hike Expectations: CRCL, WING, CAVA, FPS Stocks In Focus](https://stocktwits.com/news-articles/markets/equity/dow-s-and-p-500-nasdaq-futures-edge-higher-ahead-of-fed-rate-hike-expectations-crcl-wing-cava-fps-stocks-in-focus/cZtYTESRB22)  
  <sub>Stocktwits, 17 hours ago</sub>  
  According to CME FedWatch data, there is a 92.4% probability that the Fed will hike interest rates by 25 basis points from the current 3.50% to 3.75%.
- [VanEck Pharmaceutical ETF vs VanEck Biotech ETF: Which Fund Is Better for Drug Innovation Profits?](https://finance.yahoo.com/healthcare/articles/vaneck-pharmaceutical-etf-vs-vaneck-230401900.html)  
  <sub>Yahoo Finance, 20 hours ago</sub>  
  PPH offers higher income and lower volatility, while BBH delivers stronger growth but with deeper drawdowns.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score -0.15</summary>

```text
US Treasury yields: 3-month 3.96% (+0.16 on the week) | 5-year 4.83% (+0.21 on the week) | 10-year 4.97% (+0.14 on the week) | 30-year 5.32% (+0.03 on the week)
Yield curve, 10-year minus 3-month: +1.01 points -- upward sloping (normal)
US dollar index: 100.11 (+1.34 on the week)
Volatility (VIX): 16.79 (+0.3 on the week) -- elevated
```

</details>

<details><summary><b>Price and chart</b> — score -0.45</summary>

```text
Last close 153.48 (bar of 2026-09-16), from 502 daily bars
Trend: vs 20d SMA 162.49 (-5.5%), 50d 157.80 (-2.7%), 200d 136.75 (+12.2%); 50d above 200d
Momentum: RSI(14) 38.9 | MACD -0.698 vs signal 0.925 (histogram -1.623)
Returns: 1d -0.4% | 5d -3.7% | 1m -3.8% | 3m +13.4%
52-week range: 93.74 - 169.55 (now 78.8% of the way up)
Volatility: ATR(14) 3.90 (2.5% of price) | annualised 20d 33.8%
Volume: 0.74x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score -0.10</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score -0.10</summary>

```text
Fund type: Health
What it holds: P/E n/a | P/B 0.20 | P/S 0.12 | 3y earnings growth n/a
Yield: 0.3%
Three-year record: +26.6% a year | beta to the market 1.12
Cost and size: expense ratio 0.35% | net assets 11.40B
What it is made of: Stocks 100.0%, Cash 0.0%
Largest holdings: Moderna Inc 2.8%, Twist Bioscience Corp 1.9%, Apogee Therapeutics Inc 1.5%, Kymera Therapeutics Inc Ordinary Shares 1.4%, Halozyme Therapeutics Inc 1.4%
Sector mix: Healthcare 99.3%, Financial services 0.7%
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

<details><summary><b>What analysts and big funds say</b> — score -0.30</summary>

_Not available today._

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score -0.30</summary>

```text
Rolled up from the 5 largest holdings, 9.0% of the fund by weight  -- thin, so read this as a fact about that slice rather than the fund
Ratings by weight: buy 52.0% | hold 48.0% | sell 0.0% (mean 2.18 on a 1=strong buy to 5=strong sell scale)
Weighted price target: -8.7% above the current prices
Holdings read: MRNA, TWST, APGE, KYMR, HALO
Recent rating changes among them:
  - MRNA: 2026-09-03 Rothschild & Co: down, Neutral -> Sell
  - TWST: 2026-09-09 BWS Financial: init, ? -> Sell
  - APGE: 2026-08-13 Truist Securities: main, Hold -> Hold
  - KYMR: 2026-09-14 B of A Securities: main, Buy -> Buy
  - HALO: 2026-09-02 HC Wainwright & Co.: reit, Buy -> Buy
```

</details>

<details><summary><b>Buying and selling by company insiders</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>Who is positioned how</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>Money going into and out of this fund</b> — score n/a</summary>

_Not available today._

</details>

### US shopping and leisure (XLY) · Sector or country — BEARISH, confidence 0.35

**Result:** ACCEPTED · 63 shares · submitted sell 63 XLY @ ~110.15, stop 113.36

**In the model's own words:**

> XLY is in a clear downtrend: below 20/50/200d SMAs, 50d below 200d, RSI 33.8, MACD negative and widening, near the lower quarter of its 52-week range. The macro backdrop corroborates: yields up across the curve this week (5y +21bp, 10y +14bp) and a dollar up 1.34 points, both headwinds for a high-beta (1.16), richly valued (P/E 25.5) cyclical sector heavily concentrated in AMZN and TSLA. Offsetting this is a bullish sell-side roll-up (100% buy by weight, +24.7% targets over 55% of the fund) and low-volume selling (0.64x average), which argues against conviction. No fresh policy or data surprise, so this is a trend-plus-rates call, not a catalyst call; sized modestly. News flow is generic sector roundups and a GuruFocus valuation piece, which I discount as noise.

**Main reasons it gave:**
- Price -4.6% vs 50d and -5.7% vs 200d SMA, 50d below 200d (death cross regime)
- RSI 33.8 and MACD -1.42 below signal, histogram still widening negative
- 5y yield +21bp and 10y +14bp on the week, dollar index +1.34 — headwind for rate-sensitive discretionary
- Holdings P/E 25.5 with beta 1.16; 41.7% of fund in AMZN+TSLA
- Analyst roll-up over 55% of fund is 100% buy with +24.7% weighted target — counterweight to the tape

<details><summary><b>News</b> — score -0.10</summary>

- [XLY Looks 4.8% Undervalued on GF Value™ as Pivot Points Signal K](https://www.gurufocus.com/news/9083935/xly-looks-48-undervalued-on-gf-value-as-pivot-points-signal-key-technical-levels)  
  <sub>GuruFocus, 6 hours ago</sub>  
  On September 16, 2026, the Consumer Discretionary Sector SPDR (ticker: XLY) established critical pivot points using the DeMark analysis methodology,...
- [Leading And Lagging Sectors For September 16, 2026](https://www.benzinga.com/etfs/sector-etfs/26/09/61814178/leading-and-lagging-sectors-september-16-2026)  
  <sub>Benzinga, 6 hours ago</sub>  
  Gainers Symbol Name Price Change ($) Change (%) Volume (NYSE:XLK) State Street Technology Select Sector SPDR ETF 184.7100 0.970 0.52 122.1K (NYSE:XLI) State...
- [Sector Update: Consumer Stocks Fall Late Afternoon](https://www.bitget.com/amp/news/detail/12560605838118)  
  <sub>Bitget, 19 hours ago</sub>  
  03:49 PM EDT, 09/15/2026 (MT Newswires) -- Consumer stocks fell late Tuesday afternoon with the State Street Consumer Staples Select Sector SPDR ETF (XLP) d...
- [Sector Update: Consumer](https://www.bitget.com/amp/news/detail/12560605837871)  
  <sub>Bitget, 22 hours ago</sub>  
  01:15 PM EDT, 09/15/2026 (MT Newswires) -- Consumer stocks fell Tuesday afternoon with the State Street Consumer Staples Select Sector SPDR ETF (XLP) droppi...
- [Sector Update: Consumer Stocks Fall Tuesday Afternoon](https://www.bitget.com/amp/news/detail/12560605837916)  
  <sub>Bitget, 18 hours ago</sub>  
  01:46 PM EDT, 09/15/2026 (MT Newswires) -- Consumer stocks fell Tuesday afternoon with the State Street Consumer Staples Select Sector SPDR ETF (XLP) droppi...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score -0.10</summary>

```text
US Treasury yields: 3-month 3.96% (+0.16 on the week) | 5-year 4.83% (+0.21 on the week) | 10-year 4.97% (+0.14 on the week) | 30-year 5.32% (+0.03 on the week)
Yield curve, 10-year minus 3-month: +1.01 points -- upward sloping (normal)
US dollar index: 100.11 (+1.34 on the week)
Volatility (VIX): 16.79 (+0.3 on the week) -- elevated
```

</details>

<details><summary><b>Price and chart</b> — score -0.60</summary>

```text
Last close 110.25 (bar of 2026-09-16), from 502 daily bars
Trend: vs 20d SMA 115.13 (-4.2%), 50d 115.57 (-4.6%), 200d 116.91 (-5.7%); 50d below 200d
Momentum: RSI(14) 33.8 | MACD -1.420 vs signal -0.833 (histogram -0.588)
Returns: 1d -0.6% | 5d -2.0% | 1m -5.6% | 3m -6.9%
52-week range: 105.66 - 124.52 (now 24.4% of the way up)
Volatility: ATR(14) 1.60 (1.5% of price) | annualised 20d 17.5%
Volume: 0.64x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score -0.20</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score -0.20</summary>

```text
Fund type: Consumer Cyclical
What it holds: P/E 25.48 | P/B 5.89 | P/S 2.51 | 3y earnings growth n/a
Yield: 0.8%
Three-year record: +9.8% a year | beta to the market 1.16
Cost and size: expense ratio 0.08% | net assets 22.75B
What it is made of: Stocks 99.9%, Cash 0.1%
Largest holdings: Amazon.com Inc 24.4%, Tesla Inc 17.3%, The Home Depot Inc 5.4%, McDonald's Corp 4.1%, Booking Holdings Inc 3.9%
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
Rolled up from the 5 largest holdings, 55.0% of the fund by weight
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 1.79 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +24.7% above the current prices
Holdings read: AMZN, TSLA, HD, MCD, BKNG
Recent rating changes among them:
  - AMZN: 2026-09-03 Wells Fargo: main, Overweight -> Overweight
  - TSLA: 2026-09-16 Goldman Sachs: reit, Neutral -> Neutral
  - HD: 2026-09-09 Bernstein: main, Market Perform -> Market Perform
  - MCD: 2026-09-16 BTIG: reit, Buy -> Buy
  - BKNG: 2026-09-01 Rosenblatt: init, ? -> Buy
```

</details>

<details><summary><b>Buying and selling by company insiders</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>Who is positioned how</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>Money going into and out of this fund</b> — score n/a</summary>

_Not available today._

</details>

### Poland (EPOL) · Sector or country — NEUTRAL, confidence 0.25

**In the model's own words:**

> EPOL is a Poland-focused equity fund with a 0.73 beta and a 43% three-year annualized return. The technical picture is mixed: the fund is up 13% from its 200-day MA and sits near its 52-week high (87.2% of range), but momentum has rolled over sharply with RSI at 47.4 and MACD histogram deeply negative (-0.128). Price is 1.5% below the 20-day MA and volume is sub-average. The fund held a 3-month gain of 8% but returned -3.5% in the past 5 days, signaling momentum exhaustion at resistance. Macro backdrop shows a modestly hawkish shift: Treasury yields across the curve rose 14-21 bps this week, the dollar strengthened 1.34%, and VIX ticked up slightly to 16.79. The yield curve remains normal at +1.01 points. Analyst coverage of the largest 47.4% of holdings is unanimously bullish (100% buy rated, mean 2.14, -1.8% upside target), but the upside is minimal and implies limited near-term repricing. Fund flows and positioning data are absent. The fund's 3.3% yield and 13.47 P/E offer modest valuation appeal, but the technical break below the 20-day MA on weak momentum after a sharp 5-day decline suggests near-term consolidation or pullback risk. Without a macro catalyst or fresh news to drive the next leg, and with technicals showing momentum divergence at elevated price levels, the risk-reward is balanced rather than directional.

**Main reasons it gave:**
- RSI 47.4 and MACD histogram -0.128 show momentum rollover despite near 52-week highs
- Price broke below 20-day MA on volume 0.66x average after 5-day -3.5% decline
- Analyst consensus unanimously bullish on top 47.4% but target only -1.8% upside
- Dollar strength and rising yields week-on-week create modest headwind for emerging market equity

<details><summary><b>News</b> — score +0.00</summary>

_No news found for this one today._

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 3.96% (+0.16 on the week) | 5-year 4.83% (+0.21 on the week) | 10-year 4.97% (+0.14 on the week) | 30-year 5.32% (+0.03 on the week)
Yield curve, 10-year minus 3-month: +1.01 points -- upward sloping (normal)
US dollar index: 100.11 (+1.34 on the week)
Volatility (VIX): 16.79 (+0.3 on the week) -- elevated
```

</details>

<details><summary><b>Price and chart</b> — score -0.35</summary>

```text
Last close 43.94 (bar of 2026-09-16), from 502 daily bars
Trend: vs 20d SMA 44.59 (-1.5%), 50d 43.14 (+1.9%), 200d 38.90 (+13.0%); 50d above 200d
Momentum: RSI(14) 47.4 | MACD 0.467 vs signal 0.595 (histogram -0.128)
Returns: 1d -2.1% | 5d -3.5% | 1m -0.0% | 3m +8.0%
52-week range: 31.57 - 45.76 (now 87.2% of the way up)
Volatility: ATR(14) 0.61 (1.4% of price) | annualised 20d 19.3%
Volume: 0.66x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.15</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score +0.15</summary>

```text
Fund type: Focused Region
What it holds: P/E 13.47 | P/B 2.00 | P/S 1.36 | 3y earnings growth n/a
Yield: 3.3%
Three-year record: +43.2% a year | beta to the market 0.73
Cost and size: expense ratio 0.59% | net assets 848.26M
What it is made of: Stocks 99.3%, Cash 0.7%
Largest holdings: PKO Bank Polski SA 15.4%, Orlen SA 13.8%, Bank Polska Kasa Opieki SA 7.1%, Powszechny Zaklad Ubezpieczen SA 6.4%, KGHM Polska Miedz SA 4.6%
Sector mix: Financial services 46.1%, Energy 14.5%, Consumer cyclical 12.7%, Basic materials 6.8%
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
Rolled up from the 5 largest holdings, 47.4% of the fund by weight
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 2.14 on a 1=strong buy to 5=strong sell scale)
Weighted price target: -1.8% above the current prices
Holdings read: PKO.WA, PKN.WA, PEO.WA, PZU.WA, KGH.WA
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

_Not available today._

</details>

### Canada (EWC) · Sector or country — NEUTRAL, confidence 0.25

**In the model's own words:**

> EWC is down 3.2% versus its 20-day moving average and 4.3% over one month, with RSI at 37 and MACD histogram deeply negative, signaling technical weakness. The macro backdrop shows a strengthening US dollar (+1.34 on the week), rising Treasury yields across the curve, and elevated volatility at 16.79, all headwinds for a Canadian equity fund. News of potential EU trade benefits and critical minerals positioning is speculative and affects only a subset of holdings. Analyst coverage of the top 28% of the fund shows 74% buy-rated positions with a +9.8% upside target, which is moderately constructive but does not offset the technical deterioration and macro headwinds. The fund's 0.79 beta and defensive financial sector weighting (39% of holdings) provide some cushion, but the confluence of negative momentum, currency weakness, and rising global rates creates more near-term risk than opportunity. The 52-week position at 75.5% of range and three-year +22% annualized record suggest valuation is not compelling on weakness.

**Main reasons it gave:**
- RSI 37 and MACD histogram -0.309 indicate momentum weakness
- US dollar +1.34 on week and Treasury yields rising across curve pressure CAD equities
- Analyst buy ratings at 74% with +9.8% target on top 28% holdings
- Price down 4.3% in one month while above 50d and 200d moving averages

<details><summary><b>News</b> — score +0.00</summary>

- [Trump's New Trade War Brought an Unexpected Ally to Canada](https://www.benzinga.com/news/politics/26/09/61815671/trumps-canada-trade-war-eu-etfs-stocks?utm_source=googlefinance)  
  <sub>Benzinga, 5 hours ago</sub>  
  Trump's trade war is pushing Canada toward the EU. Here are the ETFs and stocks tied to defense, uranium and critical minerals.
- [What would an EU associate membership mean for Canada as Brussels opens the door?](https://invezz.com/pk/news/2026/09/16/what-would-an-eu-associate-membership-mean-for-canada-as-brussels-opens-the-door/)  
  <sub>Invezz, 5 hours ago</sub>  
  The European Union is considering a new form of relationship with Canada that could make Ottawa the bloc's first associate member, marking a potentially...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 3.96% (+0.16 on the week) | 5-year 4.83% (+0.21 on the week) | 10-year 4.97% (+0.14 on the week) | 30-year 5.32% (+0.03 on the week)
Yield curve, 10-year minus 3-month: +1.01 points -- upward sloping (normal)
US dollar index: 100.11 (+1.34 on the week)
Volatility (VIX): 16.79 (+0.3 on the week) -- elevated
```

</details>

<details><summary><b>Price and chart</b> — score -0.45</summary>

```text
Last close 59.48 (bar of 2026-09-16), from 502 daily bars
Trend: vs 20d SMA 61.42 (-3.2%), 50d 60.55 (-1.8%), 200d 57.34 (+3.7%); 50d above 200d
Momentum: RSI(14) 37.2 | MACD -0.176 vs signal 0.133 (histogram -0.309)
Returns: 1d -1.3% | 5d -2.5% | 1m -4.3% | 3m +0.6%
52-week range: 49.72 - 62.64 (now 75.5% of the way up)
Volatility: ATR(14) 0.69 (1.2% of price) | annualised 20d 14.1%
Volume: 1.13x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.15</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score +0.15</summary>

```text
Fund type: Focused Region
What it holds: P/E 19.49 | P/B 2.83 | P/S 2.79 | 3y earnings growth n/a
Yield: 1.2%
Three-year record: +22.0% a year | beta to the market 0.79
Cost and size: expense ratio 0.50% | net assets 6.85B
What it is made of: Stocks 99.8%, Cash 0.2%
Largest holdings: Royal Bank of Canada 9.0%, The Toronto-Dominion Bank 6.3%, Shopify Inc Registered Shs -A- Subord Vtg 5.7%, Bank of Montreal 3.7%, Bank of Nova Scotia 3.6%
Sector mix: Financial services 39.2%, Energy 17.9%, Basic materials 16.1%, Industrials 8.8%
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
Rolled up from the 5 largest holdings, 28.3% of the fund by weight
Ratings by weight: buy 74.3% | hold 25.7% | sell 0.0% (mean 2.20 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +9.8% above the current prices
Holdings read: RY, TD, SHOP, BMO.TO, BNS.TO
Recent rating changes among them:
  - RY: 2025-08-29 Argus Research: main, Buy -> Buy
  - TD: 2026-06-01 RBC Capital: main, Outperform -> Outperform
  - SHOP: 2026-09-11 Bernstein: init, ? -> Outperform
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

_Not available today._

</details>

### Sweden (EWD) · Sector or country — NEUTRAL, confidence 0.25

**In the model's own words:**

> EWD (Sweden, primarily industrials) faces mixed signals. Technicals show a downtrend with the price 3.6% below its 20-day MA, weak momentum (RSI 36.3, MACD negative), and recent losses across all timeframes. The fund is near the bottom of its 52-week range. However, the damage is moderate rather than severe: the longer-term trend remains intact (50d above 200d), the 3-month return is flat, and volatility at 15.4% annualized is not elevated. Macro headwinds are present—US Treasury yields rose across the curve, the dollar strengthened (+1.34 on the week), and VIX ticked higher—but these are incremental moves, not shocks. The fund's valuation is reasonable (P/E 14.99, yield 3.4%), and analyst coverage of its four largest holdings (29.5% of the fund) shows 82% buy ratings with an 8.5% upside target, suggesting underlying fundamentals are not negative. The absence of news and the modest technical deterioration argue against conviction in either direction. This is a modest pullback in a higher-beta regional fund during a week of modest yield and dollar moves, not a catalyst for a directional call.

**Main reasons it gave:**
- Price 3.6% below 20d MA with negative MACD and RSI 36.3
- US yields +10-21bp, dollar +1.34 on week, modest macro headwinds
- Analyst consensus 82% buy with +8.5% target on largest 29.5% of holdings
- 3-month return flat, 50d MA above 200d, intermediate trend intact

<details><summary><b>News</b> — score +0.00</summary>

_No news found for this one today._

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 3.96% (+0.16 on the week) | 5-year 4.83% (+0.21 on the week) | 10-year 4.97% (+0.14 on the week) | 30-year 5.32% (+0.03 on the week)
Yield curve, 10-year minus 3-month: +1.01 points -- upward sloping (normal)
US dollar index: 100.11 (+1.34 on the week)
Volatility (VIX): 16.79 (+0.3 on the week) -- elevated
```

</details>

<details><summary><b>Price and chart</b> — score -0.35</summary>

```text
Last close 50.91 (bar of 2026-09-16), from 502 daily bars
Trend: vs 20d SMA 52.82 (-3.6%), 50d 52.03 (-2.2%), 200d 51.24 (-0.6%); 50d above 200d
Momentum: RSI(14) 36.3 | MACD -0.282 vs signal 0.036 (histogram -0.318)
Returns: 1d -0.7% | 5d -2.8% | 1m -3.0% | 3m +0.1%
52-week range: 45.38 - 54.72 (now 59.2% of the way up)
Volatility: ATR(14) 0.63 (1.2% of price) | annualised 20d 15.4%
Volume: 1.35x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.15</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score +0.15</summary>

```text
Fund type: Focused Region
What it holds: P/E 14.99 | P/B 2.88 | P/S 2.90 | 3y earnings growth n/a
Yield: 3.4%
Three-year record: +20.0% a year | beta to the market 1.19
Cost and size: expense ratio 0.51% | net assets 755.74M
What it is made of: Stocks 98.9%, Cash 1.1%
Largest holdings: Spotify Technology SA 10.2%, Investor AB Class B 9.5%, Volvo AB Class B 7.1%, Atlas Copco AB Class A 6.9%, Sandvik AB 5.3%
Sector mix: Industrials 46.0%, Financial services 24.9%, Communication services 13.9%, Technology 6.2%
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
Rolled up from the 4 largest holdings, 29.5% of the fund by weight
Ratings by weight: buy 82.1% | hold 17.9% | sell 0.0% (mean 1.97 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +8.5% above the current prices
Holdings read: SPOT, VOLV-B.ST, ATCO-A.ST, SAND.ST
Recent rating changes among them:
  - SPOT: 2026-08-13 Argus Research: reit, Buy -> Buy
```

</details>

<details><summary><b>Buying and selling by company insiders</b> — score +0.00</summary>

_Not available today._

</details>

<details><summary><b>Who is positioned how</b> — score +0.00</summary>

_Not available today._

</details>

<details><summary><b>Money going into and out of this fund</b> — score +0.00</summary>

_Not available today._

</details>

### Germany (EWG) · Sector or country — NEUTRAL, confidence 0.25

**In the model's own words:**

> EWG (iShares MSCI Germany ETF) shows a technically challenged picture with price below all major moving averages, RSI at 36 indicating oversold conditions, and negative MACD histogram, but conviction remains low because technicals alone do not drive a macro timing call on a regional equity fund. The macro backdrop has shifted modestly negative this week: US yields have risen across the curve (notably +21bp in 5-year), the dollar has strengthened (+1.34 to 100.11), and VIX remains elevated at 16.79, all headwinds for a euro-denominated fund when translated. Fund basics show modest valuation (P/E 18.4, P/B 1.94) with a 1.9% yield, and the three-year record of +18.5% annualized is solid. Analyst coverage of the top 5 holdings (45.5% of fund weight) tilts constructively with 78% buy-rated and a +16.4% weighted price target, but this is thin coverage and does not override the technical deterioration and macro headwinds. The fund has underperformed over the past month (-3.8%) and volume is below average, suggesting low conviction in either direction. No major catalyst or data surprise has occurred. A mild bearish lean is warranted on yield curve steepening, dollar strength, and technical breakdown, but the size of the move does not justify high conviction.

**Main reasons it gave:**
- US yields rose sharply across curve this week, particularly 5-year +21bp, headwind for euro assets
- Dollar strengthened +1.34 to 100.11, directional drag on translated returns
- Price below all three major moving averages (20d, 50d, 200d) with RSI 36 and negative MACD histogram
- Analyst consensus on top 45% of holdings shows +16.4% weighted price target but thin coverage
- Volume 0.60x 20-day average suggests low conviction and reduced participation

<details><summary><b>News</b> — score +0.00</summary>

_No news found for this one today._

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 3.96% (+0.16 on the week) | 5-year 4.83% (+0.21 on the week) | 10-year 4.97% (+0.14 on the week) | 30-year 5.32% (+0.03 on the week)
Yield curve, 10-year minus 3-month: +1.01 points -- upward sloping (normal)
US dollar index: 100.11 (+1.34 on the week)
Volatility (VIX): 16.79 (+0.3 on the week) -- elevated
```

</details>

<details><summary><b>Price and chart</b> — score -0.35</summary>

```text
Last close 42.30 (bar of 2026-09-16), from 502 daily bars
Trend: vs 20d SMA 43.64 (-3.1%), 50d 42.92 (-1.5%), 200d 42.35 (-0.1%); 50d above 200d
Momentum: RSI(14) 36.1 | MACD -0.199 vs signal 0.043 (histogram -0.241)
Returns: 1d -0.5% | 5d -1.7% | 1m -3.8% | 3m +1.3%
52-week range: 38.08 - 44.59 (now 64.8% of the way up)
Volatility: ATR(14) 0.41 (1.0% of price) | annualised 20d 11.7%
Volume: 0.60x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.05</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score +0.05</summary>

```text
Fund type: Focused Region
What it holds: P/E 18.40 | P/B 1.94 | P/S 1.28 | 3y earnings growth n/a
Yield: 1.9%
Three-year record: +18.5% a year | beta to the market 0.98
Cost and size: expense ratio 0.49% | net assets 1.82B
What it is made of: Stocks 99.8%, Cash 0.2%
Largest holdings: Siemens AG 12.1%, SAP SE 11.3%, Allianz SE 10.0%, Siemens Energy AG Ordinary Shares 6.4%, Deutsche Telekom AG 5.6%
Sector mix: Industrials 28.7%, Financial services 23.2%, Technology 15.9%, Consumer cyclical 7.4%
```

</details>

<details><summary><b>Does this company beat its own forecasts</b> — score +0.05</summary>

_Not available today._

</details>

<details><summary><b>What holding this fund costs you</b> — score +0.05</summary>

_Not available today._

</details>

<details><summary><b>How much oil and gas is in storage</b> — score +0.05</summary>

_Not available today._

</details>

<details><summary><b>How the crop is growing</b> — score +0.05</summary>

_Not available today._

</details>

<details><summary><b>What analysts and big funds say</b> — score +0.25</summary>

_Not available today._

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score +0.25</summary>

```text
Rolled up from the 5 largest holdings, 45.5% of the fund by weight
Ratings by weight: buy 78.0% | hold 22.0% | sell 0.0% (mean 1.83 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +16.4% above the current prices
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

_Not available today._

</details>

### Japan (EWJ) · Sector or country — NEUTRAL, confidence 0.25

**In the model's own words:**

> EWJ trades near the upper end of its 52-week range with momentum fading: RSI at 51.8 and MACD histogram negative despite a positive trend structure. The fund is up 7.9% against its 200-day moving average, leaving limited room for continued momentum. News flow is mixed—one headline on Taiwan supply risk to semiconductors is idiosyncratic noise affecting only a portion of the portfolio (Tokyo Electron and Advantest are 5.9% combined), while broader Asian market strength is priced in. The macro backdrop is neutral to slightly headwind: US Treasury yields rose across the curve this week, the dollar strengthened +1.34 points, and volatility ticked higher to 16.79. Japan's P/E of 19.11 and P/B of 2.01 are not cheap. Analyst coverage on the top 5 holdings (17% of fund) shows buy-only ratings and +21% price targets, but this thin roll-up captures only a slice. CFTC positioning in the Nikkei is at the 30th percentile with minimal weekly change—speculators are neither crowded long nor fleeing. Fund fundamentals show a solid 3.7% yield and three-year returns of +18.9% annually, but technicals lack conviction and volume is subpar. The primary consideration is valuation after a strong run; macro yields rising slightly headwind near-term entry. No data surprise or policy catalyst is present to shift bias materially.

**Main reasons it gave:**
- Momentum fading with RSI 51.8 and negative MACD histogram at near 52-week highs
- US Treasury yields rising across curve and dollar +1.34% this week; modest headwind for yen-based assets
- Analyst coverage thin (17% of fund) with buy-only ratings; price target +21% on largest holdings but not fund-wide
- Taiwan supply risk headline affects semiconductor slice (5.9% of fund) but is idiosyncratic, not macro signal
- CFTC positioning at 30th percentile, normal range, with minimal weekly change

<details><summary><b>News</b> — score +0.10</summary>

- [Elon Musk Flags Taiwan as AI’s Weak Link. These Semiconductor ETFs Could Offer a Hedge](https://www.tradingview.com/news/benzinga:8d51fc1c5094b:0)  
  <sub>TradingView, 23 hours ago</sub>  
  Speaking at the All-In Summit, Elon Musk warned that existing fabs are running at full capacity and that a disruption in Taiwan could compound supply...
- [Asian markets advance ahead of Fed decision (FXI:NYSEARCA)](https://seekingalpha.com/news/4643213-asian-markets-advance-ahead-of-fed-decision)  
  <sub>Seeking Alpha, 14 hours ago</sub>  
  Asian markets were mostly higher on Wednesday, with Japan, China, Hong Kong, India and Australia all gaining, as investors looked ahead to the Federal...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.10</summary>

```text
US Treasury yields: 3-month 3.96% (+0.16 on the week) | 5-year 4.83% (+0.21 on the week) | 10-year 4.97% (+0.14 on the week) | 30-year 5.32% (+0.03 on the week)
Yield curve, 10-year minus 3-month: +1.01 points -- upward sloping (normal)
US dollar index: 100.11 (+1.34 on the week)
Volatility (VIX): 16.79 (+0.3 on the week) -- elevated
```

</details>

<details><summary><b>Price and chart</b> — score -0.15</summary>

```text
Last close 96.62 (bar of 2026-09-16), from 502 daily bars
Trend: vs 20d SMA 96.31 (+0.3%), 50d 94.77 (+2.0%), 200d 89.55 (+7.9%); 50d above 200d
Momentum: RSI(14) 51.8 | MACD 0.661 vs signal 0.729 (histogram -0.068)
Returns: 1d -0.3% | 5d -0.4% | 1m -1.6% | 3m +2.7%
52-week range: 78.36 - 98.56 (now 90.4% of the way up)
Volatility: ATR(14) 1.32 (1.4% of price) | annualised 20d 14.3%
Volume: 0.51x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.05</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score +0.05</summary>

```text
Fund type: Japan Stock
What it holds: P/E 19.11 | P/B 2.01 | P/S 1.68 | 3y earnings growth n/a
Yield: 3.7%
Three-year record: +18.9% a year | beta to the market 0.86
Cost and size: expense ratio 0.49% | net assets 22.69B
What it is made of: Stocks 99.8%, Cash 0.2%
Largest holdings: Mitsubishi UFJ Financial Group Inc 4.6%, Toyota Motor Corp 3.5%, Sumitomo Mitsui Financial Group Inc 3.0%, Tokyo Electron Ltd 3.0%, Advantest Corp 2.9%
Sector mix: Industrials 22.9%, Technology 21.5%, Financial services 19.1%, Consumer cyclical 11.6%
```

</details>

<details><summary><b>Does this company beat its own forecasts</b> — score +0.05</summary>

_Not available today._

</details>

<details><summary><b>What holding this fund costs you</b> — score +0.05</summary>

_Not available today._

</details>

<details><summary><b>How much oil and gas is in storage</b> — score +0.05</summary>

_Not available today._

</details>

<details><summary><b>How the crop is growing</b> — score +0.05</summary>

_Not available today._

</details>

<details><summary><b>What analysts and big funds say</b> — score +0.40</summary>

_Not available today._

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score +0.40</summary>

```text
Rolled up from the 5 largest holdings, 17.0% of the fund by weight  -- thin, so read this as a fact about that slice rather than the fund
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 1.68 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +21.0% above the current prices
Holdings read: 8306.T, 7203.T, 8316.T, 8035.T, 6857.T
Recent rating changes among them: none reported
```

</details>

<details><summary><b>Buying and selling by company insiders</b> — score -0.05</summary>

_Not available today._

</details>

<details><summary><b>Who is positioned how</b> — score -0.05</summary>

```text
Contract: NIKKEI STOCK AVERAGE (positions as of 2026-09-08, published the following Friday)
Large speculators: net long 2.7% of open interest (42,440 contracts)
Change on the week: +0.5% of open interest
Crowding: 30% percentile over 52 weeks -- within its normal range
Read this as crowding, not as a forecast: an extreme is as often the end of a move as the middle of one.
```

</details>

<details><summary><b>Money going into and out of this fund</b> — score -0.05</summary>

_Not available today._

</details>

### Switzerland (EWL) · Sector or country — NEUTRAL, confidence 0.25

**In the model's own words:**

> EWL is a Swiss-focused equity fund holding large-cap, defensive names with heavy exposure to healthcare (37.5%) and financials (20.6%). The technical picture shows clear weakness: price is 4.3-4.8% below key moving averages, RSI at 30.5 signals oversold conditions, MACD histogram is negative, and recent returns are down across all timeframes (1m -4.9%). This has created a technical setup where oversold readings normally precede bounces. Macro backdrop provides a modest tailwind: the curve is normal (10y-3m spread +101bp) and USD strength (+1.34 on the week) should benefit Swiss exporters when translated to local currency, though rising yields (+14-21bp across the curve) may pressure valuations. Fund flows and positioning data are absent, limiting conviction on mean reversion. Analyst view of the top 48.5% holdings is moderately constructive (74.5% buy-rated, +10.1% target) but does not overcome technical oversold conditions or the macro headwind of higher rates. Volume is below average (0.67x), suggesting limited conviction in either direction. The fund's valuation (P/E 24.65, P/B 4.25) is elevated, making it vulnerable to further multiple compression if macro conditions deteriorate. A bounce from oversold levels is plausible near-term, but no clear catalyst or macro surprise justifies conviction above neutral.

**Main reasons it gave:**
- RSI 30.5 and price 4-5% below 20d/50d moving averages signal oversold bounce opportunity
- Analyst target +10.1% on 48.5% of holdings, 74.5% buy-rated
- US dollar strength week-over-week favors Swiss exporters in local currency terms
- Treasury curve normal at +101bp, but yields up 14-21bp across the curve pressure valuations
- Below-average volume limits conviction on directional move from oversold levels

<details><summary><b>News</b> — score +0.00</summary>

_No news found for this one today._

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 3.96% (+0.16 on the week) | 5-year 4.83% (+0.21 on the week) | 10-year 4.97% (+0.14 on the week) | 30-year 5.32% (+0.03 on the week)
Yield curve, 10-year minus 3-month: +1.01 points -- upward sloping (normal)
US dollar index: 100.11 (+1.34 on the week)
Volatility (VIX): 16.79 (+0.3 on the week) -- elevated
```

</details>

<details><summary><b>Price and chart</b> — score -0.55</summary>

```text
Last close 59.86 (bar of 2026-09-16), from 502 daily bars
Trend: vs 20d SMA 62.56 (-4.3%), 50d 62.90 (-4.8%), 200d 61.50 (-2.7%); 50d above 200d
Momentum: RSI(14) 30.5 | MACD -0.872 vs signal -0.517 (histogram -0.356)
Returns: 1d -0.6% | 5d -1.5% | 1m -4.9% | 3m -3.3%
52-week range: 53.86 - 65.08 (now 53.5% of the way up)
Volatility: ATR(14) 0.69 (1.2% of price) | annualised 20d 16.5%
Volume: 0.67x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.15</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score +0.15</summary>

```text
Fund type: Focused Region
What it holds: P/E 24.65 | P/B 4.25 | P/S 2.78 | 3y earnings growth n/a
Yield: 1.7%
Three-year record: +12.1% a year | beta to the market 0.91
Cost and size: expense ratio 0.50% | net assets 2.42B
What it is made of: Stocks 99.0%, Cash 1.0%
Largest holdings: Roche Holding AG Ordinary Shares new 13.6%, Novartis AG Registered Shares 12.4%, Nestle SA 11.1%, UBS Group AG Registered Shares 6.8%, Compagnie Financiere Richemont SA Class A 4.6%
Sector mix: Healthcare 37.5%, Financial services 20.6%, Consumer defensive 13.3%, Industrials 11.8%
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
Rolled up from the 5 largest holdings, 48.5% of the fund by weight
Ratings by weight: buy 74.5% | hold 25.5% | sell 0.0% (mean 2.40 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +10.1% above the current prices
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

_Not available today._

</details>

### Netherlands (EWN) · Sector or country — NEUTRAL, confidence 0.25

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Netherlands fund is in a short-term pullback: price 3.4% below both the 20d and 50d SMAs, RSI 35.9, MACD negative and widening, -7.8% over a month, though the 50d remains above the 200d and price sits 3.4% above the 200d, so the longer uptrend is intact. Macro is the bigger fact this week: yields up across the curve (5y +21bp, 10y +14bp) and the dollar up 1.34 points, which is a headwind for a euro-denominated, 31% technology, high-duration-growth basket concentrated in ASML (21.8%). That is a real but not decisive impulse, and volume is 0.09x average, so the tape is thin and uninformative. Analyst roll-up covers only 44% of the fund and is 100% buy with a +38.6% weighted target, which is optimistic but structurally so and not a timing signal. No fund-level news and no positioning or flow data. Prior is that I cannot time this; NEUTRAL with a mild bearish tilt.

**Main reasons it gave:**
- Price -3.4% vs 20d and -3.3% vs 50d SMA, RSI 35.9, MACD histogram -0.337
- US yields up across curve (5y +21bp, 10y +14bp) and DXY +1.34 on the week, headwind for euro tech-heavy basket
- 50d still above 200d and price +3.4% over 200d - longer trend not broken
- Analyst roll-up 100% buy with +38.6% target but covers only 44.1% of fund
- Volume 0.09x 20-day average - move lacks confirmation

<details><summary><b>News</b> — score +0.00</summary>

_No news found for this one today._

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 3.96% (+0.16 on the week) | 5-year 4.83% (+0.21 on the week) | 10-year 4.97% (+0.14 on the week) | 30-year 5.32% (+0.03 on the week)
Yield curve, 10-year minus 3-month: +1.01 points -- upward sloping (normal)
US dollar index: 100.11 (+1.34 on the week)
Volatility (VIX): 16.79 (+0.3 on the week) -- elevated
```

</details>

<details><summary><b>Price and chart</b> — score -0.35</summary>

```text
Last close 65.93 (bar of 2026-09-16), from 502 daily bars
Trend: vs 20d SMA 68.28 (-3.4%), 50d 68.20 (-3.3%), 200d 63.78 (+3.4%); 50d above 200d
Momentum: RSI(14) 35.9 | MACD -0.540 vs signal -0.203 (histogram -0.337)
Returns: 1d -0.6% | 5d -3.7% | 1m -7.8% | 3m -4.6%
52-week range: 55.33 - 71.61 (now 65.1% of the way up)
Volatility: ATR(14) 0.91 (1.4% of price) | annualised 20d 13.5%
Volume: 0.09x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.05</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score +0.05</summary>

```text
Fund type: Focused Region
What it holds: P/E 18.97 | P/B 2.54 | P/S 1.84 | 3y earnings growth n/a
Yield: 4.1%
Three-year record: +22.3% a year | beta to the market 1.14
Cost and size: expense ratio 0.50% | net assets 626.66M
What it is made of: Stocks 99.8%, Cash 0.2%
Largest holdings: ASML Holding NV 21.8%, ING Groep NV 9.0%, Prosus NV Ordinary Shares - Class N 5.1%, Nebius Group NV Shs Class-A- 4.3%, ASM International NV 4.0%
Sector mix: Technology 31.5%, Financial services 21.4%, Industrials 10.8%, Consumer defensive 10.7%
```

</details>

<details><summary><b>Does this company beat its own forecasts</b> — score +0.05</summary>

_Not available today._

</details>

<details><summary><b>What holding this fund costs you</b> — score +0.05</summary>

_Not available today._

</details>

<details><summary><b>How much oil and gas is in storage</b> — score +0.05</summary>

_Not available today._

</details>

<details><summary><b>How the crop is growing</b> — score +0.05</summary>

_Not available today._

</details>

<details><summary><b>What analysts and big funds say</b> — score +0.30</summary>

_Not available today._

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score +0.30</summary>

```text
Rolled up from the 5 largest holdings, 44.1% of the fund by weight
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 1.61 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +38.6% above the current prices
Holdings read: ASML.AS, INGA.AS, PRX.AS, NBIS, ASM.AS
Recent rating changes among them:
  - NBIS: 2026-09-09 Truist Securities: init, ? -> Buy
```

</details>

<details><summary><b>Buying and selling by company insiders</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>Who is positioned how</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>Money going into and out of this fund</b> — score n/a</summary>

_Not available today._

</details>

### Spain (EWP) · Sector or country — NEUTRAL, confidence 0.25

**In the model's own words:**

> EWP (iShares MSCI Spain ETF) holds a concentrated portfolio of Spanish banks and utilities. The technical picture is mixed: the fund is down 2.6% from its 20-day moving average and trades below both the 20d and 50d SMAs, with RSI at 39.6 and a negative MACD histogram signaling bearish momentum. Volume is weak at 0.32x average, which undercuts any directional conviction. The fund sits near the top of its 52-week range (82.1%), which historically presents resistance. On the macro front, Treasury yields have risen meaningfully this week (3m +16bp, 5y +21bp, 10y +14bp) while the dollar has strengthened (+1.34 on the week to 100.11), both headwinds for a regional equity fund. Spanish valuations are reasonable (P/E 16.28, yield 2.7%) and analyst consensus on the largest holdings is modestly bullish (+2.0% price target), but the fund's heaviness in financial services (45.4%) and utilities (20.0%) leaves it exposed to rising rates. Recent rate moves and dollar strength argue for caution. The lack of any catalyst, combined with weak technicals and only modest analyst support, does not justify a directional lean.

**Main reasons it gave:**
- RSI 39.6 and negative MACD histogram indicate weakening momentum
- Closing below 20d and 50d SMAs with low volume suggests lack of conviction
- Treasury yields +14-21bp this week and dollar +1.34 are headwinds for regional equity
- Analyst price target of +2.0% on largest 54% of fund provides modest support only
- Fund near 52-week high (82.1%) with no fresh catalysts identified

<details><summary><b>News</b> — score +0.00</summary>

_No news found for this one today._

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 3.96% (+0.16 on the week) | 5-year 4.83% (+0.21 on the week) | 10-year 4.97% (+0.14 on the week) | 30-year 5.32% (+0.03 on the week)
Yield curve, 10-year minus 3-month: +1.01 points -- upward sloping (normal)
US dollar index: 100.11 (+1.34 on the week)
Volatility (VIX): 16.79 (+0.3 on the week) -- elevated
```

</details>

<details><summary><b>Price and chart</b> — score -0.35</summary>

```text
Last close 60.55 (bar of 2026-09-16), from 502 daily bars
Trend: vs 20d SMA 62.14 (-2.6%), 50d 61.32 (-1.3%), 200d 57.13 (+6.0%); 50d above 200d
Momentum: RSI(14) 39.6 | MACD -0.134 vs signal 0.135 (histogram -0.269)
Returns: 1d -0.9% | 5d -1.7% | 1m -3.0% | 3m +2.9%
52-week range: 48.25 - 63.23 (now 82.1% of the way up)
Volatility: ATR(14) 0.72 (1.2% of price) | annualised 20d 13.1%
Volume: 0.32x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.00</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score +0.00</summary>

```text
Fund type: Focused Region
What it holds: P/E 16.28 | P/B 2.22 | P/S 1.82 | 3y earnings growth n/a
Yield: 2.7%
Three-year record: +33.7% a year | beta to the market 0.87
Cost and size: expense ratio 0.50% | net assets 2.26B
What it is made of: Stocks 99.7%, Cash 0.3%
Largest holdings: Banco Santander SA 19.2%, Banco Bilbao Vizcaya Argentaria SA 14.0%, Iberdrola SA 12.1%, CaixaBank SA 4.6%, Industria De Diseno Textil SA Share From Split 4.4%
Sector mix: Financial services 45.4%, Utilities 20.0%, Industrials 14.4%, Technology 5.9%
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
Rolled up from the 5 largest holdings, 54.5% of the fund by weight
Ratings by weight: buy 52.0% | hold 48.0% | sell 0.0% (mean 2.20 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +2.0% above the current prices
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

_Not available today._

</details>

### United Kingdom (EWU) · Sector or country — NEUTRAL, confidence 0.25

**In the model's own words:**

> EWU is a focused UK equity fund trading near technical support with mixed signals. The technicals show momentum weakness (RSI 37.7, MACD negative, price below 20d/50d SMAs) offset by a structurally normal uptrend (50d above 200d, +1.8% above 200d SMA). The macro backdrop is headwinds: US yields rose 14-21bps across the curve this week, the dollar strengthened +1.34%, and volatility sits at elevated levels (VIX 16.79). These move against UK-focused equities. The fund's valuations are moderate (P/E 17.08, P/B 2.29) and analyst consensus on the five largest holdings (36% of weight) is evenly split between buy and hold with a +12.5% price target, suggesting fair value but no catalyst. Fund flows and positioning data are absent, limiting conviction. The three-year 18.2% annual return and 3.1% yield provide some defensive merit, but absent a rate surprise or technical reversal, the near-term setup is ambiguous. Low volume (0.61x average) suggests indecision rather than conviction in either direction.

**Main reasons it gave:**
- RSI 37.7 with negative MACD histogram signals momentum loss
- Price 2.2% below 20-day SMA and 1.3% below 50-day SMA
- US yields +14-21bps on the week, dollar +1.34%, headwinds for UK assets
- Analyst consensus +12.5% target on largest holdings lacks near-term catalyst
- Low volume 0.61x average indicates market indecision

<details><summary><b>News</b> — score +0.00</summary>

_No news found for this one today._

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 3.96% (+0.16 on the week) | 5-year 4.83% (+0.21 on the week) | 10-year 4.97% (+0.14 on the week) | 30-year 5.32% (+0.03 on the week)
Yield curve, 10-year minus 3-month: +1.01 points -- upward sloping (normal)
US dollar index: 100.11 (+1.34 on the week)
Volatility (VIX): 16.79 (+0.3 on the week) -- elevated
```

</details>

<details><summary><b>Price and chart</b> — score -0.35</summary>

```text
Last close 47.29 (bar of 2026-09-16), from 502 daily bars
Trend: vs 20d SMA 48.36 (-2.2%), 50d 47.89 (-1.3%), 200d 46.45 (+1.8%); 50d above 200d
Momentum: RSI(14) 37.7 | MACD -0.113 vs signal 0.045 (histogram -0.158)
Returns: 1d -1.1% | 5d -1.1% | 1m -1.8% | 3m +1.7%
52-week range: 41.04 - 49.39 (now 74.9% of the way up)
Volatility: ATR(14) 0.42 (0.9% of price) | annualised 20d 10.3%
Volume: 0.61x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.15</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score +0.15</summary>

```text
Fund type: Focused Region
What it holds: P/E 17.08 | P/B 2.29 | P/S 1.52 | 3y earnings growth n/a
Yield: 3.1%
Three-year record: +18.2% a year | beta to the market 0.68
Cost and size: expense ratio 0.50% | net assets 3.79B
What it is made of: Stocks 97.9%, Other 1.1%, Cash 0.9%
Largest holdings: HSBC Holdings PLC 11.0%, Shell PLC 7.8%, AstraZeneca PLC 7.6%, Rolls-Royce Holdings PLC 5.3%, Unilever PLC 4.3%
Sector mix: Financial services 26.4%, Consumer defensive 14.3%, Industrials 13.9%, Healthcare 12.7%
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
Rolled up from the 5 largest holdings, 36.0% of the fund by weight
Ratings by weight: buy 50.1% | hold 49.9% | sell 0.0% (mean 2.30 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +12.5% above the current prices
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

_Not available today._

</details>

### Mexico (EWW) · Sector or country — NEUTRAL, confidence 0.25

**In the model's own words:**

> EWW (Mexico-focused equity fund) is technically oversold with RSI at 29.4 and price 4.5-5.1% below major moving averages, presenting a potential mean-reversion setup. However, this is tempered by several headwinds: the US dollar has strengthened sharply (+1.34% on the week to 100.11), which pressures emerging market assets; Treasury yields have risen across the curve, increasing the opportunity cost of equity allocations; and the fund has underperformed over multiple timeframes (3m -7.4%, 1m -3.6%). Analyst coverage of the top 47.6% of holdings shows unanimous buy/hold ratings with a +16.7% price target, suggesting institutional conviction, but this is offset by weak recent price action and elevated macro uncertainty. The fund's 3.2% yield and reasonable valuation (P/E 12.68) provide support, but macro conditions—particularly dollar strength and rising rates—are headwinds for EM exposure. Volume is below average, suggesting limited conviction in either direction. The technical oversold condition alone does not justify a bullish call given the macro backdrop; a true reversal would require stabilization in the dollar and yields, which has not occurred.

**Main reasons it gave:**
- RSI 29.4 and price 4-5% below 20/50/200d averages signal technical oversold
- USD +1.34% this week to 100.11 headwind for EM valuations
- Analyst buy ratings with +16.7% target on 47.6% of holdings suggests institutional support
- 10yr yield +14bp this week increases opportunity cost vs equities
- Below-average trading volume suggests weak conviction in any direction

<details><summary><b>News</b> — score +0.00</summary>

_No news found for this one today._

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 3.96% (+0.16 on the week) | 5-year 4.83% (+0.21 on the week) | 10-year 4.97% (+0.14 on the week) | 30-year 5.32% (+0.03 on the week)
Yield curve, 10-year minus 3-month: +1.01 points -- upward sloping (normal)
US dollar index: 100.11 (+1.34 on the week)
Volatility (VIX): 16.79 (+0.3 on the week) -- elevated
```

</details>

<details><summary><b>Price and chart</b> — score -0.35</summary>

```text
Last close 72.21 (bar of 2026-09-16), from 502 daily bars
Trend: vs 20d SMA 76.06 (-5.1%), 50d 75.90 (-4.9%), 200d 75.58 (-4.5%); 50d above 200d
Momentum: RSI(14) 29.4 | MACD -0.566 vs signal -0.143 (histogram -0.423)
Returns: 1d -2.5% | 5d -5.6% | 1m -3.6% | 3m -7.4%
52-week range: 64.39 - 81.23 (now 46.4% of the way up)
Volatility: ATR(14) 1.30 (1.8% of price) | annualised 20d 17.5%
Volume: 0.70x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.15</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score +0.15</summary>

```text
Fund type: Focused Region
What it holds: P/E 12.68 | P/B 1.98 | P/S 1.49 | 3y earnings growth n/a
Yield: 3.2%
Three-year record: +11.4% a year | beta to the market 1.05
Cost and size: expense ratio 0.50% | net assets 1.82B
What it is made of: Stocks 99.5%, Cash 0.5%
Largest holdings: Grupo Mexico SAB de CV Class B 16.6%, Grupo Financiero Banorte SAB de CV Class O 11.1%, Fomento Economico Mexicano SAB de CV Units Cons. Of 1 Shs-B- And 4 Shs-D- 8.3%, America Movil SAB de CV Ordinary Shares - Class B 7.2%, Cemex SAB de CV 4.4%
Sector mix: Basic materials 27.3%, Consumer defensive 24.4%, Financial services 19.7%, Industrials 11.7%
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

<details><summary><b>What analysts and big funds say</b> — score +0.40</summary>

_Not available today._

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score +0.40</summary>

```text
Rolled up from the 5 largest holdings, 47.6% of the fund by weight
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 2.11 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +16.7% above the current prices
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

_Not available today._

</details>

### South Korea (EWY) · Sector or country — NEUTRAL, confidence 0.25

**In the model's own words:**

> EWY is down 8.6% over five days and trades 3.4% below its 20-day MA, with RSI at 46.2 and MACD in negative histogram, suggesting near-term weakness. Macro backdrop shows rising yields (5Y +21bp, 10Y +14bp) and a strengthening dollar (+1.34% weekly), both headwinds for Korean equities. The fund's 15.3% three-month decline reflects sector rotation away from tech. News on SK Hynix and Samsung chip production is company-specific noise immaterial to a 27B broad South Korea fund; KCHP launch and Taiwan supply chain chatter are sector commentary, not directional catalysts. Fund technicals show the 50d MA above 200d (bullish structure) and the stock up 15.8% YTD, supporting a long-term view but offering no near-term reversal signal. Volume at 0.60x average and elevated 43.5% annualized volatility suggest caution. No analyst consensus, positioning data, or fund flows data are available to corroborate a directional move. The macro environment—higher real yields, stronger dollar, elevated VIX—favors caution on risk assets, and EWY's beta of 2.50 amplifies drawdown risk. Insufficient evidence of a reversal or continuation to warrant conviction beyond a small offset to neutral.

**Main reasons it gave:**
- US yields up 14-21bp week-over-week, dollar +1.34%
- EWY down 8.6% in 5 days, RSI 46.2, MACD negative histogram
- Fund beta 2.50 amplifies macro headwinds
- No analyst coverage or positioning data available
- Company-specific chip news immaterial to broad regional fund

<details><summary><b>News</b> — score +0.00</summary>

- [New ETF Coverage: KCHP](https://finance.yahoo.com/markets/stocks/articles/etf-coverage-kchp-144057032.html)  
  <sub>Yahoo Finance, 5 hours ago</sub>  
  KCHP launched September 15, 2026 on NYSE Arca, giving U.S. investors a single-ticker bet on South Korean semiconductor companies at a 0.65% expense ratio.
- [SK Hynix, Intel Eye US Memory Chip Deal: ETFs to Watch - Intel (NASDAQ:INTC)](https://www.benzinga.com/etfs/sector-etfs/26/09/61823839/sk-hynix-intel-may-make-memories-in-ohio-these-etfs-are-along-for-the-ride)  
  <sub>Benzinga, 2 hours ago</sub>  
  SK Hynix and Intel are exploring U.S. memory chip production as demand for DRAM and high-bandwidth memory surges. Here are the ETFs to watch.
- [Elon Musk Flags Taiwan as AI’s Weak Link. These Semiconductor ETFs Could Offer a Hedge](https://www.tradingview.com/news/benzinga:8d51fc1c5094b:0)  
  <sub>TradingView, 23 hours ago</sub>  
  Speaking at the All-In Summit, Elon Musk warned that existing fabs are running at full capacity and that a disruption in Taiwan could compound supply...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 3.96% (+0.16 on the week) | 5-year 4.83% (+0.21 on the week) | 10-year 4.97% (+0.14 on the week) | 30-year 5.32% (+0.03 on the week)
Yield curve, 10-year minus 3-month: +1.01 points -- upward sloping (normal)
US dollar index: 100.11 (+1.34 on the week)
Volatility (VIX): 16.79 (+0.3 on the week) -- elevated
```

</details>

<details><summary><b>Price and chart</b> — score -0.15</summary>

```text
Last close 174.46 (bar of 2026-09-16), from 502 daily bars
Trend: vs 20d SMA 180.53 (-3.4%), 50d 173.45 (+0.6%), 200d 150.68 (+15.8%); 50d above 200d
Momentum: RSI(14) 46.2 | MACD 1.482 vs signal 2.522 (histogram -1.040)
Returns: 1d -1.2% | 5d -8.6% | 1m -5.7% | 3m -15.3%
52-week range: 78.87 - 219.20 (now 68.1% of the way up)
Volatility: ATR(14) 6.72 (3.9% of price) | annualised 20d 43.5%
Volume: 0.60x the 20-day average
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
Three-year record: +44.5% a year | beta to the market 2.50
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

_Not available today._

</details>

### Gold mining companies (GDX) · Sector or country — NEUTRAL, confidence 0.25

**In the model's own words:**

> GDX has sold off sharply (−8% in 5 days, −2.8% today) into a Fed rate decision expected tomorrow, with Treasury yields rising across the curve this week and the dollar strengthening +1.34%. The technical picture shows the fund below its 20-day moving average (−7.5%) and momentum deteriorating: RSI at 45, MACD histogram negative and below signal. The 50-day is still above 200-day so the longer trend is intact, but price is only 1% above the 200-day and volume is weak. Offsetting this: analyst coverage of the five largest holdings (40% of the fund) is uniformly bullish—100% buy-rated with a +12.1% price target—and the fund's three-year return of +49.6% annually shows structural exposure is working. News flow is benign (routine index additions), not bearish. The macro headwind is temporary: the rate decision tomorrow will clarify, and if the Fed pauses or signals a cut cycle, gold and mining equities typically respond well. The immediate setup is weak but the catalysts and fundamentals do not justify a bearish call. A stronger move down on the rate decision or a break below 87 would sharpen conviction either way. For now, the cross-currents argue for neutrality rather than a directional lean.

**Main reasons it gave:**
- Analyst consensus bullish on 40% of holdings with +12.1% price target
- Fund down 8% in 5 days into Fed decision with momentum deteriorating below signal line
- Treasury yields +14 to +21 bps on week, dollar +1.34%, headwind to commodities
- 3-year annualized return +49.6%, longer trend support at 200-day (90.54)

<details><summary><b>News</b> — score +0.00</summary>

- [Versamet (NASDAQ: VMET) to enter junior gold miners ETF it expects will boost visibility](https://www.stocktitan.net/sec-filings/VMET/6-k-versamet-royalties-corp-current-report-foreign-issuer-4c91d31d84a5.html)  
  <sub>Stock Titan, 3 hours ago</sub>  
  2026 Asset Handbook gives a deeper look at Versamet's royalty and streaming portfolio as it joins the junior gold miners ETF benchmark on Sept. 21, 2026.
- [GOEX: Ultimately Dictated By Gold Dynamics, Rate Risks Present](https://seekingalpha.com/article/4946843-goex-ultimately-dictated-by-gold-dynamics-rate-risks-present)  
  <sub>Seeking Alpha, 14 hours ago</sub>  
  Gold Explorers ETF (GOEX) analysis: higher fees/volatility, tied to gold prices. Read here for a detailed investment analysis.
- [YieldMax® ETFs Announces Weekly Distributions for Group 2 ETFs](https://www.globenewswire.com/news-release/2026/09/16/3363024/0/en/yieldmax-etfs-announces-weekly-distributions-for-group-2-etfs.html)  
  <sub>GlobeNewswire, 8 hours ago</sub>  
  CHICAGO and MILWAUKEE and NEW YORK, Sept. 16, 2026 (GLOBE NEWSWIRE) -- YieldMax® ETFs today announced distributions for the YieldMax® Group 2 weekly pay...
- [Versamet Royalties Corporation (TSX:VMET) Added to GDXJ Index](https://www.tradingview.com/news/tradingview:ec98902e04515:0-versamet-royalties-corporation-tsx-vmet-added-to-gdxj-index/)  
  <sub>TradingView, 7 hours ago</sub>  
  Versamet will be added to the MVIS Global Junior Gold Miners Index after the close Sept. 18, 2026, effective Sept. 21, 2026, as part of the semi-annual...
- [Gold and silver tick lower ahead of Fed rate decision (GLD:NYSEARCA)](https://seekingalpha.com/news/4643189-gold-and-silver-tick-lower-ahead-of-fed-rate-decision)  
  <sub>Seeking Alpha, 22 hours ago</sub>  
  Gold and silver futures settled modestly lower a day ahead of the Federal Reserve's interest-rate decision, which is widely expected to be a quarter-point...
- [Goldsky Resources Added to VanEck Junior Gold Miners ETF After Nordic Portfolio Expansion](https://www.tipranks.com/news/company-announcements/goldsky-resources-added-to-vaneck-junior-gold-miners-etf-after-nordic-portfolio-expansion)  
  <sub>TipRanks, 8 hours ago</sub>  
  The latest announcement is out from Goldsky Resources ( ($TSE:GSKR) ). Goldsky Resources has been added to the VanEck Junior Gold Miners ETF, known as GDXJ,...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 3.96% (+0.16 on the week) | 5-year 4.83% (+0.21 on the week) | 10-year 4.97% (+0.14 on the week) | 30-year 5.32% (+0.03 on the week)
Yield curve, 10-year minus 3-month: +1.01 points -- upward sloping (normal)
US dollar index: 100.11 (+1.34 on the week)
Volatility (VIX): 16.79 (+0.3 on the week) -- elevated
```

</details>

<details><summary><b>Price and chart</b> — score -0.35</summary>

```text
Last close 91.46 (bar of 2026-09-16), from 502 daily bars
Trend: vs 20d SMA 98.86 (-7.5%), 50d 87.11 (+5.0%), 200d 90.54 (+1.0%); 50d below 200d
Momentum: RSI(14) 45.0 | MACD 1.516 vs signal 3.109 (histogram -1.593)
Returns: 1d -2.8% | 5d -8.0% | 1m -0.5% | 3m +4.8%
52-week range: 68.28 - 115.84 (now 48.7% of the way up)
Volatility: ATR(14) 3.52 (3.8% of price) | annualised 20d 53.1%
Volume: 0.75x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.25</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score +0.25</summary>

```text
Fund type: Equity Precious Metals
What it holds: P/E 12.84 | P/B 2.68 | P/S 4.10 | 3y earnings growth n/a
Yield: 0.6%
Three-year record: +49.6% a year | beta to the market 0.83
Cost and size: expense ratio 0.51% | net assets 30.54B
What it is made of: Stocks 100.0%
Largest holdings: Newmont Corp 10.7%, Agnico Eagle Mines Ltd 10.7%, Barrick Mining Corp 7.4%, Wheaton Precious Metals Corp 5.8%, Anglogold Ashanti PLC 5.3%
Sector mix: Basic materials 100.0%
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
Rolled up from the 5 largest holdings, 39.9% of the fund by weight
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 1.65 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +12.1% above the current prices
Holdings read: NEM, AEM.TO, ABX.TO, WPM.TO, AU
Recent rating changes among them:
  - NEM: 2026-09-16 RBC Capital: main, Outperform -> Outperform
  - AEM.TO: 2026-09-16 RBC Capital: main, Sector Perform -> Sector Perform
  - ABX.TO: 2026-09-16 RBC Capital: main, Outperform -> Outperform
  - WPM.TO: 2026-09-16 RBC Capital: main, Outperform -> Outperform
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

_Not available today._

</details>

### Software (IGV) · Sector or country — NEUTRAL, confidence 0.25

**In the model's own words:**

> IGV holds a concentrated basket of high-valuation technology names, with the largest five positions spanning 43% of the fund. Technicals show a fund still in uptrend (trading 12.2% above 200d MA) with improving momentum over recent weeks, but momentum indicators are cooling: RSI sits at neutral 54.2 and MACD histogram has turned negative. The fund trades on a stretched P/E of 34.2x with elevated 20d volatility at 41.8%, pricing in significant growth already. Recent macro moves show Treasury yields rising across the curve (10-year +14bp this week) and the dollar strengthening (+1.34% on the week), which typically pressures growth-heavy tech valuations. Analyst consensus on the top holdings remains constructive (100% buy by weight with +8.8% upside targets), but this reflects views formed at lower valuations. News flow shows sector-specific selling pressure in speculative software names, a segment that overlaps with IGV's holding structure. Fund flows and positioning data are absent, limiting conviction on near-term direction. The macro backdrop of rising rates and a strengthening dollar is moderately headwind for a fund with 94% in high-multiple technology equities, but the technical uptrend and analyst buy ratings provide a floor. No decisive catalyst has emerged to shift the view away from neutral.

**Main reasons it gave:**
- Rising Treasury yields across curve (+14bp 10-year this week) pressure high-valuation tech multiples
- MACD momentum histogram turned negative despite uptrend, RSI at neutral 54.2 signals cooling momentum
- Elevated P/E of 34.2x already prices significant growth; analyst upside targets only +8.8% on stretched valuations
- Sector-specific selling pressure in speculative software overlaps with fund holdings; volume 0.48x average signals lower conviction
- Dollar strength (+1.34% week) headwind for multinational tech exposure

<details><summary><b>News</b> — score -0.15</summary>

- [SoundHound AI Drops 4% as Selling Concentrates in Speculative Software Names; UiPath Falls 3%, C3.ai Dips](https://247wallst.com/investing/2026/09/16/soundhound-ai-drops-4-as-selling-concentrates-in-speculative-software-names-uipath-falls-3-c3-ai-dips/)  
  <sub>24/7 Wall St., 2 hours ago</sub>  
  Concentrated selling is hammering a thin slice of speculative software names even as the broader market climbs higher, and the divergence raises a pointed...
- [How to Trade the Nasdaq in Light of the Fed Decision](https://uk.investing.com/analysis/how-to-trade-the-nasdaq-in-light-of-the-fed-decision-200628090)  
  <sub>Investing.com UK, 9 hours ago</sub>  
  Market Analysis by covering: Nasdaq 100, S&P 500, US Small Cap 2000, NVIDIA Corporation. Read 's Market Analysis on Investing.com UK.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score -0.15</summary>

```text
US Treasury yields: 3-month 3.96% (+0.16 on the week) | 5-year 4.83% (+0.21 on the week) | 10-year 4.97% (+0.14 on the week) | 30-year 5.32% (+0.03 on the week)
Yield curve, 10-year minus 3-month: +1.01 points -- upward sloping (normal)
US dollar index: 100.11 (+1.34 on the week)
Volatility (VIX): 16.79 (+0.3 on the week) -- elevated
```

</details>

<details><summary><b>Price and chart</b> — score +0.35</summary>

```text
Last close 105.06 (bar of 2026-09-16), from 502 daily bars
Trend: vs 20d SMA 104.51 (+0.5%), 50d 99.53 (+5.6%), 200d 93.67 (+12.2%); 50d above 200d
Momentum: RSI(14) 54.2 | MACD 1.152 vs signal 1.530 (histogram -0.378)
Returns: 1d -0.5% | 5d +3.2% | 1m +3.0% | 3m +15.0%
52-week range: 74.67 - 117.79 (now 70.5% of the way up)
Volatility: ATR(14) 2.76 (2.6% of price) | annualised 20d 41.8%
Volume: 0.48x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score -0.25</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score -0.25</summary>

```text
Fund type: Technology
What it holds: P/E 34.20 | P/B 8.09 | P/S 9.07 | 3y earnings growth n/a
Yield: 0.0%
Three-year record: +14.1% a year | beta to the market 1.21
Cost and size: expense ratio 0.38% | net assets 15.74B
What it is made of: Stocks 100.0%, Cash 0.1%
Largest holdings: Palantir Technologies Inc Ordinary Shares - Class A 10.3%, Palo Alto Networks Inc 9.7%, Microsoft Corp 9.2%, CrowdStrike Holdings Inc Class A 7.4%, Salesforce Inc 6.6%
Sector mix: Technology 94.4%, Communication services 3.8%, Financial services 1.5%, Consumer cyclical 0.2%
```

</details>

<details><summary><b>Does this company beat its own forecasts</b> — score -0.25</summary>

_Not available today._

</details>

<details><summary><b>What holding this fund costs you</b> — score -0.25</summary>

_Not available today._

</details>

<details><summary><b>How much oil and gas is in storage</b> — score -0.25</summary>

_Not available today._

</details>

<details><summary><b>How the crop is growing</b> — score -0.25</summary>

_Not available today._

</details>

<details><summary><b>What analysts and big funds say</b> — score +0.45</summary>

_Not available today._

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score +0.45</summary>

```text
Rolled up from the 5 largest holdings, 43.2% of the fund by weight
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 1.65 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +8.8% above the current prices
Holdings read: PLTR, PANW, MSFT, CRWD, CRM
Recent rating changes among them:
  - PLTR: 2026-09-15 UBS: main, Buy -> Buy
  - PANW: 2026-09-03 Argus Research: reit, Buy -> Buy
  - MSFT: 2026-09-15 Citizens: reit, Market Outperform -> Market Outperform
  - CRWD: 2026-09-04 Macquarie: main, Neutral -> Neutral
  - CRM: 2026-09-16 Stifel: reit, Buy -> Buy
```

</details>

<details><summary><b>Buying and selling by company insiders</b> — score +0.00</summary>

_Not available today._

</details>

<details><summary><b>Who is positioned how</b> — score +0.00</summary>

_Not available today._

</details>

<details><summary><b>Money going into and out of this fund</b> — score +0.00</summary>

_Not available today._

</details>

### India (INDA) · Sector or country — NEUTRAL, confidence 0.25

**In the model's own words:**

> INDA trades 3.8-5.7% below its moving averages in a pullback from a 52-week high, with RSI at 30.2 signaling oversold conditions and negative momentum (MACD histogram -0.252). Fundamentals show a respectable P/E of 22.87 and three-year annualized return of +2.5%, but three-year earnings growth data is unavailable. The analyst roll-up from the largest 24.7% of holdings shows unanimous buy ratings with a +30.6% weighted price target, a bullish signal; however, this thin coverage (under 25% of fund weight) limits what it says about the full basket. Macro backdrop shows rising Treasury yields across the curve (+14-21bp this week), a strengthening dollar (+1.34), and elevated volatility (VIX 16.79), creating headwinds for emerging market equities. The normal yield curve slope and absence of news surprises offer no tactical catalyst. The combination of technical oversold conditions and analyst support for the largest holdings is offset by deteriorating macro conditions and weak recent performance (-4.5% over one month). Volume is below average, suggesting weak conviction in either direction. This lacks the clarity and corroboration needed to move decisively away from neutral.

**Main reasons it gave:**
- Price 3.8-5.7% below 20d, 50d, and 200d moving averages in downtrend
- RSI 30.2 indicates oversold, but MACD histogram negative and momentum weak
- Analyst weighted buy rating with +30.6% price target on largest 24.7% of holdings, but thin coverage limits scope
- Rising yields (+14-21bp across curve) and strengthening dollar (+1.34) headwind for Indian equities
- No macro surprise or rate shock to justify tactical move; three-year earnings growth unavailable

<details><summary><b>News</b> — score +0.00</summary>

_No news found for this one today._

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 3.96% (+0.16 on the week) | 5-year 4.83% (+0.21 on the week) | 10-year 4.97% (+0.14 on the week) | 30-year 5.32% (+0.03 on the week)
Yield curve, 10-year minus 3-month: +1.01 points -- upward sloping (normal)
US dollar index: 100.11 (+1.34 on the week)
Volatility (VIX): 16.79 (+0.3 on the week) -- elevated
```

</details>

<details><summary><b>Price and chart</b> — score -0.35</summary>

```text
Last close 47.35 (bar of 2026-09-16), from 502 daily bars
Trend: vs 20d SMA 49.20 (-3.8%), 50d 49.27 (-3.9%), 200d 50.22 (-5.7%); 50d below 200d
Momentum: RSI(14) 30.2 | MACD -0.438 vs signal -0.185 (histogram -0.252)
Returns: 1d -0.5% | 5d -2.7% | 1m -4.5% | 3m -4.2%
52-week range: 45.42 - 55.29 (now 19.6% of the way up)
Volatility: ATR(14) 0.46 (1.0% of price) | annualised 20d 13.5%
Volume: 0.85x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.15</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score +0.15</summary>

```text
Fund type: India Equity
What it holds: P/E 22.87 | P/B 3.14 | P/S 2.72 | 3y earnings growth n/a
Yield: n/a
Three-year record: +2.5% a year | beta to the market 0.56
Cost and size: expense ratio 0.61% | net assets 6.75B
What it is made of: Stocks 100.1%, Cash -0.1%
Largest holdings: HDFC Bank Ltd 6.4%, Reliance Industries Ltd 6.0%, ICICI Bank Ltd 5.7%, Bharti Airtel Ltd 4.1%, Infosys Ltd 2.6%
Sector mix: Financial services 30.1%, Consumer cyclical 12.8%, Industrials 9.7%, Energy 8.6%
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

<details><summary><b>What analysts and big funds say</b> — score +0.40</summary>

_Not available today._

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score +0.40</summary>

```text
Rolled up from the 5 largest holdings, 24.7% of the fund by weight  -- thin, so read this as a fact about that slice rather than the fund
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 1.36 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +30.6% above the current prices
Holdings read: HDFCBANK.NS, RELIANCE.NS, ICICIBANK.NS, BHARTIARTL.NS, INFY.NS
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

_Not available today._

</details>

### Defence and aerospace (ITA) · Sector or country — NEUTRAL, confidence 0.25

**In the model's own words:**

> ITA is a concentrated aerospace and defense fund with extremely elevated valuation (P/E 34.66, P/B 6.62) at a time when technicals show significant weakness: the fund is down 6.9% from its 200-day moving average, with RSI at 24.5 (oversold) and negative MACD histogram indicating momentum deterioration. Recent one-month and three-month returns are -14.8% and -10.6% respectively. The macro backdrop of rising treasury yields (+14-21 bps across the curve) and a stronger dollar (+1.34 on the week) typically pressures growth-heavy, capital-intensive sectors. Analyst sentiment from the 5 largest holdings (57.5% of fund) is unanimously bullish with a weighted price target 25.8% above current prices, and recent rating changes include upgrades for Boeing and Lockheed Martin, which provide structural support. However, the timing of these recommendations against such deteriorated technicals and stretched valuation, combined with elevated VIX (16.79) and weakening momentum, argues against a confident directional call. The Boeing order announcement is modest good news but fails to offset the technical deterioration. Volume is below average, suggesting weak conviction in any direction. The fund's three-year 26.3% annualized return suggests secular tailwinds in defense spending, but a macro timing call here lacks a clear catalyst.

**Main reasons it gave:**
- RSI 24.5 and MAmalcolm histogram negative signal momentum break
- Price down 6.9% from 200-day MA and 14.8% month-to-month
- Analyst consensus unanimously buy with 25.8% upside from holdings, but timing against technicals unclear
- P/E 34.66 valuation compressed into rising rate environment
- Treasury yields up 14-21 bps across curve this week

<details><summary><b>News</b> — score +0.15</summary>

- [Invesco Aerospace & Defense vs. Global X Defense Tech: Which ETF Is Best for Your Portfolio?](https://finance.yahoo.com/markets/stocks/articles/invesco-aerospace-defense-vs-global-122501205.html)  
  <sub>Yahoo Finance, 7 hours ago</sub>  
  PPA targets legacy hardware with broader industrial exposure and stronger one-year returns, while SHLD emphasizes emerging tech and cybersecurity at lower...
- [Boeing Lands Record 103-Jet Korean Air Order](https://www.tradingview.com/news/benzinga:fea24ae2e094b:0-boeing-lands-record-103-jet-korean-air-order/)  
  <sub>TradingView, 5 hours ago</sub>  
  Boeing Co. www.benzinga.com/quote/BA(NYSE:BA) and Korean Air said Wednesday they finalized a record order for 103 Boeing jets, completing the carrier's...
- [(ITA) Movement as an Input in Quant Signal Sets](https://news.stocktradersdaily.com/news_release/35/ITA_Movement_as_an_Input_in_Quant_Signal_Sets_091626063443_1789554883.html)  
  <sub>Stock Traders Daily, 13 hours ago</sub>  
  Key findings for Ishares U.s. Aerospace & Defense Etf (NYSE: ITA). Signals: (bold = current price). Institutional Trading Strategies.
- [ETFs Investing in AeroVironment, Inc. Stocks](https://www.tradingview.com/symbols/FWB-JPX/etfs/)  
  <sub>TradingView, 4 hours ago</sub>  
  Explore funds investing in JPX in a single list with price, expense ratio, and more stats for an in-depth analysis of new opportunities.
- [Iran war costs reach $38B as inflation, supply risks mount (PPA:NYSEARCA)](https://seekingalpha.com/news/4643144-iran-war-costs-reach-38b-as-inflation-supply-risks-mount)  
  <sub>Seeking Alpha, 24 hours ago</sub>  
  The war with Iran cost U.S. taxpayers about $38 billion during its first five months and is expected to add to inflation, according to a new Congressional...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.15</summary>

```text
US Treasury yields: 3-month 3.96% (+0.16 on the week) | 5-year 4.83% (+0.21 on the week) | 10-year 4.97% (+0.14 on the week) | 30-year 5.32% (+0.03 on the week)
Yield curve, 10-year minus 3-month: +1.01 points -- upward sloping (normal)
US dollar index: 100.11 (+1.34 on the week)
Volatility (VIX): 16.79 (+0.3 on the week) -- elevated
```

</details>

<details><summary><b>Price and chart</b> — score -0.55</summary>

```text
Last close 214.08 (bar of 2026-09-16), from 502 daily bars
Trend: vs 20d SMA 227.31 (-5.8%), 50d 236.30 (-9.4%), 200d 230.02 (-6.9%); 50d above 200d
Momentum: RSI(14) 24.5 | MACD -6.943 vs signal -5.596 (histogram -1.347)
Returns: 1d +0.0% | 5d -2.4% | 1m -14.8% | 3m -10.6%
52-week range: 198.23 - 253.22 (now 28.8% of the way up)
Volatility: ATR(14) 4.05 (1.9% of price) | annualised 20d 18.0%
Volume: 0.93x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score -0.25</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score -0.25</summary>

```text
Fund type: Industrials
What it holds: P/E 34.66 | P/B 6.62 | P/S 3.21 | 3y earnings growth n/a
Yield: 0.5%
Three-year record: +26.3% a year | beta to the market 0.99
Cost and size: expense ratio 0.37% | net assets 13.63B
What it is made of: Stocks 99.8%, Cash 0.2%
Largest holdings: GE Aerospace 21.6%, RTX Corp 17.2%, Boeing Co 9.1%, General Dynamics Corp 4.8%, Lockheed Martin Corp 4.7%
Sector mix: Industrials 100.0%
```

</details>

<details><summary><b>Does this company beat its own forecasts</b> — score -0.25</summary>

_Not available today._

</details>

<details><summary><b>What holding this fund costs you</b> — score -0.25</summary>

_Not available today._

</details>

<details><summary><b>How much oil and gas is in storage</b> — score -0.25</summary>

_Not available today._

</details>

<details><summary><b>How the crop is growing</b> — score -0.25</summary>

_Not available today._

</details>

<details><summary><b>What analysts and big funds say</b> — score +0.60</summary>

_Not available today._

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score +0.60</summary>

```text
Rolled up from the 5 largest holdings, 57.5% of the fund by weight
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 1.76 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +25.8% above the current prices
Holdings read: GE, RTX, BA, GD, LMT
Recent rating changes among them:
  - GE: 2026-07-23 Bernstein: main, Outperform -> Outperform
  - RTX: 2026-08-03 Bernstein: main, Market Perform -> Market Perform
  - BA: 2026-08-11 Argus Research: up, Hold -> Buy
  - GD: 2026-09-08 UBS: main, Neutral -> Neutral
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

_Not available today._

</details>

### US regional banks (KRE) · Sector or country — NEUTRAL, confidence 0.25

**In the model's own words:**

> KRE is the financial services ETF holding regional and community banks. The fund trades at a reasonable valuation (P/E 12.60, P/B 1.27) with a 2.2% yield, but technicals show deterioration: price is 2.8% below the 20-day moving average, RSI(14) is 34.9 (oversold territory), and MACD is negative with a widening histogram. One-month returns are -6.9%, suggesting recent weakness. The macro backdrop is mixed: Treasury yields moved higher across the curve this week, which could compress net interest margins and pressure bank valuations; the dollar strengthened 1.34% and the VIX ticked up to 16.79, showing modest stress. On the positive side, the 50-day MA remains above the 200-day MA (uptrend structure intact), the fund is still 70% of the way through its 52-week range, and analyst coverage of the top 5 holdings shows 74.4% buy-rated by weight with a +20.2% upside target. However, that coverage is thin at only 7.1% of fund weight, so it carries limited significance. Recent rating upgrades to CFR and PNFP provide some support. The weakness appears tactical rather than structural, but without a clear catalyst or technical confirmation of a reversal, conviction remains low. Rates rising this week is a headwind for bank profitability, and the oversold technical state is not yet accompanied by a decisive volume bounce or other reversal signal.

**Main reasons it gave:**
- RSI 34.9 and MACD negative with widening histogram indicate oversold momentum
- Treasury yields rose 14-21 bps across the curve, headwind for bank net interest margins
- Price 4.5% below 50-day MA but uptrend structure (50d > 200d) intact
- Analyst targets on top 5 holdings show +20.2% upside but coverage only 7.1% of fund weight
- One-month return -6.9% reflects recent weakness, no catalytic news to suggest reversal

<details><summary><b>News</b> — score +0.00</summary>

_No news found for this one today._

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 3.96% (+0.16 on the week) | 5-year 4.83% (+0.21 on the week) | 10-year 4.97% (+0.14 on the week) | 30-year 5.32% (+0.03 on the week)
Yield curve, 10-year minus 3-month: +1.01 points -- upward sloping (normal)
US dollar index: 100.11 (+1.34 on the week)
Volatility (VIX): 16.79 (+0.3 on the week) -- elevated
```

</details>

<details><summary><b>Price and chart</b> — score -0.35</summary>

```text
Last close 72.05 (bar of 2026-09-16), from 502 daily bars
Trend: vs 20d SMA 74.16 (-2.8%), 50d 75.41 (-4.5%), 200d 70.24 (+2.6%); 50d above 200d
Momentum: RSI(14) 34.9 | MACD -0.590 vs signal -0.463 (histogram -0.127)
Returns: 1d -2.7% | 5d -1.9% | 1m -6.9% | 3m -0.6%
52-week range: 58.14 - 77.93 (now 70.3% of the way up)
Volatility: ATR(14) 1.23 (1.7% of price) | annualised 20d 17.8%
Volume: 0.93x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.10</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score +0.10</summary>

```text
Fund type: Financial
What it holds: P/E 12.60 | P/B 1.27 | P/S 3.77 | 3y earnings growth n/a
Yield: 2.2%
Three-year record: +22.4% a year | beta to the market 1.04
Cost and size: expense ratio 0.35% | net assets 4.01B
What it is made of: Stocks 99.9%, Cash 0.1%
Largest holdings: Cullen/Frost Bankers Inc 1.5%, SouthState Bank Corp 1.4%, Popular Inc 1.4%, Pinnacle Financial Partners Inc 1.4%, UMB Financial Corp 1.4%
Sector mix: Financial services 100.0%
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
Rolled up from the 5 largest holdings, 7.1% of the fund by weight  -- thin, so read this as a fact about that slice rather than the fund
Ratings by weight: buy 74.4% | hold 25.6% | sell 0.0% (mean 1.93 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +20.2% above the current prices
Holdings read: CFR, SSB, BPOP, PNFP, UMBF
Recent rating changes among them:
  - CFR: 2026-09-08 Morgan Stanley: up, Underweight -> Overweight
  - SSB: 2026-07-28 Citigroup: main, Buy -> Buy
  - BPOP: 2026-08-31 Benchmark: main, Buy -> Buy
  - PNFP: 2026-09-08 Morgan Stanley: init, ? -> Overweight
  - UMBF: 2026-09-14 UBS: init, ? -> Neutral
```

</details>

<details><summary><b>Buying and selling by company insiders</b> — score +0.00</summary>

_Not available today._

</details>

<details><summary><b>Who is positioned how</b> — score +0.00</summary>

_Not available today._

</details>

<details><summary><b>Money going into and out of this fund</b> — score +0.00</summary>

_Not available today._

</details>

### Saudi Arabia (KSA) · Sector or country — NEUTRAL, confidence 0.25

**In the model's own words:**

> KSA tracks Saudi equities, which face conflicting signals. Technicals show weakness: price 3.5% below the 20-day SMA, RSI at 30 (oversold), negative MACD histogram, and a falling trend across all timeframes with the 50d below 200d. Volume is depressed at 0.61x average, suggesting thin conviction in the move. Macro conditions are headwinds: US Treasury yields rose sharply this week (10y +14bp, 5y +21bp), the dollar strengthened (+1.34 on the week to 100.11), and the yield curve normalized higher -- all typically pressure EM and regional equities. The fund's 0.18 beta to broad markets means it will lag in risk-off environments. However, analyst coverage of the five largest holdings (44% of the fund) shows 90% buy-rated constituents with a +14.7% consensus price target, and the news mentions pension and ETF inflows supporting Korean and regional tech. The fund's modest 2.7% yield and reasonable 15.0x P/E offer some valuation ballast. The weakness appears tactical and possibly overdone (RSI 30), but the macro backdrop -- higher rates, a stronger dollar, and rising Treasury yields ahead of the FOMC -- argues for patience. A near-term bounce is plausible, but the structural headwinds are real. This is a hold rather than a conviction call in either direction.

**Main reasons it gave:**
- Technicals deeply oversold (RSI 30, price -3.5% vs 20d SMA) amid depressed volume
- US yields rose sharply this week (10y +14bp, 5y +21bp) and dollar strengthened +1.34 on the week
- Analyst coverage of largest 44% of fund shows 90% buy ratings with +14.7% consensus target
- Pension and ETF buying noted in news, but macro headwinds into FOMC meeting limit conviction

<details><summary><b>News</b> — score +0.15</summary>

- [Pension and ETF buying lift Korea stocks as tech rebounds before FOMC - CHOSUNBIZ](https://biz.chosun.com/en/en-finance/2026/09/16/MA6PLDP6MFD3FHQPJA3VGXNDEY/?outputType=amp)  
  <sub>Chosunbiz, 13 hours ago</sub>  
  Pension and ETF buying lift Korea stocks as tech rebounds before FOMC Pension inflows and buybacks buoy KOSPI despite oil surge and rising Treasury yi.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.15</summary>

```text
US Treasury yields: 3-month 3.96% (+0.16 on the week) | 5-year 4.83% (+0.21 on the week) | 10-year 4.97% (+0.14 on the week) | 30-year 5.32% (+0.03 on the week)
Yield curve, 10-year minus 3-month: +1.01 points -- upward sloping (normal)
US dollar index: 100.11 (+1.34 on the week)
Volatility (VIX): 16.79 (+0.3 on the week) -- elevated
```

</details>

<details><summary><b>Price and chart</b> — score -0.55</summary>

```text
Last close 37.14 (bar of 2026-09-16), from 502 daily bars
Trend: vs 20d SMA 38.47 (-3.5%), 50d 37.78 (-1.7%), 200d 38.14 (-2.6%); 50d below 200d
Momentum: RSI(14) 30.0 | MACD -0.094 vs signal 0.114 (histogram -0.208)
Returns: 1d -0.7% | 5d -3.0% | 1m -2.3% | 3m -3.7%
52-week range: 35.83 - 41.03 (now 25.2% of the way up)
Volatility: ATR(14) 0.29 (0.8% of price) | annualised 20d 11.0%
Volume: 0.61x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.35</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score +0.35</summary>

```text
Fund type: Focused Region
What it holds: P/E 15.00 | P/B 1.81 | P/S 3.04 | 3y earnings growth n/a
Yield: 2.7%
Three-year record: +1.4% a year | beta to the market 0.18
Cost and size: expense ratio 0.75% | net assets 638.50M
What it is made of: Stocks 99.7%, Cash 0.3%
Largest holdings: Al Rajhi Bank 14.1%, Saudi Arabian Oil Co 11.1%, Saudi National Bank 8.8%, Saudi Telecom Co 6.0%, Saudi Arabian Mining Co 4.4%
Sector mix: Financial services 41.9%, Basic materials 12.7%, Energy 12.1%, Communication services 8.8%
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

<details><summary><b>What analysts and big funds say</b> — score +0.65</summary>

_Not available today._

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score +0.65</summary>

```text
Rolled up from the 5 largest holdings, 44.4% of the fund by weight
Ratings by weight: buy 90.0% | hold 10.0% | sell 0.0% (mean 2.05 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +14.7% above the current prices
Holdings read: 1120.SR, 2222.SR, 1180.SR, 7010.SR, 1211.SR
Recent rating changes among them: none reported
```

</details>

<details><summary><b>Buying and selling by company insiders</b> — score +0.25</summary>

_Not available today._

</details>

<details><summary><b>Who is positioned how</b> — score +0.25</summary>

_Not available today._

</details>

<details><summary><b>Money going into and out of this fund</b> — score +0.25</summary>

_Not available today._

</details>

### China (MCHI) · Sector or country — NEUTRAL, confidence 0.25

**In the model's own words:**

> MCHI is a Greater China equity fund trading 9% below its 200-day moving average in a downtrend, with RSI at 32.8 and MACD histogram negative—technical weakness. Macro headwinds include a stronger dollar (+1.34 on the week), rising Treasury yields across the curve (notably the 5-year +0.21), and elevated VIX at 16.79. These conditions typically pressure EM equities, and China's sensitivity to dollar strength and US rate moves compounds the effect. Fund valuations are undemanding at P/E 11.9 and P/B 1.39, and the analyst consensus on the five largest holdings (32% of the fund) is unanimously buy with a +56.5% target, providing downside support. However, that analyst view is thin coverage and price targets are not binding. The fund's three-year return of +9% annually masks recent weakness (1m -5.2%, 3m -3.5%). No news catalyst appeared in the past 24 hours, and macro data surprises—the true edge for timing calls—are absent. Volume is below average, suggesting limited conviction in the move. The combination of technical oversold readings and deep valuations offers tactical appeal, but the macro backdrop (dollar, rates, China cyclical sensitivity) and absence of a clear reversal trigger prevent a higher conviction call. The risk-reward is balanced rather than directional.

**Main reasons it gave:**
- Price 9% below 200-day SMA in downtrend; RSI 32.8 and MACD negative
- US dollar +1.34 on week and Treasury 5-year +21bp pressures EM and China-exposed funds
- Fund valuation low (P/E 11.9, P/B 1.39) offers support but no catalyst to reverse technicals
- Analyst consensus buy with +56.5% target on 32% of holdings, but thin coverage (5 names) and no recent rating changes
- No macro surprise or news catalyst; volume below average

<details><summary><b>News</b> — score +0.00</summary>

_No news found for this one today._

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 3.96% (+0.16 on the week) | 5-year 4.83% (+0.21 on the week) | 10-year 4.97% (+0.14 on the week) | 30-year 5.32% (+0.03 on the week)
Yield curve, 10-year minus 3-month: +1.01 points -- upward sloping (normal)
US dollar index: 100.11 (+1.34 on the week)
Volatility (VIX): 16.79 (+0.3 on the week) -- elevated
```

</details>

<details><summary><b>Price and chart</b> — score -0.55</summary>

```text
Last close 52.22 (bar of 2026-09-16), from 502 daily bars
Trend: vs 20d SMA 54.31 (-3.9%), 50d 54.46 (-4.1%), 200d 57.36 (-9.0%); 50d below 200d
Momentum: RSI(14) 32.8 | MACD -0.561 vs signal -0.303 (histogram -0.258)
Returns: 1d -1.3% | 5d -2.1% | 1m -5.2% | 3m -3.5%
52-week range: 50.48 - 66.99 (now 10.5% of the way up)
Volatility: ATR(14) 0.60 (1.2% of price) | annualised 20d 12.9%
Volume: 0.95x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.15</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score +0.15</summary>

```text
Fund type: Greater China Region
What it holds: P/E 11.90 | P/B 1.39 | P/S 1.38 | 3y earnings growth n/a
Yield: 2.0%
Three-year record: +9.0% a year | beta to the market 0.44
Cost and size: expense ratio 0.59% | net assets 6.33B
What it is made of: Stocks 99.8%, Cash 0.2%
Largest holdings: Tencent Holdings Ltd 13.9%, Alibaba Group Holding Ltd Ordinary Shares 9.6%, China Construction Bank Corp Class H 4.0%, Industrial And Commercial Bank Of China Ltd Class H 2.5%, Xiaomi Corp Class B 2.4%
Sector mix: Consumer cyclical 23.4%, Financial services 20.0%, Communication services 18.2%, Technology 11.8%
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
Rolled up from the 5 largest holdings, 32.2% of the fund by weight
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 1.41 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +56.5% above the current prices
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

_Not available today._

</details>

### Chip makers (SMH) · Sector or country — NEUTRAL, confidence 0.25

**In the model's own words:**

> SMH faces conflicting signals that do not support a directional conviction beyond the baseline. Technicals show a deteriorating picture: the fund trades 2.5-4% below its 20- and 50-day moving averages after a 5.4% pullback over five days and an 8.5% decline over one month. Momentum has turned negative (MACD histogram -1.360, RSI 42.9 approaching oversold) on below-average volume, typical of indecision rather than decisive selling. The 12% gain over 200 days and position at 65.5% of the 52-week range suggest prior strength has faded. Macro backdrop is moderately headwindy: Treasury yields rose sharply (5-year +21bp, 3-month +16bp), the dollar rallied +1.34% on the week, and the VIX sits at elevated 16.79, all tightening financial conditions for growth assets. The yield curve remains normal (+1.01) and does not signal recession risk yet. Fund fundamentals reflect the sector's valuation: P/E 37.78, P/B 11.07, and P/S 13.20 are stretched by historical standards, and this 100% technology fund carries a 2.06 beta, amplifying both rate sensitivity and macro risk. Analyst coverage of the top 49% of holdings shows unanimous bullish ratings with a +47.6% weighted price target, but this reflects the historical positioning before recent weakness and does not address current technicals or the interest rate move. The news chatter about Taiwan supply risks, AI market concentration, and overvaluation warnings are either idiosyncratic (Taiwan), sentiment-driven (AI tug-of-war), or not actionable on a sector ETF. No specific catalyst has emerged to break the fund decisively in either direction. The recent strength in the broader market's AI narrative has not translated into upside momentum here. This is a hold pending either a macro shock that clarifies direction or a technical breakdown that confirms the weakness.

**Main reasons it gave:**
- Treasury yields rose 16-21bp across the curve, tightening conditions for high-beta growth
- Technical deterioration: -4% below 50d SMA, MACD in negative territory, RSI 42.9 on below-average volume
- Fund valuation (P/E 37.78, P/B 11.07, P/S 13.20) remains stretched despite 8.5% one-month pullback
- Analyst consensus bullish (+47.6% weighted target) but rolled up before this week's weakness
- No decisive technical or macro break; conflicting signals leave timing unclear

<details><summary><b>News</b> — score -0.15</summary>

- [New ETF Coverage: KCHP](https://247wallst.com/investing/etf/2026/09/16/new-etf-coverage-kchp/)  
  <sub>24/7 Wall St., 4 hours ago</sub>  
  A brand-new ETF just gave U.S. investors a single-ticker shortcut into South Korea's semiconductor giants, but a 0.65% fee, zero performance history,...
- [S&P 500 Warning Signs: 3 Top-Performing ETFs Caught in a $1 Trillion AI Tug-of-War](https://www.benzinga.com/etfs/broad-u-s-equity-etfs/26/09/61808469/sp-500-warning-signs-3-top-performing-etfs-caught-in-a-1-trillion-ai-tug-of-war)  
  <sub>Benzinga, 12 hours ago</sub>  
  Forecasts for the S&P 500, tracked by the SPDR S&P 500 ETF Trust (NYSE:SPY), diverge as AI dictates market direction, while specialized ETFs continue to...
- [Elon Musk Flags Taiwan as AI’s Weak Link. These Semiconductor ETFs Could Offer a Hedge](https://www.tradingview.com/news/benzinga:8d51fc1c5094b:0)  
  <sub>TradingView, 23 hours ago</sub>  
  Speaking at the All-In Summit, Elon Musk warned that existing fabs are running at full capacity and that a disruption in Taiwan could compound supply...
- [S&P 500, Nasdaq, Dow End Lower As Investors Price In Rate Hike Ahead Of Fed Meeting — AMZN, META, MU, TSLA, PLTR In Focus](https://www.tradingview.com/news/stocktwits:7a7039e74094b:0-s-p-500-nasdaq-dow-end-lower-as-investors-price-in-rate-hike-ahead-of-fed-meeting-amzn-meta-mu-tsla-pltr-in-focus/)  
  <sub>TradingView, 21 hours ago</sub>  
  U.S. stock indices fell on Tuesday as Treasury yields spiked to multi-year highs, with investors pricing in a Federal Reserve rate hike at its interest rate...
- [SMH Looks 28.7% Overvalued on GF Value™ as of September 16, 2026](https://www.gurufocus.com/news/9083925/smh-looks-287-overvalued-on-gf-value-as-of-september-16-2026)  
  <sub>GuruFocus, 4 hours ago</sub>  
  On September 16, 2026, Market Vectors Semiconductor ETF (ticker: SMH) established critical pivot points using the DeMark method, signaling potential...
- [How to Trade the Nasdaq in Light of the Fed Decision](https://uk.investing.com/analysis/how-to-trade-the-nasdaq-in-light-of-the-fed-decision-200628090)  
  <sub>Investing.com UK, 9 hours ago</sub>  
  Market Analysis by covering: Nasdaq 100, S&P 500, US Small Cap 2000, NVIDIA Corporation. Read 's Market Analysis on Investing.com UK.
- [Taiwan Semiconductor Executive Calls AI Toddler With Superpowers](https://www.tradingview.com/news/benzinga:a08b2f500094b:0)  
  <sub>TradingView, 8 hours ago</sub>  
  Taiwan Semiconductor Manufacturing Company Ltd. www.benzinga.com/quote/TSM(NYSE:TSM) stock is trading higher by more than 1% during Wednesday's premarket...
- [Micron Stock Price Target Signals 69%+ Upside Ahead of Earnings — 3 ETFs That Could Benefit](https://www.tipranks.com/news/micron-stock-price-target-signals-69-upside-ahead-of-earnings-3-etfs-that-could-benefit)  
  <sub>TipRanks, 6 hours ago</sub>  
  Memory chip company Micron ($MU) will announce its fiscal fourth-quarter earnings on September 30. The stock has been one of the standout performers in the...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score -0.15</summary>

```text
US Treasury yields: 3-month 3.96% (+0.16 on the week) | 5-year 4.83% (+0.21 on the week) | 10-year 4.97% (+0.14 on the week) | 30-year 5.32% (+0.03 on the week)
Yield curve, 10-year minus 3-month: +1.01 points -- upward sloping (normal)
US dollar index: 100.11 (+1.34 on the week)
Volatility (VIX): 16.79 (+0.3 on the week) -- elevated
```

</details>

<details><summary><b>Price and chart</b> — score -0.35</summary>

```text
Last close 543.34 (bar of 2026-09-16), from 502 daily bars
Trend: vs 20d SMA 557.21 (-2.5%), 50d 566.08 (-4.0%), 200d 485.16 (+12.0%); 50d above 200d
Momentum: RSI(14) 42.9 | MACD -5.107 vs signal -3.747 (histogram -1.360)
Returns: 1d +0.2% | 5d -5.4% | 1m -8.5% | 3m -11.8%
52-week range: 305.25 - 668.91 (now 65.5% of the way up)
Volatility: ATR(14) 16.03 (2.9% of price) | annualised 20d 31.9%
Volume: 0.59x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score -0.10</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score -0.10</summary>

```text
Fund type: Technology
What it holds: P/E 37.78 | P/B 11.07 | P/S 13.20 | 3y earnings growth n/a
Yield: 0.2%
Three-year record: +53.6% a year | beta to the market 2.06
Cost and size: expense ratio 0.35% | net assets 67.79B
What it is made of: Stocks 99.9%, Cash 0.1%
Largest holdings: NVIDIA Corp 22.6%, Taiwan Semiconductor Manufacturing Co Ltd ADR 9.7%, Broadcom Inc 6.1%, Micron Technology Inc 5.5%, Advanced Micro Devices Inc 5.4%
Sector mix: Technology 100.0%
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

<details><summary><b>What analysts and big funds say</b> — score +0.45</summary>

_Not available today._

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score +0.45</summary>

```text
Rolled up from the 5 largest holdings, 49.2% of the fund by weight
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 1.33 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +47.6% above the current prices
Holdings read: NVDA, TSM, AVGO, MU, AMD
Recent rating changes among them:
  - NVDA: 2026-09-10 Piper Sandler: init, ? -> Overweight
  - TSM: 2026-09-02 Stifel: init, ? -> Buy
  - AVGO: 2026-09-10 Piper Sandler: init, ? -> Overweight
  - MU: 2026-08-25 Mizuho: main, Outperform -> Outperform
  - AMD: 2026-09-10 Piper Sandler: init, ? -> Overweight
```

</details>

<details><summary><b>Buying and selling by company insiders</b> — score +0.05</summary>

_Not available today._

</details>

<details><summary><b>Who is positioned how</b> — score +0.05</summary>

_Not available today._

</details>

<details><summary><b>Money going into and out of this fund</b> — score +0.05</summary>

_Not available today._

</details>

### US real estate (VNQ) · Sector or country — NEUTRAL, confidence 0.25

**In the model's own words:**

> VNQ is under technical pressure with price 4.5% below its 50-day moving average, RSI at 30.4 signaling oversold conditions, and MACD histogram negative. The fund's holdings trade at elevated multiples (P/E 31.2, P/B 2.61) in a rising-rate environment where Treasury yields have moved up 14-21bps across the curve this week. The dollar has strengthened 1.34% on the week, which pressures REITs that finance in dollars. However, analyst consensus on the largest 39% of holdings is unanimously bullish with a weighted +17.5% price target, and the 3.6% yield provides income support. The yield curve remains normal and positively sloped, which is REITs-friendly. Recent rating changes are mixed: Wells Fargo downgraded Welltower (the second-largest holding at 8.5%) from Overweight to Equal-Weight on 2024-10-01, offsetting upgrades to American Tower and continued support for Prologis. The oversold technical setup creates a near-term reversal risk, but macro headwinds (higher rates, stronger dollar) and valuation concerns argue against conviction on the long side. The fund saw negative flows implied by volume at 0.89x average and three-month returns of -4.7%.

**Main reasons it gave:**
- Price 4.5% below 50-day MA with RSI 30.4 oversold but momentum negative
- Treasury yields +14-21bps on week, headwind for high-multiple REITs at P/E 31.2
- Analyst consensus on top 39% of holdings unanimously buy with +17.5% price target
- Wells Fargo downgrade of Welltower (8.5% of fund) from Overweight to Equal-Weight
- Dollar +1.34% on week, structural headwind for foreign-currency debt exposure

<details><summary><b>News</b> — score +0.00</summary>

- [IWM News | ISHARES RUSSELL 2000 ETF (NYSEARCA:IWM)](https://www.chartmill.com/stock/quote/IWM/news)  
  <sub>ChartMill, 22 hours ago</sub>  
  Latest news and press releases for ISHARES RUSSELL 2000 ETF (NYSEARCA:IWM).

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 3.96% (+0.16 on the week) | 5-year 4.83% (+0.21 on the week) | 10-year 4.97% (+0.14 on the week) | 30-year 5.32% (+0.03 on the week)
Yield curve, 10-year minus 3-month: +1.01 points -- upward sloping (normal)
US dollar index: 100.11 (+1.34 on the week)
Volatility (VIX): 16.79 (+0.3 on the week) -- elevated
```

</details>

<details><summary><b>Price and chart</b> — score -0.45</summary>

```text
Last close 93.41 (bar of 2026-09-16), from 502 daily bars
Trend: vs 20d SMA 96.52 (-3.2%), 50d 97.80 (-4.5%), 200d 94.27 (-0.9%); 50d above 200d
Momentum: RSI(14) 30.4 | MACD -1.140 vs signal -0.837 (histogram -0.304)
Returns: 1d -0.7% | 5d -1.6% | 1m -4.7% | 3m -4.7%
52-week range: 87.00 - 100.95 (now 45.9% of the way up)
Volatility: ATR(14) 1.14 (1.2% of price) | annualised 20d 10.0%
Volume: 0.89x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score -0.15</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score -0.15</summary>

```text
Fund type: Real Estate
What it holds: P/E 31.19 | P/B 2.61 | P/S 5.13 | 3y earnings growth n/a
Yield: 3.6%
Three-year record: +9.0% a year | beta to the market 0.98
Cost and size: expense ratio 0.13% | net assets 70.82B
What it is made of: Stocks 98.9%, Cash 0.8%, Other 0.4%
Largest holdings: Vanguard Real Estate II Index 14.4%, Welltower Inc 8.5%, Prologis Inc 7.0%, Equinix Inc 5.2%, American Tower Corp 4.2%
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

<details><summary><b>What analysts and big funds say</b> — score +0.55</summary>

_Not available today._

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score +0.55</summary>

```text
Rolled up from the 5 largest holdings, 39.2% of the fund by weight
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 1.71 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +17.5% above the current prices
Holdings read: VRTPX, WELL, PLD, EQIX, AMT
Recent rating changes among them:
  - WELL: 2024-10-01 Wells Fargo: down, Overweight -> Equal-Weight
  - PLD: 2026-09-01 Wells Fargo: main, Overweight -> Overweight
  - EQIX: 2026-09-10 BTIG: main, Buy -> Buy
  - AMT: 2026-08-20 Barclays: up, Equal-Weight -> Overweight
```

</details>

<details><summary><b>Buying and selling by company insiders</b> — score -0.35</summary>

_Not available today._

</details>

<details><summary><b>Who is positioned how</b> — score -0.35</summary>

_Not available today._

</details>

<details><summary><b>Money going into and out of this fund</b> — score -0.35</summary>

_Not available today._

</details>

### US materials and chemicals (XLB) · Sector or country — NEUTRAL, confidence 0.25

**In the model's own words:**

> XLB has sold off 4.1% over the past month and is trading 4.1% below its 20-day moving average, with RSI at 34.8 and MACD below signal line, signaling oversold momentum. However, the technical weakness is not yet accompanied by a decisive break—the fund remains 68.8% of the way up its 52-week range and only 0.5% below its 200-day MA. Macro backdrop shows Treasury yields rising across the curve this week (3-month +16bp, 5-year +21bp, 10-year +14bp) with the yield curve normalizing to +1.01 points, and the dollar strengthening (+1.34 on the week). The VIX has ticked up modestly to 16.79. These moves are modest, not a clear surprise, and do not yet constitute a macro regime shift. Analyst consensus on the largest holdings remains constructively weighted—100% buy-rated by weight with a +14.2% upside target, though this rollup covers only 37% of the fund. The fund's valuation multiples (P/E 24.59, P/B 3.00) are elevated and could compress in a rising-rate environment. Volume is below average, suggesting weak conviction on either side. The combination of technical oversold conditions and positive analyst sentiment argues against a bearish call, but the rising yield curve and elevated valuations prevent a bullish stance. A near-term bounce from oversold is possible, but the macro backdrop does not yet support a directional conviction.

**Main reasons it gave:**
- RSI 34.8 and MACD histogram -0.321 signal oversold momentum
- 50d MA above 200d MA and fund within 0.5% of 200d support
- Analyst consensus +14.2% target on 37% of holdings but rollup coverage thin
- Treasury yields up 14-21bp on the week with dollar +1.34; rising-rate regime pressure on materials valuations
- Volume 0.6x average reflects weak conviction on either side of recent selloff

<details><summary><b>News</b> — score +0.00</summary>

- [Leading And Lagging Sectors For September 16, 2026](https://www.benzinga.com/etfs/sector-etfs/26/09/61814178/leading-and-lagging-sectors-september-16-2026)  
  <sub>Benzinga, 6 hours ago</sub>  
  Gainers Symbol Name Price Change ($) Change (%) Volume (NYSE:XLK) State Street Technology Select Sector SPDR ETF 184.7100 0.970 0.52 122.1K (NYSE:XLI) State...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 3.96% (+0.16 on the week) | 5-year 4.83% (+0.21 on the week) | 10-year 4.97% (+0.14 on the week) | 30-year 5.32% (+0.03 on the week)
Yield curve, 10-year minus 3-month: +1.01 points -- upward sloping (normal)
US dollar index: 100.11 (+1.34 on the week)
Volatility (VIX): 16.79 (+0.3 on the week) -- elevated
```

</details>

<details><summary><b>Price and chart</b> — score -0.35</summary>

```text
Last close 50.10 (bar of 2026-09-16), from 502 daily bars
Trend: vs 20d SMA 52.24 (-4.1%), 50d 51.76 (-3.2%), 200d 50.34 (-0.5%); 50d above 200d
Momentum: RSI(14) 34.8 | MACD -0.447 vs signal -0.126 (histogram -0.321)
Returns: 1d -1.2% | 5d -2.5% | 1m -4.1% | 3m -5.0%
52-week range: 42.23 - 53.67 (now 68.8% of the way up)
Volatility: ATR(14) 0.78 (1.6% of price) | annualised 20d 15.7%
Volume: 0.60x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.15</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score +0.15</summary>

```text
Fund type: Natural Resources
What it holds: P/E 24.59 | P/B 3.00 | P/S 2.01 | 3y earnings growth n/a
Yield: 1.6%
Three-year record: +9.0% a year | beta to the market 0.82
Cost and size: expense ratio 0.08% | net assets 8.75B
What it is made of: Stocks 99.9%, Cash 0.1%
Largest holdings: Linde PLC 13.1%, Newmont Corp 7.8%, Freeport-McMoRan Inc 6.3%, Corteva Inc 4.9%, Air Products and Chemicals Inc 4.8%
Sector mix: Basic materials 84.5%, Consumer cyclical 15.5%
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

<details><summary><b>What analysts and big funds say</b> — score +0.50</summary>

_Not available today._

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score +0.50</summary>

```text
Rolled up from the 5 largest holdings, 37.0% of the fund by weight
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 1.72 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +14.2% above the current prices
Holdings read: LIN, NEM, FCX, CTVA, APD
Recent rating changes among them:
  - LIN: 2026-09-11 Keybanc: init, ? -> Overweight
  - NEM: 2026-09-16 RBC Capital: main, Outperform -> Outperform
  - FCX: 2026-09-16 RBC Capital: main, Sector Perform -> Sector Perform
  - CTVA: 2026-09-16 BMO Capital: main, Outperform -> Outperform
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

_Not available today._

</details>

### US media and communication (XLC) · Sector or country — NEUTRAL, confidence 0.25

**In the model's own words:**

> XLC shows modestly positive technicals with a price above key moving averages and positive MACD momentum, plus analyst consensus strongly bullish on its 45% of holdings by weight at a +15.9% weighted target. However, conviction is low because macro backdrop has shifted materially: the curve normalized and steepened only this week, Treasury yields rose across the board (especially 5y +21bp), the dollar strengthened sharply (+1.34%), and the VIX sits at 16.79, all of which compress valuations in growth-heavy tech and comms stocks. The fund's beta of 0.85 and P/E of 15.38 are reasonable but not cheap, and the recent rally has been modest (1m +2.4%, 3m +1.0%) with volume below average. A TipRanks mention citing 10%+ upside appears to be generic promotional content, not a fresh catalyst. The technicals do not show conviction—RSI at 55 is neutral, ATR at 1.4% of price is low—and the macro week was a headwind. This is a defensively-rated communication services basket in a rising-rate, rising-dollar environment with modest price momentum and no fresh data catalyst. The analyst bullishness and reasonable valuation do not offset the macro shift without more corroborating evidence of demand. NEUTRAL reflects this balance: not a sell, but not a compelling entry on current evidence.

**Main reasons it gave:**
- Analyst consensus 100% buy on 45.5% of holdings, weighted price target +15.9%
- Treasury curve steepened and yields rose sharply this week, headwind for growth valuations
- Dollar strengthened 1.34% on the week, pressure on comms sector with international exposure
- Price momentum modest over 1m and 3m, volume below 20-day average, RSI neutral at 55
- P/E 15.38 and P/B 2.92 reasonable but not compelling at rising rates

<details><summary><b>News</b> — score +0.00</summary>

- [3 ETFs with 10%+ Upside for Tech, Banking, and Telecom Exposure, According to AI Analyst](https://www.tipranks.com/news/3-etfs-with-10-upside-for-tech-banking-and-telecom-exposure-according-to-ai-analyst)  
  <sub>TipRanks, 23 hours ago</sub>  
  TipRanks' AI analyst rates FlexShares Quality Dividend Index Fund ($QDF), SPDR SP Bank ETF ($KBE), and Communication Services Select Sector SPDR Fund ($XLC)...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 3.96% (+0.16 on the week) | 5-year 4.83% (+0.21 on the week) | 10-year 4.97% (+0.14 on the week) | 30-year 5.32% (+0.03 on the week)
Yield curve, 10-year minus 3-month: +1.01 points -- upward sloping (normal)
US dollar index: 100.11 (+1.34 on the week)
Volatility (VIX): 16.79 (+0.3 on the week) -- elevated
```

</details>

<details><summary><b>Price and chart</b> — score +0.35</summary>

```text
Last close 113.49 (bar of 2026-09-16), from 502 daily bars
Trend: vs 20d SMA 112.26 (+1.1%), 50d 111.13 (+2.1%), 200d 114.04 (-0.5%); 50d below 200d
Momentum: RSI(14) 55.1 | MACD 0.643 vs signal 0.480 (histogram 0.163)
Returns: 1d -0.5% | 5d +2.4% | 1m +2.4% | 3m +1.0%
52-week range: 105.38 - 120.08 (now 55.2% of the way up)
Volatility: ATR(14) 1.64 (1.4% of price) | annualised 20d 16.1%
Volume: 0.72x the 20-day average
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
Three-year record: +20.3% a year | beta to the market 0.85
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

<details><summary><b>What analysts and big funds say</b> — score +0.55</summary>

_Not available today._

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score +0.55</summary>

```text
Rolled up from the 5 largest holdings, 45.5% of the fund by weight
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 1.55 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +15.9% above the current prices
Holdings read: META, GOOGL, GOOG, T, VZ
Recent rating changes among them:
  - META: 2024-09-30 Cantor Fitzgerald: reit, Overweight -> Overweight
  - GOOGL: 2026-09-03 Rosenblatt: main, Buy -> Buy
  - GOOG: 2026-07-23 JP Morgan: main, Overweight -> Overweight
  - T: 2026-07-23 Wolfe Research: up, Peer Perform -> Outperform
  - VZ: 2026-07-27 TD Cowen: main, Buy -> Buy
```

</details>

<details><summary><b>Buying and selling by company insiders</b> — score +0.00</summary>

_Not available today._

</details>

<details><summary><b>Who is positioned how</b> — score +0.00</summary>

_Not available today._

</details>

<details><summary><b>Money going into and out of this fund</b> — score +0.00</summary>

_Not available today._

</details>

### US energy companies (XLE) · Sector or country — NEUTRAL, confidence 0.25

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> XLE sits near the top of its 52-week range after a +16% three-month run, but momentum is rolling over (MACD below signal, -2.6% on the day on 1.3x volume) as crude fell 3.6% on the Saudi pipeline restart. The macro backdrop is hostile at the margin: yields up across the curve, dollar +1.34 on the week, and a Fed hike expected -- though that is broadly anticipated rather than a surprise. Analyst roll-up covers just over half the fund and is uniformly buy-rated but with only +2.4% weighted upside, i.e. priced. Heavy put activity noted in one headline is unverified single-source colour. Nothing here is a decisive enough macro catalyst to take a side with conviction.

**Main reasons it gave:**
- Crude -3.6% on Saudi pipeline restart; XLE -2.6% on 1.3x average volume
- Price 92.5% up the 52-week range with MACD histogram negative (-0.138)
- Yields higher across curve (5y +21bp, 10y +14bp) and DXY +1.34 into an expected Fed hike
- Analyst roll-up 100% buy but only +2.4% weighted upside, covering 51.7% of fund
- Oil stocks lagging a 20% crude rally per multiple reports

<details><summary><b>News</b> — score -0.20</summary>

- [Fed Most Likely to Hike Rates After 3 Years: ETFs to Win/Lose](https://www.google.com/goto?url=CAESrAEB6zswFeKbQLf7KACeoEJwR-x1_LOLbaYgzHSy4K_jDpPO8sz6Rc3lvy4K8HCYwC64JPUoEoUqhnKwUgrIQy81pvAc_MLeSje2dpmTZth-1cub11jfPikVMZYVPOQ5knHfb6XRdVOlEUx3vEOkBlY8c7VZX0OqwSatW2UP-DWd-3LPFrS7v2KiNrvumDPAdwMUC8AxAwdVMqGyghaQ8aZgsAzm-jYpAl153nr1)  
  <sub>TradingView, 6 hours ago</sub>  
  The Federal Reserve's September policy meeting kicked off Tuesday, and markets are widely expecting a 25-basis-point rate hike on Wednesday.
- [Chart Of The Day: Oil? Surging. Oil Stocks? Not So Much](https://seekingalpha.com/article/4946880-chart-of-day-oil-surging-oil-stocks-not-so-much)  
  <sub>Seeking Alpha, 9 hours ago</sub>  
  Both WTI and Brent futures have surged by more than 20% in just a few weeks. But interestingly, oil stocks have been lagging behind. Read more here...
- [(09/16/26) Chart of the Day 9/16/26: Oil? Surging. Oil Stocks? Not So Much.](https://www.google.com/goto?url=CAESqQEB6zswFW0wFzMpTXLNPgF0IMK3osFSvAIo1gZtgSsLErtZKy6MJPznQUxNRVsuVrwXVPJdPbPCQLEvNfc4BHGMVcLcdfxMUwvPSGh3SSonsoZBru89BbB8tH5dHYr1Sg8kq9UA_-mnGGGnGHDZLLMY7ZYDB0EFAZt_sdHy0Q8v44OjVsW5P6-0qXFn0RPiO9Rf4dXnRpvM6MTEPfIVFNFVZYyVvNsmv1pV)  
  <sub>www.moneyshow.com, 14 hours ago</sub>  
  We have a run for the ages underway in crude oil. Both WTI and Brent futures have surged by more than 20% in just a few weeks. But interestingly, oil stocks...
- [How to Trade the Nasdaq in Light of the Fed Decision](https://uk.investing.com/analysis/how-to-trade-the-nasdaq-in-light-of-the-fed-decision-200628090)  
  <sub>Investing.com UK, 9 hours ago</sub>  
  Market Analysis by covering: Nasdaq 100, S&P 500, US Small Cap 2000, NVIDIA Corporation. Read 's Market Analysis on Investing.com UK.
- [Futures Traders Betting On 12% Drop In Energy Stocks Over Next Month](https://www.google.com/goto?url=CAESpwEB6zswFbJPSmDwmGfc4BkSgl5ZZYJPrq3FWEo-jpnklqP54P-ff2g2dqUUrkcKHA965u73Vsx4eavauXpZSKkTnLFys6az9fXlfi7so7LzC3kpkvIHNA3LVRIk0_AvUnfuxWXoUnJBc47YTqLG_-e5cKph1ruV0uHgcy91u_BySe_D4oJmL1LBli0AoqkAwTM56GD22CjA9RprUH2tnkMJXYUTPLB7nw)  
  <sub>24/7 Wall St., 28 minutes ago</sub>  
  Energy is the year's best-performing sector, and on Wednesday the options market bet heavily that it is about to break. Volume in Energy Select Sector SPDR...
- [Diesel Export Ban May Be Good for U.S.; Fed Predictions; My 3 Energy Stocks](https://pro.thestreet.com/market-commentary/diesel-export-ban-may-be-good-for-u-s-fed-predictions-my-3-energy-stocks)  
  <sub>TheStreet Pro, 5 hours ago</sub>  
  Will the diesel export bans help U.S. pricing? Also, why a half-point hike could actually make sense, but why confusion will likely prevail.
- [S&P 500 Gains, Crude Falls Ahead Of Fed's Expected First Hike Since 2023: Stock Market Today](https://www.benzinga.com/markets/market-summary/26/09/61822672/oil-sinks-below-103-optics-stocks-rip-fed-first-hike-since-2023-markets-wednesday)  
  <sub>Benzinga, 2 hours ago</sub>  
  Crude tumbles 3.6% on a Saudi pipeline restart, easing yields and lifting chips, while the Fed prepares its first rate hike in nearly three years.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score -0.20</summary>

```text
US Treasury yields: 3-month 3.96% (+0.16 on the week) | 5-year 4.83% (+0.21 on the week) | 10-year 4.97% (+0.14 on the week) | 30-year 5.32% (+0.03 on the week)
Yield curve, 10-year minus 3-month: +1.01 points -- upward sloping (normal)
US dollar index: 100.11 (+1.34 on the week)
Volatility (VIX): 16.79 (+0.3 on the week) -- elevated
```

</details>

<details><summary><b>Price and chart</b> — score -0.10</summary>

```text
Last close 64.19 (bar of 2026-09-16), from 502 daily bars
Trend: vs 20d SMA 64.04 (+0.2%), 50d 60.81 (+5.6%), 200d 55.54 (+15.6%); 50d above 200d
Momentum: RSI(14) 55.4 | MACD 1.216 vs signal 1.354 (histogram -0.138)
Returns: 1d -2.6% | 5d -1.7% | 1m +2.6% | 3m +16.0%
52-week range: 42.61 - 65.93 (now 92.5% of the way up)
Volatility: ATR(14) 1.33 (2.1% of price) | annualised 20d 18.8%
Volume: 1.30x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.10</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score +0.10</summary>

```text
Fund type: Equity Energy
What it holds: P/E 17.74 | P/B 2.58 | P/S 1.68 | 3y earnings growth n/a
Yield: 2.4%
Three-year record: +15.0% a year | beta to the market -0.07
Cost and size: expense ratio 0.08% | net assets 41.44B
What it is made of: Stocks 99.8%, Cash 0.2%
Largest holdings: ExxonMobil Holdings Corp 19.9%, Chevron Corp 14.9%, ConocoPhillips 6.2%, Marathon Petroleum Corp 5.4%, Phillips 66 5.3%
Sector mix: Energy 100.0%
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
Rolled up from the 5 largest holdings, 51.7% of the fund by weight
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 2.05 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +2.4% above the current prices
Holdings read: XOM, CVX, COP, MPC, PSX
Recent rating changes among them:
  - XOM: 2026-09-03 Piper Sandler: main, Neutral -> Neutral
  - CVX: 2026-09-03 BMO Capital: main, Outperform -> Outperform
  - COP: 2026-09-14 UBS: main, Buy -> Buy
  - MPC: 2026-09-14 Raymond James: main, Outperform -> Outperform
  - PSX: 2026-09-14 Raymond James: main, Outperform -> Outperform
```

</details>

<details><summary><b>Buying and selling by company insiders</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>Who is positioned how</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>Money going into and out of this fund</b> — score n/a</summary>

_Not available today._

</details>

### US banks and finance (XLF) · Sector or country — NEUTRAL, confidence 0.25

**In the model's own words:**

> XLF faces conflicting signals that balance to neutral. Technicals show weakness: price is 2.9% below the 20-day SMA, RSI at 37 signals oversold conditions, MACD histogram deeply negative at -0.236, and the fund has declined 3% over one month despite a +4.1% gain versus the 200-day MA. Macro backdrop is mixed: the Fed has tightened conditions with short rates rising 16bp this week and the dollar strengthening sharply (+1.34%), both pressuring net interest margins for banks. News explicitly cites inflation and rising rates squeezing bank profitability. However, the yield curve remains normal at +101bp, which supports lending spreads, and the three-year holdings beta of 0.71 offers some defensive shelter. Analyst consensus on the five largest holdings (41.5% of fund) is unanimously bullish with an 11% price target upside, though this is thin coverage relative to the full portfolio and reflects a lagged view. The fund's valuation at 16.36x P/E is reasonable but not compelling given the macro headwinds. The recent 2.3% overvaluation estimate and -2.1% five-day decline suggest profit-taking into softness. No clear catalyst emerges to break either way in the near term; positioning data is unavailable to assess sentiment. The technical setup argues for caution, but analyst targets and the fund's defensive beta prevent a bearish call.

**Main reasons it gave:**
- Price 2.9% below 20-day SMA with RSI 37 and negative MACD histogram signals short-term weakness
- Short rates +16bp on week and dollar +1.34% compress bank NIM and weigh on sector
- Analyst consensus on 41.5% of holdings unanimously bullish with +11% price target despite thin coverage
- Yield curve normal at +101bp supports lending spreads but macro tightening limits upside
- Fund declined 3% over one month; no positioning data available to confirm flow conviction

<details><summary><b>News</b> — score -0.25</summary>

- [Midterms Won't Settle Washington's Volatility](https://www.etftrends.com/sector-investing-content-hub/midterms-washington-volatility/)  
  <sub>ETF Trends, 7 hours ago</sub>  
  Political volatility should stay elevated even after Democrats retake the House this November, State Street Investment Management said.
- [XLF Looks 2.3% Overvalued on GF Value™ as of September 16, 2026](https://www.gurufocus.com/news/9083926/xlf-looks-23-overvalued-on-gf-value-as-of-september-16-2026)  
  <sub>GuruFocus, 4 hours ago</sub>  
  On September 16, 2026, new pivot points derived from the DeMark methodology have been established for the Financial Select Sector SPDR ETF (ticker: XLF),...
- [Why Are Bank Stocks Selling Off? Look To Inflation (NYSEARCA:KBE)](https://seekingalpha.com/article/4946775-why-are-bank-stocks-selling-off-look-to-inflation?source=generic_rss)  
  <sub>Seeking Alpha, 20 hours ago</sub>  
  Bank stocks face inflation, rising rates, and debt-market uncertainty squeezing net interest margins—click to get insights on Fed policy and what to watch...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score -0.25</summary>

```text
US Treasury yields: 3-month 3.96% (+0.16 on the week) | 5-year 4.83% (+0.21 on the week) | 10-year 4.97% (+0.14 on the week) | 30-year 5.32% (+0.03 on the week)
Yield curve, 10-year minus 3-month: +1.01 points -- upward sloping (normal)
US dollar index: 100.11 (+1.34 on the week)
Volatility (VIX): 16.79 (+0.3 on the week) -- elevated
```

</details>

<details><summary><b>Price and chart</b> — score -0.40</summary>

```text
Last close 55.87 (bar of 2026-09-16), from 502 daily bars
Trend: vs 20d SMA 57.51 (-2.9%), 50d 57.15 (-2.3%), 200d 53.66 (+4.1%); 50d above 200d
Momentum: RSI(14) 37.0 | MACD -0.142 vs signal 0.094 (histogram -0.236)
Returns: 1d -1.7% | 5d -2.1% | 1m -3.0% | 3m +2.8%
52-week range: 47.81 - 58.56 (now 74.9% of the way up)
Volatility: ATR(14) 0.69 (1.2% of price) | annualised 20d 13.9%
Volume: 0.94x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score -0.15</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score -0.15</summary>

```text
Fund type: Financial
What it holds: P/E 16.36 | P/B 2.42 | P/S 3.50 | 3y earnings growth n/a
Yield: 1.4%
Three-year record: +19.5% a year | beta to the market 0.71
Cost and size: expense ratio 0.08% | net assets 54.59B
What it is made of: Stocks 99.8%, Cash 0.2%
Largest holdings: JPMorgan Chase & Co 11.7%, Berkshire Hathaway Inc Class B 11.3%, Visa Inc Class A 7.7%, Mastercard Inc Class A 5.8%, Bank of America Corp 5.0%
Sector mix: Financial services 98.1%, Technology 1.6%, Industrials 0.3%
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

<details><summary><b>What analysts and big funds say</b> — score +0.50</summary>

_Not available today._

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score +0.50</summary>

```text
Rolled up from the 5 largest holdings, 41.5% of the fund by weight
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 1.72 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +11.0% above the current prices
Holdings read: JPM, BRK-B, V, MA, BAC
Recent rating changes among them:
  - JPM: 2026-08-14 Wells Fargo: main, Overweight -> Overweight
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

_Not available today._

</details>

### US technology (XLK) · Sector or country — NEUTRAL, confidence 0.25

**In the model's own words:**

> XLK is a high-beta technology fund (beta 1.50) trading at stretched valuations (P/E 33.01, P/B 11.41) in an environment where macro momentum is turning less supportive. The Fed is widely expected to hike rates Wednesday, and Treasury yields have risen across the curve this week—3-month up 16bp, 5-year up 21bp—pushing real yields higher in an already elevated rate regime. This is headwind for richly-valued growth. Technicals show the fund near its 52-week highs (79.4% of range) with momentum divergence: RSI at 47.7 and MACD histogram negative despite price strength. The fund is down 3.5% over the past month and 2.2% over the past five days, showing recent weakness even as it sits near peaks. Analyst sentiment on the top 45.7% of holdings is uniformly bullish (100% buy, +31.7% price target), but this unanimous view reflects positioning risk rather than edge and is already priced. Fund flows and positioning data are absent, limiting conviction in either direction. The news flow is generic sector chatter with no specific catalyst to XLK itself. While the three-year record of +29.7% annual returns demonstrates the fund's historical strength and the holdings remain fundamentally sound, the combination of elevated valuations, rising rates, negative momentum divergence, and near-term weakness does not support a bullish lean at current levels. A data surprise or technical breakdown would be needed to tip conviction higher; absent that, the weight of evidence tilts slightly defensive without justifying a bearish call.

**Main reasons it gave:**
- Treasury yields up 16-21bp across the curve this week into Fed hike
- P/E 33.01 and P/B 11.41 valuations vulnerable to higher rates
- MACD histogram negative and RSI 47.7 show momentum divergence despite price near 52-week highs
- Fund down 2.2% in past 5 days and 3.5% in past month despite near-peak positioning
- Analyst roll-up 100% buy with +31.7% target reflects consensus positioning risk

<details><summary><b>News</b> — score +0.00</summary>

- [Amplify Makes Plans to Take Over TACK ETF: What to Know](https://www.etftrends.com/equity-etf-content-hub/amplify-makes-plans-take-over-tack-etf-what-to-know/)  
  <sub>ETF Trends, 2 hours ago</sub>  
  Change may very well be on the horizon for the Fairlead Tactical Sector ETF (TACK). Key Takeaways: Proposed plans were recently approved for Amplify...
- [Fed Most Likely to Hike Rates After 3 Years: ETFs to Win/Lose](https://www.tradingview.com/news/zacks:cca1fd804094b:0-fed-most-likely-to-hike-rates-after-3-years-etfs-to-win-lose/)  
  <sub>TradingView, 6 hours ago</sub>  
  The Federal Reserve's September policy meeting kicked off Tuesday, and markets are widely expecting a 25-basis-point rate hike on Wednesday.
- [E-mini NASDAQ 100 Futures (DEC6) Price Trend Today | Quotes & News](https://www.moomoo.com/stock/NQmain-US?chain_id=Name1K9-3FXPhg.1lak1hg&global_content=%7B%22promote_id%22%3A13764%2C%22sub_promote_id%22%3A107%2C%22f%22%3A%22www.moomoo.com%2Fetfs%2FXLK-US%22%7D)  
  <sub>Moomoo, 16 hours ago</sub>  
  Get today's E-mini NASDAQ 100 Futures (DEC6) price trend, live quotes, charts, news and historical data on moomoo for your futures trading.
- [Should You Invest in the First Trust Technology AlphaDEX ETF (FXL)?](https://finance.yahoo.com/markets/stocks/articles/invest-first-trust-technology-alphadex-102001745.html)  
  <sub>Yahoo Finance, 9 hours ago</sub>  
  Looking for broad exposure to the Technology - Broad segment of the equity market? You should consider the First Trust Technology AlphaDEX ETF (FXL),...
- [Midterms Won't Settle Washington's Volatility](https://www.etftrends.com/sector-investing-content-hub/midterms-washington-volatility/)  
  <sub>ETF Trends, 7 hours ago</sub>  
  Political volatility should stay elevated even after Democrats retake the House this November, State Street Investment Management said.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 3.96% (+0.16 on the week) | 5-year 4.83% (+0.21 on the week) | 10-year 4.97% (+0.14 on the week) | 30-year 5.32% (+0.03 on the week)
Yield curve, 10-year minus 3-month: +1.01 points -- upward sloping (normal)
US dollar index: 100.11 (+1.34 on the week)
Volatility (VIX): 16.79 (+0.3 on the week) -- elevated
```

</details>

<details><summary><b>Price and chart</b> — score -0.15</summary>

```text
Last close 183.65 (bar of 2026-09-16), from 502 daily bars
Trend: vs 20d SMA 184.81 (-0.6%), 50d 182.89 (+0.4%), 200d 161.98 (+13.4%); 50d above 200d
Momentum: RSI(14) 47.7 | MACD 0.395 vs signal 0.762 (histogram -0.368)
Returns: 1d -0.0% | 5d -2.2% | 1m -3.5% | 3m -1.5%
52-week range: 127.50 - 198.21 (now 79.4% of the way up)
Volatility: ATR(14) 3.35 (1.8% of price) | annualised 20d 19.9%
Volume: 0.95x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score -0.25</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score -0.25</summary>

```text
Fund type: Technology
What it holds: P/E 33.01 | P/B 11.41 | P/S 8.77 | 3y earnings growth n/a
Yield: 0.4%
Three-year record: +29.7% a year | beta to the market 1.50
Cost and size: expense ratio 0.08% | net assets 121.44B
What it is made of: Stocks 100.0%, Cash 0.0%
Largest holdings: NVIDIA Corp 14.4%, Apple Inc 12.5%, Microsoft Corp 10.1%, Broadcom Inc 4.7%, Micron Technology Inc 4.0%
Sector mix: Technology 100.0%
```

</details>

<details><summary><b>Does this company beat its own forecasts</b> — score -0.25</summary>

_Not available today._

</details>

<details><summary><b>What holding this fund costs you</b> — score -0.25</summary>

_Not available today._

</details>

<details><summary><b>How much oil and gas is in storage</b> — score -0.25</summary>

_Not available today._

</details>

<details><summary><b>How the crop is growing</b> — score -0.25</summary>

_Not available today._

</details>

<details><summary><b>What analysts and big funds say</b> — score +0.55</summary>

_Not available today._

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score +0.55</summary>

```text
Rolled up from the 5 largest holdings, 45.7% of the fund by weight
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 1.56 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +31.7% above the current prices
Holdings read: NVDA, AAPL, MSFT, AVGO, MU
Recent rating changes among them:
  - NVDA: 2026-09-10 Piper Sandler: init, ? -> Overweight
  - AAPL: 2026-09-10 TD Cowen: reit, Buy -> Buy
  - MSFT: 2026-09-15 Citizens: reit, Market Outperform -> Market Outperform
  - AVGO: 2026-09-10 Piper Sandler: init, ? -> Overweight
  - MU: 2026-08-25 Mizuho: main, Outperform -> Outperform
```

</details>

<details><summary><b>Buying and selling by company insiders</b> — score +0.00</summary>

_Not available today._

</details>

<details><summary><b>Who is positioned how</b> — score +0.00</summary>

_Not available today._

</details>

<details><summary><b>Money going into and out of this fund</b> — score +0.00</summary>

_Not available today._

</details>

### US everyday goods (XLP) · Sector or country — NEUTRAL, confidence 0.25

**In the model's own words:**

> XLP is a defensive consumer staples fund with a low-volatility profile (beta 0.49) that is currently showing weakness on a backdrop of rising Treasury yields and a strengthening dollar. The technical picture is decidedly mixed: the fund is trading below all major moving averages, momentum has turned negative (RSI 42.7, MACD below signal), and volume is subpar, suggesting distribution. However, fundamentals and analyst sentiment remain supportive. Analyst coverage of the top 39.6% of holdings shows 100% buy ratings with a +13.1% upside target, and the fund's 2.6% yield provides ballast. The recent weakness appears tactical rather than strategic—a consumer defensive fund typically outperforms in risk-off environments, yet broader market volatility (VIX 16.79) remains merely elevated rather than spiking, and the yield curve is normal. Macro headwinds—higher rates across the curve this week, dollar strength—are modest cyclical pressures that typically challenge staples less than they challenge cyclicals or discretionary. The news flow is noise: intraday sector mentions and comparisons to other funds provide no directional signal. Without a clear catalyst—neither a macro shock nor a technical reversal—the prudent call is to wait. The divergence between technicals (bearish) and fundamentals (bullish) with weak conviction on both sides supports neutrality.

**Main reasons it gave:**
- Price below 20d, 50d, and 200d SMAs with negative momentum (RSI 42.7, MACD histogram -0.188)
- Top 5 holdings 100% buy-rated by analysts with +13.1% upside target
- Treasury yields up 14-21 bps across curve; USD strengthened 1.34% on the week
- Volume at 0.60x 20-day average with 1-month drawdown of -1.4%
- Fund yield 2.6% and low beta 0.49 provide defensive characteristics amid mixed signals

<details><summary><b>News</b> — score +0.00</summary>

- [Leading And Lagging Sectors For September 16, 2026](https://www.benzinga.com/etfs/sector-etfs/26/09/61814178/leading-and-lagging-sectors-september-16-2026)  
  <sub>Benzinga, 6 hours ago</sub>  
  Gainers Symbol Name Price Change ($) Change (%) Volume (NYSE:XLK) State Street Technology Select Sector SPDR ETF 184.7100 0.970 0.52 122.1K (NYSE:XLI) State...
- [Sector Update: Consumer Stocks Fall Late Afternoon](https://www.bitget.com/amp/news/detail/12560605838118)  
  <sub>Bitget, 19 hours ago</sub>  
  03:49 PM EDT, 09/15/2026 (MT Newswires) -- Consumer stocks fell late Tuesday afternoon with the State Street Consumer Staples Select Sector SPDR ETF (XLP) d...
- [Sector Update: Consumer Stocks Fall Tuesday Afternoon](https://www.bitget.com/amp/news/detail/12560605837916)  
  <sub>Bitget, 18 hours ago</sub>  
  01:46 PM EDT, 09/15/2026 (MT Newswires) -- Consumer stocks fell Tuesday afternoon with the State Street Consumer Staples Select Sector SPDR ETF (XLP) droppi...
- [Sector Update: Consumer](https://www.bitget.com/amp/news/detail/12560605837871)  
  <sub>Bitget, 22 hours ago</sub>  
  01:15 PM EDT, 09/15/2026 (MT Newswires) -- Consumer stocks fell Tuesday afternoon with the State Street Consumer Staples Select Sector SPDR ETF (XLP) droppi...
- [Washington's Volatility Won't Settle From Midterms](https://etfdb.com/sector-investing-content-hub/washington-volatility-settle-midterms/)  
  <sub>ETF Database, 5 hours ago</sub>  
  Divided government looks likely, but historical midterm returns offer no reliable signal. Health care, utilities and financials could see targeted relief as...
- [XLV Looks 0.4% Overvalued on GF Value™](https://www.gurufocus.com/news/9083929/xlv-looks-04-overvalued-on-gf-value)  
  <sub>GuruFocus, 4 hours ago</sub>  
  On September 16, 2026, traders are closely watching the pivot points identified for the State Street Health Care Select Sector SPDR ETF (ticker: XLV).
- [MO Stock: Altria Returned Billions To Shareholders. What’s The Catch?](https://www.trefis.com/stock/mo/articles/615332/mo-stock-altria-returned-billions-to-shareholders-whats-the-catch/2026-09-15)  
  <sub>Trefis, 17 hours ago</sub>  
  A tobacco giant sent a torrent of cash back to its owners. Here's what that money actually bought, and what has to go right for the checks to keep coming.
- [Biotech Midweek Pulse: XBI Loses Steam After Hot 2026 Run — Here Are The Stocks And Catalysts To Watch Next](https://www.tradingview.com/news/stocktwits:ee8d9b8aa094b:0-biotech-midweek-pulse-xbi-loses-steam-after-hot-2026-run-here-are-the-stocks-and-catalysts-to-watch-next/)  
  <sub>TradingView, 17 hours ago</sub>  
  Biotech's 2026 rally cooled this week even as drug developers delivered major clinical updates. Definium Therapeutics (DFTX), Vera Therapeutics (VERA) and...
- [XLY Looks 4.8% Undervalued on GF Value™ as Pivot Points Signal K](https://www.gurufocus.com/news/9083935/xly-looks-48-undervalued-on-gf-value-as-pivot-points-signal-key-technical-levels)  
  <sub>GuruFocus, 6 hours ago</sub>  
  On September 16, 2026, the Consumer Discretionary Sector SPDR (ticker: XLY) established critical pivot points using the DeMark analysis methodology,...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 3.96% (+0.16 on the week) | 5-year 4.83% (+0.21 on the week) | 10-year 4.97% (+0.14 on the week) | 30-year 5.32% (+0.03 on the week)
Yield curve, 10-year minus 3-month: +1.01 points -- upward sloping (normal)
US dollar index: 100.11 (+1.34 on the week)
Volatility (VIX): 16.79 (+0.3 on the week) -- elevated
```

</details>

<details><summary><b>Price and chart</b> — score -0.35</summary>

```text
Last close 83.52 (bar of 2026-09-16), from 502 daily bars
Trend: vs 20d SMA 84.97 (-1.7%), 50d 84.95 (-1.7%), 200d 83.54 (-0.0%); 50d above 200d
Momentum: RSI(14) 42.7 | MACD -0.468 vs signal -0.280 (histogram -0.188)
Returns: 1d -0.3% | 5d +0.6% | 1m -1.4% | 3m -2.4%
52-week range: 75.60 - 90.01 (now 55.0% of the way up)
Volatility: ATR(14) 1.02 (1.2% of price) | annualised 20d 14.2%
Volume: 0.60x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.25</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score +0.25</summary>

```text
Fund type: Consumer Defensive
What it holds: P/E 25.14 | P/B 4.58 | P/S 1.36 | 3y earnings growth n/a
Yield: 2.6%
Three-year record: +8.0% a year | beta to the market 0.49
Cost and size: expense ratio 0.08% | net assets 14.52B
What it is made of: Stocks 99.9%, Cash 0.1%
Largest holdings: Walmart Inc 9.8%, Costco Wholesale Corp 8.9%, Coca-Cola Co 7.3%, Procter & Gamble Co 7.2%, Philip Morris International Inc 6.2%
Sector mix: Consumer defensive 98.2%, Consumer cyclical 1.8%
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
Rolled up from the 5 largest holdings, 39.6% of the fund by weight
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 1.81 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +13.1% above the current prices
Holdings read: WMT, COST, KO, PG, PM
Recent rating changes among them:
  - WMT: 2026-09-10 DA Davidson: main, Buy -> Buy
  - COST: 2026-09-16 Oppenheimer: reit, Outperform -> Outperform
  - KO: 2026-07-30 Argus Research: main, Buy -> Buy
  - PG: 2026-08-07 Argus Research: down, Buy -> Hold
  - PM: 2026-07-30 Citigroup: main, Buy -> Buy
```

</details>

<details><summary><b>Buying and selling by company insiders</b> — score +0.00</summary>

_Not available today._

</details>

<details><summary><b>Who is positioned how</b> — score +0.00</summary>

_Not available today._

</details>

<details><summary><b>Money going into and out of this fund</b> — score +0.00</summary>

_Not available today._

</details>

### US electricity and water (XLU) · Sector or country — NEUTRAL, confidence 0.25

**In the model's own words:**

> XLU is trading at the lower end of its range with weak momentum (RSI 29.4, MACD negative) following a 6–7% decline over the past month. Technicals suggest oversold conditions but no decisive reversal signal yet. On the fundamental side, the fund's 2.8% yield and 0.43 beta position it defensively, and analyst sentiment on its top 39% of holdings is constructive at +22% target upside, offsetting concerns that utilities may face headwinds in a higher-rate environment. The 3-month yield moved up 16 bps this week while the curve remains normal; the dollar strengthened and the VIX sits at 16.8—neither a crisis nor a tailwind for rate-sensitive utilities. One headline dismisses the AI trade in utilities, and another cites political volatility post-midterms, but macro catalysts are absent. The fund's three-year 11.9% annualized return and low expense ratio show stability, but the current setup reads as a potential near-term bounce from oversold levels rather than a conviction entry. Neutral conviction reflects the lack of a clear macro or technical catalyst; the technical floor (RSI in the low 20s) and analyst upside target prevent a bearish call.

**Main reasons it gave:**
- RSI 29.4 and 7.5% below 200-day SMA signal oversold near-term floor rather than directional break
- Analyst weighted target +22% above current prices on 39% of fund weight, offsetting rate headwinds
- Three-week treasury yield rises of 14–21 bps pressuring rate-sensitive utilities, but normal yield curve provides structural support
- No macro catalyst or policy surprise; elevated VIX of 16.8 and political volatility cited but not material to sector direction

<details><summary><b>News</b> — score +0.00</summary>

- [XLU Looks 5.4% Undervalued on GF Value™ Amid Strong Dividend Fun](https://www.gurufocus.com/news/9083931/xlu-looks-54-undervalued-on-gf-value-amid-strong-dividend-fundamentals)  
  <sub>GuruFocus, 4 hours ago</sub>  
  On September 16, 2026, recent calculations using the DeMark method established key pivot points for the State Street Utilities Select Sector SPDR ETF...
- [This Utility ETF Says the AI Trade Is Over](https://finance.yahoo.com/markets/stocks/articles/utility-etf-says-ai-trade-191906797.html)  
  <sub>Yahoo Finance, 24 hours ago</sub>  
  We always have to be careful about assigning superhero-like qualities to regular sectors. Such is the case with utilities.
- [Leading And Lagging Sectors For September 16, 2026](https://www.benzinga.com/etfs/sector-etfs/26/09/61814178/leading-and-lagging-sectors-september-16-2026)  
  <sub>Benzinga, 6 hours ago</sub>  
  Gainers Symbol Name Price Change ($) Change (%) Volume (NYSE:XLK) State Street Technology Select Sector SPDR ETF 184.7100 0.970 0.52 122.1K (NYSE:XLI) State...
- [Midterms Won't Settle Washington's Volatility](https://www.etftrends.com/sector-investing-content-hub/midterms-washington-volatility/)  
  <sub>ETF Trends, 7 hours ago</sub>  
  Political volatility should stay elevated even after Democrats retake the House this November, State Street Investment Management said.
- [2 Closed-End Fund Buys In The Month Of August 2026](https://seekingalpha.com/article/4946766-2-closed-end-fund-buys-in-the-month-of-august-2026)  
  <sub>Seeking Alpha, 21 hours ago</sub>  
  Every month I add to positions in my CEF portfolio, which helps to compound my distribution growth over the long term. Click for this month's additions.
- [Should You Invest in the Vanguard Utilities Index Fund ETF Shares (VPU)?](https://finance.yahoo.com/markets/stocks/articles/invest-vanguard-utilities-index-fund-102001971.html)  
  <sub>Yahoo Finance, 9 hours ago</sub>  
  Looking for broad exposure to the Utilities - Broad segment of the equity market? You should consider the Vanguard Utilities Index Fund ETF Shares (VPU),...
- [Trump administration appeals block on California vehicle emissions rules](https://seekingalpha.com/news/4643219-trump-administration-appeals-block-on-california-vehicle-emissions-rules)  
  <sub>Seeking Alpha, 14 hours ago</sub>  
  Trump appeals court block on EPA move to fast-track repeal of California emissions waivers.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 3.96% (+0.16 on the week) | 5-year 4.83% (+0.21 on the week) | 10-year 4.97% (+0.14 on the week) | 30-year 5.32% (+0.03 on the week)
Yield curve, 10-year minus 3-month: +1.01 points -- upward sloping (normal)
US dollar index: 100.11 (+1.34 on the week)
Volatility (VIX): 16.79 (+0.3 on the week) -- elevated
```

</details>

<details><summary><b>Price and chart</b> — score -0.35</summary>

```text
Last close 41.24 (bar of 2026-09-16), from 502 daily bars
Trend: vs 20d SMA 42.79 (-3.6%), 50d 43.97 (-6.2%), 200d 44.59 (-7.5%); 50d below 200d
Momentum: RSI(14) 29.4 | MACD -0.614 vs signal -0.489 (histogram -0.125)
Returns: 1d -0.2% | 5d -4.0% | 1m -6.7% | 3m -8.5%
52-week range: 41.24 - 47.73 (now 0.0% of the way up)
Volatility: ATR(14) 0.64 (1.6% of price) | annualised 20d 14.4%
Volume: 0.81x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.15</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score +0.15</summary>

```text
Fund type: Utilities
What it holds: P/E 19.02 | P/B 2.14 | P/S 2.65 | 3y earnings growth n/a
Yield: 2.8%
Three-year record: +11.9% a year | beta to the market 0.43
Cost and size: expense ratio 0.08% | net assets 21.84B
What it is made of: Stocks 100.0%, Cash 0.1%
Largest holdings: NextEra Energy Inc 13.0%, Southern Co 7.5%, Duke Energy Corp 7.1%, Constellation Energy Corp 6.7%, American Electric Power Co Inc 5.1%
Sector mix: Utilities 100.0%
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

<details><summary><b>What analysts and big funds say</b> — score +0.40</summary>

_Not available today._

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score +0.40</summary>

```text
Rolled up from the 5 largest holdings, 39.4% of the fund by weight
Ratings by weight: buy 70.6% | hold 29.4% | sell 0.0% (mean 2.19 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +22.0% above the current prices
Holdings read: NEE, SO, DUK, CEG, AEP
Recent rating changes among them:
  - NEE: 2026-08-21 Morgan Stanley: main, Overweight -> Overweight
  - SO: 2026-08-21 Morgan Stanley: main, Underweight -> Underweight
  - DUK: 2026-08-21 Morgan Stanley: main, Equal-Weight -> Equal-Weight
  - CEG: 2026-08-21 Morgan Stanley: main, Overweight -> Overweight
  - AEP: 2026-08-21 Morgan Stanley: main, Overweight -> Overweight
```

</details>

<details><summary><b>Buying and selling by company insiders</b> — score +0.00</summary>

_Not available today._

</details>

<details><summary><b>Who is positioned how</b> — score +0.00</summary>

_Not available today._

</details>

<details><summary><b>Money going into and out of this fund</b> — score +0.00</summary>

_Not available today._

</details>

### US health care (XLV) · Sector or country — NEUTRAL, confidence 0.25

**In the model's own words:**

> XLV is elevated on valuation at a P/E of 30.47 and near the top of its 52-week range (81.7%), with technicals showing divergence: price below the 20-day moving average, RSI neutral at 48.8, and MACD histogram deeply negative despite a modest 3-month uptrend. Analyst consensus on the top 44% of holdings is solidly bullish with a weighted target 11.7% above current prices, but that target does not reflect an immediate catalyst. Treasury yields have risen 14-21 basis points across the curve this week and the dollar has strengthened 1.34%, both headwinds to healthcare equities. The 20.3% annualized volatility and weak volume (0.63x average) suggest caution. The fund's defensive characteristics (beta 0.52, 3-year +9.8% annualized) and 1.5% yield provide structural support, but the macro backdrop of rising rates and a firmer dollar, combined with stretched valuation and losing momentum, argues for patience rather than conviction either direction. Biotech weakness noted in news adds mild headwind to the sector's edge holdings.

**Main reasons it gave:**
- P/E 30.47 above historical healthcare norms and priced for growth not yet delivered
- Analyst consensus 11.7% upside on top 44% by weight, but no near-term catalyst dated
- Price 1.6% below 20-day MA and MACD histogram -0.815 shows negative momentum divergence
- Treasury yields +14-21 bps this week and US dollar +1.34%, structural headwinds to healthcare equity valuations
- Volume 0.63x average on 81.7% of 52-week range suggests hesitation at current levels

<details><summary><b>News</b> — score +0.10</summary>

- [XLV Looks 0.4% Overvalued on GF Value™](https://www.gurufocus.com/news/9083929/xlv-looks-04-overvalued-on-gf-value)  
  <sub>GuruFocus, 4 hours ago</sub>  
  On September 16, 2026, traders are closely watching the pivot points identified for the State Street Health Care Select Sector SPDR ETF (ticker: XLV).
- [Leading And Lagging Sectors For September 16, 2026](https://www.benzinga.com/etfs/sector-etfs/26/09/61814178/leading-and-lagging-sectors-september-16-2026)  
  <sub>Benzinga, 6 hours ago</sub>  
  Gainers Symbol Name Price Change ($) Change (%) Volume (NYSE:XLK) State Street Technology Select Sector SPDR ETF 184.7100 0.970 0.52 122.1K (NYSE:XLI) State...
- [Biotech Midweek Pulse: XBI Loses Steam After Hot 2026 Run — Here Are The Stocks And Catalysts To Watch Next](https://www.tradingview.com/news/stocktwits:ee8d9b8aa094b:0-biotech-midweek-pulse-xbi-loses-steam-after-hot-2026-run-here-are-the-stocks-and-catalysts-to-watch-next/)  
  <sub>TradingView, 17 hours ago</sub>  
  Biotech's 2026 rally cooled this week even as drug developers delivered major clinical updates. Definium Therapeutics (DFTX), Vera Therapeutics (VERA) and...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.10</summary>

```text
US Treasury yields: 3-month 3.96% (+0.16 on the week) | 5-year 4.83% (+0.21 on the week) | 10-year 4.97% (+0.14 on the week) | 30-year 5.32% (+0.03 on the week)
Yield curve, 10-year minus 3-month: +1.01 points -- upward sloping (normal)
US dollar index: 100.11 (+1.34 on the week)
Volatility (VIX): 16.79 (+0.3 on the week) -- elevated
```

</details>

<details><summary><b>Price and chart</b> — score -0.20</summary>

```text
Last close 168.07 (bar of 2026-09-16), from 502 daily bars
Trend: vs 20d SMA 170.85 (-1.6%), 50d 166.50 (+0.9%), 200d 155.80 (+7.9%); 50d above 200d
Momentum: RSI(14) 48.8 | MACD 0.018 vs signal 0.832 (histogram -0.815)
Returns: 1d +0.2% | 5d +0.9% | 1m +0.6% | 3m +9.9%
52-week range: 134.13 - 175.68 (now 81.7% of the way up)
Volatility: ATR(14) 2.44 (1.5% of price) | annualised 20d 20.3%
Volume: 0.63x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.15</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score +0.15</summary>

```text
Fund type: Health
What it holds: P/E 30.47 | P/B 4.77 | P/S 1.66 | 3y earnings growth n/a
Yield: 1.5%
Three-year record: +9.8% a year | beta to the market 0.52
Cost and size: expense ratio 0.08% | net assets 43.91B
What it is made of: Stocks 99.9%, Cash 0.1%
Largest holdings: Eli Lilly and Co 14.9%, Johnson & Johnson 10.4%, AbbVie Inc 7.4%, Merck & Co Inc 5.9%, UnitedHealth Group Inc 5.7%
Sector mix: Healthcare 100.0%
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

<details><summary><b>What analysts and big funds say</b> — score +0.50</summary>

_Not available today._

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score +0.50</summary>

```text
Rolled up from the 5 largest holdings, 44.3% of the fund by weight
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 1.74 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +11.7% above the current prices
Holdings read: LLY, JNJ, ABBV, MRK, UNH
Recent rating changes among them:
  - LLY: 2026-09-10 HSBC: main, Reduce -> Reduce
  - JNJ: 2026-09-10 HSBC: main, Buy -> Buy
  - ABBV: 2026-09-10 HSBC: main, Buy -> Buy
  - MRK: 2026-09-10 HSBC: main, Buy -> Buy
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

_Not available today._

</details>

### Argentina (ARGT) · Sector or country — NEUTRAL, confidence 0.20

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> No macro catalyst specific to Argentina in the past day. Price sits below its 20d and 50d SMAs with MACD rolling over and RSI at 41.6, but the 50d is still above the 200d and price is mid-range \u2014 a drift, not a break. The macro backdrop is mildly hostile to EM/LatAm risk: 5y and 10y Treasury yields up 21bp and 14bp on the week and a dollar index up 1.34, which typically pressures a peso-linked, energy- and bank-heavy basket. Offsetting that, holdings analyst coverage over 51% of the fund is 100% buy with a +28.5% weighted target, and the basket is cheap at 15.5x with a 0.59% fee. Concentration is a caution (MELI at 25.4%). Net: no side worth taking this cycle. No flows or positioning data, so insider dimension left null.

**Main reasons it gave:**
- Price -2.6% vs 20d SMA, MACD histogram -0.272, RSI 41.6 \u2014 weakening near-term momentum
- Dollar index +1.34 on the week and 5y Treasury +21bp \u2014 headwind for LatAm equity risk
- 50d SMA above 200d, 70% of 52-week range \u2014 longer trend still intact
- Holdings roll-up covering 51.1% of fund: 100% buy, +28.5% weighted price target
- Concentrated basket \u2014 MercadoLibre 25.4% of assets
- No fund-relevant macro news in past 24 hours

<details><summary><b>News</b> — score +0.00</summary>

_No news found for this one today._

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 3.96% (+0.16 on the week) | 5-year 4.83% (+0.21 on the week) | 10-year 4.97% (+0.14 on the week) | 30-year 5.32% (+0.03 on the week)
Yield curve, 10-year minus 3-month: +1.01 points -- upward sloping (normal)
US dollar index: 100.11 (+1.34 on the week)
Volatility (VIX): 16.79 (+0.3 on the week) -- elevated
```

</details>

<details><summary><b>Price and chart</b> — score -0.25</summary>

```text
Last close 92.42 (bar of 2026-09-16), from 502 daily bars
Trend: vs 20d SMA 94.86 (-2.6%), 50d 93.93 (-1.6%), 200d 92.73 (-0.3%); 50d above 200d
Momentum: RSI(14) 41.6 | MACD 0.366 vs signal 0.638 (histogram -0.272)
Returns: 1d -2.2% | 5d -3.9% | 1m +1.2% | 3m -5.2%
52-week range: 67.55 - 102.94 (now 70.3% of the way up)
Volatility: ATR(14) 1.96 (2.1% of price) | annualised 20d 20.8%
Volume: 1.05x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.15</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score +0.15</summary>

```text
Fund type: Focused Region
What it holds: P/E 15.48 | P/B 1.77 | P/S 1.36 | 3y earnings growth n/a
Yield: 1.1%
Three-year record: +29.6% a year | beta to the market 0.50
Cost and size: expense ratio 0.59% | net assets 815.33M
What it is made of: Stocks 99.9%, Cash 0.1%
Largest holdings: MercadoLibre Inc 25.4%, YPF SA ADR 9.5%, Vista Energy SAB de CV ADR 6.2%, Grupo Financiero Galicia SA ADR 5.6%, Banco Macro SA ADR 4.3%
Sector mix: Consumer cyclical 30.4%, Energy 19.4%, Financial services 14.4%, Basic materials 12.0%
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
Rolled up from the 5 largest holdings, 51.1% of the fund by weight
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 1.59 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +28.5% above the current prices
Holdings read: MELI, YPF, VIST, GGAL, BMA
Recent rating changes among them:
  - MELI: 2026-09-03 BTIG: reit, Buy -> Buy
  - YPF: 2026-09-01 JP Morgan: main, Overweight -> Overweight
  - VIST: 2026-09-01 JP Morgan: main, Overweight -> Overweight
  - GGAL: 2026-06-25 JP Morgan: main, Overweight -> Overweight
  - BMA: 2026-06-25 JP Morgan: main, Overweight -> Overweight
```

</details>

<details><summary><b>Buying and selling by company insiders</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>Who is positioned how</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>Money going into and out of this fund</b> — score n/a</summary>

_Not available today._

</details>

### Israel (EIS) · Sector or country — NEUTRAL, confidence 0.20

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Israel equity fund sitting flat against its 20d SMA with RSI at 50 and MACD rolling slightly negative -- no decisive technical break. The only macro development of note is a broad rise in US yields (5y +21bp, 10y +14bp) and a firmer dollar, both mild headwinds for a foreign-currency equity basket, but nothing outside the range of ordinary weekly noise. News flow is a single irrelevant micro-cap gold item, which I disregard. Analyst roll-up is supportive (100% buy by weight, +12.6% target) but covers only 37.6% of the fund and is concentrated in Teva plus two banks. Fund basics are unremarkable at P/E 17.9 after a very strong three-year run. No catalyst justifies a directional call.

**Main reasons it gave:**
- RSI 50.0 and MACD histogram -0.221, price within 0.3% of 20d SMA
- 5y yield +21bp and 10y +14bp on the week, dollar index +1.34
- Analyst roll-up 100% buy, +12.6% target, but only 37.6% coverage
- Top-5 concentration: Teva 10.1% plus two banks ~17%, financials 36% of fund
- Only news item is an unrelated micro-cap gold offering -- no macro content

<details><summary><b>News</b> — score +0.00</summary>

- [Star Gold opens Nevada gold project to public investors via Regulation A](https://app.dealroom.co/news/note/star-gold-opens-nevada-gold-project-to-public-investors-via-regulation-a)  
  <sub>Dealroom, 5 hours ago</sub>  
  What's the deal? Star Gold Corp. (OTCQB: SRGZ) has launched a Re…

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 3.96% (+0.16 on the week) | 5-year 4.83% (+0.21 on the week) | 10-year 4.97% (+0.14 on the week) | 30-year 5.32% (+0.03 on the week)
Yield curve, 10-year minus 3-month: +1.01 points -- upward sloping (normal)
US dollar index: 100.11 (+1.34 on the week)
Volatility (VIX): 16.79 (+0.3 on the week) -- elevated
```

</details>

<details><summary><b>Price and chart</b> — score -0.05</summary>

```text
Last close 123.11 (bar of 2026-09-16), from 502 daily bars
Trend: vs 20d SMA 123.43 (-0.3%), 50d 121.73 (+1.1%), 200d 121.65 (+1.2%); 50d above 200d
Momentum: RSI(14) 50.0 | MACD 0.343 vs signal 0.564 (histogram -0.221)
Returns: 1d +0.4% | 5d -1.5% | 1m +0.5% | 3m -0.3%
52-week range: 94.07 - 137.69 (now 66.6% of the way up)
Volatility: ATR(14) 1.70 (1.4% of price) | annualised 20d 19.6%
Volume: 1.17x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.05</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score +0.05</summary>

```text
Fund type: Focused Region
What it holds: P/E 17.89 | P/B 2.43 | P/S 2.45 | 3y earnings growth n/a
Yield: 1.5%
Three-year record: +33.0% a year | beta to the market 1.07
Cost and size: expense ratio 0.59% | net assets 897.28M
What it is made of: Stocks 99.5%, Cash 0.5%
Largest holdings: Teva Pharmaceutical Industries Ltd ADR 10.1%, Bank Leumi Le-Israel BM 9.0%, Bank Hapoalim BM 8.1%, Tower Semiconductor Ltd 5.5%, Elbit Systems Ltd 4.8%
Sector mix: Financial services 36.1%, Technology 18.1%, Healthcare 10.7%, Industrials 10.0%
```

</details>

<details><summary><b>Does this company beat its own forecasts</b> — score +0.05</summary>

_Not available today._

</details>

<details><summary><b>What holding this fund costs you</b> — score +0.05</summary>

_Not available today._

</details>

<details><summary><b>How much oil and gas is in storage</b> — score +0.05</summary>

_Not available today._

</details>

<details><summary><b>How the crop is growing</b> — score +0.05</summary>

_Not available today._

</details>

<details><summary><b>What analysts and big funds say</b> — score +0.35</summary>

_Not available today._

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score +0.35</summary>

```text
Rolled up from the 5 largest holdings, 37.6% of the fund by weight
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 1.46 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +12.6% above the current prices
Holdings read: TEVA, LUMI.TA, POLI.TA, TSEM.TA, ESLT.TA
Recent rating changes among them:
  - TEVA: 2026-09-09 Leerink Partners: init, ? -> Outperform
  - TSEM.TA: 2026-09-02 Stifel: init, ? -> Buy
  - ESLT.TA: 2026-08-19 JP Morgan: main, Neutral -> Neutral
```

</details>

<details><summary><b>Buying and selling by company insiders</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>Who is positioned how</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>Money going into and out of this fund</b> — score n/a</summary>

_Not available today._

</details>

### Taiwan (EWT) · Sector or country — NEUTRAL, confidence 0.20

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> EWT sits near the top of its 52-week range after a huge 3-year run, but the near-term picture is mixed: price is just below the 20d SMA, MACD has rolled over negative, RSI is flat at 51 and volume is thin. The macro backdrop is a mild headwind rather than a tailwind -- yields up across the curve (5y +21bp, 10y +14bp), dollar up 1.34 on the week, which typically pressures high-beta Asian tech exposure (beta 1.30, 74% technology, 22% TSMC). Offsetting that, analyst coverage of the top five holdings (38% of fund) is uniformly buy with ~35% weighted upside, and the 50d/200d structure remains bullish. No policy or data surprise in the news window; the single headline is an unrelated HKEX ETF listing and carries no information for EWT. No clear catalyst either way, so NEUTRAL.

**Main reasons it gave:**
- Price 91.3% of 52-week range, MACD histogram -0.479 with price just under 20d SMA
- 5-year yield +21bp and DXY +1.34 on the week -- headwind for high-beta (1.30) Asian tech
- Top-5 holdings 100% buy-rated by weight, +34.9% weighted price target, but only 38% of fund covered
- P/E 27.3 and 73.9% technology concentration with 22.1% in TSMC after +41.3%/yr 3-year run
- Volume 0.59x 20-day average -- no decisive break in either direction

<details><summary><b>News</b> — score +0.00</summary>

- [Unlocking APAC Semiconductor Bottleneck Opportunities: CSOP Solactive Asia AI Bottleneck Index ETF to List on HKEX tomorrow](https://finance.yahoo.com/markets/stocks/articles/unlocking-apac-semiconductor-bottleneck-opportunities-080000456.html)  
  <sub>Yahoo Finance, 11 hours ago</sub>  
  CSOP Solactive Asia AI Bottleneck Index ETF (3499.HK) will list on HKEX tomorrow (17th September 2026). 3499.HK seeks to provide investment results that,...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 3.96% (+0.16 on the week) | 5-year 4.83% (+0.21 on the week) | 10-year 4.97% (+0.14 on the week) | 30-year 5.32% (+0.03 on the week)
Yield curve, 10-year minus 3-month: +1.01 points -- upward sloping (normal)
US dollar index: 100.11 (+1.34 on the week)
Volatility (VIX): 16.79 (+0.3 on the week) -- elevated
```

</details>

<details><summary><b>Price and chart</b> — score +0.05</summary>

```text
Last close 107.64 (bar of 2026-09-16), from 502 daily bars
Trend: vs 20d SMA 107.94 (-0.3%), 50d 103.83 (+3.7%), 200d 85.82 (+25.4%); 50d above 200d
Momentum: RSI(14) 51.4 | MACD 1.349 vs signal 1.828 (histogram -0.479)
Returns: 1d +0.9% | 5d -3.7% | 1m -0.1% | 3m +3.7%
52-week range: 60.03 - 112.18 (now 91.3% of the way up)
Volatility: ATR(14) 2.28 (2.1% of price) | annualised 20d 22.9%
Volume: 0.59x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score -0.10</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score -0.10</summary>

```text
Fund type: Greater China Region
What it holds: P/E 27.26 | P/B 4.29 | P/S 2.54 | 3y earnings growth n/a
Yield: 0.9%
Three-year record: +41.3% a year | beta to the market 1.30
Cost and size: expense ratio 0.59% | net assets 11.76B
What it is made of: Stocks 99.6%, Cash 0.4%
Largest holdings: Taiwan Semiconductor Manufacturing Co Ltd 22.1%, MediaTek Inc 6.0%, Delta Electronics Inc 4.0%, Hon Hai Precision Industry Co Ltd 3.3%, ASE Technology Holding Co Ltd 2.6%
Sector mix: Technology 73.9%, Financial services 14.0%, Basic materials 3.8%, Industrials 2.8%
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

<details><summary><b>What analysts and big funds say</b> — score +0.45</summary>

_Not available today._

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score +0.45</summary>

```text
Rolled up from the 5 largest holdings, 38.0% of the fund by weight
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 1.35 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +34.9% above the current prices
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

_Not available today._

</details>

### Brazil (EWZ) · Sector or country — NEUTRAL, confidence 0.20

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> No macro catalyst specific to Brazil in the past day. Technicals are mildly constructive (price above 20/50/200d SMAs, RSI 55, +9.7% 1m) but the 50d remains below the 200d, volume is thin at 0.70x average, and the last week was -2.1%. The macro backdrop is the main counterweight: US yields up sharply across the curve (5y +21bp, 10y +14bp) with the dollar up 1.34 to 100.11 — a tightening-and-strong-dollar combination that is historically a headwind for Brazilian equities and the BRL. Fundamentals are cheap (P/E 10.5, 4.1% yield) and analyst coverage on 41% of the fund is uniformly buy with +25% targets, but that is a slow-moving valuation argument, not a timing signal. Net: no side worth taking this cycle.

**Main reasons it gave:**
- Dollar index +1.34 on the week to 100.11 and 5y yield +21bp — headwind for Brazil equities
- 50d SMA still below 200d despite price above all three averages
- 5d return -2.1% on 0.70x average volume, momentum flattening (MACD histogram +0.04)
- Holdings P/E 10.5 with 4.1% yield; analyst roll-up 100% buy, +24.6% targets over 40.9% of fund
- Sole rating change is a downgrade: Nu Holdings (9.5% weight) cut to Market Perform

<details><summary><b>News</b> — score +0.00</summary>

_No news found for this one today._

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 3.96% (+0.16 on the week) | 5-year 4.83% (+0.21 on the week) | 10-year 4.97% (+0.14 on the week) | 30-year 5.32% (+0.03 on the week)
Yield curve, 10-year minus 3-month: +1.01 points -- upward sloping (normal)
US dollar index: 100.11 (+1.34 on the week)
Volatility (VIX): 16.79 (+0.3 on the week) -- elevated
```

</details>

<details><summary><b>Price and chart</b> — score +0.15</summary>

```text
Last close 37.28 (bar of 2026-09-16), from 502 daily bars
Trend: vs 20d SMA 36.72 (+1.5%), 50d 35.92 (+3.8%), 200d 36.14 (+3.1%); 50d below 200d
Momentum: RSI(14) 55.3 | MACD 0.719 vs signal 0.678 (histogram 0.041)
Returns: 1d -1.3% | 5d -2.1% | 1m +9.7% | 3m +8.3%
52-week range: 28.79 - 41.73 (now 65.6% of the way up)
Volatility: ATR(14) 0.80 (2.2% of price) | annualised 20d 23.9%
Volume: 0.70x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.30</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score +0.30</summary>

```text
Fund type: Focused Region
What it holds: P/E 10.48 | P/B 1.79 | P/S 1.28 | 3y earnings growth n/a
Yield: 4.1%
Three-year record: +11.5% a year | beta to the market 0.84
Cost and size: expense ratio 0.59% | net assets 8.17B
What it is made of: Stocks 96.5%, Cash 2.7%, Preferred 0.8%
Largest holdings: Vale SA 10.1%, Nu Holdings Ltd Ordinary Shares Class A 9.5%, Itau Unibanco Holding SA Participating Preferred 7.7%, Petroleo Brasileiro SA Petrobras Participating Preferred 7.0%, Petroleo Brasileiro SA Petrobras 6.6%
Sector mix: Financial services 34.1%, Energy 17.4%, Basic materials 14.5%, Utilities 12.4%
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
Rolled up from the 5 largest holdings, 40.9% of the fund by weight
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 1.48 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +24.6% above the current prices
Holdings read: VALE3.SA, NU, ITUB4, PETR4, PETR3.SA
Recent rating changes among them:
  - NU: 2026-09-16 Itau BBA: down, Outperform -> Market Perform
```

</details>

<details><summary><b>Buying and selling by company insiders</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>Who is positioned how</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>Money going into and out of this fund</b> — score n/a</summary>

_Not available today._

</details>

### South Africa (EZA) · Sector or country — NEUTRAL, confidence 0.20

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> No macro news specific to South Africa in the window. Technicals are soft: price 5% below the 20d SMA, 50d below 200d, MACD histogram negative, RSI 41, and a -6.1% week on light volume, but price sits right on the 50d and only 31% up the 52-week range rather than breaking down decisively. Macro leans against EM equity: yields up across the curve (5y +21bp, 10y +14bp) with the dollar up 1.34 to 100.11, a tightening of external conditions that historically pressures rand assets. Offsetting that, the fund is cheap (P/E 9.3, 7.1% yield) and 24% of it is gold miners with unanimous buy ratings and +23% weighted targets over 45.6% of the fund. Conflicting evidence and no policy or data surprise -- NEUTRAL with a slight bearish tilt.

**Main reasons it gave:**
- price 5.1% below 20d SMA, 50d below 200d, MACD histogram -0.62
- dollar index +1.34 on the week to 100.11 and 5y yield +21bp, tightening EM conditions
- holdings P/E 9.31 with 7.1% yield, deep-value basket
- analyst roll-up over 45.6% of fund: 100% buy, +23.3% weighted target
- 41% basic materials / 24% gold miners makes fund a de facto gold-equity proxy, not a clean SA macro bet

<details><summary><b>News</b> — score +0.00</summary>

_No news found for this one today._

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 3.96% (+0.16 on the week) | 5-year 4.83% (+0.21 on the week) | 10-year 4.97% (+0.14 on the week) | 30-year 5.32% (+0.03 on the week)
Yield curve, 10-year minus 3-month: +1.01 points -- upward sloping (normal)
US dollar index: 100.11 (+1.34 on the week)
Volatility (VIX): 16.79 (+0.3 on the week) -- elevated
```

</details>

<details><summary><b>Price and chart</b> — score -0.40</summary>

```text
Last close 67.00 (bar of 2026-09-16), from 502 daily bars
Trend: vs 20d SMA 70.56 (-5.1%), 50d 66.98 (+0.0%), 200d 69.23 (-3.2%); 50d below 200d
Momentum: RSI(14) 41.0 | MACD 0.314 vs signal 0.931 (histogram -0.616)
Returns: 1d -2.8% | 5d -6.1% | 1m -1.8% | 3m -1.5%
52-week range: 60.43 - 81.60 (now 31.0% of the way up)
Volatility: ATR(14) 1.34 (2.0% of price) | annualised 20d 30.2%
Volume: 0.46x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.25</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score +0.25</summary>

```text
Fund type: Focused Region
What it holds: P/E 9.31 | P/B 2.24 | P/S 1.92 | 3y earnings growth n/a
Yield: 7.1%
Three-year record: +27.9% a year | beta to the market 1.02
Cost and size: expense ratio 0.59% | net assets 578.49M
What it is made of: Stocks 99.7%, Cash 0.3%
Largest holdings: Anglogold Ashanti PLC 13.7%, Gold Fields Ltd 9.9%, Naspers Ltd Class N 8.8%, Firstrand Ltd 7.1%, Standard Bank Group Ltd 6.1%
Sector mix: Basic materials 41.0%, Financial services 33.2%, Consumer cyclical 12.8%, Communication services 6.2%
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
Rolled up from the 5 largest holdings, 45.6% of the fund by weight
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 1.88 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +23.3% above the current prices
Holdings read: AU, GFI.JO, NPN.JO, FSR.JO, SBK.JO
Recent rating changes among them:
  - AU: 2026-09-16 RBC Capital: main, Outperform -> Outperform
```

</details>

<details><summary><b>Buying and selling by company insiders</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>Who is positioned how</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>Money going into and out of this fund</b> — score n/a</summary>

_Not available today._

</details>

### Transport and delivery (IYT) · Sector or country — NEUTRAL, confidence 0.20

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Transports are in a clear sector downtrend: price 4.9% below the 20d and 6.9% below the 50d SMA, RSI 28.7, MACD negative, and a fresh cost shock from record diesel plus J.B. Hunt's profit warning. That is genuine sector-specific bearish news rather than noise, and rising yields (5y +21bp, 10y +14bp) with a stronger dollar tighten conditions further. But the fund sits just under its 200d with 50d still above 200d, volume is only average (no decisive break), oversold momentum cuts against chasing the downside, and analyst coverage on 53% of assets is 100% buy with +22.9% implied upside including a UNP upgrade this week. Note the news items are promotional ETF-comparison pieces; I weigh the underlying facts, not the framing. Net: no clean macro catalyst either way, so NEUTRAL with a mild bearish tilt.

**Main reasons it gave:**
- Record diesel prices (+70% y/y) squeezing trucking margins; JBH -13% on Q3 profit warning
- RSI 28.7, price -4.9% vs 20d and -6.9% vs 50d, MACD below signal
- Still only 0.9% below 200d SMA with 50d above 200d; volume 1.0x average, no decisive break
- Yields up across the curve (5y +21bp, 10y +14bp) and DXY +1.34 on the week
- Holdings roll-up 100% buy weight, +22.9% weighted target, UNP upgraded to Buy at UBS

<details><summary><b>News</b> — score -0.40</summary>

- [J.B. Hunt Diesel Shock: Which Transportation ETFs Are Most Exposed? - JB Hunt Transport Servs (NASDAQ:JBH](https://www.benzinga.com/etfs/sector-etfs/26/09/61826719/j-b-hunts-diesel-shock-hits-transportation-etfs-which-funds-have-the-most-fuel-sensitive-exposure)  
  <sub>Benzinga, 12 minutes ago</sub>  
  J.B. Hunt's profit warning and record diesel prices are putting transportation ETFs under pressure. Here's how XTN, IYT and FTXR compare on trucking...
- [Freight Stocks Sink As Record Diesel Squeezes Margins: 7 Names To Watch - JB Hunt Transport Servs (NASDAQ](https://www.benzinga.com/markets/commodities/26/09/61822024/freight-stocks-record-diesel-prices-squeeze-margins-7-names-to-watch)  
  <sub>Benzinga, 3 hours ago</sub>  
  Diesel is up 70% over the past year. J.B. Hunt fell 13% on a Q3 profit warning, dragging Knight-Swift, XPO and Old Dominion lower.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score -0.40</summary>

```text
US Treasury yields: 3-month 3.96% (+0.16 on the week) | 5-year 4.83% (+0.21 on the week) | 10-year 4.97% (+0.14 on the week) | 30-year 5.32% (+0.03 on the week)
Yield curve, 10-year minus 3-month: +1.01 points -- upward sloping (normal)
US dollar index: 100.11 (+1.34 on the week)
Volatility (VIX): 16.79 (+0.3 on the week) -- elevated
```

</details>

<details><summary><b>Price and chart</b> — score -0.50</summary>

```text
Last close 80.23 (bar of 2026-09-16), from 502 daily bars
Trend: vs 20d SMA 84.34 (-4.9%), 50d 86.13 (-6.9%), 200d 81.00 (-0.9%); 50d above 200d
Momentum: RSI(14) 28.7 | MACD -1.409 vs signal -1.060 (histogram -0.349)
Returns: 1d -1.9% | 5d -1.8% | 1m -8.1% | 3m -6.8%
52-week range: 68.14 - 90.01 (now 55.3% of the way up)
Volatility: ATR(14) 1.31 (1.6% of price) | annualised 20d 15.9%
Volume: 1.00x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score -0.10</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score -0.10</summary>

```text
Fund type: Industrials
What it holds: P/E 20.28 | P/B 4.25 | P/S 1.45 | 3y earnings growth n/a
Yield: 0.9%
Three-year record: +12.0% a year | beta to the market 1.28
Cost and size: expense ratio 0.37% | net assets 2.20B
What it is made of: Stocks 99.8%, Cash 0.2%
Largest holdings: Union Pacific Corp 17.8%, Uber Technologies Inc 15.4%, CSX Corp 9.4%, United Parcel Service Inc Class B 5.6%, Norfolk Southern Corp 4.9%
Sector mix: Industrials 83.8%, Technology 16.2%
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

<details><summary><b>What analysts and big funds say</b> — score +0.35</summary>

_Not available today._

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score +0.35</summary>

```text
Rolled up from the 5 largest holdings, 53.1% of the fund by weight
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 1.79 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +22.9% above the current prices
Holdings read: UNP, UBER, CSX, UPS, NSC
Recent rating changes among them:
  - UNP: 2026-09-16 UBS: up, Neutral -> Buy
  - UBER: 2026-09-09 Scotiabank: init, ? -> Sector Outperform
  - CSX: 2026-07-24 Citigroup: main, Neutral -> Neutral
  - UPS: 2026-07-29 Stifel: main, Buy -> Buy
  - NSC: 2026-07-27 BMO Capital: main, Market Perform -> Market Perform
```

</details>

<details><summary><b>Buying and selling by company insiders</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>Who is positioned how</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>Money going into and out of this fund</b> — score n/a</summary>

_Not available today._

</details>

### US industry (XLI) · Sector or country — NEUTRAL, confidence 0.20

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> XLI is deeply oversold (RSI 29, -9.8% in a month, below 20d/50d) into a Fed meeting where markets expect the first hike since 2023, with yields up 14-21bp across the curve and the dollar up 1.34 — a genuinely hostile rate backdrop for a cyclical sector trading at 28x earnings. Counterweight: price is still above the 200d, 50d>200d, volume is below average (no capitulation), and analyst coverage of the top 26% of the fund is 100% buy with +25% targets, plus a UBS upgrade of UNP and broad capex/reshoring narrative. Oversold plus a known binary policy event is not an edge in either direction, so NEUTRAL. Listicle and ETF-reorg headlines disregarded as noise.

**Main reasons it gave:**
- RSI(14) 29.3, price -4.0% vs 20d and -9.8% over 1m, MACD below signal
- 5y yield +21bp and 10y +14bp on the week; dollar index +1.34 ahead of expected 25bp Fed hike
- Still above 200d SMA with 50d>200d; selling on 0.88x average volume
- Top-5 holdings (25.8% of fund) 100% buy-rated, weighted target +25.5%; UBS upgrade of UNP
- Holdings P/E 28.4 with 1.2% yield — rich for a rate-sensitive cyclical basket

<details><summary><b>News</b> — score -0.10</summary>

- [Amplify Makes Plans to Take Over TACK ETF: What to Know](https://etfdb.com/equity-etf-content-hub/what-to-know-amplify-makes-plans-to-take-over-tack-etf/)  
  <sub>ETF Database, 1 hour ago</sub>  
  Proposed plans were recently approved for Amplify Investments to reorganize and take over the Fairlead Tactical Sector ETF (TACK).
- [UBS names 10 high-conviction industrial stocks as capital spending broadens (XLI:NYSEARCA)](https://seekingalpha.com/news/4643384-ubs-names-10-high-conviction-industrial-stocks-as-capital-spending-broadens)  
  <sub>Seeking Alpha, 5 hours ago</sub>  
  UBS names 10 top industrial stock picks (LMT, UAL, ETN, URI, more) as manufacturing and capex recover beyond AI.
- [Should You Invest in the First Trust Technology AlphaDEX ETF (FXL)?](https://finance.yahoo.com/markets/stocks/articles/invest-first-trust-technology-alphadex-102001745.html)  
  <sub>Yahoo Finance, 9 hours ago</sub>  
  Looking for broad exposure to the Technology - Broad segment of the equity market? You should consider the First Trust Technology AlphaDEX ETF (FXL),...
- [Leading And Lagging Sectors For September 16, 2026](https://www.benzinga.com/etfs/sector-etfs/26/09/61814178/leading-and-lagging-sectors-september-16-2026)  
  <sub>Benzinga, 6 hours ago</sub>  
  Gainers Symbol Name Price Change ($) Change (%) Volume (NYSE:XLK) State Street Technology Select Sector SPDR ETF 184.7100 0.970 0.52 122.1K (NYSE:XLI) State...
- [Fed Most Likely to Hike Rates After 3 Years: ETFs to Win/Lose](https://www.tradingview.com/news/zacks:cca1fd804094b:0-fed-most-likely-to-hike-rates-after-3-years-etfs-to-win-lose/)  
  <sub>TradingView, 6 hours ago</sub>  
  The Federal Reserve's September policy meeting kicked off Tuesday, and markets are widely expecting a 25-basis-point rate hike on Wednesday.
- [Made in America again? That'll be $6.5T, please (XLI:NYSEARCA)](https://seekingalpha.com/news/4643391-made-in-america-again-thatll-be-65t-please)  
  <sub>Seeking Alpha, 4 hours ago</sub>  
  NicoElNino. Restoring the U.S.'s eroded industrial base and securing critical supply chains will require up to $6.5T in new investment, according to a new...
- [Veralto Stock: Is VLTO Underperforming the Industrial Sector?](https://finance.yahoo.com/markets/stocks/articles/veralto-stock-vlto-underperforming-industrial-122504138.html)  
  <sub>Yahoo Finance, 7 hours ago</sub>  
  Veralto Corporation (VLTO), headquartered in Waltham, Massachusetts, provides water analytics, water treatment, marking and coding, and packaging and color...
- [S&P 500 Gains, Crude Falls Ahead Of Fed's Expected First Hike Since 2023: Stock Market Today](https://www.benzinga.com/markets/market-summary/26/09/61822672/oil-sinks-below-103-optics-stocks-rip-fed-first-hike-since-2023-markets-wednesday)  
  <sub>Benzinga, 2 hours ago</sub>  
  Crude tumbles 3.6% on a Saudi pipeline restart, easing yields and lifting chips, while the Fed prepares its first rate hike in nearly three years.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score -0.10</summary>

```text
US Treasury yields: 3-month 3.96% (+0.16 on the week) | 5-year 4.83% (+0.21 on the week) | 10-year 4.97% (+0.14 on the week) | 30-year 5.32% (+0.03 on the week)
Yield curve, 10-year minus 3-month: +1.01 points -- upward sloping (normal)
US dollar index: 100.11 (+1.34 on the week)
Volatility (VIX): 16.79 (+0.3 on the week) -- elevated
```

</details>

<details><summary><b>Price and chart</b> — score -0.40</summary>

```text
Last close 168.06 (bar of 2026-09-16), from 502 daily bars
Trend: vs 20d SMA 175.10 (-4.0%), 50d 179.42 (-6.3%), 200d 171.46 (-2.0%); 50d above 200d
Momentum: RSI(14) 29.3 | MACD -3.210 vs signal -2.531 (histogram -0.680)
Returns: 1d -0.5% | 5d -2.2% | 1m -9.8% | 3m -6.6%
52-week range: 147.83 - 186.51 (now 52.3% of the way up)
Volatility: ATR(14) 2.51 (1.5% of price) | annualised 20d 13.1%
Volume: 0.88x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score -0.10</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score -0.10</summary>

```text
Fund type: Industrials
What it holds: P/E 28.43 | P/B 6.75 | P/S 3.00 | 3y earnings growth n/a
Yield: 1.2%
Three-year record: +18.9% a year | beta to the market 1.02
Cost and size: expense ratio 0.08% | net assets 31.95B
What it is made of: Stocks 100.0%, Cash 0.1%
Largest holdings: Caterpillar Inc 6.7%, GE Aerospace 6.4%, RTX Corp 5.1%, GE Vernova Inc 4.4%, Union Pacific Corp 3.2%
Sector mix: Industrials 92.8%, Technology 6.7%, Basic materials 0.3%, Consumer cyclical 0.2%
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

<details><summary><b>What analysts and big funds say</b> — score +0.35</summary>

_Not available today._

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score +0.35</summary>

```text
Rolled up from the 5 largest holdings, 25.8% of the fund by weight
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 1.79 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +25.5% above the current prices
Holdings read: CAT, GE, RTX, GEV, UNP
Recent rating changes among them:
  - CAT: 2024-10-14 JP Morgan: main, Overweight -> Overweight
  - GE: 2026-07-23 Bernstein: main, Outperform -> Outperform
  - RTX: 2026-08-03 Bernstein: main, Market Perform -> Market Perform
  - GEV: 2026-09-15 Bernstein: reit, Outperform -> Outperform
  - UNP: 2026-09-16 UBS: up, Neutral -> Buy
```

</details>

<details><summary><b>Buying and selling by company insiders</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>Who is positioned how</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>Money going into and out of this fund</b> — score n/a</summary>

_Not available today._

</details>

## Commodities

### Gold (GLD) · Commodity — BEARISH, confidence 0.35

**Result:** ACCEPTED · 10 shares · submitted sell 10 GLD @ ~389.23, stop 404.87

**In the model's own words:**

> Rates and the dollar both moved sharply against gold this week (10y +14bp, 5y +21bp, DXY +1.34), and the technical picture corroborates: price below its 20d, 50d and 200d averages with a 50/200 death cross, negative MACD and RSI 41.6, -3.5% over five sessions on slightly above-average volume. Physically backed structure means no carry drag either way (-0.4%/yr), so this is purely a real-rates/dollar call. Speculative net long collapsed -32.8% on the week to the 17th percentile, which is real de-risking but also removes the crowded-long overhang, so I keep conviction modest ahead of the Fed decision. Headlines were mostly noise -- one was a retail chat post about having sold GLD, which I disregard as a source.

**Main reasons it gave:**
- 10y yield +14bp and 5y +21bp on the week; DXY +1.34 -- rising real rates and stronger dollar are direct headwinds to gold
- Price 6.5% below 200d SMA with 50d below 200d; MACD histogram -3.22, RSI 41.6
- -3.5% over 5 days, -4.0% over 1 month, only 33% up the 52-week range
- CFTC spec net long down 32.8% on the week to 17th percentile -- active de-risking, though no longer a crowded long
- Physically backed: carry gap only -0.4%/yr, so no structural drag distorting the fund versus spot

<details><summary><b>News</b> — score -0.10</summary>

- [damn son [Panic] lucky i sell $SPDR Gold ETF (GLD.US)$](https://www.moomoo.com/community/feed/damn-son-lucky-i-sell-spdr-gold-etf-gld-us-117281104199686)  
  <sub>Moomoo, 5 hours ago</sub>  
  damn son [Panic] lucky i sell $SPDR Gold ETF (GLD.US)$
- [Why Are Central Banks Moving Their Gold Reserves](https://seekingalpha.com/article/4946875-why-central-banks-moving-gold-reserves?source=generic_rss)  
  <sub>Seeking Alpha, 13 hours ago</sub>  
  On 2 September, De Nederlandsche Bank announced that it had transferred approximately 86t of gold from New York and Ottawa to London. Read more here.
- [Gold and silver tick lower ahead of Fed rate decision (GLD:NYSEARCA)](https://seekingalpha.com/news/4643189-gold-and-silver-tick-lower-ahead-of-fed-rate-decision)  
  <sub>Seeking Alpha, 22 hours ago</sub>  
  Gold and silver futures settled modestly lower a day ahead of the Federal Reserve's interest-rate decision, which is widely expected to be a quarter-point...
- [Daily ETF Flows: BOTZ Loses $187M](https://finance.yahoo.com/markets/options/articles/daily-etf-flows-botz-loses-210004282.html)  
  <sub>Yahoo Finance, 22 hours ago</sub>  
  Here are the daily ETF fund flows for September 14, 2026.
- [IWM News | ISHARES RUSSELL 2000 ETF (NYSEARCA:IWM)](https://www.chartmill.com/stock/quote/IWM/news)  
  <sub>ChartMill, 22 hours ago</sub>  
  Latest news and press releases for ISHARES RUSSELL 2000 ETF (NYSEARCA:IWM).
- [Day 480: Rate Hike + Trump 2.0 Day 603](https://www.moomoo.com/community/feed/day-480-rate-hike-trump-2-0-day-603-117281122746374)  
  <sub>Moomoo, 5 hours ago</sub>  
  Market Recap | Wednesday, September 16, 2026 Positioning for the verdict, a few hours early This is the calm of a market that has already made up...
- [Gold For Sovereignty, US Treasuries For Liquidity - Complementary Hedges (NASDAQ:IEF)](https://seekingalpha.com/article/4946680-gold-for-sovereignty-us-treasuries-for-liquidity-complementary-hedges)  
  <sub>Seeking Alpha, 24 hours ago</sub>  
  US Treasuries vs gold in global reserves: liquidity vs risk hedge. De-dollarization is overstated; central banks buy gold as insurance.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score -0.10</summary>

```text
US Treasury yields: 3-month 3.96% (+0.16 on the week) | 5-year 4.83% (+0.21 on the week) | 10-year 4.97% (+0.14 on the week) | 30-year 5.32% (+0.03 on the week)
Yield curve, 10-year minus 3-month: +1.01 points -- upward sloping (normal)
US dollar index: 100.11 (+1.34 on the week)
Volatility (VIX): 16.79 (+0.3 on the week) -- elevated
```

</details>

<details><summary><b>Price and chart</b> — score -0.55</summary>

```text
Last close 389.16 (bar of 2026-09-16), from 502 daily bars
Trend: vs 20d SMA 407.97 (-4.6%), 50d 391.98 (-0.7%), 200d 416.10 (-6.5%); 50d below 200d
Momentum: RSI(14) 41.6 | MACD -1.061 vs signal 2.161 (histogram -3.222)
Returns: 1d -1.3% | 5d -3.5% | 1m -4.0% | 3m -2.1%
52-week range: 335.62 - 495.90 (now 33.4% of the way up)
Volatility: ATR(14) 7.82 (2.0% of price) | annualised 20d 27.7%
Volume: 1.10x the 20-day average
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
Cost of holding this fund instead of gold itself: -0.4% a year -- close to nothing, as a physically backed fund should be
Measured: 3 months: fund -2.1%, commodity -1.6%, gap -0.5% | 6 months: fund -15.3%, commodity -14.4%, gap -0.8% | 12 months: fund +14.8%, commodity +15.2%, gap -0.4%
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
Contract: GOLD (positions as of 2026-09-08, published the following Friday)
Large speculators: net long 0.0% of open interest (12,246 contracts)
Change on the week: -32.8% of open interest
Crowding: 17% percentile over 52 weeks -- within its normal range
Read this as crowding, not as a forecast: an extreme is as often the end of a move as the middle of one.
```

</details>

<details><summary><b>Money going into and out of this fund</b> — score -0.20</summary>

_Not available today._

</details>

### Silver (SLV) · Commodity — NEUTRAL, confidence 0.25

**In the model's own words:**

> Silver is caught in a regime where macro headwinds offset structural support. The dollar surged 1.34% this week to 100.11, and Treasury yields across the curve moved higher—the 5-year up 21bp and 10-year up 14bp—both historically bearish for precious metals. The Fed decision is imminent, with rate-cut expectations uncertain. Against this, news mentions a sixth consecutive supply deficit and constrained mine output, Citigroup sees long-term potential to $90, and safe-haven demand is noted. However, technicals are materially weak: price is down 5.8% below the 20-day MA, 14.2% below the 200-day, and RSI at 43.3 signals oversold but not yet capitulation; MACD histogram is deeply negative. The 1m drawdown of 5.3% and 3m of 11.0% reflect a sustained downtrend. CFTC positioning shows speculators at the 82nd percentile—crowded but not extreme—with modest net long exposure at 13.9% of OI, suggesting neither panic nor euphoria. The cost of holding the fund is -2.8% annually, a persistent drag that requires conviction of a larger move to justify a long. Near-term technicals and rate dynamics point lower, but the supply story and valuation after a 50% pullback from January's $121 peak provide a floor. This is a coin-flip without a fresh catalyst.

**Main reasons it gave:**
- Dollar up 1.34% on week, 5-year yields +21bp and 10-year +14bp; headwind for precious metals ahead of Fed decision
- Price down 14.2% below 200-day MA, RSI 43.3, MACD histogram -0.603; sustained downtrend without reversal signals
- Supply deficit structural support and Citigroup long-term call to $90 offset by near-term technical weakness
- CFTC speculators at 82nd percentile crowding; net long positioning not extreme but not capitulation either
- Fund cost of carry -2.8% annually requires a meaningfully larger move to justify conviction on either side

<details><summary><b>News</b> — score +0.10</summary>

- [Dell Rises 5% Despite Fresh Silver Lake Share Sale Filings; Super Micro Climbs 3%, Hewlett Packard Enterprise Ticks Up](https://247wallst.com/investing/2026/09/16/dell-rises-5-despite-fresh-silver-lake-share-sale-filings-super-micro-climbs-3-hewlett-packard-enterprise-ticks-up/)  
  <sub>24/7 Wall St., 5 hours ago</sub>  
  Silver Lake just filed to sell more Dell shares into a session where the stock is surging, and the server complex is moving like the sponsor notices do not...
- [Current price of silver as of Wednesday, Sept. 16, 2026](https://www.google.com/goto?url=CAESdgHrOzAVdblwn-VWGHsuZwnLcINQoz-nfydu3rM4VV-El2Dfe5mMiv3psxSVP3PRqii4NRwj6fXl9uonlQmhhiNo3kcRAsU39F9hghfDf1Pwc_1oOS5aJUO3RaGaLHV7soazQkL7PskXGutXDwjvdHKcxHn1sLk)  
  <sub>Fortune, 8 hours ago</sub>  
  If you're worried about increased inflation, adding precious metals like silver to your portfolio can be a smart choice.
- [Gold vs Silver ETF: Which Is Better for Investors?](https://www.indmoney.com/blog/mutual-funds/gold-vs-silver-etf-india)  
  <sub>INDmoney, 6 hours ago</sub>  
  Silver ETFs are no longer a small corner of India's mutual fund industry. AMFI's August 2026 report showed 19 Silver ETF schemes with ₹85,488 crore in...
- [Silver Price Today In The UK, 16 September 2026](https://www.google.com/goto?url=CAEScQHrOzAVnKWidt5YxMSPA-UU9veqxfNMzuSWnzMiHgJ2zImNl_t3wT1Kog5gtTHe76itzD4WY29-SprQ9Gz1EwoyU4tTBJRt31DnbQcIMsMXGwmW9OBLqWsllgt3iEjTlAm3tLCKB_IiIa3mpEqd5A7l)  
  <sub>Forbes, 5 hours ago</sub>  
  The price of silver today, as of 9:10 a.m. GMT, is £47.83 per ounce.
- [Silver Price Halves from Its Peak, Citigroup Predicts It Could Eventually Rise to $90](https://nai500.com/blog/2026/09/silver-price-halves-from-its-peak-citigroup-predicts-it-could-eventually-rise-to-90/)  
  <sub>NAI500, 11 hours ago</sub>  
  The price of silver hit an all-time high of more than $121 per ounce in January and has not come close to that level since. On Tuesday, silver traded at...
- [ETF Movers and Shakers: Gold Joins Silver’s Rally as Defence ETFs Cool Off](https://www.google.com/goto?url=CAESmQEB6zswFYcIUt-a_RB2buwLDIl5SiCyPWizt4ur2Ya3uLgIS4C5veaquweGVYj8bKIhuRPNZ99HvO79AwwR_sOigbj5PQkPv1dBm-SVILeOdQQZQLQOF-WszGhPJaZxekWOusyI1KtVAQP85Irp0ZZ6LhKls8dAUnMroBpiGTv0ft-cqpHkLTBqrp-gQEQt7aKvaOHlwxUB6ms)  
  <sub>HDFC Sky, 8 hours ago</sub>  
  Silver and gold ETFs climbed in tandem as safe‑haven demand strengthened, while defence ETFs paused and liquid ETFs stayed steady.
- [Gold and silver tick lower ahead of Fed rate decision (GLD:NYSEARCA)](https://seekingalpha.com/news/4643189-gold-and-silver-tick-lower-ahead-of-fed-rate-decision)  
  <sub>Seeking Alpha, 22 hours ago</sub>  
  Gold and silver futures settled modestly lower a day ahead of the Federal Reserve's interest-rate decision, which is widely expected to be a quarter-point...
- [Silver Price Forecast: Can the Fed Delay the Next Silver Rally?](https://www.equiti.com/sc-en/news/trade-reviews/silver-price-forecast-fed-supply-deficit-2026/)  
  <sub>www.equiti.com, 17 hours ago</sub>  
  Silver prices face pressure from Fed rate expectations, but a sixth consecutive supply deficit and constrained mine output continue supporting the long-term...
- [WisdomTree broadens silver push with currency-hedged ETCs](https://www.thearmchairtrader.com/exchange-traded-funds/wisdomtree-broadens-silver-push-with-currency-hedged-etcs/)  
  <sub>The Armchair Trader, 12 hours ago</sub>  
  WisdomTree is expanding its precious metals offering with currency-hedged silver products, giving investors a more targeted access route.
- [Groww Silver ETF FOF Direct Growth Review 2026: NAV, Returns, Portfolio & Should You Invest?](https://univest.in/blogs/groww-silver-etf-fof-direct-growth-review-2026)  
  <sub>Univest, 8 hours ago</sub>  
  Groww Silver ETF FOF Direct Growth Plan has a NAV of ₹21.8134 and 1-year return of 71.08% as of 15 Sep 2026.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.10</summary>

```text
US Treasury yields: 3-month 3.96% (+0.16 on the week) | 5-year 4.83% (+0.21 on the week) | 10-year 4.97% (+0.14 on the week) | 30-year 5.32% (+0.03 on the week)
Yield curve, 10-year minus 3-month: +1.01 points -- upward sloping (normal)
US dollar index: 100.11 (+1.34 on the week)
Volatility (VIX): 16.79 (+0.3 on the week) -- elevated
```

</details>

<details><summary><b>Price and chart</b> — score -0.40</summary>

```text
Last close 56.41 (bar of 2026-09-16), from 502 daily bars
Trend: vs 20d SMA 59.86 (-5.8%), 50d 56.56 (-0.3%), 200d 65.72 (-14.2%); 50d below 200d
Momentum: RSI(14) 43.3 | MACD -0.113 vs signal 0.490 (histogram -0.603)
Returns: 1d -1.9% | 5d -7.1% | 1m -5.3% | 3m -11.0%
52-week range: 37.79 - 105.60 (now 27.5% of the way up)
Volatility: ATR(14) 1.84 (3.3% of price) | annualised 20d 40.8%
Volume: 1.01x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.15</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score +0.15</summary>

_Not available today._

</details>

<details><summary><b>Does this company beat its own forecasts</b> — score +0.15</summary>

_Not available today._

</details>

<details><summary><b>What holding this fund costs you</b> — score +0.15</summary>

```text
Cost of holding this fund instead of silver itself: -2.8% a year -- a steady drag
Measured: 3 months: fund -11.0%, commodity -9.8%, gap -1.2% | 6 months: fund -21.3%, commodity -20.7%, gap -0.6% | 12 months: fund +45.5%, commodity +48.3%, gap -2.8%
A commodity fund holds futures, not silver, and must sell each expiring contract to buy the next one. Where the next month costs more, that roll loses money every month. This gap is what the structure has actually cost, fees included -- it is history rather than a forecast, and it is not a direction: heavy carry is a reason to want a larger move to justify a long, and a tailwind for a short.
```

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

_Not available today._

</details>

<details><summary><b>Buying and selling by company insiders</b> — score +0.00</summary>

_Not available today._

</details>

<details><summary><b>Who is positioned how</b> — score +0.00</summary>

```text
Contract: SILVER (positions as of 2026-09-08, published the following Friday)
Large speculators: net long 13.9% of open interest (103,250 contracts)
Change on the week: +1.9% of open interest
Crowding: 82% percentile over 52 weeks -- within its normal range
Read this as crowding, not as a forecast: an extreme is as often the end of a move as the middle of one.
```

</details>

<details><summary><b>Money going into and out of this fund</b> — score +0.00</summary>

_Not available today._

</details>

### Soybeans (SOYB) · Commodity — NEUTRAL, confidence 0.25

**In the model's own words:**

> SOYB is at 97.9% of its 52-week range with strong uptrend momentum (price 15% above 200d MA, RSI 66.9 near overbought). Technical setup shows classic signs of an extended move, but multiple factors argue against pressing either direction: (1) positioning has swung sharply negative, with large speculators reducing net long exposure by 24% of open interest in a single week, now at only 32nd percentile--suggesting mean reversion risk or profit-taking; (2) volume is only 0.28x 20d average, indicating thin conviction despite price strength; (3) macro backdrop is mixed, with Treasury yields up 14-21bp across the curve and the dollar up 1.34% on the week, both headwinds for commodity demand; (4) no news catalyst in past 24 hours to justify continuation; (5) cost of holding is negligible at -0.9% annualized, providing no structural argument either way. The fund has delivered 15% return in 3 months, but technicals are stretched, positioning has deteriorated sharply, and breadth is weak. Wait for either a break below recent support or fresh macro/fundamental catalyst before committing to direction.

**Main reasons it gave:**
- RSI 66.9 approaching overbought after 15% 3-month rally
- Large speculator net longs cut 24% of open interest in one week
- Volume 0.28x 20d average despite price near 52-week highs
- Dollar index +1.34% on week, headwind for commodity demand
- No catalyst in latest news; technical extension without fresh conviction

<details><summary><b>News</b> — score +0.00</summary>

_No news found for this one today._

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 3.96% (+0.16 on the week) | 5-year 4.83% (+0.21 on the week) | 10-year 4.97% (+0.14 on the week) | 30-year 5.32% (+0.03 on the week)
Yield curve, 10-year minus 3-month: +1.01 points -- upward sloping (normal)
US dollar index: 100.11 (+1.34 on the week)
Volatility (VIX): 16.79 (+0.3 on the week) -- elevated
```

</details>

<details><summary><b>Price and chart</b> — score +0.40</summary>

```text
Last close 28.00 (bar of 2026-09-16), from 502 daily bars
Trend: vs 20d SMA 27.22 (+2.9%), 50d 26.13 (+7.1%), 200d 24.34 (+15.0%); 50d above 200d
Momentum: RSI(14) 66.9 | MACD 0.586 vs signal 0.579 (histogram 0.007)
Returns: 1d +0.2% | 5d +1.2% | 1m +8.5% | 3m +15.0%
52-week range: 21.46 - 28.14 (now 97.9% of the way up)
Volatility: ATR(14) 0.35 (1.3% of price) | annualised 20d 17.3%
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
Cost of holding this fund instead of soybeans itself: -0.9% a year -- close to nothing, as a physically backed fund should be
Measured: 3 months: fund +15.0%, commodity +16.9%, gap -1.9% | 6 months: fund +16.3%, commodity +14.2%, gap +2.1% | 12 months: fund +25.8%, commodity +26.7%, gap -0.9%
A commodity fund holds futures, not soybeans, and must sell each expiring contract to buy the next one. Where the next month costs more, that roll loses money every month. This gap is what the structure has actually cost, fees included -- it is history rather than a forecast, and it is not a direction: heavy carry is a reason to want a larger move to justify a long, and a tailwind for a short.
```

</details>

<details><summary><b>How much oil and gas is in storage</b> — score -0.10</summary>

_Not available today._

</details>

<details><summary><b>How the crop is growing</b> — score -0.10</summary>

_Not available today._

</details>

<details><summary><b>What analysts and big funds say</b> — score +0.00</summary>

_Not available today._

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score +0.00</summary>

_Not available today._

</details>

<details><summary><b>Buying and selling by company insiders</b> — score -0.35</summary>

_Not available today._

</details>

<details><summary><b>Who is positioned how</b> — score -0.35</summary>

```text
Contract: SOYBEANS (positions as of 2026-09-08, published the following Friday)
Large speculators: net long 0.0% of open interest (28,694 contracts)
Change on the week: -24.0% of open interest
Crowding: 32% percentile over 52 weeks -- within its normal range
Read this as crowding, not as a forecast: an extreme is as often the end of a move as the middle of one.
```

</details>

<details><summary><b>Money going into and out of this fund</b> — score -0.35</summary>

_Not available today._

</details>

### Oil (USO) · Commodity — NEUTRAL, confidence 0.25

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> USO is deeply extended after a 1970s-style energy shock: +20% in a month, +41% above its 200d, and 94% of the way up the 52-week range with RSI 67 and 42% annualised vol. The bullish catalyst (Saudi cargo cancellations, Middle East tensions) is real but already in price, and it is offset by an API build of 7.1M barrels, a crowded speculative position at the 95th percentile of the past year, a dollar up 1.34 on the week and a 21bp jump in 5-year yields. That combination -- late-stage momentum into a crowded trade against a bearish inventory print -- is a reason to stand aside rather than to take a side into the Fed decision. Note one item told readers which equities are the 'only safe way' into energy; treated as promotional noise, not evidence.

**Main reasons it gave:**
- API reports 7.14M barrel US crude build for week ending Sept 11
- Speculative positioning at 95th percentile of 52 weeks -- crowded
- Price 41.7% above 200d SMA, 94% of 52-week range, RSI 67.5
- Dollar index +1.34 and 5-year yield +21bp on the week, headwind for commodities
- Saudi cancelling/deferring European cargoes; crude above $105 on Middle East tension

<details><summary><b>News</b> — score +0.15</summary>

- [Oil Surges, Tanker Rates Soar: ETFs in Play](https://www.zacks.com/stock/news/2990915/oil-surges-tanker-rates-soar-etfs-in-play)  
  <sub>Zacks Investment Research, 27 minutes ago</sub>  
  Middle East tensions are driving oil prices and tanker rates higher. Here are the ETFs benefiting.
- [Equinor plans LNG supply expansion to 10M-15M tons/year to meet surging global demand (USO:NYSEARCA)](https://seekingalpha.com/news/4643380-equinor-plans-lng-supply-expansion-to-10mminus-15m-tons-year-to-meet-surging-global-demand)  
  <sub>Seeking Alpha, 5 hours ago</sub>  
  European natural gas supplier Equinor said it aims to expand its liquefied natural gas supply portfolio to 10M-15M metric tons/​year by the early 2030s to...
- [Navigating the Market: Inflation, Yields, & the Fed](https://finviz.com/news/392452/navigating-the-market-inflation-yields-the-fed)  
  <sub>Finviz, 19 hours ago</sub>  
  U.S. stocks experienced pressure Tuesday as a spike in bond yields and rising crude oil prices weighed on market sentiment ahead of the Federal Reserve's...
- [U.S. crude oil tops $105 as Saudi Arabia said to cancel some European cargoes (USO:NYSEARCA)](https://seekingalpha.com/news/4643207-us-crude-oil-tops-105-as-saudi-arabia-said-to-cancel-some-european-cargoes)  
  <sub>Seeking Alpha, 20 hours ago</sub>  
  US crude oil futures climbed above $105/bbl as Saudi Arabia reportedly canceled or deferred shipments to some European refiners that were scheduled to load...
- [U.S. crude stockpiles rose 7.1M barrels last week, API says (USO:NYSEARCA)](https://seekingalpha.com/news/4643199-u-s-crude-stockpiles-rose-7_1m-barrels-last-week-api-says)  
  <sub>Seeking Alpha, 21 hours ago</sub>  
  The American Petroleum Institute reportedly shows a build of 7.14M barrels of oil in US commercial stockpiles for the week ending September 11.
- [The Global Fuel Shortage Is Here](https://seekingalpha.com/article/4946692-the-global-fuel-shortage-is-here)  
  <sub>Seeking Alpha, 24 hours ago</sub>  
  I maintain that big oil (CVX, XOM) and midstream are the only safe way into energy. Click here to read the full analysis.
- [Inflation Fears and Oil Surge Rattle Markets](https://www.etf.com/sections/bonds/inflation-fears-and-oil-surge-rattle-markets)  
  <sub>ETF.com, 22 hours ago</sub>  
  The summer months may have ended, but the dog days appear to be sticking around, at least for markets. With the Fed rate decision due Wednesday and new...
- [Stocks Rise On Dovish Fed Hike Hopes—Strong Retail Sales Surprise](https://www.benzinga.com/Opinion/26/09/61824301/stocks-rise-on-dovish-fed-hike-hopes-strong-retail-sales-surprise)  
  <sub>Benzinga, 2 hours ago</sub>  
  Dovish Hike Hopium Please click here for an enlarged chart of SPDR S&P 500 ETF Trust (NYSE:SPY) which represents the benchmark stock market index S&P 500...
- [Why Oil Bears May Make a Stand as Prices Approach Highs](https://www.zacks.com/commentary/2990282/why-oil-bears-may-make-a-stand-as-prices-approach-highs)  
  <sub>Zacks Investment Research, 18 hours ago</sub>  
  So far in 2026, global markets have been shaped by a 1970s-esque energy shock that has sent the United States Oil Fund ETF (( USO Quick Quote
- [Evening digest: Clarity Act fails in Senate, US crude hits $106](https://invezz.com/au/news/2026/09/15/evening-digest-clarity-act-fails-in-senate-us-crude-hits-dollar106/)  
  <sub>Invezz, 24 hours ago</sub>  
  Crypto markets faced fresh pressure on Tuesday after the Digital Asset Market Clarity Act failed to secure enough Senate support to advance.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.15</summary>

```text
US Treasury yields: 3-month 3.96% (+0.16 on the week) | 5-year 4.83% (+0.21 on the week) | 10-year 4.97% (+0.14 on the week) | 30-year 5.32% (+0.03 on the week)
Yield curve, 10-year minus 3-month: +1.01 points -- upward sloping (normal)
US dollar index: 100.11 (+1.34 on the week)
Volatility (VIX): 16.79 (+0.3 on the week) -- elevated
```

</details>

<details><summary><b>Price and chart</b> — score +0.35</summary>

```text
Last close 156.47 (bar of 2026-09-16), from 502 daily bars
Trend: vs 20d SMA 141.48 (+10.6%), 50d 130.77 (+19.6%), 200d 110.45 (+41.7%); 50d above 200d
Momentum: RSI(14) 67.5 | MACD 8.320 vs signal 6.485 (histogram 1.835)
Returns: 1d -3.3% | 5d +4.3% | 1m +20.1% | 3m +35.5%
52-week range: 66.17 - 161.86 (now 94.4% of the way up)
Volatility: ATR(14) 5.08 (3.2% of price) | annualised 20d 42.3%
Volume: 0.99x the 20-day average
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

<details><summary><b>Buying and selling by company insiders</b> — score -0.30</summary>

_Not available today._

</details>

<details><summary><b>Who is positioned how</b> — score -0.30</summary>

```text
Contract: CRUDE OIL, LIGHT SWEET (positions as of 2026-09-08, published the following Friday)
Large speculators: net short 1.3% of open interest (753,433 contracts)
Change on the week: +0.1% of open interest
Crowding: 95% percentile over 52 weeks -- a crowded long by the standards of the past year
Read this as crowding, not as a forecast: an extreme is as often the end of a move as the middle of one.
```

</details>

<details><summary><b>Money going into and out of this fund</b> — score -0.30</summary>

_Not available today._

</details>

### Wheat (WEAT) · Commodity — NEUTRAL, confidence 0.25

**In the model's own words:**

> WEAT shows mixed signals that do not yet warrant a directional call. The technical picture is moderately positive: the fund has rallied 16.5% over three months with the 50d MA above the 200d in a constructive trend, and price is now 81.7% of the way up the 52-week range. However, momentum is flat to slightly negative (RSI 54.4, MACD histogram negative), and volume is well below average at 0.32x the 20-day average, which undermines conviction in the move. Positioning data from CFTC (published 2026-09-12, eight days stale by analysis date) shows speculators crowded at the 95th percentile of net longs, a configuration as often the end of a move as the middle of one, and positioning deteriorated 2.2% of open interest in the reporting week. Most tellingly, the cost of holding this fund is -13.9% annually due to futures roll drag: over the past 12 months the commodity returned 39.5% but the fund only 25.7%, a structural headwind that requires materially larger wheat moves to justify holding the fund itself. Macro backdrop is mixed: the dollar surged 1.34% this week to 100.11, a headwind for commodity prices generally, while Treasury yields rose modestly across the curve and the VIX sits at 16.79, neither extreme. No recent news or crop condition data are present. The rally has been real but lacks volume confirmation, positioning is extended, and roll costs are a persistent drag. Without a fresh catalyst or technical breakdown, a neutral stance is warranted.

**Main reasons it gave:**
- Speculators crowded at 95th percentile of net longs, 2.2% reduction this week
- Negative momentum: RSI 54.4, MACD histogram -0.171, volume 0.32x 20-day average
- Roll cost -13.9% annually; commodity +39.5% in 12mo but fund +25.7%
- Dollar strength +1.34% this week to 100.11, headwind for commodities

<details><summary><b>News</b> — score +0.00</summary>

_No news found for this one today._

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 3.96% (+0.16 on the week) | 5-year 4.83% (+0.21 on the week) | 10-year 4.97% (+0.14 on the week) | 30-year 5.32% (+0.03 on the week)
Yield curve, 10-year minus 3-month: +1.01 points -- upward sloping (normal)
US dollar index: 100.11 (+1.34 on the week)
Volatility (VIX): 16.79 (+0.3 on the week) -- elevated
```

</details>

<details><summary><b>Price and chart</b> — score +0.35</summary>

```text
Last close 26.51 (bar of 2026-09-16), from 502 daily bars
Trend: vs 20d SMA 26.60 (-0.3%), 50d 25.28 (+4.9%), 200d 22.90 (+15.8%); 50d above 200d
Momentum: RSI(14) 54.4 | MACD 0.391 vs signal 0.562 (histogram -0.171)
Returns: 1d +0.7% | 5d +0.9% | 1m +6.1% | 3m +16.5%
52-week range: 19.88 - 28.00 (now 81.7% of the way up)
Volatility: ATR(14) 0.64 (2.4% of price) | annualised 20d 30.7%
Volume: 0.32x the 20-day average
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
Cost of holding this fund instead of wheat itself: -13.9% a year -- heavy: rolling contracts costs this fund real money
Measured: 3 months: fund +16.5%, commodity +22.9%, gap -6.4% | 6 months: fund +17.3%, commodity +24.2%, gap -6.9% | 12 months: fund +25.7%, commodity +39.5%, gap -13.9%
A commodity fund holds futures, not wheat, and must sell each expiring contract to buy the next one. Where the next month costs more, that roll loses money every month. This gap is what the structure has actually cost, fees included -- it is history rather than a forecast, and it is not a direction: heavy carry is a reason to want a larger move to justify a long, and a tailwind for a short.
```

</details>

<details><summary><b>How much oil and gas is in storage</b> — score -0.20</summary>

_Not available today._

</details>

<details><summary><b>How the crop is growing</b> — score -0.20</summary>

_Not available today._

</details>

<details><summary><b>What analysts and big funds say</b> — score +0.00</summary>

_Not available today._

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score +0.00</summary>

_Not available today._

</details>

<details><summary><b>Buying and selling by company insiders</b> — score -0.30</summary>

_Not available today._

</details>

<details><summary><b>Who is positioned how</b> — score -0.30</summary>

```text
Contract: WHEAT-SRW (positions as of 2026-09-08, published the following Friday)
Large speculators: net long 1.0% of open interest (484,680 contracts)
Change on the week: -2.2% of open interest
Crowding: 95% percentile over 52 weeks -- a crowded long by the standards of the past year
Read this as crowding, not as a forecast: an extreme is as often the end of a move as the middle of one.
```

</details>

<details><summary><b>Money going into and out of this fund</b> — score -0.30</summary>

_Not available today._

</details>

### Sugar (CANE) · Commodity — NEUTRAL, confidence 0.20

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> CANE is in an uptrend (above all major SMAs, 50d>200d, +20.8% in 3 months) but momentum is rolling over (MACD histogram negative, 5d -1.9%) and speculative sugar longs sit at the 100th percentile of the past year -- a maximally crowded trade with no fresh catalyst. Roll carry of -11.9% a year is a heavy structural drag that demands a much larger move to justify a long. Macro is mildly hostile: yields up 14-21bp across the belly and a dollar up 1.34 on the week are headwinds for dollar-denominated softs. No news and no analyst roll-up for a single-commodity fund. Net: no edge, NEUTRAL.

**Main reasons it gave:**
- Spec net long in Sugar No. 11 at 100th percentile of 52 weeks -- maximally crowded
- Roll cost -11.9%/yr; fund +6.4% vs commodity +18.3% over 12 months
- MACD below signal (histogram -0.060) despite price above 20/50/200d SMAs
- Dollar index +1.34 on the week and 5y yield +21bp -- headwind for softs
- No macro or sector news in the window

<details><summary><b>News</b> — score +0.00</summary>

_No news found for this one today._

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 3.96% (+0.16 on the week) | 5-year 4.83% (+0.21 on the week) | 10-year 4.97% (+0.14 on the week) | 30-year 5.32% (+0.03 on the week)
Yield curve, 10-year minus 3-month: +1.01 points -- upward sloping (normal)
US dollar index: 100.11 (+1.34 on the week)
Volatility (VIX): 16.79 (+0.3 on the week) -- elevated
```

</details>

<details><summary><b>Price and chart</b> — score +0.20</summary>

```text
Last close 11.40 (bar of 2026-09-16), from 502 daily bars
Trend: vs 20d SMA 11.40 (-0.0%), 50d 10.59 (+7.6%), 200d 9.88 (+15.3%); 50d above 200d
Momentum: RSI(14) 56.8 | MACD 0.249 vs signal 0.308 (histogram -0.060)
Returns: 1d +0.1% | 5d -1.9% | 1m +4.3% | 3m +20.8%
52-week range: 9.02 - 11.82 (now 84.8% of the way up)
Volatility: ATR(14) 0.22 (1.9% of price) | annualised 20d 22.0%
Volume: 0.97x the 20-day average
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
Cost of holding this fund instead of sugar itself: -11.9% a year -- heavy: rolling contracts costs this fund real money
Measured: 3 months: fund +20.8%, commodity +36.9%, gap -16.1% | 6 months: fund +16.5%, commodity +30.9%, gap -14.4% | 12 months: fund +6.4%, commodity +18.3%, gap -11.9%
A commodity fund holds futures, not sugar, and must sell each expiring contract to buy the next one. Where the next month costs more, that roll loses money every month. This gap is what the structure has actually cost, fees included -- it is history rather than a forecast, and it is not a direction: heavy carry is a reason to want a larger move to justify a long, and a tailwind for a short.
```

</details>

<details><summary><b>How much oil and gas is in storage</b> — score -0.45</summary>

_Not available today._

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

<details><summary><b>Buying and selling by company insiders</b> — score -0.30</summary>

_Not available today._

</details>

<details><summary><b>Who is positioned how</b> — score -0.30</summary>

```text
Contract: SUGAR NO. 11 (positions as of 2026-09-08, published the following Friday)
Large speculators: net long 18.7% of open interest (1,276,579 contracts)
Change on the week: +0.4% of open interest
Crowding: 100% percentile over 52 weeks -- a crowded long by the standards of the past year
Read this as crowding, not as a forecast: an extreme is as often the end of a move as the middle of one.
```

</details>

<details><summary><b>Money going into and out of this fund</b> — score -0.30</summary>

_Not available today._

</details>

### Corn (CORN) · Commodity — NEUTRAL, confidence 0.20

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Uptrend is intact (price above 20/50/200d, +18% over 3 months, near 52-week highs), but the supporting evidence argues against chasing. Speculative net long sits at the 100th percentile of the past year -- a maximally crowded long, which is as often exhaustion as continuation -- and MACD has rolled under its signal line with volume at a quarter of average, so the push to highs is thin. Roll carry of -13.8% a year is a heavy structural drag that demands a much larger move to justify a long. Macro is a mild headwind: yields up across the curve and the dollar +1.34 on the week, both unfriendly to dollar-priced commodities. No crop condition data and no macro news this cycle. Net: no fresh catalyst, crowded positioning, punishing carry -- NEUTRAL.

**Main reasons it gave:**
- Spec net long at 100th percentile of 52 weeks, only +0.3% change on the week
- Roll cost -13.8% a year vs spot corn; fund +12.3% vs commodity +26.2% over 12m
- Price 91.6% up the 52-week range, above all major SMAs, but MACD histogram negative (-0.066)
- Volume 0.25x the 20-day average on the approach to highs
- Dollar index +1.34 and 5y yield +0.21 on the week -- commodity headwind

<details><summary><b>News</b> — score +0.00</summary>

_No news found for this one today._

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 3.96% (+0.16 on the week) | 5-year 4.83% (+0.21 on the week) | 10-year 4.97% (+0.14 on the week) | 30-year 5.32% (+0.03 on the week)
Yield curve, 10-year minus 3-month: +1.01 points -- upward sloping (normal)
US dollar index: 100.11 (+1.34 on the week)
Volatility (VIX): 16.79 (+0.3 on the week) -- elevated
```

</details>

<details><summary><b>Price and chart</b> — score +0.35</summary>

```text
Last close 19.97 (bar of 2026-09-16), from 502 daily bars
Trend: vs 20d SMA 19.79 (+0.9%), 50d 18.62 (+7.2%), 200d 18.03 (+10.7%); 50d above 200d
Momentum: RSI(14) 64.1 | MACD 0.433 vs signal 0.499 (histogram -0.066)
Returns: 1d -0.3% | 5d +0.7% | 1m +8.2% | 3m +18.0%
52-week range: 16.47 - 20.29 (now 91.6% of the way up)
Volatility: ATR(14) 0.31 (1.6% of price) | annualised 20d 15.1%
Volume: 0.25x the 20-day average
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
Cost of holding this fund instead of corn itself: -13.8% a year -- heavy: rolling contracts costs this fund real money
Measured: 3 months: fund +18.0%, commodity +29.1%, gap -11.1% | 6 months: fund +8.9%, commodity +17.6%, gap -8.7% | 12 months: fund +12.3%, commodity +26.2%, gap -13.8%
A commodity fund holds futures, not corn, and must sell each expiring contract to buy the next one. Where the next month costs more, that roll loses money every month. This gap is what the structure has actually cost, fees included -- it is history rather than a forecast, and it is not a direction: heavy carry is a reason to want a larger move to justify a long, and a tailwind for a short.
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

<details><summary><b>Buying and selling by company insiders</b> — score -0.30</summary>

_Not available today._

</details>

<details><summary><b>Who is positioned how</b> — score -0.30</summary>

```text
Contract: CORN (positions as of 2026-09-08, published the following Friday)
Large speculators: net long 23.0% of open interest (1,803,323 contracts)
Change on the week: +0.3% of open interest
Crowding: 100% percentile over 52 weeks -- a crowded long by the standards of the past year
Read this as crowding, not as a forecast: an extreme is as often the end of a move as the middle of one.
```

</details>

<details><summary><b>Money going into and out of this fund</b> — score -0.30</summary>

_Not available today._

</details>

### Copper (CPER) · Commodity — NEUTRAL, confidence 0.20

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> No macro catalyst. Copper fund is below its 20d and 50d averages with negative MACD and a 6% five-day drop, but still above the 200d and near the upper end of the 52-week range. Rates rose across the curve and the dollar gained 1.34 on the week, a mild headwind for industrial metals. Speculative net long sits at the 90th percentile and rose again, so the long is crowded, and the fund bleeds roughly 5.4% a year to roll versus copper itself. That combination argues against a long here but is not enough to short: NEUTRAL with a slight negative tilt.

**Main reasons it gave:**
- Price below 20d (-2.8%) and 50d (-2.0%) SMAs, MACD histogram -0.210
- 5-day return -6.1% on light volume (0.65x)
- CFTC spec net long 27.6% of OI, 90th percentile, +1.8% on week
- Roll cost -5.4%/yr versus physical copper
- Dollar index +1.34 and 5y yield +21bp on the week

<details><summary><b>News</b> — score +0.00</summary>

_No news found for this one today._

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 3.96% (+0.16 on the week) | 5-year 4.83% (+0.21 on the week) | 10-year 4.97% (+0.14 on the week) | 30-year 5.32% (+0.03 on the week)
Yield curve, 10-year minus 3-month: +1.01 points -- upward sloping (normal)
US dollar index: 100.11 (+1.34 on the week)
Volatility (VIX): 16.79 (+0.3 on the week) -- elevated
```

</details>

<details><summary><b>Price and chart</b> — score -0.25</summary>

```text
Last close 38.53 (bar of 2026-09-16), from 502 daily bars
Trend: vs 20d SMA 39.65 (-2.8%), 50d 39.32 (-2.0%), 200d 37.01 (+4.1%); 50d above 200d
Momentum: RSI(14) 42.6 | MACD -0.174 vs signal 0.036 (histogram -0.210)
Returns: 1d -0.4% | 5d -6.1% | 1m -4.0% | 3m -2.6%
52-week range: 28.34 - 41.05 (now 80.2% of the way up)
Volatility: ATR(14) 0.70 (1.8% of price) | annualised 20d 26.4%
Volume: 0.65x the 20-day average
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
Cost of holding this fund instead of copper itself: -5.4% a year -- heavy: rolling contracts costs this fund real money
Measured: 3 months: fund -2.6%, commodity -0.9%, gap -1.7% | 6 months: fund +9.4%, commodity +12.3%, gap -2.9% | 12 months: fund +32.7%, commodity +38.1%, gap -5.4%
A commodity fund holds futures, not copper, and must sell each expiring contract to buy the next one. Where the next month costs more, that roll loses money every month. This gap is what the structure has actually cost, fees included -- it is history rather than a forecast, and it is not a direction: heavy carry is a reason to want a larger move to justify a long, and a tailwind for a short.
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

<details><summary><b>Buying and selling by company insiders</b> — score -0.30</summary>

_Not available today._

</details>

<details><summary><b>Who is positioned how</b> — score -0.30</summary>

```text
Contract: COPPER (positions as of 2026-09-08, published the following Friday)
Large speculators: net long 27.6% of open interest (297,491 contracts)
Change on the week: +1.8% of open interest
Crowding: 90% percentile over 52 weeks -- a crowded long by the standards of the past year
Read this as crowding, not as a forecast: an extreme is as often the end of a move as the middle of one.
```

</details>

<details><summary><b>Money going into and out of this fund</b> — score -0.30</summary>

_Not available today._

</details>

### Natural gas (UNG) · Commodity — NEUTRAL, confidence 0.20

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> No macro or supply catalyst this cycle. Price is flat against 20d/50d with RSI near 50 and 50d below 200d, near the bottom decile of the 52-week range. Speculative positioning is neutral and unchanged. The one durable fact is heavy negative roll carry (-14.8%/yr), which argues against holding a long absent a strong directional case; it is not by itself a directional signal. Rising yields and a stronger dollar are a mild headwind. No inventory data available this cycle. The single LNG headline is a long-dated supply story and not tradable here.

**Main reasons it gave:**
- Roll cost -14.8% a year vs spot natural gas, heavy negative carry
- 50d SMA below 200d, price -10.6% vs 200d and only 10% up the 52-week range
- RSI 50.7, MACD barely above signal -- no momentum edge
- CFTC specs net long unchanged, 63rd percentile crowding -- normal range
- Dollar +1.34 on the week and 5y yield +21bp, mild commodity headwind

<details><summary><b>News</b> — score +0.00</summary>

- [Equinor plans LNG supply expansion to 10M-15M tons/year to meet surging global demand (USO:NYSEARCA)](https://seekingalpha.com/news/4643380-equinor-plans-lng-supply-expansion-to-10mminus-15m-tons-year-to-meet-surging-global-demand)  
  <sub>Seeking Alpha, 5 hours ago</sub>  
  European natural gas supplier Equinor said it aims to expand its liquefied natural gas supply portfolio to 10M-15M metric tons/​year by the early 2030s to...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 3.96% (+0.16 on the week) | 5-year 4.83% (+0.21 on the week) | 10-year 4.97% (+0.14 on the week) | 30-year 5.32% (+0.03 on the week)
Yield curve, 10-year minus 3-month: +1.01 points -- upward sloping (normal)
US dollar index: 100.11 (+1.34 on the week)
Volatility (VIX): 16.79 (+0.3 on the week) -- elevated
```

</details>

<details><summary><b>Price and chart</b> — score -0.10</summary>

```text
Last close 10.35 (bar of 2026-09-16), from 502 daily bars
Trend: vs 20d SMA 10.33 (+0.2%), 50d 10.27 (+0.8%), 200d 11.59 (-10.6%); 50d below 200d
Momentum: RSI(14) 50.7 | MACD 0.025 vs signal 0.018 (histogram 0.006)
Returns: 1d -1.8% | 5d +2.6% | 1m +5.3% | 3m -11.9%
52-week range: 9.63 - 16.90 (now 10.0% of the way up)
Volatility: ATR(14) 0.28 (2.7% of price) | annualised 20d 24.4%
Volume: 1.46x the 20-day average
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
Cost of holding this fund instead of natural gas itself: -14.8% a year -- heavy: rolling contracts costs this fund real money
Measured: 3 months: fund -11.9%, commodity -10.7%, gap -1.2% | 6 months: fund -15.1%, commodity -4.6%, gap -10.5% | 12 months: fund -19.8%, commodity -5.0%, gap -14.8%
A commodity fund holds futures, not natural gas, and must sell each expiring contract to buy the next one. Where the next month costs more, that roll loses money every month. This gap is what the structure has actually cost, fees included -- it is history rather than a forecast, and it is not a direction: heavy carry is a reason to want a larger move to justify a long, and a tailwind for a short.
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
Contract: NATURAL GAS (positions as of 2026-09-01, published the following Friday)
Large speculators: net long 0.0% of open interest (17,407 contracts)
Change on the week: +0.0% of open interest
Crowding: 63% percentile over 52 weeks -- within its normal range
Read this as crowding, not as a forecast: an extreme is as often the end of a move as the middle of one.
```

</details>

<details><summary><b>Money going into and out of this fund</b> — score +0.00</summary>

_Not available today._

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

