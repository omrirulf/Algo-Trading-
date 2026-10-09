# Daily report

**09 Oct 2026, 18:40 Israel time (15:40 UTC)** · 80 names checked · 3 traded · 1 with a problem

**Answers with no explanation:** 11 of 63 (the model wrote only a label, like “NEUTRAL”, where its reason should be). Their main reasons are still shown.

**Run:** started by the outside scheduler (via supabase-cron), on time (planned for 14:40 UTC).

| Group | Looked at | Took a side | No clear view | Problems |
| --- | --- | --- | --- | --- |
| Companies | 16 | 5 | 11 | 0 |
| Whole-market funds | 14 | 0 | 14 | 0 |
| Sector and country funds | 41 | 0 | 41 | 0 |
| Commodities | 9 | 0 | 8 | 1 |

## Open positions

Checked before any new trade. R is what the trade risked at entry; the ladder sells a third at +1R and another at +3R, the stop-loss follows the price up every day, and it only ever moves up.

| Position | What happened |
| --- | --- |
| Exxon Mobil (XOM) · Company | **Sold part.** Sold 4 of 13 shares at +1.11R, 9 still held. Stop-loss raised 160.76 → 162.75. |
| United Kingdom (EWU) · Sector or country | **Stop raised.** At +0.19R, following the price. Stop-loss raised 45.39 → 45.41. |
| Brazil (EWZ) · Sector or country | **Stop raised.** At +0.17R, following the price. Stop-loss raised 40.88 → 41.35. |
| Gold mining companies (GDX) · Sector or country | **Stop raised.** At +0.21R, following the price. Stop-loss raised 81.27 → 82.63. |
| Teva Pharmaceutical (TEVA) · Company | **Stop raised.** At +0.90R, following the price. Stop-loss raised 37.20 → 38.87. |
| Argentina (ARGT) · Sector or country | **Holding.** +0.07R, holding 80 shares. Stop-loss 86.01. |
| Poland (EPOL) · Sector or country | **Holding.** +0.09R, holding 164 shares. Stop-loss 43.03. |
| Gold (GLD) · Commodity | **Holding.** +0.36R, holding 10 shares. Stop-loss 389.68. |
| US company bonds, riskier (HYG) · Index fund | **Holding.** +0.02R, holding 158 shares. Stop-loss 76.59. |
| US government bonds, 7-10 years (IEF) · Index fund | **Holding.** +2.56R, holding 40 shares. Stop-loss 89.85. |
| Eli Lilly (LLY) · Company | **Holding.** +0.39R, holding 4 shares. Stop-loss 1130.70. |
| Microsoft (MSFT) · Company | **Holding.** +1.95R, holding 7 shares. Stop-loss 510.27. |
| Novo Nordisk (NVO) · Company | **Holding.** +0.47R, holding 123 shares. Stop-loss 39.01. |
| US inflation-linked bonds (TIP) · Index fund | **Holding.** +2.53R, holding 4 shares. Stop-loss 104.79. |
| US government bonds, 20+ years (TLT) · Index fund | **Holding.** +2.74R, holding 45 shares. Stop-loss 78.49. |
| US dollar (UUP) · Index fund | **Holding.** +3.07R, holding 142 shares. Stop-loss 28.80. |

## How to read this

Once a day the system looks at every name on the list. For each one it reads five kinds of evidence and gives each kind a score from -1.00 (bad) to +1.00 (good). Then it picks a side and says how sure it is, from 0.00 to 1.00.

The three sides: **BULLISH** = the model thinks the price will go up; **BEARISH** = the model thinks the price will go down; **NEUTRAL** = the model has no clear view.

Being sure is not enough on its own. A trade only happens when confidence reaches **0.30**. Below that the system writes down what it thought and does nothing. The size of a trade, the stop-loss and every limit are decided by plain code, not by the model.

Open positions are checked first, before any new trade. When a trade has earned back what it risked (+1R), a third of it is sold and the stop-loss moves up to the entry price, so it can no longer lose. At three times that (+3R) another third is sold and the stop moves up again. The last third stays open. Every day the stop-loss also follows the price up, so a position only ever closes when its stop is hit. The stop only ever moves up.

Under each name you will find the five scores. Click a grey line to open it and see the exact evidence behind that score. The words inside quotation marks are the model's own; nothing there has been rewritten.

## Companies

### Alphabet (Google) (GOOGL) · Company — BULLISH, confidence 0.85

**Result:** ACCEPTED · 14 shares · submitted buy 14 GOOGL @ ~352.30, stop 335.64

**In the model's own words:**

> The AI model launch and AI chip partnership provide a clear, material catalyst, reinforced by strong fundamentals and a bullish analyst consensus. Technicals are moderately supportive despite thin volume, and there is no insider activity to offset the view. Mixed earnings record is neutral.

**Main reasons it gave:**
- Gemini 4 Argon AI model launch (NEWS)
- AI compute scale advantage and AI chip partnership (NEWS)
- Revenue growth +24% YoY, profit margin 54.8% (FUNDAMENTALS)
- Analyst consensus strong buy with mean price target +22% (ANALYST VIEW)
- Price above 20d, 50d, 200d SMAs with positive MACD (TECHNICALS)

<details><summary><b>News</b> — score +0.85</summary>

- [Is Alphabet Stock Priced Right Against Its Peers?](https://www.trefis.com/stock/googl/articles/618146/is-alphabet-stock-priced-right-against-its-peers/2026-10-09)  
  <sub>Trefis, 1 hour ago</sub>  
  Measured against five other large companies: Microsoft, Amazon, Meta Platforms, Apple, and Netflix, Alphabet (GOOGL) looks like an anomaly.
- [GOOGL Stock Rises After Gemini 4 Argon Launch, But JPMorgan Says Google Must Reclaim AI Leadership](https://stocktwits.com/news-articles/markets/equity/googl-stock-gemini-4-argon-launch-reclaim-leadership/cZD05VWRBip)  
  <sub>Stocktwits, 4 hours ago</sub>  
  Alphabet (GOOG, GOOGL) shares rose Thursday after Google unveiled Gemini 4 Argon, its latest frontier AI model, with JPMorgan saying the launch could help...
- [Here are the Compelling Reasons to Add Alphabet (GOOGL)](https://finance.yahoo.com/markets/stocks/articles/compelling-reasons-add-alphabet-googl-140721129.html)  
  <sub>Yahoo Finance, 34 minutes ago</sub>  
  Vision Capital Fund, an investment management company, released its third-quarter 2026 investor letter. The letter can be downloaded here.
- [Alphabet: A 'Strong Buy' Due To Its AI Compute Scale](https://seekingalpha.com/article/4952964-alphabet-stock-strong-buy-due-to-its-compute-scale)  
  <sub>Seeking Alpha, 8 hours ago</sub>  
  Alphabet is reiterated as a 'Strong Buy' due to unmatched AI compute scale and TPU cost advantages. Read more on GOOG stock here.
- [$1,000 invested in GOOGL stock when Google bought YouTube is now worth](https://finbold.com/1000-invested-in-googl-stock-when-google-bought-youtube-is-now-worth/)  
  <sub>Finbold, 7 hours ago</sub>  
  When Google (NASDAQ: GOOGL) acquired the video platform YouTube twenty years ago – on October 9, 2006 – the former had its stock trading at $10.74 after...
- [Alphabet and Unity Level Up Game Development](https://www.marketbeat.com/articles/alphabet-and-unity-level-up-game-development/)  
  <sub>MarketBeat, 3 hours ago</sub>  
  Alphabet and Unity Software announced a generative AI gaming partnership on Oct. 7, letting creators build games via text prompts, a shift that strengthens...
- [Nuclear Power Deal Might Change The Case For Investing In Google (GOOGL)](https://simplywall.st/stocks/us/media/nasdaq-googl/alphabet/news/nuclear-power-deal-might-change-the-case-for-investing-in-go)  
  <sub>Simply Wall Street, 8 hours ago</sub>  
  Alphabet's Google has agreed a 20 year, US$4.3 billion nuclear power purchase with Constellation Energy to secure 890 megawatts of new carbon free capacity...
- [3 Stocks Poised to Gain as Google Brings Its AI Chips to Market](https://www.fool.com/investing/2026/10/09/3-stocks-poised-to-gain-as-google-brings-its-ai-ch/)  
  <sub>The Motley Fool, 8 hours ago</sub>  
  Google may become a major AI chipmaker, and there are some clear winners from that development.
- [Google Workspace Gets AI Agents. What It Means for Alphabet Stock.](https://www.barrons.com/articles/google-ai-agent-alphabet-stock-400e9d53)  
  <sub>Barron's, 19 hours ago</sub>  
  Google's new Gemini agent can complete tasks across workplace apps, intensifying competition with OpenAI and Microsoft for business customers.
- [GOOG, GOOGL Securities Alert: Lose Money on Your Alphabet](https://www.globenewswire.com/news-release/2026/10/09/3377970/0/en/goog-googl-securities-alert-lose-money-on-your-alphabet-investment-bfa-law-notifies-investors-of-the-filed-securities-class-action-over-ai-issues.html)  
  <sub>GlobeNewswire, 4 hours ago</sub>  
  Lose Money on Your Alphabet Investment? BFA Law Notifies Investors of the Filed Securities Class Action over AI Issues...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.85</summary>

_Not available today._

</details>

<details><summary><b>Price and chart</b> — score +0.35</summary>

```text
Last close 351.20 (bar of 2026-10-09), from 502 daily bars
Trend: vs 20d SMA 345.90 (+1.5%), 50d 346.24 (+1.4%), 200d 340.03 (+3.3%); 50d above 200d
Momentum: RSI(14) 56.0 | MACD 1.222 vs signal 0.323 (histogram 0.898)
Returns: 1d +0.8% | 5d +2.2% | 1m +5.6% | 3m -0.4%
52-week range: 236.57 - 402.62 (now 69.0% of the way up)
Volatility: ATR(14) 8.33 (2.4% of price) | annualised 20d 23.8%
Volume: 0.16x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.90</summary>

```text
Sector: Communication Services / Internet Content & Information | market cap 4.30T
Valuation: trailing P/E 17.62 | forward P/E 23.09 | P/B 6.90 | PEG 1.25
Profitability: profit margin 54.8% | operating margin 34.0% | ROE 48.7%
Growth (YoY): revenue +24.2% | earnings +294.0%
Balance sheet: debt/equity 18.9% | free cash flow 22.67B
Risk: beta 1.21 | short interest 1.5% of float
Next earnings: 2026-10-28
```

</details>

<details><summary><b>What this fund holds</b> — score +0.90</summary>

_Not available today._

</details>

<details><summary><b>Does this company beat its own forecasts</b> — score +0.90</summary>

```text
Earnings record, last 4 quarters: 2 beats, 2 missed
  2026-06-30 missed by 4% | 2026-03-31 missed by 3% | 2025-12-31 beat by 4% | 2025-09-30 beat by 29%
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

<details><summary><b>What analysts and big funds say</b> — score +0.60</summary>

```text
Consensus: strong_buy (mean 1.38 on a 1=strong buy to 5=strong sell scale, 54 analysts)
Ratings: 13 strong buy, 43 buy, 5 hold, 0 sell, 0 strong sell
Price target: mean 429.47 (+22.3% vs last close), range 340.00 - 515.00
Recent rating changes:
  - 2026-10-08 Needham: reit, Buy -> Buy
  - 2026-10-06 Wells Fargo: main, Overweight -> Overweight
  - 2026-09-28 Piper Sandler: reit, Overweight -> Overweight
  - 2026-09-18 Tigress Financial: main, Strong Buy -> Strong Buy
  - 2026-09-17 Evercore ISI Group: main, Outperform -> Outperform
  - 2026-09-03 Rosenblatt: main, Buy -> Buy
Institutional ownership: 81.0%
Largest holders: Blackrock Inc. (7.9%), Vanguard Capital Management LLC (6.5%), FMR, LLC (4.3%), State Street Corporation (4.1%), Geode Capital Management, LLC (2.6%)
```

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score +0.60</summary>

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

### Nvidia (NVDA) · Company — BULLISH, confidence 0.65

**Result:** ACCEPTED · 22 shares · submitted buy 22 NVDA @ ~230.02, stop 218.74

**In the model's own words:**

> The overall picture is bullish: strong fundamentals and earnings record, price above key moving averages, and a material ticker‑specific catalyst (SpaceX interest). Technicals are modestly supportive but low volume tempers confidence. Insider sales are routine and provide no directional signal. Analyst consensus is already strongly bullish, adding little new information.

**Main reasons it gave:**
- SpaceX intends to buy Nvidia chips (Stocktwits) – ticker‑specific catalyst
- Strong fundamentals: trailing P/E 29.2, forward P/E 14.5, ROE 117% (Fundamentals)
- 3 of last 4 quarters beat earnings (Earnings Record)
- Price above 20‑day, 50‑day, 200‑day SMAs; RSI 54.8 (Technical)
- Insider sales routine, no buying (Insider Activity)

<details><summary><b>News</b> — score +0.30</summary>

- [NVIDIA Corporation (NVDA) Stock Price, News, Quote & History](https://ca.finance.yahoo.com/quote/NVDA/)  
  <sub>Yahoo! Finance Canada, 7 hours ago</sub>  
  526,711.43% · Previous Close 237.47 · Open 234.93 · Bid 230.35 x 200 · Ask 230.55 x 400 · Day's Range 229.85 - 237.07 · 52 Week Range 164.27 - 243.37 · Volume...
- [Fund Update: 285,209 NVIDIA (NVDA) shares added to Border to Coast Pensions Partnership Ltd portfolio](https://www.quiverquant.com/news/Fund+Update%3A+285%2C209+NVIDIA+%28NVDA%29+shares+added+to+Border+to+Coast+Pensions+Partnership+Ltd+portfolio)  
  <sub>Quiver Quantitative, 4 hours ago</sub>  
  Border to Coast Pensions Partnership Ltd has added 285209 shares of $NVDA to their portfolio, per a.
- [Nvidia-Backed Firmus Cancels Mega IPO Over Market Volatility](https://www.tikr.com/blog/nvidia-backed-firmus-cancels-ipo-market-volatility?)  
  <sub>TIKR.com, 2 hours ago</sub>  
  Nvidia-backed Firmus pulled its $5B IPO over market volatility. Here's what it means for Nvidia stock and its AI data center growth.
- [NVIDIA Corporation (NVDA.NE) Stock Price, News, Quote & History](https://ca.finance.yahoo.com/quote/NVDA.NE/)  
  <sub>Yahoo! Finance Canada, 5 hours ago</sub>  
  NVIDIA Corporation (NVDA.NE) · Previous Close 52.89 · Open 52.14 · Bid 51.29 x -- · Ask -- · Day's Range 51.20 - 52.72 · 52 Week Range 17.88 - 52.72 · Volume...
- [Why NVDA, AMD, CRWD Stocks Surged To 52-Week Highs Today](https://stocktwits.com/news-articles/markets/equity/why-nvda-amd-crwd-stocks-surged-to-52-week-highs-today/cZDHyMrRBlM)  
  <sub>Stocktwits, 6 hours ago</sub>  
  NVDA stock jumped to an all-time high, closing 0.14% higher amid a broad run-up in chip stocks and SpaceX's intentions to buy its chips.
- [Nvidia: Caught Between Cyclical Downside Risk And AI Bubble](https://seekingalpha.com/article/4952948-nvidia-caught-between-cyclical-downside-risk-and-ai-bubble-reiterate-sell)  
  <sub>Seeking Alpha, 10 hours ago</sub>  
  NVIDIA stock still rated Sell: overvaluation, AI demand risks, slowing growth, and rising competition could trigger major downside. See more on NVDA stock.
- [An Nvidia Director Sold $947 Million of Stock Last Quarter, More Than Any Other U.S. Insider](https://247wallst.com/investing/2026/10/09/an-nvidia-director-sold-947-million-of-stock-last-quarter-more-than-any-other-u-s-insider/)  
  <sub>24/7 Wall St., 2 hours ago</sub>  
  A longtime Nvidia director quietly converted a massive block of stock into cash just weeks before the company hit an all-time high, raising a question...
- [Nvidia Stock Drops, but a Big Options Trade Bet Suggests It Could Go Higher](https://www.barrons.com/articles/nvidia-stock-price-options-trade-0e21d4ec)  
  <sub>Barron's, 21 hours ago</sub>  
  Nvidia stock has wavered since breaking through to a record high earlier this week. One massive options buyer is confident of further gains.
- [Trader Nets 159% Profit on NVDA Weekly Puts as Shares Dip to $23](https://www.gurufocus.com/news/9117151/trader-nets-159-profit-on-nvda-weekly-puts-as-shares-dip-to-23048)  
  <sub>GuruFocus, 2 hours ago</sub>  
  On October 09, 2026, a trader capitalized on a sharp intraday decline in NVIDIA Corp (NVDA) shares by purchasing 1630 weekly put options at $2.07 each near...
- [$NVIDIA (NVDA.US)$](https://www.moomoo.com/community/feed/nvidia-nvda-us-117411071852950)  
  <sub>Moomoo, 2 hours ago</sub>  
  Disclaimer: Community is offered by Moomoo Technologies Inc. and is for educational purposes only.Read more. 739 Views. Report. Comments.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.30</summary>

_Not available today._

</details>

<details><summary><b>Price and chart</b> — score +0.20</summary>

```text
Last close 230.75 (bar of 2026-10-09), from 502 daily bars
Trend: vs 20d SMA 226.81 (+1.7%), 50d 222.11 (+3.9%), 200d 202.16 (+14.1%); 50d above 200d
Momentum: RSI(14) 54.8 | MACD 4.067 vs signal 3.846 (histogram 0.221)
Returns: 1d +0.1% | 5d -1.4% | 1m +5.7% | 3m +13.4%
52-week range: 165.17 - 239.24 (now 88.5% of the way up)
Volatility: ATR(14) 5.59 (2.4% of price) | annualised 20d 25.0%
Volume: 0.22x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.80</summary>

```text
Sector: Technology / Semiconductors | market cap 5.57T
Valuation: trailing P/E 29.17 | forward P/E 14.50 | P/B 24.33 | PEG 0.48
Profitability: profit margin 63.7% | operating margin 66.2% | ROE 117.2%
Growth (YoY): revenue +105.9% | earnings +127.8%
Balance sheet: debt/equity 17.0% | free cash flow 41.81B
Risk: beta 2.22 | short interest 1.3% of float
Next earnings: 2026-11-17
```

</details>

<details><summary><b>What this fund holds</b> — score +0.80</summary>

_Not available today._

</details>

<details><summary><b>Does this company beat its own forecasts</b> — score +0.80</summary>

```text
Earnings record, last 4 quarters: 3 beats, 1 in line
  2026-09-30 beat by 4% | 2026-06-30 beat by 4% | 2026-03-31 beat by 4% | 2025-12-31 in line
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

<details><summary><b>What analysts and big funds say</b> — score +0.20</summary>

```text
Consensus: strong_buy (mean 1.30 on a 1=strong buy to 5=strong sell scale, 59 analysts)
Ratings: 10 strong buy, 48 buy, 2 hold, 1 sell, 0 strong sell
Price target: mean 328.72 (+42.5% vs last close), range 180.00 - 515.00
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

<details><summary><b>What analysts say about what this fund holds</b> — score +0.20</summary>

_Not available today._

</details>

<details><summary><b>Buying and selling by company insiders</b> — score +0.00</summary>

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

<details><summary><b>Who is positioned how</b> — score +0.00</summary>

_Not available today._

</details>

<details><summary><b>Money going into and out of this fund</b> — score +0.00</summary>

_Not available today._

</details>

### Royal Bank of Canada (RY) · Company — BULLISH, confidence 0.65

**Result:** REJECTED · no room under the sleeve budget limit

**In the model's own words:**

> Positive news (record profit, high ROE, institutional buying) and strong insider purchase activity outweigh mixed technicals and modest analyst view. Fundamentals remain solid, and earnings record is neutral‑positive. Overall, the balance points to a bullish outlook with moderate conviction.

**Main reasons it gave:**
- Record profit and 18% ROE reported (Motley Fool article)
- Cluster of insider purchases: 200k shares on four consecutive days
- RSI 29.7 indicating oversold condition despite thin volume
- Trailing P/E 16.68 and profit margin 33.9% suggest solid fundamentals

<details><summary><b>News</b> — score +0.45</summary>

- [Royal Bank of Canada (RY) stock price, news, quote and history](https://uk.finance.yahoo.com/quote/RY/)  
  <sub>Yahoo Finance UK, 19 hours ago</sub>
- [Mn Services Vermogensbeheer B.V. Buys 6,500 Shares of Royal Bank Of Canada $RY](https://www.marketbeat.com/instant-alerts/filing-mn-services-vermogensbeheer-bv-buys-6500-shares-of-royal-bank-of-canada-ry-2026-10-09/)  
  <sub>MarketBeat, 6 hours ago</sub>  
  Mn Services Vermogensbeheer B.V. increased its position in Royal Bank Of Canada (NYSE:RY - Free Report) (TSE:RY) by 1.6% during the 3rd quarter,...
- [OSFI’s Risk Outlook Could Test Canadian Banks: Royal Bank Looks Prepared](https://ca.finance.yahoo.com/news/osfi-risk-outlook-could-test-133000500.html)  
  <sub>Yahoo! Finance Canada, 1 hour ago</sub>
- [RBC announces CAD 1.50 billion notes: Royal Bank of Canada stock has 4.90 percent upside](https://www.ad-hoc-news.de/boerse/news/corporate-news/rbc-announces-cad-1-50-billion-notes-royal-bank-of-canada-stock-has-4-90/70279020)  
  <sub>AD HOC NEWS, 2 hours ago</sub>
- [Royal Bank Stock: Why I’d Buy It Now for the Next 5 Years](https://www.fool.ca/2026/10/08/royal-bank-stock-why-id-buy-it-now-for-the-next-5-years/)  
  <sub>The Motley Fool Canada, 15 hours ago</sub>  
  Royal Bank just posted record profit and an 18% ROE. Here's why RBC stock looks like a smart buy for the next five years.
- [RY Apr 2027 135.000 call (RY270416C00135000) Interactive Stock Chart](https://ca.finance.yahoo.com/quote/RY270416C00135000/chart/)  
  <sub>Yahoo! Finance Canada, 3 hours ago</sub>
- [Royal Bank of Canada stock pre-market at EUR 169.39: minus 0.35 percent](https://www.ad-hoc-news.de/boerse/news/vorboerse/royal-bank-of-canada-stock-pre-market-at-eur-169-39-minus-0-35-percent/70272421)  
  <sub>AD HOC NEWS, 9 hours ago</sub>
- [Why Is RBC Still Central to TSX Financial Stocks?](https://kalkinemedia.com/ca/stocks/financial/why-is-rbc-still-central-to-tsx-financial-stocks)  
  <sub>Kalkine Media, 21 hours ago</sub>  
  RBC continues operating across banking, wealth management and capital markets as changing financial conditions reshape Canada's banking sector.
- [RY Apr 2027 200.000 call (RY270416C00200000) stock price, news, quote and history](https://uk.finance.yahoo.com/quote/RY270416C00200000/)  
  <sub>Yahoo Finance UK, 13 hours ago</sub>
- [Royal Bank of Canada stock trades at EUR 170.12 with USD 264.9 billion market cap](https://www.ad-hoc-news.de/boerse/news/corporate-news/royal-bank-of-canada-stock-trades-at-eur-170-12-with-usd-264-9-billion-market-cap/70269922)  
  <sub>AD HOC NEWS, 20 hours ago</sub>

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.45</summary>

_Not available today._

</details>

<details><summary><b>Price and chart</b> — score -0.35</summary>

```text
Last close 190.82 (bar of 2026-10-09), from 502 daily bars
Trend: vs 20d SMA 199.07 (-4.1%), 50d 205.00 (-6.9%), 200d 187.02 (+2.0%); 50d above 200d
Momentum: RSI(14) 29.7 | MACD -3.855 vs signal -3.030 (histogram -0.825)
Returns: 1d +0.1% | 5d -2.5% | 1m -7.4% | 3m -9.4%
52-week range: 143.64 - 217.87 (now 63.6% of the way up)
Volatility: ATR(14) 3.02 (1.6% of price) | annualised 20d 16.2%
Volume: 0.10x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.40</summary>

```text
Sector: Financial Services / Banks - Diversified | market cap 264.18B
Valuation: trailing P/E 16.68 | forward P/E 15.22 | P/B 2.80 | PEG 2.26
Profitability: profit margin 33.9% | operating margin 46.4% | ROE 16.2%
Growth (YoY): revenue +8.9% | earnings +12.8%
Balance sheet: debt/equity n/a | free cash flow n/a
Risk: beta 0.91 | short interest n/a of float
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

<details><summary><b>What analysts and big funds say</b> — score +0.20</summary>

```text
Consensus: buy (mean 2.13 on a 1=strong buy to 5=strong sell scale, 3 analysts)
Ratings: 4 strong buy, 5 buy, 5 hold, 0 sell, 1 strong sell
Price target: mean 207.18 (+8.6% vs last close), range 182.40 - 224.44
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

<details><summary><b>What analysts say about what this fund holds</b> — score +0.20</summary>

_Not available today._

</details>

<details><summary><b>Buying and selling by company insiders</b> — score +0.70</summary>

```text
Last 180 days: bought 0 shares in 0 transaction(s) | sold n/a shares in 0
Net: +0 shares | insiders hold 387,640 shares
Distinct insiders: 1 buying, 0 selling
Open-market purchases — insiders spending their own money:
  - 2026-09-29 Royal Bank of Canada (Issuer): 200,000 shares, 39.94M
  - 2026-09-28 Royal Bank of Canada (Issuer): 200,000 shares, 40.29M
  - 2026-09-25 Royal Bank of Canada (Issuer): 200,000 shares, 40.24M
  - 2026-09-24 Royal Bank of Canada (Issuer): 200,000 shares, 39.86M
(101 grant/option/gift transaction(s) excluded — compensation, not a view on the price)
```

</details>

<details><summary><b>Who is positioned how</b> — score +0.70</summary>

_Not available today._

</details>

<details><summary><b>Money going into and out of this fund</b> — score +0.70</summary>

_Not available today._

</details>

### HDFC Bank (HDB) · Company — NEUTRAL, confidence 0.60

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> The overall picture is mixed but leans bearish: negative legal news and a new 52‑week low, technicals showing price below key moving averages, low volume and negative momentum, and an elevated P/B ratio suggest downside pressure. Analyst consensus remains bullish with a high price target, but recent downgrades temper that optimism. No insider activity and a modest earnings record provide little additional support. The net scores point to a slight bearish tilt, leading to a neutral‑to‑sell stance with moderate conviction.

**Main reasons it gave:**
- Class action lawsuit reminder (Shareholder Alert) indicates legal risk
- Stock set new 52‑week low, price below 20‑day, 50‑day, and 200‑day SMAs
- Technical indicators: RSI 43.5, negative MACD, volume at 0.08× 20‑day average
- High valuation: P/B 9.01 suggests overvaluation for a bank
- Analyst consensus still buy but recent downgrades (JP Morgan, Bernstein, Nomura) signal weakening sentiment

<details><summary><b>News</b> — score -0.40</summary>

- [HDFC Bank (NYSE:HDB) Sets New 52-Week Low - Time to Sell?](https://www.marketbeat.com/instant-alerts/price-hdfc-bank-nyse-hdb-sets-new-52-week-low-time-to-sell-2026-10-08/)  
  <sub>MarketBeat, 22 hours ago</sub>  
  HDFC Bank Limited (NYSE:HDB - Get Free Report)'s stock price reached a new 52-week low on Thursday. The stock traded as low as $21.74 and last traded at...
- [HDFC Bank Shareholder Alert: ClaimsFiler Reminds Investors With Losses In Excess Of $100,000 Of Lead Plaintiff Deadline In Class Action Lawsuit Against HDFC Bank Limited - HDB](https://www.streetinsider.com/Globe+Newswire/HDFC+Bank+Shareholder+Alert%3A+ClaimsFiler+Reminds+Investors+With+Losses+In+Excess+Of+%24100%2C000+Of+Lead+Plaintiff+Deadline+In+Class+Action+Lawsuit+Against+HDFC+Bank+Limited+-+HDB/27167658.html)  
  <sub>StreetInsider, 13 hours ago</sub>  
  NEW ORLEANS, Oct. 08, 2026 (GLOBE NEWSWIRE) -- ClaimsFiler, a FREE shareholder information service, reminds investors that they have until October 13,...
- [HDFC Bank stock trades at EUR 20.00, market value USD 112.9 billion](https://www.ad-hoc-news.de/boerse/news/corporate-news/hdfc-bank-stock-trades-at-eur-20-00-market-value-usd-112-9-billion/70279000)  
  <sub>AD HOC NEWS, 2 hours ago</sub>  
  HDB, US40415F1012. HDFC Bank stock trades at EUR 20.00, market value USD 112.9 billion. Published on 10/09/2026 at 15:04 | Editorial responsibility: Rafael...
- [VN-Index loses 3.88 points, PNJ and NVL reverse course and surge.](https://www.vietnam.vn/en/vn-index-mat-3-88-diem-pnj-va-nvl-nguoc-dong-but-pha)  
  <sub>Vietnam.vn, 3 hours ago</sub>  
  The VN-Index continued to decline as selling pressure increased on some large-cap stocks. However, capital still flowed into individual opportunities,...
- [Poonawalla Fincorp Q2 Results: Profit skyrockets 407% YoY to Rs 375 crore, NII rises 81%](https://m.economictimes.com/markets/stocks/earnings/poonawalla-fincorp-q2-results-profit-skyrockets-407-yoy-to-rs-375-crore-nii-rises-81/articleshow/134835689.cms)  
  <sub>The Economic Times, 58 minutes ago</sub>  
  Poonawalla Fincorp reported a 407% year-on-year surge in Q2FY27 profit to Rs 375 crore, while net interest income rose 81%. Operating profit more than...
- [Stock market on October 9th: Many stocks strongly attract cash flow](https://news.laodong.vn/kinh-doanh/chung-khoan-ngay-910-nhieu-co-phieu-hut-manh-dong-tien-1780373.ldo)  
  <sub>Laodong.vn, 5 hours ago</sub>  
  The stock market had a less positive trading session, but some stock codes unexpectedly had very noteworthy developments.
- [Following PNJ, Novaland shares also hit the ceiling price.](https://www.vietnam.vn/en/sau-pnj-den-luot-co-phieu-novaland-tang-tran)  
  <sub>Vietnam.vn, 5 hours ago</sub>  
  PNJ and Novaland became the focus of the stock market trading session on October 9th as they both rose to their maximum allowed limit, contrary to the...
- [HDFC Bank stock pre-market: EUR 19.75, plus 0.77 percent](https://www.ad-hoc-news.de/boerse/news/vorboerse/hdfc-bank-stock-pre-market-eur-19-75-plus-0-77-percent/70272429)  
  <sub>AD HOC NEWS, 9 hours ago</sub>  
  HDB, US40415F1012. HDFC Bank stock pre-market: EUR 19.75, plus 0.77 percent. Published on 10/09/2026 at 07:51 | Editorial responsibility: Rafael Müller,...
- [Stock market on October 9-10: PNJ and SHB regain their momentum, foreign investors net sell over 9,000 billion VND.](https://www.vietnam.vn/en/chung-khoan-9-10-pnj-shb-lay-lai-phong-do-khoi-ngoai-ban-rong-hon-9-000-ty-dong)  
  <sub>Vietnam.vn, 3 hours ago</sub>  
  Today's stock market saw foreign investors sell off over 9272 billion VND. PNJ and SHB were two stocks with notable highlights.
- [‘Happy spouse, happy house’: Singaporeans share what keeps their marriages strong](https://theindependent.sg/happy-spouse-happy-house-singaporeans-share-what-keeps-their-marriages-strong)  
  <sub>The Independent Singapore, 18 hours ago</sub>  
  What keeps couples happy after years of marriage? Singaporeans share the lessons that have worked for them.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score -0.40</summary>

_Not available today._

</details>

<details><summary><b>Price and chart</b> — score -0.50</summary>

```text
Last close 22.11 (bar of 2026-10-09), from 502 daily bars
Trend: vs 20d SMA 22.64 (-2.3%), 50d 22.99 (-3.8%), 200d 26.73 (-17.3%); 50d below 200d
Momentum: RSI(14) 43.5 | MACD -0.261 vs signal -0.214 (histogram -0.047)
Returns: 1d +0.5% | 5d -1.0% | 1m +1.2% | 3m -16.3%
52-week range: 21.84 - 37.18 (now 1.8% of the way up)
Volatility: ATR(14) 0.53 (2.4% of price) | annualised 20d 26.7%
Volume: 0.08x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score -0.20</summary>

```text
Sector: Financial Services / Banks - Regional | market cap 113.63B
Valuation: trailing P/E 14.26 | forward P/E 15.89 | P/B 9.01 | PEG n/a
Profitability: profit margin 26.8% | operating margin 33.3% | ROE 13.8%
Growth (YoY): revenue +16.6% | earnings +18.1%
Balance sheet: debt/equity n/a | free cash flow n/a
Risk: beta 0.41 | short interest 0.7% of float
Next earnings: 2026-10-17
```

</details>

<details><summary><b>What this fund holds</b> — score -0.20</summary>

_Not available today._

</details>

<details><summary><b>Does this company beat its own forecasts</b> — score -0.20</summary>

```text
Earnings record, last 4 quarters: 2 beats, 2 in line
  2026-06-30 in line | 2026-03-31 in line | 2025-12-31 beat by 61% | 2025-09-30 beat by 10%
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
Consensus: buy (mean 1.75 on a 1=strong buy to 5=strong sell scale, 4 analysts)
Ratings: 1 strong buy, 2 buy, 1 hold, 0 sell, 0 strong sell
Price target: mean 30.52 (+38.1% vs last close), range 26.10 - 35.00
Recent rating changes:
  - 2024-07-22 JP Morgan: down, Overweight -> Neutral
  - 2019-09-09 Bernstein: down, Outperform -> Market Perform
  - 2019-06-11 Nomura: down, Buy -> Neutral
  - 2017-03-21 Morgan Stanley: down, Overweight -> Equal-Weight
  - 2016-09-14 Goldman Sachs: main, ? -> Buy
  - 2015-03-11 Societe Generale: init, ? -> Buy
Institutional ownership: 15.8%
Largest holders: Morgan Stanley (1.0%), Royal Bank of Canada (0.8%), Schroder Investment Management Group (0.4%), JPMORGAN CHASE & CO (0.4%), Bank of America Corporation (0.3%)
```

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score +0.30</summary>

_Not available today._

</details>

<details><summary><b>Buying and selling by company insiders</b> — score +0.00</summary>

```text
Last 180 days: bought 0 shares in 0 transaction(s) | sold n/a shares in 0
Net: +0 shares | insiders hold 7,954,480 shares
Distinct insiders: 0 buying, 0 selling
```

</details>

<details><summary><b>Who is positioned how</b> — score +0.00</summary>

_Not available today._

</details>

<details><summary><b>Money going into and out of this fund</b> — score +0.00</summary>

_Not available today._

</details>

### ASML (ASML) · Company — BULLISH, confidence 0.55

**Result:** ACCEPTED · 2 shares · submitted buy 2 ASML @ ~1794.51, stop 1690.71

**In the model's own words:**

> Positive news from BofA (target raise and revenue guidance), strong fundamentals, bullish analyst consensus, uptrend in technicals, and neutral insider activity combine to suggest a modest upside over the next few days.

**Main reasons it gave:**
- BofA raised price target to EUR 2,557 and provided Q3 2026 revenue guidance of EUR 11‑12B
- Strong fundamentals: profit margin 30.1%, operating margin 37.1%, ROE 53.9%, debt/equity 9.1%
- Analyst consensus strong buy with mean price target +17.7% above current price
- Uptrend above 20‑day, 50‑day, 200‑day SMAs; RSI 53.4; MACD positive
- No insider buying activity (neutral signal)

<details><summary><b>News</b> — score +0.30</summary>

- [Advanced Micro Devices vs. ASML: Which Semiconductor Stock Is a Better Buy in 2026?](https://www.fool.com/coverage/better-buy/2026/10/08/advanced-micro-devices-vs-asml-which-semiconductor-stock-is-a-better-buy-in-2026/)  
  <sub>The Motley Fool, 14 hours ago</sub>  
  Both are essential to the AI chip build-out, but they carry very different risk profiles depending on where they sit in the supply chain.
- [The Growth in Micron Stock Is Being Driven by the ‘Largest Companies in the Land’: Why Wall Street Can’t Get Enough of MU](https://www.barchart.com/story/news/5309660/the-growth-in-micron-stock-is-being-driven-by-the-largest-companies-in-the-land-why-wall-street-cant-get-enough-of-mu)  
  <sub>Barchart.com, 3 hours ago</sub>  
  The associated trade with artificial intelligence (AI), or the “picks and shovels” trade, has created enormous wealth for investors.
- [ASML Oct 2026 1905.000 call (ASML261009C01905000) Stock Price, News, Quote & History](https://ca.finance.yahoo.com/quote/ASML261009C01905000/)  
  <sub>Yahoo! Finance Canada, 11 hours ago</sub>  
  Find the latest ASML Oct 2026 1905.000 call (ASML261009C01905000) stock quote, history, news and other vital information to help you with your stock trading...
- [Why ASML Holding (ENXTAM:ASML) Is Back In The Spotlight](https://simplywall.st/stocks/nl/semiconductors/ams-asml/asml-holding-shares/news/why-asml-holding-enxtamasml-is-back-in-the-spotlight)  
  <sub>Simply Wall Street, 4 hours ago</sub>  
  ASML Holding (ENXTAM:ASML) is back in focus after several major banks highlighted expectations for stronger quarterly results and a more upbeat outlook,...
- [SpaceX buys spectrum for wireless network, rattling stocks, ASML's Hyper NA leap a decade away, Nvidia, ARM, Qualcomm - Big Tech Report](http://www.proactiveinvestors.co.uk/a/f9e10ce1/spacex-buys-spectrum-for-wireless-network-rattling-stocks-asmls-hyper-na)  
  <sub>Proactive Investors, 1 hour ago</sub>  
  14:18: SpaceX, Reddit and ASML lead gainers. Top risers: SpaceX +3.2%, Reddit +3.1%, ASML +2.9%. Biggest fallers: Apple -2.5%, Netflix -1.5%, IBM -0.3%.
- [ASML Stocks Move Higher as Hyper NA Extends Its Chipmaking Moat](https://www.gurufocus.com/news/9115707/asml-stocks-move-higher-as-hyper-na-extends-its-chipmaking-moat)  
  <sub>GuruFocus, 23 hours ago</sub>  
  ASML Holding (ASML), the EUV-lithography leader, advanced about 1.3% to $1828.35 as of approximately 11:05 a.m. ET on October 8, as investors weighed a...
- [ASML Oct 2026 1910.000 call (ASML261009C01910000) interactive stock chart](https://uk.finance.yahoo.com/quote/ASML261009C01910000/chart/)  
  <sub>Yahoo Finance UK, 9 hours ago</sub>  
  Interactive chart for ASML Oct 2026 1910.000 call (ASML261009C01910000) – analyse all of the data with a huge range of indicators.
- [BofA raises target for ASML Holding stock from EUR 2,452 to EUR 2,557](https://www.ad-hoc-news.de/boerse/news/corporate-news/bofa-raises-target-for-asml-holding-stock-from-eur-2-452-to-eur-2-557/70276772)  
  <sub>AD HOC NEWS, 4 hours ago</sub>  
  ASML set third-quarter 2026 revenue at EUR 11.0-12.0 billion. ASML Holding stock costs EUR 1624.10 on October 9, 2026 versus EUR 1584.00.
- [AMD, TER Stocks Jump After Goldman Sachs Lifts Price Targets](https://stocktwits.com/news-articles/markets/equity/amd-ter-stocks-jump-after-goldman-sachs-lifts-price-targets/cZm18P6R7lx)  
  <sub>Stocktwits, 22 hours ago</sub>  
  Shares of Teradyne, Inc. (TER) and Advanced Micro Devices Inc. (AMD) jumped on Monday after Goldman Sachs raised its price targets on both semiconductor...
- [AVGO Stock Alert: What to Know About Broadcom's $50 Billion Financing Deal for OpenAI Chips](https://www.barchart.com/story/news/5126099/avgo-stock-alert-what-to-know-about-broadcom-s-50-billion-financing-deal-for-openai-chips)  
  <sub>Barchart.com, 18 hours ago</sub>  
  Broadcom stock sinks on reports of a major financing package linked to its OpenAI partnership. Here's why AVGO shares are worth buying on the dip today.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.30</summary>

_Not available today._

</details>

<details><summary><b>Price and chart</b> — score +0.20</summary>

```text
Last close 1,788.68 (bar of 2026-10-09), from 502 daily bars
Trend: vs 20d SMA 1,744.97 (+2.5%), 50d 1,738.78 (+2.9%), 200d 1,561.86 (+14.5%); 50d above 200d
Momentum: RSI(14) 53.4 | MACD 27.138 vs signal 23.938 (histogram 3.200)
Returns: 1d +1.1% | 5d -4.2% | 1m +6.0% | 3m +3.6%
52-week range: 936.19 - 1,989.44 (now 80.9% of the way up)
Volatility: ATR(14) 51.83 (2.9% of price) | annualised 20d 38.7%
Volume: 0.32x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.40</summary>

```text
Sector: Technology / Semiconductor Equipment & Materials | market cap 687.03B
Valuation: trailing P/E 58.06 | forward P/E 30.76 | P/B 1,554.07 | PEG 1.58
Profitability: profit margin 30.1% | operating margin 37.1% | ROE 53.9%
Growth (YoY): revenue +21.3% | earnings +28.5%
Balance sheet: debt/equity 9.1% | free cash flow 8.44B
Risk: beta 1.30 | short interest 0.4% of float
Next earnings: 2026-10-14
```

</details>

<details><summary><b>What this fund holds</b> — score +0.40</summary>

_Not available today._

</details>

<details><summary><b>Does this company beat its own forecasts</b> — score +0.40</summary>

```text
Earnings record, last 4 quarters: 2 beats, 1 in line, 1 missed
  2026-06-30 beat by 9% | 2026-03-31 beat by 7% | 2025-12-31 missed by 5% | 2025-09-30 in line
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
Consensus: strong_buy (mean 1.40 on a 1=strong buy to 5=strong sell scale, 16 analysts)
Ratings: 7 strong buy, 31 buy, 3 hold, 1 sell, 0 strong sell
Price target: mean 2,105.35 (+17.7% vs last close), range 866.63 - 2,913.04
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

<details><summary><b>What analysts say about what this fund holds</b> — score +0.30</summary>

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

### Procter & Gamble (PG) · Company — BULLISH, confidence 0.45

**Result:** REJECTED · no room under the sleeve budget limit

**In the model's own words:** no explanation. It wrote only “BUY”, so the main reasons below are all it gave.

**Main reasons it gave:**
- Insider net purchase of 91,724 shares (+4.5% of holdings) over past 180 days
- Price above 20‑day, 50‑day, and 200‑day SMAs with RSI 61.8 and MACD positive
- Analyst consensus buy (mean 2.12) with mean price target 160.78 (+6.4% above current price)
- High ROE (30.3%) and strong free cash flow (13.28B) despite low revenue growth (+1.5% YoY)

<details><summary><b>News</b> — score +0.00</summary>

- [Behavioral Patterns of PG and Institutional Flows](https://news.stocktradersdaily.com/news_release/141/Behavioral_Patterns_of_PG_and_Institutional_Flows_100926093401_1791552841.html)  
  <sub>Stock Traders Daily, 5 hours ago</sub>  
  Key findings for Procter & Gamble Company (the) (NYSE: PG). Near-Term Strong Sentiment Could Influence Neutral Mid and Long-Term Outlook...
- [What Is Procter & Gamble Stock’s Biggest Opportunity?](https://www.trefis.com/stock/pg/articles/617953/what-is-procter-gamble-stocks-biggest-opportunity/2026-10-08)  
  <sub>Trefis, 19 hours ago</sub>  
  Procter & Gamble (PG) stock has returned 1.2% over the past twelve months, compared to 17.1% for the S&P 500. Revenue grew a modest 1.5% in the latest...
- [4 Dividend Stocks Boomers Can Safely Buy Now and Hold Forever](https://247wallst.com/investing/2026/10/09/4-dividend-stocks-boomers-can-buy-now-and-hold-forever/)  
  <sub>24/7 Wall St., 2 hours ago</sub>  
  Four Dividend Kings sit inside millions of retirement portfolios. One is spending every dollar of free cash flow just to keep its streak alive.
- [Procter & Gamble (NYSE:PG) Shares Climb 1.9% - Should You Buy?](https://www.marketbeat.com/instant-alerts/price-procter-gamble-nyse-pg-shares-climb-19-should-you-buy-2026-10-08/)  
  <sub>MarketBeat, 17 hours ago</sub>  
  Procter & Gamble (NYSE:PG) Stock Jumps 1.9% - Should You Buy?
- [PG Sep 2027 125.000 put (PG270917P00125000) Interactive Stock Chart](https://ca.finance.yahoo.com/quote/PG270917P00125000/chart/)  
  <sub>Yahoo! Finance Canada, 15 hours ago</sub>  
  Interactive Chart for PG Sep 2027 125.000 put (PG270917P00125000), analyze all the data with a huge range of indicators.
- [Humana jumps 14.4% on Medicare Advantage ratings](https://grafa.com/en/news/united-states/humana-stock-jumps-medicare-advantage-ratings-2027)  
  <sub>grafa.com, 2 hours ago</sub>  
  Humana shares jumped 14.4% to $443 after 95% of members were shown in Medicare Advantage plans rated four stars or higher for 2027.
- [Why is Procter & Gamble (NYSE:PG) a go-to name as markets rotate toward steady payers?](https://kalkinemedia.com/us/stocks/dividend/why-is-procter-gamble-nysepg-a-go-to-name-as-markets-rotate-toward-steady-payers)  
  <sub>Kalkine Media, 1 hour ago</sub>  
  Procter & Gamble (NYSE:PG) drew attention as defensive dividend payers returned to favor; a look at the consumer group's distributions, brand portfolio and...
- [These dow jones stocks are moving in today's session](https://www.chartmill.com/news/KO/Chartmill-55946-These-dow-jones-stocks-are-moving-in-todays-session)  
  <sub>ChartMill, 22 hours ago</sub>  
  Curious about the dow jones stocks that are in motion on Thursday? Join us as we explore the top movers within the dow jones index during today's session.
- [WATCH: Kyle MacLachlan shares the real stories behind his biggest roles in new memoir Video | The View](https://abc.com/video/fa15624a-4a22-44d9-a14d-5c52f45a22ca/playlist/PL557769560)  
  <sub>ABC Network, 20 hours ago</sub>  
  The actor joins 'The View' to reflect on his favorite memories from his iconic roles and why he wrote 'Fictional Selves' for his son. TV-PG | 10.08.26 | 08:...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

_Not available today._

</details>

<details><summary><b>Price and chart</b> — score +0.20</summary>

```text
Last close 151.08 (bar of 2026-10-09), from 502 daily bars
Trend: vs 20d SMA 147.13 (+2.7%), 50d 145.91 (+3.5%), 200d 147.74 (+2.3%); 50d below 200d
Momentum: RSI(14) 61.8 | MACD 0.848 vs signal 0.403 (histogram 0.445)
Returns: 1d +0.3% | 5d +4.3% | 1m +5.7% | 3m +1.8%
52-week range: 138.04 - 167.20 (now 44.7% of the way up)
Volatility: ATR(14) 2.42 (1.6% of price) | annualised 20d 16.7%
Volume: 0.12x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.00</summary>

```text
Sector: Consumer Defensive / Household & Personal Products | market cap 351.18B
Valuation: trailing P/E 22.82 | forward P/E 20.43 | P/B 6.58 | PEG 3.79
Profitability: profit margin 18.4% | operating margin 22.1% | ROE 30.3%
Growth (YoY): revenue +1.5% | earnings -15.5%
Balance sheet: debt/equity 64.5% | free cash flow 13.28B
Risk: beta 0.38 | short interest 1.0% of float
Next earnings: 2026-10-22
```

</details>

<details><summary><b>What this fund holds</b> — score +0.00</summary>

_Not available today._

</details>

<details><summary><b>Does this company beat its own forecasts</b> — score +0.00</summary>

```text
Earnings record, last 4 quarters: 4 in line
  2026-06-30 in line | 2026-03-31 in line | 2025-12-31 in line | 2025-09-30 in line
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

<details><summary><b>What analysts and big funds say</b> — score +0.20</summary>

```text
Consensus: buy (mean 2.12 on a 1=strong buy to 5=strong sell scale, 23 analysts)
Ratings: 6 strong buy, 8 buy, 11 hold, 0 sell, 0 strong sell
Price target: mean 160.78 (+6.4% vs last close), range 143.00 - 186.00
Recent rating changes:
  - 2026-10-06 Evercore ISI Group: up, In-Line -> Outperform
  - 2026-10-06 RBC Capital: main, Outperform -> Outperform
  - 2026-09-30 TD Cowen: reit, Hold -> Hold
  - 2026-08-07 Argus Research: down, Buy -> Hold
  - 2026-07-30 HSBC: down, Buy -> Hold
  - 2026-07-30 Citigroup: main, Buy -> Buy
Institutional ownership: 71.8%
Largest holders: Blackrock Inc. (8.2%), Vanguard Capital Management LLC (6.6%), State Street Corporation (4.4%), Geode Capital Management, LLC (2.9%), Vanguard Portfolio Management LLC (2.7%)
```

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score +0.20</summary>

_Not available today._

</details>

<details><summary><b>Buying and selling by company insiders</b> — score +0.50</summary>

```text
Last 180 days: bought 140,475 shares in 31 transaction(s) | sold 48,751 shares in 16
Net: +91,724 shares (+4.5% of insider holdings) | insiders hold 2,138,478 shares
Distinct insiders: 0 buying, 10 selling
Sales — weak evidence on their own; often scheduled 10b5-1 plans, tax on vesting, or diversification:
  - 2026-10-05 WHALEY SUSAN STREET (Officer): 2,369 shares, 344.31K
  - 2026-10-05 GAMA PAUL (Officer): 2,225 shares, 323.38K
  - 2026-10-05 SCHULTEN ANDRE (Chief Financial Officer): 3,914 shares, 568.86K
  - 2026-08-24 JANZARUK MATTHEW W. (Officer): 359 shares, 52.14K
(29 grant/option/gift transaction(s) excluded — compensation, not a view on the price)
```

</details>

<details><summary><b>Who is positioned how</b> — score +0.50</summary>

_Not available today._

</details>

<details><summary><b>Money going into and out of this fund</b> — score +0.50</summary>

_Not available today._

</details>

### Caterpillar (CAT) · Company — NEUTRAL, confidence 0.35

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Mixed signals across dimensions; bullish analyst view and earnings record offset bearish technicals and high valuation/leverage, leading to a neutral stance with modest conviction.

**Main reasons it gave:**
- Mixed news: undervaluation view (Simply Wall St) vs regulatory pressure and weak sentiment (Yahoo Finance, Stock Traders Daily)
- Bearish technicals: price below 20d/50d SMA, RSI 43.7, negative MACD, low volume (0.15x avg)
- Analyst consensus buy with +21.7% price target (mean $970.80) – bullish outlook
- Four consecutive earnings beats – strong earnings record
- High leverage (debt/equity 232.8%) and high valuation (trailing P/E 34.33) – temper bullishness

<details><summary><b>News</b> — score +0.10</summary>

- [Caterpillar (CAT) Stock Looks Undervalued On Future Cash Flow](https://simplywall.st/stocks/us/capital-goods/nyse-cat/caterpillar/news/caterpillar-cat-stock-looks-undervalued-on-future-cash-flow)  
  <sub>Simply Wall Street, 6 hours ago</sub>  
  Caterpillar has turned a long run in its share price into a talking point for valuation, and the issue now is whether the current US$796.18 level is still...
- [Caterpillar (CAT) Faces Regulatory And Rate Pressure, Is The Pullback A Bargain?](https://finance.yahoo.com/markets/stocks/articles/caterpillar-cat-faces-regulatory-rate-131016970.html)  
  <sub>Yahoo Finance, 2 hours ago</sub>  
  Caterpillar (CAT) has been pulled in two directions. Regulatory scrutiny of agricultural equipment practices and a jump in long term Treasury yields have...
- [Caterpillar Is the Market in a Single Stock. That’s Not a Bad Thing.](https://www.barrons.com/articles/caterpillar-market-a-single-stock-b6be0415)  
  <sub>Barron's, 6 hours ago</sub>  
  Caterpillar is viewed by J.P. Morgan as “the biggest winner of an extended U.S. construction cycle,” though it's had a rough week.
- [CRWV Stock Rallies 13% After-Hours — AI Compute Demand Has Pushed CoreWeave Revenue To More Than Double](https://stocktwits.com/news-articles/markets/equity/ai-compute-demand-has-pushed-core-weave-revenue-to-more-than-double/cZoNQHURJXn)  
  <sub>Stocktwits, 5 hours ago</sub>  
  CoreWeave beat second-quarter top- and bottom-line expectations as soaring artificial intelligence computing demand pushed quarterly revenue up 112% to...
- [How (CAT) Movements Inform Risk Allocation Models](https://news.stocktradersdaily.com/news_release/15/How_CAT_Movements_Inform_Risk_Allocation_Models_100926073201_1791545521.html)  
  <sub>Stock Traders Daily, 7 hours ago</sub>  
  Key findings for Caterpillar Inc. (NYSE: CAT). Weak Near-Term Sentiment Could Precede Shifts in Mid and Long-Term Outlook; No clear price positioning signal...
- [Will Caterpillar's Strong Volume Growth Keep Driving Sales Up in 2026?](https://finance.yahoo.com/markets/stocks/articles/caterpillars-strong-volume-growth-keep-094600810.html)  
  <sub>Yahoo Finance, 5 hours ago</sub>  
  CAT's volume growth adds $5.4 billion to first-half 2026 revenues, prompting a higher full-year outlook as all three major segments gain momentum.
- [Trump bought over $1 million in SpaceX debt days before unveiling space policy](https://www.washingtonpost.com/politics/2026/10/08/trump-invested-spacex-shortly-before-issuing-new-space-policy/)  
  <sub>The Washington Post, 10 hours ago</sub>  
  The purchase, revealed in his latest financial disclosure, involved a firm directly affected by his administration's actions — and led by presidential ally...
- [Exploring the top movers within the dow jones index during today's session.](https://www.chartmill.com/news/DIS/Chartmill-55959-Exploring-the-top-movers-within-the-dow-jones-index-during-todays-session)  
  <sub>ChartMill, 20 hours ago</sub>  
  Stay updated with the movement of dow jones stocks in today's session. Discover which dow jones stocks are making waves on Thursday.
- [Dell To Officially Join Tesla, Oracle, Caterpillar In Texas As Stock Eyes Best Year Since Returning To Public Markets](https://stocktwits.com/news-articles/markets/equity/dell-to-officially-join-tesla-oracle-caterpillar-in-texas-as-stock-eyes-best-year-since-returning-to-public-markets/cZ1cXbeR7g3)  
  <sub>Stocktwits, 5 hours ago</sub>  
  Tesla and SpaceX CEO Elon Musk gave his sign of support to the announcement posted by founder Michael Dell on X.
- [Red Cat Holdings, Inc. (RCAT) Stock Price, News, Quote & History](https://ca.finance.yahoo.com/quote/RCAT/)  
  <sub>Yahoo! Finance Canada, 18 hours ago</sub>  
  -100.00% · Previous Close 6.15 · Open 6.08 · Bid 4.37 x 200 · Ask 13.50 x 100 · Day's Range 5.83 - 6.14 · 52 Week Range 5.77 - 18.78 · Volume 6,421,071 · Avg.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.10</summary>

_Not available today._

</details>

<details><summary><b>Price and chart</b> — score -0.50</summary>

```text
Last close 797.43 (bar of 2026-10-09), from 502 daily bars
Trend: vs 20d SMA 813.47 (-2.0%), 50d 821.93 (-3.0%), 200d 801.31 (-0.5%); 50d above 200d
Momentum: RSI(14) 43.7 | MACD -0.471 vs signal 0.172 (histogram -0.643)
Returns: 1d +0.2% | 5d -5.7% | 1m -0.9% | 3m -14.4%
52-week range: 491.30 - 1,064.90 (now 53.4% of the way up)
Volatility: ATR(14) 26.13 (3.3% of price) | annualised 20d 33.6%
Volume: 0.15x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score -0.10</summary>

```text
Sector: Industrials / Farm & Heavy Construction Machinery | market cap 366.56B
Valuation: trailing P/E 34.33 | forward P/E 24.60 | P/B 18.90 | PEG 1.42
Profitability: profit margin 14.5% | operating margin 22.2% | ROE 57.0%
Growth (YoY): revenue +24.0% | earnings +68.2%
Balance sheet: debt/equity 232.8% | free cash flow 5.05B
Risk: beta 1.58 | short interest 2.0% of float
Next earnings: 2026-10-29
```

</details>

<details><summary><b>What this fund holds</b> — score -0.10</summary>

_Not available today._

</details>

<details><summary><b>Does this company beat its own forecasts</b> — score -0.10</summary>

```text
Earnings record, last 4 quarters: 4 beats
  2026-06-30 beat by 31% | 2026-03-31 beat by 19% | 2025-12-31 beat by 9% | 2025-09-30 beat by 8%
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

<details><summary><b>What analysts and big funds say</b> — score +0.50</summary>

```text
Consensus: buy (mean 2.07 on a 1=strong buy to 5=strong sell scale, 26 analysts)
Ratings: 1 strong buy, 14 buy, 11 hold, 1 sell, 1 strong sell
Price target: mean 970.80 (+21.7% vs last close), range 575.00 - 1,155.00
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

<details><summary><b>What analysts say about what this fund holds</b> — score +0.50</summary>

_Not available today._

</details>

<details><summary><b>Buying and selling by company insiders</b> — score +0.00</summary>

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

<details><summary><b>Who is positioned how</b> — score +0.00</summary>

_Not available today._

</details>

<details><summary><b>Money going into and out of this fund</b> — score +0.00</summary>

_Not available today._

</details>

### Elbit Systems (ESLT) · Company — NEUTRAL, confidence 0.35

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Mixed signals: Jefferies target cut and downtrend technicals are bearish, but four straight earnings beats and a +21% price target suggest upside; high valuation tempers optimism. Overall view remains neutral with modest conviction.

**Main reasons it gave:**
- Jefferies cuts target to USD 790 (negative news)
- RSI 30 and price below SMAs indicating oversold but downtrend (bearish technicals)
- Four consecutive earnings beats (positive earnings record)
- High trailing P/E ~50 suggests expensive valuation (fundamental concern)

<details><summary><b>News</b> — score -0.20</summary>

- [Elbit Systems Ltd. (ESLT) stock price, news, quote and history](https://uk.finance.yahoo.com/quote/ESLT/)  
  <sub>Yahoo Finance UK, 12 hours ago</sub>  
  16,527.25% · Previous close 669.13 · Open 663.45 · Bid 844.57 x 100 · Ask 690.28 x 200 · Day's range 662.41 - 671.31 · 52-week range 453.00 - 1,016.06 · Volume...
- [Elbit Systems plans turret deliveries and Jefferies cuts Elbit Systems stock target to USD 790](https://www.ad-hoc-news.de/boerse/news/corporate-news/elbit-systems-plans-turret-deliveries-and-jefferies-cuts-elbit-systems-stock-target-to-usd-790/70276476)  
  <sub>AD HOC NEWS, 4 hours ago</sub>  
  ESLT, IL0010811243. Elbit Systems plans turret deliveries and Jefferies cuts Elbit Systems stock target to USD 790. Published on 10/09/2026 at 12:38...
- [Elbit Systems stock loses 0.13 percent pre-market to EUR 593.00](https://www.ad-hoc-news.de/boerse/news/vorboerse/elbit-systems-stock-loses-0-13-percent-pre-market-to-eur-593-00/70272972)  
  <sub>AD HOC NEWS, 9 hours ago</sub>  
  ESLT, IL0010811243. Elbit Systems stock loses 0.13 percent pre-market to EUR 593.00. Published on 10/09/2026 at 08:14 | Editorial responsibility: Rafael...
- [Elbit Systems stock trades at EUR 588.75 with a P/ E ratio of 49.3](https://www.ad-hoc-news.de/boerse/news/corporate-news/elbit-systems-stock-trades-at-eur-588-75-with-a-p-e-ratio-of-49-3/70280173)  
  <sub>AD HOC NEWS, 16 minutes ago</sub>  
  ESLT, IL0010811243. Elbit Systems stock trades at EUR 588.75 with a P/ E ratio of 49.3. Published on 10/09/2026 at 16:28 | Editorial responsibility: Rafael...
- [Elbit Systems stock trades at EUR 596.50 with USD 31.4 billion market cap](https://www.ad-hoc-news.de/boerse/news/corporate-news/elbit-systems-stock-trades-at-eur-596-50-with-usd-31-4-billion-market-cap/70267776)  
  <sub>AD HOC NEWS, 24 hours ago</sub>  
  ESLT, IL0010811243. Elbit Systems stock trades at EUR 596.50 with USD 31.4 billion market cap. Published on 10/08/2026 at 16:48 | Editorial responsibility:...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score -0.20</summary>

_Not available today._

</details>

<details><summary><b>Price and chart</b> — score -0.35</summary>

```text
Last close 660.19 (bar of 2026-10-09), from 502 daily bars
Trend: vs 20d SMA 713.79 (-7.5%), 50d 742.50 (-11.1%), 200d 777.06 (-15.0%); 50d below 200d
Momentum: RSI(14) 30.0 | MACD -18.616 vs signal -13.622 (histogram -4.994)
Returns: 1d -0.7% | 5d -5.2% | 1m -8.8% | 3m -10.2%
52-week range: 454.95 - 1,014.33 (now 36.7% of the way up)
Volatility: ATR(14) 17.51 (2.7% of price) | annualised 20d 26.8%
Volume: 0.17x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score -0.10</summary>

```text
Sector: Industrials / Aerospace & Defense | market cap 30.94B
Valuation: trailing P/E 49.68 | forward P/E 35.95 | P/B 7.00 | PEG n/a
Profitability: profit margin 7.4% | operating margin 9.6% | ROE 15.2%
Growth (YoY): revenue +15.9% | earnings +34.2%
Balance sheet: debt/equity 19.3% | free cash flow -38.48M
Risk: beta -0.30 | short interest 0.9% of float
Next earnings: 2026-11-24
```

</details>

<details><summary><b>What this fund holds</b> — score -0.10</summary>

_Not available today._

</details>

<details><summary><b>Does this company beat its own forecasts</b> — score -0.10</summary>

```text
Earnings record, last 4 quarters: 4 beats
  2026-06-30 beat by 10% | 2026-03-31 beat by 16% | 2025-12-31 beat by 16% | 2025-09-30 beat by 21%
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

<details><summary><b>What analysts and big funds say</b> — score +0.10</summary>

```text
Consensus: hold (mean 2.67 on a 1=strong buy to 5=strong sell scale, 6 analysts)
Ratings: 0 strong buy, 1 buy, 5 hold, 0 sell, 0 strong sell
Price target: mean 801.33 (+21.4% vs last close), range 518.00 - 960.00
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

<details><summary><b>What analysts say about what this fund holds</b> — score +0.10</summary>

_Not available today._

</details>

<details><summary><b>Buying and selling by company insiders</b> — score +0.00</summary>

```text
Last 180 days: bought 82,000 shares in 7 transaction(s) | sold 69,736 shares in 7
Net: +12,264 shares (+0.1% of insider holdings) | insiders hold 19,278,816 shares
Distinct insiders: 0 buying, 0 selling
```

</details>

<details><summary><b>Who is positioned how</b> — score +0.00</summary>

_Not available today._

</details>

<details><summary><b>Money going into and out of this fund</b> — score +0.00</summary>

_Not available today._

</details>

### MercadoLibre (MELI) · Company — NEUTRAL, confidence 0.35

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Mixed signals across dimensions: news shows both investor buying and selling, technicals are slightly bullish but volume is thin, fundamentals are mixed with strong revenue growth but high leverage and negative earnings growth, analysts are bullish but no fresh upgrades, insiders made modest purchases, and earnings record is weak (3 misses, 1 beat). The aggregate view is near‑neutral with low conviction.

**Main reasons it gave:**
- Mixed institutional activity: Stableford increased stake while Bell and Zevenbergen reduced stakes
- Price above 20‑day, 50‑day, and 200‑day SMAs but volume only 0.08× 20‑day average
- High debt/equity 168.6% and earnings growth -10.9% despite 49.8% revenue growth
- Earnings record: 1 beat, 3 misses in last four quarters

<details><summary><b>News</b> — score +0.20</summary>

- [MercadoLibre, Inc. $MELI Stock Position Increased by Stableford Capital II LLC](https://www.marketbeat.com/instant-alerts/filing-mercadolibre-inc-meli-stock-position-increased-by-stableford-capital-ii-llc-2026-10-09/)  
  <sub>MarketBeat, 3 hours ago</sub>  
  Stableford Capital II LLC increased its holdings in MercadoLibre, Inc. (NASDAQ:MELI - Free Report) by 34.0% in the 3rd quarter, according to the company in...
- [MELI Oct 2026 1590.000 call (MELI261009C01590000) Stock Price, News, Quote & History](https://ca.finance.yahoo.com/quote/MELI261009C01590000/)  
  <sub>Yahoo! Finance Canada, 9 hours ago</sub>  
  Find the latest MELI Oct 2026 1590.000 call (MELI261009C01590000) stock quote, history, news and other vital information to help you with your stock trading...
- [730 MercadoLibre, Inc. $MELI Shares Sold by Bell Asset Management Ltd](https://www.marketbeat.com/instant-alerts/filing-730-mercadolibre-inc-meli-shares-sold-by-bell-asset-management-ltd-2026-10-09/)  
  <sub>MarketBeat, 7 hours ago</sub>  
  Bell Asset Management Ltd decreased its stake in MercadoLibre, Inc. (NASDAQ:MELI - Free Report) by 32.1% in the third quarter, according to the company in...
- [MercadoLibre (MELI) Could Be 42% Below Fair Value After Fresh Investor Backing](https://simplywall.st/stocks/us/retail/nasdaq-meli/mercadolibre/news/mercadolibre-meli-could-be-42-below-fair-value-after-fresh-i)  
  <sub>Simply Wall Street, 21 hours ago</sub>  
  MercadoLibre (MELI) is back in focus after renewed interest from high profile investors, linked to its record of steady revenue, logistics and fintech build...
- [MELI Oct 2026 1705.000 put (MELI261009P01705000) interactive stock chart](https://uk.finance.yahoo.com/quote/MELI261009P01705000/chart/)  
  <sub>Yahoo Finance UK, 9 hours ago</sub>  
  Interactive chart for MELI Oct 2026 1705.000 put (MELI261009P01705000) – analyse all of the data with a huge range of indicators.
- [Jefferies keeps USD 2,600 target for MercadoLibre stock](https://www.ad-hoc-news.de/boerse/news/corporate-news/jefferies-keeps-usd-2-600-target-for-mercadolibre-stock/70279380)  
  <sub>AD HOC NEWS, 1 hour ago</sub>  
  MELI, US58733R1023. Jefferies keeps USD 2,600 target for MercadoLibre stock. Published on 10/09/2026 at 15:28 | Editorial responsibility: Rafael Müller,...
- [MELI Dec 2027 2070.000 call (MELI271217C02070000) Interactive Stock Chart](https://ca.finance.yahoo.com/quote/MELI271217C02070000/chart/)  
  <sub>Yahoo! Finance Canada, 13 hours ago</sub>  
  Interactive Chart for MELI Dec 2027 2070.000 call (MELI271217C02070000), analyze all the data with a huge range of indicators.
- [Zevenbergen Capital Investments LLC Reduces Stake in MercadoLibre, Inc. $MELI](https://www.marketbeat.com/instant-alerts/filing-zevenbergen-capital-investments-llc-reduces-stake-in-mercadolibre-inc-meli-2026-10-08/)  
  <sub>MarketBeat, 15 hours ago</sub>  
  Zevenbergen Capital Investments LLC decreased its holdings in shares of MercadoLibre, Inc. (NASDAQ:MELI - Free Report) by 18.2% during the third quarter,...
- [MELI Oct 2026 2210.000 call (MELI261009C02210000) interactive stock chart](https://uk.finance.yahoo.com/quote/MELI261009C02210000/chart/)  
  <sub>Yahoo Finance UK, 14 hours ago</sub>  
  Interactive chart for MELI Oct 2026 2210.000 call (MELI261009C02210000) – analyse all of the data with a huge range of indicators.
- [MercadoLibre closed USD 1 billion notes: MercadoLibre stock sits 23.39 percent below its high](https://www.ad-hoc-news.de/boerse/news/corporate-news/mercadolibre-closed-usd-1-billion-notes-mercadolibre-stock-sits-23-39-percent-below-its-high/70267831)  
  <sub>AD HOC NEWS, 24 hours ago</sub>  
  MELI, US58733R1023. MercadoLibre closed USD 1 billion notes: MercadoLibre stock sits 23.39 percent below its high. Published on 10/08/2026 at 16:54...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.20</summary>

_Not available today._

</details>

<details><summary><b>Price and chart</b> — score +0.20</summary>

```text
Last close 1,865.88 (bar of 2026-10-09), from 502 daily bars
Trend: vs 20d SMA 1,799.80 (+3.7%), 50d 1,861.88 (+0.2%), 200d 1,835.15 (+1.7%); 50d above 200d
Momentum: RSI(14) 55.2 | MACD -8.000 vs signal -23.973 (histogram 15.974)
Returns: 1d +0.5% | 5d +10.0% | 1m -2.1% | 3m -0.1%
52-week range: 1,546.81 - 2,360.76 (now 39.2% of the way up)
Volatility: ATR(14) 56.84 (3.0% of price) | annualised 20d 43.0%
Volume: 0.08x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score -0.20</summary>

```text
Sector: Consumer Cyclical / Internet Retail | market cap 94.59B
Valuation: trailing P/E 50.74 | forward P/E 32.94 | P/B 12.07 | PEG 1.00
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

<details><summary><b>What analysts and big funds say</b> — score +0.30</summary>

```text
Consensus: buy (mean 1.58 on a 1=strong buy to 5=strong sell scale, 26 analysts)
Ratings: 5 strong buy, 16 buy, 5 hold, 0 sell, 0 strong sell
Price target: mean 2,275.78 (+22.0% vs last close), range 1,750.00 - 2,800.00
Recent rating changes:
  - 2026-10-06 Susquehanna: main, Positive -> Positive
  - 2026-09-03 BTIG: reit, Buy -> Buy
  - 2026-08-11 JP Morgan: main, Neutral -> Neutral
  - 2026-08-06 Cantor Fitzgerald: main, Overweight -> Overweight
  - 2026-08-06 BTIG: reit, Buy -> Buy
  - 2026-07-15 Citigroup: main, Neutral -> Neutral
Institutional ownership: 80.2%
Largest holders: Capital Research Global Investors (6.2%), BAILLIE GIFFORD & CO (6.0%), Capital International Investors (3.7%), Capital World Investors (3.5%), Morgan Stanley (2.9%)
```

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score +0.30</summary>

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

### Toyota (TM) · Company — NEUTRAL, confidence 0.35

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Mixed signals: bullish fundamentals (cheap P/E, strong earnings growth), analyst optimism (2 strong‑buy, 2 buy, +26.7% target) and a solid earnings record (4 straight beats) are offset by bearish technicals (price below 20‑, 50‑ and 200‑day SMAs, RSI 44, thin volume). No material news catalyst and contradictory dimensions lead to a neutral stance with low conviction.

**Main reasons it gave:**
- Trailing P/E 8.12 (cheap valuation)
- Four consecutive earnings beats (44%, 12%, 27%, 24%)
- Price below 20d/50d/200d SMA, RSI 44, volume 0.22× average (bearish technicals)
- Analyst ratings: 2 strong buy, 2 buy; price target +26.7% above current price

<details><summary><b>News</b> — score +0.00</summary>

- [15 new hires receive stock awards from Ocular Therapeutix](https://www.stocktitan.net/news/OCUL/ocular-therapeutix-tm-reports-inducement-grants-under-nasdaq-listing-pqg63od9shwu.html)  
  <sub>Stock Titan, 4 hours ago</sub>  
  22900 restricted stock units vest over three years; options carry a $7.25 exercise price and vest over four years, subject to continued service.
- [Toyota Motor Q2 2027 Earnings Date and Estimates](https://www.marketbeat.com/earnings/reports/2026-11-5-toyota-motor-co-stock/)  
  <sub>MarketBeat, 14 hours ago</sub>  
  Toyota Motor is expected to report Q2 2027 earnings on November 5, 2026. See the scheduled call time, analyst EPS and revenue estimates, and past results...
- [Gorilla Technology and Hoya Capital Interviews to Air Nationally on the RedChip Small Stocks, Big Money(TM) Show on CNBC and Bloomberg TV](https://www.accessnewswire.com/newsroom/en/business-and-professional-services/gorilla-technology-and-hoya-capital-interviews-to-air-nationally-1234948)  
  <sub>ACCESS Newswire, 1 hour ago</sub>  
  ORLANDO, FL / ACCESS Newswire / October 9, 2026 / RedChip Companies will air interviews with Gorilla Technology Group Inc. (NASDAQ:GRRR) and Hoya Capital on...
- [How to Take Advantage of moves in (FMAX) (FMAX:CA)](https://news.stocktradersdaily.com/canada/how-to-take-advantage-of-moves-in-fmax-_20261009_480d3e)  
  <sub>Stock Traders Daily, 9 hours ago</sub>  
  When Investors Make Decisions in Hamilton U.S. Financials YIELD MAXIMIZER TM ETF FMAX Opportunities Surface.
- [Nexalin Technology, Inc. (NXL) Stock Price, News, Quote & History](https://ca.finance.yahoo.com/quote/NXL/)  
  <sub>Yahoo! Finance Canada, 13 hours ago</sub>  
  Find the latest Nexalin Technology, Inc. (NXL) stock quote, history, news and other vital information to help you with your stock trading and investing.
- [Toyota Motor stock at EUR 164.50, down 14.6 percent in 2026](https://www.ad-hoc-news.de/boerse/news/corporate-news/toyota-motor-stock-at-eur-164-50-down-14-6-percent-in-2026/70279426)  
  <sub>AD HOC NEWS, 1 hour ago</sub>  
  TM, US8923313071. Toyota Motor stock at EUR 164.50, down 14.6 percent in 2026. Published on 10/09/2026 at 15:30 | Editorial responsibility: Rafael Müller,...
- [Unusual Volume Stocks Today: MI, BIYA, SMXT Gain; VCIG and KAPA Slide](https://www.chartmill.com/news/KAPA/Chartmill-55892-Unusual-Volume-Stocks-Today-MI-BIYA-SMXT-Gain-VCIG-and-KAPA-Slide)  
  <sub>ChartMill, 22 hours ago</sub>  
  Today's unusual-volume screen focuses on stocks trading well above their 50-day average volume, often alongside notable price moves.
- [Arrive AI and Modovolo Partner to Advance Autonomous Drone Delivery](https://www.stocktitan.net/news/ARAI/arrive-ai-and-modovolo-partner-to-advance-autonomous-drone-c130ggx52vss.html)  
  <sub>Stock Titan, 2 hours ago</sub>  
  The companies are developing a drone-to-station handoff; live deliveries in Fishers are planned after testing and any required regulatory approvals.
- [SpaceX Acquires Nationwide Low-Frequency Spectrum, Impacting T-M](https://www.gurufocus.com/news/9116286/spacex-acquires-nationwide-lowfrequency-spectrum-impacting-tmobile-tmus-verizon-vz)  
  <sub>GuruFocus, 17 hours ago</sub>  
  On October 08, 2026, SpaceX announced its agreement to acquire a comprehensive set of low-frequency spectrum licenses across the United States.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

_Not available today._

</details>

<details><summary><b>Price and chart</b> — score -0.60</summary>

```text
Last close 184.76 (bar of 2026-10-09), from 502 daily bars
Trend: vs 20d SMA 188.45 (-2.0%), 50d 190.54 (-3.0%), 200d 200.59 (-7.9%); 50d below 200d
Momentum: RSI(14) 44.0 | MACD -2.111 vs signal -1.707 (histogram -0.404)
Returns: 1d -0.7% | 5d +1.8% | 1m -4.0% | 3m +5.7%
52-week range: 166.50 - 248.29 (now 22.3% of the way up)
Volatility: ATR(14) 3.02 (1.6% of price) | annualised 20d 19.0%
Volume: 0.22x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.00</summary>

```text
Sector: Consumer Cyclical / Auto Manufacturers | market cap 218.78B
Valuation: trailing P/E 8.12 | forward P/E 11.71 | P/B 14.66 | PEG n/a
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
Price target: mean 234.08 (+26.7% vs last close), range 230.00 - 239.31
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

### JPMorgan Chase (JPM) · Company — NEUTRAL, confidence 0.32

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Fundamentals and earnings record are strong, but technicals show short‑term weakness and the news is generic. Conflicting signals lead to a neutral stance with low conviction.

**Main reasons it gave:**
- Strong earnings record: 4 consecutive beats
- Solid fundamentals: low P/E, high profit margins
- Technical weakness: price below 20‑day/50‑day SMA, low volume
- Upcoming earnings in a few days
- Positive news: dividend raise and digital‑asset product launch

<details><summary><b>News</b> — score +0.20</summary>

- [JPMorgan Chase Stock: Earnings Tell Half The Story (NYSE:JPM)](https://seekingalpha.com/article/4953036-jpm-earnings-tell-half-the-story)  
  <sub>Seeking Alpha, 3 hours ago</sub>  
  JPMorgan Chase (JPM) Stock Q2 highlights: deposit/loan growth, wealth inflows, and IB gains. Read here for a detailed investment analysis.
- [JPMorgan Chase & Co. $JPM Stock Position Lifted by GAMMA Investing LLC](https://www.marketbeat.com/instant-alerts/filing-jpmorgan-chase-co-jpm-stock-position-lifted-by-gamma-investing-llc-2026-10-09/)  
  <sub>MarketBeat, 6 hours ago</sub>  
  GAMMA Investing LLC grew its position in JPMorgan Chase & Co. (NYSE:JPM) by 8.5% during the 3rd quarter, according to the company in its most recent filing...
- [What is drawing attention to JPMorgan Chase (NYSE:JPM) stock as the earnings stretch nears today?](https://kalkinemedia.com/us/stocks/bluechip/what-is-drawing-attention-to-jpmorgan-chase-nysejpm-stock-as-the-earnings-stretch-nears-today)  
  <sub>Kalkine Media, 1 hour ago</sub>  
  JPMorgan Chase (NYSE:JPM) draws market focus as large banks step into the earnings stretch, with lending, trading, deposits and fee businesses in view.
- [(JPM) as a Liquidity Pulse for Institutional Tactics](https://news.stocktradersdaily.com/news_release/1/JPM_as_a_Liquidity_Pulse_for_Institutional_Tactics_100926083001_1791549001.html)  
  <sub>Stock Traders Daily, 6 hours ago</sub>  
  Key findings for Jpmorgan Chase & Co. (NYSE: JPM). Divergent Sentiment Across All Horizons Suggests Choppy Conditions; A mid-channel oscillation pattern is...
- [Goldman Sachs expected to lead Wall Street's $19B trading revenue in Q3 - report](https://www.tradingview.com/news/seekingalpha:9dd54d843094b:0-goldman-sachs-expected-to-lead-wall-street-s-19b-trading-revenue-in-q3-report/)  
  <sub>TradingView, 3 hours ago</sub>  
  The top Wall Street banks are expected to report a total of almost $19B in stock trading revenue when firms report Q3 earnings next week, according to a...
- [JPM, BofA Eye Payments Deal — Why JPMorgan, Bank Of America And Other Banks Want Fiserv’s Debit Network](https://stocktwits.com/news-articles/markets/equity/jpm-bof-a-eye-payments-deal-why-jp-morgan-bank-of-america-and-other-banks-want-fiserv-s-debit-network/cZmlGh2R7mc)  
  <sub>Stocktwits, 13 hours ago</sub>  
  Fiserv (FISV) share price gained 4% after-hours amid a report that several top financial institutions are looking to acquire a network owned by the firm to...
- [JPMorgan Chase (JPM) Puts JLTXX On Ethereum As Stablecoin Reserve Rules Near](https://simplywall.st/stocks/us/banks/nyse-jpm/jpmorgan-chase/news/jpmorgan-chase-jpm-puts-jltxx-on-ethereum-as-stablecoin-rese)  
  <sub>Simply Wall Street, 16 hours ago</sub>  
  JPMorgan Chase (NYSE:JPM) launched JLTXX, a tokenized money market fund on Ethereum, expanding its digital asset infrastructure offering.
- [JPM vs. C: Which Bank Dividend Actually Survives the Next Crisis?](https://www.aol.com/articles/jpm-vs-c-bank-dividend-130052000.html)  
  <sub>AOL.com, 2 hours ago</sub>  
  Both JPM and C just raised dividends, but Citi's crisis-era cuts to $0.01 per quarter give JPMorgan the clear reliability edge for retirees.
- [JPMorgan Chase & Co. $JPM Shares Purchased by Mn Services Vermogensbeheer B.V.](https://www.marketbeat.com/instant-alerts/filing-jpmorgan-chase-co-jpm-shares-purchased-by-mn-services-vermogensbeheer-bv-2026-10-09/)  
  <sub>MarketBeat, 6 hours ago</sub>  
  Mn Services Vermogensbeheer B.V. grew its position in shares of JPMorgan Chase & Co. (NYSE:JPM) by 1.1% during the 3rd quarter, according to its most recent...
- [JPM Oct 2026 360.000 put (JPM261009P00360000) stock price, news, quote and history](https://uk.finance.yahoo.com/quote/JPM261009P00360000/)  
  <sub>Yahoo Finance UK, 21 hours ago</sub>  
  Find the latest JPM Oct 2026 360.000 put (JPM261009P00360000) stock quote, history, news and other vital information to help you with your stock trading and...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.20</summary>

_Not available today._

</details>

<details><summary><b>Price and chart</b> — score -0.35</summary>

```text
Last close 331.14 (bar of 2026-10-09), from 502 daily bars
Trend: vs 20d SMA 339.27 (-2.4%), 50d 350.11 (-5.4%), 200d 322.13 (+2.8%); 50d above 200d
Momentum: RSI(14) 35.1 | MACD -5.766 vs signal -5.221 (histogram -0.545)
Returns: 1d -0.1% | 5d -0.4% | 1m -6.3% | 3m -1.0%
52-week range: 282.84 - 365.18 (now 58.7% of the way up)
Volatility: ATR(14) 5.76 (1.7% of price) | annualised 20d 17.5%
Volume: 0.13x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.55</summary>

```text
Sector: Financial Services / Banks - Diversified | market cap 880.22B
Valuation: trailing P/E 14.19 | forward P/E 13.18 | P/B 2.49 | PEG 1.57
Profitability: profit margin 34.9% | operating margin 50.4% | ROE 17.8%
Growth (YoY): revenue +30.4% | earnings +46.9%
Balance sheet: debt/equity n/a | free cash flow n/a
Risk: beta 1.01 | short interest 0.9% of float
Next earnings: 2026-10-13
```

</details>

<details><summary><b>What this fund holds</b> — score +0.55</summary>

_Not available today._

</details>

<details><summary><b>Does this company beat its own forecasts</b> — score +0.55</summary>

```text
Earnings record, last 4 quarters: 4 beats
  2026-06-30 beat by 4% | 2026-03-31 beat by 8% | 2025-12-31 beat by 3% | 2025-09-30 beat by 4%
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

<details><summary><b>What analysts and big funds say</b> — score +0.35</summary>

```text
Consensus: buy (mean 2.12 on a 1=strong buy to 5=strong sell scale, 22 analysts)
Ratings: 4 strong buy, 9 buy, 12 hold, 0 sell, 0 strong sell
Price target: mean 372.68 (+12.5% vs last close), range 305.00 - 420.00
Recent rating changes:
  - 2026-10-05 UBS: main, Buy -> Buy
  - 2026-09-28 HSBC: main, Hold -> Hold
  - 2026-08-14 Wells Fargo: main, Overweight -> Overweight
  - 2026-08-03 UBS: main, Buy -> Buy
  - 2026-07-20 Citigroup: main, Neutral -> Neutral
  - 2026-07-17 Evercore ISI Group: main, Outperform -> Outperform
Institutional ownership: 75.6%
Largest holders: Blackrock Inc. (7.8%), Vanguard Capital Management LLC (6.1%), State Street Corporation (4.7%), Bank of America Corporation (2.6%), Morgan Stanley (2.5%)
```

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score +0.35</summary>

_Not available today._

</details>

<details><summary><b>Buying and selling by company insiders</b> — score +0.00</summary>

```text
Last 180 days: bought 136,610 shares in 7 transaction(s) | sold 230,236 shares in 19
Net: -93,626 shares (-0.9% of insider holdings) | insiders hold 10,393,508 shares
Distinct insiders: 0 buying, 10 selling
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

### Eli Lilly (LLY) · Company — no answer, no confidence given

<details><summary><b>News</b> — score n/a</summary>

- [Here is What to Know Beyond Why Eli Lilly and Company (LLY) is a Trending Stock](https://uk.finance.yahoo.com/news/know-beyond-why-eli-lilly-120006081.html)  
  <sub>Yahoo Finance UK, 3 hours ago</sub>  
  Lilly (LLY) has been one of the stocks most watched by Zacks.com users lately. So, it is worth exploring what lies ahead for the stock.
- [Eli Lilly’s Biggest Shareholder Just Filed to Sell $347 Million of Stock](https://247wallst.com/investing/2026/10/09/eli-lillys-biggest-shareholder-just-filed-to-sell-347-million-of-stock/)  
  <sub>24/7 Wall St., 1 hour ago</sub>  
  Lilly's largest shareholder just filed to unload nearly $350 million in stock while analysts keep raising their price targets, and those two facts point in...
- [Lilly’s two medicines were linked to changes in 482 blood proteins, versus 140 with Taltz alone.](https://www.stocktitan.net/news/LLY/new-phase-3b-data-on-lilly-s-taltz-ixekizumab-and-zepbound-qnnu10fy7psj.html)  
  <sub>Stock Titan, 4 hours ago</sub>  
  Eli Lilly and Company (LLY) announced exploratory Phase 3b results comparing combined Taltz and Zepbound treatment with Taltz alone in psoriasis.
- [Eli Lilly: Weight-Loss Money Machine Isn't Slowing Down (NYSE:LLY)](https://seekingalpha.com/article/4953040-eli-lilly-weight-loss-money-machine-isnt-slowing-down)  
  <sub>Seeking Alpha, 3 hours ago</sub>  
  Eli Lilly and Company leads GLP-1 with Mounjaro/Zepbound growth, Retatrutide catalyst, and a 50%+ EPS outlook. Click here to read more on LLY stock.
- [Discipline and Rules-Based Execution in LLY Response](https://news.stocktradersdaily.com/news_release/12/Discipline_and_Rules-Based_Execution_in_LLY_Response_100926084001_1791549601.html)  
  <sub>Stock Traders Daily, 6 hours ago</sub>  
  Price-action only: Eli Lilly And Company (LLY) movements set the tone for institutional models. Discipline and Rules-Based Execution in LLY Response.
- [SPY is down 0.4% today, on LLY stock price movement](https://www.quiverquant.com/news/SPY+is+down+0.4%25+today%2C+on+LLY+stock+price+movement)  
  <sub>Quiver Quantitative, 22 hours ago</sub>  
  $SPY stock has fallen 0.4% today, according to our price data from Polygon. It has been dragged by LLY stock falling 4.4%.
- [Top 3 Biotech Stocks To Watch In October 2026](https://simplywall.st/stocks/us/pharmaceuticals-biotech/nyse-lly/eli-lilly/news/top-3-biotech-stocks-to-watch-in-october-2026/amp)  
  <sub>Simply Wall Street, 8 hours ago</sub>  
  Bond giant Pimco now sees a real chance of US 10 year Treasury yields hitting 6%, which pulls money toward safer income and makes investors choosier about...
- [ETFs Bought $19.3 Million of Eli Lilly (LLY) on Wednesday](https://www.gurufocus.com/news/9116971/etfs-bought-193-million-of-eli-lilly-lly-on-wednesday)  
  <sub>GuruFocus, 3 hours ago</sub>  
  ETF flows into Eli Lilly (LLY) totaled a net $19.3 million in Wednesday's session, as 34 ETFs bought shares and 16 sold. The buying marked a second straight...
- [New data for Eli Lilly and the Taltz-Zepbound combination](https://www.marketscreener.com/quote/stock/ELI-LILLY-AND-COMPANY-13401/news/New-data-for-Eli-Lilly-and-the-Taltz-Zepbound-combination-54459692/)  
  <sub>marketscreener.com, 1 hour ago</sub>  
  The US giant has unveiled new exploratory data from a Phase 3b clinical trial evaluating the concomitant use of Taltz and Zepbound compared with Taltz alone...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>Price and chart</b> — score n/a</summary>

```text
Last close 1,171.58 (bar of 2026-10-09), from 502 daily bars
Trend: vs 20d SMA 1,160.93 (+0.9%), 50d 1,173.82 (-0.2%), 200d 1,076.46 (+8.8%); 50d above 200d
Momentum: RSI(14) 52.1 | MACD 0.151 vs signal -2.175 (histogram 2.326)
Returns: 1d +0.2% | 5d +2.5% | 1m +4.3% | 3m -0.9%
52-week range: 799.57 - 1,280.34 (now 77.4% of the way up)
Volatility: ATR(14) 34.10 (2.9% of price) | annualised 20d 21.0%
Volume: 0.13x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score n/a</summary>

```text
Sector: Healthcare / Drug Manufacturers - General | market cap 1.04T
Valuation: trailing P/E 39.33 | forward P/E 24.62 | P/B 30.83 | PEG 1.14
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
Consensus: buy (mean 1.63 on a 1=strong buy to 5=strong sell scale, 29 analysts)
Ratings: 6 strong buy, 19 buy, 3 hold, 1 sell, 1 strong sell
Price target: mean 1,329.21 (+13.5% vs last close), range 930.00 - 1,600.00
Recent rating changes:
  - 2026-10-08 Cantor Fitzgerald: main, Overweight -> Overweight
  - 2026-10-07 Morgan Stanley: main, Overweight -> Overweight
  - 2026-09-28 JP Morgan: main, Overweight -> Overweight
  - 2026-09-22 TD Cowen: reit, Buy -> Buy
  - 2026-09-18 Guggenheim: main, Buy -> Buy
  - 2026-09-10 HSBC: main, Reduce -> Reduce
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

- [Fund Update: 95,439 MICROSOFT (MSFT) shares added to Border to Coast Pensions Partnership Ltd portfolio](https://www.quiverquant.com/news/Fund+Update%3A+95%2C439+MICROSOFT+%28MSFT%29+shares+added+to+Border+to+Coast+Pensions+Partnership+Ltd+portfolio)  
  <sub>Quiver Quantitative, 4 hours ago</sub>  
  Border to Coast Pensions Partnership Ltd has added 95439 shares of $MSFT to their portfolio, per a.
- [MSFT Stock Rises Premarket Ahead Of Q4 Results: CapEx, Azure Growth In Focus](https://stocktwits.com/news-articles/markets/equity/msft-stock-rises-premarket-ahead-of-q4-results-cap-ex-azure-growth-in-focus/cZNR8GoRJRW)  
  <sub>Stocktwits, 18 hours ago</sub>  
  Analysts expect Microsoft's fiscal fourth quarter revenue to rise 15% to $87.63 billion – which would be the lowest in the last five quarters – and adjusted...
- [Microsoft (MSFT) Posted 43% Azure Growth, Yet Trades Below Its Own Five-Year P/E. A Real Discount?](https://finance.yahoo.com/markets/stocks/articles/microsoft-msft-posted-43-azure-132642768.html)  
  <sub>Yahoo Finance, 1 hour ago</sub>
- [Use This Unconventional Add-On Entry To Add To Breakouts In Microsoft, Palantir Technologies](https://www.investors.com/how-to-invest/investors-corner/dow-jones-microsoft-stock-msft-palantir-pltr-shelf-entry/)  
  <sub>Investor's Business Daily, 3 hours ago</sub>  
  Dow Jones software giant Microsoft stock and Palantir have been big winners in recent months. They recently moved above shelf entries.
- [What's Going On With Microsoft Stock Thursday?](https://www.benzinga.com/markets/tech/26/10/62253346/whats-going-on-with-microsoft-stock-thursday-5)  
  <sub>Benzinga, 22 hours ago</sub>  
  Microsoft stock dips as tech stocks weaken and overbought signals emerge, while Activision Blizzard faces fresh EU scrutiny.
- [(MSFT) Price Dynamics and Execution-Aware Positioning](https://news.stocktradersdaily.com/news_release/40/MSFT_Price_Dynamics_and_Execution-Aware_Positioning_100926090801_1791551281.html)  
  <sub>Stock Traders Daily, 6 hours ago</sub>  
  Key findings for Microsoft Corporation (NASDAQ: MSFT). If Near and Mid-Term Strong Sentiment Holds, It Could Extend to Long Term; No clear price positioning...
- [3 High Quality Stocks With ROE Over 30%](https://simplywall.st/stocks/us/software/nasdaq-msft/microsoft/news/3-high-quality-stocks-with-roe-over-30)  
  <sub>Simply Wall Street, 8 hours ago</sub>  
  Bond giant Pimco now sees a real risk that the US 10 year Treasury yield could reach 6% for the first time since 2000. Higher risk free returns can quickly...
- [MSFT Stock Hits Highest Level This Year: Microsoft To Reportedly Hike Production Of AI Chips](https://stocktwits.com/news-articles/markets/equity/microsoft-to-reportedly-hike-production-of-ai-chips/cZojwJgRJO6)  
  <sub>Stocktwits, 14 hours ago</sub>  
  Morgan Stanley lowered its price target on the stock to $13 from $26 and keeps an 'Equal Weight' rating on the shares. The company announced revenue guidance...
- [MSFT Oct 2026 585.000 call (MSFT261007C00585000) interactive stock chart](https://uk.finance.yahoo.com/quote/MSFT261007C00585000/chart/)  
  <sub>Yahoo Finance UK, 8 hours ago</sub>
- [Here’s How Much You Would Have Made Owning Microsoft Stock In The Last 20 Years](https://www.benzinga.com/news/26/10/62263077/here-s-how-much-you-would-have-made-owning-microsoft-stock-last-20-years)  
  <sub>Benzinga, 17 hours ago</sub>  
  Microsoft (NASDAQ:MSFT) has outperformed the market over the past 20 years by 6.6% on an annualized basis producing an average annual return of 15.67%.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>Price and chart</b> — score n/a</summary>

```text
Last close 531.82 (bar of 2026-10-09), from 502 daily bars
Trend: vs 20d SMA 509.94 (+4.3%), 50d 500.38 (+6.3%), 200d 433.99 (+22.5%); 50d above 200d
Momentum: RSI(14) 66.1 | MACD 10.382 vs signal 9.080 (histogram 1.302)
Returns: 1d +1.8% | 5d +2.8% | 1m +8.0% | 3m +36.0%
52-week range: 352.83 - 542.07 (now 94.6% of the way up)
Volatility: ATR(14) 11.49 (2.2% of price) | annualised 20d 22.1%
Volume: 0.18x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score n/a</summary>

```text
Sector: Technology / Software - Infrastructure | market cap 3.95T
Valuation: trailing P/E 29.63 | forward P/E 22.46 | P/B 8.93 | PEG 1.62
Profitability: profit margin 40.3% | operating margin 45.1% | ROE 34.0%
Growth (YoY): revenue +17.7% | earnings +31.7%
Balance sheet: debt/equity 29.1% | free cash flow 16.55B
Risk: beta 1.10 | short interest 0.9% of float
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
Consensus: strong_buy (mean 1.29 on a 1=strong buy to 5=strong sell scale, 53 analysts)
Ratings: 14 strong buy, 41 buy, 1 hold, 0 sell, 0 strong sell
Price target: mean 587.63 (+10.5% vs last close), range 440.00 - 870.00
Recent rating changes:
  - 2026-10-07 Evercore ISI Group: main, Outperform -> Outperform
  - 2026-10-05 Scotiabank: main, Sector Outperform -> Sector Outperform
  - 2026-10-01 Wells Fargo: main, Overweight -> Overweight
  - 2026-09-30 Piper Sandler: main, Overweight -> Overweight
  - 2026-09-23 Stifel: up, Hold -> Buy
  - 2026-09-22 Oppenheimer: main, Outperform -> Outperform
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
Net: +271,300 shares (+4.2% of insider holdings) | insiders hold 6,682,991 shares
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

### Novo Nordisk (NVO) · Company — no answer, no confidence given

<details><summary><b>News</b> — score n/a</summary>

- [NVO Nov 2026 43.000 call (NVO261106C00043000) Stock Price, News, Quote & History](https://ca.finance.yahoo.com/quote/NVO261106C00043000/)  
  <sub>Yahoo! Finance Canada, 16 hours ago</sub>  
  Find the latest NVO Nov 2026 43.000 call (NVO261106C00043000) stock quote, history, news and other vital information to help you with your stock trading and...
- [NVO Oct 2026 42.000 put (NVO261023P00042000) interactive stock chart](https://uk.finance.yahoo.com/quote/NVO261023P00042000/chart/)  
  <sub>Yahoo Finance UK, 14 hours ago</sub>  
  Interactive chart for NVO Oct 2026 42.000 put (NVO261023P00042000) – analyse all of the data with a huge range of indicators.
- [NVO Nov 2026 31.000 call (NVO261106C00031000) Stock Price, News, Quote & History](https://ca.finance.yahoo.com/quote/NVO261106C00031000/)  
  <sub>Yahoo! Finance Canada, 18 hours ago</sub>  
  Find the latest NVO Nov 2026 31.000 call (NVO261106C00031000) stock quote, history, news and other vital information to help you with your stock trading and...
- [Novo Nordisk’s CEO Was Asked Why His Stock Keeps Falling on Good News: ‘The Stock Market Is Always Right, but With a Bit of a Time Difference’](https://finance.yahoo.com/markets/stocks/articles/novo-nordisk-ceo-asked-why-153319353.html)  
  <sub>Yahoo Finance, 23 hours ago</sub>  
  Jim Cramer put the obvious question to Novo Nordisk's (NVO) chief executive: Why does the stock keep falling when the news keeps getting better?
- [AMCX, NWL Stocks Hit Fresh 52-Week Highs – Here’s What Wall Street Is Saying About ‘The Walking Dead’ Licensing Deal With Netflix](https://stocktwits.com/news-articles/markets/equity/amcx-nwl-stocks-hit-52-week-highs-the-walking-dead-licensing-deal-with-netflix/cZN4iWhRJPw)  
  <sub>Stocktwits, 7 hours ago</sub>  
  Analysts raised their price targets on AMCX stock, with Wells Fargo stating that the deal should provide additional cash flow and improve balance-sheet...
- [NVO Oct 2026 39.500 put (NVO261009P00039500) interactive stock chart – Yahoo Finance](https://sg.finance.yahoo.com/quote/NVO261009P00039500/chart/)  
  <sub>Yahoo Finance Singapore, 23 hours ago</sub>  
  Interactive chart for NVO Oct 2026 39.500 put (NVO261009P00039500) – analyse all of the data with a huge range of indicators.
- [SLS Stock In Spotlight After Vanguard Capital Discloses 5.19% Stake – Retail Calls It ‘Huge Vote Of Conviction’ As AML Trial Readout Nears](https://stocktwits.com/news-articles/markets/equity/sls-stock-in-spotlight-after-vanguard-capital-discloses-beneficial-stake/cZN4WEaRJPY)  
  <sub>Stocktwits, 12 hours ago</sub>  
  A new Schedule 13G filing showed Vanguard Capital Management owned 9.67 million SLS shares as of June 30, 2026.
- [SOFI Stock Got Hit With Price-Target Cuts After Q2 Earnings, But One Contrarian Says Market Is Missing Bigger Story](https://stocktwits.com/news-articles/markets/equity/sofi-stock-got-hit-with-price-target-cuts-after-q2-earnings-but-one-contrarian-says-market-is-missing-bigger-story/cZoRwebRJ5l)  
  <sub>Stocktwits, 22 hours ago</sub>  
  Shay Boloor, chief market strategist at Futrum Equities, said in a post on X that the market is overpricing credit risk and underpricing the platform even...
- [Novo Nordisk (NVO) Raised Its Outlook, Then Aimed for Average Growth](https://www.insidermonkey.com/news/novo-nordisk-nvo-raised-its-outlook-then-aimed-for-average-growth-1849934/)  
  <sub>Insider Monkey, 1 hour ago</sub>  
  Novo Nordisk (NYSE:NVO) did something this year that usually pleases investors: it raised its full-year outlook. The shares fell anyway, with investors...
- [Novo Nordisk (NYSE: NVO) Stock Price Closes Higher As Broader Markets Fall](https://www.foreignpolicyjournal.com/2026/10/08/novo-nordisk-nyse-nvo-stock-price-closes-higher-as-broader-markets-fall/)  
  <sub>Foreign Policy Journal, 21 hours ago</sub>  
  Novo Nordisk (NYSE: NVO) closed at $38.26 in the latest trading session, representing a gain of 1.95% against the prior day's closing price.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>Price and chart</b> — score n/a</summary>

```text
Last close 38.45 (bar of 2026-10-09), from 502 daily bars
Trend: vs 20d SMA 39.43 (-2.5%), 50d 43.43 (-11.5%), 200d 45.40 (-15.3%); 50d below 200d
Momentum: RSI(14) 36.4 | MACD -1.766 vs signal -1.945 (histogram 0.178)
Returns: 1d +0.7% | 5d +3.0% | 1m -12.6% | 3m -22.0%
52-week range: 35.29 - 63.98 (now 11.0% of the way up)
Volatility: ATR(14) 0.97 (2.5% of price) | annualised 20d 36.4%
Volume: 0.18x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score n/a</summary>

```text
Sector: Healthcare / Drug Manufacturers - General | market cap 169.73B
Valuation: trailing P/E 9.40 | forward P/E 11.56 | P/B 5.11 | PEG 4.32
Profitability: profit margin 35.3% | operating margin 42.5% | ROE 59.8%
Growth (YoY): revenue +2.1% | earnings -20.6%
Balance sheet: debt/equity 63.3% | free cash flow 37.67B
Risk: beta 0.38 | short interest 0.8% of float
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
Price target: mean 46.08 (+19.8% vs last close), range 39.77 - 61.83
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

### Teva Pharmaceutical (TEVA) · Company — no answer, no confidence given

<details><summary><b>News</b> — score n/a</summary>

- [Teva Pharmaceutical Industries Limited (TEVA) Stock Price, News, Quote & History](https://ca.finance.yahoo.com/quote/TEVA/)  
  <sub>Yahoo! Finance Canada, 13 hours ago</sub>  
  Teva Pharmaceutical Industries Limited (TEVA) · -0.15% · 6.77% · 28.60% · 25.76% · 94.21% · 286.32% · 4,231.03%. Key Events. Baseline. Advanced Chart. Loading...
- [Teva Announces U.S. Food and Drug Administration (FDA) Approval of WELTRUZA™ (Olanzapine) For Extended-Release Injectable Suspension, as the First and Only Once-Monthly Subcutaneous Injectable Olanzapine for Adults with Schizophrenia](https://ir.tevapharm.com/news-and-events/press-releases/press-release-details/2026/Teva-Announces-U-S--Food-and-Drug-Administration-FDA-Approval-of-WELTRUZA-Olanzapine-For-Extended-Release-Injectable-Suspension-as-the-First-and-Only-Once-Monthly-Subcutaneous-Injectable-Olanzapine-for-Adults-with-Schizophrenia/default.aspx)  
  <sub>Teva Pharmaceuticals, 4 hours ago</sub>  
  WELTRUZA ™ (olanzapine) for extended-release injectable suspension is the first and only once-monthly subcutaneous long-acting injectable (LAI) formulation...
- [FDA Approves Once-Monthly Subcutaneous Olanzapine for Schizophrenia](https://www.ajmc.com/view/fda-approves-once-monthly-subcutaneous-olanzapine-for-schizophrenia)  
  <sub>AJMC, 22 minutes ago</sub>  
  The FDA has approved olanzapine extended-release injectable suspension (Weltruza; Teva Pharmaceuticals), a once-monthly subcutaneous long-acting injectable...
- [Teva stock hits 52-week high at 40.84 USD By Investing.com](https://za.investing.com/news/stock-market-news/teva-stock-hits-52week-high-at-4084-usd-93CH-4497655)  
  <sub>Investing.com South Africa, 51 minutes ago</sub>  
  Teva Pharmaceutical Industries Ltd ADR has reached a significant milestone, with its stock hitting a 52-week high of $40.84. The stock currently trades at...
- [A monthly schizophrenia injection gets FDA approval without added pills or post-shot monitoring](https://www.stocktitan.net/news/TEVA/teva-announces-u-s-food-and-drug-administration-fda-approval-of-daxd43e6alhv.html)  
  <sub>Stock Titan, 4 hours ago</sub>  
  Teva (TEVA) has received FDA approval for WELTRUZA, a once-monthly subcutaneous olanzapine injection for treating schizophrenia in adults. Teva expects U.S....
- [Teva wins FDA approval for monthly schizophrenia injection Weltruza](https://www.cnbc.com/2026/10/09/teva-wins-fda-approval-for-monthly-schizophrenia-injection-weltruza.html)  
  <sub>CNBC, 1 hour ago</sub>  
  Teva has received FDA approval for once monthly injectable schizophrenia drug Weltruza. The announcement sent Teva shares gaining in premarket.
- [Teva Pharmaceutical Industries wins WELTRUZA approval](https://mugglehead.com/teva-pharmaceutical-industries-ltd-weltruza-fda-approval/)  
  <sub>Mugglehead Investment Magazine, 3 hours ago</sub>  
  FDA approved Teva's monthly WELTRUZA for adults with schizophrenia; three strengths are expected in the U.S. in the coming weeks.
- [Teva (TEVA) Gains FDA Approval for Weltruza, a Once-Monthly Schi](https://www.gurufocus.com/news/9117119/teva-teva-gains-fda-approval-for-weltruza-a-oncemonthly-schizophrenia-treatment)  
  <sub>GuruFocus, 3 hours ago</sub>  
  On October 09, 2026, Teva Pharmaceutical Industries Ltd (NYSE: TEVA) announced FDA approval for Weltruza, a new once-monthly injectable medication designed...
- [Simply Wall St raises fair value for Teva stock to USD 45.30](https://www.ad-hoc-news.de/boerse/news/corporate-news/simply-wall-st-raises-fair-value-for-teva-stock-to-usd-45-30/70277212)  
  <sub>AD HOC NEWS, 3 hours ago</sub>  
  Q2 revenue reached USD 4.14 billion, down 1.00 percent year over year. Teva stock last stood at USD 39.25 versus USD 40.79 high.
- [Teva (TEVA) Stock Fair Value Rises As Analysts Back CNS Transformation](https://finance.yahoo.com/healthcare/articles/teva-teva-stock-fair-value-011753525.html)  
  <sub>Yahoo Finance, 13 hours ago</sub>  
  Teva Pharmaceutical Industries is back in focus after a fair value estimate was lifted from US$42.00 to US$45.30, a move that puts fresh attention on how...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>Price and chart</b> — score n/a</summary>

```text
Last close 41.20 (bar of 2026-10-09), from 502 daily bars
Trend: vs 20d SMA 39.41 (+4.5%), 50d 37.62 (+9.5%), 200d 33.91 (+21.5%); 50d above 200d
Momentum: RSI(14) 65.7 | MACD 0.712 vs signal 0.739 (histogram -0.026)
Returns: 1d +5.0% | 5d +4.2% | 1m +13.3% | 3m +28.0%
52-week range: 18.95 - 41.20 (now 100.0% of the way up)
Volatility: ATR(14) 1.26 (3.1% of price) | annualised 20d 33.2%
Volume: 1.03x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score n/a</summary>

```text
Sector: Healthcare / Drug Manufacturers - Specialty & Generic | market cap 48.05B
Valuation: trailing P/E 68.67 | forward P/E 13.33 | P/B 6.19 | PEG n/a
Profitability: profit margin 4.1% | operating margin 4.0% | ROE 9.7%
Growth (YoY): revenue -0.8% | earnings n/a
Balance sheet: debt/equity 217.8% | free cash flow 2.22B
Risk: beta 0.82 | short interest 2.7% of float
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
Consensus: buy (mean 1.55 on a 1=strong buy to 5=strong sell scale, 10 analysts)
Ratings: 4 strong buy, 6 buy, 1 hold, 0 sell, 0 strong sell
Price target: mean 45.30 (+10.0% vs last close), range 40.00 - 55.00
Recent rating changes:
  - 2026-10-01 TD Cowen: init, ? -> Buy
  - 2026-09-23 Oppenheimer: init, ? -> Outperform
  - 2026-09-09 Leerink Partners: init, ? -> Outperform
  - 2026-09-04 UBS: main, Buy -> Buy
  - 2026-08-12 Barclays: main, Overweight -> Overweight
  - 2026-07-28 Piper Sandler: main, Overweight -> Overweight
Institutional ownership: 24.3%
Largest holders: Blackrock Inc. (5.5%), Harel Insurance Investments & Financial Services Ltd. (4.1%), Phoenix Financial Ltd. (3.7%), WCM Investment Management, LLC (3.5%), Clal Insurance Enterprises Holdings Ltd (3.5%)
```

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>Buying and selling by company insiders</b> — score n/a</summary>

```text
Last 180 days: bought 43,476 shares in 3 transaction(s) | sold 194,459 shares in 6
Net: -150,983 shares (-2.3% of insider holdings) | insiders hold 6,514,005 shares
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

- [ExxonMobil Holdings (XOM) Shares Climbed, What Is Behind The Move?](https://simplywall.st/stocks/us/energy/nyse-xom/exxonmobil-holdings/news/exxonmobil-holdings-xom-shares-climbed-what-is-behind-the-mo)  
  <sub>Simply Wall Street, 7 hours ago</sub>  
  A Gulf tanker attack and hurricane-related outages in the Gulf of Mexico squeezed oil supply, lifting crude prices and pushing ExxonMobil Holdings (XOM) up...
- [4 stocks to watch on Friday: DAL, SKYD, XOM, and IBM (SPX:)](https://seekingalpha.com/news/4651733-4-stocks-to-watch-on-friday-dal-skyd-xom-and-ibm)  
  <sub>Seeking Alpha, 2 hours ago</sub>  
  Stock index futures were higher on Friday as Wall Street looked to regain some momentum after the AI trade came under pressure on Thursday.
- [The 'Black Box' That Solves AI Fears, And The Stock Behind It](https://www.investors.com/research/the-new-america/xometry-ai-marketplace-black-box-solves-ai-fears-seizes-massive-market-opening/)  
  <sub>Investor's Business Daily, 3 hours ago</sub>  
  Xometry (XMTR) has the inside track to dominate one of the biggest remaining largely untapped online markets: the market for things that don't yet exist.
- [Fund Update: New $43.6M $XOM stock position opened by Farther Finance Advisors, LLC](https://www.quiverquant.com/news/Fund+Update%3A+New+%2443.6M+%24XOM+stock+position+opened+by+Farther+Finance+Advisors%2C+LLC)  
  <sub>Quiver Quantitative, 18 hours ago</sub>  
  Farther Finance Advisors, LLC has opened a new $43.6M position in $XOM, per a new SEC 13F filing. Th.
- [Why Are BATL, TPET, XOM, CVX, USO, UCO Stocks Rising Overnight?](https://stocktwits.com/news-articles/markets/equity/why-are-batl-tpet-xom-cvx-uso-uco-stocks-rising-overnight/cZZLqW1R7Mp)  
  <sub>Stocktwits, 13 hours ago</sub>  
  As a result, oil companies Battalion Oil Corp. (BATL) and Trio Petroleum Corp. (TPET) rose more than 7% and by over 8% in the overnight session. Oil majors...
- [XOM Oct 2026 175.000 call (XOM261009C00175000) stock price, news, quote and history](https://uk.finance.yahoo.com/quote/XOM261009C00175000/)  
  <sub>Yahoo Finance UK, 7 hours ago</sub>  
  Find the latest XOM Oct 2026 175.000 call (XOM261009C00175000) stock quote, history, news and other vital information to help you with your stock trading...
- [ExxonMobil (XOM) Blocks $5B Environmental Fine Settlement Amid K](https://www.gurufocus.com/news/9117124/exxonmobil-xom-blocks-5b-environmental-fine-settlement-amid-kashagan-expansion-talks)  
  <sub>GuruFocus, 3 hours ago</sub>  
  On October 09, 2026, ExxonMobil (XOM) successfully prevented a proposal by its partners to settle a $5 billion environmental fine with the Kazakh government...
- [ExxonMobil (NYSE:XOM) Shares Up 2.7% - What's Next?](https://www.marketbeat.com/instant-alerts/price-exxonmobil-nyse-xom-shares-up-27-whats-next-2026-10-08/)  
  <sub>MarketBeat, 17 hours ago</sub>  
  ExxonMobil (NYSE:XOM) Stock Price Up 2.7% - Here's Why.
- [Exxon Mobil Corp Stock (XOM) Moved Up by 3.07% on Oct 8: What Investors Need To Know](https://www.tradingkey.com/news/market-movers/262206915-market-movers-xom-20261008)  
  <sub>TradingKey, 20 hours ago</sub>  
  Rising global crude prices and geopolitical risks drove Exxon Mobil upward momentum.Strategic expansions in Trinidad, Permian Basin, and Guyana bolstered...
- [What's Going On With ExxonMobil Stock On Thursday?](https://www.benzinga.com/markets/large-cap/26/10/62253597/whats-going-on-with-exxonmobil-stock-on-thursday)  
  <sub>Benzinga, 22 hours ago</sub>  
  ExxonMobil Holdings (NYSE:XOM) shares are trading about 2% higher on Thursday as traders react to the Trump administration's planned rollback of Biden-era...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>Price and chart</b> — score n/a</summary>

```text
Last close 169.45 (bar of 2026-10-09), from 502 daily bars
Trend: vs 20d SMA 163.52 (+3.6%), 50d 161.58 (+4.9%), 200d 150.33 (+12.7%); 50d above 200d
Momentum: RSI(14) 65.0 | MACD 1.556 vs signal 1.022 (histogram 0.534)
Returns: 1d +0.6% | 5d +3.3% | 1m +2.6% | 3m +17.3%
52-week range: 110.64 - 171.47 (now 96.7% of the way up)
Volatility: ATR(14) 3.48 (2.1% of price) | annualised 20d 24.2%
Volume: 0.11x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score n/a</summary>

```text
Sector: Energy / Oil & Gas Integrated | market cap 696.76B
Valuation: trailing P/E 21.81 | forward P/E 14.88 | P/B 2.69 | PEG 1.38
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
Price target: mean 173.64 (+2.5% vs last close), range 142.00 - 200.00
Recent rating changes:
  - 2026-10-01 Wells Fargo: down, Overweight -> Equal-Weight
  - 2026-09-28 TD Cowen: main, Buy -> Buy
  - 2026-09-03 Piper Sandler: main, Neutral -> Neutral
  - 2026-08-19 Morgan Stanley: main, Overweight -> Overweight
  - 2026-08-17 Barclays: main, Overweight -> Overweight
  - 2026-08-07 TD Cowen: main, Buy -> Buy
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

> Neutral overall – no macro surprise, flat fund flows, mixed technicals, and no analyst coverage.

**Main reasons it gave:**
- Flat fund flows (0% change) indicating no demand shift
- Price above 200‑day SMA (+4.6%) but RSI near 50 (49.5) and MACD slightly bearish
- Macro data stable: inflation 3.4% and Fed target unchanged at 4.0%
- No analyst rating coverage (no rating reported for holdings)

<details><summary><b>News</b> — score +0.00</summary>

_No news found for this one today._

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.06% (+0.06 on the week) | 5-year 5.04% (-0.02 on the week) | 10-year 5.27% (-0.00 on the week) | 30-year 5.64% (+0.01 on the week)
Yield curve, 10-year minus 3-month: +1.22 points -- upward sloping (normal)
US dollar index: 102.26 (+0.33 on the week)
Volatility (VIX): 15.01 (-0.3 on the week) -- elevated
Latest US data: inflation 3.4% (2026-08-01) | unemployment 4.2% (2026-09-01) | jobless claims 197k (2026-10-03)
Policy and expectations: Fed target 4.00% | market expects 2.4% inflation over 10 years
Rate path: 2-year Treasury 4.77% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 28.46 (bar of 2026-10-09), from 502 daily bars
Trend: vs 20d SMA 28.48 (-0.1%), 50d 28.41 (+0.2%), 200d 27.20 (+4.6%); 50d above 200d
Momentum: RSI(14) 49.5 | MACD -0.032 vs signal -0.023 (histogram -0.009)
Returns: 1d +0.4% | 5d +0.9% | 1m -2.9% | 3m +2.7%
52-week range: 25.44 - 29.49 (now 74.6% of the way up)
Volatility: ATR(14) 0.28 (1.0% of price) | annualised 20d 12.9%
Volume: 0.17x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.30</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score +0.30</summary>

```text
Fund type: Commodities Focused
What it holds: P/E n/a | P/B 0.00 | P/S 0.00 | 3y earnings growth n/a
Yield: 3.2%
Three-year record: +14.7% a year | beta to the market 0.35
Cost and size: expense ratio 0.85% | net assets 1.36B
What it is made of: Other 51.0%, Cash 47.0%, Bonds 2.0%
Largest holdings: Invesco Shrt-Trm Inv Gov&Agcy Instl 42.3%, Invesco Short Term Treasury ETF 4.6%
Sector mix: Healthcare 16.8%, Industrials 15.2%, Financial services 13.7%, Consumer cyclical 11.8%
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
Direction: flat (1 week)
Share count change: 1 week: +0.0% (0.00) over 7d
Shares outstanding: 27.60M | fund size: 785.50M
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Commodities basket (DBC) · Index fund — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Mixed signals: positive fund inflows, bearish price outlook, mixed inventory data, and technicals near a 52‑week high with low volume. No macro surprise or decisive technical break.

**Main reasons it gave:**
- Fund flows: +5.1% share count increase over the week (net inflow)
- EIA price outlook: WTI forecast down 14% and natural gas down 18% over six months (bearish)
- Energy inventories: crude draw of 3.2 MMbbl (bullish) and natural‑gas build of 85 Bcf (bearish)
- Technicals: price near 52‑week high, low volume, no decisive break (limited momentum)

<details><summary><b>News</b> — score +0.00</summary>

- [Think 5% Treasury Yields Are Scary? This CEO Expects 8% - iShares TIPS Bond ETF (ARCA:TIP)](https://www.benzinga.com/etfs/sector-etfs/26/10/62269770/exclusive-think-5-treasury-yields-are-scary-this-ceo-says-8-is-coming)  
  <sub>Benzinga, 2 hours ago</sub>  
  Canary Capital CEO Steven McClurg sees 10-year Treasury yields hitting 8% within four years. TIPS and commodity ETFs could gain attention.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.06% (+0.06 on the week) | 5-year 5.04% (-0.02 on the week) | 10-year 5.27% (-0.00 on the week) | 30-year 5.64% (+0.01 on the week)
Yield curve, 10-year minus 3-month: +1.22 points -- upward sloping (normal)
US dollar index: 102.26 (+0.33 on the week)
Volatility (VIX): 15.01 (-0.3 on the week) -- elevated
Latest US data: inflation 3.4% (2026-08-01) | unemployment 4.2% (2026-09-01) | jobless claims 197k (2026-10-03)
Policy and expectations: Fed target 4.00% | market expects 2.4% inflation over 10 years
Rate path: 2-year Treasury 4.77% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 33.07 (bar of 2026-10-09), from 502 daily bars
Trend: vs 20d SMA 32.77 (+0.9%), 50d 31.54 (+4.9%), 200d 28.42 (+16.4%); 50d above 200d
Momentum: RSI(14) 59.0 | MACD 0.287 vs signal 0.353 (histogram -0.066)
Returns: 1d +0.5% | 5d +1.6% | 1m -1.6% | 3m +16.7%
52-week range: 22.07 - 33.68 (now 94.7% of the way up)
Volatility: ATR(14) 0.50 (1.5% of price) | annualised 20d 16.6%
Volume: 0.11x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score -0.40</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score -0.40</summary>

```text
Fund type: Commodities Broad Basket
What it holds: P/E n/a | P/B 0.00 | P/S 0.00 | 3y earnings growth n/a
Yield: 2.3%
Three-year record: +16.0% a year | beta to the market 1.05
Cost and size: expense ratio 0.85% | net assets 1.92B
What it is made of: Other 50.4%, Cash 45.1%, Bonds 2.5%, Stocks 2.0%
Largest holdings: Invesco Shrt-Trm Inv Gov&Agcy Instl 41.5%, Brent Crude Future Dec 26 9.7%, Invesco Short Term Treasury ETF 5.8%, Mini Ibovespa Future Dec 26 2.0%
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
US inventories, week ending 2026-10-02 (published the following Wednesday)
  Crude oil: 424.1 million barrels, -3.2 on the week (a draw), 40% percentile over 52 weeks
  Natural gas: 3,500.0 billion cubic feet, +85.0 on the week (a build), 81% percentile over 52 weeks
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
Direction: money coming in (1 week)
Share count change: 1 week: +5.1% (95.36M) over 7d
Shares outstanding: 59.02M | fund size: 1.95B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Developing country bonds (EMB) · Index fund — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Neutral call based on lack of macro surprise, bearish technicals without decisive break, and large outflows indicating negative sentiment but not a clear macro catalyst.

**Main reasons it gave:**
- Share count down 12.8% over 1 week (large outflows)
- Price below 20‑day, 50‑day, and 200‑day SMAs (bearish trend)
- RSI 33.8 (low momentum)
- Fed target unchanged at 4.00% and inflation 3.4% in line with expectations (no macro surprise)

<details><summary><b>News</b> — score +0.00</summary>

- [NVIT Investor Destinations Capital Appreciation Fund EMB Holdings History](https://www.gurufocus.com/guru-portfolio/NVIT%20Investor%20Destinations%20Capital%20Appreciation%20Fund/EMB)  
  <sub>GuruFocus, 24 hours ago</sub>  
  iShares J.P. Morgan USD Emerging Markets Bond ETF(EMB) Buys and Sells Made by NVIT Investor Destinations Capital Appreciation Fund.
- [EDD: Diversify Your Currency Risk While Getting A High Yield (NYSE:EDD)](https://seekingalpha.com/article/4952819-edd-diversify-your-currency-risk-while-getting-a-high-yield)  
  <sub>Seeking Alpha, 23 hours ago</sub>  
  The Morgan Stanley Emerging Markets Domestic Debt Fund offers a high 15.76% yield by investing in local-currency emerging market bonds.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.06% (+0.06 on the week) | 5-year 5.04% (-0.02 on the week) | 10-year 5.27% (-0.00 on the week) | 30-year 5.64% (+0.01 on the week)
Yield curve, 10-year minus 3-month: +1.22 points -- upward sloping (normal)
US dollar index: 102.26 (+0.33 on the week)
Volatility (VIX): 15.01 (-0.3 on the week) -- elevated
Latest US data: inflation 3.4% (2026-08-01) | unemployment 4.2% (2026-09-01) | jobless claims 197k (2026-10-03)
Policy and expectations: Fed target 4.00% | market expects 2.4% inflation over 10 years
Rate path: 2-year Treasury 4.77% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score -0.40</summary>

```text
Last close 90.95 (bar of 2026-10-09), from 502 daily bars
Trend: vs 20d SMA 91.93 (-1.1%), 50d 93.61 (-2.8%), 200d 95.31 (-4.6%); 50d below 200d
Momentum: RSI(14) 33.8 | MACD -0.917 vs signal -0.904 (histogram -0.013)
Returns: 1d -0.0% | 5d +0.9% | 1m -2.6% | 3m -4.6%
52-week range: 90.14 - 97.74 (now 10.7% of the way up)
Volatility: ATR(14) 0.55 (0.6% of price) | annualised 20d 7.3%
Volume: 0.27x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.20</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score +0.20</summary>

```text
Fund type: Emerging Markets Bond
Yield: 5.4%
Credit quality: BBB 33.9%, BB 25.2%, B 19.3%, A 17.6% | US government debt 88.0%
Three-year record: +9.7% a year | beta to the market 1.10
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

<details><summary><b>Buying and selling by company insiders</b> — score -0.60</summary>

_Not available today._

</details>

<details><summary><b>Who is positioned how</b> — score -0.60</summary>

_Not available today._

</details>

<details><summary><b>Money going into and out of this fund</b> — score -0.60</summary>

```text
Direction: money going out (1 week)
Share count change: 1 week: -12.8% (-1.91B) over 7d
Shares outstanding: 142.42M | fund size: 12.95B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### US small companies (IWM) · Index fund — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> No macro surprise, no decisive technical break, and mixed but modest signals from fundamentals, analyst coverage, and positioning.

**Main reasons it gave:**
- Inflation 3.4% and unemployment 4.2% in line with expectations, no macro surprise
- Technical: price below 20‑day SMA, RSI 36.2, volume 0.2× 20‑day avg, no decisive breakout
- CFTC net short 26.8% of open interest, change -0.7% week, crowded short at 3% percentile
- Analyst coverage only 2% of fund, 100% buy rating, weighted price target +1.9% above current

<details><summary><b>News</b> — score +0.00</summary>

- [Should Invesco S&P SmallCap 600 Revenue ETF (RWJ) Be on Your Investing Radar?](https://finance.yahoo.com/markets/stocks/articles/invesco-p-smallcap-600-revenue-092002324.html)  
  <sub>Yahoo Finance, 5 hours ago</sub>  
  Launched on February 22, 2008, the Invesco S&P SmallCap 600 Revenue ETF (RWJ) is a passively managed exchange traded fund designed to provide a broad...
- [Flow Focus | OpenAI Cracks, Oil Breaks $100(Again): Where Is the Smart Money Going?](https://www.moomoo.com/community/feed/flow-focus-openai-cracks-oil-breaks-100-again-where-is-117409856749574)  
  <sub>Moomoo, 7 hours ago</sub>  
  Oil ripped nearly five percent higher, $Brent Last Day Financial Futures (DEC6) (BZmain.US)$ reclaimed $100, and Energy led the market. Utilities and ...
- [Stock Market Today: S&P 500 Slips as Oil Spikes 5%, 10-Year Yields Near 5.35%](https://www.tradingview.com/news/benzinga:483f8f015094b:0-stock-market-today-s-p-500-slips-as-oil-spikes-5-10-year-yields-near-5-35/)  
  <sub>TradingView, 21 hours ago</sub>  
  U.S. stocks slipped by midday Thursday as oil surged more than 5% on fresh Persian Gulf tanker attacks, while Treasury yields climbed back toward their...
- [Exchange-Traded Funds Drop as US Equities Fall After Midday](https://finance.yahoo.com/markets/articles/exchange-traded-funds-drop-us-171415436.html)  
  <sub>Yahoo Finance, 22 hours ago</sub>  
  Broad Market Indicators Broad-market exchange-traded funds IWM and IVV were lower. Actively traded Invesco QQQ Trust (QQQ) eased 1%.
- [Invesco S&P 500 Equal Weight ETF (RSP) Stock Price, News, Quote & History](https://ca.finance.yahoo.com/quote/RSP/)  
  <sub>Yahoo! Finance Canada, 23 hours ago</sub>  
  Find the latest Invesco S&P 500 Equal Weight ETF (RSP) stock quote, history, news and other vital information to help you with your stock trading and...
- [Tech Feels the Pinch from OpenAI, But Broader Market Finds Support | Options Market Statistics](https://www.moomoo.com/community/feed/tech-feels-the-pinch-from-openai-but-broader-market-finds-117410896609286?chain_id=Name1K9-3FXPhg.1lchlq0&global_content=%7B%22promote_id%22%3A13764%2C%22sub_promote_id%22%3A57%2C%22f%22%3A%22www.moomoo.com%2Fstock%2FRIOT-US%2Fcommunity%22%7D)  
  <sub>Moomoo, 3 hours ago</sub>  
  By Luke Wu | Oct 9, 2026 Key Takeaways - Broader vol continues falling into the week end; vol-control provides steady demand Broader volatility kept d...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.06% (+0.06 on the week) | 5-year 5.04% (-0.02 on the week) | 10-year 5.27% (-0.00 on the week) | 30-year 5.64% (+0.01 on the week)
Yield curve, 10-year minus 3-month: +1.22 points -- upward sloping (normal)
US dollar index: 102.26 (+0.33 on the week)
Volatility (VIX): 15.01 (-0.3 on the week) -- elevated
Latest US data: inflation 3.4% (2026-08-01) | unemployment 4.2% (2026-09-01) | jobless claims 197k (2026-10-03)
Policy and expectations: Fed target 4.00% | market expects 2.4% inflation over 10 years
Rate path: 2-year Treasury 4.77% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 278.06 (bar of 2026-10-09), from 502 daily bars
Trend: vs 20d SMA 282.02 (-1.4%), 50d 291.37 (-4.6%), 200d 277.06 (+0.4%); 50d above 200d
Momentum: RSI(14) 36.2 | MACD -3.536 vs signal -3.609 (histogram 0.073)
Returns: 1d +0.2% | 5d -1.2% | 1m -3.4% | 3m -5.3%
52-week range: 229.11 - 305.09 (now 64.4% of the way up)
Volatility: ATR(14) 3.55 (1.3% of price) | annualised 20d 11.2%
Volume: 0.20x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score -0.10</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score -0.10</summary>

```text
Fund type: Small Blend
What it holds: P/E 16.35 | P/B 2.02 | P/S 1.25 | 3y earnings growth n/a
Yield: 1.0%
Three-year record: +18.9% a year | beta to the market 1.27
Cost and size: expense ratio 0.19% | net assets 78.04B
What it is made of: Stocks 99.7%, Cash 0.3%
Largest holdings: BlackRock Cash Funds Treasury SL Agency 0.5%, Twist Bioscience Corp 0.4%, Moog Inc Class A 0.4%, JFrog Ltd Ordinary Shares 0.4%, 10x Genomics Inc Ordinary Shares - Class A 0.4%
Sector mix: Healthcare 20.9%, Financial services 18.0%, Technology 14.5%, Industrials 13.3%
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
Rolled up from the 5 largest holdings, 2.0% of the fund by weight  -- thin, so read this as a fact about that slice rather than the fund
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 2.05 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +1.9% above the current prices
Holdings read: XTSLA, TWST, MOG-A, FROG, TXG
Recent rating changes among them:
  - TWST: 2026-10-08 Jefferies: init, ? -> Hold
  - MOG-A: 2026-09-15 Guggenheim: init, ? -> Neutral
  - FROG: 2026-09-04 DA Davidson: main, Buy -> Buy
  - TXG: 2026-10-07 Barclays: main, Overweight -> Overweight
```

</details>

<details><summary><b>Buying and selling by company insiders</b> — score -0.30</summary>

_Not available today._

</details>

<details><summary><b>Who is positioned how</b> — score -0.30</summary>

```text
Contract: RUSSELL E-MINI - CHICAGO MERCANTILE EXCHANGE (positions as of 2026-09-29, published the following Friday)
Large speculators: net short 26.8% of open interest (428,048 contracts)
Change on the week: -0.7% of open interest
Crowding: 3% percentile over 52 weeks -- a crowded short by the standards of the past year
Read this as crowding, not as a forecast: an extreme is as often the end of a move as the middle of one.
```

</details>

<details><summary><b>Money going into and out of this fund</b> — score -0.30</summary>

```text
Direction: flat (1 week)
Share count change: 1 week: +0.0% (0.00) over 7d
Shares outstanding: 281.05M | fund size: 78.15B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### US company bonds, safer (LQD) · Index fund — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Most macro and technical indicators are unchanged; no policy surprise or decisive technical break. Large outflows suggest bearish sentiment but not a macro catalyst.

**Main reasons it gave:**
- Fund outflows of -11.5% share count (-$3.69B) over 1 week
- Price below 20‑day, 50‑day, and 200‑day SMAs; RSI 32.8 indicating oversold
- No macro surprise: yields stable, no policy shift
- Low volume (0.24× 20‑day average) suggests limited conviction

<details><summary><b>News</b> — score +0.00</summary>

- [Daily ETF Flows: EWZ Keeps Gathering Assets](https://www.etf.com/sections/daily-etf-flows/daily-etf-flows-ewz-keeps-gathering-assets)  
  <sub>ETF.com, 22 hours ago</sub>  
  Here are the daily ETF fund flows for October 8, 2026.
- [U.S. ETF Express | Direxion Daily Semiconductor Bear 3x Shares ETF Was the Top Gainer, Rising 10.24%](https://www.moomoo.com/news/post/1000788320/us-etf-express-direxion-daily-semiconductor-bear-3x-shares-etf)  
  <sub>Moomoo, 17 hours ago</sub>  
  TopGainers/Losers2638 U.S. ETFs rose and 3496 fell today.The top gainer was $Direxion Daily Semiconductor Bear 3x Shares ETF(SOXS.US)$, climbing 10.24% to...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.06% (+0.06 on the week) | 5-year 5.04% (-0.02 on the week) | 10-year 5.27% (-0.00 on the week) | 30-year 5.64% (+0.01 on the week)
Yield curve, 10-year minus 3-month: +1.22 points -- upward sloping (normal)
US dollar index: 102.26 (+0.33 on the week)
Volatility (VIX): 15.01 (-0.3 on the week) -- elevated
Latest US data: inflation 3.4% (2026-08-01) | unemployment 4.2% (2026-09-01) | jobless claims 197k (2026-10-03)
Policy and expectations: Fed target 4.00% | market expects 2.4% inflation over 10 years
Rate path: 2-year Treasury 4.77% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score -0.20</summary>

```text
Last close 102.26 (bar of 2026-10-09), from 502 daily bars
Trend: vs 20d SMA 103.25 (-1.0%), 50d 104.90 (-2.5%), 200d 108.21 (-5.5%); 50d below 200d
Momentum: RSI(14) 32.8 | MACD -0.889 vs signal -0.892 (histogram 0.003)
Returns: 1d -0.2% | 5d +0.4% | 1m -2.0% | 3m -4.4%
52-week range: 101.83 - 112.92 (now 3.9% of the way up)
Volatility: ATR(14) 0.61 (0.6% of price) | annualised 20d 6.6%
Volume: 0.24x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.00</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score +0.00</summary>

```text
Fund type: Corporate Bond
Yield: 4.9%
Credit quality: A 46.6%, BBB 40.2%, AA 12.3%, AAA 1.0%
Three-year record: +5.3% a year | beta to the market 1.35
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

<details><summary><b>Buying and selling by company insiders</b> — score -0.50</summary>

_Not available today._

</details>

<details><summary><b>Who is positioned how</b> — score -0.50</summary>

_Not available today._

</details>

<details><summary><b>Money going into and out of this fund</b> — score -0.50</summary>

```text
Direction: money going out (1 week)
Share count change: 1 week: -11.5% (-3.69B) over 7d
Shares outstanding: 277.00M | fund size: 28.33B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### S&P 500, equal weight (RSP) · Index fund — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> No material macro surprise, mixed technicals, modest bearish positioning, outflows, thin analyst coverage.

**Main reasons it gave:**
- Macro data unchanged: Treasury yields stable, VIX down 0.3, inflation 3.4% near expectations
- Technical indicators mixed: price above 200‑day SMA but below 50‑day SMA, RSI neutral, low volume
- CFTC positioning net short 19.6% with only +0.2% change, indicating slight bearish bias but minimal shift
- Fund flows show 6% share count decline over the week, indicating outflows
- Analyst coverage thin (1.4% of fund) with 78.5% buy rating, yielding modest bullish score

<details><summary><b>News</b> — score +0.00</summary>

- [Invesco S&P 500 Equal Weight ETF (RSP) Stock Price, News, Quote & History](https://ca.finance.yahoo.com/quote/RSP/)  
  <sub>Yahoo! Finance Canada, 23 hours ago</sub>  
  Invesco S&P 500 Equal Weight ETF (RSP) · 1.34% · -2.27% · 6.99% · 9.62% · 10.91% · 38.34% · 738.81%. Key Events. Baseline. Advanced Chart. Loading...
- [AI Bubble Nearing a Breaking Point? Ray Dalio’s Warning Reveals a Risk Hiding in These ETFs](https://www.tradingview.com/news/benzinga:6f2c587d9094b:0-ai-bubble-nearing-a-breaking-point-ray-dalio-s-warning-reveals-a-risk-hiding-in-these-etfs/)  
  <sub>TradingView, 22 hours ago</sub>  
  ETF investors may be carrying far more exposure to the artificial intelligence trade than they realize. Some of the biggest funds are heavily concentrated...
- [Equal-Weight ETFs to Play AI Despite Rising Bubble Concerns](https://www.tradingview.com/news/zacks:f62071eef094b:0-equal-weight-etfs-to-play-ai-despite-rising-bubble-concerns/)  
  <sub>TradingView, 24 hours ago</sub>  
  Investor optimism surrounding artificial intelligence has been one of the primary catalysts behind the market's resilience so far this year despite...
- [Daily ETF Flows: EWZ Keeps Gathering Assets](https://www.etf.com/sections/daily-etf-flows/daily-etf-flows-ewz-keeps-gathering-assets)  
  <sub>ETF.com, 22 hours ago</sub>  
  Here are the daily ETF fund flows for October 8, 2026.
- [Should Invesco S&P SmallCap 600 Revenue ETF (RWJ) Be on Your Investing Radar?](https://finance.yahoo.com/markets/stocks/articles/invesco-p-smallcap-600-revenue-092002324.html)  
  <sub>Yahoo Finance, 5 hours ago</sub>  
  Launched on February 22, 2008, the Invesco S&P SmallCap 600 Revenue ETF (RWJ) is a passively managed exchange traded fund designed to provide a broad...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.06% (+0.06 on the week) | 5-year 5.04% (-0.02 on the week) | 10-year 5.27% (-0.00 on the week) | 30-year 5.64% (+0.01 on the week)
Yield curve, 10-year minus 3-month: +1.22 points -- upward sloping (normal)
US dollar index: 102.26 (+0.33 on the week)
Volatility (VIX): 15.01 (-0.3 on the week) -- elevated
Latest US data: inflation 3.4% (2026-08-01) | unemployment 4.2% (2026-09-01) | jobless claims 197k (2026-10-03)
Policy and expectations: Fed target 4.00% | market expects 2.4% inflation over 10 years
Rate path: 2-year Treasury 4.77% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 212.43 (bar of 2026-10-09), from 502 daily bars
Trend: vs 20d SMA 211.47 (+0.5%), 50d 216.28 (-1.8%), 200d 206.22 (+3.0%); 50d above 200d
Momentum: RSI(14) 48.9 | MACD -1.311 vs signal -1.741 (histogram 0.430)
Returns: 1d +0.3% | 5d +1.3% | 1m -0.3% | 3m -0.8%
52-week range: 182.18 - 222.77 (now 74.5% of the way up)
Volatility: ATR(14) 1.86 (0.9% of price) | annualised 20d 8.4%
Volume: 0.31x the 20-day average
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
Three-year record: +16.8% a year | beta to the market 0.84
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

<details><summary><b>What analysts and big funds say</b> — score +0.20</summary>

_Not available today._

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score +0.20</summary>

```text
Rolled up from the 5 largest holdings, 1.4% of the fund by weight  -- thin, so read this as a fact about that slice rather than the fund
Ratings by weight: buy 78.5% | hold 21.5% | sell 0.0% (mean 2.19 on a 1=strong buy to 5=strong sell scale)
Weighted price target: -16.5% above the current prices
Holdings read: MRNA, P, ILMN, CRWD, RVTY
Recent rating changes among them:
  - MRNA: 2026-10-07 Morgan Stanley: main, Equal-Weight -> Equal-Weight
  - P: 2026-10-08 Needham: main, Buy -> Buy
  - ILMN: 2026-10-07 Barclays: main, Underweight -> Underweight
  - CRWD: 2026-10-09 Needham: main, Buy -> Buy
  - RVTY: 2026-10-07 Barclays: main, Equal-Weight -> Equal-Weight
```

</details>

<details><summary><b>Buying and selling by company insiders</b> — score -0.15</summary>

_Not available today._

</details>

<details><summary><b>Who is positioned how</b> — score -0.15</summary>

```text
Contract: E-MINI S&P 500 - CHICAGO MERCANTILE EXCHANGE (positions as of 2026-09-29, published the following Friday)
Large speculators: net short 19.6% of open interest (1,895,922 contracts)
Change on the week: +0.2% of open interest
Crowding: 55% percentile over 52 weeks -- within its normal range
Read this as crowding, not as a forecast: an extreme is as often the end of a move as the middle of one.
```

</details>

<details><summary><b>Money going into and out of this fund</b> — score -0.15</summary>

```text
Direction: money going out (1 week)
Share count change: 1 week: -6.0% (-6.17B) over 7d
Shares outstanding: 452.49M | fund size: 96.12B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### US government bonds, 1-3 years (SHY) · Index fund — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> No clear macro surprise, no decisive technical break, and mixed behavioural signals. Positioning shows a modest bearish tilt (net short 2‑yr note), but fund flows are positive and fundamentals are solid. Overall the evidence points to a neutral stance.

**Main reasons it gave:**
- CFTC data: large speculators net short 25.7% of 2‑year note, up 4% week (crowded short position)
- Fund flows: share count up 1.5% over the week, indicating new money into SHY
- Fund basics: AA credit quality, 3.6% yield, low expense ratio 0.15%, stable 3‑year return
- Technicals: price below 50‑day and 200‑day SMA, RSI 41.4 (slightly bearish)
- Macro: Treasury yields stable this week, no rate surprise; market pricing ~4 hikes over next 2 years

<details><summary><b>News</b> — score +0.00</summary>

- [How To Position In A High Interest Rate Environment (NYSEARCA:EDV)](https://seekingalpha.com/article/4953028-how-to-position-in-a-high-interest-rate-environment)  
  <sub>Seeking Alpha, 2 hours ago</sub>  
  Vanguard Extended Duration ETF remains a high-risk play as rising yields and intensified capital competition threaten further downside.
- [What Did 197,000 Jobless Claims Say for SHY (NASDAQ:SHY)?](https://kalkine.ca/news/daily-wrap/what-did-197000-jobless-claims-say-for-shy-nasdaqshy-1)  
  <sub>kalkine.ca, 2 hours ago</sub>  
  You are reading a free article with opinions that may differ from the recommendation given by Kalkine in its paid research reports.
- [Maklakova / Mamedova vs Chang / Shymanovich](https://www.coinbase.com/predictions/event/KXITFWDOUBLES-26OCT08MAKMAMCHASHY?marketTicker=KXITFWDOUBLES-26OCT08MAKMAMCHASHY-MAKMAM-KALSHI)  
  <sub>Coinbase, 15 hours ago</sub>  
  If Chang / Shymanovich wins the Maklakova / Mamedova vs Chang / Shymanovich professional tennis match in the 2026 W35 Las Vegas NV Quarterfinal after a ball...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.06% (+0.06 on the week) | 5-year 5.04% (-0.02 on the week) | 10-year 5.27% (-0.00 on the week) | 30-year 5.64% (+0.01 on the week)
Yield curve, 10-year minus 3-month: +1.22 points -- upward sloping (normal)
US dollar index: 102.26 (+0.33 on the week)
Volatility (VIX): 15.01 (-0.3 on the week) -- elevated
Latest US data: inflation 3.4% (2026-08-01) | unemployment 4.2% (2026-09-01) | jobless claims 197k (2026-10-03)
Policy and expectations: Fed target 4.00% | market expects 2.4% inflation over 10 years
Rate path: 2-year Treasury 4.77% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score -0.10</summary>

```text
Last close 81.18 (bar of 2026-10-09), from 502 daily bars
Trend: vs 20d SMA 81.19 (-0.0%), 50d 81.59 (-0.5%), 200d 82.22 (-1.3%); 50d below 200d
Momentum: RSI(14) 41.4 | MACD -0.128 vs signal -0.154 (histogram 0.027)
Returns: 1d -0.0% | 5d +0.2% | 1m -0.3% | 3m -0.8%
52-week range: 81.05 - 83.18 (now 5.9% of the way up)
Volatility: ATR(14) 0.11 (0.1% of price) | annualised 20d 1.6%
Volume: 0.12x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.30</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score +0.30</summary>

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

<details><summary><b>Buying and selling by company insiders</b> — score -0.40</summary>

_Not available today._

</details>

<details><summary><b>Who is positioned how</b> — score -0.40</summary>

```text
Contract: UST 2Y NOTE - CHICAGO BOARD OF TRADE (positions as of 2026-09-29, published the following Friday)
Large speculators: net short 25.7% of open interest (4,530,145 contracts)
Change on the week: +4.0% of open interest
Crowding: 100% percentile over 52 weeks -- a crowded long by the standards of the past year
Read this as crowding, not as a forecast: an extreme is as often the end of a move as the middle of one.
```

</details>

<details><summary><b>Money going into and out of this fund</b> — score -0.40</summary>

```text
Direction: money coming in (1 week)
Share count change: 1 week: +1.5% (385.12M) over 7d
Shares outstanding: 324.03M | fund size: 26.30B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Europe (VGK) · Index fund — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Neutral overall as no material macro surprise, no decisive technical break, and mixed signals from analyst coverage (positive), positioning (net long reduced), and fund flows (outflows).

**Main reasons it gave:**
- Analyst coverage: 65.7% buy, weighted price target +14.1% above current price
- CFTC positioning: net long reduced by 3.7% week over week
- Fund flows: share count down 3.4% over the past week
- Technicals: price below 20‑day SMA, RSI 34.9 indicating oversold conditions

<details><summary><b>News</b> — score +0.00</summary>

- [Trump's top August holdings fall short of bullish Quant ratings (VGK:NYSEARCA)](https://seekingalpha.com/news/4651483-trumps-top-august-holdings-fall-short-of-bullish-quant-ratings)  
  <sub>Seeking Alpha, 22 hours ago</sub>  
  U.S. President Donald Trump executed 517 securities trades in August totaling between $74.3M and $273M, with the activity led by portfolio reallocations...
- [Trump's top August holdings fall short of bullish Quant ratings](https://www.tradingview.com/news/seekingalpha:54153fa2f094b:0-trump-s-top-august-holdings-fall-short-of-bullish-quant-ratings/)  
  <sub>TradingView, 22 hours ago</sub>  
  U.S. President Donald Trump executed 517 securities trades in August totaling between $74.3M and $273M, with the activity led by portfolio reallocations...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.06% (+0.06 on the week) | 5-year 5.04% (-0.02 on the week) | 10-year 5.27% (-0.00 on the week) | 30-year 5.64% (+0.01 on the week)
Yield curve, 10-year minus 3-month: +1.22 points -- upward sloping (normal)
US dollar index: 102.26 (+0.33 on the week)
Volatility (VIX): 15.01 (-0.3 on the week) -- elevated
Latest US data: inflation 3.4% (2026-08-01) | unemployment 4.2% (2026-09-01) | jobless claims 197k (2026-10-03)
Policy and expectations: Fed target 4.00% | market expects 2.4% inflation over 10 years
Rate path: 2-year Treasury 4.77% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score -0.10</summary>

```text
Last close 85.75 (bar of 2026-10-09), from 502 daily bars
Trend: vs 20d SMA 87.61 (-2.1%), 50d 90.09 (-4.8%), 200d 87.71 (-2.2%); 50d above 200d
Momentum: RSI(14) 34.9 | MACD -1.249 vs signal -1.091 (histogram -0.158)
Returns: 1d +0.4% | 5d -0.7% | 1m -4.1% | 3m -2.4%
52-week range: 77.90 - 93.19 (now 51.3% of the way up)
Volatility: ATR(14) 0.96 (1.1% of price) | annualised 20d 13.4%
Volume: 0.15x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.10</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score +0.10</summary>

```text
Fund type: Europe Stock
What it holds: P/E 17.85 | P/B 2.31 | P/S 1.64 | 3y earnings growth n/a
Yield: 3.0%
Three-year record: +18.1% a year | beta to the market 0.90
Cost and size: expense ratio 0.06% | net assets 37.17B
What it is made of: Stocks 99.0%, Cash 0.7%, Other 0.3%
Largest holdings: ASML Holding NV 4.0%, HSBC Holdings PLC 2.2%, Roche Holding AG Ordinary Shares new 1.9%, Novartis AG Registered Shares 1.7%, Shell PLC 1.6%
Sector mix: Financial services 25.3%, Industrials 19.8%, Healthcare 12.1%, Technology 9.0%
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
Rolled up from the 5 largest holdings, 11.4% of the fund by weight  -- thin, so read this as a fact about that slice rather than the fund
Ratings by weight: buy 65.7% | hold 34.3% | sell 0.0% (mean 2.10 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +14.1% above the current prices
Holdings read: ASML.AS, HSBA.L, ROP.SW, NOVN.SW, SHEL.L
Recent rating changes among them: none reported
```

</details>

<details><summary><b>Buying and selling by company insiders</b> — score -0.20</summary>

_Not available today._

</details>

<details><summary><b>Who is positioned how</b> — score -0.20</summary>

```text
Contract: MSCI EAFE  - ICE FUTURES U.S. (positions as of 2026-09-29, published the following Friday)
Large speculators: net long 2.3% of open interest (490,633 contracts)
Change on the week: -3.7% of open interest
Crowding: 87% percentile over 52 weeks -- within its normal range
Read this as crowding, not as a forecast: an extreme is as often the end of a move as the middle of one.
```

</details>

<details><summary><b>Money going into and out of this fund</b> — score -0.20</summary>

```text
Direction: money going out (1 week)
Share count change: 1 week: -3.4% (-1.31B) over 7d
Shares outstanding: 429.25M | fund size: 36.81B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Emerging markets (VWO) · Index fund — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> No macro surprise, technicals show price below short‑term SMAs with low volume and no decisive breakout, analyst view bullish but thin coverage, speculators reduced net‑long positions indicating slight bearish sentiment. Overall neutral.

**Main reasons it gave:**
- Technicals: price below 20‑day and 50‑day SMA, RSI 47.7, low volume, no decisive breakout
- Analyst view: all‑buy rating for top 22.2% holdings with +35% price target, but coverage thin
- Positioning: net long 3.1% of open interest fell by -1.5% week, indicating slight bearish sentiment
- Macro: stable yields, low VIX, no surprise in inflation or Fed policy

<details><summary><b>News</b> — score +0.00</summary>

_No news found for this one today._

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.06% (+0.06 on the week) | 5-year 5.04% (-0.02 on the week) | 10-year 5.27% (-0.00 on the week) | 30-year 5.64% (+0.01 on the week)
Yield curve, 10-year minus 3-month: +1.22 points -- upward sloping (normal)
US dollar index: 102.26 (+0.33 on the week)
Volatility (VIX): 15.01 (-0.3 on the week) -- elevated
Latest US data: inflation 3.4% (2026-08-01) | unemployment 4.2% (2026-09-01) | jobless claims 197k (2026-10-03)
Policy and expectations: Fed target 4.00% | market expects 2.4% inflation over 10 years
Rate path: 2-year Treasury 4.77% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 59.68 (bar of 2026-10-09), from 502 daily bars
Trend: vs 20d SMA 59.87 (-0.3%), 50d 60.15 (-0.8%), 200d 58.12 (+2.7%); 50d above 200d
Momentum: RSI(14) 47.7 | MACD -0.125 vs signal -0.085 (histogram -0.040)
Returns: 1d +1.0% | 5d +0.2% | 1m -0.4% | 3m +1.5%
52-week range: 52.42 - 61.44 (now 80.4% of the way up)
Volatility: ATR(14) 0.68 (1.1% of price) | annualised 20d 15.9%
Volume: 0.58x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.30</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score +0.30</summary>

```text
Fund type: Diversified Emerging Mkts
What it holds: P/E 15.91 | P/B 2.13 | P/S 1.86 | 3y earnings growth n/a
Yield: 2.0%
Three-year record: +19.0% a year | beta to the market 0.75
Cost and size: expense ratio 0.06% | net assets 164.66B
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

<details><summary><b>What analysts and big funds say</b> — score +0.35</summary>

_Not available today._

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score +0.35</summary>

```text
Rolled up from the 5 largest holdings, 22.2% of the fund by weight  -- thin, so read this as a fact about that slice rather than the fund
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 1.33 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +35.3% above the current prices
Holdings read: 2330.TW, 0700.HK, 9988.HK, 2454.TW, 2308.TW
Recent rating changes among them: none reported
```

</details>

<details><summary><b>Buying and selling by company insiders</b> — score -0.30</summary>

_Not available today._

</details>

<details><summary><b>Who is positioned how</b> — score -0.30</summary>

```text
Contract: MSCI EM INDEX - ICE FUTURES U.S. (positions as of 2026-09-29, published the following Friday)
Large speculators: net long 3.1% of open interest (1,066,077 contracts)
Change on the week: -1.5% of open interest
Crowding: 35% percentile over 52 weeks -- within its normal range
Read this as crowding, not as a forecast: an extreme is as often the end of a move as the middle of one.
```

</details>

<details><summary><b>Money going into and out of this fund</b> — score -0.30</summary>

```text
Direction: flat (1 week)
Share count change: 1 week: +0.0% (0.00) over 7d
Shares outstanding: 1.42B | fund size: 84.63B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### US company bonds, riskier (HYG) · Index fund — no answer, no confidence given

<details><summary><b>News</b> — score n/a</summary>

_No news found for this one today._

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score n/a</summary>

```text
US Treasury yields: 3-month 4.06% (+0.06 on the week) | 5-year 5.04% (-0.02 on the week) | 10-year 5.27% (-0.00 on the week) | 30-year 5.64% (+0.01 on the week)
Yield curve, 10-year minus 3-month: +1.22 points -- upward sloping (normal)
US dollar index: 102.26 (+0.33 on the week)
Volatility (VIX): 15.01 (-0.3 on the week) -- elevated
Latest US data: inflation 3.4% (2026-08-01) | unemployment 4.2% (2026-09-01) | jobless claims 197k (2026-10-03)
Policy and expectations: Fed target 4.00% | market expects 2.4% inflation over 10 years
Rate path: 2-year Treasury 4.77% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score n/a</summary>

```text
Last close 77.11 (bar of 2026-10-09), from 502 daily bars
Trend: vs 20d SMA 77.77 (-0.8%), 50d 78.79 (-2.1%), 200d 79.80 (-3.4%); 50d below 200d
Momentum: RSI(14) 27.9 | MACD -0.533 vs signal -0.519 (histogram -0.014)
Returns: 1d -0.0% | 5d +0.3% | 1m -1.9% | 3m -3.0%
52-week range: 76.90 - 81.28 (now 4.8% of the way up)
Volatility: ATR(14) 0.31 (0.4% of price) | annualised 20d 4.1%
Volume: 0.12x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score n/a</summary>

```text
Fund type: High Yield Bond
Yield: 6.1%
Credit quality: BB 57.9%, B 32.2%, Below B 8.3%, BBB 1.1%
Three-year record: +8.3% a year | beta to the market 0.70
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
Direction: money coming in (1 week)
Share count change: 1 week: +3.7% (601.88M) over 7d
Shares outstanding: 217.47M | fund size: 16.77B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### US government bonds, 7-10 years (IEF) · Index fund — no answer, no confidence given

<details><summary><b>News</b> — score n/a</summary>

- [Renting Is Cheaper Than Owning, But J.P. Morgan Sees Strain - iShares 7-10 Year Treasury Bond ETF (NASDAQ](https://www.benzinga.com/markets/economic-data/26/10/62267245/renting-is-cheaper-than-owning-says-jp-morgan-but-incomes-have-failed-to-keep-up)  
  <sub>Benzinga, 4 hours ago</sub>  
  Renting is still cheaper than owning, but J.P. Morgan says housing costs have outpaced incomes and high mortgage rates are squeezing buyers.
- [Foreign Buyers Took 80% of the Treasury’s $39 Billion Auction](https://247wallst.com/investing/2026/10/08/foreign-buyers-took-80-of-the-treasurys-39-billion-auction/)  
  <sub>24/7 Wall St., 24 hours ago</sub>  
  Foreign buyers snapped up 80% of the $39B 10-year auction, leaving dealers with a record-low 2.54% share, signaling genuine demand at 5.3% yields.
- [What Did Waller Say About Hikes and IEF (NASDAQ:IEF)?](https://kalkine.ca/news/daily-wrap/what-did-waller-say-about-hikes-and-ief-nasdaqief-1)  
  <sub>kalkine.ca, 3 hours ago</sub>  
  You are reading a free article with opinions that may differ from the recommendation given by Kalkine in its paid research reports.
- [The Stock Market Has A 5% Problem (SP500)](https://seekingalpha.com/article/4952882-the-stock-market-has-a-5-percent-problem)  
  <sub>Seeking Alpha, 20 hours ago</sub>  
  10-year yields at 5.3% are reshaping stocks and bonds. Click here to learn valuation discipline, Treasury ETF tactics, and better-priced growth picks.
- [Franklin Templeton CEO Jenny Johnson Reportedly Flags ‘Very Complex’ AI Debt Financing — Favors Short-Term Investments](https://www.tradingview.com/news/stocktwits:f475c006e094b:0-franklin-templeton-ceo-jenny-johnson-reportedly-flags-very-complex-ai-debt-financing-favors-short-term-investments/)  
  <sub>TradingView, 4 hours ago</sub>  
  Franklin Templeton CEO Jenny Johnson reportedly said artificial intelligence (AI) debt financing is becoming “very complex” as technology companies find new...
- [Ed Yardeni Says Stocks Could Face Trouble If Bond Yields Hit 6% — ‘We’d All Start To Get Concerned’](https://stocktwits.com/news-articles/markets/equity/ed-yardeni-stocks-trouble-bond-yields-6/cZMggCYRBOU)  
  <sub>Stocktwits, 20 hours ago</sub>  
  Yardeni said the 5.2% level on bond yields is not high enough to “kneecap” the stock market or the broader economy. However, he identified 6% yield as the...
- [Foreign buyers took 80% of a record $39B U.S. T...](https://pluang.com/en/news-feed/pembeli-asing-kuasai-lelang-treasury-39-miliar)  
  <sub>Pluang, 20 hours ago</sub>  
  In a record-setting auction on October 7, 2026, foreign buyers (indirect bidders) purchased 80.34% of $39 billion in 10-year U.S. Treasury notes,...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score n/a</summary>

```text
US Treasury yields: 3-month 4.06% (+0.06 on the week) | 5-year 5.04% (-0.02 on the week) | 10-year 5.27% (-0.00 on the week) | 30-year 5.64% (+0.01 on the week)
Yield curve, 10-year minus 3-month: +1.22 points -- upward sloping (normal)
US dollar index: 102.26 (+0.33 on the week)
Volatility (VIX): 15.01 (-0.3 on the week) -- elevated
Latest US data: inflation 3.4% (2026-08-01) | unemployment 4.2% (2026-09-01) | jobless claims 197k (2026-10-03)
Policy and expectations: Fed target 4.00% | market expects 2.4% inflation over 10 years
Rate path: 2-year Treasury 4.77% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score n/a</summary>

```text
Last close 89.21 (bar of 2026-10-09), from 502 daily bars
Trend: vs 20d SMA 89.96 (-0.8%), 50d 91.63 (-2.6%), 200d 94.29 (-5.4%); 50d below 200d
Momentum: RSI(14) 32.6 | MACD -0.762 vs signal -0.790 (histogram 0.028)
Returns: 1d -0.3% | 5d +0.2% | 1m -2.2% | 3m -4.4%
52-week range: 88.92 - 97.99 (now 3.2% of the way up)
Volatility: ATR(14) 0.48 (0.5% of price) | annualised 20d 6.1%
Volume: 0.17x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score n/a</summary>

```text
Fund type: Long Government
Yield: 4.1%
Credit quality: AA 100.0% | US government debt 99.7%
Three-year record: +3.4% a year | beta to the market 1.16
Cost and size: expense ratio 0.15% | net assets 41.56B
What it is made of: Bonds 99.7%, Cash 0.3%
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
Contract: UST 10Y NOTE - CHICAGO BOARD OF TRADE (positions as of 2026-09-29, published the following Friday)
Large speculators: net short 35.9% of open interest (5,676,556 contracts)
Change on the week: -0.2% of open interest
Crowding: 83% percentile over 52 weeks -- within its normal range
Read this as crowding, not as a forecast: an extreme is as often the end of a move as the middle of one.
```

</details>

<details><summary><b>Money going into and out of this fund</b> — score n/a</summary>

```text
Direction: flat (1 week)
Share count change: 1 week: -0.3% (-110.69M) over 7d
Shares outstanding: 466.40M | fund size: 41.61B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### US inflation-linked bonds (TIP) · Index fund — no answer, no confidence given

<details><summary><b>News</b> — score n/a</summary>

- [Think 5% Treasury Yields Are Scary? This CEO Expects 8% - iShares TIPS Bond ETF (ARCA:TIP)](https://www.benzinga.com/etfs/sector-etfs/26/10/62269770/exclusive-think-5-treasury-yields-are-scary-this-ceo-says-8-is-coming)  
  <sub>Benzinga, 2 hours ago</sub>  
  Canary Capital CEO Steven McClurg sees 10-year Treasury yields hitting 8% within four years. TIPS and commodity ETFs could gain attention.
- [HAA TIP Momentum (Wouter Keller) — Indicator by HenriqueCentieiro](https://www.tradingview.com/script/ezYlFKRd-HAA-TIP-Momentum-Wouter-Keller/)  
  <sub>TradingView, 5 hours ago</sub>  
  A monthly risk-on / risk-off regime indicator based on the TIPS momentum "canary" from Wouter Keller & Jan Willem Keuning's Hybrid Asset Allocation paper...
- [Some Popular ETF Tax Strategies Dodge Government’s Curbs](https://www.bloomberg.com/news/newsletters/2026-10-08/treasury-s-tax-warning-leaves-key-etf-maneuvers-untouched?srnd=homepage-americas)  
  <sub>Bloomberg.com, 20 hours ago</sub>  
  Welcome to ETF IQ, a weekly newsletter dedicated to the $24 trillion global ETF industry. I'm Bloomberg News reporter Vildana Hajric, in for Katie Greifeld.
- [What Will UMich Sentiment Show for TIP (NYSEARCA:TIP) Holders?](https://kalkine.ca/news/daily-wrap/what-will-umich-sentiment-show-for-tip-nysearcatip-holders-1)  
  <sub>kalkine.ca, 3 hours ago</sub>  
  You are reading a free article with opinions that may differ from the recommendation given by Kalkine in its paid research reports.
- [Inflation Expectations Just Jumped to a Three-Year High as Americans Now Expect 3.9% Inflation](https://247wallst.com/investing/2026/10/08/inflation-expectations-just-jumped-to-a-three-year-high-as-americans-now-expect-3-9-inflation/)  
  <sub>24/7 Wall St., 24 hours ago</sub>  
  Gas prices have surged more than a dollar per gallon in a year, and now consumer inflation expectations have hit a level not seen since 2023,...
- [Lion-OCBC TECH ETF Tightens Liquidity Controls Ahead of 2026 Changes](https://www.tipranks.com/news/company-announcements/lion-ocbc-tech-etf-tightens-liquidity-controls-ahead-of-2026-changes)  
  <sub>TipRanks, 4 hours ago</sub>  
  An announcement from Lion-OCBC Securities Hang Seng TECH ETF ( ($SG:HST) ) is now available. Lion Global Investors will introduce new liquidity risk...
- [SPDR Straits Times Index ETF Adds Tyxeros Trading as Designated Market Maker](https://www.tipranks.com/news/company-announcements/spdr-straits-times-index-etf-adds-tyxeros-trading-as-designated-market-maker)  
  <sub>TipRanks, 4 hours ago</sub>  
  SPDR Straits Times Index ETF ( ($SG:ES3) ) has provided an announcement. State Street Global Advisors Singapore Limited, manager of the SPDR Straits Times...
- [İş Yatırım Discloses Market Making Activity in ISMDL ETF](https://www.tipranks.com/news/company-announcements/is-yatirim-discloses-market-making-activity-in-ismdl-etf)  
  <sub>TipRanks, 4 hours ago</sub>  
  An update from Is Yatirim Menkul Degerler AS ( ($TR:ISMEN) ) is now available. İş Yatırım Menkul Değerler A.Ş. reported its market making activity in the...
- [Is Yatirim Reports No Market‑Making Activity in ISGLK ETF](https://www.tipranks.com/news/company-announcements/is-yatirim-reports-no-marketmaking-activity-in-isglk-etf)  
  <sub>TipRanks, 4 hours ago</sub>  
  Is Yatirim Menkul Degerler AS ( ($TR:ISMEN) ) has shared an update. Is Yatirim Menkul Degerler AS reported that on 08/10/2026 it conducted no market‑making...
- [Is Yatirim Details Market-Making Trades in ISX30 ETF](https://www.tipranks.com/news/company-announcements/is-yatirim-details-market-making-trades-in-isx30-etf-4)  
  <sub>TipRanks, 4 hours ago</sub>  
  An announcement from Is Yatirim Menkul Degerler AS ( ($TR:ISMEN) ) is now available. Is Yatirim Menkul Degerler AS reported its market making activity in...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score n/a</summary>

```text
US Treasury yields: 3-month 4.06% (+0.06 on the week) | 5-year 5.04% (-0.02 on the week) | 10-year 5.27% (-0.00 on the week) | 30-year 5.64% (+0.01 on the week)
Yield curve, 10-year minus 3-month: +1.22 points -- upward sloping (normal)
US dollar index: 102.26 (+0.33 on the week)
Volatility (VIX): 15.01 (-0.3 on the week) -- elevated
Latest US data: inflation 3.4% (2026-08-01) | unemployment 4.2% (2026-09-01) | jobless claims 197k (2026-10-03)
Policy and expectations: Fed target 4.00% | market expects 2.4% inflation over 10 years
Rate path: 2-year Treasury 4.77% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score n/a</summary>

```text
Last close 104.34 (bar of 2026-10-09), from 502 daily bars
Trend: vs 20d SMA 104.73 (-0.4%), 50d 106.10 (-1.7%), 200d 109.19 (-4.4%); 50d below 200d
Momentum: RSI(14) 37.4 | MACD -0.605 vs signal -0.671 (histogram 0.066)
Returns: 1d -0.2% | 5d +0.2% | 1m -1.9% | 3m -3.3%
52-week range: 103.98 - 112.20 (now 4.4% of the way up)
Volatility: ATR(14) 0.40 (0.4% of price) | annualised 20d 4.8%
Volume: 0.17x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score n/a</summary>

```text
Fund type: Inflation-Protected Bond
Yield: 4.7%
Credit quality: AA 99.9% | US government debt 100.0%
Three-year record: +4.1% a year | beta to the market 0.71
Cost and size: expense ratio 0.18% | net assets 14.23B
What it is made of: Bonds 100.0%
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
Contract: UST 10Y NOTE - CHICAGO BOARD OF TRADE (positions as of 2026-09-29, published the following Friday)
Large speculators: net short 35.9% of open interest (5,676,556 contracts)
Change on the week: -0.2% of open interest
Crowding: 83% percentile over 52 weeks -- within its normal range
Read this as crowding, not as a forecast: an extreme is as often the end of a move as the middle of one.
```

</details>

<details><summary><b>Money going into and out of this fund</b> — score n/a</summary>

```text
Direction: money going out (1 week)
Share count change: 1 week: -5.3% (-793.79M) over 7d
Shares outstanding: 136.69M | fund size: 14.26B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### US government bonds, 20+ years (TLT) · Index fund — no answer, no confidence given

<details><summary><b>News</b> — score n/a</summary>

- [EXCLUSIVE: Think 5% Treasury Yields Are Scary? This CEO Says 8% Is Coming](https://www.tradingview.com/news/benzinga:75811bb31094b:0-exclusive-think-5-treasury-yields-are-scary-this-ceo-says-8-is-coming/)  
  <sub>TradingView, 2 hours ago</sub>  
  Canary Capital CEO Steven McClurg expects 10-year U.S. Treasury yields to climb to 8% within four years, warning that mounting government borrowing could...
- [The Big Bet on Interest Rates: Gold Has Yet to Deliver Its Verdict](https://goldbroker.com/news/big-bet-interest-rates-gold-deliver-verdict)  
  <sub>GoldBroker, 6 hours ago</sub>  
  Investors are piling into Treasuries and major tech stocks, betting on lower interest rates ahead. Yet banks are cutting their exposure, credit markets are...
- [Daily ETF Flows: EWZ Keeps Gathering Assets](https://finance.yahoo.com/markets/options/articles/daily-etf-flows-ewz-keeps-210004744.html)  
  <sub>Yahoo Finance, 18 hours ago</sub>  
  Here are the daily ETF fund flows for October 8, 2026.
- [How Will TLT (NASDAQ:TLT) Fare After the 5.35% Yield Spike?](https://kalkine.ca/by-topic/mutual-funds-etfs/how-will-tlt-nasdaqtlt-fare-after-the-535-yield-spike-1)  
  <sub>kalkine.ca, 3 hours ago</sub>  
  You are reading a free article with opinions that may differ from the recommendation given by Kalkine in its paid research reports. Become a Kalkine member...
- [The Stock Market Has A 5% Problem (SP500)](https://seekingalpha.com/article/4952882-the-stock-market-has-a-5-percent-problem)  
  <sub>Seeking Alpha, 20 hours ago</sub>  
  10-year yields at 5.3% are reshaping stocks and bonds. Click here to learn valuation discipline, Treasury ETF tactics, and better-priced growth picks.
- [S&P 500, Nasdaq, Dow Futures Edge Higher Ahead Of Fed Rate Decision: INTC, SNAP, SOFI, RUM In Focus](https://stocktwits.com/news-articles/markets/equity/sp500-nasdaq-dow-futures-edge-higher-ahead-of-fed-rate-decision/cZK0WgFR74u)  
  <sub>Stocktwits, 13 hours ago</sub>  
  The Dow surged to a fresh intraday record on Tuesday before finishing at an all-time closing high, marking its second straight record close.
- [Options traders bet on a rebound in long-term U...](https://pluang.com/en/news-feed/trader-opsi-mulai-memanggil-bawah-pasar-obligasi-setelah-lelang-10-tahun)  
  <sub>Pluang, 20 hours ago</sub>  
  Options trading in the iShares 20+ Year Treasury Bond ETF (TLT) surged with heavy call buying, signaling some traders expect a bottom in the recent U.S....
- [Foreign Buyers Took 80% of the Treasury’s $39 Billion Auction](https://247wallst.com/investing/2026/10/08/foreign-buyers-took-80-of-the-treasurys-39-billion-auction/)  
  <sub>24/7 Wall St., 24 hours ago</sub>  
  Foreign buyers snapped up 80% of the $39B 10-year auction, leaving dealers with a record-low 2.54% share, signaling genuine demand at 5.3% yields.
- [Franklin Templeton CEO Jenny Johnson Reportedly Flags ‘Very Complex’ AI Debt Financing — Favors Short-Term Investments](https://www.tradingview.com/news/stocktwits:f475c006e094b:0-franklin-templeton-ceo-jenny-johnson-reportedly-flags-very-complex-ai-debt-financing-favors-short-term-investments/)  
  <sub>TradingView, 4 hours ago</sub>  
  Franklin Templeton CEO Jenny Johnson reportedly said artificial intelligence (AI) debt financing is becoming “very complex” as technology companies find new...
- [Foreign buyers took 80% of a record $39B U.S. T...](https://pluang.com/en/news-feed/pembeli-asing-kuasai-lelang-treasury-39-miliar)  
  <sub>Pluang, 20 hours ago</sub>  
  In a record-setting auction on October 7, 2026, foreign buyers (indirect bidders) purchased 80.34% of $39 billion in 10-year U.S. Treasury notes,...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score n/a</summary>

```text
US Treasury yields: 3-month 4.06% (+0.06 on the week) | 5-year 5.04% (-0.02 on the week) | 10-year 5.27% (-0.00 on the week) | 30-year 5.64% (+0.01 on the week)
Yield curve, 10-year minus 3-month: +1.22 points -- upward sloping (normal)
US dollar index: 102.26 (+0.33 on the week)
Volatility (VIX): 15.01 (-0.3 on the week) -- elevated
Latest US data: inflation 3.4% (2026-08-01) | unemployment 4.2% (2026-09-01) | jobless claims 197k (2026-10-03)
Policy and expectations: Fed target 4.00% | market expects 2.4% inflation over 10 years
Rate path: 2-year Treasury 4.77% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score n/a</summary>

```text
Last close 77.56 (bar of 2026-10-09), from 502 daily bars
Trend: vs 20d SMA 79.25 (-2.1%), 50d 81.07 (-4.3%), 200d 85.17 (-8.9%); 50d below 200d
Momentum: RSI(14) 31.6 | MACD -1.217 vs signal -1.128 (histogram -0.090)
Returns: 1d -0.4% | 5d +0.1% | 1m -4.0% | 3m -7.6%
52-week range: 77.11 - 92.06 (now 3.0% of the way up)
Volatility: ATR(14) 0.77 (1.0% of price) | annualised 20d 10.5%
Volume: 0.14x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score n/a</summary>

```text
Fund type: Long Government
Yield: 5.0%
Credit quality: AA 100.0% | US government debt 99.6%
Three-year record: +1.2% a year | beta to the market 2.31
Cost and size: expense ratio 0.15% | net assets 46.23B
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
Contract: ULTRA UST BOND - CHICAGO BOARD OF TRADE (positions as of 2026-09-29, published the following Friday)
Large speculators: net short 32.3% of open interest (2,507,580 contracts)
Change on the week: +1.0% of open interest
Crowding: 57% percentile over 52 weeks -- within its normal range
Read this as crowding, not as a forecast: an extreme is as often the end of a move as the middle of one.
```

</details>

<details><summary><b>Money going into and out of this fund</b> — score n/a</summary>

```text
Direction: flat (1 week)
Share count change: 1 week: +0.0% (0.00) over 7d
Shares outstanding: 109.70M | fund size: 8.51B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### US dollar (UUP) · Index fund — no answer, no confidence given

<details><summary><b>News</b> — score n/a</summary>

- [What Is Next for the Dollar Near 102.37, and UUP (NYSEARCA:UUP)?](https://kalkine.com.au/news/daily-wrap/what-is-next-for-the-dollar-near-10237-and-uup-nysearcauup-1)  
  <sub>Kalkine, 2 hours ago</sub>  
  You are reading a free article with opinions that may differ from the recommendation given by Kalkine in its paid research reports.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score n/a</summary>

```text
US Treasury yields: 3-month 4.06% (+0.06 on the week) | 5-year 5.04% (-0.02 on the week) | 10-year 5.27% (-0.00 on the week) | 30-year 5.64% (+0.01 on the week)
Yield curve, 10-year minus 3-month: +1.22 points -- upward sloping (normal)
US dollar index: 102.26 (+0.33 on the week)
Volatility (VIX): 15.01 (-0.3 on the week) -- elevated
Latest US data: inflation 3.4% (2026-08-01) | unemployment 4.2% (2026-09-01) | jobless claims 197k (2026-10-03)
Policy and expectations: Fed target 4.00% | market expects 2.4% inflation over 10 years
Rate path: 2-year Treasury 4.77% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score n/a</summary>

```text
Last close 29.05 (bar of 2026-10-09), from 502 daily bars
Trend: vs 20d SMA 28.68 (+1.3%), 50d 28.32 (+2.6%), 200d 27.79 (+4.5%); 50d above 200d
Momentum: RSI(14) 70.6 | MACD 0.215 vs signal 0.188 (histogram 0.028)
Returns: 1d +0.2% | 5d +0.5% | 1m +3.6% | 3m +1.9%
52-week range: 26.47 - 29.05 (now 100.0% of the way up)
Volatility: ATR(14) 0.12 (0.4% of price) | annualised 20d 4.7%
Volume: 0.07x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score n/a</summary>

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
Rolled up from the 1 largest holdings, 49.4% of the fund by weight
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
Contract: USD INDEX - ICE FUTURES U.S. (positions as of 2026-09-29, published the following Friday)
Large speculators: net long 0.7% of open interest (48,342 contracts)
Change on the week: +10.4% of open interest
Crowding: 78% percentile over 52 weeks -- within its normal range
Read this as crowding, not as a forecast: an extreme is as often the end of a move as the middle of one.
```

</details>

<details><summary><b>Money going into and out of this fund</b> — score n/a</summary>

```text
Direction: money coming in (1 week)
Share count change: 1 week: +43.5% (131.42M) over 7d
Shares outstanding: 14.92M | fund size: 433.30M
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

## Sector and country funds

### Netherlands (EWN) · Sector or country — NEUTRAL, confidence 0.45

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Analyst consensus 100% buy on top holdings, weighted price target +29.1% above current price; fund flows flat (share count unchanged +0.0% over 7d); fundamentals stable (P/E 18.85, dividend yield 4.2%, expense ratio 0.5%); technicals show price above 200‑day SMA (+3.0%) but below 20‑day SMA (-1.1%) and 50‑day SMA (-2.6%), RSI 43.7, volume 0.10× 20‑day average.

**Main reasons it gave:**
- Analyst ratings: 100% buy, mean rating 1.61 (strong buy) on top holdings
- Weighted price target: +29.1% above current price
- Fund flows flat: share count unchanged (+0.0% over 7d)
- Fund fundamentals stable: P/E 18.85, dividend yield 4.2%, expense ratio 0.5%
- Technicals: price above 200‑day SMA (+3.0%) but below 20‑day SMA (-1.1%) and 50‑day SMA (-2.6%), RSI 43.7, volume 0.10× 20‑day average

<details><summary><b>News</b> — score +0.00</summary>

- [ETF List: All ETFs by Assets, Style and Annualized Returns — Page 15 of 58](https://www.gurufocus.com/etfs?page=15)  
  <sub>GuruFocus, 20 hours ago</sub>  
  Browse every ETF we track, ranked by assets, with investment style and YTD, 1-year, 3-year, 5-year and 10-year returns.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.06% (+0.06 on the week) | 5-year 5.04% (-0.02 on the week) | 10-year 5.27% (-0.00 on the week) | 30-year 5.64% (+0.01 on the week)
Yield curve, 10-year minus 3-month: +1.22 points -- upward sloping (normal)
US dollar index: 102.26 (+0.33 on the week)
Volatility (VIX): 15.01 (-0.3 on the week) -- elevated
Latest US data: inflation 3.4% (2026-08-01) | unemployment 4.2% (2026-09-01) | jobless claims 197k (2026-10-03)
Policy and expectations: Fed target 4.00% | market expects 2.4% inflation over 10 years
Rate path: 2-year Treasury 4.77% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 66.55 (bar of 2026-10-09), from 502 daily bars
Trend: vs 20d SMA 67.31 (-1.1%), 50d 68.33 (-2.6%), 200d 64.59 (+3.0%); 50d above 200d
Momentum: RSI(14) 43.7 | MACD -0.333 vs signal -0.236 (histogram -0.097)
Returns: 1d +0.6% | 5d -2.0% | 1m -1.5% | 3m -0.8%
52-week range: 55.33 - 71.61 (now 68.9% of the way up)
Volatility: ATR(14) 0.95 (1.4% of price) | annualised 20d 18.3%
Volume: 0.10x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.00</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score +0.00</summary>

```text
Fund type: Focused Region
What it holds: P/E 18.85 | P/B 2.55 | P/S 1.87 | 3y earnings growth n/a
Yield: 4.2%
Three-year record: +25.0% a year | beta to the market 1.09
Cost and size: expense ratio 0.50% | net assets 710.44M
What it is made of: Stocks 98.9%, Cash 1.1%
Largest holdings: ASML Holding NV 23.6%, ING Groep NV 9.1%, Nebius Group NV Shs Class-A- 4.9%, Prosus NV Ordinary Shares - Class N 4.6%, ASM International NV 4.4%
Sector mix: Technology 33.4%, Financial services 21.5%, Consumer defensive 10.4%, Industrials 9.6%
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
Rolled up from the 5 largest holdings, 46.7% of the fund by weight
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 1.61 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +29.1% above the current prices
Holdings read: ASML.AS, INGA.AS, NBIS, PRX.AS, ASM.AS
Recent rating changes among them:
  - NBIS: 2026-10-08 Rosenblatt: init, ? -> Buy
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
Shares outstanding: 5.55M | fund size: 369.35M
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Israel (EIS) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Neutral overall; technicals are bearish, analyst coverage is bullish, but fund flows are flat and macro data show no surprise.

**Main reasons it gave:**
- Price below 20‑day, 50‑day, 200‑day SMAs (‑3.4% to ‑3.7%)
- Analyst coverage: 100% buy on 37.6% of fund, weighted price target +24.5%
- Fund flows flat: share count change +0.0% over 7 days
- Macro data unchanged: yields stable, no policy surprise

<details><summary><b>News</b> — score +0.00</summary>

_No news found for this one today._

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.06% (+0.06 on the week) | 5-year 5.04% (-0.02 on the week) | 10-year 5.27% (-0.00 on the week) | 30-year 5.64% (+0.01 on the week)
Yield curve, 10-year minus 3-month: +1.22 points -- upward sloping (normal)
US dollar index: 102.26 (+0.33 on the week)
Volatility (VIX): 15.01 (-0.3 on the week) -- elevated
Latest US data: inflation 3.4% (2026-08-01) | unemployment 4.2% (2026-09-01) | jobless claims 197k (2026-10-03)
Policy and expectations: Fed target 4.00% | market expects 2.4% inflation over 10 years
Rate path: 2-year Treasury 4.77% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score -0.20</summary>

```text
Last close 118.24 (bar of 2026-10-09), from 502 daily bars
Trend: vs 20d SMA 122.39 (-3.4%), 50d 122.68 (-3.6%), 200d 122.81 (-3.7%); 50d below 200d
Momentum: RSI(14) 37.5 | MACD -1.254 vs signal -0.609 (histogram -0.645)
Returns: 1d +0.5% | 5d -3.5% | 1m -3.2% | 3m +0.2%
52-week range: 97.88 - 137.69 (now 51.1% of the way up)
Volatility: ATR(14) 1.70 (1.4% of price) | annualised 20d 17.4%
Volume: 0.27x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.00</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score +0.00</summary>

```text
Fund type: Focused Region
What it holds: P/E 17.89 | P/B 2.43 | P/S 2.45 | 3y earnings growth n/a
Yield: 1.5%
Three-year record: +32.3% a year | beta to the market 1.09
Cost and size: expense ratio 0.59% | net assets 874.00M
What it is made of: Stocks 99.5%, Cash 0.5%
Largest holdings: Teva Pharmaceutical Industries Ltd ADR 10.1%, Bank Leumi Le-Israel BM 9.0%, Bank Hapoalim BM 8.1%, Tower Semiconductor Ltd 5.5%, Elbit Systems Ltd 4.8%
Sector mix: Financial services 36.1%, Technology 18.1%, Healthcare 10.7%, Industrials 10.0%
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
Rolled up from the 5 largest holdings, 37.6% of the fund by weight
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 1.29 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +24.5% above the current prices
Holdings read: TEVA, LUMI.TA, POLI.TA, TSEM.TA, ESLT.TA
Recent rating changes among them:
  - TEVA: 2026-10-01 TD Cowen: init, ? -> Buy
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
Direction: flat (1 week)
Share count change: 1 week: +0.0% (0.00) over 7d
Shares outstanding: 2.55M | fund size: 301.51M
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Australia (EWA) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:** no explanation. It wrote only “NEUTRAL”, so the main reasons below are all it gave.

**Main reasons it gave:**
- No macro surprise: yields stable, VIX low, no policy shift
- Technicals: price below 20d, 50d, 200d SMAs, low volume, no decisive break
- Analyst view: 59.5% hold, 40.5% sell, weighted price target -5.4% vs current price
- Fund flows: 9.5% share count decline (~$127M outflow) over 1 week

<details><summary><b>News</b> — score +0.00</summary>

_No news found for this one today._

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.06% (+0.06 on the week) | 5-year 5.04% (-0.02 on the week) | 10-year 5.27% (-0.00 on the week) | 30-year 5.64% (+0.01 on the week)
Yield curve, 10-year minus 3-month: +1.22 points -- upward sloping (normal)
US dollar index: 102.26 (+0.33 on the week)
Volatility (VIX): 15.01 (-0.3 on the week) -- elevated
Latest US data: inflation 3.4% (2026-08-01) | unemployment 4.2% (2026-09-01) | jobless claims 197k (2026-10-03)
Policy and expectations: Fed target 4.00% | market expects 2.4% inflation over 10 years
Rate path: 2-year Treasury 4.77% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 28.46 (bar of 2026-10-09), from 502 daily bars
Trend: vs 20d SMA 28.55 (-0.3%), 50d 29.36 (-3.1%), 200d 28.70 (-0.8%); 50d above 200d
Momentum: RSI(14) 44.9 | MACD -0.292 vs signal -0.312 (histogram 0.021)
Returns: 1d +0.8% | 5d +0.5% | 1m -2.1% | 3m +0.4%
52-week range: 24.95 - 30.43 (now 64.0% of the way up)
Volatility: ATR(14) 0.35 (1.2% of price) | annualised 20d 17.1%
Volume: 0.08x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.00</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score +0.00</summary>

```text
Fund type: Focused Region
What it holds: P/E 20.31 | P/B 2.65 | P/S 3.31 | 3y earnings growth n/a
Yield: 3.0%
Three-year record: +13.9% a year | beta to the market 0.98
Cost and size: expense ratio 0.50% | net assets 1.21B
What it is made of: Stocks 99.2%, Cash 0.8%
Largest holdings: BHP Group Ltd 15.4%, Commonwealth Bank of Australia 12.6%, National Australia Bank Ltd 6.1%, Westpac Banking Corp 6.0%, ANZ Group Holdings Ltd 5.8%
Sector mix: Financial services 42.0%, Basic materials 25.4%, Consumer cyclical 6.5%, Healthcare 5.6%
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
Rolled up from the 5 largest holdings, 45.9% of the fund by weight
Ratings by weight: buy 0.0% | hold 59.5% | sell 40.5% (mean 3.43 on a 1=strong buy to 5=strong sell scale)
Weighted price target: -5.4% above the current prices
Holdings read: BHP.AX, CBA.AX, NAB.AX, WBC.AX, ANZ.AX
Recent rating changes among them: none reported
```

</details>

<details><summary><b>Buying and selling by company insiders</b> — score -0.65</summary>

_Not available today._

</details>

<details><summary><b>Who is positioned how</b> — score -0.65</summary>

_Not available today._

</details>

<details><summary><b>Money going into and out of this fund</b> — score -0.65</summary>

```text
Direction: money going out (1 week)
Share count change: 1 week: -9.5% (-127.19M) over 7d
Shares outstanding: 42.45M | fund size: 1.21B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Canada (EWC) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> No macro surprise, technicals neutral, modestly positive analyst view and fund flows, but no decisive catalyst.

**Main reasons it gave:**
- US Treasury yields unchanged (10‑yr 5.27% Δ0.00) – no macro surprise
- EWC price below 20‑day SMA (58.74 vs 59.37) and volume 0.14× 20‑day avg – neutral technicals
- Analyst coverage 29.3% of fund, 74% buy, price target +6.5% – modest bullish bias
- Fund flows positive: share count +2.0% over 7 days – modest demand

<details><summary><b>News</b> — score +0.00</summary>

- [BlackRock LifePath ESG Index 2030 Fund's iShares MSCI Canada ETF(EWC) Holding History](https://www.gurufocus.com/guru-portfolio/BlackRock%20LifePath%20ESG%20Index%202030%20Fund/EWC)  
  <sub>GuruFocus, 20 hours ago</sub>  
  iShares MSCI Canada ETF(EWC) Buys and Sells Made by BlackRock LifePath ESG Index 2030 Fund. Latest and Historical Data and Chart.
- [NDXP 261008 28100.00P (NDXP261008P28100000) Stock Options Chain | Quotes & News](https://www.moomoo.com/options/NDXP261008P28100000-US?chain_id=Name1K9-3FXPhg.1l1ka40&global_content=%7B%22promote_id%22%3A13764,%22sub_promote_id%22%3A61,%22f%22%3A%22www.moomoo.com%2Fcommunity%2Ffeed%2Fishares-msci-canada-etf-ewc-technical-analysis-continued-strong-momentum-114596034117637%22%7D)  
  <sub>Moomoo, 11 hours ago</sub>  
  Track real-time NDXP 261008 28100.00P (NDXP261008P28100000) stock options chain data and pricing information and news on moomoo App for your options trading...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.06% (+0.06 on the week) | 5-year 5.04% (-0.02 on the week) | 10-year 5.27% (-0.00 on the week) | 30-year 5.64% (+0.01 on the week)
Yield curve, 10-year minus 3-month: +1.22 points -- upward sloping (normal)
US dollar index: 102.26 (+0.33 on the week)
Volatility (VIX): 15.01 (-0.3 on the week) -- elevated
Latest US data: inflation 3.4% (2026-08-01) | unemployment 4.2% (2026-09-01) | jobless claims 197k (2026-10-03)
Policy and expectations: Fed target 4.00% | market expects 2.4% inflation over 10 years
Rate path: 2-year Treasury 4.77% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 58.74 (bar of 2026-10-09), from 502 daily bars
Trend: vs 20d SMA 59.37 (-1.1%), 50d 60.61 (-3.1%), 200d 57.85 (+1.5%); 50d above 200d
Momentum: RSI(14) 42.6 | MACD -0.630 vs signal -0.575 (histogram -0.054)
Returns: 1d +0.7% | 5d +0.0% | 1m -2.6% | 3m +0.0%
52-week range: 49.72 - 62.64 (now 69.8% of the way up)
Volatility: ATR(14) 0.66 (1.1% of price) | annualised 20d 13.2%
Volume: 0.14x the 20-day average
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
Three-year record: +24.1% a year | beta to the market 0.80
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
Ratings by weight: buy 74.1% | hold 25.9% | sell 0.0% (mean 2.19 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +6.5% above the current prices
Holdings read: RY, TD, SHOP, BMO.TO, BNS.TO
Recent rating changes among them:
  - RY: 2025-08-29 Argus Research: main, Buy -> Buy
  - TD: 2026-06-01 RBC Capital: main, Outperform -> Outperform
  - SHOP: 2026-10-06 JP Morgan: main, Overweight -> Overweight
  - BMO.TO: 2026-05-28 RBC Capital: main, Sector Perform -> Sector Perform
  - BNS.TO: 2026-05-28 RBC Capital: main, Sector Perform -> Sector Perform
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
Share count change: 1 week: +2.0% (138.20M) over 7d
Shares outstanding: 118.55M | fund size: 6.96B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Sweden (EWD) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> The fund shows strong inflows (share count up 26% in a week) and a bullish analyst consensus (81.7% buy rating, +10% price target), but technicals are slightly bearish (price below 20‑, 50‑ and 200‑day SMAs, RSI 44.4, MACD marginally negative) and macro conditions are neutral with stable yields and low volatility. The mixed signals lead to a neutral overall stance.

**Main reasons it gave:**
- Share count increased 26% over the past week, showing strong inflows
- Analyst coverage: 81.7% buy rating and weighted price target +10% above current price
- Technicals: price below 20‑day, 50‑day and 200‑day SMAs; RSI 44.4, MACD slightly negative, volume 0.19x 20‑day average
- Macro: Treasury yields stable, VIX low at 15.01, no surprise in inflation or unemployment data

<details><summary><b>News</b> — score +0.00</summary>

_No news found for this one today._

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.06% (+0.06 on the week) | 5-year 5.04% (-0.02 on the week) | 10-year 5.27% (-0.00 on the week) | 30-year 5.64% (+0.01 on the week)
Yield curve, 10-year minus 3-month: +1.22 points -- upward sloping (normal)
US dollar index: 102.26 (+0.33 on the week)
Volatility (VIX): 15.01 (-0.3 on the week) -- elevated
Latest US data: inflation 3.4% (2026-08-01) | unemployment 4.2% (2026-09-01) | jobless claims 197k (2026-10-03)
Policy and expectations: Fed target 4.00% | market expects 2.4% inflation over 10 years
Rate path: 2-year Treasury 4.77% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score -0.20</summary>

```text
Last close 50.47 (bar of 2026-10-09), from 502 daily bars
Trend: vs 20d SMA 50.81 (-0.7%), 50d 52.15 (-3.2%), 200d 51.43 (-1.9%); 50d above 200d
Momentum: RSI(14) 44.4 | MACD -0.565 vs signal -0.551 (histogram -0.014)
Returns: 1d +0.7% | 5d +0.8% | 1m -2.2% | 3m +1.7%
52-week range: 45.38 - 54.72 (now 54.5% of the way up)
Volatility: ATR(14) 0.71 (1.4% of price) | annualised 20d 15.0%
Volume: 0.19x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.00</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score +0.00</summary>

```text
Fund type: Focused Region
What it holds: P/E 14.64 | P/B 2.82 | P/S 2.83 | 3y earnings growth n/a
Yield: 3.6%
Three-year record: +18.8% a year | beta to the market 1.25
Cost and size: expense ratio 0.51% | net assets 947.21M
What it is made of: Stocks 99.1%, Cash 0.9%
Largest holdings: Spotify Technology SA 9.7%, Investor AB Class B 9.6%, Atlas Copco AB Class A 7.1%, Volvo AB Class B 6.8%, Sandvik AB 5.3%
Sector mix: Industrials 46.3%, Financial services 25.6%, Communication services 13.5%, Technology 6.1%
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
Rolled up from the 4 largest holdings, 28.9% of the fund by weight
Ratings by weight: buy 81.7% | hold 18.3% | sell 0.0% (mean 1.98 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +10.0% above the current prices
Holdings read: SPOT, ATCO-A.ST, VOLV-B.ST, SAND.ST
Recent rating changes among them:
  - SPOT: 2026-10-08 Piper Sandler: init, ? -> Neutral
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
Direction: money coming in (1 week)
Share count change: 1 week: +26.0% (196.24M) over 7d
Shares outstanding: 18.82M | fund size: 950.08M
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Germany (EWG) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Neutral overall: no macro surprise, flat fund flows, technicals bearish but not decisive, analyst view bullish but not enough to tilt, fundamentals solid but not a catalyst.

**Main reasons it gave:**
- Flat fund flows (0.0% share count change over 1 week)
- Inflation 3.4% above 10‑year expectation of 2.4%
- Technical indicators bearish: price below 20‑day SMA, RSI 35.8, low volume (0.08× 20‑day avg)
- Analyst coverage bullish: 78.7% buy rating, price target +18.2% above current price
- Fund fundamentals solid: P/E 17.64, 3‑year return +19.1% per year

<details><summary><b>News</b> — score +0.00</summary>

_No news found for this one today._

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.06% (+0.06 on the week) | 5-year 5.04% (-0.02 on the week) | 10-year 5.27% (-0.00 on the week) | 30-year 5.64% (+0.01 on the week)
Yield curve, 10-year minus 3-month: +1.22 points -- upward sloping (normal)
US dollar index: 102.26 (+0.33 on the week)
Volatility (VIX): 15.01 (-0.3 on the week) -- elevated
Latest US data: inflation 3.4% (2026-08-01) | unemployment 4.2% (2026-09-01) | jobless claims 197k (2026-10-03)
Policy and expectations: Fed target 4.00% | market expects 2.4% inflation over 10 years
Rate path: 2-year Treasury 4.77% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score -0.20</summary>

```text
Last close 40.86 (bar of 2026-10-09), from 502 daily bars
Trend: vs 20d SMA 41.82 (-2.3%), 50d 43.01 (-5.0%), 200d 42.36 (-3.5%); 50d above 200d
Momentum: RSI(14) 35.8 | MACD -0.593 vs signal -0.510 (histogram -0.083)
Returns: 1d +0.5% | 5d -1.1% | 1m -4.1% | 3m -0.9%
52-week range: 38.08 - 44.59 (now 42.7% of the way up)
Volatility: ATR(14) 0.52 (1.3% of price) | annualised 20d 13.9%
Volume: 0.08x the 20-day average
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
Three-year record: +19.1% a year | beta to the market 0.98
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

<details><summary><b>What analysts and big funds say</b> — score +0.45</summary>

_Not available today._

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score +0.45</summary>

```text
Rolled up from the 5 largest holdings, 45.4% of the fund by weight
Ratings by weight: buy 78.7% | hold 21.3% | sell 0.0% (mean 1.90 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +18.2% above the current prices
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
Shares outstanding: 79.50M | fund size: 3.25B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Italy (EWI) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> No material macro surprise, technicals bearish but oversold with low volume, modest net inflows, and strong analyst buy rating covering just over half of the fund.

**Main reasons it gave:**
- No macro surprise: Treasury yields stable, inflation 3.4% within expectations
- Technical: price below 20‑day, 50‑day, and 200‑day SMAs; RSI 26.9 (oversold) with volume 0.07× 20‑day average
- Fund flows: share count up 6.7% week‑over‑week, indicating net inflows
- Analyst view: 100% buy rating on 53% of fund weight, weighted price target +19.6% above current price

<details><summary><b>News</b> — score +0.00</summary>

_No news found for this one today._

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.06% (+0.06 on the week) | 5-year 5.04% (-0.02 on the week) | 10-year 5.27% (-0.00 on the week) | 30-year 5.64% (+0.01 on the week)
Yield curve, 10-year minus 3-month: +1.22 points -- upward sloping (normal)
US dollar index: 102.26 (+0.33 on the week)
Volatility (VIX): 15.01 (-0.3 on the week) -- elevated
Latest US data: inflation 3.4% (2026-08-01) | unemployment 4.2% (2026-09-01) | jobless claims 197k (2026-10-03)
Policy and expectations: Fed target 4.00% | market expects 2.4% inflation over 10 years
Rate path: 2-year Treasury 4.77% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score -0.20</summary>

```text
Last close 56.09 (bar of 2026-10-09), from 502 daily bars
Trend: vs 20d SMA 59.13 (-5.1%), 50d 61.15 (-8.3%), 200d 58.07 (-3.4%); 50d above 200d
Momentum: RSI(14) 26.9 | MACD -1.346 vs signal -1.014 (histogram -0.332)
Returns: 1d +0.1% | 5d -2.3% | 1m -8.1% | 3m -7.2%
52-week range: 50.31 - 63.35 (now 44.3% of the way up)
Volatility: ATR(14) 0.84 (1.5% of price) | annualised 20d 19.0%
Volume: 0.07x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.30</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score +0.30</summary>

```text
Fund type: Focused Region
What it holds: P/E 14.42 | P/B 1.77 | P/S 1.50 | 3y earnings growth n/a
Yield: 3.2%
Three-year record: +28.7% a year | beta to the market 0.88
Cost and size: expense ratio 0.50% | net assets 1.17B
What it is made of: Stocks 99.9%, Cash 0.1%
Largest holdings: UniCredit SpA 18.0%, Intesa Sanpaolo 15.0%, Enel SpA 10.6%, Eni SpA 4.7%, Prysmian SpA 4.7%
Sector mix: Financial services 54.1%, Utilities 16.5%, Industrials 12.0%, Consumer cyclical 8.0%
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
Rolled up from the 5 largest holdings, 53.0% of the fund by weight
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 2.02 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +19.6% above the current prices
Holdings read: UCG.MI, ISP.MI, ENEL.MI, ENI.MI, PRY.MI
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
Share count change: 1 week: +6.7% (70.96M) over 7d
Shares outstanding: 20.28M | fund size: 1.14B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Japan (EWJ) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> No macro surprise or decisive technical breakout; mixed but modestly positive signals from analyst coverage, positioning, fund flows, and fundamentals lead to a neutral stance.

**Main reasons it gave:**
- Analyst view: 100% buy on top holdings with +15.6% price target, but only 17% of fund covered
- Positioning: CFTC net short fell 5% of open interest, now 1.4% short (reduced bearish bets)
- Fund flows: share count up 1.4% over week, indicating net inflows
- Technical: price just below 20‑day SMA, MACD histogram negative, volume 0.18× 20‑day average

<details><summary><b>News</b> — score +0.00</summary>

- [iShares MSCI EAFE ETF (EFA) Stock Price, News, Quote & History](https://ca.finance.yahoo.com/quote/EFA/)  
  <sub>Yahoo! Finance Canada, 4 hours ago</sub>  
  Find the latest iShares MSCI EAFE ETF (EFA) stock quote, history, news and other vital information to help you with your stock trading and investing.
- [Stocktwits Passport Portfolio: Wall Street Outpaces Asia As AI Trade Wobbles And Bond Yields Climb](https://stocktwits.com/news-articles/markets/equity/stocktwits-passport-portfolio-wall-street-outpaces-asia-as-ai-trade-wobbles-and-bond-yields-climb/cZD60nORBVY)  
  <sub>Stocktwits, 8 hours ago</sub>  
  The S&P 500 and Dow Jones Industrial Average are headed for marginal gains this week, even as South Korea, Japan, and Taiwan are poised to end lower.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.06% (+0.06 on the week) | 5-year 5.04% (-0.02 on the week) | 10-year 5.27% (-0.00 on the week) | 30-year 5.64% (+0.01 on the week)
Yield curve, 10-year minus 3-month: +1.22 points -- upward sloping (normal)
US dollar index: 102.26 (+0.33 on the week)
Volatility (VIX): 15.01 (-0.3 on the week) -- elevated
Latest US data: inflation 3.4% (2026-08-01) | unemployment 4.2% (2026-09-01) | jobless claims 197k (2026-10-03)
Policy and expectations: Fed target 4.00% | market expects 2.4% inflation over 10 years
Rate path: 2-year Treasury 4.77% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score -0.10</summary>

```text
Last close 97.49 (bar of 2026-10-09), from 502 daily bars
Trend: vs 20d SMA 97.64 (-0.2%), 50d 96.71 (+0.8%), 200d 90.84 (+7.3%); 50d above 200d
Momentum: RSI(14) 50.5 | MACD 0.445 vs signal 0.514 (histogram -0.068)
Returns: 1d +0.2% | 5d -1.4% | 1m +1.1% | 3m +5.1%
52-week range: 78.36 - 99.32 (now 91.3% of the way up)
Volatility: ATR(14) 1.33 (1.4% of price) | annualised 20d 16.9%
Volume: 0.18x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.30</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score +0.30</summary>

```text
Fund type: Japan Stock
What it holds: P/E 15.27 | P/B 1.98 | P/S 1.37 | 3y earnings growth n/a
Yield: 3.7%
Three-year record: +22.2% a year | beta to the market 0.83
Cost and size: expense ratio 0.49% | net assets 23.53B
What it is made of: Stocks 99.1%, Cash 0.9%
Largest holdings: Mitsubishi UFJ Financial Group Inc 4.7%, Toyota Motor Corp 3.3%, Tokyo Electron Ltd 3.1%, Sumitomo Mitsui Financial Group Inc 3.0%, Advantest Corp 3.0%
Sector mix: Industrials 22.8%, Technology 22.0%, Financial services 19.3%, Consumer cyclical 11.1%
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
Rolled up from the 5 largest holdings, 17.0% of the fund by weight  -- thin, so read this as a fact about that slice rather than the fund
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 1.73 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +15.6% above the current prices
Holdings read: 8306.T, 7203.T, 8035.T, 8316.T, 6857.T
Recent rating changes among them: none reported
```

</details>

<details><summary><b>Buying and selling by company insiders</b> — score +0.25</summary>

_Not available today._

</details>

<details><summary><b>Who is positioned how</b> — score +0.25</summary>

```text
Contract: NIKKEI STOCK AVERAGE YEN DENOM - CHICAGO MERCANTILE EXCHANGE (positions as of 2026-09-29, published the following Friday)
Large speculators: net short 1.4% of open interest (23,003 contracts)
Change on the week: -5.0% of open interest
Crowding: 15% percentile over 52 weeks -- within its normal range
Read this as crowding, not as a forecast: an extreme is as often the end of a move as the middle of one.
```

</details>

<details><summary><b>Money going into and out of this fund</b> — score +0.25</summary>

```text
Direction: money coming in (1 week)
Share count change: 1 week: +1.4% (317.25M) over 7d
Shares outstanding: 236.50M | fund size: 23.06B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Switzerland (EWL) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:** no explanation. It wrote only “NEUTRAL”, so the main reasons below are all it gave.

**Main reasons it gave:**
- Macro: yields stable, no policy surprise
- Technical: price below 20d SMA (-1.0%), RSI 37.1, volume 0.11x avg
- Analyst view: 64.8% buy, weighted price target +8.7% above price
- Fund flows: flat share count, 0% change over week

<details><summary><b>News</b> — score +0.00</summary>

_No news found for this one today._

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.06% (+0.06 on the week) | 5-year 5.04% (-0.02 on the week) | 10-year 5.27% (-0.00 on the week) | 30-year 5.64% (+0.01 on the week)
Yield curve, 10-year minus 3-month: +1.22 points -- upward sloping (normal)
US dollar index: 102.26 (+0.33 on the week)
Volatility (VIX): 15.01 (-0.3 on the week) -- elevated
Latest US data: inflation 3.4% (2026-08-01) | unemployment 4.2% (2026-09-01) | jobless claims 197k (2026-10-03)
Policy and expectations: Fed target 4.00% | market expects 2.4% inflation over 10 years
Rate path: 2-year Treasury 4.77% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 59.32 (bar of 2026-10-09), from 502 daily bars
Trend: vs 20d SMA 59.94 (-1.0%), 50d 61.93 (-4.2%), 200d 61.62 (-3.7%); 50d above 200d
Momentum: RSI(14) 37.1 | MACD -0.749 vs signal -0.780 (histogram 0.031)
Returns: 1d +0.1% | 5d +0.2% | 1m -1.6% | 3m -5.0%
52-week range: 55.06 - 65.08 (now 42.5% of the way up)
Volatility: ATR(14) 0.62 (1.0% of price) | annualised 20d 10.4%
Volume: 0.11x the 20-day average
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
Three-year record: +13.0% a year | beta to the market 0.91
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
Ratings by weight: buy 64.8% | hold 35.2% | sell 0.0% (mean 2.48 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +8.7% above the current prices
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
Direction: flat (1 week)
Share count change: 1 week: +0.0% (0.00) over 7d
Shares outstanding: 28.62M | fund size: 1.70B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Spain (EWP) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Neutral overall as there is no material macro surprise, technicals are mixed, flows are flat, and fundamentals unchanged.

**Main reasons it gave:**
- Macro data unchanged: yields stable, no policy surprise
- Technical indicators mixed: price below 20‑day and 50‑day SMAs, RSI 33.9 (oversold), low volume
- Fund flows flat over the week, indicating no net demand
- Analyst view modestly bullish: price target +5.1% above current and 51.5% buy rating

<details><summary><b>News</b> — score +0.00</summary>

_No news found for this one today._

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.06% (+0.06 on the week) | 5-year 5.04% (-0.02 on the week) | 10-year 5.27% (-0.00 on the week) | 30-year 5.64% (+0.01 on the week)
Yield curve, 10-year minus 3-month: +1.22 points -- upward sloping (normal)
US dollar index: 102.26 (+0.33 on the week)
Volatility (VIX): 15.01 (-0.3 on the week) -- elevated
Latest US data: inflation 3.4% (2026-08-01) | unemployment 4.2% (2026-09-01) | jobless claims 197k (2026-10-03)
Policy and expectations: Fed target 4.00% | market expects 2.4% inflation over 10 years
Rate path: 2-year Treasury 4.77% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 57.76 (bar of 2026-10-09), from 502 daily bars
Trend: vs 20d SMA 59.87 (-3.5%), 50d 61.36 (-5.9%), 200d 57.72 (+0.1%); 50d above 200d
Momentum: RSI(14) 33.9 | MACD -0.992 vs signal -0.756 (histogram -0.236)
Returns: 1d -0.2% | 5d -0.9% | 1m -6.0% | 3m -2.0%
52-week range: 48.33 - 63.23 (now 63.3% of the way up)
Volatility: ATR(14) 0.84 (1.4% of price) | annualised 20d 18.4%
Volume: 0.39x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.00</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score +0.00</summary>

```text
Fund type: Focused Region
What it holds: P/E 15.94 | P/B 2.15 | P/S 1.78 | 3y earnings growth n/a
Yield: 2.8%
Three-year record: +33.9% a year | beta to the market 0.88
Cost and size: expense ratio 0.50% | net assets 2.38B
What it is made of: Stocks 99.8%, Cash 0.2%
Largest holdings: Banco Santander SA 19.2%, Banco Bilbao Vizcaya Argentaria SA 14.3%, Iberdrola SA 12.8%, Repsol SA 5.0%, CaixaBank SA 4.5%
Sector mix: Financial services 45.6%, Utilities 20.7%, Industrials 14.1%, Technology 5.5%
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
Rolled up from the 5 largest holdings, 55.8% of the fund by weight
Ratings by weight: buy 51.5% | hold 48.5% | sell 0.0% (mean 2.26 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +5.1% above the current prices
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
Direction: flat (1 week)
Share count change: 1 week: +0.0% (0.00) over 7d
Shares outstanding: 37.35M | fund size: 2.16B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Taiwan (EWT) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> The fund shows a strong bullish analyst consensus and modest inflows, but technical momentum is weakening and there is no macro catalyst or surprise data to justify a directional tilt.

**Main reasons it gave:**
- Analyst view: 100% buy rating and +27% price target
- Fund flows: share count up 1.3% in the past week
- Technicals: price above 200‑day SMA (+26.7%) but MACD below signal and volume at 0.56× 20‑day average
- Macro: no rate or data surprise; yields stable, VIX low

<details><summary><b>News</b> — score +0.00</summary>

- [Stocktwits Passport Portfolio: Wall Street Outpaces Asia As AI Trade Wobbles And Bond Yields Climb](https://stocktwits.com/news-articles/markets/equity/stocktwits-passport-portfolio-wall-street-outpaces-asia-as-ai-trade-wobbles-and-bond-yields-climb/cZD60nORBVY)  
  <sub>Stocktwits, 8 hours ago</sub>  
  The S&P 500 and Dow Jones Industrial Average are headed for marginal gains this week, even as South Korea, Japan, and Taiwan are poised to end lower.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.06% (+0.06 on the week) | 5-year 5.04% (-0.02 on the week) | 10-year 5.27% (-0.00 on the week) | 30-year 5.64% (+0.01 on the week)
Yield curve, 10-year minus 3-month: +1.22 points -- upward sloping (normal)
US dollar index: 102.26 (+0.33 on the week)
Volatility (VIX): 15.01 (-0.3 on the week) -- elevated
Latest US data: inflation 3.4% (2026-08-01) | unemployment 4.2% (2026-09-01) | jobless claims 197k (2026-10-03)
Policy and expectations: Fed target 4.00% | market expects 2.4% inflation over 10 years
Rate path: 2-year Treasury 4.77% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 114.16 (bar of 2026-10-09), from 502 daily bars
Trend: vs 20d SMA 113.27 (+0.8%), 50d 108.90 (+4.8%), 200d 90.11 (+26.7%); 50d above 200d
Momentum: RSI(14) 54.3 | MACD 1.882 vs signal 2.113 (histogram -0.231)
Returns: 1d +0.7% | 5d -1.9% | 1m +4.8% | 3m +12.1%
52-week range: 60.03 - 118.00 (now 93.4% of the way up)
Volatility: ATR(14) 2.21 (1.9% of price) | annualised 20d 28.4%
Volume: 0.56x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.20</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score +0.20</summary>

```text
Fund type: Greater China Region
What it holds: P/E 28.15 | P/B 4.48 | P/S 2.64 | 3y earnings growth n/a
Yield: 0.9%
Three-year record: +46.5% a year | beta to the market 1.26
Cost and size: expense ratio 0.59% | net assets 12.34B
What it is made of: Stocks 99.8%, Cash 0.2%
Largest holdings: Taiwan Semiconductor Manufacturing Co Ltd 21.9%, MediaTek Inc 7.2%, Delta Electronics Inc 3.9%, Hon Hai Precision Industry Co Ltd 3.2%, ASE Technology Holding Co Ltd 3.0%
Sector mix: Technology 74.2%, Financial services 14.3%, Basic materials 3.8%, Industrials 2.8%
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
Rolled up from the 5 largest holdings, 39.1% of the fund by weight
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 1.35 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +27.0% above the current prices
Holdings read: 2330.TW, 2454.TW, 2308.TW, 2317.TW, 3711.TW
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
Share count change: 1 week: +1.3% (157.13M) over 7d
Shares outstanding: 104.75M | fund size: 11.96B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Mexico (EWW) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Neutral overall: technicals show price below key SMAs and modest weakness (RSI 40.7), while analyst coverage is strongly bullish (90.9% buy, +13% price target) and fundamentals are positive (low P/E 12.17, 3‑year return +13.9%/yr). No macro surprise and fund flows are flat, leading to a neutral directional call.

**Main reasons it gave:**
- Price below 20‑day, 50‑day and 200‑day SMAs
- RSI 40.7 indicating modest weakness
- Analyst coverage: 90.9% buy rating and +13% price target
- Fundamentals: low P/E 12.17 and 3‑year return +13.9% per year

<details><summary><b>News</b> — score +0.00</summary>

_No news found for this one today._

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.06% (+0.06 on the week) | 5-year 5.04% (-0.02 on the week) | 10-year 5.27% (-0.00 on the week) | 30-year 5.64% (+0.01 on the week)
Yield curve, 10-year minus 3-month: +1.22 points -- upward sloping (normal)
US dollar index: 102.26 (+0.33 on the week)
Volatility (VIX): 15.01 (-0.3 on the week) -- elevated
Latest US data: inflation 3.4% (2026-08-01) | unemployment 4.2% (2026-09-01) | jobless claims 197k (2026-10-03)
Policy and expectations: Fed target 4.00% | market expects 2.4% inflation over 10 years
Rate path: 2-year Treasury 4.77% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score -0.30</summary>

```text
Last close 71.38 (bar of 2026-10-09), from 502 daily bars
Trend: vs 20d SMA 72.63 (-1.7%), 50d 74.87 (-4.7%), 200d 75.87 (-5.9%); 50d below 200d
Momentum: RSI(14) 40.7 | MACD -1.034 vs signal -1.044 (histogram 0.010)
Returns: 1d -0.2% | 5d +0.4% | 1m -5.1% | 3m -3.7%
52-week range: 64.39 - 81.23 (now 41.5% of the way up)
Volatility: ATR(14) 1.28 (1.8% of price) | annualised 20d 19.5%
Volume: 0.11x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.30</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score +0.30</summary>

```text
Fund type: Focused Region
What it holds: P/E 12.17 | P/B 1.90 | P/S 1.42 | 3y earnings growth n/a
Yield: 3.5%
Three-year record: +13.9% a year | beta to the market 1.07
Cost and size: expense ratio 0.50% | net assets 1.49B
What it is made of: Stocks 99.4%, Cash 0.6%
Largest holdings: Grupo Mexico SAB de CV Class B 16.4%, Grupo Financiero Banorte SAB de CV Class O 11.1%, Fomento Economico Mexicano SAB de CV Units Cons. Of 1 Shs-B- And 4 Shs-D- 8.8%, America Movil SAB de CV Ordinary Shares - Class B 7.2%, Wal - Mart de Mexico SAB de CV 4.4%
Sector mix: Basic materials 26.8%, Consumer defensive 24.8%, Financial services 19.5%, Industrials 12.1%
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
Rolled up from the 5 largest holdings, 47.8% of the fund by weight
Ratings by weight: buy 90.9% | hold 9.1% | sell 0.0% (mean 2.16 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +13.0% above the current prices
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
Direction: flat (1 week)
Share count change: 1 week: +0.0% (0.00) over 7d
Shares outstanding: 18.90M | fund size: 1.35B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### South Korea (EWY) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:** no explanation. It wrote only “NEUTRAL”, so the main reasons below are all it gave.

**Main reasons it gave:**
- 6.2% share count outflow over the past week
- Price below 20‑day and 50‑day SMAs, RSI 44.7, MACD histogram negative
- Low P/E 10.41 and 3‑year return +50.6% per year
- No macro surprise; yields stable and VIX low

<details><summary><b>News</b> — score +0.00</summary>

- [Darden Wealth Group Inc's iShares MSCI South Korea ETF(EWY) Holding History](https://www.gurufocus.com/guru-portfolio/Darden%20Wealth%20Group%20Inc/EWY)  
  <sub>GuruFocus, 13 hours ago</sub>  
  iShares MSCI South Korea ETF(EWY) Buys and Sells Made by Darden Wealth Group Inc. Latest and Historical Data and Chart.
- [Stocktwits Passport Portfolio: Wall Street Outpaces Asia As AI Trade Wobbles And Bond Yields Climb](https://stocktwits.com/news-articles/markets/equity/stocktwits-passport-portfolio-wall-street-outpaces-asia-as-ai-trade-wobbles-and-bond-yields-climb/cZD60nORBVY)  
  <sub>Stocktwits, 8 hours ago</sub>  
  The S&P 500 and Dow Jones Industrial Average are headed for marginal gains this week, even as South Korea, Japan, and Taiwan are poised to end lower.
- [EWY Oct 2026 172.000 call (EWY261009C00172000) Stock Price, News, Quote & History](https://ca.finance.yahoo.com/quote/EWY261009C00172000/)  
  <sub>Yahoo! Finance Canada, 9 hours ago</sub>  
  Find the latest EWY Oct 2026 172.000 call (EWY261009C00172000) stock quote, history, news and other vital information to help you with your stock trading...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.06% (+0.06 on the week) | 5-year 5.04% (-0.02 on the week) | 10-year 5.27% (-0.00 on the week) | 30-year 5.64% (+0.01 on the week)
Yield curve, 10-year minus 3-month: +1.22 points -- upward sloping (normal)
US dollar index: 102.26 (+0.33 on the week)
Volatility (VIX): 15.01 (-0.3 on the week) -- elevated
Latest US data: inflation 3.4% (2026-08-01) | unemployment 4.2% (2026-09-01) | jobless claims 197k (2026-10-03)
Policy and expectations: Fed target 4.00% | market expects 2.4% inflation over 10 years
Rate path: 2-year Treasury 4.77% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score -0.20</summary>

```text
Last close 177.34 (bar of 2026-10-09), from 502 daily bars
Trend: vs 20d SMA 183.79 (-3.5%), 50d 179.33 (-1.1%), 200d 158.56 (+11.8%); 50d above 200d
Momentum: RSI(14) 44.7 | MACD 0.407 vs signal 1.695 (histogram -1.288)
Returns: 1d +0.6% | 5d -7.6% | 1m -3.0% | 3m +5.5%
52-week range: 80.72 - 219.20 (now 69.8% of the way up)
Volatility: ATR(14) 5.79 (3.3% of price) | annualised 20d 45.2%
Volume: 0.24x the 20-day average
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
Three-year record: +50.6% a year | beta to the market 2.48
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

<details><summary><b>Buying and selling by company insiders</b> — score -0.40</summary>

_Not available today._

</details>

<details><summary><b>Who is positioned how</b> — score -0.40</summary>

_Not available today._

</details>

<details><summary><b>Money going into and out of this fund</b> — score -0.40</summary>

```text
Direction: money going out (1 week)
Share count change: 1 week: -6.2% (-1.65B) over 7d
Shares outstanding: 139.63M | fund size: 24.76B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### South Africa (EZA) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> No macro surprise, flat fund flows, weak technical momentum, and a bullish analyst view covering less than half the fund. Overall conditions do not justify a directional tilt.

**Main reasons it gave:**
- Treasury yields stable (10‑yr 5.27% Δ0.00) – no rate surprise
- Fund flows flat: share count +0.0% week‑over‑week
- Technical momentum weak: RSI 40, MACD -1.587 vs signal -1.325
- Analyst view bullish (mean rating 2.09 → buy) covering 43.4% of fund

<details><summary><b>News</b> — score +0.00</summary>

_No news found for this one today._

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.06% (+0.06 on the week) | 5-year 5.04% (-0.02 on the week) | 10-year 5.27% (-0.00 on the week) | 30-year 5.64% (+0.01 on the week)
Yield curve, 10-year minus 3-month: +1.22 points -- upward sloping (normal)
US dollar index: 102.26 (+0.33 on the week)
Volatility (VIX): 15.01 (-0.3 on the week) -- elevated
Latest US data: inflation 3.4% (2026-08-01) | unemployment 4.2% (2026-09-01) | jobless claims 197k (2026-10-03)
Policy and expectations: Fed target 4.00% | market expects 2.4% inflation over 10 years
Rate path: 2-year Treasury 4.77% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 63.65 (bar of 2026-10-09), from 502 daily bars
Trend: vs 20d SMA 65.66 (-3.1%), 50d 67.88 (-6.2%), 200d 69.04 (-7.8%); 50d below 200d
Momentum: RSI(14) 40.0 | MACD -1.587 vs signal -1.325 (histogram -0.262)
Returns: 1d +1.6% | 5d +0.7% | 1m -8.5% | 3m +1.4%
52-week range: 60.43 - 81.60 (now 15.2% of the way up)
Volatility: ATR(14) 1.27 (2.0% of price) | annualised 20d 25.7%
Volume: 0.17x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.70</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score +0.70</summary>

```text
Fund type: Focused Region
What it holds: P/E 10.44 | P/B 2.00 | P/S 1.73 | 3y earnings growth n/a
Yield: 7.9%
Three-year record: +26.7% a year | beta to the market 1.07
Cost and size: expense ratio 0.59% | net assets 473.79M
What it is made of: Stocks 99.7%, Cash 0.3%
Largest holdings: Anglogold Ashanti PLC 12.7%, Gold Fields Ltd 8.7%, Naspers Ltd Class N 8.4%, Firstrand Ltd 7.4%, Standard Bank Group Ltd 6.2%
Sector mix: Basic materials 39.1%, Financial services 34.4%, Consumer cyclical 12.8%, Communication services 6.4%
```

</details>

<details><summary><b>Does this company beat its own forecasts</b> — score +0.70</summary>

_Not available today._

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

<details><summary><b>What analysts and big funds say</b> — score +0.46</summary>

_Not available today._

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score +0.46</summary>

```text
Rolled up from the 5 largest holdings, 43.4% of the fund by weight
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 2.09 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +32.5% above the current prices
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
Shares outstanding: 7.90M | fund size: 502.84M
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

**Data that was missing** (counted as 0.00, never guessed):
- news unavailable: Bright Data returned an empty body with its 200; nothing to parse

### Software (IGV) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Neutral overall view; analyst sentiment is bullish but limited in coverage, technicals are positive but on low volume, macro backdrop shows no surprise, and fund flows are flat.

**Main reasons it gave:**
- Analyst consensus: 100% buy, price target +9.7% above current (covers 42.9% of fund)
- Technicals: price above 20‑day, 50‑day, 200‑day SMAs, RSI 63.7, MACD positive, but volume only 0.14× 20‑day average
- Macro: Treasury yields stable, no policy surprise, VIX low at 15.0, indicating neutral backdrop
- Fund flows: flat share count over past week (0% net creation/redemption)

<details><summary><b>News</b> — score +0.00</summary>

- [How to Play AI Theme With ETFs Amid Overvaluation Concerns?](https://www.tradingview.com/news/zacks:804265d72094b:0-how-to-play-ai-theme-with-etfs-amid-overvaluation-concerns/)  
  <sub>TradingView, 3 hours ago</sub>  
  CNBC's Jim Cramer believes investors looking to ride the artificial intelligence (AI) boom should focus on established technology companies that have...
- [AI Agents Don't Clock Out, So Cloud Software Keeps Billing (NYSEARCA:XSW)](https://seekingalpha.com/article/4952875-ai-agents-dont-clock-out-so-cloud-software-keeps-billing)  
  <sub>Seeking Alpha, 21 hours ago</sub>  
  Software sector ETFs like XSW and IGV have rebounded YTD as AI fears around seat license erosion proved overblown. I expect the market to increasingly...
- [3 Financial Stocks Tied To AI Financing That Retail Investors May Be Missing](https://finance.yahoo.com/markets/stocks/articles/3-financial-stocks-tied-ai-043100024.html)  
  <sub>Yahoo Finance, 10 hours ago</sub>  
  AI hype is colliding with rising rates, pricier oil and a reality check on OpenAI revenue, and that mix is reshaping where capital flows in global markets.
- [Form 4 iShares Expanded Tech-Software Sector ETF For: 9 October](https://in.investing.com/news/stock-market-news/form-4-ishares-expanded-techsoftware-sector-etf-for-9-october-93CH-5625660)  
  <sub>Investing.com India, 4 hours ago</sub>  
  The information in this preliminary pricing supplement is not complete and may be changed. This preliminary pricing supplement and the accompanying...
- [JPMorgan Names Four Software Stock Picks as Rally Builds](https://www.tradingview.com/news/gurufocus:960465efd094b:0)  
  <sub>TradingView, 18 hours ago</sub>  
  JPMorgan expects the software rally to extend through third-quarter earnings, arguing that artificial intelligence is supporting infrastructure software...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.06% (+0.06 on the week) | 5-year 5.04% (-0.02 on the week) | 10-year 5.27% (-0.00 on the week) | 30-year 5.64% (+0.01 on the week)
Yield curve, 10-year minus 3-month: +1.22 points -- upward sloping (normal)
US dollar index: 102.26 (+0.33 on the week)
Volatility (VIX): 15.01 (-0.3 on the week) -- elevated
Latest US data: inflation 3.4% (2026-08-01) | unemployment 4.2% (2026-09-01) | jobless claims 197k (2026-10-03)
Policy and expectations: Fed target 4.00% | market expects 2.4% inflation over 10 years
Rate path: 2-year Treasury 4.77% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 111.54 (bar of 2026-10-09), from 502 daily bars
Trend: vs 20d SMA 107.40 (+3.8%), 50d 104.89 (+6.3%), 200d 93.70 (+19.0%); 50d above 200d
Momentum: RSI(14) 63.7 | MACD 1.810 vs signal 1.517 (histogram 0.293)
Returns: 1d +1.8% | 5d +2.9% | 1m +10.2% | 3m +20.3%
52-week range: 74.67 - 117.08 (now 86.9% of the way up)
Volatility: ATR(14) 2.32 (2.1% of price) | annualised 20d 25.1%
Volume: 0.14x the 20-day average
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
Three-year record: +16.8% a year | beta to the market 1.22
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
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 1.63 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +9.7% above the current prices
Holdings read: PANW, PLTR, CRWD, MSFT, ORCL
Recent rating changes among them:
  - PANW: 2026-10-08 Amerx: init, ? -> Hold
  - PLTR: 2026-10-09 Barclays: init, ? -> Overweight
  - CRWD: 2026-10-09 Needham: main, Buy -> Buy
  - MSFT: 2026-10-07 Evercore ISI Group: main, Outperform -> Outperform
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
Direction: flat (1 week)
Share count change: 1 week: +0.0% (0.00) over 7d
Shares outstanding: 12.50M | fund size: 1.39B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### India (INDA) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> No material macro surprise, no decisive technical break, and mixed fund‑specific signals lead to a neutral view.

**Main reasons it gave:**
- Share count fell 13.7% (-$909M) over the past week, indicating strong outflows
- Analyst coverage thin (23.7% of fund) but bullish (100% buy, +33.5% price target)
- Price below 20‑day, 50‑day and 200‑day SMAs; RSI 33 suggests oversold but no decisive breakout
- Macro: US Treasury yields stable, upward‑sloping curve, VIX low; no major data surprise

<details><summary><b>News</b> — score +0.00</summary>

- [FLIN: Economy Growing At A Fast Pace And Valuation Becoming Cheaper (Rating Upgrade)](https://seekingalpha.com/article/4952888-flin-economy-growing-at-a-fast-pace-and-valuation-becoming-cheaper-rating-upgrade)  
  <sub>Seeking Alpha, 20 hours ago</sub>  
  Franklin FTSE India ETF is upgraded from sell to hold as Indian asset valuations normalize. Click here to read this latest analysis of FLIN.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.06% (+0.06 on the week) | 5-year 5.04% (-0.02 on the week) | 10-year 5.27% (-0.00 on the week) | 30-year 5.64% (+0.01 on the week)
Yield curve, 10-year minus 3-month: +1.22 points -- upward sloping (normal)
US dollar index: 102.26 (+0.33 on the week)
Volatility (VIX): 15.01 (-0.3 on the week) -- elevated
Latest US data: inflation 3.4% (2026-08-01) | unemployment 4.2% (2026-09-01) | jobless claims 197k (2026-10-03)
Policy and expectations: Fed target 4.00% | market expects 2.4% inflation over 10 years
Rate path: 2-year Treasury 4.77% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score -0.20</summary>

```text
Last close 45.97 (bar of 2026-10-09), from 502 daily bars
Trend: vs 20d SMA 47.21 (-2.6%), 50d 48.70 (-5.6%), 200d 49.67 (-7.5%); 50d below 200d
Momentum: RSI(14) 33.0 | MACD -0.777 vs signal -0.672 (histogram -0.106)
Returns: 1d +0.9% | 5d -1.2% | 1m -4.5% | 3m -5.8%
52-week range: 45.42 - 55.29 (now 5.5% of the way up)
Volatility: ATR(14) 0.48 (1.0% of price) | annualised 20d 13.4%
Volume: 0.18x the 20-day average
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
Three-year record: +1.8% a year | beta to the market 0.62
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
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 1.36 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +33.5% above the current prices
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
Direction: money going out (1 week)
Share count change: 1 week: -13.7% (-909.45M) over 7d
Shares outstanding: 124.23M | fund size: 5.71B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Defence and aerospace (ITA) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> The fund shows mixed signals: analysts are strongly bullish (100% buy rating with a +30.9% price target), but recent fund flows indicate a sizable outflow (-10.5% share count, $1.40 B) and technicals are weak (price below all moving averages, low volume, RSI near oversold). Macro conditions are neutral with stable yields and no surprise data. The net effect is a neutral stance.

**Main reasons it gave:**
- Analyst view: 100% buy rating covering 53.9% of fund with +30.9% price target
- Fund flows: -10.5% share count decline (outflow $1.40B) over the past week
- Technical: RSI 30.6 (oversold) and MACD histogram positive but low volume and downtrend
- Macro: Treasury yields stable, normal upward sloping curve, no surprise data releases

<details><summary><b>News</b> — score +0.00</summary>

- [Bet on These Defense ETFs Amid Escalating Yemen War](https://finance.yahoo.com/markets/stocks/articles/bet-defense-etfs-amid-escalating-132300300.html)  
  <sub>Yahoo Finance, 1 hour ago</sub>  
  Houthi attacks on Saudi Arabia could boost defense spending, putting defense ETFs in focus as contractors brace for rising demand.
- [Trump says U.S. won't attack Iran before midterms, citing 'productive discussions' (ITA:BATS)](https://seekingalpha.com/news/4651480-trump-says-u-s-wont-attack-iran-before-midterms-citing-productive-discussions)  
  <sub>Seeking Alpha, 22 hours ago</sub>  
  Trump says no Iran strikes before Nov. 3 as Strait of Hormuz blockade holds; oil prices react after tanker attack and hurricane risks.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.06% (+0.06 on the week) | 5-year 5.04% (-0.02 on the week) | 10-year 5.27% (-0.00 on the week) | 30-year 5.64% (+0.01 on the week)
Yield curve, 10-year minus 3-month: +1.22 points -- upward sloping (normal)
US dollar index: 102.26 (+0.33 on the week)
Volatility (VIX): 15.01 (-0.3 on the week) -- elevated
Latest US data: inflation 3.4% (2026-08-01) | unemployment 4.2% (2026-09-01) | jobless claims 197k (2026-10-03)
Policy and expectations: Fed target 4.00% | market expects 2.4% inflation over 10 years
Rate path: 2-year Treasury 4.77% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score -0.10</summary>

```text
Last close 205.69 (bar of 2026-10-09), from 502 daily bars
Trend: vs 20d SMA 210.77 (-2.4%), 50d 227.34 (-9.5%), 200d 230.34 (-10.7%); 50d below 200d
Momentum: RSI(14) 30.6 | MACD -5.737 vs signal -6.025 (histogram 0.288)
Returns: 1d +0.4% | 5d -1.0% | 1m -5.8% | 3m -12.5%
52-week range: 198.23 - 253.22 (now 13.6% of the way up)
Volatility: ATR(14) 3.62 (1.8% of price) | annualised 20d 14.6%
Volume: 0.11x the 20-day average
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
Three-year record: +26.9% a year | beta to the market 0.98
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

<details><summary><b>What analysts and big funds say</b> — score +0.30</summary>

_Not available today._

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score +0.30</summary>

```text
Rolled up from the 5 largest holdings, 53.9% of the fund by weight
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 1.69 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +30.9% above the current prices
Holdings read: GE, RTX, BA, HWM, LMT
Recent rating changes among them:
  - GE: 2026-09-30 Wells Fargo: main, Overweight -> Overweight
  - RTX: 2026-10-09 Barclays: init, ? -> Overweight
  - BA: 2026-10-09 Barclays: init, ? -> Overweight
  - HWM: 2026-09-30 Wells Fargo: main, Equal-Weight -> Equal-Weight
  - LMT: 2026-10-09 Barclays: init, ? -> Equal-Weight
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
Direction: money going out (1 week)
Share count change: 1 week: -10.5% (-1.40B) over 7d
Shares outstanding: 58.28M | fund size: 11.99B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Transport and delivery (IYT) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Mixed signals: analysts are strongly bullish (100% buy, +26.9% price target) while fund flows show a sharp outflow of -14.8% share count over the week, indicating bearish sentiment. Technicals show price below the 50‑day and 200‑day SMAs, though MACD is bullish and RSI is modestly low. Macro data are stable with no policy surprise.

**Main reasons it gave:**
- Analyst coverage 100% buy with +26.9% price target
- Fund flows -14.8% share count over 1 week (outflows)
- Price below 50‑day SMA (-4.2%) and 200‑day SMA (-1.8%)
- Macro data stable: yields unchanged, VIX low, no policy surprise

<details><summary><b>News</b> — score +0.00</summary>

_No news found for this one today._

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.06% (+0.06 on the week) | 5-year 5.04% (-0.02 on the week) | 10-year 5.27% (-0.00 on the week) | 30-year 5.64% (+0.01 on the week)
Yield curve, 10-year minus 3-month: +1.22 points -- upward sloping (normal)
US dollar index: 102.26 (+0.33 on the week)
Volatility (VIX): 15.01 (-0.3 on the week) -- elevated
Latest US data: inflation 3.4% (2026-08-01) | unemployment 4.2% (2026-09-01) | jobless claims 197k (2026-10-03)
Policy and expectations: Fed target 4.00% | market expects 2.4% inflation over 10 years
Rate path: 2-year Treasury 4.77% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 79.91 (bar of 2026-10-09), from 502 daily bars
Trend: vs 20d SMA 79.92 (-0.0%), 50d 83.38 (-4.2%), 200d 81.38 (-1.8%); 50d above 200d
Momentum: RSI(14) 43.5 | MACD -1.055 vs signal -1.317 (histogram 0.261)
Returns: 1d -0.0% | 5d -0.4% | 1m -2.6% | 3m -9.2%
52-week range: 68.14 - 90.01 (now 53.8% of the way up)
Volatility: ATR(14) 1.12 (1.4% of price) | annualised 20d 14.3%
Volume: 0.17x the 20-day average
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
Three-year record: +12.4% a year | beta to the market 1.32
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
Weighted price target: +26.9% above the current prices
Holdings read: UNP, UBER, CSX, DAL, UAL
Recent rating changes among them:
  - UNP: 2026-10-07 Citigroup: main, Buy -> Buy
  - UBER: 2026-10-07 Citizens: reit, Market Outperform -> Market Outperform
  - CSX: 2026-10-07 Citigroup: main, Neutral -> Neutral
  - DAL: 2026-10-07 Bernstein: main, Outperform -> Outperform
  - UAL: 2026-10-07 Susquehanna: main, Positive -> Positive
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
Direction: money going out (1 week)
Share count change: 1 week: -14.8% (-327.01M) over 7d
Shares outstanding: 23.65M | fund size: 1.89B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### US regional banks (KRE) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> No material macro surprise, technicals lack decisive break, fund flows show outflows but analyst view and fundamentals are modestly positive.

**Main reasons it gave:**
- Fund flows: -7.3% share count decline over 7 days (outflows)
- Analyst view: 74.9% buy rating, +14.8% price target for top holdings (5.7% weight)
- Fund basics: P/E 12.02, P/B 1.21, yield 2.3% (low valuation, decent dividend)
- Technical: RSI 35 (oversold) with price below 20‑day SMA, volume 0.16× 20‑day average
- Macro: Yield curve normal (+1.22), no policy surprise; Fed likely to hike rates (4 hikes priced)

<details><summary><b>News</b> — score +0.00</summary>

- [Which Financial ETF is the Better Fit? Invesco KBW Bank ETF (KBWB) or iShares Regional Banks ETF (IAT)](https://www.fool.com/coverage/etfs/2026/10/09/which-financial-etf-is-the-better-fit-invesco-kbw-bank-etf-kbwb-or-ishares-regional-banks-etf-iat/)  
  <sub>The Motley Fool, 2 hours ago</sub>  
  KBWB delivered stronger 5-year returns and lower volatility, while IAT offers higher dividend income for yield-focused investors.
- [Midland States Bancorp Stock Rises With Regional Banks](https://admiralmarkets.com/analytics/traders-blog/midland-states-bancorp-stock-msbi-regional-banks)  
  <sub>Admirals, 16 hours ago</sub>  
  Midland States Bancorp stock (MSBI) rose with regional banks on 8 October 2026 after three losing sessions. Key levels, Q2 data and Q3 dates.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.06% (+0.06 on the week) | 5-year 5.04% (-0.02 on the week) | 10-year 5.27% (-0.00 on the week) | 30-year 5.64% (+0.01 on the week)
Yield curve, 10-year minus 3-month: +1.22 points -- upward sloping (normal)
US dollar index: 102.26 (+0.33 on the week)
Volatility (VIX): 15.01 (-0.3 on the week) -- elevated
Latest US data: inflation 3.4% (2026-08-01) | unemployment 4.2% (2026-09-01) | jobless claims 197k (2026-10-03)
Policy and expectations: Fed target 4.00% | market expects 2.4% inflation over 10 years
Rate path: 2-year Treasury 4.77% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 69.13 (bar of 2026-10-09), from 502 daily bars
Trend: vs 20d SMA 71.05 (-2.7%), 50d 73.70 (-6.2%), 200d 70.65 (-2.2%); 50d above 200d
Momentum: RSI(14) 35.0 | MACD -1.227 vs signal -1.174 (histogram -0.053)
Returns: 1d -0.7% | 5d -2.3% | 1m -6.3% | 3m -8.0%
52-week range: 58.14 - 77.93 (now 55.5% of the way up)
Volatility: ATR(14) 1.24 (1.8% of price) | annualised 20d 14.6%
Volume: 0.16x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.30</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score +0.30</summary>

```text
Fund type: Financial
What it holds: P/E 12.02 | P/B 1.21 | P/S 3.59 | 3y earnings growth n/a
Yield: 2.3%
Three-year record: +22.7% a year | beta to the market 1.04
Cost and size: expense ratio 0.35% | net assets 3.73B
What it is made of: Stocks 99.9%, Cash 0.1%
Largest holdings: United Bankshares Inc 1.1%, First Interstate BancSystem Inc 1.1%, Old National Bancorp 1.1%, Hancock Whitney Corp 1.1%, East West Bancorp Inc 1.1%
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

<details><summary><b>What analysts and big funds say</b> — score +0.30</summary>

_Not available today._

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score +0.30</summary>

```text
Rolled up from the 5 largest holdings, 5.7% of the fund by weight  -- thin, so read this as a fact about that slice rather than the fund
Ratings by weight: buy 74.9% | hold 25.1% | sell 0.0% (mean 2.14 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +14.8% above the current prices
Holdings read: UBSI, FIBK, ONB, HWC, EWBC
Recent rating changes among them:
  - UBSI: 2026-07-27 Keefe, Bruyette & Woods: main, Market Perform -> Market Perform
  - FIBK: 2026-10-05 Barclays: main, Underweight -> Underweight
  - ONB: 2026-10-06 Raymond James: up, Market Perform -> Outperform
  - HWC: 2026-10-05 Barclays: main, Overweight -> Overweight
  - EWBC: 2026-10-09 Truist Securities: main, Hold -> Hold
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
Direction: money going out (1 week)
Share count change: 1 week: -7.3% (-291.70M) over 7d
Shares outstanding: 53.23M | fund size: 3.68B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Saudi Arabia (KSA) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Neutral overall; bearish fund outflows and technical weakness offset bullish analyst view and stable macro backdrop.

**Main reasons it gave:**
- Fund flows: -8.9% share count change (redemptions) over 1 week
- Technicals: price below 20d, 50d, 200d SMAs; RSI 33.8 (oversold)
- Analyst view: 90.3% buy rating, weighted price target +18.9% above current price
- Macro: US Treasury yields stable, VIX low (15.01) and no surprise data

<details><summary><b>News</b> — score +0.00</summary>

_No news found for this one today._

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.06% (+0.06 on the week) | 5-year 5.04% (-0.02 on the week) | 10-year 5.27% (-0.00 on the week) | 30-year 5.64% (+0.01 on the week)
Yield curve, 10-year minus 3-month: +1.22 points -- upward sloping (normal)
US dollar index: 102.26 (+0.33 on the week)
Volatility (VIX): 15.01 (-0.3 on the week) -- elevated
Latest US data: inflation 3.4% (2026-08-01) | unemployment 4.2% (2026-09-01) | jobless claims 197k (2026-10-03)
Policy and expectations: Fed target 4.00% | market expects 2.4% inflation over 10 years
Rate path: 2-year Treasury 4.77% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score -0.30</summary>

```text
Last close 36.10 (bar of 2026-10-09), from 502 daily bars
Trend: vs 20d SMA 36.87 (-2.1%), 50d 37.71 (-4.2%), 200d 38.12 (-5.3%); 50d below 200d
Momentum: RSI(14) 33.8 | MACD -0.444 vs signal -0.406 (histogram -0.037)
Returns: 1d +0.0% | 5d -0.3% | 1m -5.6% | 3m -2.7%
52-week range: 35.83 - 41.03 (now 5.3% of the way up)
Volatility: ATR(14) 0.32 (0.9% of price) | annualised 20d 12.0%
Volume: 0.54x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.20</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score +0.20</summary>

```text
Fund type: Focused Region
What it holds: P/E 14.08 | P/B 1.70 | P/S 2.84 | 3y earnings growth n/a
Yield: 2.8%
Three-year record: +1.7% a year | beta to the market 0.19
Cost and size: expense ratio 0.75% | net assets 588.43M
What it is made of: Stocks 99.6%, Cash 0.4%
Largest holdings: Al Rajhi Bank 14.1%, Saudi Arabian Oil Co 11.5%, Saudi National Bank 8.6%, Saudi Telecom Co 6.1%, Saudi Arabian Mining Co 4.3%
Sector mix: Financial services 42.2%, Energy 12.5%, Basic materials 12.4%, Communication services 9.0%
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
Rolled up from the 5 largest holdings, 44.6% of the fund by weight
Ratings by weight: buy 90.3% | hold 9.7% | sell 0.0% (mean 2.08 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +18.9% above the current prices
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
Direction: money going out (1 week)
Share count change: 1 week: -8.9% (-56.54M) over 7d
Shares outstanding: 15.93M | fund size: 575.23M
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### China (MCHI) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Neutral overall – no material macro surprise, technicals lack a decisive break, and mixed sentiment from flows versus analyst optimism.

**Main reasons it gave:**
- Fund flows: -5.8% share count (outflows) over 1 week
- US dollar index up 0.33% on the week (strengthening)
- Analyst view: 100% buy rating, price target +56.4% above current price
- Technical trend: price below 20‑day, 50‑day, and 200‑day SMAs, indicating downtrend

<details><summary><b>News</b> — score +0.00</summary>

_No news found for this one today._

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.06% (+0.06 on the week) | 5-year 5.04% (-0.02 on the week) | 10-year 5.27% (-0.00 on the week) | 30-year 5.64% (+0.01 on the week)
Yield curve, 10-year minus 3-month: +1.22 points -- upward sloping (normal)
US dollar index: 102.26 (+0.33 on the week)
Volatility (VIX): 15.01 (-0.3 on the week) -- elevated
Latest US data: inflation 3.4% (2026-08-01) | unemployment 4.2% (2026-09-01) | jobless claims 197k (2026-10-03)
Policy and expectations: Fed target 4.00% | market expects 2.4% inflation over 10 years
Rate path: 2-year Treasury 4.77% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 52.42 (bar of 2026-10-09), from 502 daily bars
Trend: vs 20d SMA 52.56 (-0.3%), 50d 54.04 (-3.0%), 200d 56.60 (-7.4%); 50d below 200d
Momentum: RSI(14) 46.7 | MACD -0.579 vs signal -0.578 (histogram -0.001)
Returns: 1d +2.1% | 5d +2.3% | 1m -0.7% | 3m -0.2%
52-week range: 50.48 - 65.59 (now 12.8% of the way up)
Volatility: ATR(14) 0.69 (1.3% of price) | annualised 20d 18.1%
Volume: 0.78x the 20-day average
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
Three-year record: +9.3% a year | beta to the market 0.45
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
Weighted price target: +56.4% above the current prices
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
Direction: money going out (1 week)
Share count change: 1 week: -5.8% (-366.69M) over 7d
Shares outstanding: 114.15M | fund size: 5.98B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

**Data that was missing** (counted as 0.00, never guessed):
- news unavailable: Bright Data returned an empty body with its 200; nothing to parse

### Chip makers (SMH) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> No material macro surprise, no decisive technical break on heavy volume, mixed news; overall neutral stance.

**Main reasons it gave:**
- Fund flows: +6.1% share count increase (money inflow) in past week
- Analyst coverage: 44.3% of fund, all buy, price target +34.8% above current price
- Technical: price above 20d, 50d, 200d SMAs; RSI 53.8, MACD slightly positive
- Macro: Treasury yields stable, VIX low at 15.01, no policy surprise

<details><summary><b>News</b> — score +0.00</summary>

- [Nasdaq 100 Ends Lower As Report Of Weaker-Than-Expected OpenAI Revenue Drags Chipmakers — NVDA, DIS, ORCL, SBUX In Focus](https://www.tradingview.com/news/stocktwits:815daf0c7094b:0-nasdaq-100-ends-lower-as-report-of-weaker-than-expected-openai-revenue-drags-chipmakers-nvda-dis-orcl-sbux-in-focus/)  
  <sub>TradingView, 16 hours ago</sub>  
  U.S. stock indices ended lower on Thursday after reports showed OpenAI's annualized revenue was $20 billion below expectations, sparking a selloff in...
- [ETFs to Benefit as Nasdaq's Breakthrough Still Matters](https://www.theglobeandmail.com/investing/markets/stocks/TSLA/pressreleases/5089943/etfs-to-benefit-as-nasdaqs-breakthrough-still-matters/)  
  <sub>The Globe and Mail, 24 hours ago</sub>  
  The Nasdaq Composite extended its record-setting run as investors continued to favor technology and artificial intelligence (AI) stocks despite elevated...
- [S&P 500, Dow End Lower As Oil Prices Rise Amid US-Iran Crisis — PSKY, GOOGL, IREN, AMD, NVDA, AVGO In Focus](https://stocktwits.com/news-articles/markets/equity/s-and-p-500-dow-end-lower-as-oil-prices-rise-amid-us-iran-crisis/cZZiiqPR7H7)  
  <sub>Stocktwits, 9 hours ago</sub>  
  The S&P 500 and Dow ended lower on Monday over worries about soaring oil prices, while chipmaker stocks staged a comeback.
- [MSFT, ORCL, NVDA, QQQ In Focus: OpenAI’s Annualized Revenue Reportedly Trails Prior Expectations By $20B](https://www.tradingview.com/news/stocktwits:cbf78e9b6094b:0-msft-orcl-nvda-qqq-in-focus-openai-s-annualized-revenue-reportedly-trails-prior-expectations-by-20b/)  
  <sub>TradingView, 20 hours ago</sub>  
  OpenAI's annualized revenue is about $20 billion lower than previously indicated, financial documents provided to investors reveal, potentially cooling...
- [S&P 500, Dow Snap Three-Day Losses, Nasdaq Ends Best Day In Three Weeks As Earnings Take Centerstage — GOOGL, AAPL, AMD, TSLA, DIS In Focus](https://stocktwits.com/news-articles/markets/equity/s-and-p-500-dow-snap-three-day-losses-nasdaq-ends-best-day-in-three-weeks-earnings-take-centerstage/cZZS8knR7vC)  
  <sub>Stocktwits, 14 hours ago</sub>  
  U.S. stock indices ended higher on Tuesday, as a surge in chipmaker stocks and a strong set of earnings reports boosted investor sentiment.
- [Dow Ends Higher For Third Straight Session As Oil Cools, Nasdaq Slides On Chipmaker Rout — PYPL, SPCX, AAPL, V, F Stocks In Focus](https://stocktwits.com/news-articles/markets/equity/nasdaq-continues-to-drop-on-chipmaker-rout/cZZ6TnzRJbt)  
  <sub>Stocktwits, 13 hours ago</sub>  
  The S&P 500 ended 0.2% higher, while the Nasdaq 100 slipped 1% and the Dow Jones Industrial Average added 1%. Brent crude prices dropped close to 5% to end...
- [Nasdaq 100 Hits Record Highs As Investors Shrug Off Pressure From Soaring Yields — NVDA, SPCX, CRML, TSLA, QCOM In Focus](https://stocktwits.com/news-articles/markets/equity/nasdaq-100-hits-record-highs-as-investors-shrug-off-pressure-from-soaring-yields-nvda-spcx-crml-tsla-qcom-in-focus/cZDqO2yRBjp)  
  <sub>Stocktwits, 12 hours ago</sub>  
  U.S. stock indices ended higher on Monday, tracking sharp gains in chipmakers and broader technology stocks as investors shrugged off risk tied to soaring...
- [S&P 500, Dow End Lower As Blowout Jobs Report Fans Rate Hike Fears, While Chipmaker Strength Aids Nasdaq —TSLA, NFLX, BE, NVDA In Focus](https://stocktwits.com/news-articles/markets/equity/s-and-p-500-dow-end-lower-as-blowout-jobs-report-fans-rate-hike-fears-while-chipmaker-strength-aids-nasdaq-tsla-nflx-be-nvda-in-focus/cZsDjVKRJDg)  
  <sub>Stocktwits, 19 hours ago</sub>  
  Nonfarm payrolls grew by 162000 in August, while the unemployment rate held steady at 4.1%.
- [Nasdaq Posts Worst Drop Since April 2025, S&P 500 And Dow Drop As Strong Jobs Data Ignites Rate Hike Bets — TSLA, GME, META, BA, MSTR, GOOGL In Focus](https://stocktwits.com/news-articles/markets/equity/nasdaq-posts-worst-drop-since-april-2025-s-and-p-500-and-dow-drop-as-strong-jobs-data-ignites-rate-hike-bets-tsla-gme-meta-ba-mstr-in-focus/cZ0FUXKReCv)  
  <sub>Stocktwits, 22 hours ago</sub>  
  Nasdaq, S&P 500 and Dow Jones indices all ended the week ending June 5, lower.
- [S&P 500, Dow, Nasdaq Drop Under Pressure From Elevated Yields As Investors Shrug Off Trump’s Iran Sanction Relief — NVDA, BA, AMD, NVTS, CBRS In Focus](https://stocktwits.com/news-articles/markets/equity/s-and-p-500-dow-nasdaq-drop-under-pressure-from-elevated-yields/cZMjBLyRBXW)  
  <sub>Stocktwits, 14 hours ago</sub>  
  U.S. stock indices ended Monday lower as elevated Treasury yields continued to dampen the demand for riskier assets, while media reports suggested President...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.06% (+0.06 on the week) | 5-year 5.04% (-0.02 on the week) | 10-year 5.27% (-0.00 on the week) | 30-year 5.64% (+0.01 on the week)
Yield curve, 10-year minus 3-month: +1.22 points -- upward sloping (normal)
US dollar index: 102.26 (+0.33 on the week)
Volatility (VIX): 15.01 (-0.3 on the week) -- elevated
Latest US data: inflation 3.4% (2026-08-01) | unemployment 4.2% (2026-09-01) | jobless claims 197k (2026-10-03)
Policy and expectations: Fed target 4.00% | market expects 2.4% inflation over 10 years
Rate path: 2-year Treasury 4.77% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 605.03 (bar of 2026-10-09), from 502 daily bars
Trend: vs 20d SMA 597.14 (+1.3%), 50d 578.27 (+4.6%), 200d 506.25 (+19.5%); 50d above 200d
Momentum: RSI(14) 53.8 | MACD 13.397 vs signal 13.319 (histogram 0.078)
Returns: 1d -0.4% | 5d -4.1% | 1m +8.0% | 3m +3.3%
52-week range: 325.10 - 668.91 (now 81.4% of the way up)
Volatility: ATR(14) 14.83 (2.5% of price) | annualised 20d 31.4%
Volume: 0.39x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score -0.20</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score -0.20</summary>

```text
Fund type: Technology
What it holds: P/E 32.50 | P/B 11.65 | P/S 13.32 | 3y earnings growth n/a
Yield: 0.2%
Three-year record: +62.9% a year | beta to the market 2.00
Cost and size: expense ratio 0.35% | net assets 74.88B
What it is made of: Stocks 100.0%, Cash 0.0%
Largest holdings: NVIDIA Corp 19.3%, Taiwan Semiconductor Manufacturing Co Ltd ADR 9.3%, Advanced Micro Devices Inc 5.5%, Broadcom Inc 5.3%, Micron Technology Inc 4.9%
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
Rolled up from the 5 largest holdings, 44.3% of the fund by weight
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 1.34 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +34.8% above the current prices
Holdings read: NVDA, TSM, AMD, AVGO, MU
Recent rating changes among them:
  - NVDA: 2026-10-01 Cantor Fitzgerald: reit, Overweight -> Overweight
  - TSM: 2026-10-06 Barclays: main, Overweight -> Overweight
  - AMD: 2026-10-06 Citigroup: main, Buy -> Buy
  - AVGO: 2026-09-10 Piper Sandler: init, ? -> Overweight
  - MU: 2026-10-07 DA Davidson: main, Buy -> Buy
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
Direction: money coming in (1 week)
Share count change: 1 week: +6.1% (4.09B) over 7d
Shares outstanding: 118.41M | fund size: 71.64B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Turkey (TUR) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Technical downtrend with price below 20‑day, 50‑day and 200‑day SMAs; RSI near oversold; MACD negative. Analyst view overwhelmingly bullish (100% buy, +25.1% price target). Fund flows flat (no net creations/redemptions). Fundamentals show low valuations (P/E 11.69, P/B 1.02) but negative 3‑year return (-2.4% per year). No macro surprise or decisive technical break on heavy volume, so overall stance remains neutral.

**Main reasons it gave:**
- Technicals: price below 20‑day, 50‑day and 200‑day SMAs; RSI 31.6; MACD negative
- Analyst view: 100% buy rating; weighted price target +25.1% above current price
- Fund flows: flat over past week; share count unchanged (+0.0%)
- Fund fundamentals: low valuations (P/E 11.69, P/B 1.02) but negative 3‑year return (-2.4% per year)

<details><summary><b>News</b> — score +0.00</summary>

_No news found for this one today._

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.06% (+0.06 on the week) | 5-year 5.04% (-0.02 on the week) | 10-year 5.27% (-0.00 on the week) | 30-year 5.64% (+0.01 on the week)
Yield curve, 10-year minus 3-month: +1.22 points -- upward sloping (normal)
US dollar index: 102.26 (+0.33 on the week)
Volatility (VIX): 15.01 (-0.3 on the week) -- elevated
Latest US data: inflation 3.4% (2026-08-01) | unemployment 4.2% (2026-09-01) | jobless claims 197k (2026-10-03)
Policy and expectations: Fed target 4.00% | market expects 2.4% inflation over 10 years
Rate path: 2-year Treasury 4.77% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score -0.40</summary>

```text
Last close 33.97 (bar of 2026-10-09), from 502 daily bars
Trend: vs 20d SMA 35.94 (-5.5%), 50d 38.17 (-11.0%), 200d 39.30 (-13.6%); 50d below 200d
Momentum: RSI(14) 31.6 | MACD -1.368 vs signal -1.237 (histogram -0.131)
Returns: 1d +0.1% | 5d -0.9% | 1m -15.7% | 3m -11.1%
52-week range: 31.90 - 43.74 (now 17.5% of the way up)
Volatility: ATR(14) 0.66 (2.0% of price) | annualised 20d 35.0%
Volume: 0.12x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.20</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score +0.20</summary>

```text
Fund type: Focused Region
What it holds: P/E 11.69 | P/B 1.02 | P/S 0.63 | 3y earnings growth n/a
Yield: 2.5%
Three-year record: -2.4% a year | beta to the market 0.61
Cost and size: expense ratio 0.59% | net assets 163.33M
What it is made of: Stocks 99.7%, Cash 0.3%
Largest holdings: Aselsan Elektronik Sanayi Ve Ticaret AS 11.4%, Tupras-Turkiye Petrol Rafineleri AS 10.6%, Bim Birlesik Magazalar AS 10.4%, Akbank TAS 6.1%, Turk Hava Yollari AO 4.8%
Sector mix: Industrials 29.2%, Financial services 16.1%, Consumer defensive 13.9%, Basic materials 11.4%
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
Rolled up from the 5 largest holdings, 43.2% of the fund by weight
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 1.79 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +25.1% above the current prices
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

**In the model's own words:** no explanation. It wrote only “neutral”, so the main reasons below are all it gave.

**Main reasons it gave:**
- 10-year Treasury yield 5.27% compresses REIT valuations
- Share count down -5.6% week (-$3.93B) indicating outflows
- Price below 20d SMA (91.32) and 50d SMA (95.02) showing downtrend
- Analyst coverage 39.9% of fund, 100% buy rating but limited scope

<details><summary><b>News</b> — score +0.00</summary>

- [REET: The Two Enemies I Can't Ignore (NYSEARCA:REET)](https://seekingalpha.com/article/4952895-reet-the-two-enemies-i-cant-ignore)  
  <sub>Seeking Alpha, 19 hours ago</sub>  
  The iShares Global REIT ETF outlook worsens as inflation and 4%+ Treasury yields shrink real returns and REIT demand. Click to read more on REET.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.06% (+0.06 on the week) | 5-year 5.04% (-0.02 on the week) | 10-year 5.27% (-0.00 on the week) | 30-year 5.64% (+0.01 on the week)
Yield curve, 10-year minus 3-month: +1.22 points -- upward sloping (normal)
US dollar index: 102.26 (+0.33 on the week)
Volatility (VIX): 15.01 (-0.3 on the week) -- elevated
Latest US data: inflation 3.4% (2026-08-01) | unemployment 4.2% (2026-09-01) | jobless claims 197k (2026-10-03)
Policy and expectations: Fed target 4.00% | market expects 2.4% inflation over 10 years
Rate path: 2-year Treasury 4.77% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 90.15 (bar of 2026-10-09), from 502 daily bars
Trend: vs 20d SMA 91.32 (-1.3%), 50d 95.02 (-5.1%), 200d 94.38 (-4.5%); 50d above 200d
Momentum: RSI(14) 38.3 | MACD -1.712 vs signal -1.763 (histogram 0.051)
Returns: 1d +0.9% | 5d +0.7% | 1m -4.2% | 3m -7.8%
52-week range: 87.00 - 100.95 (now 22.6% of the way up)
Volatility: ATR(14) 1.17 (1.3% of price) | annualised 20d 13.0%
Volume: 0.25x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score -0.20</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score -0.20</summary>

```text
Fund type: Real Estate
What it holds: P/E 30.19 | P/B 2.59 | P/S 4.94 | 3y earnings growth n/a
Yield: 3.8%
Three-year record: +10.8% a year | beta to the market 0.98
Cost and size: expense ratio 0.13% | net assets 66.42B
What it is made of: Stocks 99.1%, Cash 0.7%, Other 0.2%
Largest holdings: Vanguard Real Estate II Index 14.5%, Welltower Inc 8.7%, Prologis Inc 6.9%, Equinix Inc 5.5%, American Tower Corp 4.3%
Sector mix: Real estate 99.4%, Communication services 0.4%, Energy 0.1%, Industrials 0.0%
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

<details><summary><b>What analysts and big funds say</b> — score +0.20</summary>

_Not available today._

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score +0.20</summary>

```text
Rolled up from the 5 largest holdings, 39.9% of the fund by weight
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 1.69 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +19.8% above the current prices
Holdings read: VRTPX, WELL, PLD, EQIX, AMT
Recent rating changes among them:
  - WELL: 2024-10-01 Wells Fargo: down, Overweight -> Equal-Weight
  - PLD: 2026-09-01 Wells Fargo: main, Overweight -> Overweight
  - EQIX: 2026-09-21 Rothschild & Co: init, ? -> Buy
  - AMT: 2026-09-30 Barclays: main, Overweight -> Overweight
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
Share count change: 1 week: -5.6% (-3.93B) over 7d
Shares outstanding: 738.63M | fund size: 66.59B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Biotech (XBI) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Neutral overall – no macro surprise, mixed technicals, modest outflows, and mixed analyst signals.

**Main reasons it gave:**
- Fund flows: -5.6% share count change over 1 week indicating outflows of $617M
- Technicals: price below 20‑day (155.25) and 50‑day (158.20) SMA, RSI 41, MACD negative, indicating bearish momentum
- Analyst view: 61% buy rating but weighted price target -14.2% suggests downside for holdings
- Macro: no policy or data surprise; yields stable, upward‑sloping curve, VIX low at 15

<details><summary><b>News</b> — score +0.00</summary>

- [Behavioral Patterns of XBI and Institutional Flows](https://news.stocktradersdaily.com/news_release/40/Behavioral_Patterns_of_XBI_and_Institutional_Flows_100926102001_1791555601.html)  
  <sub>Stock Traders Daily, 5 hours ago</sub>  
  Key findings for Spdr Biotech Etf (NYSE: XBI). Weak Near and Mid-Term Sentiment Could Challenge Long-Term Positive Outlook; A mid-channel oscillation...
- [Stocktwits Pharma Pulse: Roche Faces FDA Decision, Gene-Therapy Stocks Step Into Focus — The Week’s Biotech Watchlist](https://stocktwits.com/news-articles/markets/equity/stocktwits-pharma-pulse-roche-faces-fda-gene-therapy-stocks-week-biotech-watchlist/cZDpS8iRBSc)  
  <sub>Stocktwits, 8 hours ago</sub>  
  Rocket, RegenXBio, Precision BioSciences, Kyverna and uniQure will present on Monday at a cell and gene-therapy conference.
- [SLS, IBRX Eye Green Month As Biotech ETF Gains Steam: Analyst Sees ‘Continued Opportunities’ In Immuno-Oncology](https://stocktwits.com/news-articles/markets/equity/sls-ibrx-xbi-analyst-continued-opportunities-immuno-oncology/cZ1BDwKR7hT)  
  <sub>Stocktwits, 16 hours ago</sub>  
  XBI, which includes both SLS and IBRX, is on track for its strongest monthly performance since December 2023.
- [Biotech Stocks Need A Shot In The Arm After Brutal July: Could AstraZeneca-Bristol Myers Megadeal Be The Cure?](https://stocktwits.com/news-articles/markets/equity/biotech-stocks-brutal-july-astrazeneca-bristol-myers-megadeal-cure/cZoRxFHRJ5V)  
  <sub>Stocktwits, 22 hours ago</sub>  
  A potential AstraZeneca-Bristol Myers deal worth $400 billion would create one of the world's largest drugmakers and combine major cancer franchises.
- [This week in charts: What’s driving biotech’s recent pullback?](https://finance.yahoo.com/healthcare/articles/week-charts-driving-biotech-recent-142800164.html)  
  <sub>Yahoo Finance, 22 minutes ago</sub>  
  The latest installment in BioPharma Dive's data visualization series features a look at the factors pressuring biotech stocks of late and the frenetic pace...
- [Michael Burry Says His Puts Give Him 'Far More Upside' In A Crash As He Pulls His AI Bubble Timeline Forward](https://stocktwits.com/news-articles/markets/equity/michael-burry-puts-far-more-upside-crash-pulls-ai-bubble-timeline-forward/cZMnDzGRBWH)  
  <sub>Stocktwits, 4 hours ago</sub>  
  Fresh research accelerated Burry's bearish AI timeline from an earlier 2028 base case, prompting a shift toward more leveraged positions.
- [AAPL Stock Retreats From All-Time High: Research Firm Says Apple Could Sell 6M iPhone Duos This Year](https://stocktwits.com/news-articles/markets/equity/aapl-stock-retreats-from-all-time-high-research-firm-says-apple-could-sell-6-m-i-phone-duos-this-year/cZMnDDFRBWu)  
  <sub>Stocktwits, 12 hours ago</sub>  
  Apple's foldable bet, leadership transition, and expanding payments ecosystem are giving investors fresh factors to watch.
- [ASTS Stock Jumps Overnight As Japan D2C Launch With Rakuten Nears — Guinness World Record Sparks Fresh Optimism](https://stocktwits.com/news-articles/markets/equity/asts-japan-d2c-rakuten-guinness-world-record/cZoRCU3RJ58)  
  <sub>Stocktwits, 9 hours ago</sub>  
  BlueBirds 11, 12 and 13 are set to launch this week after the satellite arrays earned a Guinness World Record.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.06% (+0.06 on the week) | 5-year 5.04% (-0.02 on the week) | 10-year 5.27% (-0.00 on the week) | 30-year 5.64% (+0.01 on the week)
Yield curve, 10-year minus 3-month: +1.22 points -- upward sloping (normal)
US dollar index: 102.26 (+0.33 on the week)
Volatility (VIX): 15.01 (-0.3 on the week) -- elevated
Latest US data: inflation 3.4% (2026-08-01) | unemployment 4.2% (2026-09-01) | jobless claims 197k (2026-10-03)
Policy and expectations: Fed target 4.00% | market expects 2.4% inflation over 10 years
Rate path: 2-year Treasury 4.77% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score -0.30</summary>

```text
Last close 151.15 (bar of 2026-10-09), from 502 daily bars
Trend: vs 20d SMA 155.25 (-2.6%), 50d 158.20 (-4.5%), 200d 139.56 (+8.3%); 50d above 200d
Momentum: RSI(14) 41.0 | MACD -2.126 vs signal -1.464 (histogram -0.662)
Returns: 1d +1.2% | 5d -2.1% | 1m -3.6% | 3m -2.7%
52-week range: 104.99 - 169.55 (now 71.5% of the way up)
Volatility: ATR(14) 4.33 (2.9% of price) | annualised 20d 27.7%
Volume: 0.45x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.30</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score +0.30</summary>

```text
Fund type: Health
What it holds: P/E n/a | P/B 0.21 | P/S 0.12 | 3y earnings growth n/a
Yield: 0.3%
Three-year record: +28.1% a year | beta to the market 1.09
Cost and size: expense ratio 0.35% | net assets 10.36B
What it is made of: Stocks 100.0%, Cash 0.0%
Largest holdings: Twist Bioscience Corp 2.2%, Moderna Inc 2.0%, Natera Inc 1.8%, Iovance Biotherapeutics Inc 1.6%, Amgen Inc 1.5%
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

<details><summary><b>What analysts and big funds say</b> — score -0.20</summary>

_Not available today._

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score -0.20</summary>

```text
Rolled up from the 5 largest holdings, 9.2% of the fund by weight  -- thin, so read this as a fact about that slice rather than the fund
Ratings by weight: buy 61.1% | hold 38.9% | sell 0.0% (mean 2.06 on a 1=strong buy to 5=strong sell scale)
Weighted price target: -14.2% above the current prices
Holdings read: TWST, MRNA, NTRA, IOVA, AMGN
Recent rating changes among them:
  - TWST: 2026-10-08 Jefferies: init, ? -> Hold
  - MRNA: 2026-10-07 Morgan Stanley: main, Equal-Weight -> Equal-Weight
  - NTRA: 2026-10-07 Barclays: main, Overweight -> Overweight
  - IOVA: 2026-10-08 Baird: main, Neutral -> Neutral
  - AMGN: 2026-10-08 RBC Capital: main, Outperform -> Outperform
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
Direction: money going out (1 week)
Share count change: 1 week: -5.6% (-617.28M) over 7d
Shares outstanding: 68.64M | fund size: 10.38B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### US house builders (XHB) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Neutral overall: macro pressure from rising mortgage rates and bearish technicals offset by positive fund inflows and thin but bullish analyst coverage.

**Main reasons it gave:**
- Mortgage rates near 7.5% and rising for seventh week (negative for homebuilders)
- ETF price at $94.80 below 20‑day, 50‑day, and 200‑day SMAs (bearish technical trend)
- Share count rose 6.9% over the past week, indicating net inflows
- Analyst coverage thin (17% of fund) but 100% buy with +17.8% price target (bullish but limited impact)

<details><summary><b>News</b> — score +0.00</summary>

- [XHB Oct 2026 114.000 call (XHB261009C00114000) Interactive Stock Chart](https://ca.finance.yahoo.com/quote/XHB261009C00114000/chart/)  
  <sub>Yahoo! Finance Canada, 20 hours ago</sub>  
  Interactive Chart for XHB Oct 2026 114.000 call (XHB261009C00114000), analyze all the data with a huge range of indicators.
- [Mortgage rates near 7.5%, rises for seventh consecutive week (XLRE:NYSEARCA)](https://seekingalpha.com/news/4651468-mortgage-rates-near-75-rises-for-seventh-consecutive-week)  
  <sub>Seeking Alpha, 23 hours ago</sub>  
  Mortgage rates rose for the seventh straight week, approaching 7.5%, according to the Freddie Mac Weekly Mortgage Applications Survey.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.06% (+0.06 on the week) | 5-year 5.04% (-0.02 on the week) | 10-year 5.27% (-0.00 on the week) | 30-year 5.64% (+0.01 on the week)
Yield curve, 10-year minus 3-month: +1.22 points -- upward sloping (normal)
US dollar index: 102.26 (+0.33 on the week)
Volatility (VIX): 15.01 (-0.3 on the week) -- elevated
Latest US data: inflation 3.4% (2026-08-01) | unemployment 4.2% (2026-09-01) | jobless claims 197k (2026-10-03)
Policy and expectations: Fed target 4.00% | market expects 2.4% inflation over 10 years
Rate path: 2-year Treasury 4.77% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score -0.30</summary>

```text
Last close 94.80 (bar of 2026-10-09), from 502 daily bars
Trend: vs 20d SMA 96.88 (-2.2%), 50d 102.02 (-7.1%), 200d 105.91 (-10.5%); 50d below 200d
Momentum: RSI(14) 37.8 | MACD -1.705 vs signal -1.817 (histogram 0.112)
Returns: 1d -0.9% | 5d -2.0% | 1m -2.2% | 3m -11.5%
52-week range: 94.80 - 121.36 (now 0.0% of the way up)
Volatility: ATR(14) 2.17 (2.3% of price) | annualised 20d 19.3%
Volume: 0.17x the 20-day average
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
Three-year record: +10.0% a year | beta to the market 1.48
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
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 1.67 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +17.8% above the current prices
Holdings read: SN, CVCO, SKY, JCI, W
Recent rating changes among them:
  - SN: 2026-08-07 TD Cowen: main, Buy -> Buy
  - CVCO: 2026-09-30 Oppenheimer: init, ? -> Outperform
  - SKY: 2026-09-30 Oppenheimer: init, ? -> Perform
  - JCI: 2026-10-08 B of A Securities: main, Buy -> Buy
  - W: 2026-10-08 Baird: main, Neutral -> Neutral
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
Direction: money coming in (1 week)
Share count change: 1 week: +6.9% (90.19M) over 7d
Shares outstanding: 14.69M | fund size: 1.39B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### US materials and chemicals (XLB) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:** no explanation. It wrote only “NEUTRAL”, so the main reasons below are all it gave.

**Main reasons it gave:**
- Analyst consensus 100% buy with +13.7% price target for top holdings
- Fund flows flat: share count unchanged (+0.0% over 1 week)
- Technical momentum slight bullish: RSI 44.2, MACD above signal, but volume 0.19x 20‑day average
- Macro stable: yields unchanged, VIX low at 15.01, no data surprises

<details><summary><b>News</b> — score +0.00</summary>

- [State Street Consumer Discretionary Select Sector SPDR ETF (XLY) stock price, news, quote and history](https://sg.finance.yahoo.com/quote/XLY/)  
  <sub>Yahoo Finance Singapore, 5 hours ago</sub>  
  State Street Consumer Discretionary Select Sector SPDR ETF (XLY) · 2.67% · -2.00% · 0.80% · -6.45% · -5.49% · 22.33% · 782.65%. Key events.
- [(XLB) Pivots Trading Plans and Risk Controls (XLB:CA)](https://news.stocktradersdaily.com/canada/xlb-pivots-trading-plans-and-risk-controls_20261008_cb994e)  
  <sub>Stock Traders Daily, 16 hours ago</sub>  
  Pivot Points for iShares Core Canadian Long Term Bond Index ETF XLB that help investors see where to buy and sell XLB_.
- [Starbucks Eyes Chipotle, Could Restaurant M&A Be the Next ETF Trade? 5 Funds to Watch](https://www.tradingview.com/news/benzinga:41638d221094b:0-starbucks-eyes-chipotle-could-restaurant-m-a-be-the-next-etf-trade-5-funds-to-watch/)  
  <sub>TradingView, 20 hours ago</sub>  
  Starbucks Corp.'s NASDAQ:SBUX reported interest in acquiring Chipotle Mexican Grill Inc NYSE:CMG could put the spotlight on a broader restaurant...
- [8 Of 11 Sectors Fall In Thursday Trading As Energy Leads](https://www.benzinga.com/etfs/sector-etfs/26/10/62250165/8-of-11-sectors-fall-in-thursday-trading-as-energy-leads)  
  <sub>Benzinga, 24 hours ago</sub>  
  Three sectors are higher and eight are lower in Thursday's regular session, with the top three split across cyclical, defensive and growth groups.
- [S&P 500 Sector Outlook: Favor XLC And XLK, Underweight XLP With Uneven Earnings Leadership](https://seekingalpha.com/article/4952969-s-and-p-500-sector-outlook-favor-xlc-and-xlk-underweight-xlp-as-earnings-leadership-remains-uneven)  
  <sub>Seeking Alpha, 8 hours ago</sub>  
  S&P 500 outlook for 2027: earnings strong but revisions concentrated. See sector ratings—Buy XLC & XLK, Sell XLP—and allocation tips.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.06% (+0.06 on the week) | 5-year 5.04% (-0.02 on the week) | 10-year 5.27% (-0.00 on the week) | 30-year 5.64% (+0.01 on the week)
Yield curve, 10-year minus 3-month: +1.22 points -- upward sloping (normal)
US dollar index: 102.26 (+0.33 on the week)
Volatility (VIX): 15.01 (-0.3 on the week) -- elevated
Latest US data: inflation 3.4% (2026-08-01) | unemployment 4.2% (2026-09-01) | jobless claims 197k (2026-10-03)
Policy and expectations: Fed target 4.00% | market expects 2.4% inflation over 10 years
Rate path: 2-year Treasury 4.77% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 49.51 (bar of 2026-10-09), from 502 daily bars
Trend: vs 20d SMA 49.70 (-0.4%), 50d 51.33 (-3.5%), 200d 50.76 (-2.5%); 50d above 200d
Momentum: RSI(14) 44.2 | MACD -0.613 vs signal -0.681 (histogram 0.067)
Returns: 1d +0.5% | 5d +1.3% | 1m -2.5% | 3m -2.1%
52-week range: 42.23 - 53.67 (now 63.6% of the way up)
Volatility: ATR(14) 0.74 (1.5% of price) | annualised 20d 14.3%
Volume: 0.19x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.00</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score +0.00</summary>

```text
Fund type: Natural Resources
What it holds: P/E 22.69 | P/B 2.70 | P/S 1.78 | 3y earnings growth n/a
Yield: 1.8%
Three-year record: +10.5% a year | beta to the market 0.85
Cost and size: expense ratio 0.08% | net assets 7.78B
What it is made of: Stocks 99.8%, Cash 0.2%
Largest holdings: Linde PLC 12.2%, Newmont Corp 6.8%, Freeport-McMoRan Inc 5.6%, Ecolab Inc 4.7%, Sherwin-Williams Co 4.7%
Sector mix: Basic materials 83.2%, Consumer cyclical 16.8%
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
Rolled up from the 5 largest holdings, 34.1% of the fund by weight
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 1.70 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +13.7% above the current prices
Holdings read: LIN, NEM, FCX, ECL, SHW
Recent rating changes among them:
  - LIN: 2026-10-07 Citigroup: main, Buy -> Buy
  - NEM: 2026-09-16 RBC Capital: main, Outperform -> Outperform
  - FCX: 2026-10-08 UBS: main, Buy -> Buy
  - ECL: 2026-10-05 UBS: main, Buy -> Buy
  - SHW: 2026-10-05 UBS: main, Neutral -> Neutral
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
Shares outstanding: 71.92M | fund size: 3.56B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### US media and communication (XLC) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:** no explanation. It wrote only “neutral”, so the main reasons below are all it gave.

**Main reasons it gave:**
- Analyst coverage 90.6% buy with weighted price target +14.4% above current price
- Technical trend: price below 20‑day, 50‑day, and 200‑day SMAs; MACD negative
- Fund flows flat: share count +0.3% over the week
- Macro data stable: inflation 3.4% and yields unchanged, no surprise
- Sector outlook (Seeking Alpha) recommends buying XLC

<details><summary><b>News</b> — score +0.00</summary>

- [S&P 500 Sector Outlook: Favor XLC And XLK, Underweight XLP With Uneven Earnings Leadership](https://seekingalpha.com/article/4952969-s-and-p-500-sector-outlook-favor-xlc-and-xlk-underweight-xlp-as-earnings-leadership-remains-uneven)  
  <sub>Seeking Alpha, 8 hours ago</sub>  
  S&P 500 outlook for 2027: earnings strong but revisions concentrated. See sector ratings—Buy XLC & XLK, Sell XLP—and allocation tips.
- [Trump Made His Biggest August Buy a Tech Giant That Jumped Over 30% in Seven Weeks](https://247wallst.com/investing/2026/10/08/trump-made-his-biggest-august-buy-a-tech-giant-that-jumped-over-30-in-seven-weeks/)  
  <sub>24/7 Wall St., 20 hours ago</sub>  
  President Trump's largest August stock purchase landed in a tech company already moving fast, and the trade raises questions about what investors betting on...
- [8 Of 11 Sectors Fall In Thursday Trading As Energy Leads](https://www.benzinga.com/etfs/sector-etfs/26/10/62250165/8-of-11-sectors-fall-in-thursday-trading-as-energy-leads)  
  <sub>Benzinga, 24 hours ago</sub>  
  Three sectors are higher and eight are lower in Thursday's regular session, with the top three split across cyclical, defensive and growth groups.
- [VZ, TMUS, T Stock Price Targets Cut By Scotiabank – Analyst Sees Higher Risk Of Disruption From SpaceX Spectrum Deal](https://www.tradingview.com/news/stocktwits:f51f9f14c094b:0-vz-tmus-t-stock-price-targets-cut-by-scotiabank-analyst-sees-higher-risk-of-disruption-from-spacex-spectrum-deal/)  
  <sub>TradingView, 3 hours ago</sub>  
  Verizon Communications Inc. (VZ), T-Mobile US Inc. (TMUS), and AT&T Inc. (T) stocks remained in the spotlight as Scotiabank on Friday issued fresh price...
- [SpaceX Climbs 4% on Nationwide Low-Band Spectrum Deal for Starlink Mobile; Verizon and AT&T Drop 7%](https://247wallst.com/investing/2026/10/09/spacex-climbs-4-on-nationwide-low-band-spectrum-deal-for-starlink-mobile-verizon-and-att-drop-7/)  
  <sub>24/7 Wall St., 2 hours ago</sub>  
  SpaceX gained 4% on a nationwide low-band spectrum deal positioning Starlink as a direct cellular rival, while Verizon fell 7% and AT&T dropped 8%.
- [Skydance Climbs 5% as Buyers Return After Its Debut Selloff; Netflix and Walt Disney Edge Higher](https://247wallst.com/investing/2026/10/08/skydance-climbs-5-as-buyers-return-after-its-debut-selloff-netflix-and-walt-disney-edge-higher/)  
  <sub>24/7 Wall St., 23 hours ago</sub>  
  Skydance stock posted back-to-back losses from the moment its new NYSE listing began, and now buyers are rushing back in at a pace that dwarfs moves in...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.06% (+0.06 on the week) | 5-year 5.04% (-0.02 on the week) | 10-year 5.27% (-0.00 on the week) | 30-year 5.64% (+0.01 on the week)
Yield curve, 10-year minus 3-month: +1.22 points -- upward sloping (normal)
US dollar index: 102.26 (+0.33 on the week)
Volatility (VIX): 15.01 (-0.3 on the week) -- elevated
Latest US data: inflation 3.4% (2026-08-01) | unemployment 4.2% (2026-09-01) | jobless claims 197k (2026-10-03)
Policy and expectations: Fed target 4.00% | market expects 2.4% inflation over 10 years
Rate path: 2-year Treasury 4.77% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 111.44 (bar of 2026-10-09), from 502 daily bars
Trend: vs 20d SMA 112.25 (-0.7%), 50d 111.85 (-0.4%), 200d 113.67 (-2.0%); 50d below 200d
Momentum: RSI(14) 48.5 | MACD -0.185 vs signal -0.091 (histogram -0.094)
Returns: 1d -0.6% | 5d +1.0% | 1m -0.0% | 3m -0.1%
52-week range: 105.38 - 120.08 (now 41.3% of the way up)
Volatility: ATR(14) 1.55 (1.4% of price) | annualised 20d 20.5%
Volume: 0.20x the 20-day average
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
Three-year record: +20.0% a year | beta to the market 0.85
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
Weighted price target: +14.4% above the current prices
Holdings read: META, GOOGL, GOOG, WBD, DIS
Recent rating changes among them:
  - META: 2024-09-30 Cantor Fitzgerald: reit, Overweight -> Overweight
  - GOOGL: 2026-10-08 Needham: reit, Buy -> Buy
  - GOOG: 2026-10-08 TD Cowen: main, Buy -> Buy
  - WBD: 2026-09-29 Argus Research: down, Hold -> Sell
  - DIS: 2026-10-09 Needham: reit, Buy -> Buy
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
Share count change: 1 week: +0.3% (62.57M) over 7d
Shares outstanding: 201.86M | fund size: 22.50B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### US energy companies (XLE) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> No macro surprise; technical uptrend but low volume; flat fund flows; mixed fundamentals (bullish valuations vs bearish price outlook); mixed inventory signals.

**Main reasons it gave:**
- Flat fund flows (share count +0.0% over 7d)
- No macro surprise: Fed target unchanged at 4.00% and yields stable
- Technical uptrend (price above 20d, 50d, 200d SMAs) but low volume (0.21x 20-day avg)
- Mixed energy inventories: crude draw of -3.2M barrels (bullish) vs gas build of +85Bcf (bearish)
- EIA forecast predicts WTI price falling from $100 to $86 in six months (bearish)

<details><summary><b>News</b> — score +0.00</summary>

- [Exchange-Traded Funds, Equity Futures Up Pre-Bell Friday as Oil Prices Fall, Traders Assess SpaceX Spectrum Deal](https://ca.finance.yahoo.com/news/exchange-traded-funds-equity-futures-132619334.html)  
  <sub>Yahoo! Finance Canada, 1 hour ago</sub>  
  The broad market exchange-traded fund SPDR S&P 500 ETF Trust (SPY) was up 0.3%, and the actively tra.
- [Energy Leads State Street Premium Income ETF Returns, Flows](https://etfdb.com/sector-investing-content-hub/energy-leads-state-street-premium-income/)  
  <sub>ETF Database, 20 hours ago</sub>  
  Energy tops State Street's premium income ETF suite in returns and inflows, while utilities and consumer funds also draw cash.
- [Think 5% Treasury Yields Are Scary? This CEO Expects 8% - iShares TIPS Bond ETF (ARCA:TIP)](https://www.benzinga.com/etfs/sector-etfs/26/10/62269770/exclusive-think-5-treasury-yields-are-scary-this-ceo-says-8-is-coming)  
  <sub>Benzinga, 2 hours ago</sub>  
  Canary Capital CEO Steven McClurg sees 10-year Treasury yields hitting 8% within four years. TIPS and commodity ETFs could gain attention.
- [MLPI Is Inferior To Alternatives (BATS:MLPI)](https://seekingalpha.com/article/4952913-mlpi-is-inferior-to-alternatives)  
  <sub>Seeking Alpha, 17 hours ago</sub>  
  MLPI ETF may look like a smart way to diversify beyond AI with high income and energy infrastructure exposure—but red flags emerge. Click for more on MLPI.
- [Vanguard Utilities Index Fund ETF Shares (VPU) Stock Price, News, Quote & History](https://ca.finance.yahoo.com/quote/VPU/)  
  <sub>Yahoo! Finance Canada, 18 hours ago</sub>  
  Find the latest Vanguard Utilities Index Fund ETF Shares (VPU) stock quote, history, news and other vital information to help you with your stock trading...
- [8 Of 11 Sectors Fall In Thursday Trading As Energy Leads](https://www.benzinga.com/etfs/sector-etfs/26/10/62250165/8-of-11-sectors-fall-in-thursday-trading-as-energy-leads)  
  <sub>Benzinga, 24 hours ago</sub>  
  Three sectors are higher and eight are lower in Thursday's regular session, with the top three split across cyclical, defensive and growth groups.
- [Sector Update: Energy Stocks Gain Late Afternoon](https://finance.yahoo.com/energy/articles/sector-energy-stocks-gain-afternoon-195732427.html)  
  <sub>Yahoo Finance, 19 hours ago</sub>  
  Energy stocks were higher late Thursday afternoon, with the NYSE Energy Sector Index rising 3% and the State Street Energy Select Sector SPDR ETF (XLE)...
- [Sector Update: Energy Stocks Rise Thursday Afternoon](https://finance.yahoo.com/energy/articles/sector-energy-stocks-rise-thursday-175217724.html)  
  <sub>Yahoo Finance, 21 hours ago</sub>  
  Energy stocks were higher Thursday afternoon, with the NYSE Energy Sector Index rising 2.8% and the State Street Energy Select Sector SPDR ETF (XLE) up 3%.
- [Swisscanto CH Gold ETF (ZGLDUZ.XC) performance history](https://uk.finance.yahoo.com/quote/ZGLDUZ.XC/performance/)  
  <sub>Yahoo Finance UK, 15 hours ago</sub>  
  Cboe UK • USD. Swisscanto CH Gold ETF (ZGLDUZ.XC). 4,129.00 0.00 (0.00%). At close: 3 September at 10:14:42 BST. Trailing returns (%) vs. Benchmarks.
- [L U ETF I SEC C EUR (INDS.PA) holdings](https://uk.finance.yahoo.com/quote/INDS.PA/holdings/)  
  <sub>Yahoo Finance UK, 11 hours ago</sub>  
  View top holdings and key holding information for L U ETF I SEC C EUR (INDS.PA).

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.06% (+0.06 on the week) | 5-year 5.04% (-0.02 on the week) | 10-year 5.27% (-0.00 on the week) | 30-year 5.64% (+0.01 on the week)
Yield curve, 10-year minus 3-month: +1.22 points -- upward sloping (normal)
US dollar index: 102.26 (+0.33 on the week)
Volatility (VIX): 15.01 (-0.3 on the week) -- elevated
Latest US data: inflation 3.4% (2026-08-01) | unemployment 4.2% (2026-09-01) | jobless claims 197k (2026-10-03)
Policy and expectations: Fed target 4.00% | market expects 2.4% inflation over 10 years
Rate path: 2-year Treasury 4.77% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.20</summary>

```text
Last close 65.69 (bar of 2026-10-09), from 502 daily bars
Trend: vs 20d SMA 63.33 (+3.7%), 50d 62.68 (+4.8%), 200d 57.05 (+15.1%); 50d above 200d
Momentum: RSI(14) 64.5 | MACD 0.409 vs signal 0.173 (histogram 0.236)
Returns: 1d +0.7% | 5d +4.6% | 1m +1.2% | 3m +15.8%
52-week range: 42.61 - 65.93 (now 99.0% of the way up)
Volatility: ATR(14) 1.29 (2.0% of price) | annualised 20d 23.4%
Volume: 0.21x the 20-day average
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
Three-year record: +17.8% a year | beta to the market -0.03
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
US inventories, week ending 2026-10-02 (published the following Wednesday)
  Crude oil: 424.1 million barrels, -3.2 on the week (a draw), 40% percentile over 52 weeks
  Petrol: 204.7 million barrels, +0.4 on the week (a build), 4% percentile over 52 weeks -- low for the time of year
  Diesel: 105.1 million barrels, -0.0 on the week (a draw), 23% percentile over 52 weeks
  Natural gas: 3,500.0 billion cubic feet, +85.0 on the week (a build), 81% percentile over 52 weeks
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
Weighted price target: +1.2% above the current prices
Holdings read: XOM, CVX, COP, VLO, MPC
Recent rating changes among them:
  - XOM: 2026-10-01 Wells Fargo: down, Overweight -> Equal-Weight
  - CVX: 2026-10-08 UBS: main, Buy -> Buy
  - COP: 2026-10-07 Jefferies: main, Buy -> Buy
  - VLO: 2026-10-08 Jefferies: main, Hold -> Hold
  - MPC: 2026-10-08 Mizuho: main, Neutral -> Neutral
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
Shares outstanding: 186.42M | fund size: 12.25B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### US banks and finance (XLF) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Overall neutral outlook; no material macro surprise, mixed technicals, flat fund flows, and bullish analyst view limited to <50% of the fund.

**Main reasons it gave:**
- Flat fund flows (0% change) indicating no net demand
- Mixed technicals: short‑term price below 20‑day SMA, 50‑day SMA down, low volume
- No macro surprise: Fed target unchanged, yields stable, VIX low
- Analyst view bullish (+11.6% price target) but covers only 42.7% of fund

<details><summary><b>News</b> — score +0.00</summary>

- [Wells Fargo, State Street among financial stocks with A+ EPS revision grades (XLF:NYSEARCA)](https://seekingalpha.com/news/4651696-wells-fargo-state-street-among-financial-stocks-with-a-eps-revision-grades)  
  <sub>Seeking Alpha, 45 minutes ago</sub>  
  Q3 2026 earnings season: explore 16 financial stocks with A+ EPS Revision Quant Grades as analysts raise estimates across banks, insurers, fintech—read now.
- [Daily ETF Flows: EWZ Keeps Gathering Assets](https://finance.yahoo.com/markets/options/articles/daily-etf-flows-ewz-keeps-210004744.html)  
  <sub>Yahoo Finance, 18 hours ago</sub>  
  Here are the daily ETF fund flows for October 8, 2026.
- [S&P 500, Nasdaq, Dow Futures Edge Higher Ahead Of Fed Rate Decision: INTC, SNAP, SOFI, RUM In Focus](https://stocktwits.com/news-articles/markets/equity/sp500-nasdaq-dow-futures-edge-higher-ahead-of-fed-rate-decision/cZK0WgFR74u)  
  <sub>Stocktwits, 13 hours ago</sub>  
  The Dow surged to a fresh intraday record on Tuesday before finishing at an all-time closing high, marking its second straight record close.
- [What Drove XLF (NYSEARCA:XLF) Up 0.89% in a Split Sector Tape?](https://kalkine.ca/news/daily-wrap/what-drove-xlf-nysearcaxlf-up-089-in-a-split-sector-tape-1)  
  <sub>kalkine.ca, 2 hours ago</sub>  
  You are reading a free article with opinions that may differ from the recommendation given by Kalkine in its paid research reports. Become a Kalkine member...
- [Financial Stocks Rose As Waller Kept Rate Hikes On The Table](https://finimize.com/content/financial-stocks-rose-as-waller-kept-rate-hikes-on-the-table)  
  <sub>Finimize, 15 hours ago</sub>  
  The NYSE Financial Index gained 0.6% as the Fed governor said more tightening may be needed to get inflation back to 2% faster.
- [The RBI of Stanley Druckenmiller, a legendary Wall Street investor nicknamed the "investment machine..](https://www.mk.co.kr/en/stock/12172188)  
  <sub>매일경제, 15 hours ago</sub>  
  iShares MSCI Brazil (EWZ), bought by Drucken Miller, is up 33% this year. In particular, it soared 12% on the 5th (local time) alone, when Liberal candidate...
- [Exchange-Traded Funds, Equity Futures Up Pre-Bell Friday as Oil Prices Fall, Traders Assess SpaceX Spectrum Deal](https://finance.yahoo.com/markets/stocks/articles/exchange-traded-funds-equity-futures-132619334.html)  
  <sub>Yahoo Finance, 1 hour ago</sub>  
  The broad market exchange-traded fund SPDR S&P 500 ETF Trust (SPY) was up 0.3%, and the actively tra.
- [Sector Update: Financial Stocks Advance Late Afternoon](https://finance.yahoo.com/markets/stocks/articles/sector-financial-stocks-advance-afternoon-200612296.html)  
  <sub>Yahoo Finance, 19 hours ago</sub>  
  Financial stocks were rising in late Thursday afternoon trading, with the NYSE Financial Index up 0.3% and the State Street Financial Select Sector SPDR ETF...
- [Sector Update: Financial](https://finance.yahoo.com/markets/stocks/articles/sector-financial-194243493.html)  
  <sub>Yahoo Finance, 19 hours ago</sub>  
  Financial stocks were rising in late Thursday afternoon trading, with the NYSE Financial Index up 0.6% and the State Street Financial Select Sector SPDR ETF...
- [Sector Update: Financial Stocks Advance Thursday Afternoon](https://finance.yahoo.com/markets/stocks/articles/sector-financial-stocks-advance-thursday-175951196.html)  
  <sub>Yahoo Finance, 21 hours ago</sub>  
  Financial stocks were rising in Thursday afternoon trading, with the NYSE Financial Index fractionally higher and the State Street Financial Select Sector...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.06% (+0.06 on the week) | 5-year 5.04% (-0.02 on the week) | 10-year 5.27% (-0.00 on the week) | 30-year 5.64% (+0.01 on the week)
Yield curve, 10-year minus 3-month: +1.22 points -- upward sloping (normal)
US dollar index: 102.26 (+0.33 on the week)
Volatility (VIX): 15.01 (-0.3 on the week) -- elevated
Latest US data: inflation 3.4% (2026-08-01) | unemployment 4.2% (2026-09-01) | jobless claims 197k (2026-10-03)
Policy and expectations: Fed target 4.00% | market expects 2.4% inflation over 10 years
Rate path: 2-year Treasury 4.77% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 54.53 (bar of 2026-10-09), from 502 daily bars
Trend: vs 20d SMA 54.76 (-0.4%), 50d 56.53 (-3.5%), 200d 53.69 (+1.6%); 50d above 200d
Momentum: RSI(14) 43.3 | MACD -0.756 vs signal -0.817 (histogram 0.061)
Returns: 1d +0.6% | 5d +2.0% | 1m -4.1% | 3m -2.7%
52-week range: 47.81 - 58.56 (now 62.6% of the way up)
Volatility: ATR(14) 0.66 (1.2% of price) | annualised 20d 12.0%
Volume: 0.15x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.20</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score +0.20</summary>

```text
Fund type: Financial
What it holds: P/E 15.21 | P/B 2.25 | P/S 3.26 | 3y earnings growth n/a
Yield: 1.6%
Three-year record: +19.6% a year | beta to the market 0.75
Cost and size: expense ratio 0.08% | net assets 50.97B
What it is made of: Stocks 99.9%, Cash 0.1%
Largest holdings: Berkshire Hathaway Inc Class B 12.3%, JPMorgan Chase & Co 11.7%, Visa Inc Class A 8.1%, Mastercard Inc Class A 5.9%, Bank of America Corp 4.7%
Sector mix: Financial services 98.2%, Technology 1.6%, Industrials 0.2%
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
Rolled up from the 5 largest holdings, 42.7% of the fund by weight
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 1.80 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +11.6% above the current prices
Holdings read: BRK-B, JPM, V, MA, BAC
Recent rating changes among them:
  - BRK-B: 2026-08-10 UBS: main, Buy -> Buy
  - JPM: 2026-10-05 UBS: main, Buy -> Buy
  - V: 2026-08-31 RBC Capital: main, Outperform -> Outperform
  - MA: 2026-10-09 Baird: main, Outperform -> Outperform
  - BAC: 2026-10-05 UBS: main, Buy -> Buy
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
Shares outstanding: 883.44M | fund size: 48.18B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### US industry (XLI) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Neutral overall as there is no material macro surprise, technicals show modest weakness, flows are flat, and fundamentals are mixed.

**Main reasons it gave:**
- Fund flows flat (share count +0.0% over 7 days)
- Analyst coverage of top holdings (25.7% weight) is 100% buy with +22.4% price target
- Technical price below 20‑day SMA (169.05 vs 169.32) and volume 0.16× 20‑day average
- Fundamentals show high valuations (P/E 27.43, P/B 6.56) despite strong 3‑yr record (+21.1%/yr)

<details><summary><b>News</b> — score +0.00</summary>

- [Exchange-Traded Funds, Equity Futures Up Pre-Bell Friday as Oil Prices Fall, Traders Assess SpaceX Spectrum Deal](https://finance.yahoo.com/markets/stocks/articles/exchange-traded-funds-equity-futures-132619334.html)  
  <sub>Yahoo Finance, 1 hour ago</sub>  
  The broad market exchange-traded fund SPDR S&P 500 ETF Trust (SPY) was up 0.3%, and the actively tra.
- [S&P 500 Sector Outlook: Favor XLC And XLK, Underweight XLP With Uneven Earnings Leadership](https://seekingalpha.com/article/4952969-s-and-p-500-sector-outlook-favor-xlc-and-xlk-underweight-xlp-as-earnings-leadership-remains-uneven)  
  <sub>Seeking Alpha, 8 hours ago</sub>  
  S&P 500 outlook for 2027: earnings strong but revisions concentrated. See sector ratings—Buy XLC & XLK, Sell XLP—and allocation tips.
- [The Technology Select Sector SPDR® Fund (XLK) Stock Price | Quotes & News](https://www.moomoo.com/etfs/XLK-US)  
  <sub>Moomoo, 24 hours ago</sub>  
  Shift money among sector ETFs (XLK, XLE, XLV, XLU and so on) based on economic cycle stage or relative strength. Overweight leaders, underweight laggards,...
- [State Street Consumer Discretionary Select Sector SPDR ETF (XLY) stock price, news, quote and history](https://sg.finance.yahoo.com/quote/XLY/)  
  <sub>Yahoo Finance Singapore, 5 hours ago</sub>  
  Find the latest State Street Consumer Discretionary Select Sector SPDR ETF (XLY) stock quote, history, news and other vital information to help you with...
- [8 Of 11 Sectors Fall In Thursday Trading As Energy Leads](https://www.benzinga.com/etfs/sector-etfs/26/10/62250165/8-of-11-sectors-fall-in-thursday-trading-as-energy-leads)  
  <sub>Benzinga, 24 hours ago</sub>  
  Three sectors are higher and eight are lower in Thursday's regular session, with the top three split across cyclical, defensive and growth groups.
- [Tech Bull Ives Returns to Research: Names Top Five Picks for 2027, Bullish on Nvidia Ecosystem and the $4 Trillion AI Spending Wave](https://finance.biggo.com/news/c86bfe87-ebc9-4d0a-8e3d-3067032fd6e6)  
  <sub>BigGo Finance, 21 hours ago</sub>  
  Wall Street's well-known tech bull analyst Dan Ives has relaunched his technology research through the startup Yorkville Ives after leaving Wedbush…
- [Exchange-Traded Funds Drop as US Equities Fall After Midday](https://finance.yahoo.com/markets/articles/exchange-traded-funds-drop-us-171415436.html)  
  <sub>Yahoo Finance, 22 hours ago</sub>  
  Broad Market Indicators Broad-market exchange-traded funds IWM and IVV were lower. Actively traded Invesco QQQ Trust (QQQ) eased 1%.
- [Invesco S&P 500 Equal Weight ETF (RSP) Stock Price, News, Quote & History](https://ca.finance.yahoo.com/quote/RSP/)  
  <sub>Yahoo! Finance Canada, 23 hours ago</sub>  
  Find the latest Invesco S&P 500 Equal Weight ETF (RSP) stock quote, history, news and other vital information to help you with your stock trading and...
- [Sector Update: Tech Stocks Fall Thursday Afternoon](https://ca.finance.yahoo.com/news/sector-tech-stocks-fall-thursday-173838228.html)  
  <sub>Yahoo! Finance Canada, 21 hours ago</sub>  
  Tech stocks were lower Thursday afternoon, with the State Street Technology Select Sector SPDR ETF (XLK) falling 2% and the State Street SPDR S&P...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.06% (+0.06 on the week) | 5-year 5.04% (-0.02 on the week) | 10-year 5.27% (-0.00 on the week) | 30-year 5.64% (+0.01 on the week)
Yield curve, 10-year minus 3-month: +1.22 points -- upward sloping (normal)
US dollar index: 102.26 (+0.33 on the week)
Volatility (VIX): 15.01 (-0.3 on the week) -- elevated
Latest US data: inflation 3.4% (2026-08-01) | unemployment 4.2% (2026-09-01) | jobless claims 197k (2026-10-03)
Policy and expectations: Fed target 4.00% | market expects 2.4% inflation over 10 years
Rate path: 2-year Treasury 4.77% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score -0.10</summary>

```text
Last close 169.05 (bar of 2026-10-09), from 502 daily bars
Trend: vs 20d SMA 169.32 (-0.2%), 50d 175.71 (-3.8%), 200d 172.69 (-2.1%); 50d above 200d
Momentum: RSI(14) 43.6 | MACD -1.596 vs signal -1.958 (histogram 0.362)
Returns: 1d +0.4% | 5d -0.5% | 1m -0.9% | 3m -6.3%
52-week range: 147.83 - 186.51 (now 54.9% of the way up)
Volatility: ATR(14) 2.40 (1.4% of price) | annualised 20d 13.6%
Volume: 0.16x the 20-day average
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

<details><summary><b>What analysts and big funds say</b> — score +0.50</summary>

_Not available today._

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score +0.50</summary>

```text
Rolled up from the 5 largest holdings, 25.7% of the fund by weight
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 1.79 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +22.4% above the current prices
Holdings read: CAT, GE, GEV, RTX, DE
Recent rating changes among them:
  - CAT: 2024-10-14 JP Morgan: main, Overweight -> Overweight
  - GE: 2026-09-30 Wells Fargo: main, Overweight -> Overweight
  - GEV: 2026-09-15 Bernstein: reit, Outperform -> Outperform
  - RTX: 2026-10-09 Barclays: init, ? -> Overweight
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
Direction: flat (1 week)
Share count change: 1 week: +0.0% (0.00) over 7d
Shares outstanding: 136.63M | fund size: 23.10B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### US technology (XLK) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> No material macro surprise, technical uptrend but low volume, modest inflows, bullish analyst view covering half the fund, high valuation suggests limited upside.

**Main reasons it gave:**
- No macro surprise: yields stable, inflation 3.4% and unemployment 4.2% in line with expectations
- Technical uptrend: price above 20d, 50d, 200d SMAs, RSI 60.2, but volume 0.26x 20‑day average
- Fund flows positive: share count +0.9% (1.15B) over 7 days
- Analyst view bullish: 100% buy, price target +19.7% above current price (covers 49.5% of fund)
- High valuation: P/E 32.04 suggests limited upside

<details><summary><b>News</b> — score +0.00</summary>

_No news found for this one today._

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.06% (+0.06 on the week) | 5-year 5.04% (-0.02 on the week) | 10-year 5.27% (-0.00 on the week) | 30-year 5.64% (+0.01 on the week)
Yield curve, 10-year minus 3-month: +1.22 points -- upward sloping (normal)
US dollar index: 102.26 (+0.33 on the week)
Volatility (VIX): 15.01 (-0.3 on the week) -- elevated
Latest US data: inflation 3.4% (2026-08-01) | unemployment 4.2% (2026-09-01) | jobless claims 197k (2026-10-03)
Policy and expectations: Fed target 4.00% | market expects 2.4% inflation over 10 years
Rate path: 2-year Treasury 4.77% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.20</summary>

```text
Last close 198.18 (bar of 2026-10-09), from 502 daily bars
Trend: vs 20d SMA 194.49 (+1.9%), 50d 189.04 (+4.8%), 200d 166.38 (+19.1%); 50d above 200d
Momentum: RSI(14) 60.2 | MACD 3.510 vs signal 3.390 (histogram 0.120)
Returns: 1d +0.2% | 5d -0.8% | 1m +7.0% | 3m +9.3%
52-week range: 127.50 - 202.00 (now 94.9% of the way up)
Volatility: ATR(14) 3.04 (1.5% of price) | annualised 20d 17.8%
Volume: 0.26x the 20-day average
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
Three-year record: +34.8% a year | beta to the market 1.45
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
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 1.56 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +19.7% above the current prices
Holdings read: NVDA, AAPL, MSFT, AMD, AVGO
Recent rating changes among them:
  - NVDA: 2026-10-01 Cantor Fitzgerald: reit, Overweight -> Overweight
  - AAPL: 2026-10-01 Morgan Stanley: main, Overweight -> Overweight
  - MSFT: 2026-10-07 Evercore ISI Group: main, Outperform -> Outperform
  - AMD: 2026-10-06 Citigroup: main, Buy -> Buy
  - AVGO: 2026-09-10 Piper Sandler: init, ? -> Overweight
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
Share count change: 1 week: +0.9% (1.15B) over 7d
Shares outstanding: 630.34M | fund size: 124.92B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

**Data that was missing** (counted as 0.00, never guessed):
- news unavailable: Bright Data returned an empty body with its 200; nothing to parse

### US everyday goods (XLP) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:** no explanation. It wrote only “NEUTRAL”, so the main reasons below are all it gave.

**Main reasons it gave:**
- Flat fund flows (0% change) over the past week
- No macro surprise: Treasury yields stable, VIX low, inflation 3.4% near target
- Technical indicators modestly bullish (price above 20-day SMA, MACD above signal) but low volume (0.29x 20-day average)
- Analyst consensus 100% buy with weighted price target +9.4% for top holdings

<details><summary><b>News</b> — score +0.00</summary>

- [State Street Consumer Discretionary Select Sector SPDR ETF (XLY) stock price, news, quote and history](https://sg.finance.yahoo.com/quote/XLY/)  
  <sub>Yahoo Finance Singapore, 5 hours ago</sub>  
  State Street Consumer Discretionary Select Sector SPDR ETF (XLY) · 2.67% · -2.00% · 0.80% · -6.45% · -5.49% · 22.33% · 782.65%. Key events.
- [Consumer staples stocks with A+ EPS revision grades ahead of Q3 results (XLP:NYSEARCA)](https://seekingalpha.com/news/4651694-consumer-staples-stocks-with-a-eps-revision-grades-ahead-of-q3-results)  
  <sub>Seeking Alpha, 5 hours ago</sub>  
  Q3 2026 earnings season preview: 7 consumer staples stocks with A+ EPS revision grades (ADM, BJ, DAR, DG, SJM, USFD, WDFC).
- [Exchange-Traded Funds, Equity Futures Up Pre-Bell Friday as Oil Prices Fall, Traders Assess SpaceX Spectrum Deal](https://finance.yahoo.com/markets/stocks/articles/exchange-traded-funds-equity-futures-132619334.html)  
  <sub>Yahoo Finance, 1 hour ago</sub>  
  The broad market exchange-traded fund SPDR S&P 500 ETF Trust (SPY) was up 0.3%, and the actively tra.
- [Sector Update: Consumer Stocks Rise Late Afternoon](https://finance.yahoo.com/markets/stocks/articles/sector-consumer-stocks-rise-afternoon-195031530.html)  
  <sub>Yahoo Finance, 19 hours ago</sub>  
  Consumer stocks rose late Thursday afternoon with the State Street Consumer Staples Select Sector SPDR ETF (XLP) adding 2.2% and the State Street Consumer...
- [S&P 500 Sector Outlook: Favor XLC And XLK, Underweight XLP With Uneven Earnings Leadership](https://seekingalpha.com/article/4952969-s-and-p-500-sector-outlook-favor-xlc-and-xlk-underweight-xlp-as-earnings-leadership-remains-uneven)  
  <sub>Seeking Alpha, 8 hours ago</sub>  
  S&P 500 outlook for 2027: earnings strong but revisions concentrated. See sector ratings—Buy XLC & XLK, Sell XLP—and allocation tips.
- [Sector Update: Consumer](https://finance.yahoo.com/markets/stocks/articles/sector-consumer-171239120.html)  
  <sub>Yahoo Finance, 22 hours ago</sub>  
  Consumer stocks were higher Thursday afternoon, with the State Street Consumer Staples Select Sector SPDR ETF (XLP) adding 2.2% and the State Street...
- [Sector Update: Consumer Stocks Mixed Thursday Afternoon](https://finance.yahoo.com/markets/stocks/articles/sector-consumer-stocks-mixed-thursday-173208871.html)  
  <sub>Yahoo Finance, 21 hours ago</sub>  
  Consumer stocks were mixed Thursday afternoon, with the State Street Consumer Staples Select Sector SPDR ETF (XLP) adding 2.2% and the State Street Consumer...
- [PepsiCo Is Handing Market Share to Coca-Cola, Analyst Warns](https://www.benzinga.com/trading-ideas/movers/26/10/62255352/pepsico-is-handing-market-share-to-coca-cola-analyst-warns)  
  <sub>Benzinga, 21 hours ago</sub>  
  Coca-Cola stock gains as investors flock to defensive stocks and PepsiCo's beverage struggles fuel hopes of market-share gains.
- [Exchange-Traded Funds Drop as US Equities Fall After Midday](https://finance.yahoo.com/markets/articles/exchange-traded-funds-drop-us-171415436.html)  
  <sub>Yahoo Finance, 22 hours ago</sub>  
  Broad Market Indicators Broad-market exchange-traded funds IWM and IVV were lower. Actively traded Invesco QQQ Trust (QQQ) eased 1%.
- [Three beaten down consumer stocks that are now screaming opportunity](https://invezz.com/sg/news/2026/10/08/three-beaten-down-consumer-stocks-that-are-now-screaming-opportunity/)  
  <sub>Invezz, 24 hours ago</sub>  
  Wall Street is climbing without the consumer. Over three months, the S&P 500 has gained 4.3%, while the consumer staples ETF (XLP) has lost about 4%,...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.06% (+0.06 on the week) | 5-year 5.04% (-0.02 on the week) | 10-year 5.27% (-0.00 on the week) | 30-year 5.64% (+0.01 on the week)
Yield curve, 10-year minus 3-month: +1.22 points -- upward sloping (normal)
US dollar index: 102.26 (+0.33 on the week)
Volatility (VIX): 15.01 (-0.3 on the week) -- elevated
Latest US data: inflation 3.4% (2026-08-01) | unemployment 4.2% (2026-09-01) | jobless claims 197k (2026-10-03)
Policy and expectations: Fed target 4.00% | market expects 2.4% inflation over 10 years
Rate path: 2-year Treasury 4.77% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 83.25 (bar of 2026-10-09), from 502 daily bars
Trend: vs 20d SMA 82.27 (+1.2%), 50d 84.02 (-0.9%), 200d 83.81 (-0.7%); 50d above 200d
Momentum: RSI(14) 53.4 | MACD -0.524 vs signal -0.785 (histogram 0.261)
Returns: 1d -0.2% | 5d +3.4% | 1m +0.2% | 3m -1.6%
52-week range: 75.60 - 90.01 (now 53.1% of the way up)
Volatility: ATR(14) 0.98 (1.2% of price) | annualised 20d 14.1%
Volume: 0.29x the 20-day average
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
Three-year record: +10.0% a year | beta to the market 0.48
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

<details><summary><b>What analysts and big funds say</b> — score +0.60</summary>

_Not available today._

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score +0.60</summary>

```text
Rolled up from the 5 largest holdings, 41.8% of the fund by weight
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 1.80 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +9.4% above the current prices
Holdings read: WMT, COST, PG, KO, PM
Recent rating changes among them:
  - WMT: 2026-09-29 Mizuho: main, Outperform -> Outperform
  - COST: 2026-10-09 RBC Capital: reit, Sector Perform -> Sector Perform
  - PG: 2026-10-06 Evercore ISI Group: up, In-Line -> Outperform
  - KO: 2026-10-05 Wells Fargo: main, Overweight -> Overweight
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
Shares outstanding: 210.17M | fund size: 17.50B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### US electricity and water (XLU) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> No macro surprise, flat fund flows, mixed technicals, and a bullish analyst view without a catalyst lead to a neutral overall stance.

**Main reasons it gave:**
- Fund flows flat (share count unchanged over the week)
- US Treasury yields stable, no macro surprise or policy shift
- Utilities sector pressured by high yields (NiSource stock falls as yields near 5.3%)
- Technicals: price below 50‑day and 200‑day SMA, low volume, no decisive break
- Analyst consensus bullish (80.6% buy, +19% price target) but lacking macro catalyst

<details><summary><b>News</b> — score +0.00</summary>

- [NiSource Stock Falls as Utilities Slide on 5.3% Yields](https://admiralmarkets.com/analytics/traders-blog/nisource-stock-utilities-xlu-treasury-yields)  
  <sub>Admirals, 18 hours ago</sub>  
  NiSource stock slips with the XLU ETF as the 10-year Treasury yield nears 5.3%. Mortgage rates at 7.40%, jobless claims 197k, gas storage +85 Bcf.
- [GMAC ETF Holds 98% in Treasury Bills. How Is It Trading Gold and Silver?](https://www.ebc.com/forex/gmac-etf-treasury-bills-gold-silver-swaps)  
  <sub>EBC Financial Group, 10 hours ago</sub>  
  Nearly 98% of the Simplify Brookwood Global Macro ETF's (GMAC) reported net assets were held in just two US Treasury bills on October 6, one day after its...
- [32 ETFs Add to NextEra Energy (NEE) on Oct. 7](https://www.gurufocus.com/news/9116961/32-etfs-add-to-nextera-energy-nee-on-oct-7)  
  <sub>GuruFocus, 3 hours ago</sub>  
  On Wednesday, 32 ETFs were buying NextEra Energy (NEE) shares versus 16 selling, for a net $29.4 million in ETF buying. ETF activity has now favored the...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.06% (+0.06 on the week) | 5-year 5.04% (-0.02 on the week) | 10-year 5.27% (-0.00 on the week) | 30-year 5.64% (+0.01 on the week)
Yield curve, 10-year minus 3-month: +1.22 points -- upward sloping (normal)
US dollar index: 102.26 (+0.33 on the week)
Volatility (VIX): 15.01 (-0.3 on the week) -- elevated
Latest US data: inflation 3.4% (2026-08-01) | unemployment 4.2% (2026-09-01) | jobless claims 197k (2026-10-03)
Policy and expectations: Fed target 4.00% | market expects 2.4% inflation over 10 years
Rate path: 2-year Treasury 4.77% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 41.14 (bar of 2026-10-09), from 502 daily bars
Trend: vs 20d SMA 40.47 (+1.6%), 50d 42.23 (-2.6%), 200d 44.33 (-7.2%); 50d below 200d
Momentum: RSI(14) 50.5 | MACD -0.450 vs signal -0.723 (histogram 0.273)
Returns: 1d +0.2% | 5d +3.3% | 1m -3.2% | 3m -10.0%
52-week range: 39.25 - 47.73 (now 22.3% of the way up)
Volatility: ATR(14) 0.62 (1.5% of price) | annualised 20d 17.7%
Volume: 0.17x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.20</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score +0.20</summary>

```text
Fund type: Utilities
What it holds: P/E 17.86 | P/B 2.04 | P/S 2.49 | 3y earnings growth n/a
Yield: 3.1%
Three-year record: +16.3% a year | beta to the market 0.40
Cost and size: expense ratio 0.08% | net assets 21.33B
What it is made of: Stocks 99.8%, Cash 0.2%
Largest holdings: NextEra Energy Inc 12.7%, Southern Co 7.7%, Duke Energy Corp 7.2%, Constellation Energy Corp 6.7%, American Electric Power Co Inc 5.2%
Sector mix: Utilities 100.0%
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
Rolled up from the 5 largest holdings, 39.5% of the fund by weight
Ratings by weight: buy 80.6% | hold 19.4% | sell 0.0% (mean 2.02 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +19.1% above the current prices
Holdings read: NEE, SO, DUK, CEG, AEP
Recent rating changes among them:
  - NEE: 2026-10-06 Mizuho: main, Neutral -> Neutral
  - SO: 2026-09-25 Citigroup: main, Buy -> Buy
  - DUK: 2026-10-09 Barclays: main, Overweight -> Overweight
  - CEG: 2026-10-06 Bernstein: reit, Outperform -> Outperform
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
Shares outstanding: 163.27M | fund size: 6.72B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### US health care (XLV) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Neutral overall as there is no macro surprise, technicals show modest upward trend without decisive break, and fund flows indicate only modest net inflow despite bullish analyst coverage.

**Main reasons it gave:**
- Treasury yields stable (3‑month 4.06% +0.06, 10‑year 5.27% -0.00) and VIX down 0.3 to 15.01
- Price above 20‑day (168.59), 50‑day (168.88) and 200‑day (157.05) SMAs, RSI 51.8, low volume (0.22× 20‑day avg)
- Share count up 0.9% (409.76M) over the week, indicating modest net inflow
- Analyst view covers 44.3% of fund, all buy, weighted price target +11.8% above current price

<details><summary><b>News</b> — score +0.00</summary>

- [These healthcare stocks have the highest EPS revision grade ahead of Q3 results (XLV:NYSEARCA)](https://seekingalpha.com/news/4651695-these-healthcare-stocks-have-the-highest-eps-revision-grade-ahead-of-q3-results)  
  <sub>Seeking Alpha, 2 hours ago</sub>  
  Q3 2026 earnings season watchlist: 20 healthcare stocks with A+ EPS revision grades (Agilent, Amgen, CVS, Tenet).
- [Humana Soars 16% on Improved Medicare Advantage Star Ratings; CVS Slides 3%, UnitedHealth Holds Steady](https://247wallst.com/investing/2026/10/09/humana-soars-16-on-improved-medicare-advantage-star-ratings-cvs-slides-3-unitedhealth-holds-steady/)  
  <sub>24/7 Wall St., 2 hours ago</sub>  
  A single Medicare quality ratings release sent one major insurer soaring while dragging a rival into the red, and the gap between winners and losers points...
- [Stocktwits Pharma Pulse: Roche Faces FDA Decision, Gene-Therapy Stocks Step Into Focus — The Week’s Biotech Watchlist](https://stocktwits.com/news-articles/markets/equity/stocktwits-pharma-pulse-roche-faces-fda-gene-therapy-stocks-week-biotech-watchlist/cZDpS8iRBSc)  
  <sub>Stocktwits, 8 hours ago</sub>  
  Rocket, RegenXBio, Precision BioSciences, Kyverna and uniQure will present on Monday at a cell and gene-therapy conference.
- [Exchange-Traded Funds, Equity Futures Up Pre-Bell Friday as Oil Prices Fall, Traders Assess SpaceX Spectrum Deal](https://finance.yahoo.com/markets/stocks/articles/exchange-traded-funds-equity-futures-132619334.html)  
  <sub>Yahoo Finance, 1 hour ago</sub>  
  The broad market exchange-traded fund SPDR S&P 500 ETF Trust (SPY) was up 0.3%, and the actively tra.
- [ETFs Bought $19.3 Million of Eli Lilly (LLY) on Wednesday](https://www.gurufocus.com/news/9116971/etfs-bought-193-million-of-eli-lilly-lly-on-wednesday)  
  <sub>GuruFocus, 3 hours ago</sub>  
  ETF flows into Eli Lilly (LLY) totaled a net $19.3 million in Wednesday's session, as 34 ETFs bought shares and 16 sold. The buying marked a second straight...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.06% (+0.06 on the week) | 5-year 5.04% (-0.02 on the week) | 10-year 5.27% (-0.00 on the week) | 30-year 5.64% (+0.01 on the week)
Yield curve, 10-year minus 3-month: +1.22 points -- upward sloping (normal)
US dollar index: 102.26 (+0.33 on the week)
Volatility (VIX): 15.01 (-0.3 on the week) -- elevated
Latest US data: inflation 3.4% (2026-08-01) | unemployment 4.2% (2026-09-01) | jobless claims 197k (2026-10-03)
Policy and expectations: Fed target 4.00% | market expects 2.4% inflation over 10 years
Rate path: 2-year Treasury 4.77% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 169.01 (bar of 2026-10-09), from 502 daily bars
Trend: vs 20d SMA 168.59 (+0.2%), 50d 168.88 (+0.1%), 200d 157.05 (+7.6%); 50d above 200d
Momentum: RSI(14) 51.8 | MACD -0.158 vs signal -0.076 (histogram -0.082)
Returns: 1d +0.5% | 5d +1.7% | 1m +2.0% | 3m +4.7%
52-week range: 141.95 - 175.68 (now 80.2% of the way up)
Volatility: ATR(14) 2.61 (1.5% of price) | annualised 20d 11.2%
Volume: 0.22x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.20</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score +0.20</summary>

```text
Fund type: Health
What it holds: P/E 30.01 | P/B 4.74 | P/S 1.66 | 3y earnings growth n/a
Yield: 1.5%
Three-year record: +10.5% a year | beta to the market 0.52
Cost and size: expense ratio 0.08% | net assets 43.39B
What it is made of: Stocks 99.8%, Cash 0.2%
Largest holdings: Eli Lilly and Co 15.1%, Johnson & Johnson 10.4%, AbbVie Inc 7.5%, Merck & Co Inc 5.8%, UnitedHealth Group Inc 5.4%
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

<details><summary><b>What analysts and big funds say</b> — score +0.40</summary>

_Not available today._

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score +0.40</summary>

```text
Rolled up from the 5 largest holdings, 44.3% of the fund by weight
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 1.72 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +11.8% above the current prices
Holdings read: LLY, JNJ, ABBV, MRK, UNH
Recent rating changes among them:
  - LLY: 2026-10-08 Cantor Fitzgerald: main, Overweight -> Overweight
  - JNJ: 2026-10-07 Guggenheim: reit, Buy -> Buy
  - ABBV: 2026-10-09 Guggenheim: reit, Buy -> Buy
  - MRK: 2026-10-08 Cantor Fitzgerald: main, Neutral -> Neutral
  - UNH: 2026-07-21 JP Morgan: main, Overweight -> Overweight
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
Share count change: 1 week: +0.9% (409.76M) over 7d
Shares outstanding: 259.71M | fund size: 43.89B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### US shopping and leisure (XLY) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Mixed evidence: strong analyst consensus but significant outflows and mixed technicals; macro backdrop unchanged.

**Main reasons it gave:**
- Fund flows: -8.7% share count (outflows) over 1 week
- Analyst consensus: 100% buy, weighted price target +18.6% above current price
- Technical: price below 50‑day and 200‑day SMA, MACD bullish but volume 0.25× 20‑day average
- Macro: yields stable, no policy surprise, VIX low at 15.0

<details><summary><b>News</b> — score +0.00</summary>

- [State Street Consumer Discretionary Select Sector SPDR ETF (XLY) stock price, news, quote and history](https://sg.finance.yahoo.com/quote/XLY/)  
  <sub>Yahoo Finance Singapore, 5 hours ago</sub>
- [Chipotle Takeover Buzz: 5 ETFs to Watch as Restaurant M&A Heats Up - Chipotle Mexican Grill (NYSE:CMG)](https://www.benzinga.com/etfs/sector-etfs/26/10/62257479/starbucks-eyes-chipotle-could-restaurant-ma-be-the-next-etf-trade-5-funds-to-watch)  
  <sub>Benzinga, 20 hours ago</sub>  
  Starbucks' reported Chipotle takeover interest could spark a broader restaurant M&A trade. Here are 5 ETFs offering exposure to potential beneficiaries.
- [Top 10 consumer discretionary stocks with A+ EPS revision grades ahead of Q3 earnings (XLY:NYSEARCA)](https://seekingalpha.com/news/4651693-top-10-consumer-discretionary-stocks-with-a-eps-revision-grades-ahead-of-q3-earnings)  
  <sub>Seeking Alpha, 5 hours ago</sub>  
  As Q3 2026 earnings season approaches, consumer discretionary stocks are drawing investor attention as markets assess consumer spending trends across...
- [Exchange-Traded Funds, Equity Futures Up Pre-Bell Friday as Oil Prices Fall, Traders Assess SpaceX Spectrum Deal](https://finance.yahoo.com/markets/stocks/articles/exchange-traded-funds-equity-futures-132619334.html)  
  <sub>Yahoo Finance, 1 hour ago</sub>
- [What's Going On With Starbucks Stock Friday?](https://www.benzinga.com/analyst-stock-ratings/analyst-color/26/10/62270770/whats-going-on-with-starbucks-stock-friday)  
  <sub>Benzinga, 2 hours ago</sub>  
  Starbucks Corporation (NASDAQ:SBUX) stock edged lower Friday as investors weighed reports of a potential acquisition of Chipotle Mexican Grill Inc.
- [Sector Update: Consumer Stocks Rise Late Afternoon](https://finance.yahoo.com/markets/stocks/articles/sector-consumer-stocks-rise-afternoon-195031530.html)  
  <sub>Yahoo Finance, 19 hours ago</sub>
- [Sector Update: Consumer](https://finance.yahoo.com/markets/stocks/articles/sector-consumer-171239120.html)  
  <sub>Yahoo Finance, 22 hours ago</sub>
- [Sector Update: Consumer Stocks Mixed Thursday Afternoon](https://finance.yahoo.com/markets/stocks/articles/sector-consumer-stocks-mixed-thursday-173208871.html)  
  <sub>Yahoo Finance, 21 hours ago</sub>

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.06% (+0.06 on the week) | 5-year 5.04% (-0.02 on the week) | 10-year 5.27% (-0.00 on the week) | 30-year 5.64% (+0.01 on the week)
Yield curve, 10-year minus 3-month: +1.22 points -- upward sloping (normal)
US dollar index: 102.26 (+0.33 on the week)
Volatility (VIX): 15.01 (-0.3 on the week) -- elevated
Latest US data: inflation 3.4% (2026-08-01) | unemployment 4.2% (2026-09-01) | jobless claims 197k (2026-10-03)
Policy and expectations: Fed target 4.00% | market expects 2.4% inflation over 10 years
Rate path: 2-year Treasury 4.77% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 112.76 (bar of 2026-10-09), from 502 daily bars
Trend: vs 20d SMA 110.81 (+1.8%), 50d 114.41 (-1.4%), 200d 116.12 (-2.9%); 50d below 200d
Momentum: RSI(14) 54.2 | MACD -0.705 vs signal -1.177 (histogram 0.472)
Returns: 1d +0.9% | 5d +2.5% | 1m +0.7% | 3m -2.8%
52-week range: 105.66 - 124.52 (now 37.6% of the way up)
Volatility: ATR(14) 1.42 (1.3% of price) | annualised 20d 13.8%
Volume: 0.25x the 20-day average
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
Three-year record: +12.6% a year | beta to the market 1.18
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

<details><summary><b>What analysts and big funds say</b> — score +0.60</summary>

_Not available today._

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score +0.60</summary>

```text
Rolled up from the 5 largest holdings, 54.4% of the fund by weight
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 1.80 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +18.6% above the current prices
Holdings read: AMZN, TSLA, HD, MCD, TJX
Recent rating changes among them:
  - AMZN: 2026-10-06 Tigress Financial: main, Buy -> Buy
  - TSLA: 2026-10-08 Tigress Financial: main, Buy -> Buy
  - HD: 2026-09-09 Bernstein: main, Market Perform -> Market Perform
  - MCD: 2026-10-08 Bernstein: main, Market Perform -> Market Perform
  - TJX: 2026-08-26 Jefferies: down, Buy -> Hold
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
Direction: money going out (1 week)
Share count change: 1 week: -8.7% (-2.04B) over 7d
Shares outstanding: 190.39M | fund size: 21.47B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Argentina (ARGT) · Sector or country — no answer, no confidence given

<details><summary><b>News</b> — score n/a</summary>

- [The RBI of Stanley Druckenmiller, a legendary Wall Street investor nicknamed the "investment machine..](https://www.mk.co.kr/en/stock/12172188)  
  <sub>매일경제, 15 hours ago</sub>  
  iShares MSCI Brazil (EWZ), bought by Drucken Miller, is up 33% this year. In particular, it soared 12% on the 5th (local time) alone, when Liberal candidate...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score n/a</summary>

```text
US Treasury yields: 3-month 4.06% (+0.06 on the week) | 5-year 5.04% (-0.02 on the week) | 10-year 5.27% (-0.00 on the week) | 30-year 5.64% (+0.01 on the week)
Yield curve, 10-year minus 3-month: +1.22 points -- upward sloping (normal)
US dollar index: 102.26 (+0.33 on the week)
Volatility (VIX): 15.01 (-0.3 on the week) -- elevated
Latest US data: inflation 3.4% (2026-08-01) | unemployment 4.2% (2026-09-01) | jobless claims 197k (2026-10-03)
Policy and expectations: Fed target 4.00% | market expects 2.4% inflation over 10 years
Rate path: 2-year Treasury 4.77% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score n/a</summary>

```text
Last close 88.71 (bar of 2026-10-09), from 502 daily bars
Trend: vs 20d SMA 89.79 (-1.2%), 50d 92.28 (-3.9%), 200d 92.53 (-4.1%); 50d below 200d
Momentum: RSI(14) 44.7 | MACD -1.567 vs signal -1.658 (histogram 0.091)
Returns: 1d +0.6% | 5d +5.0% | 1m -8.4% | 3m -6.1%
52-week range: 70.49 - 102.94 (now 56.1% of the way up)
Volatility: ATR(14) 1.85 (2.1% of price) | annualised 20d 28.4%
Volume: 0.20x the 20-day average
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
Three-year record: +32.1% a year | beta to the market 0.45
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
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 1.65 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +32.6% above the current prices
Holdings read: MELI, YPF, VIST, GGAL, PAM
Recent rating changes among them:
  - MELI: 2026-10-06 Susquehanna: main, Positive -> Positive
  - YPF: 2026-09-01 JP Morgan: main, Overweight -> Overweight
  - VIST: 2026-09-01 JP Morgan: main, Overweight -> Overweight
  - GGAL: 2026-06-25 JP Morgan: main, Overweight -> Overweight
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
Direction: money going out (1 week)
Share count change: 1 week: -15.3% (-127.78M) over 7d
Shares outstanding: 8.00M | fund size: 709.69M
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Poland (EPOL) · Sector or country — no answer, no confidence given

<details><summary><b>News</b> — score n/a</summary>

_No news found for this one today._

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score n/a</summary>

```text
US Treasury yields: 3-month 4.06% (+0.06 on the week) | 5-year 5.04% (-0.02 on the week) | 10-year 5.27% (-0.00 on the week) | 30-year 5.64% (+0.01 on the week)
Yield curve, 10-year minus 3-month: +1.22 points -- upward sloping (normal)
US dollar index: 102.26 (+0.33 on the week)
Volatility (VIX): 15.01 (-0.3 on the week) -- elevated
Latest US data: inflation 3.4% (2026-08-01) | unemployment 4.2% (2026-09-01) | jobless claims 197k (2026-10-03)
Policy and expectations: Fed target 4.00% | market expects 2.4% inflation over 10 years
Rate path: 2-year Treasury 4.77% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score n/a</summary>

```text
Last close 43.65 (bar of 2026-10-09), from 502 daily bars
Trend: vs 20d SMA 44.35 (-1.6%), 50d 44.31 (-1.5%), 200d 39.74 (+9.8%); 50d above 200d
Momentum: RSI(14) 46.0 | MACD -0.195 vs signal -0.045 (histogram -0.150)
Returns: 1d +0.5% | 5d +1.4% | 1m -3.3% | 3m +8.7%
52-week range: 31.78 - 45.76 (now 84.9% of the way up)
Volatility: ATR(14) 0.68 (1.6% of price) | annualised 20d 22.0%
Volume: 0.08x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score n/a</summary>

```text
Fund type: Focused Region
What it holds: P/E 13.22 | P/B 2.06 | P/S 1.40 | 3y earnings growth n/a
Yield: 3.3%
Three-year record: +44.3% a year | beta to the market 0.64
Cost and size: expense ratio 0.59% | net assets 833.96M
What it is made of: Stocks 99.1%, Cash 0.9%
Largest holdings: PKO Bank Polski SA 16.2%, Orlen SA 12.7%, Bank Polska Kasa Opieki SA 7.4%, Powszechny Zaklad Ubezpieczen SA 6.0%, Allegro.EU SA Ordinary Shares 4.9%
Sector mix: Financial services 46.9%, Energy 13.3%, Consumer cyclical 13.2%, Basic materials 6.2%
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
Rolled up from the 5 largest holdings, 47.1% of the fund by weight
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 2.17 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +2.2% above the current prices
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
Direction: money going out (1 week)
Share count change: 1 week: -2.4% (-20.18M) over 7d
Shares outstanding: 18.73M | fund size: 817.52M
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### United Kingdom (EWU) · Sector or country — no answer, no confidence given

<details><summary><b>News</b> — score n/a</summary>

_No news found for this one today._

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score n/a</summary>

```text
US Treasury yields: 3-month 4.06% (+0.06 on the week) | 5-year 5.04% (-0.02 on the week) | 10-year 5.27% (-0.00 on the week) | 30-year 5.64% (+0.01 on the week)
Yield curve, 10-year minus 3-month: +1.22 points -- upward sloping (normal)
US dollar index: 102.26 (+0.33 on the week)
Volatility (VIX): 15.01 (-0.3 on the week) -- elevated
Latest US data: inflation 3.4% (2026-08-01) | unemployment 4.2% (2026-09-01) | jobless claims 197k (2026-10-03)
Policy and expectations: Fed target 4.00% | market expects 2.4% inflation over 10 years
Rate path: 2-year Treasury 4.77% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score n/a</summary>

```text
Last close 46.34 (bar of 2026-10-09), from 502 daily bars
Trend: vs 20d SMA 46.95 (-1.3%), 50d 47.83 (-3.1%), 200d 46.75 (-0.9%); 50d above 200d
Momentum: RSI(14) 40.0 | MACD -0.490 vs signal -0.434 (histogram -0.057)
Returns: 1d +0.2% | 5d +0.3% | 1m -2.5% | 3m -0.0%
52-week range: 41.34 - 49.39 (now 62.1% of the way up)
Volatility: ATR(14) 0.47 (1.0% of price) | annualised 20d 11.8%
Volume: 0.10x the 20-day average
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
Three-year record: +18.3% a year | beta to the market 0.71
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
Ratings by weight: buy 59.1% | hold 40.9% | sell 0.0% (mean 2.16 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +15.8% above the current prices
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
Direction: money going out (1 week)
Share count change: 1 week: -2.3% (-87.73M) over 7d
Shares outstanding: 79.14M | fund size: 3.67B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Brazil (EWZ) · Sector or country — no answer, no confidence given

<details><summary><b>News</b> — score n/a</summary>

- [Daily ETF Flows: EWZ Keeps Gathering Assets](https://www.etf.com/sections/daily-etf-flows/daily-etf-flows-ewz-keeps-gathering-assets)  
  <sub>ETF.com, 22 hours ago</sub>  
  Here are the daily ETF fund flows for October 8, 2026.
- [The RBI of Stanley Druckenmiller, a legendary Wall Street investor nicknamed the "investment machine..](https://www.mk.co.kr/en/stock/12172188)  
  <sub>매일경제, 15 hours ago</sub>  
  iShares MSCI Brazil (EWZ), bought by Drucken Miller, is up 33% this year. In particular, it soared 12% on the 5th (local time) alone, when Liberal candidate...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score n/a</summary>

```text
US Treasury yields: 3-month 4.06% (+0.06 on the week) | 5-year 5.04% (-0.02 on the week) | 10-year 5.27% (-0.00 on the week) | 30-year 5.64% (+0.01 on the week)
Yield curve, 10-year minus 3-month: +1.22 points -- upward sloping (normal)
US dollar index: 102.26 (+0.33 on the week)
Volatility (VIX): 15.01 (-0.3 on the week) -- elevated
Latest US data: inflation 3.4% (2026-08-01) | unemployment 4.2% (2026-09-01) | jobless claims 197k (2026-10-03)
Policy and expectations: Fed target 4.00% | market expects 2.4% inflation over 10 years
Rate path: 2-year Treasury 4.77% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score n/a</summary>

```text
Last close 43.40 (bar of 2026-10-09), from 502 daily bars
Trend: vs 20d SMA 38.76 (+12.0%), 50d 37.03 (+17.2%), 200d 36.67 (+18.4%); 50d above 200d
Momentum: RSI(14) 75.8 | MACD 1.538 vs signal 0.939 (histogram 0.599)
Returns: 1d +1.9% | 5d +13.7% | 1m +12.6% | 3m +22.6%
52-week range: 28.79 - 43.40 (now 100.0% of the way up)
Volatility: ATR(14) 1.11 (2.5% of price) | annualised 20d 49.2%
Volume: 0.46x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score n/a</summary>

```text
Fund type: Focused Region
What it holds: P/E 10.73 | P/B 1.84 | P/S 1.40 | 3y earnings growth n/a
Yield: 3.9%
Three-year record: +20.4% a year | beta to the market 0.83
Cost and size: expense ratio 0.59% | net assets 8.64B
What it is made of: Stocks 97.5%, Cash 2.0%, Preferred 0.5%
Largest holdings: Vale SA 8.9%, Itau Unibanco Holding SA Participating Preferred 8.4%, Nu Holdings Ltd Ordinary Shares Class A 8.1%, Petroleo Brasileiro SA Petrobras Participating Preferred 7.5%, Petroleo Brasileiro SA Petrobras 7.0%
Sector mix: Financial services 34.4%, Energy 18.1%, Basic materials 13.0%, Utilities 12.8%
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
Rolled up from the 5 largest holdings, 39.9% of the fund by weight
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 1.79 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +14.1% above the current prices
Holdings read: VALE3.SA, ITUB4, NU, PETR4, PETR3.SA
Recent rating changes among them:
  - NU: 2026-10-06 JP Morgan: main, Overweight -> Overweight
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
Share count change: 1 week: +0.0% (0.00) over 7d
Shares outstanding: 200.55M | fund size: 8.70B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Gold mining companies (GDX) · Sector or country — no answer, no confidence given

<details><summary><b>News</b> — score n/a</summary>

- [GLD, GDX, and GDXJ Are 3 Ways to Bet on Gold. The Same Move Can Produce Wildly Different Returns](https://247wallst.com/investing/etf/2026/10/08/gld-gdx-and-gdxj-are-3-ways-to-bet-on-gold-the-same-move-can-produce-wildly-different-returns/)  
  <sub>24/7 Wall St., 14 hours ago</sub>  
  Choosing between GLD, GDX, and GDXJ feels like splitting hairs until a single market move exposes just how differently these three gold funds can treat your...
- [Gold & Silver Mining Companies: Two Indices to Analyze for FX_IDC:XAUUSD by Swissquote](https://www.tradingview.com/chart/XAUUSD/RmdDHNIA-Gold-Silver-Mining-Companies-Two-Indices-to-Analyze/)  
  <sub>TradingView, 10 hours ago</sub>  
  Where does the underlying trend in gold and silver prices currently stand in the commodities market? This is a question I often address through my analyses...
- [Flow Focus | OpenAI Cracks, Oil Breaks $100(Again): Where Is the Smart Money Going?](https://www.moomoo.com/community/feed/flow-focus-openai-cracks-oil-breaks-100-again-where-is-117409856749574)  
  <sub>Moomoo, 7 hours ago</sub>  
  Oil ripped nearly five percent higher, $Brent Last Day Financial Futures (DEC6) (BZmain.US)$ reclaimed $100, and Energy led the market. Utilities and ...
- [VanEck UCITS ETFs Plc - Net Asset Value(s)](https://uk.finance.yahoo.com/news/vaneck-ucits-etfs-plc-net-060000654.html)  
  <sub>Yahoo Finance UK, 9 hours ago</sub>  
  Fund Name. NAV Date. Ticker Symbol. ISIN. Shares in Issue. Net Asset Value. NAV per Share. VanEck Emerging Markets High Yield Bond UCITS ETF. 2026-10-08.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score n/a</summary>

```text
US Treasury yields: 3-month 4.06% (+0.06 on the week) | 5-year 5.04% (-0.02 on the week) | 10-year 5.27% (-0.00 on the week) | 30-year 5.64% (+0.01 on the week)
Yield curve, 10-year minus 3-month: +1.22 points -- upward sloping (normal)
US dollar index: 102.26 (+0.33 on the week)
Volatility (VIX): 15.01 (-0.3 on the week) -- elevated
Latest US data: inflation 3.4% (2026-08-01) | unemployment 4.2% (2026-09-01) | jobless claims 197k (2026-10-03)
Policy and expectations: Fed target 4.00% | market expects 2.4% inflation over 10 years
Rate path: 2-year Treasury 4.77% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score n/a</summary>

```text
Last close 88.61 (bar of 2026-10-09), from 502 daily bars
Trend: vs 20d SMA 90.96 (-2.6%), 50d 92.66 (-4.4%), 200d 91.10 (-2.7%); 50d above 200d
Momentum: RSI(14) 45.3 | MACD -1.920 vs signal -1.395 (histogram -0.525)
Returns: 1d +2.2% | 5d +0.9% | 1m -7.7% | 3m +20.8%
52-week range: 68.28 - 115.84 (now 42.7% of the way up)
Volatility: ATR(14) 2.94 (3.3% of price) | annualised 20d 37.8%
Volume: 0.20x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score n/a</summary>

```text
Fund type: Equity Precious Metals
What it holds: P/E 13.93 | P/B 3.18 | P/S 4.54 | 3y earnings growth n/a
Yield: 0.7%
Three-year record: +50.3% a year | beta to the market 0.81
Cost and size: expense ratio 0.51% | net assets 26.25B
What it is made of: Stocks 100.0%, Cash 0.0%
Largest holdings: Newmont Corp 11.1%, Agnico Eagle Mines Ltd 11.0%, Barrick Mining Corp 7.9%, Wheaton Precious Metals Corp 5.5%, Franco-Nevada Corp 5.2%
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
Rolled up from the 5 largest holdings, 40.8% of the fund by weight
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 1.63 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +16.4% above the current prices
Holdings read: NEM, AEM.TO, ABX.TO, WPM.TO, FNV.TO
Recent rating changes among them:
  - NEM: 2026-09-16 RBC Capital: main, Outperform -> Outperform
  - AEM.TO: 2026-10-08 UBS: main, Neutral -> Neutral
  - ABX.TO: 2026-09-16 RBC Capital: main, Outperform -> Outperform
  - WPM.TO: 2026-10-08 UBS: main, Buy -> Buy
  - FNV.TO: 2026-09-16 RBC Capital: main, Outperform -> Outperform
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
Direction: money going out (1 week)
Share count change: 1 week: -13.2% (-4.01B) over 7d
Shares outstanding: 297.98M | fund size: 26.40B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

## Commodities

### Sugar (CANE) · Commodity — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:** no explanation. It wrote only “NEUTRAL”, so the main reasons below are all it gave.

**Main reasons it gave:**
- Crowded long: net long 19.9% of open interest, 100% percentile over 52 weeks
- Outflows: share count down 15.2% over past week
- Heavy cost of holding: -9.8% annualized drag versus sugar spot
- Technicals: price above 20‑day, 50‑day, 200‑day SMAs but volume only 0.31× 20‑day average

<details><summary><b>News</b> — score +0.00</summary>

_No news found for this one today._

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.06% (+0.06 on the week) | 5-year 5.04% (-0.02 on the week) | 10-year 5.27% (-0.00 on the week) | 30-year 5.64% (+0.01 on the week)
Yield curve, 10-year minus 3-month: +1.22 points -- upward sloping (normal)
US dollar index: 102.26 (+0.33 on the week)
Volatility (VIX): 15.01 (-0.3 on the week) -- elevated
Latest US data: inflation 3.4% (2026-08-01) | unemployment 4.2% (2026-09-01) | jobless claims 197k (2026-10-03)
Policy and expectations: Fed target 4.00% | market expects 2.4% inflation over 10 years
Rate path: 2-year Treasury 4.77% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 12.03 (bar of 2026-10-09), from 502 daily bars
Trend: vs 20d SMA 11.52 (+4.4%), 50d 11.20 (+7.4%), 200d 10.05 (+19.8%); 50d above 200d
Momentum: RSI(14) 63.3 | MACD 0.257 vs signal 0.197 (histogram 0.060)
Returns: 1d +0.4% | 5d +1.8% | 1m +1.8% | 3m +23.4%
52-week range: 9.02 - 12.28 (now 92.3% of the way up)
Volatility: ATR(14) 0.22 (1.8% of price) | annualised 20d 23.8%
Volume: 0.31x the 20-day average
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
Cost of holding this fund instead of sugar itself: -9.8% a year -- heavy: rolling contracts costs this fund real money
Measured: 3 months: fund +23.4%, commodity +38.2%, gap -14.8% | 6 months: fund +28.9%, commodity +48.2%, gap -19.3% | 12 months: fund +15.3%, commodity +25.1%, gap -9.8%
A commodity fund holds futures, not sugar, and must sell each expiring contract to buy the next one. Where the next month costs more, that roll loses money every month. This gap is what the structure has actually cost, fees included -- it is history rather than a forecast, and it is not a direction: heavy carry is a reason to want a larger move to justify a long, and a tailwind for a short.
```

</details>

<details><summary><b>How much oil and gas is in storage</b> — score -0.50</summary>

_Not available today._

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

<details><summary><b>Buying and selling by company insiders</b> — score -0.40</summary>

_Not available today._

</details>

<details><summary><b>Who is positioned how</b> — score -0.40</summary>

```text
Contract: SUGAR NO. 11 - ICE FUTURES U.S. (positions as of 2026-09-29, published the following Friday)
Large speculators: net long 19.9% of open interest (1,099,176 contracts)
Change on the week: +1.0% of open interest
Crowding: 100% percentile over 52 weeks -- a crowded long by the standards of the past year
Read this as crowding, not as a forecast: an extreme is as often the end of a move as the middle of one.
```

</details>

<details><summary><b>Money going into and out of this fund</b> — score -0.40</summary>

```text
Direction: money going out (1 week)
Share count change: 1 week: -15.2% (-9.35M) over 7d
Shares outstanding: 4.34M | fund size: 52.15M
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Corn (CORN) · Commodity — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> No macro surprise, technicals lack decisive break, fundamentals offsetting (heavy roll cost vs deteriorating crop condition).

**Main reasons it gave:**
- Inflation 3.4% (2026-08-01) in line with expectations
- RSI 43.9, price below 20‑day SMA (19.51) and 50‑day SMA (19.17)
- CORN net long 20.5% of OI, -1.3% weekly change, 93rd percentile crowding
- Cost of holding fund vs corn: -10.2% annual roll cost
- US crop condition rating down 3 points over 3 weeks (steady, -3 points)

<details><summary><b>News</b> — score +0.00</summary>

- [Corn Posting Losses at Midday](https://www.barchart.com/story/news/5099876/corn-posting-losses-at-midday)  
  <sub>Barchart.com, 22 hours ago</sub>  
  Corn futures are trading with 2 to 3 cent losses across most contracts at Thursday's midday. The CmdtyView national average Cash Corn price is down 2 1/4...
- [CORN Price Today: CORN to IDR = Rp452.11](https://pluang.com/en/asset/crypto/CORN/10618)  
  <sub>Pluang, 15 hours ago</sub>  
  1 CORN to IDR = Rp452.11 right now. Track CORN price today on Pluang, updated in real time with live charts and market data. CORN currently has a market...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.06% (+0.06 on the week) | 5-year 5.04% (-0.02 on the week) | 10-year 5.27% (-0.00 on the week) | 30-year 5.64% (+0.01 on the week)
Yield curve, 10-year minus 3-month: +1.22 points -- upward sloping (normal)
US dollar index: 102.26 (+0.33 on the week)
Volatility (VIX): 15.01 (-0.3 on the week) -- elevated
Latest US data: inflation 3.4% (2026-08-01) | unemployment 4.2% (2026-09-01) | jobless claims 197k (2026-10-03)
Policy and expectations: Fed target 4.00% | market expects 2.4% inflation over 10 years
Rate path: 2-year Treasury 4.77% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 19.07 (bar of 2026-10-09), from 502 daily bars
Trend: vs 20d SMA 19.51 (-2.3%), 50d 19.17 (-0.6%), 200d 18.17 (+4.9%); 50d above 200d
Momentum: RSI(14) 43.9 | MACD -0.119 vs signal -0.020 (histogram -0.100)
Returns: 1d +0.6% | 5d +1.1% | 1m -4.7% | 3m +8.6%
52-week range: 16.47 - 20.29 (now 67.9% of the way up)
Volatility: ATR(14) 0.29 (1.5% of price) | annualised 20d 18.5%
Volume: 0.04x the 20-day average
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
Cost of holding this fund instead of corn itself: -10.2% a year -- heavy: rolling contracts costs this fund real money
Measured: 3 months: fund +8.6%, commodity +14.4%, gap -5.8% | 6 months: fund +7.4%, commodity +13.5%, gap -6.1% | 12 months: fund +8.4%, commodity +18.7%, gap -10.2%
A commodity fund holds futures, not corn, and must sell each expiring contract to buy the next one. Where the next month costs more, that roll loses money every month. This gap is what the structure has actually cost, fees included -- it is history rather than a forecast, and it is not a direction: heavy carry is a reason to want a larger move to justify a long, and a tailwind for a short.
```

</details>

<details><summary><b>How much oil and gas is in storage</b> — score -0.10</summary>

_Not available today._

</details>

<details><summary><b>How the crop is growing</b> — score -0.10</summary>

```text
Corn rated good or excellent: 54% of the US crop (week 40 of 2026)
Direction over 3 weeks: steady, -3 points
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
Contract: CORN - CHICAGO BOARD OF TRADE (positions as of 2026-09-29, published the following Friday)
Large speculators: net long 20.5% of open interest (1,857,317 contracts)
Change on the week: -1.3% of open interest
Crowding: 93% percentile over 52 weeks -- a crowded long by the standards of the past year
Read this as crowding, not as a forecast: an extreme is as often the end of a move as the middle of one.
```

</details>

<details><summary><b>Money going into and out of this fund</b> — score -0.20</summary>

```text
Direction: money going out (1 week)
Share count change: 1 week: -19.9% (-32.04M) over 7d
Shares outstanding: 6.77M | fund size: 128.99M
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Copper (CPER) · Commodity — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:** no explanation. It wrote only “NEUTRAL”, so the main reasons below are all it gave.

**Main reasons it gave:**
- Fund flows: -5.6% share count in past week (outflows)
- Cost of holding: -4.4% annual drag versus copper
- Positioning: net long decreased 1.4% week over week
- Technicals: price above 20d, 50d, 200d SMAs but MACD below signal

<details><summary><b>News</b> — score +0.00</summary>

_No news found for this one today._

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.06% (+0.06 on the week) | 5-year 5.04% (-0.02 on the week) | 10-year 5.27% (-0.00 on the week) | 30-year 5.64% (+0.01 on the week)
Yield curve, 10-year minus 3-month: +1.22 points -- upward sloping (normal)
US dollar index: 102.26 (+0.33 on the week)
Volatility (VIX): 15.01 (-0.3 on the week) -- elevated
Latest US data: inflation 3.4% (2026-08-01) | unemployment 4.2% (2026-09-01) | jobless claims 197k (2026-10-03)
Policy and expectations: Fed target 4.00% | market expects 2.4% inflation over 10 years
Rate path: 2-year Treasury 4.77% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 40.26 (bar of 2026-10-09), from 502 daily bars
Trend: vs 20d SMA 39.86 (+1.0%), 50d 39.90 (+0.9%), 200d 37.61 (+7.1%); 50d above 200d
Momentum: RSI(14) 53.7 | MACD 0.032 vs signal 0.059 (histogram -0.027)
Returns: 1d +2.0% | 5d +1.9% | 1m +3.1% | 3m +6.1%
52-week range: 30.27 - 41.43 (now 89.6% of the way up)
Volatility: ATR(14) 0.62 (1.5% of price) | annualised 20d 22.2%
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
Cost of holding this fund instead of copper itself: -4.4% a year -- a steady drag
Measured: 3 months: fund +6.1%, commodity +7.5%, gap -1.3% | 6 months: fund +12.3%, commodity +14.1%, gap -1.9% | 12 months: fund +28.3%, commodity +32.7%, gap -4.4%
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
Contract: COPPER- #1 - COMMODITY EXCHANGE INC. (positions as of 2026-09-29, published the following Friday)
Large speculators: net long 25.9% of open interest (301,201 contracts)
Change on the week: -1.4% of open interest
Crowding: 70% percentile over 52 weeks -- within its normal range
Read this as crowding, not as a forecast: an extreme is as often the end of a move as the middle of one.
```

</details>

<details><summary><b>Money going into and out of this fund</b> — score -0.10</summary>

```text
Direction: money going out (1 week)
Share count change: 1 week: -5.6% (-42.98M) over 7d
Shares outstanding: 17.87M | fund size: 719.38M
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

**Data that was missing** (counted as 0.00, never guessed):
- news unavailable: Bright Data returned an empty body with its 200; nothing to parse

### Silver (SLV) · Commodity — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> No macro surprise; technicals remain in downtrend; large outflows and reduced net‑long position suggest bearish pressure but no decisive catalyst.

**Main reasons it gave:**
- Silver ETFs rose up to 2% on the day
- Large speculators net long fell 5.4% week over week
- Fund share count down 13.8% over 7 days
- SLV price below 20‑day, 50‑day, and 200‑day SMAs
- No macro surprise: yields stable, inflation 3.4% in line with expectations

<details><summary><b>News</b> — score +0.00</summary>

- [Gold And Silver: Correction In Progress (Technical And Fundamental)](https://seekingalpha.com/article/4953052-gold-and-silver-correction-in-progress-technical-and-fundamental)  
  <sub>Seeking Alpha, 3 hours ago</sub>  
  Gold and silver test key support as real yields and USD pressure prices. Technical setups suggest both metals are poised for a potential bounce.
- [First Majestic Silver Corp. (AG.TO) Stock Price, News, Quote & History](https://ca.finance.yahoo.com/quote/AG.TO/)  
  <sub>Yahoo! Finance Canada, 15 hours ago</sub>  
  Find the latest First Majestic Silver Corp. (AG.TO) stock quote, history, news and other vital information to help you with your stock trading and...
- [ZBKA ETF Holdings List — TRADEGATE:ZBKA](https://www.tradingview.com/symbols/TRADEGATE-ZBKA/holdings/)  
  <sub>TradingView, 12 hours ago</sub>  
  Explore Swisscanto (CH) Silver ETF EAH EUR holdings with weight, market value, and other helpful data to make more informed decisions for ZBKA trading.
- [Gold (XAUUSD) & Silver Price Forecast: Gold Breaks $4,184, Can Silver Clear $61.72?](https://www.fxempire.com/forecasts/article/gold-xauusd-silver-price-forecast-gold-breaks-4184-can-silver-clear-61-72-1636947)  
  <sub>FXEmpire, 7 hours ago</sub>  
  Gold breaks above $4184 as softer yields and record ETF inflows support recovery, while silver reclaims $59.96 and targets $61.72 resistance.
- [Silver's long-term outlook remains bullish as new investment products offer income opportunities - Amplify ETFs](https://www.kitco.com/news/article/2026-10-08/silvers-long-term-outlook-remains-bullish-new-investment-products-offer)  
  <sub>Kitco, 23 hours ago</sub>  
  (Kitco News) - The silver market continues to struggle in the face of persistent inflation pressures and higher bond yields. However, one market strategist...
- [Silver ETFs Outshine Gold in Rebound as IT Leads Gains; Defence Firms, Liquid Steady on Friday](https://hdfcsky.com/news/silver-etfs-outshine-gold-in-rebound-as-it-leads-gains-defence-firms-liquid-steady-on-friday)  
  <sub>HDFC Sky, 8 hours ago</sub>  
  All gold, silver and IT ETFs gained on Friday, with silver ETFs rising up to 2%. Defence ETFs posted mild gains while liquid ETFs stayed flat.
- [Positive ETF Gold Flows Pushed Holdings to a New Record in September](https://www.linkedin.com/posts/money-metals_positive-etf-gold-flows-pushed-holdings-to-activity-7514025605814870016-a1bL)  
  <sub>LinkedIn, 21 hours ago</sub>
- [Gold, silver prices rebound on MCX: Key factors to watch next](https://www.cnbctv18.com/market/commodities/gold-silver-prices-rebound-on-mcx-key-factors-to-watch-next-20008472.htm)  
  <sub>CNBC TV18, 6 hours ago</sub>  
  Gold and silver prices rose in domestic futures trade, tracking international market gains driven by easing US Treasury yields and a weaker dollar.
- [Gold & Silver Mining Companies: Two Indices to Analyze for FX_IDC:XAUUSD by Swissquote](https://www.tradingview.com/chart/XAUUSD/RmdDHNIA-Gold-Silver-Mining-Companies-Two-Indices-to-Analyze/)  
  <sub>TradingView, 10 hours ago</sub>  
  Where does the underlying trend in gold and silver prices currently stand in the commodities market? This is a question I often address through my analyses...
- [Silver Grove Financial Group, Inc.'s Vanguard Index Funds Vanguard Morningstar Growth ETF(VUG) Holding History](https://www.gurufocus.com/guru-portfolio/Silver%20Grove%20Financial%20Group,%20Inc./VUG)  
  <sub>GuruFocus, 23 hours ago</sub>  
  Vanguard Index Funds Vanguard Morningstar Growth ETF(VUG) Buys and Sells Made by Silver Grove Financial Group, Inc.. Latest and Historical Data and Chart.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.06% (+0.06 on the week) | 5-year 5.04% (-0.02 on the week) | 10-year 5.27% (-0.00 on the week) | 30-year 5.64% (+0.01 on the week)
Yield curve, 10-year minus 3-month: +1.22 points -- upward sloping (normal)
US dollar index: 102.26 (+0.33 on the week)
Volatility (VIX): 15.01 (-0.3 on the week) -- elevated
Latest US data: inflation 3.4% (2026-08-01) | unemployment 4.2% (2026-09-01) | jobless claims 197k (2026-10-03)
Policy and expectations: Fed target 4.00% | market expects 2.4% inflation over 10 years
Rate path: 2-year Treasury 4.77% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score -0.30</summary>

```text
Last close 54.83 (bar of 2026-10-09), from 502 daily bars
Trend: vs 20d SMA 56.60 (-3.1%), 50d 57.94 (-5.4%), 200d 65.77 (-16.6%); 50d below 200d
Momentum: RSI(14) 43.3 | MACD -1.175 vs signal -0.894 (histogram -0.281)
Returns: 1d +2.6% | 5d +0.2% | 1m -4.7% | 3m +5.1%
52-week range: 42.40 - 105.60 (now 19.7% of the way up)
Volatility: ATR(14) 1.59 (2.9% of price) | annualised 20d 35.4%
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
Cost of holding this fund instead of silver itself: -2.5% a year -- a steady drag
Measured: 3 months: fund +5.1%, commodity +6.0%, gap -0.8% | 6 months: fund -20.6%, commodity -20.0%, gap -0.6% | 12 months: fund +23.0%, commodity +25.5%, gap -2.5%
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

<details><summary><b>Buying and selling by company insiders</b> — score -0.50</summary>

_Not available today._

</details>

<details><summary><b>Who is positioned how</b> — score -0.50</summary>

```text
Contract: SILVER - COMMODITY EXCHANGE INC. (positions as of 2026-09-29, published the following Friday)
Large speculators: net long 7.1% of open interest (107,047 contracts)
Change on the week: -5.4% of open interest
Crowding: 13% percentile over 52 weeks -- within its normal range
Read this as crowding, not as a forecast: an extreme is as often the end of a move as the middle of one.
```

</details>

<details><summary><b>Money going into and out of this fund</b> — score -0.50</summary>

```text
Direction: money going out (1 week)
Share count change: 1 week: -13.8% (-4.77B) over 7d
Shares outstanding: 543.93M | fund size: 29.82B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Soybeans (SOYB) · Commodity — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:** no explanation. It wrote only “NEUTRAL”, so the main reasons below are all it gave.

**Main reasons it gave:**
- Positioning: net long 22.6% of OI, down -1.2% week, crowded long (90th percentile)
- Fund flows: share count down 2.6% over past week (outflows)
- Crop condition: US soybeans condition down 1 point over 3 weeks (worsening, bullish)
- Technicals: price near 52‑week high (91.3% of range) with low volume and RSI 53 (neutral)

<details><summary><b>News</b> — score +0.00</summary>

_No news found for this one today._

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.06% (+0.06 on the week) | 5-year 5.04% (-0.02 on the week) | 10-year 5.27% (-0.00 on the week) | 30-year 5.64% (+0.01 on the week)
Yield curve, 10-year minus 3-month: +1.22 points -- upward sloping (normal)
US dollar index: 102.26 (+0.33 on the week)
Volatility (VIX): 15.01 (-0.3 on the week) -- elevated
Latest US data: inflation 3.4% (2026-08-01) | unemployment 4.2% (2026-09-01) | jobless claims 197k (2026-10-03)
Policy and expectations: Fed target 4.00% | market expects 2.4% inflation over 10 years
Rate path: 2-year Treasury 4.77% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 27.57 (bar of 2026-10-09), from 502 daily bars
Trend: vs 20d SMA 27.68 (-0.4%), 50d 26.85 (+2.7%), 200d 24.76 (+11.4%); 50d above 200d
Momentum: RSI(14) 53.1 | MACD 0.111 vs signal 0.194 (histogram -0.083)
Returns: 1d +0.7% | 5d +1.3% | 1m -2.0% | 3m +8.8%
52-week range: 21.56 - 28.14 (now 91.3% of the way up)
Volatility: ATR(14) 0.32 (1.2% of price) | annualised 20d 13.2%
Volume: 0.04x the 20-day average
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
Cost of holding this fund instead of soybeans itself: -0.2% a year -- close to nothing, as a physically backed fund should be
Measured: 3 months: fund +8.8%, commodity +7.9%, gap +0.9% | 6 months: fund +12.5%, commodity +10.3%, gap +2.2% | 12 months: fund +25.8%, commodity +26.0%, gap -0.2%
A commodity fund holds futures, not soybeans, and must sell each expiring contract to buy the next one. Where the next month costs more, that roll loses money every month. This gap is what the structure has actually cost, fees included -- it is history rather than a forecast, and it is not a direction: heavy carry is a reason to want a larger move to justify a long, and a tailwind for a short.
```

</details>

<details><summary><b>How much oil and gas is in storage</b> — score +0.20</summary>

_Not available today._

</details>

<details><summary><b>How the crop is growing</b> — score +0.20</summary>

```text
Soybeans rated good or excellent: 57% of the US crop (week 40 of 2026)
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

<details><summary><b>Buying and selling by company insiders</b> — score -0.20</summary>

_Not available today._

</details>

<details><summary><b>Who is positioned how</b> — score -0.20</summary>

```text
Contract: SOYBEANS - CHICAGO BOARD OF TRADE (positions as of 2026-09-29, published the following Friday)
Large speculators: net long 22.6% of open interest (1,090,227 contracts)
Change on the week: -1.2% of open interest
Crowding: 90% percentile over 52 weeks -- a crowded long by the standards of the past year
Read this as crowding, not as a forecast: an extreme is as often the end of a move as the middle of one.
```

</details>

<details><summary><b>Money going into and out of this fund</b> — score -0.20</summary>

```text
Direction: money going out (1 week)
Share count change: 1 week: -2.6% (-1.23M) over 7d
Shares outstanding: 1.64M | fund size: 45.14M
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Oil (USO) · Commodity — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> The fund shows mixed fundamentals with a bearish price outlook and modest outflows, but no clear macro catalyst or decisive technical break. Positioning indicates a slight bearish shift, while inventories are mixed. Overall, the evidence does not justify a strong directional bias.

**Main reasons it gave:**
- EIA price outlook projects WTI falling to $86 in six months, below current price
- CFTC speculators net long decreased 1.3% week‑over‑week, indicating slight bearish positioning
- Fund flows show 11.4% share redemption (outflows) over the past week
- Energy inventories: crude draw of 3.2 M bbl (bullish) offset by gasoline build of 0.4 M bbl (bearish), net mixed

<details><summary><b>News</b> — score +0.00</summary>

- [ETFs Investing in uSonar Co., Ltd. Stocks](https://www.tradingview.com/symbols/TSE-431A/etfs/)  
  <sub>TradingView, 13 hours ago</sub>  
  Sorted by market value, the list below shows funds with uSonar Co., Ltd. stocks. Equipped with price, change, and other helpful stats, they make investing...
- [Dow Falls Nearly 200 Points, S&P 500 And Nasdaq In Red As Treasury Yields Stay Near 24-Year Highs, Oil Prices Jump](https://stocktwits.com/news-articles/markets/equity/dow-falls-nearly-200-points-s-and-p-500-and-nasdaq-in-red-as-treasury-yields-stay-near-24-year-highs-oil-prices-jump/cZDUkhDRBNj)  
  <sub>Stocktwits, 19 hours ago</sub>  
  U.S. stocks slipped on Thursday as investors continued to track elevated Treasury yields while crude prices jumped.
- [Trump Says US Will Not Attack Iran Before Midterm Election - ExxonMobil Holdings (NYSE:XOM), Chevron (NYS](https://www.benzinga.com/trading-ideas/movers/26/10/62254835/quick-spark-trump-says-us-will-not-attack-iran-before-midterm-election)  
  <sub>Benzinga, 22 hours ago</sub>  
  President Donald Trump rules out U.S. military action against Iran before the Nov. 3 midterm elections.
- [Trump says U.S. won't attack Iran before midterms, citing 'productive discussions' (ITA:BATS)](https://seekingalpha.com/news/4651480-trump-says-u-s-wont-attack-iran-before-midterms-citing-productive-discussions)  
  <sub>Seeking Alpha, 22 hours ago</sub>  
  Trump says no Iran strikes before Nov. 3 as Strait of Hormuz blockade holds; oil prices react after tanker attack and hurricane risks.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.06% (+0.06 on the week) | 5-year 5.04% (-0.02 on the week) | 10-year 5.27% (-0.00 on the week) | 30-year 5.64% (+0.01 on the week)
Yield curve, 10-year minus 3-month: +1.22 points -- upward sloping (normal)
US dollar index: 102.26 (+0.33 on the week)
Volatility (VIX): 15.01 (-0.3 on the week) -- elevated
Latest US data: inflation 3.4% (2026-08-01) | unemployment 4.2% (2026-09-01) | jobless claims 197k (2026-10-03)
Policy and expectations: Fed target 4.00% | market expects 2.4% inflation over 10 years
Rate path: 2-year Treasury 4.77% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 148.73 (bar of 2026-10-09), from 502 daily bars
Trend: vs 20d SMA 149.59 (-0.6%), 50d 139.17 (+6.9%), 200d 117.12 (+27.0%); 50d above 200d
Momentum: RSI(14) 53.9 | MACD 1.373 vs signal 2.366 (histogram -0.994)
Returns: 1d +0.8% | 5d +0.9% | 1m -6.1% | 3m +26.3%
52-week range: 66.17 - 161.86 (now 86.3% of the way up)
Volatility: ATR(14) 5.13 (3.4% of price) | annualised 20d 40.6%
Volume: 0.18x the 20-day average
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
US inventories, week ending 2026-10-02 (published the following Wednesday)
  Crude oil: 424.1 million barrels, -3.2 on the week (a draw), 40% percentile over 52 weeks
  Petrol: 204.7 million barrels, +0.4 on the week (a build), 4% percentile over 52 weeks -- low for the time of year
  Diesel: 105.1 million barrels, -0.0 on the week (a draw), 23% percentile over 52 weeks
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
Contract: WTI-PHYSICAL - NEW YORK MERCANTILE EXCHANGE (positions as of 2026-09-29, published the following Friday)
Large speculators: net long 4.2% of open interest (1,878,576 contracts)
Change on the week: -1.3% of open interest
Crowding: 68% percentile over 52 weeks -- within its normal range
Read this as crowding, not as a forecast: an extreme is as often the end of a move as the middle of one.
```

</details>

<details><summary><b>Money going into and out of this fund</b> — score -0.20</summary>

```text
Direction: money going out (1 week)
Share count change: 1 week: -11.4% (-222.96M) over 7d
Shares outstanding: 11.70M | fund size: 1.74B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Wheat (WEAT) · Commodity — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> No macro surprise, technicals show no decisive break, mixed signals from positioning (slight bullish) and heavy roll cost plus strong outflows (bearish).

**Main reasons it gave:**
- Positioning: net short decreased 2.1% of open interest this week
- Cost of holding: -13.8% annual roll cost versus wheat, tailwind for short
- Fund flows: share count fell 22.9% in one week, indicating strong outflow
- Technicals: price 2.3% below 20‑day SMA, RSI 42.9, no decisive break

<details><summary><b>News</b> — score +0.00</summary>

_No news found for this one today._

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.06% (+0.06 on the week) | 5-year 5.04% (-0.02 on the week) | 10-year 5.27% (-0.00 on the week) | 30-year 5.64% (+0.01 on the week)
Yield curve, 10-year minus 3-month: +1.22 points -- upward sloping (normal)
US dollar index: 102.26 (+0.33 on the week)
Volatility (VIX): 15.01 (-0.3 on the week) -- elevated
Latest US data: inflation 3.4% (2026-08-01) | unemployment 4.2% (2026-09-01) | jobless claims 197k (2026-10-03)
Policy and expectations: Fed target 4.00% | market expects 2.4% inflation over 10 years
Rate path: 2-year Treasury 4.77% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 24.88 (bar of 2026-10-09), from 502 daily bars
Trend: vs 20d SMA 25.47 (-2.3%), 50d 25.54 (-2.6%), 200d 23.31 (+6.7%); 50d above 200d
Momentum: RSI(14) 42.9 | MACD -0.295 vs signal -0.218 (histogram -0.078)
Returns: 1d +0.5% | 5d +0.5% | 1m -6.9% | 3m +5.1%
52-week range: 19.88 - 28.00 (now 61.5% of the way up)
Volatility: ATR(14) 0.49 (2.0% of price) | annualised 20d 19.4%
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
Cost of holding this fund instead of wheat itself: -13.8% a year -- heavy: rolling contracts costs this fund real money
Measured: 3 months: fund +5.1%, commodity +9.3%, gap -4.2% | 6 months: fund +14.2%, commodity +20.1%, gap -5.9% | 12 months: fund +21.4%, commodity +35.1%, gap -13.8%
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

<details><summary><b>Buying and selling by company insiders</b> — score +0.20</summary>

_Not available today._

</details>

<details><summary><b>Who is positioned how</b> — score +0.20</summary>

```text
Contract: WHEAT-SRW - CHICAGO BOARD OF TRADE (positions as of 2026-09-29, published the following Friday)
Large speculators: net short 4.6% of open interest (483,142 contracts)
Change on the week: -2.1% of open interest
Crowding: 67% percentile over 52 weeks -- within its normal range
Read this as crowding, not as a forecast: an extreme is as often the end of a move as the middle of one.
```

</details>

<details><summary><b>Money going into and out of this fund</b> — score +0.20</summary>

```text
Direction: money going out (1 week)
Share count change: 1 week: -22.9% (-82.48M) over 7d
Shares outstanding: 11.16M | fund size: 277.71M
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Gold (GLD) · Commodity — no answer, no confidence given

<details><summary><b>News</b> — score n/a</summary>

_No news found for this one today._

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score n/a</summary>

```text
US Treasury yields: 3-month 4.06% (+0.06 on the week) | 5-year 5.04% (-0.02 on the week) | 10-year 5.27% (-0.00 on the week) | 30-year 5.64% (+0.01 on the week)
Yield curve, 10-year minus 3-month: +1.22 points -- upward sloping (normal)
US dollar index: 102.26 (+0.33 on the week)
Volatility (VIX): 15.01 (-0.3 on the week) -- elevated
Latest US data: inflation 3.4% (2026-08-01) | unemployment 4.2% (2026-09-01) | jobless claims 197k (2026-10-03)
Policy and expectations: Fed target 4.00% | market expects 2.4% inflation over 10 years
Rate path: 2-year Treasury 4.77% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score n/a</summary>

```text
Last close 383.28 (bar of 2026-10-09), from 502 daily bars
Trend: vs 20d SMA 387.94 (-1.2%), 50d 397.00 (-3.5%), 200d 415.65 (-7.8%); 50d below 200d
Momentum: RSI(14) 44.7 | MACD -5.399 vs signal -4.790 (histogram -0.609)
Returns: 1d +1.2% | 5d +0.8% | 1m -3.3% | 3m +4.4%
52-week range: 362.32 - 495.90 (now 15.7% of the way up)
Volatility: ATR(14) 6.39 (1.7% of price) | annualised 20d 21.0%
Volume: 0.43x the 20-day average
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
Cost of holding this fund instead of gold itself: -0.4% a year -- close to nothing, as a physically backed fund should be
Measured: 3 months: fund +4.4%, commodity +5.0%, gap -0.6% | 6 months: fund -12.3%, commodity -12.1%, gap -0.2% | 12 months: fund +2.9%, commodity +3.4%, gap -0.4%
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
Contract: GOLD - COMMODITY EXCHANGE INC. (positions as of 2026-09-29, published the following Friday)
Large speculators: net long 29.6% of open interest (406,456 contracts)
Change on the week: -1.3% of open interest
Crowding: 60% percentile over 52 weeks -- within its normal range
Read this as crowding, not as a forecast: an extreme is as often the end of a move as the middle of one.
```

</details>

<details><summary><b>Money going into and out of this fund</b> — score n/a</summary>

```text
Direction: flat (1 week)
Share count change: 1 week: +0.0% (0.00) over 7d
Shares outstanding: 260.30M | fund size: 99.77B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

**Data that was missing** (counted as 0.00, never guessed):
- news unavailable: Bright Data unreachable: The read operation timed out

### Natural gas (UNG) · Commodity — no answer, no confidence given

**This one did not finish:** https://api.deepinfra.com/v1/openai/chat/completions answered with an empty message

<details><summary><b>News</b> — score n/a</summary>

_No news found for this one today._

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score n/a</summary>

```text
US Treasury yields: 3-month 4.06% (+0.06 on the week) | 5-year 5.04% (-0.02 on the week) | 10-year 5.27% (-0.00 on the week) | 30-year 5.64% (+0.01 on the week)
Yield curve, 10-year minus 3-month: +1.22 points -- upward sloping (normal)
US dollar index: 102.26 (+0.33 on the week)
Volatility (VIX): 15.01 (-0.3 on the week) -- elevated
Latest US data: inflation 3.4% (2026-08-01) | unemployment 4.2% (2026-09-01) | jobless claims 197k (2026-10-03)
Policy and expectations: Fed target 4.00% | market expects 2.4% inflation over 10 years
Rate path: 2-year Treasury 4.77% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score n/a</summary>

```text
Last close 11.07 (bar of 2026-10-09), from 502 daily bars
Trend: vs 20d SMA 10.65 (+4.0%), 50d 10.35 (+7.0%), 200d 11.32 (-2.2%); 50d below 200d
Momentum: RSI(14) 58.1 | MACD 0.119 vs signal 0.089 (histogram 0.031)
Returns: 1d +2.5% | 5d +5.8% | 1m +8.7% | 3m +6.8%
52-week range: 9.63 - 16.90 (now 19.9% of the way up)
Volatility: ATR(14) 0.36 (3.3% of price) | annualised 20d 45.3%
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
Cost of holding this fund instead of natural gas itself: -12.5% a year -- heavy: rolling contracts costs this fund real money
Measured: 3 months: fund +6.8%, commodity +11.6%, gap -4.8% | 6 months: fund +2.8%, commodity +22.1%, gap -19.3% | 12 months: fund -15.5%, commodity -3.0%, gap -12.5%
A commodity fund holds futures, not natural gas, and must sell each expiring contract to buy the next one. Where the next month costs more, that roll loses money every month. This gap is what the structure has actually cost, fees included -- it is history rather than a forecast, and it is not a direction: heavy carry is a reason to want a larger move to justify a long, and a tailwind for a short.
```

</details>

<details><summary><b>How much oil and gas is in storage</b> — score n/a</summary>

```text
US inventories, week ending 2026-10-02 (published the following Wednesday)
  Natural gas: 3,500.0 billion cubic feet, +85.0 on the week (a build), 81% percentile over 52 weeks
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
Contract: NAT GAS NYME - NEW YORK MERCANTILE EXCHANGE (positions as of 2026-09-29, published the following Friday)
Large speculators: net short 7.5% of open interest (1,782,129 contracts)
Change on the week: -3.9% of open interest
Crowding: 5% percentile over 52 weeks -- a crowded short by the standards of the past year
Read this as crowding, not as a forecast: an extreme is as often the end of a move as the middle of one.
```

</details>

<details><summary><b>Money going into and out of this fund</b> — score n/a</summary>

```text
Direction: money going out (1 week)
Share count change: 1 week: -23.5% (-145.81M) over 7d
Shares outstanding: 42.78M | fund size: 473.83M
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

**Data that was missing** (counted as 0.00, never guessed):
- news unavailable: Bright Data returned an empty body with its 200; nothing to parse

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

