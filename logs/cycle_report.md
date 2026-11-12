# Daily report

**12 Nov 2026, 17:52 Israel time (15:52 UTC)** · 80 names checked · 2 traded · 0 with a problem

**Answers with no explanation:** 15 of 63 (the model wrote only a label, like “NEUTRAL”, where its reason should be). Their main reasons are still shown.

**Run:** started by the outside scheduler (via supabase-cron), on time (planned for 14:40 UTC).

| Group | Looked at | Took a side | No clear view | Problems |
| --- | --- | --- | --- | --- |
| Companies | 16 | 6 | 10 | 0 |
| Whole-market funds | 14 | 0 | 14 | 0 |
| Sector and country funds | 41 | 2 | 39 | 0 |
| Commodities | 9 | 0 | 9 | 0 |

## Open positions

Checked before any new trade. R is what the trade risked at entry; the ladder sells a third at +1R and another at +3R, the stop-loss follows the price up every day, and it only ever moves up.

| Position | What happened |
| --- | --- |
| Teva Pharmaceutical (TEVA) · Company | **Sold part.** Sold 18 of 54 shares at +1.08R, 36 still held. Stop-loss raised 40.47 → 41.01. |
| Poland (EPOL) · Sector or country | **Stop raised.** At +0.22R, following the price. Stop-loss raised 41.87 → 42.32. |
| Brazil (EWZ) · Sector or country | **Stop raised.** At +0.43R, following the price. Stop-loss raised 34.44 → 34.10. |
| Defence and aerospace (ITA) · Sector or country | **Stop raised.** At +0.46R, following the price. Stop-loss raised 68.78 → 69.44. |
| MercadoLibre (MELI) · Company | **Stop raised.** At +0.06R, following the price. Stop-loss raised 1625.00 → 1615.69. |
| Nvidia (NVDA) · Company | **Stop raised.** At +4.75R, following the price. Stop-loss raised 188.69 → 179.59. |
| Procter & Gamble (PG) · Company | **Stop raised.** At +1.20R, following the price. Stop-loss raised 162.55 → 162.86. |
| US house builders (XHB) · Sector or country | **Stop raised.** At +0.10R, following the price. Stop-loss raised 96.69 → 97.50. |
| US media and communication (XLC) · Sector or country | **Stop raised.** At +2.24R, following the price. Stop-loss raised 104.22 → 104.47. |
| Elbit Systems (ESLT) · Company | **Holding.** +1.18R, holding 5 shares. Stop-loss 682.06. |
| Canada (EWC) · Sector or country | **Holding.** -0.25R, holding 116 shares. Stop-loss 58.92. |
| South Korea (EWY) · Sector or country | **Holding.** -0.50R, holding 51 shares. Stop-loss 152.20. |
| Alphabet (Google) (GOOGL) · Company | **Holding.** -0.43R, holding 12 shares. Stop-loss 298.22. |
| HDFC Bank (HDB) · Company | **Holding.** +2.42R, holding 102 shares. Stop-loss 24.78. |
| Microsoft (MSFT) · Company | **Holding.** -0.53R, holding 9 shares. Stop-loss 512.86. |
| Novo Nordisk (NVO) · Company | **Holding.** -0.04R, holding 124 shares. Stop-loss 38.63. |
| Toyota (TM) · Company | **Holding.** +3.10R, holding 2 shares. Stop-loss 210.74. |

## How to read this

Once a day the system looks at every name on the list. For each one it reads five kinds of evidence and gives each kind a score from -1.00 (bad) to +1.00 (good). Then it picks a side and says how sure it is, from 0.00 to 1.00.

The three sides: **BULLISH** = the model thinks the price will go up; **BEARISH** = the model thinks the price will go down; **NEUTRAL** = the model has no clear view.

Being sure is not enough on its own. A trade only happens when confidence reaches **0.30**. Below that the system writes down what it thought and does nothing. The size of a trade, the stop-loss and every limit are decided by plain code, not by the model.

Open positions are checked first, before any new trade. When a trade has earned back what it risked (+1R), a third of it is sold and the stop-loss moves up to the entry price, so it can no longer lose. At three times that (+3R) another third is sold and the stop moves up again. The last third stays open. Every day the stop-loss also follows the price up, so a position only ever closes when its stop is hit. The stop only ever moves up.

Under each name you will find the five scores. Click a grey line to open it and see the exact evidence behind that score. The words inside quotation marks are the model's own; nothing there has been rewritten.

## Companies

### Eli Lilly (LLY) · Company — BULLISH, confidence 0.75

**Result:** REJECTED · no room under the sleeve budget limit

**In the model's own words:** no explanation. It wrote only “BUY”, so the main reasons below are all it gave.

**Main reasons it gave:**
- China approved Orforglipron, the first oral GLP-1 weight-loss pill
- Bank of America raised LLY price target to $1,557 ahead of R&D Day
- Four consecutive earnings beats, latest beat 18% above consensus
- Strong profit margin (31.9%) and revenue growth (+38.6% YoY) support fundamentals
- Technicals show overbought RSI 71 and thin volume, indicating short-term risk

<details><summary><b>News</b> — score +0.90</summary>

- [Bank of America resets Eli Lilly stock target ahead of key event](http://www.bing.com/news/apiclick.aspx?ref=FexRss&aid=&tid=6af5d0446fe94b4fb534b996920b30a4&url=https%3a%2f%2fwww.msn.com%2fen-us%2fmoney%2ftop-stocks%2fbank-of-america-resets-eli-lilly-stock-target-ahead-of-key-event%2far-AA2hfaVy&c=5159421767452965606&mkt=en-us)  
  <sub>TheStreet on MSN, 31h ago</sub>  
  BofA's Jason Gerberry raised Eli Lilly's stock target to $1,557 before the drugmaker's Dec. 7 R&D Day, looking past its weight-loss franchise.
- [Can LLY's expanding obesity pipeline sustain its GLP-1 leadership?](http://www.bing.com/news/apiclick.aspx?ref=FexRss&aid=&tid=6af5d0446fe94b4fb534b996920b30a4&url=https%3a%2f%2fwww.msn.com%2fen-us%2fhealth%2fweightloss%2fcan-lly-s-expanding-obesity-pipeline-sustain-its-glp-1-leadership%2far-AA2hi60b&c=10255341123747634727&mkt=en-us)  
  <sub>Zacks Investment Research on MSN, 11h ago</sub>  
  Eli Lilly and Company LLY has established itself as a dominant player in the rapidly expanding obesity treatment market, driven by the strong efficacy, robust demand and growing adoption of its ...
- [Eli Lilly (LLY) Stock Climbs as China Approves First GLP-1 Weight-Loss Pill](http://www.bing.com/news/apiclick.aspx?ref=FexRss&aid=&tid=6af5d0446fe94b4fb534b996920b30a4&url=https%3a%2f%2fblockonomi.com%2feli-lilly-lly-stock-climbs-as-china-approves-first-glp-1-weight-loss-pill%2f&c=16553061389739453744&mkt=en-us)  
  <sub>Blockonomi, 10h ago</sub>  
  Eli Lilly (LLY) stock hit a record high premarket after China approved orforglipron, the first GLP-1 weight-loss pill there, ahead of Novo Nordisk.
- [Eli Lilly’s Orforglipron Wins Big In China – Gains Edge Over Novo In Race For Potential $4.5B Market](http://www.bing.com/news/apiclick.aspx?ref=FexRss&aid=&tid=6af5d0446fe94b4fb534b996920b30a4&url=https%3a%2f%2fstocktwits.com%2fnews-articles%2fmarkets%2fequity%2feli-lilly-orforglipron-china-approval-novo-race-for-potential-market-share%2fcNGzsl1R9a5&c=1710885891918305100&mkt=en-us)  
  <sub>Stocktwits, 12h ago</sub>  
  Orforglipron, which is marketed as Foundayo, became the first weight-loss pill to receive approval in China, according to a Reuters report.
- [Eli Lilly & Co (LLY) Stock Forecast & Price Target](http://www.bing.com/news/apiclick.aspx?ref=FexRss&aid=&tid=6af5d0446fe94b4fb534b996920b30a4&url=https%3a%2f%2fwww.tipranks.com%2fstocks%2flly%2fforecast&c=16406667696964200623&mkt=en-us)  
  <sub>tipranks, 26h ago</sub>  
  Next quarter’s earnings estimate for LLY is $11.19 with a range of $10.36 to $12.42. The previous quarter’s EPS was $7.48. Its overall industry beat the EPS estimate 57.80% of the time in the past 12 ...
- [Eli Lilly Just Raised Its 2026 Sales Forecast to as Much as $92 Billion. But Is Viking Therapeutics the Next Big Obesity Winner?](http://www.bing.com/news/apiclick.aspx?ref=FexRss&aid=&tid=6af5d0446fe94b4fb534b996920b30a4&url=https%3a%2f%2fwww.msn.com%2fen-us%2fmoney%2fother%2feli-lilly-just-raised-its-2026-sales-forecast-to-as-much-as-92-billion-but-is-viking-therapeutics-the-next-big-obesity-winner%2far-AA2hfyTK&c=16605784061087818946&mkt=en-us)  
  <sub>The Motley Fool on MSN, 23h ago</sub>  
  These drugmakers offer very different risk-reward profiles.
- [Hims & Hers Lands Eli Lilly's GLP-1s at $149 a Month, Drops Compounded Copies](http://www.bing.com/news/apiclick.aspx?ref=FexRss&aid=&tid=6af5d0446fe94b4fb534b996920b30a4&url=https%3a%2f%2f247wallst.com%2fcards%2fnasdaq-jumps-over-4-this-week-as-chip-names-drive-a-sharp-midweek-rally-nvda-press-release-01m75y57wh3k6dmx1ne1nmxcah&c=13351945905093285717&mkt=en-us)  
  <sub>24/7 Wall St., 28h ago</sub>  
  Hims & Hers just landed Eli Lilly's branded GLP-1s on its platform, with self-pay pricing starting at $149 a month for Foundayo, and it agreed to stop offering compounded copies of Lilly's drugs.
- [中国での初の経口GLP-1減量薬承認を受けイーライリリーが時間外で3％超上昇、LLYは過去最高値に迫る](http://www.bing.com/news/apiclick.aspx?ref=FexRss&aid=&tid=6af5d0446fe94b4fb534b996920b30a4&url=https%3a%2f%2fwww.tradingkey.com%2fjp%2fanalysis%2fstocks%2fus-stocks%2f262302519-eli-lilly-surges-approval-china-first-oral-glp-1-lly-stock-toward-all-time-high-tradingkey&c=6685851019795334106&mkt=en-us)  
  <sub>tradingkey, 11h ago</sub>  
  TradingKey - 木曜日の米株市場のプレマーケット取引で、イーライリリー（LLY）は3%超上昇し、1,488ドル近辺まで値を上げた。この上昇が通常取引でも維持されれば、過去最高値を更新する見込みとなっている。市場の強気センチメントを後押しする主な材料は、イーライリリーの経口GLP-1減量薬であるオルホルグリプロンカルシウム錠が、「Muyouda」のブランド名で中国国家薬品監督管理局（NMP ...
- [禮來盤前漲超3%，中國首款口服減肥藥GLP-1獲批助推LLY股價衝擊歷史新高](http://www.bing.com/news/apiclick.aspx?ref=FexRss&aid=&tid=6af5d0446fe94b4fb534b996920b30a4&url=https%3a%2f%2fwww.tradingkey.com%2fzh-hant%2fanalysis%2fstocks%2fus-stock%2f262302506-eli-lilly-surges-approval-china-first-oral-glp-1-lly-stock-toward-all-time-high-tradingkey&c=12894542078362004263&mkt=en-us)  
  <sub>tradingkey, 19h ago</sub>  
  TradingKey - 禮來（LLY）週四美股盤前一度上漲逾3%，股價升至1488美元附近，若此漲勢延續至正式開盤，公司股價有望刷新歷史紀錄。推動市場情緒升溫的核心因素，是禮來旗下口服GLP-1減重藥奧氟格列隆鈣片正式獲得中國國家藥監局批准，商品名為「穆優達」。

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.90</summary>

_Not available today._

</details>

<details><summary><b>Price and chart</b> — score -0.50</summary>

```text
Last close 1,444.60 (bar of 2026-11-12), from 502 daily bars
Trend: vs 20d SMA 1,347.79 (+7.2%), 50d 1,235.75 (+16.9%), 200d 1,107.31 (+30.5%); 50d above 200d
Momentum: RSI(14) 71.0 | MACD 58.251 vs signal 53.125 (histogram 5.126)
Returns: 1d +0.5% | 5d +5.9% | 1m +19.5% | 3m +22.4%
52-week range: 851.21 - 1,444.60 (now 100.0% of the way up)
Volatility: ATR(14) 44.98 (3.1% of price) | annualised 20d 38.1%
Volume: 0.09x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.20</summary>

```text
Sector: Healthcare / Drug Manufacturers - General | market cap 1.29T
Valuation: trailing P/E 46.85 | forward P/E 28.50 | P/B 31.94 | PEG 1.32
Profitability: profit margin 31.9% | operating margin 51.3% | ROE 86.0%
Growth (YoY): revenue +38.6% | earnings +16.3%
Balance sheet: debt/equity 122.9% | free cash flow 9.34B
Risk: beta 0.39 | short interest 0.8% of float
Next earnings: 2026-10-29
```

</details>

<details><summary><b>What this fund holds</b> — score +0.20</summary>

_Not available today._

</details>

<details><summary><b>Does this company beat its own forecasts</b> — score +0.20</summary>

```text
Earnings record, last 4 quarters: 4 beats
  2026-09-30 beat by 18% | 2026-06-30 beat by 38% | 2026-03-31 beat by 27% | 2025-12-31 beat by 12%
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

<details><summary><b>What analysts and big funds say</b> — score +0.10</summary>

```text
Consensus: buy (mean 1.61 on a 1=strong buy to 5=strong sell scale, 29 analysts)
Ratings: 5 strong buy, 20 buy, 4 hold, 1 sell, 1 strong sell
Price target: mean 1,460.30 (+1.1% vs last close), range 940.00 - 1,690.00
Recent rating changes:
  - 2026-11-09 Jefferies: main, Buy -> Buy
  - 2026-11-02 Cantor Fitzgerald: main, Overweight -> Overweight
  - 2026-10-31 UBS: main, Buy -> Buy
  - 2026-10-30 JP Morgan: main, Overweight -> Overweight
  - 2026-10-30 Citigroup: main, Buy -> Buy
  - 2026-10-30 Scotiabank: main, Sector Outperform -> Sector Outperform
Institutional ownership: 85.9%
Largest holders: Lilly Endowment, Inc (9.6%), Blackrock Inc. (7.2%), Vanguard Capital Management LLC (5.7%), PNC Financial Services Group, Inc. (5.5%), State Street Corporation (3.9%)
```

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score +0.10</summary>

_Not available today._

</details>

<details><summary><b>Buying and selling by company insiders</b> — score +0.00</summary>

```text
Last 180 days: bought 38,018 shares in 36 transaction(s) | sold 313,215 shares in 9
Net: -275,197 shares (-16.1% of insider holdings) | insiders hold 1,434,099 shares
Distinct insiders: 0 buying, 4 selling
Sales — weak evidence on their own; often scheduled 10b5-1 plans, tax on vesting, or diversification:
  - 2026-11-02 HAKIM ANAT (General Counsel): 5,000 shares, 7.01M
  - 2026-08-17 JONSSON PATRIK (Officer): 6,500 shares, 7.64M
  - 2026-08-10 ZAKROWSKI DONALD A (Officer): 2,000 shares, 2.37M
  - 2026-08-07 HAKIM ANAT (General Counsel): 5,000 shares, 5.95M
(36 grant/option/gift transaction(s) excluded — compensation, not a view on the price)
```

</details>

<details><summary><b>Who is positioned how</b> — score +0.00</summary>

_Not available today._

</details>

<details><summary><b>Money going into and out of this fund</b> — score +0.00</summary>

_Not available today._

</details>

### ASML (ASML) · Company — BULLISH, confidence 0.68

**Result:** REJECTED · no room under the sleeve budget limit

**In the model's own words:**

> Strong, ticker‑specific news of record sales and multi‑year demand outlook, combined with exceptionally robust fundamentals, outweighs the bearish technical positioning. Analyst consensus is already strongly positive, adding little incremental edge, and there is no insider activity to alter the view.

**Main reasons it gave:**
- Record Q3 sales reported, indicating strong demand
- Customers planning orders through 2029, suggesting long‑term growth
- Fundamentals: 55% YoY revenue growth, 136% earnings growth, high margins and low debt
- Technical: price below 20‑day, 50‑day and 200‑day SMAs with very low volume

<details><summary><b>News</b> — score +0.90</summary>

- [Wall Street's Next Blockbuster Stock Split Could Come From This Chip Equipment Giant](http://www.bing.com/news/apiclick.aspx?ref=FexRss&aid=&tid=6af5d00925b34383bb512a990e9a4f85&url=https%3a%2f%2fwww.fool.com%2finvesting%2f2026%2f11%2f12%2fwall-streets-next-blockbuster-stock-split-could-co%2f&c=6708155906090681053&mkt=en-us)  
  <sub>The Motley Fool, 9h ago</sub>  
  ASML posted record sales in its latest quarter, and some customers are already eyeing orders for delivery in 2029.
- [ASML stock enters capacity test as AI demand reaches into 2030](http://www.bing.com/news/apiclick.aspx?ref=FexRss&aid=&tid=6af5d00925b34383bb512a990e9a4f85&url=https%3a%2f%2fwww.ad-hoc-news.de%2fboerse%2fnews%2fcorporate-news%2fasml-stock-enters-capacity-test-as-ai-demand-reaches-into-2030%2f70496481&c=12907182551071478185&mkt=en-us)  
  <sub>Ad Hoc News, 13h ago</sub>  
  ASML Holding stock is tied to a stronger AI equipment cycle and customer planning through 2030. Capacity expansion is now the key execution test. ASML reported record third-quarter sales and raised ...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.90</summary>

_Not available today._

</details>

<details><summary><b>Price and chart</b> — score -0.50</summary>

```text
Last close 1,521.52 (bar of 2026-11-12), from 502 daily bars
Trend: vs 20d SMA 1,564.62 (-2.8%), 50d 1,664.00 (-8.6%), 200d 1,602.14 (-5.0%); 50d above 200d
Momentum: RSI(14) 44.1 | MACD -55.404 vs signal -55.293 (histogram -0.110)
Returns: 1d -0.8% | 5d +12.2% | 1m -7.8% | 3m -17.5%
52-week range: 966.57 - 1,989.44 (now 54.3% of the way up)
Volatility: ATR(14) 66.00 (4.3% of price) | annualised 20d 61.9%
Volume: 0.16x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.90</summary>

```text
Sector: Technology / Semiconductor Equipment & Materials | market cap 586.42B
Valuation: trailing P/E 37.44 | forward P/E 24.00 | P/B 1,306.45 | PEG 0.79
Profitability: profit margin 34.1% | operating margin 38.6% | ROE 65.6%
Growth (YoY): revenue +55.2% | earnings +135.9%
Balance sheet: debt/equity 8.9% | free cash flow 10.37B
Risk: beta 1.33 | short interest 0.3% of float
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

<details><summary><b>What analysts and big funds say</b> — score +0.00</summary>

```text
Consensus: strong_buy (mean 1.37 on a 1=strong buy to 5=strong sell scale, 17 analysts)
Ratings: 7 strong buy, 31 buy, 2 hold, 1 sell, 0 strong sell
Price target: mean 2,127.30 (+39.8% vs last close), range 858.07 - 2,818.73
Recent rating changes:
  - 2026-10-15 JP Morgan: main, Overweight -> Overweight
  - 2026-07-16 JP Morgan: main, Overweight -> Overweight
  - 2026-07-16 Wells Fargo: main, Overweight -> Overweight
  - 2026-07-16 RBC Capital: main, Outperform -> Outperform
  - 2026-07-14 RBC Capital: main, Outperform -> Outperform
  - 2026-07-06 Bernstein: main, Outperform -> Outperform
Institutional ownership: 20.4%
Largest holders: FMR, LLC (1.5%), Fisher Asset Management, LLC (1.2%), Capital World Investors (1.0%), Invesco Ltd. (0.8%), State Farm Mutual Automobile Insurance Co (0.7%)
```

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score +0.00</summary>

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

### Caterpillar (CAT) · Company — BULLISH, confidence 0.65

**Result:** REJECTED · no room under the sleeve budget limit

**In the model's own words:**

> A material $3.4B AI generator contract (news) provides a strong bullish catalyst, supported by solid fundamentals and a recent earnings beat record. Technicals are weak (downtrend, low volume) and insider activity is neutral‑to‑slightly bearish, tempering conviction to a moderate level.

**Main reasons it gave:**
- Anthropic $3.4B AI generator contract announced (news)
- RSI 34.6, price below 20d/50d/200d SMAs, volume 0.06x 20‑day avg (technical)
- Forward P/E 18.5, PEG 1.02, ROE 56% (fundamentals)
- 3 earnings beats, 1 in line in last 4 quarters (earnings)
- Insider net +20,022 shares; 1,000‑share director purchase vs CEO sold 32,401 shares (insider)

<details><summary><b>News</b> — score +0.80</summary>

- [Caterpillar (CAT) Stock Looks Like A Bargain On Its 222% Run](https://finance.yahoo.com/markets/stocks/articles/caterpillar-cat-stock-looks-bargain-231435012.html)  
  <sub>Yahoo Finance, 15 hours ago</sub>  
  Caterpillar has climbed sharply over the past few years and now trades at US$601.61, which naturally raises a simple question for anyone looking at the...
- [Can Caterpillar Stock Hit $820?](https://www.trefis.com/stock/cat/articles/624242/can-caterpillar-stock-hit-820/2026-11-11)  
  <sub>Trefis, 17 hours ago</sub>  
  For questions about this article or underlying research, email help@trefis.com. Caterpillar (CAT) stock closed at $584.57 on November 10, down 26.8% from...
- [Red Cat Earnings Preview: Real Army Orders, But A Stock Price I Can't Justify](https://www.google.com/goto?url=CAESsAEBxCJF15GTMApRLRPyVAt222EZP0_YgReNzvHE7Zg20VSZunPcwQdAx1yAXDjETiJYge4rMhASnAgkoaNa1bGxXnGVZsWjBp3s8UMb7keC0w2iIYQiGzX3n8Jon_sJaEuy30F3Si9pLv0KE8D7RRMqkLNyDNziFw79AX6rYQHT_JWWhdMKXwlBRPS3sG3WNA1sXNnVdFDJ8XNzwdlhD0svbVz37fOU3Z_dqbBziu5bFA&gsessionid=GxP4UoDrw6aE_-Bi8G55W6p7jP76LdZtH-3-M4F-Ggjjw-xueJgHsw)  
  <sub>Seeking Alpha, 2 hours ago</sub>  
  Red Cat has secured real defense contracts, but current valuation already prices in aggressive success and growth. Click here for this RCAT stock update.
- [Red Cat Climbs 5%, Ondas Gains 4% as Drone Stocks Rebound; AeroVironment Rises 2% on $405 Million Laser Order](https://www.google.com/goto?url=CAES0QEBxCJF150BVEeUIhYTfQTG1stH0lT1Ng4-_26IZ6uvgiCpMuHE9IA-Tia4yyysAs-f7I7nQ0rmI_gFcDTGZrHTOyzmm5__vJeJUR6hsKvDb7gDTkLty9vj0ekg6NGeoHDxpUk_ywK9RTK6pZg9EoMM5JVQBbyxgY5ct9gvWs9zHgPm8FyBQbWhiPbZqDXirtIzi123LKG0aAkTQq06HeGHLlB2d0k5dBbVSWpdQyBugV9WXraDvAXqKRuSQ4yxmWLutw6_Z10cC3BUw1swiB_b9A&gsessionid=GxP4UoDrw6aE_-Bi8G55W6p7jP76LdZtH-3-M4F-Ggjjw-xueJgHsw)  
  <sub>24/7 Wall St., 21 hours ago</sub>  
  Red Cat and Ondas are bouncing back from Monday's rate-fear sell-off, rising 5% and 4% as buyers return to high-beta drone stocks.
- [LTH,LKQ,CAT,CVNA,GKOS,DOV,AER,BA | Stock Prices | Quote Comparison - Yahoo Finance](https://www.google.com/goto?url=CAESggEBxCJF16zzi49w96rWbNw0ndxImreTV-f1yGMKZqWahtbPioI93lTFiwT6fhTBqi_9OLRmS1QZjXu6AoIyLalCT_0a2yR4dONIM6JArnQjJxCUacovGes9renV_6ho_PRjGQfAo3dULtTsOiqz38Oo-SWD8qbJNzden9VdPhtCy-Ly&gsessionid=GxP4UoDrw6aE_-Bi8G55W6p7jP76LdZtH-3-M4F-Ggjjw-xueJgHsw)  
  <sub>Yahoo! Finance Canada, 10 hours ago</sub>  
  View and compare LTH,LKQ,CAT,CVNA,GKOS,DOV,AER,BA on Yahoo Finance.
- [Caterpillar Inc Stock (CAT) Moved Up by 3.21% on Nov 11: What Investors Need To Know](https://www.google.com/goto?url=CAESjwEBxCJF12BFwAaVQI0CciNNx6DdQYygKJOtQH6dN9gGNabJEiTyHYCtnL4m995kN-ENzNhwPOaZ5FHJK43PO0ZAp7lV-Df6qmDFMzV4zSM2rzQHsK-6iDyG4EXmX6i4eN4T7Rwo-a00GjWm1nN4y8fmRf1uG_6TmSVfGnHikjvkwsXMB0rXZuop8BFRIZNVzA&gsessionid=GxP4UoDrw6aE_-Bi8G55W6p7jP76LdZtH-3-M4F-Ggjjw-xueJgHsw)  
  <sub>TradingKey, 21 hours ago</sub>  
  Caterpillar generated $67.59 billion in annual revenue with $8.88 billion net profit.The Energy and Transportation segment acts as a powerful multi-year...
- [Caterpillar stock rallies as Anthropic generator order and record results boost sentiment](https://www.google.com/goto?url=CAESnQEBxCJF12B-de4ayNDZrD71Ek6rZbT5-TAZCZj48lO0owzDElw2v0T9ikdNPNtCCUG9P0gTiJ62rYd53xB1oaLR4ouCmH3lkpF970dQ_r0GFOAIUrEqMtHNIoPdgydNsPtCcVspVp8kJHVKCZWO6eIMGwItTuI01OJQ6iLAYnGAVaqWudBY1hJoBCPjxsfuZZQzic6AmnJkVrbyNHHe&gsessionid=GxP4UoDrw6aE_-Bi8G55W6p7jP76LdZtH-3-M4F-Ggjjw-xueJgHsw)  
  <sub>Traders Union, 22 hours ago</sub>  
  Caterpillar trades at $603.6 today, gaining 3.26% as Anthropic's $3.4B order boosts momentum amid strong Q3 results.
- [Caterpillar (CAT) Looks Cheap Following Anthropic’s $3.4b AI Power Deal](https://www.google.com/goto?url=CAESwgEBxCJF16UUDPTHlo-hgbLQq0fQynowcNOMUiaiRQi6uLEYVuQomt2ZXBlocczxoKp0z0J3f_yNG7IwcL8wyswMZOSmeGbsaOCnQGZOtaWEko2lyyQQu7veDYNdAHEYiM2F2PoC4MAEkjHtCEjp-P6driWR5xlMkAlITCUrOi_MCeTwP-CkUw3BclAflvAYRnazoZd7mITNrqGtn6CcPu9cyY6XqGjnZ_wfChfDkcFkyAsc63pdj7JQ8ouI1bSuBUMGGg&gsessionid=GxP4UoDrw6aE_-Bi8G55W6p7jP76LdZtH-3-M4F-Ggjjw-xueJgHsw)  
  <sub>Simply Wall St, 19 hours ago</sub>  
  Caterpillar (CAT) just landed a headline contract, with Anthropic agreeing to buy about US$3.4b of gas generators for AI data centers, taking over 1.7...
- [How Does Owning Fabick Cat Reshape Caterpillar's (NYSE:CAT) Model?](https://www.google.com/goto?url=CAESqAEBxCJF109e1-d7TFNBzmxcirZF6hLepFLel9Og3v88UDZOhNHUSxRo3YVk0ARxtVfzvux9GVDEeQ8Y7-EnyeAFUsh9P448lmi2fb-XIrkhjSGvxHw-B0PneqSjSKYnsIJAgSOFaJVppeklLZgW25fJYeWLUpmGQstY17K4koz1PB8NwaQmzcWJItdWGEWIcCw489dWwRdr1JzJc0dhgX-2dSQQigrKu9o&gsessionid=GxP4UoDrw6aE_-Bi8G55W6p7jP76LdZtH-3-M4F-Ggjjw-xueJgHsw)  
  <sub>Kalkine Media, 4 hours ago</sub>  
  Caterpillar has completed its acquisition of the Fabick Cat dealership, an unusual step for a company that relies on an independent dealer network.
- [Is Caterpillar (NYSE:CAT) Taking Control of Its Dealers?](https://www.google.com/goto?url=CAESnwEBxCJF18eZCoG_cuqugbPcTFE7Dm0MN7hRQNnI4H1NwmxSD6FdQuX_9V3yDiT3hTCjfWS0eeaVabwCYUv-bzJvzvLdRPHWEqZFTZAfDsXOtTJYqGFC3lYdOa-84zlZiK4J9zj7LtuZlMpUmR82-g_yY1oT9P163B_f1JIkzbecgnDXMwIFZD4xggbJWW-Z_5jWbiTmi-fQdJiNRtTvRmw&gsessionid=GxP4UoDrw6aE_-Bi8G55W6p7jP76LdZtH-3-M4F-Ggjjw-xueJgHsw)  
  <sub>Kalkine Media, 9 hours ago</sub>  
  Caterpillar has completed its acquisition of the Fabick Cat dealership, an unusual step for a company that relies on an independent dealer network.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.80</summary>

_Not available today._

</details>

<details><summary><b>Price and chart</b> — score -0.60</summary>

```text
Last close 596.09 (bar of 2026-11-12), from 502 daily bars
Trend: vs 20d SMA 651.21 (-8.5%), 50d 744.58 (-19.9%), 200d 807.71 (-26.2%); 50d below 200d
Momentum: RSI(14) 34.6 | MACD -50.537 vs signal -49.320 (histogram -1.216)
Returns: 1d -0.9% | 5d +7.7% | 1m -20.4% | 3m -30.4%
52-week range: 546.13 - 1,064.90 (now 9.6% of the way up)
Volatility: ATR(14) 28.82 (4.8% of price) | annualised 20d 59.4%
Volume: 0.06x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.40</summary>

```text
Sector: Industrials / Farm & Heavy Construction Machinery | market cap 272.77B
Valuation: trailing P/E 23.39 | forward P/E 18.49 | P/B 12.70 | PEG 1.02
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

<details><summary><b>What analysts and big funds say</b> — score +0.30</summary>

```text
Consensus: buy (mean 1.97 on a 1=strong buy to 5=strong sell scale, 26 analysts)
Ratings: 2 strong buy, 15 buy, 11 hold, 1 sell, 0 strong sell
Price target: mean 823.41 (+38.1% vs last close), range 575.00 - 1,044.68
Recent rating changes:
  - 2026-11-10 Evercore ISI Group: main, Outperform -> Outperform
  - 2026-11-02 Freedom Broker: main, Buy -> Buy
  - 2026-11-02 DA Davidson: main, Neutral -> Neutral
  - 2026-10-30 JP Morgan: main, Overweight -> Overweight
  - 2026-10-30 Citigroup: main, Buy -> Buy
  - 2026-10-30 Wells Fargo: main, Overweight -> Overweight
Institutional ownership: 74.2%
Largest holders: Blackrock Inc. (8.3%), State Street Corporation (7.5%), Vanguard Capital Management LLC (6.6%), State Farm Mutual Automobile Insurance Co (3.2%), Vanguard Portfolio Management LLC (2.6%)
```

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score +0.30</summary>

_Not available today._

</details>

<details><summary><b>Buying and selling by company insiders</b> — score -0.10</summary>

```text
Last 180 days: bought 71,584 shares in 13 transaction(s) | sold 51,562 shares in 4
Net: +20,022 shares (+2.0% of insider holdings) | insiders hold 1,029,586 shares
Distinct insiders: 1 buying, 1 selling
Open-market purchases — insiders spending their own money:
  - 2026-11-02 FISH JAMES C JR (Director): 1,000 shares, 620.39K
Sales — weak evidence on their own; often scheduled 10b5-1 plans, tax on vesting, or diversification:
  - 2026-08-28 CREED JOSEPH E (Chief Executive Officer): 32,401 shares, 26.21M
(9 grant/option/gift transaction(s) excluded — compensation, not a view on the price)
```

</details>

<details><summary><b>Who is positioned how</b> — score -0.10</summary>

_Not available today._

</details>

<details><summary><b>Money going into and out of this fund</b> — score -0.10</summary>

_Not available today._

</details>

### Royal Bank of Canada (RY) · Company — BULLISH, confidence 0.58

**Result:** REJECTED · no room under the sleeve budget limit

**In the model's own words:** no explanation. It wrote only “BUY”, so the main reasons below are all it gave.

**Main reasons it gave:**
- Trailing P/E 17.75, forward P/E 15.94, ROE 16.2%, revenue +8.9% YoY
- Analyst consensus buy; mean target 209.15 (+3% vs 203.05)
- Insiders bought 745 shares (~$152k) on 2026-10-30
- Technical weakness: low volume (0.01x 20‑day avg) and MACD slightly negative

<details><summary><b>News</b> — score +0.00</summary>

- [Royal Bank of Canada stock gets broader cash-back rewards](http://www.bing.com/news/apiclick.aspx?ref=FexRss&aid=&tid=6af5d02b554f4569b3a5949fff6b9365&url=https%3a%2f%2fwww.ad-hoc-news.de%2fboerse%2fnews%2fcorporate-news%2froyal-bank-of-canada-stock-gets-broader-cash-back-rewards%2f70498197&c=9246113712062136370&mkt=en-us)  
  <sub>Ad Hoc News, 9h ago</sub>  
  Royal Bank of Canada stock is set for more flexible cash-back redemptions from December. New earning rates have applied to existing and new cardholders since October 1. Royal Bank of Canada raised ...
- [RBC appoints Chana Martineau to lead the bank's Indigenous banking and economic reconciliation strategy](http://www.bing.com/news/apiclick.aspx?ref=FexRss&aid=&tid=6af5d02b554f4569b3a5949fff6b9365&url=https%3a%2f%2ffinance.yahoo.com%2feconomy%2fpolicy%2farticles%2frbc-appoints-chana-martineau-lead-140100583.html&c=7671676278947406819&mkt=en-us)  
  <sub>Yahoo Finance, 9h ago</sub>  
  Royal Bank of Canada (RBC), today announced the appointment of Chana Martineau as National Head, Indigenous Banking and RBC Origins, which combines the bank's Indigenous Banking strategy team and ...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

_Not available today._

</details>

<details><summary><b>Price and chart</b> — score -0.20</summary>

```text
Last close 203.05 (bar of 2026-11-12), from 502 daily bars
Trend: vs 20d SMA 202.69 (+0.2%), 50d 201.29 (+0.9%), 200d 190.82 (+6.4%); 50d above 200d
Momentum: RSI(14) 51.7 | MACD 1.032 vs signal 1.074 (histogram -0.042)
Returns: 1d -0.2% | 5d -0.3% | 1m +4.8% | 3m -6.2%
52-week range: 146.56 - 217.87 (now 79.2% of the way up)
Volatility: ATR(14) 3.25 (1.6% of price) | annualised 20d 20.5%
Volume: 0.01x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.30</summary>

```text
Sector: Financial Services / Banks - Diversified | market cap 281.11B
Valuation: trailing P/E 17.75 | forward P/E 15.94 | P/B 2.95 | PEG 1.91
Profitability: profit margin 33.9% | operating margin 45.7% | ROE 16.2%
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

```text
Earnings record, last 4 quarters: 2 beats, 2 in line
  2026-09-30 in line | 2026-06-30 in line | 2026-03-31 beat by 3% | 2026-03-31 beat by 3%
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
Consensus: buy (mean 2.21 on a 1=strong buy to 5=strong sell scale, 3 analysts)
Ratings: 4 strong buy, 4 buy, 5 hold, 0 sell, 1 strong sell
Price target: mean 209.15 (+3.0% vs last close), range 182.54 - 230.03
Recent rating changes:
  - 2025-08-29 Argus Research: main, Buy -> Buy
  - 2024-12-05 BMO Capital: main, Outperform -> Outperform
  - 2024-08-29 BMO Capital: main, Outperform -> Outperform
  - 2024-06-06 Argus Research: main, Buy -> Buy
  - 2024-04-05 BMO Capital: up, Market Perform -> Outperform
  - 2023-12-18 B of A Securities: up, Neutral -> Buy
Institutional ownership: 50.7%
Largest holders: Royal Bank of Canada (5.1%), Bank of Montreal /CAN/ (4.2%), Vanguard Capital Management LLC (3.1%), TD Asset Management, Inc (1.7%), NORGES BANK (1.4%)
```

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score +0.30</summary>

_Not available today._

</details>

<details><summary><b>Buying and selling by company insiders</b> — score +0.20</summary>

```text
Last 180 days: bought 0 shares in 0 transaction(s) | sold n/a shares in 0
Net: +0 shares | insiders hold 373,796 shares
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

### Exxon Mobil (XOM) · Company — BULLISH, confidence 0.58

**Result:** REJECTED · no room under the sleeve budget limit

**In the model's own words:**

> Fundamentals are strong, insiders are net buying heavily, analysts are bullish with ~10% upside target, while technicals show short‑term weakness. Overall view is moderately bullish over the next few days.

**Main reasons it gave:**
- Insider net purchase of +6.9M shares (188% of holdings) in last 180 days
- Strong fundamentals: low debt/equity 12.6%, free cash flow $28.3B, revenue +32.6% YoY, earnings +111.4% YoY
- Analyst consensus buy with mean target $184.32 (+9.9% upside)
- Technical weakness: price below 20‑day SMA, RSI 43.7, low volume (0.05× 20‑day avg)
- Valuation: trailing P/E 17.26, forward P/E 13.47, PEG 1.30 suggests undervaluation

<details><summary><b>News</b> — score +0.00</summary>

- [ExxonMobil (XOM) Stock May Be 24% Undervalued Despite Venezuela Oil Deal](http://www.bing.com/news/apiclick.aspx?ref=FexRss&aid=&tid=6af5d09cf51744188febd3c591201585&url=https%3a%2f%2ffinance.yahoo.com%2fmarkets%2fstocks%2farticles%2fexxonmobil-xom-stock-may-24-181015023.html&c=16454503939405675286&mkt=en-us)  
  <sub>Yahoo Finance, 29h ago</sub>  
  ExxonMobil Holdings has delivered a powerful share price run over the past few years, yet the recent pullback and busy deal slate raise a sharper question about whether the current market value lines ...
- [Chevron Vs. ExxonMobil: Buy The Peace, Not The War Premium](http://www.bing.com/news/apiclick.aspx?ref=FexRss&aid=&tid=6af5d09cf51744188febd3c591201585&url=https%3a%2f%2fseekingalpha.com%2farticle%2f4966854-chevron-vs-exxonmobil-buy-the-peace-not-the-war-premium&c=3491531569525282847&mkt=en-us)  
  <sub>Seeking Alpha, 13h ago</sub>  
  Chevron and ExxonMobil both banked a war windfall and have already started giving it back to the shareholders. See why CVX stock is a Buy and XOM stock a Hold.
- [Your $300,000 in XLE holds $116,286 in just two oil companies](http://www.bing.com/news/apiclick.aspx?ref=FexRss&aid=&tid=6af5d09cf51744188febd3c591201585&url=https%3a%2f%2fwww.msn.com%2fen-us%2fmoney%2feconomy%2fyour-300-000-in-xle-holds-116-286-in-just-two-oil-companies%2far-AA2hii5M&c=4089088233187273972&mkt=en-us)  
  <sub>24/7 Wall St. on MSN, 11h ago</sub>  
  Quick ReadXLE puts 39% of its assets into Exxon and Chevron, so a $300,000 stake carries about $116,000 in just two oil companies.Exxon's 23% weight and Chevron's 16% stem from market-cap weighting, ...
- [Exxon, Chevron, and Shell Just Reported. Here's What Each One Said About Where Oil Goes Next.](http://www.bing.com/news/apiclick.aspx?ref=FexRss&aid=&tid=6af5d09cf51744188febd3c591201585&url=https%3a%2f%2fwww.aol.com%2farticles%2fexxon-chevron-shell-just-reported-033500000.html&c=14952748611870131740&mkt=en-us)  
  <sub>AOL, 23h ago</sub>  
  Uncertainty is the main issue in the oil market, but that doesn't mean that these integrated energy giants aren't making plans.
- [Exxon files legal challenge to EU carbon capture law, FT reports](http://www.bing.com/news/apiclick.aspx?ref=FexRss&aid=&tid=6af5d09cf51744188febd3c591201585&url=https%3a%2f%2fclubofmozambique.com%2fnews%2fexxon-files-legal-challenge-to-eu-carbon-capture-law-ft-reports%2f&c=2728968175990733314&mkt=en-us)  
  <sub>Club of Mozambique, 23h ago</sub>  
  ExxonMobil has filed a confidential legal challenge to the European Union's carbon capture rules, the Financial Times ​reported on Wednesday, citing a memo from ...
- [Exxon vs. Chevron: 45 and 39 Straight Years of Raises. Which Oil Dividend Wins the Next Decade?](http://www.bing.com/news/apiclick.aspx?ref=FexRss&aid=&tid=6af5d09cf51744188febd3c591201585&url=https%3a%2f%2ffinance.yahoo.com%2fenergy%2farticles%2fexxon-vs-chevron-45-39-195052283.html&c=11502637208400498614&mkt=en-us)  
  <sub>Yahoo Finance, 27h ago</sub>  
  Chevron (CVX:NYSE) reported the same day, and told investors on its call that it has raised its dividend for 39 consecutive years. Its streak is shorter, but it pays the bigger check: a 3.5% yield to ...
- [Exxon Mobil (XOM) share price](http://www.bing.com/news/apiclick.aspx?ref=FexRss&aid=&tid=6af5d09cf51744188febd3c591201585&url=https%3a%2f%2feconomictimes.indiatimes.com%2fmarkets%2fus-stocks%2fexxonmobil-holdings-corporation%2fxom&c=7725295780730614059&mkt=en-us)  
  <sub>The Economic Times, 9h ago</sub>  
  Get the live share price of ExxonMobil Holdings Corporation (XOM), including intraday charts, historical performance, key financials, and market updates. Track the latest US stock market activity.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

_Not available today._

</details>

<details><summary><b>Price and chart</b> — score -0.50</summary>

```text
Last close 167.73 (bar of 2026-11-12), from 502 daily bars
Trend: vs 20d SMA 175.64 (-4.5%), 50d 169.17 (-0.9%), 200d 156.20 (+7.4%); 50d above 200d
Momentum: RSI(14) 43.7 | MACD -1.204 vs signal 0.830 (histogram -2.034)
Returns: 1d +0.6% | 5d +1.5% | 1m -5.2% | 3m +4.8%
52-week range: 114.51 - 187.25 (now 73.2% of the way up)
Volatility: ATR(14) 4.27 (2.5% of price) | annualised 20d 31.4%
Volume: 0.05x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.70</summary>

```text
Sector: Energy / Oil & Gas Integrated | market cap 684.21B
Valuation: trailing P/E 17.26 | forward P/E 13.47 | P/B 2.57 | PEG 1.30
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
Price target: mean 184.32 (+9.9% vs last close), range 160.00 - 213.00
Recent rating changes:
  - 2026-11-12 Bernstein: main, Outperform -> Outperform
  - 2026-11-07 Freedom Broker: main, Hold -> Hold
  - 2026-11-04 Citigroup: main, Neutral -> Neutral
  - 2026-11-04 TD Cowen: main, Buy -> Buy
  - 2026-11-02 UBS: main, Buy -> Buy
  - 2026-11-02 Morgan Stanley: main, Overweight -> Overweight
Institutional ownership: 69.3%
Largest holders: Blackrock Inc. (8.2%), Vanguard Capital Management LLC (6.6%), State Street Corporation (5.1%), FMR, LLC (3.6%), Vanguard Portfolio Management LLC (2.9%)
```

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score +0.30</summary>

_Not available today._

</details>

<details><summary><b>Buying and selling by company insiders</b> — score +0.90</summary>

```text
Last 180 days: bought 10,818,651 shares in 251 transaction(s) | sold 3,904,152 shares in 49
Net: +6,914,499 shares (-188.2% of insider holdings) | insiders hold 3,222,586 shares
Distinct insiders: 0 buying, 0 selling
```

</details>

<details><summary><b>Who is positioned how</b> — score +0.90</summary>

_Not available today._

</details>

<details><summary><b>Money going into and out of this fund</b> — score +0.90</summary>

_Not available today._

</details>

### JPMorgan Chase (JPM) · Company — BULLISH, confidence 0.55

**Result:** REJECTED · no room under the sleeve budget limit

**In the model's own words:**

> The stock trades above key moving averages with modest positive momentum, fundamentals show reasonable valuation and strong profitability, analysts maintain a buy consensus with an 8.6% price‑target upside, and earnings have historically beat expectations (3 of 4 quarters). No material news catalyst is present and insider activity is neutral, so the view is moderately bullish.

**Main reasons it gave:**
- Price above 20‑day, 50‑day, and 200‑day SMAs (+1.5% to +5.9%)
- Trailing P/E 14.43 and forward P/E 13.45 indicate reasonable valuation
- Analyst consensus buy with mean price target +8.6% vs last close
- 3 out of 4 earnings beats in the past year

<details><summary><b>News</b> — score +0.00</summary>

- [JPMorgan predicted strong Wegovy pill sales (and was right). Is Novo Nordisk stock a buy now?](http://www.bing.com/news/apiclick.aspx?ref=FexRss&aid=&tid=6af5d027fb154edfae6d47d1490fb8c6&url=https%3a%2f%2fwww.msn.com%2fen-us%2fmoney%2ftop-stocks%2fjpmorgan-predicted-strong-wegovy-pill-sales-and-was-right-is-novo-nordisk-stock-a-buy-now%2far-AA2hgeMa&c=10489054287266506430&mkt=en-us)  
  <sub>The Motley Fool on MSN, 19h ago</sub>  
  Novo Nordisk lived up to expectations for its Wegovy pill in the third quarter, but it still has more work ahead.
- [J.P. Morgan launches global value active equity UCITS ETF](http://www.bing.com/news/apiclick.aspx?ref=FexRss&aid=&tid=6af5d027fb154edfae6d47d1490fb8c6&url=https%3a%2f%2fportfolio-adviser.com%2fj-p-morgan-launches-global-value-active-equity-ucits-etf%2f&c=11170408049982673227&mkt=en-us)  
  <sub>Portfolio Adviser, 12h ago</sub>  
  J.P. Morgan Asset Management has launched the JPM Global Value Equity Active UCITS ETF, targetting undervalued global equities.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

_Not available today._

</details>

<details><summary><b>Price and chart</b> — score +0.10</summary>

```text
Last close 343.93 (bar of 2026-11-12), from 502 daily bars
Trend: vs 20d SMA 338.78 (+1.5%), 50d 340.76 (+0.9%), 200d 324.67 (+5.9%); 50d above 200d
Momentum: RSI(14) 54.2 | MACD 1.085 vs signal 0.239 (histogram 0.846)
Returns: 1d +0.2% | 5d +2.0% | 1m +2.6% | 3m -5.2%
52-week range: 282.84 - 365.18 (now 74.2% of the way up)
Volatility: ATR(14) 7.27 (2.1% of price) | annualised 20d 27.5%
Volume: 0.04x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.50</summary>

```text
Sector: Financial Services / Banks - Diversified | market cap 913.34B
Valuation: trailing P/E 14.43 | forward P/E 13.45 | P/B 2.60 | PEG 1.45
Profitability: profit margin 34.6% | operating margin 44.8% | ROE 18.0%
Growth (YoY): revenue +10.2% | earnings +9.9%
Balance sheet: debt/equity n/a | free cash flow n/a
Risk: beta 1.02 | short interest 0.9% of float
Next earnings: 2027-01-14
```

</details>

<details><summary><b>What this fund holds</b> — score +0.50</summary>

_Not available today._

</details>

<details><summary><b>Does this company beat its own forecasts</b> — score +0.50</summary>

```text
Earnings record, last 4 quarters: 3 beats, 1 missed
  2026-09-30 missed by 7% | 2026-06-30 beat by 4% | 2026-03-31 beat by 8% | 2025-12-31 beat by 3%
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
Consensus: buy (mean 2.04 on a 1=strong buy to 5=strong sell scale, 23 analysts)
Ratings: 5 strong buy, 10 buy, 11 hold, 0 sell, 0 strong sell
Price target: mean 373.48 (+8.6% vs last close), range 312.00 - 425.00
Recent rating changes:
  - 2026-11-02 UBS: main, Buy -> Buy
  - 2026-10-15 Citigroup: main, Neutral -> Neutral
  - 2026-10-14 Truist Securities: main, Hold -> Hold
  - 2026-10-14 Barclays: main, Overweight -> Overweight
  - 2026-10-14 RBC Capital: reit, Outperform -> Outperform
  - 2026-10-14 Morgan Stanley: main, Equal-Weight -> Equal-Weight
Institutional ownership: 75.7%
Largest holders: Blackrock Inc. (7.8%), Vanguard Capital Management LLC (6.1%), State Street Corporation (4.7%), Bank of America Corporation (2.6%), Morgan Stanley (2.5%)
```

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score +0.60</summary>

_Not available today._

</details>

<details><summary><b>Buying and selling by company insiders</b> — score +0.00</summary>

```text
Last 180 days: bought 136,610 shares in 7 transaction(s) | sold 37,834 shares in 8
Net: +98,776 shares (+1.0% of insider holdings) | insiders hold 10,489,659 shares
Distinct insiders: 0 buying, 2 selling
Sales — weak evidence on their own; often scheduled 10b5-1 plans, tax on vesting, or diversification:
  - 2026-09-10 LEOPOLD ROBIN (Officer): 2,500 shares, 882.03K
  - 2026-08-11 LEOPOLD ROBIN (Officer): 2,500 shares, 903.52K
  - 2026-06-22 FRIEDMAN STACEY R. (General Counsel): 5,467 shares, 1.81M
  - 2026-05-20 FRIEDMAN STACEY R. (General Counsel): 5,468 shares, 1.64M
(6 grant/option/gift transaction(s) excluded — compensation, not a view on the price)
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

- [Elbit Systems Ltd. (ESLT) stock price, news, quote and history](https://au.finance.yahoo.com/quote/ESLT/)  
  <sub>Yahoo Finance Australia, 12 hours ago</sub>  
  Elbit Systems Ltd. (ESLT) · 3.12% · 10.63% · -7.26% · 25.29% · 49.19% · 376.86% · 18,036.00%. Key events. Baseline. Advanced chart. Loading chart for...
- [Elbit Systems Lands $260 Million NATO Deal](https://www.benzinga.com/news/contracts/26/11/63175478/elbit-systems-lands-260-million-nato-deal)  
  <sub>Benzinga, 4 hours ago</sub>  
  Elbit Systems (ESLT) stock rises over 2% after landing a $260 million contract to supply PULS rocket artillery to a European NATO member.
- [Ahead of Elbit (ESLT) Q3 Earnings: Get Ready With Wall Street Estimates for Key Metrics](https://www.google.com/goto?url=CAESmgEBxCJF15c1D6rGJIf82maWgd_tMDRNoFGdb4U_ffncGCgy-nsUHC9Tkian0iPXpfvNAwL2mxcLaEebp9BuCapBIymgLumkeRZFa6-RGWSC5qVUBgLjV51-1LOkFmZvGz_N5Q-GmGkAiUHDHoQC2oq7CiPeTK8L7o3BkflfnriC1w7QgASivPt88KBRmWwpxhZbgBWFU6SsHWkr&gsessionid=hqXQwN5OGE1p07ah7r2MqhqVPMetpzTipOMMTa6PVRMVvVM-wm1ApQ)  
  <sub>Yahoo Finance, 1 hour ago</sub>  
  Looking beyond Wall Street's top-and-bottom-line estimate forecasts for Elbit (ESLT), delve into some of its key metrics to gain a deeper insight into the...
- [Elbit Systems Awarded $260 Million Contract to Supply PULS Rocket Artillery Systems to a European NATO Country](https://www.google.com/goto?url=CAESpAEBxCJF16LXvhy8cPv3WhiViJDEMNsNK11zNS09e_7bJ5wrvhW4YDZOjWBEIJ020Xd3Hf0bMNu1j6cT8MEa1AjsB9GCXzQWh6iAIBCHIeITwXe3PVmH1iTHN7W9KxA16MiRI2Ct7ZvfHx_q9UTxLpPBbj3lurzJYgoNjG-eGwNl1smd8oROLCN3eeGWoXSYup576ATUDqqq7LlwHwZyMSn8yn5WCg&gsessionid=hqXQwN5OGE1p07ah7r2MqhqVPMetpzTipOMMTa6PVRMVvVM-wm1ApQ)  
  <sub>Quantisnow, 7 hours ago</sub>  
  HAIFA, Israel, Nov. 12, 2026 /PRNewswire/ -- Elbit Systems Ltd. (NASDAQ:ESLT) (TASE: ESLT) ("Elbit Systems" or the "Company") announced today that it was...
- [$100 Invested In Elbit Systems 10 Years Ago Would Be Worth This Much Today](https://www.google.com/goto?url=CAESqwEBxCJF1xiZNIDhgloTkZwFJ1SggBYFNv6Lrre_5MeaMCwGN3rWMrjgR_v1l8oOBVEc5HDe4jXTOFl2ie7EZ7YyJUvm8xZSzTg_KiXw6IPCNWvS0aq_CH70dmuv080K8gGWg9W7s5smLvt0wsRVvRfKHaO0mRkDsMz3QEmYhj6wXaRWI-gC9YW649MdkfpySb1VKwpVfrB9DPBfGzMihsFb1p1HVSQwP5w9a94&gsessionid=hqXQwN5OGE1p07ah7r2MqhqVPMetpzTipOMMTa6PVRMVvVM-wm1ApQ)  
  <sub>Benzinga, 17 hours ago</sub>  
  Elbit Systems (NASDAQ:ESLT) has outperformed the market over the past 10 years by 8.13% on an annualized basis producing an average annual return of 21.41%.
- [Elbit Systems Wins $260 Million NATO Rocket Artillery Order, Shares Climb](https://www.google.com/goto?url=CAESgAEBxCJF18h8RHz2_ksQUygjWp7vaRypytOLeJM_C2nWx-92X5pzAmZ0X8lElxStJMCdHpFH8g7AJ_jX81-wrWIF049dpRAqH4Qf7xXY58Wt_taN_-SllQqtUld5bpxN8Io50590yoTDIwd2iUXukDcp34R34vPROcXFJrFbh_qvGA&gsessionid=hqXQwN5OGE1p07ah7r2MqhqVPMetpzTipOMMTa6PVRMVvVM-wm1ApQ)  
  <sub>BigGo Finance, 3 hours ago</sub>  
  Elbit Systems has won a contract worth about $260 million to supply PULS rocket artillery systems and munitions to an unnamed European NATO member,…
- [How Does a $260 Million PULS Contract Change Elbit Systems’ (NASDAQ:ESLT) European Outlook?](https://www.google.com/goto?url=CAESugEBxCJF11KXqrUr9BNJ6UOs9-Q7QhAnjLg1_MEUTV8YNyx34yiDpAVpK3S3GD5FSdXdBIs-r1hYrXyhY9flH4ThB7Ohlu5v2BuQRkugqb918jbpLOrjQfGj_5cOn7C1W2i7CujJYOAo-tdaeYVNNcP_bcQHeuFOhlPq5HF0DftOLA-2Gt6cDgEusGjcOLRfVBCuUv91RO2h_b4yWEBRm6ROhkuzSx53WDwIuZoIbdG8GCw0n0TKc8iZ_qI&gsessionid=hqXQwN5OGE1p07ah7r2MqhqVPMetpzTipOMMTa6PVRMVvVM-wm1ApQ)  
  <sub>Kalkine, 2 hours ago</sub>  
  How Does a $260 Million PULS Contract Change Elbit Systems' (NASDAQ:ESLT) European Outlook?
- [Elbit : Other Report or Announcement](https://www.google.com/goto?url=CAESlAEBxCJF19nZstV25EOZGkbbY0rs6DQUm3BX4ZUKuYoQAsVljxgsS-MG370axzlct-9FfVGt3zZvuE5NWNRYC_brsK9KWnfUx2z5y063mK4z1Thqm7Q5EYRJYVuWyzfkvt4I1xpNO6ryocz8AKMVpFrHJwz-AlkIKpxz8H3gVjHKdC-KysNtn_GcBLlloMBQQ3Dp4d54&gsessionid=hqXQwN5OGE1p07ah7r2MqhqVPMetpzTipOMMTa6PVRMVvVM-wm1ApQ)  
  <sub>www.marketscreener.com, 8 hours ago</sub>  
  אלביט מערכות בעמ ELBIT SYSTEMS LTD Corporation no: 520043027 -November 12, 2026 at 01:53 am EST - MarketScreener.
- [Coherent CEO Jim Anderson buys about $1 million of stock](https://www.google.com/goto?url=CAESiQEBxCJF182TvEzMP5m629i8LyA0u7qeaiV7hlo8YRT0l1RFmR_6GWbGbK1c7j03J94f_gXKdTe0cs5OEuReTDO4WfBnYxaNXz5ObEVIYwNDYLNuCk2P4bKdbW9DBXq1eSIgbH3IWHUqmhu7Hth2O1gySAX4yNH_al0ymnNk_v1ihNncM256JLiJMA&gsessionid=hqXQwN5OGE1p07ah7r2MqhqVPMetpzTipOMMTa6PVRMVvVM-wm1ApQ)  
  <sub>MLQ.ai, 2 hours ago</sub>  
  Coherent chief executive Jim Anderson bought 5000 shares of the optical components maker on the open market on Nov. 9 at $199.48, about $997000,...
- [Wed: Bezeq bucks market](https://www.google.com/goto?url=CAESgQEBxCJF18jlJiFYt0_vjbEAkbu5nZwKrCOmNVsFXf4ruWfTIc36K6KBX0OyfIfiDW4bga2dFQKJVuIBCopqqr7xms6lPVOjxz1eol1hV0M0flijqIf3WiApCaDgNAaHlvhhGeyWBNjz-rroTZkidPS5tqtwaEyhdWyKu2VGSNL2IqE&gsessionid=hqXQwN5OGE1p07ah7r2MqhqVPMetpzTipOMMTa6PVRMVvVM-wm1ApQ)  
  <sub>Globes - Israel Business News, 10 hours ago</sub>  
  The banks, Enlight and the TASE stock itself led the market lower while Bezeq led the gains.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>Price and chart</b> — score n/a</summary>

```text
Last close 726.67 (bar of 2026-11-12), from 502 daily bars
Trend: vs 20d SMA 743.27 (-2.2%), 50d 723.61 (+0.4%), 200d 785.41 (-7.5%); 50d below 200d
Momentum: RSI(14) 49.5 | MACD -1.989 vs signal 1.463 (histogram -3.452)
Returns: 1d +0.2% | 5d +11.6% | 1m +3.6% | 3m -7.3%
52-week range: 454.95 - 1,014.33 (now 48.6% of the way up)
Volatility: ATR(14) 27.28 (3.8% of price) | annualised 20d 59.7%
Volume: 0.06x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score n/a</summary>

```text
Sector: Industrials / Aerospace & Defense | market cap 34.07B
Valuation: trailing P/E 54.68 | forward P/E 39.04 | P/B 7.71 | PEG n/a
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
Price target: mean 838.92 (+15.4% vs last close), range 738.50 - 960.00
Recent rating changes:
  - 2026-10-05 Jefferies: main, Hold -> Hold
  - 2026-08-19 JP Morgan: main, Neutral -> Neutral
  - 2026-06-24 Jefferies: main, Hold -> Hold
  - 2026-05-27 Jefferies: main, Hold -> Hold
  - 2026-05-27 JP Morgan: main, Neutral -> Neutral
  - 2026-04-13 JP Morgan: main, Neutral -> Neutral
Institutional ownership: 27.6%
Largest holders: Clal Insurance Enterprises Holdings Ltd (3.5%), Vanguard Capital Management LLC (1.6%), Van Eck Associates Corporation (1.2%), Y.D. More Investments Ltd (1.1%), Altshuler Shaham Ltd (1.0%)
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

- [Google’s New AI Model Can Identify Nearly Twice as Many DNA Changes Linked to Disease](http://www.bing.com/news/apiclick.aspx?ref=FexRss&aid=&tid=6af5d019973a4b2fb63fe86821f0b971&url=https%3a%2f%2fwww.tipranks.com%2fnews%2fgoogles-new-ai-model-can-identify-nearly-twice-as-many-dna-changes-linked-to-disease&c=10475111207637940250&mkt=en-us)  
  <sub>TipRanks, 25h ago</sub>  
  Tech giant Alphabet ($GOOGL) introduced AlphaGenome 2 on Wednesday, which is a new AI model that helps scientists understand how changes in DNA affect different ...
- [Google’s Gemini AI Lands on Apple CarPlay for Hands-Free Use](http://www.bing.com/news/apiclick.aspx?ref=FexRss&aid=&tid=6af5d019973a4b2fb63fe86821f0b971&url=https%3a%2f%2fwww.tipranks.com%2fnews%2fgoogles-gemini-ai-lands-on-apple-carplay-for-hands-free-use&c=16397924399279271184&mkt=en-us)  
  <sub>TipRanks, 16h ago</sub>  
  Google ($GOOGL) is bringing its Gemini AI assistant to Apple ($AAPL) CarPlay. The new feature will let drivers have hands-free conversations with Gemini through ...
- [Anthropic Says Its Revenue Run Rate Jumped to an $81 Billion Run Rate](http://www.bing.com/news/apiclick.aspx?ref=FexRss&aid=&tid=6af5d019973a4b2fb63fe86821f0b971&url=https%3a%2f%2f247wallst.com%2finvesting%2f2026%2f11%2f11%2fanthropic-says-its-revenue-run-rate-jumped-to-an-81-billion-run-rate%2f&c=14822037426485093962&mkt=en-us)  
  <sub>24/7 Wall St., 27h ago</sub>  
  Anthropic's latest filing shows a startling one-month surge, but buried in the fine print is a warning that growth may slow sharply. Amazon and Alphabet both have billions riding on it, and only one ...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>Price and chart</b> — score n/a</summary>

```text
Last close 295.26 (bar of 2026-11-12), from 502 daily bars
Trend: vs 20d SMA 305.49 (-3.3%), 50d 329.05 (-10.3%), 200d 338.68 (-12.8%); 50d below 200d
Momentum: RSI(14) 39.5 | MACD -13.541 vs signal -13.951 (histogram 0.409)
Returns: 1d +0.6% | 5d +4.5% | 1m -15.1% | 3m -14.6%
52-week range: 273.50 - 402.62 (now 16.9% of the way up)
Volatility: ATR(14) 9.79 (3.3% of price) | annualised 20d 51.3%
Volume: 0.14x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score n/a</summary>

```text
Sector: Communication Services / Internet Content & Information | market cap 3.63T
Valuation: trailing P/E 15.42 | forward P/E 19.13 | P/B 5.50 | PEG 1.02
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
Price target: mean 400.37 (+35.6% vs last close), range 300.00 - 500.00
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
Net: +0 shares | insiders hold 196,826,928 shares
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

- [HDFC Bank Limited (HDB) stock price, news, quote and history](https://uk.finance.yahoo.com/quote/HDB/)  
  <sub>Yahoo Finance UK, 5 hours ago</sub>  
  HDFC Bank Limited (HDB) · 5.34% · 16.79% · 7.52% · -28.59% · -29.10% · -27.06% · 3,488.97%. Key events. Baseline. Advanced chart. Loading chart...
- [Vingroup shares rally, adding $1.5 billion to Pham Nhat Vuong's fortune](https://vietnamnet.vn/en/vingroup-shares-rally-adding-1-5-billion-to-pham-nhat-vuong-s-fortune-2574215.html)  
  <sub>Báo VietNamNet, 7 hours ago</sub>  
  Foreign investors stepped up purchases of Vingroup shares despite selling pressure across Vietnam's stock market, lifting billionaire Pham Nhat Vuong's net...
- [Understanding the Setup: (HDB) and Scalable Risk](https://www.google.com/goto?url=CAESuwEBxCJF19RtAOZVJl6HuxT5bo2oGzMjrww40qBmSuPdg5BbQr8z-6nSCtBBCs0kAhgX19iGB3YmMXAS1hT2T3z4iiPRlWqw3FufQrPeUxc0nhFLlhQDvXvjU7kgeLqzEpKclAIGVyP4BCufz20Vaezq4h_XfMwDD2OLbo2X6fXAKjSarMsuDdTeSwhgOt6LbPAvJ2odCHSf5vN5sophcElZ5UqCSkq_iaA1tzaoHNNR5AqG9c4jLB1-aLAb&gsessionid=zimiL4BZAmoXpZFCJijgfhmZaE6F7mshZZKLyL8RZjCEcfiIJLdmwQ)  
  <sub>Stock Traders Daily, 22 hours ago</sub>  
  Key findings for Hdfc Bank Limited (NYSE: HDB). Near and Mid-Term Strong Sentiment Could Shift Weak Long-Term Outlook; No clear price positioning signal...
- [ComfortDelGro taxi catches fire along Geylang Road , Singapore News](https://www.google.com/goto?url=CAEShAEBxCJF13llAGd3cNzgCLS2RiEvVZO539EocgwwRiekYm6F2-BmQf_xfAPe9SuNZRL-zSfT4-Pfgx6yfq9nK26VXCLldfxfR_SQTXc6jI0MCs87_ZzAdZL6bFGtx_aNKUSuGZlCKRoE_Ue_dMbM_ciKtfHWqfmx1UzzNQmrGfxP1WddkWQ&gsessionid=zimiL4BZAmoXpZFCJijgfhmZaE6F7mshZZKLyL8RZjCEcfiIJLdmwQ)  
  <sub>AsiaOne.com, 4 hours ago</sub>  
  A ComfortDelGro hybrd taxi caught fire in Geylang on Wednesday (Nov 11) evening.The incident happened at about 9.05pm along Geylang Road, near Lorong 35...
- [Bharat Heavy Electricals Ltd. Share Price, Stock Price - NSE/BSE Live](https://www.google.com/goto?url=CAESdgHEIkXXCaIE3GqDDP87IDOZJzPVZNP8hNaWhaX31q2b4nVWXkNAYWxX7cRXMUpsi9SveS46Ze0mzkFw16LToTc7DULcTywExJNtZHyeL4I6IfYb7fJIpH4Rq18hFOYYryb7UGk48N-n-MOmHZP39M0vpD18mQE&gsessionid=zimiL4BZAmoXpZFCJijgfhmZaE6F7mshZZKLyL8RZjCEcfiIJLdmwQ)  
  <sub>NDTV Profit, 11 hours ago</sub>  
  Track Bharat Heavy Electricals Ltd. share price live on NSE & BSE with real-time updates, charts, historical data, market cap, news, and expert analysis on...
- [HDFC Bank stock gains 3.98% since Bagchi vote report](https://www.google.com/goto?url=CAESrgEBxCJF18ELnREazsPE54UB90yP1glpWcIBs2GzkEVUauf4PlU49hO_oGXmF6l-q_2m7Rsq-LfeeU80CpbARRUAMJinv7TNow6Ytih9EIW1vQUZcj3qCxcUkK1RrBXxyFOONCEzs-fDnixmUwdFYU5AQlObge878dpC5U6x-iWFrhnduxlxqpiWP2SG-SuxQ0hpzhPg21B4C1WKxHrgYSRcfG1FSschZmh4t7qLwMo&gsessionid=zimiL4BZAmoXpZFCJijgfhmZaE6F7mshZZKLyL8RZjCEcfiIJLdmwQ)  
  <sub>ad-hoc-news.de, 13 minutes ago</sub>  
  HDFC Bank stock gains 3.98% since the latest report. Shareholders have approved Anup Bagchi as the bank's next chief executive.
- [Bond rush continues amid milder yields, costly loans](https://www.google.com/goto?url=CAESswEBxCJF10HVSGjy0q1v65sH8EMuoupJhGoz8gxIXxtC_pJ-M1pSi_yYAGck7HKCm384YR-Lp_gUnMlX4N2Opz_hmDW_lrD3ft7nI7T4swl2t75Qe99eCg9JciH3NB_fRDmy9tc2lM_IDbv3fNbb4FRh_sHLysRx1FrhcXSIpfVNh3c04mcK26g_wGKv3hHgUJwzIQtf9SK5yGmxjltioCe6cB9L7Tx6nZxOnf1i_3leOOZAfQ&gsessionid=zimiL4BZAmoXpZFCJijgfhmZaE6F7mshZZKLyL8RZjCEcfiIJLdmwQ)  
  <sub>The Economic Times, 13 hours ago</sub>  
  Indian companies are raising funds through bond issuances as government bond yields improve and borrowing conditions become favorable.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>Price and chart</b> — score n/a</summary>

```text
Last close 25.90 (bar of 2026-11-12), from 502 daily bars
Trend: vs 20d SMA 23.47 (+10.4%), 50d 23.00 (+12.6%), 200d 25.47 (+1.7%); 50d below 200d
Momentum: RSI(14) 72.8 | MACD 0.847 vs signal 0.446 (histogram 0.401)
Returns: 1d -0.5% | 5d +4.9% | 1m +14.4% | 3m +10.8%
52-week range: 21.36 - 37.13 (now 28.8% of the way up)
Volatility: ATR(14) 0.60 (2.3% of price) | annualised 20d 31.7%
Volume: 0.06x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score n/a</summary>

```text
Sector: Financial Services / Banks - Regional | market cap 133.23B
Valuation: trailing P/E 16.71 | forward P/E 18.75 | P/B 10.31 | PEG n/a
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
Price target: mean 30.30 (+17.0% vs last close), range 26.20 - 33.00
Recent rating changes:
  - 2024-07-22 JP Morgan: down, Overweight -> Neutral
  - 2019-09-09 Bernstein: down, Outperform -> Market Perform
  - 2019-06-11 Nomura: down, Buy -> Neutral
  - 2017-03-21 Morgan Stanley: down, Overweight -> Equal-Weight
  - 2016-09-14 Goldman Sachs: main, ? -> Buy
  - 2015-03-11 Societe Generale: init, ? -> Buy
Institutional ownership: 13.7%
Largest holders: Morgan Stanley (1.0%), Royal Bank of Canada (0.8%), Schroder Investment Management Group (0.4%), Temasek Holdings (Private) Ltd (0.4%), JPMORGAN CHASE & CO (0.4%)
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

### MercadoLibre (MELI) · Company — no answer, no confidence given

<details><summary><b>News</b> — score n/a</summary>

- [MercadoLibre (MELI) Stock Could Be Fairly Valued As Margin Pressure Builds](http://www.bing.com/news/apiclick.aspx?ref=FexRss&aid=&tid=6af5d07ce2c9467ab23562a4ecbfc3ec&url=https%3a%2f%2ffinance.yahoo.com%2fmarkets%2fstocks%2farticles%2fmercadolibre-meli-stock-could-fairly-191225782.html&c=10813871003511415448&mkt=en-us)  
  <sub>Yahoo Finance, 28h ago</sub>  
  MercadoLibre has seen its share price fall sharply over the past year, and that slide has pushed investors to focus more squarely on what the current market value implies about its earnings power.
- [MercadoLibre Keeps Sliding: Why Goldman Sachs Still Sees 41% Upside](http://www.bing.com/news/apiclick.aspx?ref=FexRss&aid=&tid=6af5d07ce2c9467ab23562a4ecbfc3ec&url=https%3a%2f%2ffinance.yahoo.com%2fmarkets%2fstocks%2farticles%2fmercadolibre-keeps-sliding-why-goldman-170848212.html&c=10124193388939815212&mkt=en-us)  
  <sub>Yahoo Finance, 30h ago</sub>  
  Key TakeawaysMercadoLibre stock has fallen 29% in a year, and Goldman Sachs cut its price target to $2,100 from $2,230 on Nov. 11 while keeping its Buy rating.
- [MercadoLibre stock balances 45% Q3 growth against margin pressure](http://www.bing.com/news/apiclick.aspx?ref=FexRss&aid=&tid=6af5d07ce2c9467ab23562a4ecbfc3ec&url=https%3a%2f%2fwww.ad-hoc-news.de%2fboerse%2fnews%2fcorporate-news%2fmercadolibre-stock-balances-45-prozent-q3-growth-against-margin-pressure%2f70497978&c=16204772370679270114&mkt=en-us)  
  <sub>Ad Hoc News, 9h ago</sub>  
  MercadoLibre stock is facing a sharper test of profitable growth after a strong third quarter. Logistics and marketing investment remain central to the outlook. Revenue and financial income rose ...
- [Michael Burry re-enters LULU on weakness, boosts positions in MercadoLibre, PayPal, JD and more](http://www.bing.com/news/apiclick.aspx?ref=FexRss&aid=&tid=6af5d07ce2c9467ab23562a4ecbfc3ec&url=https%3a%2f%2fwww.msn.com%2fen-in%2fnews%2fother%2fmichael-burry-re-enters-lulu-on-weakness-boosts-positions-in-mercadolibre-paypal-jd-and-more%2far-AA2heZWf&c=12792108800203321688&mkt=en-us)  
  <sub>Asianet Newsable on MSN, 24h ago</sub>  
  Burry cited lululemon’s new management’s failure so far to reverse a prolonged “black hole” in marketing and messaging, which has left the stock overlooked during a low-information stretch.
- [MercadoLibre收涨1.46%，成交额8.91亿美元](http://www.bing.com/news/apiclick.aspx?ref=FexRss&aid=&tid=6af5d07ce2c9467ab23562a4ecbfc3ec&url=https%3a%2f%2ffinance.sina.com.cn%2fstock%2fusstock%2fnotice%2f2026-11-12%2fdoc-iniymftt4095476.shtml&c=18346102354337902532&mkt=en-us)  
  <sub>新浪财经, 23h ago</sub>  
  11月12日，MercadoLibre（MELI）收涨1.46%，报1512.02美元，成交额8.91亿美元，市值766.55亿美元。 公司最新财报显示，季度营收107.5亿美元，同比增长45.09%；净利润4.48亿美元，同比增长6.41%。 公司简介 该公司的电子商务产品通过互联网平台实现零售和批发，旨在为用户提供一系列服务以促进商业交易。该公司的地理覆盖范围包括拉丁美洲的约18个国家。该公司 ...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>Price and chart</b> — score n/a</summary>

```text
Last close 1,481.55 (bar of 2026-11-12), from 502 daily bars
Trend: vs 20d SMA 1,674.29 (-11.5%), 50d 1,770.92 (-16.3%), 200d 1,787.33 (-17.1%); 50d below 200d
Momentum: RSI(14) 31.9 | MACD -84.136 vs signal -64.419 (histogram -19.717)
Returns: 1d -2.0% | 5d -3.2% | 1m -19.4% | 3m -19.7%
52-week range: 1,481.55 - 2,295.00 (now 0.0% of the way up)
Volatility: ATR(14) 69.14 (4.7% of price) | annualised 20d 57.8%
Volume: 0.11x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score n/a</summary>

```text
Sector: Consumer Cyclical / Internet Retail | market cap 75.11B
Valuation: trailing P/E 39.74 | forward P/E 27.64 | P/B 9.16 | PEG 0.81
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
Price target: mean 2,216.09 (+49.6% vs last close), range 1,600.00 - 2,800.00
Recent rating changes:
  - 2026-11-11 UBS: main, Neutral -> Neutral
  - 2026-11-09 JP Morgan: main, Neutral -> Neutral
  - 2026-11-05 Scotiabank: main, Sector Outperform -> Sector Outperform
  - 2026-11-05 StoneX: main, Buy -> Buy
  - 2026-11-05 Cantor Fitzgerald: main, Overweight -> Overweight
  - 2026-11-05 BTIG: main, Buy -> Buy
Institutional ownership: 80.6%
Largest holders: Capital Research Global Investors (6.2%), BAILLIE GIFFORD & CO (5.8%), Capital International Investors (3.7%), Capital World Investors (3.5%), Morgan Stanley (2.9%)
```

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>Buying and selling by company insiders</b> — score n/a</summary>

```text
Last 180 days: bought 0 shares in 0 transaction(s) | sold n/a shares in 0
Net: +0 shares | insiders hold 3,528,497 shares
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

- [How Big Could Microsoft Stock’s Next Fall Be?](https://www.trefis.com/stock/msft/articles/624529/how-big-could-microsoft-stocks-next-fall-be/2026-11-12)  
  <sub>Trefis, 6 hours ago</sub>  
  For questions about this article or underlying research, email help@trefis.com.Microsoft (MSFT) stock returned 29.1% over the six months to November 11,...
- [ETFs Are Buying Microsoft (MSFT) on Nov. 10](https://finance.yahoo.com/markets/stocks/articles/etfs-buying-microsoft-msft-nov-110043033.html)  
  <sub>Yahoo Finance, 4 hours ago</sub>  
  ETFs bought $337.7 million of Microsoft stock on Tuesday, with 53 funds buying and 16 selling.
- [Stock Market Today: CoreWeave (CRWV) Reignites the AI Trade, Then Nvidia’s (NVDA) Boardroom Takes Over the Story](https://www.google.com/goto?url=CAESwQEBxCJF17nk6tc3aMR3XpwHuGcWRV0xo2eSX_JTesMio0wOWMIjFWoqfUG019b-q4psz2uYlodSkPfXx2BZzPBw6XU3f96TfPKkNhdbdxbtAC9MzNeOtXpBNIiFJdvD_0x2Ox6aiHli6oXaG13MP5iqXcGNABVZvmmmZSCupXFL6xiT-ltSivtLYP3vpEHHWy0S5WusakL6HXY_IisgFlCab3LKyKS_l1i1pDZgOEupTzE3UnkqaPsPG5503iJguryb&gsessionid=z0HBgkBuWo1DjC9Pk_GkFfkc1NUTPrQeADYIzI7Uyg2v9MGgCpFuKw)  
  <sub>ChartMill, 5 hours ago</sub>  
  CoreWeave's strong quarter sent AI and chip stocks sharply higher, but a report that Nvidia's board is preparing to remove CEO Jensen Huang hit the stock...
- [Microsoft Beats Nvidia for the First Time Since 2025: So Why Is MSFT Stock Falling?](https://www.google.com/goto?url=CAESfAHEIkXX0PrS86W85b5_a7K8CgNEsmnpKnzvU5RFz8pVhj3TIS0Lxcob7_0MfLw66UfarVd3pM-smw8Dse6qiUiJEuziT9-QW5hIZEUHBgee-aFJ410rb04j39gA_SLEJB3KJaGPkdOlsJYNm1iYSta6WBk7K3kDjhkMqos&gsessionid=z0HBgkBuWo1DjC9Pk_GkFfkc1NUTPrQeADYIzI7Uyg2v9MGgCpFuKw)  
  <sub>BeInCrypto, 16 hours ago</sub>  
  Microsoft beats Nvidia in market value for the first time since 2025, yet MSFT stock falls over 3%. See why.
- [Anthropic Now Makes Its Own Spreadsheet Software. Here's What I'd Do With Microsoft Stock.](https://www.google.com/goto?url=CAESwQEBxCJF19gEKOCk_PWXoCxIqbkimAAdU_aBYdM6wemhls-HocuvRM9qnvrxVGES7Oky-NQBpxM1Ws8wQYeyxMxQL72ZqgvaEssbRxFBJnvmCKke7lSVW0IP0GWmnJR6orZSl32VddlvjX-zSeoToNc6qY3HdTS_iVH9fnGsVW3P_QECmNs6IndXxh8I0lUVzLiGEj4U_QQcsZEeJH_R48fAxepeTSop3UF6gYhyQJsqr4q3AiL999zVcwKrCR2iROTr&gsessionid=z0HBgkBuWo1DjC9Pk_GkFfkc1NUTPrQeADYIzI7Uyg2v9MGgCpFuKw)  
  <sub>The Motley Fool, 12 hours ago</sub>  
  Claude Sheets is still in beta. Should the Excel maker's shareholders worry?
- [MSFT 261030 500.00C (MSFT261030C500000) Stock Options Chain | Quotes & News](https://www.google.com/goto?url=CAEScAHEIkXXizrigK2F9XOGBGl65TD6kNQ7LVA5y2XFT1V4KC9-I2Oi4JE2ZUp5gor6oT37RCd8L3mrawSB0LbPiFf9FovtkNfNG3tN-jWz7kd4VLDDWerIvzjxVyx5a5LaON4ZCyGr4mbckpF8qCbMOPE&gsessionid=z0HBgkBuWo1DjC9Pk_GkFfkc1NUTPrQeADYIzI7Uyg2v9MGgCpFuKw)  
  <sub>Moomoo, 13 hours ago</sub>  
  Track real-time MSFT 261030 500.00C (MSFT261030C500000) stock options chain data and pricing information and news on moomoo App for your options trading and...
- [What's Going On With Microsoft Stock Wednesday?](https://www.google.com/goto?url=CAESoQEBxCJF1-iDtLHRCrJ17yQpnIFjTeV5kGTmYLy3eFReaRA7puH1uq57EAaKHooSeneGoT3TuGuLcwH-FP41DxfPoO3wUILGCYwTRuuhdpnb7xZfSP0t03ASRYZu3UZiqzyH_2nHpuAqjOTGasQSVVa9lNRa0wp-VvIC-HVtFJKsktw3R54G1_mnXmCJoui0YBD3Y9pk4wPONbJ82NqDso6Sfw&gsessionid=z0HBgkBuWo1DjC9Pk_GkFfkc1NUTPrQeADYIzI7Uyg2v9MGgCpFuKw)  
  <sub>Benzinga, 21 hours ago</sub>  
  Microsoft (NASDAQ:MSFT) stock slips amid potential China component bans and fresh workplace AI pressure from Anthropic.
- [Microsoft Stock At $521: Anthropic’s Landlord, Customer And Rival?](https://www.google.com/goto?url=CAESuAEBxCJF18F5G3-FTZ6IJiaRpgSoXesHwkDM3ZfVmEautY3ICmh4t3gTxSozMuIB8Ze5au23lBAWEO-EO8Rix8IIGAn9z32qVAF1Nq1O0E055y1EJJz-TJ_MRaQz8yzsQuzWZ4mwF9_qyNX3wK6_GkJUrBrxUynLYzjcMgcarSc17gsY8pA60Oa_4w_V8-2y-PimKtoKBs-bFBE1gcesEs6VghGSznt_dJK_3j2RC0doNFsnZ9c8Tj6D&gsessionid=z0HBgkBuWo1DjC9Pk_GkFfkc1NUTPrQeADYIzI7Uyg2v9MGgCpFuKw)  
  <sub>Trefis, 3 hours ago</sub>  
  More on the Anthropic IPO: our Anthropic IPO storyline page collects our pieces on it. Open Word at work, ask Copilot to draft Monday's board memo,...
- [Microsoft Corporation (MSFT) stock price, news, quote and history](https://www.google.com/goto?url=CAESZQHEIkXXbYYbnJpDaduVkb_i95BOIvI4kc-57ZAmr9DM73jFpRJewwLHBld2lgbjc6R6OzdKR4_6Z3nsiQsYQiboDof_YxkRMM4SXKQr04fOEEDZ4OXJ5udiN1W_1XxWyAcS-RNg&gsessionid=z0HBgkBuWo1DjC9Pk_GkFfkc1NUTPrQeADYIzI7Uyg2v9MGgCpFuKw)  
  <sub>Yahoo Finance Singapore, 23 hours ago</sub>  
  588,462.45% · Previous close 533.16 · Open 534.22 · Bid 525.02 x 400 · Ask 528.11 x 200 · Day's range 518.45 - 534.76 · 52-week range 349.20 - 559.15 · Volume...
- [MSFT Stock Heads to $500 as Microsoft Data-Centre Spending and Anthropic Workplace Competition Intensify](https://www.google.com/goto?url=CAES0AEBxCJF149ojYB5gPdV7SPYMh8QHX7WYyLP7sTUAnglG8FvO-cWUbG2SIgvv_doJL787gCAfrzV-NqTmM7Kp-lsZpsW2Z-igFsXkc-4zhnNZxy1EZekQ4BYeHXLkIxJFr9tbWehE7dykliZNLYjQjMrbRaerYi65u7f_8d8-1jEq6QztfNc6tx3aUES8gXAY_Qoo7u6IWtGR3LlgSGI9x2ZCw-fho00OzulU60VsrWWl30W6LOZ8Qwqqb-CawYdq0-4WFJumjYxde4yZiyOEU89&gsessionid=z0HBgkBuWo1DjC9Pk_GkFfkc1NUTPrQeADYIzI7Uyg2v9MGgCpFuKw)  
  <sub>FXLeaders, 11 hours ago</sub>  
  Microsoft stock retreat from the record high near $560 as renewed data-centre spending commitments, competition from Anthropic's workplace software and...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>Price and chart</b> — score n/a</summary>

```text
Last close 523.55 (bar of 2026-11-12), from 502 daily bars
Trend: vs 20d SMA 529.67 (-1.2%), 50d 518.73 (+0.9%), 200d 440.97 (+18.7%); 50d above 200d
Momentum: RSI(14) 48.7 | MACD 2.729 vs signal 4.309 (histogram -1.581)
Returns: 1d +0.5% | 5d -2.3% | 1m -1.9% | 3m +5.7%
52-week range: 352.83 - 555.80 (now 84.1% of the way up)
Volatility: ATR(14) 15.11 (2.9% of price) | annualised 20d 37.5%
Volume: 0.07x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score n/a</summary>

```text
Sector: Technology / Software - Infrastructure | market cap 3.89T
Valuation: trailing P/E 27.33 | forward P/E 21.64 | P/B 8.26 | PEG 1.58
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
Price target: mean 636.12 (+21.5% vs last close), range 440.00 - 870.00
Recent rating changes:
  - 2026-10-29 Bernstein: main, Outperform -> Outperform
  - 2026-10-29 RBC Capital: reit, Outperform -> Outperform
  - 2026-10-29 Citigroup: main, Buy -> Buy
  - 2026-10-29 DA Davidson: main, Buy -> Buy
  - 2026-10-29 TD Cowen: main, Buy -> Buy
  - 2026-10-29 Scotiabank: main, Sector Outperform -> Sector Outperform
Institutional ownership: 76.2%
Largest holders: Blackrock Inc. (8.2%), Vanguard Capital Management LLC (6.5%), State Street Corporation (4.2%), FMR, LLC (2.7%), Geode Capital Management, LLC (2.6%)
```

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>Buying and selling by company insiders</b> — score n/a</summary>

```text
Last 180 days: bought 518,348 shares in 17 transaction(s) | sold 256,954 shares in 11
Net: +261,394 shares (+4.5% of insider holdings) | insiders hold 6,015,217 shares
Distinct insiders: 0 buying, 4 selling
Sales — weak evidence on their own; often scheduled 10b5-1 plans, tax on vesting, or diversification:
  - 2026-11-09 HOOD AMY E (Chief Financial Officer): 7,305 shares, 3.98M
  - 2026-10-13 HOOD AMY E (Chief Financial Officer): 7,305 shares, 3.98M
  - 2026-09-14 HOOD AMY E (Chief Financial Officer): 41,674 shares, 20.76M
  - 2026-09-01 NADELLA SATYA (Chief Executive Officer): 86,525 shares, 43.39M
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

- [NVDA Stock On Track To Hit Lowest Level In Over A Year: Dan Ives Values Nvidia At $225 Without Jensen Huang](http://www.bing.com/news/apiclick.aspx?ref=FexRss&aid=&tid=6af5cffaa6014d2299bc7ed4b5c78892&url=https%3a%2f%2ffinance.yahoo.com%2fmarkets%2fstocks%2farticles%2fnvda-stock-track-hit-lowest-113858426.html&c=16031417559787308707&mkt=en-us)  
  <sub>Yahoo Finance, 11h ago</sub>  
  Dan Ives said he expects Huang to be removed and estimated Nvidia shares could be worth $225 without him, compared with $300 if he remains CEO.
- [Nvidia (NVDA) stock is trending in pre-market: Here’s what is happening](http://www.bing.com/news/apiclick.aspx?ref=FexRss&aid=&tid=6af5cffaa6014d2299bc7ed4b5c78892&url=https%3a%2f%2fwww.msn.com%2fen-us%2fnews%2fother%2fnvidia-nvda-stock-is-trending-in-pre-market-here-s-what-is-happening%2far-AA2hhI5d&c=15411940408183678453&mkt=en-us)  
  <sub>Benzinga on MSN, 13h ago</sub>  
  Nvidia Corp. NVDA shares are trending on Thursday. Second Affair Report Weighs on Nvidia Stock Shares of the Californian developer of AI and graphics chips fell 7.06% to 161.47 in the pre-market ...
- [Stock Market Today: Futures Fall On Trump Oil Remarks; Nvidia Plunges As Jensen Huang Resigns (Live Coverage)](http://www.bing.com/news/apiclick.aspx?ref=FexRss&aid=&tid=6af5cffaa6014d2299bc7ed4b5c78892&url=https%3a%2f%2fwww.investors.com%2fmarket-trend%2fstock-market-today%2fstock-market-today-nvidia-stock-nvda-jensen-huang%2f&c=11179059018980382696&mkt=en-us)  
  <sub>Investor's Business Daily, 9h ago</sub>  
  IBD, IBD Digital, IBD Live, IBD Weekly, Investor's Business Daily, Leaderboard, MarketDiem, MarketSurge and other marks are trademarks owned by Investor's Business Daily, LLC.
- [Nvidia Stock Price Today: NVDA Plunges 8% Toward $160 as CEO Crisis Deepens](http://www.bing.com/news/apiclick.aspx?ref=FexRss&aid=&tid=6af5cffaa6014d2299bc7ed4b5c78892&url=https%3a%2f%2fcoinpaper.com%2f38734%2fnvidia-stock-price-today-nvda-plunges-8-toward-160-as-ceo-crisis-deepens&c=10053142498566961053&mkt=en-us)  
  <sub>coinpaper.com, 18h ago</sub>  
  Nvidia stock tumbles 8.6% after hours toward $160 as reports of Jensen Huang's potential ouster intensify ahead of November 17 earnings.
- [NVDA Stock Rout: Another Analyst Slashes Rating, Beijing Warns US Against Tech Curbs](http://www.bing.com/news/apiclick.aspx?ref=FexRss&aid=&tid=6af5cffaa6014d2299bc7ed4b5c78892&url=https%3a%2f%2fstocktwits.com%2fnews-articles%2fmarkets%2fequity%2fnvda-stock-rout-another-analyst-slashes-rating-beijing-warns-us-against-tech-curbs%2fcNGzqRtR99y&c=16423008571101939486&mkt=en-us)  
  <sub>Stocktwits, 13h ago</sub>  
  Nvidia is at the center of a major controversy, with reports of a second alleged affair involving CEO Jensen Huang and the company’s board considering removing him.
- [How low will Nvidia stock go? Analysts worry that CEO succession could be a long-term threat to the price](http://www.bing.com/news/apiclick.aspx?ref=FexRss&aid=&tid=6af5cffaa6014d2299bc7ed4b5c78892&url=https%3a%2f%2fwww.fastcompany.com%2f91640961%2fhow-low-will-nvidia-stock-go-analysts-worry-that-ceo-succession-could-be-a-long-term-threat-to-the-price&c=988151165148795480&mkt=en-us)  
  <sub>Fast Company, 9h ago</sub>  
  Even under ideal conditions, leadership changes can weigh on shares. Add a scandal or two into the mix, and investors could be in for a bumpy ride.
- [Is Nvidia still a good buy after the stock sell-off?](http://www.bing.com/news/apiclick.aspx?ref=FexRss&aid=&tid=6af5cffaa6014d2299bc7ed4b5c78892&url=https%3a%2f%2finvezz.com%2fnews%2f2026%2f11%2f12%2fis-nvidia-still-a-good-buy-after-the-stock-sell-off%2f&c=4491410399037957627&mkt=en-us)  
  <sub>Invezz, 15h ago</sub>  
  Reuters reported that 59 of 64 brokerages covering Nvidia still rated the stock a buy or strong buy, with a median price target of $314. However, those targets should be treated cautiously. Some may ...
- [Nvidia (NVDA) Stock Drops 8% After Hours as Board Weighs Jensen Huang’s Future](http://www.bing.com/news/apiclick.aspx?ref=FexRss&aid=&tid=6af5cffaa6014d2299bc7ed4b5c78892&url=https%3a%2f%2fcoincentral.com%2fnvidia-nvda-stock-drops-8-after-hours-as-board-weighs-jensen-huangs-future%2f&c=4618884522892253655&mkt=en-us)  
  <sub>CoinCentral, 14h ago</sub>  
  Nvidia (NVDA) stock fell 8% after hours to $159.76 as the board reportedly prepares to oust CEO Jensen Huang. Here is what the report says.
- [Stock Market Today: S&P 500, DJI Slide as Nvidia CEO Jensen Huang Resigns, NVDA Drops 10%](http://www.bing.com/news/apiclick.aspx?ref=FexRss&aid=&tid=6af5cffaa6014d2299bc7ed4b5c78892&url=https%3a%2f%2fcoinpaper.com%2f38746%2fstock-market-today-s-and-p-500-futures-slide-as-nvidia-ceo-jensen-huang-resigns-nvda-drops-10&c=14497551248225692410&mkt=en-us)  
  <sub>coinpaper.com, 16h ago</sub>  
  S&P 500 futures fall 0.67% as Nvidia CEO Jensen Huang resigns and NVDA plunges 10%. Nasdaq futures drop 1.22% amid AI stock pressure.
- [NVDA Stock Price Forecast — Top Analysts Give Multiple Downgrades Ahead of November 17 Earnings amid CEO Jensen Huang Fiasco](http://www.bing.com/news/apiclick.aspx?ref=FexRss&aid=&tid=6af5cffaa6014d2299bc7ed4b5c78892&url=https%3a%2f%2fwww.tipranks.com%2fnews%2fnvda-stock-price-forecast-what-wall-street-sees-ahead-of-november-17-earnings-amid-ceo-jensen-huang-fiasco&c=6033928331728410705&mkt=en-us)  
  <sub>TipRanks, 10h ago</sub>  
  Nvidia ($NVDA) stock fell over 7% in Thursday’s pre-market session. The decline came after a 2.87% gain during regular hours, as reports about CEO Jensen Huang’s ...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>Price and chart</b> — score n/a</summary>

```text
Last close 160.35 (bar of 2026-11-12), from 502 daily bars
Trend: vs 20d SMA 200.96 (-20.2%), 50d 215.84 (-25.7%), 200d 204.31 (-21.5%); 50d above 200d
Momentum: RSI(14) 24.2 | MACD -13.708 vs signal -9.173 (histogram -4.535)
Returns: 1d -7.7% | 5d -11.7% | 1m -27.5% | 3m -28.8%
52-week range: 160.35 - 239.24 (now 0.0% of the way up)
Volatility: ATR(14) 9.86 (6.1% of price) | annualised 20d 56.5%
Volume: 1.26x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score n/a</summary>

```text
Sector: Technology / Semiconductors | market cap 3.87T
Valuation: trailing P/E 20.28 | forward P/E 10.07 | P/B 16.91 | PEG 0.21
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
Consensus: strong_buy (mean 1.39 on a 1=strong buy to 5=strong sell scale, 56 analysts)
Ratings: 10 strong buy, 45 buy, 6 hold, 1 sell, 0 strong sell
Price target: mean 309.72 (+93.2% vs last close), range 180.00 - 515.00
Recent rating changes:
  - 2026-11-12 Stifel: main, Buy -> Buy
  - 2026-11-12 RBC Capital: main, Outperform -> Outperform
  - 2026-11-12 William Blair: down, Outperform -> Market Perform
  - 2026-11-12 Keybanc: down, Overweight -> Sector Weight
  - 2026-11-12 Bernstein: down, Outperform -> Market Perform
  - 2026-11-12 Cantor Fitzgerald: main, Overweight -> Overweight
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
Net: -3,585,082 shares (-0.4% of insider holdings) | insiders hold 965,445,952 shares
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

- [Novo Nordisk (CPSE:NOVO B) Stock Still Looks Undervalued As Shares Fell 56%](https://finance.yahoo.com/markets/stocks/articles/novo-nordisk-cpse-novo-b-002421410.html)  
  <sub>Yahoo Finance, 14 hours ago</sub>  
  Novo Nordisk has had a rough three years in the market, even as interest in its GLP-1 obesity and diabetes treatments has grown.
- [Novo Nordisk Stock: Better Than It Looks, But Not A Buy Yet (NYSE:NVO)](https://seekingalpha.com/article/4966880-novo-nordisk-better-than-it-looks-but-not-a-buy-yet)  
  <sub>Seeking Alpha, 4 hours ago</sub>  
  Novo Nordisk's future hinges on broadening its drug franchises, notably CagriSema and Zenagamtide. Read why NVO stock is a hold.
- [NVO trades flat as consolidation near a key level continues](https://www.google.com/goto?url=CAESlAEBxCJF1zWeqMuIIL3T0FEvwdgTKXQMNv6o2ZMdKhA8wGUcDdbCytA_Bx8jKMuz9mSFodxCk8k4dREShu8skbtSSYV-0psva2WXrYQ8l32MhmiJXiQUxM9yRZRJ6H4ud9eivHtpUHB-mmtpLC8X961ROn2TQ7sRWbRMEqI6cUSpg_pnO3NhPYjLy1vqiaoS3UstAQ0J&gsessionid=ck2IbK18lzMYNqJ25RKAw7crvi6r-zrZF0Pt_5YbGP2aWPJJasx5-A)  
  <sub>Traders Union, 7 hours ago</sub>  
  Novo Nordisk (NVO) stock is trading at $41.1, up 0.98% for the day. The stock stands above its key short- and medium-term moving averages,...
- [Novo Nordisk (NVO) Stock May Trade Below Fair Value Following Raised Outlook](https://www.google.com/goto?url=CAES0AEBxCJF17d0i73OGSgvx3J6SxPwJS-2gLbM8VnooXowKl-ukcuNTuOWJTOl9k0tyOz7eBXAJzn25pEAlsaYvnCYbqw6qoP38wnucvUDnRFKdi9YKc8pEO9pRDipOlRnOwC5Z_zeiA7AJoF-8qXAnLWCi_mebR1ewM5P-DD95-Ysu3dp-IiUlDl2n3dj8sOsc0gyKqRnZLpTLiI_ZheP9IY9vE5j0sZE-CxPLdfTmiqUB-JhiBiDahYUVmz88q4ChmKBOtqyGa76wxcb5XnUpWMz&gsessionid=ck2IbK18lzMYNqJ25RKAw7crvi6r-zrZF0Pt_5YbGP2aWPJJasx5-A)  
  <sub>Simply Wall St, 17 hours ago</sub>  
  Novo Nordisk has seen a sharp reset in its share price over the past few years, even as it remains in the spotlight for obesity and diabetes treatments.
- [NVO Sep 2027 60.000 call (NVO270917C00060000) Interactive Stock Chart - Yahoo Finance](https://www.google.com/goto?url=CAESeQHEIkXXXk0Ivg3-XvK2S5N4tM72Jjzi89F2lO801LIOkAGWzy8sY6NEeYNCoW6iZoGjADd6ZcXsA0RRQdHRCW7H0TS48QqMe93aeZ6BTU12sM7NIyjrnoDzLDP8fzhkWdurcq9YAexfmY6qDIsjps7SHz43kM7gxZo&gsessionid=ck2IbK18lzMYNqJ25RKAw7crvi6r-zrZF0Pt_5YbGP2aWPJJasx5-A)  
  <sub>Yahoo! Finance Canada, 7 hours ago</sub>  
  Interactive Chart for NVO Sep 2027 60.000 call (NVO270917C00060000), analyze all the data with a huge range of indicators.
- [NVO Dec 2026 50.000 call (NVO261224C00050000) Stock Price, News, Quote & History](https://www.google.com/goto?url=CAEScwHEIkXXlguNI-KWnKnZ63EdOyBGSqlwqUFvcijUF7R72CGj2PZ_TGlD7CjDckeBDC1Sx3kNFkj3XerA93lsSpqVAi2s46i8SyiqvsbFtF3kcu7BvxSVxQARZhNFn5Nq0WcNcugpwW2EMboMjebA5ZlnOfY&gsessionid=ck2IbK18lzMYNqJ25RKAw7crvi6r-zrZF0Pt_5YbGP2aWPJJasx5-A)  
  <sub>Yahoo! Finance Canada, 13 hours ago</sub>  
  Find the latest NVO Dec 2026 50.000 call (NVO261224C00050000) stock quote, history, news and other vital information to help you with your stock trading and...
- [Novo Nordisk: Valuations Are Blind To The Upside (NYSE:NVO)](https://www.google.com/goto?url=CAESlQEBxCJF11-P7_4pkWunp1NHTgRhKsuya9An6GYyAMFDHpM2qtO_osmgVTq4th-v4KqhMtaptda_yoxUQJ41RyNLUGZlo8RN6xyYZP5Y06YHGkc6m4WJXtgNNilxQJm8kGwCGkOUQ3ZkGScPTDjy86tiAL_qXxNXxshw88PK0Qlwr-hCy9bw9wFg9aljFYqDC_b1Fnyxgg&gsessionid=ck2IbK18lzMYNqJ25RKAw7crvi6r-zrZF0Pt_5YbGP2aWPJJasx5-A)  
  <sub>Seeking Alpha, 15 hours ago</sub>  
  Novo Nordisk's Q3 2026 beat and overlooked guidance upgrades make medium-term de-rating exceedingly unlikely. Click for more on the NVO stock.
- [NVO Nov 2026 41.500 call (NVO261113C00041500) interactive stock chart](https://www.google.com/goto?url=CAESeQHEIkXXpfHleuqaYCnReTjXluUSo7KQos6qK9GdAHkw3mznENX5E-s_enpVLskxQFSFq7PGiwcJ2tD4VNJGFJt2NRlgjpNqt1Aa_IIwIPCW8jBk70G_d2HqyniJ34YhT8ECh1Yld1n9AH2YI_ciFM3opd6LhQlpEDI&gsessionid=ck2IbK18lzMYNqJ25RKAw7crvi6r-zrZF0Pt_5YbGP2aWPJJasx5-A)  
  <sub>Yahoo Finance UK, 11 hours ago</sub>  
  Interactive chart for NVO Nov 2026 41.500 call (NVO261113C00041500) – analyse all of the data with a huge range of indicators.
- [NVO Dec 2026 38.000 put (NVO261224P00038000) stock price, news, quote and history](https://www.google.com/goto?url=CAEScwHEIkXXTZK0_BDZKLH2aBZd1isbZNCsfwnaIP1xv-_p7HMXTCRdavHxMUiKiir_420d2jsO_o7_d8hSbuxZ-9Kx1zk-HSnlBJobeMMoPQjUAygsH5FLa6Bmnct9i0CCY1gbW7Gq-SLgHkXLm_8CPpMb_Oc&gsessionid=ck2IbK18lzMYNqJ25RKAw7crvi6r-zrZF0Pt_5YbGP2aWPJJasx5-A)  
  <sub>Yahoo Finance UK, 15 hours ago</sub>  
  Find the latest NVO Dec 2026 38.000 put (NVO261224P00038000) stock quote, history, news and other vital information to help you with your stock trading and...
- [NVO Nov 2026 40.000 call (NVO261113C00040000) stock price, news, quote and history](https://www.google.com/goto?url=CAEScwHEIkXXmWdS2talDDCQ2I2-ty4-zwsk8Nmm4zYAyHq2q8xcv87cpfaYe2nRvQE_D1pDB3jKOiumvPgP6nUU3dJ5vj8qGr6Y4iaZH4KmG2t244-kTHw9vzQT8Eq88r5rixqdNaEcP3QoM5lXYFauFZOvCg8&gsessionid=ck2IbK18lzMYNqJ25RKAw7crvi6r-zrZF0Pt_5YbGP2aWPJJasx5-A)  
  <sub>Yahoo Finance UK, 16 hours ago</sub>  
  Find the latest NVO Nov 2026 40.000 call (NVO261113C00040000) stock quote, history, news and other vital information to help you with your stock trading and...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>Price and chart</b> — score n/a</summary>

```text
Last close 40.48 (bar of 2026-11-12), from 502 daily bars
Trend: vs 20d SMA 39.82 (+1.7%), 50d 40.20 (+0.7%), 200d 43.27 (-6.4%); 50d below 200d
Momentum: RSI(14) 52.2 | MACD 0.299 vs signal 0.086 (histogram 0.213)
Returns: 1d -1.5% | 5d +0.4% | 1m +6.2% | 3m -11.8%
52-week range: 35.29 - 63.98 (now 18.1% of the way up)
Volatility: ATR(14) 1.05 (2.6% of price) | annualised 20d 32.7%
Volume: 0.25x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score n/a</summary>

```text
Sector: Healthcare / Drug Manufacturers - General | market cap 178.45B
Valuation: trailing P/E 10.22 | forward P/E 11.86 | P/B 5.45 | PEG 4.17
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
Price target: mean 45.74 (+13.0% vs last close), range 39.77 - 64.63
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

- [Is Procter & Gamble (PG) Worth More Than Its Price Today?](https://finance.yahoo.com/markets/stocks/articles/procter-gamble-pg-worth-more-121415536.html)  
  <sub>Yahoo Finance, 2 hours ago</sub>  
  Procter & Gamble has delivered steady gains for long term holders, and the share price now puts a spotlight on a simple question for you as an investor.
- [The Ultimate Dividend Stock to Buy With $1,000 Right Now](https://www.fool.com/investing/2026/11/12/ultimate-dividend-stock-to-buy-1k-procter-pg/)  
  <sub>The Motley Fool, 4 hours ago</sub>  
  Past performance is no guarantee of future results, but it's a pretty good indication of what's likely for Procter & Gamble.
- [Procter & Gamble (PG) Has Raised Its Dividend for 70 Straight Years. Here's Why I'd Buy Before 2027.](https://www.google.com/goto?url=CAES7wEBxCJF15W9Ysq-E1VEoKamnseqJaSyGFFe4FOzUGxlGMxsFVAtfaP1xy_yct6GEpWwiLNBsMplHoKQgOfCdnwZJAQ9yY7p3BiCXCcr37XnG0qdNeLLsorPCAuLintMQc39kfJRkdsvPWcsKEnVC7BFDeJ69SkGSdww3OHFku2xqdzAS_FXKHmcH5ajHSRyB1RzP4Vs7uoUO7i_A98BN40-A1Kx5o07qEMKD8RYIeIiQwHY614FKyYlkHfms-VLxhJnFPBHF3C8G78f8ePOVe2QvFH8tsNLWxcTBA9GTnp4vL1VbuR5f8c7_O98wnxOMw&gsessionid=1bj4UNY1xlX3F26hlAqkY-cGsajdnSEoWW7c_C75QT85DU-6ZlviEQ)  
  <sub>The Globe and Mail, 7 hours ago</sub>  
  Detailed price information for Nvidia Corp (NVDA-Q) from The Globe and Mail including charting and trades.
- [Grooming CEO sells 5,370 Procter & Gamble (PG) shares at $169 each.](https://www.google.com/goto?url=CAESqgEBxCJF10ZmYtAqYo-sdt885_lGkkGZiOMUJRpkAvEuquh_yn__IB5_Dr3oV147vVUvRZUb5sdySK4eQpbw0ZsJkcQZJe5lCMNwKxDdgJbMKIPUEcot01qOf3mYaP_K1TUf9yuaTISBwzV43FMuLFXTNvvz3GDmxd4UvNRzs4ByD9E-O6NtlDS6f1zEJ4Wwi-Ef_xI7Nhiu2g0kpUqZsyyLpwc6k1HjOyS71Q&gsessionid=1bj4UNY1xlX3F26hlAqkY-cGsajdnSEoWW7c_C75QT85DU-6ZlviEQ)  
  <sub>Stock Titan, 3 hours ago</sub>  
  de Azevedo Juliana Monteiro Santos reported 21361.2363 shares held directly after the November 5, 2026 sale. No Rule 10b5-1 plan was reported.
- [Procter & Gamble (PG) Reshuffles India Leadership As Fair Value Debate Stays In Focus](https://www.google.com/goto?url=CAESwwEBxCJF1-XBjQNuFUjlrazrem44YmqbJ3H6mn_dfdPbiVU4wV4KpOOHxV1iThVRA8bOMELlUMisTfmVa1h6EwyF1SgFk831iM7yhJX3mZnhJShgx8ClkWj4oCKtDdXoGofzzWCRRgU900ZLbOWikoDLi0TyTUSLwxpAtaIrA1E2AcEmN8tvqv7D6o39-lT8P_pGFamlbSLKcyD_tAsCO3ggUvhV9LiouGRgP6xlDlMKvba0r2bzco1tZKPVIq2uesmubME&gsessionid=1bj4UNY1xlX3F26hlAqkY-cGsajdnSEoWW7c_C75QT85DU-6ZlviEQ)  
  <sub>Simply Wall St, 2 hours ago</sub>  
  Procter & Gamble (PG) just reshuffled its leadership bench in India, promoting Shalini Saraswat to Brand Director and Business Head for Pantene India,...
- [Fifth Third Bancorp Sells 177,691 Shares of Procter & Gamble Company (The) $PG](https://www.google.com/goto?url=CAESwwEBxCJF11X00cgX7K3qUixJjgCaa3L4fxbryLMWB_-eSKbQvuI5zQ5XUOcMH4GFwdYPMwnRcgRfVfzA8ql8FW92cySMXkBl6GweJo8mkUFXOrR9O0-cZTGQx0EUhszitOruPzbCdAU-0t92aJt4jtN7jv0I_VfobGMiDVWD32kiXG1sPEGobsqT3oPYj2gNYWCFljTHk3-cvWtBLk-hiKdMD-efX69B-z-raJWFZDrqwzDuTmuokiegRn2R9sjroKqwVGI&gsessionid=1bj4UNY1xlX3F26hlAqkY-cGsajdnSEoWW7c_C75QT85DU-6ZlviEQ)  
  <sub>MarketBeat, 5 hours ago</sub>  
  Fifth Third Bancorp lowered its holdings in shares of Procter & Gamble Company (The) (NYSE:PG - Free Report) by 6.6% in the third quarter, according to the...
- [What Will Procter & Gamble (NYSE:PG) Lay Out at Strategy Day?](https://www.google.com/goto?url=CAESoAEBxCJF1yoPVDL6_WpBKc1qYPppfxIZMqR6yPA7e5UWYZQw81JmQ0Nlm4fb-Jo4itPrEQr_euC-KrH8T-F7jndsb7GyhaEoja87F4JD-1nO4FTGaZffkZOzXUs-sUwBSm8K2pem30-4oiLzmsVeuGLEGYCCo6MPyTo2KEhrcoIr-bhXDIUhv7QkRZIq9txbQyw4VUgPMnJjZonQO5afqB8_&gsessionid=1bj4UNY1xlX3F26hlAqkY-cGsajdnSEoWW7c_C75QT85DU-6ZlviEQ)  
  <sub>Kalkine Media, 8 hours ago</sub>  
  Procter & Gamble will webcast its strategy day presentation next week, following a quarter that lifted its sales guidance and put beauty in front.
- [These 5 Dividend Aristocrats® Have Raised Payouts for Decades](https://www.google.com/goto?url=CAESzQEBxCJF16XGYmt35de4Lds8ykQuMzK2prjZny8nOq6vc9oqX5vjlxCWLAZsUeK3MU4B0VYr3j75ZbjDIosucJXXD1IF1U-B9GHm20qQFcjBXQNr-cxlVceBwznr3C3mnL1GeG0c4CTnkeUkrN9v4-7DvXYKy2XKAtfXAhuyO46Q1uAs-_K4RWOAw1j7p1XmH28WZHQq1BI_W5-HR8KSR3qr0MpcokCdeJqTeS-_6F5Q5Q2NNh5e4RqeLSg1Dx4nnUzNd4HLqXIPeSVp0nbH&gsessionid=1bj4UNY1xlX3F26hlAqkY-cGsajdnSEoWW7c_C75QT85DU-6ZlviEQ)  
  <sub>The Globe and Mail, 13 hours ago</sub>  
  Coca-Cola, Procter & Gamble, Johnson & Johnson, PepsiCo, and Colgate-Palmolive have incredible dividend histories. Each of these reliable dividend stocks...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>Price and chart</b> — score n/a</summary>

```text
Last close 169.27 (bar of 2026-11-12), from 502 daily bars
Trend: vs 20d SMA 162.94 (+3.9%), 50d 153.83 (+10.0%), 200d 149.78 (+13.0%); 50d above 200d
Momentum: RSI(14) 67.4 | MACD 4.275 vs signal 4.001 (histogram 0.274)
Returns: 1d +1.0% | 5d +1.3% | 1m +8.1% | 3m +17.1%
52-week range: 138.04 - 169.27 (now 100.0% of the way up)
Volatility: ATR(14) 3.24 (1.9% of price) | annualised 20d 29.2%
Volume: 0.08x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score n/a</summary>

```text
Sector: Consumer Defensive / Household & Personal Products | market cap 392.34B
Valuation: trailing P/E 25.49 | forward P/E 22.88 | P/B 7.22 | PEG 4.33
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
Price target: mean 174.04 (+2.8% vs last close), range 151.00 - 190.00
Recent rating changes:
  - 2026-10-26 Barclays: main, Equal-Weight -> Equal-Weight
  - 2026-10-26 Piper Sandler: main, Neutral -> Neutral
  - 2026-10-23 Freedom Broker: up, Hold -> Buy
  - 2026-10-23 UBS: main, Buy -> Buy
  - 2026-10-23 Citigroup: main, Buy -> Buy
  - 2026-10-23 BNP Paribas: main, Outperform -> Outperform
Institutional ownership: 72.0%
Largest holders: Blackrock Inc. (8.2%), Vanguard Capital Management LLC (6.6%), State Street Corporation (4.4%), Geode Capital Management, LLC (2.9%), Vanguard Portfolio Management LLC (2.7%)
```

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>Buying and selling by company insiders</b> — score n/a</summary>

```text
Last 180 days: bought 322,138 shares in 48 transaction(s) | sold 231,372 shares in 26
Net: +90,766 shares (+4.2% of insider holdings) | insiders hold 2,248,249 shares
Distinct insiders: 0 buying, 10 selling
Sales — weak evidence on their own; often scheduled 10b5-1 plans, tax on vesting, or diversification:
  - 2026-11-05 SCHULTEN ANDRE (Chief Financial Officer): 30,677 shares, 5.18M
  - 2026-11-04 SCHULTEN ANDRE (Chief Financial Officer): 33,624 shares, 5.55M
  - 2026-11-03 JANZARUK MATTHEW W. (Officer and Director): 9,479 shares, 1.55M
  - 2026-10-30 GAMA PAUL (Officer): 2,894 shares, 477.51K
(46 grant/option/gift transaction(s) excluded — compensation, not a view on the price)
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

- [Teva Pharmaceutical Industries (TEVA) Earnings Put Its Turnaround Valuation Back In Focus](http://www.bing.com/news/apiclick.aspx?ref=FexRss&aid=&tid=6af5d063754946b78484ad305351c162&url=https%3a%2f%2ffinance.yahoo.com%2fhealthcare%2farticles%2fteva-pharmaceutical-industries-teva-earnings-051318202.html&c=12738527130080672487&mkt=en-us)  
  <sub>Yahoo Finance, 18h ago</sub>  
  Teva Pharmaceutical Industries (NYSE:TEVA) just delivered third quarter 2026 earnings, reporting sales of US$4.4b and net income of US$233m, along with higher impairment charges and a slightly raised ...
- [Teva Pharmaceutical Industries (TEVA) Holds First R&D Day With New Pipeline Milestones](http://www.bing.com/news/apiclick.aspx?ref=FexRss&aid=&tid=6af5d063754946b78484ad305351c162&url=https%3a%2f%2ffinance.yahoo.com%2fhealthcare%2farticles%2fteva-pharmaceutical-industries-teva-holds-101405555.html&c=10505910702908359838&mkt=en-us)  
  <sub>Yahoo Finance, 12h ago</sub>  
  Teva Pharmaceutical Industries (NYSE:TEVA) hosted its first R&D Day at the New York Stock Exchange in 2026. Management outlined a long term growth plan centered on higher value medicines and a shift ...
- [Teva stock targets $6-7 billion in innovative medicines by 2030](http://www.bing.com/news/apiclick.aspx?ref=FexRss&aid=&tid=6af5d063754946b78484ad305351c162&url=https%3a%2f%2fwww.ad-hoc-news.de%2fboerse%2fnews%2fcorporate-news%2fteva-stock-targets-6-7-billion-in-innovative-medicines-by-2030%2f70496738&c=12456323447138655268&mkt=en-us)  
  <sub>Ad Hoc News, 12h ago</sub>  
  Teva lifted its 2030 revenue target for innovative medicines to $6-7 billion from about $5 billion, according to Globes. The company projects branded products at $3.77-3.92 billion this year, or ...
- [Teva CEO: We have evolved into a biopharma company](http://www.bing.com/news/apiclick.aspx?ref=FexRss&aid=&tid=6af5d063754946b78484ad305351c162&url=https%3a%2f%2fen.globes.co.il%2fen%2farticle-teva-ceo-we-have-evolved-into-a-biopharma-company-1001563136&c=15394006594581091880&mkt=en-us)  
  <sub>Globes, 12h ago</sub>  
  During the R&D Day, Teva provided updates on its innovative drug pipeline and announced an increase in its revenue target for innovative medicines by 2030, raising it from about $ ...
- [Teva CEO Richard Francis goes one-on-one with Jim Cramer](http://www.bing.com/news/apiclick.aspx?ref=FexRss&aid=&tid=6af5d063754946b78484ad305351c162&url=https%3a%2f%2fwww.cnbc.com%2finvestingclub%2fvideo%2f2026%2f11%2f11%2fteva-ceo-richard-francis-goes-one-on-one-with-jim-cramer.html&c=16139143144500789296&mkt=en-us)  
  <sub>CNBC, 21h ago</sub>  
  Teva President and CEO Richard Francis joins 'Mad Money' host Jim Cramer to talk its first R&D day, where it is seeing growth opportunities, its individual offerings, and more.
- [Teva outlines aggressive R&D strategy with $7 billion in innovative medicine revenue by 2030](http://www.bing.com/news/apiclick.aspx?ref=FexRss&aid=&tid=6af5d063754946b78484ad305351c162&url=https%3a%2f%2fwww.msn.com%2fen-us%2fmoney%2fgeneral%2fteva-outlines-aggressive-r-d-strategy-with-7-billion-in-innovative-medicine-revenue-by-2030%2far-AA2heudI&c=16950381737004309121&mkt=en-us)  
  <sub>Benzinga on MSN, 29h ago</sub>  
  Teva Pharmaceutical Industries Ltd. TEVA on Wednesday said it targets $6 billion to $7 billion in innovative medicine revenue by 2030. President and CEO Richard Francis outlined a comprehensive ...
- [Teva Pharmaceutical R&D Day 2026: First-in-class drugs for Tourette syndrome, celiac disease, and IBD scarring](http://www.bing.com/news/apiclick.aspx?ref=FexRss&aid=&tid=6af5d063754946b78484ad305351c162&url=https%3a%2f%2fwww.msn.com%2fen-us%2fscience%2fbiology%2fteva-pharmaceutical-r-d-day-2026-first-in-class-drugs-for-tourette-syndrome-celiac-disease-and-ibd-scarring%2far-AA2hfMHn&c=7041494951266367642&mkt=en-us)  
  <sub>Tech Times on MSN, 20h ago</sub>  
  Teva Pharmaceutical's inaugural R&D Day unveiled three first-in-class drugs targeting Tourette syndrome in children, celiac disease, and IBD -- conditions no approved therapy fully addresses -- ...
- [Teva Pharmaceutical Industries Aims to Generate Up to $7 Billion in Innovative Medicines Revenue by 2030](http://www.bing.com/news/apiclick.aspx?ref=FexRss&aid=&tid=6af5d063754946b78484ad305351c162&url=https%3a%2f%2fwww.marketscreener.com%2fnews%2fteva-pharmaceutical-industries-aims-to-generate-up-to-7-billion-in-innovative-medicines-revenue-by-ce785edbdc81f723&c=17819226282711457565&mkt=en-us)  
  <sub>MarketScreener, 30h ago</sub>  
  Teva Pharmaceutical Industries Insider Sold Shares Worth $1,095,567, According to a Recent SEC Filing MT Nov. 06 Teva Pharmaceutical Industries Insider Sold Shares Worth $1,928,729, According to a ...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>Price and chart</b> — score n/a</summary>

```text
Last close 43.36 (bar of 2026-11-12), from 502 daily bars
Trend: vs 20d SMA 41.43 (+4.7%), 50d 40.02 (+8.3%), 200d 35.04 (+23.7%); 50d above 200d
Momentum: RSI(14) 64.4 | MACD 0.877 vs signal 0.727 (histogram 0.151)
Returns: 1d +0.3% | 5d +3.8% | 1m +6.5% | 3m +17.9%
52-week range: 24.21 - 43.36 (now 100.0% of the way up)
Volatility: ATR(14) 1.18 (2.7% of price) | annualised 20d 27.4%
Volume: 0.07x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score n/a</summary>

```text
Sector: Healthcare / Drug Manufacturers - Specialty & Generic | market cap 50.59B
Valuation: trailing P/E 100.84 | forward P/E 13.86 | P/B 6.34 | PEG 0.71
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
Price target: mean 49.44 (+14.0% vs last close), range 42.12 - 57.00
Recent rating changes:
  - 2026-11-12 Piper Sandler: main, Overweight -> Overweight
  - 2026-11-05 Leerink Partners: main, Outperform -> Outperform
  - 2026-11-04 TD Cowen: main, Buy -> Buy
  - 2026-11-04 HC Wainwright & Co.: main, Buy -> Buy
  - 2026-11-02 HC Wainwright & Co.: init, ? -> Buy
  - 2026-10-15 Barclays: main, Overweight -> Overweight
Institutional ownership: 43.9%
Largest holders: Blackrock Inc. (5.5%), Phoenix Financial Ltd. (3.6%), WCM Investment Management, LLC (3.6%), Clal Insurance Enterprises Holdings Ltd (3.5%), Menora Mivtachim Holdings Ltd. (3.4%)
```

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>Buying and selling by company insiders</b> — score n/a</summary>

```text
Last 180 days: bought 43,476 shares in 3 transaction(s) | sold 29,021 shares in 4
Net: +14,455 shares (+0.3% of insider holdings) | insiders hold 5,635,773 shares
Distinct insiders: 0 buying, 8 selling
Sales — weak evidence on their own; often scheduled 10b5-1 plans, tax on vesting, or diversification:
  - 2026-09-18 SAVAGE BRIAN (Officer): 7,342 shares, 285.21K
  - 2026-09-18 MIGNONE ROBERTO A. (Director): 367,600 shares, 14.36M
  - 2026-08-21 WEISS AMIR (Officer): 9,445 shares, 355.30K
  - 2026-08-03 HUGHES ERIC A (Officer): 25,578 shares, 892.05K
(12 grant/option/gift transaction(s) excluded — compensation, not a view on the price)
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

- [AIML Subsidiary NeuralCloud Signs Agreement With MyCor360+ to Integrate MaxYield(TM) into Next-Generation Cardiac Monitoring Device](https://finance.yahoo.com/healthcare/articles/aiml-subsidiary-neuralcloud-signs-agreement-123000497.html)  
  <sub>Yahoo Finance, 2 hours ago</sub>  
  Collaboration to Combine AI-Powered ECG Signal Processing with New Cardiac Monitoring Hardware for Clinical ApplicationsTORONTO, ON / ACCESS Newswire...
- [Zentek Adds Direct-to-Consumer Channel for ZenGUARD(TM), Alongside Its Government and Institutional Sales](https://www.marketscreener.com/news/zentek-adds-direct-to-consumer-channel-for-zenguard-tm-alongside-its-government-and-institutional-ce785ed8df89f327)  
  <sub>www.marketscreener.com, 1 hour ago</sub>  
  Guelph, Ontario-- - Zentek Ltd. today announced the launch of its ZenGUARD™ online store at zenguard.com. The store is an additional sales channel.
- [Toyota Motor (NYSE:TM) Rating Lowered to "Hold" at Freedom Broker](https://www.google.com/goto?url=CAESuAEBxCJF15kcAYeYwZICw6CFwUlpPKBQAreZxmwwO7S9OemUy5EKifJIJKlKfRW_K4DcIZIuRp9A5x0ytrhjAUqRMqE4Vj-buiz8bmIwq_3egzIaik7rZovt0at5rFXwstjGOnW1UWik1_-mhtMgk7hc71r02e70DbHdRD_vtPkWThkvPTPvWcGgXx9irtcdzs1MfQoemi_9S4KWjKVO8G9beLzPcBTQnu11JFN74zt2A_dxWE8sQOt1&gsessionid=Y9qOC8ZPI9wVdDf9Au-oDUZA3Ips2gCSXyLPQ1-UU0hLpofkKQzE7Q)  
  <sub>MarketBeat, 3 hours ago</sub>  
  Freedom Broker downgraded Toyota Motor from a "buy" rating to a "hold" rating and set a $230.00 price objective for the company. in a research report on...
- [(HBIL) Long Term Investment Analysis (HBIL:CA)](https://www.google.com/goto?url=CAESmQEBxCJF13RaaFICzUhT1Izoc1pqY24r2W9F6qgdmgysOU1Eb1BILFw7ItJ1St5vp5UT2rtzbSpAR3YSBfH51J9Xt83KiJbju3w0m2t-AgNnpfvL9BdQDavAWC7Jc6cS9vX0-xuZiIA-rHs_ZWa8-qoOZEuv0WyGKyVfDTQF6RDg1vjcG6YUUDpt15S2PDtghWkJHplWFtSFMcM&gsessionid=Y9qOC8ZPI9wVdDf9Au-oDUZA3Ips2gCSXyLPQ1-UU0hLpofkKQzE7Q)  
  <sub>Stock Traders Daily, 1 hour ago</sub>  
  Political Decisions Influence Hamilton U.S. T-Bill YIELD MAXIMIZER TM ETF HBIL and Investors Should Listen.
- [Learn to Evaluate (HBIL.U) using the Charts (HBIL.U:CA)](https://www.google.com/goto?url=CAESnwEBxCJF15oEQl7tL1Gpnzn_hdkWNnUB85FRbj3xQMIipUBhRHEX0bukparo_OW14ckbHou2reXgAgaaYX1UQTXZnVDwVv5ks0ZahELj5V8b36SWoYE_HoAju4SisEuNraIvNtR1AMt64KB1GbTcESBvlomFCmN1eVCM3N81g6YCmYNfxPUwlvO6-tM7e5OFX9dYA23TqADMXZeftxtwBUo&gsessionid=Y9qOC8ZPI9wVdDf9Au-oDUZA3Ips2gCSXyLPQ1-UU0hLpofkKQzE7Q)  
  <sub>Stock Traders Daily, 2 hours ago</sub>  
  Learn to Evaluate Hamilton U.S. T-Bill YIELD MAXIMIZER TM ETF HBIL.U using the Charts.
- [LovelySkin Voted No. 1 Beauty Retailer in Newsweek's 2026 Readers' Choice(TM) Awards](https://www.google.com/goto?url=CAESnQEBxCJF12c5Zkzv4FSSAudXmvV4NurmmVCOhAGpxPuCiN4jwKNHIXQShiGTn1ItXNfAHSpqZGbLKAT2jJI1XjczvkJ5E8c_x9ij4RC14X4l7dy1ajRFbg5BK5eChV0N_myY-VgNNu2MvR0ogQPbmXVqOA7BYH7QTkdOtvPzTgzpg_kyqJxYqoEnwf1xaZ4ELD1mfrv3TIqRrEhYGqi6&gsessionid=Y9qOC8ZPI9wVdDf9Au-oDUZA3Ips2gCSXyLPQ1-UU0hLpofkKQzE7Q)  
  <sub>Yahoo Finance, 22 hours ago</sub>  
  The Newsweek Readers' Choice™ Awards highlight top companies as voted on by our readers across a wide range of categories, including Best Beauty Retailer.
- [Apple's foldable phone now lets teams work with AI live](https://www.google.com/goto?url=CAESswEBxCJF10qjsJXeoYi1vPYmyqtvIwpP1RIMw-7l4r3X97aFGpv3HsbTNIh3evr80LtAq8aG3f2BfhSzY51orOrJd4lA8vvTJKZh4nsI4lj-4ApZn960utEcJwezJ_s9XBEj1ZZfEDRf1tqDhDH40Hsx8rfMXF8bD_-exrY8AlJdT-qHgahPzJua-VUxK6kfcsGg_FMhsTr2zo-deckcpdwZkm5N281W9HhRQaH2lYwJQoEFTw&gsessionid=Y9qOC8ZPI9wVdDf9Au-oDUZA3Ips2gCSXyLPQ1-UU0hLpofkKQzE7Q)  
  <sub>Stock Titan, 1 hour ago</sub>  
  The 7.6-inch inner screen puts team chat beside live AI work; IT controls participation, model choice and data access. Video and audio features are expected...
- [Indian Stock Market News, Equity Market and Sensex Today in India](https://www.google.com/goto?url=CAES9wEBxCJF14dVwHeQB0KCkOYlNS-bSizfAVSmWWYhdLDO4S8Gjr2bvgdM5IF7auNCZZgqBDpk32xjsP7AOmotBtfPm75r__qIeRzJWQ3p6jDbHc_ncBpubrd9g4LETkAKPH0FDd5qzpGvQpckKPR3hAVN0qBTFsdMV0VDo2A8ajCNx3aNu1k72J5wQEuIBMEu0Gi8YrfFYoGc-IDUQgJ85h9S4vE7VVRvtnOn0j1pwxjirUsPOyhN8550iD7Lfh3yvfbCBDuxuMpQ9R7qmZ5noBfK1Ea5C-xtckLpAd0Y2A2Lsb4hq8qrL8EE48C9pqk8Sl6oBwQRs1W4&gsessionid=Y9qOC8ZPI9wVdDf9Au-oDUZA3Ips2gCSXyLPQ1-UU0hLpofkKQzE7Q)  
  <sub>Equitymaster, 14 hours ago</sub>  
  Top cues to track in today's stock market session.
- [(QMAX) Optimized Trading Opportunities (QMAX:CA)](https://www.google.com/goto?url=CAESmwEBxCJF1yIwb-6ttEcoYbAbtc1QE4QWVQ_bckqF4UJhoetYVS0FP1bEDQyFQnijnX5Mz-9KnNe8716MsTCBazErhDSMKl17sz8VMAdimpt71b0xVxgQQxMIoaKJtbL6EzzZRHzIud6gyksbKnC4L_xiUBPTELGMg8xYrxM2WIyacCDT4EmmprhkrAjCYcrA25WqC2p-HSImE0InqQ&gsessionid=Y9qOC8ZPI9wVdDf9Au-oDUZA3Ips2gCSXyLPQ1-UU0hLpofkKQzE7Q)  
  <sub>Stock Traders Daily, 13 hours ago</sub>  
  Optimized Trading Opportunities for Hamilton Technology YIELD MAXIMIZER TM ETF (QMAX) with Buy and Sell Indicators.
- [A sale of enzymes that break down antibiotics could bring Theriva up to $91 million if targets are met](https://www.google.com/goto?url=CAESrwEBxCJF1_37hPJiNYJRNUH1HrivE07C-P65Ddu5QM_kLJDWl_Dd_7sm_gLBBgapqUNyV5rySA3pNvNnMiyZ4ZeKCCBXHVJ2bfmt0oDWjkjo37uCAN8apOAX8ns7WGXWA5gH9D-01oFmMK1lw8RlLXCySTxfpS8TAhKxTyAIPWMpUQfqwyi4jbFFeHAib2Cn8BzOEvKlqxhy_t_cFrJQl1VAkjDd_gCDN7ajgwZJM9Tw&gsessionid=Y9qOC8ZPI9wVdDf9Au-oDUZA3Ips2gCSXyLPQ1-UU0hLpofkKQzE7Q)  
  <sub>Stock Titan, 2 hours ago</sub>  
  The SYN-004 sale brought $350000 upfront; cash was $8.5 million at Sept. 30, with runway into Q1 2027. VIRAGE2 initial data are expected by Q3 2027.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>Price and chart</b> — score n/a</summary>

```text
Last close 212.49 (bar of 2026-11-12), from 502 daily bars
Trend: vs 20d SMA 201.89 (+5.2%), 50d 194.63 (+9.2%), 200d 197.99 (+7.3%); 50d below 200d
Momentum: RSI(14) 65.0 | MACD 6.248 vs signal 4.694 (histogram 1.555)
Returns: 1d -0.2% | 5d -2.6% | 1m +12.7% | 3m +11.2%
52-week range: 166.50 - 248.29 (now 56.2% of the way up)
Volatility: ATR(14) 4.36 (2.1% of price) | annualised 20d 38.3%
Volume: 0.05x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score n/a</summary>

```text
Sector: Consumer Cyclical / Auto Manufacturers | market cap 250.28B
Valuation: trailing P/E 9.69 | forward P/E 13.47 | P/B 16.91 | PEG n/a
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
Consensus: buy (mean 1.75 on a 1=strong buy to 5=strong sell scale, 4 analysts)
Ratings: 1 strong buy, 2 buy, 1 hold, 0 sell, 0 strong sell
Price target: mean 238.08 (+12.0% vs last close), range 230.00 - 253.00
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
Net: +0 shares | insiders hold 942,259 shares
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

### US government bonds, 20+ years (TLT) · Index fund — NEUTRAL, confidence 0.20

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Neutral stance given mixed signals: rising yields pressuring bond prices, large speculators net short 33% (slight bearish sentiment), price below short‑term and long‑term SMAs with no bullish breakout, and fund fundamentals unchanged.

**Main reasons it gave:**
- 10-year Treasury yield up 0.19% on the week, pressuring bond prices
- CFTC data shows large speculators net short 33% of open interest, slight increase
- Price below 20-day and 200-day SMA, RSI 47.4, no bullish breakout
- Fund basics unchanged: AA credit quality, modest 3-year return, low expense ratio

<details><summary><b>News</b> — score +0.00</summary>

- [Which Long-Term Bond ETF Is the Better Buy: State Street’s SPLB or iShares’ TLT?](https://www.fool.com/coverage/etfs/2026/11/11/which-long-term-bond-etf-is-the-better-buy-state-street-s-splb-or-ishares-tlt/)  
  <sub>The Motley Fool, 16 hours ago</sub>  
  The State Street SPDR Portfolio Long Term Corporate Bond ETF (SPLB +0.29%) offers lower costs and corporate credit exposure, while the iShares 20+ Year...
- [iShares 20+ Year Treasury Bond ETF (TLT) options chain](https://uk.finance.yahoo.com/quote/TLT/options/?date=1796342400&straddle=false&type=all)  
  <sub>Yahoo Finance UK, 16 hours ago</sub>  
  View the basic TLT option chain and compare options of iShares 20+ Year Treasury Bond ETF on Yahoo Finance.
- [TLTW: Recent Treasury Auctions Point To Rangebound Yields](https://www.google.com/goto?url=CAESngEBxCJF11u1HafWi6ovasAUrBiDCUcIUPwqfRu1o-vC1JyfuyyhdZlkJBpHdX_M2yR0W2kwnSN1is-4fkSoIRA8wUIRyispc5PypnoFuBtqa7I9yk4sqH0YEGZ3lQKVvLMB63IFdxUi1YXeeYKOYejjNz2a7gIg8dOMslYyxxHwcYseeBi9s2vaczmzdW0aZBf8TKOzadFB6u2nfdpQSA&gsessionid=DhXVUVO7oGHxWpydZKCz1rB7A63m5DCZcNjn1mUVcQnsE9LyUzRzAw)  
  <sub>Seeking Alpha, 19 hours ago</sub>  
  iShares TLT Premium Income+ ETF is a Strong Buy, as its 7.5%-8% real distribution yield tops TLT's 5.25% SEC yield with manageable downside risk.
- [The 2-Year Treasury Yield Just Had Its Biggest Jump in 19 Months](https://www.google.com/goto?url=CAESzQEBxCJF1-K6mnNiBUG3Sdc3eDjFX1AEHNh6pXCg7M2bMYzaSHrjRZyL1KZObPLRT6WHSllzuS-0cDc7BA4PMeB3HVB747tp6cu3hWG3VvU8g2LD69Z-VxH9VupbcIoY_wRFeSURS59O-N2RZ-NAkB44BvwSTLftM3Rbv_zPhDEc2jDr2SWZo-scoMZmJnqyqOLRt82j5-U5IQYyGEu6_VzAdEYZqrlo0kx9XnMKrT6eJ8qsu9FsrRbcG9YH1bCdev5oddBAnIxuGQ1W51cU&gsessionid=DhXVUVO7oGHxWpydZKCz1rB7A63m5DCZcNjn1mUVcQnsE9LyUzRzAw)  
  <sub>24/7 Wall St., 18 hours ago</sub>  
  The 2-year Treasury yield rose 17 basis points on Tuesday, November 10, 2026, closing at 4.73% after closing at 4.56% on Monday, November 9.
- [TLT Mar 2027 105.000 put (TLT270319P00105000) Seasonal Returns Chart](https://www.google.com/goto?url=CAESfwHEIkXX54rojheqX-BbCbbPn7n0GR-8Clh-qsOfGeblDilCp5qXX84x25n75HfqdV-gmpPBpzAo5D1cLkJI-SIAenPQwICKlTA6GyjSynwwzRZwZY5_NhfkYoe8Yxx8W302oBoCJsrqm3-xwa_05FcfOOeufYICalQlN1J-WLk&gsessionid=DhXVUVO7oGHxWpydZKCz1rB7A63m5DCZcNjn1mUVcQnsE9LyUzRzAw)  
  <sub>Yahoo! Finance Canada, 19 hours ago</sub>  
  TLT Mar 2027 105.000 put (TLT270319P00105000) seasonal returns chart provides the mean and median returns by month to inform your investment strategy.
- [TLT Dec 2026 76.000 call (TLT261211C00076000) Seasonal Returns Chart](https://www.google.com/goto?url=CAESfwHEIkXXYwX-e2QfT03DKCVO0oQMKsNJHxGrgkVgYL0sHH51E2hvnNjq1gGl8v1iYGYXO4_TWjIIultSWlxs0Ng1KH_Laq9e0QjNGP01LFBx6edfsutreae9g9FQlx8jgzsNcUG5Z5Kr-yO8NCeA33zIzmvR8KeLU2esh6PX018&gsessionid=DhXVUVO7oGHxWpydZKCz1rB7A63m5DCZcNjn1mUVcQnsE9LyUzRzAw)  
  <sub>Yahoo! Finance Canada, 18 hours ago</sub>  
  TLT Dec 2026 76.000 call (TLT261211C00076000) seasonal returns chart provides the mean and median returns by month to inform your investment strategy.
- [Top Tokenized ETFs by Market Cap](https://www.google.com/goto?url=CAESXgHEIkXXj03xkJNbR7R7shZkLyzbOzGwiP9M3OMMy5MDGNICd4nSbai6itsyC1hykn3z-3mrluvo3G1SqfypMxM_2SnH9PZvaU9tb5dP9Zh1jcg_LRD3f54DZIrUxNs&gsessionid=DhXVUVO7oGHxWpydZKCz1rB7A63m5DCZcNjn1mUVcQnsE9LyUzRzAw)  
  <sub>CoinGecko, 1 hour ago</sub>  
  Discover the top ETFs (exchange-traded funds) by tokenized market cap. Track ETF prices alongside their tokenized prices, market cap, and volume on...
- [Daily ETF Flows: $4B Flows Into SOXX](https://www.google.com/goto?url=CAESlwEBxCJF1z0mk_O2lprS1OODYcwAEsyOhs76XJkoQpZjHmdyja1OoPPqcV_rzNgIHLJEa0GprbB2FuAa4ceFBDaJhAx30T-eovO_uIzj7ylfDaLKYWmT2T5yjzhK9li7T325dTeX8wQIi-Bz5ArJPlCBDZrdZEQSIw2C56dR5pUBYZFGO0poiydKhoS0miw1qQGQcu4aLjQ1&gsessionid=DhXVUVO7oGHxWpydZKCz1rB7A63m5DCZcNjn1mUVcQnsE9LyUzRzAw)  
  <sub>Yahoo Finance, 15 hours ago</sub>  
  Top 10 Creations (All ETFs). Ticker. Name. Net Flows ($, mm). AUM ($, mm). AUM % Change. SOXX · iShares Semiconductor ETF. 3,976.38. 41,502.53. 9.58%.
- [Dow, S&P 500, Nasdaq Futures Mixed As Tech Rebounds Despite Nvidia CEO Crisis: AMD, CSCO, AMAT In Focus](https://www.google.com/goto?url=CAES5AEBxCJF1zwHbhS-x7xj5k8IiAtElXxPDxhMhGYnozFVkzcSc6xnIBGR28-tKm6W5iURgFfLl5EET0bWa5oGua1z9HVhirDq0b8aqE7bZTHrLEraGIkVF8LTlCmZ1HsmLGI10P4tnY45mZ54Pdh-C055hl-2tyJkjovouPiLaVmaHlgpmQQIQ5G1ySqpN_HTK1bolHhOBKRZKTfzZNXWY3VmNxpvXpgcnxfERTuv8upDo46jxNjsbPLjMhFFi2Y9QENR5X-kyhz6_6dJH9oL70EbovHyy6_rZsWRvyictRsU18vxniQ&gsessionid=DhXVUVO7oGHxWpydZKCz1rB7A63m5DCZcNjn1mUVcQnsE9LyUzRzAw)  
  <sub>Stocktwits, 11 hours ago</sub>  
  Media reports suggest that Nvidia's board is looking to replace CEO Jensen Huang after additional news indicated that he had an affair with a company...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.11% (+0.12 on the week) | 5-year 4.87% (+0.27 on the week) | 10-year 5.03% (+0.19 on the week) | 30-year 5.37% (+0.12 on the week)
Yield curve, 10-year minus 3-month: +0.92 points -- upward sloping (normal)
US dollar index: 102.91 (+1.36 on the week)
Volatility (VIX): 18.99 (-9.2 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.1% (2026-10-01) | jobless claims 200k (2026-11-07)
Policy and expectations: Fed target 4.00% | market expects 2.2% inflation over 10 years
Rate path: 2-year Treasury 4.56% vs Fed target 3.75-4.00% -- the bond market prices about 3 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 80.56 (bar of 2026-11-12), from 502 daily bars
Trend: vs 20d SMA 81.17 (-0.8%), 50d 80.28 (+0.3%), 200d 84.34 (-4.5%); 50d below 200d
Momentum: RSI(14) 47.4 | MACD 0.332 vs signal 0.430 (histogram -0.098)
Returns: 1d -0.4% | 5d -1.7% | 1m +2.1% | 3m -1.8%
52-week range: 77.11 - 90.82 (now 25.2% of the way up)
Volatility: ATR(14) 0.75 (0.9% of price) | annualised 20d 11.3%
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
Three-year record: +1.5% a year | beta to the market 2.30
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

<details><summary><b>Buying and selling by company insiders</b> — score -0.20</summary>

_Not available today._

</details>

<details><summary><b>Who is positioned how</b> — score -0.20</summary>

```text
Contract: ULTRA UST BOND - CHICAGO BOARD OF TRADE (positions as of 2026-11-03, published the following Friday)
Large speculators: net short 33.3% of open interest (2,394,358 contracts)
Change on the week: +1.1% of open interest
Crowding: 55% percentile over 52 weeks -- within its normal range
Read this as crowding, not as a forecast: an extreme is as often the end of a move as the middle of one.
```

</details>

<details><summary><b>Money going into and out of this fund</b> — score -0.20</summary>

```text
Direction: flat (1 month)
Share count change: 1 week: +0.0% (0.00) over 7d | 1 month: +0.0% (0.00) over 30d
Shares outstanding: 109.70M | fund size: 8.84B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Farm goods basket (DBA) · Index fund — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Neutral call due to flat fund flows, no macro surprise, technicals showing downtrend without decisive break, and lack of analyst coverage.

**Main reasons it gave:**
- Fund flows flat: 0% share count change over 1 week and 1 month
- Macro unchanged: yields up modestly, dollar +1.36% on week, inflation 3.7% (no surprise)
- Technical downtrend: price below 20‑day SMA (27.09) and 50‑day SMA (27.98), RSI 25.2, low volume (0.03× 20‑day avg)
- Analyst coverage missing: no ratings, analyst_score null

<details><summary><b>News</b> — score +0.00</summary>

_No news found for this one today._

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.11% (+0.12 on the week) | 5-year 4.87% (+0.27 on the week) | 10-year 5.03% (+0.19 on the week) | 30-year 5.37% (+0.12 on the week)
Yield curve, 10-year minus 3-month: +0.92 points -- upward sloping (normal)
US dollar index: 102.91 (+1.36 on the week)
Volatility (VIX): 18.99 (-9.2 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.1% (2026-10-01) | jobless claims 200k (2026-11-07)
Policy and expectations: Fed target 4.00% | market expects 2.2% inflation over 10 years
Rate path: 2-year Treasury 4.56% vs Fed target 3.75-4.00% -- the bond market prices about 3 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score -0.10</summary>

```text
Last close 26.30 (bar of 2026-11-12), from 502 daily bars
Trend: vs 20d SMA 27.09 (-2.9%), 50d 27.98 (-6.0%), 200d 27.40 (-4.0%); 50d above 200d
Momentum: RSI(14) 25.2 | MACD -0.545 vs signal -0.494 (histogram -0.051)
Returns: 1d -0.2% | 5d +0.5% | 1m -6.9% | 3m -5.3%
52-week range: 25.44 - 29.49 (now 21.2% of the way up)
Volatility: ATR(14) 0.24 (0.9% of price) | annualised 20d 8.0%
Volume: 0.03x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.20</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score +0.20</summary>

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
Shares outstanding: 27.60M | fund size: 725.88M
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Commodities basket (DBC) · Index fund — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Mixed fundamentals and strong inflows offset each other, with no macro surprise or decisive technical break, leading to a neutral stance.

**Main reasons it gave:**
- Share count up 11.6% in 1 week (strong inflows)
- EIA forecasts WTI price down 13% over 6 months (bearish)
- Crude oil inventories draw 0.9M barrels (10th percentile) bullish
- RSI 28.8 (oversold) but MACD negative, no decisive technical break
- No macro surprise in rates or data

<details><summary><b>News</b> — score +0.00</summary>

- [商品指数ETF-PowerShares DB收涨0.26%，成交额2415.01万美元](http://www.bing.com/news/apiclick.aspx?ref=FexRss&aid=&tid=6af5d127e50c40e789a9c791c1126e06&url=https%3a%2f%2ffinance.sina.com.cn%2fstock%2fusstock%2fnotice%2f2026-11-12%2fdoc-iniymmzq8659032.shtml&c=3662575638738826082&mkt=en-us)  
  <sub>新浪财经, 23h ago</sub>  
  11月12日，商品指数ETF-PowerShares DB（DBC）收涨0.26%，报30.84美元，成交额2415.01万美元，市值17.59亿美元。 声明：市场有风险，投资需谨慎。本文基于第三方数据库发布，不代表新浪财经观点，任何在本文出现的信息均只作为参考，不构成个人投资建议。如有出入请以实际公告为准。如有疑问，请联系biz@staff.sina.com.cn。

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.11% (+0.12 on the week) | 5-year 4.87% (+0.27 on the week) | 10-year 5.03% (+0.19 on the week) | 30-year 5.37% (+0.12 on the week)
Yield curve, 10-year minus 3-month: +0.92 points -- upward sloping (normal)
US dollar index: 102.91 (+1.36 on the week)
Volatility (VIX): 18.99 (-9.2 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.1% (2026-10-01) | jobless claims 200k (2026-11-07)
Policy and expectations: Fed target 4.00% | market expects 2.2% inflation over 10 years
Rate path: 2-year Treasury 4.56% vs Fed target 3.75-4.00% -- the bond market prices about 3 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 30.70 (bar of 2026-11-12), from 502 daily bars
Trend: vs 20d SMA 32.66 (-6.0%), 50d 32.75 (-6.3%), 200d 29.57 (+3.8%); 50d above 200d
Momentum: RSI(14) 28.8 | MACD -0.563 vs signal -0.253 (histogram -0.311)
Returns: 1d -0.5% | 5d -2.4% | 1m -7.8% | 3m +2.3%
52-week range: 22.36 - 34.10 (now 71.0% of the way up)
Volatility: ATR(14) 0.51 (1.6% of price) | annualised 20d 20.4%
Volume: 0.04x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score -0.20</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score -0.20</summary>

```text
Fund type: Commodities Broad Basket
What it holds: P/E n/a | P/B 0.00 | P/S 0.00 | 3y earnings growth n/a
Yield: 2.2%
Three-year record: +13.5% a year | beta to the market 1.04
Cost and size: expense ratio 0.85% | net assets 1.94B
What it is made of: Other 50.0%, Cash 45.2%, Bonds 2.7%, Stocks 2.1%
Largest holdings: Invesco Shrt-Trm Inv Gov&Agcy Instl 41.8%, Brent Crude Future Jan 27 11.0%, Invesco Short Term Treasury ETF 5.8%, Mini Ibovespa Future Dec 26 2.1%
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
US inventories, week ending 2026-10-30 (published the following Wednesday)
  Crude oil: 409.8 million barrels, -0.9 on the week (a draw), 10% percentile over 52 weeks -- low for the time of year
  Natural gas: 3,801.0 billion cubic feet, +77.0 on the week (a build), 92% percentile over 52 weeks -- high for the time of year
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
Share count change: 1 week: +11.6% (201.99M) over 9d | 1 month: +9.3% (166.16M) over 30d
Shares outstanding: 63.36M | fund size: 1.95B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Developing country bonds (EMB) · Index fund — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Neutral – no material macro surprise, technicals are mixed, and fund flows are modestly positive but not decisive.

**Main reasons it gave:**
- Share count increased 4.4% week over week (positive fund flows)
- Yield curve upward sloping (+0.92 points), no inversion
- Price below 20‑day, 50‑day, and 200‑day SMAs; RSI 47.7 (neutral momentum)
- 10‑year Treasury yield up 0.19% week, dollar index up 1.36% week

<details><summary><b>News</b> — score +0.00</summary>

- [EMB.IV:IND - iShares JP Morgan USD Emerging Markets Bond ETF Intraday](http://www.bing.com/news/apiclick.aspx?ref=FexRss&aid=&tid=6af5d118d5f843db9ea990313e5298ff&url=https%3a%2f%2fseekingalpha.com%2fsymbol%2fEMB.IV%3aIND&c=3875407947087937905&mkt=en-us)  
  <sub>Seeking Alpha, 31h ago</sub>  
  A high-level overview of iShares JP Morgan USD Emerging Markets Bond ETF Intraday (EMB.IV:IND) stock. View (EMB.IV:IND) real-time stock price, chart, news, analysis, analyst reviews and more.
- [iShares J.P. Morgan USD Emerging Markets Bond ETF](http://www.bing.com/news/apiclick.aspx?ref=FexRss&aid=&tid=6af5d118d5f843db9ea990313e5298ff&url=https%3a%2f%2fmarkets.ft.com%2fdata%2fetfs%2ftearsheet%2fsummary%3fs%3dEMB%3aNMQ%3aUSD&c=14444127834652429199&mkt=en-us)  
  <sub>Financial Times, 31h ago</sub>  
  The investment seeks to track the investment results of the J.P. Morgan Emerging Markets Bond Index Global Diversified Core composed of U.S. dollar-denominated, emerging market bonds. The fund will ...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.11% (+0.12 on the week) | 5-year 4.87% (+0.27 on the week) | 10-year 5.03% (+0.19 on the week) | 30-year 5.37% (+0.12 on the week)
Yield curve, 10-year minus 3-month: +0.92 points -- upward sloping (normal)
US dollar index: 102.91 (+1.36 on the week)
Volatility (VIX): 18.99 (-9.2 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.1% (2026-10-01) | jobless claims 200k (2026-11-07)
Policy and expectations: Fed target 4.00% | market expects 2.2% inflation over 10 years
Rate path: 2-year Treasury 4.56% vs Fed target 3.75-4.00% -- the bond market prices about 3 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 91.72 (bar of 2026-11-12), from 502 daily bars
Trend: vs 20d SMA 91.81 (-0.1%), 50d 92.09 (-0.4%), 200d 94.76 (-3.2%); 50d below 200d
Momentum: RSI(14) 47.7 | MACD 0.028 vs signal -0.024 (histogram 0.052)
Returns: 1d -0.4% | 5d -0.3% | 1m +0.6% | 3m -3.5%
52-week range: 90.14 - 97.74 (now 20.9% of the way up)
Volatility: ATR(14) 0.49 (0.5% of price) | annualised 20d 6.9%
Volume: 0.09x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.00</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score +0.00</summary>

```text
Fund type: Emerging Markets Bond
Yield: 5.4%
Credit quality: BBB 33.5%, BB 25.3%, B 19.5%, A 17.7% | US government debt 87.8%
Three-year record: +9.2% a year | beta to the market 1.06
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

<details><summary><b>Buying and selling by company insiders</b> — score +0.00</summary>

_Not available today._

</details>

<details><summary><b>Who is positioned how</b> — score +0.00</summary>

_Not available today._

</details>

<details><summary><b>Money going into and out of this fund</b> — score +0.00</summary>

```text
Direction: money coming in (1 month)
Share count change: 1 week: +4.4% (573.03M) over 7d | 1 month: +3.7% (488.30M) over 30d
Shares outstanding: 147.60M | fund size: 13.54B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### US company bonds, riskier (HYG) · Index fund — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Most macro and technical indicators are mixed: rising Treasury yields suggest pressure on high‑yield spreads, but strong net inflows show demand for the ETF, while price remains below key moving averages with low volume, offering no clear bullish or bearish breakout.

**Main reasons it gave:**
- Treasury yields rose across the curve (+0.12 to +0.27) indicating higher rates that could pressure high‑yield spreads
- Fund experienced strong net inflows (+5.7% share count increase in 1 week, +5.5% in 1 month) showing demand for high‑yield exposure
- Technicals show price below 20‑day, 50‑day and 200‑day SMAs with low volume, indicating lack of bullish momentum

<details><summary><b>News</b> — score +0.00</summary>

- [iShares Interest Rate Hedged High Yield Bond ETF](http://www.bing.com/news/apiclick.aspx?ref=FexRss&aid=&tid=6af5d108d9ce4615ba3427840b814a49&url=https%3a%2f%2fmarkets.ft.com%2fdata%2fetfs%2ftearsheet%2fsummary%3fs%3dHYGH%3aNYS&c=14268048453760237085&mkt=en-us)  
  <sub>Financial Times, 27h ago</sub>  
  The investment seeks to track the investment results of the BlackRock Interest Rate Hedged High Yield Bond Index designed to mitigate the interest rate risk of a portfolio composed of U.S. dollar- ...
- [债券指数ETF-iShares iBoxx高收益公司债收涨0.22%，成交额10.37亿美元](http://www.bing.com/news/apiclick.aspx?ref=FexRss&aid=&tid=6af5d108d9ce4615ba3427840b814a49&url=https%3a%2f%2ffinance.sina.com.cn%2fstock%2fusstock%2fnotice%2f2026-11-12%2fdoc-iniymmzp1866064.shtml&c=8052371745990327689&mkt=en-us)  
  <sub>新浪财经, 23h ago</sub>  
  11月12日，债券指数ETF-iShares iBoxx高收益公司债（HYG）收涨0.22%，报77.35美元，成交额10.37亿美元，市值184.17亿美元。 声明：市场有风险，投资需谨慎。本文基于第三方数据库发布，不代表新浪财经观点，任何在本文出现的信息均只作为参考，不构成个人投资建议。如有出入请以实际公告为准。如有疑问，请联系biz@staff.sina.com.cn。

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.11% (+0.12 on the week) | 5-year 4.87% (+0.27 on the week) | 10-year 5.03% (+0.19 on the week) | 30-year 5.37% (+0.12 on the week)
Yield curve, 10-year minus 3-month: +0.92 points -- upward sloping (normal)
US dollar index: 102.91 (+1.36 on the week)
Volatility (VIX): 18.99 (-9.2 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.1% (2026-10-01) | jobless claims 200k (2026-11-07)
Policy and expectations: Fed target 4.00% | market expects 2.2% inflation over 10 years
Rate path: 2-year Treasury 4.56% vs Fed target 3.75-4.00% -- the bond market prices about 3 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 77.17 (bar of 2026-11-12), from 502 daily bars
Trend: vs 20d SMA 77.21 (-0.1%), 50d 77.63 (-0.6%), 200d 79.35 (-2.8%); 50d below 200d
Momentum: RSI(14) 46.3 | MACD -0.077 vs signal -0.119 (histogram 0.042)
Returns: 1d -0.2% | 5d -0.1% | 1m +0.5% | 3m -3.2%
52-week range: 76.81 - 81.18 (now 8.1% of the way up)
Volatility: ATR(14) 0.32 (0.4% of price) | annualised 20d 5.2%
Volume: 0.03x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.10</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score +0.10</summary>

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

<details><summary><b>Buying and selling by company insiders</b> — score +0.40</summary>

_Not available today._

</details>

<details><summary><b>Who is positioned how</b> — score +0.40</summary>

_Not available today._

</details>

<details><summary><b>Money going into and out of this fund</b> — score +0.40</summary>

```text
Direction: money coming in (1 month)
Share count change: 1 week: +5.7% (961.21M) over 9d | 1 month: +5.5% (929.96M) over 30d
Shares outstanding: 229.87M | fund size: 17.74B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### US government bonds, 7-10 years (IEF) · Index fund — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:** no explanation. It wrote only “NEUTRAL”, so the main reasons below are all it gave.

**Main reasons it gave:**
- 2-year Treasury yield jumped 17 bps to 4.73%, biggest rise in 19 months
- Large speculators net short 38% of open interest, slight weekly decrease of -0.2%
- IEF share count rose 5.5% over the past week, indicating inflows
- Price below 200‑day SMA (93.66) and RSI at 45.7, showing modest bearish technicals

<details><summary><b>News</b> — score +0.00</summary>

- [Discipline and Rules-Based Execution in IEF Response](https://news.stocktradersdaily.com/news_release/12/Discipline_and_Rules-Based_Execution_in_IEF_Response_111126095602_1794452162.html)  
  <sub>Stock Traders Daily, 17 hours ago</sub>  
  Price-action only: Ishares 7-10 Year Treasury Bond Etf (IEF) movements set the tone for institutional models. Discipline and Rules-Based Execution in IEF...
- [The 2-Year Treasury Yield Just Had Its Biggest Jump in 19 Months](https://247wallst.com/investing/2026/11/11/the-2-year-treasury-yield-just-had-its-biggest-jump-in-19-months/?tpid=1702334&tv=link&tc=in_content)  
  <sub>24/7 Wall St., 18 hours ago</sub>  
  The 2-year Treasury yield rose 17 basis points on Tuesday, November 10, 2026, closing at 4.73% after closing at 4.56% on Monday, November 9.
- [SWC (CH) IPF I IEF USA Resp NT USD (0P0001PYAM) Seasonal Returns Chart](https://www.google.com/goto?url=CAESdwHEIkXXrecY5E4Gbd9Z9khbjexRux4LvZlCquIqqfW0ClcIDWiYZGdPJ_wen33iVZDZ0yi6wqFtS8ElJNm33miHZpOrS3wuqxxr2sLRjYZBTVQ2TOPHd6QEhJo1zkRSWftXgepzt1pVvsYEseC2B0Z4rrwvBY5y&gsessionid=0_Cv3MU3Rz6rpQEg4Dlm25jmkLoFGX5Iq4lFGildSEqT904v3QJPog)  
  <sub>Yahoo! Finance Canada, 22 hours ago</sub>  
  SWC (CH) IPF I IEF USA Resp NT USD (0P0001PYAM) seasonal returns chart provides the mean and median returns by month to inform your investment strategy.
- [The Bond Rally Faces a Reality Check](https://www.google.com/goto?url=CAESjQEBxCJF14FN72J-TGROVZgjsr9MMz7i9ayszXKGyivRsXrsxuxqp9um7BxqAf5hZ3d1nKyftj1WdzZ3fXD4Ohe3ljcJif277dzKWnWdC0XInpPaPuBOk8r9o5liHs2DdX9MGmzi_Ve0wKlTwUt8WI555unFOAv6c_WPU3iOJmlAu7k0jmo9LNn8elN6P7g&gsessionid=0_Cv3MU3Rz6rpQEg4Dlm25jmkLoFGX5Iq4lFGildSEqT904v3QJPog)  
  <sub>Investing.com UK, 51 minutes ago</sub>  
  Market Analysis by James Picerno covering: Vanguard Total Bond Market Index Fund ETF Shares, iShares 1-3 Year Treasury Bond ETF, iShares 7-10 Year Treasury...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.11% (+0.12 on the week) | 5-year 4.87% (+0.27 on the week) | 10-year 5.03% (+0.19 on the week) | 30-year 5.37% (+0.12 on the week)
Yield curve, 10-year minus 3-month: +0.92 points -- upward sloping (normal)
US dollar index: 102.91 (+1.36 on the week)
Volatility (VIX): 18.99 (-9.2 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.1% (2026-10-01) | jobless claims 200k (2026-11-07)
Policy and expectations: Fed target 4.00% | market expects 2.2% inflation over 10 years
Rate path: 2-year Treasury 4.56% vs Fed target 3.75-4.00% -- the bond market prices about 3 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 90.65 (bar of 2026-11-12), from 502 daily bars
Trend: vs 20d SMA 91.09 (-0.5%), 50d 90.62 (+0.0%), 200d 93.66 (-3.2%); 50d below 200d
Momentum: RSI(14) 45.7 | MACD 0.201 vs signal 0.253 (histogram -0.052)
Returns: 1d -0.3% | 5d -1.4% | 1m +1.1% | 3m -2.6%
52-week range: 88.92 - 97.99 (now 19.1% of the way up)
Volatility: ATR(14) 0.47 (0.5% of price) | annualised 20d 6.8%
Volume: 0.03x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.20</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score +0.20</summary>

```text
Fund type: Long Government
Yield: 4.0%
Credit quality: AA 100.0% | US government debt 99.6%
Three-year record: +3.7% a year | beta to the market 1.17
Cost and size: expense ratio 0.15% | net assets 43.53B
What it is made of: Bonds 99.6%, Cash 0.4%
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
Share count change: 1 week: +5.5% (2.28B) over 9d | 1 month: +2.8% (1.19B) over 30d
Shares outstanding: 478.29M | fund size: 43.36B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### US small companies (IWM) · Index fund — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:** no explanation. It wrote only “NEUTRAL”, so the main reasons below are all it gave.

**Main reasons it gave:**
- Net short positions fell 1.8% of open interest (insider_score modestly bullish)
- Analyst coverage thin (1.9% weight) but all buy with +20.8% price target (analyst_score modest)
- Fund fundamentals solid: P/E 16.28, 3-year return +19.7% (fundamental_score positive)
- Technicals show price near 20‑day SMA, low volume, no decisive break (neutral)
- Large net outflow of $367.5M on Tuesday (negative sentiment)

<details><summary><b>News</b> — score +0.00</summary>

- [What iShares Russell 2000 (IWM) Sold: Glaukos Leads on Nov. 10](http://www.bing.com/news/apiclick.aspx?ref=FexRss&aid=&tid=6af5d0b56ea44ffe8a87f1f4f47f365b&url=https%3a%2f%2ffinance.yahoo.com%2fmarkets%2fstocks%2farticles%2fishares-russell-2000-iwm-sold-110501746.html&c=252350367464461273&mkt=en-us)  
  <sub>Yahoo Finance, 12h ago</sub>  
  iShares Russell 2000 Index Fund ( IWM) posted a net outflow of $367.5 million in Tuesday's session, with $367.5 million in gross ETF activity all on the sell side. IWM increased 0 positions and ...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.11% (+0.12 on the week) | 5-year 4.87% (+0.27 on the week) | 10-year 5.03% (+0.19 on the week) | 30-year 5.37% (+0.12 on the week)
Yield curve, 10-year minus 3-month: +0.92 points -- upward sloping (normal)
US dollar index: 102.91 (+1.36 on the week)
Volatility (VIX): 18.99 (-9.2 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.1% (2026-10-01) | jobless claims 200k (2026-11-07)
Policy and expectations: Fed target 4.00% | market expects 2.2% inflation over 10 years
Rate path: 2-year Treasury 4.56% vs Fed target 3.75-4.00% -- the bond market prices about 3 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 280.46 (bar of 2026-11-12), from 502 daily bars
Trend: vs 20d SMA 278.12 (+0.8%), 50d 281.16 (-0.2%), 200d 279.35 (+0.4%); 50d above 200d
Momentum: RSI(14) 51.0 | MACD -0.004 vs signal -0.671 (histogram 0.667)
Returns: 1d -0.9% | 5d +3.5% | 1m +3.3% | 3m -8.1%
52-week range: 229.11 - 305.09 (now 67.6% of the way up)
Volatility: ATR(14) 4.73 (1.7% of price) | annualised 20d 25.2%
Volume: 0.10x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.30</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score +0.30</summary>

```text
Fund type: Small Blend
What it holds: P/E 16.28 | P/B 1.99 | P/S 1.23 | 3y earnings growth n/a
Yield: 1.0%
Three-year record: +19.7% a year | beta to the market 1.26
Cost and size: expense ratio 0.19% | net assets 75.49B
What it is made of: Stocks 99.8%, Cash 0.2%
Largest holdings: Glaukos Corp 0.5%, BrightSpring Health Services Inc 0.4%, JFrog Ltd Ordinary Shares 0.3%, Twist Bioscience Corp 0.3%, Moog Inc Class A 0.3%
Sector mix: Healthcare 21.0%, Financial services 18.2%, Technology 14.0%, Industrials 12.7%
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

<details><summary><b>What analysts and big funds say</b> — score +0.20</summary>

_Not available today._

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score +0.20</summary>

```text
Rolled up from the 5 largest holdings, 1.9% of the fund by weight  -- thin, so read this as a fact about that slice rather than the fund
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 1.45 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +20.8% above the current prices
Holdings read: GKOS, BTSG, FROG, TWST, MOG-A
Recent rating changes among them:
  - GKOS: 2026-10-29 HC Wainwright & Co.: main, Buy -> Buy
  - BTSG: 2026-11-03 Guggenheim: main, Buy -> Buy
  - FROG: 2026-11-12 Morgan Stanley: main, Equal-Weight -> Equal-Weight
  - TWST: 2026-10-13 TD Cowen: main, Buy -> Buy
  - MOG-A: 2026-10-13 JP Morgan: main, Overweight -> Overweight
```

</details>

<details><summary><b>Buying and selling by company insiders</b> — score +0.15</summary>

_Not available today._

</details>

<details><summary><b>Who is positioned how</b> — score +0.15</summary>

```text
Contract: RUSSELL E-MINI - CHICAGO MERCANTILE EXCHANGE (positions as of 2026-11-03, published the following Friday)
Large speculators: net short 12.3% of open interest (449,399 contracts)
Change on the week: -1.8% of open interest
Crowding: 67% percentile over 52 weeks -- within its normal range
Read this as crowding, not as a forecast: an extreme is as often the end of a move as the middle of one.
```

</details>

<details><summary><b>Money going into and out of this fund</b> — score +0.15</summary>

```text
Direction: flat (1 month)
Share count change: 1 week: +0.0% (0.00) over 7d | 1 month: +0.0% (0.00) over 30d
Shares outstanding: 281.05M | fund size: 78.82B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### US company bonds, safer (LQD) · Index fund — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> The macro backdrop shows higher yields and inflation above the Fed target, which is bearish for corporate bonds, while technicals indicate a downtrend with weak momentum. However, strong inflows (13.6% share count increase in a week) suggest bullish demand. The mixed signals lead to a neutral overall stance.

**Main reasons it gave:**
- US Treasury yields rose across the curve (+0.12 to +0.27) indicating higher rates
- LQD price below 20‑day, 50‑day and 200‑day SMAs (103.61 vs 103.95/103.72/107.39) showing a downtrend
- Share count up 13.6% in the past week (3.83B) reflecting strong inflows
- RSI at 46.6 and MACD histogram -0.014 indicate weak momentum

<details><summary><b>News</b> — score +0.00</summary>

- [iShares Inflation Hedged Corporate Bond ETF](http://www.bing.com/news/apiclick.aspx?ref=FexRss&aid=&tid=6af5d0f351184526880c23ee5bd15607&url=https%3a%2f%2fmarkets.ft.com%2fdata%2fetfs%2ftearsheet%2fsummary%3fs%3dLQDI%3aNYS&c=14029472308531570695&mkt=en-us)  
  <sub>FT Markets, 26h ago</sub>  
  Pricing for ETFs is the latest price and not "real time". Share price information may be rounded up/down and therefore not entirely accurate. FT is not responsible for any use of content by you ...
- [债券指数ETF-iShares iBoxx投资级公司债收涨0.08%，成交额9.01亿美元](http://www.bing.com/news/apiclick.aspx?ref=FexRss&aid=&tid=6af5d0f351184526880c23ee5bd15607&url=https%3a%2f%2ffinance.sina.com.cn%2fstock%2fusstock%2fnotice%2f2026-11-12%2fdoc-iniymmzq8640571.shtml&c=3707958024606185534&mkt=en-us)  
  <sub>新浪财经, 23h ago</sub>  
  11月12日，债券指数ETF-iShares iBoxx投资级公司债（LQD）收涨0.08%，报103.96美元，成交额9.01亿美元，市值329.97亿美元。 声明：市场有风险，投资需谨慎。本文基于第三方数据库发布，不代表新浪财经观点，任何在本文出现的信息均只作为参考，不构成个人投资建议。如有出入请以实际公告为准。如有疑问，请联系biz@staff.sina.com.cn。

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.11% (+0.12 on the week) | 5-year 4.87% (+0.27 on the week) | 10-year 5.03% (+0.19 on the week) | 30-year 5.37% (+0.12 on the week)
Yield curve, 10-year minus 3-month: +0.92 points -- upward sloping (normal)
US dollar index: 102.91 (+1.36 on the week)
Volatility (VIX): 18.99 (-9.2 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.1% (2026-10-01) | jobless claims 200k (2026-11-07)
Policy and expectations: Fed target 4.00% | market expects 2.2% inflation over 10 years
Rate path: 2-year Treasury 4.56% vs Fed target 3.75-4.00% -- the bond market prices about 3 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score -0.20</summary>

```text
Last close 103.61 (bar of 2026-11-12), from 502 daily bars
Trend: vs 20d SMA 103.95 (-0.3%), 50d 103.72 (-0.1%), 200d 107.39 (-3.5%); 50d below 200d
Momentum: RSI(14) 46.6 | MACD 0.143 vs signal 0.157 (histogram -0.014)
Returns: 1d -0.3% | 5d -1.0% | 1m +0.9% | 3m -2.4%
52-week range: 101.83 - 112.05 (now 17.5% of the way up)
Volatility: ATR(14) 0.58 (0.6% of price) | annualised 20d 6.7%
Volume: 0.05x the 20-day average
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
Three-year record: +5.2% a year | beta to the market 1.32
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

<details><summary><b>Buying and selling by company insiders</b> — score +0.50</summary>

_Not available today._

</details>

<details><summary><b>Who is positioned how</b> — score +0.50</summary>

_Not available today._

</details>

<details><summary><b>Money going into and out of this fund</b> — score +0.50</summary>

```text
Direction: money coming in (1 month)
Share count change: 1 week: +13.6% (3.83B) over 9d | 1 month: +11.6% (3.33B) over 30d
Shares outstanding: 308.37M | fund size: 31.95B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### S&P 500, equal weight (RSP) · Index fund — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Neutral stance as no material macro surprise, no decisive technical break, and mixed signals from analyst, insider, and fundamentals.

**Main reasons it gave:**
- Large speculators net short 18.7% of open interest, up 1.7% week over week (bearish)
- Fund share count rose 3.6% in one week, indicating inflows (bullish)
- Analyst price target for top holdings is 8.4% below current price (bearish)
- Price above 200‑day SMA but volume only 7% of 20‑day average (neutral)
- No macro surprise; yields modestly higher, VIX down but still elevated (neutral)

<details><summary><b>News</b> — score +0.00</summary>

- [What Invesco S&P 500 Equal Weight ETF (RSP) Bought: Moderna Leads on Nov. 10](https://finance.yahoo.com/markets/stocks/articles/invesco-p-500-equal-weight-110426545.html)  
  <sub>Yahoo Finance, 4 hours ago</sub>  
  This article first appeared on GuruFocus. Invesco S&P 500 Equal Weight ETF (RSP) was the single fund that moved the most in Tuesday's session,...
- [RSPS: Consumer Staples ETF Reduces Company Risk (NYSEARCA:RSPS)](https://seekingalpha.com/article/4966643-rsps-consumer-staples-etf-reduces-company-risk)  
  <sub>Seeking Alpha, 17 hours ago</sub>  
  The Invesco S&P 500 Equal Weight Consumer Staples ETF offers equal-weight exposure to 33 consumer staples stocks. Discover more about the RSPS fund here.
- [Options Whale Alert: $531K Bullish Short Put Opened on $RSP](https://www.google.com/goto?url=CAESoQEBxCJF1ylQQ_3mYweaT8FtdTCGW-qfi7kbxGDoWUvPSvGw8dvU7HZVngJqASeEinVuIKDfRcDogF4WX7OTJYw6Dt0LHfxxyD7R3_YKEaSNb0jelz1RdMIROCipetRBcdgIfqXke-zOEk4pLOh_45B-t2zblKRzfls7lRqZyp-lcMtDCGYV7sfwpcAyMB7NREuF64MCIUsk9K2H8nn97YJQSg&gsessionid=G_b3zc4AE84vzGplUDgDwGGBBtCSRrtJVaZPinYbQ83C4d7F_mKZuQ)  
  <sub>Moomoo, 15 hours ago</sub>  
  InvescoExchange Traded Fd Tr S&P 500 Equal Weight Etf(RSP.US)$ closed up 0.80% at $222.65. A trader sold 1800 Dec 11, 2026 $222.50 puts to open a Short Put.
- [AKRE: Worth A Look, But Concentration And Factor Risks Remain](https://www.google.com/goto?url=CAESrAEBxCJF15FBJ9Y1GuI3jTAIZnv-Xy8ZE5LYZtJ8xg1WOdtUYB2bLi3sgCeccIhvX4N3irZxLQq6R35czR4h11ypejtN74s-0slv1c2lbtOGaf8RJuOILyCx8ll9pvjfKQAbr3YehBvutisAIUOK2KSesHUVS8cSAR6AbTzRA4SgTJ0uoqrIWGyKwr3Vq6J3Rdd-dhHJ8U5DPPysGcrt7t_-J_5-iENdL37ytDYj&gsessionid=G_b3zc4AE84vzGplUDgDwGGBBtCSRrtJVaZPinYbQ83C4d7F_mKZuQ)  
  <sub>Seeking Alpha, 12 hours ago</sub>  
  Akre Focus ETF is rated a Hold. AKRE's active return vs. IVV was -21.4% from November 2025 to October 2026. Read here for a detailed analysis.
- [Pacer US Cash Cows Growth ETF (BUL) Stock Price, News, Quote & History](https://www.google.com/goto?url=CAESZAHEIkXX5k8ot12xED_u78rhku1FpMxyb5bLFlv3YXfjfZMnUamiT5axwpQ7QPKHLzocHJFsXh92nt7rLglIiCmiLYe84zinyMmNfUUilQQdECNsm7rOtT_ITx8WD7BV4sabzGM&gsessionid=G_b3zc4AE84vzGplUDgDwGGBBtCSRrtJVaZPinYbQ83C4d7F_mKZuQ)  
  <sub>Yahoo! Finance Canada, 10 minutes ago</sub>  
  Find the latest Pacer US Cash Cows Growth ETF (BUL) stock quote, history, news and other vital information to help you with your stock trading and...
- [Is Invesco S&P MidCap 400 Pure Growth ETF (RFG) a Strong ETF Right Now?](https://www.google.com/goto?url=CAESlwEBxCJF1xoC7DwIziyMhmk5-DiuybdHuSq24NZa8JAqEDYNHOWmjX7oQ3LBinU6rsXS_jt7aIxT8hVHlamILSkOnth7gpqNil03aXL8L7pGr_y2EszNl70poctW15BcF2YzpNPK4rRVW9JlZ0nptIJ2Kq1U1WBTF6KyenKCzCVJ2-YfFi5FhPmExzYymscwmq5I2SvMoHAL&gsessionid=G_b3zc4AE84vzGplUDgDwGGBBtCSRrtJVaZPinYbQ83C4d7F_mKZuQ)  
  <sub>Yahoo Finance, 18 hours ago</sub>  
  Designed to provide broad exposure to the Style Box - Mid Cap Growth category of the market, the Invesco S&P MidCap 400 Pure Growth ETF (RFG) is a smart...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.11% (+0.12 on the week) | 5-year 4.87% (+0.27 on the week) | 10-year 5.03% (+0.19 on the week) | 30-year 5.37% (+0.12 on the week)
Yield curve, 10-year minus 3-month: +0.92 points -- upward sloping (normal)
US dollar index: 102.91 (+1.36 on the week)
Volatility (VIX): 18.99 (-9.2 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.1% (2026-10-01) | jobless claims 200k (2026-11-07)
Policy and expectations: Fed target 4.00% | market expects 2.2% inflation over 10 years
Rate path: 2-year Treasury 4.56% vs Fed target 3.75-4.00% -- the bond market prices about 3 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 222.00 (bar of 2026-11-12), from 502 daily bars
Trend: vs 20d SMA 218.37 (+1.7%), 50d 214.99 (+3.3%), 200d 208.75 (+6.3%); 50d above 200d
Momentum: RSI(14) 59.5 | MACD 1.878 vs signal 1.574 (histogram 0.304)
Returns: 1d -0.3% | 5d +2.4% | 1m +4.7% | 3m -0.3%
52-week range: 182.18 - 223.33 (now 96.8% of the way up)
Volatility: ATR(14) 2.64 (1.2% of price) | annualised 20d 17.5%
Volume: 0.07x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.20</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score +0.20</summary>

```text
Fund type: Large Blend
What it holds: P/E 19.93 | P/B 2.93 | P/S 1.83 | 3y earnings growth n/a
Yield: 1.5%
Three-year record: +18.1% a year | beta to the market 0.80
Cost and size: expense ratio 0.20% | net assets 100.66B
What it is made of: Stocks 99.8%, Cash 0.2%
Largest holdings: Moderna Inc 0.3%, PTC Inc 0.3%, Accenture PLC Class A 0.3%, Gartner Inc 0.3%, Hasbro Inc 0.3%
Sector mix: Technology 16.9%, Industrials 15.1%, Financial services 13.9%, Healthcare 12.9%
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

<details><summary><b>What analysts and big funds say</b> — score -0.10</summary>

_Not available today._

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score -0.10</summary>

```text
Rolled up from the 5 largest holdings, 1.4% of the fund by weight  -- thin, so read this as a fact about that slice rather than the fund
Ratings by weight: buy 38.4% | hold 61.6% | sell 0.0% (mean 2.57 on a 1=strong buy to 5=strong sell scale)
Weighted price target: -8.4% above the current prices
Holdings read: MRNA, PTC, ACN, IT, HAS
Recent rating changes among them:
  - MRNA: 2026-11-09 Goldman Sachs: main, Neutral -> Neutral
  - PTC: 2026-10-06 Citigroup: main, Neutral -> Neutral
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
Contract: E-MINI S&P 500 - CHICAGO MERCANTILE EXCHANGE (positions as of 2026-11-03, published the following Friday)
Large speculators: net short 18.7% of open interest (1,986,532 contracts)
Change on the week: +1.7% of open interest
Crowding: 68% percentile over 52 weeks -- within its normal range
Read this as crowding, not as a forecast: an extreme is as often the end of a move as the middle of one.
```

</details>

<details><summary><b>Money going into and out of this fund</b> — score -0.20</summary>

```text
Direction: money coming in (1 month)
Share count change: 1 week: +3.6% (3.50B) over 9d | 1 month: +1.1% (1.08B) over 30d
Shares outstanding: 455.78M | fund size: 101.18B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### US government bonds, 1-3 years (SHY) · Index fund — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Neutral outlook as macro data shows no surprise, positioning shift is modestly bullish but still net short, fund’s short duration mitigates yield rise, and technicals lack decisive break.

**Main reasons it gave:**
- 2-year Treasury yield rose 17 bps to 4.73% – largest jump in 19 months (macro)
- Large speculators net short 32.5% of open interest, but net short decreased by 2.5% week‑over‑week (insider)
- Fund’s short‑duration (99.8% 1‑3 year Treasuries) limits price impact of rising yields (fund basics)
- Technical indicators show slight downtrend (price below 20‑, 50‑, 200‑day SMAs) with low volume and no decisive break (technical)

<details><summary><b>News</b> — score +0.00</summary>

- [The 2-Year Treasury Yield Just Had Its Biggest Jump in 19 Months](https://247wallst.com/investing/2026/11/11/the-2-year-treasury-yield-just-had-its-biggest-jump-in-19-months/?tpid=1702334&tv=link&tc=in_content)  
  <sub>24/7 Wall St., 18 hours ago</sub>  
  The 2-year Treasury yield rose 17 basis points on Tuesday, November 10, 2026, closing at 4.73% after closing at 4.56% on Monday, November 9.
- [The Bond Rally Faces a Reality Check](https://www.google.com/goto?url=CAESjQEBxCJF13pX8QuzGi48k01gPWQ9rhgPI2DvIrQYcyHwYd_LC9SVllvn-QHpiCmcZoDSgqgkK3MBPXK3z7bNC0KzneK5TvEwWy-X4DlCWHs9drjVBhF8ALZqzucFfaazs_-I9r5khiuSurOFBEPZ7-XxkS6O8uqO7EBGEUIHBYOpfzhKk0j3MwNl7cVj8aY&gsessionid=Vf25-oQhStcxuUvjkqvPgS3ud3VVN7647ci-uLyHGdYwgeVJemkIuQ)  
  <sub>Investing.com UK, 50 minutes ago</sub>  
  Market Analysis by James Picerno covering: Vanguard Total Bond Market Index Fund ETF Shares, iShares 1-3 Year Treasury Bond ETF, iShares 7-10 Year Treasury...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.11% (+0.12 on the week) | 5-year 4.87% (+0.27 on the week) | 10-year 5.03% (+0.19 on the week) | 30-year 5.37% (+0.12 on the week)
Yield curve, 10-year minus 3-month: +0.92 points -- upward sloping (normal)
US dollar index: 102.91 (+1.36 on the week)
Volatility (VIX): 18.99 (-9.2 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.1% (2026-10-01) | jobless claims 200k (2026-11-07)
Policy and expectations: Fed target 4.00% | market expects 2.2% inflation over 10 years
Rate path: 2-year Treasury 4.56% vs Fed target 3.75-4.00% -- the bond market prices about 3 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 81.23 (bar of 2026-11-12), from 502 daily bars
Trend: vs 20d SMA 81.45 (-0.3%), 50d 81.35 (-0.1%), 200d 82.05 (-1.0%); 50d below 200d
Momentum: RSI(14) 41.5 | MACD 0.011 vs signal 0.039 (histogram -0.028)
Returns: 1d -0.1% | 5d -0.5% | 1m +0.1% | 3m -0.9%
52-week range: 81.05 - 83.18 (now 8.4% of the way up)
Volatility: ATR(14) 0.13 (0.2% of price) | annualised 20d 2.3%
Volume: 0.06x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score -0.10</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score -0.10</summary>

```text
Fund type: Short Government
Yield: 3.6%
Credit quality: AA 100.0% | US government debt 99.8%
Three-year record: +4.0% a year | beta to the market 0.25
Cost and size: expense ratio 0.15% | net assets 27.44B
What it is made of: Bonds 99.8%, Cash 0.2%
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

<details><summary><b>Buying and selling by company insiders</b> — score +0.20</summary>

_Not available today._

</details>

<details><summary><b>Who is positioned how</b> — score +0.20</summary>

```text
Contract: UST 2Y NOTE - CHICAGO BOARD OF TRADE (positions as of 2026-11-03, published the following Friday)
Large speculators: net short 32.5% of open interest (4,464,182 contracts)
Change on the week: -2.5% of open interest
Crowding: 78% percentile over 52 weeks -- within its normal range
Read this as crowding, not as a forecast: an extreme is as often the end of a move as the middle of one.
```

</details>

<details><summary><b>Money going into and out of this fund</b> — score +0.20</summary>

```text
Direction: money coming in (1 month)
Share count change: 1 week: +4.9% (1.27B) over 9d | 1 month: +4.2% (1.10B) over 30d
Shares outstanding: 337.40M | fund size: 27.41B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### US inflation-linked bonds (TIP) · Index fund — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Neutral overall; no macro surprise, technicals weak, modest positioning and flows.

**Main reasons it gave:**
- US Treasury yields rose modestly across the curve (+0.12 to +0.27) with no surprise rate move
- Technical indicators show weak momentum (RSI 38.7, MACD histogram -0.139) and price below 20‑day SMA
- CFTC positioning shows net short 38% of open interest, change only -0.2% (neutral crowding)
- Fund flows positive (+4.4% share count week) but modest, indicating limited new demand

<details><summary><b>News</b> — score +0.00</summary>

- [Vanguard Says Tax-Loss Inflows to Muni ETFs Likely to Stick](https://www.bloomberg.com/news/articles/2026-11-11/vanguard-says-tax-loss-inflows-to-muni-etfs-likely-to-stick?srnd=homepage-europe)  
  <sub>Bloomberg.com, 22 hours ago</sub>  
  Tax-loss harvesting has turbocharged the growth of municipal-bond exchange traded funds in 2026 at the expense of open-end mutual funds, which may lose much...
- [Taiwan Stocks Plunge 5,510 Points in a Single Week, Yet Taiwan Equity ETF Beneficiaries Top 20.25 Million to Hit Record High](https://finance.biggo.com/news/b91b2f3c-ad88-4056-8a40-ffd22b34a6a9)  
  <sub>BigGo Finance, 10 hours ago</sub>  
  Taiwan stocks plunged 5510.19 points last week, a 12.19% decline that marked the largest single-week point drop on record. Yet the number of Taiwan…
- [MFF Director Sally Chaplain Acquires 13,000 Shares](https://www.google.com/goto?url=CAESogEBxCJF17nYaparjNq4RSQwAY2R40vlgJa-CO3frZKLokhLlpKy9sMx2suLXjRpt6kDnjxwtZTVCXiBrZMIgBAOQwcTo1NSC7GLSBML0v-kvkExINs3iw7jcJUvblPn0KqqRQ8tu9iZKvIpvoXWEj4bc-Wbiu0vYTqRuNzuFcIatA4TWPhK05eW1OZGqoF0FdbF1kGowMqTDL5e_QvNnZJnn4c&gsessionid=J0Lh32EaQ-QNgrhcgZiJdfDnAHgiY0OhTy6l_bVtQ_GKLqdFxciH7w)  
  <sub>TipRanks, 3 hours ago</sub>  
  MFF Capital Investments Ltd. ( ($AU:MFF) ) just unveiled an announcement. MFF Capital Investments Limited owns 100% of Montaka Global Pty Ltd,...
- [Cerebras (CBRS) vs. TSMC (TSM): Which Stock Has More Upside, According to Analysts?](https://www.google.com/goto?url=CAESrgEBxCJF1_GIOhYwQEy_Wxu3EicxDkYVuDisb7EgQxFwYmvEONGgiIViwt_g50EZwQXBC1aBFroCMfDm8at_oXQiiKzW7xrYzpQhmiglKLe4xB_pha3cSVG2ohU0YPsWDfc7ZTSJCIsqIpuywdFhotaN2587T3RmyHtQyqWwWZuhckhM-TYmQcVH11rmDaMOif-Mh7C3OtaoFafZwTY6SyGOVE0PgAZL9pvBuRxcpwQ&gsessionid=J0Lh32EaQ-QNgrhcgZiJdfDnAHgiY0OhTy6l_bVtQ_GKLqdFxciH7w)  
  <sub>TipRanks, 5 hours ago</sub>  
  Cerebras ($CBRS) and TSMC ($TSM) are two stocks that could benefit from demand for computing power, but one may offer more upside, according to analysts.
- [Why Is Alibaba Stock (BABA) Falling in Premarket Today Ahead of November 19 Earnings?](https://www.google.com/goto?url=CAESpwEBxCJF10EpNQOegu89pdM41aoR1oXLhiCT_xYc2p6UjI26376KphsSfe74_QsLWkunYGrlmyVyLV97-bXh9C4FM9qHk41McAFGG8rTsYTULaOOPxJ0Q-PFdvKRz1AyY8RkvTuUQZbMaeud2Wt-jnw-iJwvX78SImJwNIzvD7rt7HWt5cP_se06DMQwDv4FmNOtYM6IzyHptRyA27sEHj8JUwR-hcJvxQ&gsessionid=J0Lh32EaQ-QNgrhcgZiJdfDnAHgiY0OhTy6l_bVtQ_GKLqdFxciH7w)  
  <sub>TipRanks, 4 hours ago</sub>  
  Alibaba ($BABA) stock trended lower in Thursday's pre-market trading as concerns over Nvidia ($NVDA) chip supplies weighed on Chinese AI shares.
- [La Trobe Private Credit Fund Applies for Quotation of 83,782 Units](https://www.google.com/goto?url=CAESsgEBxCJF18aiEOaz0GWKByv6bITr1n8LEP0XCipoee4AVE54nghl6l4LWIJsHgEGtY_Pwzza0_QMC3BvPavou897iDJY280oH43h0jz3bKTUlSG1nclfI4xT0aoimSnoO5AFoIKJz7q2L3isRMVzj9StP8_9-HIHgvxJYPKPBbZdsG5ZvQyIUq7jyWW-4KiTwgqH6GkVNyW89Rx_SCPdgbl1iXPBcG3AODniXWIw8T3MsMQL&gsessionid=J0Lh32EaQ-QNgrhcgZiJdfDnAHgiY0OhTy6l_bVtQ_GKLqdFxciH7w)  
  <sub>TipRanks, 3 hours ago</sub>  
  La Trobe Private Credit Fund ( ($AU:LF1) ) has issued an update. La Trobe Private Credit Fund applies for ASX quotation of 83782 fully paid ordinary units...
- [Brambles Applies to Quote 11,700 Ordinary Securities](https://www.google.com/goto?url=CAESpAEBxCJF1_L5EcQMPnxC7WLaQ42L3wBLkgXGnyQXJ9yiuSsH1Bn8-0xq7__WU0sPmCQ1QsYndU-Y1IZGzGygrpBljt4uMSWxXG7odyItgJwPJx4dMtRk12t-KENuWftyxveSIxAIiLtbx3YRZECsb-K5s0QFnSnVtHh1WdsOFnEh3OAVXJWnxK7YZZ1RjOY0Rul9dB1L6S0jSfofPI0WoEc_jDy6Yg&gsessionid=J0Lh32EaQ-QNgrhcgZiJdfDnAHgiY0OhTy6l_bVtQ_GKLqdFxciH7w)  
  <sub>TipRanks, 3 hours ago</sub>  
  Brambles ( ($AU:BXB) ) just unveiled an announcement. Brambles Limited, identified by ASX issuer code BXB, applied for quotation of 11700 fully paid...
- [Why AMD and Broadcom Stocks Gained After Hours While Nvidia Fell over 8%](https://www.google.com/goto?url=CAESogEBxCJF1wH6N2t10bwKi9-3j0ueUQvkeAqU3kK3R4NnCVzF0xx28Nv96ibWdIAPQZ8iliAZjPov6L_pPFaZ3pVFv4UOjuwOb3wzsnPuLyC1kF2x1rULBp3BiiV4A4r6-Cz2vKuDwNmm-ydXirdzatY4GBQfADiHRyoSFUW0E8ytvIv-zV40jsGDJWyGOLnAhOWX-DecTWVaAHfnZ1ZckX7MpS4&gsessionid=J0Lh32EaQ-QNgrhcgZiJdfDnAHgiY0OhTy6l_bVtQ_GKLqdFxciH7w)  
  <sub>TipRanks, 6 hours ago</sub>  
  Nvidia ($NVDA) stock plunged 8.61% in Wednesday's after-hours trading, reversing a 2.87% gain during the regular session. Meanwhile, AMD ($AMD) and Broadcom...
- [Google’s Gemini AI Lands on Apple CarPlay for Hands-Free Use](https://www.google.com/goto?url=CAESlgEBxCJF163Of6oM-whEXZyjTxBhz4NumFh2wpGvkAGfZzT-SlY1fKkcZwmDVuXhAPdCoH00VmSeoe9Ug9KtJpV32jcdmyml9D4-h96MNPx34tHzgmsxCcH87ugAx7E3N8pDYyqnlQKYKy5VAKXzw6Iavdjwme-I76Aw0jAV6gp9l2MJu18-f59ntPmQF6F2xGTJ4ILAOKQ&gsessionid=J0Lh32EaQ-QNgrhcgZiJdfDnAHgiY0OhTy6l_bVtQ_GKLqdFxciH7w)  
  <sub>TipRanks, 8 hours ago</sub>  
  Google ($GOOGL) is bringing its Gemini AI assistant to Apple ($AAPL) CarPlay. The new feature will let drivers have hands-free conversations with Gemini...
- [Why Nvidia Stock Is Plunging 7% in After-Hours Trading — and What Wall Street Sees Next](https://www.google.com/goto?url=CAESrwEBxCJF1xYGLvEvdVUY0sN2wmyUYz_nwWGyG3cqVJjn7FRNTnEkXA4oZkV200nhNnr-8mbS7tiRB02KoAaSPOPW_FKe-FdEHycL4wv2bvVOl11RHjwhR1_hmxMPWOsGYn6Zch25kEtX5EiJDJrbhQVJlUOiboR3nBr1JL7XqqsAU9MCJhiTuv5GBp4nrW10QgMxAyPRzbf14ZfpqAt8R3TsXrLXSmnTxiU-HBiU4xt9&gsessionid=J0Lh32EaQ-QNgrhcgZiJdfDnAHgiY0OhTy6l_bVtQ_GKLqdFxciH7w)  
  <sub>TipRanks, 9 hours ago</sub>  
  Nvidia (NASDAQ:NVDA) is plunging 7% in Wednesday's after-hours trading, wiping out its earlier gains as a scandal surrounding CEO Jensen Huang takes another...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.11% (+0.12 on the week) | 5-year 4.87% (+0.27 on the week) | 10-year 5.03% (+0.19 on the week) | 30-year 5.37% (+0.12 on the week)
Yield curve, 10-year minus 3-month: +0.92 points -- upward sloping (normal)
US dollar index: 102.91 (+1.36 on the week)
Volatility (VIX): 18.99 (-9.2 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.1% (2026-10-01) | jobless claims 200k (2026-11-07)
Policy and expectations: Fed target 4.00% | market expects 2.2% inflation over 10 years
Rate path: 2-year Treasury 4.56% vs Fed target 3.75-4.00% -- the bond market prices about 3 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score -0.10</summary>

```text
Last close 105.09 (bar of 2026-11-12), from 502 daily bars
Trend: vs 20d SMA 105.96 (-0.8%), 50d 105.46 (-0.4%), 200d 108.67 (-3.3%); 50d below 200d
Momentum: RSI(14) 38.7 | MACD 0.035 vs signal 0.174 (histogram -0.139)
Returns: 1d -0.2% | 5d -1.1% | 1m +0.3% | 3m -1.8%
52-week range: 103.98 - 111.88 (now 14.1% of the way up)
Volatility: ATR(14) 0.38 (0.4% of price) | annualised 20d 4.5%
Volume: 0.06x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.20</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score +0.20</summary>

```text
Fund type: Inflation-Protected Bond
Yield: 4.4%
Credit quality: AA 100.0% | US government debt 99.8%
Three-year record: +3.8% a year | beta to the market 0.73
Cost and size: expense ratio 0.18% | net assets 14.65B
What it is made of: Bonds 99.8%, Cash 0.2%
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
Share count change: 1 week: +4.4% (614.22M) over 9d | 1 month: +2.1% (295.11M) over 30d
Shares outstanding: 139.22M | fund size: 14.63B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### US dollar (UUP) · Index fund — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Neutral overall; modest bullish positioning and strong inflows are offset by lack of a clear macro surprise or decisive technical breakout on heavy volume.

**Main reasons it gave:**
- US dollar index rose 1.36% on the week, indicating a stronger dollar
- Share count increased 11.1% in one week, showing strong inflows
- Price near 52‑week high and above 20‑, 50‑, and 200‑day SMAs, indicating bullish trend
- Large speculators net long 6.7% of open interest, modest weekly increase

<details><summary><b>News</b> — score +0.00</summary>

- [Is Invesco DB US Dollar Index Bullish ETF (UUP) a Strong ETF Right Now?](https://sg.finance.yahoo.com/news/invesco-db-us-dollar-index-102002666.html)  
  <sub>Yahoo Finance Singapore, 4 hours ago</sub>  
  Launched on 02/20/2007, the Invesco DB US Dollar Index Bullish ETF (UUP) is a smart beta exchange traded fund offering broad exposure to the Currency ETFs...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.11% (+0.12 on the week) | 5-year 4.87% (+0.27 on the week) | 10-year 5.03% (+0.19 on the week) | 30-year 5.37% (+0.12 on the week)
Yield curve, 10-year minus 3-month: +0.92 points -- upward sloping (normal)
US dollar index: 102.91 (+1.36 on the week)
Volatility (VIX): 18.99 (-9.2 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.1% (2026-10-01) | jobless claims 200k (2026-11-07)
Policy and expectations: Fed target 4.00% | market expects 2.2% inflation over 10 years
Rate path: 2-year Treasury 4.56% vs Fed target 3.75-4.00% -- the bond market prices about 3 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 29.33 (bar of 2026-11-12), from 502 daily bars
Trend: vs 20d SMA 29.03 (+1.0%), 50d 28.77 (+2.0%), 200d 28.02 (+4.7%); 50d above 200d
Momentum: RSI(14) 64.5 | MACD 0.110 vs signal 0.093 (histogram 0.017)
Returns: 1d -0.1% | 5d +1.4% | 1m +0.7% | 3m +4.3%
52-week range: 26.47 - 29.35 (now 99.4% of the way up)
Volatility: ATR(14) 0.13 (0.4% of price) | annualised 20d 5.6%
Volume: 0.03x the 20-day average
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
Three-year record: +3.9% a year | beta to the market -7.93
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
Contract: USD INDEX - ICE FUTURES U.S. (positions as of 2026-11-03, published the following Friday)
Large speculators: net long 6.7% of open interest (49,091 contracts)
Change on the week: +0.2% of open interest
Crowding: 87% percentile over 52 weeks -- within its normal range
Read this as crowding, not as a forecast: an extreme is as often the end of a move as the middle of one.
```

</details>

<details><summary><b>Money going into and out of this fund</b> — score +0.10</summary>

```text
Direction: money coming in (1 month)
Share count change: 1 week: +11.1% (48.46M) over 7d | 1 month: +11.2% (48.91M) over 30d
Shares outstanding: 16.52M | fund size: 484.54M
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Europe (VGK) · Index fund — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> No material macro surprise or decisive technical break; mixed signals from analyst view, positioning, fundamentals and flows lead to a neutral stance.

**Main reasons it gave:**
- Analyst view: 85.7% buy, weighted price target +23.3%, but only 12.1% of fund covered
- CFTC positioning: net short 2.6% of open interest, down 2.8% week‑over‑week
- Fund flows: share count fell 2.4% in one week and 4.2% over the month, indicating outflows
- Technicals: price above 20‑, 50‑, 200‑day SMAs and MACD positive, but volume at 0.03x 20‑day average
- Macro: US Treasury yields rose across the curve and dollar index up 1.36% on the week, adding pressure on European equities

<details><summary><b>News</b> — score +0.00</summary>

- [VGK Mar 2027 90.000 put (VGK270319P00090000) Interactive Stock Chart](https://ca.finance.yahoo.com/quote/VGK270319P00090000/chart/)  
  <sub>Yahoo! Finance Canada, 21 hours ago</sub>  
  Interactive Chart for VGK Mar 2027 90.000 put (VGK270319P00090000), analyze all the data with a huge range of indicators.
- [Utah vs Vegas | Prediction Markets](https://www.coinbase.com/predictions/event/KXNHLGAME-26NOV11UTAVGK)  
  <sub>Coinbase, 9 hours ago</sub>  
  Make your prediction on Utah vs Vegas. Trade on the future with Coinbase Predictions.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.11% (+0.12 on the week) | 5-year 4.87% (+0.27 on the week) | 10-year 5.03% (+0.19 on the week) | 30-year 5.37% (+0.12 on the week)
Yield curve, 10-year minus 3-month: +0.92 points -- upward sloping (normal)
US dollar index: 102.91 (+1.36 on the week)
Volatility (VIX): 18.99 (-9.2 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.1% (2026-10-01) | jobless claims 200k (2026-11-07)
Policy and expectations: Fed target 4.00% | market expects 2.2% inflation over 10 years
Rate path: 2-year Treasury 4.56% vs Fed target 3.75-4.00% -- the bond market prices about 3 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 89.30 (bar of 2026-11-12), from 502 daily bars
Trend: vs 20d SMA 87.90 (+1.6%), 50d 88.01 (+1.5%), 200d 87.96 (+1.5%); 50d above 200d
Momentum: RSI(14) 55.5 | MACD 0.495 vs signal 0.224 (histogram 0.271)
Returns: 1d -0.2% | 5d +1.0% | 1m +3.8% | 3m -3.3%
52-week range: 77.90 - 93.19 (now 74.6% of the way up)
Volatility: ATR(14) 1.12 (1.3% of price) | annualised 20d 20.0%
Volume: 0.03x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.20</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score +0.20</summary>

```text
Fund type: Europe Stock
What it holds: P/E 17.26 | P/B 2.24 | P/S 1.59 | 3y earnings growth n/a
Yield: 2.9%
Three-year record: +19.1% a year | beta to the market 0.88
Cost and size: expense ratio 0.06% | net assets 37.08B
What it is made of: Stocks 99.0%, Cash 0.7%, Other 0.3%
Largest holdings: ASML Holding NV 4.5%, HSBC Holdings PLC 2.2%, Roche Holding AG Ordinary Shares new 1.9%, Shell PLC 1.8%, Novartis AG Registered Shares 1.7%
Sector mix: Financial services 25.4%, Industrials 19.5%, Healthcare 12.1%, Technology 9.4%
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
Rolled up from the 5 largest holdings, 12.1% of the fund by weight  -- thin, so read this as a fact about that slice rather than the fund
Ratings by weight: buy 85.7% | hold 14.3% | sell 0.0% (mean 2.04 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +23.3% above the current prices
Holdings read: ASML.AS, HSBA.L, ROP.SW, SHEL.L, NOVN.SW
Recent rating changes among them: none reported
```

</details>

<details><summary><b>Buying and selling by company insiders</b> — score +0.10</summary>

_Not available today._

</details>

<details><summary><b>Who is positioned how</b> — score +0.10</summary>

```text
Contract: MSCI EAFE  - ICE FUTURES U.S. (positions as of 2026-11-03, published the following Friday)
Large speculators: net short 2.6% of open interest (505,889 contracts)
Change on the week: -2.8% of open interest
Crowding: 22% percentile over 52 weeks -- within its normal range
Read this as crowding, not as a forecast: an extreme is as often the end of a move as the middle of one.
```

</details>

<details><summary><b>Money going into and out of this fund</b> — score +0.10</summary>

```text
Direction: money going out (1 month)
Share count change: 1 week: -2.4% (-926.97M) over 9d | 1 month: -4.2% (-1.63B) over 30d
Shares outstanding: 414.75M | fund size: 37.04B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Emerging markets (VWO) · Index fund — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Neutral overall; no macro surprise, technicals lack decisive bullish break, and analyst coverage is thin despite bullish ratings.

**Main reasons it gave:**
- US Treasury yields rose modestly across the curve (+0.12 to +0.27) and dollar index up (+1.36), indicating tighter financial conditions for EM
- Technical indicators show price below 20‑day, 50‑day, and 200‑day SMAs, RSI 45.1, and low volume, suggesting lack of bullish momentum
- Analyst coverage thin (23.5% of fund) despite 100% buy rating and +53.4% price target, limiting impact on overall fund
- CFTC positioning shows only 1.1% net long with a modest weekly increase (+0.6% OI) and low crowding (22% percentile), indicating limited bullish pressure

<details><summary><b>News</b> — score +0.00</summary>

- [Wall Street Sees 37% Upside Over the Next 12 Months for This Vanguard ETF](https://www.fool.com/investing/2026/11/11/wall-street-sees-37-upside-over-the-next-12-months-for-this-vanguard-etf/)  
  <sub>The Motley Fool, 22 hours ago</sub>  
  A lot of investors are still focused on U.S. stocks, but emerging markets present a really attractive opportunity.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.11% (+0.12 on the week) | 5-year 4.87% (+0.27 on the week) | 10-year 5.03% (+0.19 on the week) | 30-year 5.37% (+0.12 on the week)
Yield curve, 10-year minus 3-month: +0.92 points -- upward sloping (normal)
US dollar index: 102.91 (+1.36 on the week)
Volatility (VIX): 18.99 (-9.2 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.1% (2026-10-01) | jobless claims 200k (2026-11-07)
Policy and expectations: Fed target 4.00% | market expects 2.2% inflation over 10 years
Rate path: 2-year Treasury 4.56% vs Fed target 3.75-4.00% -- the bond market prices about 3 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score -0.10</summary>

```text
Last close 56.35 (bar of 2026-11-12), from 502 daily bars
Trend: vs 20d SMA 56.61 (-0.5%), 50d 58.63 (-3.9%), 200d 58.30 (-3.4%); 50d above 200d
Momentum: RSI(14) 45.1 | MACD -0.715 vs signal -0.882 (histogram 0.167)
Returns: 1d -1.5% | 5d +3.9% | 1m -4.3% | 3m -6.3%
52-week range: 52.42 - 61.44 (now 43.5% of the way up)
Volatility: ATR(14) 0.90 (1.6% of price) | annualised 20d 23.4%
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
Three-year record: +16.0% a year | beta to the market 0.78
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
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 1.33 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +53.4% above the current prices
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
Shares outstanding: 1.42B | fund size: 79.90B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

## Sector and country funds

### US health care (XLV) · Sector or country — BULLISH, confidence 0.45

**Result:** ACCEPTED · 37 shares · submitted buy 37 XLV @ ~189.10, stop 182.28

**In the model's own words:**

> The fund shows moderate bullish bias based on strong analyst coverage, positive fund flows, and supportive technicals, while macro conditions remain neutral.

**Main reasons it gave:**
- Analyst view: 100% buy rating on top holdings, weighted price target +4.6% above current price
- Fund flows: share count up 10.8% in the past week (~$4.78B inflow)
- Technicals: price above 20‑day, 50‑day and 200‑day SMAs; RSI 68, MACD positive
- Fund basics: 3‑year annualized return of 16.3% and low beta (0.41) indicating strong performance and low volatility

<details><summary><b>News</b> — score +0.20</summary>

- [State Street Health Care SPDR (XLV) Adds Eli Lilly and Johnson & Johnson on Nov. 10](https://finance.yahoo.com/healthcare/articles/state-street-health-care-spdr-110554537.html)  
  <sub>Yahoo Finance, 4 hours ago</sub>  
  This article first appeared on GuruFocus. In ETF activity on Tuesday, State Street Health Care Select Sector SPDR ETF (XLV) was a buyer only,...
- [ETFs in Spotlight as FDA Vision Loss Warning Meets Lilly's Sleep Apnea Win](https://es.tradingview.com/news/zacks:16c63ee90094b:0-etfs-in-spotlight-as-fda-vision-loss-warning-meets-lilly-s-sleep-apnea-win/)  
  <sub>TradingView, 22 hours ago</sub>  
  Two developments this week are forcing investors to reconsider how they gain exposure to the weight-loss drug boom. On one side, Eli Lilly's (LLY) oral...
- [In the Year of AI, Tech Isn’t the Top Sector](https://www.google.com/goto?url=CAESfwHEIkXXS2OUovFxCRfrD_m_mJTW-agI8qtH8mLtkWm_sd2u_s-8YDjViP1S6Y6YdL1uPW-JeBUKwUm4LgVWXPR-V-SZr_0l-LCk4-rtVMXr8TZ_A91z8HMsPrFHeSCDoQK1jDWBT-kwZs0Iz_4k_9yayaEyW1tAH54AXgUK4GQ&gsessionid=Kv4t8gH8kVzRzuHsjqGNB6JzTxGi3aMWcBinnELbsEu1iW3cmJ5ZQQ)  
  <sub>ETF.com, 21 hours ago</sub>  
  Energy leads the S&P 500's sectors by a mile, and health care has caught up with tech.
- [BrightSpring, Centene stand out as healthcare's most persistent Strong Buys (XLV:NYSEARCA)](https://www.google.com/goto?url=CAESrAEBxCJF1yXsio3oqakchQ_T-VCaF8VEb3Id5qmZypg7ri-10h-D4GkHbMZiPBuZp6bHeqhA8rwlcSEsS17lxZ3N6QQxcfMCcpYGgF-chM6toDgITemXm1ujHTnLMaVPwT0LDbPkxskX7A1S2jRjO78CM2KX4q3rdx9S-VfhJzwvnrFrEgfp-4Y3tfN18eqPNXe5UFh-ve0CUnTnMxJdQ3LAzFgA1j-ty8NzBl7b&gsessionid=Kv4t8gH8kVzRzuHsjqGNB6JzTxGi3aMWcBinnELbsEu1iW3cmJ5ZQQ)  
  <sub>Seeking Alpha, 2 hours ago</sub>  
  Seven healthcare stocks retain Strong Buy Quant Ratings for 28 to 256 days; Iovance Biotherapeutics leads with a 4.95 score.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.20</summary>

```text
US Treasury yields: 3-month 4.11% (+0.12 on the week) | 5-year 4.87% (+0.27 on the week) | 10-year 5.03% (+0.19 on the week) | 30-year 5.37% (+0.12 on the week)
Yield curve, 10-year minus 3-month: +0.92 points -- upward sloping (normal)
US dollar index: 102.91 (+1.36 on the week)
Volatility (VIX): 18.99 (-9.2 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.1% (2026-10-01) | jobless claims 200k (2026-11-07)
Policy and expectations: Fed target 4.00% | market expects 2.2% inflation over 10 years
Rate path: 2-year Treasury 4.56% vs Fed target 3.75-4.00% -- the bond market prices about 3 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.40</summary>

```text
Last close 188.80 (bar of 2026-11-12), from 502 daily bars
Trend: vs 20d SMA 183.09 (+3.1%), 50d 174.75 (+8.0%), 200d 160.03 (+18.0%); 50d above 200d
Momentum: RSI(14) 68.1 | MACD 4.183 vs signal 3.908 (histogram 0.275)
Returns: 1d -0.1% | 5d +2.1% | 1m +8.5% | 3m +12.8%
52-week range: 142.84 - 189.66 (now 98.2% of the way up)
Volatility: ATR(14) 3.37 (1.8% of price) | annualised 20d 20.8%
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
Three-year record: +16.3% a year | beta to the market 0.41
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
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 1.72 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +4.6% above the current prices
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
Share count change: 1 week: +10.8% (4.78B) over 9d | 1 month: +2.3% (1.12B) over 30d
Shares outstanding: 260.00M | fund size: 49.09B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### US regional banks (KRE) · Sector or country — BULLISH, confidence 0.35

**Result:** ACCEPTED · 97 shares · submitted buy 97 KRE @ ~72.55, stop 69.67

**In the model's own words:**

> The fund shows modest bullish signals across multiple dimensions.

**Main reasons it gave:**
- Fund flows: share count up 7.0% in one week, indicating strong inflows
- Technical trend: price above 20d, 50d, 200d SMAs and MACD positive
- Analyst view: 50.1% buy rating and weighted price target +9.9% above current price
- Macro: rising Treasury yields (10-year +0.19% week) supportive for banks

<details><summary><b>News</b> — score +0.00</summary>

- [KRE Dec 2026 75.000 call (KRE261211C00075000) Interactive Stock Chart](https://ca.finance.yahoo.com/quote/KRE261211C00075000/chart/)  
  <sub>Yahoo! Finance Canada, 14 hours ago</sub>  
  Interactive Chart for KRE Dec 2026 75.000 call (KRE261211C00075000), analyze all the data with a huge range of indicators.
- [META_TITLE_QUOTE](https://finance.yahoo.com/quote/ITB/)  
  <sub>Yahoo Finance, 14 hours ago</sub>  
  Biogen is an established biopharmaceutical company focused on treatments for neurodegenerative and rare diseases. Its declining multiple sclerosis franchise...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.11% (+0.12 on the week) | 5-year 4.87% (+0.27 on the week) | 10-year 5.03% (+0.19 on the week) | 30-year 5.37% (+0.12 on the week)
Yield curve, 10-year minus 3-month: +0.92 points -- upward sloping (normal)
US dollar index: 102.91 (+1.36 on the week)
Volatility (VIX): 18.99 (-9.2 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.1% (2026-10-01) | jobless claims 200k (2026-11-07)
Policy and expectations: Fed target 4.00% | market expects 2.2% inflation over 10 years
Rate path: 2-year Treasury 4.56% vs Fed target 3.75-4.00% -- the bond market prices about 3 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.30</summary>

```text
Last close 72.69 (bar of 2026-11-12), from 502 daily bars
Trend: vs 20d SMA 72.25 (+0.6%), 50d 71.77 (+1.3%), 200d 71.20 (+2.1%); 50d above 200d
Momentum: RSI(14) 52.8 | MACD 0.477 vs signal 0.416 (histogram 0.062)
Returns: 1d -0.4% | 5d +0.5% | 1m +6.1% | 3m -6.7%
52-week range: 58.63 - 77.93 (now 72.8% of the way up)
Volatility: ATR(14) 1.43 (2.0% of price) | annualised 20d 20.7%
Volume: 0.10x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.30</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score +0.30</summary>

```text
Fund type: Financial
What it holds: P/E 12.00 | P/B 1.21 | P/S 3.59 | 3y earnings growth n/a
Yield: 2.2%
Three-year record: +24.2% a year | beta to the market 0.97
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

<details><summary><b>What analysts and big funds say</b> — score +0.20</summary>

_Not available today._

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score +0.20</summary>

```text
Rolled up from the 5 largest holdings, 5.9% of the fund by weight  -- thin, so read this as a fact about that slice rather than the fund
Ratings by weight: buy 50.1% | hold 49.9% | sell 0.0% (mean 2.27 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +9.9% above the current prices
Holdings read: GBCI, UCB, TCBI, OZK, EBC
Recent rating changes among them:
  - GBCI: 2026-10-26 Piper Sandler: main, Overweight -> Overweight
  - UCB: 2026-10-21 Stephens & Co.: main, Overweight -> Overweight
  - TCBI: 2026-11-03 Barclays: main, Equal-Weight -> Equal-Weight
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
Share count change: 1 week: +7.0% (261.31M) over 7d | 1 month: +1.5% (59.88M) over 30d
Shares outstanding: 54.80M | fund size: 3.98B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Argentina (ARGT) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> No macro surprise; technicals oversold but no decisive break; mixed fund flows; strong analyst view but limited coverage; price at 52‑week low with low valuation.

**Main reasons it gave:**
- RSI 21.7 shows oversold momentum but no decisive technical break
- Share count fell 8% in the last week (-52.71M) indicating redemptions
- Analyst coverage 51.1% with 100% buy rating and +67.7% price target
- No macro surprise; yields rose modestly, dollar up, VIX down but still elevated
- Price at 52‑week low (71.67) with low valuation (P/E 13.9)

<details><summary><b>News</b> — score +0.00</summary>

_No news found for this one today._

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.11% (+0.12 on the week) | 5-year 4.87% (+0.27 on the week) | 10-year 5.03% (+0.19 on the week) | 30-year 5.37% (+0.12 on the week)
Yield curve, 10-year minus 3-month: +0.92 points -- upward sloping (normal)
US dollar index: 102.91 (+1.36 on the week)
Volatility (VIX): 18.99 (-9.2 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.1% (2026-10-01) | jobless claims 200k (2026-11-07)
Policy and expectations: Fed target 4.00% | market expects 2.2% inflation over 10 years
Rate path: 2-year Treasury 4.56% vs Fed target 3.75-4.00% -- the bond market prices about 3 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 71.67 (bar of 2026-11-12), from 502 daily bars
Trend: vs 20d SMA 80.41 (-10.9%), 50d 86.68 (-17.3%), 200d 91.04 (-21.3%); 50d below 200d
Momentum: RSI(14) 21.7 | MACD -4.067 vs signal -3.418 (histogram -0.649)
Returns: 1d -3.0% | 5d -3.2% | 1m -17.6% | 3m -21.2%
52-week range: 71.67 - 102.94 (now 0.0% of the way up)
Volatility: ATR(14) 2.15 (3.0% of price) | annualised 20d 31.4%
Volume: 0.08x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.50</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score +0.50</summary>

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

<details><summary><b>What analysts and big funds say</b> — score +0.85</summary>

_Not available today._

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score +0.85</summary>

```text
Rolled up from the 5 largest holdings, 51.1% of the fund by weight
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 1.60 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +67.7% above the current prices
Holdings read: MELI, YPF, VIST, GGAL, PAM
Recent rating changes among them:
  - MELI: 2026-11-11 UBS: main, Neutral -> Neutral
  - YPF: 2026-10-29 JP Morgan: main, Overweight -> Overweight
  - VIST: 2026-10-29 JP Morgan: main, Overweight -> Overweight
  - GGAL: 2026-10-13 UBS: main, Neutral -> Neutral
  - PAM: 2026-11-02 JP Morgan: main, Neutral -> Neutral
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
Direction: money coming in (1 month)
Share count change: 1 week: -8.0% (-52.71M) over 7d | 1 month: +3.7% (21.48M) over 30d
Shares outstanding: 8.43M | fund size: 604.35M
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Israel (EIS) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Neutral overall as bullish fundamentals and analyst view are offset by bearish technicals and a lack of macro catalyst.

**Main reasons it gave:**
- Analyst coverage of top 5 holdings (39.6% weight) all buy with +25.6% price target
- Fund flows flat over past week and month (no net creation/redemption)
- Technical indicators: price below 20‑day, 50‑day, 200‑day SMAs; RSI 44.4; MACD slightly negative
- Fund basics: 3‑year record +33.2% per year; moderate valuations (P/E 18.09)
- Macro: US Treasury yields rising and dollar strengthening

<details><summary><b>News</b> — score +0.00</summary>

_No news found for this one today._

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.11% (+0.12 on the week) | 5-year 4.87% (+0.27 on the week) | 10-year 5.03% (+0.19 on the week) | 30-year 5.37% (+0.12 on the week)
Yield curve, 10-year minus 3-month: +0.92 points -- upward sloping (normal)
US dollar index: 102.91 (+1.36 on the week)
Volatility (VIX): 18.99 (-9.2 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.1% (2026-10-01) | jobless claims 200k (2026-11-07)
Policy and expectations: Fed target 4.00% | market expects 2.2% inflation over 10 years
Rate path: 2-year Treasury 4.56% vs Fed target 3.75-4.00% -- the bond market prices about 3 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score -0.20</summary>

```text
Last close 114.20 (bar of 2026-11-12), from 502 daily bars
Trend: vs 20d SMA 116.86 (-2.3%), 50d 120.15 (-5.0%), 200d 122.93 (-7.1%); 50d below 200d
Momentum: RSI(14) 44.4 | MACD -1.992 vs signal -1.952 (histogram -0.040)
Returns: 1d -0.9% | 5d +6.9% | 1m -3.3% | 3m -8.4%
52-week range: 99.40 - 137.69 (now 38.6% of the way up)
Volatility: ATR(14) 2.46 (2.2% of price) | annualised 20d 36.0%
Volume: 0.10x the 20-day average
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
Three-year record: +33.2% a year | beta to the market 0.98
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
Weighted price target: +25.6% above the current prices
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
Shares outstanding: 2.55M | fund size: 291.20M
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Australia (EWA) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Neutral overall; analyst view slightly bearish, modest inflows and solid fundamentals offset each other, technicals lack a decisive break.

**Main reasons it gave:**
- Analyst view: 57.4% hold, 42.6% sell, mean rating 3.45 (slightly bearish) and price target -10.2% below current price
- Fund flows: 1‑week share count up 3.3% (≈$41 M) indicating modest net inflow
- Technicals: price above 20‑day, 50‑day and 200‑day SMAs but MACD histogram negative and volume 0.02× 20‑day average
- Macro: Treasury yields rose modestly, no policy surprise; VIX down but still elevated at 19

<details><summary><b>News</b> — score +0.00</summary>

_No news found for this one today._

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.11% (+0.12 on the week) | 5-year 4.87% (+0.27 on the week) | 10-year 5.03% (+0.19 on the week) | 30-year 5.37% (+0.12 on the week)
Yield curve, 10-year minus 3-month: +0.92 points -- upward sloping (normal)
US dollar index: 102.91 (+1.36 on the week)
Volatility (VIX): 18.99 (-9.2 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.1% (2026-10-01) | jobless claims 200k (2026-11-07)
Policy and expectations: Fed target 4.00% | market expects 2.2% inflation over 10 years
Rate path: 2-year Treasury 4.56% vs Fed target 3.75-4.00% -- the bond market prices about 3 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 29.35 (bar of 2026-11-12), from 502 daily bars
Trend: vs 20d SMA 29.30 (+0.2%), 50d 29.01 (+1.2%), 200d 28.99 (+1.2%); 50d above 200d
Momentum: RSI(14) 52.2 | MACD 0.139 vs signal 0.145 (histogram -0.007)
Returns: 1d -0.2% | 5d +0.3% | 1m +2.8% | 3m -1.0%
52-week range: 24.95 - 30.43 (now 80.3% of the way up)
Volatility: ATR(14) 0.34 (1.2% of price) | annualised 20d 16.5%
Volume: 0.02x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.10</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score +0.10</summary>

```text
Fund type: Focused Region
What it holds: P/E 20.37 | P/B 2.63 | P/S 3.35 | 3y earnings growth n/a
Yield: 2.9%
Three-year record: +15.1% a year | beta to the market 0.94
Cost and size: expense ratio 0.50% | net assets 1.25B
What it is made of: Stocks 99.8%, Cash 0.2%
Largest holdings: BHP Group Ltd 14.3%, Commonwealth Bank of Australia 13.7%, National Australia Bank Ltd 6.3%, Westpac Banking Corp 6.2%, ANZ Group Holdings Ltd 6.0%
Sector mix: Financial services 43.9%, Basic materials 22.9%, Consumer cyclical 6.6%, Healthcare 6.0%
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

<details><summary><b>What analysts and big funds say</b> — score -0.22</summary>

_Not available today._

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score -0.22</summary>

```text
Rolled up from the 5 largest holdings, 46.5% of the fund by weight
Ratings by weight: buy 0.0% | hold 57.4% | sell 42.6% (mean 3.45 on a 1=strong buy to 5=strong sell scale)
Weighted price target: -10.2% above the current prices
Holdings read: BHP.AX, CBA.AX, NAB.AX, WBC.AX, ANZ.AX
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
Direction: flat (1 month)
Share count change: 1 week: +3.3% (39.47M) over 9d | 1 month: +0.3% (4.06M) over 30d
Shares outstanding: 42.45M | fund size: 1.25B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Sweden (EWD) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> The fund shows modest bullish signals from analyst coverage, strong inflows, and decent fundamentals, but there is no material macro surprise or decisive technical breakout. The overall environment remains neutral.

**Main reasons it gave:**
- Analyst view: 100% buy rating on top holdings (33.9% weight) with +8.3% price target
- Fund flows: share count increased 13.9% in the past week
- Fundamentals: P/E 14.5, 3-year return +21.3% per year, yield 3.5%
- Technicals: price above 20d, 50d, 200d SMAs; RSI 56, MACD positive
- Macro: no significant surprise in rates or data; yields up modestly, VIX down but elevated

<details><summary><b>News</b> — score +0.00</summary>

_No news found for this one today._

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.11% (+0.12 on the week) | 5-year 4.87% (+0.27 on the week) | 10-year 5.03% (+0.19 on the week) | 30-year 5.37% (+0.12 on the week)
Yield curve, 10-year minus 3-month: +0.92 points -- upward sloping (normal)
US dollar index: 102.91 (+1.36 on the week)
Volatility (VIX): 18.99 (-9.2 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.1% (2026-10-01) | jobless claims 200k (2026-11-07)
Policy and expectations: Fed target 4.00% | market expects 2.2% inflation over 10 years
Rate path: 2-year Treasury 4.56% vs Fed target 3.75-4.00% -- the bond market prices about 3 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 52.90 (bar of 2026-11-12), from 502 daily bars
Trend: vs 20d SMA 51.94 (+1.9%), 50d 51.48 (+2.8%), 200d 51.55 (+2.6%); 50d below 200d
Momentum: RSI(14) 56.4 | MACD 0.557 vs signal 0.415 (histogram 0.141)
Returns: 1d -0.6% | 5d +0.8% | 1m +4.5% | 3m +0.0%
52-week range: 45.38 - 54.72 (now 80.6% of the way up)
Volatility: ATR(14) 0.80 (1.5% of price) | annualised 20d 21.7%
Volume: 0.08x the 20-day average
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
Three-year record: +21.3% a year | beta to the market 1.18
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
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 1.97 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +8.3% above the current prices
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
Share count change: 1 week: +13.9% (133.62M) over 9d | 1 month: +10.6% (104.94M) over 30d
Shares outstanding: 20.72M | fund size: 1.10B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

**Data that was missing** (counted as 0.00, never guessed):
- news unavailable: Bright Data returned an empty body with its 200; nothing to parse (Bright Data said: x-brd-status-code 502; x-brd-error redirect location was rejected) (Bing's feed, direct: 2 headline(s), none naming EWD)

### Germany (EWG) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Neutral overall as no material macro surprise or decisive technical break occurred; bullish analyst view and solid fundamentals are offset by flat fund flows and a tightening yield environment.

**Main reasons it gave:**
- US Treasury yields rose this week (3‑month +0.12%, 5‑year +0.27%, 10‑year +0.19%)
- Fund flows flat: share count unchanged (+0.0% over 1 week and 1 month)
- Analyst coverage: 78% buy rating, weighted price target +15.3% above current
- Technicals: price above 20‑, 50‑, 200‑day SMAs, MACD positive, volume 0.05× 20‑day average

<details><summary><b>News</b> — score +0.00</summary>

- [META_TITLE_QUOTE](https://finance.yahoo.com/quote/EWZ/)  
  <sub>Yahoo Finance, 14 hours ago</sub>  
  EWZ tracks Brazilian equities through the MSCI Brazil Index. The latest political repricing triggered a sharp October selloff, while EWZ was down 1.60%...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.11% (+0.12 on the week) | 5-year 4.87% (+0.27 on the week) | 10-year 5.03% (+0.19 on the week) | 30-year 5.37% (+0.12 on the week)
Yield curve, 10-year minus 3-month: +0.92 points -- upward sloping (normal)
US dollar index: 102.91 (+1.36 on the week)
Volatility (VIX): 18.99 (-9.2 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.1% (2026-10-01) | jobless claims 200k (2026-11-07)
Policy and expectations: Fed target 4.00% | market expects 2.2% inflation over 10 years
Rate path: 2-year Treasury 4.56% vs Fed target 3.75-4.00% -- the bond market prices about 3 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.20</summary>

```text
Last close 42.98 (bar of 2026-11-12), from 502 daily bars
Trend: vs 20d SMA 42.04 (+2.2%), 50d 42.04 (+2.2%), 200d 42.21 (+1.8%); 50d below 200d
Momentum: RSI(14) 56.8 | MACD 0.316 vs signal 0.168 (histogram 0.148)
Returns: 1d -0.1% | 5d +0.5% | 1m +5.0% | 3m -2.7%
52-week range: 38.08 - 44.59 (now 75.3% of the way up)
Volatility: ATR(14) 0.64 (1.5% of price) | annualised 20d 24.0%
Volume: 0.05x the 20-day average
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
Three-year record: +20.1% a year | beta to the market 0.95
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

<details><summary><b>What analysts and big funds say</b> — score +0.40</summary>

_Not available today._

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score +0.40</summary>

```text
Rolled up from the 5 largest holdings, 45.1% of the fund by weight
Ratings by weight: buy 78.0% | hold 22.0% | sell 0.0% (mean 1.93 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +15.3% above the current prices
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
Shares outstanding: 79.50M | fund size: 3.42B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Italy (EWI) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Neutral overall as there is no material macro surprise or decisive technical break; bullish analyst view and fundamentals are offset by bearish fund outflows and mixed technical signals.

**Main reasons it gave:**
- Fund flows: 1‑week share count down 4% (≈$48.9M) indicating net redemptions
- Technical: price above 20‑day SMA (+3.2%) but 50‑day SMA below 200‑day SMA, volume 0.17× 20‑day average
- Analyst view: 52.1% coverage, 90.8% buy rating, weighted price target +11.7% above current
- Macro: no surprise in rates or data; yields modestly higher, VIX down but still elevated

<details><summary><b>News</b> — score +0.00</summary>

_No news found for this one today._

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.11% (+0.12 on the week) | 5-year 4.87% (+0.27 on the week) | 10-year 5.03% (+0.19 on the week) | 30-year 5.37% (+0.12 on the week)
Yield curve, 10-year minus 3-month: +0.92 points -- upward sloping (normal)
US dollar index: 102.91 (+1.36 on the week)
Volatility (VIX): 18.99 (-9.2 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.1% (2026-10-01) | jobless claims 200k (2026-11-07)
Policy and expectations: Fed target 4.00% | market expects 2.2% inflation over 10 years
Rate path: 2-year Treasury 4.56% vs Fed target 3.75-4.00% -- the bond market prices about 3 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 58.55 (bar of 2026-11-12), from 502 daily bars
Trend: vs 20d SMA 56.74 (+3.2%), 50d 58.25 (+0.5%), 200d 58.28 (+0.5%); 50d below 200d
Momentum: RSI(14) 55.8 | MACD 0.232 vs signal -0.208 (histogram 0.440)
Returns: 1d -0.1% | 5d +2.2% | 1m +4.4% | 3m -7.5%
52-week range: 50.70 - 63.35 (now 62.1% of the way up)
Volatility: ATR(14) 0.95 (1.6% of price) | annualised 20d 28.8%
Volume: 0.17x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.40</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score +0.40</summary>

```text
Fund type: Focused Region
What it holds: P/E 14.58 | P/B 1.75 | P/S 1.42 | 3y earnings growth n/a
Yield: 3.4%
Three-year record: +28.2% a year | beta to the market 0.92
Cost and size: expense ratio 0.50% | net assets 1.19B
What it is made of: Stocks 99.8%, Cash 0.2%
Largest holdings: UniCredit SpA 16.4%, Intesa Sanpaolo 13.8%, Enel SpA 11.7%, Eni SpA 5.5%, Generali 4.8%
Sector mix: Financial services 50.9%, Utilities 18.2%, Industrials 11.9%, Consumer cyclical 8.4%
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
Rolled up from the 5 largest holdings, 52.1% of the fund by weight
Ratings by weight: buy 90.8% | hold 9.2% | sell 0.0% (mean 2.15 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +11.7% above the current prices
Holdings read: UCG.MI, ISP.MI, ENEL.MI, ENI.MI, G.MI
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
Share count change: 1 week: -4.0% (-48.95M) over 9d | 1 month: -3.5% (-42.53M) over 30d
Shares outstanding: 20.18M | fund size: 1.18B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Japan (EWJ) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Neutral – no material macro surprise, mixed technical and sentiment signals, and modestly positive but thin analyst coverage.

**Main reasons it gave:**
- RSI 43, price 1.8% below 20‑day SMA, MACD negative – modest bearish technicals
- Analyst coverage: 100% buy on top holdings with +22% price target, but only 17.2% of fund weight
- CFTC net long 8% of open interest, up 4.7% week‑over‑week
- Fund inflows: share count +2.3% weekly and +7.4% monthly

<details><summary><b>News</b> — score +0.00</summary>

- [META_TITLE_QUOTE](https://finance.yahoo.com/quote/EWZ/)  
  <sub>Yahoo Finance, 14 hours ago</sub>  
  EWZ tracks Brazilian equities through the MSCI Brazil Index. The latest political repricing triggered a sharp October selloff, while EWZ was down 1.60%...
- [Why Nomura says active beats passive in Japanese equities – and how its new ETF draws on local research](https://www.pionline.com/asset-management/exchange-traded-funds/pi-nomura-active-beats-passive-japan-equity-new-etf-launch/)  
  <sub>Pensions & Investments, 2 hours ago</sub>  
  Nomura Asset Management is leveraging its position as the largest asset manager in Japan to bring a new active Japan equity ETF to the U.S. — a strategy the...
- [Nikkei leads Asian sell-off after reports of Nvidia shake-up weigh on U.S. futures; Japan PPI beats forecasts](https://www.google.com/goto?url=CAESxAEBxCJF1_SKzuXbWw90Igi8dyzOpiI57iUAzsarEiFixfVzPWAAARUUdDnE5VCPnDspwJXOCCTkq-dlgeZTbrmFGcJ4UHJhAoZIAnhy2DpzeDNBbgY2B0lAcFj5P-mE2LwyY-kY_IzglvqQXejA8gL18ksKRApQzZzqz54J8fnYcNUcnicAyZJmRRAUzMYuO0hWA9cO1B6upZ742eJYwVD9cxrAVR7EPHiHdHotz5k6z4e9GB2ceGbhNfSyaDnSLYWheT_T&gsessionid=eQ7bPtdeNwCR0pOySjaFzWffmttFmEMO09u8sRGAWB7OkwosGyWN4g)  
  <sub>Seeking Alpha, 8 hours ago</sub>  
  Asian equity markets retreated across the board on Thursday, pressured by a drop in U.S. equity futures following reports of potential leadership turmoil at...
- [iShares MSCI EAFE ETF (EFA) Stock Price, News, Quote & History](https://www.google.com/goto?url=CAESZAHEIkXXTEiugFbArbhxBLGQdHiFlF1LMESLhMXciLUEsdl4MQVaWNTjLwQOcjoYDFEYXBU8mwvlcBcDQDYFs1oNIVRScmO40xF7Of1kHQvgxrXxWdAeSr4l_zq-xVjpBT7zEuU&gsessionid=eQ7bPtdeNwCR0pOySjaFzWffmttFmEMO09u8sRGAWB7OkwosGyWN4g)  
  <sub>Yahoo! Finance Canada, 19 hours ago</sub>  
  Find the latest iShares MSCI EAFE ETF (EFA) stock quote, history, news and other vital information to help you with your stock trading and investing.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.11% (+0.12 on the week) | 5-year 4.87% (+0.27 on the week) | 10-year 5.03% (+0.19 on the week) | 30-year 5.37% (+0.12 on the week)
Yield curve, 10-year minus 3-month: +0.92 points -- upward sloping (normal)
US dollar index: 102.91 (+1.36 on the week)
Volatility (VIX): 18.99 (-9.2 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.1% (2026-10-01) | jobless claims 200k (2026-11-07)
Policy and expectations: Fed target 4.00% | market expects 2.2% inflation over 10 years
Rate path: 2-year Treasury 4.56% vs Fed target 3.75-4.00% -- the bond market prices about 3 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score -0.20</summary>

```text
Last close 91.50 (bar of 2026-11-12), from 502 daily bars
Trend: vs 20d SMA 93.17 (-1.8%), 50d 95.77 (-4.5%), 200d 92.07 (-0.6%); 50d above 200d
Momentum: RSI(14) 43.0 | MACD -1.466 vs signal -1.338 (histogram -0.128)
Returns: 1d -0.7% | 5d +3.7% | 1m -4.5% | 3m -6.8%
52-week range: 79.49 - 99.32 (now 60.6% of the way up)
Volatility: ATR(14) 1.63 (1.8% of price) | annualised 20d 29.1%
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
Three-year record: +17.7% a year | beta to the market 0.86
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

<details><summary><b>What analysts and big funds say</b> — score +0.30</summary>

_Not available today._

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score +0.30</summary>

```text
Rolled up from the 5 largest holdings, 17.2% of the fund by weight  -- thin, so read this as a fact about that slice rather than the fund
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 1.64 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +22.1% above the current prices
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
Share count change: 1 week: +2.3% (533.05M) over 9d | 1 month: +7.4% (1.64B) over 30d
Shares outstanding: 259.14M | fund size: 23.71B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Switzerland (EWL) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Neutral overall: no macro surprise, flat fund flows, mixed analyst view, technicals lack decisive break.

**Main reasons it gave:**
- Fund flows flat: 0% change week and month
- Analyst coverage 49.6% of fund, 64.8% buy, 0% sell
- Technical price above 20d, 50d, 200d SMAs but 50d SMA below 200d SMA, low volume (0.10x 20‑day avg)
- US Treasury yields up across curve, no macro surprise

<details><summary><b>News</b> — score +0.00</summary>

_No news found for this one today._

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.11% (+0.12 on the week) | 5-year 4.87% (+0.27 on the week) | 10-year 5.03% (+0.19 on the week) | 30-year 5.37% (+0.12 on the week)
Yield curve, 10-year minus 3-month: +0.92 points -- upward sloping (normal)
US dollar index: 102.91 (+1.36 on the week)
Volatility (VIX): 18.99 (-9.2 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.1% (2026-10-01) | jobless claims 200k (2026-11-07)
Policy and expectations: Fed target 4.00% | market expects 2.2% inflation over 10 years
Rate path: 2-year Treasury 4.56% vs Fed target 3.75-4.00% -- the bond market prices about 3 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 65.16 (bar of 2026-11-12), from 502 daily bars
Trend: vs 20d SMA 64.13 (+1.6%), 50d 61.86 (+5.3%), 200d 61.98 (+5.1%); 50d below 200d
Momentum: RSI(14) 59.5 | MACD 1.069 vs signal 1.041 (histogram 0.028)
Returns: 1d +0.4% | 5d -0.4% | 1m +7.7% | 3m +3.0%
52-week range: 55.69 - 66.56 (now 87.1% of the way up)
Volatility: ATR(14) 0.86 (1.3% of price) | annualised 20d 19.8%
Volume: 0.10x the 20-day average
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
Three-year record: +17.3% a year | beta to the market 0.82
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
Ratings by weight: buy 64.8% | hold 35.2% | sell 0.0% (mean 2.45 on a 1=strong buy to 5=strong sell scale)
Weighted price target: -0.3% above the current prices
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
Shares outstanding: 28.62M | fund size: 1.87B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

**Data that was missing** (counted as 0.00, never guessed):
- news unavailable: Bright Data returned an empty body with its 200; nothing to parse (Bright Data said: x-brd-status-code 502; x-brd-error redirect location was rejected) (Bing's feed, direct: 2 headline(s), none naming EWL)

### Netherlands (EWN) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Mixed evidence: strong analyst buy rating on top holdings, flat fund flows, modestly positive fundamentals, but neutral technicals and no macro catalyst.

**Main reasons it gave:**
- Analyst view: 42.3% of fund weighted holdings all rated Buy with +53% price target
- Fund flows: flat share count (0% change) over past month
- Technical: price 0.1% above 200‑day SMA, RSI 49.3 (neutral), volume 0.03× 20‑day average
- Fund basics: P/E 18.38, dividend yield 4.4%, three‑year annualized return 21.3%
- Macro: Treasury yields up across curve, dollar index +1.36% on week, VIX 18.99 (down 9.2% but still elevated)

<details><summary><b>News</b> — score +0.00</summary>

_No news found for this one today._

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.11% (+0.12 on the week) | 5-year 4.87% (+0.27 on the week) | 10-year 5.03% (+0.19 on the week) | 30-year 5.37% (+0.12 on the week)
Yield curve, 10-year minus 3-month: +0.92 points -- upward sloping (normal)
US dollar index: 102.91 (+1.36 on the week)
Volatility (VIX): 18.99 (-9.2 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.1% (2026-10-01) | jobless claims 200k (2026-11-07)
Policy and expectations: Fed target 4.00% | market expects 2.2% inflation over 10 years
Rate path: 2-year Treasury 4.56% vs Fed target 3.75-4.00% -- the bond market prices about 3 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 65.23 (bar of 2026-11-12), from 502 daily bars
Trend: vs 20d SMA 64.80 (+0.7%), 50d 66.30 (-1.6%), 200d 65.16 (+0.1%); 50d above 200d
Momentum: RSI(14) 49.3 | MACD -0.291 vs signal -0.526 (histogram 0.234)
Returns: 1d -1.5% | 5d +3.2% | 1m +0.5% | 3m -8.9%
52-week range: 55.33 - 71.61 (now 60.8% of the way up)
Volatility: ATR(14) 1.10 (1.7% of price) | annualised 20d 25.1%
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
Three-year record: +21.3% a year | beta to the market 1.13
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

<details><summary><b>What analysts and big funds say</b> — score +0.60</summary>

_Not available today._

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score +0.60</summary>

```text
Rolled up from the 5 largest holdings, 42.3% of the fund by weight
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 1.58 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +53.1% above the current prices
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
Shares outstanding: 5.55M | fund size: 362.03M
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

**Data that was missing** (counted as 0.00, never guessed):
- news unavailable: Bright Data returned an empty body with its 200; nothing to parse (Bright Data said: x-brd-status-code 502; x-brd-error response body was rejected) (Bing's feed, direct: 3 headline(s), none naming EWN)

### Spain (EWP) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Neutral overall: analyst view moderately bullish but limited to 53% of holdings; fund flows flat indicating no net demand; technicals show price above moving averages but very low volume and near 52‑week high; macro data show rising US yields and a stronger dollar with no surprise, keeping risk appetite unchanged.

**Main reasons it gave:**
- Analyst coverage of top 5 holdings (53% weight) shows 76% buy and +6.2% price target
- Fund flows flat over the past week and month (0% share count change)
- Technicals: price above 20‑, 50‑, 200‑day SMAs and MACD positive, but volume only 5% of 20‑day average
- Macro: US yields rose across the curve, dollar up, no policy surprise; VIX down but still elevated

<details><summary><b>News</b> — score +0.00</summary>

- [西班牙ETF-iShares MSCI收跌0.68%，成交额6326.88万美元](http://www.bing.com/news/apiclick.aspx?ref=FexRss&aid=&tid=6af5d25efb2a442983086efe6302d4db&url=https%3a%2f%2ffinance.sina.com.cn%2fstock%2fusstock%2fnotice%2f2026-11-12%2fdoc-iniymmzr3981024.shtml&c=9566255541378824584&mkt=en-us)  
  <sub>新浪财经, 23h ago</sub>  
  11月12日，西班牙ETF-iShares MSCI（EWP）收跌0.68%，报59.92美元，成交额6326.88万美元，市值20.54亿美元。 声明：市场有风险，投资需谨慎。本文基于第三方数据库发布，不代表新浪财经观点，任何在本文出现的信息均只作为参考，不构成个人投资建议。如有出入请以实际公告为准。如有疑问，请联系biz@staff.sina.com.cn。

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.11% (+0.12 on the week) | 5-year 4.87% (+0.27 on the week) | 10-year 5.03% (+0.19 on the week) | 30-year 5.37% (+0.12 on the week)
Yield curve, 10-year minus 3-month: +0.92 points -- upward sloping (normal)
US dollar index: 102.91 (+1.36 on the week)
Volatility (VIX): 18.99 (-9.2 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.1% (2026-10-01) | jobless claims 200k (2026-11-07)
Policy and expectations: Fed target 4.00% | market expects 2.2% inflation over 10 years
Rate path: 2-year Treasury 4.56% vs Fed target 3.75-4.00% -- the bond market prices about 3 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 59.90 (bar of 2026-11-12), from 502 daily bars
Trend: vs 20d SMA 58.10 (+3.1%), 50d 59.30 (+1.0%), 200d 58.13 (+3.0%); 50d above 200d
Momentum: RSI(14) 57.5 | MACD 0.213 vs signal -0.210 (histogram 0.423)
Returns: 1d -0.0% | 5d +2.2% | 1m +3.4% | 3m -4.7%
52-week range: 49.37 - 63.23 (now 75.9% of the way up)
Volatility: ATR(14) 0.95 (1.6% of price) | annualised 20d 25.0%
Volume: 0.05x the 20-day average
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
Three-year record: +33.3% a year | beta to the market 0.91
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
Weighted price target: +6.2% above the current prices
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
Shares outstanding: 37.35M | fund size: 2.24B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Taiwan (EWT) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:** no explanation. It wrote only “NEUTRAL”, so the main reasons below are all it gave.

**Main reasons it gave:**
- Analyst view covers 37.7% of fund, 100% buy rating, +50% price target
- Fund flows: +7.6% net inflow over month but -4.5% outflow over week
- Technical: price below 20‑day (101.28) and 50‑day (108.08) SMAs, RSI 42.2, low volume
- Macro: yields up modestly across curve, no policy surprise; VIX down 9.2% but still elevated
- Fund basics: high valuation (P/E 27.3) and recent 1‑month -13.2% performance

<details><summary><b>News</b> — score +0.00</summary>

- [META_TITLE_QUOTE](https://finance.yahoo.com/quote/EWZ/)  
  <sub>Yahoo Finance, 14 hours ago</sub>  
  EWZ tracks Brazilian equities through the MSCI Brazil Index. The latest political repricing triggered a sharp October selloff, while EWZ was down 1.60%...
- [Pacer US Cash Cows Growth ETF (BUL) Stock Price, News, Quote & History](https://ca.finance.yahoo.com/quote/BUL/)  
  <sub>Yahoo! Finance Canada, 19 minutes ago</sub>  
  Find the latest Pacer US Cash Cows Growth ETF (BUL) stock quote, history, news and other vital information to help you with your stock trading and...
- [Themes Global Systemically Important Banks ETF (GSIB) Stock Price, News, Quote & History](https://www.google.com/goto?url=CAESZAHEIkXXFFBNca5fE_v6cLV1UQ2DXKp06wepUmVZRbDKADhMGQtalI4oAEk8BaD_GeuJ5_7EDoOaZgIGf11sH2uxzs7Li3uGgRT8rMT8GQRmUyNwBJa_hslNwCS_xnfwC3gU8qU&gsessionid=R0JQ8pmMhq3D6Ezf8B_2LEsG4a-1ZmVRVszeQh3MohA5Prr_d_eTHg)  
  <sub>Yahoo! Finance Canada, 51 minutes ago</sub>  
  Find the latest Themes Global Systemically Important Banks ETF (GSIB) stock quote, history, news and other vital information to help you with your stock...
- [United States Oil Fund, LP (USO) Stock Price, News, Quote & History](https://www.google.com/goto?url=CAESYwHEIkXXulsylgbD1CpEaXPuDVYIKiNiEF8iGr3X6g-dQfClD_IE6ODJPpxFUDtboHU8VjuQaj8xAFnp7_WjeYEuB0eh5Jz01Mlcwp99m1jR_BjPs3FV_i1tMOWMB7aAMawL7Q&gsessionid=R0JQ8pmMhq3D6Ezf8B_2LEsG4a-1ZmVRVszeQh3MohA5Prr_d_eTHg)  
  <sub>Yahoo! Finance Canada, 5 hours ago</sub>  
  Find the latest United States Oil Fund, LP (USO) stock quote, history, news and other vital information to help you with your stock trading and investing.
- [VanEck Digital Transformation ETF (DAPP) Stock Price, News, Quote & History](https://www.google.com/goto?url=CAESZAHEIkXXqlYCzGmgi7roQmqGlq9xYX_qHmFnysJZo8XGTlRvvNyCcR4AmvXPujTZfFZtIoJsYqG7QOZjPwdHcsiIQgl6PrZIwmBFBQmpRKuIZ1mlzHbXvirF5mJKaf4b6PW8JWQ&gsessionid=R0JQ8pmMhq3D6Ezf8B_2LEsG4a-1ZmVRVszeQh3MohA5Prr_d_eTHg)  
  <sub>Yahoo! Finance Canada, 14 hours ago</sub>  
  Find the latest VanEck Digital Transformation ETF (DAPP) stock quote, history, news and other vital information to help you with your stock trading and...
- [Direxion Daily Semiconductor Bear 3X Shares (SOXS) Stock Price, News, Quote & History](https://www.google.com/goto?url=CAESZAHEIkXXpDzqg28Xri91FFIu0Mec_ao3j_2gFpOPa7g5LxBBOf7r_4-83v6VSs0R11MMQOgtvEpNIo5rOwAW9koF2ikCh9KmtfMvJzPQdzRTeReTgBgc-AJsmb40bfWhBhP5ldg&gsessionid=R0JQ8pmMhq3D6Ezf8B_2LEsG4a-1ZmVRVszeQh3MohA5Prr_d_eTHg)  
  <sub>Yahoo! Finance Canada, 14 hours ago</sub>  
  Find the latest Direxion Daily Semiconductor Bear 3X Shares (SOXS) stock quote, history, news and other vital information to help you with your stock...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.11% (+0.12 on the week) | 5-year 4.87% (+0.27 on the week) | 10-year 5.03% (+0.19 on the week) | 30-year 5.37% (+0.12 on the week)
Yield curve, 10-year minus 3-month: +0.92 points -- upward sloping (normal)
US dollar index: 102.91 (+1.36 on the week)
Volatility (VIX): 18.99 (-9.2 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.1% (2026-10-01) | jobless claims 200k (2026-11-07)
Policy and expectations: Fed target 4.00% | market expects 2.2% inflation over 10 years
Rate path: 2-year Treasury 4.56% vs Fed target 3.75-4.00% -- the bond market prices about 3 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 96.26 (bar of 2026-11-12), from 502 daily bars
Trend: vs 20d SMA 101.28 (-5.0%), 50d 108.08 (-10.9%), 200d 94.53 (+1.8%); 50d above 200d
Momentum: RSI(14) 42.2 | MACD -4.052 vs signal -3.758 (histogram -0.294)
Returns: 1d -3.9% | 5d +12.1% | 1m -13.2% | 3m -10.1%
52-week range: 60.03 - 118.00 (now 62.5% of the way up)
Volatility: ATR(14) 3.93 (4.1% of price) | annualised 20d 64.9%
Volume: 0.34x the 20-day average
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
Three-year record: +35.6% a year | beta to the market 1.35
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
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 1.35 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +50.1% above the current prices
Holdings read: 2330.TW, 2454.TW, 2317.TW, 3711.TW, 2308.TW
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
Share count change: 1 week: -4.5% (-520.45M) over 9d | 1 month: +7.6% (789.80M) over 30d
Shares outstanding: 115.88M | fund size: 11.16B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### United Kingdom (EWU) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:** no explanation. It wrote only “NEUTRAL”, so the main reasons below are all it gave.

**Main reasons it gave:**
- No macro surprise: yields up modestly, VIX down but still elevated, no policy surprise
- Technicals show price above SMAs but RSI near 52 and low volume, no decisive break
- Fund flows net outflow of -1.3% over past month, indicating slight bearish sentiment
- Analyst coverage of top holdings (36.9% weight) is 100% buy with +14.4% price target, but limited coverage

<details><summary><b>News</b> — score +0.00</summary>

_No news found for this one today._

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.11% (+0.12 on the week) | 5-year 4.87% (+0.27 on the week) | 10-year 5.03% (+0.19 on the week) | 30-year 5.37% (+0.12 on the week)
Yield curve, 10-year minus 3-month: +0.92 points -- upward sloping (normal)
US dollar index: 102.91 (+1.36 on the week)
Volatility (VIX): 18.99 (-9.2 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.1% (2026-10-01) | jobless claims 200k (2026-11-07)
Policy and expectations: Fed target 4.00% | market expects 2.2% inflation over 10 years
Rate path: 2-year Treasury 4.56% vs Fed target 3.75-4.00% -- the bond market prices about 3 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 47.87 (bar of 2026-11-12), from 502 daily bars
Trend: vs 20d SMA 47.76 (+0.2%), 50d 47.43 (+0.9%), 200d 47.08 (+1.7%); 50d above 200d
Momentum: RSI(14) 52.0 | MACD 0.174 vs signal 0.162 (histogram 0.012)
Returns: 1d +0.1% | 5d -0.1% | 1m +2.0% | 3m -0.8%
52-week range: 41.34 - 49.39 (now 81.1% of the way up)
Volatility: ATR(14) 0.63 (1.3% of price) | annualised 20d 20.7%
Volume: 0.30x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.35</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score +0.35</summary>

```text
Fund type: Focused Region
What it holds: P/E 16.62 | P/B 2.25 | P/S 1.41 | 3y earnings growth n/a
Yield: 3.1%
Three-year record: +20.2% a year | beta to the market 0.66
Cost and size: expense ratio 0.50% | net assets 3.73B
What it is made of: Stocks 98.5%, Other 1.0%, Cash 0.5%
Largest holdings: Shell PLC 9.9%, HSBC Holdings PLC 9.3%, AstraZeneca PLC 8.9%, Unilever PLC 4.4%, Rolls-Royce Holdings PLC 4.4%
Sector mix: Financial services 23.2%, Consumer defensive 15.3%, Energy 14.3%, Healthcare 13.9%
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

<details><summary><b>What analysts and big funds say</b> — score +0.60</summary>

_Not available today._

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score +0.60</summary>

```text
Rolled up from the 5 largest holdings, 36.9% of the fund by weight
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 2.08 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +14.4% above the current prices
Holdings read: SHEL.L, HSBA.L, AZN.L, ULVR.L, RR.L
Recent rating changes among them:
  - AZN.L: 2026-08-24 CICC: init, ? -> Outperform
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
Share count change: 1 week: +1.5% (56.53M) over 9d | 1 month: -1.3% (-47.80M) over 30d
Shares outstanding: 78.11M | fund size: 3.74B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Mexico (EWW) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Neutral overall – no macro surprise, flat fund flows, and technicals lack decisive volume‑driven break despite modest bullish fundamentals and analyst view.

**Main reasons it gave:**
- No macro surprise: yields rose modestly, inflation and unemployment in line with expectations
- Fund flows flat over the past month, indicating no net demand
- Technicals: price above SMAs and positive momentum but volume at 0.03× 20‑day average, no decisive break
- Analyst view bullish for top holdings (100% buy, +9.2% target) but covers only 47.5% of the fund

<details><summary><b>News</b> — score +0.00</summary>

- [META_TITLE_QUOTE](https://finance.yahoo.com/quote/EWZ/)  
  <sub>Yahoo Finance, 14 hours ago</sub>  
  EWZ tracks Brazilian equities through the MSCI Brazil Index. The latest political repricing triggered a sharp October selloff, while EWZ was down 1.60%...
- [EWW Jan 2027 54.000 put (EWW270115P00054000) Interactive Stock Chart](https://ca.finance.yahoo.com/quote/EWW270115P00054000/chart/)  
  <sub>Yahoo! Finance Canada, 19 hours ago</sub>  
  Interactive Chart for EWW Jan 2027 54.000 put (EWW270115P00054000), analyze all the data with a huge range of indicators.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.11% (+0.12 on the week) | 5-year 4.87% (+0.27 on the week) | 10-year 5.03% (+0.19 on the week) | 30-year 5.37% (+0.12 on the week)
Yield curve, 10-year minus 3-month: +0.92 points -- upward sloping (normal)
US dollar index: 102.91 (+1.36 on the week)
Volatility (VIX): 18.99 (-9.2 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.1% (2026-10-01) | jobless claims 200k (2026-11-07)
Policy and expectations: Fed target 4.00% | market expects 2.2% inflation over 10 years
Rate path: 2-year Treasury 4.56% vs Fed target 3.75-4.00% -- the bond market prices about 3 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 77.59 (bar of 2026-11-12), from 502 daily bars
Trend: vs 20d SMA 75.77 (+2.4%), 50d 74.38 (+4.3%), 200d 76.20 (+1.8%); 50d below 200d
Momentum: RSI(14) 64.5 | MACD 0.946 vs signal 0.692 (histogram 0.253)
Returns: 1d -0.2% | 5d +2.0% | 1m +6.7% | 3m +3.4%
52-week range: 65.87 - 81.23 (now 76.3% of the way up)
Volatility: ATR(14) 1.31 (1.7% of price) | annualised 20d 14.2%
Volume: 0.03x the 20-day average
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
Three-year record: +13.5% a year | beta to the market 0.99
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

<details><summary><b>What analysts and big funds say</b> — score +0.45</summary>

_Not available today._

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score +0.45</summary>

```text
Rolled up from the 5 largest holdings, 47.5% of the fund by weight
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 2.05 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +9.2% above the current prices
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
Shares outstanding: 18.90M | fund size: 1.47B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### South Africa (EZA) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Neutral overall; no macro surprise, flat fund flows, mixed technicals, and bullish analyst view limited to 41.8% of holdings.

**Main reasons it gave:**
- Flat fund flows: 0% change in share count over 1 week and 1 month
- No macro surprise: Fed target unchanged at 4.00%, yields rose modestly
- Technical indicators: price above 20‑day SMA, MACD positive, but volume only 0.09× 20‑day average
- Analyst coverage: 100% buy rating on top holdings with +27.3% price target, covering 41.8% of fund

<details><summary><b>News</b> — score +0.00</summary>

_No news found for this one today._

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.11% (+0.12 on the week) | 5-year 4.87% (+0.27 on the week) | 10-year 5.03% (+0.19 on the week) | 30-year 5.37% (+0.12 on the week)
Yield curve, 10-year minus 3-month: +0.92 points -- upward sloping (normal)
US dollar index: 102.91 (+1.36 on the week)
Volatility (VIX): 18.99 (-9.2 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.1% (2026-10-01) | jobless claims 200k (2026-11-07)
Policy and expectations: Fed target 4.00% | market expects 2.2% inflation over 10 years
Rate path: 2-year Treasury 4.56% vs Fed target 3.75-4.00% -- the bond market prices about 3 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 65.89 (bar of 2026-11-12), from 502 daily bars
Trend: vs 20d SMA 65.03 (+1.3%), 50d 65.92 (-0.0%), 200d 68.11 (-3.3%); 50d below 200d
Momentum: RSI(14) 51.7 | MACD 0.502 vs signal 0.086 (histogram 0.415)
Returns: 1d -1.5% | 5d -1.5% | 1m +4.1% | 3m -2.4%
52-week range: 60.43 - 81.60 (now 25.8% of the way up)
Volatility: ATR(14) 1.49 (2.3% of price) | annualised 20d 29.6%
Volume: 0.09x the 20-day average
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
Three-year record: +27.4% a year | beta to the market 1.12
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

<details><summary><b>What analysts and big funds say</b> — score +0.50</summary>

_Not available today._

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score +0.50</summary>

```text
Rolled up from the 5 largest holdings, 41.8% of the fund by weight
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 1.99 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +27.3% above the current prices
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
Shares outstanding: 7.90M | fund size: 520.53M
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

**Data that was missing** (counted as 0.00, never guessed):
- news unavailable: Bright Data returned an empty body with its 200; nothing to parse (Bright Data said: x-brd-status-code 502; x-brd-error response body was rejected) (Bing's feed, direct: 2 headline(s), none naming EZA)

### Gold mining companies (GDX) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Neutral overall; bearish technicals and strong outflows offset bullish analyst view and solid fundamentals.

**Main reasons it gave:**
- Share count fell 19% in one week (large outflows)
- Price below 20‑day, 50‑day and 200‑day SMAs; RSI 46.5 (downtrend)
- Analyst consensus 100% buy with +19.1% price target for top holdings
- Gold price down 0.42% and higher yields/dollar pressure on miners
- No macro surprise or decisive technical break on heavy volume

<details><summary><b>News</b> — score +0.00</summary>

- [VanEck Gold Miners ETF (GDX) Stock Price, News, Quote & History](https://ca.finance.yahoo.com/quote/GDX/)  
  <sub>Yahoo! Finance Canada, 21 hours ago</sub>  
  VanEck Gold Miners ETF (GDX) ... This price reflects trading activity during the overnight session on the Blue Ocean ATS, available 8 PM to 4 AM ET, Sunday...
- [Form 4 iShares Semiconductor ETF For: 12 November By Investing.com](https://ng.investing.com/news/stock-market-news/form-4-ishares-semiconductor-etf-for-12-november-93CH-2801503)  
  <sub>Investing.com Nigeria, 9 hours ago</sub>  
  This pricing supplement, which is not complete and may be changed, relates to an effective Registration Statement under the Securities Act of 1933.
- [All that glitters isn’t gold as year-end bets turn cautious (XAUUSD:CUR:Commodity)](https://www.google.com/goto?url=CAESnQEBxCJF1zcYiv80uWlGDMqcOypVieksgFyz5aZIBqwi2nGmB-ITkH6UCsIv8DmCcz7XPN1RyeW2ixcPFylmofMWqJlNZQs3QPQkRNCkBU0r_6NDmXh4BA2Dk_QUNQOXRYyW0RUpKff-HvQ7ZtxF4sLiBXtaqxyT01jMUfxBNBwXM51qWHzSGdbgd6pk2X--bSmX_mrhS-IwuocCnomu&gsessionid=0y0iD-Mq7CcUPZVmK9mDvEQ_mg3PWAdZ5iYeS1LydPjW5yTdsKMHKA)  
  <sub>Seeking Alpha, 22 hours ago</sub>  
  Gold's remarkable rally has given way to a bruising reversal, leaving traders to weigh whether the metal can regain lost ground before the year ends.
- [Gold Price Forecast — XAU/USD ($4,013) Holds $4,000 as Fed Hike Odds Hit 100% — $4,300 Target](https://www.google.com/goto?url=CAESqAEBxCJF16CP9rWkJLSnP9HT7aFf23WQGnlG8-KnoOI1D5bvydwkjvLGA1h2VPqxi1mBWFL6dSrGvvdbtbFG-eV7aM_X5Swc5_bBjIqXQtg2FoVcLRrqH0qcoZwJO3QhSDw4r-t6tu9yUWzQNZwrRFLATlnYeVRn5zv2k9NubT2Cm_GU-RTpYyjZ4ffCgzAuDfeYVI9d232W9BoUM205zg4DOkpMKcbF55A&gsessionid=0y0iD-Mq7CcUPZVmK9mDvEQ_mg3PWAdZ5iYeS1LydPjW5yTdsKMHKA)  
  <sub>TradingNEWS, 20 hours ago</sub>  
  Trading News Gold trades at $4013, down 0.42%, after a $107.60 CPI-day drop, as December Fed hike odds reach 100% and the 10-year sits at 4.998% | That's .

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.11% (+0.12 on the week) | 5-year 4.87% (+0.27 on the week) | 10-year 5.03% (+0.19 on the week) | 30-year 5.37% (+0.12 on the week)
Yield curve, 10-year minus 3-month: +0.92 points -- upward sloping (normal)
US dollar index: 102.91 (+1.36 on the week)
Volatility (VIX): 18.99 (-9.2 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.1% (2026-10-01) | jobless claims 200k (2026-11-07)
Policy and expectations: Fed target 4.00% | market expects 2.2% inflation over 10 years
Rate path: 2-year Treasury 4.56% vs Fed target 3.75-4.00% -- the bond market prices about 3 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score -0.40</summary>

```text
Last close 83.16 (bar of 2026-11-12), from 502 daily bars
Trend: vs 20d SMA 83.82 (-0.8%), 50d 88.69 (-6.2%), 200d 89.72 (-7.3%); 50d below 200d
Momentum: RSI(14) 46.5 | MACD -0.600 vs signal -1.275 (histogram 0.675)
Returns: 1d -2.4% | 5d -3.0% | 1m -0.3% | 3m -7.6%
52-week range: 70.74 - 115.84 (now 27.5% of the way up)
Volatility: ATR(14) 3.53 (4.2% of price) | annualised 20d 56.6%
Volume: 0.14x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.50</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score +0.50</summary>

```text
Fund type: Equity Precious Metals
What it holds: P/E 12.25 | P/B 2.71 | P/S 3.99 | 3y earnings growth n/a
Yield: 0.8%
Three-year record: +48.7% a year | beta to the market 0.98
Cost and size: expense ratio 0.51% | net assets 23.82B
What it is made of: Stocks 99.8%, Cash 0.2%
Largest holdings: Newmont Corp 11.6%, Agnico Eagle Mines Ltd 11.3%, Barrick Mining Corp 8.2%, Wheaton Precious Metals Corp 5.5%, Franco-Nevada Corp 5.5%
Sector mix: Basic materials 100.0%
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

<details><summary><b>What analysts and big funds say</b> — score +0.60</summary>

_Not available today._

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score +0.60</summary>

```text
Rolled up from the 5 largest holdings, 42.0% of the fund by weight
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 1.71 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +19.1% above the current prices
Holdings read: NEM, AEM.TO, ABX.TO, WPM.TO, FNV.TO
Recent rating changes among them:
  - NEM: 2026-10-27 Scotiabank: main, Sector Outperform -> Sector Outperform
  - AEM.TO: 2026-11-02 Freedom Broker: up, Hold -> Buy
  - ABX.TO: 2026-11-10 JP Morgan: main, Overweight -> Overweight
  - WPM.TO: 2026-10-08 UBS: main, Buy -> Buy
  - FNV.TO: 2026-11-12 HC Wainwright & Co.: reit, Buy -> Buy
```

</details>

<details><summary><b>Buying and selling by company insiders</b> — score -0.80</summary>

_Not available today._

</details>

<details><summary><b>Who is positioned how</b> — score -0.80</summary>

_Not available today._

</details>

<details><summary><b>Money going into and out of this fund</b> — score -0.80</summary>

```text
Direction: money going out (1 month)
Share count change: 1 week: -19.0% (-5.34B) over 7d | 1 month: -7.0% (-1.73B) over 30d
Shares outstanding: 274.24M | fund size: 22.81B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Software (IGV) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Neutral overall; no macro surprise, mixed technicals, flat flows, and analyst bullishness limited to 42% of holdings.

**Main reasons it gave:**
- No macro surprise; yields rose modestly and Fed policy unchanged
- Technicals show short-term downtrend (price below 20‑day and 50‑day SMA, RSI 41.3) with low volume
- Fund flows flat over the past month, indicating no new demand
- Analyst coverage bullish for top holdings (100% buy, +32.6% price target) but covers only 42.2% of the fund

<details><summary><b>News</b> — score +0.00</summary>

- [Daily ETF Flows: $4B Flows Into SOXX](https://finance.yahoo.com/markets/options/articles/daily-etf-flows-4b-flows-235544540.html)  
  <sub>Yahoo Finance, 15 hours ago</sub>  
  Top 10 Creations (All ETFs). Ticker. Name. Net Flows ($, mm). AUM ($, mm). AUM % Change. SOXX · iShares Semiconductor ETF. 3,976.38. 41,502.53. 9.58%.
- [Cyber stocks catch wave and ride along as tech sector rallies](https://seekingalpha.com/news/4670907-cyber-stocks-catch-wave-and-ride-along-as-tech-sector-rallies)  
  <sub>Seeking Alpha, 20 hours ago</sub>  
  Cybersecurity stocks lead software gains Wednesday: Netskope rises 6%, SentinelOne and Fortinet gain 5%, while software ETF IGV adds 2.5%.
- [IGV Dec 2026 110.000 put (IGV261204P00110000) Stock Price, News, Quote & History](https://www.google.com/goto?url=CAEScwHEIkXXx9UPPwhxG8TSIS5wXHiqF8lTrBnptcei9KnT7ON9GdtKNuB3t3r-iWjixWmLlpGaDEz5Q7Q01H8dzu_yLNH8C1WPXAd74XqRqM2MbBbDiqBzkP9JEmeGfbeLP1ck-HvhHktbzO2e6QhYoGTdsnY&gsessionid=0VzLn2oUaKj7SsWShmvYZouCiCd2hPei2DdedP3E5U_gAdzbXYzdLQ)  
  <sub>Yahoo! Finance Canada, 24 hours ago</sub>  
  Find the latest IGV Dec 2026 110.000 put (IGV261204P00110000) stock quote, history, news and other vital information to help you with your stock trading and...
- [Ignitis Group AB (FRA:IGV) (Q3 2026) Earnings Call Highlights: E](https://www.google.com/goto?url=CAESvgIBxCJF1-ajlYjgvw3sH4PXjP04WqaQUiVmSnqUimC2TvdiuMmMb3sm5QppugB4RxWXIiDzzWaTowrkGR8RoRPad-sUv_uzDyosIfvPme3QGUmDqH3lhethvXvML38zj0g_EB7K_nFCfAaWXQLFMk_k0wj2QBw93B-aPE5giS5JlU7m3TDVCwoxmHPIgMM5ifL0hvXoGjyD-EEvtbD3_qaVeG5iUHASP3en5ROW456iOCKQpmZYWBWMZCZ6nvhb8nanOmitFKDlUe_5hpffWefG3JdMEm_Bp4WxurTDvMbmJlWEy_zOUuREoJ7-4CRt4XfnIA9M8OQ9y6O9MinDb8msD0LAv_i--4KAYK1N5h7ov35zD9ZqkkVsFXf-C672OpQqNK61Pfsxg9E209-9q-s2O4jcOLlNz-AL8KDQZUM&gsessionid=0VzLn2oUaKj7SsWShmvYZouCiCd2hPei2DdedP3E5U_gAdzbXYzdLQ)  
  <sub>GuruFocus, 18 hours ago</sub>  
  Adjusted EBITDA: EUR430.4 million, up 6% year-over-year.Adjusted Net Profit: EUR146 million, down 18% year-over-year, due to higher depreciation and...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.11% (+0.12 on the week) | 5-year 4.87% (+0.27 on the week) | 10-year 5.03% (+0.19 on the week) | 30-year 5.37% (+0.12 on the week)
Yield curve, 10-year minus 3-month: +0.92 points -- upward sloping (normal)
US dollar index: 102.91 (+1.36 on the week)
Volatility (VIX): 18.99 (-9.2 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.1% (2026-10-01) | jobless claims 200k (2026-11-07)
Policy and expectations: Fed target 4.00% | market expects 2.2% inflation over 10 years
Rate path: 2-year Treasury 4.56% vs Fed target 3.75-4.00% -- the bond market prices about 3 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score -0.20</summary>

```text
Last close 100.89 (bar of 2026-11-12), from 502 daily bars
Trend: vs 20d SMA 105.18 (-4.1%), 50d 106.22 (-5.0%), 200d 94.13 (+7.2%); 50d above 200d
Momentum: RSI(14) 41.3 | MACD -1.903 vs signal -1.263 (histogram -0.640)
Returns: 1d -1.3% | 5d +1.9% | 1m -6.3% | 3m -3.1%
52-week range: 74.67 - 112.67 (now 69.0% of the way up)
Volatility: ATR(14) 2.95 (2.9% of price) | annualised 20d 35.2%
Volume: 0.06x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score -0.10</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score -0.10</summary>

```text
Fund type: Technology
What it holds: P/E 30.79 | P/B 7.22 | P/S 8.03 | 3y earnings growth n/a
Yield: 0.0%
Three-year record: +11.3% a year | beta to the market 1.25
Cost and size: expense ratio 0.38% | net assets 13.46B
What it is made of: Stocks 99.9%, Cash 0.1%
Largest holdings: Palo Alto Networks Inc 9.1%, Palantir Technologies Inc Ordinary Shares - Class A 9.0%, Microsoft Corp 8.8%, CrowdStrike Holdings Inc Class A 8.6%, Oracle Corp 6.7%
Sector mix: Technology 94.4%, Communication services 3.6%, Financial services 1.7%, Consumer cyclical 0.2%
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
Rolled up from the 5 largest holdings, 42.2% of the fund by weight
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 1.62 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +32.6% above the current prices
Holdings read: PANW, PLTR, MSFT, CRWD, ORCL
Recent rating changes among them:
  - PANW: 2026-10-15 Citigroup: main, Buy -> Buy
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
Shares outstanding: 12.50M | fund size: 1.26B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### India (INDA) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:** no explanation. It wrote only “NEUTRAL”, so the main reasons below are all it gave.

**Main reasons it gave:**
- Fund flows: -10.2% share count over 1 month (outflows)
- US Treasury yields up (3‑month +0.12%, 5‑year +0.27%) and dollar index +1.36% on the week
- Technicals: RSI 75.2 (overbought) with volume 0.08x 20‑day average
- Analyst coverage thin (24.8% of fund weight) despite 100% buy rating and +14.4% price target

<details><summary><b>News</b> — score +0.00</summary>

- [Time to Consider India ETFs Amid AI Fatigue & Market Concentration?](http://www.bing.com/news/apiclick.aspx?ref=FexRss&aid=&tid=6af5d29cc1984a8a8245179b4ef03c2e&url=https%3a%2f%2fwww.msn.com%2fen-us%2fmoney%2ftop-stocks%2ftime-to-consider-india-etfs-amid-ai-fatigue-market-concentration%2far-AA2hejFQ&c=13678499685928769109&mkt=en-us)  
  <sub>Zacks Investment Research on MSN, 31h ago</sub>  
  Investors are increasingly reassessing their exposure to the crowded AI trade and the broader technology sector amid growing AI-related uncertainty. These developments could encourage a broader ...
- [These gold and silver ETFs accounted for 55% of trading turnover during Diwali week](http://www.bing.com/news/apiclick.aspx?ref=FexRss&aid=&tid=6af5d29cc1984a8a8245179b4ef03c2e&url=https%3a%2f%2fwww.cnbctv18.com%2fmarket%2fnippon-india-mutual-fund-gold-silver-etfs-accounted-55-pc-trading-turnover-diwali-week-20032643.htm&c=11236124792122908026&mkt=en-us)  
  <sub>CNBCTV18, 11h ago</sub>  
  Nippon India Mutual Fund Gold and Silver ETFs captured around 55 percent of average daily turnover on the NSE during the Diwali trading period.
- [India's 50 leading companies arrive on SGX: UTI India Nifty 50 Index ETF begins trading](http://www.bing.com/news/apiclick.aspx?ref=FexRss&aid=&tid=6af5d29cc1984a8a8245179b4ef03c2e&url=https%3a%2f%2fwww.manilatimes.net%2f2026%2f11%2f12%2ftmt-newswire%2fpr-newswire%2findias-50-leading-companies-arrive-on-sgx-uti-india-nifty-50-index-etf-begins-trading%2f2468016&c=9875522237607580746&mkt=en-us)  
  <sub>The Manila Times, 23h ago</sub>  
  The first Nifty 50 ETF listed in Singapore, and the first scheme authorized under the MAS Code on Collective Investment Schemes to feed directly into an India-domiciled fund ...
- [SGX Stock Exchange welcomes listing of UTI India Nifty 50 Index ETF](http://www.bing.com/news/apiclick.aspx?ref=FexRss&aid=&tid=6af5d29cc1984a8a8245179b4ef03c2e&url=https%3a%2f%2ffxnewsgroup.com%2fforex-news%2fexchanges%2fsgx-stock-exchange-welcomes-listing-of-uti-india-nifty-50-index-etf%2f&c=5395751866059042372&mkt=en-us)  
  <sub>FX News Group, 16h ago</sub>  
  SGX Stock Exchange today welcomed the listing of the UTI India Nifty 50 Index ETF, offering investors convenient access to India’s equity market.
- [SBI Mutual Fund launches SBI BSE India Defence ETF FOF](http://www.bing.com/news/apiclick.aspx?ref=FexRss&aid=&tid=6af5d29cc1984a8a8245179b4ef03c2e&url=https%3a%2f%2fwww.newsbytesapp.com%2fnews%2fbusiness%2fsbi-mutual-fund-launches-sbi-bse-india-defence-etf-fof%2ftldr&c=13862357232723388400&mkt=en-us)  
  <sub>NewsBytes, 19h ago</sub>  
  SBI Mutual Fund has introduced the SBI BSE India Defence ETF FOF, with the New Fund Offer available from November 16 to 30, 2026.
- [Bitcoin price today, November 12, 2026: BTC at $73,596 - check latest price in India, market trends & key drivers](http://www.bing.com/news/apiclick.aspx?ref=FexRss&aid=&tid=6af5d29cc1984a8a8245179b4ef03c2e&url=https%3a%2f%2fwww.msn.com%2fen-in%2fnews%2fother%2fbitcoin-price-today-november-12-2026-btc-at-73596-check-latest-price-in-india-market-trends-key-drivers%2far-AA2hgCYP&c=9349803732321185184&mkt=en-us)  
  <sub>The Sunday Guardian Live on MSN, 11h ago</sub>  
  India, Nov. 12 -- Bitcoin Price Today, November 12, 2026: Bitcoin (BTC) is trading near $73,596 globally as of November 12, 2026. In India, the live exchange rate converts to roughly Rs.68.99 lakh per ...
- [SBI Mutual Fund to launch defence sector fund of fund on November 16](http://www.bing.com/news/apiclick.aspx?ref=FexRss&aid=&tid=6af5d29cc1984a8a8245179b4ef03c2e&url=https%3a%2f%2fwww.cnbctv18.com%2fpersonal-finance%2fsbi-mutual-fund-launch-defence-sector-fund-of-fund-nfo-details-20032605.htm&c=747372147965638767&mkt=en-us)  
  <sub>CNBCTV18, 12h ago</sub>  
  SBI Mutual Fund launches an open-ended fund of fund investing in the SBI BSE India Defence ETF. NFO opens November 16 and closes November 30.
- [NIPPON INDIA MUTUAL FUND](http://www.bing.com/news/apiclick.aspx?ref=FexRss&aid=&tid=6af5d29cc1984a8a8245179b4ef03c2e&url=https%3a%2f%2fupstox.com%2fetfs%2fnippon-india-mutual-fund-share-price%2fINF204KB16U2%2f&c=480845957290489639&mkt=en-us)  
  <sub>upstox, 23h ago</sub>  
  NIPPON INDIA MUTUAL FUND share price is ₹51.54 as on 12 Nov, 2026 | 15:23 IST. What is the the 52-week high and low of NIPPON INDIA MUTUAL FUND shares ? The 52-week high and low of NIPPON INDIA MUTUAL ...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.11% (+0.12 on the week) | 5-year 4.87% (+0.27 on the week) | 10-year 5.03% (+0.19 on the week) | 30-year 5.37% (+0.12 on the week)
Yield curve, 10-year minus 3-month: +0.92 points -- upward sloping (normal)
US dollar index: 102.91 (+1.36 on the week)
Volatility (VIX): 18.99 (-9.2 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.1% (2026-10-01) | jobless claims 200k (2026-11-07)
Policy and expectations: Fed target 4.00% | market expects 2.2% inflation over 10 years
Rate path: 2-year Treasury 4.56% vs Fed target 3.75-4.00% -- the bond market prices about 3 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 51.53 (bar of 2026-11-12), from 502 daily bars
Trend: vs 20d SMA 48.68 (+5.9%), 50d 48.01 (+7.3%), 200d 49.11 (+4.9%); 50d below 200d
Momentum: RSI(14) 75.2 | MACD 1.102 vs signal 0.656 (histogram 0.445)
Returns: 1d -0.1% | 5d +3.0% | 1m +9.6% | 3m +3.5%
52-week range: 45.42 - 54.83 (now 65.0% of the way up)
Volatility: ATR(14) 0.55 (1.1% of price) | annualised 20d 16.4%
Volume: 0.08x the 20-day average
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
Three-year record: +5.4% a year | beta to the market 0.61
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

<details><summary><b>What analysts and big funds say</b> — score +0.35</summary>

_Not available today._

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score +0.35</summary>

```text
Rolled up from the 5 largest holdings, 24.8% of the fund by weight  -- thin, so read this as a fact about that slice rather than the fund
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 1.37 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +14.4% above the current prices
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
Share count change: 1 week: -5.0% (-310.11M) over 7d | 1 month: -10.2% (-666.55M) over 30d
Shares outstanding: 113.42M | fund size: 5.85B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Transport and delivery (IYT) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> No macro surprise, no decisive technical break, modest fund inflows, strong analyst buy rating but not enough to shift overall view.

**Main reasons it gave:**
- Analyst view: 90.9% buy rating, mean rating 1.87 (strong buy)
- Fund flows: share count increased 3.6% in the past week
- Technical: price above 20‑day, 50‑day, 200‑day SMAs, RSI 59.5, but volume 0.01× 20‑day average
- Macro: Treasury yields rose modestly, no policy surprise; inflation 3.7% in line with expectations

<details><summary><b>News</b> — score +0.00</summary>

- [META_TITLE_QUOTE](https://finance.yahoo.com/quote/IYT/)  
  <sub>Yahoo Finance, 14 hours ago</sub>  
  iShares U.S. Transportation ETF (IYT) · -0.62% · 5.41% · 5.53% · 13.39% · 16.73% · 22.06% · 525.85%. Baseline. OPEN_ADVANCED_CHART · ALPHASPACE_CHART.
- [How Does the iShares U.S. Transportation ETF (CBOE:IYT) Track Airlines, Railroads and Trucking Companies?](https://kalkine.com.au/news/mutual-funds-etfs/how-does-the-ishares-us-transportation-etf-cboeiyt-track-airlines-railroads-and-trucking-companies)  
  <sub>Kalkine, 4 hours ago</sub>  
  How Does the iShares U.S. Transportation ETF (CBOE:IYT) Track Airlines, Railroads and Trucking Companies?

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.11% (+0.12 on the week) | 5-year 4.87% (+0.27 on the week) | 10-year 5.03% (+0.19 on the week) | 30-year 5.37% (+0.12 on the week)
Yield curve, 10-year minus 3-month: +0.92 points -- upward sloping (normal)
US dollar index: 102.91 (+1.36 on the week)
Volatility (VIX): 18.99 (-9.2 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.1% (2026-10-01) | jobless claims 200k (2026-11-07)
Policy and expectations: Fed target 4.00% | market expects 2.2% inflation over 10 years
Rate path: 2-year Treasury 4.56% vs Fed target 3.75-4.00% -- the bond market prices about 3 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 84.54 (bar of 2026-11-12), from 502 daily bars
Trend: vs 20d SMA 81.93 (+3.2%), 50d 81.08 (+4.3%), 200d 81.98 (+3.1%); 50d below 200d
Momentum: RSI(14) 59.5 | MACD 0.864 vs signal 0.541 (histogram 0.323)
Returns: 1d +0.1% | 5d +3.1% | 1m +6.3% | 3m -3.3%
52-week range: 68.14 - 90.01 (now 75.0% of the way up)
Volatility: ATR(14) 1.52 (1.8% of price) | annualised 20d 27.5%
Volume: 0.01x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.25</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score +0.25</summary>

```text
Fund type: Industrials
What it holds: P/E 19.04 | P/B 4.01 | P/S 1.38 | 3y earnings growth n/a
Yield: 0.9%
Three-year record: +14.9% a year | beta to the market 1.24
Cost and size: expense ratio 0.37% | net assets 2.00B
What it is made of: Stocks 100.0%, Cash 0.0%
Largest holdings: Union Pacific Corp 18.7%, Uber Technologies Inc 13.8%, CSX Corp 10.0%, United Parcel Service Inc Class B 4.9%, Norfolk Southern Corp 4.8%
Sector mix: Industrials 85.3%, Technology 14.7%
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

<details><summary><b>What analysts and big funds say</b> — score +0.49</summary>

_Not available today._

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score +0.49</summary>

```text
Rolled up from the 5 largest holdings, 52.2% of the fund by weight
Ratings by weight: buy 90.9% | hold 9.1% | sell 0.0% (mean 1.87 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +15.1% above the current prices
Holdings read: UNP, UBER, CSX, UPS, NSC
Recent rating changes among them:
  - UNP: 2026-11-05 Baird: down, Outperform -> Neutral
  - UBER: 2026-11-06 UBS: main, Buy -> Buy
  - CSX: 2026-10-27 Susquehanna: main, Positive -> Positive
  - UPS: 2026-10-28 UBS: main, Buy -> Buy
  - NSC: 2026-10-23 Citigroup: main, Neutral -> Neutral
```

</details>

<details><summary><b>Buying and selling by company insiders</b> — score +0.36</summary>

_Not available today._

</details>

<details><summary><b>Who is positioned how</b> — score +0.36</summary>

_Not available today._

</details>

<details><summary><b>Money going into and out of this fund</b> — score +0.36</summary>

```text
Direction: money coming in (1 month)
Share count change: 1 week: +3.6% (70.76M) over 9d | 1 month: +1.7% (34.44M) over 30d
Shares outstanding: 23.92M | fund size: 2.02B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Saudi Arabia (KSA) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Neutral overall: no macro surprise, no decisive technical break, analyst view bullish but limited to 45% of fund, strong outflows and weak fundamentals pull the call toward bearish, netting a neutral stance.

**Main reasons it gave:**
- Analyst view: 90.6% buy rating and +15.8% price target for top holdings (45.3% weight)
- Fund flows: 8.2% share count decline in one week (≈$50.6M outflow)
- Fundamentals: weak 3‑year record (+0.2% annual) and high expense ratio (0.75%)
- Technicals: price below 200‑day SMA, low volume (0.04× 20‑day avg) despite short‑term RSI 61.3
- Macro: no surprise in rates or data; yields up modestly, VIX down

<details><summary><b>News</b> — score +0.00</summary>

- [Almarai : Ethiopian Ambassador to the Kingdom Visits Almarai’s Factories and Farms in Al Kharj](http://www.bing.com/news/apiclick.aspx?ref=FexRss&aid=&tid=6af5d2dbde4d4ea286bd6ddf4d60fd49&url=https%3a%2f%2fwww.marketscreener.com%2fnews%2falmarai-ethiopian-ambassador-to-the-kingdom-visits-almaraia-s-factories-and-farms-in-al-kharj-ce785ed8de88f426&c=9349025013949585087&mkt=en-us)  
  <sub>MarketScreener, 9h ago</sub>  
  The Ambassador of the Federal Democratic Republic of Ethiopia to the Kingdom of Saudi Arabia, H.E. Awwal Wagris Mohammed, accompanied by the Vice Chairman of Al Kharj Chamber of Commerce, visited ...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.11% (+0.12 on the week) | 5-year 4.87% (+0.27 on the week) | 10-year 5.03% (+0.19 on the week) | 30-year 5.37% (+0.12 on the week)
Yield curve, 10-year minus 3-month: +0.92 points -- upward sloping (normal)
US dollar index: 102.91 (+1.36 on the week)
Volatility (VIX): 18.99 (-9.2 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.1% (2026-10-01) | jobless claims 200k (2026-11-07)
Policy and expectations: Fed target 4.00% | market expects 2.2% inflation over 10 years
Rate path: 2-year Treasury 4.56% vs Fed target 3.75-4.00% -- the bond market prices about 3 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 36.12 (bar of 2026-11-12), from 502 daily bars
Trend: vs 20d SMA 34.79 (+3.8%), 50d 36.10 (+0.0%), 200d 37.80 (-4.4%); 50d below 200d
Momentum: RSI(14) 61.3 | MACD -0.062 vs signal -0.351 (histogram 0.289)
Returns: 1d +0.2% | 5d +3.3% | 1m +2.7% | 3m -4.5%
52-week range: 33.69 - 40.63 (now 34.9% of the way up)
Volatility: ATR(14) 0.35 (1.0% of price) | annualised 20d 16.9%
Volume: 0.04x the 20-day average
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
Three-year record: +0.2% a year | beta to the market 0.20
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

<details><summary><b>What analysts and big funds say</b> — score +0.60</summary>

_Not available today._

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score +0.60</summary>

```text
Rolled up from the 5 largest holdings, 45.3% of the fund by weight
Ratings by weight: buy 90.6% | hold 9.4% | sell 0.0% (mean 2.07 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +15.8% above the current prices
Holdings read: 1120.SR, 2222.SR, 1180.SR, 7010.SR, 1211.SR
Recent rating changes among them: none reported
```

</details>

<details><summary><b>Buying and selling by company insiders</b> — score -0.70</summary>

_Not available today._

</details>

<details><summary><b>Who is positioned how</b> — score -0.70</summary>

_Not available today._

</details>

<details><summary><b>Money going into and out of this fund</b> — score -0.70</summary>

```text
Direction: money going out (1 month)
Share count change: 1 week: -8.2% (-50.64M) over 7d | 1 month: -3.8% (-22.18M) over 30d
Shares outstanding: 15.68M | fund size: 566.31M
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### China (MCHI) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> The analyst view is bullish (100% buy on 32.6% coverage with a +66.5% price target), but the fund is experiencing strong outflows (‑11.4% week, ‑5.6% month) indicating bearish sentiment. Technicals show the price below short‑ and long‑term moving averages, low RSI and low volume, also bearish. Macro data show rising US yields, a stronger dollar and lower VIX, but no surprise events. The fundamentals (low valuation, low beta, modest yield) are neutral‑to‑slightly positive. The mixed signals lead to a neutral overall stance.

**Main reasons it gave:**
- Analyst view: 100% buy on 32.6% coverage, weighted price target +66.5% above current price
- Fund flows: outflows of -11.4% week and -5.6% month indicate bearish sentiment
- Technical trend: price below 20‑day, 50‑day, 200‑day SMAs, RSI 41.9, low volume
- Macro: US yields rising, dollar up, VIX down, no major surprise

<details><summary><b>News</b> — score +0.40</summary>

- [Can the iShares MSCI China ETF (NASDAQ:MCHI) Capture Chinese Companies Open to International Investors?](https://kalkine.com.au/news/mutual-funds-etfs/can-the-ishares-msci-china-etf-nasdaqmchi-capture-chinese-companies-open-to-international-investors)  
  <sub>Kalkine, 4 hours ago</sub>  
  Can the iShares MSCI China ETF (NASDAQ:MCHI) Capture Chinese Companies Open to International Investors?
- [How Does the iShares Core U.S. REIT ETF (NYSEARCA:USRT) Spread Holdings Across 122 Real Estate Companies?](https://kalkine.com.au/news/mutual-funds-etfs/how-does-the-ishares-core-us-reit-etf-nysearcausrt-spread-holdings-across-122-real-estate-companies)  
  <sub>Kalkine, 4 hours ago</sub>  
  You are reading a free article with opinions that may differ from the recommendation given by Kalkine in its paid research reports.
- [Can the iShares U.S. Small-Cap Equity Factor ETF (NYSEARCA:SMLF) Hold Nearly 1,000 Smaller American Companies?](https://www.google.com/goto?url=CAES0wEBxCJF17eeFMXq0CdPRqQlI7FhhZg15o73y3EuwaGLi0MMpWdrv5KO2fSLBUXBc_obEDJMgJ4L-YUvFOm-hiWQtSN9wWGry2VhA-HkCM67rHMFgbImDHNoFY4MqTDlq6oEemSO9_w2gWzk4YyRNGYiN6rSMv9wcl9VwOvi5l-VpZElf4UrKd3jmzCNbVxdfR0tWp5-jeFigYiXSfP5QgWlEXsFf9txDGizLWByHMdFxUrzYB5ZNTebjq3PU5d137aMkRzA-uq54ba_-DypqR5UW1aY&gsessionid=fW-WDcQiDYHTpo10vfAXGZnhk_e9g0deMNF45SKrse-bmXtg9XT-iw)  
  <sub>Kalkine, 4 hours ago</sub>  
  Can the iShares U.S. Small-Cap Equity Factor ETF (NYSEARCA:SMLF) Hold Nearly 1000 Smaller American Companies?
- [How Does the iShares U.S. Equity Factor ETF (NYSEARCA:LRGF) Combine Five Investment Factors in One Fund?](https://www.google.com/goto?url=CAESzgEBxCJF13NWyiMx_6E43K7TiQsyG872vfuBeJkwtkceTnZglhaeI369kWDXh-oxTNAHXrSMl0vNnFP61w58VQ8umuoPguSO-EiQJIocZXXc8xs_7Q8HkjwIqQ3MtsCW2oFoJqzCGP2Eaqsn_KMSfumni54XvGACgo2F5F1PVs0gaytJQAZt8J8xHTAd1f3dYW-Ko2XgU6exjWLVzTdm3XaZVpwThR-HZkCrX1UsuaWTfDusg1sTNgi8XJYwCxodVt8i9V7GoHXQSnQrnjWccQ&gsessionid=fW-WDcQiDYHTpo10vfAXGZnhk_e9g0deMNF45SKrse-bmXtg9XT-iw)  
  <sub>Kalkine, 4 hours ago</sub>  
  You are reading a free article with opinions that may differ from the recommendation given by Kalkine in its paid research reports.
- [Can the iShares Dow Jones U.S. ETF (NYSEARCA:IYY) Provide Broad Access to American Large and Mid-Cap Stocks?](https://www.google.com/goto?url=CAES0gEBxCJF11rtz_rZcWLZz785s2cmdpwW90sfxOEizrzGN_U4PA3y7nCrGNeHjtXPaunmGlTS15O_wLXPBNPkH2kzUCg1X-RXycnybv251IklnwBNYfwS4mWSCPEw0B5GM6DsJmu8kS-7Y6r8T4njJRKCHFt5WBQo4tMNafKYQDHV_wrl5xFr3Ed7KoKN4xIwbzGAEs8sSvYC18OxoE2fC9FNVolVGLur7RLsBZQWDOHa1DHdG-WpCD2goS_FtHAfn-pY4v4r39RD6AGnG3K0WImLT00&gsessionid=fW-WDcQiDYHTpo10vfAXGZnhk_e9g0deMNF45SKrse-bmXtg9XT-iw)  
  <sub>Kalkine, 4 hours ago</sub>  
  You are reading a free article with opinions that may differ from the recommendation given by Kalkine in its paid research reports.
- [How Does the iShares U.S. Transportation ETF (CBOE:IYT) Track Airlines, Railroads and Trucking Companies?](https://www.google.com/goto?url=CAESzgEBxCJF1xrw5XjP7qvyEpMtL2PycmPhWzLZ8XZ287DVpSKnhLYMrfIBkIUVGTDEtQRDa21l03mR-v30iT-Zqfaty3RhPIKjnbO_qCnCWpQU33dYwmn0iw1qUdQtgt7gsZvWVIifMLqJTKRRfFajA_Y39BfrFe-fWeoCX1BWqaOMHnrqyzlEpt6mZorzBkYrv4uvQM6QATsIGt--bXVtVS9kgtwdzOFsnAu7v0cc7dcGBUQaecWqQy9EicaaNAzQ3O-l8GuIxLchrRlZO036ig&gsessionid=fW-WDcQiDYHTpo10vfAXGZnhk_e9g0deMNF45SKrse-bmXtg9XT-iw)  
  <sub>Kalkine, 4 hours ago</sub>  
  How Does the iShares U.S. Transportation ETF (CBOE:IYT) Track Airlines, Railroads and Trucking Companies?
- [What Does the iShares U.S. Healthcare ETF (NYSEARCA:IYH) Concentrate On Within American Healthcare?](https://www.google.com/goto?url=CAESyQEBxCJF10ogJx0fc9-T5_30WcVZ630_ony9KsyaUpv3sWiTb1D6zF17M4_xzgeJEHjIHlmRkrX79AsTqi20zqe-PKD2pYSsXohZA0HF2MoXgwWnmxiapdLy-icCM1vJqmkIpL60MGgRzM8TlLPfEvSwnlQKj8c17ucFIh1bMGRuDbLBcpy7fnTmrTCZMD1g-TajYDNStZMF0t6FYVFrgW4y-eFWdJYGgbmIfzw78DszeQswf42TWU9uMaJaj5Dux70irqCsZg2ACt0&gsessionid=fW-WDcQiDYHTpo10vfAXGZnhk_e9g0deMNF45SKrse-bmXtg9XT-iw)  
  <sub>Kalkine, 4 hours ago</sub>  
  You are reading a free article with opinions that may differ from the recommendation given by Kalkine in its paid research reports.
- [How Does the iShares U.S. Financial Services ETF (NYSEARCA:IYG) Cover Banks, Exchanges and Payment Networks?](https://www.google.com/goto?url=CAES0QEBxCJF14UZc-dRO8G-SHC1jTii4UX6DqxktfFlb05gRW20ETemLwCEGdAofKCbYk3kU1kVx3eD1agbo39ZnqC6S5AapaEA0aicFZh2gWQ48FABCOLJFJg7WfsXCLB4dFveLA3e3zKOnCTkW7Fq-EW5JI4b96JVaLFUP1WpJVDlpU33y-PhFGrdTqO_6K47LQZ0y9dFJ59nvwZ5wmAIfsqk2nsF1ezFB7np4JUipAZFEDSopiAp-tMUJ8JuYJjQtn6yifdd-azNR6BwdKUTpG-yoQ&gsessionid=fW-WDcQiDYHTpo10vfAXGZnhk_e9g0deMNF45SKrse-bmXtg9XT-iw)  
  <sub>Kalkine, 4 hours ago</sub>  
  You are reading a free article with opinions that may differ from the recommendation given by Kalkine in its paid research reports.
- [How Does the iShares U.S. Thematic Rotation Active ETF (NYSEARCA:THRO) Shift Among Market Themes?](https://www.google.com/goto?url=CAESxwEBxCJF115rPGftmWnTXvsJbH9Xc4-yu6CICTzpQnLcRvYDqqKzlECN1W0PWi71_mrBZTAM0Tuwr8iuy0BS1Z2ttL7l-pnYm3tFYm8XUNWTJktVUHKqInyOhc5LDEInVybmoWwszMOhFZBx_pppDmjiFEFBGP2lPxRDs62-0glM_3UxLLb5ThCmo91tz6NGc0FB2JcUwsSt3fjZhW0_qs7p6C063zN5p_NglGLovOVXKi5PjKUmkuTzw652Njt9AQsdutfC0yNS&gsessionid=fW-WDcQiDYHTpo10vfAXGZnhk_e9g0deMNF45SKrse-bmXtg9XT-iw)  
  <sub>Kalkine, 4 hours ago</sub>  
  You are reading a free article with opinions that may differ from the recommendation given by Kalkine in its paid research reports.
- [How Does the iShares Global REIT ETF (NYSEARCA:REET) Reach Property Companies Across the World?](https://www.google.com/goto?url=CAESxwEBxCJF1zYNrUcdj-pjbQTgpnLgpJiK8P-4AWTtyS8npXtABfShQaaTpare4fukeodjra134Iga_HBOE7-t414ZfOciYnoSEGwxdkeZnR2lW1TLtZZB9LY8TLoIw5o60UQ4Xk5Vg43GFVKR9L56Me8AIvniGK_e6_JUE8Lui_ABMKYFDXCvRNwA4u_XEd2Qm23N1X9hKuMgFawIhXvba-PBakVqLZ_1Qb8FbMZHwTPuX_AfHjXucS860A233n2zQXzbtRGTLZ4f&gsessionid=fW-WDcQiDYHTpo10vfAXGZnhk_e9g0deMNF45SKrse-bmXtg9XT-iw)  
  <sub>Kalkine, 4 hours ago</sub>  
  You are reading a free article with opinions that may differ from the recommendation given by Kalkine in its paid research reports.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.40</summary>

```text
US Treasury yields: 3-month 4.11% (+0.12 on the week) | 5-year 4.87% (+0.27 on the week) | 10-year 5.03% (+0.19 on the week) | 30-year 5.37% (+0.12 on the week)
Yield curve, 10-year minus 3-month: +0.92 points -- upward sloping (normal)
US dollar index: 102.91 (+1.36 on the week)
Volatility (VIX): 18.99 (-9.2 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.1% (2026-10-01) | jobless claims 200k (2026-11-07)
Policy and expectations: Fed target 4.00% | market expects 2.2% inflation over 10 years
Rate path: 2-year Treasury 4.56% vs Fed target 3.75-4.00% -- the bond market prices about 3 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score -0.60</summary>

```text
Last close 49.88 (bar of 2026-11-12), from 502 daily bars
Trend: vs 20d SMA 50.20 (-0.6%), 50d 51.70 (-3.5%), 200d 55.19 (-9.6%); 50d below 200d
Momentum: RSI(14) 41.9 | MACD -0.227 vs signal -0.411 (histogram 0.185)
Returns: 1d -1.6% | 5d -4.2% | 1m -3.0% | 3m -8.7%
52-week range: 48.96 - 64.58 (now 5.9% of the way up)
Volatility: ATR(14) 0.69 (1.4% of price) | annualised 20d 21.3%
Volume: 0.20x the 20-day average
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
Three-year record: +9.1% a year | beta to the market 0.47
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

<details><summary><b>What analysts and big funds say</b> — score +0.40</summary>

_Not available today._

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score +0.40</summary>

```text
Rolled up from the 5 largest holdings, 32.6% of the fund by weight
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 1.42 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +66.5% above the current prices
Holdings read: 0700.HK, 9988.HK, 00939, 01398, 1810.HK
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
Share count change: 1 week: -11.4% (-690.84M) over 7d | 1 month: -5.6% (-318.27M) over 30d
Shares outstanding: 107.28M | fund size: 5.35B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Chip makers (SMH) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:** no explanation. It wrote only “NEUTRAL”, so the main reasons below are all it gave.

**Main reasons it gave:**
- No macro surprise: yields up modestly, VIX down, inflation stable
- Technicals: price below 20‑day, 50‑day, 200‑day SMAs; RSI 42.3; MACD negative
- Fund flows: net inflow +10.6% over month, weekly outflow -4.1%
- Analyst view: 100% buy, weighted price target +58% above current, coverage 46.4% of fund
- Fundamentals: strong growth record (+46.1% yr), high valuation (P/E 28.2, P/B 9.8)

<details><summary><b>News</b> — score +0.00</summary>

- [Why Retirees Should Still Own Chip Stocks In 2027 (NASDAQ:SMH)](https://seekingalpha.com/article/4966882-why-retirees-should-still-own-chip-stocks-in-2027?source=feed_all_articles)  
  <sub>Seeking Alpha, 4 hours ago</sub>  
  The bull case for semiconductor ETFs in retirement: a 5% allocation targets growth as AI capex fuels projected 41% tech earnings growth by 2027.
- [Semiconductor ETFs to Buy as Qualcomm Plunges Despite Q4 Earnings Beat](https://www.tradingview.com/news/zacks:97fdf40f5094b:0-semiconductor-etfs-to-buy-as-qualcomm-plunges-despite-q4-earnings-beat/)  
  <sub>TradingView, 4 hours ago</sub>  
  Shares of Qualcomm QCOM plunged 9.5% on Nov. 5, despite the company delivering better-than-expected fourth-quarter fiscal 2026 revenues and earnings.
- [Nasdaq 100 Jumps 2.8% as CoreWeave, Nvidia Climb: Stock Market Today](https://www.google.com/goto?url=CAESuQEBxCJF12FgQDZW8ODJQR5kxZuVQcxOQxBRP5Ur-8_-MoHuT9OsS0t2EMEkHhpjWhySZJH_GMidLg3gQongiHI25rLVzvUIV4s6jTemNhiQgREetZMLF9dnhQjLsrlEp7Tkg1hPKWlIq9Yn1DwXhpVVokpZoFRrTy1c-oPLDPatZIaTjE-Gx1AXZGYC3uMuzVvL1gXaef5WGg26KQTWSj7Lsn9fL5RSy48kGDchAmFggMmN7CsdnM_kPg&gsessionid=bvPtwWGEFbHE3pwHht227ySFWbzpOEhwMlfDaaM1Qu3PbJD0oCqr8w)  
  <sub>TradingView, 21 hours ago</sub>  
  The Nasdaq 100 rose 2.8% to 28509. Chipmakers did the heavy lifting. The VanEck Semiconductor ETF NASDAQ:SMH jumped 6.3%, and Micron Technology Inc.
- [CoreWeave's strong results lift chip stocks; Micron leads Quant rankings (SMH:NASDAQ)](https://www.google.com/goto?url=CAESqQEBxCJF19KNbWlRld42f5oap4J6v4hmHkOmh1HKZ1z1wH8KvlMinKLfnrNm63vUoN8s0AkDGCq4PVRIflyxoaX8CLGWQnwtdMXY0PkIYQj9JHjYfJyAZozwFk9uZua-oD3FwGahkuyTsitzhFQhK36V9zvXQ371bDy5l_jOSXJ1Qog1cItFL83jVwHdtSphSD9VmyqJJyM-jS_kbvhQbHRQWhfG_tH9QpAu&gsessionid=bvPtwWGEFbHE3pwHht227ySFWbzpOEhwMlfDaaM1Qu3PbJD0oCqr8w)  
  <sub>Seeking Alpha, 23 hours ago</sub>  
  Micron tops Seeking Alpha's semiconductor rankings at 4.99, ahead of AMD at 4.98, as CoreWeave's strong results ease AI spending concerns.
- [ETFs & Nvidia: Midterms, Investigations & Dip Buyers](https://www.google.com/goto?url=CAESnQEBxCJF19hiPDo1Wszfxht704nRAtMfGXC8DeMxyXACCzyX1NHkqBXUPyJpAMAcUbmty9_yZGT5GjD8uK2tvqpNqVhf04T_LrpRMORQLy7Xl64b44vaW-9mOI8eEv0Z4vC6MMg5XEa9ZSlGCJjBAtm6UEAdz-ae0PJT6l3EF3onuRAvnYKmz9F34Swfvv8ZG1cY6N9n0OiMnBk2-Y8x&gsessionid=bvPtwWGEFbHE3pwHht227ySFWbzpOEhwMlfDaaM1Qu3PbJD0oCqr8w)  
  <sub>ETF Trends, 3 hours ago</sub>  
  The Nvidia investigation and midterm uncertainty highlight ETF concentration risks as tech and semiconductor inflows signal continued demand.
- [Daily ETF Flows: $4B Flows Into SOXX](https://www.google.com/goto?url=CAEShwEBxCJF1xoR18MVKg0WOUZzjVIzPuRZGKFenHD5cGu47RUb-5CRBEFTWZhxlleYTUa93d9dT4ioPdgU9w6m0v0aHkh9XxKoUEcZ_ORJZYraw18ACCCUypOeZzecsX3iZv4u7qj4GExZNeZ5xnjB7J4oZt9sRKimJSm3FRLtf3J1_91O3Ma4JXQ&gsessionid=bvPtwWGEFbHE3pwHht227ySFWbzpOEhwMlfDaaM1Qu3PbJD0oCqr8w)  
  <sub>ETF.com, 20 hours ago</sub>  
  Here are the daily ETF fund flows for November 10, 2026.
- [SMH draws bullish trade interest as late-2026 semiconductor outlook steadies amid correction and valuation risks](https://www.google.com/goto?url=CAES3AEBxCJF11tk0g9F8_mhAYE2QSMGbp12zaEgu-xIBR9x1H_CpsqcoNDbiCTmU6ohbCR34UGjmBmw1-QNXbEh6Nwo2TF8UNhdf9Ll9ksXZhGpr1bmZ0xjJFddWGbxxKJ0sOusM45o29dsb3jdTr0zQ2Mu-Fjj3vdOvkkUvPIQFGsX7ZSAc_Q1xK5DeAGudkXg_58QUqhlO1wfOanT8CIm8yfogI3iUk2B1F6FYPkzZwIuMCrZY5ioNGEAPUnD8OZNoTlMCM_ZIL6GVAua6s74dd5oNkjk5-nriqN5jd8r&gsessionid=bvPtwWGEFbHE3pwHht227ySFWbzpOEhwMlfDaaM1Qu3PbJD0oCqr8w)  
  <sub>VT Markets, 21 hours ago</sub>  
  Analysts expect resilient AI-driven semiconductor demand into 2026; SMH correction offers bullish setups within key support.
- [IVES: Both The AI Bulls And Bears Can Take A Hard Pass](https://www.google.com/goto?url=CAESmwEBxCJF166XMNWeN0FfzSHT5Y1gjYZkiS74xvMJygVQjP90_5_o2b5kinYqC-BxwEb788cOgYTG9r03XhvE6lKtSN4UQqxsOSsP6in618Cl8Cyid3Cith2UtQ3UrBX-AscCKbqr1urle_I7kZrN7o9uP45QhzIIkliHcgub36a93lRv8_n1_cRNWaVCOJnZG4pXZl3mBLJwLHnm_Q&gsessionid=bvPtwWGEFbHE3pwHht227ySFWbzpOEhwMlfDaaM1Qu3PbJD0oCqr8w)  
  <sub>Seeking Alpha, 4 hours ago</sub>  
  Dan IVES Wedbush AI Revolution ETF offers no incremental upside versus low-cost alternatives and should be avoided by AI bulls and bears.
- [Nasdaq 100 Futures Drop As Reports Relating To Jensen Huang’s Ousting Outweigh CoreWeave’s Strong Outlook — NVDA, TSLA, SNDK, CAPR, CRWV In Focus](https://www.google.com/goto?url=CAEShgIBxCJF10miRERWWvIJGj0S9fdnfbTQoK08LnVXm55cPushAeyTbkqCQdgxVMhpbiq7d0pvWjV6cdqnn9se8H_i04t2vLnecZKRDHS8hxRqmVNRVfGsF4YJ7CfiLYCZaL4b72_iChHUkmrud5fBCP1paSEXUmS7pNwznTp5M-S8RpfPFU3roitHb7EwEvGfyc-GfjXi40YBt6RBAY826qgh4MFruYlkELin5WbaINlIROF_ys-Jc9hsXmdoJnRFJ612fFx-lLvn7V9caEfwhTraPfoULN6P_DCfuMM2D92uFG_C5g-edroufWb7IRA2Kh5GPoZHSPYYOcmncbnoUrPH9C2yhwDY&gsessionid=bvPtwWGEFbHE3pwHht227ySFWbzpOEhwMlfDaaM1Qu3PbJD0oCqr8w)  
  <sub>TradingView, 14 hours ago</sub>  
  U.S. stock indices ended higher on Wednesday, as an upbeat outlook from CoreWeave aided overall AI sentiment; however, stock futures dipped after-hours amid...
- [The growth vs. value 10-year uptrend has been ‘so far, so perfect’ (IWF:NYSEARCA)](https://www.google.com/goto?url=CAESoQEBxCJF1wOkFVF9yYHbK56VmnZ8YecmmectwUKD8lYvRrCd2kvmWiQQs_tU2hlUjEPN9ciFgEfkPYyk8s_lCLDE8BXioP32JbYJPZvKIPPncKucVO09VVbPOBrqLe5ufgl7HoOOjGWJJQZarRhhI_1QQOeQTNh0TpJN8K7p2hucxCXt0-xBrDxFEvI5huHNaClm57caEyfh6rIyZ3ChUr0vMg&gsessionid=bvPtwWGEFbHE3pwHht227ySFWbzpOEhwMlfDaaM1Qu3PbJD0oCqr8w)  
  <sub>Seeking Alpha, 12 minutes ago</sub>  
  The 10-year growth-versus-value uptrend remains intact, while semiconductor ETFs are up nearly 20% from local lows amid AI volatility.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.11% (+0.12 on the week) | 5-year 4.87% (+0.27 on the week) | 10-year 5.03% (+0.19 on the week) | 30-year 5.37% (+0.12 on the week)
Yield curve, 10-year minus 3-month: +0.92 points -- upward sloping (normal)
US dollar index: 102.91 (+1.36 on the week)
Volatility (VIX): 18.99 (-9.2 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.1% (2026-10-01) | jobless claims 200k (2026-11-07)
Policy and expectations: Fed target 4.00% | market expects 2.2% inflation over 10 years
Rate path: 2-year Treasury 4.56% vs Fed target 3.75-4.00% -- the bond market prices about 3 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 497.74 (bar of 2026-11-12), from 502 daily bars
Trend: vs 20d SMA 520.59 (-4.4%), 50d 561.04 (-11.3%), 200d 523.52 (-4.9%); 50d above 200d
Momentum: RSI(14) 42.3 | MACD -23.293 vs signal -21.750 (histogram -1.543)
Returns: 1d -1.8% | 5d +11.2% | 1m -11.9% | 3m -15.3%
52-week range: 325.10 - 668.91 (now 50.2% of the way up)
Volatility: ATR(14) 23.69 (4.8% of price) | annualised 20d 66.1%
Volume: 0.14x the 20-day average
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
Three-year record: +46.1% a year | beta to the market 2.12
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

<details><summary><b>What analysts and big funds say</b> — score +0.70</summary>

_Not available today._

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score +0.70</summary>

```text
Rolled up from the 5 largest holdings, 46.4% of the fund by weight
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 1.37 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +58.0% above the current prices
Holdings read: NVDA, TSM, TXN, AVGO, AMD
Recent rating changes among them:
  - NVDA: 2026-11-12 Stifel: main, Buy -> Buy
  - TSM: 2026-11-04 Bernstein: main, Outperform -> Outperform
  - TXN: 2026-10-22 Jefferies: main, Hold -> Hold
  - AVGO: 2026-10-27 Rosenblatt: main, Buy -> Buy
  - AMD: 2026-11-12 William Blair: up, Market Perform -> Outperform
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
Share count change: 1 week: -4.1% (-2.95B) over 9d | 1 month: +10.6% (6.57B) over 30d
Shares outstanding: 137.31M | fund size: 68.35B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Turkey (TUR) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> The analyst view is strongly bullish (100% buy, +28.8% price target) but only covers 44.9% of the fund, while fund flows are flat (neutral demand). Technicals show price above the 20‑day SMA but below the 50‑day and 200‑day SMAs with low volume, indicating no decisive breakout. Macro conditions (rising US yields, stronger dollar) present headwinds for emerging markets, and fundamentals are mixed (low P/E 11.63 but negative 3‑year return and high expense ratio). These factors balance out, leading to a neutral overall stance.

**Main reasons it gave:**
- Analyst view: 44.9% coverage, 100% buy, price target +28.8% above current price
- Fund flows: flat (0% change) over 1 week and 1 month
- Technicals: price above 20‑day SMA but below 50‑day and 200‑day SMA, low volume
- Macro: US yields rising, dollar index up 1.36% week, VIX down but still elevated

<details><summary><b>News</b> — score +0.00</summary>

- [TUR May 2027 37.000 call (TUR270521C00037000) Interactive Stock Chart](https://ca.finance.yahoo.com/quote/TUR270521C00037000/chart/)  
  <sub>Yahoo! Finance Canada, 21 hours ago</sub>  
  Interactive Chart for TUR May 2027 37.000 call (TUR270521C00037000), analyze all the data with a huge range of indicators.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.11% (+0.12 on the week) | 5-year 4.87% (+0.27 on the week) | 10-year 5.03% (+0.19 on the week) | 30-year 5.37% (+0.12 on the week)
Yield curve, 10-year minus 3-month: +0.92 points -- upward sloping (normal)
US dollar index: 102.91 (+1.36 on the week)
Volatility (VIX): 18.99 (-9.2 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.1% (2026-10-01) | jobless claims 200k (2026-11-07)
Policy and expectations: Fed target 4.00% | market expects 2.2% inflation over 10 years
Rate path: 2-year Treasury 4.56% vs Fed target 3.75-4.00% -- the bond market prices about 3 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 32.01 (bar of 2026-11-12), from 502 daily bars
Trend: vs 20d SMA 31.25 (+2.4%), 50d 34.38 (-6.9%), 200d 38.65 (-17.2%); 50d below 200d
Momentum: RSI(14) 48.1 | MACD -0.700 vs signal -1.078 (histogram 0.378)
Returns: 1d +0.4% | 5d +5.0% | 1m -4.8% | 3m -19.1%
52-week range: 29.53 - 43.74 (now 17.5% of the way up)
Volatility: ATR(14) 0.67 (2.1% of price) | annualised 20d 37.0%
Volume: 0.19x the 20-day average
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
Three-year record: -0.8% a year | beta to the market 0.60
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

<details><summary><b>What analysts and big funds say</b> — score +0.50</summary>

_Not available today._

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score +0.50</summary>

```text
Rolled up from the 5 largest holdings, 44.9% of the fund by weight
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 1.65 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +28.8% above the current prices
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
Shares outstanding: 15.65M | fund size: 500.96M
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### US real estate (VNQ) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Neutral overall as no macro surprise or decisive technical break; mixed fundamentals and modest bearish flow offset bullish analyst view

**Main reasons it gave:**
- US Treasury yields rose across the curve (+0.12 to +0.27) indicating higher rates for REITs
- Fund flows show net outflow over the month (-2.3%) indicating bearish sentiment
- Technical momentum is positive (RSI 62.9, MACD above signal) but volume is low (0.06x 20‑day average)
- Analyst coverage is bullish (100% buy, price target +12.6%) but only covers 40.5% of the fund

<details><summary><b>News</b> — score +0.00</summary>

- [Vanguard Real Estate Index Fund ETF Shares](http://www.bing.com/news/apiclick.aspx?ref=FexRss&aid=&tid=6af5d1e82dfe47ebab2ecdc9db13bff3&url=https%3a%2f%2fmarkets.ft.com%2fdata%2fetfs%2ftearsheet%2fsummary%3fs%3dVNQ&c=13231636711615488534&mkt=en-us)  
  <sub>FT Markets, 26h ago</sub>  
  Pricing for ETFs is the latest price and not "real time". Share price information may be rounded up/down and therefore not entirely accurate. FT is not responsible for any use of content by you ...
- [The U.S. CRE Health Index: Taking The Market's Pulse](http://www.bing.com/news/apiclick.aspx?ref=FexRss&aid=&tid=6af5d1e82dfe47ebab2ecdc9db13bff3&url=https%3a%2f%2fseekingalpha.com%2farticle%2f4966840-us-cre-health-index-taking-the-markets-pulse&c=443331111450637555&mkt=en-us)  
  <sub>Seeking Alpha, 14h ago</sub>  
  The U.S. CRE Health Index currently scores U.S. commercial real estate at 46 out of 100, placing the market on the slightly cautious side of neutral.
- [不动产信托指数ETF-Vanguard收跌0.06%，成交额2.95亿美元](http://www.bing.com/news/apiclick.aspx?ref=FexRss&aid=&tid=6af5d1e82dfe47ebab2ecdc9db13bff3&url=https%3a%2f%2ffinance.sina.com.cn%2fstock%2fusstock%2fnotice%2f2026-11-12%2fdoc-iniymmzq8640280.shtml&c=14446474179528426274&mkt=en-us)  
  <sub>新浪财经, 23h ago</sub>  
  11月12日，不动产信托指数ETF-Vanguard（VNQ）收跌0.06%，报97.02美元，成交额2.95亿美元，市值389.65亿美元。 声明：市场有风险，投资需谨慎。本文基于第三方数据库发布，不代表新浪财经观点，任何在本文出现的信息均只作为参考，不构成个人投资建议。如有出入请以实际公告为准。如有疑问，请联系biz@staff.sina.com.cn。

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.11% (+0.12 on the week) | 5-year 4.87% (+0.27 on the week) | 10-year 5.03% (+0.19 on the week) | 30-year 5.37% (+0.12 on the week)
Yield curve, 10-year minus 3-month: +0.92 points -- upward sloping (normal)
US dollar index: 102.91 (+1.36 on the week)
Volatility (VIX): 18.99 (-9.2 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.1% (2026-10-01) | jobless claims 200k (2026-11-07)
Policy and expectations: Fed target 4.00% | market expects 2.2% inflation over 10 years
Rate path: 2-year Treasury 4.56% vs Fed target 3.75-4.00% -- the bond market prices about 3 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 97.03 (bar of 2026-11-12), from 502 daily bars
Trend: vs 20d SMA 94.26 (+2.9%), 50d 92.98 (+4.4%), 200d 94.86 (+2.3%); 50d below 200d
Momentum: RSI(14) 62.9 | MACD 1.346 vs signal 0.975 (histogram 0.372)
Returns: 1d +0.0% | 5d +0.8% | 1m +7.4% | 3m -1.8%
52-week range: 87.00 - 100.95 (now 71.9% of the way up)
Volatility: ATR(14) 1.40 (1.4% of price) | annualised 20d 19.7%
Volume: 0.06x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.20</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score +0.20</summary>

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
Rolled up from the 5 largest holdings, 40.5% of the fund by weight
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 1.56 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +12.6% above the current prices
Holdings read: VRTPX, WELL, PLD, EQIX, AMT
Recent rating changes among them:
  - WELL: 2026-11-11 UBS: main, Buy -> Buy
  - PLD: 2026-11-02 Wells Fargo: main, Overweight -> Overweight
  - EQIX: 2026-10-29 JP Morgan: main, Overweight -> Overweight
  - AMT: 2026-11-05 Argus Research: reit, Buy -> Buy
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
Share count change: 1 week: +1.2% (805.70M) over 9d | 1 month: -2.3% (-1.66B) over 30d
Shares outstanding: 715.48M | fund size: 69.42B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Biotech (XBI) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> No macro surprise, mixed technicals, thin analyst coverage, but strong inflows and modestly positive fundamentals lead to a neutral overall view.

**Main reasons it gave:**
- Share count up 5.3% in the past week (strong inflows)
- Analyst coverage thin (9.5% of fund) with 75% buy rating and +12.9% price target
- Price below 20‑day and 50‑day SMAs (-0.6% and -1.5%) indicating slight short‑term weakness
- Biotech sector strong: Bank of America notes biotech stocks among market's stronger performers
- No macro surprise: yields up modestly, VIX down, inflation and unemployment stable

<details><summary><b>News</b> — score +0.00</summary>

- [Drug Makers or Biotech Bets: Which ETF Is the Better Buy, State Street’s XPH or First Trust’s FBT?](https://finance.yahoo.com/healthcare/articles/drug-makers-biotech-bets-etf-221327235.html)  
  <sub>Yahoo Finance, 17 hours ago</sub>  
  State Street SPDR S&P Pharmaceuticals ETF (NYSEMKT:XPH) provides broad, low-cost exposure to the pharmaceutical industry, while First Trust NYSE Arca...
- [ETFs Investing in Achieve Life Sciences, Inc. Stocks](https://www.tradingview.com/symbols/BOATS-QUIT/etfs/)  
  <sub>TradingView, 22 hours ago</sub>  
  Explore funds investing in QUIT in a single list with price, expense ratio, and more stats for an in-depth analysis of new opportunities.
- [XBI Jan 2028 83.000 call (XBI280121C00083000) Interactive Stock Chart](https://www.google.com/goto?url=CAESeAHEIkXXAB5jNNvcb6whZKxjECRyYfwK8L7KZ-Ujaxcu5KlQ1_pgITuec5jJQYP1pk8R1TXTh5BVpmTJMXCPLNZ5A1JzCQSJYNvWraxiucIodxHKeWaPi7ZirdlOIGxw3zyQEV4v1mSlmSKVj8kCnX-m1Z8GrFFz6A&gsessionid=ti02ijkt9MIEFVYXmgGQg1X4w3cvlbWb9BzBOfrrn3Bt4ChBrrQCbw)  
  <sub>Yahoo! Finance Canada, 20 hours ago</sub>  
  Interactive Chart for XBI Jan 2028 83.000 call (XBI280121C00083000), analyze all the data with a huge range of indicators.
- [XBI Dec 2026 200.000 call (XBI261211C00200000) Stock Price, News, Quote & History](https://www.google.com/goto?url=CAEScgHEIkXXeRzH7Y3o6O8ri6fSNp_zMfpfGwbStMWBLKhbV_FuLTE85OuXHZdFiviu_oBzXTRDFEoZenS_PlTzpMV1aNaCQW3A8g5iBC7iW7t76zagVc9hGwNfmaOat2KwOcE_8gpFgPaYXM9aewjfyrA4OA&gsessionid=ti02ijkt9MIEFVYXmgGQg1X4w3cvlbWb9BzBOfrrn3Bt4ChBrrQCbw)  
  <sub>Yahoo! Finance Canada, 21 hours ago</sub>  
  Find the latest XBI Dec 2026 200.000 call (XBI261211C00200000) stock quote, history, news and other vital information to help you with your stock trading...
- [Bank of America Names 2 ‘Strong Buy’ Stocks With 60%+ Upside](https://www.google.com/goto?url=CAESmgEBxCJF14kPP4PB9G3w7K_MqaTjeU5Gr_LCkaSMfA_xjYVDVKCOJ63WeTHY562ZUGJquWtBZYRoQuUwbucN-iypBJHmALw30U7mmFIvJNhrGzTTA-jBAdQUxrv9D4IhnDjhTcSMDq21ApTgjc2G6xw5W33VZYbBI2hN4KfCYFpaSDDShy5rCLbXZ-8zYT21hwB-ntVB2C7VcNWW&gsessionid=ti02ijkt9MIEFVYXmgGQg1X4w3cvlbWb9BzBOfrrn3Bt4ChBrrQCbw)  
  <sub>TipRanks, 4 hours ago</sub>  
  Biotech stocks have been among the market's stronger performers this year, benefiting from advances in drug development, growing interest in AI,...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.11% (+0.12 on the week) | 5-year 4.87% (+0.27 on the week) | 10-year 5.03% (+0.19 on the week) | 30-year 5.37% (+0.12 on the week)
Yield curve, 10-year minus 3-month: +0.92 points -- upward sloping (normal)
US dollar index: 102.91 (+1.36 on the week)
Volatility (VIX): 18.99 (-9.2 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.1% (2026-10-01) | jobless claims 200k (2026-11-07)
Policy and expectations: Fed target 4.00% | market expects 2.2% inflation over 10 years
Rate path: 2-year Treasury 4.56% vs Fed target 3.75-4.00% -- the bond market prices about 3 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 152.26 (bar of 2026-11-12), from 502 daily bars
Trend: vs 20d SMA 153.16 (-0.6%), 50d 154.56 (-1.5%), 200d 142.86 (+6.6%); 50d above 200d
Momentum: RSI(14) 48.1 | MACD 0.232 vs signal 0.047 (histogram 0.186)
Returns: 1d -2.6% | 5d +2.6% | 1m +3.7% | 3m -3.3%
52-week range: 111.91 - 169.55 (now 70.0% of the way up)
Volatility: ATR(14) 4.94 (3.2% of price) | annualised 20d 42.3%
Volume: 0.12x the 20-day average
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
Three-year record: +32.6% a year | beta to the market 1.01
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

<details><summary><b>What analysts and big funds say</b> — score +0.30</summary>

_Not available today._

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score +0.30</summary>

```text
Rolled up from the 5 largest holdings, 9.5% of the fund by weight  -- thin, so read this as a fact about that slice rather than the fund
Ratings by weight: buy 75.0% | hold 25.0% | sell 0.0% (mean 2.05 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +12.9% above the current prices
Holdings read: MRNA, NTRA, HALO, TWST, BIIB
Recent rating changes among them:
  - MRNA: 2026-11-09 Goldman Sachs: main, Neutral -> Neutral
  - NTRA: 2026-11-09 Baird: main, Outperform -> Outperform
  - HALO: 2026-11-11 Morgan Stanley: down, Overweight -> Equal-Weight
  - TWST: 2026-10-13 TD Cowen: main, Buy -> Buy
  - BIIB: 2026-11-09 Piper Sandler: reit, Overweight -> Overweight
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
Share count change: 1 week: +5.3% (539.65M) over 7d | 1 month: +4.6% (467.77M) over 30d
Shares outstanding: 70.45M | fund size: 10.73B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### US materials and chemicals (XLB) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:** no explanation. It wrote only “Neutral”, so the main reasons below are all it gave.

**Main reasons it gave:**
- Flat fund flows (0% change week/month) indicating no net demand
- Technicals: price above 20‑day, 50‑day, and 200‑day SMAs but 50‑day SMA below 200‑day SMA and low volume, no decisive breakout
- Macro: modest yield increases, dollar up, VIX down but still elevated, no surprise data
- Analyst coverage limited to 34% of fund, all buy with +8.4% price target, but limited weight

<details><summary><b>News</b> — score +0.00</summary>

- [State Street Materials Select Sector SPDR ETF (XLB) Stock Price, News, Quote & History](https://ca.finance.yahoo.com/quote/XLB/)  
  <sub>Yahoo! Finance Canada, 4 hours ago</sub>  
  State Street Materials Select Sector SPDR ETF (XLB) · -1.63% · 7.26% · 1.45% · 16.91% · 21.15% · 18.57% · 410.27%. Key Events. Baseline. Advanced Chart.
- [In the Year of AI, Tech Isn’t the Top Sector](https://www.etf.com/sections/features/year-ai-tech-isnt-top-sector)  
  <sub>ETF.com, 21 hours ago</sub>  
  Energy leads the S&P 500's sectors by a mile, and health care has caught up with tech.
- [State Street Communication Services Select Sector SPDR ETF (XLC) stock price, news, quote and history](https://www.google.com/goto?url=CAESZAHEIkXXwInGPNhsUI8Wg0MGfF2aqILRfw8cIAJ0Rdq-xhs9mOmyXdy0v0R7RFfoKiG4TY4Gbo7jDTLHK1d14KZmkebRbMlxrJMjhZttALPcOnexDAH7h30aKqWzeh1ah10ccWg&gsessionid=XBuC0OzpgNGH9xaqEeLqI8mBeHAfDcd4GH_eSFGpNuZmo2s_seIrsQ)  
  <sub>Yahoo Finance Singapore, 3 hours ago</sub>  
  Find the latest State Street Communication Services Select Sector SPDR ETF (XLC) stock quote, history, news and other vital information to help you with...
- [Cyclicals Lead Sectors In Wednesday Trading As Defensives Trail](https://www.google.com/goto?url=CAEStQEBxCJF16eabiVPNH5JBVxsK5bplC2xfu_wJP0-YrI2MTL7-wTO0znf7widDMENQnSnmI9IvejsqfuCeOBTgg-B7nj9lGp5ILdctsFHU_Z1hFLf4nVEGzsx8nXQx336tjoPd4BmXRjj1ugpx3qeHDSFTZbHlIZ0ltUFkgkluCMTOksGV_IDwkeCb0xcvCWgpHGuURQFHnpWp7BObzOA1EMdTkKWHKt8PgWxPDNUK3FFovNJgyRJ&gsessionid=XBuC0OzpgNGH9xaqEeLqI8mBeHAfDcd4GH_eSFGpNuZmo2s_seIrsQ)  
  <sub>Benzinga, 23 hours ago</sub>  
  Five sectors are higher and six are lower in Wednesday's regular session, with cyclical sectors holding two of the top three positions.
- [Tech Stocks Lead Market Rally as Investors Move Away from Safer Sectors](https://www.google.com/goto?url=CAESogEBxCJF19C6v1vJoPOwJsG2tcZvI6y7A1QWGI9VxTk4YVI5fAtLkC99cr7QYtiJ9tfdGQLi-mGE71NWiQst-SlgvkAn3fk5ZGaNvaq8QOZCJKcgJJ6QS5ejdnwAhwYQ1vuMKa1uHvp0J-0z5-Em-vvXRDofFf0yGG0Puyr9O0B8YXG5pS5dHNq4FDG5fVu5SA4KSVO68tg7Wjz9I9l50CpVsrQ&gsessionid=XBuC0OzpgNGH9xaqEeLqI8mBeHAfDcd4GH_eSFGpNuZmo2s_seIrsQ)  
  <sub>TipRanks, 19 hours ago</sub>  
  Technology stocks are leading Wednesday's market rally after strong earnings from AI cloud company CoreWeave ($CRWV) helped ease worries about AI spending.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.11% (+0.12 on the week) | 5-year 4.87% (+0.27 on the week) | 10-year 5.03% (+0.19 on the week) | 30-year 5.37% (+0.12 on the week)
Yield curve, 10-year minus 3-month: +0.92 points -- upward sloping (normal)
US dollar index: 102.91 (+1.36 on the week)
Volatility (VIX): 18.99 (-9.2 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.1% (2026-10-01) | jobless claims 200k (2026-11-07)
Policy and expectations: Fed target 4.00% | market expects 2.2% inflation over 10 years
Rate path: 2-year Treasury 4.56% vs Fed target 3.75-4.00% -- the bond market prices about 3 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 53.01 (bar of 2026-11-12), from 502 daily bars
Trend: vs 20d SMA 52.20 (+1.6%), 50d 50.95 (+4.0%), 200d 51.23 (+3.5%); 50d below 200d
Momentum: RSI(14) 58.7 | MACD 0.637 vs signal 0.605 (histogram 0.032)
Returns: 1d -0.0% | 5d +1.3% | 1m +6.7% | 3m +0.9%
52-week range: 42.23 - 53.90 (now 92.4% of the way up)
Volatility: ATR(14) 0.89 (1.7% of price) | annualised 20d 19.7%
Volume: 0.10x the 20-day average
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
Three-year record: +13.1% a year | beta to the market 0.76
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

<details><summary><b>What analysts and big funds say</b> — score +0.40</summary>

_Not available today._

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score +0.40</summary>

```text
Rolled up from the 5 largest holdings, 34.0% of the fund by weight
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 1.73 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +8.4% above the current prices
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
Shares outstanding: 71.92M | fund size: 3.81B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### US energy companies (XLE) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Mixed signals: strong analyst bullish view, bullish inventory draws, bearish EIA price outlook, slightly bearish technicals, flat fund flows. No material macro surprise or decisive technical break.

**Main reasons it gave:**
- Analyst view: 100% buy rating, +11.4% price target
- Energy inventories: crude and diesel draws, low percentile levels
- EIA price outlook: WTI forecast down 13% over six months
- Technical indicators: price below 20‑day and 50‑day SMA, RSI 43.9, MACD negative
- Fund flows: flat share count, no net inflows

<details><summary><b>News</b> — score +0.00</summary>

- [Your $300,000 in XLE holds $116,286 in just two oil companies](http://www.bing.com/news/apiclick.aspx?ref=FexRss&aid=&tid=6af5d14c30be421eb54c53e6148cfb27&url=https%3a%2f%2fwww.msn.com%2fen-us%2fnews%2fother%2fyour-300000-in-xle-holds-116286-in-just-two-oil-companies%2far-AA2hii5M&c=8692564509298185597&mkt=en-us)  
  <sub>24/7 Wall St. on MSN, 11h ago</sub>  
  Quick ReadXLE puts 39% of its assets into Exxon and Chevron, so a $300,000 stake carries about $116,000 in just two oil companies.Exxon's 23% weight and Chevron's 16% stem from market-cap weighting, ...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.11% (+0.12 on the week) | 5-year 4.87% (+0.27 on the week) | 10-year 5.03% (+0.19 on the week) | 30-year 5.37% (+0.12 on the week)
Yield curve, 10-year minus 3-month: +0.92 points -- upward sloping (normal)
US dollar index: 102.91 (+1.36 on the week)
Volatility (VIX): 18.99 (-9.2 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.1% (2026-10-01) | jobless claims 200k (2026-11-07)
Policy and expectations: Fed target 4.00% | market expects 2.2% inflation over 10 years
Rate path: 2-year Treasury 4.56% vs Fed target 3.75-4.00% -- the bond market prices about 3 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score -0.20</summary>

```text
Last close 63.65 (bar of 2026-11-12), from 502 daily bars
Trend: vs 20d SMA 66.30 (-4.0%), 50d 64.97 (-2.0%), 200d 59.40 (+7.2%); 50d above 200d
Momentum: RSI(14) 43.9 | MACD -0.746 vs signal -0.111 (histogram -0.635)
Returns: 1d +0.4% | 5d +3.3% | 1m -5.9% | 3m +2.8%
52-week range: 43.81 - 70.02 (now 75.7% of the way up)
Volatility: ATR(14) 1.58 (2.5% of price) | annualised 20d 31.3%
Volume: 0.09x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.30</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score +0.30</summary>

```text
Fund type: Equity Energy
What it holds: P/E 17.48 | P/B 2.46 | P/S 1.71 | 3y earnings growth n/a
Yield: 2.2%
Three-year record: +17.9% a year | beta to the market -0.22
Cost and size: expense ratio 0.08% | net assets 46.37B
What it is made of: Stocks 99.8%, Cash 0.2%
Largest holdings: ExxonMobil Holdings Corp 24.3%, Chevron Corp 18.3%, ConocoPhillips 7.3%, Marathon Petroleum Corp 4.6%, Phillips 66 4.5%
Sector mix: Energy 100.0%
```

</details>

<details><summary><b>Does this company beat its own forecasts</b> — score +0.30</summary>

_Not available today._

</details>

<details><summary><b>What holding this fund costs you</b> — score +0.30</summary>

_Not available today._

</details>

<details><summary><b>How much oil and gas is in storage</b> — score +0.30</summary>

```text
US inventories, week ending 2026-10-30 (published the following Wednesday)
  Crude oil: 409.8 million barrels, -0.9 on the week (a draw), 10% percentile over 52 weeks -- low for the time of year
  Petrol: 209.0 million barrels, -0.2 on the week (a draw), 25% percentile over 52 weeks
  Diesel: 99.3 million barrels, -3.6 on the week (a draw), 2% percentile over 52 weeks -- low for the time of year
  Natural gas: 3,801.0 billion cubic feet, +77.0 on the week (a build), 92% percentile over 52 weeks -- high for the time of year
A build is more supply than demand and a draw is the reverse, so a build reads bearish and a draw bullish -- as a rule of thumb, not a law. Weigh the change and how unusual the level is above the level itself, and remember the market has already seen this number.
```

</details>

<details><summary><b>How the crop is growing</b> — score +0.30</summary>

_Not available today._

</details>

<details><summary><b>What analysts and big funds say</b> — score +0.50</summary>

_Not available today._

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score +0.50</summary>

```text
Rolled up from the 5 largest holdings, 59.0% of the fund by weight
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 2.10 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +11.4% above the current prices
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
Shares outstanding: 186.42M | fund size: 11.87B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### US banks and finance (XLF) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> No macro surprise; yields modestly up, Fed unchanged; Technical trend bullish but volume low; Analyst coverage 100% buy with +4.9% price target; Fund flows flat (no net creation/redemption)

**Main reasons it gave:**
- Yield curve up 0.92 points, no policy surprise
- Technical trend above SMA, RSI 63, but volume 0.09x 20‑day avg
- Analyst coverage 100% buy, weighted price target +4.9% above price
- Fund flows flat: share count unchanged over week and month

<details><summary><b>News</b> — score +0.00</summary>

- [State Street Financial Select Sector SPDR ETF (XLF) Stock Price, News, Quote & History](https://ca.finance.yahoo.com/quote/XLF/)  
  <sub>Yahoo! Finance Canada, 21 hours ago</sub>  
  State Street Financial Select Sector SPDR ETF (XLF) ... This price reflects trading activity during the overnight session on the Blue Ocean ATS, available 8 PM to...
- [Financial Select Sector SPDR (XLF) Sells $18.9 Million of Berkshire on Nov. 10](https://finance.yahoo.com/markets/stocks/articles/financial-select-sector-spdr-xlf-110546923.html)  
  <sub>Yahoo Finance, 4 hours ago</sub>  
  This article first appeared on GuruFocus. Financial Select Sector SPDR ETF (XLF) was the only ETF selling on Tuesday, Nov. 10, with no funds buying.
- [These 10 financial stocks have stayed in Strong Buy territory for months (XLF:NYSEARCA)](https://www.google.com/goto?url=CAESqwEBxCJF15MNX9P28uCdpdYIMUx8EhqlqCgGTCIf9WbPZi-5DVs3_2OCxLC4NTjCH5pi7d9v4YqTl3ff4qBFo6xdH2FggsNfawsoZRygo9nTqh0LVAMpxKpr9HUkcvL6mjioeMdtH4T-SfIISQdmCbjQLVzFKCSGmmCzbjGRvMRjq-hbdsIo-RuNz7RjqmDAc2ZE0FAnMDe7javXDu_3FgEeZBcEjscs7jUfahs&gsessionid=wEeVCRe76UV3SsepNZuFxN90VAWFDNcceg9u5QbZf3bj2GWKF5WIgg)  
  <sub>Seeking Alpha, 2 hours ago</sub>  
  Ten financial stocks hold Strong Buy Quant Ratings for 74 to 273 days; The Hanover Insurance Group leads at 273 days, and Sezzle scores highest at 4.98.
- [BTO: A 6.8% Bank Yield At A Rare Discount (NYSE:BTO)](https://www.google.com/goto?url=CAESjAEBxCJF1_iKRQBktldNo1z_nTYuecMxjhx4fa8HNQm4U2S4kf7Odg1fPlxewooAknN0k1lBxTrrWsSNCZolgI0ZuRwaBnSH1tQ3JFUsjVgdtACW8GTThruGBk20zQTGcioSSD6K0b87Rk7x9GxkAsIptc0UrHBgpHWq6mDlSd3NzMdmZvHnfWoATCx_cw&gsessionid=wEeVCRe76UV3SsepNZuFxN90VAWFDNcceg9u5QbZf3bj2GWKF5WIgg)  
  <sub>Seeking Alpha, 16 hours ago</sub>  
  John Hancock Financial Opportunities Fund is rated a Buy at an 8.8% discount to NAV and a 6.8% yield, creating a value opportunity. Click for more on BTO.
- [In the Year of AI, Tech Isn’t the Top Sector](https://www.google.com/goto?url=CAESfwHEIkXXE9NO93xyzL1QEA_vnlJX7HWHkXVGpcL_fu0nwMs7jGXR3K9N2Z_WlXtBBVtCJbKz3lMRUjQv-L1mSiY2Al-tEceSN1nM9xZG_mc4dvVOSLiODbSOo5C3T7mxW0U7v5KxJ_ScCpDmMyYBhokdrern0BjtBgMNECw6eJg&gsessionid=wEeVCRe76UV3SsepNZuFxN90VAWFDNcceg9u5QbZf3bj2GWKF5WIgg)  
  <sub>ETF.com, 21 hours ago</sub>  
  Energy leads the S&P 500's sectors by a mile, and health care has caught up with tech.
- [Tech Futures Fall; Nvidia Dives As It Mulls Ousting CEO Huang](https://www.google.com/goto?url=CAESswEBxCJF1wayxAz4Ei0DiCm-sQE_n2bZtktEwTzCjS4Ga3Xco_TJZzrAFT-_aiygwO66iEoZlHmqEPQOhD3kMQzGu8AhQ2J7_0RjbJTGdEnawI-YloAj0vtsLhFR6VAVRZ4T46GsmsejMcY1Cj22gCoHCx2efQd290FLlb4uQ88Zf98a6UxZA5wWmle7GZpmtykp8j4cN0k2gITG3TpmLMzHRhAcSu9TbNYSwRLFPEkFexzFbQ&gsessionid=wEeVCRe76UV3SsepNZuFxN90VAWFDNcceg9u5QbZf3bj2GWKF5WIgg)  
  <sub>Investor's Business Daily, 2 hours ago</sub>  
  Dow Jones futures: Techs fell as Nvidia dived on news that the board may oust CEO Huang. CoreWeave rival Nebius beat views.
- [Berkshire Hathaway Stock Hits 52-Week High Despite 6% Earnings Drop](https://www.google.com/goto?url=CAESigEBxCJF13wc607d7JC1eg_Mg6-zgk28qQJSoOFilDhH9NSkLNupEUyrHKFUU5loAV9jFNglXyL03qZC39c7swIU-3wtu6tqZIB7AHIExqBgbYfNkRb838kHN6eHqgtVHEwusiarY5ETJhdv-Q4S0PP2TQoJwdTKMWDlP2flLja_Zl-Yo-I8J9MSFNY&gsessionid=wEeVCRe76UV3SsepNZuFxN90VAWFDNcceg9u5QbZf3bj2GWKF5WIgg)  
  <sub>EBC Financial Group, 9 hours ago</sub>  
  Why did Berkshire Hathaway stock hit a 52-week high despite a 6% earnings drop? Explore insurance weakness, $9.6B buybacks and BRK.B's rally.
- [What Are Wall Street Analysts' Target Price for American Express Stock?](https://www.google.com/goto?url=CAESnwEBxCJF16k9t0MAIe2vHZCWmTysqYoPI0EVxAVX_P6FbUbkqtfmysuUDcbdRDptCd73Uvtv5C-GXImoMY4NgjSHHPR6hIcikgbddwV7hqFrpPBtCMD7mysdUZUso_NHiisG1HHg_-fyunfeFz7sNXiPfcfluKbsz2HuWFqHzmEQpm1X0U6K3ilGrzUoWjM2NfZrdXgZoWCYmnnFsSsHdrM&gsessionid=wEeVCRe76UV3SsepNZuFxN90VAWFDNcceg9u5QbZf3bj2GWKF5WIgg)  
  <sub>Yahoo Finance, 7 hours ago</sub>  
  Although American Express has underperformed the broader market over the past 52 weeks, Wall Street analysts remain moderately optimistic about the stock's...
- [Tech Stocks Lead Market Rally as Investors Move Away from Safer Sectors](https://www.google.com/goto?url=CAESogEBxCJF1zkM5kySlcT5Z-6fAso8L5OIZ4Jox59DfUoe0G4CGVdYKiOHTvP_p0CaMiHbyj4hQF_Mt0el6043ysptBkj1WwbSyfoLje4eyFxdLXLvuxAP2EgqpDhXGgQ02zaaAkkI73JVlfOMIIWGAqe-CHP9TUf2hJowYVKLB2w_MkWinr9xLvaKLt1WQgpdI_iICOOhHQdH-VB3ftsJIWxnFpQ&gsessionid=wEeVCRe76UV3SsepNZuFxN90VAWFDNcceg9u5QbZf3bj2GWKF5WIgg)  
  <sub>TipRanks, 19 hours ago</sub>  
  Technology stocks are leading Wednesday's market rally after strong earnings from AI cloud company CoreWeave ($CRWV) helped ease worries about AI spending.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.11% (+0.12 on the week) | 5-year 4.87% (+0.27 on the week) | 10-year 5.03% (+0.19 on the week) | 30-year 5.37% (+0.12 on the week)
Yield curve, 10-year minus 3-month: +0.92 points -- upward sloping (normal)
US dollar index: 102.91 (+1.36 on the week)
Volatility (VIX): 18.99 (-9.2 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.1% (2026-10-01) | jobless claims 200k (2026-11-07)
Policy and expectations: Fed target 4.00% | market expects 2.2% inflation over 10 years
Rate path: 2-year Treasury 4.56% vs Fed target 3.75-4.00% -- the bond market prices about 3 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 58.71 (bar of 2026-11-12), from 502 daily bars
Trend: vs 20d SMA 56.93 (+3.1%), 50d 55.97 (+4.9%), 200d 53.92 (+8.9%); 50d above 200d
Momentum: RSI(14) 63.0 | MACD 0.807 vs signal 0.618 (histogram 0.190)
Returns: 1d +0.1% | 5d +2.1% | 1m +7.7% | 3m +0.9%
52-week range: 47.81 - 59.20 (now 95.7% of the way up)
Volatility: ATR(14) 0.89 (1.5% of price) | annualised 20d 21.3%
Volume: 0.09x the 20-day average
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
Three-year record: +21.6% a year | beta to the market 0.68
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
Weighted price target: +4.9% above the current prices
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
Shares outstanding: 883.44M | fund size: 51.87B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### US industry (XLI) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Neutral stance due to flat fund flows, thin analyst coverage despite bullish ratings, mixed technicals, and no macro surprise.

**Main reasons it gave:**
- Fund flows flat (0% change week/month) – no net inflow/outflow
- Analyst coverage thin (24% of fund) despite 100% buy rating and +23.7% price target
- Technical indicators mixed: price above 20‑day/50‑day SMA but below 200‑day SMA, low volume
- Macro environment unchanged: modest yield rises, VIX down, no surprise data

<details><summary><b>News</b> — score +0.00</summary>

- [Better Tech ETF for 2027: State Street's XLK vs. Fidelity's FTEC](https://www.fool.com/coverage/etfs/2026/11/12/better-tech-etf-for-2027-state-street-s-xlk-vs-fidelity-s-ftec/)  
  <sub>The Motley Fool, 7 hours ago</sub>  
  The State Street Technology Select Sector SPDR ETF (XLK +3.23%) and Fidelity MSCI Information Technology Index ETF (FTEC +2.91%) both provide ultra-low-cost...
- [Tech & Energy Lead Sector Fund Flows in October](https://www.google.com/goto?url=CAESnwEBxCJF1-mJGnw4O0qkKv-RI7BYDB3K4QI27uiRj1o2Uy9FDEwyVwGC49JnC9agIRUNF-dR-Gi4PkjvwZLzeB040dH-ygcGbmLSZ9drtc0yBTK_0X_nBc99mR6oAwPy1ERVx3JfVijESuzTzBVm5oix8D-DdrOgiD8RsqxiyKnGGn6TCcbLm08xlPxEvFmM2U4heKtrast7lZwKJcNIBdI&gsessionid=TLcn-C2yYDKcFLpp3O1YhYXZrP9uqmAu2kjta2IBkTVUg3So_9P7Aw)  
  <sub>ETF Trends, 18 hours ago</sub>  
  October's fund flows saw more than $10 billion go in to the energy and tech sectors combined, creating a strong case for targeted exposure.
- [Only these four industrial stocks have sustained Strong Buy Quant ratings (XLI:NYSEARCA)](https://www.google.com/goto?url=CAESrAEBxCJF19Apt1oADvDrAAyC7ncqTKn_tOqTJUh0uINY08kmS6Kx_Ml2g0gFGJPJwLiK1Rf8760nSwyg1oSQwnW-lTdGr2PGydiuybwHTFCo0e-O1L1qKJwocMDrydMnY69bGLfeAcNz166raTJvokzZ3C0JihXwXCjPJ1BoBoUecLQ-MZ0P-NWQPHYPwkyqnI8PH10rzbcPs9suEVbnyS8uPYEWtBkg1P65xjzA&gsessionid=TLcn-C2yYDKcFLpp3O1YhYXZrP9uqmAu2kjta2IBkTVUg3So_9P7Aw)  
  <sub>Seeking Alpha, 23 hours ago</sub>  
  Four industrial stocks retain Seeking Alpha Strong Buy Quant Ratings for 20 to 93 days; The GEO Group scores 4.88 and RXO leads at 4.92.
- [Cyclicals Lead Sectors In Wednesday Trading As Defensives Trail](https://www.google.com/goto?url=CAEStQEBxCJF1yeKmyOVRSYBx8QvenSQ6b_T5Drv2Vk7XwmoEZrGJ1FO4l48nW3bUTSJNKU5sBA1OMl19o84ITyMk12bhthr8JiBqXlbfm8iZZSA3OBhnAYYwkkPJ5MlYinTrj9pHHrTwCZDvx0GO31qaF5xwhmyMxtz0J23W4bEExqYz0iaZlrw22lNJu7UtqC0e2izv-8IIydRYWgCDrDhiPoXNss5jtXqpy331EMw1_TyPC-LS6rN&gsessionid=TLcn-C2yYDKcFLpp3O1YhYXZrP9uqmAu2kjta2IBkTVUg3So_9P7Aw)  
  <sub>Benzinga, 23 hours ago</sub>  
  Five sectors are higher and six are lower in Wednesday's regular session, with cyclical sectors holding two of the top three positions.
- [Nvidia: Midterms, Investigations & Dip Buyers](https://www.google.com/goto?url=CAESlQEBxCJF13swSO4YWStY3CXt3OS1aE5b-KLjEZX40_2rBIyHmwAOdui4h-DdMduPaoE_2QnbQpuXqtQMnbODwLBNDnlDcr4exedfajlUWCjcdWXwNY6orEuMvlH3wf2VwIP27eqVGy5yx6am3D3FhPbo_RLlZr_ccZa2ja9BNAqyxke1m80e14MmzTJup5TRsNGQrDDCdw&gsessionid=TLcn-C2yYDKcFLpp3O1YhYXZrP9uqmAu2kjta2IBkTVUg3So_9P7Aw)  
  <sub>ETF Database, 46 minutes ago</sub>  
  The Nvidia investigation and midterm uncertainty highlight ETF concentration risks as tech and semiconductor inflows signal continued demand.
- [In the Year of AI, Tech Isn’t the Top Sector](https://www.google.com/goto?url=CAESfwHEIkXX9t2FtxexHSgEfrMNIJdd2oCZsW-4PO0LHXP0zNFMMn0yWPoziiqBGUPy9Ceu4SnVzdn0LOBbt9tQJJbHwIEUZSmxbkuem1g9F-bBs50dmj8VoK9pcsxfpfDFNVz4RgwbvmdanslRVNg2VCZgIyO6UFtUo7QTcsLnMnw&gsessionid=TLcn-C2yYDKcFLpp3O1YhYXZrP9uqmAu2kjta2IBkTVUg3So_9P7Aw)  
  <sub>ETF.com, 21 hours ago</sub>  
  Energy leads the S&P 500's sectors by a mile, and health care has caught up with tech.
- [Are Wall Street Analysts Predicting Stanley Black & Decker Stock Will Climb or Sink?](https://www.google.com/goto?url=CAESpQEBxCJF1xGXvJphZzMVoFZKZSyKdda1I06F9CGD4TVMt0gdDqofcPsypBgrDvDpKc6Q7qh8OFf_L4KJXMXcDJX1Z1918_122waaDSppxjS6Bz5cSQgykZ_ozLITfitWriIOPRxJNdODAeRoceaTrMjFmrbfX80PUEq9ELD4VuYSM0JP7eY5geUdHCFQh53x04sjp8HhtBuq0KOORp5rtNWL9KPk4AI&gsessionid=TLcn-C2yYDKcFLpp3O1YhYXZrP9uqmAu2kjta2IBkTVUg3So_9P7Aw)  
  <sub>Yahoo Finance, 23 hours ago</sub>  
  Stanley Black & Decker has notably outperformed the broader market over the past year, and analysts are moderately optimistic about the stock's prospects.
- [GE Vernova Stock Rebounds as AI Optimism Counters SoftBank Concerns](https://www.google.com/goto?url=CAESugEBxCJF10fR1wPy4Yk5wpitLUW8FB8_9e_iItPrmSOU-WXEfL46xZRE4iUT2DRY-KgMAl5JPhaeicdTDEeiZkBupjPNDm1VvhBhomTRfDZ8_y_LMqfNuz8kgeiod1PYDVsTXJT-f8vO7WqdIqc-wsY3WFo2kBMmBTLJ-fnRvfZPkJdMM3xKyTez_BgYGDUvvC0adhQtoDwVTl8Dn9T4KpFNkNVNYGcAAdz8fkVzAm6vAccz_8pEt_TLxbg&gsessionid=TLcn-C2yYDKcFLpp3O1YhYXZrP9uqmAu2kjta2IBkTVUg3So_9P7Aw)  
  <sub>Benzinga, 24 hours ago</sub>  
  GE Vernova shares rebound as CoreWeave boosts AI infrastructure sentiment, despite SoftBank plan concerns, bearish technicals and a $540 Sell call.
- [Tech Stocks Lead Market Rally as Investors Move Away from Safer Sectors](https://www.google.com/goto?url=CAESogEBxCJF12xMQ9j0Hq8KwvKGjJYzhThud1D8joj_Oi_HUo434nCTqxZ7Gky7EtEOwRfVIJI9I9WcVQxBgDM3VSkumXY5kpKMJHXJIrAEYV2UXvYIjMYioiLdO_Zn1JU-WESbc7JYNt_2DDBv6daePd9ffUqeAiDDw9FINQupRMfm3SSrVDcBCG7YzHat1Ww1_cnZmiDA2F4gwJEr7TMicj6enBs&gsessionid=TLcn-C2yYDKcFLpp3O1YhYXZrP9uqmAu2kjta2IBkTVUg3So_9P7Aw)  
  <sub>TipRanks, 19 hours ago</sub>  
  Technology stocks are leading Wednesday's market rally after strong earnings from AI cloud company CoreWeave ($CRWV) helped ease worries about AI spending.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.11% (+0.12 on the week) | 5-year 4.87% (+0.27 on the week) | 10-year 5.03% (+0.19 on the week) | 30-year 5.37% (+0.12 on the week)
Yield curve, 10-year minus 3-month: +0.92 points -- upward sloping (normal)
US dollar index: 102.91 (+1.36 on the week)
Volatility (VIX): 18.99 (-9.2 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.1% (2026-10-01) | jobless claims 200k (2026-11-07)
Policy and expectations: Fed target 4.00% | market expects 2.2% inflation over 10 years
Rate path: 2-year Treasury 4.56% vs Fed target 3.75-4.00% -- the bond market prices about 3 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 170.57 (bar of 2026-11-12), from 502 daily bars
Trend: vs 20d SMA 167.83 (+1.6%), 50d 169.10 (+0.9%), 200d 173.45 (-1.7%); 50d below 200d
Momentum: RSI(14) 54.2 | MACD -0.117 vs signal -0.590 (histogram 0.474)
Returns: 1d -0.2% | 5d +5.0% | 1m +2.1% | 3m -8.5%
52-week range: 147.83 - 186.51 (now 58.8% of the way up)
Volatility: ATR(14) 3.05 (1.8% of price) | annualised 20d 25.0%
Volume: 0.11x the 20-day average
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

<details><summary><b>What analysts and big funds say</b> — score +0.30</summary>

_Not available today._

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score +0.30</summary>

```text
Rolled up from the 5 largest holdings, 24.0% of the fund by weight  -- thin, so read this as a fact about that slice rather than the fund
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 1.73 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +23.7% above the current prices
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
Shares outstanding: 136.63M | fund size: 23.30B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### US technology (XLK) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Neutral overall; bullish analyst coverage and net inflows are offset by weak short‑term technical momentum and a macro backdrop of rising yields and a stronger dollar that is less supportive for growth‑oriented tech stocks.

**Main reasons it gave:**
- Analyst coverage of top holdings is 100% buy with a weighted price target +36.7% above current price
- Fund flows show a 9.7% increase in share count over the past month, indicating net inflows
- Technical indicators show price below 20‑day and 50‑day SMAs, RSI 41.4, negative MACD, and low volume, suggesting weak short‑term momentum
- Rising Treasury yields and a stronger dollar create a less favorable environment for growth‑oriented tech stocks

<details><summary><b>News</b> — score +0.00</summary>

- [Better Tech ETF for 2027: State Street's XLK vs. Fidelity's FTEC](https://www.fool.com/coverage/etfs/2026/11/12/better-tech-etf-for-2027-state-street-s-xlk-vs-fidelity-s-ftec/)  
  <sub>The Motley Fool, 7 hours ago</sub>  
  The State Street Technology Select Sector SPDR ETF (XLK +3.23%) and Fidelity MSCI Information Technology Index ETF (FTEC +2.91%) both provide ultra-low-cost...
- [Tech & Energy Lead Sector Fund Flows in October](https://www.google.com/goto?url=CAESnwEBxCJF1zo6fa33k0mRqBdwS6_HUnZvB1ahf1L-M4XrbZLNsQWI2e6vPffaZ4PdcEpxhfkvncjv9j8zjAKB-9L9dYmmgpmbyPePh5mLQZ6kD1T5hqKayRek0DTdh1TsGc5_LkQmXcapK81woB37CTkiiuRw2hLm6n3eNhTw_46gOKCTrwEVwtwoDS8dy4hhIFEYvGnEoMrGwJG5t2GPopI&gsessionid=QNASBEkGCl-0jQjO-sNcfoNklwecjbuVBKh4S4GwodQnhLn4scFtCw)  
  <sub>ETF Trends, 18 hours ago</sub>  
  October's fund flows saw more than $10 billion go in to the energy and tech sectors combined, creating a strong case for targeted exposure.
- [Anthropic’s IPO Buzz Put AI Stocks Back In Charge](https://www.google.com/goto?url=CAESigEBxCJF1whQZaQ3z5YIQqK7JgYm5iokIIraobYLpHBn_ujO_1LuKbdtWEspaW1nMuEfOnUNtgiEpf80IVYBraM9-b5_JKStB2aBF4d-DBZ36F39XyiQKTMnReRaHxo6muQwFCFc34eSDMU_H582atK63jB75R7wHjN5e8AckdXpsvTlzCsnj-Wcv90&gsessionid=QNASBEkGCl-0jQjO-sNcfoNklwecjbuVBKh4S4GwodQnhLn4scFtCw)  
  <sub>Finimize, 13 hours ago</sub>  
  Chip ETFs jumped and bankers weighed pricing Anthropic above $70-78 a share as demand piled up.
- [In the Year of AI, Tech Isn’t the Top Sector](https://www.google.com/goto?url=CAESfwHEIkXXs7z0FEQT8wdBzwP3hi_C8n_fhqZojmXOebvTNJNaLaVp5QoStWVI8h7u7cTYpl12uv0O5YIC-PRY6UEKYtXhR3SCuQUjOQwU6ZLPbiVr-4RJRcl0cZmxhjOzJ5XUU9Qzyex4EhvrSoqnJw9GnYa4hdTPwQKTGLwid7k&gsessionid=QNASBEkGCl-0jQjO-sNcfoNklwecjbuVBKh4S4GwodQnhLn4scFtCw)  
  <sub>ETF.com, 21 hours ago</sub>  
  Energy leads the S&P 500's sectors by a mile, and health care has caught up with tech.
- [The growth vs. value 10-year uptrend has been ‘so far, so perfect’ (IWF:NYSEARCA)](https://www.google.com/goto?url=CAESoQEBxCJF137b-s7IVoFvHB4wghBFOzapuMXO8AbvHj0XDoc2pubS-LPUYtICZkgSt8r60_o26yiRzuiuDr3J2r0ZnMaZyeqbB3t4Qq_pJssmtouRxJHxAm74f7lyyRcv7buNs61szl6gGX0nRLPI_xgqoUDzdmddwq3PxCDbTS26JwvS52_02wa4GH1WSvebRcIe4wcSOywbcAcNZtKgfwRsGQ&gsessionid=QNASBEkGCl-0jQjO-sNcfoNklwecjbuVBKh4S4GwodQnhLn4scFtCw)  
  <sub>Seeking Alpha, 12 minutes ago</sub>  
  The 10-year growth-versus-value uptrend remains intact, while semiconductor ETFs are up nearly 20% from local lows amid AI volatility.
- [Cyclicals Lead Sectors In Wednesday Trading As Defensives Trail](https://www.google.com/goto?url=CAEStQEBxCJF1yI_cWnI4xSTa2FdkJErHsh1lqcypbw1LBrywv-LMNyryYetIuzcnA97ECj9yFLmQm5W2KNZ8Ed6D5QWGGgjSe9IJhPphtyG5Oy9K8k2GLFKchMC6CVPuc1Fr_8zsBTcHE1O9wd3IgXBOBvYC7sbLNzH0WghR0NPn4y0Hq5bpwgIAW0rdJ9oI6Aq_b7iQEpg6U0-5qfkhqndaR3uwOusrdt-MZp0tyB6uxB2cuMv-TGA&gsessionid=QNASBEkGCl-0jQjO-sNcfoNklwecjbuVBKh4S4GwodQnhLn4scFtCw)  
  <sub>Benzinga, 23 hours ago</sub>  
  Five sectors are higher and six are lower in Wednesday's regular session, with cyclical sectors holding two of the top three positions.
- [Why Is CleanSpark Stock Surging on Wednesday?](https://www.google.com/goto?url=CAESpgEBxCJF1_0HlRIfJFCwQskC7n-U6cqg5clCIGbR63CrYR0MXkosINUTd9gWjBnvL1MJLVRegDk99Px7XQF-K1G2A8ss1adXzbh3QmXuCqlK_pJjpEHP96jy1_fAfmlJKjFx8dIIBAoakc5x5tzg91XejAtZTQKQC5hq_tzcScJn3nYmFreYby7oybgGhuadxmECJcqDf_e4l4kXXnk_Rm8iMvN6g-gQ&gsessionid=QNASBEkGCl-0jQjO-sNcfoNklwecjbuVBKh4S4GwodQnhLn4scFtCw)  
  <sub>Benzinga, 21 hours ago</sub>  
  CleanSpark Inc (NASDAQ: CLSK) stock climbed Wednesday alongside broader tech indexes following strong earnings from CoreWeave. Read the details here.
- [Tech Stocks Lead Market Rally as Investors Move Away from Safer Sectors](https://www.google.com/goto?url=CAESogEBxCJF1w-w7oULieb-svhXXaupfe_dwbry8zeODM6kzofhEh058-ZS_HxJZFxxscwZ92fjK6TJfpcmaaVXB64s4RcLwvVMzZ_Hy6MNuLnuK3GURZg6tEFQ5TblUvdW2J-mT8y5ZAIM-rswhqFGsJHsnlXwmXPPz6_Y3H9EEZyxQwh-geYPdybHuNDqPJ4GDRRyZagAFldUVParcIqrvzl0WkA&gsessionid=QNASBEkGCl-0jQjO-sNcfoNklwecjbuVBKh4S4GwodQnhLn4scFtCw)  
  <sub>TipRanks, 19 hours ago</sub>  
  Technology stocks are leading Wednesday's market rally after strong earnings from AI cloud company CoreWeave ($CRWV) helped ease worries about AI spending.
- [MPC Energy Solutions CFO Buys 50,000 Shares](https://www.google.com/goto?url=CAESmwEBxCJF18K4sT_P73VIE8X8WKA4KFnU-HYyOLC3F9jTlA8KaAVQijD2uviceq1pB5jIl7Kd1v4sN1n3I_nWVnFC7PEiYLng9QF5-G089_H7jym-hPDr9kqSIAvsrLWwMAe1EuVoRyY-mCKqkxIr74_D3qtf-oePHtCBNeNtRrf4YturD4EHLH0c6kx2rq3cywN8JySGLny3ZtcI4A&gsessionid=QNASBEkGCl-0jQjO-sNcfoNklwecjbuVBKh4S4GwodQnhLn4scFtCw)  
  <sub>TipRanks, 19 hours ago</sub>  
  MPC Energy Solutions NV ( ($DE:5IX) ) has provided an announcement. MPC Energy Solutions N.V. reported receiving trade notifications from persons...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.11% (+0.12 on the week) | 5-year 4.87% (+0.27 on the week) | 10-year 5.03% (+0.19 on the week) | 30-year 5.37% (+0.12 on the week)
Yield curve, 10-year minus 3-month: +0.92 points -- upward sloping (normal)
US dollar index: 102.91 (+1.36 on the week)
Volatility (VIX): 18.99 (-9.2 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.1% (2026-10-01) | jobless claims 200k (2026-11-07)
Policy and expectations: Fed target 4.00% | market expects 2.2% inflation over 10 years
Rate path: 2-year Treasury 4.56% vs Fed target 3.75-4.00% -- the bond market prices about 3 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score -0.20</summary>

```text
Last close 172.42 (bar of 2026-11-12), from 502 daily bars
Trend: vs 20d SMA 179.25 (-3.8%), 50d 187.39 (-8.0%), 200d 170.69 (+1.0%); 50d above 200d
Momentum: RSI(14) 41.4 | MACD -5.486 vs signal -4.773 (histogram -0.714)
Returns: 1d -1.1% | 5d +6.2% | 1m -9.5% | 3m -9.3%
52-week range: 127.50 - 202.00 (now 60.3% of the way up)
Volatility: ATR(14) 5.40 (3.1% of price) | annualised 20d 45.5%
Volume: 0.15x the 20-day average
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
Three-year record: +24.2% a year | beta to the market 1.56
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

<details><summary><b>What analysts and big funds say</b> — score +0.50</summary>

_Not available today._

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score +0.50</summary>

```text
Rolled up from the 5 largest holdings, 51.5% of the fund by weight
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 1.61 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +36.7% above the current prices
Holdings read: AAPL, NVDA, MSFT, AVGO, AMD
Recent rating changes among them:
  - AAPL: 2026-11-11 China Renaissance: up, Hold -> Buy
  - NVDA: 2026-11-12 Stifel: main, Buy -> Buy
  - MSFT: 2026-10-29 Bernstein: main, Outperform -> Outperform
  - AVGO: 2026-10-27 Rosenblatt: main, Buy -> Buy
  - AMD: 2026-11-12 William Blair: up, Market Perform -> Outperform
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
Share count change: 1 week: -0.9% (-1.16B) over 9d | 1 month: +9.7% (10.72B) over 30d
Shares outstanding: 702.46M | fund size: 121.12B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### US everyday goods (XLP) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Neutral overall: no macro surprise, flat fund flows, technicals bullish but low volume, analyst coverage strongly positive but not enough to outweigh neutral macro, fundamentals moderate.

**Main reasons it gave:**
- Technicals: price above 20‑day, 50‑day, and 200‑day SMAs with positive RSI (63.2) and MACD
- Analyst coverage: 100% buy on top holdings with a weighted price target +2.3% above current price
- Fund flows: flat share count over the past week and month, indicating no net inflow/outflow
- Macro: no policy or rate surprise; yields rose modestly and VIX fell, indicating stable environment
- Fundamentals: P/E 24.06, yield 2.5%, low beta 0.39, supporting defensive positioning

<details><summary><b>News</b> — score +0.00</summary>

- [State Street Health Care SPDR (XLV) Adds Eli Lilly and Johnson & Johnson on Nov. 10](https://finance.yahoo.com/healthcare/articles/state-street-health-care-spdr-110554537.html)  
  <sub>Yahoo Finance, 4 hours ago</sub>  
  This article first appeared on GuruFocus. In ETF activity on Tuesday, State Street Health Care Select Sector SPDR ETF (XLV) was a buyer only,...
- [RSPS: Consumer Staples ETF Reduces Company Risk (NYSEARCA:RSPS)](https://seekingalpha.com/article/4966643-rsps-consumer-staples-etf-reduces-company-risk)  
  <sub>Seeking Alpha, 17 hours ago</sub>  
  The Invesco S&P 500 Equal Weight Consumer Staples ETF offers equal-weight exposure to 33 consumer staples stocks. Discover more about the RSPS fund here.
- [In the Year of AI, Tech Isn’t the Top Sector](https://www.google.com/goto?url=CAESfwHEIkXXgo_AeOjJ7iJti3CL2KYpTGPBXBnXYlWH0MUbdmk2KiJI9Bsx15iW2QcBlgbWTZm1dewp0wJyh2B6g7Wg2HacJuU7fP49JOeMHuibxSYO2BohPWu8mhmk5lTmQ2m1Fbmq_INaUY-cNr3GLAUpDsTOSjqI7jKnrOXK-VA&gsessionid=tHsga-D96vxNOqM22orgdd6Yh_2h13dpSgInDM5VacUkM74MK6vICg)  
  <sub>ETF.com, 21 hours ago</sub>  
  Energy leads the S&P 500's sectors by a mile, and health care has caught up with tech.
- [Options Whale Alert: $488K Bearish Long Put Opened on $XLP](https://www.google.com/goto?url=CAESoAEBxCJF13PUM8nghuUqwjv_cvZQQ8V-zg0T64Ss3graqSTh5wvhXDYhK3n4C7QJ7JmNlLyRTBdcgpWIpOpvGjQCmqyIpZGmuXPRwsw8cjnI1RhIDnoPWjwkXKmS7FCtVGFpgh4r3nmnIWK8EgWGEQDzpSNgvFGmeuGsF8jVZR-lVhwOtgQLZM-N6teUmq5KPPuwUFMaBDKah8LwVtOe5gXy&gsessionid=tHsga-D96vxNOqM22orgdd6Yh_2h13dpSgInDM5VacUkM74MK6vICg)  
  <sub>Moomoo, 16 hours ago</sub>  
  ConsumerStaples Select Sector SPDR Fund(XLP.US)$ closed up 0.46% at $91.45. A trader bought 8000 Nov 20, 2026 $89.00 puts to open a Long Put.
- [Is Philip Morris International (PM) Fairly Valued On State Street’s Latest ETF Buy?](https://www.google.com/goto?url=CAESowEBxCJF18zo15GzsXHFGkhh4uSatCs6wA-7hH_w1zuT2VoBj3qBqTKsmaflLyyRy8N_YyZ1jzRh5es-DE8GntRIn9mu80pbQur7ne6e9O1jKeqB2NV8YpqSUclO0_zV9wtovgTKcN4WpbconKiO5dcLHjxA5cZU4a6pDGkNHaBpTgNhmstXY4r50XkiYyH_HwVpQsHa21lOfY7UkrwRP5gM3msr&gsessionid=tHsga-D96vxNOqM22orgdd6Yh_2h13dpSgInDM5VacUkM74MK6vICg)  
  <sub>Yahoo Finance, 16 hours ago</sub>  
  Philip Morris International (PM) is back in focus after State Street's Consumer Staples Select Sector SPDR ETF, XLP, lifted its exposure by US$25.2 million...
- [Only these two consumer staples stocks have sustained Strong Buy Quant ratings (XLP:NYSEARCA)](https://www.google.com/goto?url=CAESsQEBxCJF17TN5Km0mAHzk32vYd3_w_e1owAmu4LpSOw7KH0BqVQhLLe0UB-Mpcpw2soQcm_nQ2auifrJJdQKw2SbyFS6U_idarVQ-AlBsYkaVHlxG1wd_W3zBBQxSS4YudUnKh8V_OYXdZXCb2nUCGNGLy2srgNqDmKa7nGqVnqKXmuAtHF8CDW3yHhmouj3PG_Gj9jkPiShbU94QzaFWrbm1kFe_37wQMpL0DPd6ulwO6s&gsessionid=tHsga-D96vxNOqM22orgdd6Yh_2h13dpSgInDM5VacUkM74MK6vICg)  
  <sub>Seeking Alpha, 3 hours ago</sub>  
  Archer-Daniels-Midland and Dollar Tree are the only consumer staples stocks with Strong Buy Quant Ratings, held for 190 and 32 days at scores of 4.52 and...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.11% (+0.12 on the week) | 5-year 4.87% (+0.27 on the week) | 10-year 5.03% (+0.19 on the week) | 30-year 5.37% (+0.12 on the week)
Yield curve, 10-year minus 3-month: +0.92 points -- upward sloping (normal)
US dollar index: 102.91 (+1.36 on the week)
Volatility (VIX): 18.99 (-9.2 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.1% (2026-10-01) | jobless claims 200k (2026-11-07)
Policy and expectations: Fed target 4.00% | market expects 2.2% inflation over 10 years
Rate path: 2-year Treasury 4.56% vs Fed target 3.75-4.00% -- the bond market prices about 3 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.60</summary>

```text
Last close 91.47 (bar of 2026-11-12), from 502 daily bars
Trend: vs 20d SMA 89.27 (+2.5%), 50d 85.51 (+7.0%), 200d 84.84 (+7.8%); 50d above 200d
Momentum: RSI(14) 63.2 | MACD 1.725 vs signal 1.636 (histogram 0.089)
Returns: 1d +0.0% | 5d +0.2% | 1m +6.3% | 3m +6.2%
52-week range: 76.51 - 91.94 (now 97.0% of the way up)
Volatility: ATR(14) 1.49 (1.6% of price) | annualised 20d 23.6%
Volume: 0.10x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.40</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score +0.40</summary>

```text
Fund type: Consumer Defensive
What it holds: P/E 24.06 | P/B 4.52 | P/S 1.32 | 3y earnings growth n/a
Yield: 2.5%
Three-year record: +12.7% a year | beta to the market 0.39
Cost and size: expense ratio 0.08% | net assets 15.03B
What it is made of: Stocks 99.9%, Cash 0.1%
Largest holdings: Walmart Inc 11.1%, Costco Wholesale Corp 9.1%, Procter & Gamble Co 7.6%, Coca-Cola Co 7.4%, Philip Morris International Inc 6.6%
Sector mix: Consumer defensive 97.0%, Financial services 1.5%, Consumer cyclical 1.5%
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
Rolled up from the 5 largest holdings, 41.8% of the fund by weight
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 1.79 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +2.3% above the current prices
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
Shares outstanding: 210.17M | fund size: 19.22B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### US electricity and water (XLU) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> No macro surprise, flat fund flows, and no decisive technical break; bullish technical momentum and positive fundamentals are offset by a large reported net outflow.

**Main reasons it gave:**
- Net ETF outflow of $673M reported
- Technical momentum bullish (RSI 65.4, MACD positive) but price below 200‑day SMA
- Fund flows flat (0% change week/month)
- Analyst view bullish (80% buy) covering 39.4% of fund

<details><summary><b>News</b> — score +0.00</summary>

- [What Utilities Select Sector SPDR ETF (XLU) Sold: NextEra Leads on Nov. 10](https://finance.yahoo.com/markets/stocks/articles/utilities-select-sector-spdr-etf-110433066.html)  
  <sub>Yahoo Finance, 4 hours ago</sub>  
  This article first appeared on GuruFocus. State Street Utilities Select Sector SPDR ETF (XLU) posted a net outflow of $673.0 million in ETF activity on...
- [State Street Utilities Select Sector SPDR ETF (XLU) stock price, news, quote and history](https://au.finance.yahoo.com/quote/XLU/)  
  <sub>Yahoo Finance Australia, 16 hours ago</sub>  
  State Street Utilities Select Sector SPDR ETF (XLU) · 0.48% · 5.82% · -2.92% · 2.65% · -2.31% · 31.41% · 189.72%. Key events. Baseline. Advanced...
- [ETFs Are Net Sellers of Duke Energy (DUK) on Nov. 10](https://www.google.com/goto?url=CAESmgEBxCJF1wmKaVdDHJwdt7mKO5SLjlNoUrhkfNwJktymCS7pyRZXpFkeUDW_AK1CtB3kcCPfiDcrfiVgi735ccZ_eWmIksckCXdELR4YCuA4rgss4J2Ez-wbKBnbULJoIi5XyuMOvhUAJV3DwnsDC6MGRHacR6Mcc8VtbBqEVE0v0xNj-2kdGd67gDgjfr5LegzYGj2Xm5mK6XvV&gsessionid=FVqS1XrHHy2jL2LbPx44dsdZNL7_j-6FPRIrd6AEoMbAJvwJy4GCGw)  
  <sub>Yahoo Finance, 4 hours ago</sub>  
  ETFs sold a net $43.7 million of Duke Energy stock on Tuesday.
- [ETFs Are Net Sellers of Dominion (D) on Nov. 10](https://www.google.com/goto?url=CAESmQEBxCJF18NnI87kUkjBFJRBzZMNbduo2sGqy__V3LO0zryEWzxsF4UPpWadGDkCMWuuXFaiLI-xmgAWb0DtUXeoW3-cCsApDrHnNXK8SpP9pau7vNQKU0qNC9Pyt-ufPo4SkGv3pqT_lR2TU4TOBNgA-HiUZMBNpWwIeHj2LZpp3FllH7mNh8dqg3_A132BQ6oK_iNsAFQtHnM&gsessionid=FVqS1XrHHy2jL2LbPx44dsdZNL7_j-6FPRIrd6AEoMbAJvwJy4GCGw)  
  <sub>Yahoo Finance, 4 hours ago</sub>  
  This article first appeared on GuruFocus. The Utilities Select Sector SPDR (XLU) drove the move, cutting 431,816 shares worth $29.5 million. ETF activity on...
- [ETFs Are Net Sellers of PG&E (PCG) on Tuesday](https://www.google.com/goto?url=CAESjgEBxCJF12ctTnSqqLPrJgyrjoi0Vi535eSSW__NhXZGDHsFTSG69RaLt2Yk6DmeuDq25yNcO3vL4awu91IQeiBNHOXa1lZqRK-39XUnOU4SN0-XyHYb3oT3L7Z8Yr-S7l0BXayBPxky60Ya_vFzpqSD0Lua1VzKj-oljIng1B8tGiRws9OGlUv-vIUx19TU&gsessionid=FVqS1XrHHy2jL2LbPx44dsdZNL7_j-6FPRIrd6AEoMbAJvwJy4GCGw)  
  <sub>GuruFocus, 3 hours ago</sub>  
  XLU led the move, cutting its PG&E (PCG) stake by 2.77% as ETF activity produced a net $12.5 million of selling on Tuesday. More funds traded the other way,...
- [ETFs Are Net Sellers of American Electric Power (AEP) on Nov. 10](https://www.google.com/goto?url=CAESoQEBxCJF1y-tMZmQ9XQJ9eNMZoRqf_ShPezDPPOjMae5vLYFMNHdFWJmMHyr6DFmD33OBSkZ9uXT42rUNhUzSAbN1OHarQQ0G_weptkExG48LIMKG4Rp2KamteMBaF_r4v1mBr9IvHKT8_4aA4fTNl4AFdyZPWauR3S8A2gPpe-TDRUIYJfyKOH_xZQQPltSkIr1UZdmtx8ZjK4y7QkkVKrvIA&gsessionid=FVqS1XrHHy2jL2LbPx44dsdZNL7_j-6FPRIrd6AEoMbAJvwJy4GCGw)  
  <sub>GuruFocus, 3 hours ago</sub>  
  American Electric Power (AEP) saw its first day of net ETF selling in three sessions on Tuesday, with a net outflow of $19.0 million.
- [Evergy Stock: Analyst Estimates & Ratings](https://www.google.com/goto?url=CAEShgEBxCJF15KdXOrSIw03ZP71kwnpqtdinr2LnpGNfdCRxJOpWpIwwtUUai5dWXCA1T0wTd0JCuDx4rxGJr_L9GsVgp1RqPi3okZj82pUEk8f7TI7I9qLX6Ml5iUiJkUMR6DISNV_fHV1XK9HzEdyTfQ5LW3WQl75yHOU9y8BND52p0YU9Hnr5A&gsessionid=FVqS1XrHHy2jL2LbPx44dsdZNL7_j-6FPRIrd6AEoMbAJvwJy4GCGw)  
  <sub>inkl, 23 hours ago</sub>  
  Evergy has outperformed the broader market over the past year, and analysts are moderately optimistic about the stock's prospects.
- [ETFs Are Net Sellers of Vistra (VST) on Nov. 10](https://www.google.com/goto?url=CAES-wEBxCJF1_Bx-SDIrAwPcK-5nvShBTq9HGjIB04qCoh2AWygxAqBLx9GkNBHO0SFJtDQlIiWr45tOhgg0d1sHGUn2NijwFClLpqPe-zPycCtdcKPIYd5l4tqPM7Ljhn2JggYRb1-gOp5Ewntiv40a892-0GcllJgankoKEAeWqCI2z5IcyadrWYcARgIbPHPyVHk7IukS25FVbCQQkbGBlGm7-brfd8HNuS43qRKOs6sOBpQXDjCxoqa3bXxXRzN6OTYxpECUPejSkp0PhlJaj-CaydiFOY4B1a7fIsTLXLQ1Suj2aXj9AJQA7hTS62KoklFYfaURbBj-PdOZg&gsessionid=FVqS1XrHHy2jL2LbPx44dsdZNL7_j-6FPRIrd6AEoMbAJvwJy4GCGw)  
  <sub>GuruFocus, 3 hours ago</sub>  
  ETF flows turned negative for Vistra (VST) on Tuesday, snapping a one-day buying streak, as ETFs sold a net $17.9 million of the stock.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.11% (+0.12 on the week) | 5-year 4.87% (+0.27 on the week) | 10-year 5.03% (+0.19 on the week) | 30-year 5.37% (+0.12 on the week)
Yield curve, 10-year minus 3-month: +0.92 points -- upward sloping (normal)
US dollar index: 102.91 (+1.36 on the week)
Volatility (VIX): 18.99 (-9.2 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.1% (2026-10-01) | jobless claims 200k (2026-11-07)
Policy and expectations: Fed target 4.00% | market expects 2.2% inflation over 10 years
Rate path: 2-year Treasury 4.56% vs Fed target 3.75-4.00% -- the bond market prices about 3 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.30</summary>

```text
Last close 44.00 (bar of 2026-11-12), from 502 daily bars
Trend: vs 20d SMA 42.99 (+2.3%), 50d 41.88 (+5.1%), 200d 44.33 (-0.7%); 50d below 200d
Momentum: RSI(14) 65.4 | MACD 0.582 vs signal 0.521 (histogram 0.062)
Returns: 1d +0.4% | 5d +1.6% | 1m +5.5% | 3m -0.7%
52-week range: 39.25 - 47.73 (now 56.0% of the way up)
Volatility: ATR(14) 0.61 (1.4% of price) | annualised 20d 15.8%
Volume: 0.07x the 20-day average
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
Three-year record: +16.6% a year | beta to the market 0.34
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

<details><summary><b>What analysts and big funds say</b> — score +0.30</summary>

_Not available today._

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score +0.30</summary>

```text
Rolled up from the 5 largest holdings, 39.4% of the fund by weight
Ratings by weight: buy 80.0% | hold 20.0% | sell 0.0% (mean 2.03 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +8.5% above the current prices
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
Shares outstanding: 163.27M | fund size: 7.18B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### US shopping and leisure (XLY) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:** no explanation. It wrote only “NEUTRAL”, so the main reasons below are all it gave.

**Main reasons it gave:**
- Treasury yields rose modestly across the curve with no policy surprise
- Fund flows show net outflows of -1.9% over the past month, indicating bearish sentiment
- Analyst view covers 54% of fund with 100% buy rating and +12.7% price target, indicating bullish outlook
- Technicals show price above 20‑day, 50‑day, and 200‑day SMAs but volume is only 0.10× 20‑day average, limiting momentum

<details><summary><b>News</b> — score +0.00</summary>

- [These ten consumer discretionary stocks have held Strong Buy ratings for weeks (XLY:NYSEARCA)](https://seekingalpha.com/news/4670914-these-ten-consumer-discretionary-stocks-have-held-strong-buy-ratings-for-weeks?source=generic_rss)  
  <sub>Seeking Alpha, 20 hours ago</sub>  
  Ten consumer discretionary stocks hold Strong Buy Quant Ratings for 22 to 182 days; Life Time leads on longevity, while Victoria's Secret scores 4.94.
- [Tech Stocks Lead Market Rally as Investors Move Away from Safer Sectors](https://www.tipranks.com/news/tech-stocks-lead-market-rally-as-investors-move-away-from-safer-sectors)  
  <sub>TipRanks, 19 hours ago</sub>  
  Technology stocks are leading Wednesday's market rally after strong earnings from AI cloud company CoreWeave ($CRWV) helped ease worries about AI spending.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.11% (+0.12 on the week) | 5-year 4.87% (+0.27 on the week) | 10-year 5.03% (+0.19 on the week) | 30-year 5.37% (+0.12 on the week)
Yield curve, 10-year minus 3-month: +0.92 points -- upward sloping (normal)
US dollar index: 102.91 (+1.36 on the week)
Volatility (VIX): 18.99 (-9.2 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.1% (2026-10-01) | jobless claims 200k (2026-11-07)
Policy and expectations: Fed target 4.00% | market expects 2.2% inflation over 10 years
Rate path: 2-year Treasury 4.56% vs Fed target 3.75-4.00% -- the bond market prices about 3 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 121.89 (bar of 2026-11-12), from 502 daily bars
Trend: vs 20d SMA 117.03 (+4.2%), 50d 113.79 (+7.1%), 200d 115.45 (+5.6%); 50d below 200d
Momentum: RSI(14) 64.9 | MACD 2.163 vs signal 1.679 (histogram 0.484)
Returns: 1d +0.7% | 5d +3.6% | 1m +9.3% | 3m +3.1%
52-week range: 105.66 - 124.52 (now 86.1% of the way up)
Volatility: ATR(14) 2.18 (1.8% of price) | annualised 20d 27.3%
Volume: 0.10x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.30</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score +0.30</summary>

```text
Fund type: Consumer Cyclical
What it holds: P/E 24.15 | P/B 5.62 | P/S 2.30 | 3y earnings growth n/a
Yield: 0.8%
Three-year record: +15.4% a year | beta to the market 1.10
Cost and size: expense ratio 0.08% | net assets 22.40B
What it is made of: Stocks 99.9%, Cash 0.1%
Largest holdings: Amazon.com Inc 21.3%, Tesla Inc 18.8%, The Home Depot Inc 5.5%, McDonald's Corp 4.5%, TJX Companies Inc 4.1%
Sector mix: Consumer cyclical 98.8%, Technology 1.2%
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
Rolled up from the 5 largest holdings, 54.1% of the fund by weight
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 1.80 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +12.7% above the current prices
Holdings read: AMZN, TSLA, HD, MCD, TJX
Recent rating changes among them:
  - AMZN: 2026-11-03 Freedom Broker: main, Buy -> Buy
  - TSLA: 2026-11-05 GLJ Research: reit, Sell -> Sell
  - HD: 2026-11-10 Bernstein: main, Market Perform -> Market Perform
  - MCD: 2026-11-06 Argus Research: main, Buy -> Buy
  - TJX: 2026-11-10 UBS: main, Buy -> Buy
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
Share count change: 1 week: +0.3% (78.20M) over 9d | 1 month: -1.9% (-425.35M) over 30d
Shares outstanding: 185.01M | fund size: 22.55B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Poland (EPOL) · Sector or country — no answer, no confidence given

<details><summary><b>News</b> — score n/a</summary>

_No news found for this one today._

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score n/a</summary>

```text
US Treasury yields: 3-month 4.11% (+0.12 on the week) | 5-year 4.87% (+0.27 on the week) | 10-year 5.03% (+0.19 on the week) | 30-year 5.37% (+0.12 on the week)
Yield curve, 10-year minus 3-month: +0.92 points -- upward sloping (normal)
US dollar index: 102.91 (+1.36 on the week)
Volatility (VIX): 18.99 (-9.2 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.1% (2026-10-01) | jobless claims 200k (2026-11-07)
Policy and expectations: Fed target 4.00% | market expects 2.2% inflation over 10 years
Rate path: 2-year Treasury 4.56% vs Fed target 3.75-4.00% -- the bond market prices about 3 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score n/a</summary>

```text
Last close 43.78 (bar of 2026-11-12), from 502 daily bars
Trend: vs 20d SMA 43.81 (-0.1%), 50d 44.24 (-1.0%), 200d 40.66 (+7.7%); 50d above 200d
Momentum: RSI(14) 49.8 | MACD -0.157 vs signal -0.178 (histogram 0.021)
Returns: 1d +0.4% | 5d +0.9% | 1m -0.5% | 3m -1.5%
52-week range: 32.56 - 45.76 (now 85.0% of the way up)
Volatility: ATR(14) 0.70 (1.6% of price) | annualised 20d 24.7%
Volume: 0.20x the 20-day average
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
Three-year record: +35.7% a year | beta to the market 0.85
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
Ratings by weight: buy 68.5% | hold 31.5% | sell 0.0% (mean 2.28 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +6.2% above the current prices
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
Share count change: 1 week: +20.8% (177.55M) over 7d | 1 month: +23.7% (197.01M) over 30d
Shares outstanding: 23.51M | fund size: 1.03B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

**Data that was missing** (counted as 0.00, never guessed):
- news unavailable: Bright Data returned an empty body with its 200; nothing to parse (Bright Data said: x-brd-status-code 502; x-brd-error redirect location was rejected) (Bing's feed, direct: 2 headline(s), none naming EPOL)

### Canada (EWC) · Sector or country — no answer, no confidence given

<details><summary><b>News</b> — score n/a</summary>

- [iShares MSCI Canada ETF (EWC)](https://ca.finance.yahoo.com/quote/EWC/options/?date=1832025600&straddle=false&type=all)  
  <sub>Yahoo! Finance Canada, 13 hours ago</sub>  
  View the basic EWC option chain and compare options of iShares MSCI Canada ETF on Yahoo Finance.
- [META_TITLE_QUOTE](https://finance.yahoo.com/quote/EWZ/)  
  <sub>Yahoo Finance, 14 hours ago</sub>  
  EWZ tracks Brazilian equities through the MSCI Brazil Index. The latest political repricing triggered a sharp October selloff, while EWZ was down 1.60%...
- [Canadian AI-buildout stocks: hardware, power, engineering and software](https://www.google.com/goto?url=CAESvgEBxCJF1_RCPUxOgZ2DvRq8QH51bShUa0sUwr7oRVmVUlImesHL1k7jMG1mlSp9QJYwX68SchzWaQkL44xwa-nyTG0flTamp1-6QXc9KPxkeSvXFSuWKSEVgzsrnwYAI07XeUYnm7aosdXgvpif2qnv7REVbjO8oE9ZBr3eZHokbHyXuyVa5wgLZG6pGFUAm402Eum7qV7y9E3PX7GwvsD4YRaTP0rQS0nUFwl5CaKTOpLGi57v6FlsGAMh0Muc&gsessionid=8_BHV6gbaHbQPNPEHhn9Dt0kRvDRvba3_QZqpHW1XnSTlmbNjHjz9w)  
  <sub>Investing.com, 18 hours ago</sub>  
  Investing.com -- Canada has no pure-play chip giant. Its AI exposure sits in the supporting layers: hardware assembly, power, engineering and software.
- [Energy World announces major shareholder exit and director resignations](https://www.google.com/goto?url=CAESuAEBxCJF12XXVgqr7nBeqG6JNjSEcpmKCF9tjYmaOVUBlsVk9afCuGjQY7dF2HF67XHfvjg1cnFNPfNaFnpum3J43j1J0kY0Vfogs7I9zK4jEuSgj43zdDZq3F6OZSMw81KNEFXiyH8iBR7bHxRt_4yCnXrGZ8Pbt2V1xc7Z-RsqENPw8ih5z61OmqLJV-MNX8U9zyLegcu_77kIzLo8pvHzUuFIFZEJYrnj0ng0GhqqmY7BgNMTiHZn&gsessionid=8_BHV6gbaHbQPNPEHhn9Dt0kRvDRvba3_QZqpHW1XnSTlmbNjHjz9w)  
  <sub>TipRanks, 3 hours ago</sub>  
  Energy World Corporation Ltd ( ($AU:EWC) ) has shared an update. Energy World Corporation is an energy-sector company focused on commercialising assets,...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score n/a</summary>

```text
US Treasury yields: 3-month 4.11% (+0.12 on the week) | 5-year 4.87% (+0.27 on the week) | 10-year 5.03% (+0.19 on the week) | 30-year 5.37% (+0.12 on the week)
Yield curve, 10-year minus 3-month: +0.92 points -- upward sloping (normal)
US dollar index: 102.91 (+1.36 on the week)
Volatility (VIX): 18.99 (-9.2 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.1% (2026-10-01) | jobless claims 200k (2026-11-07)
Policy and expectations: Fed target 4.00% | market expects 2.2% inflation over 10 years
Rate path: 2-year Treasury 4.56% vs Fed target 3.75-4.00% -- the bond market prices about 3 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score n/a</summary>

```text
Last close 60.27 (bar of 2026-11-12), from 502 daily bars
Trend: vs 20d SMA 60.76 (-0.8%), 50d 60.20 (+0.1%), 200d 58.54 (+3.0%); 50d above 200d
Momentum: RSI(14) 48.8 | MACD 0.092 vs signal 0.181 (histogram -0.089)
Returns: 1d -0.3% | 5d +0.2% | 1m +1.7% | 3m -3.1%
52-week range: 49.91 - 62.64 (now 81.4% of the way up)
Volatility: ATR(14) 0.83 (1.4% of price) | annualised 20d 18.5%
Volume: 0.07x the 20-day average
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
Three-year record: +24.2% a year | beta to the market 0.73
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
Weighted price target: +5.7% above the current prices
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
Share count change: 1 week: +8.6% (602.13M) over 9d | 1 month: +5.8% (413.99M) over 30d
Shares outstanding: 125.72M | fund size: 7.58B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### South Korea (EWY) · Sector or country — no answer, no confidence given

<details><summary><b>News</b> — score n/a</summary>

- [META_TITLE_QUOTE](https://finance.yahoo.com/quote/EWZ/)  
  <sub>Yahoo Finance, 14 hours ago</sub>  
  EWZ tracks Brazilian equities through the MSCI Brazil Index. The latest political repricing triggered a sharp October selloff, while EWZ was down 1.60%...
- [Top Tokenized ETFs by Market Cap](https://www.coingecko.com/en/etfs)  
  <sub>CoinGecko, 1 hour ago</sub>  
  Discover the top ETFs (exchange-traded funds) by tokenized market cap. Track ETF prices alongside their tokenized prices, market cap, and volume on...
- [Daily ETF Flows: $4B Flows Into SOXX](https://www.google.com/goto?url=CAEShwEBxCJF10Y66l2sGGfGzJy3R2u7RGtp0TG4VNTV1mN5F57ExHQ9JNlUw3jLYEbJYSGmaRgYNnXvTyg_ZM4rjf8nvW6UVsd0JcXCR8icpCUyMq1uL50EosIwTuOurBBBR43fP_Qi8w0b8nTM8dmradU-woBogll6RSjvxbBgh6n3lOLc5XYAkxg&gsessionid=f4ExO3dV4BP--cyrQEaLuzIpnrdGF9RKa6xbxM-Ggb2v9VQTU4l3bw)  
  <sub>ETF.com, 20 hours ago</sub>  
  Here are the daily ETF fund flows for November 10, 2026.
- [Nikkei leads Asian sell-off after reports of Nvidia shake-up weigh on U.S. futures; Japan PPI beats forecasts](https://www.google.com/goto?url=CAESxAEBxCJF1yTYmjxPlE8I9iJwbVjGDM_kXgqrJZrrDq7T4ycZ6lbLygLoWKY2SC-hM-UihGg0Z3xJ9P14Qe7K12ku5vJWp9Y0OTlCsY-lm0SMNpOQs0PAz_F9YGbK5rsGbVt9QZD4IKFHTjhK8pWh0RmIxZtIdSOlYqKlC102kTgD83yxVWwS_NmH4Lq4hdQCskhQvB6aOlMP15GUKKLBwFpFFrb3iX2wcS2Cgbx92xhVamjtPbO6CUxAbUmyzF0-p30K1F22&gsessionid=f4ExO3dV4BP--cyrQEaLuzIpnrdGF9RKa6xbxM-Ggb2v9VQTU4l3bw)  
  <sub>Seeking Alpha, 8 hours ago</sub>  
  Asian equity markets retreated across the board on Thursday, pressured by a drop in U.S. equity futures following reports of potential leadership turmoil at...
- [EWY Dec 2026 186.000 call (EWY261211C00186000) Stock Price, News, Quote & History](https://www.google.com/goto?url=CAEScwHEIkXXLgIvbwCwDh647KM1eqHrdUuiAsVwCP4RYUG8YpA8gk0rD_TccRV-kHWhjNiAprQ0diMvIrvhExD7yKiu9HQ-U0djjaL4goeTCTpbq72yuXNt0FMMxy9inNdLb1UJ_8JUfPKxzbG7AcORnRXscig&gsessionid=f4ExO3dV4BP--cyrQEaLuzIpnrdGF9RKa6xbxM-Ggb2v9VQTU4l3bw)  
  <sub>Yahoo! Finance Canada, 3 hours ago</sub>  
  Find the latest EWY Dec 2026 186.000 call (EWY261211C00186000) stock quote, history, news and other vital information to help you with your stock trading...
- [iShares MSCI South Korea ETF (EWY) Price Prediction: South Korea ETF holds a rebound attempt as momentum stays mixed](https://www.google.com/goto?url=CAESlwEBxCJF15LJtL9nVTQHc665Tkup1Zoq7wShul-Nk2l0IcRSUqmJ-nmRBThtUsu2c8QNIKYaiRji4U0g-bR-L8Zcy6R_m75gbxzeIUVljIMiQNsieYn-RQ8LbRP9J3fh4sjvInp2e0gONwG8uaXMVg4aGJbY_pBOQBab7_qdJJ07pCowALMW-tMV5PonAQpCdsGABwvtNQkm&gsessionid=f4ExO3dV4BP--cyrQEaLuzIpnrdGF9RKa6xbxM-Ggb2v9VQTU4l3bw)  
  <sub>Blockchain News, 4 hours ago</sub>  
  iShares MSCI South Korea ETF (EWY) was quoted at $144.71, down 0.82% on the day, after trading between $144.56 and $150.55. The setup is still technically.
- [Direxion South Korea Bull 3X ETF (KORU) Price Prediction: Oversold Bounce or Further Compression After a Heavy Reset](https://www.google.com/goto?url=CAESpQEBxCJF16KNNlPvhTcxehFaYJEHT4CLZF2kvVlJeFIncuiK0TKcqNMu2euU16oe0wq1Y4InLmFaD2Vrop8eAhUYtk4XyuWiNStA7A-Q-4_ZgVbx8XV3KALLjJXT4XURBjM8QvEo8F8DEx3IlYHphw6JuZwdCFzHYvWiizwmMJfaAuGI9YkXJyp5nkrRjGanm2OW9n3g3CE6OG3-etDx52zLlWbkjkI&gsessionid=f4ExO3dV4BP--cyrQEaLuzIpnrdGF9RKa6xbxM-Ggb2v9VQTU4l3bw)  
  <sub>Blockchain News, 4 hours ago</sub>  
  Direxion South Korea Bull 3X ETF (KORU) is trading at $7.99 after a 3.03% drop in the latest 24 hours, leaving it below its 20-day and 50-day moving...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score n/a</summary>

```text
US Treasury yields: 3-month 4.11% (+0.12 on the week) | 5-year 4.87% (+0.27 on the week) | 10-year 5.03% (+0.19 on the week) | 30-year 5.37% (+0.12 on the week)
Yield curve, 10-year minus 3-month: +0.92 points -- upward sloping (normal)
US dollar index: 102.91 (+1.36 on the week)
Volatility (VIX): 18.99 (-9.2 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.1% (2026-10-01) | jobless claims 200k (2026-11-07)
Policy and expectations: Fed target 4.00% | market expects 2.2% inflation over 10 years
Rate path: 2-year Treasury 4.56% vs Fed target 3.75-4.00% -- the bond market prices about 3 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score n/a</summary>

```text
Last close 144.79 (bar of 2026-11-12), from 502 daily bars
Trend: vs 20d SMA 150.52 (-3.8%), 50d 169.21 (-14.4%), 200d 163.93 (-11.7%); 50d above 200d
Momentum: RSI(14) 42.6 | MACD -7.503 vs signal -7.523 (histogram 0.020)
Returns: 1d -2.0% | 5d +10.0% | 1m -9.4% | 3m -19.4%
52-week range: 88.53 - 219.20 (now 43.1% of the way up)
Volatility: ATR(14) 7.44 (5.1% of price) | annualised 20d 73.4%
Volume: 0.16x the 20-day average
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
Three-year record: +35.4% a year | beta to the market 2.62
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
Share count change: 1 week: -7.3% (-1.82B) over 9d | 1 month: +8.0% (1.70B) over 30d
Shares outstanding: 159.71M | fund size: 23.12B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Brazil (EWZ) · Sector or country — no answer, no confidence given

<details><summary><b>News</b> — score n/a</summary>

- [Brazil Promised to Spend Less. The Real Is Betting It's Not Enough](http://www.bing.com/news/apiclick.aspx?ref=FexRss&aid=&tid=6af5d2c51628412383bce1f59f2174e4&url=https%3a%2f%2fwww.ainvest.com%2fnews%2fbrazil-promised-spend-real-betting-2611%2f&c=13376315092872748948&mkt=en-us)  
  <sub>ainvest, 23h ago</sub>  
  Brazil's Lula government proposed a 2027 fiscal plan to cap real spending growth at 2% and cut tax breaks, aiming to reduce the primary deficit by ...
- [Bitrue expands tradable markets with new USDT perpetuals on Brazilian equities and Latin American e-commerce](http://www.bing.com/news/apiclick.aspx?ref=FexRss&aid=&tid=6af5d2c51628412383bce1f59f2174e4&url=https%3a%2f%2ftradersunion.com%2fnews%2fbrokers-news%2fshow%2f4207874-bitrue-unveils-new-futures-contracts%2f&c=12078358632879491687&mkt=en-us)  
  <sub>tradersunion, 23h ago</sub>  
  Bitrue launches seven new USDT-settled perpetual futures contracts, including EWZ/USDT and MELI/USDT, with trading starting July 10, 2026.
- [Brazil's half-point answer to a nine-point deficit](http://www.bing.com/news/apiclick.aspx?ref=FexRss&aid=&tid=6af5d2c51628412383bce1f59f2174e4&url=https%3a%2f%2fwww.ainvest.com%2fnews%2fbrazil-point-answer-point-deficit-2611%2f&c=1576092989460249788&mkt=en-us)  
  <sub>ainvest, 27h ago</sub>  
  Brazil's government proposes 0.5% GDP fiscal tightening via spending caps and tax reforms to address a 9% deficit.
- [Verde de Stuhlberger pisa no freio após eleição: veja a estratégia da gestora para o Lula 4](http://www.bing.com/news/apiclick.aspx?ref=FexRss&aid=&tid=6af5d2c51628412383bce1f59f2174e4&url=https%3a%2f%2fwww.msn.com%2fpt-br%2fdinheiro%2feconomia%2fverde-de-stuhlberger-pisa-no-freio-ap%25C3%25B3s-elei%25C3%25A7%25C3%25A3o-veja-a-estrat%25C3%25A9gia-da-gestora-para-o-lula-4%2far-AA2hfyDc&c=2332453175418740405&mkt=en-us)  
  <sub>Estadão on MSN, 24h ago</sub>  
  Fundo multimercado caiu 1,96% em outubro, enquanto sua estratégia de ações desvalorizou 10,11% ...
- [Nvidia derruba futuros de NY e pressiona bolsas globais](http://www.bing.com/news/apiclick.aspx?ref=FexRss&aid=&tid=6af5d2c51628412383bce1f59f2174e4&url=https%3a%2f%2fwww.spacemoney.com.br%2feconomia%2fexterior%2fnvidia-crise-bolsas-globais%2f&c=16692607338611337033&mkt=en-us)  
  <sub>SpaceMoney, 13h ago</sub>  
  No pré-mercado de Nova York, o EWZ, ETF que replica o desempenho do índice MSCI Brazil 25/50, recuava 0,03%, a US$ 32,43, às 8h22 (horário de Brasília). Negociado na NYSE Arca, o fundo reúne ações de ...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score n/a</summary>

```text
US Treasury yields: 3-month 4.11% (+0.12 on the week) | 5-year 4.87% (+0.27 on the week) | 10-year 5.03% (+0.19 on the week) | 30-year 5.37% (+0.12 on the week)
Yield curve, 10-year minus 3-month: +0.92 points -- upward sloping (normal)
US dollar index: 102.91 (+1.36 on the week)
Volatility (VIX): 18.99 (-9.2 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.1% (2026-10-01) | jobless claims 200k (2026-11-07)
Policy and expectations: Fed target 4.00% | market expects 2.2% inflation over 10 years
Rate path: 2-year Treasury 4.56% vs Fed target 3.75-4.00% -- the bond market prices about 3 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score n/a</summary>

```text
Last close 31.81 (bar of 2026-11-12), from 502 daily bars
Trend: vs 20d SMA 35.51 (-10.4%), 50d 37.71 (-15.7%), 200d 37.04 (-14.1%); 50d above 200d
Momentum: RSI(14) 31.3 | MACD -2.051 vs signal -1.792 (histogram -0.259)
Returns: 1d -1.9% | 5d +0.2% | 1m -25.3% | 3m -6.2%
52-week range: 30.97 - 43.54 (now 6.7% of the way up)
Volatility: ATR(14) 1.11 (3.5% of price) | annualised 20d 73.3%
Volume: 0.04x the 20-day average
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
Three-year record: +5.7% a year | beta to the market 0.92
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
Weighted price target: +36.3% above the current prices
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
Shares outstanding: 200.55M | fund size: 6.38B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Defence and aerospace (ITA) · Sector or country — no answer, no confidence given

<details><summary><b>News</b> — score n/a</summary>

- [ITA Airways promo codes, coupons, and deals for November 2026](http://www.bing.com/news/apiclick.aspx?ref=FexRss&aid=&tid=6af5d1b8cef44c1685b0a8816f33f19e&url=https%3a%2f%2fwww.usatoday.com%2fdeals%2fita-airways&c=3433505390676177068&mkt=en-us)  
  <sub>USA Today, 27h ago</sub>  
  Our team of savvy editors independently handpicks all recommendations. If you make a purchase through our links, we may earn a commission. Deals and coupons were accurate at the time of publication ...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score n/a</summary>

```text
US Treasury yields: 3-month 4.11% (+0.12 on the week) | 5-year 4.87% (+0.27 on the week) | 10-year 5.03% (+0.19 on the week) | 30-year 5.37% (+0.12 on the week)
Yield curve, 10-year minus 3-month: +0.92 points -- upward sloping (normal)
US dollar index: 102.91 (+1.36 on the week)
Volatility (VIX): 18.99 (-9.2 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.1% (2026-10-01) | jobless claims 200k (2026-11-07)
Policy and expectations: Fed target 4.00% | market expects 2.2% inflation over 10 years
Rate path: 2-year Treasury 4.56% vs Fed target 3.75-4.00% -- the bond market prices about 3 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score n/a</summary>

```text
Last close 72.87 (bar of 2026-11-12), from 502 daily bars
Trend: vs 20d SMA 70.10 (+4.0%), 50d 70.50 (+3.4%), 200d 75.96 (-4.1%); 50d below 200d
Momentum: RSI(14) 58.6 | MACD 0.501 vs signal 0.005 (histogram 0.497)
Returns: 1d -0.5% | 5d +7.0% | 1m +7.0% | 3m -13.7%
52-week range: 66.08 - 84.41 (now 37.1% of the way up)
Volatility: ATR(14) 1.76 (2.4% of price) | annualised 20d 29.8%
Volume: 0.04x the 20-day average
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
Three-year record: +24.8% a year | beta to the market 1.03
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
Weighted price target: +15.0% above the current prices
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
Share count change: 1 week: +201.1% (8.22B) over 7d | 1 month: +187.6% (8.03B) over 30d
Shares outstanding: 168.85M | fund size: 12.30B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### US house builders (XHB) · Sector or country — no answer, no confidence given

<details><summary><b>News</b> — score n/a</summary>

- [State Street SPDR S&P Homebuilders ETF (XHB)](http://www.bing.com/news/apiclick.aspx?ref=FexRss&aid=&tid=6af5d200f7584b628df70faaf8256ed6&url=https%3a%2f%2ffinance.yahoo.com%2fquote%2fXHB%2fnews%2f&c=10180005848060629306&mkt=en-us)  
  <sub>Yahoo Finance, 218h ago</sub>  
  The above button links to Coinbase. Yahoo Finance is not a broker-dealer or investment adviser and does not offer securities or cryptocurrencies for sale or facilitate trading. Coinbase pays us for ...
- [房屋建筑商指数ETF-SPDR收跌0.07%，成交额2.41亿美元](http://www.bing.com/news/apiclick.aspx?ref=FexRss&aid=&tid=6af5d200f7584b628df70faaf8256ed6&url=https%3a%2f%2ffinance.sina.com.cn%2fstock%2fusstock%2fnotice%2f2026-11-12%2fdoc-iniymmzp1884093.shtml&c=9861035624291482073&mkt=en-us)  
  <sub>新浪财经, 23h ago</sub>  
  11月12日，房屋建筑商指数ETF-SPDR（XHB）收跌0.07%，报103.1美元，成交额2.41亿美元，市值15.67亿美元。 声明：市场有风险，投资需谨慎。本文基于第三方数据库发布，不代表新浪财经观点，任何在本文出现的信息均只作为参考，不构成个人投资建议。如有出入请以实际公告为准。如有疑问，请联系biz@staff.sina.com.cn。

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score n/a</summary>

```text
US Treasury yields: 3-month 4.11% (+0.12 on the week) | 5-year 4.87% (+0.27 on the week) | 10-year 5.03% (+0.19 on the week) | 30-year 5.37% (+0.12 on the week)
Yield curve, 10-year minus 3-month: +0.92 points -- upward sloping (normal)
US dollar index: 102.91 (+1.36 on the week)
Volatility (VIX): 18.99 (-9.2 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.1% (2026-10-01) | jobless claims 200k (2026-11-07)
Policy and expectations: Fed target 4.00% | market expects 2.2% inflation over 10 years
Rate path: 2-year Treasury 4.56% vs Fed target 3.75-4.00% -- the bond market prices about 3 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score n/a</summary>

```text
Last close 103.75 (bar of 2026-11-12), from 502 daily bars
Trend: vs 20d SMA 100.60 (+3.1%), 50d 98.56 (+5.3%), 200d 104.75 (-1.0%); 50d below 200d
Momentum: RSI(14) 56.0 | MACD 1.771 vs signal 1.454 (histogram 0.317)
Returns: 1d +0.6% | 5d -0.1% | 1m +11.8% | 3m -4.8%
52-week range: 92.84 - 121.36 (now 38.3% of the way up)
Volatility: ATR(14) 2.83 (2.7% of price) | annualised 20d 39.1%
Volume: 0.11x the 20-day average
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
Three-year record: +10.9% a year | beta to the market 1.40
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
Weighted price target: +7.7% above the current prices
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
Share count change: 1 week: +12.7% (184.27M) over 7d | 1 month: +4.7% (74.15M) over 30d
Shares outstanding: 15.81M | fund size: 1.64B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### US media and communication (XLC) · Sector or country — no answer, no confidence given

<details><summary><b>News</b> — score n/a</summary>

- [State Street Communication Services Select Sector SPDR ETF (XLC) stock price, news, quote and history](https://sg.finance.yahoo.com/quote/XLC/)  
  <sub>Yahoo Finance Singapore, 3 hours ago</sub>  
  State Street Communication Services Select Sector SPDR ETF (XLC) · 3.47% · -1.61% · -6.04% · -8.19% · -4.13% · 35.38% · 118.51%. Key...
- [What State Street Comm Services SPDR (XLC) Bought: No Buys, META Sold on Tuesday](https://finance.yahoo.com/markets/stocks/articles/state-street-comm-services-spdr-110445746.html)  
  <sub>Yahoo Finance, 4 hours ago</sub>  
  This article first appeared on GuruFocus. State Street Communication Services Select Sector SPDR ETF (XLC) extended a one-sided stretch of ETF activity in...
- [In the Year of AI, Tech Isn’t the Top Sector](https://www.google.com/goto?url=CAESfwHEIkXXgUy1KHqpIcYMZRJxTT3DokH85vNNfn5yMILcF10vGR3BsRT1PKHQx1VLc9NjiTt7A0rT_Ljca2GwY0qfTe6Di_3reaCW6gGjWUH9-ceXOZBblrNbS_hzAtKtS3-YA-Up8UTHg6BwYDQPoY5n2J1BKll81cYLEYCWNtU&gsessionid=wpLiDJ0xzUs7Uf6UuMQs1OMj3FypRF3xjVJh7Hn3XsS0nNA1HJdv8A)  
  <sub>ETF.com, 21 hours ago</sub>  
  Energy leads the S&P 500's sectors by a mile, and health care has caught up with tech.
- [A 6-Day Winning Streak Has T-Mobile US Stock Up 12%](https://www.google.com/goto?url=CAESrAEBxCJF1z-68jLLStD__tX0zHsV8L7D86Q8tqMNrxcXJfSvpw_FzrotjDJNBQry5YxVGovZvPbRD1lJyITGimE3_gf2Jjo7GpS0nLa3LtZxOvQTIqDzodMKLm6lzMHML0DIzBBkYVommfxus5Z1LP8-Bn31QmktNfZ8jSLTnAHbR_VKnnJhe3guv-z5fuX3jCAPkwIqqqv6jeC1CFsikF81v7za2tgMO8dUyei9&gsessionid=wpLiDJ0xzUs7Uf6UuMQs1OMj3FypRF3xjVJh7Hn3XsS0nNA1HJdv8A)  
  <sub>Trefis, 6 hours ago</sub>  
  Shares of T-Mobile US (TMUS) have closed higher in each of the last 6 sessions, a cumulative gain of 11.5%. That added about $19.0 billion to the company's...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score n/a</summary>

```text
US Treasury yields: 3-month 4.11% (+0.12 on the week) | 5-year 4.87% (+0.27 on the week) | 10-year 5.03% (+0.19 on the week) | 30-year 5.37% (+0.12 on the week)
Yield curve, 10-year minus 3-month: +0.92 points -- upward sloping (normal)
US dollar index: 102.91 (+1.36 on the week)
Volatility (VIX): 18.99 (-9.2 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.1% (2026-10-01) | jobless claims 200k (2026-11-07)
Policy and expectations: Fed target 4.00% | market expects 2.2% inflation over 10 years
Rate path: 2-year Treasury 4.56% vs Fed target 3.75-4.00% -- the bond market prices about 3 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score n/a</summary>

```text
Last close 108.42 (bar of 2026-11-12), from 502 daily bars
Trend: vs 20d SMA 105.61 (+2.7%), 50d 109.50 (-1.0%), 200d 112.43 (-3.6%); 50d below 200d
Momentum: RSI(14) 55.2 | MACD -0.716 vs signal -1.558 (histogram 0.841)
Returns: 1d -0.2% | 5d +3.9% | 1m -2.2% | 3m -4.0%
52-week range: 99.90 - 120.08 (now 42.2% of the way up)
Volatility: ATR(14) 1.97 (1.8% of price) | annualised 20d 22.5%
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
Three-year record: +17.7% a year | beta to the market 0.93
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
Weighted price target: +30.0% above the current prices
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
Share count change: 1 week: -10.3% (-2.49B) over 7d | 1 month: -2.5% (-545.34M) over 30d
Shares outstanding: 199.07M | fund size: 21.58B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

## Commodities

### Silver (SLV) · Commodity — NEUTRAL, confidence 0.20

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Downtrend, large outflows, negative cost of holding, and no macro catalyst lead to a neutral view with low conviction.

**Main reasons it gave:**
- Share count fell 19.4% in 9 days (large outflows)
- Price 45.31 below 20‑day SMA 48.11, 50‑day SMA 53.20, 200‑day SMA 62.23 (downtrend)
- Cost of holding -1.8% per year (steady drag on long)
- No macro surprise: yields rose, dollar up, Fed unchanged
- Positioning: net long 3.5% OI, short crowding 8% percentile (weak bullish bias)

<details><summary><b>News</b> — score +0.00</summary>

- [Sprott Physical Silver Trust (PSLV.TO) Stock Price, News, Quote & History](https://ca.finance.yahoo.com/quote/PSLV.TO/)  
  <sub>Yahoo! Finance Canada, 3 hours ago</sub>  
  Find the latest Sprott Physical Silver Trust (PSLV.TO) stock quote, history, news and other vital information to help you with your stock trading and...
- [Is the iShares Silver Trust a Buy After Falling Nearly 60% From Its High?](https://www.fool.com/investing/2026/11/11/is-the-ishares-silver-trust-a-buy-after-falling-mo/)  
  <sub>The Motley Fool, 18 hours ago</sub>  
  The iShares Silver Trust (SLV +0.37%), the world's largest silver exchange-traded fund (ETF), is one of the easiest ways to invest in silver without buying...
- [Silver Demand Beyond the U.S.: What India’s ETF Flows Reveal](https://www.google.com/goto?url=CAESoAEBxCJF13_5khOKvdJAsdf8qJxAgOyOlgVg1aLDa934CtVnc2LXE2vnTz_2D3zHLD3OceTCiiLamupeT7TkQrao3caVZ0uPP57caWnyoolzO-heUwmtGYm7bCUcySV7bHjV-Ooq_GgSbNb9gfmoqmez4Sj7BcgH-uejOk5-BW1kDuQ7nm4wSxOZCv_vc5dkokn0ZgYopllQ9ChJtw-ecUvp&gsessionid=mkPwPHGKqljsKoGlSlZCbbGPGsotgDml4tJzPO84b0KtltAUNHFt6w)  
  <sub>GoldSilver, 21 hours ago</sub>  
  India's silver ETFs recorded a 56.6% increase in net inflows in October 2026. For U.S. bullion owners, the report offers another perspective on silver...
- [News by CNBC TV18 on TradingView, 2026-11-12 — cnbctv:1c6b50100094b:0](https://www.google.com/goto?url=CAESdQHEIkXXXhZ1F51LOiBt3qVKjVUUUAeRVUq9aD078-dL_5Nl47xVAVWYfjNdb5ABZx1M3ugDvo5vqVRcB9av38DX3vhlr3QBtDXZj8sXEfkZJq83EV6yRzWusIo9Yz19I2JBNsvaQd0-nxg-7mIOewjztdWSAw&gsessionid=mkPwPHGKqljsKoGlSlZCbbGPGsotgDml4tJzPO84b0KtltAUNHFt6w)  
  <sub>TradingView, 3 hours ago</sub>  
  Nippon India Mutual Fund's Gold and Silver exchange-traded funds (ETFs) together accounted for around 55% of the average daily turnover in the two...
- [Nippon India Mutual Fund (NIMF) Dominates Volumes in Gold & Silver ETFs during Diwali 2026 with 55% Market Share Rs 806 Crore Combined Average Daily Turnover; Gold BeES at 54% and Silver ETF at 57% Market Share](https://www.google.com/goto?url=CAESvQIBxCJF1-0np6YjKK_XJEuWmiNI0G8dDR7mpoN8mtUFNN5ZhWwMcEz_uig5IYTw14eKth4s8CLJ2rTy5Pn_pBINswvuD0-mUXLEdIwy5ijBqxiDEI44GcrTc8cD2PRVS_Fp776UvJKRBE8UpKmctdkJ25VGXlQGjQuY200cigA3uO5t0mmZx3vzFMfvMUwFDXN5X365QJpDI3lag_rs73PJA-sfZQy_1iExGa6Fy6f6sBBSV3etGMa5Ru9sukuYwCpLa6FJqSVNc4nN0z1IQbcUQ1QimcWIvKVCEEi7LhIJPTMHPs98OAF8LvBudeGFES5U3xyOqD5iK9cVrWR9R7WIHTJzI6E5lvXb7khBuzahgpUBkoFRwAo3psunljTDhN11zZ4qBpUg_h7dbUc68OywDvJPD63jDjLi2IcDwA&gsessionid=mkPwPHGKqljsKoGlSlZCbbGPGsotgDml4tJzPO84b0KtltAUNHFt6w)  
  <sub>Investment Guru India, 6 hours ago</sub>  
  ... * Combined: rs 806 crore combined Average Daily Turnover (ADT) across Nippon India's Gold and Silver ETFs during Diwali 2026, capturing a ~55% share of...
- [Current price of silver as of Thursday, Nov. 12, 2026](https://www.google.com/goto?url=CAESfAHEIkXXZACN3CW-zNzADhQ95XQUO30IKsiHiYUXHFDaXcVvQEdaIDj6UDrbMuyZ9SmQmay3BuSI0-ZRhIbYZmB48zLSczqrqfyUdCnSr04mcL1PnxaLpk7myWcgECDL_jjoojzyjFZlWuzSWrab9v-PXHIxt8y-IZqd8jc&gsessionid=mkPwPHGKqljsKoGlSlZCbbGPGsotgDml4tJzPO84b0KtltAUNHFt6w)  
  <sub>Fortune, 2 hours ago</sub>  
  If you're worried about increased inflation, adding precious metals like silver to your portfolio can be a smart choice.
- [Critical Mineral Miners Dip: Time to Buy Copper & Uranium?](https://www.google.com/goto?url=CAESoAEBxCJF14vVBOi_ntH10HDQgFs0zqgRR1Lg_0XDcFF2AfF5lN5WAA3NNNGtoE15sEy98Gt1ptpiiwnSwk5ZeOkhc7vLW0ZiC_5T3-2LS85rKdcA7_w4CiTaMudixguh66LYVj9zBWr7BbdaSGHUqZTMZkcEpO9Uzjve1u-IqMSdA4NSlkBgS56g9dMoKUV5OV2G3xwzaIQJC_aIB2h6Xbpq&gsessionid=mkPwPHGKqljsKoGlSlZCbbGPGsotgDml4tJzPO84b0KtltAUNHFt6w)  
  <sub>ETF Database, 22 hours ago</sub>  
  October may have been a difficult month for some mining companies, but this sector still warrants focused exposure through the ETF wrapper.
- [Is CoreWeave's Rally Durable? Nvidia Stock Can Fall 25% If Huang Leaves](https://www.google.com/goto?url=CAESuAEBxCJF1wFU9Mwt_fQuoc_ISfHScMkx342-Mfwn7ng0V_VDqY2V7EJx17FtWwZv56gqDgPf9giKQ8RbG5p1tlKSs-QGTNPv5mC1A7Eo3RR5EBpNO4BgnbwpGu-PGKoI4jK0xltVQf5lz5kn8EMgWcuGUcPL9ND_vpS8CmKPY4n0exhG2IGR1ZC1nMltIwG-qHISGqhINa0DhUfxSota0VtlkrTmXmEYex2b5E2OgmOsI12K0aImaTeX&gsessionid=mkPwPHGKqljsKoGlSlZCbbGPGsotgDml4tJzPO84b0KtltAUNHFt6w)  
  <sub>Benzinga, 21 hours ago</sub>  
  AI Trade Rally Please click here for an enlarged chart of Direxion Daily Semiconductor Bull 3X ETF (NYSE:SOXL). Note the following: Semiconductors reflect...
- [Which Gold ETF Is the Better Buy: iShares’ Gold Trust IAU or Sprott’s Gold Miners SGDM?](https://www.google.com/goto?url=CAESngEBxCJF1_8ZWI1RMYbGHItBqjD9Z9AlXvoeQb3z1RCtHvXrVkJ5BMzKID5gZUFcht2Ngafa5UTYZLMnn2tgInZcwFEE_dCn0L6A3UIHkL_WBAge0tCVoRNDSmmhrCKblGJeds0eD_U8LKMlkRG-xKkOB98HNNMivvkECBwWKb_pWMIp9Dp9Bnylbd6BzwCobh31ceKbqI_b2LBWQ5fyeg&gsessionid=mkPwPHGKqljsKoGlSlZCbbGPGsotgDml4tJzPO84b0KtltAUNHFt6w)  
  <sub>Yahoo Finance, 16 hours ago</sub>  
  Mining stocks have led recently, but they have also fallen much harder than bullion. Cost and volatility differences reveal which fund fits your goals.
- [Nippon India Mutual Fund dominates volumes in gold & silver ETFs during Diwali 2026 with 55% market share](https://www.google.com/goto?url=CAES5QEBxCJF1xY-gdFbGFDBdMDSFfsAuM6GFK_aPgYlcU394jGnG_Ez69BfUoVM4iXoN7PebmCRqL3q5xnebcizxgRCJCPxGFMfPpD0npF43nk0tKSFDh50CzV2GdRm5hOr5HTGzbCsiClLgNDxcP6LSg0m4sj4lvBCFdhkUgw_qEmQ4hLWrfsOHJuAxFyZJoZ34pN2hpkqDjNMY7LHSYqXMo5LAHfo8uDLJVRAYTR_fuvrNBEp3Hyj2tJ8Kuhs_igIs98R0rft2sScVcWClQo8KXlXWI4JZtKgN4J6ttyojRVjLyHN5YVV&gsessionid=mkPwPHGKqljsKoGlSlZCbbGPGsotgDml4tJzPO84b0KtltAUNHFt6w)  
  <sub>The Economic Times, 5 hours ago</sub>  
  Nippon India Mutual Fund's Gold BeES and Silver ETF together accounted for 55% of the average daily trading turnover across gold and silver ETFs during...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.11% (+0.12 on the week) | 5-year 4.87% (+0.27 on the week) | 10-year 5.03% (+0.19 on the week) | 30-year 5.37% (+0.12 on the week)
Yield curve, 10-year minus 3-month: +0.92 points -- upward sloping (normal)
US dollar index: 102.91 (+1.36 on the week)
Volatility (VIX): 18.99 (-9.2 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.1% (2026-10-01) | jobless claims 200k (2026-11-07)
Policy and expectations: Fed target 4.00% | market expects 2.2% inflation over 10 years
Rate path: 2-year Treasury 4.56% vs Fed target 3.75-4.00% -- the bond market prices about 3 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 45.31 (bar of 2026-11-12), from 502 daily bars
Trend: vs 20d SMA 48.11 (-5.8%), 50d 53.20 (-14.8%), 200d 62.23 (-27.2%); 50d below 200d
Momentum: RSI(14) 35.2 | MACD -2.024 vs signal -2.168 (histogram 0.144)
Returns: 1d -2.9% | 5d -3.5% | 1m -9.8% | 3m -22.5%
52-week range: 44.60 - 105.60 (now 1.2% of the way up)
Volatility: ATR(14) 1.52 (3.4% of price) | annualised 20d 42.3%
Volume: 0.23x the 20-day average
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
Cost of holding this fund instead of silver itself: -1.8% a year -- a steady drag
Measured: 3 months: fund -22.5%, commodity -22.6%, gap +0.1% | 6 months: fund -40.0%, commodity -40.8%, gap +0.8% | 12 months: fund -2.5%, commodity -0.7%, gap -1.8%
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

<details><summary><b>Buying and selling by company insiders</b> — score +0.15</summary>

_Not available today._

</details>

<details><summary><b>Who is positioned how</b> — score +0.15</summary>

```text
Contract: SILVER - COMMODITY EXCHANGE INC. (positions as of 2026-11-03, published the following Friday)
Large speculators: net long 3.5% of open interest (115,583 contracts)
Change on the week: +0.6% of open interest
Crowding: 8% percentile over 52 weeks -- a crowded short by the standards of the past year
Read this as crowding, not as a forecast: an extreme is as often the end of a move as the middle of one.
```

</details>

<details><summary><b>Money going into and out of this fund</b> — score +0.15</summary>

```text
Direction: money going out (1 month)
Share count change: 1 week: -19.4% (-5.83B) over 9d | 1 month: -3.2% (-787.20M) over 30d
Shares outstanding: 533.80M | fund size: 24.18B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Sugar (CANE) · Commodity — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:** no explanation. It wrote only “NEUTRAL”, so the main reasons below are all it gave.

**Main reasons it gave:**
- Price 10.98 below 20‑day SMA 11.56 and 50‑day SMA 11.61
- RSI 36.9 (below 40) and MACD -0.215 below signal -0.136 (bearish momentum)
- CFTC net long 18.8% of open interest, crowding 90th percentile, week‑on‑week change -0.9%
- Cost of holding -8.0% annual roll cost (heavy cost for long)
- Share count +21.8% over 30 days (strong inflows)

<details><summary><b>News</b> — score +0.00</summary>

_No news found for this one today._

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.11% (+0.12 on the week) | 5-year 4.87% (+0.27 on the week) | 10-year 5.03% (+0.19 on the week) | 30-year 5.37% (+0.12 on the week)
Yield curve, 10-year minus 3-month: +0.92 points -- upward sloping (normal)
US dollar index: 102.91 (+1.36 on the week)
Volatility (VIX): 18.99 (-9.2 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.1% (2026-10-01) | jobless claims 200k (2026-11-07)
Policy and expectations: Fed target 4.00% | market expects 2.2% inflation over 10 years
Rate path: 2-year Treasury 4.56% vs Fed target 3.75-4.00% -- the bond market prices about 3 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score -0.20</summary>

```text
Last close 10.98 (bar of 2026-11-12), from 502 daily bars
Trend: vs 20d SMA 11.56 (-5.0%), 50d 11.61 (-5.4%), 200d 10.29 (+6.8%); 50d above 200d
Momentum: RSI(14) 36.9 | MACD -0.215 vs signal -0.136 (histogram -0.079)
Returns: 1d -1.5% | 5d -1.6% | 1m -10.9% | 3m +2.1%
52-week range: 9.02 - 12.47 (now 57.0% of the way up)
Volatility: ATR(14) 0.21 (1.9% of price) | annualised 20d 26.6%
Volume: 0.06x the 20-day average
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
Cost of holding this fund instead of sugar itself: -8.0% a year -- heavy: rolling contracts costs this fund real money
Measured: 3 months: fund +2.1%, commodity +9.2%, gap -7.1% | 6 months: fund +8.8%, commodity +20.9%, gap -12.1% | 12 months: fund +19.1%, commodity +27.2%, gap -8.0%
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

<details><summary><b>Buying and selling by company insiders</b> — score -0.25</summary>

_Not available today._

</details>

<details><summary><b>Who is positioned how</b> — score -0.25</summary>

```text
Contract: SUGAR NO. 11 - ICE FUTURES U.S. (positions as of 2026-11-03, published the following Friday)
Large speculators: net long 18.8% of open interest (1,191,088 contracts)
Change on the week: -0.9% of open interest
Crowding: 90% percentile over 52 weeks -- a crowded long by the standards of the past year
Read this as crowding, not as a forecast: an extreme is as often the end of a move as the middle of one.
```

</details>

<details><summary><b>Money going into and out of this fund</b> — score -0.25</summary>

```text
Direction: money coming in (1 month)
Share count change: 1 week: +12.3% (6.46M) over 7d | 1 month: +21.8% (10.60M) over 30d
Shares outstanding: 5.38M | fund size: 59.14M
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Corn (CORN) · Commodity — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:** no explanation. It wrote only “NEUTRAL”, so the main reasons below are all it gave.

**Main reasons it gave:**
- Positioning net long 0.5% of OI, down -3.9% week-over-week
- Fund flows show -18.7% share count change in 1 week
- Technical RSI 34.3 (oversold) and price below 20‑day SMA
- No macro surprise: yields up modestly, inflation 3.7% in line with expectations

<details><summary><b>News</b> — score +0.00</summary>

- [CME : Live Cattle Futures Ease as Screwworm Facility Progresses](http://www.bing.com/news/apiclick.aspx?ref=FexRss&aid=&tid=6af5d386a99943c1b7d9a8b26ffe3180&url=https%3a%2f%2fwww.marketscreener.com%2fnews%2fcme-live-cattle-futures-ease-as-screwworm-facility-progresses-ce785edbd180f126&c=17310334209561803126&mkt=en-us)  
  <sub>MarketScreener, 24h ago</sub>  
  Live Cattle futures declined across the board as advancing progress on the new screwworm facility bolstered market confidence ahead of its scheduled April 2027 opening. A sharp jump in corn prices ...
- [CBOT corn may rise into $4.52 to $4.53-3/4 range](http://www.bing.com/news/apiclick.aspx?ref=FexRss&aid=&tid=6af5d386a99943c1b7d9a8b26ffe3180&url=https%3a%2f%2fwww.tradingview.com%2fnews%2freuters.com%2c2026%3anewsml_L2N46T08E%3a0-cbot-corn-may-rise-into-4-52-to-4-53-3-4-range%2f&c=9844370488883328211&mkt=en-us)  
  <sub>TradingView, 17h ago</sub>  
  CBOT December corn (CZ26) may rise into a range of $4.52 to $4.53-3/4 per bushel, driven by a wave c.The bounce from $4.38 may consist of three waves. So far, only two have unfolded. The third wave, ...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.11% (+0.12 on the week) | 5-year 4.87% (+0.27 on the week) | 10-year 5.03% (+0.19 on the week) | 30-year 5.37% (+0.12 on the week)
Yield curve, 10-year minus 3-month: +0.92 points -- upward sloping (normal)
US dollar index: 102.91 (+1.36 on the week)
Volatility (VIX): 18.99 (-9.2 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.1% (2026-10-01) | jobless claims 200k (2026-11-07)
Policy and expectations: Fed target 4.00% | market expects 2.2% inflation over 10 years
Rate path: 2-year Treasury 4.56% vs Fed target 3.75-4.00% -- the bond market prices about 3 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 17.30 (bar of 2026-11-12), from 502 daily bars
Trend: vs 20d SMA 17.51 (-1.2%), 50d 18.67 (-7.3%), 200d 18.18 (-4.8%); 50d above 200d
Momentum: RSI(14) 34.3 | MACD -0.374 vs signal -0.424 (histogram 0.050)
Returns: 1d -0.4% | 5d +0.9% | 1m -6.1% | 3m -5.3%
52-week range: 16.47 - 20.29 (now 21.7% of the way up)
Volatility: ATR(14) 0.23 (1.3% of price) | annualised 20d 11.7%
Volume: 0.28x the 20-day average
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
Cost of holding this fund instead of corn itself: -7.2% a year -- heavy: rolling contracts costs this fund real money
Measured: 3 months: fund -5.3%, commodity -2.8%, gap -2.4% | 6 months: fund -6.6%, commodity -1.2%, gap -5.4% | 12 months: fund -3.9%, commodity +3.2%, gap -7.2%
A commodity fund holds futures, not corn, and must sell each expiring contract to buy the next one. Where the next month costs more, that roll loses money every month. This gap is what the structure has actually cost, fees included -- it is history rather than a forecast, and it is not a direction: heavy carry is a reason to want a larger move to justify a long, and a tailwind for a short.
```

</details>

<details><summary><b>How much oil and gas is in storage</b> — score -0.20</summary>

_Not available today._

</details>

<details><summary><b>How the crop is growing</b> — score -0.20</summary>

```text
Corn rated good or excellent: 56% of the US crop (week 43 of 2026)
Direction over 3 weeks: steady, 0 points
A better crop means more supply, which reads bearish for the price, and a worse one bullish. The trend matters more than the level, and the market has already seen this: it is published on a schedule everyone trades.
```

</details>

<details><summary><b>What analysts and big funds say</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>Buying and selling by company insiders</b> — score -0.55</summary>

_Not available today._

</details>

<details><summary><b>Who is positioned how</b> — score -0.55</summary>

```text
Contract: CORN - CHICAGO BOARD OF TRADE (positions as of 2026-11-03, published the following Friday)
Large speculators: net long 0.5% of open interest (1,918,622 contracts)
Change on the week: -3.9% of open interest
Crowding: 45% percentile over 52 weeks -- within its normal range
Read this as crowding, not as a forecast: an extreme is as often the end of a move as the middle of one.
```

</details>

<details><summary><b>Money going into and out of this fund</b> — score -0.55</summary>

```text
Direction: money going out (1 month)
Share count change: 1 week: -18.7% (-24.44M) over 7d | 1 month: -12.8% (-15.68M) over 30d
Shares outstanding: 6.15M | fund size: 106.46M
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Copper (CPER) · Commodity — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> No policy or rate surprise this week; copper price below 20‑day SMA and RSI 37 indicating bearish momentum with low volume; positioning shows crowded short (2% percentile) and net long fell 1.4% of OI; fund flows show net outflows (-4.6% week); cost of holding fund vs copper is -3.7% annual drag.

**Main reasons it gave:**
- No policy or rate surprise this week
- Copper price below 20‑day SMA and RSI 37 indicating bearish momentum with low volume
- Positioning shows crowded short (2% percentile) and net long fell 1.4% of OI
- Fund flows show net outflows (-4.6% week)
- Cost of holding fund vs copper is -3.7% annual drag

<details><summary><b>News</b> — score +0.00</summary>

- [Commodities: Stronger Dollar Weighs On Commodities](http://www.bing.com/news/apiclick.aspx?ref=FexRss&aid=&tid=6af5d34e396849f890fa21bbce751b67&url=https%3a%2f%2fseekingalpha.com%2farticle%2f4966893-commodities-stronger-dollar-weighs-on-commodities&c=8742246983035574367&mkt=en-us)  
  <sub>Seeking Alpha, 12h ago</sub>  
  Oil prices edged lower this morning, with Brent around $91/bbl. Copper traded near a 4-month low this morning as renewed selling in tech stocks and a firmer USD weighed on the metals complex ...
- [Chile weighs private investment in copper giant Codelco amid money woes](http://www.bing.com/news/apiclick.aspx?ref=FexRss&aid=&tid=6af5d34e396849f890fa21bbce751b67&url=https%3a%2f%2fseekingalpha.com%2fnews%2f4670932-chile-weighs-private-investment-in-copper-giant-codelco-amid-money-woes&c=10906355625579784330&mkt=en-us)  
  <sub>Seeking Alpha, 28h ago</sub>  
  Chile could eventually allow minority private investment in Codelco while keeping state control; its overhaul targets costs, debt and management.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.11% (+0.12 on the week) | 5-year 4.87% (+0.27 on the week) | 10-year 5.03% (+0.19 on the week) | 30-year 5.37% (+0.12 on the week)
Yield curve, 10-year minus 3-month: +0.92 points -- upward sloping (normal)
US dollar index: 102.91 (+1.36 on the week)
Volatility (VIX): 18.99 (-9.2 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.1% (2026-10-01) | jobless claims 200k (2026-11-07)
Policy and expectations: Fed target 4.00% | market expects 2.2% inflation over 10 years
Rate path: 2-year Treasury 4.56% vs Fed target 3.75-4.00% -- the bond market prices about 3 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score -0.30</summary>

```text
Last close 37.21 (bar of 2026-11-12), from 502 daily bars
Trend: vs 20d SMA 38.85 (-4.2%), 50d 39.48 (-5.8%), 200d 37.98 (-2.0%); 50d above 200d
Momentum: RSI(14) 37.0 | MACD -0.573 vs signal -0.396 (histogram -0.177)
Returns: 1d -1.4% | 5d -0.4% | 1m -6.2% | 3m -7.0%
52-week range: 30.77 - 41.43 (now 60.4% of the way up)
Volatility: ATR(14) 0.67 (1.8% of price) | annualised 20d 24.2%
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
Cost of holding this fund instead of copper itself: -3.7% a year -- a steady drag
Measured: 3 months: fund -7.0%, commodity -6.3%, gap -0.6% | 6 months: fund -7.0%, commodity -5.9%, gap -1.1% | 12 months: fund +18.7%, commodity +22.4%, gap -3.7%
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

<details><summary><b>Buying and selling by company insiders</b> — score -0.40</summary>

_Not available today._

</details>

<details><summary><b>Who is positioned how</b> — score -0.40</summary>

```text
Contract: COPPER- #1 - COMMODITY EXCHANGE INC. (positions as of 2026-11-03, published the following Friday)
Large speculators: net long 10.6% of open interest (327,850 contracts)
Change on the week: -1.4% of open interest
Crowding: 2% percentile over 52 weeks -- a crowded short by the standards of the past year
Read this as crowding, not as a forecast: an extreme is as often the end of a move as the middle of one.
```

</details>

<details><summary><b>Money going into and out of this fund</b> — score -0.40</summary>

```text
Direction: flat (1 month)
Share count change: 1 week: -4.6% (-31.81M) over 7d | 1 month: -0.5% (-3.16M) over 30d
Shares outstanding: 17.66M | fund size: 657.10M
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Gold (GLD) · Commodity — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:** no explanation. It wrote only “NEUTRAL”, so the main reasons below are all it gave.

**Main reasons it gave:**
- Technical indicators show bearish trend: price below 20‑day, 50‑day, and 200‑day SMAs; RSI 37.8; MACD near zero but negative
- Large speculators net long 26% of open interest, down 0.6% week‑over‑week, indicating no strong bullish crowding
- Fund flows flat over the past month, showing no new demand or redemption pressure
- Cost of holding near zero (‑0.9% per year) suggests no structural bias in the fund's roll cost
- Macro data shows no surprise: modest yield rises, dollar up, VIX down but still elevated

<details><summary><b>News</b> — score +0.00</summary>

- [Tether Gold Passes KPMG Audit: Can It Beat America’s Biggest Gold Fund?](http://www.bing.com/news/apiclick.aspx?ref=FexRss&aid=&tid=6af5d33847284b66afc2ea7b02696c6a&url=https%3a%2f%2fcryptorank.io%2fnews%2ffeed%2fe6c9a-tether-gold-kpmg-audit-america-gold-fund&c=6520923439598092030&mkt=en-us)  
  <sub>cryptorank, 9h ago</sub>  
  In Brief KPMG counted every gold bar behind Tether Gold and issued a clean audit. XAU₮ costs less to hold than GLD, but GLD is 39 times larger. Tether's terms ...
- [All that glitters isn’t gold as year-end bets turn cautious](http://www.bing.com/news/apiclick.aspx?ref=FexRss&aid=&tid=6af5d33847284b66afc2ea7b02696c6a&url=https%3a%2f%2fwww.msn.com%2fen-us%2fmoney%2feconomy%2fall-that-glitters-isn-t-gold-as-year-end-bets-turn-cautious%2far-AA2heoks&c=8258392583755205606&mkt=en-us)  
  <sub>Seeking Alpha on MSN, 30h ago</sub>  
  Gold’s remarkable rally has given way to a bruising reversal, leaving traders to weigh whether the metal can regain lost ground before the year ends. On prediction markets, the focus has shifted from ...
- [Gold price: Two major banks, two scenarios - who will be right?](http://www.bing.com/news/apiclick.aspx?ref=FexRss&aid=&tid=6af5d33847284b66afc2ea7b02696c6a&url=https%3a%2f%2fgoldinvest.de%2fen%2fgold-price-two-major-banks-two-scenarios-who-will-be-right&c=2686807428612637262&mkt=en-us)  
  <sub>GOLDINVEST.de, 23h ago</sub>  
  A sharp debate has erupted between two leading investment firms over the future direction of the gold price. While Goldman Sachs significantly cuts its ...
- [Gold Rate Today in Nagpur](http://www.bing.com/news/apiclick.aspx?ref=FexRss&aid=&tid=6af5d33847284b66afc2ea7b02696c6a&url=https%3a%2f%2fwww.financialexpress.com%2fgold-rate-in-nagpur%2f&c=2231066737140324799&mkt=en-us)  
  <sub>The Financial Express, 26h ago</sub>  
  Check for gold price in Nagpur today and the last 10 days of gold rate in Nagpur for 18, 22 and 24 carat based on 1gm, 8gm, 10gm, and 100 gm on financialexpress.com.
- [SPDR Gold Shares ETF - USD Stock](http://www.bing.com/news/apiclick.aspx?ref=FexRss&aid=&tid=6af5d33847284b66afc2ea7b02696c6a&url=https%3a%2f%2fwww.marketscreener.com%2fquote%2fetf%2fSPDR-GOLD-SHARES-ETF-USD-29425888%2f&c=12463440268478694818&mkt=en-us)  
  <sub>MarketScreener, 8h ago</sub>  
  Aug. 04 SPDR Gold Shares Reports Earnings Results for the Third Quarter and Nine Months Ended June 30, 2026 CI May. 05 SPDR Gold Shares Reports Earnings Results for the Second Quarter and Six Months ...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.11% (+0.12 on the week) | 5-year 4.87% (+0.27 on the week) | 10-year 5.03% (+0.19 on the week) | 30-year 5.37% (+0.12 on the week)
Yield curve, 10-year minus 3-month: +0.92 points -- upward sloping (normal)
US dollar index: 102.91 (+1.36 on the week)
Volatility (VIX): 18.99 (-9.2 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.1% (2026-10-01) | jobless claims 200k (2026-11-07)
Policy and expectations: Fed target 4.00% | market expects 2.2% inflation over 10 years
Rate path: 2-year Treasury 4.56% vs Fed target 3.75-4.00% -- the bond market prices about 3 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score -0.20</summary>

```text
Last close 355.61 (bar of 2026-11-12), from 502 daily bars
Trend: vs 20d SMA 370.15 (-3.9%), 50d 382.02 (-6.9%), 200d 409.12 (-13.1%); 50d below 200d
Momentum: RSI(14) 37.8 | MACD -4.536 vs signal -4.545 (histogram 0.009)
Returns: 1d -2.6% | 5d -5.3% | 1m -5.4% | 3m -11.4%
52-week range: 355.61 - 495.90 (now 0.0% of the way up)
Volatility: ATR(14) 7.07 (2.0% of price) | annualised 20d 27.7%
Volume: 0.21x the 20-day average
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
Cost of holding this fund instead of gold itself: -0.9% a year -- close to nothing, as a physically backed fund should be
Measured: 3 months: fund -11.4%, commodity -12.3%, gap +0.9% | 6 months: fund -16.8%, commodity -16.9%, gap +0.2% | 12 months: fund -6.4%, commodity -5.4%, gap -0.9%
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

<details><summary><b>Buying and selling by company insiders</b> — score +0.00</summary>

_Not available today._

</details>

<details><summary><b>Who is positioned how</b> — score +0.00</summary>

```text
Contract: GOLD - COMMODITY EXCHANGE INC. (positions as of 2026-11-03, published the following Friday)
Large speculators: net long 26.0% of open interest (399,169 contracts)
Change on the week: -0.6% of open interest
Crowding: 43% percentile over 52 weeks -- within its normal range
Read this as crowding, not as a forecast: an extreme is as often the end of a move as the middle of one.
```

</details>

<details><summary><b>Money going into and out of this fund</b> — score +0.00</summary>

```text
Direction: flat (1 month)
Share count change: 1 week: +0.0% (0.00) over 7d | 1 month: +0.0% (0.00) over 30d
Shares outstanding: 260.30M | fund size: 92.57B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Soybeans (SOYB) · Commodity — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> No macro surprise, no decisive technical break, and mixed behavioural signals lead to a neutral stance.

**Main reasons it gave:**
- Positioning net long decreased by 4.9% week‑over‑week
- Cost of holding low at 0.5% annual
- Price below 20‑day SMA but above 200‑day SMA, RSI 40.6
- Macro data (inflation 3.7%, unemployment 4.1%, jobless claims 200k) in line with expectations
- US soybean crop condition 57% good/excellent, no trend

<details><summary><b>News</b> — score +0.00</summary>

_No news found for this one today._

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.11% (+0.12 on the week) | 5-year 4.87% (+0.27 on the week) | 10-year 5.03% (+0.19 on the week) | 30-year 5.37% (+0.12 on the week)
Yield curve, 10-year minus 3-month: +0.92 points -- upward sloping (normal)
US dollar index: 102.91 (+1.36 on the week)
Volatility (VIX): 18.99 (-9.2 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.1% (2026-10-01) | jobless claims 200k (2026-11-07)
Policy and expectations: Fed target 4.00% | market expects 2.2% inflation over 10 years
Rate path: 2-year Treasury 4.56% vs Fed target 3.75-4.00% -- the bond market prices about 3 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 25.83 (bar of 2026-11-12), from 502 daily bars
Trend: vs 20d SMA 26.11 (-1.1%), 50d 27.02 (-4.4%), 200d 25.26 (+2.2%); 50d above 200d
Momentum: RSI(14) 40.6 | MACD -0.381 vs signal -0.394 (histogram 0.013)
Returns: 1d -0.5% | 5d +2.1% | 1m -5.0% | 3m +1.8%
52-week range: 21.71 - 28.14 (now 64.1% of the way up)
Volatility: ATR(14) 0.29 (1.1% of price) | annualised 20d 13.6%
Volume: 0.16x the 20-day average
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
Cost of holding this fund instead of soybeans itself: 0.5% a year -- close to nothing, as a physically backed fund should be
Measured: 3 months: fund +1.8%, commodity +4.4%, gap -2.6% | 6 months: fund +3.5%, commodity +4.4%, gap -0.9% | 12 months: fund +10.6%, commodity +10.1%, gap +0.5%
A commodity fund holds futures, not soybeans, and must sell each expiring contract to buy the next one. Where the next month costs more, that roll loses money every month. This gap is what the structure has actually cost, fees included -- it is history rather than a forecast, and it is not a direction: heavy carry is a reason to want a larger move to justify a long, and a tailwind for a short.
```

</details>

<details><summary><b>How much oil and gas is in storage</b> — score +0.00</summary>

_Not available today._

</details>

<details><summary><b>How the crop is growing</b> — score +0.00</summary>

```text
Soybeans rated good or excellent: 57% of the US crop (week 41 of 2026)
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

<details><summary><b>Buying and selling by company insiders</b> — score -0.10</summary>

_Not available today._

</details>

<details><summary><b>Who is positioned how</b> — score -0.10</summary>

```text
Contract: SOYBEANS - CHICAGO BOARD OF TRADE (positions as of 2026-11-03, published the following Friday)
Large speculators: net long 14.9% of open interest (959,576 contracts)
Change on the week: -4.9% of open interest
Crowding: 43% percentile over 52 weeks -- within its normal range
Read this as crowding, not as a forecast: an extreme is as often the end of a move as the middle of one.
```

</details>

<details><summary><b>Money going into and out of this fund</b> — score -0.10</summary>

```text
Direction: money going out (1 month)
Share count change: 1 week: -14.3% (-6.53M) over 7d | 1 month: -8.3% (-3.51M) over 30d
Shares outstanding: 1.51M | fund size: 39.05M
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

**Data that was missing** (counted as 0.00, never guessed):
- news unavailable: Bright Data returned an empty body with its 200; nothing to parse (Bright Data said: x-brd-status-code 502; x-brd-error response body was rejected) (Bing's feed, direct: 2 headline(s), none naming SOYB)

### Natural gas (UNG) · Commodity — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> No material macro surprise, technicals mixed with low volume, and no decisive break. Positioning shows a crowded short that is easing, inventories are high (bearish), cost of holding is a small drag, and the EIA outlook points to a price decline over six months. These factors offset each other, leading to a neutral stance.

**Main reasons it gave:**
- Large speculators net short 13.4% of open interest, short position decreased 1.2% week over week (crowded short)
- US natural gas inventories built 77 BCF to 3,801 BCF, 92nd percentile (high level) – bearish supply signal
- Cost of holding fund vs commodity is -1.4% per year, a small drag on long positions
- Technicals mixed: price above 20‑day SMA but below 200‑day SMA, low volume, no decisive break
- EIA price outlook projects a decline in natural gas price over six months, tempering bullish case

<details><summary><b>News</b> — score +0.00</summary>

- [United States Natural Gas Fund, LP (UNG) Stock Price, News, Quote & History](https://ca.finance.yahoo.com/quote/UNG/)  
  <sub>Yahoo! Finance Canada, 3 hours ago</sub>  
  Find the latest United States Natural Gas Fund, LP (UNG) stock quote, history, news and other vital information to help you with your stock trading and...
- [Oil And Gas Prices Lift Energy ETFs Before The Open](https://finimize.com/content/oil-and-gas-prices-lift-energy-etfs-before-the-open)  
  <sub>Finimize, 23 hours ago</sub>  
  WTI rose to $87.25 a barrel and Brent to $92.82, while Petrobras slid over 3% after a weaker-than-expected Q3 net income report.
- [UNG Jan 2029 7.000 put (UNG290119P00007000) Interactive Stock Chart - Yahoo Finance](https://www.google.com/goto?url=CAESeQHEIkXX7UAYcaEOHOTaVBnaTttzc2xxLzvm1scCieh_SC59lee9SBwJvTA94EZNJSu6G57P38OBP962Z0UYn224qbLcimDpgZSycSI85qDFow_XPpHqAh8b0pHGjzglC2kcFh6fKzi9C37Lbi0gmfjSLItgS8CeBvQ&gsessionid=NFwf4n3w6yzcdl7o29tuQEWbLMU9Xm0b3SBrnXtGHx35sUim6_bthg)  
  <sub>Yahoo! Finance Canada, 15 hours ago</sub>  
  Interactive Chart for UNG Jan 2029 7.000 put (UNG290119P00007000), analyze all the data with a huge range of indicators.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.11% (+0.12 on the week) | 5-year 4.87% (+0.27 on the week) | 10-year 5.03% (+0.19 on the week) | 30-year 5.37% (+0.12 on the week)
Yield curve, 10-year minus 3-month: +0.92 points -- upward sloping (normal)
US dollar index: 102.91 (+1.36 on the week)
Volatility (VIX): 18.99 (-9.2 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.1% (2026-10-01) | jobless claims 200k (2026-11-07)
Policy and expectations: Fed target 4.00% | market expects 2.2% inflation over 10 years
Rate path: 2-year Treasury 4.56% vs Fed target 3.75-4.00% -- the bond market prices about 3 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 10.35 (bar of 2026-11-12), from 502 daily bars
Trend: vs 20d SMA 9.76 (+6.1%), 50d 10.29 (+0.6%), 200d 11.04 (-6.2%); 50d below 200d
Momentum: RSI(14) 56.9 | MACD -0.098 vs signal -0.236 (histogram 0.138)
Returns: 1d +1.3% | 5d +11.7% | 1m -7.7% | 3m +4.4%
52-week range: 9.00 - 16.90 (now 17.2% of the way up)
Volatility: ATR(14) 0.38 (3.7% of price) | annualised 20d 44.9%
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
Cost of holding this fund instead of natural gas itself: -1.4% a year -- a steady drag
Measured: 3 months: fund +4.4%, commodity +21.1%, gap -16.7% | 6 months: fund -7.2%, commodity +14.3%, gap -21.6% | 12 months: fund -28.9%, commodity -27.5%, gap -1.4%
A commodity fund holds futures, not natural gas, and must sell each expiring contract to buy the next one. Where the next month costs more, that roll loses money every month. This gap is what the structure has actually cost, fees included -- it is history rather than a forecast, and it is not a direction: heavy carry is a reason to want a larger move to justify a long, and a tailwind for a short.
```

</details>

<details><summary><b>How much oil and gas is in storage</b> — score -0.50</summary>

```text
US inventories, week ending 2026-10-30 (published the following Wednesday)
  Natural gas: 3,801.0 billion cubic feet, +77.0 on the week (a build), 92% percentile over 52 weeks -- high for the time of year
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

<details><summary><b>Buying and selling by company insiders</b> — score +0.10</summary>

_Not available today._

</details>

<details><summary><b>Who is positioned how</b> — score +0.10</summary>

```text
Contract: NAT GAS NYME - NEW YORK MERCANTILE EXCHANGE (positions as of 2026-11-03, published the following Friday)
Large speculators: net short 13.4% of open interest (1,678,554 contracts)
Change on the week: -1.2% of open interest
Crowding: 2% percentile over 52 weeks -- a crowded short by the standards of the past year
Read this as crowding, not as a forecast: an extreme is as often the end of a move as the middle of one.
```

</details>

<details><summary><b>Money going into and out of this fund</b> — score +0.10</summary>

```text
Direction: money coming in (1 month)
Share count change: 1 week: -3.6% (-18.51M) over 9d | 1 month: +17.3% (74.27M) over 30d
Shares outstanding: 48.54M | fund size: 502.63M
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Oil (USO) · Commodity — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:** no explanation. It wrote only “NEUTRAL”, so the main reasons below are all it gave.

**Main reasons it gave:**
- Positioning: net long down 0.5% of OI, low crowding (25th percentile)
- Energy inventories: draws in crude (-0.9) and diesel (-3.6) indicating bullish supply
- EIA price outlook forecasts WTI at $97, well below current $142, bearish
- Fund flows: share count up 21% in month, indicating strong demand

<details><summary><b>News</b> — score +0.00</summary>

_No news found for this one today._

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.11% (+0.12 on the week) | 5-year 4.87% (+0.27 on the week) | 10-year 5.03% (+0.19 on the week) | 30-year 5.37% (+0.12 on the week)
Yield curve, 10-year minus 3-month: +0.92 points -- upward sloping (normal)
US dollar index: 102.91 (+1.36 on the week)
Volatility (VIX): 18.99 (-9.2 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.1% (2026-10-01) | jobless claims 200k (2026-11-07)
Policy and expectations: Fed target 4.00% | market expects 2.2% inflation over 10 years
Rate path: 2-year Treasury 4.56% vs Fed target 3.75-4.00% -- the bond market prices about 3 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 142.06 (bar of 2026-11-12), from 502 daily bars
Trend: vs 20d SMA 156.67 (-9.3%), 50d 152.66 (-6.9%), 200d 127.30 (+11.6%); 50d above 200d
Momentum: RSI(14) 37.5 | MACD -2.776 vs signal 0.072 (histogram -2.848)
Returns: 1d +0.4% | 5d -4.1% | 1m -7.5% | 3m +12.2%
52-week range: 66.17 - 169.53 (now 73.4% of the way up)
Volatility: ATR(14) 5.24 (3.7% of price) | annualised 20d 47.6%
Volume: 0.14x the 20-day average
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
US inventories, week ending 2026-10-30 (published the following Wednesday)
  Crude oil: 409.8 million barrels, -0.9 on the week (a draw), 10% percentile over 52 weeks -- low for the time of year
  Petrol: 209.0 million barrels, -0.2 on the week (a draw), 25% percentile over 52 weeks
  Diesel: 99.3 million barrels, -3.6 on the week (a draw), 2% percentile over 52 weeks -- low for the time of year
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
Share count change: 1 week: +39.2% (552.08M) over 9d | 1 month: +21.4% (346.21M) over 30d
Shares outstanding: 13.81M | fund size: 1.96B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

**Data that was missing** (counted as 0.00, never guessed):
- news unavailable: Bright Data returned an empty body with its 200; nothing to parse (Bright Data said: x-brd-status-code 502; x-brd-error response body was rejected) (Bing's feed, direct: 10 headline(s), none naming USO)

### Wheat (WEAT) · Commodity — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:** no explanation. It wrote only “NEUTRAL”, so the main reasons below are all it gave.

**Main reasons it gave:**
- No macro surprise: yields rose modestly, inflation 3.7% in line with expectations
- Technical indicators weak (RSI 32.7, price below 20‑day/50‑day/200‑day SMAs) but no high‑volume breakout
- Fund outflows: share count down 16.8% in one week indicating bearish demand
- Positioning: net short 16.3% of OI, decreasing by 2.1% (bullish change)
- Heavy cost of holding (-8.7% annual) creates tailwind for short positions

<details><summary><b>News</b> — score +0.00</summary>

- [Teucrium 2x Daily Wheat ETF](http://www.bing.com/news/apiclick.aspx?ref=FexRss&aid=&tid=6af5d3975eef42d0b9e12bc6c42c8955&url=https%3a%2f%2fmarkets.businessinsider.com%2fetfs%2fteucrium-2x-daily-wheat-etf-us53656g2820&c=2324053413144968507&mkt=en-us)  
  <sub>Business Insider, 21h ago</sub>  
  Copyright © 2026 Insider Inc and finanzen.net GmbH (Imprint). All rights reserved. Registration on or use of this site constitutes acceptance of our Terms of Service ...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.11% (+0.12 on the week) | 5-year 4.87% (+0.27 on the week) | 10-year 5.03% (+0.19 on the week) | 30-year 5.37% (+0.12 on the week)
Yield curve, 10-year minus 3-month: +0.92 points -- upward sloping (normal)
US dollar index: 102.91 (+1.36 on the week)
Volatility (VIX): 18.99 (-9.2 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.1% (2026-10-01) | jobless claims 200k (2026-11-07)
Policy and expectations: Fed target 4.00% | market expects 2.2% inflation over 10 years
Rate path: 2-year Treasury 4.56% vs Fed target 3.75-4.00% -- the bond market prices about 3 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score -0.20</summary>

```text
Last close 21.98 (bar of 2026-11-12), from 502 daily bars
Trend: vs 20d SMA 22.45 (-2.1%), 50d 24.30 (-9.6%), 200d 23.60 (-6.9%); 50d above 200d
Momentum: RSI(14) 32.7 | MACD -0.695 vs signal -0.763 (histogram 0.067)
Returns: 1d -0.9% | 5d +0.2% | 1m -9.9% | 3m -12.0%
52-week range: 19.88 - 28.00 (now 25.8% of the way up)
Volatility: ATR(14) 0.36 (1.6% of price) | annualised 20d 14.5%
Volume: 0.13x the 20-day average
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
Cost of holding this fund instead of wheat itself: -8.7% a year -- heavy: rolling contracts costs this fund real money
Measured: 3 months: fund -12.0%, commodity -11.7%, gap -0.3% | 6 months: fund -11.5%, commodity -7.9%, gap -3.5% | 12 months: fund +2.4%, commodity +11.1%, gap -8.7%
A commodity fund holds futures, not wheat, and must sell each expiring contract to buy the next one. Where the next month costs more, that roll loses money every month. This gap is what the structure has actually cost, fees included -- it is history rather than a forecast, and it is not a direction: heavy carry is a reason to want a larger move to justify a long, and a tailwind for a short.
```

</details>

<details><summary><b>How much oil and gas is in storage</b> — score -0.30</summary>

_Not available today._

</details>

<details><summary><b>How the crop is growing</b> — score -0.30</summary>

```text
Wheat rated good or excellent: 45% of the US crop (week 46 of 2026)
Direction over 1 weeks: not enough readings to say
Same week last year: 49% (-4 points)
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
Contract: WHEAT-SRW - CHICAGO BOARD OF TRADE (positions as of 2026-11-03, published the following Friday)
Large speculators: net short 16.3% of open interest (534,858 contracts)
Change on the week: -2.1% of open interest
Crowding: 28% percentile over 52 weeks -- within its normal range
Read this as crowding, not as a forecast: an extreme is as often the end of a move as the middle of one.
```

</details>

<details><summary><b>Money going into and out of this fund</b> — score +0.20</summary>

```text
Direction: money going out (1 month)
Share count change: 1 week: -16.8% (-47.78M) over 7d | 1 month: -7.5% (-19.22M) over 30d
Shares outstanding: 10.76M | fund size: 236.55M
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

