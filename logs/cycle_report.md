# Daily report

**23 Oct 2026, 18:59 Israel time (15:59 UTC)** · 80 names checked · 0 traded · 0 with a problem

**Answers with no explanation:** 13 of 67 (the model wrote only a label, like “NEUTRAL”, where its reason should be). Their main reasons are still shown.

**Run:** started by the outside scheduler (via supabase-cron), on time (planned for 14:40 UTC).

| Group | Looked at | Took a side | No clear view | Problems |
| --- | --- | --- | --- | --- |
| Companies | 16 | 5 | 11 | 0 |
| Whole-market funds | 14 | 0 | 14 | 0 |
| Sector and country funds | 41 | 0 | 41 | 0 |
| Commodities | 9 | 0 | 9 | 0 |

## Open positions

Checked before any new trade. R is what the trade risked at entry; the ladder sells a third at +1R and another at +3R, the stop-loss follows the price up every day, and it only ever moves up.

| Position | What happened |
| --- | --- |
| ASML (ASML) · Company | **Stop raised.** At +0.61R, following the price. Stop-loss raised 1714.37 → 1684.98. |
| Gold (GLD) · Commodity | **Stop raised.** At +1.46R, following the price. Stop-loss raised 383.47 → 378.03. |
| Nvidia (NVDA) · Company | **Stop raised.** At +0.28R, following the price. Stop-loss raised 226.55 → 225.68. |
| Exxon Mobil (XOM) · Company | **Stop raised.** At +2.67R, following the price. Stop-loss raised 170.88 → 174.17. |
| Israel (EIS) · Sector or country | **Holding.** -0.91R, holding 57 shares. Stop-loss 118.59. |
| United Kingdom (EWU) · Sector or country | **Holding.** +1.18R, holding 104 shares. Stop-loss 47.23. |
| HDFC Bank (HDB) · Company | **Holding.** -0.69R, holding 60 shares. Stop-loss 21.65. |
| US company bonds, riskier (HYG) · Index fund | **Holding.** -0.32R, holding 158 shares. Stop-loss 76.66. |
| JPMorgan Chase (JPM) · Company | **Holding.** -0.25R, holding 15 shares. Stop-loss 321.20. |
| Eli Lilly (LLY) · Company | **Holding.** +2.10R, holding 3 shares. Stop-loss 1233.74. |
| Microsoft (MSFT) · Company | **Holding.** -0.38R, holding 9 shares. Stop-loss 509.74. |
| Royal Bank of Canada (RY) · Company | **Holding.** +0.62R, holding 17 shares. Stop-loss 194.88. |
| US materials and chemicals (XLB) · Sector or country | **Holding.** +0.05R, holding 138 shares. Stop-loss 49.68. |

## How to read this

Once a day the system looks at every name on the list. For each one it reads five kinds of evidence and gives each kind a score from -1.00 (bad) to +1.00 (good). Then it picks a side and says how sure it is, from 0.00 to 1.00.

The three sides: **BULLISH** = the model thinks the price will go up; **BEARISH** = the model thinks the price will go down; **NEUTRAL** = the model has no clear view.

Being sure is not enough on its own. A trade only happens when confidence reaches **0.30**. Below that the system writes down what it thought and does nothing. The size of a trade, the stop-loss and every limit are decided by plain code, not by the model.

Open positions are checked first, before any new trade. When a trade has earned back what it risked (+1R), a third of it is sold and the stop-loss moves up to the entry price, so it can no longer lose. At three times that (+3R) another third is sold and the stop moves up again. The last third stays open. Every day the stop-loss also follows the price up, so a position only ever closes when its stop is hit. The stop only ever moves up.

Under each name you will find the five scores. Click a grey line to open it and see the exact evidence behind that score. The words inside quotation marks are the model's own; nothing there has been rewritten.

## Companies

### Procter & Gamble (PG) · Company — BULLISH, confidence 0.62

**Result:** REJECTED · no room under the sleeve budget limit

**In the model's own words:** no explanation. It wrote only “BUY”, so the main reasons below are all it gave.

**Main reasons it gave:**
- Q1 earnings beat consensus by 3% (earnings record)
- PG stock rose 5.6% to $165.59 after earnings beat (news)
- TD Cowen raised price target to $166 (analyst view)
- Price above 20‑day, 50‑day, and 200‑day SMAs; RSI 64.1 (technical)
- Insiders net bought 107,542 shares (+5.2% holdings) (insider activity)

<details><summary><b>News</b> — score +0.60</summary>

- [Procter & Gamble (PG) Stock Climbs As Q1 Earnings Highlight Margin Pressure](https://finance.yahoo.com/markets/stocks/articles/procter-gamble-pg-stock-climbs-231718524.html)  
  <sub>Yahoo Finance, 16 hours ago</sub>  
  Procter & Gamble stock ripped higher today, jumping 5.6% to US$165.59 after its Q1 2027 update hit the tape. The market reacted quickly, but the real story...
- [P&G (PG) Stock Jumps As Q1 Earnings Fuel Cash Flow Cheer](https://simplywall.st/stocks/us/household/nyse-pg/procter-gamble/news/pg-pg-stock-jumps-as-q1-earnings-fuel-cash-flow-cheer)  
  <sub>Simply Wall Street, 5 hours ago</sub>  
  Procter & Gamble came into this print with a premium consumer staples reputation and a trailing P/E of 24.4x, and the stock had largely moved sideways in...
- [TD Cowen raises Procter & Gamble stock price target on turnaround progress](https://www.investing.com/news/analyst-ratings/td-cowen-raises-procter--gamble-stock-price-target-on-turnaround-progress-93CH-4969905)  
  <sub>Investing.com, 9 minutes ago</sub>  
  Investing.com - TD Cowen raised its price target on Procter & Gamble stock (NYSE:PG) to $166 from $150 while maintaining a Hold rating.
- [PG Stock Technicals: What to Know](https://journalarta.com/en/2026/10/23/pg-stock-technicals-gains-5-58-on-thursday-rsi-overbought/)  
  <sub>JournalArta, 5 hours ago</sub>  
  On October 22, 2026: price 165.59 USD, trend uptrend, RSI 74.5, support 143.95, resistance 165.59. technical analysis of pg stock. PG Stock Technicals...
- [Procter & Gamble Company (The) $PG Stock Sold by Howland Capital Management LLC](https://www.marketbeat.com/instant-alerts/filing-procter-gamble-company-the-pg-stock-sold-by-howland-capital-management-llc-2026-10-23/)  
  <sub>MarketBeat, 6 hours ago</sub>  
  Howland Capital Management LLC trimmed its position in shares of Procter & Gamble Company (The) (NYSE:PG - Free Report) by 9.6% in the third quarter,...
- [Dow Jones Top Movers Today: PG and JNJ Lead Gainers, CAT and AMZN Lead Losers](https://www.chartmill.com/news/BA/Chartmill-56660-Dow-Jones-Top-Movers-Today-PG-and-JNJ-Lead-Gainers-CAT-and-AMZN-Lead-Losers)  
  <sub>ChartMill, 20 hours ago</sub>  
  During today's session, the largest moves among dow jones components produced a 10-stock gainers list and an 8-stock losers list, led by PG and JNJ on the...
- [Is It Too Late to Buy Procter & Gamble Co (PG) After 5.6% Rally? GF Value Says Undervalued](https://www.gurufocus.com/news/9138013/is-it-too-late-to-buy-procter-gamble-co-pg-after-56-rally-gf-value-says-undervalued)  
  <sub>GuruFocus, 17 hours ago</sub>  
  On October 22, 2026, Procter & Gamble Co (PG) shares rose 5.6% to a current price of $165.59, reflecting a strong momentum in the stock price as it has...
- [U.S. Stock Market Moves | Procter & Gamble (PG.US) rises over 6%; Coca-Cola (KO.US) hits all-time high](https://www.moomoo.com/news/post/1002049522/us-stock-market-moves-procter-gamble-pgus-rises-over-6)  
  <sub>Moomoo, 22 hours ago</sub>  
  Zhitong Finance APP learned that on Thursday, Coca-Cola (KO.US) rose 2%, closing at $94.56 and hitting an all-time high; Procter & Gamble (PG.
- [Procter & Gamble (PG) Reaches a New 52-Week High After Earnings Beat](https://247wallst.com/cards/a-fiscal-q1-earnings-beat-pushed-p-g-to-165-59-a-fresh-52-pg-price-extreme-01m5k06jbczr992vtxb0njqxz4)  
  <sub>24/7 Wall St., 15 hours ago</sub>  
  A fiscal Q1 earnings beat pushed P&G to $165.59, a fresh 52-week high that clears its February 27 peak by 0.5%. The staples giant spent eight months going...
- [PG Oct 2026 155.000 put (PG261023P00155000) Stock Price, News, Quote & History](https://ca.finance.yahoo.com/quote/PG261023P00155000/)  
  <sub>Yahoo! Finance Canada, 10 hours ago</sub>  
  Find the latest PG Oct 2026 155.000 put (PG261023P00155000) stock quote, history, news and other vital information to help you with your stock trading and...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.60</summary>

_Not available today._

</details>

<details><summary><b>Price and chart</b> — score +0.30</summary>

```text
Last close 161.24 (bar of 2026-10-23), from 502 daily bars
Trend: vs 20d SMA 152.77 (+5.5%), 50d 148.37 (+8.7%), 200d 148.51 (+8.6%); 50d below 200d
Momentum: RSI(14) 64.1 | MACD 3.914 vs signal 2.885 (histogram 1.029)
Returns: 1d -2.6% | 5d +1.2% | 1m +10.7% | 3m +8.5%
52-week range: 138.04 - 167.20 (now 79.5% of the way up)
Volatility: ATR(14) 3.15 (2.0% of price) | annualised 20d 29.0%
Volume: 0.27x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.20</summary>

```text
Sector: Consumer Defensive / Household & Personal Products | market cap 373.71B
Valuation: trailing P/E 24.28 | forward P/E 21.76 | P/B 6.89 | PEG 3.79
Profitability: profit margin 18.2% | operating margin 26.4% | ROE 29.6%
Growth (YoY): revenue +4.0% | earnings +1.1%
Balance sheet: debt/equity 70.3% | free cash flow 12.51B
Risk: beta n/a | short interest 1.1% of float
Next earnings: 2027-01-21
```

</details>

<details><summary><b>What this fund holds</b> — score +0.20</summary>

_Not available today._

</details>

<details><summary><b>Does this company beat its own forecasts</b> — score +0.20</summary>

```text
Earnings record, last 4 quarters: 1 beat, 3 in line
  2026-09-30 beat by 3% | 2026-06-30 in line | 2026-06-30 in line | 2026-03-31 in line
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

<details><summary><b>What analysts and big funds say</b> — score +0.20</summary>

```text
Consensus: buy (mean 2.16 on a 1=strong buy to 5=strong sell scale, 23 analysts)
Ratings: 5 strong buy, 8 buy, 12 hold, 0 sell, 0 strong sell
Price target: mean 168.87 (+4.7% vs last close), range 143.00 - 190.00
Recent rating changes:
  - 2026-10-23 Wells Fargo: main, Overweight -> Overweight
  - 2026-10-23 TD Cowen: main, Hold -> Hold
  - 2026-10-23 Morgan Stanley: main, Overweight -> Overweight
  - 2026-10-20 RBC Capital: reit, Outperform -> Outperform
  - 2026-10-14 Citigroup: main, Buy -> Buy
  - 2026-10-06 Evercore ISI Group: up, In-Line -> Outperform
Institutional ownership: 71.7%
Largest holders: Blackrock Inc. (8.2%), Vanguard Capital Management LLC (6.6%), State Street Corporation (4.4%), Geode Capital Management, LLC (2.9%), Vanguard Portfolio Management LLC (2.7%)
```

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score +0.20</summary>

_Not available today._

</details>

<details><summary><b>Buying and selling by company insiders</b> — score +0.10</summary>

```text
Last 180 days: bought 156,293 shares in 42 transaction(s) | sold 48,751 shares in 16
Net: +107,542 shares (+5.2% of insider holdings) | insiders hold 2,176,260 shares
Distinct insiders: 0 buying, 10 selling
Sales — weak evidence on their own; often scheduled 10b5-1 plans, tax on vesting, or diversification:
  - 2026-10-05 GAMA PAUL (Officer): 2,225 shares, 323.38K
  - 2026-10-05 WHALEY SUSAN STREET (Officer): 2,369 shares, 344.31K
  - 2026-10-05 SCHULTEN ANDRE (Chief Financial Officer): 3,914 shares, 568.86K
  - 2026-08-24 JANZARUK MATTHEW W. (Officer): 359 shares, 52.14K
(40 grant/option/gift transaction(s) excluded — compensation, not a view on the price)
```

</details>

<details><summary><b>Who is positioned how</b> — score +0.10</summary>

_Not available today._

</details>

<details><summary><b>Money going into and out of this fund</b> — score +0.10</summary>

_Not available today._

</details>

### Elbit Systems (ESLT) · Company — BULLISH, confidence 0.60

**Result:** REJECTED · no room under the sleeve budget limit

**In the model's own words:**

> A material $235M contract win and a strong earnings beat streak provide a bullish catalyst, while technicals are mixed and valuation is high, leading to moderate conviction.

**Main reasons it gave:**
- $235M contract to supply rocket artillery systems to European customer (Stocktwits, 18h ago)
- Four consecutive earnings beats (10‑21% over consensus) (Earnings record)
- Price above 20‑day and 50‑day SMA (+3.3%/+1.0%) with positive MACD but volume at 0.09× 20‑day average (Technical)
- High valuation: trailing P/E 54.86, forward P/E 39.17 (Fundamentals)
- Morgan Stanley raises price target to $850 (+10% vs last close) (AD HOC NEWS, 1h ago)

<details><summary><b>News</b> — score +0.70</summary>

- [Can Elbit (ESLT) Keep the Earnings Surprise Streak Alive?](https://finance.yahoo.com/markets/stocks/articles/elbit-eslt-keep-earnings-surprise-151004582.html)  
  <sub>Yahoo Finance, 24 hours ago</sub>
- [Elbit Systems stock: Morgan Stanley raises target to USD 850 for Elbit Systems stock](https://www.ad-hoc-news.de/boerse/news/corporate-news/elbit-systems-stock-morgan-stanley-raises-target-to-usd-850-for-elbit-systems-stock/70399394)  
  <sub>AD HOC NEWS, 1 hour ago</sub>
- [Elbit Systems stock trades at EUR 658.25 before November 24 results](https://www.ad-hoc-news.de/boerse/news/corporate-news/elbit-systems-stock-trades-at-eur-658-25-before-november-24-results/70397482)  
  <sub>AD HOC NEWS, 7 hours ago</sub>
- [Elbit Systems Wins $235M Contract To Supply Rocket Artillery Systems To European Customer: What Investors Need To Know](https://stocktwits.com/news-articles/markets/equity/elbit-systems-wins-235-m-contract-to-supply-rocket-artillery-systems-to-european-customer-what-investors-need-to-know/cZx8ZAKRBMS)  
  <sub>Stocktwits, 18 hours ago</sub>  
  Elbit Systems (ESLT) drew investor attention on Monday after the defense technology company announced a $235 million contract to supply EXTRA-MR rockets and...
- [Cathie Wood sells $16 million of surging tech stock](https://www.thestreet.com/investing/stocks/cathie-wood-sells-16-million-of-surging-tech-stock-palantir-pltr)  
  <sub>TheStreet, 23 hours ago</sub>  
  Cathie Wood, head of Ark Investment Management, often takes profits when her favorite tech stocks rally. That's what she's been doing with Palantir...
- [Black Monday Calls, $110 Oil, A Chip Rout: 3 Charts to Watch This Week](https://stocktwits.com/news-articles/markets/equity/black-monday-oil-prices-memory-chips-market-outlook/cZx8ZyaRBMj)  
  <sub>Stocktwits, 19 hours ago</sub>  
  Calls for a “Black Monday” crash spread across social media over the weekend, but U.S. stock futures were pointing higher early Monday, the 39th anniversary...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.70</summary>

_Not available today._

</details>

<details><summary><b>Price and chart</b> — score -0.50</summary>

```text
Last close 729.10 (bar of 2026-10-23), from 502 daily bars
Trend: vs 20d SMA 705.54 (+3.3%), 50d 722.20 (+1.0%), 200d 783.30 (-6.9%); 50d below 200d
Momentum: RSI(14) 52.9 | MACD 5.068 vs signal -2.064 (histogram 7.132)
Returns: 1d -1.9% | 5d -3.5% | 1m -1.4% | 3m -10.3%
52-week range: 454.95 - 1,014.33 (now 49.0% of the way up)
Volatility: ATR(14) 19.29 (2.6% of price) | annualised 20d 41.2%
Volume: 0.09x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.30</summary>

```text
Sector: Industrials / Aerospace & Defense | market cap 34.17B
Valuation: trailing P/E 54.86 | forward P/E 39.17 | P/B 7.73 | PEG n/a
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
Price target: mean 802.17 (+10.0% vs last close), range 518.00 - 960.00
Recent rating changes:
  - 2026-10-05 Jefferies: main, Hold -> Hold
  - 2026-08-19 JP Morgan: main, Neutral -> Neutral
  - 2026-06-24 Jefferies: main, Hold -> Hold
  - 2026-05-27 Jefferies: main, Hold -> Hold
  - 2026-05-27 JP Morgan: main, Neutral -> Neutral
  - 2026-04-13 JP Morgan: main, Neutral -> Neutral
Institutional ownership: 27.6%
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

### Caterpillar (CAT) · Company — BULLISH, confidence 0.55

**Result:** REJECTED · no room under the sleeve budget limit

**In the model's own words:**

> The company shows strong earnings momentum and a positive analyst consensus, while technicals are weak but not a decisive bearish signal. Fundamentals are solid on profitability and growth but offset by high leverage. Insider activity is neutral. Overall, the bullish factors outweigh the bearish, leading to a moderate‑conviction buy.

**Main reasons it gave:**
- Four consecutive earnings beats (31% to 8% beats) indicating strong earnings momentum
- Analyst consensus buy with mean price target $945.76 (+36.9% upside)
- Technical oversold RSI 27.2 and price below 20‑day, 50‑day, 200‑day SMAs; volume 0.36× 20‑day average
- Fundamentals: high ROE 57% and operating margin 22.2% but high debt/equity 232.8%

<details><summary><b>News</b> — score +0.00</summary>

- [What Has The Market Missed In Caterpillar Stock’s Drop?](https://www.trefis.com/stock/cat/articles/620221/what-has-the-market-missed-in-caterpillar-stocks-drop/2026-10-23)  
  <sub>Trefis, 1 hour ago</sub>  
  For questions about this article or underlying research, email help@trefis.com. Caterpillar (CAT) stock fell 20.8% between July 24 and October 22, 2026,...
- [Dividend Roundup: Citigroup, IBM, Caterpillar, Costco, and more (DVY:NASDAQ)](https://seekingalpha.com/news/4656553-dividend-roundup-citigroup-ibm-caterpillar-costco-and-more)  
  <sub>Seeking Alpha, 2 hours ago</sub>  
  Track this week's dividend increases and declarations along with next week's ex-dividend dates. Learn more here.
- [CAT 261023 555.00P (CAT261023P555000) Stock Options Chain | Quotes & News](https://www.moomoo.com/options/CAT261023P555000-US)  
  <sub>Moomoo, 11 hours ago</sub>  
  Track real-time CAT 261023 555.00P (CAT261023P555000) stock options chain data and pricing information and news on moomoo App for your options trading and...
- [Caterpillar, Inc. Estimates – NYSE:CAT](https://www.tradingview.com/symbols/NYSE-CAT/financials-estimates/)  
  <sub>TradingView, 2 hours ago</sub>  
  See how Caterpillar, Inc. performed against analyst expectations and compare actual results with revenue, earnings, cash flow, and valuation estimates.
- [Caterpillar Inc (CAT) Stock Down 4.9% but Still Overvalued -- GF Score: 90/100](https://www.gurufocus.com/news/9138015/caterpillar-inc-cat-stock-down-49-but-still-overvalued-gf-score-90100)  
  <sub>GuruFocus, 17 hours ago</sub>  
  On October 22, 2026, Caterpillar Inc (CAT) shares fell 4.9%, bringing the current price to $704.05. The stock has seen a 52-week range between $510.21 and...
- [CAT Oct 2026 700.000 put (CAT261023P00700000) Interactive Stock Chart - Yahoo Finance](https://ca.finance.yahoo.com/quote/CAT261023P00700000/chart/)  
  <sub>Yahoo! Finance Canada, 8 hours ago</sub>  
  Interactive Chart for CAT Oct 2026 700.000 put (CAT261023P00700000), analyze all the data with a huge range of indicators.
- [‘It’s made me take stock’ - Cat Deeley on turning 50](https://www.womanandhome.com/life/news-entertainment/cat-deeley-50th-birthday/)  
  <sub>Woman & Home, 3 hours ago</sub>  
  As the This Morning presenter marks her milestone birthday she opens up to woman&home about confidence, ageing and her career goals.
- [CAT Nov 2026 950.000 call (CAT261106C00950000) Stock Price, News, Quote & History](https://ca.finance.yahoo.com/quote/CAT261106C00950000/)  
  <sub>Yahoo! Finance Canada, 16 hours ago</sub>  
  Find the latest CAT Nov 2026 950.000 call (CAT261106C00950000) stock quote, history, news and other vital information to help you with your stock trading...
- [CAT 261023 680.00C (CAT261023C680000) Stock Options Chain | Quotes & News](https://www.moomoo.com/options/CAT261023C680000-US)  
  <sub>Moomoo, 22 hours ago</sub>  
  Track real-time CAT 261023 680.00C (CAT261023C680000) stock options chain data and pricing information and news on moomoo App for your options trading and...
- [CAT Nov 2026 875.000 call (CAT261127C00875000) Stock Price, News, Quote & History](https://ca.finance.yahoo.com/quote/CAT261127C00875000/)  
  <sub>Yahoo! Finance Canada, 11 hours ago</sub>  
  Find the latest CAT Nov 2026 875.000 call (CAT261127C00875000) stock quote, history, news and other vital information to help you with your stock trading...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

_Not available today._

</details>

<details><summary><b>Price and chart</b> — score -0.20</summary>

```text
Last close 690.64 (bar of 2026-10-23), from 502 daily bars
Trend: vs 20d SMA 781.23 (-11.6%), 50d 799.81 (-13.6%), 200d 808.64 (-14.6%); 50d below 200d
Momentum: RSI(14) 27.2 | MACD -29.178 vs signal -19.562 (histogram -9.617)
Returns: 1d -1.9% | 5d -5.5% | 1m -14.2% | 3m -20.9%
52-week range: 520.50 - 1,064.90 (now 31.3% of the way up)
Volatility: ATR(14) 27.38 (4.0% of price) | annualised 20d 35.9%
Volume: 0.36x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.10</summary>

```text
Sector: Industrials / Farm & Heavy Construction Machinery | market cap 317.36B
Valuation: trailing P/E 29.72 | forward P/E 21.19 | P/B 16.36 | PEG 1.42
Profitability: profit margin 14.5% | operating margin 22.2% | ROE 57.0%
Growth (YoY): revenue +24.0% | earnings +68.2%
Balance sheet: debt/equity 232.8% | free cash flow 5.05B
Risk: beta 1.58 | short interest 1.9% of float
Next earnings: 2026-10-29
```

</details>

<details><summary><b>What this fund holds</b> — score +0.10</summary>

_Not available today._

</details>

<details><summary><b>Does this company beat its own forecasts</b> — score +0.10</summary>

```text
Earnings record, last 4 quarters: 4 beats
  2026-06-30 beat by 31% | 2026-03-31 beat by 19% | 2025-12-31 beat by 9% | 2025-09-30 beat by 8%
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
Consensus: buy (mean 2.00 on a 1=strong buy to 5=strong sell scale, 26 analysts)
Ratings: 1 strong buy, 15 buy, 12 hold, 1 sell, 0 strong sell
Price target: mean 945.76 (+36.9% vs last close), range 575.00 - 1,155.00
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

<details><summary><b>What analysts say about what this fund holds</b> — score +0.30</summary>

_Not available today._

</details>

<details><summary><b>Buying and selling by company insiders</b> — score +0.00</summary>

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

<details><summary><b>Who is positioned how</b> — score +0.00</summary>

_Not available today._

</details>

<details><summary><b>Money going into and out of this fund</b> — score +0.00</summary>

_Not available today._

</details>

### Novo Nordisk (NVO) · Company — NEUTRAL, confidence 0.55

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:** no explanation. It wrote only “SELL”, so the main reasons below are all it gave.

**Main reasons it gave:**
- Technical: price below 50‑day and 200‑day SMA, volume 0.21× 20‑day average
- Earnings record: 2 of last 4 quarters missed expectations
- Analyst consensus: neutral hold with recent downgrades (Morgan Stanley, Goldman Sachs)
- News: Zacks article notes intensifying competition for Wegovy

<details><summary><b>News</b> — score -0.10</summary>

- [NVO261023C00053000 Interactive Stock Chart | NVO Oct 2026 53.000 call Stock](https://finance.yahoo.com/chart/NVO261023C00053000)  
  <sub>Yahoo Finance, 10 hours ago</sub>  
  At Yahoo Finance, you get free stock quotes, up-to-date news, portfolio management resources, international market data, social interaction and mortgage...
- [NVO vs. VKTX: Which Obesity Stock Could Deliver Bigger Gains?](https://www.zacks.com/stock/news/3013236/nvo-vs-vktx-which-obesity-stock-could-deliver-bigger-gains)  
  <sub>Zacks Investment Research, 22 hours ago</sub>  
  Viking advances VK2735 in phase III injectable and oral studies, with data expected from 2027. NVO's Wegovy growth faces intensifying competition from Eli...
- [NVO Jun 2027 27.500 put (NVO270617P00027500) Interactive Stock Chart - Yahoo Finance](https://ca.finance.yahoo.com/quote/NVO270617P00027500/chart/)  
  <sub>Yahoo! Finance Canada, 11 hours ago</sub>  
  Interactive Chart for NVO Jun 2027 27.500 put (NVO270617P00027500), analyze all the data with a huge range of indicators.
- [NVO Oct 2026 35.500 call (NVO261023C00035500) Stock Price, News, Quote & History](https://ca.finance.yahoo.com/quote/NVO261023C00035500/)  
  <sub>Yahoo! Finance Canada, 22 hours ago</sub>  
  Find the latest NVO Oct 2026 35.500 call (NVO261023C00035500) stock quote, history, news and other vital information to help you with your stock trading and...
- [NVO261030P00031000 interactive stock chart | NVO Oct 2026 31.000 put stock](https://uk.finance.yahoo.com/chart/NVO261030P00031000)  
  <sub>Yahoo Finance UK, 23 hours ago</sub>  
  At Yahoo Finance, you get free stock quotes, up-to-date news, portfolio management resources, international market data, social interaction and mortgage...
- [NVO261023C00035500 interactive stock chart | NVO Oct 2026 35.500 call stock](https://uk.finance.yahoo.com/chart/NVO261023C00035500)  
  <sub>Yahoo Finance UK, 18 hours ago</sub>  
  At Yahoo Finance, you get free stock quotes, up-to-date news, portfolio management resources, international market data, social interaction and mortgage...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score -0.10</summary>

_Not available today._

</details>

<details><summary><b>Price and chart</b> — score -0.50</summary>

```text
Last close 38.95 (bar of 2026-10-23), from 502 daily bars
Trend: vs 20d SMA 38.39 (+1.5%), 50d 41.91 (-7.1%), 200d 44.69 (-12.8%); 50d below 200d
Momentum: RSI(14) 45.0 | MACD -0.682 vs signal -1.065 (histogram 0.383)
Returns: 1d -1.2% | 5d +0.3% | 1m +0.9% | 3m -21.6%
52-week range: 35.29 - 63.98 (now 12.8% of the way up)
Volatility: ATR(14) 0.85 (2.2% of price) | annualised 20d 20.2%
Volume: 0.21x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.00</summary>

```text
Sector: Healthcare / Drug Manufacturers - General | market cap 171.86B
Valuation: trailing P/E 9.17 | forward P/E 11.37 | P/B 5.21 | PEG 4.32
Profitability: profit margin 35.3% | operating margin 42.5% | ROE 59.8%
Growth (YoY): revenue +2.1% | earnings -20.6%
Balance sheet: debt/equity 63.3% | free cash flow 37.67B
Risk: beta 0.38 | short interest 1.0% of float
Next earnings: 2026-11-04
```

</details>

<details><summary><b>What this fund holds</b> — score +0.00</summary>

_Not available today._

</details>

<details><summary><b>Does this company beat its own forecasts</b> — score +0.00</summary>

```text
Earnings record, last 4 quarters: 1 beat, 1 in line, 2 missed
  2026-06-30 missed by 6% | 2026-03-31 beat by 23% | 2025-12-31 in line | 2025-09-30 missed by 7%
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

<details><summary><b>What analysts and big funds say</b> — score -0.10</summary>

```text
Consensus: hold (mean 2.71 on a 1=strong buy to 5=strong sell scale, 12 analysts)
Ratings: 0 strong buy, 3 buy, 10 hold, 1 sell, 0 strong sell
Price target: mean 45.14 (+15.9% vs last close), range 39.79 - 61.85
Recent rating changes:
  - 2026-10-12 BMO Capital: main, Market Perform -> Market Perform
  - 2026-09-11 Morgan Stanley: down, Equal-Weight -> Underweight
  - 2026-03-02 Goldman Sachs: down, Buy -> Neutral
  - 2026-02-24 JP Morgan: down, Overweight -> Neutral
  - 2026-01-09 CICC: init, ? -> Outperform
  - 2025-12-08 Argus Research: down, Buy -> Hold
Institutional ownership: 9.8%
Largest holders: Dodge & Cox Inc. (0.6%), LOOMIS SAYLES & CO L P (0.5%), Franklin Resources, Inc. (0.4%), Price (T.Rowe) Associates Inc (0.3%), Morgan Stanley (0.3%)
```

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score -0.10</summary>

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

### Toyota (TM) · Company — BULLISH, confidence 0.55

**Result:** REJECTED · no room under the sleeve budget limit

**In the model's own words:** no explanation. It wrote only “BUY”, so the main reasons below are all it gave.

**Main reasons it gave:**
- Analyst mean price target $234 (+20% vs last close)
- Four consecutive earnings beats (44%, 12%, 27%, 24% beats)
- Technical: price above 20d SMA (+3.4%) and 50d SMA (+1.9%) with RSI 57.3 and positive MACD
- Trailing P/E 8.57 indicates cheap valuation

<details><summary><b>News</b> — score +0.20</summary>

- [Should Value Investors Buy Honda Motor Co. (HMC) Stock?](https://finance.yahoo.com/markets/stocks/articles/value-investors-buy-honda-motor-124002962.html)  
  <sub>Yahoo Finance, 2 hours ago</sub>  
  Here at Zacks, our focus is on the proven Zacks Rank system, which emphasizes earnings estimates and estimate revisions to find great stocks.
- [Winnebago Stock After Q4 Earnings: Buy, Hold or Sell Now?](https://www.zacks.com/stock/news/3013554/winnebago-stock-after-q4-earnings-buy-hold-or-sell-now)  
  <sub>Zacks Investment Research, 3 hours ago</sub>  
  Winnebago's Motorhome RV revenue rose 8.4% to $1.26B as operating income reached $33.2M. WGO plans manufacturing consolidations as fiscal 2026 operating...
- [Edge Total Intelligence and Beamr Imaging Interviews to Air Nationally on the RedChip Small Stocks, Big Money(TM) Show on CNBC and Bloomberg TV](https://www.guardonline.com/news/national/edge-total-intelligence-and-beamr-imaging-interviews-to-air-nationally-on-the-redchip-small-stocks/article_22d667e9-cd49-5f3f-93ca-faf44144ac46.html)  
  <sub>The Batesville Daily Guard, 2 hours ago</sub>  
  ORLANDO, FL / ACCESS Newswire / October 23, 2026 / RedChip Companies will air interviews with Edge Total Intelligence Inc. (TSXV:CTRL)(OTCQB:UNFYF)(FSE:Q5I)...
- [A sensor can spot nearby objects and interpret data on the device. MicroVision is taking orders.](https://www.stocktitan.net/news/MVIS/micro-vision-begins-commercial-production-of-movia-tm-pro-to-meet-9fr6smpunj6k.html)  
  <sub>Stock Titan, 14 hours ago</sub>  
  It captures multiple returns per pulse and supports drones, traffic systems and warehouse robots; customers can update its perception software on-device.
- [How to Take Advantage of moves in (RMAX) (RMAX:CA)](https://news.stocktradersdaily.com/canada/how-to-take-advantage-of-moves-in-rmax-_20261023_0b1470)  
  <sub>Stock Traders Daily, 2 hours ago</sub>  
  When Investors Make Decisions in Hamilton REITs YIELD MAXIMIZER TM ETF RMAX Opportunities Surface.
- [Toyota stock: Bernstein sets JPY 4,100 target for Toyota stock](https://www.ad-hoc-news.de/boerse/news/corporate-news/toyota-stock-bernstein-sets-jpy-4-100-target-for-toyota-stock/70399113)  
  <sub>AD HOC NEWS, 2 hours ago</sub>  
  Fiscal 2026 revenue rose 5.50 percent to JPY 50.68 trillion. Toyota stock costs EUR 175.50 on October 23, 2026 at USD 236.2 billion value.
- [TM Jan 2028 340.000 call (TM280121C00340000) Interactive Stock Chart - Yahoo Finance](https://ca.finance.yahoo.com/quote/TM280121C00340000/chart/)  
  <sub>Yahoo! Finance Canada, 8 hours ago</sub>  
  Interactive Chart for TM Jan 2028 340.000 call (TM280121C00340000), analyze all the data with a huge range of indicators.
- [A 4:30 p.m. ET call is set for Nov. 5, when FocalTherics will release third-quarter results.](https://www.stocktitan.net/news/FOCL/focal-therics-tm-to-announce-third-quarter-2026-financial-results-on-khnc3nma34zy.html)  
  <sub>Stock Titan, 18 hours ago</sub>  
  CEO Ryan Rhodes and CFO Ken Mobeck will lead the call and webcast; results are scheduled after market close and cover the quarter ended Sept. 30, 2026.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.20</summary>

_Not available today._

</details>

<details><summary><b>Price and chart</b> — score +0.30</summary>

```text
Last close 195.05 (bar of 2026-10-23), from 502 daily bars
Trend: vs 20d SMA 188.71 (+3.4%), 50d 191.44 (+1.9%), 200d 199.41 (-2.2%); 50d below 200d
Momentum: RSI(14) 57.3 | MACD 1.711 vs signal 0.453 (histogram 1.258)
Returns: 1d -1.6% | 5d +0.2% | 1m +4.5% | 3m +7.1%
52-week range: 166.50 - 248.29 (now 34.9% of the way up)
Volatility: ATR(14) 3.14 (1.6% of price) | annualised 20d 20.6%
Volume: 0.21x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.00</summary>

```text
Sector: Consumer Cyclical / Auto Manufacturers | market cap 229.73B
Valuation: trailing P/E 8.57 | forward P/E 12.36 | P/B 15.67 | PEG n/a
Profitability: profit margin 8.6% | operating margin 7.9% | ROE 12.4%
Growth (YoY): revenue +10.4% | earnings +86.9%
Balance sheet: debt/equity 115.0% | free cash flow -3.60T
Risk: beta 0.38 | short interest 0.1% of float
Next earnings: 2026-11-05
```

</details>

<details><summary><b>What this fund holds</b> — score +0.00</summary>

_Not available today._

</details>

<details><summary><b>Does this company beat its own forecasts</b> — score +0.00</summary>

```text
Earnings record, last 4 quarters: 4 beats
  2026-06-30 beat by 44% | 2026-03-31 beat by 12% | 2025-12-31 beat by 27% | 2025-09-30 beat by 24%
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

<details><summary><b>What analysts and big funds say</b> — score +0.50</summary>

```text
Consensus: none (mean n/a on a 1=strong buy to 5=strong sell scale, 4 analysts)
Ratings: 2 strong buy, 2 buy, 0 hold, 0 sell, 0 strong sell
Price target: mean 234.08 (+20.0% vs last close), range 230.00 - 239.31
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

### Alphabet (Google) (GOOGL) · Company — BEARISH, confidence 0.45

**Result:** REJECTED · no room under the sleeve budget limit

**In the model's own words:**

> The short‑term technical picture is clearly bearish (price below all major SMAs, low RSI and negative MACD, weak recent returns and thin volume). News is mixed but leans negative due to a recent 3 % price drop on AI‑spending concerns, a cloud outage and net ETF selling. Fundamentals remain strong (low trailing P/E, high margins and ROE), and analysts are still strongly bullish, but those views are already priced in and there is no fresh upgrade. Earnings history is mixed with recent misses, adding downside risk ahead of the upcoming earnings report. The net effect is a modest bearish tilt with moderate confidence.

**Main reasons it gave:**
- RSI 32.9 and MACD -3.553 indicate bearish momentum (Technical)
- Price below 20‑day, 50‑day, and 200‑day SMAs (Technical)
- Trailing P/E 16.2 and 48.7% ROE show strong fundamentals (Fundamentals)
- 3.1% price drop on AI spending concerns and cloud outage (News)
- Mixed earnings record: 2 beats, 2 misses, recent misses (Earnings)

<details><summary><b>News</b> — score -0.20</summary>

- [Pre-Q3 Earnings: Is Alphabet Stock a Portfolio Must-Have?](https://finance.yahoo.com/markets/stocks/articles/pre-q3-earnings-alphabet-stock-131000590.html)  
  <sub>Yahoo Finance, 2 hours ago</sub>  
  GOOGL's Q3 earnings outlook is fueled by AI adoption, cloud growth and advertising strength, but premium valuation and margin pressures warrant attention.
- [Alphabet (NASDAQ:GOOGL) Screens as a GARP-Friendly Quality Compounder](https://www.chartmill.com/news/GOOGL/Chartmill-56714-Alphabet-NASDAQGOOGL-Screens-as-a-GARP-Friendly-Quality-Compounder)  
  <sub>ChartMill, 4 hours ago</sub>  
  Alphabet fits Peter Lynch's GARP screen with strong EPS growth, low debt, high ROE, and a PEG below 1, though valuation and ROIC trends warrant monitoring.
- [Google Stock News (Oct 23, 2026): GOOGL Falls 3.1% to $324.22](https://www.heygotrade.com/en/news/google-googl-stock-news-october-23-2026/)  
  <sub>Gotrade, 10 hours ago</sub>  
  Alphabet (GOOGL) fell $10.54, or 3.15%, to $324.22 on October 22, 2026, as worries over AI spending and the cost of capital hit tech stocks.
- [Dan Ives Says AI Capex Boom Continues 'Full Steam Ahead' After TSLA, GOOGL Earnings — Gene Munster Notes Tech Industry Still In '3rd Inning'](https://stocktwits.com/news-articles/markets/equity/dan-ives-ai-capex-boom-continues-full-steam-tsla-googl-q2-gene-munster-3rd-inning/cZZnV4ER7xp)  
  <sub>Stocktwits, 15 hours ago</sub>  
  Tech strategist Dan Ives said that the AI capital expenditure boom remains “full steam ahead” after the latest quarterly results from Tesla Inc. (TSLA) and...
- [Alphabet (GOOGL) Cloud Outage And Share Token Fight Put Regulation In Focus](https://finance.yahoo.com/technology/articles/alphabet-googl-cloud-outage-share-131307505.html)  
  <sub>Yahoo Finance, 2 hours ago</sub>  
  Alphabet (NasdaqGS: GOOGL) is under scrutiny after a major Google Cloud outage in London disrupted UK financial and government services.
- [Should You Buy Alphabet Stock Before the Huge Investor Update?](https://www.fool.com/investing/2026/10/22/should-you-buy-alphabet-stock-before-the-huge-investor-update/)  
  <sub>The Motley Fool, 13 hours ago</sub>  
  Alphabet's AI business is booming, but the search business is not out of the woods just yet.
- [ETFs Are Net Sellers of Alphabet (GOOGL) on Oct. 21](https://finance.yahoo.com/markets/stocks/articles/etfs-net-sellers-alphabet-googl-110330183.html)  
  <sub>Yahoo Finance, 4 hours ago</sub>  
  This article first appeared on GuruFocus. Alphabet (GOOGL) recorded $31.0 million in net ETF selling in Wednesday's session, even though more funds traded...
- [Countdown to Alphabet (GOOGL) Q3 Earnings: Wall Street Forecasts for Key Metrics](https://finance.yahoo.com/markets/stocks/articles/countdown-alphabet-googl-q3-earnings-121507781.html)  
  <sub>Yahoo Finance, 2 hours ago</sub>  
  Evaluate the expected performance of Alphabet (GOOGL) for the quarter ended September 2026, looking beyond the conventional Wall Street top-and-bottom-line...
- [Alphabet (GOOGL) vs. MSFT and AMZN: Can AI Investments and Google Cloud Growth Unlock a 26% Upside?](https://finance.yahoo.com/markets/stocks/articles/alphabet-googl-vs-msft-amzn-202624782.html)  
  <sub>Yahoo Finance, 18 hours ago</sub>  
  Is GOOGL a good stock to buy? We came across a bullish thesis on Alphabet Inc. on Astute Optics – US's Substack. In this article, we will summarize the...
- [GOOGL Oct 2026 317.500 put (GOOGL261023P00317500) Stock Price, News, Quote & History](https://ca.finance.yahoo.com/quote/GOOGL261023P00317500/)  
  <sub>Yahoo! Finance Canada, 14 hours ago</sub>  
  Find the latest GOOGL Oct 2026 317.500 put (GOOGL261023P00317500) stock quote, history, news and other vital information to help you with your stock trading...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score -0.20</summary>

_Not available today._

</details>

<details><summary><b>Price and chart</b> — score -0.60</summary>

```text
Last close 323.20 (bar of 2026-10-23), from 502 daily bars
Trend: vs 20d SMA 343.23 (-5.8%), 50d 343.00 (-5.8%), 200d 341.33 (-5.3%); 50d above 200d
Momentum: RSI(14) 32.9 | MACD -3.553 vs signal -0.728 (histogram -2.825)
Returns: 1d -0.3% | 5d -5.1% | 1m -5.6% | 3m -1.0%
52-week range: 253.08 - 402.62 (now 46.9% of the way up)
Volatility: ATR(14) 8.58 (2.7% of price) | annualised 20d 20.6%
Volume: 0.21x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.60</summary>

```text
Sector: Communication Services / Internet Content & Information | market cap 3.95T
Valuation: trailing P/E 16.22 | forward P/E 21.04 | P/B 6.35 | PEG 1.25
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

<details><summary><b>What analysts and big funds say</b> — score +0.40</summary>

```text
Consensus: strong_buy (mean 1.38 on a 1=strong buy to 5=strong sell scale, 54 analysts)
Ratings: 13 strong buy, 43 buy, 5 hold, 0 sell, 0 strong sell
Price target: mean 429.12 (+32.8% vs last close), range 340.00 - 500.00
Recent rating changes:
  - 2026-10-22 Citizens: main, Market Outperform -> Market Outperform
  - 2026-10-20 BMO Capital: main, Outperform -> Outperform
  - 2026-10-19 Keybanc: main, Overweight -> Overweight
  - 2026-10-15 JP Morgan: main, Overweight -> Overweight
  - 2026-10-14 UBS: main, Neutral -> Neutral
  - 2026-10-12 Cantor Fitzgerald: reit, Overweight -> Overweight
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

### Teva Pharmaceutical (TEVA) · Company — NEUTRAL, confidence 0.40

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Mixed signals: technicals show negative momentum and thin volume, fundamentals are weighed down by high leverage, while analyst consensus remains strongly bullish with a sizable price‑target gap but no fresh upgrades. Insider sales appear routine, and earnings history is mixed (3 beats, 1 large miss). The net effect is a near‑neutral outlook, warranting a low‑conviction neutral signal.

**Main reasons it gave:**
- Technical momentum negative: RSI 48.8, MACD below signal, thin volume (0.39x avg)
- High leverage: debt/equity 217.8%
- Analyst consensus strong buy with +19.9% price‑target gap but no recent upgrades
- Recent insider net selling (-150,983 shares, -2.3% holdings) considered routine

<details><summary><b>News</b> — score +0.00</summary>

- [Market Movers RX: Car Zeiss Meditec Leads Gainers](https://www.pharmexec.com/shorts/market-movers-rx-car-zeiss-meditec-leads-gainers)  
  <sub>Pharmaceutical Executive, 5 hours ago</sub>  
  This week on Market Movers Rx, we break down the key stock movers on the week, from gains at Carl Zeiss Meditec and Moderna to declines for Humana and Teva...
- [TEVA Oct 2026 34.000 call (TEVA261030C00034000) Stock Price, News, Quote & History](https://ca.finance.yahoo.com/quote/TEVA261030C00034000/)  
  <sub>Yahoo! Finance Canada, 19 hours ago</sub>  
  Find the latest TEVA Oct 2026 34.000 call (TEVA261030C00034000) stock quote, history, news and other vital information to help you with your stock trading...
- [Lupin appoints Brian Savage as President, Chief Legal Officer](https://legal.economictimes.indiatimes.com/news/corporate-business/lupin-appoints-brian-savage-as-president-chief-legal-officer/135134002)  
  <sub>ETLegalWorld.com, 11 hours ago</sub>  
  Pharmaceutical major Lupin Ltd has appointed Brian Savage as President and Chief Legal Officer, effective October 22, 2026, according to a stock exchange...
- [Lupin appoints Brian Savage as President and Chief Legal Officer](https://scanx.trade/stock-market-news/companies/lupin-appoints-brian-savage-president-chief-legal-officer/54234581)  
  <sub>scanx.trade, 10 hours ago</sub>  
  Lupin appointed Brian Savage as President and Chief Legal Officer effective October 22, 2026. Savage previously served as Executive Vice President and...
- [Teva stock: At 4.31 percent below its high, Teva stock traded at USD 40.21 on October 22](https://www.ad-hoc-news.de/boerse/news/corporate-news/teva-stock-at-4-31-percent-below-its-high-teva-stock-traded-at-usd-40-21-on-october-22/70399130)  
  <sub>AD HOC NEWS, 2 hours ago</sub>  
  Barclays kept Overweight at USD 47.00 on October 15, 2026. Teva stock was USD 40.21 on October 22, 2026 at 4:00 p.m. ET, down 1.01 percent on NYSE.
- [TEVA Nov 2026 37.000 call (TEVA261106C00037000) Interactive Stock Chart](https://ca.finance.yahoo.com/quote/TEVA261106C00037000/chart/)  
  <sub>Yahoo! Finance Canada, 19 hours ago</sub>  
  Interactive Chart for TEVA Nov 2026 37.000 call (TEVA261106C00037000), analyze all the data with a huge range of indicators.
- [Teva reports Uvakitug efficacy data. November 3 results matter for Teva stock](https://www.ad-hoc-news.de/boerse/news/corporate-news/teva-reports-uvakitug-efficacy-data-november-3-results-matter-for-teva-stock/70397468)  
  <sub>AD HOC NEWS, 7 hours ago</sub>  
  Weltruza launched with three approved doses after FDA approval on October 9, 2026. For Teva stock, revenue was USD 4.14 billion before November 3 results.
- [TEVA Nov 2026 31.000 call (TEVA261120C00031000) interactive stock chart – Yahoo Finance](https://sg.finance.yahoo.com/quote/TEVA261120C00031000/chart/)  
  <sub>Yahoo Finance Singapore, 16 hours ago</sub>  
  Interactive chart for TEVA Nov 2026 31.000 call (TEVA261120C00031000) – analyse all of the data with a huge range of indicators.
- [TEVA Nov 2026 43.000 put (TEVA261120P00043000) Stock Price, News, Quote & History](https://ca.finance.yahoo.com/quote/TEVA261120P00043000/)  
  <sub>Yahoo! Finance Canada, 21 hours ago</sub>  
  Find the latest TEVA Nov 2026 43.000 put (TEVA261120P00043000) stock quote, history, news and other vital information to help you with your stock trading...
- [GALAPAGOS TEVA TESOURO SELIC & IPCA+ FUNDO DE ÍNDICE (POSB11.SA) stock price, news, quote and history](https://sg.finance.yahoo.com/quote/POSB11.SA/)  
  <sub>Yahoo Finance Singapore, 19 hours ago</sub>  
  Find the latest GALAPAGOS TEVA TESOURO SELIC & IPCA+ FUNDO DE ÍNDICE (POSB11.SA) stock quote, history, news and other vital information to help you with...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

_Not available today._

</details>

<details><summary><b>Price and chart</b> — score -0.40</summary>

```text
Last close 39.67 (bar of 2026-10-23), from 502 daily bars
Trend: vs 20d SMA 40.19 (-1.3%), 50d 38.69 (+2.5%), 200d 34.37 (+15.4%); 50d above 200d
Momentum: RSI(14) 48.8 | MACD 0.568 vs signal 0.750 (histogram -0.182)
Returns: 1d -1.3% | 5d -4.4% | 1m -1.4% | 3m +27.6%
52-week range: 18.95 - 41.50 (now 91.9% of the way up)
Volatility: ATR(14) 1.12 (2.8% of price) | annualised 20d 22.9%
Volume: 0.39x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score -0.15</summary>

```text
Sector: Healthcare / Drug Manufacturers - Specialty & Generic | market cap 46.27B
Valuation: trailing P/E 66.12 | forward P/E 12.86 | P/B 5.96 | PEG 0.71
Profitability: profit margin 4.1% | operating margin 4.0% | ROE 9.7%
Growth (YoY): revenue -0.8% | earnings n/a
Balance sheet: debt/equity 217.8% | free cash flow 2.22B
Risk: beta 0.82 | short interest 2.6% of float
Next earnings: 2026-11-03
```

</details>

<details><summary><b>What this fund holds</b> — score -0.15</summary>

_Not available today._

</details>

<details><summary><b>Does this company beat its own forecasts</b> — score -0.15</summary>

```text
Earnings record, last 4 quarters: 3 beats, 1 missed
  2026-06-30 missed by 92% | 2026-03-31 beat by 9% | 2025-12-31 beat by 39% | 2025-09-30 beat by 17%
```

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

<details><summary><b>What analysts and big funds say</b> — score +0.40</summary>

```text
Consensus: strong_buy (mean 1.46 on a 1=strong buy to 5=strong sell scale, 12 analysts)
Ratings: 4 strong buy, 8 buy, 1 hold, 0 sell, 0 strong sell
Price target: mean 47.58 (+19.9% vs last close), range 42.00 - 55.00
Recent rating changes:
  - 2026-10-15 Barclays: main, Overweight -> Overweight
  - 2026-10-12 JP Morgan: main, Overweight -> Overweight
  - 2026-10-01 TD Cowen: init, ? -> Buy
  - 2026-09-23 Oppenheimer: init, ? -> Outperform
  - 2026-09-09 Leerink Partners: init, ? -> Outperform
  - 2026-09-04 UBS: main, Buy -> Buy
Institutional ownership: 27.2%
Largest holders: Blackrock Inc. (5.5%), Harel Insurance Investments & Financial Services Ltd. (4.1%), Phoenix Financial Ltd. (3.7%), WCM Investment Management, LLC (3.5%), Clal Insurance Enterprises Holdings Ltd (3.5%)
```

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score +0.40</summary>

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

### MercadoLibre (MELI) · Company — NEUTRAL, confidence 0.33

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> The inputs are mixed: bullish analyst consensus and insider purchases are offset by weak earnings record, high valuation and leverage, and mixed technical signals. With contradictory evidence, a neutral stance with low conviction is appropriate.

**Main reasons it gave:**
- Insider purchases: 124 shares by officer (MELAMUD MARCELO) and 600 shares by director (AGUZIN ALEJANDRO NICOLAS)
- Earnings record: 3 misses and 1 beat in the last 4 quarters
- Analyst consensus: buy with mean price target +25% vs current price
- Fundamentals: high valuation (trailing P/E 49.44) and high debt/equity (168.6%)
- Technical indicators mixed: MACD bullish but price below 20‑day/50‑day SMA and volume at 0.2× 20‑day average

<details><summary><b>News</b> — score +0.00</summary>

- [MELI Nov 2026 1865.000 put (MELI261106P01865000) Interactive Stock Chart - Yahoo Finance](https://ca.finance.yahoo.com/quote/MELI261106P01865000/chart/)  
  <sub>Yahoo! Finance Canada, 3 hours ago</sub>  
  Interactive Chart for MELI Nov 2026 1865.000 put (MELI261106P01865000), analyze all the data with a huge range of indicators.
- [MercadoLibre, Inc. Estimates – NASDAQ:MELI](https://www.tradingview.com/symbols/NASDAQ-MELI/financials-estimates/)  
  <sub>TradingView, 2 hours ago</sub>  
  See how MercadoLibre, Inc. performed against analyst expectations and compare actual results with revenue, earnings, cash flow, and valuation estimates.
- [MercadoLibre, Inc. $MELI Stock: AMF Tjanstepension AB Reduces Stake](https://www.marketbeat.com/instant-alerts/filing-mercadolibre-inc-meli-stock-amf-tjanstepension-ab-reduces-stake-2026-10-23/)  
  <sub>MarketBeat, 6 hours ago</sub>  
  AMF Tjanstepension AB cut its stake in shares of MercadoLibre, Inc. (NASDAQ:MELI - Free Report) by 1.9% during the third quarter, according to the company...
- [If You Invested $1000 In MercadoLibre Stock 10 Years Ago, You Would Have This Much Today](https://www.benzinga.com/news/26/10/62546474/if-you-invested-1000-mercadolibre-stock-10-years-ago-you-would-have-much-today)  
  <sub>Benzinga, 19 hours ago</sub>  
  MercadoLibre (NASDAQ:MELI) has outperformed the market over the past 10 years by 13.16% on an annualized basis producing an average annual return of 26.74%.
- [MELI Nov 2026 2040.000 put (MELI261106P02040000) Stock Price, News, Quote & History](https://ca.finance.yahoo.com/quote/MELI261106P02040000/)  
  <sub>Yahoo! Finance Canada, 8 hours ago</sub>  
  Find the latest MELI Nov 2026 2040.000 put (MELI261106P02040000) stock quote, history, news and other vital information to help you with your stock trading...
- [877 MercadoLibre, Inc. $MELI Shares Sold by E. Ohman J or Asset Management AB](https://www.marketbeat.com/instant-alerts/filing-877-mercadolibre-inc-meli-shares-sold-by-e-ohman-j-or-asset-management-ab-2026-10-23/)  
  <sub>MarketBeat, 5 hours ago</sub>  
  E. Ohman J or Asset Management AB reduced its stake in MercadoLibre, Inc. (NASDAQ:MELI - Free Report) by 4.6% in the third quarter, according to the company...
- [MercadoLibre (MELI) Registers a Bigger Fall Than the Market: Important Facts to Note](https://finance.yahoo.com/markets/stocks/articles/mercadolibre-meli-registers-bigger-fall-205002768.html)  
  <sub>Yahoo Finance, 18 hours ago</sub>  
  MercadoLibre (MELI) ended the recent trading session at $1,824.96, demonstrating a -1.61% change from the preceding day's closing price. The stock's change...
- [MELI Nov 2026 1530.000 call (MELI261106C01530000) stock price, news, quote and history](https://uk.finance.yahoo.com/quote/MELI261106C01530000/)  
  <sub>Yahoo Finance UK, 14 hours ago</sub>  
  Find the latest MELI Nov 2026 1530.000 call (MELI261106C01530000) stock quote, history, news and other vital information to help you with your stock trading...
- [MELI Nov 2026 1895.000 put (MELI261106P01895000) Interactive Stock Chart - Yahoo Finance](https://ca.finance.yahoo.com/quote/MELI261106P01895000/chart/)  
  <sub>Yahoo! Finance Canada, 13 hours ago</sub>  
  Interactive Chart for MELI Nov 2026 1895.000 put (MELI261106P01895000), analyze all the data with a huge range of indicators.
- [MELI Nov 2026 2130.000 put (MELI261106P02130000) Stock Price, News, Quote & History](https://ca.finance.yahoo.com/quote/MELI261106P02130000/)  
  <sub>Yahoo! Finance Canada, 17 hours ago</sub>  
  Find the latest MELI Nov 2026 2130.000 put (MELI261106P02130000) stock quote, history, news and other vital information to help you with your stock trading...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

_Not available today._

</details>

<details><summary><b>Price and chart</b> — score -0.10</summary>

```text
Last close 1,817.75 (bar of 2026-10-23), from 502 daily bars
Trend: vs 20d SMA 1,820.04 (-0.1%), 50d 1,859.48 (-2.2%), 200d 1,825.25 (-0.4%); 50d above 200d
Momentum: RSI(14) 46.9 | MACD 1.777 vs signal 0.985 (histogram 0.791)
Returns: 1d -0.4% | 5d -0.9% | 1m +3.6% | 3m -0.1%
52-week range: 1,546.81 - 2,360.76 (now 33.3% of the way up)
Volatility: ATR(14) 53.32 (2.9% of price) | annualised 20d 40.9%
Volume: 0.20x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score -0.20</summary>

```text
Sector: Consumer Cyclical / Internet Retail | market cap 92.15B
Valuation: trailing P/E 49.44 | forward P/E 32.09 | P/B 11.76 | PEG 1.00
Profitability: profit margin 5.3% | operating margin 6.7% | ROE 27.5%
Growth (YoY): revenue +49.8% | earnings -10.9%
Balance sheet: debt/equity 168.6% | free cash flow 353.38M
Risk: beta 1.31 | short interest 1.8% of float
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

<details><summary><b>What analysts and big funds say</b> — score +0.30</summary>

```text
Consensus: buy (mean 1.62 on a 1=strong buy to 5=strong sell scale, 26 analysts)
Ratings: 4 strong buy, 16 buy, 6 hold, 0 sell, 0 strong sell
Price target: mean 2,273.86 (+25.1% vs last close), range 1,750.00 - 2,800.00
Recent rating changes:
  - 2026-10-13 Citigroup: main, Neutral -> Neutral
  - 2026-10-12 Cantor Fitzgerald: main, Overweight -> Overweight
  - 2026-10-06 Susquehanna: main, Positive -> Positive
  - 2026-09-03 BTIG: reit, Buy -> Buy
  - 2026-08-11 JP Morgan: main, Neutral -> Neutral
  - 2026-08-06 Cantor Fitzgerald: main, Overweight -> Overweight
Institutional ownership: 80.1%
Largest holders: Capital Research Global Investors (6.2%), BAILLIE GIFFORD & CO (6.0%), Capital International Investors (3.7%), Capital World Investors (3.5%), Morgan Stanley (2.9%)
```

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score +0.30</summary>

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

### ASML (ASML) · Company — no answer, no confidence given

<details><summary><b>News</b> — score n/a</summary>

- [Stock-Split Watch: Is ASML Next?](https://finance.yahoo.com/markets/stocks/articles/stock-split-watch-asml-next-092100911.html)  
  <sub>Yahoo Finance, 5 hours ago</sub>  
  ASML has underperformed the broader semiconductor sector, and a stock split could be just what the company needs right now.
- [ASML: The AI Bottleneck That Could Be Bigger Than Investors Expect (NASDAQ:ASML)](https://seekingalpha.com/article/4956854-asml-the-ai-bottleneck-that-could-be-bigger-than-investors-expect)  
  <sub>Seeking Alpha, 3 hours ago</sub>  
  ASML's current valuation already reflects significant AI-driven growth; upside depends on a prolonged AI supercycle. Read why ASML stock is a buy.
- [ASML Holding N.V. - New York Registry Shares Stock 12‑Month Price Target Raised to $2408.5, Implies 54% Upside](https://www.tradingview.com/news/tradingview:4962a5442b8ff:0-asml-holding-n-v-new-york-registry-shares-stock-12-month-price-target-raised-to-2408-5-implies-54-upside/)  
  <sub>TradingView, 10 hours ago</sub>  
  Explore more price target data and ratings for ASML Holding N.V. - New York Registry Shares on the Forecasts tab, and track all previous and future analyst...
- [ETFs Bought $25.7 Million of ASML (ASML) on Oct. 21](https://finance.yahoo.com/markets/stocks/articles/etfs-bought-25-7-million-110157080.html)  
  <sub>Yahoo Finance, 4 hours ago</sub>  
  Nine ETFs bought ASML shares while three sold, for a net inflow of $25.7 million.
- [ASML Holding NV (ASML) Shares Fall 6.9% -- What GF Score of 95 Tells Investors](https://www.gurufocus.com/news/9138007/asml-holding-nv-asml-shares-fall-69-what-gf-score-of-95-tells-investors)  
  <sub>GuruFocus, 17 hours ago</sub>  
  On October 22, 2026, ASML Holding NV (ASML) shares fell 6.9% to a current price of $1560.54, moving within a 52-week range of $946.11 to $1999.96.
- [Binance Will Support the ASML Holding N.V. (ASML) and Nokia Corporation (NOK) Cash Dividend Distribution via bStocks | Binance announcement](https://www.binance.com/en/support/announcement/b3609ecc681f4be1a56da77f5fd26c9f)  
  <sub>Binance, 10 hours ago</sub>  
  Binance will support the ASML Holding N.V. (ASML) and Nokia Corporation (NOK) cash dividend distribution via bStocks for ASMLB and NOKB holders.
- [Lam Research Sinks 9% as Supply Constraints Cap Outlook; Applied Materials Drops 6%, ASML Holding Falls 4%](https://247wallst.com/investing/2026/10/22/lam-research-sinks-9-as-supply-constraints-cap-outlook-applied-materials-drops-6-asml-holding-falls-4/)  
  <sub>24/7 Wall St., 24 hours ago</sub>  
  Lam Research stock sank 8% after supply chain constraints capped its December-quarter guidance at $8.6 billion, overshadowing record revenue of $8.22...
- [Taiwan Semiconductor and ASML Are Incredible, but 1 of These Monopoly Chip Stocks Is Far Safer.](https://www.fool.com/investing/2026/10/22/taiwan-semiconductor-and-asml-are-incredible-but-1/)  
  <sub>The Motley Fool, 20 hours ago</sub>  
  There are few companies on the market more impressive than Taiwan Semiconductor Manufacturing (TSM -4.52%) and ASML Holding (ASML -6.93%).
- [ASML Stocks Fall 4.8% as Besi Clarifies the Hybrid-Bonding Bound](https://www.gurufocus.com/news/9137239/asml-stocks-fall-48-as-besi-clarifies-the-hybridbonding-boundary)  
  <sub>GuruFocus, 21 hours ago</sub>  
  Lithography equipment supplier ASML (ASML) received some clarity on a potential expansion market as its U.S.-listed shares traded at $1595.50,...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>Price and chart</b> — score n/a</summary>

```text
Last close 1,574.10 (bar of 2026-10-23), from 502 daily bars
Trend: vs 20d SMA 1,732.43 (-9.1%), 50d 1,722.78 (-8.6%), 200d 1,588.00 (-0.9%); 50d above 200d
Momentum: RSI(14) 35.5 | MACD -37.430 vs signal -16.356 (histogram -21.074)
Returns: 1d +0.9% | 5d -4.1% | 1m -8.6% | 3m -4.9%
52-week range: 966.57 - 1,989.44 (now 59.4% of the way up)
Volatility: ATR(14) 55.47 (3.5% of price) | annualised 20d 38.6%
Volume: 0.28x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score n/a</summary>

```text
Sector: Technology / Semiconductor Equipment & Materials | market cap 606.69B
Valuation: trailing P/E 38.73 | forward P/E 25.05 | P/B 1,351.60 | PEG 1.58
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
Price target: mean 2,142.94 (+36.1% vs last close), range 866.63 - 2,846.83
Recent rating changes:
  - 2026-10-15 JP Morgan: main, Overweight -> Overweight
  - 2026-07-16 JP Morgan: main, Overweight -> Overweight
  - 2026-07-16 Wells Fargo: main, Overweight -> Overweight
  - 2026-07-16 RBC Capital: main, Outperform -> Outperform
  - 2026-07-14 RBC Capital: main, Outperform -> Outperform
  - 2026-07-06 Bernstein: main, Outperform -> Outperform
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

### HDFC Bank (HDB) · Company — no answer, no confidence given

<details><summary><b>News</b> — score n/a</summary>

- [Trading Systems Reacting to (HDB) Volatility](https://news.stocktradersdaily.com/news_release/141/Trading_Systems_Reacting_to_HDB_Volatility_102226043402_1792701242.html)  
  <sub>Stock Traders Daily, 22 hours ago</sub>  
  Key findings for Hdfc Bank Limited (NYSE: HDB). Stable Neutral Readings in Shorter Horizons Could Signal Easing of Long-Term Weak Bias...
- [OFS dominates IPO fundraising as shareholders cash out ₹48,260 crore across 15 financial-services listings](https://bfsi.economictimes.indiatimes.com/amp/articles/ofs-dominates-ipo-fundraising-as-shareholders-cash-out-48260-crore-across-15-financial-services-listings/135139348)  
  <sub>bfsi.economictimes.indiatimes.com, 7 hours ago</sub>  
  India's financial services IPO market sees a staggering ₹48260 crore from offers for sale, revealing a trend where existing shareholders prioritize cashing...
- [NextEra Energy (NEE) Stock Price Today, Live Chart & News](https://techgraph.co/stock-market/quote/nee/)  
  <sub>TechGraph, 21 hours ago</sub>  
  NextEra Energy (NEE) stock price today: latest $81.38 (+3.96%) on NYSE. NEE share price, live chart, market cap, 52-week range, dividends and news on...
- [HDB stock pre-market at EUR 20.00 before the Xetra open](https://www.ad-hoc-news.de/boerse/news/vorboerse/hdb-stock-pre-market-at-eur-20-00-before-the-xetra-open/70397091)  
  <sub>AD HOC NEWS, 8 hours ago</sub>  
  HDFC Bank serves individual and corporate clients through banking and financial services in India and selected international markets. At Lang & Schwarz the...
- [HDB Financial Services appoints Jimmy Tata, renews two independent directors](https://scanx.trade/stock-market-news/companies/hdb-financial-services-appoints-jimmy-tata-renews-two-independent/54226532)  
  <sub>scanx.trade, 24 hours ago</sub>  
  HDB Financial Services appointed Jimmy Tata as Additional Non-Executive Director effective October 22, 2026. Jayesh Chakravarthi re-appointed as Independent...
- [Duke Energy (DUK) Stock Price Today, Live Chart & News](https://techgraph.co/stock-market/quote/duk/)  
  <sub>TechGraph, 21 hours ago</sub>  
  Duke Energy (DUK) stock price today: latest $124.46 (+3.14%) on NYSE. DUK share price, live chart, market cap, 52-week range, dividends and news on...
- [With over 1 crore applications, Jio IPO sets global record](https://english.dhanamonline.com/stock-markets/with-over-1-crore-applications-jio-ipo-sets-global-record-9004029)  
  <sub>DhanamOnline, 6 hours ago</sub>  
  The ₹30213-crore issue reportedly became the first IPO globally to cross the one-crore mark, surpassing 97 lakh applications received by Waaree Energies.
- [HDBank stock: HDBank completes two share issues. HDBank stock adds 30 percent more shares](https://www.ad-hoc-news.de/boerse/news/nebenwerte/hdbank-stock-hdbank-completes-two-share-issues-hdbank-stock-adds-30-percent-more-shares/70395798)  
  <sub>AD HOC NEWS, 15 hours ago</sub>  
  HDBank (VN000000HDB1) completed two share issues that increased its outstanding share count by 30 percent, according to Fili on October 19, 2026.
- [HDFC Bank reports Q2 profit growth: what it means for HDFC Bank stock](https://www.ad-hoc-news.de/boerse/news/corporate-news/hdfc-bank-reports-q2-profit-growth-what-it-means-for-hdfc-bank-stock/70397471)  
  <sub>AD HOC NEWS, 7 hours ago</sub>  
  Net interest income rose 9.70 percent to INR 346.19 billion in Q2 FY27. HDFC Bank stock costs EUR 20.15 on October 23, 2026.
- [HDFC Bank stock: Jefferies keeps INR 880 target for HDFC Bank stock](https://www.ad-hoc-news.de/boerse/news/corporate-news/hdfc-bank-stock-jefferies-keeps-inr-880-target-for-hdfc-bank-stock/70394328)  
  <sub>AD HOC NEWS, 24 hours ago</sub>  
  Gross NPA fell to 1.11 percent in the second quarter of fiscal 2027. HDFC Bank stock costs EUR 20.05 on October 22, 2026 at 4:36 p.m. CEST.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>Price and chart</b> — score n/a</summary>

```text
Last close 22.04 (bar of 2026-10-23), from 502 daily bars
Trend: vs 20d SMA 22.61 (-2.5%), 50d 22.85 (-3.5%), 200d 26.10 (-15.5%); 50d below 200d
Momentum: RSI(14) 42.2 | MACD -0.059 vs signal -0.037 (histogram -0.023)
Returns: 1d -1.8% | 5d -7.6% | 1m -3.5% | 3m -5.1%
52-week range: 21.84 - 37.13 (now 1.3% of the way up)
Volatility: ATR(14) 0.55 (2.5% of price) | annualised 20d 29.9%
Volume: 0.17x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score n/a</summary>

```text
Sector: Financial Services / Banks - Regional | market cap 113.34B
Valuation: trailing P/E 14.22 | forward P/E 15.95 | P/B 8.77 | PEG n/a
Profitability: profit margin 26.5% | operating margin 38.5% | ROE 11.0%
Growth (YoY): revenue +80.8% | earnings +21.3%
Balance sheet: debt/equity n/a | free cash flow n/a
Risk: beta 0.41 | short interest 0.7% of float
Next earnings: 2027-01-16
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
Price target: mean 30.30 (+37.5% vs last close), range 26.20 - 33.00
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

- [JPM Oct 2026 250.000 call (JPM261030C00250000) Interactive Stock Chart - Yahoo Finance](https://ca.finance.yahoo.com/quote/JPM261030C00250000/chart/)  
  <sub>Yahoo! Finance Canada, 5 hours ago</sub>  
  Interactive Chart for JPM Oct 2026 250.000 call (JPM261030C00250000), analyze all the data with a huge range of indicators.
- [JPMorgan Chase & Co. $JPM Stock Sold by Grandview Asset Management LLC](https://www.marketbeat.com/instant-alerts/filing-jpmorgan-chase-co-jpm-stock-sold-by-grandview-asset-management-llc-2026-10-23/)  
  <sub>MarketBeat, 6 hours ago</sub>  
  Grandview Asset Management LLC trimmed its holdings in JPMorgan Chase & Co. (NYSE:JPM - Free Report) by 30.8% in the third quarter, according to its most...
- [JPM Nov 2026 295.000 put (JPM261127P00295000) stock price, news, quote and history](https://uk.finance.yahoo.com/quote/JPM261127P00295000/)  
  <sub>Yahoo Finance UK, 6 hours ago</sub>  
  Find the latest JPM Nov 2026 295.000 put (JPM261127P00295000) stock quote, history, news and other vital information to help you with your stock trading and...
- [5,154 JPMorgan Chase & Co. $JPM Shares Sold by Commonwealth Financial Services LLC](https://www.marketbeat.com/instant-alerts/filing-5154-jpmorgan-chase-co-jpm-shares-sold-by-commonwealth-financial-services-llc-2026-10-23/)  
  <sub>MarketBeat, 3 hours ago</sub>  
  Commonwealth Financial Services LLC decreased its stake in shares of JPMorgan Chase & Co. (NYSE:JPM - Free Report) by 26.9% during the third quarter,...
- [JPM Oct 2026 327.500 call (JPM261023C00327500) stock price, news, quote and history](https://au.finance.yahoo.com/quote/JPM261023C00327500/)  
  <sub>Yahoo Finance Australia, 1 hour ago</sub>  
  Find the latest JPM Oct 2026 327.500 call (JPM261023C00327500) stock quote, history, news and other vital information to help you with your stock trading...
- [JPMorgan Chase & Co. $JPM Stock: Focused Alpha LLC Increases Position](https://www.marketbeat.com/instant-alerts/filing-jpmorgan-chase-co-jpm-stock-focused-alpha-llc-increases-position-2026-10-23/)  
  <sub>MarketBeat, 7 hours ago</sub>  
  Focused Alpha LLC increased its holdings in JPMorgan Chase & Co. (NYSE:JPM - Free Report) by 37.2% in the 3rd quarter, according to the company in its most...
- [JPM Oct 2026 310.000 call (JPM261023C00310000) stock price, news, quote and history](https://uk.finance.yahoo.com/quote/JPM261023C00310000/)  
  <sub>Yahoo Finance UK, 9 hours ago</sub>  
  Find the latest JPM Oct 2026 310.000 call (JPM261023C00310000) stock quote, history, news and other vital information to help you with your stock trading...
- [JPMorgan Chase & Co. $JPM Shares Sold by Willis Investment Counsel](https://www.marketbeat.com/instant-alerts/filing-jpmorgan-chase-co-jpm-shares-sold-by-willis-investment-counsel-2026-10-23/)  
  <sub>MarketBeat, 6 hours ago</sub>  
  Willis Investment Counsel lessened its stake in shares of JPMorgan Chase & Co. (NYSE:JPM - Free Report) by 24.2% during the third quarter, according to the...
- [JPM Jun 2027 375.000 put (JPM270617P00375000) Stock Price, News, Quote & History](https://ca.finance.yahoo.com/quote/JPM270617P00375000/)  
  <sub>Yahoo! Finance Canada, 14 hours ago</sub>  
  Find the latest JPM Jun 2027 375.000 put (JPM270617P00375000) stock quote, history, news and other vital information to help you with your stock trading and...
- [Erste Group Bank Issues Optimistic Forecast for JPM Earnings](https://www.marketbeat.com/instant-alerts/estimates-erste-group-bank-issues-optimistic-forecast-for-jpm-earnings-2026-10-23/)  
  <sub>MarketBeat, 2 hours ago</sub>  
  JPMorgan Chase & Co. (NYSE:JPM - Free Report) - Stock analysts at Erste Group Bank upped their FY2027 earnings per share (EPS) estimates for JPMorgan Chase...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>Price and chart</b> — score n/a</summary>

```text
Last close 331.36 (bar of 2026-10-23), from 502 daily bars
Trend: vs 20d SMA 333.69 (-0.7%), 50d 345.40 (-4.1%), 200d 322.51 (+2.7%); 50d above 200d
Momentum: RSI(14) 40.9 | MACD -2.677 vs signal -3.422 (histogram 0.745)
Returns: 1d -1.5% | 5d -2.5% | 1m -2.1% | 3m -7.0%
52-week range: 282.84 - 365.18 (now 58.9% of the way up)
Volatility: ATR(14) 6.34 (1.9% of price) | annualised 20d 14.6%
Volume: 0.14x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score n/a</summary>

```text
Sector: Financial Services / Banks - Diversified | market cap 880.17B
Valuation: trailing P/E 13.90 | forward P/E 12.98 | P/B 2.51 | PEG 1.57
Profitability: profit margin 34.6% | operating margin 42.6% | ROE 18.0%
Growth (YoY): revenue +10.2% | earnings +9.9%
Balance sheet: debt/equity n/a | free cash flow n/a
Risk: beta 1.01 | short interest 0.9% of float
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
Price target: mean 372.26 (+12.3% vs last close), range 312.00 - 425.00
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

<details><summary><b>What analysts say about what this fund holds</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>Buying and selling by company insiders</b> — score n/a</summary>

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

<details><summary><b>Who is positioned how</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>Money going into and out of this fund</b> — score n/a</summary>

_Not available today._

</details>

### Eli Lilly (LLY) · Company — no answer, no confidence given

<details><summary><b>News</b> — score n/a</summary>

- [What Sent Eli Lilly Stock Higher Over The Past Year?](https://finance.yahoo.com/markets/stocks/articles/sent-eli-lilly-stock-higher-101403667.html)  
  <sub>Yahoo Finance, 5 hours ago</sub>  
  For questions about this article or underlying research, email help@trefis.com. Eli Lilly (LLY) stock returned 61.9% over the year to October 22, 2026,...
- [Amgen vs. Eli Lilly: Does the GLP-1 Mania Make LLY Stock a Better Buy in 2026?](https://www.fool.com/coverage/better-buy/2026/10/22/amgen-vs-eli-lilly-does-the-glp-1-mania-make-lly-stock-a-better-buy-in-2026/)  
  <sub>The Motley Fool, 16 hours ago</sub>  
  Amgen trades at half the valuation multiple of Eli Lilly while generating stronger free cash flow, but explosive growth in obesity drugs tells a different...
- [(10/23/26) LLY: How to Trade This Pharma Stock That’s Hitting New Highs](https://www.moneyshow.com/articles/tradingidea-65564/lly-how-to-trade-this-pharma-stock-thats-hitting-new-highs/)  
  <sub>www.moneyshow.com, 11 hours ago</sub>  
  Valued at $1.17 trillion, Eli Lilly & Co. (LLY) is one of the world's largest pharmaceutical companies. The Trend Seeker issued a new “Buy” signal on Oct.
- [Eli Lilly stock may move 6.6% on Oct. 29 earnings release](https://www.investing.com/news/stock-market-news/eli-lilly-stock-may-move-66-on-oct-29-earnings-release-93CH-4966657)  
  <sub>Investing.com, 13 hours ago</sub>  
  Investing.com -- Eli Lilly & Co. (NYSE:LLY) stock may move 6.6% when the company reports earnings on Oct. 29 before the market opens, according to options...
- [Why Eli Lilly (LLY) Stock Is Up Today](https://www.moomoo.com/news/post/1002096748/why-eli-lilly-lly-stock-is-up-today)  
  <sub>Moomoo, 23 hours ago</sub>  
  EliLilly and Company (LLY) is up 3.5% today. Here is some analysis on what might have caused this price movement.Analysis: The most likely driver is fresh...
- [Eli Lilly (LLY) Sees $64.0 Million in Net ETF Selling on Oct. 21](https://finance.yahoo.com/markets/stocks/articles/eli-lilly-lly-sees-64-110229277.html)  
  <sub>Yahoo Finance, 4 hours ago</sub>  
  ETFs pulled $64.0 million from Eli Lilly on Wednesday, Oct. 21, extending a three-day selling streak.
- [Eli Lilly (LLY) Price Forecast: Breakout Strengthens Ahead of Earnings](https://www.fxempire.com/forecasts/article/eli-lilly-lly-price-forecast-breakout-strengthens-ahead-of-earnings-1639895)  
  <sub>FXEmpire, 11 hours ago</sub>  
  Eli Lilly reaches a record high ahead of earnings, strengthening its bullish trend as technical signals point toward potential upside targets between $1384...
- [Eli Lilly and Co Stock (LLY) Moved Up by 3.37% on Oct 22: What Investors Need To Know](https://www.tradingkey.com/news/market-movers/262232751-market-movers-lly-20261022)  
  <sub>TradingKey, 24 hours ago</sub>  
  Analysts raised Eli Lilly targets ahead of third-quarter earnings.Strong demand for Mounjaro and Zepbound drove momentum.Capital investments expanded...
- [Eli Lilly (LLY) Launches $5B Manufacturing Plant in Virginia to Boost Cancer Therapy Production](https://www.gurufocus.com/news/9137101/eli-lilly-lly-launches-5b-manufacturing-plant-in-virginia-to-boost-cancer-therapy-production)  
  <sub>GuruFocus, 23 hours ago</sub>  
  On October 22, 2026, Eli Lilly and Co (NYSE: LLY) announced the commencement of a $5 billion manufacturing facility in Goochland County, Virginia,...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>Price and chart</b> — score n/a</summary>

```text
Last close 1,279.04 (bar of 2026-10-23), from 502 daily bars
Trend: vs 20d SMA 1,205.22 (+6.1%), 50d 1,186.72 (+7.8%), 200d 1,084.97 (+17.9%); 50d above 200d
Momentum: RSI(14) 63.5 | MACD 31.241 vs signal 19.781 (histogram 11.460)
Returns: 1d -2.1% | 5d +1.8% | 1m +8.2% | 3m +6.8%
52-week range: 813.53 - 1,306.69 (now 94.4% of the way up)
Volatility: ATR(14) 37.06 (2.9% of price) | annualised 20d 30.5%
Volume: 0.25x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score n/a</summary>

```text
Sector: Healthcare / Drug Manufacturers - General | market cap 1.14T
Valuation: trailing P/E 42.94 | forward P/E 27.09 | P/B 33.66 | PEG 1.14
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
Price target: mean 1,331.55 (+4.1% vs last close), range 930.00 - 1,600.00
Recent rating changes:
  - 2026-10-21 Leerink Partners: main, Outperform -> Outperform
  - 2026-10-12 RBC Capital: reit, Outperform -> Outperform
  - 2026-10-08 Cantor Fitzgerald: main, Overweight -> Overweight
  - 2026-10-07 Morgan Stanley: main, Overweight -> Overweight
  - 2026-09-28 JP Morgan: main, Overweight -> Overweight
  - 2026-09-22 TD Cowen: reit, Buy -> Buy
Institutional ownership: 85.4%
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

### Microsoft (MSFT) · Company — no answer, no confidence given

<details><summary><b>News</b> — score n/a</summary>

- [ETFs Are Net Sellers of Microsoft (MSFT) on Wednesday](https://finance.yahoo.com/markets/stocks/articles/etfs-net-sellers-microsoft-msft-110223638.html)  
  <sub>Yahoo Finance, 4 hours ago</sub>  
  ETFs sold $83.6 million of Microsoft stock on Oct. 21, with 40 funds buying and 24 selling.
- [Could You Have Seen The Run In Microsoft Stock Coming?](https://www.trefis.com/stock/msft/articles/620174/could-you-have-seen-the-run-in-microsoft-stock-coming/2026-10-23)  
  <sub>Trefis, 6 hours ago</sub>  
  For questions about this article or underlying research, email help@trefis.com. Microsoft (MSFT) stock returned 36.8% from July 24 to October 22, 2026,...
- [Microsoft's Earnings Are Days Away: Here’s What Investors Need to Know](https://www.benzinga.com/trading-ideas/movers/26/10/62559686/microsofts-earnings-are-days-away-heres-what-investors-need-to-know)  
  <sub>Benzinga, 50 minutes ago</sub>  
  Microsoft Corporation (NASDAQ:MSFT) shares are in the spotlight, with earnings on deck, Azure growth and capital spending in focus, recent analyst activity,...
- [Microsoft Has a $1 Trillion Opportunity Hiding in Plain Sight](https://247wallst.com/investing/2026/10/23/microsoft-has-a-1-trillion-opportunity-hiding-in-plain-sight/)  
  <sub>24/7 Wall St., 3 hours ago</sub>  
  Microsoft (MSFT) earns a BUY with a $648 price target, backed by a $678 billion contracted backlog and Azure crossing $100 billion in annual revenue.
- [Seeking Clues to Microsoft (MSFT) Q1 Earnings? A Peek Into Wall Street Projections for Key Metrics](https://finance.yahoo.com/markets/stocks/articles/seeking-clues-microsoft-msft-q1-121507389.html)  
  <sub>Yahoo Finance, 2 hours ago</sub>  
  Wall Street analysts expect Microsoft (MSFT) to post quarterly earnings of $4.71 per share in its upcoming report, which indicates a year-over-year increase...
- [Microsoft AI Diagnostic Tool Outperforms Physicians In Medical Study](https://www.tikr.com/blog/microsoft-stock-ai-diagnostic-tool-outperforms-physicians)  
  <sub>TIKR.com, 1 hour ago</sub>  
  Now Live: Discover how much upside your favorite stocks could have using TIKR's new Valuation Model (It's free)>>>. What Happened? Microsoft (MSFT)...
- [OpenAI Just Cut Its Valuation Target by $150 Billion](https://247wallst.com/investing/2026/10/23/openai-just-cut-its-valuation-target-by-150-billion/)  
  <sub>24/7 Wall St., 3 hours ago</sub>  
  OpenAI slashed its funding ask by a staggering amount just as public AI stocks cratered, and the timing raises serious questions about what private...
- [How much MSFT stock does Microsoft CEO Satya Nadella actually own?](https://finance.yahoo.com/markets/stocks/articles/much-msft-stock-does-microsoft-170702323.html)  
  <sub>Yahoo Finance, 22 hours ago</sub>  
  Satya Nadella transformed Microsoft into a Cloud and AI powerhouse. But compared with his predecessors, his stake in the company is surprisingly small.
- [Microsoft (MSFT) Falls More Steeply Than Broader Market: What Investors Need to Know](https://finance.yahoo.com/markets/stocks/articles/microsoft-msft-falls-more-steeply-204503019.html)  
  <sub>Yahoo Finance, 18 hours ago</sub>  
  In the latest close session, Microsoft (MSFT) was down 2.23% at $521.08. The stock's change was less than the S&P 500's daily loss of 1.21%.
- [Microsoft Stock Could Be Closer to Its Next Big Breakout Than Investors Think](https://finance.yahoo.com/markets/stocks/articles/microsoft-stock-could-closer-next-153056788.html)  
  <sub>Yahoo Finance, 23 hours ago</sub>  
  MSFT's BUY rating targets $650 with 90% confidence, powered by Azure's 43% growth and CFO Amy Hood's confirmation that customer demand still exceeds...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>Price and chart</b> — score n/a</summary>

```text
Last close 522.94 (bar of 2026-10-23), from 502 daily bars
Trend: vs 20d SMA 526.62 (-0.7%), 50d 508.40 (+2.9%), 200d 436.51 (+19.8%); 50d above 200d
Momentum: RSI(14) 51.7 | MACD 7.027 vs signal 9.427 (histogram -2.400)
Returns: 1d +0.4% | 5d -1.2% | 1m +5.0% | 3m +34.4%
52-week range: 352.83 - 543.45 (now 89.2% of the way up)
Volatility: ATR(14) 11.16 (2.1% of price) | annualised 20d 19.6%
Volume: 0.19x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score n/a</summary>

```text
Sector: Technology / Software - Infrastructure | market cap 3.88T
Valuation: trailing P/E 29.13 | forward P/E 22.06 | P/B 8.78 | PEG 1.62
Profitability: profit margin 40.3% | operating margin 45.1% | ROE 34.0%
Growth (YoY): revenue +17.7% | earnings +31.7%
Balance sheet: debt/equity 29.1% | free cash flow 16.55B
Risk: beta 1.10 | short interest 0.8% of float
Next earnings: 2026-10-28
```

</details>

<details><summary><b>What this fund holds</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>Does this company beat its own forecasts</b> — score n/a</summary>

```text
Earnings record, last 4 quarters: 4 beats
  2026-06-30 beat by 10% | 2026-06-30 beat by 10% | 2026-03-31 beat by 3% | 2026-03-31 beat by 3%
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
Consensus: strong_buy (mean 1.33 on a 1=strong buy to 5=strong sell scale, 53 analysts)
Ratings: 13 strong buy, 41 buy, 3 hold, 0 sell, 0 strong sell
Price target: mean 601.73 (+15.1% vs last close), range 440.00 - 870.00
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

<details><summary><b>What analysts say about what this fund holds</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>Buying and selling by company insiders</b> — score n/a</summary>

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

<details><summary><b>Who is positioned how</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>Money going into and out of this fund</b> — score n/a</summary>

_Not available today._

</details>

### Nvidia (NVDA) · Company — no answer, no confidence given

<details><summary><b>News</b> — score n/a</summary>

- [NVIDIA Corporation (NVDA.NE) Stock Price, News, Quote & History](https://ca.finance.yahoo.com/quote/NVDA.NE/)  
  <sub>Yahoo! Finance Canada, 10 hours ago</sub>  
  NVIDIA Corporation (NVDA.NE) · Previous Close 49.33 · Open 48.27 · Bid 47.20 x -- · Ask 47.22 x -- · Day's Range 47.00 - 48.61 · 52 Week Range 17.88 - 48.61...
- [Nvidia Stock’s 2 Critical Flaws and More Reasons an Analyst Says Sell](https://www.barrons.com/articles/nvidia-stock-price-sell-analyst-64e607bf)  
  <sub>Barron's, 41 minutes ago</sub>  
  Competitive pressures are mounting for Nvidia stock and there is a strategic tension at the heart of the business, according to Seaport Research.
- [NVDA Stock Falls 4.4% to $212.21 as AI Financing Fears Hit Chips](https://www.fxleaders.com/news/2026/10/23/nvda-stock-falls-4-4-to-212-21-as-ai-financing-fears-hit-chips/)  
  <sub>FXLeaders, 2 hours ago</sub>  
  Nvidia (NASDAQ: NVDA) dropped 4.40% on Thursday and closed at $212.21. In early trading today, U.S. futures pointed lower after the Nasdaq fell around 2.6%...
- [NVDA vs. LRCX: Which AI Semiconductor Stock Is the Better Buy?](https://www.zacks.com/stock/news/3013740/nvda-vs-lrcx-which-ai-semiconductor-stock-is-the-better-buy)  
  <sub>Zacks Investment Research, 2 hours ago</sub>  
  Both NVIDIA and Lam Research benefit from the AI boom, but NVIDIA's faster growth, stronger margins and lower valuation give it an edge. Here's why.
- [My Nvidia Stock Price Prediction for 2027 Is More Bullish Than You Might Expect](https://247wallst.com/investing/2026/10/23/my-nvidia-stock-price-prediction-for-2027-is-more-bullish-than-you-might-expect/)  
  <sub>24/7 Wall St., 12 minutes ago</sub>  
  NVDA's 59 bullish analysts project a $329 consensus target, while 5 straight earnings beats and rising FY2028 estimates support a more aggressive $350 call.
- [Nvidia Stock News (Oct 23, 2026): NVDA Falls 4.4% to $212.21](https://www.heygotrade.com/en/news/nvidia-nvda-stock-news-october-23-2026/)  
  <sub>Gotrade, 10 hours ago</sub>  
  Nvidia (NVDA) closed at $212.21 on Oct 22, 2026, down 4.40%, as worries over AI spending and the cost of capital hit chip stocks and the Nasdaq.
- [Nvidia Stock Forecast: Huang's Neocloud Funding Remarks Push NVDA Into the $206.89 Demand Zone](https://www.tradingkey.com/analysis/stocks/us-stocks/262235232-nvidia-stock-forecast-huang-neocloud-funding-chip-selloff-206-support-october-23-2026-tradingkey)  
  <sub>TradingKey, 6 hours ago</sub>  
  TradingKey - Nvidia stock forecast: NVDA drops 4.4% as Huang's neocloud funding remarks hit chip stocks, pushing price into the $206.89 to $212 demand zone.
- [Robert Bender&Associates trims Nvidia Corporation stake by 12,742 shares](https://www.theglobeandmail.com/investing/markets/stocks/NVDA/pressreleases/8348886/robert-benderassociates-trims-nvidia-corporation-stake-by-12742-shares/)  
  <sub>The Globe and Mail, 11 hours ago</sub>  
  Detailed price information for Nvidia Corp (NVDA-Q) from The Globe and Mail including charting and trades.
- [NVIDIA Corporation Estimates – NASDAQ:NVDA](https://www.tradingview.com/symbols/NASDAQ-NVDA/financials-estimates/)  
  <sub>TradingView, 3 hours ago</sub>  
  See how NVIDIA Corporation performed against analyst expectations and compare actual results with revenue, earnings, cash flow, and valuation estimates.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>Price and chart</b> — score n/a</summary>

```text
Last close 213.47 (bar of 2026-10-23), from 502 daily bars
Trend: vs 20d SMA 225.67 (-5.4%), 50d 222.53 (-4.1%), 200d 203.68 (+4.8%); 50d above 200d
Momentum: RSI(14) 40.6 | MACD -2.449 vs signal -0.457 (histogram -1.992)
Returns: 1d +0.6% | 5d -0.3% | 1m -4.9% | 3m +8.6%
52-week range: 165.17 - 239.24 (now 65.2% of the way up)
Volatility: ATR(14) 6.04 (2.8% of price) | annualised 20d 29.5%
Volume: 0.23x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score n/a</summary>

```text
Sector: Technology / Semiconductors | market cap 5.15T
Valuation: trailing P/E 26.99 | forward P/E 13.41 | P/B 22.51 | PEG 0.48
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
  2026-09-30 beat by 4% | 2026-06-30 beat by 4% | 2026-06-30 beat by 4% | 2026-03-31 beat by 4%
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
Consensus: strong_buy (mean 1.29 on a 1=strong buy to 5=strong sell scale, 58 analysts)
Ratings: 10 strong buy, 49 buy, 2 hold, 1 sell, 0 strong sell
Price target: mean 328.95 (+54.1% vs last close), range 180.00 - 515.00
Recent rating changes:
  - 2026-10-22 Needham: reit, Buy -> Buy
  - 2026-10-01 Cantor Fitzgerald: reit, Overweight -> Overweight
  - 2026-09-29 Rosenblatt: main, Buy -> Buy
  - 2026-09-10 Piper Sandler: init, ? -> Overweight
  - 2026-09-04 Rosenblatt: main, Buy -> Buy
  - 2026-09-04 Needham: reit, Buy -> Buy
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

- [The Toronto-Dominion Bank (TD.TO) stock price, news, quote and history](https://uk.finance.yahoo.com/quote/TD.TO/)  
  <sub>Yahoo Finance UK, 8 hours ago</sub>  
  Find the latest The Toronto-Dominion Bank (TD.TO) stock quote, history, news and other vital information to help you with your stock trading and investing.
- [Royal Bank Of Canada $RY Stock Sold by Pinnacle Associates Ltd.](https://www.marketbeat.com/instant-alerts/filing-royal-bank-of-canada-ry-stock-sold-by-pinnacle-associates-ltd-2026-10-23/)  
  <sub>MarketBeat, 5 hours ago</sub>  
  Pinnacle Associates Ltd. reduced its position in Royal Bank Of Canada (NYSE:RY - Free Report) (TSE:RY) by 52.4% during the third quarter, according to the...
- [Royal Bank of Canada stock outperforms market despite losses on the day](https://www.marketwatch.com/data-news/royal-bank-of-canada-stock-outperforms-market-despite-losses-on-the-day-f7be3050-de2510e8dd57?mod=mw_quote_news)  
  <sub>MarketWatch, 18 hours ago</sub>  
  Shares of Royal Bank of Canada. RY. +0.96%. slipped 0.30% to C$282.78 Thursday, in what proved to be an all-around negative trading session for the Canadian...
- [RY Nov 2026 195.000 call (RY261120C00195000) Stock Price, News, Quote & History](https://ca.finance.yahoo.com/quote/RY261120C00195000/)  
  <sub>Yahoo! Finance Canada, 14 hours ago</sub>  
  Find the latest RY Nov 2026 195.000 call (RY261120C00195000) stock quote, history, news and other vital information to help you with your stock trading and...
- [Royal Bank of Canada (TSE:RY) Shares Break Above Two Hundred Day Moving Average - Here's Why](https://www.marketbeat.com/instant-alerts/price-royal-bank-of-canada-tse-ry-shares-break-above-two-hundred-day-moving-average-heres-why-2026-10-23/)  
  <sub>MarketBeat, 7 hours ago</sub>  
  Royal Bank of Canada (TSE:RY) Stock Price Breaks Above 200-Day Moving Average - Here's What Happened.
- [Costco's Last Stock Split Was in 2000. Is Its Board Close to Another?](https://www.theglobeandmail.com/investing/markets/stocks/NVDA-Q/pressreleases/8323764/costco-s-last-stock-split-was-in-2000-is-its-board-close-to-another/)  
  <sub>The Globe and Mail, 24 hours ago</sub>  
  Costco's last stock split was a 2-for-1 split in January 2000. Walmart and O'Reilly Automotive both split their shares to help employees buy whole shares...
- [Royal Bank of Canada stock: Zacks expects December 2 results for Royal Bank of Canada stock](https://www.ad-hoc-news.de/boerse/news/corporate-news/royal-bank-of-canada-stock-zacks-expects-december-2-results-for-royal-bank-of-canada-stock/70399763)  
  <sub>AD HOC NEWS, 36 minutes ago</sub>  
  RBC reported third-quarter earnings up 11.00 percent on August 27, 2026. Royal Bank of Canada stock costs EUR 178.57 on October 23, 2026.
- [RY Nov 2026 190.000 put (RY261120P00190000) stock price, news, quote and history](https://au.finance.yahoo.com/quote/RY261120P00190000/)  
  <sub>Yahoo Finance Australia, 17 hours ago</sub>  
  Find the latest RY Nov 2026 190.000 put (RY261120P00190000) stock quote, history, news and other vital information to help you with your stock trading and...
- [Could Royal Bank of Canada (TSX:RY) Maintain Its Dividend Strength?](https://kalkinemedia.com/ca/stocks/dividend/could-royal-bank-of-canada-tsxry-maintain-its-dividend-strength)  
  <sub>Kalkine Media, 21 hours ago</sub>  
  Royal Bank of Canada (TSX:RY) in dividend stocks: a neutral look at canadian bank distributions, operating factors and the Canadian market context.
- [RBC Investor Services named service provider for NEI Investments' new ETF series](https://www.theglobeandmail.com/investing/markets/stocks/RY-N/pressreleases/8325280/rbc-investor-services-named-service-provider-for-nei-investments-new-etf-series/)  
  <sub>The Globe and Mail, 24 hours ago</sub>  
  Detailed price information for Royal Bank of Canada (RY-N) from The Globe and Mail including charting and trades.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>Price and chart</b> — score n/a</summary>

```text
Last close 199.81 (bar of 2026-10-23), from 502 daily bars
Trend: vs 20d SMA 196.40 (+1.7%), 50d 202.29 (-1.2%), 200d 188.35 (+6.1%); 50d above 200d
Momentum: RSI(14) 52.1 | MACD -0.566 vs signal -1.781 (histogram 1.215)
Returns: 1d -1.1% | 5d +1.0% | 1m +0.2% | 3m -4.6%
52-week range: 145.41 - 217.87 (now 75.1% of the way up)
Volatility: ATR(14) 2.97 (1.5% of price) | annualised 20d 17.0%
Volume: 2.52x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score n/a</summary>

```text
Sector: Financial Services / Banks - Diversified | market cap 276.62B
Valuation: trailing P/E 17.47 | forward P/E 15.67 | P/B 2.90 | PEG 2.26
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
Earnings record, last 4 quarters: 1 beat, 3 in line
  2026-09-30 in line | 2026-06-30 in line | 2026-06-30 in line | 2026-03-31 beat by 3%
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
Price target: mean 213.30 (+6.8% vs last close), range 186.17 - 234.61
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

- [Exxon Mobil Holdings (XOM) Reports Next Week: Wall Street Expects Earnings Growth](https://finance.yahoo.com/markets/stocks/articles/exxon-mobil-holdings-xom-reports-130008430.html)  
  <sub>Yahoo Finance, 2 hours ago</sub>  
  Exxon (XOM) possesses the right combination of the two key ingredients for a likely earnings beat in its upcoming report. Get prepared with the key...
- [Fund Update: New $68.5M $XOM stock position opened by MUTUAL OF AMERICA CAPITAL MANAGEMENT LLC](https://www.quiverquant.com/news/Fund+Update%3A+New+%2468.5M+%24XOM+stock+position+opened+by+MUTUAL+OF+AMERICA+CAPITAL+MANAGEMENT+LLC)  
  <sub>Quiver Quantitative, 2 hours ago</sub>  
  MUTUAL OF AMERICA CAPITAL MANAGEMENT LLC has opened a new $68.5M position in $XOM, per a new SEC 13F filing. This disclosure reflects the funds' holdings...
- [ExxonMobil Holdings (NYSE:XOM) Stock Forecast & Analyst Predictions](https://simplywall.st/stocks/us/energy/nyse-xom/exxonmobil-holdings/future)  
  <sub>Simply Wall Street, 6 hours ago</sub>  
  Discover ExxonMobil Holdings' earnings and revenue growth rates, forecasts, and the latest analyst predictions while comparing them to its industry peers.
- [Why Did XOM, CVX, MPC Stocks Surge To 52-Week Highs Today?](https://stocktwits.com/news-articles/markets/equity/why-did-xom-cvx-mpc-stocks-surge-to-52-week-highs-today/cZxq1SXRBua)  
  <sub>Stocktwits, 18 hours ago</sub>  
  XOM stock clocked an annual high of $179.30 on Monday during trading hours, before closing about 0.4% down. CVX stock surged to a 52-week high of $225.67,...
- [XOM Apr 2027 210.000 call (XOM270416C00210000) Interactive Stock Chart - Yahoo Finance](https://ca.finance.yahoo.com/quote/XOM270416C00210000/chart/)  
  <sub>Yahoo! Finance Canada, 5 hours ago</sub>  
  Interactive Chart for XOM Apr 2027 210.000 call (XOM270416C00210000), analyze all the data with a huge range of indicators.
- [Eni SpA Q3 Earnings Ahead: What's in Store for the Stock?](https://www.tradingview.com/news/zacks:89a424426094b:0-eni-spa-q3-earnings-ahead-what-s-in-store-for-the-stock/)  
  <sub>TradingView, 18 hours ago</sub>  
  Eni SpA E is set to report third-quarter 2026 results on Oct. 23, after the closing bell.In the last reported quarter, its earnings of $1.76 per share...
- [Midwest pump prices surge after disruption at Exxon's Illinois refinery (XOM:NYSE)](https://seekingalpha.com/news/4656076-midwest-pump-prices-surge-after-disruption-at-exxons-illinois-refinery)  
  <sub>Seeking Alpha, 22 hours ago</sub>  
  Chicago-area bulk gasoline prices surged after ExxonMobil's (XOM) 275K-barrel refinery in Joliet, Illinois, shut a key unit on Wednesday, threatening to hit...
- [Vest Financial LLC Sells 13,751 Shares of ExxonMobil Corporation $XOM](https://www.marketbeat.com/instant-alerts/filing-vest-financial-llc-sells-13751-shares-of-exxonmobil-corporation-xom-2026-10-23/)  
  <sub>MarketBeat, 5 hours ago</sub>  
  Vest Financial LLC reduced its stake in shares of ExxonMobil Corporation (NYSE:XOM - Free Report) by 3.1% during the third quarter, according to its most...
- [ExxonMobil (XOM) Joliet Refinery Shutdown Pushes Chicago Gasoline Prices Higher](https://www.gurufocus.com/news/9137376/exxonmobil-xom-joliet-refinery-shutdown-pushes-chicago-gasoline-prices-higher)  
  <sub>GuruFocus, 21 hours ago</sub>  
  On October 22, 2026, gasoline prices in the Chicago area surged following the shutdown of a catalytic reformer unit at ExxonMobil Holdings Corp's (NYSE:...
- [XOM vs. BP: Which Integrated Energy Giant Has the Edge?](https://www.theglobeandmail.com/investing/markets/stocks/XOM-N/pressreleases/8326674/xom-vs-bp-which-integrated-energy-giant-has-the-edge/)  
  <sub>The Globe and Mail, 23 hours ago</sub>  
  Detailed price information for Exxonmobil Holdings Corp (XOM-N) from The Globe and Mail including charting and trades.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>Price and chart</b> — score n/a</summary>

```text
Last close 182.02 (bar of 2026-10-23), from 502 daily bars
Trend: vs 20d SMA 170.79 (+6.6%), 50d 165.76 (+9.8%), 200d 153.15 (+18.9%); 50d above 200d
Momentum: RSI(14) 75.0 | MACD 4.676 vs signal 3.781 (histogram 0.895)
Returns: 1d +2.1% | 5d +1.7% | 1m +12.3% | 3m +17.6%
52-week range: 113.68 - 182.02 (now 100.0% of the way up)
Volatility: ATR(14) 3.78 (2.1% of price) | annualised 20d 17.4%
Volume: 0.24x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score n/a</summary>

```text
Sector: Energy / Oil & Gas Integrated | market cap 748.45B
Valuation: trailing P/E 23.43 | forward P/E 14.83 | P/B 2.89 | PEG 1.38
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
Price target: mean 179.41 (-1.4% vs last close), range 142.00 - 206.00
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

> No material macro surprise, flat fund flows, weak short‑term technical momentum, and no analyst coverage or rating target.

**Main reasons it gave:**
- Flat fund flows (no net creation/redemption) indicating no directional pressure
- Technical indicators (RSI 37.5, MACD below signal) show weak short‑term momentum
- No macro news or data surprise this week, no policy or rate surprise
- Analyst view provides no rating or price target, indicating neutral coverage

<details><summary><b>News</b> — score +0.00</summary>

_No news found for this one today._

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.04% (-0.03 on the week) | 5-year 4.81% (-0.09 on the week) | 10-year 4.99% (-0.11 on the week) | 30-year 5.31% (-0.12 on the week)
Yield curve, 10-year minus 3-month: +0.95 points -- upward sloping (normal)
US dollar index: 101.76 (-0.08 on the week)
Volatility (VIX): 20.36 (+0.4 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.2% (2026-09-01) | jobless claims 194k (2026-10-17)
Policy and expectations: Fed target 4.00% | market expects 2.3% inflation over 10 years
Rate path: 2-year Treasury 4.81% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 27.93 (bar of 2026-10-23), from 502 daily bars
Trend: vs 20d SMA 28.27 (-1.2%), 50d 28.52 (-2.1%), 200d 27.33 (+2.2%); 50d above 200d
Momentum: RSI(14) 37.5 | MACD -0.126 vs signal -0.082 (histogram -0.044)
Returns: 1d +0.0% | 5d -1.1% | 1m -2.2% | 3m +1.1%
52-week range: 25.44 - 29.49 (now 61.5% of the way up)
Volatility: ATR(14) 0.23 (0.8% of price) | annualised 20d 9.4%
Volume: 0.10x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.00</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score +0.00</summary>

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
Share count change: 1 week: +0.0% (0.00) over 7d | 1 month: +0.0% (0.00) over 30d
Shares outstanding: 27.60M | fund size: 770.87M
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Commodities basket (DBC) · Index fund — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:** no explanation. It wrote only “NEUTRAL”, so the main reasons below are all it gave.

**Main reasons it gave:**
- Fund flows: +5.4% share count increase over 1 month (positive inflow)
- EIA price outlook forecasts WTI down 14% over six months (bearish)
- Technicals: price above SMA20/50/200, RSI 65.9, but volume only 0.22x 20‑day average (no decisive break)
- Analyst view of holdings provides no rating (neutral)

<details><summary><b>News</b> — score +0.00</summary>

_No news found for this one today._

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.04% (-0.03 on the week) | 5-year 4.81% (-0.09 on the week) | 10-year 4.99% (-0.11 on the week) | 30-year 5.31% (-0.12 on the week)
Yield curve, 10-year minus 3-month: +0.95 points -- upward sloping (normal)
US dollar index: 101.76 (-0.08 on the week)
Volatility (VIX): 20.36 (+0.4 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.2% (2026-09-01) | jobless claims 194k (2026-10-17)
Policy and expectations: Fed target 4.00% | market expects 2.3% inflation over 10 years
Rate path: 2-year Treasury 4.81% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 33.97 (bar of 2026-10-23), from 502 daily bars
Trend: vs 20d SMA 33.05 (+2.8%), 50d 32.39 (+4.9%), 200d 28.97 (+17.3%); 50d above 200d
Momentum: RSI(14) 65.9 | MACD 0.408 vs signal 0.385 (histogram 0.023)
Returns: 1d +1.2% | 5d +0.7% | 1m +2.4% | 3m +17.1%
52-week range: 22.36 - 33.97 (now 100.0% of the way up)
Volatility: ATR(14) 0.46 (1.4% of price) | annualised 20d 13.0%
Volume: 0.22x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score -0.30</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score -0.30</summary>

```text
Fund type: Commodities Broad Basket
What it holds: P/E n/a | P/B 0.00 | P/S 0.00 | 3y earnings growth n/a
Yield: 2.3%
Three-year record: +15.0% a year | beta to the market 1.05
Cost and size: expense ratio 0.85% | net assets 1.92B
What it is made of: Other 50.4%, Cash 45.1%, Bonds 2.5%, Stocks 2.0%
Largest holdings: Invesco Shrt-Trm Inv Gov&Agcy Instl 41.5%, Brent Crude Future Dec 26 9.7%, Invesco Short Term Treasury ETF 5.8%, Mini Ibovespa Future Dec 26 2.0%
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
US inventories, week ending 2026-10-16 (published the following Wednesday)
  Crude oil: 412.5 million barrels, -3.1 on the week (a draw), 15% percentile over 52 weeks
  Natural gas: 3,644.0 billion cubic feet, +77.0 on the week (a build), 87% percentile over 52 weeks -- high for the time of year
A build is more supply than demand and a draw is the reverse, so a build reads bearish and a draw bullish -- as a rule of thumb, not a law. Weigh the change and how unusual the level is above the level itself, and remember the market has already seen this number.
```

</details>

<details><summary><b>How the crop is growing</b> — score -0.30</summary>

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

<details><summary><b>Buying and selling by company insiders</b> — score +0.30</summary>

_Not available today._

</details>

<details><summary><b>Who is positioned how</b> — score +0.30</summary>

_Not available today._

</details>

<details><summary><b>Money going into and out of this fund</b> — score +0.30</summary>

```text
Direction: money coming in (1 month)
Share count change: 1 week: +0.0% (583.73K) over 7d | 1 month: +5.4% (100.49M) over 30d
Shares outstanding: 57.41M | fund size: 1.95B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Developing country bonds (EMB) · Index fund — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Neutral – no macro surprise, mixed technical picture, and modest bearish flow offset by solid fundamentals.

**Main reasons it gave:**
- US Treasury yields fell modestly across the curve this week (3‑month -0.03, 5‑year -0.09, 10‑year -0.11)
- EMB price 91.63 is 0.6% above 20‑day SMA but 1.4% below 50‑day SMA and 3.6% below 200‑day SMA, with volume at 0.22× 20‑day average
- Share count declined 11.4% over the past month (-1.67B), indicating net redemptions
- Fund basics: 5.4% yield, three‑year annual return +10.1%, credit mix includes 19.5% B‑rated bonds

<details><summary><b>News</b> — score +0.00</summary>

_No news found for this one today._

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.04% (-0.03 on the week) | 5-year 4.81% (-0.09 on the week) | 10-year 4.99% (-0.11 on the week) | 30-year 5.31% (-0.12 on the week)
Yield curve, 10-year minus 3-month: +0.95 points -- upward sloping (normal)
US dollar index: 101.76 (-0.08 on the week)
Volatility (VIX): 20.36 (+0.4 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.2% (2026-09-01) | jobless claims 194k (2026-10-17)
Policy and expectations: Fed target 4.00% | market expects 2.3% inflation over 10 years
Rate path: 2-year Treasury 4.81% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 91.63 (bar of 2026-10-23), from 502 daily bars
Trend: vs 20d SMA 91.11 (+0.6%), 50d 92.89 (-1.4%), 200d 95.07 (-3.6%); 50d below 200d
Momentum: RSI(14) 47.6 | MACD -0.339 vs signal -0.531 (histogram 0.193)
Returns: 1d -0.2% | 5d +0.1% | 1m -0.6% | 3m -3.5%
52-week range: 90.14 - 97.74 (now 19.6% of the way up)
Volatility: ATR(14) 0.51 (0.6% of price) | annualised 20d 6.6%
Volume: 0.22x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.30</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score +0.30</summary>

```text
Fund type: Emerging Markets Bond
Yield: 5.4%
Credit quality: BBB 33.5%, BB 25.3%, B 19.5%, A 17.7% | US government debt 88.0%
Three-year record: +10.1% a year | beta to the market 1.10
Cost and size: expense ratio 0.39% | net assets 12.93B
What it is made of: Bonds 99.1%, Cash 0.9%
Largest holdings: BlackRock Cash Funds Treasury SL Agency 0.7%
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

<details><summary><b>Buying and selling by company insiders</b> — score -0.50</summary>

_Not available today._

</details>

<details><summary><b>Who is positioned how</b> — score -0.50</summary>

_Not available today._

</details>

<details><summary><b>Money going into and out of this fund</b> — score -0.50</summary>

```text
Direction: money going out (1 month)
Share count change: 1 week: -0.1% (-18.13M) over 7d | 1 month: -11.4% (-1.67B) over 30d
Shares outstanding: 141.64M | fund size: 12.98B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### US government bonds, 7-10 years (IEF) · Index fund — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> No material macro surprise, yields slipped modestly, positioning unchanged, fundamentals stable, technicals neutral.

**Main reasons it gave:**
- 10‑year Treasury yield down 0.11% on the week, modestly supportive for bond prices
- CFTC positioning shows net short 37.9% of open interest with a -0.6% change, indicating no strong bearish pressure
- Fund basics unchanged: AA credit quality, 4.1% yield, 99.7% US government bonds
- Fed target unchanged at 4.0% and inflation at 3.7% within expectations, no policy surprise
- Technicals: price above 20‑day SMA, RSI 60.8, no decisive break

<details><summary><b>News</b> — score +0.00</summary>

- [Rob Kaplan Sees Fed Hike Likely In December — Warns Aggressive Tightening May Hurt Jobs Without Taming Inflation](https://es.tradingview.com/news/stocktwits:71131d490094b:0-rob-kaplan-sees-fed-hike-likely-in-december-warns-aggressive-tightening-may-hurt-jobs-without-taming-inflation/)  
  <sub>TradingView, 24 hours ago</sub>  
  Goldman Sachs Vice Chairman Rob Kaplan said Thursday that the Federal Reserve will likely raise interest rates in December but warned that aggressive...
- [(IEF) Movement Within Algorithmic Entry Frameworks](https://news.stocktradersdaily.com/news_release/12/IEF_Movement_Within_Algorithmic_Entry_Frameworks_102226094001_1792719602.html)  
  <sub>Stock Traders Daily, 17 hours ago</sub>  
  Price-action only: Ishares 7-10 Year Treasury Bond Etf (IEF) movements set the tone for institutional models. (IEF) Movement Within Algorithmic Entry...
- [META_TITLE_QUOTE](https://ca.finance.yahoo.com/quote/TLT/)  
  <sub>Yahoo! Finance Canada, 6 hours ago</sub>  
  The United States economy is full of innovation. It has to be. Manufacturing industries that dominated the economy decades ago - textiles, televisions,...
- [Black Monday Calls, $110 Oil, A Chip Rout: 3 Charts to Watch This Week](https://stocktwits.com/news-articles/markets/equity/black-monday-oil-prices-memory-chips-market-outlook/cZx8ZyaRBMj)  
  <sub>Stocktwits, 19 hours ago</sub>  
  Calls for a “Black Monday” crash spread across social media over the weekend, but U.S. stock futures were pointing higher early Monday, the 39th anniversary...
- [Former Fed Insider Warns Recession May Already Be Underway - iShares 7-10 Year Treasury Bond ETF (NASDAQ](https://www.benzinga.com/markets/economic-data/26/10/62550709/former-fed-insider-warns-recession-underway-treasury-rally)  
  <sub>Benzinga, 10 hours ago</sub>  
  Danielle DiMartino Booth warns a recession may already be underway, with Treasury yields falling and credit stress widening at AI spenders.
- [‘The economics of AI cannot work as tech is deflationary’ – Praetorian Capital’s Q3 investor letter](https://seekingalpha.com/news/4656149-the-economics-of-ai-cannot-work-as-tech-is-deflationary-praetorian-capital-s-q3-investor)  
  <sub>Seeking Alpha, 20 hours ago</sub>  
  Harris Kupperman warns AI economics may be unsustainable, risking recession and market declines.
- [Anthony Scaramucci Says the Working Class Are Not 'Inflation-Adjusted Rich' - iShares 7-10 Year Treasury](https://www.benzinga.com/markets/economic-data/26/10/62550516/anthony-scaramucci-americans-not-inflation-adjusted-rich)  
  <sub>Benzinga, 11 hours ago</sub>  
  Anthony Scaramucci says politicians get away with eroding workers' wealth because Americans can't tell nominal gains from real ones.
- [Ethereum stays below $2,400 as geopolitical tensions trigger long liquidations](https://invezz.com/au/news/2026/10/23/ethereum-stays-below-dollar2400-as-geopolitical-tensions-trigger-long-liquidations/)  
  <sub>Invezz, 9 hours ago</sub>  
  Ethereum stays below $2,400 on Friday as renewed Middle East tensions and concerns about AI-related spending sparked selling across cryptocurrency and...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.04% (-0.03 on the week) | 5-year 4.81% (-0.09 on the week) | 10-year 4.99% (-0.11 on the week) | 30-year 5.31% (-0.12 on the week)
Yield curve, 10-year minus 3-month: +0.95 points -- upward sloping (normal)
US dollar index: 101.76 (-0.08 on the week)
Volatility (VIX): 20.36 (+0.4 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.2% (2026-09-01) | jobless claims 194k (2026-10-17)
Policy and expectations: Fed target 4.00% | market expects 2.3% inflation over 10 years
Rate path: 2-year Treasury 4.81% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 91.06 (bar of 2026-10-23), from 502 daily bars
Trend: vs 20d SMA 89.75 (+1.5%), 50d 91.07 (-0.0%), 200d 93.99 (-3.1%); 50d below 200d
Momentum: RSI(14) 60.8 | MACD -0.031 vs signal -0.309 (histogram 0.278)
Returns: 1d -0.1% | 5d +0.7% | 1m +1.5% | 3m -2.4%
52-week range: 88.92 - 97.99 (now 23.6% of the way up)
Volatility: ATR(14) 0.51 (0.6% of price) | annualised 20d 5.7%
Volume: 0.25x the 20-day average
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
Three-year record: +4.1% a year | beta to the market 1.16
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

<details><summary><b>Buying and selling by company insiders</b> — score -0.40</summary>

_Not available today._

</details>

<details><summary><b>Who is positioned how</b> — score -0.40</summary>

```text
Contract: UST 10Y NOTE - CHICAGO BOARD OF TRADE (positions as of 2026-10-13, published the following Friday)
Large speculators: net short 37.9% of open interest (5,819,512 contracts)
Change on the week: -0.6% of open interest
Crowding: 60% percentile over 52 weeks -- within its normal range
Read this as crowding, not as a forecast: an extreme is as often the end of a move as the middle of one.
```

</details>

<details><summary><b>Money going into and out of this fund</b> — score -0.40</summary>

```text
Direction: flat (1 month)
Share count change: 1 week: -0.8% (-318.51M) over 7d | 1 month: -0.0% (-11.85M) over 30d
Shares outstanding: 460.69M | fund size: 41.95B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### US small companies (IWM) · Index fund — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Overall neutral as no material macro surprise, technicals are mixed, and behavioural data shows modest bearish positioning offset by slight bullish analyst and fundamental views.

**Main reasons it gave:**
- Large speculators net short 20.6% and increased short position (+4.2% OI) – bearish
- Analyst coverage thin (2% of fund) but 100% buy rating with +18.7% price target – modest bullish
- Technical indicators mixed: price below SMAs, RSI 42.3, MACD above signal – neutral
- Macro unchanged: yields down slightly, no policy surprise – neutral

<details><summary><b>News</b> — score +0.00</summary>

- [iShares Russell 2000 (IWM) Adds Axos Financial, Cuts Moog on Wednesday](https://www.google.com/goto?url=CAESmQEB6zswFQTUMv5D4uneLsNDGpt01JgvH7g7jyFTaAKivt3y01qqXFKbkbbAIXjOy7xDhLMsbUaKB4-eOphETJndXTU07FHaM-XuTYnVW1Cu-wAVGMSH23FNt_dIHDRnLFPjjNy5qELCn7NJ_JyhxSzCbgVLD60k9GgjY5ysQ-QPq0ui3-g9qMBoujxr1gF_R4KQGVOO218-ysM)  
  <sub>Yahoo Finance, 4 hours ago</sub>  
  This article first appeared on GuruFocus. iShares Russell 2000 Index Fund (IWM) reported ETF activity of $931.9 million in gross trades on Wednesday,...
- [AI Names Crater, Average Stocks Rise in Dramatic Rotation](https://www.google.com/goto?url=CAESnwEB6zswFbsPl6FB6GMZ_bgZIUKwXreRSYpv5VBuEpMmwK3zG8llHDjoEGvbuZG05wf3WO-4stykKtLHs-gbQJmVkUw3Szfz4PUjo1EMFmt7qbraHcN2JKTI1z9Zkt9s9qKWu9sMHTLR5xR870-5VnSbXeD_Xr4ZX0yCi0SIVR02NtEth2bEd7hgTHIPLuLkp61_8_f5I-34rVSntmkghQI)  
  <sub>TheStreet Pro, 18 hours ago</sub>  
  I've been discussing the two-tiered nature of this market and the gap in performance between AI-related names and the rest of the market for months now.
- [Webull Brings Options into Pre-Market as Brokers Adopt Cboe’s New Sessions](https://www.google.com/goto?url=CAESyAEB6zswFRWDQu7lR4gA6AUxYoheQoGbO-ChgcEwY4xJtYZJ3N68UAxaKFUhXnQVo4iEX35drEY4wCuhlVejAE1Ai5QiQGhPIWfwPTpSYHs1R_3fdDqNKOcXVd3kywcaiwMSUk-16B-f8M_20o3oP_y6_BxOuU7kwRWxMK9TvD8H6VsV7Ti0Z1Aj52SoGWWsZNYLhfQWNKY9Z6VPlHrQIYWpGJP4o9L5Fuc3JfQ14x6-_IHR3W1hRoRgX1HSoRRIy-p8EtHmF0cA0A)  
  <sub>TradingView, 23 hours ago</sub>  
  Webull joins the growing list of retail brokers offering extended-hours trading for eligible U.S. customers. The new trading hours and available instruments...
- [Defensives Lead Sectors In Thursday Trading As Growth Trails](https://www.benzinga.com/etfs/sector-etfs/26/10/62531733/defensives-lead-sectors-in-thursday-trading-as-growth-trails)  
  <sub>Benzinga, 24 hours ago</sub>  
  Five sectors are higher and six are lower in Thursday's regular session, with defensive sectors holding the top three positions. The leaders are separated...
- [Webull to introduce extended-hours options trading](https://fxnewsgroup.com/forex-news/retail-forex/webull-to-introduce-extended-hours-options-trading/)  
  <sub>FX News Group, 24 hours ago</sub>  
  Webull Corp (NASDAQ:BULL), an online investment platform, today announced it will introduce extended-hours trading for select single-stock and...
- [Exchange-Traded Funds, US Equities Lower After Midday](https://finance.yahoo.com/markets/stocks/articles/exchange-traded-funds-us-equities-171320665.html)  
  <sub>Yahoo Finance, 22 hours ago</sub>  
  Broad Market Indicators Broad-market exchange-traded funds IWM and IVV fell. Actively traded Invesco QQQ Trust (QQQ) lost 2.7%. US equity indexes were lower...
- [META_TITLE_QUOTE](https://www.google.com/goto?url=CAESYgHrOzAVWo4Pnk-MJdX3_udEKN6qqLhOSg7P0sbc3YJJIKLmK2ehwcCezNZtPvzOaw5UKE-k_6Nxlxavo08A3AW2yD7Se6h7zDDungAqBH_6FALZLnUWhx99hWETXDGapgyz)  
  <sub>Yahoo! Finance Canada, 6 hours ago</sub>  
  The United States economy is full of innovation. It has to be. Manufacturing industries that dominated the economy decades ago - textiles, televisions,...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.04% (-0.03 on the week) | 5-year 4.81% (-0.09 on the week) | 10-year 4.99% (-0.11 on the week) | 30-year 5.31% (-0.12 on the week)
Yield curve, 10-year minus 3-month: +0.95 points -- upward sloping (normal)
US dollar index: 101.76 (-0.08 on the week)
Volatility (VIX): 20.36 (+0.4 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.2% (2026-09-01) | jobless claims 194k (2026-10-17)
Policy and expectations: Fed target 4.00% | market expects 2.3% inflation over 10 years
Rate path: 2-year Treasury 4.81% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 275.25 (bar of 2026-10-23), from 502 daily bars
Trend: vs 20d SMA 277.17 (-0.7%), 50d 286.40 (-3.9%), 200d 278.23 (-1.1%); 50d above 200d
Momentum: RSI(14) 42.3 | MACD -3.120 vs signal -3.600 (histogram 0.480)
Returns: 1d -0.5% | 5d +1.8% | 1m -2.3% | 3m -6.0%
52-week range: 229.11 - 305.09 (now 60.7% of the way up)
Volatility: ATR(14) 3.68 (1.3% of price) | annualised 20d 14.7%
Volume: 0.27x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.10</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score +0.10</summary>

```text
Fund type: Small Blend
What it holds: P/E 16.35 | P/B 2.02 | P/S 1.25 | 3y earnings growth n/a
Yield: 1.0%
Three-year record: +19.8% a year | beta to the market 1.27
Cost and size: expense ratio 0.19% | net assets 78.04B
What it is made of: Stocks 99.7%, Cash 0.3%
Largest holdings: BlackRock Cash Funds Treasury SL Agency 0.5%, Twist Bioscience Corp 0.4%, Moog Inc Class A 0.4%, JFrog Ltd Ordinary Shares 0.4%, 10x Genomics Inc Ordinary Shares - Class A 0.4%
Sector mix: Healthcare 20.9%, Financial services 18.0%, Technology 14.5%, Industrials 13.3%
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
Rolled up from the 5 largest holdings, 2.0% of the fund by weight  -- thin, so read this as a fact about that slice rather than the fund
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 1.86 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +18.7% above the current prices
Holdings read: XTSLA, TWST, MOG-A, FROG, TXG
Recent rating changes among them:
  - TWST: 2026-10-13 TD Cowen: main, Buy -> Buy
  - MOG-A: 2026-10-13 JP Morgan: main, Overweight -> Overweight
  - FROG: 2026-10-21 Truist Securities: main, Buy -> Buy
  - TXG: 2026-10-13 TD Cowen: main, Hold -> Hold
```

</details>

<details><summary><b>Buying and selling by company insiders</b> — score -0.25</summary>

_Not available today._

</details>

<details><summary><b>Who is positioned how</b> — score -0.25</summary>

```text
Contract: RUSSELL E-MINI - CHICAGO MERCANTILE EXCHANGE (positions as of 2026-10-13, published the following Friday)
Large speculators: net short 20.6% of open interest (444,784 contracts)
Change on the week: +4.2% of open interest
Crowding: 22% percentile over 52 weeks -- within its normal range
Read this as crowding, not as a forecast: an extreme is as often the end of a move as the middle of one.
```

</details>

<details><summary><b>Money going into and out of this fund</b> — score -0.25</summary>

```text
Direction: flat (1 month)
Share count change: 1 week: +0.0% (0.00) over 7d | 1 month: +0.0% (0.00) over 30d
Shares outstanding: 281.05M | fund size: 77.36B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### US company bonds, safer (LQD) · Index fund — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Neutral overall; no macro surprise, technicals lack decisive break, and fund fundamentals are balanced. Bearish flow pressure is offset by stable fundamentals and modest technical support.

**Main reasons it gave:**
- U.S. 10-year Treasury yield fell below 5% for the first time in a month
- Fund flows show net outflows of -10.5% over the past month
- Price below 50‑day and 200‑day SMA, MACD negative, RSI neutral
- Fund yield 4.9% slightly below 10‑yr Treasury yield 4.99%

<details><summary><b>News</b> — score +0.00</summary>

- [U.S. 10-Year Treasury yield cracks below 5% for the first time in a month as bonds rally](https://seekingalpha.com/news/4656078-us-10-year-treasury-yield-cracks-below-5-for-the-first-time-in-a-a-month-as-bonds-rally)  
  <sub>Seeking Alpha, 22 hours ago</sub>  
  U.S. Treasury yields fell across the curve as bond buying pushed the 10-year below 5%.
- [‘The economics of AI cannot work as tech is deflationary’ – Praetorian Capital’s Q3 investor letter](https://seekingalpha.com/news/4656149-the-economics-of-ai-cannot-work-as-tech-is-deflationary-praetorian-capital-s-q3-investor)  
  <sub>Seeking Alpha, 20 hours ago</sub>  
  Harris Kupperman warns AI economics may be unsustainable, risking recession and market declines.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.04% (-0.03 on the week) | 5-year 4.81% (-0.09 on the week) | 10-year 4.99% (-0.11 on the week) | 30-year 5.31% (-0.12 on the week)
Yield curve, 10-year minus 3-month: +0.95 points -- upward sloping (normal)
US dollar index: 101.76 (-0.08 on the week)
Volatility (VIX): 20.36 (+0.4 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.2% (2026-09-01) | jobless claims 194k (2026-10-17)
Policy and expectations: Fed target 4.00% | market expects 2.3% inflation over 10 years
Rate path: 2-year Treasury 4.81% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 103.93 (bar of 2026-10-23), from 502 daily bars
Trend: vs 20d SMA 102.70 (+1.2%), 50d 104.27 (-0.3%), 200d 107.84 (-3.6%); 50d below 200d
Momentum: RSI(14) 55.9 | MACD -0.121 vs signal -0.406 (histogram 0.285)
Returns: 1d -0.3% | 5d +0.5% | 1m +0.8% | 3m -2.4%
52-week range: 101.83 - 112.92 (now 18.9% of the way up)
Volatility: ATR(14) 0.65 (0.6% of price) | annualised 20d 6.4%
Volume: 0.29x the 20-day average
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

<details><summary><b>Buying and selling by company insiders</b> — score -0.40</summary>

_Not available today._

</details>

<details><summary><b>Who is positioned how</b> — score -0.40</summary>

_Not available today._

</details>

<details><summary><b>Money going into and out of this fund</b> — score -0.40</summary>

```text
Direction: money going out (1 month)
Share count change: 1 week: -0.6% (-174.51M) over 7d | 1 month: -10.5% (-3.34B) over 30d
Shares outstanding: 274.15M | fund size: 28.49B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### S&P 500, equal weight (RSP) · Index fund — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:** no explanation. It wrote only “NEUTRAL”, so the main reasons below are all it gave.

**Main reasons it gave:**
- Large speculators net short 21.2% of open interest (CFTC) indicates bearish sentiment
- Fund flows show net outflows of -6.6% over the past month, indicating reduced demand
- Technicals show price above 20‑day, 50‑day and 200‑day SMAs but low volume, limiting bullish conviction
- Analyst coverage of top holdings is thin (1.4% of fund) with 78.5% buy rating, providing limited bullish signal
- Rotation out of AI stocks lifts equal‑weight S&P 500 ETF, offering short‑term upside

<details><summary><b>News</b> — score +0.00</summary>

- [The Average Stock Is Beating the S&P 500 by the Most Since April 2009: Is the Rotation Now Over?](https://www.benzinga.com/markets/equities/26/10/62556800/equal-weight-sp-500-rsp-spy-best-month-since-2009-rotation)  
  <sub>Benzinga, 2 hours ago</sub>  
  The equal-weight S&P 500 ETF (RSP) is beating SPY by the most since April 2009 as money exits AI stocks. Analysts weigh whether the rotation can last.
- [AI Names Crater, Average Stocks Rise in Dramatic Rotation](https://realmoney.thestreet.com/market-commentary/ai-names-crater-average-stocks-rise-in-dramatic-rotation)  
  <sub>TheStreet Pro, 18 hours ago</sub>  
  I've been discussing the two-tiered nature of this market and the gap in performance between AI-related names and the rest of the market for months now.
- [Investors' Recent Money Moves Show a Preference for Quality Over Momentum Within the S&P 500](https://www.moomoo.com/th/news/post/1002046262/investors-recent-money-moves-show-a-preference-for-quality-over)  
  <sub>Moomoo, 23 hours ago</sub>  
  ByPhilip van Doorn Investors have been steadily pouring money into the Invesco S&P 500 Quality ETF this year The AI buildout is not the only thing investors...
- [Bill Baruch market update: SMH & QQQ slide, RSP, WMT, LLY, AAPL rise, GLD pressured](https://www.theglobeandmail.com/investing/markets/indices/TTGD/pressreleases/8341118/bill-baruch-market-update-smh-qqq-slide-rsp-wmt-lly-aapl-rise-gld-pressured/)  
  <sub>The Globe and Mail, 17 hours ago</sub>  
  Ugly day led by $SMH $QQQ. On bright side $RSP $WMT $LLY $AAPL +. Also $GLD bludgeoned despite $TLT #USD central bank buying and great ETF flows.
- [The Semiconductor Selloff Could Be About To Get Much Worse](https://mottcapitalmanagement.com/the-ai-trade-faces-growing-downside-risks-as-semiconductor-stocks-approach-critical-support-the-kospi-weakens-asian-currencies-strengthen-and-investors-rotate-away-from-mega-cap-technology-stocks/)  
  <sub>Mott Capital Management, 16 hours ago</sub>  
  It looked like a rough day for stocks, with the S&P 500 down more than 1% and the Nasdaq down almost 3%. However, the RSP, the equal-weight S&P 500 ETF,...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.04% (-0.03 on the week) | 5-year 4.81% (-0.09 on the week) | 10-year 4.99% (-0.11 on the week) | 30-year 5.31% (-0.12 on the week)
Yield curve, 10-year minus 3-month: +0.95 points -- upward sloping (normal)
US dollar index: 101.76 (-0.08 on the week)
Volatility (VIX): 20.36 (+0.4 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.2% (2026-09-01) | jobless claims 194k (2026-10-17)
Policy and expectations: Fed target 4.00% | market expects 2.3% inflation over 10 years
Rate path: 2-year Treasury 4.81% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 216.63 (bar of 2026-10-23), from 502 daily bars
Trend: vs 20d SMA 212.67 (+1.9%), 50d 215.35 (+0.6%), 200d 207.27 (+4.5%); 50d above 200d
Momentum: RSI(14) 58.1 | MACD 0.764 vs signal -0.034 (histogram 0.799)
Returns: 1d -0.7% | 5d +1.2% | 1m +3.0% | 3m +0.7%
52-week range: 182.18 - 222.77 (now 84.9% of the way up)
Volatility: ATR(14) 2.05 (0.9% of price) | annualised 20d 10.3%
Volume: 0.34x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.20</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score +0.20</summary>

```text
Fund type: Large Blend
What it holds: P/E 20.26 | P/B 2.97 | P/S 1.87 | 3y earnings growth n/a
Yield: 1.5%
Three-year record: +18.4% a year | beta to the market 0.84
Cost and size: expense ratio 0.20% | net assets 96.06B
What it is made of: Stocks 99.9%, Cash 0.1%
Largest holdings: Moderna Inc 0.3%, Everpure Inc Class A 0.3%, Illumina Inc 0.3%, CrowdStrike Holdings Inc Class A 0.3%, Revvity Inc 0.3%
Sector mix: Technology 18.0%, Industrials 15.2%, Financial services 13.5%, Healthcare 12.6%
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
Rolled up from the 5 largest holdings, 1.4% of the fund by weight  -- thin, so read this as a fact about that slice rather than the fund
Ratings by weight: buy 78.5% | hold 21.5% | sell 0.0% (mean 2.20 on a 1=strong buy to 5=strong sell scale)
Weighted price target: -5.7% above the current prices
Holdings read: MRNA, P, ILMN, CRWD, RVTY
Recent rating changes among them:
  - MRNA: 2026-10-21 TD Cowen: main, Hold -> Hold
  - P: 2026-10-12 Guggenheim: main, Buy -> Buy
  - ILMN: 2026-10-19 Canaccord Genuity: main, Hold -> Hold
  - CRWD: 2026-10-22 Mizuho: main, Outperform -> Outperform
  - RVTY: 2026-10-13 TD Cowen: main, Buy -> Buy
```

</details>

<details><summary><b>Buying and selling by company insiders</b> — score -0.30</summary>

_Not available today._

</details>

<details><summary><b>Who is positioned how</b> — score -0.30</summary>

```text
Contract: E-MINI S&P 500 - CHICAGO MERCANTILE EXCHANGE (positions as of 2026-10-13, published the following Friday)
Large speculators: net short 21.2% of open interest (1,931,607 contracts)
Change on the week: +0.3% of open interest
Crowding: 35% percentile over 52 weeks -- within its normal range
Read this as crowding, not as a forecast: an extreme is as often the end of a move as the middle of one.
```

</details>

<details><summary><b>Money going into and out of this fund</b> — score -0.30</summary>

```text
Direction: money going out (1 month)
Share count change: 1 week: -1.5% (-1.46B) over 7d | 1 month: -6.6% (-6.83B) over 30d
Shares outstanding: 443.57M | fund size: 96.09B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### US government bonds, 1-3 years (SHY) · Index fund — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Neutral overall: modest bullish tilt from a slight reduction in net short positions, but fundamentals unchanged and macro move modest.

**Main reasons it gave:**
- 10-year Treasury yield fell 15 bps to 4.99% this week
- Large speculators net short 30% of open interest in 2-year note, down 2% week-over-week
- Fund basics unchanged: yield 3.6%, AA credit quality, 99.5% bonds
- Technicals: price 81.49, 20‑day SMA 81.22, RSI 60.7, MACD slightly positive

<details><summary><b>News</b> — score +0.00</summary>

- [META_TITLE_QUOTE](https://ca.finance.yahoo.com/quote/TLT/)  
  <sub>Yahoo! Finance Canada, 6 hours ago</sub>  
  The United States economy is full of innovation. It has to be. Manufacturing industries that dominated the economy decades ago - textiles, televisions,...
- [Treasury ETFs Soar as Tech Stocks Sell Off and 10-Year Yield Falls Below 5% — What's Fueling the Bond Rush?](https://www.benzinga.com/etfs/sector-etfs/26/10/62551919/treasury-etfs-soar-as-tech-stocks-sell-off-and-10-year-yield-falls-below-5-whats-fueling-the-bond-rush)  
  <sub>Benzinga, 7 hours ago</sub>  
  Long-term bond ETFs rally as Treasury yields fall below 5%, even as hot PPI keeps inflation and Fed policy in focus.
- [U.S. 10-Year Treasury yield cracks below 5% for the first time in a month as bonds rally](https://seekingalpha.com/news/4656078-us-10-year-treasury-yield-cracks-below-5-for-the-first-time-in-a-a-month-as-bonds-rally)  
  <sub>Seeking Alpha, 22 hours ago</sub>  
  U.S. Treasury yields fell across the curve as bond buying pushed the 10-year below 5%.
- [Nvidia's $35 Billion Order Book Fails to Calm AI Jitters Weighing on Vanguard's All-World Fund](https://www.ad-hoc-news.de/boerse/news/unternehmensnachrichten/nvidia-s-35-billion-order-book-fails-to-calm-ai-jitters-weighing-on-vanguard-s-all-world-fund/70398652)  
  <sub>AD HOC NEWS, 4 hours ago</sub>  
  Vanguard FTSE All-World ETF falls 0.2% to €168.94, 2.9% below its 52-week high, as AI spending doubts hit Nvidia and Meta while oil rises on Iran tensions.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.04% (-0.03 on the week) | 5-year 4.81% (-0.09 on the week) | 10-year 4.99% (-0.11 on the week) | 30-year 5.31% (-0.12 on the week)
Yield curve, 10-year minus 3-month: +0.95 points -- upward sloping (normal)
US dollar index: 101.76 (-0.08 on the week)
Volatility (VIX): 20.36 (+0.4 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.2% (2026-09-01) | jobless claims 194k (2026-10-17)
Policy and expectations: Fed target 4.00% | market expects 2.3% inflation over 10 years
Rate path: 2-year Treasury 4.81% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 81.49 (bar of 2026-10-23), from 502 daily bars
Trend: vs 20d SMA 81.22 (+0.3%), 50d 81.48 (+0.0%), 200d 82.14 (-0.8%); 50d below 200d
Momentum: RSI(14) 60.7 | MACD 0.004 vs signal -0.051 (histogram 0.055)
Returns: 1d -0.0% | 5d +0.2% | 1m +0.5% | 3m -0.5%
52-week range: 81.05 - 83.18 (now 20.8% of the way up)
Volatility: ATR(14) 0.12 (0.1% of price) | annualised 20d 1.5%
Volume: 0.13x the 20-day average
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

<details><summary><b>Buying and selling by company insiders</b> — score +0.00</summary>

_Not available today._

</details>

<details><summary><b>Who is positioned how</b> — score +0.00</summary>

```text
Contract: UST 2Y NOTE - CHICAGO BOARD OF TRADE (positions as of 2026-10-13, published the following Friday)
Large speculators: net short 30.0% of open interest (4,554,153 contracts)
Change on the week: -2.0% of open interest
Crowding: 87% percentile over 52 weeks -- within its normal range
Read this as crowding, not as a forecast: an extreme is as often the end of a move as the middle of one.
```

</details>

<details><summary><b>Money going into and out of this fund</b> — score +0.00</summary>

```text
Direction: money coming in (1 month)
Share count change: 1 week: -0.1% (-28.70M) over 7d | 1 month: +1.4% (353.52M) over 30d
Shares outstanding: 323.37M | fund size: 26.35B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### US inflation-linked bonds (TIP) · Index fund — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> No material macro surprise, no decisive technical break, and mixed signals from positioning and flows lead to a neutral stance.

**Main reasons it gave:**
- Yields fell modestly across the curve this week, supporting bond prices but no surprise
- Large speculators remain net short 10‑yr Treasuries, with a negligible -0.6% change, indicating no new directional pressure
- Fund flows show modest outflows (-5.4% month) but not enough to outweigh other signals
- Technical indicators are mixed: price near low of 52‑week range with modest bullish momentum (RSI 65, MACD positive) yet still below 200‑day SMA

<details><summary><b>News</b> — score +0.00</summary>

- [TIP Lost $36,720 on $300,000 in 2022, the Year It Was Built For](https://247wallst.com/investing/etf/2026/10/22/tip-lost-36720-on-300000-in-2022-the-year-it-was-built-for/)  
  <sub>24/7 Wall St., 19 hours ago</sub>  
  A retiree who put $300000 into an inflation-protection fund during the worst inflation spike in decades watched the position shrink, not grow.
- [Better Forecasting Starts With Admitting You’re Wrong](https://etfdb.com/active-etf-content-hub/better-forecasting-starts-with-admitting-you-re-wrong/)  
  <sub>ETF Database, 20 hours ago</sub>  
  Author Dan Gardner says strong forecasting rests on humility, base rates and small, steady updates, habits investors can learn with practice.
- [Inflation-protected ETF TIP lost $36,720 in 202...](https://pluang.com/en/news-feed/etf-tip-rugi-36720-dolar-2022-tahun-inflasi-tinggi)  
  <sub>Pluang, 18 hours ago</sub>  
  In 2022, the iShares TIPS Bond ETF (TIP), designed to protect against inflation, lost $36720 on a $300000 investment due to rising interest rates that...
- [These 3 ETFs Have 15%+ Upside Potential, Says the AI Analyst](https://www.tipranks.com/news/these-3-etfs-have-15-upside-potential-says-the-ai-analyst)  
  <sub>TipRanks, 16 hours ago</sub>  
  TipRanks' ETF AI Analyst sees more than 15% upside in VanEck Semiconductor ETF ($SMH), iShares U.S. Technology ETF ($IYW), and State Street SPDR Portfolio...
- [Bitcoin Bulls Tap the Brakes as Leveraged BTCU ETF Sees Double-Digit Outflow](https://www.tipranks.com/news/cryptocurrencies/bitcoin-bulls-tap-the-brakes-as-leveraged-btcu-etf-sees-double-digit-outflow)  
  <sub>TipRanks, 13 hours ago</sub>  
  Bitcoin bulls blink as Direxion Daily Bitcoin Bull 2X ETF's BTCU records a sharp outflow of $668548 on September 04, 2026, slicing roughly 14.3% off its...
- [SOFA Stock Latest News](https://www.tipranks.com/news/topic/sofa)  
  <sub>TipRanks, 4 hours ago</sub>  
  Find the latest SOFA stock news. View the Direxion Daily SOFI Bull 2X ETF news and quotes for today, invesment news based on TipRanks market-leading...
- [Stock Market Volatility Is Back – 3 Best Vanguard ETFs Worth Owning Right Now](https://www.tipranks.com/news/3-best-vanguard-etfs-to-weather-the-market-volatility)  
  <sub>TipRanks, 18 hours ago</sub>  
  When Wall Street gets nervous, finding the right investments can become a real challenge. Concerns about elevated stock valuations, uncertainty surrounding...
- [Ethereum ETF Outflow Signals Traders Taking Profits After Double-Digit Rally](https://www.tipranks.com/news/cryptocurrencies/ethereum-etf-outflow-signals-traders-taking-profits-after-double-digit-rally)  
  <sub>TipRanks, 16 hours ago</sub>  
  Ethereum ETF Sees Sudden Outflow as Traders Lock In Gains iShares Ethereum Trust ETF, ETHA, recorded a sharp outflow of $33.0 million on October 21, 2026,...
- [Bitcoin ETF Giant Draws Fresh Inflows as Rally Accelerates](https://www.tipranks.com/news/cryptocurrencies/bitcoin-etf-giant-draws-fresh-inflows-as-rally-accelerates)  
  <sub>TipRanks, 17 hours ago</sub>  
  Bitcoin ETF Giant Draws Fresh Inflows as Rally Accelerates IShares Bitcoin Trust Registered's IBIT logged fresh inflows of $29.9 million on October 21,...
- [TSE:GLCC Stock Latest News](https://www.tipranks.com/news/topic/tseglcc)  
  <sub>TipRanks, 8 hours ago</sub>  
  PremiumMarket NewsGLCC, NFAM: 2 Canadian ETFs with Strong Upside Potential, According to Analysts. 2y ago. Trending. Indices. Stocks. ETFs. Name. Price.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.04% (-0.03 on the week) | 5-year 4.81% (-0.09 on the week) | 10-year 4.99% (-0.11 on the week) | 30-year 5.31% (-0.12 on the week)
Yield curve, 10-year minus 3-month: +0.95 points -- upward sloping (normal)
US dollar index: 101.76 (-0.08 on the week)
Volatility (VIX): 20.36 (+0.4 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.2% (2026-09-01) | jobless claims 194k (2026-10-17)
Policy and expectations: Fed target 4.00% | market expects 2.3% inflation over 10 years
Rate path: 2-year Treasury 4.81% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 106.28 (bar of 2026-10-23), from 502 daily bars
Trend: vs 20d SMA 104.78 (+1.4%), 50d 105.77 (+0.5%), 200d 108.95 (-2.5%); 50d below 200d
Momentum: RSI(14) 65.4 | MACD 0.114 vs signal -0.167 (histogram 0.281)
Returns: 1d -0.0% | 5d +0.7% | 1m +1.9% | 3m -1.0%
52-week range: 103.98 - 112.03 (now 28.6% of the way up)
Volatility: ATR(14) 0.41 (0.4% of price) | annualised 20d 4.1%
Volume: 0.29x the 20-day average
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
Direction: money going out (1 month)
Share count change: 1 week: -0.9% (-136.15M) over 7d | 1 month: -5.4% (-817.64M) over 30d
Shares outstanding: 134.91M | fund size: 14.34B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### US government bonds, 20+ years (TLT) · Index fund — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Neutral stance as no material policy surprise, data shock, or decisive technical break is present. Mixed signals from macro, positioning, and technicals offset each other.

**Main reasons it gave:**
- 10-year Treasury yield fell 0.11% on the week, supporting bond prices
- Large speculators net short 29.8% of open interest, indicating bearish sentiment
- RSI 63.9 and MACD positive show modest bullish momentum, but price remains below 200‑day SMA
- Fund flows flat over the past month, indicating no net demand shift

<details><summary><b>News</b> — score +0.00</summary>

- [META_TITLE_QUOTE](https://ca.finance.yahoo.com/quote/TLT/)  
  <sub>Yahoo! Finance Canada, 6 hours ago</sub>  
  iShares 20+ Year Treasury Bond ETF (TLT) · 2.21% · -0.01% · -5.76% · -6.97% · -11.21% · -43.29% · -0.01%.
- [The 10-Year Yield Just Fell Below 5% as Investors Fled AI Stocks](https://247wallst.com/investing/2026/10/23/the-10-year-yield-just-fell-below-5-as-investors-fled-ai-stocks/)  
  <sub>24/7 Wall St., 4 hours ago</sub>  
  AI stocks cracked on Thursday and spooked investors sent billions pouring into Treasuries, but the bond rally now faces a Fed meeting, a fresh inflation...
- [US Treasury bonds on track for biggest rally since February](https://protos.com/us-treasury-bonds-on-track-for-biggest-rally-since-february/)  
  <sub>Protos | Informed crypto news, 21 hours ago</sub>  
  As oil prices, military conflicts, and inflation weigh down on the world's economies, owners of US Treasury bonds are benefitting from capital flight to...
- [Treasury ETFs Soar as Tech Stocks Sell Off and 10-Year Yield Falls Below 5% — What's Fueling the Bond Rush?](https://www.benzinga.com/etfs/sector-etfs/26/10/62551919/treasury-etfs-soar-as-tech-stocks-sell-off-and-10-year-yield-falls-below-5-whats-fueling-the-bond-rush)  
  <sub>Benzinga, 7 hours ago</sub>  
  Long-term bond ETFs rally as Treasury yields fall below 5%, even as hot PPI keeps inflation and Fed policy in focus.
- [TLT 261021 90.00P (TLT261021P90000) Stock Options Chain | Quotes & News](https://www.moomoo.com/options/TLT261021P90000-US?search_track_info=)  
  <sub>Moomoo, 24 hours ago</sub>  
  Track real-time TLT 261021 90.00P (TLT261021P90000) stock options chain data and pricing information and news on moomoo App for your options trading and...
- [Rob Kaplan Sees Fed Hike Likely In December — Warns Aggressive Tightening May Hurt Jobs Without Taming Inflation](https://es.tradingview.com/news/stocktwits:71131d490094b:0-rob-kaplan-sees-fed-hike-likely-in-december-warns-aggressive-tightening-may-hurt-jobs-without-taming-inflation/)  
  <sub>TradingView, 24 hours ago</sub>  
  Goldman Sachs Vice Chairman Rob Kaplan said Thursday that the Federal Reserve will likely raise interest rates in December but warned that aggressive...
- [Chart Of The Day: The First 'Recession Trade' Day In A Long Time](https://seekingalpha.com/article/4956907-chart-of-day-first-recession-trade-day-in-a-long-time)  
  <sub>Seeking Alpha, 2 hours ago</sub>  
  The MoneyShow Chart of the Day shows the intraday move through late afternoon on Thursday for several ETFs, including defensive sector funds like the State...
- [Nasdaq Futures Rise After Chip Selloff While S&P 500, Dow Track Mixed Open: SLV, GLD, SOXL, BE In Focus](https://stocktwits.com/news-articles/markets/equity/nasdaq-futures-rise-after-chip-selloff-while-s-and-p-500-dow-track-mixed-open-slv-gld-soxl-be-in-focus/cZxyG6qRBDq)  
  <sub>Stocktwits, 7 hours ago</sub>  
  Semiconductor stocks were in focus on Thursday as the sector fell sharply after LAM Research CEO Tim Archer cited supply chain concerns.
- [Flow Focus | Tech Falls Behind. Is Old-School Wall Street Back?](https://www.moomoo.com/community/feed/flow-focus-tech-falls-behind-is-old-school-wall-street-117489058250758)  
  <sub>Moomoo, 7 hours ago</sub>  
  The $Dow Jones Industrial Average (.DJI.US)$ held its ground while tech sold off. In the supplied weekly snapshot, industrials, regional banks and bio...
- [Bill Baruch market update: SMH & QQQ slide, RSP, WMT, LLY, AAPL rise, GLD pressured](https://www.theglobeandmail.com/investing/markets/indices/TTGD/pressreleases/8341118/bill-baruch-market-update-smh-qqq-slide-rsp-wmt-lly-aapl-rise-gld-pressured/)  
  <sub>The Globe and Mail, 17 hours ago</sub>  
  Ugly day led by $SMH $QQQ. On bright side $RSP $WMT $LLY $AAPL +. Also $GLD bludgeoned despite $TLT #USD central bank buying and great ETF flows.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.04% (-0.03 on the week) | 5-year 4.81% (-0.09 on the week) | 10-year 4.99% (-0.11 on the week) | 30-year 5.31% (-0.12 on the week)
Yield curve, 10-year minus 3-month: +0.95 points -- upward sloping (normal)
US dollar index: 101.76 (-0.08 on the week)
Volatility (VIX): 20.36 (+0.4 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.2% (2026-09-01) | jobless claims 194k (2026-10-17)
Policy and expectations: Fed target 4.00% | market expects 2.3% inflation over 10 years
Rate path: 2-year Treasury 4.81% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 81.49 (bar of 2026-10-23), from 502 daily bars
Trend: vs 20d SMA 78.78 (+3.4%), 50d 80.56 (+1.2%), 200d 84.78 (-3.9%); 50d below 200d
Momentum: RSI(14) 63.9 | MACD 0.163 vs signal -0.349 (histogram 0.512)
Returns: 1d -0.3% | 5d +1.8% | 1m +2.6% | 3m -2.7%
52-week range: 77.11 - 92.02 (now 29.4% of the way up)
Volatility: ATR(14) 0.84 (1.0% of price) | annualised 20d 11.3%
Volume: 0.21x the 20-day average
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
Three-year record: +3.1% a year | beta to the market 2.31
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

<details><summary><b>Buying and selling by company insiders</b> — score -0.20</summary>

_Not available today._

</details>

<details><summary><b>Who is positioned how</b> — score -0.20</summary>

```text
Contract: ULTRA UST BOND - CHICAGO BOARD OF TRADE (positions as of 2026-10-13, published the following Friday)
Large speculators: net short 29.8% of open interest (2,397,995 contracts)
Change on the week: +0.4% of open interest
Crowding: 87% percentile over 52 weeks -- within its normal range
Read this as crowding, not as a forecast: an extreme is as often the end of a move as the middle of one.
```

</details>

<details><summary><b>Money going into and out of this fund</b> — score -0.20</summary>

```text
Direction: flat (1 month)
Share count change: 1 week: +0.0% (0.00) over 7d | 1 month: +0.0% (0.00) over 30d
Shares outstanding: 109.70M | fund size: 8.94B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### US dollar (UUP) · Index fund — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Neutral overall; no macro surprise, no decisive technical break, modest positioning tilt, no analyst rating, stable fundamentals.

**Main reasons it gave:**
- US dollar index down 0.08% on the week (no bullish catalyst)
- Price near 52‑week high (92.5% of range) with RSI 56.6 and low volume (no decisive technical break)
- CFTC positioning: net long 4% of open interest, +2.3% weekly change (small bullish tilt)
- Analyst view provides no rating (neutral)
- Fund flows: share count up 41.5% over 1 month (strong inflows but no price catalyst)

<details><summary><b>News</b> — score +0.00</summary>

- [Invesco DB Dollar Index Fund Appoints New Finance Officer](https://www.theglobeandmail.com/investing/markets/stocks/UUP-A/pressreleases/8341449/invesco-db-dollar-index-fund-appoints-new-finance-officer/)  
  <sub>The Globe and Mail, 17 hours ago</sub>  
  Detailed price information for Invesco DB USD Index Bullish Fund ETF (UUP-A) from The Globe and Mail including charting and trades.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.04% (-0.03 on the week) | 5-year 4.81% (-0.09 on the week) | 10-year 4.99% (-0.11 on the week) | 30-year 5.31% (-0.12 on the week)
Yield curve, 10-year minus 3-month: +0.95 points -- upward sloping (normal)
US dollar index: 101.76 (-0.08 on the week)
Volatility (VIX): 20.36 (+0.4 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.2% (2026-09-01) | jobless claims 194k (2026-10-17)
Policy and expectations: Fed target 4.00% | market expects 2.3% inflation over 10 years
Rate path: 2-year Treasury 4.81% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 28.93 (bar of 2026-10-23), from 502 daily bars
Trend: vs 20d SMA 28.94 (-0.0%), 50d 28.48 (+1.6%), 200d 27.88 (+3.8%); 50d above 200d
Momentum: RSI(14) 56.6 | MACD 0.121 vs signal 0.159 (histogram -0.039)
Returns: 1d +0.1% | 5d +0.0% | 1m +0.8% | 3m +1.2%
52-week range: 26.47 - 29.13 (now 92.5% of the way up)
Volatility: ATR(14) 0.12 (0.4% of price) | annualised 20d 5.1%
Volume: 0.13x the 20-day average
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
Three-year record: +3.7% a year | beta to the market -11.39
Cost and size: expense ratio 0.75% | net assets 431.14M
What it is made of: Cash 100.0%
Largest holdings: Invesco Shrt-Trm Inv Gov&Agcy Instl 49.4%
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
Share count change: 1 week: +0.3% (1.19M) over 7d | 1 month: +41.5% (126.49M) over 30d
Shares outstanding: 14.90M | fund size: 430.99M
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Europe (VGK) · Index fund — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> No macro surprise; yields down modestly, VIX elevated, outflows; mixed technicals; thin analyst coverage but bullish price target; slight shift in CFTC positioning toward net long.

**Main reasons it gave:**
- Analyst coverage thin (12.1% of fund) but price target +20.4% bullish
- CFTC positioning net short 0.3% with -0.4% change (slight shift to net long)
- Fund outflows: -4.1% share count over 1 month (bearish sentiment)
- Macro: yields down modestly, VIX 20.36 elevated, no data surprise

<details><summary><b>News</b> — score +0.00</summary>

- [Weight Loss Drugs Create a Problem. Beauty Companies See a Market. Where’s the Proof?](https://www.moomoo.com/community/feed/weight-loss-drugs-create-a-problem-beauty-companies-see-a-117485212270598?chain_id=Name1K9-3FXPhg.1ldk97g&global_content=%7B%22promote_id%22%3A13764%2C%22sub_promote_id%22%3A107%2C%22f%22%3A%22www.moomoo.com%2Fetfs%2FIVV-AU%22%7D)  
  <sub>Moomoo, 24 hours ago</sub>  
  Swiss skincare firm Galderma, Brazilian group Natura, and L'Oreal are testing treatments for consumers worried about facial sagging and volume loss,...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.04% (-0.03 on the week) | 5-year 4.81% (-0.09 on the week) | 10-year 4.99% (-0.11 on the week) | 30-year 5.31% (-0.12 on the week)
Yield curve, 10-year minus 3-month: +0.95 points -- upward sloping (normal)
US dollar index: 101.76 (-0.08 on the week)
Volatility (VIX): 20.36 (+0.4 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.2% (2026-09-01) | jobless claims 194k (2026-10-17)
Policy and expectations: Fed target 4.00% | market expects 2.3% inflation over 10 years
Rate path: 2-year Treasury 4.81% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 86.11 (bar of 2026-10-23), from 502 daily bars
Trend: vs 20d SMA 86.57 (-0.5%), 50d 89.05 (-3.3%), 200d 87.83 (-2.0%); 50d above 200d
Momentum: RSI(14) 42.1 | MACD -0.554 vs signal -0.743 (histogram 0.190)
Returns: 1d -0.8% | 5d -1.4% | 1m -2.2% | 3m -3.1%
52-week range: 77.90 - 93.19 (now 53.7% of the way up)
Volatility: ATR(14) 0.92 (1.1% of price) | annualised 20d 13.0%
Volume: 0.15x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.20</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score +0.20</summary>

```text
Fund type: Europe Stock
What it holds: P/E 17.26 | P/B 2.24 | P/S 1.59 | 3y earnings growth n/a
Yield: 3.0%
Three-year record: +19.8% a year | beta to the market 0.90
Cost and size: expense ratio 0.06% | net assets 37.17B
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
Ratings by weight: buy 67.6% | hold 32.4% | sell 0.0% (mean 2.03 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +20.4% above the current prices
Holdings read: ASML.AS, HSBA.L, ROP.SW, SHEL.L, NOVN.SW
Recent rating changes among them: none reported
```

</details>

<details><summary><b>Buying and selling by company insiders</b> — score +0.10</summary>

_Not available today._

</details>

<details><summary><b>Who is positioned how</b> — score +0.10</summary>

```text
Contract: MSCI EAFE  - ICE FUTURES U.S. (positions as of 2026-10-13, published the following Friday)
Large speculators: net short 0.3% of open interest (480,891 contracts)
Change on the week: -0.4% of open interest
Crowding: 65% percentile over 52 weeks -- within its normal range
Read this as crowding, not as a forecast: an extreme is as often the end of a move as the middle of one.
```

</details>

<details><summary><b>Money going into and out of this fund</b> — score +0.10</summary>

```text
Direction: money going out (1 month)
Share count change: 1 week: -1.6% (-591.94M) over 7d | 1 month: -4.1% (-1.55B) over 30d
Shares outstanding: 423.82M | fund size: 36.49B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Emerging markets (VWO) · Index fund — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Neutral stance as no macro surprise, mixed technicals, thin analyst coverage, and slight bearish shift in speculator positioning.

**Main reasons it gave:**
- Analyst coverage thin (23.5% weight) despite 100% buy rating and +50% price target
- CFTC speculators reduced net long by 1.5% week-over-week, indicating slight bearish shift
- Technical indicators: RSI 29.6 (oversold) but price below 20‑day, 50‑day, 200‑day SMAs and MACD negative
- No macro surprise: yields unchanged, inflation 3.7% near target, VIX modestly elevated

<details><summary><b>News</b> — score +0.00</summary>

_No news found for this one today._

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.04% (-0.03 on the week) | 5-year 4.81% (-0.09 on the week) | 10-year 4.99% (-0.11 on the week) | 30-year 5.31% (-0.12 on the week)
Yield curve, 10-year minus 3-month: +0.95 points -- upward sloping (normal)
US dollar index: 101.76 (-0.08 on the week)
Volatility (VIX): 20.36 (+0.4 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.2% (2026-09-01) | jobless claims 194k (2026-10-17)
Policy and expectations: Fed target 4.00% | market expects 2.3% inflation over 10 years
Rate path: 2-year Treasury 4.81% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 56.81 (bar of 2026-10-23), from 502 daily bars
Trend: vs 20d SMA 59.02 (-3.7%), 50d 59.82 (-5.0%), 200d 58.32 (-2.6%); 50d above 200d
Momentum: RSI(14) 29.6 | MACD -0.700 vs signal -0.438 (histogram -0.261)
Returns: 1d -0.1% | 5d -2.1% | 1m -5.1% | 3m -2.4%
52-week range: 52.42 - 61.44 (now 48.7% of the way up)
Volatility: ATR(14) 0.65 (1.1% of price) | annualised 20d 14.9%
Volume: 0.25x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.30</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score +0.30</summary>

```text
Fund type: Diversified Emerging Mkts
What it holds: P/E 16.13 | P/B 2.13 | P/S 1.85 | 3y earnings growth n/a
Yield: 2.0%
Three-year record: +18.6% a year | beta to the market 0.75
Cost and size: expense ratio 0.06% | net assets 164.66B
What it is made of: Stocks 95.8%, Cash 4.0%, Other 0.1%, Preferred 0.0%
Largest holdings: Taiwan Semiconductor Manufacturing Co Ltd 15.7%, Tencent Holdings Ltd 2.8%, Alibaba Group Holding Ltd Ordinary Shares 2.1%, MediaTek Inc 1.9%, Delta Electronics Inc 0.9%
Sector mix: Technology 33.8%, Financial services 19.5%, Consumer cyclical 9.3%, Industrials 7.5%
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

<details><summary><b>What analysts and big funds say</b> — score +0.35</summary>

_Not available today._

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score +0.35</summary>

```text
Rolled up from the 5 largest holdings, 23.5% of the fund by weight  -- thin, so read this as a fact about that slice rather than the fund
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 1.33 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +50.2% above the current prices
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
Share count change: 1 week: +0.0% (0.00) over 7d | 1 month: +0.0% (0.00) over 30d
Shares outstanding: 1.42B | fund size: 80.57B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### US company bonds, riskier (HYG) · Index fund — no answer, no confidence given

<details><summary><b>News</b> — score n/a</summary>

- [Ishares Iboxx $ High Yield Corporate Bond Etf Options Spot-On: On October 22nd, 497.2K Contracts Were Traded, With 9.7 Million Open Interest](https://news.futunn.com/en/post/1002007788/ishares-iboxx-high-yield-corporate-bond-etf-options-spot-on)  
  <sub>富途牛牛, 13 hours ago</sub>  
  OnOctober 22nd ET, $Ishares Iboxx $ High Yield Corporate Bond Etf(HYG.US)$ had active options trading, with a total trading volume of 497.2K options for the...
- [(HYG) Price Dynamics and Execution-Aware Positioning](https://news.stocktradersdaily.com/news_release/24/HYG_Price_Dynamics_and_Execution-Aware_Positioning_102226073402_1792712042.html)  
  <sub>Stock Traders Daily, 19 hours ago</sub>  
  Price-action only: Ishares Iboxx Usd High Yield Corporate Bond Etf (HYG) movements set the tone for institutional models. (HYG) Price Dynamics and...
- [EHI: High Yield And Deep Discount Aren't Enough (NYSE:EHI)](https://seekingalpha.com/article/4956623-ehi-high-yield-and-deep-discount-arent-enough)  
  <sub>Seeking Alpha, 19 hours ago</sub>  
  Western Asset Global High Income Fund trades at a deep discount with a 15% yield, but rate and leverage risks loom. Read the full CEF analysis here.
- [iShares Preferred and Income Securities ETF (PFF) Stock Price, News, Quote & History](https://ca.finance.yahoo.com/quote/PFF/)  
  <sub>Yahoo! Finance Canada, 18 hours ago</sub>  
  Find the latest iShares Preferred and Income Securities ETF (PFF) stock quote, history, news and other vital information to help you with your stock trading...
- [Illusion Of Undervaluation: DSU’s Negative Z-Score May Mislead Investors](https://seekingalpha.com/article/4956818-illusion-of-undervaluation-dsu-negative-z-score-may-mislead-investors)  
  <sub>Seeking Alpha, 5 hours ago</sub>  
  BlackRock Debt Strategies Fund offers a 13.7% yield, driven by a portfolio concentrated in floating-rate senior loans and a short duration profile.
- [U.S. 10-Year Treasury yield cracks below 5% for the first time in a month as bonds rally](https://seekingalpha.com/news/4656078-us-10-year-treasury-yield-cracks-below-5-for-the-first-time-in-a-a-month-as-bonds-rally)  
  <sub>Seeking Alpha, 22 hours ago</sub>  
  U.S. Treasury yields fell across the curve as bond buying pushed the 10-year below 5%.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score n/a</summary>

```text
US Treasury yields: 3-month 4.04% (-0.03 on the week) | 5-year 4.81% (-0.09 on the week) | 10-year 4.99% (-0.11 on the week) | 30-year 5.31% (-0.12 on the week)
Yield curve, 10-year minus 3-month: +0.95 points -- upward sloping (normal)
US dollar index: 101.76 (-0.08 on the week)
Volatility (VIX): 20.36 (+0.4 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.2% (2026-09-01) | jobless claims 194k (2026-10-17)
Policy and expectations: Fed target 4.00% | market expects 2.3% inflation over 10 years
Rate path: 2-year Treasury 4.81% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score n/a</summary>

```text
Last close 76.92 (bar of 2026-10-23), from 502 daily bars
Trend: vs 20d SMA 77.08 (-0.2%), 50d 78.28 (-1.7%), 200d 79.61 (-3.4%); 50d below 200d
Momentum: RSI(14) 36.8 | MACD -0.366 vs signal -0.429 (histogram 0.063)
Returns: 1d -0.2% | 5d +0.1% | 1m -1.3% | 3m -3.0%
52-week range: 76.81 - 81.28 (now 2.3% of the way up)
Volatility: ATR(14) 0.30 (0.4% of price) | annualised 20d 3.9%
Volume: 0.23x the 20-day average
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
Direction: money coming in (1 month)
Share count change: 1 week: +0.1% (19.21M) over 7d | 1 month: +5.8% (915.21M) over 30d
Shares outstanding: 218.29M | fund size: 16.79B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

## Sector and country funds

### Argentina (ARGT) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Neutral stance as no macro surprise, technicals weak but not decisive, net outflows, and bullish analyst view not enough to outweigh other factors.

**Main reasons it gave:**
- Analyst coverage of top 5 holdings (49.4% weight) is 100% buy with +32.8% price target
- Fund flows: net outflows of 7% over the past month
- Technicals: price below 20‑day, 50‑day, 200‑day SMAs; RSI 38.2; volume 0.32× 20‑day average
- Macro: Treasury yields down slightly; VIX up 0.4 points; no major data surprise
- Fundamentals: P/E 13.9, P/B 1.57, 3‑yr return +31.6% per year, beta 0.45

<details><summary><b>News</b> — score +0.00</summary>

_No news found for this one today._

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.04% (-0.03 on the week) | 5-year 4.81% (-0.09 on the week) | 10-year 4.99% (-0.11 on the week) | 30-year 5.31% (-0.12 on the week)
Yield curve, 10-year minus 3-month: +0.95 points -- upward sloping (normal)
US dollar index: 101.76 (-0.08 on the week)
Volatility (VIX): 20.36 (+0.4 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.2% (2026-09-01) | jobless claims 194k (2026-10-17)
Policy and expectations: Fed target 4.00% | market expects 2.3% inflation over 10 years
Rate path: 2-year Treasury 4.81% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score -0.20</summary>

```text
Last close 85.93 (bar of 2026-10-23), from 502 daily bars
Trend: vs 20d SMA 87.27 (-1.5%), 50d 91.12 (-5.7%), 200d 92.29 (-6.9%); 50d below 200d
Momentum: RSI(14) 38.2 | MACD -1.266 vs signal -1.280 (histogram 0.014)
Returns: 1d +0.2% | 5d -2.4% | 1m -4.1% | 3m -8.2%
52-week range: 73.88 - 102.94 (now 41.5% of the way up)
Volatility: ATR(14) 1.74 (2.0% of price) | annualised 20d 28.4%
Volume: 0.32x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.30</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score +0.30</summary>

```text
Fund type: Focused Region
What it holds: P/E 13.92 | P/B 1.57 | P/S 1.21 | 3y earnings growth n/a
Yield: 1.2%
Three-year record: +31.6% a year | beta to the market 0.45
Cost and size: expense ratio 0.59% | net assets 718.85M
What it is made of: Stocks 99.9%, Cash 0.1%
Largest holdings: MercadoLibre Inc 21.7%, YPF SA ADR 10.4%, Vista Energy SAB de CV ADR 7.0%, Grupo Financiero Galicia SA ADR 5.7%, Pampa Energia SA ADR 4.7%
Sector mix: Consumer cyclical 27.8%, Energy 21.2%, Financial services 14.2%, Basic materials 11.8%
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
Rolled up from the 5 largest holdings, 49.4% of the fund by weight
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 1.66 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +32.8% above the current prices
Holdings read: MELI, YPF, VIST, GGAL, PAM
Recent rating changes among them:
  - MELI: 2026-10-13 Citigroup: main, Neutral -> Neutral
  - YPF: 2026-09-01 JP Morgan: main, Overweight -> Overweight
  - VIST: 2026-09-01 JP Morgan: main, Overweight -> Overweight
  - GGAL: 2026-10-13 UBS: main, Neutral -> Neutral
  - PAM: 2026-09-01 JP Morgan: main, Neutral -> Neutral
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
Share count change: 1 week: +1.2% (8.26M) over 7d | 1 month: -7.0% (-52.84M) over 30d
Shares outstanding: 8.20M | fund size: 704.58M
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Poland (EPOL) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Neutral overall: analyst view is bullish, but fund outflows and bearish technicals offset the positive fundamentals and macro backdrop.

**Main reasons it gave:**
- Analyst consensus: 100% buy with +4.9% price target
- Fund flows: net outflows of -2.9% over past month
- Technical indicators: price below 20‑day and 50‑day SMAs, MACD negative
- Macro: yields down slightly, no surprise data releases

<details><summary><b>News</b> — score +0.00</summary>

_No news found for this one today._

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.04% (-0.03 on the week) | 5-year 4.81% (-0.09 on the week) | 10-year 4.99% (-0.11 on the week) | 30-year 5.31% (-0.12 on the week)
Yield curve, 10-year minus 3-month: +0.95 points -- upward sloping (normal)
US dollar index: 101.76 (-0.08 on the week)
Volatility (VIX): 20.36 (+0.4 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.2% (2026-09-01) | jobless claims 194k (2026-10-17)
Policy and expectations: Fed target 4.00% | market expects 2.3% inflation over 10 years
Rate path: 2-year Treasury 4.81% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score -0.20</summary>

```text
Last close 43.49 (bar of 2026-10-23), from 502 daily bars
Trend: vs 20d SMA 44.04 (-1.3%), 50d 44.39 (-2.0%), 200d 40.18 (+8.2%); 50d above 200d
Momentum: RSI(14) 44.5 | MACD -0.035 vs signal -0.024 (histogram -0.011)
Returns: 1d -1.4% | 5d -2.4% | 1m -2.8% | 3m +5.9%
52-week range: 32.56 - 45.76 (now 82.8% of the way up)
Volatility: ATR(14) 0.70 (1.6% of price) | annualised 20d 21.2%
Volume: 0.32x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.00</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score +0.00</summary>

```text
Fund type: Focused Region
What it holds: P/E 13.22 | P/B 2.06 | P/S 1.40 | 3y earnings growth n/a
Yield: 3.3%
Three-year record: +40.7% a year | beta to the market 0.64
Cost and size: expense ratio 0.59% | net assets 833.96M
What it is made of: Stocks 99.1%, Cash 0.9%
Largest holdings: PKO Bank Polski SA 16.2%, Orlen SA 12.7%, Bank Polska Kasa Opieki SA 7.4%, Powszechny Zaklad Ubezpieczen SA 6.0%, Allegro.EU SA Ordinary Shares 4.9%
Sector mix: Financial services 46.9%, Energy 13.3%, Consumer cyclical 13.2%, Basic materials 6.2%
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
Rolled up from the 5 largest holdings, 47.1% of the fund by weight
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 2.18 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +4.9% above the current prices
Holdings read: PKO.WA, PKN.WA, PEO.WA, PZU.WA, ALE.WA
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
Share count change: 1 week: -1.4% (-11.25M) over 7d | 1 month: -2.9% (-23.94M) over 30d
Shares outstanding: 18.53M | fund size: 805.99M
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Australia (EWA) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Neutral overall as no macro catalyst or decisive technical break; mixed signals from analyst view (negative), fund outflows (negative) and fundamentals/technicals (positive).

**Main reasons it gave:**
- Fund flows: -10.2% share count over 1 month
- Analyst view: weighted price target -6.6% below current price
- Technicals: price above 20-day SMA (+1.6%) and MACD positive
- Fundamentals: P/E 20.31 and three-year record +16.2% per year

<details><summary><b>News</b> — score +0.00</summary>

_No news found for this one today._

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.04% (-0.03 on the week) | 5-year 4.81% (-0.09 on the week) | 10-year 4.99% (-0.11 on the week) | 30-year 5.31% (-0.12 on the week)
Yield curve, 10-year minus 3-month: +0.95 points -- upward sloping (normal)
US dollar index: 101.76 (-0.08 on the week)
Volatility (VIX): 20.36 (+0.4 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.2% (2026-09-01) | jobless claims 194k (2026-10-17)
Policy and expectations: Fed target 4.00% | market expects 2.3% inflation over 10 years
Rate path: 2-year Treasury 4.81% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 29.06 (bar of 2026-10-23), from 502 daily bars
Trend: vs 20d SMA 28.62 (+1.6%), 50d 29.15 (-0.3%), 200d 28.82 (+0.8%); 50d above 200d
Momentum: RSI(14) 54.4 | MACD 0.025 vs signal -0.080 (histogram 0.104)
Returns: 1d +0.3% | 5d +1.1% | 1m +2.6% | 3m +0.6%
52-week range: 24.95 - 30.43 (now 75.0% of the way up)
Volatility: ATR(14) 0.31 (1.1% of price) | annualised 20d 11.7%
Volume: 0.21x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.35</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score +0.35</summary>

```text
Fund type: Focused Region
What it holds: P/E 20.31 | P/B 2.65 | P/S 3.31 | 3y earnings growth n/a
Yield: 3.0%
Three-year record: +16.2% a year | beta to the market 0.98
Cost and size: expense ratio 0.50% | net assets 1.21B
What it is made of: Stocks 99.2%, Cash 0.8%
Largest holdings: BHP Group Ltd 15.4%, Commonwealth Bank of Australia 12.6%, National Australia Bank Ltd 6.1%, Westpac Banking Corp 6.0%, ANZ Group Holdings Ltd 5.8%
Sector mix: Financial services 42.0%, Basic materials 25.4%, Consumer cyclical 6.5%, Healthcare 5.6%
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

<details><summary><b>What analysts and big funds say</b> — score -0.35</summary>

_Not available today._

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score -0.35</summary>

```text
Rolled up from the 5 largest holdings, 45.9% of the fund by weight
Ratings by weight: buy 0.0% | hold 59.5% | sell 40.5% (mean 3.41 on a 1=strong buy to 5=strong sell scale)
Weighted price target: -6.6% above the current prices
Holdings read: BHP.AX, CBA.AX, NAB.AX, WBC.AX, ANZ.AX
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
Share count change: 1 week: -1.5% (-18.71M) over 7d | 1 month: -10.2% (-136.38M) over 30d
Shares outstanding: 41.47M | fund size: 1.21B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Canada (EWC) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:** no explanation. It wrote only “NEUTRAL”, so the main reasons below are all it gave.

**Main reasons it gave:**
- No macro surprise; US yields and inflation unchanged
- Technicals show price above 20d, 50d, 200d SMAs, RSI 55, MACD positive but volume only 0.19x 20‑day average
- Analyst coverage 79.8% buy with weighted price target +3.7% above current price
- Fund flows mixed: +0.6% net inflow over month, -2.3% outflow over week

<details><summary><b>News</b> — score +0.00</summary>

_No news found for this one today._

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.04% (-0.03 on the week) | 5-year 4.81% (-0.09 on the week) | 10-year 4.99% (-0.11 on the week) | 30-year 5.31% (-0.12 on the week)
Yield curve, 10-year minus 3-month: +0.95 points -- upward sloping (normal)
US dollar index: 101.76 (-0.08 on the week)
Volatility (VIX): 20.36 (+0.4 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.2% (2026-09-01) | jobless claims 194k (2026-10-17)
Policy and expectations: Fed target 4.00% | market expects 2.3% inflation over 10 years
Rate path: 2-year Treasury 4.81% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 60.64 (bar of 2026-10-23), from 502 daily bars
Trend: vs 20d SMA 59.51 (+1.9%), 50d 60.51 (+0.2%), 200d 58.15 (+4.3%); 50d above 200d
Momentum: RSI(14) 55.0 | MACD 0.229 vs signal -0.030 (histogram 0.259)
Returns: 1d -0.5% | 5d +0.1% | 1m +2.0% | 3m +2.1%
52-week range: 49.72 - 62.64 (now 84.5% of the way up)
Volatility: ATR(14) 0.71 (1.2% of price) | annualised 20d 15.0%
Volume: 0.19x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.30</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score +0.30</summary>

```text
Fund type: Focused Region
What it holds: P/E 18.94 | P/B 2.75 | P/S 2.69 | 3y earnings growth n/a
Yield: 1.3%
Three-year record: +25.9% a year | beta to the market 0.80
Cost and size: expense ratio 0.50% | net assets 7.02B
What it is made of: Stocks 99.6%, Cash 0.4%
Largest holdings: Royal Bank of Canada 9.1%, The Toronto-Dominion Bank 6.5%, Shopify Inc Registered Shs -A- Subord Vtg 6.0%, Bank of Montreal 3.8%, Bank of Nova Scotia 3.7%
Sector mix: Financial services 39.9%, Energy 17.3%, Basic materials 15.2%, Technology 9.3%
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
Rolled up from the 5 largest holdings, 29.3% of the fund by weight
Ratings by weight: buy 79.8% | hold 20.2% | sell 0.0% (mean 2.12 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +3.7% above the current prices
Holdings read: RY, TD, SHOP, BMO.TO, BNS.TO
Recent rating changes among them:
  - RY: 2025-08-29 Argus Research: main, Buy -> Buy
  - TD: 2026-06-01 RBC Capital: main, Outperform -> Outperform
  - SHOP: 2026-10-16 RBC Capital: main, Outperform -> Outperform
  - BMO.TO: 2026-05-28 RBC Capital: main, Sector Perform -> Sector Perform
  - BNS.TO: 2026-05-28 RBC Capital: main, Sector Perform -> Sector Perform
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
Share count change: 1 week: -2.3% (-161.60M) over 7d | 1 month: +0.6% (44.47M) over 30d
Shares outstanding: 114.44M | fund size: 6.94B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Sweden (EWD) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> No macro surprise, no decisive technical break, and low‑volume price action. Positive analyst coverage and strong inflows are offset by modest technical weakness.

**Main reasons it gave:**
- Fund flows: +25.4% share count increase over 30 days
- Analyst ratings: 81.7% buy, mean rating 2.0 (bullish)
- Technical indicators: price below 20‑day SMA, RSI 42.2, low volume
- Macro: yields down modestly, no surprise data

<details><summary><b>News</b> — score +0.00</summary>

- [Spotify Stock Jumps on Upbeat Q3 as AI Takes Center Stage](https://finance.yahoo.com/markets/stocks/articles/spotify-stock-jumps-upbeat-q3-120000133.html)  
  <sub>Yahoo Finance, 3 hours ago</sub>  
  Spotify stock jumped 11% after Q3 results. Can AI growth and improving margins fuel further gains? Explore ETFs with SPOT exposure.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.04% (-0.03 on the week) | 5-year 4.81% (-0.09 on the week) | 10-year 4.99% (-0.11 on the week) | 30-year 5.31% (-0.12 on the week)
Yield curve, 10-year minus 3-month: +0.95 points -- upward sloping (normal)
US dollar index: 101.76 (-0.08 on the week)
Volatility (VIX): 20.36 (+0.4 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.2% (2026-09-01) | jobless claims 194k (2026-10-17)
Policy and expectations: Fed target 4.00% | market expects 2.3% inflation over 10 years
Rate path: 2-year Treasury 4.81% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score -0.20</summary>

```text
Last close 50.15 (bar of 2026-10-23), from 502 daily bars
Trend: vs 20d SMA 50.52 (-0.7%), 50d 51.70 (-3.0%), 200d 51.49 (-2.6%); 50d above 200d
Momentum: RSI(14) 42.2 | MACD -0.219 vs signal -0.265 (histogram 0.045)
Returns: 1d -0.4% | 5d -2.1% | 1m -1.8% | 3m -1.6%
52-week range: 45.38 - 54.72 (now 51.1% of the way up)
Volatility: ATR(14) 0.68 (1.3% of price) | annualised 20d 14.1%
Volume: 0.05x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.50</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score +0.50</summary>

```text
Fund type: Focused Region
What it holds: P/E 14.64 | P/B 2.82 | P/S 2.83 | 3y earnings growth n/a
Yield: 3.6%
Three-year record: +21.0% a year | beta to the market 1.25
Cost and size: expense ratio 0.51% | net assets 947.21M
What it is made of: Stocks 99.1%, Cash 0.9%
Largest holdings: Spotify Technology SA 9.7%, Investor AB Class B 9.6%, Atlas Copco AB Class A 7.1%, Volvo AB Class B 6.8%, Sandvik AB 5.3%
Sector mix: Industrials 46.3%, Financial services 25.6%, Communication services 13.5%, Technology 6.1%
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

<details><summary><b>What analysts and big funds say</b> — score +0.50</summary>

_Not available today._

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score +0.50</summary>

```text
Rolled up from the 4 largest holdings, 28.9% of the fund by weight
Ratings by weight: buy 81.7% | hold 18.3% | sell 0.0% (mean 2.00 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +17.0% above the current prices
Holdings read: SPOT, ATCO-A.ST, VOLV-B.ST, SAND.ST
Recent rating changes among them:
  - SPOT: 2026-10-23 Barclays: main, Overweight -> Overweight
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
Share count change: 1 week: +0.2% (2.25M) over 7d | 1 month: +25.4% (188.59M) over 30d
Shares outstanding: 18.59M | fund size: 932.07M
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Germany (EWG) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Neutral overall; mixed signals with bullish analyst coverage, modest fundamentals, flat flows, and weak technicals.

**Main reasons it gave:**
- Germany composite PMI fell to 52.8, missing consensus 53.3
- CDS spreads widening across Europe, indicating credit risk concerns
- EWG price below 20‑day, 50‑day and 200‑day SMAs, indicating downtrend
- Analyst coverage shows 78.7% buy rating and +23.4% price target

<details><summary><b>News</b> — score +0.00</summary>

- [Germany's composite PMI hits two-month low as services growth eases (EWG:NYSEARCA)](https://seekingalpha.com/news/4656440-germanys-composite-pmi-hits-two-month-low-as-services-growth-eases)  
  <sub>Seeking Alpha, 7 hours ago</sub>  
  Germany's flash composite PMI fell to 52.8 in October from 53.8 in September, missing the consensus estimate of 53.3.
- [Capital scarcity meets a debt surge: CDS spreads widen across the board, from AI cloud infrastructure to French sovereign bonds. Who is footing the bill for high leverage?](https://news.futunn.com/en/post/1002022560/capital-scarcity-meets-a-debt-surge-cds-spreads-widen-across)  
  <sub>富途牛牛, 15 hours ago</sub>  
  FromAI firms financing data-center projects to the heavily indebted French government, credit markets are flashing warning signs as investors grow...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.04% (-0.03 on the week) | 5-year 4.81% (-0.09 on the week) | 10-year 4.99% (-0.11 on the week) | 30-year 5.31% (-0.12 on the week)
Yield curve, 10-year minus 3-month: +0.95 points -- upward sloping (normal)
US dollar index: 101.76 (-0.08 on the week)
Volatility (VIX): 20.36 (+0.4 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.2% (2026-09-01) | jobless claims 194k (2026-10-17)
Policy and expectations: Fed target 4.00% | market expects 2.3% inflation over 10 years
Rate path: 2-year Treasury 4.81% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score -0.20</summary>

```text
Last close 40.90 (bar of 2026-10-23), from 502 daily bars
Trend: vs 20d SMA 41.27 (-0.9%), 50d 42.53 (-3.8%), 200d 42.28 (-3.3%); 50d above 200d
Momentum: RSI(14) 41.4 | MACD -0.301 vs signal -0.378 (histogram 0.077)
Returns: 1d -1.1% | 5d -1.6% | 1m -2.3% | 3m -2.1%
52-week range: 38.08 - 44.59 (now 43.4% of the way up)
Volatility: ATR(14) 0.50 (1.2% of price) | annualised 20d 14.4%
Volume: 0.12x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.25</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score +0.25</summary>

```text
Fund type: Focused Region
What it holds: P/E 17.64 | P/B 1.86 | P/S 1.23 | 3y earnings growth n/a
Yield: 2.0%
Three-year record: +20.7% a year | beta to the market 0.98
Cost and size: expense ratio 0.49% | net assets 1.47B
What it is made of: Stocks 99.9%, Cash 0.1%
Largest holdings: Siemens AG 12.1%, SAP SE 11.5%, Allianz SE 9.6%, Siemens Energy AG Ordinary Shares 6.7%, Deutsche Telekom AG 5.4%
Sector mix: Industrials 28.9%, Financial services 22.9%, Technology 16.4%, Healthcare 7.2%
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
Rolled up from the 5 largest holdings, 45.4% of the fund by weight
Ratings by weight: buy 78.7% | hold 21.3% | sell 0.0% (mean 1.96 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +23.4% above the current prices
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
Share count change: 1 week: +0.0% (0.00) over 7d | 1 month: +0.0% (0.00) over 30d
Shares outstanding: 79.50M | fund size: 3.25B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Italy (EWI) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> No macro surprise, technicals show downtrend but no decisive break, positive analyst view limited to 53% of fund, net inflows modest, credit risk indicated by widening CDS spreads.

**Main reasons it gave:**
- Analyst view: 100% buy rating and +25.5% price target covering 53% of fund
- Fund flows: +10.6% share count increase over past month indicating net inflows
- Technicals: price below 20d, 50d, 200d SMAs, RSI 30.5, no decisive break
- Macro: US inflation, unemployment, and Fed policy unchanged, no surprise
- Credit risk: CDS spreads widening across European sovereigns and banks

<details><summary><b>News</b> — score +0.00</summary>

- [EWI: Your Guide To This Bank-Heavy Portfolio Of Italian Stocks (NYSEARCA:EWI)](https://seekingalpha.com/article/4956498-ewi-your-guide-to-bank-heavy-portfolio-of-italian-stocks)  
  <sub>Seeking Alpha, 22 hours ago</sub>  
  The iShares MSCI Italy ETF is the only US-listed Italy ETF with value, income, and diversification potential amid high financial exposure. Click for more.
- [Capital scarcity meets a debt surge: CDS spreads widen across the board, from AI cloud infrastructure to French sovereign bonds. Who is footing the bill for high leverage?](https://news.futunn.com/en/post/1002022560/capital-scarcity-meets-a-debt-surge-cds-spreads-widen-across)  
  <sub>富途牛牛, 15 hours ago</sub>  
  FromAI firms financing data-center projects to the heavily indebted French government, credit markets are flashing warning signs as investors grow...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.04% (-0.03 on the week) | 5-year 4.81% (-0.09 on the week) | 10-year 4.99% (-0.11 on the week) | 30-year 5.31% (-0.12 on the week)
Yield curve, 10-year minus 3-month: +0.95 points -- upward sloping (normal)
US dollar index: 101.76 (-0.08 on the week)
Volatility (VIX): 20.36 (+0.4 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.2% (2026-09-01) | jobless claims 194k (2026-10-17)
Policy and expectations: Fed target 4.00% | market expects 2.3% inflation over 10 years
Rate path: 2-year Treasury 4.81% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score -0.10</summary>

```text
Last close 54.71 (bar of 2026-10-23), from 502 daily bars
Trend: vs 20d SMA 56.82 (-3.7%), 50d 59.75 (-8.4%), 200d 58.13 (-5.9%); 50d above 200d
Momentum: RSI(14) 30.5 | MACD -1.277 vs signal -1.241 (histogram -0.036)
Returns: 1d -0.6% | 5d -3.1% | 1m -8.7% | 3m -10.0%
52-week range: 50.70 - 63.35 (now 31.7% of the way up)
Volatility: ATR(14) 0.82 (1.5% of price) | annualised 20d 18.7%
Volume: 0.11x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.50</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score +0.50</summary>

```text
Fund type: Focused Region
What it holds: P/E 14.42 | P/B 1.77 | P/S 1.50 | 3y earnings growth n/a
Yield: 3.2%
Three-year record: +28.2% a year | beta to the market 0.88
Cost and size: expense ratio 0.50% | net assets 1.17B
What it is made of: Stocks 99.9%, Cash 0.1%
Largest holdings: UniCredit SpA 18.0%, Intesa Sanpaolo 15.0%, Enel SpA 10.6%, Eni SpA 4.7%, Prysmian SpA 4.7%
Sector mix: Financial services 54.1%, Utilities 16.5%, Industrials 12.0%, Consumer cyclical 8.0%
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

<details><summary><b>What analysts and big funds say</b> — score +0.70</summary>

_Not available today._

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score +0.70</summary>

```text
Rolled up from the 5 largest holdings, 53.0% of the fund by weight
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 2.03 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +25.5% above the current prices
Holdings read: UCG.MI, ISP.MI, ENEL.MI, ENI.MI, PRY.MI
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
Share count change: 1 week: +0.6% (6.27M) over 7d | 1 month: +10.6% (109.33M) over 30d
Shares outstanding: 20.83M | fund size: 1.14B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Japan (EWJ) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:** no explanation. It wrote only “NEUTRAL”, so the main reasons below are all it gave.

**Main reasons it gave:**
- Japan inflation 2.1% Y/Y, highest since Dec 2025 (moderate rise, no surprise)
- CFTC speculators net short 2.4% and increased 5.8% week over week (slight bearish tilt)
- Analyst coverage thin (17% of fund) but 100% buy with +28.7% price target (modest bullish bias)
- Fund inflows +5.1% month over month (bullish demand)
- Technical: price below 20‑day and 50‑day SMA, RSI 36.9, MACD negative (short‑term bearish but no decisive break)

<details><summary><b>News</b> — score +0.00</summary>

- [Japan inflation reaches highest level since December 2025 (EWJ:NYSEARCA)](https://seekingalpha.com/news/4656422-japan-inflation-reaches-highest-level-since-december-2025)  
  <sub>Seeking Alpha, 10 hours ago</sub>  
  Japan's annual inflation rate accelerated to 2.1% Y/Y in September 2026 from 1.9% in each of the previous two months, reaching its highest level since...
- [How Exposed Is EWJ (NYSEARCA:EWJ) to a Roughly 3% Slide in the Nikkei?](https://kalkine.ca/news/general-news/how-exposed-is-ewj-nysearcaewj-to-a-roughly-3-slide-in-the-nikkei)  
  <sub>kalkine.ca, 22 hours ago</sub>  
  You are reading a free article with opinions that may differ from the recommendation given by Kalkine in its paid research reports. Become a Kalkine member...
- [Asian markets mixed as tech sell-off on Wall Street weighs on sentiment (EWJ:NYSEARCA)](https://seekingalpha.com/news/4656418-asian-markets-mixed-as-tech-sell-off-on-wall-street-weighs-on-sentiment)  
  <sub>Seeking Alpha, 10 hours ago</sub>  
  Asian markets traded mixed on Friday after a sell-off in U.S. technology stocks weighed on global sentiment, while rising oil prices amid escalating...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.04% (-0.03 on the week) | 5-year 4.81% (-0.09 on the week) | 10-year 4.99% (-0.11 on the week) | 30-year 5.31% (-0.12 on the week)
Yield curve, 10-year minus 3-month: +0.95 points -- upward sloping (normal)
US dollar index: 101.76 (-0.08 on the week)
Volatility (VIX): 20.36 (+0.4 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.2% (2026-09-01) | jobless claims 194k (2026-10-17)
Policy and expectations: Fed target 4.00% | market expects 2.3% inflation over 10 years
Rate path: 2-year Treasury 4.81% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 93.98 (bar of 2026-10-23), from 502 daily bars
Trend: vs 20d SMA 96.74 (-2.8%), 50d 96.71 (-2.8%), 200d 91.54 (+2.7%); 50d above 200d
Momentum: RSI(14) 36.9 | MACD -0.640 vs signal -0.263 (histogram -0.377)
Returns: 1d -0.7% | 5d -0.9% | 1m -1.9% | 3m +2.7%
52-week range: 79.49 - 99.32 (now 73.1% of the way up)
Volatility: ATR(14) 1.26 (1.3% of price) | annualised 20d 12.5%
Volume: 0.22x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.25</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score +0.25</summary>

```text
Fund type: Japan Stock
What it holds: P/E 15.27 | P/B 1.98 | P/S 1.37 | 3y earnings growth n/a
Yield: 3.7%
Three-year record: +21.6% a year | beta to the market 0.83
Cost and size: expense ratio 0.49% | net assets 23.53B
What it is made of: Stocks 99.1%, Cash 0.9%
Largest holdings: Mitsubishi UFJ Financial Group Inc 4.7%, Toyota Motor Corp 3.3%, Tokyo Electron Ltd 3.1%, Sumitomo Mitsui Financial Group Inc 3.0%, Advantest Corp 3.0%
Sector mix: Industrials 22.8%, Technology 22.0%, Financial services 19.3%, Consumer cyclical 11.1%
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

<details><summary><b>What analysts and big funds say</b> — score +0.20</summary>

_Not available today._

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score +0.20</summary>

```text
Rolled up from the 5 largest holdings, 17.0% of the fund by weight  -- thin, so read this as a fact about that slice rather than the fund
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 1.69 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +28.7% above the current prices
Holdings read: 8306.T, 7203.T, 8035.T, 8316.T, 6857.T
Recent rating changes among them: none reported
```

</details>

<details><summary><b>Buying and selling by company insiders</b> — score -0.15</summary>

_Not available today._

</details>

<details><summary><b>Who is positioned how</b> — score -0.15</summary>

```text
Contract: NIKKEI STOCK AVERAGE YEN DENOM - CHICAGO MERCANTILE EXCHANGE (positions as of 2026-10-13, published the following Friday)
Large speculators: net short 2.4% of open interest (23,701 contracts)
Change on the week: +5.8% of open interest
Crowding: 15% percentile over 52 weeks -- within its normal range
Read this as crowding, not as a forecast: an extreme is as often the end of a move as the middle of one.
```

</details>

<details><summary><b>Money going into and out of this fund</b> — score -0.15</summary>

```text
Direction: money coming in (1 month)
Share count change: 1 week: +1.6% (372.93M) over 7d | 1 month: +5.1% (1.11B) over 30d
Shares outstanding: 246.14M | fund size: 23.13B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Switzerland (EWL) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Neutral overall; no macro surprise, mixed technicals, modest analyst bullishness, flat flows.

**Main reasons it gave:**
- Analyst consensus 64.8% buy with +4.8% price target
- Technicals: price above 20d, 50d, 200d SMAs, RSI 64.6, but 50d SMA below 200d SMA and low volume
- Fund flows flat (0% change) indicating no net demand
- Macro: no policy or data surprise; yields slightly down, curve normal, VIX modestly elevated

<details><summary><b>News</b> — score +0.00</summary>

_No news found for this one today._

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.04% (-0.03 on the week) | 5-year 4.81% (-0.09 on the week) | 10-year 4.99% (-0.11 on the week) | 30-year 5.31% (-0.12 on the week)
Yield curve, 10-year minus 3-month: +0.95 points -- upward sloping (normal)
US dollar index: 101.76 (-0.08 on the week)
Volatility (VIX): 20.36 (+0.4 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.2% (2026-09-01) | jobless claims 194k (2026-10-17)
Policy and expectations: Fed target 4.00% | market expects 2.3% inflation over 10 years
Rate path: 2-year Treasury 4.81% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 63.08 (bar of 2026-10-23), from 502 daily bars
Trend: vs 20d SMA 60.68 (+4.0%), 50d 61.56 (+2.5%), 200d 61.70 (+2.2%); 50d below 200d
Momentum: RSI(14) 64.6 | MACD 0.591 vs signal 0.110 (histogram 0.481)
Returns: 1d -0.9% | 5d +1.3% | 1m +4.4% | 3m +1.0%
52-week range: 55.06 - 65.08 (now 80.1% of the way up)
Volatility: ATR(14) 0.68 (1.1% of price) | annualised 20d 14.5%
Volume: 0.16x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.00</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score +0.00</summary>

```text
Fund type: Focused Region
What it holds: P/E 24.08 | P/B 4.13 | P/S 2.67 | 3y earnings growth n/a
Yield: 1.8%
Three-year record: +16.5% a year | beta to the market 0.91
Cost and size: expense ratio 0.50% | net assets 2.67B
What it is made of: Stocks 99.0%, Cash 1.0%
Largest holdings: Roche Holding AG Ordinary Shares new 13.9%, Novartis AG Registered Shares 12.4%, Nestle SA 11.0%, UBS Group AG Registered Shares 6.4%, ABB Ltd 4.6%
Sector mix: Healthcare 38.0%, Financial services 19.6%, Consumer defensive 13.1%, Industrials 12.3%
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
Rolled up from the 5 largest holdings, 48.2% of the fund by weight
Ratings by weight: buy 64.8% | hold 35.2% | sell 0.0% (mean 2.41 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +4.8% above the current prices
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
Share count change: 1 week: +0.0% (0.00) over 7d | 1 month: +0.0% (0.00) over 30d
Shares outstanding: 28.62M | fund size: 1.81B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Netherlands (EWN) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Neutral overall; analyst view is bullish but technicals are weak and fund flows are flat, with no macro surprise.

**Main reasons it gave:**
- Analyst view: 100% buy rating, weighted price target +50.8% above current price
- Technicals: price 63.55 below 20‑day, 50‑day, and 200‑day SMAs; RSI 33.1 (oversold) and negative MACD
- Fund flows: flat share count change (0% week, 0% month) indicating neutral demand
- Macro: yields slightly down, VIX stable (+0.4), no surprise data releases

<details><summary><b>News</b> — score +0.00</summary>

- [Can You Invest in Stack Overflow in 2026? Details & Alternatives](https://www.fool.com/investing/how-to-invest/stocks/how-to-invest-in-stack-overflow-stock/)  
  <sub>The Motley Fool, 17 hours ago</sub>  
  Stack Overflow operates a popular Q&A website for software developers and other professionals. Here's everything you need to know about investing in the...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.04% (-0.03 on the week) | 5-year 4.81% (-0.09 on the week) | 10-year 4.99% (-0.11 on the week) | 30-year 5.31% (-0.12 on the week)
Yield curve, 10-year minus 3-month: +0.95 points -- upward sloping (normal)
US dollar index: 101.76 (-0.08 on the week)
Volatility (VIX): 20.36 (+0.4 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.2% (2026-09-01) | jobless claims 194k (2026-10-17)
Policy and expectations: Fed target 4.00% | market expects 2.3% inflation over 10 years
Rate path: 2-year Treasury 4.81% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score -0.20</summary>

```text
Last close 63.55 (bar of 2026-10-23), from 502 daily bars
Trend: vs 20d SMA 66.22 (-4.0%), 50d 67.53 (-5.9%), 200d 64.93 (-2.1%); 50d above 200d
Momentum: RSI(14) 33.1 | MACD -0.921 vs signal -0.715 (histogram -0.207)
Returns: 1d -0.9% | 5d -2.1% | 1m -5.9% | 3m -3.5%
52-week range: 55.33 - 71.61 (now 50.5% of the way up)
Volatility: ATR(14) 0.94 (1.5% of price) | annualised 20d 17.3%
Volume: 0.02x the 20-day average
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
Three-year record: +25.1% a year | beta to the market 1.09
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

<details><summary><b>What analysts and big funds say</b> — score +0.50</summary>

_Not available today._

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score +0.50</summary>

```text
Rolled up from the 5 largest holdings, 46.7% of the fund by weight
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 1.59 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +50.8% above the current prices
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
Share count change: 1 week: +0.0% (0.00) over 7d | 1 month: +0.0% (0.00) over 30d
Shares outstanding: 5.55M | fund size: 352.70M
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Spain (EWP) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> The macro backdrop shows no surprise (yields down slightly, normal upward curve, stable inflation and unemployment). Fund flows are flat, indicating no net demand shift. Analyst coverage is modestly bullish (+10.6% price target, 51.5% buy) but only covers 55.8% of the fund, so the signal is limited. Technicals show the ETF trading below its 20‑, 50‑ and 200‑day SMAs with a low RSI and weak volume, offering no decisive breakout. Overall, none of these dimensions provide a material catalyst, so the directional call remains neutral.

**Main reasons it gave:**
- Flat fund flows (0% share count change) indicating no net demand shift
- Analyst view modestly bullish (+10.6% price target, 51.5% buy) covering 55.8% of the fund
- Technicals: price below 20‑, 50‑ and 200‑day SMAs; RSI 37.1; low volume; no decisive break
- Macro backdrop unchanged: yields down slightly, normal upward curve, stable inflation and unemployment

<details><summary><b>News</b> — score +0.00</summary>

_No news found for this one today._

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.04% (-0.03 on the week) | 5-year 4.81% (-0.09 on the week) | 10-year 4.99% (-0.11 on the week) | 30-year 5.31% (-0.12 on the week)
Yield curve, 10-year minus 3-month: +0.95 points -- upward sloping (normal)
US dollar index: 101.76 (-0.08 on the week)
Volatility (VIX): 20.36 (+0.4 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.2% (2026-09-01) | jobless claims 194k (2026-10-17)
Policy and expectations: Fed target 4.00% | market expects 2.3% inflation over 10 years
Rate path: 2-year Treasury 4.81% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 57.20 (bar of 2026-10-23), from 502 daily bars
Trend: vs 20d SMA 58.33 (-1.9%), 50d 60.49 (-5.4%), 200d 57.90 (-1.2%); 50d above 200d
Momentum: RSI(14) 37.1 | MACD -0.791 vs signal -0.816 (histogram 0.025)
Returns: 1d -0.5% | 5d -1.8% | 1m -5.9% | 3m -5.8%
52-week range: 49.37 - 63.23 (now 56.5% of the way up)
Volatility: ATR(14) 0.83 (1.5% of price) | annualised 20d 16.1%
Volume: 0.09x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.30</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score +0.30</summary>

```text
Fund type: Focused Region
What it holds: P/E 15.94 | P/B 2.15 | P/S 1.78 | 3y earnings growth n/a
Yield: 2.8%
Three-year record: +34.4% a year | beta to the market 0.88
Cost and size: expense ratio 0.50% | net assets 2.38B
What it is made of: Stocks 99.8%, Cash 0.2%
Largest holdings: Banco Santander SA 19.2%, Banco Bilbao Vizcaya Argentaria SA 14.3%, Iberdrola SA 12.8%, Repsol SA 5.0%, CaixaBank SA 4.5%
Sector mix: Financial services 45.6%, Utilities 20.7%, Industrials 14.1%, Technology 5.5%
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
Rolled up from the 5 largest holdings, 55.8% of the fund by weight
Ratings by weight: buy 51.5% | hold 48.5% | sell 0.0% (mean 2.32 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +10.6% above the current prices
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
Share count change: 1 week: +0.0% (0.00) over 7d | 1 month: +0.0% (0.00) over 30d
Shares outstanding: 37.35M | fund size: 2.14B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Taiwan (EWT) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Neutral overall: bullish analyst view and inflows are offset by mixed technicals, high valuation and no macro surprise.

**Main reasons it gave:**
- Analyst view: 100% buy rating and +43.5% price target for top holdings
- Fund flows: 3.5% share count increase in 1 week (net inflows)
- Technical: price below 20‑day and 50‑day SMAs, RSI 36.4, MACD negative
- Macro: no rate or data surprise, normal upward yield curve
- Fundamentals: high P/E 28.15 and strong 3‑year record (+44.3% per year) indicating mixed outlook

<details><summary><b>News</b> — score +0.00</summary>

- [iShares MSCI Taiwan ETF (EWT) Options Chain - Yahoo Finance](https://ca.finance.yahoo.com/quote/EWT/options/?date=1805414400&straddle=false&type=all)  
  <sub>Yahoo! Finance Canada, 6 hours ago</sub>  
  View the basic EWT option chain and compare options of iShares MSCI Taiwan ETF on Yahoo Finance.
- [Buy on the Dip Prospects: October 21 Edition](https://etfdb.com/news/2026/10/22/buy-on-the-dip-prospets-oct-21-edit/)  
  <sub>ETF Database, 23 hours ago</sub>  
  Below is a look at ETFs that currently offer attractive buying opportunities. The ETFs included in this list are rated as buy candidates for two reasons.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.04% (-0.03 on the week) | 5-year 4.81% (-0.09 on the week) | 10-year 4.99% (-0.11 on the week) | 30-year 5.31% (-0.12 on the week)
Yield curve, 10-year minus 3-month: +0.95 points -- upward sloping (normal)
US dollar index: 101.76 (-0.08 on the week)
Volatility (VIX): 20.36 (+0.4 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.2% (2026-09-01) | jobless claims 194k (2026-10-17)
Policy and expectations: Fed target 4.00% | market expects 2.3% inflation over 10 years
Rate path: 2-year Treasury 4.81% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score -0.20</summary>

```text
Last close 104.49 (bar of 2026-10-23), from 502 daily bars
Trend: vs 20d SMA 111.80 (-6.5%), 50d 110.16 (-5.2%), 200d 92.34 (+13.2%); 50d above 200d
Momentum: RSI(14) 36.4 | MACD -1.463 vs signal -0.238 (histogram -1.225)
Returns: 1d +0.5% | 5d -1.7% | 1m -7.6% | 3m +6.8%
52-week range: 60.03 - 118.00 (now 76.7% of the way up)
Volatility: ATR(14) 2.43 (2.3% of price) | annualised 20d 27.6%
Volume: 0.17x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score -0.10</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score -0.10</summary>

```text
Fund type: Greater China Region
What it holds: P/E 28.15 | P/B 4.48 | P/S 2.64 | 3y earnings growth n/a
Yield: 0.9%
Three-year record: +44.3% a year | beta to the market 1.26
Cost and size: expense ratio 0.59% | net assets 12.34B
What it is made of: Stocks 99.8%, Cash 0.2%
Largest holdings: Taiwan Semiconductor Manufacturing Co Ltd 21.9%, MediaTek Inc 7.2%, Delta Electronics Inc 3.9%, Hon Hai Precision Industry Co Ltd 3.2%, ASE Technology Holding Co Ltd 3.0%
Sector mix: Technology 74.2%, Financial services 14.3%, Basic materials 3.8%, Industrials 2.8%
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
Rolled up from the 5 largest holdings, 39.1% of the fund by weight
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 1.35 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +43.5% above the current prices
Holdings read: 2330.TW, 2454.TW, 2308.TW, 2317.TW, 3711.TW
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
Share count change: 1 week: +3.5% (398.85M) over 7d | 1 month: +7.3% (798.86M) over 30d
Shares outstanding: 112.89M | fund size: 11.80B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Mexico (EWW) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Neutral overall – no macro surprise, flat fund flows, and technicals show mixed signals with low volume and no decisive break. Analyst coverage is bullish but only covers ~48% of the fund, insufficient to shift the view.

**Main reasons it gave:**
- Flat fund flows: share count unchanged over 1 week and 1 month
- No macro surprise: US yields down slightly, inflation 3.7% near target, no policy change
- Technicals: price above 20‑day and 50‑day SMAs but below 200‑day SMA, low volume, no decisive break
- Analyst view bullish (90.9% buy) but covers only 47.8% of fund, limited impact

<details><summary><b>News</b> — score +0.00</summary>

_No news found for this one today._

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.04% (-0.03 on the week) | 5-year 4.81% (-0.09 on the week) | 10-year 4.99% (-0.11 on the week) | 30-year 5.31% (-0.12 on the week)
Yield curve, 10-year minus 3-month: +0.95 points -- upward sloping (normal)
US dollar index: 101.76 (-0.08 on the week)
Volatility (VIX): 20.36 (+0.4 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.2% (2026-09-01) | jobless claims 194k (2026-10-17)
Policy and expectations: Fed target 4.00% | market expects 2.3% inflation over 10 years
Rate path: 2-year Treasury 4.81% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 75.02 (bar of 2026-10-23), from 502 daily bars
Trend: vs 20d SMA 73.04 (+2.7%), 50d 74.44 (+0.8%), 200d 76.08 (-1.4%); 50d below 200d
Momentum: RSI(14) 56.8 | MACD 0.359 vs signal -0.061 (histogram 0.420)
Returns: 1d +0.1% | 5d +0.1% | 1m +3.5% | 3m -2.0%
52-week range: 65.37 - 81.23 (now 60.8% of the way up)
Volatility: ATR(14) 1.20 (1.6% of price) | annualised 20d 17.9%
Volume: 0.22x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.20</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score +0.20</summary>

```text
Fund type: Focused Region
What it holds: P/E 12.17 | P/B 1.90 | P/S 1.42 | 3y earnings growth n/a
Yield: 3.5%
Three-year record: +16.4% a year | beta to the market 1.07
Cost and size: expense ratio 0.50% | net assets 1.49B
What it is made of: Stocks 99.4%, Cash 0.6%
Largest holdings: Grupo Mexico SAB de CV Class B 16.4%, Grupo Financiero Banorte SAB de CV Class O 11.1%, Fomento Economico Mexicano SAB de CV Units Cons. Of 1 Shs-B- And 4 Shs-D- 8.8%, America Movil SAB de CV Ordinary Shares - Class B 7.2%, Wal - Mart de Mexico SAB de CV 4.4%
Sector mix: Basic materials 26.8%, Consumer defensive 24.8%, Financial services 19.5%, Industrials 12.1%
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
Rolled up from the 5 largest holdings, 47.8% of the fund by weight
Ratings by weight: buy 90.9% | hold 9.1% | sell 0.0% (mean 2.12 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +6.8% above the current prices
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
Share count change: 1 week: +0.0% (0.00) over 7d | 1 month: +0.0% (0.00) over 30d
Shares outstanding: 18.90M | fund size: 1.42B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### South Korea (EWY) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Neutral overall; modest inflows support a slight bullish tilt, but fundamentals and technicals are mixed and no analyst rating is available.

**Main reasons it gave:**
- Share count rose 4.8% week‑over‑week and 8.7% month‑over‑month (Fund flows)
- Low P/E 10.41 and strong 3‑year record (+43.7%/yr) but price below 20‑day SMA and RSI 34.5 (Fundamentals & Technicals)
- Bearish technical momentum: MACD -8.32 vs signal -5.86, RSI 34.5, volume 0.30× 20‑day avg (Technical)
- Macro environment stable: yields down slightly, normal upward‑sloping curve, VIX 20.36 (Macro)
- Analyst view provides no rating data, so analyst_score is null (Analyst view of holdings)

<details><summary><b>News</b> — score +0.00</summary>

- [Daily ETF Flows: Chip ETFs See Inflows](https://finance.yahoo.com/markets/options/articles/daily-etf-flows-chip-etfs-213158129.html)  
  <sub>Yahoo Finance, 18 hours ago</sub>  
  Top 10 Creations (All ETFs). Ticker. Name. Net Flows ($, mm). AUM ($, mm). AUM % Change. SOXX · iShares Semiconductor ETF. 2,551.44. 44,525.14. 5.73%.
- [EXCLUSIVE: Korea 'Capitulation' Signal Flashes Before SK Hynix Earnings - iShares MSCI South Korea ETF (A](https://www.benzinga.com/markets/asia/26/10/62563168/korea-capitulation-signal-ewy-sk-hynix-earnings-leinweber-exclusive)  
  <sub>Benzinga, 6 minutes ago</sub>  
  Korea capitulation signal hits EWY as SK hynix earnings near. MarketVector's Martin Leinweber tells Benzinga what history shows and the line to watch.
- [Selling pressure on AI infrastructure stocks may not have subsided. JPMorgan warns: insufficient retail investor appetite for bottom-fishing and the ebb of share buyback funds are exacerbating market risks.](https://www.moomoo.com/news/post/1001326845/selling-pressure-on-ai-infrastructure-stocks-may-not-have-subsided)  
  <sub>Moomoo, 13 hours ago</sub>  
  Zhitong Finance APP learned that in its latest "Capital Flows and Liquidity" report released on October 14, JPMorgan warned that although AI‑related...
- [Stock Market Outlook: Key Movers Ahead of Friday Trading Session](https://www.kucoin.com/news/flash/stock-market-outlook-key-movers-ahead-of-friday-trading-session)  
  <sub>KuCoin, 15 hours ago</sub>  
  This roundup covers stocks ahead of Friday's trading session, after the Nasdaq Composite recorded the index's largest daily decline since June.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.04% (-0.03 on the week) | 5-year 4.81% (-0.09 on the week) | 10-year 4.99% (-0.11 on the week) | 30-year 5.31% (-0.12 on the week)
Yield curve, 10-year minus 3-month: +0.95 points -- upward sloping (normal)
US dollar index: 101.76 (-0.08 on the week)
Volatility (VIX): 20.36 (+0.4 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.2% (2026-09-01) | jobless claims 194k (2026-10-17)
Policy and expectations: Fed target 4.00% | market expects 2.3% inflation over 10 years
Rate path: 2-year Treasury 4.81% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score -0.20</summary>

```text
Last close 151.10 (bar of 2026-10-23), from 502 daily bars
Trend: vs 20d SMA 170.87 (-11.6%), 50d 177.29 (-14.8%), 200d 161.42 (-6.4%); 50d above 200d
Momentum: RSI(14) 34.5 | MACD -8.320 vs signal -5.860 (histogram -2.460)
Returns: 1d +1.4% | 5d +0.4% | 1m -17.2% | 3m -6.3%
52-week range: 88.53 - 219.20 (now 47.9% of the way up)
Volatility: ATR(14) 6.26 (4.1% of price) | annualised 20d 42.4%
Volume: 0.30x the 20-day average
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
Three-year record: +43.7% a year | beta to the market 2.48
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

<details><summary><b>Buying and selling by company insiders</b> — score +0.40</summary>

_Not available today._

</details>

<details><summary><b>Who is positioned how</b> — score +0.40</summary>

_Not available today._

</details>

<details><summary><b>Money going into and out of this fund</b> — score +0.40</summary>

```text
Direction: money coming in (1 month)
Share count change: 1 week: +4.8% (1.14B) over 7d | 1 month: +8.7% (2.01B) over 30d
Shares outstanding: 165.62M | fund size: 25.03B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Brazil (EWZ) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> No macro surprise, flat fund flows, mixed technicals, strong analyst view but not enough to outweigh lack of catalyst.

**Main reasons it gave:**
- Fund flows flat: 0% share count change over 1 week and 1 month
- No macro surprise: US Treasury yields unchanged and no policy shift
- Technicals: price above 20d/50d/200d SMAs but MACD histogram negative and volume 0.44x 20‑day average
- Analyst coverage: 100% buy rating with +21.9% price target for top holdings
- Fund fundamentals: low P/E 10.73 and yield 3.9%

<details><summary><b>News</b> — score +0.00</summary>

- [Brazil stocks emerge as top AI hedge ahead of pivotal election (EWZ:NYSEARCA)](https://seekingalpha.com/news/4656572-brazil-stocks-emerge-as-top-ai-hedge-ahead-of-pivotal-election)  
  <sub>Seeking Alpha, 1 hour ago</sub>  
  Brazilian equities have become a clear “must own” for dedicated emerging-market investors seeking to hedge their artificial intelligence exposure,...
- [Weight Loss Drugs Create a Problem. Beauty Companies See a Market. Where’s the Proof?](https://www.moomoo.com/community/feed/weight-loss-drugs-create-a-problem-beauty-companies-see-a-117485212270598?chain_id=Name1K9-3FXPhg.1ldk97g&global_content=%7B%22promote_id%22%3A13764%2C%22sub_promote_id%22%3A107%2C%22f%22%3A%22www.moomoo.com%2Fetfs%2FIVV-AU%22%7D)  
  <sub>Moomoo, 24 hours ago</sub>  
  Swiss skincare firm Galderma, Brazilian group Natura, and L'Oreal are testing treatments for consumers worried about facial sagging and volume loss,...
- [How to Buy Nu Holdings Stock (NU) in 2026](https://www.fool.com/investing/how-to-invest/stocks/how-to-invest-in-nu-holdings-stock/)  
  <sub>The Motley Fool, 19 hours ago</sub>  
  Nu Holdings has grown from offering credit cards to providing banking and financial services to customers. Here's a step-by-step guide to investing in the...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.04% (-0.03 on the week) | 5-year 4.81% (-0.09 on the week) | 10-year 4.99% (-0.11 on the week) | 30-year 5.31% (-0.12 on the week)
Yield curve, 10-year minus 3-month: +0.95 points -- upward sloping (normal)
US dollar index: 101.76 (-0.08 on the week)
Volatility (VIX): 20.36 (+0.4 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.2% (2026-09-01) | jobless claims 194k (2026-10-17)
Policy and expectations: Fed target 4.00% | market expects 2.3% inflation over 10 years
Rate path: 2-year Treasury 4.81% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 41.87 (bar of 2026-10-23), from 502 daily bars
Trend: vs 20d SMA 41.16 (+1.7%), 50d 38.44 (+8.9%), 200d 37.18 (+12.6%); 50d above 200d
Momentum: RSI(14) 58.3 | MACD 1.160 vs signal 1.320 (histogram -0.160)
Returns: 1d +0.0% | 5d +0.1% | 1m +13.4% | 3m +16.7%
52-week range: 30.47 - 43.54 (now 87.2% of the way up)
Volatility: ATR(14) 0.95 (2.3% of price) | annualised 20d 50.1%
Volume: 0.44x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.60</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score +0.60</summary>

```text
Fund type: Focused Region
What it holds: P/E 10.73 | P/B 1.84 | P/S 1.40 | 3y earnings growth n/a
Yield: 3.9%
Three-year record: +19.2% a year | beta to the market 0.83
Cost and size: expense ratio 0.59% | net assets 8.64B
What it is made of: Stocks 97.5%, Cash 2.0%, Preferred 0.5%
Largest holdings: Vale SA 8.9%, Itau Unibanco Holding SA Participating Preferred 8.4%, Nu Holdings Ltd Ordinary Shares Class A 8.1%, Petroleo Brasileiro SA Petrobras Participating Preferred 7.5%, Petroleo Brasileiro SA Petrobras 7.0%
Sector mix: Financial services 34.4%, Energy 18.1%, Basic materials 13.0%, Utilities 12.8%
```

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

<details><summary><b>What analysts and big funds say</b> — score +0.80</summary>

_Not available today._

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score +0.80</summary>

```text
Rolled up from the 5 largest holdings, 39.9% of the fund by weight
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 1.83 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +21.9% above the current prices
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
Share count change: 1 week: +0.0% (0.00) over 7d | 1 month: +0.0% (0.00) over 30d
Shares outstanding: 200.55M | fund size: 8.40B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### South Africa (EZA) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Neutral overall: technicals show a downtrend (price below 20‑day, 50‑day and 200‑day SMAs, low volume), but no macro surprise or decisive technical break; analyst view is strongly bullish (100% buy rating for 43.4% of holdings with +37% price target); fund flows are flat, indicating neutral demand.

**Main reasons it gave:**
- Technical: price below 20‑day, 50‑day and 200‑day SMAs indicating downtrend
- Analyst view: 100% buy rating for 43.4% of holdings with +37% price target
- Fund flows: share count unchanged over week and month (neutral demand)

<details><summary><b>News</b> — score +0.00</summary>

_No news found for this one today._

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.04% (-0.03 on the week) | 5-year 4.81% (-0.09 on the week) | 10-year 4.99% (-0.11 on the week) | 30-year 5.31% (-0.12 on the week)
Yield curve, 10-year minus 3-month: +0.95 points -- upward sloping (normal)
US dollar index: 101.76 (-0.08 on the week)
Volatility (VIX): 20.36 (+0.4 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.2% (2026-09-01) | jobless claims 194k (2026-10-17)
Policy and expectations: Fed target 4.00% | market expects 2.3% inflation over 10 years
Rate path: 2-year Treasury 4.81% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score -0.30</summary>

```text
Last close 63.07 (bar of 2026-10-23), from 502 daily bars
Trend: vs 20d SMA 63.94 (-1.4%), 50d 67.34 (-6.3%), 200d 68.76 (-8.3%); 50d below 200d
Momentum: RSI(14) 40.4 | MACD -0.713 vs signal -0.883 (histogram 0.171)
Returns: 1d -1.2% | 5d -3.4% | 1m -4.3% | 3m +1.8%
52-week range: 60.43 - 81.60 (now 12.5% of the way up)
Volatility: ATR(14) 1.24 (2.0% of price) | annualised 20d 23.7%
Volume: 0.26x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.50</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score +0.50</summary>

```text
Fund type: Focused Region
What it holds: P/E 10.44 | P/B 2.00 | P/S 1.73 | 3y earnings growth n/a
Yield: 7.9%
Three-year record: +27.6% a year | beta to the market 1.07
Cost and size: expense ratio 0.59% | net assets 473.79M
What it is made of: Stocks 99.7%, Cash 0.3%
Largest holdings: Anglogold Ashanti PLC 12.7%, Gold Fields Ltd 8.7%, Naspers Ltd Class N 8.4%, Firstrand Ltd 7.4%, Standard Bank Group Ltd 6.2%
Sector mix: Basic materials 39.1%, Financial services 34.4%, Consumer cyclical 12.8%, Communication services 6.4%
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
Rolled up from the 5 largest holdings, 43.4% of the fund by weight
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 2.04 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +37.2% above the current prices
Holdings read: AU, GFI.JO, NPN.JO, FSR.JO, SBK.JO
Recent rating changes among them:
  - AU: 2026-10-22 Freedom Broker: main, Buy -> Buy
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
Shares outstanding: 7.90M | fund size: 498.25M
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Gold mining companies (GDX) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Neutral overall due to mixed signals: bearish technicals and net outflows suggest downside pressure, while analyst consensus remains strongly bullish but recent downgrades temper optimism. No macro surprise or policy shift provides a clear catalyst.

**Main reasons it gave:**
- Price below 20‑day, 50‑day and 200‑day SMAs with RSI 34.6 and negative MACD indicating bearish technicals
- Net outflows of -5% share count over the past month, showing reduced investor demand
- Macro environment unchanged: modest yield declines, inflation and unemployment near expectations, no policy surprise
- Analyst consensus remains 100% buy with a +25% price target, but three top holdings were downgraded from Buy to Hold

<details><summary><b>News</b> — score +0.00</summary>

- [Looking for a Hedge? These 2 Gold ETFs Offer Very Different Ways to Invest](https://www.fool.com/coverage/etfs/2026/10/23/looking-for-a-hedge-these-2-gold-etfs-offer-very-different-ways-to-invest/)  
  <sub>The Motley Fool, 5 hours ago</sub>  
  The iShares Gold Trust and VanEck Gold Miners ETF offer two distinct ways to invest in gold, but their differences could have a significant impact on your...
- [TD GDX ETF-Linked Autocallable Coupon Notes - Series 3054 NL (869794A2) (TDAKEXX)](https://sg.finance.yahoo.com/quote/TDAKEXX/performance/)  
  <sub>Yahoo Finance Singapore, 16 hours ago</sub>
- [GDXJ 261023 143.00C (GDXJ261023C143000) Stock Options Chain | Quotes & News](https://www.moomoo.com/options/GDXJ261023C143000-US)  
  <sub>Moomoo, 8 hours ago</sub>  
  Track real-time GDXJ 261023 143.00C (GDXJ261023C143000) stock options chain data and pricing information and news on moomoo App for your options trading and...
- [GDXJ Stock Price, Quote & News](https://www.syfe.com/stocks/us/gdxj)  
  <sub>Syfe, 23 hours ago</sub>  
  Overview. VanEck Junior Gold Miners ETF (GDXJ) is trading at US$101.80, down 6.20% today as of Oct 22, 12:06 EDT. Over the past 52 weeks, GDXJ has traded...
- [Meta Tumbles 6% on AI Spending Fears, 10-Year Yield Falls Below 5%: Stock Market Today](https://www.tradingview.com/news/benzinga:0f1220f07094b:0-meta-tumbles-6-on-ai-spending-fears-10-year-yield-falls-below-5-stock-market-today/)  
  <sub>TradingView, 22 hours ago</sub>  
  Meta Platforms Inc. NASDAQ:META led a broad tech sell-off Thursday after the Facebook parent raised its artificial intelligence spending plan,...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.04% (-0.03 on the week) | 5-year 4.81% (-0.09 on the week) | 10-year 4.99% (-0.11 on the week) | 30-year 5.31% (-0.12 on the week)
Yield curve, 10-year minus 3-month: +0.95 points -- upward sloping (normal)
US dollar index: 101.76 (-0.08 on the week)
Volatility (VIX): 20.36 (+0.4 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.2% (2026-09-01) | jobless claims 194k (2026-10-17)
Policy and expectations: Fed target 4.00% | market expects 2.3% inflation over 10 years
Rate path: 2-year Treasury 4.81% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score -0.40</summary>

```text
Last close 80.32 (bar of 2026-10-23), from 502 daily bars
Trend: vs 20d SMA 86.58 (-7.2%), 50d 92.87 (-13.5%), 200d 90.95 (-11.7%); 50d above 200d
Momentum: RSI(14) 34.6 | MACD -2.330 vs signal -1.891 (histogram -0.439)
Returns: 1d -1.7% | 5d -8.4% | 1m -13.0% | 3m +6.1%
52-week range: 68.28 - 115.84 (now 25.3% of the way up)
Volatility: ATR(14) 3.04 (3.8% of price) | annualised 20d 41.3%
Volume: 0.46x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.00</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score +0.00</summary>

```text
Fund type: Equity Precious Metals
What it holds: P/E 13.93 | P/B 3.18 | P/S 4.54 | 3y earnings growth n/a
Yield: 0.7%
Three-year record: +45.0% a year | beta to the market 0.81
Cost and size: expense ratio 0.51% | net assets 26.25B
What it is made of: Stocks 100.0%, Cash 0.0%
Largest holdings: Newmont Corp 11.1%, Agnico Eagle Mines Ltd 11.0%, Barrick Mining Corp 7.9%, Wheaton Precious Metals Corp 5.5%, Franco-Nevada Corp 5.2%
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

<details><summary><b>What analysts and big funds say</b> — score +0.40</summary>

_Not available today._

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score +0.40</summary>

```text
Rolled up from the 5 largest holdings, 40.8% of the fund by weight
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 1.69 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +25.0% above the current prices
Holdings read: NEM, AEM.TO, ABX.TO, WPM.TO, FNV.TO
Recent rating changes among them:
  - NEM: 2026-10-22 Freedom Broker: down, Buy -> Hold
  - AEM.TO: 2026-10-22 Freedom Broker: down, Buy -> Hold
  - ABX.TO: 2026-10-22 Freedom Broker: down, Buy -> Hold
  - WPM.TO: 2026-10-08 UBS: main, Buy -> Buy
  - FNV.TO: 2026-09-16 RBC Capital: main, Outperform -> Outperform
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
Share count change: 1 week: +0.8% (184.31M) over 7d | 1 month: -5.0% (-1.28B) over 30d
Shares outstanding: 303.28M | fund size: 24.36B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Software (IGV) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Neutral overall – no macro surprise, flat fund flows, mixed technicals, and bullish analyst coverage not enough to outweigh neutral fundamentals.

**Main reasons it gave:**
- Flat fund flows: 0% share count change over 1 week and 1 month
- Analyst coverage (42.9% weight) all buy with weighted price target +18.8% above current
- Technicals: ETF above 20‑day, 50‑day, 200‑day SMAs but MACD histogram negative and volume at 0.25× 20‑day average
- Macro: Treasury yields down modestly, VIX at 20.36 (elevated) and no major data surprise

<details><summary><b>News</b> — score +0.00</summary>

- [iShares Expanded Tech-Software Sector ETF (IGV) stock price, news, quote and history](https://au.finance.yahoo.com/quote/IGV/)  
  <sub>Yahoo Finance Australia, 6 hours ago</sub>  
  iShares Expanded Tech-Software Sector ETF (IGV) · -0.80% · 1.85% · 22.52% · 1.62% · -4.22% · 25.48% · 971.13%. Key events. Baseline. Advanced...
- [iShares North American Tech-Software ETF (IGV) stock price, news, quote and history](https://uk.finance.yahoo.com/quote/IGV/)  
  <sub>Yahoo Finance UK, 7 hours ago</sub>  
  iShares North American Tech-Software ETF (IGV) · -0.80% · 1.85% · 22.52% · 1.62% · -4.22% · 25.48% · 971.13%. Key events. Baseline. Advanced...
- [Flow Focus | Tech Falls Behind. Is Old-School Wall Street Back?](https://www.moomoo.com/community/feed/flow-focus-tech-falls-behind-is-old-school-wall-street-117489058250758)  
  <sub>Moomoo, 7 hours ago</sub>  
  The $Dow Jones Industrial Average (.DJI.US)$ held its ground while tech sold off. In the supplied weekly snapshot, industrials, regional banks and bio...
- [S&P 500 best performers: Zero mag 7 stocks past 13 weeks](https://www.thestreet.com/investing/sp-500-best-performers-zero-mag-7-stocks-past-13-weeks)  
  <sub>TheStreet, 14 hours ago</sub>  
  The biggest tech stocks have handed the baton as leadership has firmly shifted toward other S&P 500 sectors and industries.
- [Adobe Jumps 5% as Beaten-Down Software Names Rebound Despite Risk-Off Day; Salesforce Rises 3%](https://247wallst.com/investing/2026/10/22/adobe-jumps-5-as-beaten-down-software-names-rebound-despite-risk-off-day-salesforce-rises-3/)  
  <sub>24/7 Wall St., 21 hours ago</sub>  
  Enterprise software stocks are staging a surprise rebound even as large-cap tech crumbles around them, and the reason buyers are zeroing in on Adobe and...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.04% (-0.03 on the week) | 5-year 4.81% (-0.09 on the week) | 10-year 4.99% (-0.11 on the week) | 30-year 5.31% (-0.12 on the week)
Yield curve, 10-year minus 3-month: +0.95 points -- upward sloping (normal)
US dollar index: 101.76 (-0.08 on the week)
Volatility (VIX): 20.36 (+0.4 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.2% (2026-09-01) | jobless claims 194k (2026-10-17)
Policy and expectations: Fed target 4.00% | market expects 2.3% inflation over 10 years
Rate path: 2-year Treasury 4.81% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 110.14 (bar of 2026-10-23), from 502 daily bars
Trend: vs 20d SMA 108.56 (+1.5%), 50d 106.29 (+3.6%), 200d 93.82 (+17.4%); 50d above 200d
Momentum: RSI(14) 56.0 | MACD 0.737 vs signal 0.952 (histogram -0.214)
Returns: 1d +1.3% | 5d +5.6% | 1m +2.8% | 3m +21.2%
52-week range: 74.67 - 117.08 (now 83.6% of the way up)
Volatility: ATR(14) 2.71 (2.5% of price) | annualised 20d 28.5%
Volume: 0.25x the 20-day average
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
Three-year record: +17.1% a year | beta to the market 1.22
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

<details><summary><b>What analysts and big funds say</b> — score +0.60</summary>

_Not available today._

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score +0.60</summary>

```text
Rolled up from the 5 largest holdings, 42.9% of the fund by weight
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 1.65 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +18.8% above the current prices
Holdings read: PANW, PLTR, CRWD, MSFT, ORCL
Recent rating changes among them:
  - PANW: 2026-10-15 Citigroup: main, Buy -> Buy
  - PLTR: 2026-10-22 Citigroup: main, Buy -> Buy
  - CRWD: 2026-10-22 Mizuho: main, Outperform -> Outperform
  - MSFT: 2026-10-21 Guggenheim: reit, Buy -> Buy
  - ORCL: 2026-10-22 Cantor Fitzgerald: reit, Overweight -> Overweight
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
Shares outstanding: 12.50M | fund size: 1.38B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### India (INDA) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Neutral overall; bullish analyst view is offset by bearish fund outflows, weak technicals and modest fundamentals.

**Main reasons it gave:**
- Fund flows: 1‑month share count down 12% (-$782.6M)
- Technicals: price below 20‑day, 50‑day, 200‑day SMAs, RSI 42.3
- Analyst view: 100% buy rating on 23.7% of fund, price target +29.8% above current
- Macro: US Treasury yields up slightly, no surprise data

<details><summary><b>News</b> — score +0.00</summary>

- [iShares MSCI India ETF • Robinhood Token (INDA) Price Prediction for 2026 to 2031](https://www.bybit.com/en-GB/price-prediction/ishares-msci-india-etf-robinhood-token/)  
  <sub>Bybit, 19 hours ago</sub>  
  Forecast data for 2029 places iShares MSCI India ETF • Robinhood Token's expected price at approximately $54.63. Historically, 2029 sees a positive trend as...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.04% (-0.03 on the week) | 5-year 4.81% (-0.09 on the week) | 10-year 4.99% (-0.11 on the week) | 30-year 5.31% (-0.12 on the week)
Yield curve, 10-year minus 3-month: +0.95 points -- upward sloping (normal)
US dollar index: 101.76 (-0.08 on the week)
Volatility (VIX): 20.36 (+0.4 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.2% (2026-09-01) | jobless claims 194k (2026-10-17)
Policy and expectations: Fed target 4.00% | market expects 2.3% inflation over 10 years
Rate path: 2-year Treasury 4.81% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score -0.40</summary>

```text
Last close 46.54 (bar of 2026-10-23), from 502 daily bars
Trend: vs 20d SMA 46.86 (-0.7%), 50d 48.13 (-3.3%), 200d 49.33 (-5.7%); 50d below 200d
Momentum: RSI(14) 42.3 | MACD -0.204 vs signal -0.314 (histogram 0.111)
Returns: 1d -1.7% | 5d -2.3% | 1m -2.1% | 3m -4.8%
52-week range: 45.42 - 54.83 (now 11.9% of the way up)
Volatility: ATR(14) 0.53 (1.1% of price) | annualised 20d 16.7%
Volume: 0.47x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score -0.20</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score -0.20</summary>

```text
Fund type: India Equity
What it holds: P/E 21.36 | P/B 2.96 | P/S 2.56 | 3y earnings growth n/a
Yield: n/a
Three-year record: +2.7% a year | beta to the market 0.62
Cost and size: expense ratio 0.61% | net assets 5.83B
What it is made of: Stocks 99.3%, Cash 0.7%
Largest holdings: HDFC Bank Ltd 6.4%, ICICI Bank Ltd 5.6%, Reliance Industries Ltd 5.4%, Bharti Airtel Ltd 3.9%, Infosys Ltd 2.4%
Sector mix: Financial services 29.7%, Consumer cyclical 12.3%, Industrials 10.2%, Basic materials 8.5%
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
Rolled up from the 5 largest holdings, 23.7% of the fund by weight  -- thin, so read this as a fact about that slice rather than the fund
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 1.35 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +29.8% above the current prices
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
Share count change: 1 week: -0.4% (-22.20M) over 7d | 1 month: -12.0% (-782.59M) over 30d
Shares outstanding: 123.12M | fund size: 5.73B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Defence and aerospace (ITA) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Neutral overall: bullish analyst coverage and price target are offset by net outflows and mixed technical signals, with no macro surprise.

**Main reasons it gave:**
- Fund flows: -7.4% share count over 1 month, indicating net outflows
- Analyst view: 100% buy rating covering 53.9% of fund, weighted price target +32.3% above current price
- Technical: price below 20‑day, 50‑day, 200‑day SMAs; RSI 30.9 (oversold) and MACD bullish crossover with low volume
- Macro: yields up modestly, upward‑sloping yield curve, VIX elevated at 20.36, no policy surprise

<details><summary><b>News</b> — score +0.00</summary>

- [State Street SPDR S&P Aerospace & Defense ETF (XAR) Stock Price, News, Quote & History](https://ca.finance.yahoo.com/quote/XAR/)  
  <sub>Yahoo! Finance Canada, 18 hours ago</sub>  
  Find the latest State Street SPDR S&P Aerospace & Defense ETF (XAR) stock quote, history, news and other vital information to help you with your stock...
- [BioNTech (BNTX) Collaborates with Gilead to Test Pumitamig and T](https://www.gurufocus.com/news/9138250/biontech-bntx-collaborates-with-gilead-to-test-pumitamig-and-trodelvy-in-breast-cancer-trial)  
  <sub>GuruFocus, 15 hours ago</sub>  
  On October 22, 2026, BioNTech SE (NASDAQ: BNTX) announced a strategic collaboration with Gilead Sciences (GILD) to evaluate the combination of BioNTech's...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.04% (-0.03 on the week) | 5-year 4.81% (-0.09 on the week) | 10-year 4.99% (-0.11 on the week) | 30-year 5.31% (-0.12 on the week)
Yield curve, 10-year minus 3-month: +0.95 points -- upward sloping (normal)
US dollar index: 101.76 (-0.08 on the week)
Volatility (VIX): 20.36 (+0.4 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.2% (2026-09-01) | jobless claims 194k (2026-10-17)
Policy and expectations: Fed target 4.00% | market expects 2.3% inflation over 10 years
Rate path: 2-year Treasury 4.81% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 201.35 (bar of 2026-10-23), from 502 daily bars
Trend: vs 20d SMA 206.39 (-2.4%), 50d 218.60 (-7.9%), 200d 229.57 (-12.3%); 50d below 200d
Momentum: RSI(14) 30.9 | MACD -3.673 vs signal -4.190 (histogram 0.516)
Returns: 1d -1.5% | 5d -3.7% | 1m -5.4% | 3m -17.4%
52-week range: 198.23 - 253.22 (now 5.7% of the way up)
Volatility: ATR(14) 4.09 (2.0% of price) | annualised 20d 15.6%
Volume: 0.37x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.00</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score +0.00</summary>

```text
Fund type: Industrials
What it holds: P/E 31.87 | P/B 5.88 | P/S 2.95 | 3y earnings growth n/a
Yield: 0.3%
Three-year record: +25.3% a year | beta to the market 0.98
Cost and size: expense ratio 0.37% | net assets 12.14B
What it is made of: Stocks 100.0%, Cash 0.0%
Largest holdings: GE Aerospace 21.0%, RTX Corp 16.2%, Boeing Co 7.5%, Howmet Aerospace Inc 4.6%, Lockheed Martin Corp 4.6%
Sector mix: Industrials 100.0%
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
Rolled up from the 5 largest holdings, 53.9% of the fund by weight
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 1.68 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +32.3% above the current prices
Holdings read: GE, RTX, BA, HWM, LMT
Recent rating changes among them:
  - GE: 2026-10-21 UBS: main, Buy -> Buy
  - RTX: 2026-10-21 UBS: main, Neutral -> Neutral
  - BA: 2026-10-19 Morgan Stanley: main, Equal-Weight -> Equal-Weight
  - HWM: 2026-10-15 RBC Capital: main, Outperform -> Outperform
  - LMT: 2026-10-23 RBC Capital: main, Sector Perform -> Sector Perform
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
Share count change: 1 week: -0.8% (-96.09M) over 7d | 1 month: -7.4% (-952.21M) over 30d
Shares outstanding: 59.00M | fund size: 11.88B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Transport and delivery (IYT) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Neutral overall: strong analyst buy rating (+27.4% price target) is offset by sizable outflows (‑14.2% month‑over‑month) and mixed technicals (price below 50‑ and 200‑day SMA, RSI 47.9, MACD near zero). Macro shows modest yield rises, elevated VIX, and no surprise data, providing no clear catalyst.

**Main reasons it gave:**
- Analyst view: 100% buy rating with +27.4% price target
- Fund flows: 14.2% outflow over past month (share count down 14.2%)
- Technicals: price below 50‑day and 200‑day SMA, RSI 47.9, MACD near zero
- Macro: yields up modestly, VIX elevated, no surprise data

<details><summary><b>News</b> — score +0.00</summary>

_No news found for this one today._

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.04% (-0.03 on the week) | 5-year 4.81% (-0.09 on the week) | 10-year 4.99% (-0.11 on the week) | 30-year 5.31% (-0.12 on the week)
Yield curve, 10-year minus 3-month: +0.95 points -- upward sloping (normal)
US dollar index: 101.76 (-0.08 on the week)
Volatility (VIX): 20.36 (+0.4 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.2% (2026-09-01) | jobless claims 194k (2026-10-17)
Policy and expectations: Fed target 4.00% | market expects 2.3% inflation over 10 years
Rate path: 2-year Treasury 4.81% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 80.14 (bar of 2026-10-23), from 502 daily bars
Trend: vs 20d SMA 79.82 (+0.4%), 50d 82.06 (-2.3%), 200d 81.60 (-1.8%); 50d above 200d
Momentum: RSI(14) 47.9 | MACD -0.314 vs signal -0.604 (histogram 0.290)
Returns: 1d -2.2% | 5d +0.1% | 1m +1.5% | 3m -8.1%
52-week range: 68.14 - 90.01 (now 54.9% of the way up)
Volatility: ATR(14) 1.39 (1.7% of price) | annualised 20d 17.6%
Volume: 0.48x the 20-day average
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
Three-year record: +13.6% a year | beta to the market 1.32
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

<details><summary><b>What analysts and big funds say</b> — score +0.50</summary>

_Not available today._

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score +0.50</summary>

```text
Rolled up from the 5 largest holdings, 51.6% of the fund by weight
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 1.64 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +27.4% above the current prices
Holdings read: UNP, UBER, CSX, DAL, UAL
Recent rating changes among them:
  - UNP: 2026-10-23 RBC Capital: main, Outperform -> Outperform
  - UBER: 2026-10-16 Guggenheim: reit, Buy -> Buy
  - CSX: 2026-10-22 UBS: main, Buy -> Buy
  - DAL: 2026-10-12 UBS: main, Buy -> Buy
  - UAL: 2026-10-22 BMO Capital: main, Outperform -> Outperform
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
Share count change: 1 week: -0.1% (-1.67M) over 7d | 1 month: -14.2% (-311.95M) over 30d
Shares outstanding: 23.57M | fund size: 1.89B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### US regional banks (KRE) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Neutral overall – analyst view modestly bullish on a thin slice, but fund outflows are bearish and fundamentals are only mildly positive; no macro surprise or decisive technical break.

**Main reasons it gave:**
- Analyst coverage of top 5 holdings (5.7% of fund) shows 59.8% buy and +9.8% price target
- Fund flows indicate net outflows of -4.2% share count over the past month
- Fund fundamentals: low P/E 12.02, P/B 1.21, dividend yield 2.3%, three‑year return +25.1% per year
- Macro environment: upward‑sloping yield curve, no rate surprise, VIX elevated at 20.36

<details><summary><b>News</b> — score +0.00</summary>

- [Composition vs. Returns: Breaking Down the Structural Drift Between KBE and KRE](https://finance.yahoo.com/markets/stocks/articles/composition-vs-returns-breaking-down-133701474.html)  
  <sub>Yahoo Finance, 1 hour ago</sub>  
  State Street SPDR S&P Regional Banking ETF (NYSEMKT:KRE) provides targeted exposure to local lenders, while State Street SPDR S&P Bank ETF (NYSEMKT:KBE)...
- [Flow Focus | Tech Falls Behind. Is Old-School Wall Street Back?](https://www.moomoo.com/community/feed/flow-focus-tech-falls-behind-is-old-school-wall-street-117489058250758)  
  <sub>Moomoo, 7 hours ago</sub>  
  The $Dow Jones Industrial Average (.DJI.US)$ held its ground while tech sold off. In the supplied weekly snapshot, industrials, regional banks and bio...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.04% (-0.03 on the week) | 5-year 4.81% (-0.09 on the week) | 10-year 4.99% (-0.11 on the week) | 30-year 5.31% (-0.12 on the week)
Yield curve, 10-year minus 3-month: +0.95 points -- upward sloping (normal)
US dollar index: 101.76 (-0.08 on the week)
Volatility (VIX): 20.36 (+0.4 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.2% (2026-09-01) | jobless claims 194k (2026-10-17)
Policy and expectations: Fed target 4.00% | market expects 2.3% inflation over 10 years
Rate path: 2-year Treasury 4.81% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 72.30 (bar of 2026-10-23), from 502 daily bars
Trend: vs 20d SMA 70.02 (+3.3%), 50d 72.36 (-0.1%), 200d 70.85 (+2.0%); 50d above 200d
Momentum: RSI(14) 58.2 | MACD -0.266 vs signal -0.758 (histogram 0.492)
Returns: 1d -0.2% | 5d +3.6% | 1m +1.9% | 3m -4.3%
52-week range: 58.63 - 77.93 (now 70.8% of the way up)
Volatility: ATR(14) 1.29 (1.8% of price) | annualised 20d 18.6%
Volume: 0.44x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.10</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score +0.10</summary>

```text
Fund type: Financial
What it holds: P/E 12.02 | P/B 1.21 | P/S 3.59 | 3y earnings growth n/a
Yield: 2.3%
Three-year record: +25.1% a year | beta to the market 1.04
Cost and size: expense ratio 0.35% | net assets 3.73B
What it is made of: Stocks 99.8%, Cash 0.2%
Largest holdings: United Bankshares Inc 1.1%, First Interstate BancSystem Inc 1.1%, Old National Bancorp 1.1%, Hancock Whitney Corp 1.1%, East West Bancorp Inc 1.1%
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

<details><summary><b>What analysts and big funds say</b> — score +0.20</summary>

_Not available today._

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score +0.20</summary>

```text
Rolled up from the 5 largest holdings, 5.7% of the fund by weight  -- thin, so read this as a fact about that slice rather than the fund
Ratings by weight: buy 59.8% | hold 40.2% | sell 0.0% (mean 2.24 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +9.8% above the current prices
Holdings read: UBSI, FIBK, ONB, HWC, EWBC
Recent rating changes among them:
  - UBSI: 2026-07-27 Keefe, Bruyette & Woods: main, Market Perform -> Market Perform
  - FIBK: 2026-10-05 Barclays: main, Underweight -> Underweight
  - ONB: 2026-10-22 TD Cowen: main, Buy -> Buy
  - HWC: 2026-10-21 Keefe, Bruyette & Woods: main, Market Perform -> Market Perform
  - EWBC: 2026-10-22 Citigroup: main, Buy -> Buy
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
Share count change: 1 week: -2.2% (-84.46M) over 7d | 1 month: -4.2% (-168.37M) over 30d
Shares outstanding: 52.81M | fund size: 3.82B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Saudi Arabia (KSA) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Mixed signals: bullish analyst coverage and modest weekly inflow versus bearish technicals and weak fundamentals lead to a neutral overall stance.

**Main reasons it gave:**
- Analyst view: 90% buy rating with +24% price target
- Weekly fund inflow: +3.6% share count increase
- Technicals: price below 20d, 50d, 200d SMAs and RSI 17.3 (oversold)
- Fundamentals: low three-year return (+0.6% per year) and high expense ratio (0.75%)

<details><summary><b>News</b> — score +0.00</summary>

_No news found for this one today._

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.04% (-0.03 on the week) | 5-year 4.81% (-0.09 on the week) | 10-year 4.99% (-0.11 on the week) | 30-year 5.31% (-0.12 on the week)
Yield curve, 10-year minus 3-month: +0.95 points -- upward sloping (normal)
US dollar index: 101.76 (-0.08 on the week)
Volatility (VIX): 20.36 (+0.4 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.2% (2026-09-01) | jobless claims 194k (2026-10-17)
Policy and expectations: Fed target 4.00% | market expects 2.3% inflation over 10 years
Rate path: 2-year Treasury 4.81% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score -0.30</summary>

```text
Last close 33.69 (bar of 2026-10-23), from 502 daily bars
Trend: vs 20d SMA 35.65 (-5.5%), 50d 37.14 (-9.3%), 200d 38.04 (-11.4%); 50d below 200d
Momentum: RSI(14) 17.3 | MACD -0.850 vs signal -0.677 (histogram -0.173)
Returns: 1d -0.0% | 5d -4.0% | 1m -8.7% | 3m -8.9%
52-week range: 33.69 - 41.03 (now 0.0% of the way up)
Volatility: ATR(14) 0.35 (1.0% of price) | annualised 20d 14.3%
Volume: 0.41x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.00</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score +0.00</summary>

```text
Fund type: Focused Region
What it holds: P/E 14.08 | P/B 1.70 | P/S 2.84 | 3y earnings growth n/a
Yield: 2.8%
Three-year record: +0.6% a year | beta to the market 0.19
Cost and size: expense ratio 0.75% | net assets 588.43M
What it is made of: Stocks 99.6%, Cash 0.4%
Largest holdings: Al Rajhi Bank 14.1%, Saudi Arabian Oil Co 11.5%, Saudi National Bank 8.6%, Saudi Telecom Co 6.1%, Saudi Arabian Mining Co 4.3%
Sector mix: Financial services 42.2%, Energy 12.5%, Basic materials 12.4%, Communication services 9.0%
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
Rolled up from the 5 largest holdings, 44.6% of the fund by weight
Ratings by weight: buy 90.3% | hold 9.7% | sell 0.0% (mean 2.06 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +24.2% above the current prices
Holdings read: 1120.SR, 2222.SR, 1180.SR, 7010.SR, 1211.SR
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
Share count change: 1 week: +3.6% (20.10M) over 7d | 1 month: -0.1% (-676.11K) over 30d
Shares outstanding: 17.00M | fund size: 572.80M
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

**Data that was missing** (counted as 0.00, never guessed):
- news unavailable: Bright Data returned an empty body with its 200; nothing to parse (Bright Data said: x-brd-status-code 502; x-brd-error waiting for selector "#main" failed: timeout 30000ms exceeded)

### China (MCHI) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> No material macro surprise, technicals mixed, modest flow, bullish analyst view limited in coverage.

**Main reasons it gave:**
- Technical trend down: price below 20‑day, 50‑day and 200‑day SMAs, RSI 27.9 (oversold) with low volume
- Macro data stable: US inflation 3.7% near target, no surprise in rates, upward‑sloping yield curve
- Analyst coverage limited to 32.3% of fund, all buy with +69.4% price target but limited weight
- Fund flows modestly positive: weekly share count +4.1% but monthly only +0.3%, indicating limited new demand

<details><summary><b>News</b> — score +0.00</summary>

- [MCHI May 2027 60.000 call (MCHI270521C00060000) interactive stock chart – Yahoo Finance](https://sg.finance.yahoo.com/quote/MCHI270521C00060000/chart/)  
  <sub>Yahoo Finance Singapore, 23 hours ago</sub>  
  Interactive chart for MCHI May 2027 60.000 call (MCHI270521C00060000) – analyse all of the data with a huge range of indicators.
- [How to Buy Tencent Stock (TCEHY) in 2026](https://www.fool.com/investing/how-to-invest/stocks/how-to-invest-in-tencent-stock/)  
  <sub>The Motley Fool, 17 hours ago</sub>  
  Tencent is a huge Chinese technology company. Its stock trades on the OTC market, but you can buy shares through most brokerages. Here's what you need to...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.04% (-0.03 on the week) | 5-year 4.81% (-0.09 on the week) | 10-year 4.99% (-0.11 on the week) | 30-year 5.31% (-0.12 on the week)
Yield curve, 10-year minus 3-month: +0.95 points -- upward sloping (normal)
US dollar index: 101.76 (-0.08 on the week)
Volatility (VIX): 20.36 (+0.4 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.2% (2026-09-01) | jobless claims 194k (2026-10-17)
Policy and expectations: Fed target 4.00% | market expects 2.3% inflation over 10 years
Rate path: 2-year Treasury 4.81% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score -0.20</summary>

```text
Last close 49.04 (bar of 2026-10-23), from 502 daily bars
Trend: vs 20d SMA 51.44 (-4.7%), 50d 53.05 (-7.5%), 200d 56.08 (-12.5%); 50d below 200d
Momentum: RSI(14) 27.9 | MACD -0.920 vs signal -0.692 (histogram -0.229)
Returns: 1d +0.1% | 5d -4.2% | 1m -7.1% | 3m -9.6%
52-week range: 49.02 - 65.59 (now 0.2% of the way up)
Volatility: ATR(14) 0.68 (1.4% of price) | annualised 20d 17.7%
Volume: 0.26x the 20-day average
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
Three-year record: +9.7% a year | beta to the market 0.45
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

<details><summary><b>What analysts and big funds say</b> — score +0.40</summary>

_Not available today._

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score +0.40</summary>

```text
Rolled up from the 5 largest holdings, 32.3% of the fund by weight
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 1.42 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +69.4% above the current prices
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
Share count change: 1 week: +4.1% (233.27M) over 7d | 1 month: +0.3% (19.69M) over 30d
Shares outstanding: 119.43M | fund size: 5.86B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Chip makers (SMH) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Neutral overall; bullish analyst view and strong inflows are offset by weak technicals and a stable macro backdrop with no surprise data.

**Main reasons it gave:**
- Analyst consensus all buy with weighted price target +50.3% above current price
- Fund flows show strong inflows: share count up 13.7% over past month
- Technical indicators weak: price below 20‑day and 50‑day SMA, RSI 35.2, MACD negative
- Macro environment stable: yields down slightly, no surprise data

<details><summary><b>News</b> — score +0.00</summary>

- [Is iShares Semiconductor ETF (SOXX) a Strong ETF Right Now?](https://finance.yahoo.com/markets/stocks/articles/ishares-semiconductor-etf-soxx-strong-092002545.html)  
  <sub>Yahoo Finance, 6 hours ago</sub>  
  Designed to provide broad exposure to the Technology ETFs category of the market, the iShares Semiconductor ETF (SOXX) is a smart beta exchange traded fund...
- [VanEck Semiconductor ETF Cert Deposito Arg Repr 0.02 Estimates – BCBA:SMH](https://www.tradingview.com/symbols/BCBA-SMH/financials-estimates/)  
  <sub>TradingView, 3 hours ago</sub>  
  Explore reported financial data and analyst estimates across the income statement, balance sheet, cash flow statement, and valuation metrics.
- [SOXX, SOXL, SMH Plunge As Chip Stocks Sell Off Amid Supply Chain Concerns](https://stocktwits.com/news-articles/markets/equity/soxx-soxl-smh-plunge-as-chip-stocks-sell-off-amid-supply-chain-concerns/cZxUCbMRBDF)  
  <sub>Stocktwits, 13 hours ago</sub>  
  The iShares Semiconductor ETF fell nearly 7% at close, while the Direxion Daily Semiconductor Bull 3X Shares plunged more than 20%, and the VanEck...
- [A $1.3T Equity-Fund Rush Is Shattering Records. These Tech ETFs Are in Play - VanEck Semiconductor ETF (N](https://www.benzinga.com/etfs/broad-u-s-equity-etfs/26/10/62559118/1-3-trillion-equity-fund-rush-is-shattering-records-tech-etfs-that-are-in-play)  
  <sub>Benzinga, 1 hour ago</sub>  
  Global equity funds are on track for record $1.3 trillion in 2026 inflows. Here's what VOO and semiconductor ETF flows reveal about investor demand.
- [VanEck Semiconductor ETF (SMH) Options Chain](https://ca.finance.yahoo.com/quote/SMH/options/?date=1795737600&straddle=false&type=all)  
  <sub>Yahoo! Finance Canada, 21 hours ago</sub>  
  View the basic SMH option chain and compare options of VanEck Semiconductor ETF on Yahoo Finance.
- [SOXX Is Splitting 3-for-1 Again: What Changes for Your Shares and What Doesn’t](https://247wallst.com/investing/etf/2026/10/22/soxx-is-splitting-3-for-1-again-what-changes-for-your-shares-and-what-doesnt/)  
  <sub>24/7 Wall St., 24 hours ago</sub>  
  SOXX splits 3-for-1 on November 5, 2026, tripling each shareholder's count while the fund trades near $492, down 12% over the past month.
- [SOXL Sinks To 6-Month Low As Nasdaq Slides Amid Oil Surge: Trump Blames Iran, But Wells Fargo Says Huang’s Comments Spooked Markets](https://www.tradingview.com/news/stocktwits:b00a7d78b094b:0-soxl-sinks-to-6-month-low-as-nasdaq-slides-amid-oil-surge-trump-blames-iran-but-wells-fargo-says-huang-s-comments-spooked-markets/)  
  <sub>TradingView, 22 hours ago</sub>  
  U.S. President Donald Trump blamed Iran on Thursday for the surge in oil prices as a purposeful ploy ahead of the U.S. midterm elections.
- [The Zacks Analyst Blog Highlights SHOC, XSD, FTXL, CHPS and SMH](https://www.zacks.com/stock/news/3013452/the-zacks-analyst-blog-highlights-shoc-xsd-ftxl-chps-and-smh)  
  <sub>Zacks Investment Research, 7 hours ago</sub>  
  SHOC, XSD, FTXL, CHPS and SMH offer semiconductor exposure as chip demand fuels growth forecasts, while oversupply risks and Chinese competition cloud the...
- [Bill Baruch market update: SMH & QQQ slide, RSP, WMT, LLY, AAPL rise, GLD pressured](https://www.theglobeandmail.com/investing/markets/indices/TTGD/pressreleases/8341118/bill-baruch-market-update-smh-qqq-slide-rsp-wmt-lly-aapl-rise-gld-pressured/)  
  <sub>The Globe and Mail, 17 hours ago</sub>  
  Ugly day led by $SMH $QQQ. On bright side $RSP $WMT $LLY $AAPL +. Also $GLD bludgeoned despite $TLT #USD central bank buying and great ETF flows.
- [Nvidia's AI Warning, $111 Oil: Why SOXL Just Suffered a Brutal 20% Wipeout](https://www.benzinga.com/etfs/specialty-etfs/26/10/62545840/nvidias-ai-warning-111-oil-why-soxl-just-suffered-a-brutal-20-wipeout)  
  <sub>Benzinga, 19 hours ago</sub>  
  SOXL dropped to a six-month low as chip stocks came under pressure. Nvidia CEO's warning and a surge in oil prices may hold clues to what spooked investors.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.04% (-0.03 on the week) | 5-year 4.81% (-0.09 on the week) | 10-year 4.99% (-0.11 on the week) | 30-year 5.31% (-0.12 on the week)
Yield curve, 10-year minus 3-month: +0.95 points -- upward sloping (normal)
US dollar index: 101.76 (-0.08 on the week)
Volatility (VIX): 20.36 (+0.4 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.2% (2026-09-01) | jobless claims 194k (2026-10-17)
Policy and expectations: Fed target 4.00% | market expects 2.3% inflation over 10 years
Rate path: 2-year Treasury 4.81% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score -0.30</summary>

```text
Last close 531.24 (bar of 2026-10-23), from 502 daily bars
Trend: vs 20d SMA 585.75 (-9.3%), 50d 575.17 (-7.6%), 200d 515.46 (+3.1%); 50d above 200d
Momentum: RSI(14) 35.2 | MACD -13.635 vs signal -5.017 (histogram -8.618)
Returns: 1d +1.5% | 5d -1.6% | 1m -11.5% | 3m -3.2%
52-week range: 325.10 - 668.91 (now 60.0% of the way up)
Volatility: ATR(14) 17.46 (3.3% of price) | annualised 20d 34.3%
Volume: 0.39x the 20-day average
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
Three-year record: +58.3% a year | beta to the market 2.00
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

<details><summary><b>What analysts and big funds say</b> — score +0.50</summary>

_Not available today._

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score +0.50</summary>

```text
Rolled up from the 5 largest holdings, 44.3% of the fund by weight
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 1.34 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +50.3% above the current prices
Holdings read: NVDA, TSM, AMD, AVGO, MU
Recent rating changes among them:
  - NVDA: 2026-10-22 Needham: reit, Buy -> Buy
  - TSM: 2026-10-16 Barclays: main, Overweight -> Overweight
  - AMD: 2026-10-21 Susquehanna: main, Positive -> Positive
  - AVGO: 2026-10-22 Tigress Financial: init, ? -> Buy
  - MU: 2026-10-22 Rosenblatt: main, Buy -> Buy
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
Share count change: 1 week: +5.7% (3.83B) over 7d | 1 month: +13.7% (8.58B) over 30d
Shares outstanding: 134.49M | fund size: 71.45B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Turkey (TUR) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Neutral overall; no macro surprise, flat fund flows, modest bullish analyst rating limited to 43.2% of holdings, fundamentals are low‑valuation but flat performance, technicals oversold but no decisive break and low volume.

**Main reasons it gave:**
- Analyst view: 100% buy for 43.2% of fund (mean rating 1.69) → modest bullish
- Fund flows flat: 0% share count change over week and month
- Fundamentals: low P/E 11.69, P/B 1.02 but 3‑yr return 0% → neutral
- Technicals: price 21.5% below 200‑day SMA, RSI 25.2, low volume, no decisive break

<details><summary><b>News</b> — score +0.00</summary>

_No news found for this one today._

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.04% (-0.03 on the week) | 5-year 4.81% (-0.09 on the week) | 10-year 4.99% (-0.11 on the week) | 30-year 5.31% (-0.12 on the week)
Yield curve, 10-year minus 3-month: +0.95 points -- upward sloping (normal)
US dollar index: 101.76 (-0.08 on the week)
Volatility (VIX): 20.36 (+0.4 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.2% (2026-09-01) | jobless claims 194k (2026-10-17)
Policy and expectations: Fed target 4.00% | market expects 2.3% inflation over 10 years
Rate path: 2-year Treasury 4.81% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 30.76 (bar of 2026-10-23), from 502 daily bars
Trend: vs 20d SMA 33.49 (-8.2%), 50d 36.96 (-16.8%), 200d 39.17 (-21.5%); 50d below 200d
Momentum: RSI(14) 25.2 | MACD -1.534 vs signal -1.393 (histogram -0.141)
Returns: 1d -1.1% | 5d -5.3% | 1m -15.9% | 3m -20.5%
52-week range: 30.76 - 43.74 (now 0.0% of the way up)
Volatility: ATR(14) 0.70 (2.3% of price) | annualised 20d 26.3%
Volume: 0.33x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.25</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score +0.25</summary>

```text
Fund type: Focused Region
What it holds: P/E 11.69 | P/B 1.02 | P/S 0.63 | 3y earnings growth n/a
Yield: 2.5%
Three-year record: +0.0% a year | beta to the market 0.61
Cost and size: expense ratio 0.59% | net assets 163.33M
What it is made of: Stocks 99.7%, Cash 0.3%
Largest holdings: Aselsan Elektronik Sanayi Ve Ticaret AS 11.4%, Tupras-Turkiye Petrol Rafineleri AS 10.6%, Bim Birlesik Magazalar AS 10.4%, Akbank TAS 6.1%, Turk Hava Yollari AO 4.8%
Sector mix: Industrials 29.2%, Financial services 16.1%, Consumer defensive 13.9%, Basic materials 11.4%
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

<details><summary><b>What analysts and big funds say</b> — score +0.28</summary>

_Not available today._

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score +0.28</summary>

```text
Rolled up from the 5 largest holdings, 43.2% of the fund by weight
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 1.69 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +33.9% above the current prices
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
Shares outstanding: 15.65M | fund size: 481.39M
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### US real estate (VNQ) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Neutral overall: bullish analyst coverage is offset by net outflows and mixed technicals in a high‑yield environment.

**Main reasons it gave:**
- Analyst coverage: 100% buy, mean rating 1.62, price target +17.7% above current price
- Fund flows: net outflows of -4.7% over past month indicating bearish demand
- Technicals: price above 20‑day SMA but below 50‑day/200‑day SMAs, MACD bullish but low volume, mixed momentum
- Macro: high yields (10‑yr 4.99%) and upward‑sloping curve, inflation 3.7% above target

<details><summary><b>News</b> — score +0.00</summary>

- [3 Vanguard ETFs Pay Up to 3.71%, and One Is Beating the S&P 500](https://247wallst.com/investing/etf/2026/10/22/3-vanguard-etfs-pay-up-to-3-71-and-one-is-beating-the-sp-500/)  
  <sub>24/7 Wall St., 16 hours ago</sub>  
  Three Vanguard ETFs offer yields as high as 3.71%, but their total returns over the past year tell very different stories about which one actually rewarded...
- [Three Vanguard ETFs offer yields up to 3.71%, b...](https://pluang.com/en/news-feed/3-etf-vanguard-bayar-dividen-tinggi-satu-lebih-baik-dari-sp500)  
  <sub>Pluang, 16 hours ago</sub>  
  Three Vanguard ETFs—Vanguard International High Dividend Yield (VYMI), Vanguard Real Estate (VNQ), and Vanguard Utilities (VPU)—pay yields between 2.9% and...
- [Howard Hughes, Millrose Properties lead list of undervalued real estate stocks (VNQ:NYSEARCA)](https://seekingalpha.com/news/4656523-howard-hughes-millrose-properties-lead-list-of-undervalued-real-estate-stocks)  
  <sub>Seeking Alpha, 3 hours ago</sub>  
  Funtap/iStock via Getty Images. As the third-quarter 2026 earnings season unfolds, investors are assessing valuations across the U.S. real estate sector,...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.04% (-0.03 on the week) | 5-year 4.81% (-0.09 on the week) | 10-year 4.99% (-0.11 on the week) | 30-year 5.31% (-0.12 on the week)
Yield curve, 10-year minus 3-month: +0.95 points -- upward sloping (normal)
US dollar index: 101.76 (-0.08 on the week)
Volatility (VIX): 20.36 (+0.4 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.2% (2026-09-01) | jobless claims 194k (2026-10-17)
Policy and expectations: Fed target 4.00% | market expects 2.3% inflation over 10 years
Rate path: 2-year Treasury 4.81% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 92.83 (bar of 2026-10-23), from 502 daily bars
Trend: vs 20d SMA 90.66 (+2.4%), 50d 93.72 (-0.9%), 200d 94.53 (-1.8%); 50d below 200d
Momentum: RSI(14) 54.8 | MACD -0.270 vs signal -0.771 (histogram 0.502)
Returns: 1d +0.2% | 5d +1.2% | 1m +1.8% | 3m -7.7%
52-week range: 87.00 - 100.95 (now 41.8% of the way up)
Volatility: ATR(14) 1.28 (1.4% of price) | annualised 20d 14.8%
Volume: 0.38x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score -0.20</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score -0.20</summary>

```text
Fund type: Real Estate
What it holds: P/E 28.36 | P/B 2.42 | P/S 4.59 | 3y earnings growth n/a
Yield: 3.8%
Three-year record: +12.4% a year | beta to the market 0.98
Cost and size: expense ratio 0.13% | net assets 66.42B
What it is made of: Stocks 99.0%, Cash 0.7%, Other 0.3%
Largest holdings: Vanguard Real Estate II Index 14.5%, Welltower Inc 9.1%, Prologis Inc 6.9%, Equinix Inc 5.7%, American Tower Corp 4.3%
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

<details><summary><b>What analysts and big funds say</b> — score +0.80</summary>

_Not available today._

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score +0.80</summary>

```text
Rolled up from the 5 largest holdings, 40.5% of the fund by weight
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 1.62 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +17.7% above the current prices
Holdings read: VRTPX, WELL, PLD, EQIX, AMT
Recent rating changes among them:
  - WELL: 2026-10-19 Wells Fargo: main, Overweight -> Overweight
  - PLD: 2026-10-21 Raymond James: up, Market Perform -> Outperform
  - EQIX: 2026-10-21 CIBC: init, ? -> Outperformer
  - AMT: 2026-10-20 Bernstein: main, Outperform -> Outperform
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
Share count change: 1 week: -0.3% (-229.27M) over 7d | 1 month: -4.7% (-3.32B) over 30d
Shares outstanding: 726.20M | fund size: 67.41B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Biotech (XBI) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Mixed signals: modest analyst bullishness (61% buy, +3.7% price target) offset by notable outflows (-6.8% month) and technicals showing price below short‑term averages with low volume. No macro surprise or decisive technical break.

**Main reasons it gave:**
- Fund flows show net outflows of -6.8% over the past month (67.82M shares, -739M USD)
- Analyst coverage of top holdings (9.2% of fund) is 61% buy, 39% hold, with a weighted price target +3.7% above current price
- Technicals: price below 20‑day (151.71) and 50‑day (157.26) SMAs, RSI 44.8, MACD slightly bullish, volume at 0.24× 20‑day average
- Macro: Treasury yields up slightly, VIX elevated at 20.36, no policy surprise

<details><summary><b>News</b> — score +0.00</summary>

- [Options Whale Alert: $471K Bullish Long Call Opened on $XBI](https://www.moomoo.com/news/post/1002080973/options-whale-alert-471k-bullish-long-call-opened-on-xbi)  
  <sub>Moomoo, 15 hours ago</sub>  
  SPDRS&P Biotech ETF(XBI.US)$ closed down 0.75% at $151.64. A trader bought 333 Jun 17, 2027 $158.00 calls to open a Long Call. The position carries a net...
- [Ionis Pharmaceuticals Secures FDA Orphan Drug Designation For Rare Epilepsy Treatment](https://stocktwits.com/news-articles/markets/equity/ionis-pharmaceuticals-secures-fda-orphan-drug-designation-for-rare-epilepsy-treatment/cZxw0yGRBDO)  
  <sub>Stocktwits, 21 hours ago</sub>  
  The treatment targets the SCN1A gene, which helps the brain produce a protein that controls electrical activity and prevents seizures.
- [Flow Focus | Tech Falls Behind. Is Old-School Wall Street Back?](https://www.moomoo.com/community/feed/flow-focus-tech-falls-behind-is-old-school-wall-street-117489058250758)  
  <sub>Moomoo, 7 hours ago</sub>  
  The $Dow Jones Industrial Average (.DJI.US)$ held its ground while tech sold off. In the supplied weekly snapshot, industrials, regional banks and bio...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.04% (-0.03 on the week) | 5-year 4.81% (-0.09 on the week) | 10-year 4.99% (-0.11 on the week) | 30-year 5.31% (-0.12 on the week)
Yield curve, 10-year minus 3-month: +0.95 points -- upward sloping (normal)
US dollar index: 101.76 (-0.08 on the week)
Volatility (VIX): 20.36 (+0.4 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.2% (2026-09-01) | jobless claims 194k (2026-10-17)
Policy and expectations: Fed target 4.00% | market expects 2.3% inflation over 10 years
Rate path: 2-year Treasury 4.81% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 149.27 (bar of 2026-10-23), from 502 daily bars
Trend: vs 20d SMA 151.71 (-1.6%), 50d 157.26 (-5.1%), 200d 140.87 (+6.0%); 50d above 200d
Momentum: RSI(14) 44.8 | MACD -1.849 vs signal -2.151 (histogram 0.303)
Returns: 1d -1.6% | 5d +3.4% | 1m -4.3% | 3m -0.9%
52-week range: 107.56 - 169.55 (now 67.3% of the way up)
Volatility: ATR(14) 4.41 (3.0% of price) | annualised 20d 32.3%
Volume: 0.24x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.20</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score +0.20</summary>

```text
Fund type: Health
What it holds: P/E n/a | P/B 0.21 | P/S 0.12 | 3y earnings growth n/a
Yield: 0.3%
Three-year record: +31.9% a year | beta to the market 1.09
Cost and size: expense ratio 0.35% | net assets 10.36B
What it is made of: Stocks 100.0%, Cash 0.0%
Largest holdings: Twist Bioscience Corp 2.2%, Moderna Inc 2.0%, Natera Inc 1.8%, Iovance Biotherapeutics Inc 1.6%, Amgen Inc 1.5%
Sector mix: Healthcare 99.3%, Financial services 0.7%
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
Rolled up from the 5 largest holdings, 9.2% of the fund by weight  -- thin, so read this as a fact about that slice rather than the fund
Ratings by weight: buy 61.1% | hold 38.9% | sell 0.0% (mean 2.09 on a 1=strong buy to 5=strong sell scale)
Weighted price target: -3.7% above the current prices
Holdings read: TWST, MRNA, NTRA, IOVA, AMGN
Recent rating changes among them:
  - TWST: 2026-10-13 TD Cowen: main, Buy -> Buy
  - MRNA: 2026-10-21 TD Cowen: main, Hold -> Hold
  - NTRA: 2026-10-19 Canaccord Genuity: main, Buy -> Buy
  - IOVA: 2026-10-13 Barclays: main, Overweight -> Overweight
  - AMGN: 2026-10-21 Barclays: main, Equal-Weight -> Equal-Weight
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
Share count change: 1 week: -3.9% (-413.87M) over 7d | 1 month: -6.8% (-739.08M) over 30d
Shares outstanding: 67.82M | fund size: 10.12B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### US house builders (XHB) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> No material macro surprise, technicals mixed, modest inflows, analyst view positive but thin coverage.

**Main reasons it gave:**
- Analyst coverage thin (17% weight) but all buy with +16.8% price target
- Fund flows net +8.3% over past month indicating modest demand
- Technical indicators mixed: price above 20‑day SMA but below 50‑day and 200‑day SMA, MACD above signal
- Homebuilder sector down 30% from peak yet rallying on recent yield drop; 10‑year yield fell 0.11% to 4.99% with no policy surprise

<details><summary><b>News</b> — score +0.00</summary>

- [Homebuilder ETF ITB Down 30% As Builder Profits Fall Faster - iShares U.S. Home Construction ETF (BATS:IT](https://www.benzinga.com/opinion/26/10/62561030/rise-and-fall-of-homebuilders-what-drove-itbs-30-drop)  
  <sub>Benzinga, 43 minutes ago</sub>  
  ITB, the biggest homebuilder ETF, is 30% below its October 2024 peak. Builders' earnings fell faster than its price, so its P/E is above its median.
- [Ten-Year Yield Falls Below 5%: 10 Real-Estate Stocks Rally - iShares U.S. Home Construction ETF (BATS:ITB](https://www.benzinga.com/real-estate/26/10/62545365/10-year-treasury-yield-falls-homebuilder-real-estate-stocks-rally)  
  <sub>Benzinga, 19 hours ago</sub>  
  Homebuilders rally as the 10-year Treasury yield falls below 5%. Lennar, KB Home and Zillow lead while REITs lag ahead of next week's Fed meeting.
- [BlueSphere US Equity UCITS ETF HUF HdgAcc (BSUH.AS) stock historical prices and data](https://sg.finance.yahoo.com/quote/BSUH.AS/history/)  
  <sub>Yahoo Finance Singapore, 16 hours ago</sub>  
  BlueSphere US Equity UCITS ETF HUF HdgAcc (BSUH.AS). 3,199.63 -38.32 (-1.18%). At close: 22 October at 9:04:17 am GMT+2. 22 Oct 2025 - 22 Oct 2026.
- [Xtr-MSCI Wld Min.Vola.ESG ETF R (XWEB.HA) performance history](https://au.finance.yahoo.com/quote/XWEB.HA/performance/)  
  <sub>Yahoo Finance Australia, 15 hours ago</sub>  
  Current and historical performance for Xtr-MSCI Wld Min.Vola.ESG ETF R on Yahoo Finance.
- [iShsV-iBds Dec 2027 Te.EO Co. R (FCEBD.DE) company profile and facts](https://au.finance.yahoo.com/quote/FCEBD.DE/profile/)  
  <sub>Yahoo Finance Australia, 12 hours ago</sub>  
  See the company profile for iShsV-iBds Dec 2027 Te.EO Co. R (FCEBD.DE), including business summary, industry/sector information, number of employees,...
- [BSF - BlackRock MIPD A (XMHT.DU)](https://sg.finance.yahoo.com/quote/XMHT.DU/holdings/)  
  <sub>Yahoo Finance Singapore, 21 hours ago</sub>  
  Holdings data is currently unavailable for XMHT.DU. Related tickers. ITB iShares U.S. Home Construction ETF. 90.40 +4.42%. FSTA Fidelity MSCI Consumer...
- [Corgi FTSE 5–10 Year IG Corporate Bond ETF (FTN) options chain](https://au.finance.yahoo.com/quote/FTN/options/)  
  <sub>Yahoo Finance Australia, 20 hours ago</sub>  
  Contract name, Last trade date (GMT-4), Strike, Last price, Bid, Ask, Change, % change, Volume, Open interest, Implied volatility...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.04% (-0.03 on the week) | 5-year 4.81% (-0.09 on the week) | 10-year 4.99% (-0.11 on the week) | 30-year 5.31% (-0.12 on the week)
Yield curve, 10-year minus 3-month: +0.95 points -- upward sloping (normal)
US dollar index: 101.76 (-0.08 on the week)
Volatility (VIX): 20.36 (+0.4 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.2% (2026-09-01) | jobless claims 194k (2026-10-17)
Policy and expectations: Fed target 4.00% | market expects 2.3% inflation over 10 years
Rate path: 2-year Treasury 4.81% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 98.51 (bar of 2026-10-23), from 502 daily bars
Trend: vs 20d SMA 95.93 (+2.7%), 50d 99.40 (-0.9%), 200d 105.46 (-6.6%); 50d below 200d
Momentum: RSI(14) 54.4 | MACD -0.590 vs signal -1.260 (histogram 0.670)
Returns: 1d -0.7% | 5d +3.8% | 1m +1.8% | 3m -9.8%
52-week range: 92.84 - 121.36 (now 19.9% of the way up)
Volatility: ATR(14) 2.33 (2.4% of price) | annualised 20d 25.2%
Volume: 0.29x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.00</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score +0.00</summary>

```text
Fund type: Consumer Cyclical
What it holds: P/E 18.56 | P/B 2.09 | P/S 1.23 | 3y earnings growth n/a
Yield: 1.2%
Three-year record: +11.4% a year | beta to the market 1.48
Cost and size: expense ratio 0.35% | net assets 1.43B
What it is made of: Stocks 99.9%, Cash 0.1%
Largest holdings: SharkNinja Inc 3.5%, Cavco Industries Inc 3.4%, Champion Homes Inc 3.4%, Johnson Controls International PLC Registered Shares 3.4%, Wayfair Inc Class A 3.4%
Sector mix: Consumer cyclical 63.4%, Industrials 31.7%, Basic materials 3.2%, Real estate 1.8%
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
Rolled up from the 5 largest holdings, 17.0% of the fund by weight  -- thin, so read this as a fact about that slice rather than the fund
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 1.79 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +16.8% above the current prices
Holdings read: SN, CVCO, SKY, JCI, W
Recent rating changes among them:
  - SN: 2026-10-19 JP Morgan: main, Overweight -> Overweight
  - CVCO: 2026-09-30 Oppenheimer: init, ? -> Outperform
  - SKY: 2026-10-15 RBC Capital: main, Outperform -> Outperform
  - JCI: 2026-10-15 Mizuho: main, Neutral -> Neutral
  - W: 2026-10-23 RBC Capital: main, Sector Perform -> Sector Perform
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
Share count change: 1 week: -1.0% (-15.53M) over 7d | 1 month: +8.3% (112.73M) over 30d
Shares outstanding: 14.96M | fund size: 1.47B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### US media and communication (XLC) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> No macro surprise, no decisive technical break, mixed signals: bearish technicals vs bullish analyst view and positive fund flows. Default to neutral.

**Main reasons it gave:**
- Price below 20‑day, 50‑day and 200‑day SMAs (down 3.7‑6.0%)
- RSI 35.1; MACD histogram -0.481 (negative)
- Analyst coverage 90.6% buy, weighted price target +26.6% above current
- Fund flows: share count increased 3% week‑over‑week

<details><summary><b>News</b> — score +0.00</summary>

_No news found for this one today._

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.04% (-0.03 on the week) | 5-year 4.81% (-0.09 on the week) | 10-year 4.99% (-0.11 on the week) | 30-year 5.31% (-0.12 on the week)
Yield curve, 10-year minus 3-month: +0.95 points -- upward sloping (normal)
US dollar index: 101.76 (-0.08 on the week)
Volatility (VIX): 20.36 (+0.4 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.2% (2026-09-01) | jobless claims 194k (2026-10-17)
Policy and expectations: Fed target 4.00% | market expects 2.3% inflation over 10 years
Rate path: 2-year Treasury 4.81% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score -0.40</summary>

```text
Last close 106.52 (bar of 2026-10-23), from 502 daily bars
Trend: vs 20d SMA 110.57 (-3.7%), 50d 111.62 (-4.6%), 200d 113.29 (-6.0%); 50d below 200d
Momentum: RSI(14) 35.1 | MACD -0.976 vs signal -0.495 (histogram -0.481)
Returns: 1d -0.8% | 5d -3.4% | 1m -6.6% | 3m -1.1%
52-week range: 105.38 - 120.08 (now 7.8% of the way up)
Volatility: ATR(14) 1.72 (1.6% of price) | annualised 20d 16.0%
Volume: 0.25x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.50</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score +0.50</summary>

```text
Fund type: Communications
What it holds: P/E 16.28 | P/B 3.24 | P/S 2.42 | 3y earnings growth n/a
Yield: 1.2%
Three-year record: +19.2% a year | beta to the market 0.85
Cost and size: expense ratio 0.08% | net assets 22.53B
What it is made of: Stocks 99.8%, Cash 0.2%
Largest holdings: Meta Platforms Inc Class A 22.2%, Alphabet Inc Class A 11.6%, Alphabet Inc Class C 9.3%, Warner Bros. Discovery Inc Ordinary Shares - Class A 4.9%, The Walt Disney Co 4.5%
Sector mix: Communication services 100.0%
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

<details><summary><b>What analysts and big funds say</b> — score +0.75</summary>

_Not available today._

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score +0.75</summary>

```text
Rolled up from the 5 largest holdings, 52.5% of the fund by weight
Ratings by weight: buy 90.6% | hold 9.4% | sell 0.0% (mean 1.52 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +26.6% above the current prices
Holdings read: META, GOOGL, GOOG, WBD, DIS
Recent rating changes among them:
  - META: 2026-10-22 UBS: main, Buy -> Buy
  - GOOGL: 2026-10-22 Citizens: main, Market Outperform -> Market Outperform
  - GOOG: 2026-10-15 JP Morgan: main, Overweight -> Overweight
  - WBD: 2026-09-29 Argus Research: down, Hold -> Sell
  - DIS: 2026-10-16 Citigroup: main, Buy -> Buy
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
Share count change: 1 week: +3.0% (646.34M) over 7d | 1 month: +2.2% (473.65M) over 30d
Shares outstanding: 206.75M | fund size: 22.02B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

**Data that was missing** (counted as 0.00, never guessed):
- news unavailable: Bright Data returned an empty body with its 200; nothing to parse (Bright Data said: x-brd-status-code 502; x-brd-error waiting for selector "#main" failed: timeout 30000ms exceeded)

### US energy companies (XLE) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:** no explanation. It wrote only “NEUTRAL”, so the main reasons below are all it gave.

**Main reasons it gave:**
- Analyst view: 58.2% coverage, 100% buy rating
- Fund flows flat: 0% share count change over 1 week and 1 month
- Energy inventories mixed: crude draw (-3.1 mb, 15% percentile) and gas build (+77 bcf, 87% percentile)
- EIA forecast: WTI price expected to fall ~14% over six months
- Technicals: price 18.9% above 200-day SMA, RSI 68.9 (near overbought) but no decisive breakout

<details><summary><b>News</b> — score +0.00</summary>

- [Lower Fees, Higher Yield: Why XLE Tops XOP](https://finance.yahoo.com/energy/articles/lower-fees-higher-yield-why-130501575.html)  
  <sub>Yahoo Finance, 2 hours ago</sub>  
  Investors choosing between State Street Energy Select Sector SPDR ETF (NYSEMKT:XLE) and State Street SPDR S&P Oil & Gas Exploration & Production ETF...
- [Sector Update: Energy](https://ca.finance.yahoo.com/news/sector-energy-194357690.html)  
  <sub>Yahoo! Finance Canada, 19 hours ago</sub>  
  Energy stocks were lower late Thursday afternoon, with the NYSE Energy Sector Index falling 1.1% and the State Street Energy Select Sector SPDR ETF (XLE)...
- [Sector Update: Energy Stocks Decline Thursday Afternoon](https://ca.finance.yahoo.com/news/sector-energy-stocks-decline-thursday-175318835.html)  
  <sub>Yahoo! Finance Canada, 21 hours ago</sub>  
  Energy stocks were lower Thursday afternoon, with the NYSE Energy Sector Index falling 1% and the State Street Energy Select Sector SPDR ETF (XLE) shedding...
- [S&P 500 best performers: Zero mag 7 stocks past 13 weeks](https://www.thestreet.com/investing/sp-500-best-performers-zero-mag-7-stocks-past-13-weeks)  
  <sub>TheStreet, 14 hours ago</sub>  
  The biggest tech stocks have handed the baton as leadership has firmly shifted toward other S&P 500 sectors and industries.
- [Exchange-Traded Funds, Equity Futures Lower Pre-Bell Friday Amid AI Spending Concerns](https://finance.yahoo.com/markets/stocks/articles/exchange-traded-funds-equity-futures-131317616.html)  
  <sub>Yahoo Finance, 2 hours ago</sub>  
  The broad market exchange-traded fund SPDR S&P 500 ETF Trust (SPY) was down 0.2% and the actively tr.
- [Sector Update: Energy Stocks Decline Late Afternoon](https://finance.yahoo.com/energy/articles/sector-energy-stocks-decline-afternoon-195839307.html)  
  <sub>Yahoo Finance, 19 hours ago</sub>  
  Energy stocks were lower late Thursday afternoon, with the NYSE Energy Sector Index falling 1.1% and the State Street Energy Select Sector SPDR ETF (XLE)...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.04% (-0.03 on the week) | 5-year 4.81% (-0.09 on the week) | 10-year 4.99% (-0.11 on the week) | 30-year 5.31% (-0.12 on the week)
Yield curve, 10-year minus 3-month: +0.95 points -- upward sloping (normal)
US dollar index: 101.76 (-0.08 on the week)
Volatility (VIX): 20.36 (+0.4 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.2% (2026-09-01) | jobless claims 194k (2026-10-17)
Policy and expectations: Fed target 4.00% | market expects 2.3% inflation over 10 years
Rate path: 2-year Treasury 4.81% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 69.18 (bar of 2026-10-23), from 502 daily bars
Trend: vs 20d SMA 65.39 (+5.8%), 50d 64.34 (+7.5%), 200d 58.18 (+18.9%); 50d above 200d
Momentum: RSI(14) 68.9 | MACD 1.438 vs signal 1.139 (histogram 0.299)
Returns: 1d +2.4% | 5d +1.4% | 1m +10.5% | 3m +18.5%
52-week range: 43.60 - 69.18 (now 100.0% of the way up)
Volatility: ATR(14) 1.40 (2.0% of price) | annualised 20d 20.1%
Volume: 0.43x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score -0.10</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score -0.10</summary>

```text
Fund type: Equity Energy
What it holds: P/E 17.51 | P/B 2.47 | P/S 1.70 | 3y earnings growth n/a
Yield: 2.5%
Three-year record: +18.4% a year | beta to the market -0.03
Cost and size: expense ratio 0.08% | net assets 39.13B
What it is made of: Stocks 99.8%, Cash 0.2%
Largest holdings: ExxonMobil Holdings Corp 24.0%, Chevron Corp 18.1%, ConocoPhillips 6.7%, Valero Energy Corp 4.7%, Marathon Petroleum Corp 4.7%
Sector mix: Energy 100.0%
```

</details>

<details><summary><b>Does this company beat its own forecasts</b> — score -0.10</summary>

_Not available today._

</details>

<details><summary><b>What holding this fund costs you</b> — score -0.10</summary>

_Not available today._

</details>

<details><summary><b>How much oil and gas is in storage</b> — score -0.10</summary>

```text
US inventories, week ending 2026-10-16 (published the following Wednesday)
  Crude oil: 412.5 million barrels, -3.1 on the week (a draw), 15% percentile over 52 weeks
  Petrol: 205.3 million barrels, -3.0 on the week (a draw), 8% percentile over 52 weeks -- low for the time of year
  Diesel: 104.3 million barrels, +1.7 on the week (a build), 25% percentile over 52 weeks
  Natural gas: 3,644.0 billion cubic feet, +77.0 on the week (a build), 87% percentile over 52 weeks -- high for the time of year
A build is more supply than demand and a draw is the reverse, so a build reads bearish and a draw bullish -- as a rule of thumb, not a law. Weigh the change and how unusual the level is above the level itself, and remember the market has already seen this number.
```

</details>

<details><summary><b>How the crop is growing</b> — score -0.10</summary>

_Not available today._

</details>

<details><summary><b>What analysts and big funds say</b> — score +0.60</summary>

_Not available today._

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score +0.60</summary>

```text
Rolled up from the 5 largest holdings, 58.2% of the fund by weight
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 2.12 on a 1=strong buy to 5=strong sell scale)
Weighted price target: -1.0% above the current prices
Holdings read: XOM, CVX, COP, VLO, MPC
Recent rating changes among them:
  - XOM: 2026-10-19 Barclays: main, Overweight -> Overweight
  - CVX: 2026-10-15 Morgan Stanley: main, Overweight -> Overweight
  - COP: 2026-10-20 Susquehanna: main, Positive -> Positive
  - VLO: 2026-10-23 Wells Fargo: main, Overweight -> Overweight
  - MPC: 2026-10-22 TD Cowen: main, Buy -> Buy
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
Shares outstanding: 186.42M | fund size: 12.90B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### US banks and finance (XLF) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Neutral overall; no material macro surprise, flat fund flows, and technicals are indecisive despite positive analyst coverage.

**Main reasons it gave:**
- Analyst coverage of 42.7% of fund weight, all buy with +8.4% price target
- Fund flows flat: 0% change in share count over 1 week and 1 month
- Technical indicators neutral: RSI 56.3, price just below 50‑day SMA, low volume
- Macro environment unchanged: Treasury yields down modestly, inflation 3.7% near target, no surprise data

<details><summary><b>News</b> — score +0.00</summary>

- [What State Street Fin. Sel. Sector SPDR (XLF) Sold: Berkshire Leads on Wednesday](https://finance.yahoo.com/markets/stocks/articles/state-street-fin-sel-sector-110442304.html)  
  <sub>Yahoo Finance, 4 hours ago</sub>  
  This article first appeared on GuruFocus. State Street Financial Select Sector SPDR ETF (XLF) recorded a one-sided day of ETF activity on Wednesday,...
- [Sector Update: Financial Stocks Rise Late Afternoon](https://ca.finance.yahoo.com/news/sector-financial-stocks-rise-afternoon-195728507.html)  
  <sub>Yahoo! Finance Canada, 19 hours ago</sub>  
  Financial stocks were advancing in late Thursday afternoon trading, with the NYSE Financial Index ri.
- [Webull Brings Options into Pre-Market as Brokers Adopt Cboe’s New Sessions](https://www.tradingview.com/news/financemagnates:83d2b85b3094b:0-webull-brings-options-into-pre-market-as-brokers-adopt-cboe-s-new-sessions/)  
  <sub>TradingView, 23 hours ago</sub>  
  Webull joins the growing list of retail brokers offering extended-hours trading for eligible U.S. customers. The new trading hours and available instruments...
- [American Express Falls 3% Despite Q3 Beat and Higher Profit Floor; Visa and Mastercard Slip](https://247wallst.com/investing/2026/10/23/american-express-falls-3-despite-q3-beat-and-higher-profit-floor-visa-and-mastercard-slip/)  
  <sub>24/7 Wall St., 1 hour ago</sub>  
  A higher profit floor isn't protecting American Express (NYSE:AXP | AXP Price Prediction) from a skeptical response to its Q3 2026 report.
- [Exchange-Traded Funds, Equity Futures Lower Pre-Bell Friday Amid AI Spending Concerns](https://finance.yahoo.com/markets/stocks/articles/exchange-traded-funds-equity-futures-131317616.html)  
  <sub>Yahoo Finance, 2 hours ago</sub>  
  The broad market exchange-traded fund SPDR S&P 500 ETF Trust (SPY) was down 0.2% and the actively tr.
- [Composition vs. Returns: Breaking Down the Structural Drift Between KBE and KRE](https://finance.yahoo.com/markets/stocks/articles/composition-vs-returns-breaking-down-133701474.html)  
  <sub>Yahoo Finance, 1 hour ago</sub>  
  State Street SPDR S&P Regional Banking ETF (NYSEMKT:KRE) provides targeted exposure to local lenders, while State Street SPDR S&P Bank ETF (NYSEMKT:KBE)...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.04% (-0.03 on the week) | 5-year 4.81% (-0.09 on the week) | 10-year 4.99% (-0.11 on the week) | 30-year 5.31% (-0.12 on the week)
Yield curve, 10-year minus 3-month: +0.95 points -- upward sloping (normal)
US dollar index: 101.76 (-0.08 on the week)
Volatility (VIX): 20.36 (+0.4 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.2% (2026-09-01) | jobless claims 194k (2026-10-17)
Policy and expectations: Fed target 4.00% | market expects 2.3% inflation over 10 years
Rate path: 2-year Treasury 4.81% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 56.03 (bar of 2026-10-23), from 502 daily bars
Trend: vs 20d SMA 54.69 (+2.4%), 50d 56.08 (-0.1%), 200d 53.69 (+4.3%); 50d above 200d
Momentum: RSI(14) 56.3 | MACD 0.106 vs signal -0.204 (histogram 0.310)
Returns: 1d -1.1% | 5d +0.9% | 1m +2.7% | 3m -1.5%
52-week range: 47.81 - 58.56 (now 76.4% of the way up)
Volatility: ATR(14) 0.72 (1.3% of price) | annualised 20d 13.0%
Volume: 0.18x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.00</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score +0.00</summary>

```text
Fund type: Financial
What it holds: P/E 15.21 | P/B 2.25 | P/S 3.26 | 3y earnings growth n/a
Yield: 1.6%
Three-year record: +22.2% a year | beta to the market 0.75
Cost and size: expense ratio 0.08% | net assets 50.97B
What it is made of: Stocks 99.9%, Cash 0.1%
Largest holdings: Berkshire Hathaway Inc Class B 12.3%, JPMorgan Chase & Co 11.7%, Visa Inc Class A 8.1%, Mastercard Inc Class A 5.9%, Bank of America Corp 4.7%
Sector mix: Financial services 98.2%, Technology 1.6%, Industrials 0.2%
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
Rolled up from the 5 largest holdings, 42.7% of the fund by weight
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 1.77 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +8.4% above the current prices
Holdings read: BRK-B, JPM, V, MA, BAC
Recent rating changes among them:
  - BRK-B: 2026-10-22 UBS: main, Buy -> Buy
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
Share count change: 1 week: +0.0% (0.00) over 7d | 1 month: +0.0% (0.00) over 30d
Shares outstanding: 883.44M | fund size: 49.50B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### US industry (XLI) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Neutral overall as no macro surprise, technicals bearish but not decisive, analyst view limited coverage, flows flat.

**Main reasons it gave:**
- Technical: price below 20‑day SMA (-2.2%) and RSI 34.9 (bearish momentum)
- Analyst view covers 25.7% of fund, 100% buy rating, +32.1% price target
- Fund flows flat: 0% share count change over 1 week and 1 month
- Macro: yields fell modestly, inflation 3.7% and unemployment 4.2% in line with expectations

<details><summary><b>News</b> — score +0.00</summary>

- [State Street Industrial Select Sector SPDR (XLI) Adds Caterpillar and GE on Oct. 21](https://finance.yahoo.com/markets/stocks/articles/state-street-industrial-select-sector-110500719.html)  
  <sub>Yahoo Finance, 4 hours ago</sub>  
  This article first appeared on GuruFocus. State Street Industrial Select Sector SPDR ETF (XLI) reported $244.0 million of gross ETF activity on Wednesday,...
- [Chart Of The Day: The First 'Recession Trade' Day In A Long Time](https://seekingalpha.com/article/4956907-chart-of-day-first-recession-trade-day-in-a-long-time)  
  <sub>Seeking Alpha, 2 hours ago</sub>  
  The MoneyShow Chart of the Day shows the intraday move through late afternoon on Thursday for several ETFs, including defensive sector funds like the State...
- [Exchange-Traded Funds, Equity Futures Lower Pre-Bell Friday Amid AI Spending Concerns](https://finance.yahoo.com/markets/stocks/articles/exchange-traded-funds-equity-futures-131317616.html)  
  <sub>Yahoo Finance, 2 hours ago</sub>  
  The broad market exchange-traded fund SPDR S&P 500 ETF Trust (SPY) was down 0.2% and the actively tr.
- [Chart of the Day 10/23/26: The First "Recession Trade" Day in a LONG Time](https://www.moneyshow.com/articles/tradingidea-65568/chart-of-the-day-10-23-26-the-first-recession-trade-day-in-a-long-time/)  
  <sub>www.moneyshow.com, 11 hours ago</sub>  
  Yes, that was the first, powerful “Recession Trade” day I've seen in a LONG time. The question is, should you worry?
- [iShares Expanded Tech-Software Sector ETF (IGV) stock price, news, quote and history](https://au.finance.yahoo.com/quote/IGV/)  
  <sub>Yahoo Finance Australia, 6 hours ago</sub>  
  Find the latest iShares Expanded Tech-Software Sector ETF (IGV) stock quote, history, news and other vital information to help you with your stock trading...
- [Exchange-Traded Funds, US Equities Lower After Midday](https://finance.yahoo.com/markets/stocks/articles/exchange-traded-funds-us-equities-171320665.html)  
  <sub>Yahoo Finance, 22 hours ago</sub>  
  Broad Market Indicators Broad-market exchange-traded funds IWM and IVV fell. Actively traded Invesco QQQ Trust (QQQ) lost 2.7%. US equity indexes were lower...
- [iShares North American Tech-Software ETF (IGV) stock price, news, quote and history](https://uk.finance.yahoo.com/quote/IGV/)  
  <sub>Yahoo Finance UK, 7 hours ago</sub>  
  Find the latest iShares North American Tech-Software ETF (IGV) stock quote, history, news and other vital information to help you with your stock trading...
- [Product Due Diligence Session: Beyond the Chip: Investing in the Optical Infrastructure Powering AI | ETF Trends](https://www.advisorperspectives.com/webinars/2026/10/30/beyond-the-chip-investing-in-the-optical-infrastructure-powering-ai?partnerref=APWebinarLandingPage)  
  <sub>Advisor Perspectives, 21 hours ago</sub>  
  Join Aura ETFs and VettaFi for a 30-minute livecast exploring recent industry developments, how the photonics ecosystem fits together, and the opportunities...
- [The Technology Select Sector SPDR® Fund (XLK) Stock Price | Quotes & News](https://www.moomoo.com/stock/XLK-US?chain_id=Name1K9-3FXPhg.1ld4bf0&global_content=%7B%22promote_id%22%3A13764%2C%22sub_promote_id%22%3A107%2C%22f%22%3A%22www.moomoo.com%2Fetfs%2FSMH-US%2Fcommunity%22%7D)  
  <sub>Moomoo, 23 hours ago</sub>  
  Track the latest The Technology Select Sector SPDR® Fund (XLK) price, quotes, financial information, news, and analyst ratings on moomoo App for your ETF...
- [Ten-Year Treasury Yields Fall Below 5%: These 10 Real-Estate Stocks Are Rallying Sharply](https://www.tradingview.com/news/benzinga:84dfa12ab094b:0-ten-year-treasury-yields-fall-below-5-these-10-real-estate-stocks-are-rallying-sharply/)  
  <sub>TradingView, 19 hours ago</sub>  
  Wall Street is heavily selling tech and AI-linked stocks on Thursday. Homebuilders are seeing one of the best rallies in months.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.04% (-0.03 on the week) | 5-year 4.81% (-0.09 on the week) | 10-year 4.99% (-0.11 on the week) | 30-year 5.31% (-0.12 on the week)
Yield curve, 10-year minus 3-month: +0.95 points -- upward sloping (normal)
US dollar index: 101.76 (-0.08 on the week)
Volatility (VIX): 20.36 (+0.4 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.2% (2026-09-01) | jobless claims 194k (2026-10-17)
Policy and expectations: Fed target 4.00% | market expects 2.3% inflation over 10 years
Rate path: 2-year Treasury 4.81% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score -0.30</summary>

```text
Last close 164.52 (bar of 2026-10-23), from 502 daily bars
Trend: vs 20d SMA 168.21 (-2.2%), 50d 172.23 (-4.5%), 200d 173.17 (-5.0%); 50d below 200d
Momentum: RSI(14) 34.9 | MACD -1.547 vs signal -1.514 (histogram -0.033)
Returns: 1d -1.3% | 5d -1.9% | 1m -2.6% | 3m -10.2%
52-week range: 147.83 - 186.51 (now 43.1% of the way up)
Volatility: ATR(14) 2.63 (1.6% of price) | annualised 20d 13.9%
Volume: 0.37x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score -0.20</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score -0.20</summary>

```text
Fund type: Industrials
What it holds: P/E 27.43 | P/B 6.56 | P/S 2.92 | 3y earnings growth n/a
Yield: 1.1%
Three-year record: +21.1% a year | beta to the market 1.01
Cost and size: expense ratio 0.08% | net assets 29.83B
What it is made of: Stocks 99.9%, Cash 0.1%
Largest holdings: Caterpillar Inc 7.0%, GE Aerospace 6.1%, GE Vernova Inc 4.8%, RTX Corp 4.7%, Deere & Co 3.2%
Sector mix: Industrials 93.4%, Technology 6.1%, Basic materials 0.3%, Consumer cyclical 0.2%
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

<details><summary><b>What analysts and big funds say</b> — score +0.30</summary>

_Not available today._

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score +0.30</summary>

```text
Rolled up from the 5 largest holdings, 25.7% of the fund by weight
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 1.76 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +32.1% above the current prices
Holdings read: CAT, GE, GEV, RTX, DE
Recent rating changes among them:
  - CAT: 2026-10-14 Oppenheimer: main, Outperform -> Outperform
  - GE: 2026-10-21 UBS: main, Buy -> Buy
  - GEV: 2026-10-14 Susquehanna: main, Positive -> Positive
  - RTX: 2026-10-21 UBS: main, Neutral -> Neutral
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
Share count change: 1 week: +0.0% (0.00) over 7d | 1 month: +0.0% (0.00) over 30d
Shares outstanding: 136.63M | fund size: 22.48B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### US technology (XLK) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Neutral overall; no material macro surprise, technicals lack decisive break, modest inflows, strong analyst optimism not enough to shift view.

**Main reasons it gave:**
- US Treasury yields unchanged (10‑year 4.99% down 0.11% week) – no rate surprise
- XLK price below 20‑day SMA (184.27 vs 193.28) and low volume (0.32× 20‑day avg) – no decisive technical break
- Fund flows net inflow +5.5% in 1 month (4.86B) – modest demand
- Analyst consensus 100% buy with +26.6% price target – bullish but not material

<details><summary><b>News</b> — score +0.00</summary>

- [Exchange-Traded Funds, US Equities Lower After Midday](https://finance.yahoo.com/markets/stocks/articles/exchange-traded-funds-us-equities-171320665.html)  
  <sub>Yahoo Finance, 22 hours ago</sub>  
  Broad Market Indicators Broad-market exchange-traded funds IWM and IVV fell. Actively traded Invesco QQQ Trust (QQQ) lost 2.7%. US equity indexes were lower...
- [Chart of the Day 10/23/26: The First "Recession Trade" Day in a LONG Time](https://www.moneyshow.com/articles/tradingidea-65568/chart-of-the-day-10-23-26-the-first-recession-trade-day-in-a-long-time/)  
  <sub>www.moneyshow.com, 11 hours ago</sub>  
  Yes, that was the first, powerful “Recession Trade” day I've seen in a LONG time. The question is, should you worry?
- [The Technology Select Sector SPDR® Fund (XLK) Stock Price | Quotes & News](https://www.moomoo.com/stock/XLK-US?chain_id=Name1K9-3FXPhg.1ld4bf0&global_content=%7B%22promote_id%22%3A13764%2C%22sub_promote_id%22%3A107%2C%22f%22%3A%22www.moomoo.com%2Fetfs%2FSMH-US%2Fcommunity%22%7D)  
  <sub>Moomoo, 23 hours ago</sub>  
  Track the latest The Technology Select Sector SPDR® Fund (XLK) price, quotes, financial information, news, and analyst ratings on moomoo App for your ETF...
- [Sector Update: Tech Stocks Fall Late Afternoon](https://ca.finance.yahoo.com/news/sector-tech-stocks-fall-afternoon-195124429.html)  
  <sub>Yahoo! Finance Canada, 19 hours ago</sub>  
  Tech stocks were sharply lower late Thursday afternoon, with the State Street Technology Select Sector SPDR ETF (XLK) falling 3.4% and the State Street SPDR...
- [The Average Stock Is Beating the S&P 500 by the Most Since April 2009: Is the Rotation Now Over?](https://www.benzinga.com/markets/equities/26/10/62556800/equal-weight-sp-500-rsp-spy-best-month-since-2009-rotation)  
  <sub>Benzinga, 2 hours ago</sub>  
  The equal-weight S&P 500 ETF (RSP) is beating SPY by the most since April 2009 as money exits AI stocks. Analysts weigh whether the rotation can last.
- [Nokia Tumbles 10% Despite Data Center-Driven Profit Beat; Ericsson Slips](https://247wallst.com/investing/2026/10/22/nokia-tumbles-10-despite-data-center-driven-profit-beat-ericsson-slips/)  
  <sub>24/7 Wall St., 24 hours ago</sub>  
  Nokia just beat earnings on surging AI data center demand, yet its stock is cratering while rival Ericsson barely flinches. The reason why reveals something...
- [Walmart Stock Heads for Best Month Since 1999 - Walmart (NASDAQ:WMT)](https://www.benzinga.com/etfs/sector-etfs/26/10/62546738/walmart-stock-best-month-since-1999-record-staples-rally)  
  <sub>Benzinga, 19 hours ago</sub>  
  Walmart is on track for its best month since 1999 as XLP heads for a record October. Past staples surges like this often came before weaker markets.
- [Ten-Year Yield Falls Below 5%: 10 Real-Estate Stocks Rally - iShares U.S. Home Construction ETF (BATS:ITB](https://www.benzinga.com/real-estate/26/10/62545365/10-year-treasury-yield-falls-homebuilder-real-estate-stocks-rally)  
  <sub>Benzinga, 19 hours ago</sub>  
  Homebuilders rally as the 10-year Treasury yield falls below 5%. Lennar, KB Home and Zillow lead while REITs lag ahead of next week's Fed meeting.
- [QUICK SPARK: Procter & Gamble Stock Eyes Best Day Since 2020 – The Rally Is Hiding Something Bigger](https://www.benzinga.com/markets/equities/26/10/62539221/procter-gamble-stock-best-day-since-2020)  
  <sub>Benzinga, 21 hours ago</sub>  
  Procter & Gamble stock jumps more than 6% on Thursday, its biggest one-day gain since March 2020, after first-quarter results. XLP rose 2.6%.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.04% (-0.03 on the week) | 5-year 4.81% (-0.09 on the week) | 10-year 4.99% (-0.11 on the week) | 30-year 5.31% (-0.12 on the week)
Yield curve, 10-year minus 3-month: +0.95 points -- upward sloping (normal)
US dollar index: 101.76 (-0.08 on the week)
Volatility (VIX): 20.36 (+0.4 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.2% (2026-09-01) | jobless claims 194k (2026-10-17)
Policy and expectations: Fed target 4.00% | market expects 2.3% inflation over 10 years
Rate path: 2-year Treasury 4.81% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score -0.10</summary>

```text
Last close 184.27 (bar of 2026-10-23), from 502 daily bars
Trend: vs 20d SMA 193.28 (-4.7%), 50d 189.66 (-2.8%), 200d 168.51 (+9.4%); 50d above 200d
Momentum: RSI(14) 40.0 | MACD -1.821 vs signal -0.090 (histogram -1.731)
Returns: 1d +1.1% | 5d +0.4% | 1m -5.4% | 3m +5.7%
52-week range: 127.50 - 202.00 (now 76.2% of the way up)
Volatility: ATR(14) 3.88 (2.1% of price) | annualised 20d 23.7%
Volume: 0.32x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score -0.20</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score -0.20</summary>

```text
Fund type: Technology
What it holds: P/E 32.04 | P/B 11.88 | P/S 9.26 | 3y earnings growth n/a
Yield: 0.4%
Three-year record: +32.8% a year | beta to the market 1.45
Cost and size: expense ratio 0.08% | net assets 127.30B
What it is made of: Stocks 100.0%, Cash 0.0%
Largest holdings: NVIDIA Corp 15.5%, Apple Inc 13.6%, Microsoft Corp 10.7%, Advanced Micro Devices Inc 5.1%, Broadcom Inc 4.7%
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
Rolled up from the 5 largest holdings, 49.5% of the fund by weight
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 1.58 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +26.6% above the current prices
Holdings read: NVDA, AAPL, MSFT, AMD, AVGO
Recent rating changes among them:
  - NVDA: 2026-10-22 Needham: reit, Buy -> Buy
  - AAPL: 2026-10-20 MoffettNathanson: main, Neutral -> Neutral
  - MSFT: 2026-10-21 Guggenheim: reit, Buy -> Buy
  - AMD: 2026-10-21 Susquehanna: main, Positive -> Positive
  - AVGO: 2026-10-22 Tigress Financial: init, ? -> Buy
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
Share count change: 1 week: +4.1% (4.86B) over 7d | 1 month: +5.5% (6.44B) over 30d
Shares outstanding: 675.13M | fund size: 124.41B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### US everyday goods (XLP) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Neutral overall; no macro surprise, technical bullish but low volume, flat fund flows, and positive but limited analyst coverage.

**Main reasons it gave:**
- No macro surprise in rates or data releases this week
- Technical indicators show price above 20‑day, 50‑day, and 200‑day SMAs but volume is only 0.77× 20‑day average
- Fund flows flat over the past month with share count unchanged
- Analyst consensus 100% buy for 41.8% of holdings with a weighted price target +4.9% above current price

<details><summary><b>News</b> — score +0.00</summary>

- [Exchange-Traded Funds, Equity Futures Lower Pre-Bell Friday Amid AI Spending Concerns](https://finance.yahoo.com/markets/stocks/articles/exchange-traded-funds-equity-futures-131317616.html)  
  <sub>Yahoo Finance, 2 hours ago</sub>  
  The broad market exchange-traded fund SPDR S&P 500 ETF Trust (SPY) was down 0.2% and the actively tr.
- [Consumer staples on track for best month since 1998 as sector surges (XLP:NYSEARCA)](https://seekingalpha.com/news/4656563-consumer-staples-on-track-for-best-month-since-1998-as-sector-surges)  
  <sub>Seeking Alpha, 2 hours ago</sub>  
  The S&P 500 consumer staples sector is on track for its strongest monthly performance since October 1998, with the sector's latest advance standing out...
- [The Average Stock Is Beating the S&P 500 by the Most Since April 2009: Is the Rotation Now Over?](https://www.benzinga.com/markets/equities/26/10/62556800/equal-weight-sp-500-rsp-spy-best-month-since-2009-rotation)  
  <sub>Benzinga, 2 hours ago</sub>  
  The equal-weight S&P 500 ETF (RSP) is beating SPY by the most since April 2009 as money exits AI stocks. Analysts weigh whether the rotation can last.
- [Chart of the Day 10/23/26: The First "Recession Trade" Day in a LONG Time](https://www.moneyshow.com/articles/tradingidea-65568/chart-of-the-day-10-23-26-the-first-recession-trade-day-in-a-long-time/)  
  <sub>www.moneyshow.com, 11 hours ago</sub>  
  Yes, that was the first, powerful “Recession Trade” day I've seen in a LONG time. The question is, should you worry?
- [Tesla Earnings Test XLY After Sector-Leading 5-Day Run](https://www.etftrends.com/sector-investing-content-hub/tesla-earnings-test-xly-after-sector-leading-5-day-run/)  
  <sub>ETF Trends, 21 hours ago</sub>  
  Tesla topped profit estimates as auto revenue fell 3%, putting focus on XLY, which has 18% of its assets in the EV maker after a strong week.
- [Chart Of The Day: The First 'Recession Trade' Day In A Long Time](https://seekingalpha.com/article/4956907-chart-of-day-first-recession-trade-day-in-a-long-time)  
  <sub>Seeking Alpha, 2 hours ago</sub>  
  The MoneyShow Chart of the Day shows the intraday move through late afternoon on Thursday for several ETFs, including defensive sector funds like the State...
- [Sector Update: Consumer Stocks Mixed Late Afternoon](https://finance.yahoo.com/markets/stocks/articles/sector-consumer-stocks-mixed-afternoon-194726150.html)  
  <sub>Yahoo Finance, 19 hours ago</sub>  
  Consumer stocks were mixed late Thursday afternoon, with the State Street Consumer Staples Select Sector SPDR ETF (XLP) rising 2.9% and the State Street...
- [Amazon leads ten top-rated consumer stocks as fund outflows deepen (XLY:NYSEARCA)](https://seekingalpha.com/news/4656583-amazon-leads-ten-top-rated-consumer-stocks-as-fund-outflows-deepen)  
  <sub>Seeking Alpha, 59 minutes ago</sub>  
  BofA Research said consumer funds have recorded their second-largest outflow on record, with the latest weekly data showing a sharp decline in consumer...
- [Exchange-Traded Funds, US Equities Lower After Midday](https://finance.yahoo.com/markets/stocks/articles/exchange-traded-funds-us-equities-171320665.html)  
  <sub>Yahoo Finance, 22 hours ago</sub>  
  Broad Market Indicators Broad-market exchange-traded funds IWM and IVV fell. Actively traded Invesco QQQ Trust (QQQ) lost 2.7%. US equity indexes were lower...
- [Walmart Stock Best Month Since 2014: A Recession Signal? - Walmart (NASDAQ:WMT)](https://www.benzinga.com/markets/equities/26/10/62537079/walmart-stock-best-month-since-2014-recession-signal)  
  <sub>Benzinga, 22 hours ago</sub>  
  Walmart stock is on track for its best month since 2014 and its widest lead over the S&P 500 since 2020. History shows when that preceded a recession.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.04% (-0.03 on the week) | 5-year 4.81% (-0.09 on the week) | 10-year 4.99% (-0.11 on the week) | 30-year 5.31% (-0.12 on the week)
Yield curve, 10-year minus 3-month: +0.95 points -- upward sloping (normal)
US dollar index: 101.76 (-0.08 on the week)
Volatility (VIX): 20.36 (+0.4 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.2% (2026-09-01) | jobless claims 194k (2026-10-17)
Policy and expectations: Fed target 4.00% | market expects 2.3% inflation over 10 years
Rate path: 2-year Treasury 4.81% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.20</summary>

```text
Last close 88.52 (bar of 2026-10-23), from 502 daily bars
Trend: vs 20d SMA 84.33 (+5.0%), 50d 84.38 (+4.9%), 200d 84.27 (+5.0%); 50d above 200d
Momentum: RSI(14) 65.3 | MACD 1.438 vs signal 0.789 (histogram 0.649)
Returns: 1d -1.6% | 5d +1.0% | 1m +8.3% | 3m +3.7%
52-week range: 75.60 - 90.01 (now 89.7% of the way up)
Volatility: ATR(14) 1.27 (1.4% of price) | annualised 20d 19.4%
Volume: 0.77x the 20-day average
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
Three-year record: +12.0% a year | beta to the market 0.48
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

<details><summary><b>What analysts and big funds say</b> — score +0.50</summary>

_Not available today._

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score +0.50</summary>

```text
Rolled up from the 5 largest holdings, 41.8% of the fund by weight
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 1.79 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +4.9% above the current prices
Holdings read: WMT, COST, PG, KO, PM
Recent rating changes among them:
  - WMT: 2026-10-20 Evercore ISI Group: main, Outperform -> Outperform
  - COST: 2026-10-21 CICC: init, ? -> Outperform
  - PG: 2026-10-23 RBC Capital: main, Outperform -> Outperform
  - KO: 2026-10-16 Barclays: main, Overweight -> Overweight
  - PM: 2026-10-22 UBS: main, Neutral -> Neutral
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
Shares outstanding: 210.17M | fund size: 18.60B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### US electricity and water (XLU) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Neutral overall – no macro surprise, flat fund flows, mixed technicals, and analyst coverage bullish but limited to a minority of the fund.

**Main reasons it gave:**
- Flat fund flows: 0% change in share count over week and month
- Macro data unchanged: yields down slightly, normal upward sloping curve, VIX stable
- Technical indicators mixed: price above 20‑day and 50‑day SMA but below 200‑day SMA, low volume
- Analyst coverage bullish (80.6% buy) but limited to 39.5% of fund

<details><summary><b>News</b> — score +0.00</summary>

- [State Street Utilities Select SPDR (XLU) Sells NextEra and Southern on Oct. 21](https://finance.yahoo.com/markets/stocks/articles/state-street-utilities-select-spdr-110413721.html)  
  <sub>Yahoo Finance, 4 hours ago</sub>
- [Undervalued utilities stocks to watch as Q3 earnings season unfolds (XLU:NYSEARCA)](https://seekingalpha.com/news/4656514-undervalued-utilities-stocks-to-watch-as-q3-earnings-season-unfolds)  
  <sub>Seeking Alpha, 3 hours ago</sub>  
  As the third-quarter 2026 earnings season unfolds, investors are assessing valuations across the U.S. utilities sector, where electric utilities,...
- [The Average Stock Is Beating the S&P 500 by the Most Since April 2009: Is the Rotation Now Over?](https://www.benzinga.com/markets/equities/26/10/62556800/equal-weight-sp-500-rsp-spy-best-month-since-2009-rotation)  
  <sub>Benzinga, 2 hours ago</sub>  
  The equal-weight S&P 500 ETF (RSP) is beating SPY by the most since April 2009 as money exits AI stocks. Analysts weigh whether the rotation can last.
- [NLR ETF: Tech Giants Are Going For Nuclear Power (NYSEARCA:NLR)](https://seekingalpha.com/article/4956594-nlr-etf-tech-giants-are-going-for-nuclear-power)  
  <sub>Seeking Alpha, 20 hours ago</sub>  
  The VanEck Uranium and Nuclear ETF provides attractive exposure to nuclear and utility companies, benefiting from the growing baseload electricity demand...
- [ETFs Are Net Sellers of NextEra Energy (NEE) on Wednesday](https://finance.yahoo.com/markets/stocks/articles/etfs-net-sellers-nextera-energy-110219251.html)  
  <sub>Yahoo Finance, 4 hours ago</sub>
- [Southern (SO) Sees $57.3 Million in Net ETF Selling on Oct. 21](https://finance.yahoo.com/markets/stocks/articles/southern-sees-57-3-million-110237349.html)  
  <sub>Yahoo Finance, 4 hours ago</sub>
- [Earnings Preview: What to Expect From American Electric Power's Report](https://www.inkl.com/news/earnings-preview-what-to-expect-from-american-electric-powers-report)  
  <sub>inkl, 22 hours ago</sub>  
  American Electric Power will release its third-quarter earnings next week, and analysts anticipate a double-digit bottom-line growth.
- [Defensives Lead Sectors In Thursday Trading As Growth Trails](https://www.benzinga.com/etfs/sector-etfs/26/10/62531733/defensives-lead-sectors-in-thursday-trading-as-growth-trails)  
  <sub>Benzinga, 24 hours ago</sub>  
  Five sectors are higher and six are lower in Thursday's regular session, with defensive sectors holding the top three positions. The leaders are separated...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.04% (-0.03 on the week) | 5-year 4.81% (-0.09 on the week) | 10-year 4.99% (-0.11 on the week) | 30-year 5.31% (-0.12 on the week)
Yield curve, 10-year minus 3-month: +0.95 points -- upward sloping (normal)
US dollar index: 101.76 (-0.08 on the week)
Volatility (VIX): 20.36 (+0.4 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.2% (2026-09-01) | jobless claims 194k (2026-10-17)
Policy and expectations: Fed target 4.00% | market expects 2.3% inflation over 10 years
Rate path: 2-year Treasury 4.81% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 42.51 (bar of 2026-10-23), from 502 daily bars
Trend: vs 20d SMA 41.12 (+3.4%), 50d 41.87 (+1.5%), 200d 44.30 (-4.0%); 50d below 200d
Momentum: RSI(14) 59.3 | MACD 0.248 vs signal -0.001 (histogram 0.249)
Returns: 1d -0.8% | 5d +0.7% | 1m +8.0% | 3m -6.9%
52-week range: 39.25 - 47.73 (now 38.5% of the way up)
Volatility: ATR(14) 0.65 (1.5% of price) | annualised 20d 17.5%
Volume: 0.19x the 20-day average
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
Three-year record: +16.5% a year | beta to the market 0.40
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
Ratings by weight: buy 80.6% | hold 19.4% | sell 0.0% (mean 1.98 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +13.7% above the current prices
Holdings read: NEE, SO, DUK, CEG, AEP
Recent rating changes among them:
  - NEE: 2026-10-23 Barclays: main, Equal-Weight -> Equal-Weight
  - SO: 2026-10-22 HSBC: init, ? -> Buy
  - DUK: 2026-10-22 HSBC: init, ? -> Hold
  - CEG: 2026-10-22 HSBC: init, ? -> Buy
  - AEP: 2026-10-22 Jefferies: main, Buy -> Buy
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
Shares outstanding: 163.27M | fund size: 6.94B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### US health care (XLV) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Neutral overall as bullish analyst view (+5.7% price target) is offset by net outflows and low trading volume, with no macro surprise or decisive technical break.

**Main reasons it gave:**
- Analyst view: 100% buy rating, weighted price target +5.7% above current price
- Fund flows: net outflows of -5.1% in 1 week and -6.9% in 1 month
- Technicals: price above 20d, 50d, 200d SMAs, RSI 64.5, but volume only 0.35x 20‑day average
- Macro: Treasury yields rose slightly, VIX 20.36, no surprise data releases

<details><summary><b>News</b> — score +0.00</summary>

- [State Street Health Care SPDR (XLV) Sells $64.6 Million More Eli Lilly on Wednesday](https://finance.yahoo.com/healthcare/articles/state-street-health-care-spdr-110436786.html)  
  <sub>Yahoo Finance, 4 hours ago</sub>  
  This article first appeared on GuruFocus. State Street Health Care Select Sector SPDR ETF (XLV) extended a run of one-sided trading on Wednesday,...
- [Why Healthcare ETFs Are Hovering Around One-Year Highs](https://finance.yahoo.com/healthcare/articles/why-healthcare-etfs-hovering-around-110000411.html)  
  <sub>Yahoo Finance, 4 hours ago</sub>  
  Healthcare ETFs are hovering near 52-week highs as earnings prospects improve, clinical breakthroughs advance and GLP-1 demand expands.
- [Johnson & Johnson (JNJ) Sees $54.1 Million in Net ETF Selling on Oct. 21](https://www.gurufocus.com/news/9139233/johnson-johnson-jnj-sees-541-million-in-net-etf-selling-on-oct-21)  
  <sub>GuruFocus, 4 hours ago</sub>  
  ETFs sold $54.1 million of Johnson & Johnson (JNJ) on Wednesday, extending a two-day run of net selling. Twenty-five funds reduced their holdings while 24...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.04% (-0.03 on the week) | 5-year 4.81% (-0.09 on the week) | 10-year 4.99% (-0.11 on the week) | 30-year 5.31% (-0.12 on the week)
Yield curve, 10-year minus 3-month: +0.95 points -- upward sloping (normal)
US dollar index: 101.76 (-0.08 on the week)
Volatility (VIX): 20.36 (+0.4 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.2% (2026-09-01) | jobless claims 194k (2026-10-17)
Policy and expectations: Fed target 4.00% | market expects 2.3% inflation over 10 years
Rate path: 2-year Treasury 4.81% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 179.46 (bar of 2026-10-23), from 502 daily bars
Trend: vs 20d SMA 172.49 (+4.0%), 50d 171.12 (+4.9%), 200d 158.07 (+13.5%); 50d above 200d
Momentum: RSI(14) 64.5 | MACD 2.898 vs signal 1.894 (histogram 1.003)
Returns: 1d -1.0% | 5d +1.6% | 1m +5.6% | 3m +9.8%
52-week range: 142.84 - 181.30 (now 95.2% of the way up)
Volatility: ATR(14) 2.84 (1.6% of price) | annualised 20d 19.3%
Volume: 0.35x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.00</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score +0.00</summary>

```text
Fund type: Health
What it holds: P/E 30.01 | P/B 4.74 | P/S 1.66 | 3y earnings growth n/a
Yield: 1.5%
Three-year record: +13.7% a year | beta to the market 0.52
Cost and size: expense ratio 0.08% | net assets 43.39B
What it is made of: Stocks 99.8%, Cash 0.2%
Largest holdings: Eli Lilly and Co 15.1%, Johnson & Johnson 10.4%, AbbVie Inc 7.5%, Merck & Co Inc 5.8%, UnitedHealth Group Inc 5.4%
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

<details><summary><b>What analysts and big funds say</b> — score +0.70</summary>

_Not available today._

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score +0.70</summary>

```text
Rolled up from the 5 largest holdings, 44.3% of the fund by weight
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 1.72 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +5.7% above the current prices
Holdings read: LLY, JNJ, ABBV, MRK, UNH
Recent rating changes among them:
  - LLY: 2026-10-21 Leerink Partners: main, Outperform -> Outperform
  - JNJ: 2026-10-16 Wells Fargo: main, Overweight -> Overweight
  - ABBV: 2026-10-21 Barclays: main, Overweight -> Overweight
  - MRK: 2026-10-12 Citigroup: main, Neutral -> Neutral
  - UNH: 2026-10-22 Mizuho: main, Outperform -> Outperform
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
Share count change: 1 week: -5.1% (-2.36B) over 7d | 1 month: -6.9% (-3.24B) over 30d
Shares outstanding: 242.56M | fund size: 43.53B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### US shopping and leisure (XLY) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Neutral overall due to mixed signals: strong analyst buy rating and positive fundamentals are offset by significant outflows and technicals showing price below the 200‑day SMA.

**Main reasons it gave:**
- Share count fell 10.1% over the past month (outflows)
- Analyst ratings: 100% buy on 54.4% of fund weight, weighted price target +21.8% above current
- Price below 200-day SMA (115.76) while near 20-day SMA (111.99) and 50-day SMA (113.44)
- RSI 52.5, MACD histogram 0.451, volume 0.33× 20‑day average
- Treasury yields rose modestly; VIX up 0.4 to 20.36

<details><summary><b>News</b> — score +0.00</summary>

- [Tesla Earnings Test XLY After Sector-Leading 5-Day Run](https://www.etftrends.com/sector-investing-content-hub/tesla-earnings-test-xly-after-sector-leading-5-day-run/)  
  <sub>ETF Trends, 21 hours ago</sub>  
  Tesla topped profit estimates as auto revenue fell 3%, putting focus on XLY, which has 18% of its assets in the EV maker after a strong week.
- [Tesla Volatility Exposes Hidden Risk Across 553 Funds](https://www.tradingview.com/news/gurufocus:b97243782094b:0-tesla-volatility-exposes-hidden-risk-across-553-funds/)  
  <sub>TradingView, 19 hours ago</sub>  
  Tesla's (TSLA) post-earnings volatility is putting a wide range of exchange traded funds under the microscope, underscoring just how deeply the stock is...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.04% (-0.03 on the week) | 5-year 4.81% (-0.09 on the week) | 10-year 4.99% (-0.11 on the week) | 30-year 5.31% (-0.12 on the week)
Yield curve, 10-year minus 3-month: +0.95 points -- upward sloping (normal)
US dollar index: 101.76 (-0.08 on the week)
Volatility (VIX): 20.36 (+0.4 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.2% (2026-09-01) | jobless claims 194k (2026-10-17)
Policy and expectations: Fed target 4.00% | market expects 2.3% inflation over 10 years
Rate path: 2-year Treasury 4.81% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 113.47 (bar of 2026-10-23), from 502 daily bars
Trend: vs 20d SMA 111.99 (+1.3%), 50d 113.44 (+0.0%), 200d 115.76 (-2.0%); 50d below 200d
Momentum: RSI(14) 52.5 | MACD 0.579 vs signal 0.128 (histogram 0.451)
Returns: 1d -1.3% | 5d +0.9% | 1m +2.9% | 3m +2.4%
52-week range: 105.66 - 124.52 (now 41.4% of the way up)
Volatility: ATR(14) 1.60 (1.4% of price) | annualised 20d 14.7%
Volume: 0.33x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.30</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score +0.30</summary>

```text
Fund type: Consumer Cyclical
What it holds: P/E 24.00 | P/B 5.56 | P/S 2.32 | 3y earnings growth n/a
Yield: 0.9%
Three-year record: +16.0% a year | beta to the market 1.18
Cost and size: expense ratio 0.08% | net assets 21.27B
What it is made of: Stocks 99.9%, Cash 0.1%
Largest holdings: Amazon.com Inc 23.4%, Tesla Inc 17.7%, The Home Depot Inc 5.0%, McDonald's Corp 4.2%, TJX Companies Inc 4.1%
Sector mix: Consumer cyclical 98.7%, Technology 1.3%
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
Rolled up from the 5 largest holdings, 54.4% of the fund by weight
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 1.79 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +21.8% above the current prices
Holdings read: AMZN, TSLA, HD, MCD, TJX
Recent rating changes among them:
  - AMZN: 2026-10-19 Morgan Stanley: main, Overweight -> Overweight
  - TSLA: 2026-10-22 UBS: main, Neutral -> Neutral
  - HD: 2026-09-09 Bernstein: main, Market Perform -> Market Perform
  - MCD: 2026-10-20 Citigroup: main, Buy -> Buy
  - TJX: 2026-10-22 Wolfe Research: init, ? -> Peer Perform
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
Share count change: 1 week: -2.8% (-596.52M) over 7d | 1 month: -10.1% (-2.35B) over 30d
Shares outstanding: 184.10M | fund size: 20.89B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Israel (EIS) · Sector or country — no answer, no confidence given

<details><summary><b>News</b> — score n/a</summary>

_No news found for this one today._

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score n/a</summary>

```text
US Treasury yields: 3-month 4.04% (-0.03 on the week) | 5-year 4.81% (-0.09 on the week) | 10-year 4.99% (-0.11 on the week) | 30-year 5.31% (-0.12 on the week)
Yield curve, 10-year minus 3-month: +0.95 points -- upward sloping (normal)
US dollar index: 101.76 (-0.08 on the week)
Volatility (VIX): 20.36 (+0.4 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.2% (2026-09-01) | jobless claims 194k (2026-10-17)
Policy and expectations: Fed target 4.00% | market expects 2.3% inflation over 10 years
Rate path: 2-year Treasury 4.81% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score n/a</summary>

```text
Last close 119.65 (bar of 2026-10-23), from 502 daily bars
Trend: vs 20d SMA 119.99 (-0.3%), 50d 122.26 (-2.1%), 200d 123.16 (-2.9%); 50d below 200d
Momentum: RSI(14) 46.0 | MACD -0.641 vs signal -0.873 (histogram 0.233)
Returns: 1d -0.4% | 5d +0.0% | 1m -2.5% | 3m -0.0%
52-week range: 99.40 - 137.69 (now 52.9% of the way up)
Volatility: ATR(14) 1.77 (1.5% of price) | annualised 20d 16.4%
Volume: 0.73x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score n/a</summary>

```text
Fund type: Focused Region
What it holds: P/E 17.89 | P/B 2.43 | P/S 2.45 | 3y earnings growth n/a
Yield: 1.5%
Three-year record: +39.7% a year | beta to the market 1.09
Cost and size: expense ratio 0.59% | net assets 874.00M
What it is made of: Stocks 99.5%, Cash 0.5%
Largest holdings: Teva Pharmaceutical Industries Ltd ADR 10.1%, Bank Leumi Le-Israel BM 9.0%, Bank Hapoalim BM 8.1%, Tower Semiconductor Ltd 5.5%, Elbit Systems Ltd 4.8%
Sector mix: Financial services 36.1%, Technology 18.1%, Healthcare 10.7%, Industrials 10.0%
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
Rolled up from the 5 largest holdings, 37.6% of the fund by weight
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 1.17 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +22.9% above the current prices
Holdings read: TEVA, LUMI.TA, POLI.TA, TSEM.TA, ESLT.TA
Recent rating changes among them:
  - TEVA: 2026-10-15 Barclays: main, Overweight -> Overweight
  - TSEM.TA: 2026-09-25 Mizuho: init, ? -> Outperform
  - ESLT.TA: 2026-10-05 Jefferies: main, Hold -> Hold
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
Shares outstanding: 2.55M | fund size: 305.11M
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### United Kingdom (EWU) · Sector or country — no answer, no confidence given

<details><summary><b>News</b> — score n/a</summary>

_No news found for this one today._

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score n/a</summary>

```text
US Treasury yields: 3-month 4.04% (-0.03 on the week) | 5-year 4.81% (-0.09 on the week) | 10-year 4.99% (-0.11 on the week) | 30-year 5.31% (-0.12 on the week)
Yield curve, 10-year minus 3-month: +0.95 points -- upward sloping (normal)
US dollar index: 101.76 (-0.08 on the week)
Volatility (VIX): 20.36 (+0.4 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.2% (2026-09-01) | jobless claims 194k (2026-10-17)
Policy and expectations: Fed target 4.00% | market expects 2.3% inflation over 10 years
Rate path: 2-year Treasury 4.81% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score n/a</summary>

```text
Last close 47.40 (bar of 2026-10-23), from 502 daily bars
Trend: vs 20d SMA 46.91 (+1.1%), 50d 47.65 (-0.5%), 200d 46.90 (+1.1%); 50d above 200d
Momentum: RSI(14) 51.6 | MACD 0.076 vs signal -0.078 (histogram 0.154)
Returns: 1d -0.9% | 5d -1.3% | 1m +0.5% | 3m +0.1%
52-week range: 41.34 - 49.39 (now 75.3% of the way up)
Volatility: ATR(14) 0.49 (1.0% of price) | annualised 20d 13.1%
Volume: 0.18x the 20-day average
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
Three-year record: +20.3% a year | beta to the market 0.71
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
Weighted price target: +15.5% above the current prices
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
Direction: money going out (1 month)
Share count change: 1 week: -2.0% (-75.87M) over 7d | 1 month: -4.0% (-151.83M) over 30d
Shares outstanding: 76.72M | fund size: 3.64B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### US materials and chemicals (XLB) · Sector or country — no answer, no confidence given

<details><summary><b>News</b> — score n/a</summary>

- [Tesla Earnings Test XLY After Sector-Leading 5-Day Run](https://www.etftrends.com/sector-investing-content-hub/tesla-earnings-test-xly-after-sector-leading-5-day-run/)  
  <sub>ETF Trends, 21 hours ago</sub>  
  Tesla topped profit estimates as auto revenue fell 3%, putting focus on XLY, which has 18% of its assets in the EV maker after a strong week.
- [An 8-Day Winning Streak Has Amcor Stock Up 11%](https://www.trefis.com/stock/amcr/articles/620096/an-8-day-winning-streak-has-amcor-stock-up-11/2026-10-23)  
  <sub>Trefis, 9 hours ago</sub>  
  Amcor (AMCR) stock has risen for 8 consecutive trading days, gaining 11.3% over that stretch. That added about $2.2 billion to the company's market value,...
- [Amazon leads ten top-rated consumer stocks as fund outflows deepen (XLY:NYSEARCA)](https://seekingalpha.com/news/4656583-amazon-leads-ten-top-rated-consumer-stocks-as-fund-outflows-deepen)  
  <sub>Seeking Alpha, 60 minutes ago</sub>  
  BofA Research said consumer funds have recorded their second-largest outflow on record, with the latest weekly data showing a sharp decline in consumer...
- [Tesla Volatility Exposes Hidden Risk Across 553 Funds](https://www.tradingview.com/news/gurufocus:b97243782094b:0-tesla-volatility-exposes-hidden-risk-across-553-funds/)  
  <sub>TradingView, 19 hours ago</sub>  
  Tesla's (TSLA) post-earnings volatility is putting a wide range of exchange traded funds under the microscope, underscoring just how deeply the stock is...
- [Defensives Lead Sectors In Thursday Trading As Growth Trails](https://www.benzinga.com/etfs/sector-etfs/26/10/62531733/defensives-lead-sectors-in-thursday-trading-as-growth-trails)  
  <sub>Benzinga, 24 hours ago</sub>  
  Five sectors are higher and six are lower in Thursday's regular session, with defensive sectors holding the top three positions. The leaders are separated...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score n/a</summary>

```text
US Treasury yields: 3-month 4.04% (-0.03 on the week) | 5-year 4.81% (-0.09 on the week) | 10-year 4.99% (-0.11 on the week) | 30-year 5.31% (-0.12 on the week)
Yield curve, 10-year minus 3-month: +0.95 points -- upward sloping (normal)
US dollar index: 101.76 (-0.08 on the week)
Volatility (VIX): 20.36 (+0.4 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.2% (2026-09-01) | jobless claims 194k (2026-10-17)
Policy and expectations: Fed target 4.00% | market expects 2.3% inflation over 10 years
Rate path: 2-year Treasury 4.81% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score n/a</summary>

```text
Last close 51.43 (bar of 2026-10-23), from 502 daily bars
Trend: vs 20d SMA 49.93 (+3.0%), 50d 51.02 (+0.8%), 200d 50.98 (+0.9%); 50d above 200d
Momentum: RSI(14) 61.1 | MACD 0.229 vs signal -0.084 (histogram 0.313)
Returns: 1d -0.5% | 5d +1.0% | 1m +3.5% | 3m +0.1%
52-week range: 42.23 - 53.67 (now 80.4% of the way up)
Volatility: ATR(14) 0.72 (1.4% of price) | annualised 20d 12.3%
Volume: 0.27x the 20-day average
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
Three-year record: +13.0% a year | beta to the market 0.85
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
Weighted price target: +14.3% above the current prices
Holdings read: LIN, NEM, FCX, ECL, SHW
Recent rating changes among them:
  - LIN: 2026-10-15 RBC Capital: main, Outperform -> Outperform
  - NEM: 2026-10-22 Freedom Broker: down, Buy -> Hold
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
Share count change: 1 week: +0.0% (0.00) over 7d | 1 month: +0.0% (0.00) over 30d
Shares outstanding: 71.92M | fund size: 3.70B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

## Commodities

### Sugar (CANE) · Commodity — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> No macro surprise; technicals show price above key SMAs but no decisive break and low volume; heavy roll cost (-8.2% annual) penalizes long exposure; positioning is a crowded long (22% net long, 100th percentile) with minimal weekly change; fund flows show a 17.6% outflow over the past month.

**Main reasons it gave:**
- Inflation 3.7% aligns with expectations – no macro surprise
- Price above 20‑day, 50‑day, and 200‑day SMAs but no decisive technical break; volume at 0.38× 20‑day average
- Cost of holding fund is -8.2% annual, indicating heavy roll cost for longs
- Positioning shows a crowded long (22% net long, 100th percentile) with only +0.2% weekly change
- Fund flows show a net outflow of 17.6% over the past month

<details><summary><b>News</b> — score +0.00</summary>

_No news found for this one today._

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.04% (-0.03 on the week) | 5-year 4.81% (-0.09 on the week) | 10-year 4.99% (-0.11 on the week) | 30-year 5.31% (-0.12 on the week)
Yield curve, 10-year minus 3-month: +0.95 points -- upward sloping (normal)
US dollar index: 101.76 (-0.08 on the week)
Volatility (VIX): 20.36 (+0.4 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.2% (2026-09-01) | jobless claims 194k (2026-10-17)
Policy and expectations: Fed target 4.00% | market expects 2.3% inflation over 10 years
Rate path: 2-year Treasury 4.81% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 12.10 (bar of 2026-10-23), from 502 daily bars
Trend: vs 20d SMA 12.03 (+0.6%), 50d 11.59 (+4.4%), 200d 10.17 (+19.0%); 50d above 200d
Momentum: RSI(14) 56.3 | MACD 0.222 vs signal 0.261 (histogram -0.039)
Returns: 1d +0.4% | 5d -1.7% | 1m +7.4% | 3m +26.0%
52-week range: 9.02 - 12.47 (now 89.4% of the way up)
Volatility: ATR(14) 0.19 (1.6% of price) | annualised 20d 22.7%
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
Cost of holding this fund instead of sugar itself: -8.2% a year -- heavy: rolling contracts costs this fund real money
Measured: 3 months: fund +26.0%, commodity +38.5%, gap -12.6% | 6 months: fund +28.0%, commodity +45.0%, gap -17.1% | 12 months: fund +25.6%, commodity +33.8%, gap -8.2%
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
Share count change: 1 week: +1.3% (656.28K) over 7d | 1 month: -17.6% (-11.22M) over 30d
Shares outstanding: 4.34M | fund size: 52.48M
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Corn (CORN) · Commodity — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:** no explanation. It wrote only “NEUTRAL”, so the main reasons below are all it gave.

**Main reasons it gave:**
- Positioning: net long fell 4.4% of open interest this week
- Crop condition: US corn rating steady, +2 points over 3 weeks
- Cost of holding: -6.8% annual roll cost, heavy tailwind for short
- Technicals: price below 20‑day SMA, RSI 26.9, low volume, no decisive break

<details><summary><b>News</b> — score +0.00</summary>

- [Corn Slipping Lower on Friday Morning](https://www.barchart.com/story/news/8365106/corn-slipping-lower-on-friday-morning)  
  <sub>Barchart.com, 3 hours ago</sub>  
  Corn prices are fractionally to 1 ¼ cents lower early on Friday. Futures fell back weaker on Thursday, after the midweek gains, as contracts were down 2 ¼...
- [Corn Futures: Testing 50-Week MA at 3-Month Lows](https://www.barchart.com/story/news/8365239/corn-futures-testing-50-week-ma-at-3-month-lows)  
  <sub>Barchart.com, 3 hours ago</sub>  
  Analysis of weekly corn futures as prices reach a 3-month low, testing key support at the rising 50-week moving average and 61.8% Fibonacci level.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.04% (-0.03 on the week) | 5-year 4.81% (-0.09 on the week) | 10-year 4.99% (-0.11 on the week) | 30-year 5.31% (-0.12 on the week)
Yield curve, 10-year minus 3-month: +0.95 points -- upward sloping (normal)
US dollar index: 101.76 (-0.08 on the week)
Volatility (VIX): 20.36 (+0.4 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.2% (2026-09-01) | jobless claims 194k (2026-10-17)
Policy and expectations: Fed target 4.00% | market expects 2.3% inflation over 10 years
Rate path: 2-year Treasury 4.81% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 17.71 (bar of 2026-10-23), from 502 daily bars
Trend: vs 20d SMA 18.59 (-4.7%), 50d 19.23 (-7.9%), 200d 18.18 (-2.6%); 50d above 200d
Momentum: RSI(14) 26.9 | MACD -0.422 vs signal -0.327 (histogram -0.095)
Returns: 1d -0.4% | 5d -2.6% | 1m -10.0% | 3m -1.1%
52-week range: 16.47 - 20.29 (now 32.5% of the way up)
Volatility: ATR(14) 0.27 (1.5% of price) | annualised 20d 16.4%
Volume: 0.13x the 20-day average
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
Cost of holding this fund instead of corn itself: -6.8% a year -- heavy: rolling contracts costs this fund real money
Measured: 3 months: fund -1.1%, commodity +0.9%, gap -2.1% | 6 months: fund -3.1%, commodity +0.2%, gap -3.3% | 12 months: fund +1.0%, commodity +7.8%, gap -6.8%
A commodity fund holds futures, not corn, and must sell each expiring contract to buy the next one. Where the next month costs more, that roll loses money every month. This gap is what the structure has actually cost, fees included -- it is history rather than a forecast, and it is not a direction: heavy carry is a reason to want a larger move to justify a long, and a tailwind for a short.
```

</details>

<details><summary><b>How much oil and gas is in storage</b> — score -0.35</summary>

_Not available today._

</details>

<details><summary><b>How the crop is growing</b> — score -0.35</summary>

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

<details><summary><b>Buying and selling by company insiders</b> — score -0.25</summary>

_Not available today._

</details>

<details><summary><b>Who is positioned how</b> — score -0.25</summary>

```text
Contract: CORN - CHICAGO BOARD OF TRADE (positions as of 2026-10-13, published the following Friday)
Large speculators: net long 13.4% of open interest (1,845,260 contracts)
Change on the week: -4.4% of open interest
Crowding: 78% percentile over 52 weeks -- within its normal range
Read this as crowding, not as a forecast: an extreme is as often the end of a move as the middle of one.
```

</details>

<details><summary><b>Money going into and out of this fund</b> — score -0.25</summary>

```text
Direction: money going out (1 month)
Share count change: 1 week: +3.2% (4.00M) over 7d | 1 month: -13.2% (-19.63M) over 30d
Shares outstanding: 7.27M | fund size: 128.70M
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Copper (CPER) · Commodity — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:** no explanation. It wrote only “NEUTRAL”, so the main reasons below are all it gave.

**Main reasons it gave:**
- Inflation 3.7% (in line with expectations) – no macro surprise.
- Technical: price below 20‑day SMA (39.03 vs 39.70) and RSI 43.9 – mixed signals.
- Positioning: net long 19.5% of OI, down -0.7% week, low crowding (15th percentile).
- Fund flows: 1‑month outflow -3.6% shares, week inflow +2.1% – mixed demand.
- Cost of holding: -4.8% annual drag versus copper – structural headwind for long.

<details><summary><b>News</b> — score +0.00</summary>

_No news found for this one today._

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.04% (-0.03 on the week) | 5-year 4.81% (-0.09 on the week) | 10-year 4.99% (-0.11 on the week) | 30-year 5.31% (-0.12 on the week)
Yield curve, 10-year minus 3-month: +0.95 points -- upward sloping (normal)
US dollar index: 101.76 (-0.08 on the week)
Volatility (VIX): 20.36 (+0.4 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.2% (2026-09-01) | jobless claims 194k (2026-10-17)
Policy and expectations: Fed target 4.00% | market expects 2.3% inflation over 10 years
Rate path: 2-year Treasury 4.81% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 39.03 (bar of 2026-10-23), from 502 daily bars
Trend: vs 20d SMA 39.70 (-1.7%), 50d 39.80 (-1.9%), 200d 37.82 (+3.2%); 50d above 200d
Momentum: RSI(14) 43.9 | MACD -0.186 vs signal -0.059 (histogram -0.127)
Returns: 1d +1.5% | 5d -1.2% | 1m -4.0% | 3m +0.7%
52-week range: 30.53 - 41.43 (now 78.0% of the way up)
Volatility: ATR(14) 0.60 (1.5% of price) | annualised 20d 18.9%
Volume: 0.25x the 20-day average
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
Cost of holding this fund instead of copper itself: -4.8% a year -- a steady drag
Measured: 3 months: fund +0.7%, commodity +2.4%, gap -1.7% | 6 months: fund +5.7%, commodity +7.8%, gap -2.1% | 12 months: fund +26.0%, commodity +30.9%, gap -4.8%
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

<details><summary><b>Buying and selling by company insiders</b> — score -0.20</summary>

_Not available today._

</details>

<details><summary><b>Who is positioned how</b> — score -0.20</summary>

```text
Contract: COPPER- #1 - COMMODITY EXCHANGE INC. (positions as of 2026-10-13, published the following Friday)
Large speculators: net long 19.5% of open interest (313,832 contracts)
Change on the week: -0.7% of open interest
Crowding: 15% percentile over 52 weeks -- within its normal range
Read this as crowding, not as a forecast: an extreme is as often the end of a move as the middle of one.
```

</details>

<details><summary><b>Money going into and out of this fund</b> — score -0.20</summary>

```text
Direction: money going out (1 month)
Share count change: 1 week: +2.1% (14.55M) over 7d | 1 month: -3.6% (-26.60M) over 30d
Shares outstanding: 18.03M | fund size: 703.54M
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Silver (SLV) · Commodity — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:** no explanation. It wrote only “NEUTRAL”, so the main reasons below are all it gave.

**Main reasons it gave:**
- No macro policy or data surprise (inflation 3.7% in line, Fed target unchanged)
- Technical downtrend: price below 20d/50d/200d SMAs, RSI 31.5, no decisive break on volume
- Positioning: net long 5.2% of OI, down 2% week over week, slight bearish tilt
- Cost of holding: -2.6% annual drag relative to silver, tempering bullish conviction

<details><summary><b>News</b> — score +0.00</summary>

- [Nasdaq Futures Rise After Chip Selloff While S&P 500, Dow Track Mixed Open: SLV, GLD, SOXL, BE In Focus](https://es.tradingview.com/news/stocktwits:704374f6a094b:0-nasdaq-futures-rise-after-chip-selloff-while-s-p-500-dow-track-mixed-open-slv-gld-soxl-be-in-focus/)  
  <sub>TradingView, 12 hours ago</sub>  
  U.S. stock futures were mixed overnight late Thursday after a sharp selloff in chip stocks.As of 10:36 p.m. EDT, Nasdaq-100 futures were up 0.18%.
- [Nasdaq Futures Rise After Chip Selloff: 3 ETFs [2026]](https://shattered.io/nasdaq-futures-rise-chip-selloff-slv-gld-soxl-be-2026/)  
  <sub>shattered.io, 4 hours ago</sub>  
  Nasdaq futures rise after the chip selloff. See how SLV, GLD and SOXL are positioned and which of these 3 ETFs looks strongest in 2026.
- [Nasdaq Futures Rise 0.18% After 2.6% Chip Rout [2026]](https://tech-insider.org/nasdaq-futures-rise-chip-selloff-slv-gld-soxl-be-2026/)  
  <sub>https://tech-insider.org/, 3 hours ago</sub>  
  Nasdaq futures rose 0.18% after a 2.60% chip-led drop. See how Intel, AMD, SLV, GLD, SOXL and BE moved and what it means for hardware.
- [Gold Is Sliding Back Toward $4,000 as the Haven Trade Breaks](https://247wallst.com/investing/2026/10/23/gold-is-sliding-back-toward-4000-as-the-haven-trade-breaks/)  
  <sub>24/7 Wall St., 2 hours ago</sub>  
  Stocks sold off, Treasuries rallied, and gold collapsed anyway, breaking the rule that bullion rises when markets panic. Something shifted in how traders...
- [Nippon Silver ETF, other silver ETFs slide up to 4% as silver prices tumble. Here’s why](https://m.economictimes.com/markets/stocks/news/nippon-silver-etf-other-silver-etfs-slide-up-to-4-as-silver-prices-tumble-heres-why/articleshow/135137769.cms)  
  <sub>The Economic Times, 8 hours ago</sub>  
  Silver ETFs tumble up to 4% as India permits 6500 metric tonnes of silver imports over six months, raising expectations of easing domestic supply tightness...
- [Silver Stalls: SLVP And Other Silver Mining ETFs Can Provide Clues (BATS:SLVP)](https://seekingalpha.com/article/4956569-silver-stalls-slvp-and-other-silver-mining-etfs-can-provide-clues)  
  <sub>Seeking Alpha, 21 hours ago</sub>  
  The iShares MSCI Global Silver and Metals Miners ETF is reiterated as a Buy below $34 per share in October 2026. Click to read more on the SLVP fund.
- [Is A War Imminent? Concerns Overshadow Strong Meta, Tesla Earnings](https://www.benzinga.com/opinion/26/10/62537507/is-a-war-imminent-concerns-overshadow-strong-meta-tesla-earnings)  
  <sub>Benzinga, 22 hours ago</sub>  
  Crosscurrents In The Market Please click here for an enlarged chart of United States Oil ETF (NYSE:USO). Note the following: The chart shows that oil ETF...
- [Silver ETFs fall up to 5% as oil surge, inflation fears hit bullion markets](https://www.business-standard.com/markets/news/silver-etfs-fall-up-to-5-as-oil-surge-inflation-fears-hit-bullion-markets-126102300376_1.html)  
  <sub>Business Standard, 9 hours ago</sub>  
  Silver exchange-traded funds (ETFs) continued to remain under selling pressure on Friday, October 23, 2026, mirroring a fall in precious metals prices.
- [Daily ETF Flows: Chip ETFs See Inflows](https://finance.yahoo.com/markets/options/articles/daily-etf-flows-chip-etfs-213158129.html)  
  <sub>Yahoo Finance, 18 hours ago</sub>  
  Top 10 Creations (All ETFs). Ticker. Name. Net Flows ($, mm). AUM ($, mm). AUM % Change. SOXX · iShares Semiconductor ETF. 2,551.44. 44,525.14. 5.73%.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.04% (-0.03 on the week) | 5-year 4.81% (-0.09 on the week) | 10-year 4.99% (-0.11 on the week) | 30-year 5.31% (-0.12 on the week)
Yield curve, 10-year minus 3-month: +0.95 points -- upward sloping (normal)
US dollar index: 101.76 (-0.08 on the week)
Volatility (VIX): 20.36 (+0.4 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.2% (2026-09-01) | jobless claims 194k (2026-10-17)
Policy and expectations: Fed target 4.00% | market expects 2.3% inflation over 10 years
Rate path: 2-year Treasury 4.81% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 48.78 (bar of 2026-10-23), from 502 daily bars
Trend: vs 20d SMA 53.14 (-8.2%), 50d 56.99 (-14.4%), 200d 64.95 (-24.9%); 50d below 200d
Momentum: RSI(14) 31.5 | MACD -1.910 vs signal -1.595 (histogram -0.315)
Returns: 1d -1.1% | 5d -5.3% | 1m -15.3% | 3m -7.8%
52-week range: 42.40 - 105.60 (now 10.1% of the way up)
Volatility: ATR(14) 1.56 (3.2% of price) | annualised 20d 40.5%
Volume: 0.70x the 20-day average
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
Cost of holding this fund instead of silver itself: -2.6% a year -- a steady drag
Measured: 3 months: fund -7.8%, commodity -7.7%, gap -0.1% | 6 months: fund -29.1%, commodity -29.3%, gap +0.2% | 12 months: fund +11.2%, commodity +13.7%, gap -2.6%
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
Direction: money coming in (1 month)
Share count change: 1 week: +4.6% (1.25B) over 7d | 1 month: +0.7% (191.04M) over 30d
Shares outstanding: 576.71M | fund size: 28.13B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Soybeans (SOYB) · Commodity — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:** no explanation. It wrote only “NEUTRAL”, so the main reasons below are all it gave.

**Main reasons it gave:**
- Technical indicators mixed: price below 20‑day and 50‑day SMA, RSI 42.5, MACD negative
- Fund flows: share count up 2.9% in 1 week, indicating modest inflows
- Crop condition: slight deterioration (-1 point) over 3 weeks, bullish supply
- Cost of holding: -1% annual drag, tempering bullish case
- Positioning: crowded long (92% percentile) with small net long increase (+0.3%)

<details><summary><b>News</b> — score +0.00</summary>

_No news found for this one today._

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.04% (-0.03 on the week) | 5-year 4.81% (-0.09 on the week) | 10-year 4.99% (-0.11 on the week) | 30-year 5.31% (-0.12 on the week)
Yield curve, 10-year minus 3-month: +0.95 points -- upward sloping (normal)
US dollar index: 101.76 (-0.08 on the week)
Volatility (VIX): 20.36 (+0.4 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.2% (2026-09-01) | jobless claims 194k (2026-10-17)
Policy and expectations: Fed target 4.00% | market expects 2.3% inflation over 10 years
Rate path: 2-year Treasury 4.81% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 26.83 (bar of 2026-10-23), from 502 daily bars
Trend: vs 20d SMA 27.19 (-1.3%), 50d 27.21 (-1.4%), 200d 25.00 (+7.3%); 50d above 200d
Momentum: RSI(14) 42.5 | MACD -0.169 vs signal -0.072 (histogram -0.097)
Returns: 1d +0.7% | 5d -0.2% | 1m -3.9% | 3m +4.8%
52-week range: 21.71 - 28.14 (now 79.6% of the way up)
Volatility: ATR(14) 0.27 (1.0% of price) | annualised 20d 11.0%
Volume: 1.33x the 20-day average
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
Cost of holding this fund instead of soybeans itself: -1.0% a year -- a steady drag
Measured: 3 months: fund +4.8%, commodity +5.2%, gap -0.3% | 6 months: fund +9.6%, commodity +9.2%, gap +0.4% | 12 months: fund +21.8%, commodity +22.8%, gap -1.0%
A commodity fund holds futures, not soybeans, and must sell each expiring contract to buy the next one. Where the next month costs more, that roll loses money every month. This gap is what the structure has actually cost, fees included -- it is history rather than a forecast, and it is not a direction: heavy carry is a reason to want a larger move to justify a long, and a tailwind for a short.
```

</details>

<details><summary><b>How much oil and gas is in storage</b> — score +0.00</summary>

_Not available today._

</details>

<details><summary><b>How the crop is growing</b> — score +0.00</summary>

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
Share count change: 1 week: +2.9% (1.31M) over 7d | 1 month: +1.8% (830.76K) over 30d
Shares outstanding: 1.71M | fund size: 45.79M
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Natural gas (UNG) · Commodity — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> No macro surprise, policy shift, or decisive technical break on heavy volume; bearish technicals and fundamentals are present but not strong enough to justify a directional call.

**Main reasons it gave:**
- CFTC net short 7.3% of open interest, up 0.7% week over week
- Cost of holding -14.9% annual, heavy roll cost
- US natural gas inventories built 77 Bcf, 87th percentile
- EIA forecast price down 18% over six months
- Technicals: price below 20d, 50d, 200d SMAs, RSI 34.3

<details><summary><b>News</b> — score +0.00</summary>

- [UNG Jan 2029 20.000 call (UNG290119C00020000) Interactive Stock Chart](https://ca.finance.yahoo.com/quote/UNG290119C00020000/chart/)  
  <sub>Yahoo! Finance Canada, 22 hours ago</sub>  
  Interactive Chart for UNG Jan 2029 20.000 call (UNG290119C00020000), analyze all the data with a huge range of indicators.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.04% (-0.03 on the week) | 5-year 4.81% (-0.09 on the week) | 10-year 4.99% (-0.11 on the week) | 30-year 5.31% (-0.12 on the week)
Yield curve, 10-year minus 3-month: +0.95 points -- upward sloping (normal)
US dollar index: 101.76 (-0.08 on the week)
Volatility (VIX): 20.36 (+0.4 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.2% (2026-09-01) | jobless claims 194k (2026-10-17)
Policy and expectations: Fed target 4.00% | market expects 2.3% inflation over 10 years
Rate path: 2-year Treasury 4.81% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score -0.20</summary>

```text
Last close 9.56 (bar of 2026-10-23), from 502 daily bars
Trend: vs 20d SMA 10.60 (-9.8%), 50d 10.48 (-8.8%), 200d 11.23 (-14.9%); 50d below 200d
Momentum: RSI(14) 34.3 | MACD -0.136 vs signal 0.023 (histogram -0.159)
Returns: 1d -3.4% | 5d -10.4% | 1m -17.3% | 3m -5.5%
52-week range: 9.56 - 16.90 (now 0.0% of the way up)
Volatility: ATR(14) 0.37 (3.9% of price) | annualised 20d 41.3%
Volume: 0.37x the 20-day average
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
Cost of holding this fund instead of natural gas itself: -14.9% a year -- heavy: rolling contracts costs this fund real money
Measured: 3 months: fund -5.5%, commodity +9.8%, gap -15.2% | 6 months: fund -7.3%, commodity +20.4%, gap -27.7% | 12 months: fund -26.8%, commodity -12.0%, gap -14.9%
A commodity fund holds futures, not natural gas, and must sell each expiring contract to buy the next one. Where the next month costs more, that roll loses money every month. This gap is what the structure has actually cost, fees included -- it is history rather than a forecast, and it is not a direction: heavy carry is a reason to want a larger move to justify a long, and a tailwind for a short.
```

</details>

<details><summary><b>How much oil and gas is in storage</b> — score -0.50</summary>

```text
US inventories, week ending 2026-10-16 (published the following Wednesday)
  Natural gas: 3,644.0 billion cubic feet, +77.0 on the week (a build), 87% percentile over 52 weeks -- high for the time of year
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
Direction: money going out (1 month)
Share count change: 1 week: +13.1% (50.68M) over 7d | 1 month: -17.2% (-91.19M) over 30d
Shares outstanding: 45.87M | fund size: 438.25M
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Oil (USO) · Commodity — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:** no explanation. It wrote only “NEUTRAL”, so the main reasons below are all it gave.

**Main reasons it gave:**
- Treasury yields down slightly, no rate surprise
- RSI 70.6 indicates overbought but no decisive break on volume
- CFTC large speculators net long decreased 0.7% week over week
- EIA price outlook forecasts WTI falling to $100, well below current $167 price

<details><summary><b>News</b> — score +0.00</summary>

- [U.S. oil exports to Asia plunge as war disrupts shipping, lifting tanker rates to record high](https://seekingalpha.com/news/4656368-us-oil-exports-to-asia-plunge-as-war-disrupts-shipping-lifting-tanker-rates-to-record-high)  
  <sub>Seeking Alpha, 15 hours ago</sub>  
  US crude oil exports to Asia are poised to hit multiyear lows after the Iran war disrupted global shipping and lifted the cost to lease a tanker for the...
- [Is A War Imminent? Concerns Overshadow Strong Meta, Tesla Earnings](https://www.benzinga.com/opinion/26/10/62537507/is-a-war-imminent-concerns-overshadow-strong-meta-tesla-earnings)  
  <sub>Benzinga, 22 hours ago</sub>  
  Crosscurrents In The Market Please click here for an enlarged chart of United States Oil ETF (NYSE:USO). Note the following: The chart shows that oil ETF...
- [USO Nov 2026 159.000 call (USO261106C00159000) Stock Price, News, Quote & History](https://ca.finance.yahoo.com/quote/USO261106C00159000/)  
  <sub>Yahoo! Finance Canada, 20 hours ago</sub>  
  Find the latest USO Nov 2026 159.000 call (USO261106C00159000) stock quote, history, news and other vital information to help you with your stock trading...
- [USO Aug 2027 105.000 call (USO270820C00105000) Interactive Stock Chart](https://ca.finance.yahoo.com/quote/USO270820C00105000/chart/)  
  <sub>Yahoo! Finance Canada, 20 hours ago</sub>  
  Interactive Chart for USO Aug 2027 105.000 call (USO270820C00105000), analyze all the data with a huge range of indicators.
- [USO Jul 2027 100.000 put (USO270716P00100000) Interactive Stock Chart](https://ca.finance.yahoo.com/quote/USO270716P00100000/chart/)  
  <sub>Yahoo! Finance Canada, 21 hours ago</sub>  
  Interactive Chart for USO Jul 2027 100.000 put (USO270716P00100000), analyze all the data with a huge range of indicators.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.04% (-0.03 on the week) | 5-year 4.81% (-0.09 on the week) | 10-year 4.99% (-0.11 on the week) | 30-year 5.31% (-0.12 on the week)
Yield curve, 10-year minus 3-month: +0.95 points -- upward sloping (normal)
US dollar index: 101.76 (-0.08 on the week)
Volatility (VIX): 20.36 (+0.4 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.2% (2026-09-01) | jobless claims 194k (2026-10-17)
Policy and expectations: Fed target 4.00% | market expects 2.3% inflation over 10 years
Rate path: 2-year Treasury 4.81% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 167.42 (bar of 2026-10-23), from 502 daily bars
Trend: vs 20d SMA 152.64 (+9.7%), 50d 146.43 (+14.3%), 200d 121.59 (+37.7%); 50d above 200d
Momentum: RSI(14) 70.6 | MACD 4.940 vs signal 3.741 (histogram 1.199)
Returns: 1d +3.0% | 5d +3.5% | 1m +9.4% | 3m +34.2%
52-week range: 66.17 - 167.42 (now 100.0% of the way up)
Volatility: ATR(14) 4.90 (2.9% of price) | annualised 20d 31.1%
Volume: 0.54x the 20-day average
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
US inventories, week ending 2026-10-16 (published the following Wednesday)
  Crude oil: 412.5 million barrels, -3.1 on the week (a draw), 15% percentile over 52 weeks
  Petrol: 205.3 million barrels, -3.0 on the week (a draw), 8% percentile over 52 weeks -- low for the time of year
  Diesel: 104.3 million barrels, +1.7 on the week (a build), 25% percentile over 52 weeks
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

<details><summary><b>Buying and selling by company insiders</b> — score -0.10</summary>

_Not available today._

</details>

<details><summary><b>Who is positioned how</b> — score -0.10</summary>

```text
Contract: WTI-PHYSICAL - NEW YORK MERCANTILE EXCHANGE (positions as of 2026-10-13, published the following Friday)
Large speculators: net long 2.1% of open interest (1,900,179 contracts)
Change on the week: -0.7% of open interest
Crowding: 35% percentile over 52 weeks -- within its normal range
Read this as crowding, not as a forecast: an extreme is as often the end of a move as the middle of one.
```

</details>

<details><summary><b>Money going into and out of this fund</b> — score -0.10</summary>

```text
Direction: money going out (1 month)
Share count change: 1 week: -4.2% (-77.28M) over 7d | 1 month: -13.4% (-274.94M) over 30d
Shares outstanding: 10.64M | fund size: 1.78B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Wheat (WEAT) · Commodity — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Neutral stance given lack of material macro surprise, mixed technicals, modest bearish positioning, outflows, and heavy roll cost for longs.

**Main reasons it gave:**
- RSI 24.9 indicates oversold condition while price below 20‑day SMA
- Large speculators net short 6.4% of open interest, modest bearish bias
- Fund share count down 11.9% over past month, indicating outflows
- Cost of holding -11.1% annual reflects heavy roll cost for longs

<details><summary><b>News</b> — score +0.00</summary>

- [WEAT Nov 2026 19.000 put (WEAT261120P00019000) Stock Price, News, Quote & History](https://ca.finance.yahoo.com/quote/WEAT261120P00019000/)  
  <sub>Yahoo! Finance Canada, 19 hours ago</sub>  
  Find the latest WEAT Nov 2026 19.000 put (WEAT261120P00019000) stock quote, history, news and other vital information to help you with your stock trading...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.04% (-0.03 on the week) | 5-year 4.81% (-0.09 on the week) | 10-year 4.99% (-0.11 on the week) | 30-year 5.31% (-0.12 on the week)
Yield curve, 10-year minus 3-month: +0.95 points -- upward sloping (normal)
US dollar index: 101.76 (-0.08 on the week)
Volatility (VIX): 20.36 (+0.4 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.2% (2026-09-01) | jobless claims 194k (2026-10-17)
Policy and expectations: Fed target 4.00% | market expects 2.3% inflation over 10 years
Rate path: 2-year Treasury 4.81% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score -0.20</summary>

```text
Last close 22.79 (bar of 2026-10-23), from 502 daily bars
Trend: vs 20d SMA 24.31 (-6.3%), 50d 25.48 (-10.6%), 200d 23.48 (-3.0%); 50d above 200d
Momentum: RSI(14) 24.9 | MACD -0.671 vs signal -0.507 (histogram -0.164)
Returns: 1d -0.2% | 5d -5.0% | 1m -10.9% | 3m -7.1%
52-week range: 19.88 - 28.00 (now 35.8% of the way up)
Volatility: ATR(14) 0.45 (2.0% of price) | annualised 20d 17.9%
Volume: 0.72x the 20-day average
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
Cost of holding this fund instead of wheat itself: -11.1% a year -- heavy: rolling contracts costs this fund real money
Measured: 3 months: fund -7.1%, commodity -5.4%, gap -1.7% | 6 months: fund -1.7%, commodity +2.7%, gap -4.4% | 12 months: fund +12.8%, commodity +24.0%, gap -11.1%
A commodity fund holds futures, not wheat, and must sell each expiring contract to buy the next one. Where the next month costs more, that roll loses money every month. This gap is what the structure has actually cost, fees included -- it is history rather than a forecast, and it is not a direction: heavy carry is a reason to want a larger move to justify a long, and a tailwind for a short.
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
Contract: WHEAT-SRW - CHICAGO BOARD OF TRADE (positions as of 2026-10-13, published the following Friday)
Large speculators: net short 6.4% of open interest (506,774 contracts)
Change on the week: -0.6% of open interest
Crowding: 58% percentile over 52 weeks -- within its normal range
Read this as crowding, not as a forecast: an extreme is as often the end of a move as the middle of one.
```

</details>

<details><summary><b>Money going into and out of this fund</b> — score -0.10</summary>

```text
Direction: money going out (1 month)
Share count change: 1 week: +5.6% (14.88M) over 7d | 1 month: -11.9% (-38.03M) over 30d
Shares outstanding: 12.34M | fund size: 281.13M
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Gold (GLD) · Commodity — no answer, no confidence given

<details><summary><b>News</b> — score n/a</summary>

- [Nasdaq Futures Rise After Chip Selloff: 3 ETFs [2026]](https://shattered.io/nasdaq-futures-rise-chip-selloff-slv-gld-soxl-be-2026/)  
  <sub>shattered.io, 4 hours ago</sub>  
  Nasdaq futures rise after the chip selloff. See how SLV, GLD and SOXL are positioned and which of these 3 ETFs looks strongest in 2026.
- [Nasdaq Futures Rise After Chip Selloff While S&P 500, Dow Track Mixed Open: SLV, GLD, SOXL, BE In Focus](https://es.tradingview.com/news/stocktwits:704374f6a094b:0-nasdaq-futures-rise-after-chip-selloff-while-s-p-500-dow-track-mixed-open-slv-gld-soxl-be-in-focus/)  
  <sub>TradingView, 12 hours ago</sub>  
  U.S. stock futures were mixed overnight late Thursday after a sharp selloff in chip stocks.As of 10:36 p.m. EDT, Nasdaq-100 futures were up 0.18%.
- [Nasdaq Futures Rise 0.18% After 2.6% Chip Rout [2026]](https://tech-insider.org/nasdaq-futures-rise-chip-selloff-slv-gld-soxl-be-2026/)  
  <sub>https://tech-insider.org/, 3 hours ago</sub>  
  Nasdaq futures rose 0.18% after a 2.60% chip-led drop. See how Intel, AMD, SLV, GLD, SOXL and BE moved and what it means for hardware.
- [Flight to Safety: Treasuries Rally as Gold Draws Dip-Buyers](https://www.moomoo.com/community/feed/flight-to-safety-us-treasuries-regain-safe-haven-status-as-117489323147270?chain_id=Name1K9-3FXPhg.1ldm500&global_content=%7B%22promote_id%22%3A13764%2C%22sub_promote_id%22%3A107%2C%22f%22%3A%22www.moomoo.com%2Fetfs%2FSPXL-US%22%7D)  
  <sub>Moomoo, 6 hours ago</sub>  
  Executive Summary: · Macro Regime Shift: The market logic is transitioning from "inflation and hawkish Fed risk" to "growth deceleration and AI capex ...
- [Gold And Midterms: Is This Time Different?](https://seekingalpha.com/article/4956929-gold-midterms-is-this-time-different)  
  <sub>Seeking Alpha, 1 hour ago</sub>  
  Prediction markets are pricing in a high chance of Democrats regaining at least some control of Congress. Read more here.
- [Why Did AAPL, KO, KDP Stocks Hit 52-Week Highs Today?](https://stocktwits.com/news-articles/markets/equity/why-did-aapl-ko-kdp-stocks-hit-52-week-highs-today/cZxyRFLRBDA)  
  <sub>Stocktwits, 6 hours ago</sub>  
  Apple Inc. (AAPL), Coca-Cola Co. (KO) and Keurig Dr Pepper (KDP) hit fresh 52-week highs on Thursday as investors reacted to strong demand for Apple's new...
- [SPDR Gold Trust (GLD) Stock Price Today: $368.12](https://pluang.com/en/asset/usstock/GLD/10890)  
  <sub>Pluang, 12 hours ago</sub>  
  Track SPDR Gold Trust (GLD) stock price today on Pluang, updated in real time with live charts and market data. Over the past 52 weeks, SPDR Gold Trust has...
- [Bill Baruch market update: SMH & QQQ slide, RSP, WMT, LLY, AAPL rise, GLD pressured](https://www.theglobeandmail.com/investing/markets/indices/TTGD/pressreleases/8341118/bill-baruch-market-update-smh-qqq-slide-rsp-wmt-lly-aapl-rise-gld-pressured/)  
  <sub>The Globe and Mail, 17 hours ago</sub>  
  Ugly day led by $SMH $QQQ. On bright side $RSP $WMT $LLY $AAPL +. Also $GLD bludgeoned despite $TLT #USD central bank buying and great ETF flows.
- [GLD NTA 22-10-2026 $3.83925](https://www.businessdesk.co.nz/nzx-announcements/gld-etf-units/482310)  
  <sub>BusinessDesk, 12 hours ago</sub>  
  View the full NZX announcement for Smart Gold ETF (GLD): GLD NTA 22-10-2026 $3.83925. Financial updates and company disclosures on BusinessDesk.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score n/a</summary>

```text
US Treasury yields: 3-month 4.04% (-0.03 on the week) | 5-year 4.81% (-0.09 on the week) | 10-year 4.99% (-0.11 on the week) | 30-year 5.31% (-0.12 on the week)
Yield curve, 10-year minus 3-month: +0.95 points -- upward sloping (normal)
US dollar index: 101.76 (-0.08 on the week)
Volatility (VIX): 20.36 (+0.4 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.2% (2026-09-01) | jobless claims 194k (2026-10-17)
Policy and expectations: Fed target 4.00% | market expects 2.3% inflation over 10 years
Rate path: 2-year Treasury 4.81% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score n/a</summary>

```text
Last close 366.33 (bar of 2026-10-23), from 502 daily bars
Trend: vs 20d SMA 379.08 (-3.4%), 50d 394.50 (-7.1%), 200d 414.21 (-11.6%); 50d below 200d
Momentum: RSI(14) 33.9 | MACD -5.334 vs signal -4.633 (histogram -0.701)
Returns: 1d -0.7% | 5d -4.1% | 1m -6.5% | 3m -2.2%
52-week range: 362.32 - 495.90 (now 3.0% of the way up)
Volatility: ATR(14) 5.83 (1.6% of price) | annualised 20d 21.9%
Volume: 0.55x the 20-day average
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
Cost of holding this fund instead of gold itself: -1.6% a year -- a steady drag
Measured: 3 months: fund -2.2%, commodity -1.6%, gap -0.6% | 6 months: fund -15.4%, commodity -15.4%, gap -0.1% | 12 months: fund -2.9%, commodity -1.3%, gap -1.6%
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
Share count change: 1 week: +0.0% (0.00) over 7d | 1 month: +0.0% (0.00) over 30d
Shares outstanding: 260.30M | fund size: 95.36B
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

