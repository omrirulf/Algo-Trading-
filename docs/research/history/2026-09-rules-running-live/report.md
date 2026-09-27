# History screen: the rules that run live, on past prices

*Written by `python -m history.screen run` (workflow run 36351241413, commit `178fef8f9faa`) on 2026-09-27T22:14:08+00:00. Lines from 2000-01-03; prices through 2026-09-27. Price table SHA-256 `3f52d3623084e55084520c22bc6b30f0d54cba91a830d9e7950b408a5c42d7c7`; history journal SHA-256 `6362a1227890e3e24826fb4bc17f86c1a17f6ffeea0989f6941b435e52e2abd8` (461,925 lines).*

**Nothing here changes the locked test, its rules or its decisions.** This is a history screen: it replays, on past prices, the rules that already run live, with the real code. It did not read the live race.

## How it was made

- **Names:** the watchlist as it is today (80 names), from 2000 or from each name's first price. Most funds started later than 2000, so the early years have fewer names (see *Data*). **Survivorship:** the list was chosen in 2026, so funds and companies that closed or failed before then are missing. This flatters "always long" and the long side most.
- **Journal:** one line per name per session, built from prices only. Technicals come from production's own function (`build_snapshot`) on the two years of final daily closes up to the **previous session**. A live line also has the current session's partial bar; history does not. So a history line knows about one session less than a live line.
- **Live price:** there is none in the past. **The previous session's final close stands in for it.** A's veto compares that price with the 200-day average, and C's limit is set from it.
- **Race:** the race's own scoring. Enter at the next open, hold 3 sessions, the ATR stop, the conviction floor 0.30, 0.10% per side. No taxes. The coin flip is the race's own (`rules/control.py`), 1,000 seeds, on each rule's own lines.
- **Funds:** the production engine and position manager, $100,000 each, the same costs, dividends paid. No name is held by a real account in the past, and no short refusal (they date from 2026) applies.
- **Not tested:** anything that uses the AI (the model, the hybrid, and the three model funds). The AI has read about the past, so only live results can test it.
- **t:** Newey-West t, lag 3 for race trades and lag 5 for fund days, as registered. Above about 2 (or below -2) is unlikely to be luck alone; these screens are many, so read a t near 2 with care.

## 1. The race (3-session trades)

Each rule's trades, as the live race scores them. *Mean per day* is the race's main number: the mean net return of the trades opened each entry day, 0 on a day with none. *Minus a coin flip*: the rule's trade minus what a coin flip earns on the same line on average. *Always long*: the same trade, bought.

### Momentum (the locked rule)

| Years | Trades | Mean per trade | Hit rate | Mean per day | Coin flip, mean per day (5th to 95th) | Percentile in the coin flip | Minus a coin flip (per day, t) | Minus always long, same lines (per day, t) | Minus always long, every line (per day, t) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| all years | 227,313 | -0.227% | 45.5% | -0.214% | -0.224% to -0.201% | 41 | -0.002% (t -0.07) | -0.069% (t -1.55) | -0.073% (t -1.67) |
| before 2010 | 64,623 | -0.216% | 47.1% | -0.209% | -0.251% to -0.201% | 84 | +0.016% (t +0.29) | -0.019% (t -0.20) | -0.042% (t -0.46) |
| 2010 on | 162,690 | -0.232% | 44.9% | -0.217% | -0.216% to -0.194% | 3 | -0.013% (t -0.51) | -0.099% (t -2.33) | -0.091% (t -2.14) |
| after the source (2013 on) | 136,588 | -0.221% | 44.9% | -0.204% | -0.216% to -0.193% | 56 | +0.001% (t +0.04) | -0.085% (t -1.98) | -0.081% (t -1.87) |

Longs and shorts:

