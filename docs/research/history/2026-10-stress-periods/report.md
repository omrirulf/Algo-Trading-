# History screen: stress periods (2000-2002, 2008, 2020 and 2022)

*Written by `python -m history.screen run --kind stress` (workflow run 37013435615, commit `1f28fec6c710`) on 2026-10-02T13:35:08+00:00. Prices through 2026-10-01. Price table SHA-256 `53c10c908d66284a330f327fec181651052e790052abe8ad0af937eb6bc46591`; history journal SHA-256 `f0826e889bc1982041fa395c12f7a028d648e2fe5b95ebe5a2d70e33feb84d89` (87,089 lines).*

**Nothing here changes the locked test, its rules or its decisions.** This is a history screen: it replays, on past prices, the rules that need no model, with the real code. It did not read the live race.

**Descriptive only.** This report shows how deep each fund fell, and how it did against holding VT (or SPY), in four bad stretches of the market. It has no t and no verdict: four periods, each chosen because it was bad, cannot show whether a rule is good or bad. The 80 names are today's watchlist: many did not exist in 2000 (each period below says how many had prices), and funds and companies that closed before 2026 are missing (survivorship).

## How it was made

- **Periods** (fixed in the code, `history/stress.py`): 2000-2002: 2000-01-03 to 2002-12-31; 2008: 2008-01-02 to 2008-12-31; 2020: 2020-01-02 to 2020-12-31; 2022: 2022-01-03 to 2022-12-30. Each end is a trading day.
- **A fresh start in each period:** every fund starts with $100,000 on the period's first session. The indicators warm up on the prices before it: each line's technicals (momentum's 63-day return and 50-day average) read the two years of final closes before its day, A's 200-day average reads the 200 closes before it, and B decides at the last month-end before the period from VT's 10 month-end closes up to it. The first trades are at the open of the first session, on the lines of the session before it (the live funds act on the previous session's lines the same way).
- **Funds:** momentum, A (the 200-day veto) and C (the pullback limit) through the production engine; B (VT or T-bills by the 10-month average); VT and SPY bought and held. The same code as the full screen. **No AI arms:** the model has read about these years, so they cannot test it.
- **As in the full screen:** the previous session's final close stands in for the live price; prices are Yahoo's daily bars adjusted for splits (not for dividends); 0.10% per side on every trade; dividends on the ex-date (the held funds keep them as cash); no taxes.
- **Not possible:** where a fund's prices do not exist, the report says "not possible" and why. Nothing stands in for a missing fund.
- **Words:** *total return* is over the fund's own sessions in the period; *worst fall* is the maximum drawdown, the deepest fall from the running high within the period (the start counts as a high); *minus VT* is the fund's total return minus VT's over the same sessions (when VT starts later in the period, over VT's sessions only: VT is then measured from its cash before its purchase at that session's open, so its 0.10% cost is inside, and the other fund from its close the session before, so one overnight move is inside), and *minus SPY* the same against SPY; *invested* is the book's gross exposure as a share of equity.

## 2000-2002 (2000-01-03 to 2002-12-31, 752 sessions)

Names with prices: 44 of the 80 watchlist names (33 from the first session; the others started during the period). First trades at the open of 2000-01-03, on the lines of 1999-12-31.

**VT did not exist; against SPY instead.** VT's first price is 2008-06-26, so there is no VT fund here, and each fund's return is shown against SPY (bought and held from the same $100,000).