| Years | Side | Trades | Mean per trade | Hit rate | Minus a coin flip (per day, t) | Minus always long, every line, same days (per day, t) |
| --- | --- | --- | --- | --- | --- | --- |
| all years | longs | 151,112 | -0.164% | 46.6% | +0.066% (t +2.42) | +0.005% (t +0.20) |
| all years | shorts | 76,201 | -0.352% | 43.3% | -0.054% (t -1.49) | - |
| before 2010 | longs | 42,350 | -0.164% | 47.6% | +0.079% (t +1.34) | +0.048% (t +0.93) |
| before 2010 | shorts | 22,273 | -0.315% | 46.2% | -0.054% (t -0.70) | - |
| 2010 on | longs | 108,762 | -0.164% | 46.3% | +0.059% (t +2.21) | -0.020% (t -0.91) |
| 2010 on | shorts | 53,928 | -0.368% | 42.1% | -0.054% (t -1.45) | - |
| after the source (2013 on) | longs | 91,019 | -0.161% | 46.2% | +0.067% (t +2.27) | -0.016% (t -0.71) |
| after the source (2013 on) | shorts | 45,569 | -0.341% | 42.4% | -0.062% (t -1.56) | - |

For scale, *always long on every line* (every name bought for 3 sessions, every day), all years: 455,285 trades, -0.138% per trade, hit rate 47.3%.

### A: momentum with the 200-day veto

| Years | Trades | Mean per trade | Hit rate | Mean per day | Coin flip, mean per day (5th to 95th) | Percentile in the coin flip | Minus a coin flip (per day, t) | Minus always long, same lines (per day, t) | Minus always long, every line (per day, t) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| all years | 214,328 | -0.225% | 45.6% | -0.208% | -0.226% to -0.202% | 80 | +0.006% (t +0.23) | -0.064% (t -1.42) | -0.066% (t -1.51) |
| before 2010 | 61,285 | -0.215% | 47.2% | -0.208% | -0.254% to -0.200% | 89 | +0.020% (t +0.35) | -0.015% (t -0.16) | -0.041% (t -0.44) |
| 2010 on | 153,043 | -0.229% | 44.9% | -0.208% | -0.217% to -0.194% | 38 | -0.002% (t -0.09) | -0.093% (t -2.18) | -0.081% (t -1.91) |

Longs and shorts:

| Years | Side | Trades | Mean per trade | Hit rate | Minus a coin flip (per day, t) | Minus always long, every line, same days (per day, t) |
| --- | --- | --- | --- | --- | --- | --- |
| all years | longs | 143,229 | -0.161% | 46.7% | +0.068% (t +2.47) | +0.007% (t +0.29) |
| all years | shorts | 71,099 | -0.354% | 43.4% | -0.051% (t -1.36) | - |
| before 2010 | longs | 40,180 | -0.167% | 47.5% | +0.069% (t +1.19) | +0.042% (t +0.78) |
| before 2010 | shorts | 21,105 | -0.306% | 46.6% | -0.051% (t -0.66) | - |
| 2010 on | longs | 103,049 | -0.159% | 46.4% | +0.067% (t +2.46) | -0.013% (t -0.57) |
| 2010 on | shorts | 49,994 | -0.374% | 42.0% | -0.050% (t -1.30) | - |

For scale, *always long on every line* (every name bought for 3 sessions, every day), all years: 455,285 trades, -0.138% per trade, hit rate 47.3%.

### A against momentum

A's main race number (section 13.2): A minus momentum, per day.

| Years | Momentum signals | Vetoed by A | Veto share | No 200-day average yet | A minus momentum (per day, t) |
| --- | --- | --- | --- | --- | --- |
| all years | 229,668 | 13,181 | 5.7% | 3,062 | +0.007% (t +1.74) |
| before 2010 | 65,291 | 3,401 | 5.2% | 2,290 | +0.001% (t +0.16) |
| 2010 on | 164,377 | 9,780 | 5.9% | 772 | +0.010% (t +3.01) |

## 2. The funds (the production engine)

Each fund against the VT fund (VT bought and held). VT has prices only from 2008-06-26, so every comparison with VT starts there; the SPY fund (SPY bought and held from the first session) is a longer yardstick. *Invested* is the book's gross exposure as a share of equity; *worst fall* is the maximum drawdown.

| Fund | Years | Total return | A year | Worst fall | Invested (mean) | Minus VT fund (per day, t) | A year: fund vs VT (same days) | Worst fall: fund vs VT | Minus SPY fund (per day, t) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Momentum fund | all years | -61.7% | -3.5% | 65.0% | 84% | -0.0440% (t -2.11) | -2.6% vs +7.6% | 55.8% vs 50.6% | -0.0444% (t -2.79) |
| Momentum fund | before 2010 | -27.7% | -3.2% | 45.3% | 79% | +0.0502% (t +0.32) | +10.6% vs -8.1% | 28.0% vs 50.6% | -0.0142% (t -0.44) |
| Momentum fund | 2010 on | -47.1% | -3.7% | 50.1% | 87% | -0.0526% (t -2.99) | -3.7% vs +9.1% | 50.1% vs 29.1% | -0.0624% (t -3.74) |
| Momentum fund | after the source (2013 on) | -40.0% | -3.7% | 43.4% | 87% | -0.0535% (t -2.99) | -3.7% vs +9.6% | 43.4% vs 29.1% | -0.0644% (t -3.63) |
| A fund (200-day veto) | all years | -50.3% | -2.6% | 55.1% | 83% | -0.0389% (t -1.84) | -1.4% vs +7.6% | 43.3% vs 50.6% | -0.0404% (t -2.50) |
| A fund (200-day veto) | before 2010 | -21.1% | -2.4% | 45.1% | 77% | +0.0661% (t +0.40) | +14.7% vs -8.1% | 20.2% vs 50.6% | -0.0105% (t -0.32) |
| A fund (200-day veto) | 2010 on | -37.0% | -2.7% | 43.3% | 87% | -0.0484% (t -2.77) | -2.7% vs +9.1% | 43.3% vs 29.1% | -0.0583% (t -3.51) |
| C fund (pullback limit) | all years | -54.8% | -2.9% | 58.6% | 86% | -0.0433% (t -2.04) | -2.5% vs +7.6% | 54.8% vs 50.6% | -0.0418% (t -2.61) |
| C fund (pullback limit) | before 2010 | -17.7% | -1.9% | 36.9% | 80% | +0.0483% (t +0.29) | +9.7% vs -8.1% | 24.7% vs 50.6% | -0.0089% (t -0.28) |
| C fund (pullback limit) | 2010 on | -45.1% | -3.5% | 51.1% | 89% | -0.0516% (t -2.94) | -3.5% vs +9.1% | 51.1% vs 29.1% | -0.0615% (t -3.67) |

Held funds, for scale:

| Fund | Years | From | Total return | A year | Worst fall |
| --- | --- | --- | --- | --- | --- |
| VT fund (held) | all years | 2008-06-26 | +276.8% | +7.6% | 50.6% |
| VT fund (held) | before 2010 | 2008-06-26 | -12.0% | -8.1% | 50.6% |
| VT fund (held) | 2010 on | 2010-01-04 | +328.4% | +9.1% | 29.1% |
| SPY fund (held) | all years | 2000-01-04 | +509.3% | +7.0% | 49.6% |
| SPY fund (held) | before 2010 | 2000-01-04 | -8.2% | -0.9% | 49.6% |
| SPY fund (held) | 2010 on | 2010-01-04 | +563.8% | +12.0% | 28.6% |