| Fund | From | To | Sessions | Total return | Worst fall | Invested (mean) | Minus VT (same sessions) | Minus SPY (same sessions): VT did not exist; against SPY instead |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Momentum fund | 2000-01-03 | 2002-12-31 | 752 | -29.5% | 33.7% | 72% | not possible: VT did not exist (its first price is 2008-06-26) | +8.0% (-29.5% vs -37.5%) |
| A fund (200-day veto) | 2000-01-03 | 2002-12-31 | 752 | -27.9% | 33.0% | 70% | not possible: VT did not exist (its first price is 2008-06-26) | +9.6% (-27.9% vs -37.5%) |
| B fund (VT or T-bills) | not possible: VT did not exist (its first price is 2008-06-26); BIL (B's T-bills) did not exist yet (its first price is 2007-05-30) | - | - | - | - | - | - | - |
| C fund (pullback limit) | 2000-01-03 | 2002-12-31 | 752 | -23.4% | 27.1% | 71% | not possible: VT did not exist (its first price is 2008-06-26) | +14.1% (-23.4% vs -37.5%) |
| VT fund (held) | not possible: VT did not exist (its first price is 2008-06-26) | - | - | - | - | - | - | - |
| SPY fund (held) | 2000-01-03 | 2002-12-31 | 752 | -37.5% | 46.6% | 98% | not possible: VT did not exist (its first price is 2008-06-26) | - |

Entries: Momentum fund 1,467, A fund (200-day veto) 1,382, C fund (pullback limit) 1,269.

## 2008 (2008-01-02 to 2008-12-31, 253 sessions)

Names with prices: 69 of the 80 watchlist names (67 from the first session; the others started during the period). First trades at the open of 2008-01-02, on the lines of 2007-12-31.

VT only from 2008-06-26 (its first price): *minus VT* is over VT's sessions only, from that day; *minus SPY* is over the whole period.

| Fund | From | To | Sessions | Total return | Worst fall | Invested (mean) | Minus VT (same sessions) | Minus SPY (same sessions) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Momentum fund | 2008-01-02 | 2008-12-31 | 253 | -3.2% | 19.0% | 86% | +43.7% (+10.1% vs -33.6%), from 2008-06-26 | +33.4% (-3.2% vs -36.6%) |
| A fund (200-day veto) | 2008-01-02 | 2008-12-31 | 253 | +5.8% | 17.4% | 85% | +46.0% (+12.4% vs -33.6%), from 2008-06-26 | +42.4% (+5.8% vs -36.6%) |
| B fund (VT or T-bills) | not possible: B needs VT's month-end closes for the 10 months up to 2007-12-31, its first decision; VT's first price is 2008-06-26 | - | - | - | - | - | - | - |
| C fund (pullback limit) | 2008-01-02 | 2008-12-31 | 253 | -5.5% | 20.3% | 85% | +44.8% (+11.2% vs -33.6%), from 2008-06-26 | +31.0% (-5.5% vs -36.6%) |
| VT fund (held) | 2008-06-26 | 2008-12-31 | 131 | -33.6% | 46.7% | 100% | - | -3.5% (-33.6% vs -30.1%), from 2008-06-26 |
| SPY fund (held) | 2008-01-02 | 2008-12-31 | 253 | -36.6% | 47.1% | 99% | +3.5% (-30.1% vs -33.6%), from 2008-06-26 | - |

Entries: Momentum fund 629, A fund (200-day veto) 602, C fund (pullback limit) 607.

## 2020 (2020-01-02 to 2020-12-31, 253 sessions)

Names with prices: 80 of the 80 watchlist names (80 from the first session). First trades at the open of 2020-01-02, on the lines of 2019-12-31.

| Fund | From | To | Sessions | Total return | Worst fall | Invested (mean) | Minus VT (same sessions) | Minus SPY (same sessions) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Momentum fund | 2020-01-02 | 2020-12-31 | 253 | -3.1% | 21.5% | 87% | -18.6% (-3.1% vs +15.5%) | -20.3% (-3.1% vs +17.2%) |
| A fund (200-day veto) | 2020-01-02 | 2020-12-31 | 253 | -1.8% | 21.5% | 86% | -17.3% (-1.8% vs +15.5%) | -19.0% (-1.8% vs +17.2%) |
| B fund (VT or T-bills) | 2020-01-02 | 2020-12-31 | 253 | +13.0% | 11.1% | 100% | -2.5% (+13.0% vs +15.5%) | -4.2% (+13.0% vs +17.2%) |
| C fund (pullback limit) | 2020-01-02 | 2020-12-31 | 253 | +0.5% | 23.5% | 87% | -15.0% (+0.5% vs +15.5%) | -16.7% (+0.5% vs +17.2%) |
| VT fund (held) | 2020-01-02 | 2020-12-31 | 253 | +15.5% | 34.2% | 99% | - | -1.7% (+15.5% vs +17.2%) |
| SPY fund (held) | 2020-01-02 | 2020-12-31 | 253 | +17.2% | 33.6% | 99% | +1.7% (+17.2% vs +15.5%) | - |

Entries: Momentum fund 719, A fund (200-day veto) 717, C fund (pullback limit) 707. B fund (VT or T-bills): first decision 2019-12-31, 2 switches in the period.

## 2022 (2022-01-03 to 2022-12-30, 251 sessions)

Names with prices: 80 of the 80 watchlist names (80 from the first session). First trades at the open of 2022-01-03, on the lines of 2021-12-31.

| Fund | From | To | Sessions | Total return | Worst fall | Invested (mean) | Minus VT (same sessions) | Minus SPY (same sessions) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Momentum fund | 2022-01-03 | 2022-12-30 | 251 | -12.4% | 19.2% | 87% | +6.0% (-12.4% vs -18.4%) | +6.0% (-12.4% vs -18.4%) |
| A fund (200-day veto) | 2022-01-03 | 2022-12-30 | 251 | -10.1% | 16.0% | 87% | +8.3% (-10.1% vs -18.4%) | +8.3% (-10.1% vs -18.4%) |
| B fund (VT or T-bills) | 2022-01-03 | 2022-12-30 | 251 | -8.8% | 9.9% | 100% | +9.7% (-8.8% vs -18.4%) | +9.6% (-8.8% vs -18.4%) |
| C fund (pullback limit) | 2022-01-03 | 2022-12-30 | 251 | -14.2% | 18.3% | 88% | +4.2% (-14.2% vs -18.4%) | +4.2% (-14.2% vs -18.4%) |
| VT fund (held) | 2022-01-03 | 2022-12-30 | 251 | -18.4% | 26.0% | 99% | - | -0.0% (-18.4% vs -18.4%) |
| SPY fund (held) | 2022-01-03 | 2022-12-30 | 251 | -18.4% | 24.3% | 99% | +0.0% (-18.4% vs -18.4%) | - |

Entries: Momentum fund 709, A fund (200-day veto) 705, C fund (pullback limit) 738. B fund (VT or T-bills): first decision 2021-12-31, 2 switches in the period.

## VT 21-day realized volatility terciles, from its first 21 returns to 2026-09-30 (the regime split's cut-offs, pre-registration section 13.10)

Each session's volatility is the annualised standard deviation (x sqrt(252)) of VT's 21 daily log returns ending at that session's own final close (adjusted for splits, not for dividends, as the race and the funds read it), from the first session with 21 returns (2008-07-28) to 2026-09-30: 4,573 sessions. The cut-offs are the 1/3 and 2/3 quantiles of that series (numpy's default method, 'linear'; `analysis.regimes.tercile_cutoffs`). In the regime split itself, a session's state uses the volatility up to the previous close.

| Tercile | 21-day volatility (a year) | Sessions |
| --- | --- | --- |
| low | up to 11.30% | 1,525 |
| mid | over 11.30%, up to 16.97% | 1,524 |
| high | over 16.97% | 1,524 |

At full precision (`results.json`, `regime_cutoffs`): c1 = 0.11302353418809083, c2 = 0.16965241927688823.

## Data

First prices: SPY 1997-01-02, VT 2008-06-26, BIL 2007-05-30.

Warm-up: the first period needs prices from 1997-12-24; the calendar (SPY) starts 1997-01-02 (enough).

- 2000-2002: fund integrity no problems; 0 ticker-days with no bar met by the funds.
- 2008: fund integrity no problems; 0 ticker-days with no bar met by the funds.
- 2020: fund integrity no problems; 0 ticker-days with no bar met by the funds.
- 2022: fund integrity no problems; 0 ticker-days with no bar met by the funds.