Longs and shorts in the funds (closed trades; the return is the trade's profit over what it cost to open, costs and dividends in):

| Fund | Years | Side | Closed trades | Mean return | Hit rate |
| --- | --- | --- | --- | --- | --- |
| Momentum fund | all years | long | 10,414 | +0.15% | 40.5% |
| Momentum fund | all years | short | 6,318 | -0.65% | 34.5% |
| Momentum fund | before 2010 | long | 3,307 | +0.18% | 40.9% |
| Momentum fund | before 2010 | short | 2,136 | -0.48% | 36.5% |
| Momentum fund | 2010 on | long | 7,107 | +0.14% | 40.4% |
| Momentum fund | 2010 on | short | 4,182 | -0.74% | 33.5% |
| Momentum fund | after the source (2013 on) | long | 5,928 | +0.13% | 40.2% |
| Momentum fund | after the source (2013 on) | short | 3,495 | -0.72% | 33.3% |
| A fund (200-day veto) | all years | long | 10,254 | +0.17% | 40.6% |
| A fund (200-day veto) | all years | short | 6,004 | -0.62% | 34.3% |
| A fund (200-day veto) | before 2010 | long | 3,163 | +0.18% | 41.4% |
| A fund (200-day veto) | before 2010 | short | 2,006 | -0.41% | 36.8% |
| A fund (200-day veto) | 2010 on | long | 7,091 | +0.17% | 40.2% |
| A fund (200-day veto) | 2010 on | short | 3,998 | -0.73% | 33.1% |
| C fund (pullback limit) | all years | long | 10,442 | +0.15% | 40.9% |
| C fund (pullback limit) | all years | short | 6,216 | -0.52% | 35.1% |
| C fund (pullback limit) | before 2010 | long | 3,132 | +0.27% | 43.4% |
| C fund (pullback limit) | before 2010 | short | 1,925 | -0.33% | 36.6% |
| C fund (pullback limit) | 2010 on | long | 7,310 | +0.09% | 39.8% |
| C fund (pullback limit) | 2010 on | short | 4,291 | -0.61% | 34.4% |

A and C against the momentum fund (their registered comparator, section 13):

| Fund | Years | Minus momentum fund (per day, t) | Total return: fund vs momentum fund |
| --- | --- | --- | --- |
| A fund (200-day veto) | all years | +0.0040% (t +1.59) | -50.3% vs -61.7% |
| A fund (200-day veto) | before 2010 | +0.0037% (t +0.73) | -21.1% vs -27.7% |
| A fund (200-day veto) | 2010 on | +0.0041% (t +1.58) | -37.0% vs -47.1% |
| C fund (pullback limit) | all years | +0.0026% (t +0.70) | -54.8% vs -61.7% |
| C fund (pullback limit) | before 2010 | +0.0052% (t +0.81) | -17.7% vs -27.7% |
| C fund (pullback limit) | 2010 on | +0.0010% (t +0.22) | -45.1% vs -47.1% |

The momentum fund ran out of room (cash, the gross cap, a group or sleeve cap, the stock-market limit or the 40-position limit) before the end of the list on 6,030 of 6,722 cycle days (90%), skipping 79,495 signals. On those days watchlist order, not the signal, decided what it bought.

## 3. B: VT or T-bills by the 10-month average

The registered rule on VT. VT has prices from 2008-06-26, so B's first decision is the first month-end with ten month-end closes, and B holds from 2009-04-01. So B's history starts after the 2008 crash. Beside it, B's own code with SPY in place of VT, from the first month-end BIL (the T-bills) had prices (2007-05-31): not the registered rule, a check against the owner's quick test on SPY. *Worst fall* is the maximum drawdown.

| Fund | Years | Days | A year: B vs held | Worst fall: B vs held | B minus held (per day, t) |
| --- | --- | --- | --- | --- | --- |
| B fund (VT or T-bills) | all years | 2009-04-01 to 2026-09-25 | +6.5% vs +11.3% | 27.6% vs 29.1% | -0.0190% (t -2.03) |
| B fund (VT or T-bills) | before 2010 | 2009-04-01 to 2009-12-31 | +29.1% vs +71.9% | 8.0% vs 7.9% | -0.1178% (t -2.05) |
| B fund (VT or T-bills) | 2010 on | 2010-01-04 to 2026-09-25 | +5.6% vs +9.1% | 27.6% vs 29.1% | -0.0145% (t -1.54) |
| B's rule on SPY (check only) | all years | 2007-06-01 to 2026-09-25 | +7.8% vs +9.0% | 25.3% vs 49.6% | -0.0067% (t -0.67) |
| B's rule on SPY (check only) | before 2010 | 2007-06-01 to 2009-12-31 | +7.0% vs -8.6% | 9.8% vs 49.6% | +0.0511% (t +1.03) |
| B's rule on SPY (check only) | 2010 on | 2010-01-04 to 2026-09-25 | +7.9% vs +12.0% | 25.3% vs 28.6% | -0.0156% (t -1.86) |

B fund (VT or T-bills): 31 switches, 998 trading days out of the market, now in VT (last month-end 2026-08-31).

B's rule on SPY (check only): 32 switches, 1,068 trading days out of the market, now in SPY (last month-end 2026-08-31).

## 4. C: the pullback limit

Would each momentum signal's limit (signal price minus half the ATR; a short, plus) have filled in its 3 sessions? Counted from prices, as the live counter is.

| Years | Filled | Missed | Fill rate |
| --- | --- | --- | --- |
| all years | 140,569 | 89,020 | 61.2% |
| before 2010 | 39,907 | 25,384 | 61.1% |
| 2010 on | 100,662 | 63,636 | 61.3% |

The race trade (next open, 3 sessions) of signals whose limit filled against those whose limit did not. **Read with care:** a long's limit fills only if the price falls first, inside the same 3 sessions the race trade is scored on, so filled signals must look worse here. This says what C avoids, not what C earns; C's result is its fund (section 2).

| Years | Side | Filled | Filled: mean | Missed | Missed: mean | Missed minus filled | Welch t (reading only) |
| --- | --- | --- | --- | --- | --- | --- | --- |
| all years | all | 139,166 | -0.93% | 88,147 | +0.88% | +1.81% | +163.34 |
| all years | longs | 90,600 | -0.77% | 60,512 | +0.75% | +1.52% | +139.75 |
| all years | shorts | 48,566 | -1.22% | 27,635 | +1.17% | +2.39% | +94.44 |
| before 2010 | all | 39,473 | -1.08% | 25,150 | +1.14% | +2.22% | +84.64 |
| before 2010 | longs | 25,421 | -0.87% | 16,929 | +0.90% | +1.76% | +72.81 |
| before 2010 | shorts | 14,052 | -1.46% | 8,221 | +1.64% | +3.10% | +51.04 |
| 2010 on | all | 99,693 | -0.87% | 62,997 | +0.77% | +1.64% | +144.33 |
| 2010 on | longs | 65,179 | -0.73% | 43,583 | +0.69% | +1.42% | +120.92 |
| 2010 on | shorts | 34,514 | -1.12% | 19,414 | +0.97% | +2.09% | +82.94 |

In the C fund: 61,238 orders placed, 9,647 filled at the open and 7,042 during the day (27.3%), 17,991 cancelled after 3 sessions, 26,552 filled but refused for lack of room; 23,815 signals on which C and the momentum fund did differently (section 13.7).

## 5. What this means for the live race (context only)

On history, momentum's 3-session trades are **close to a coin flip**: inside the coin flip's band (percentile 41; minus a coin flip -0.002% per day, t -0.07).

The owner's observation, written here as context: *at a 3-day horizon, momentum looks close to random on history. So in the live race, "the AI beats momentum" may mean little more than "the AI beats random".* The race already has the coin flip as its floor (the model must also be above the 95th percentile of its own coin flip, section 5), and the index test (the winner must beat VT). This screen **changes nothing in the locked test**: the arms, the metric, the looks and the decision rule stay as registered.

## 6. Data

Lines per year: 2000: 9,019, 2001: 9,645, 2002: 10,508, 2003: 11,500, 2004: 12,282, 2005: 13,262, 2006: 14,788, 2007: 16,236, 2008: 17,337, 2009: 17,388, 2010: 17,683, 2011: 18,539, 2012: 19,477, 2013: 19,656, 2014: 19,656, 2015: 19,729, 2016: 19,908, 2017: 19,829, 2018: 19,963, 2019: 20,160, 2020: 20,240, 2021: 20,160, 2022: 20,080, 2023: 20,000, 2024: 20,160, 2025: 20,000, 2026: 14,720.

Missing price days (a name trading, no bar): 0 of 461,972 ticker-days (0.00%).

The calendar is the days SPY traded (production's list covers 2025-2027 only). Where it differs from production's list since 2025: {'traded_but_production_says_closed': [], 'no_bar_but_production_says_open': ['2025-01-09']}.

Fund integrity: no problems; 0 ticker-days with no bar met by the funds.

First price of each name:

| Name | First bar | Bars |
| --- | --- | --- |
| MSFT | 1997-01-02 | 7,480 |
| NVDA | 1999-01-22 | 6,962 |
| ASML | 1997-01-02 | 7,480 |
| GOOGL | 2004-08-19 | 5,561 |
| JPM | 1997-01-02 | 7,480 |
| RY | 1997-01-02 | 7,480 |
| HDB | 2001-07-20 | 6,333 |
| LLY | 1997-01-02 | 7,480 |
| NVO | 1997-01-02 | 7,480 |
| TEVA | 1997-01-02 | 7,480 |
| CAT | 1997-01-02 | 7,480 |
| ESLT | 1997-01-02 | 7,480 |
| TM | 1997-01-02 | 7,480 |
| MELI | 2007-08-10 | 4,812 |
| PG | 1997-01-02 | 7,480 |
| XOM | 1997-01-02 | 7,480 |
| RSP | 2003-05-01 | 5,889 |
| IWM | 2000-05-26 | 6,622 |
| VGK | 2005-03-10 | 5,421 |
| VWO | 2005-03-10 | 5,421 |
| SHY | 2002-07-30 | 6,079 |
| IEF | 2002-07-30 | 6,079 |
| TLT | 2002-07-30 | 6,079 |
| TIP | 2003-12-05 | 5,737 |
| LQD | 2002-07-30 | 6,079 |
| HYG | 2007-04-11 | 4,897 |
| EMB | 2007-12-19 | 4,721 |
| DBC | 2006-02-06 | 5,192 |
| DBA | 2007-01-05 | 4,962 |
| UUP | 2007-03-01 | 4,925 |
| XLE | 1998-12-22 | 6,982 |
| XLF | 1998-12-22 | 6,982 |
| KRE | 2006-06-22 | 5,097 |
| XLV | 1998-12-22 | 6,982 |
| XBI | 2006-02-06 | 5,192 |
| XLK | 1998-12-22 | 6,982 |
| XLC | 2018-06-19 | 2,079 |
| SMH | 2000-06-05 | 6,617 |
| IGV | 2001-07-17 | 6,336 |
| XLI | 1998-12-22 | 6,982 |
| ITA | 2006-05-05 | 5,130 |
| IYT | 2004-01-02 | 5,719 |
| XLY | 1998-12-22 | 6,982 |
| XLP | 1998-12-22 | 6,982 |
| XLU | 1998-12-22 | 6,982 |
| XLB | 1998-12-22 | 6,982 |
| VNQ | 2004-09-29 | 5,533 |
| XHB | 2006-02-06 | 5,192 |
| GDX | 2006-05-22 | 5,119 |
| EWJ | 1997-01-02 | 7,480 |
| EIS | 2008-03-28 | 4,654 |
| EWU | 1997-01-02 | 7,480 |
| EWG | 1997-01-02 | 7,480 |
| EWL | 1997-01-02 | 7,480 |
| EWN | 1997-01-02 | 7,480 |
| EWI | 1997-01-02 | 7,480 |
| EWP | 1997-01-02 | 7,480 |
| EWD | 1997-01-02 | 7,480 |
| EWC | 1997-01-02 | 7,480 |
| EWA | 1997-01-02 | 7,480 |
| MCHI | 2011-03-31 | 3,895 |
| INDA | 2012-02-03 | 3,682 |
| EWY | 2000-05-12 | 6,632 |
| EWT | 2000-06-23 | 6,603 |
| EWZ | 2000-07-14 | 6,589 |
| EWW | 1997-01-02 | 7,480 |
| KSA | 2015-09-17 | 2,772 |
| TUR | 2008-03-28 | 4,654 |
| EZA | 2003-02-07 | 5,946 |
| EPOL | 2010-05-26 | 4,109 |
| ARGT | 2011-03-03 | 3,915 |
| GLD | 2004-11-18 | 5,497 |
| SLV | 2006-04-28 | 5,135 |
| CPER | 2011-11-15 | 3,736 |
| USO | 2006-04-10 | 5,148 |
| UNG | 2007-04-18 | 4,892 |
| CORN | 2010-06-09 | 4,100 |
| WEAT | 2011-09-19 | 3,777 |
| SOYB | 2011-09-19 | 3,777 |
| CANE | 2011-09-19 | 3,777 |
| SPY | 1997-01-02 | 7,480 |
| VT | 2008-06-26 | 4,591 |
| BIL | 2007-05-30 | 4,863 |
