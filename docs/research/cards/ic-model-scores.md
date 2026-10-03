# The IC report: do the model's scores rank tomorrow's returns?

**Date:** 2026-10-02 (prepared; **registered at the first checkpoint, 2026-12-22**, pre-registration section 13.9). The owner's decisions on the main metric and the trial count: 2026-10-03, before any IC value existed. Nothing on this card is changed after registration.

**Source:** The information coefficient, the cross-sectional rank correlation of a forecast with the next return (Grinold and Kahn, *Active Portfolio Management*, 2000). The owner's choice of scores, horizons and comparator (2026-10-02).

**Exact rule and settings:** For every journal line the model answered (a signal about this ticker, not held; a line with an error written after the answer, such as an unreachable engine, still counts, as in the race), journalled on or after 2026-09-28 (UTC): six scores, the blended score (`blend.composite`) and the five dimension scores (`news_score`, `technical_score`, `fundamental_score`, `analyst_score`, `insider_score`; a missing score leaves that line out for that score). The comparator: the momentum score, +conviction for a BULLISH momentum signal, −conviction for BEARISH, 0 for NEUTRAL (`arms.momentum` on the line). The forward return of a line journalled on UTC day D at horizon h: the open of the first session after D (the race's entry rule) to the close of the h-th session counting that one, price only; h = 1 and h = 3. Each entry day, for each score and horizon: the Spearman rank correlation (ties at their average rank) over the names with both values, if there are at least 10 of them and the score and the return are not the same for every one of them (else the day is skipped for that score, and counted; a news score of 0 on every line is common). A name with two lines on one entry day keeps its last. Then: the mean daily IC; a Newey-West t with lag equal to the horizon (1 and 3); the number of days; the effective number of independent names, measured from the correlations of the names' daily close-to-close returns over the window after each day's average return across the names is taken out (a rank IC ignores a move every name shares): names with returns on fewer than 90% of the window's dates or fewer than 20 returns are left out, the dates every kept name has are used (at least 20 of them, else no n_eff and the reason is given), and n_eff = N² ÷ max(ΣC² − N(N−1)/(T−1), N) for N names, T dates and correlation matrix C (the noise-corrected participation ratio; the uncorrected N² ÷ ΣC² is shown beside it); and the smallest IC that could be detected at t = 2.4: 2.4 × the Newey-West standard error of the mean IC (measured), and 2.4 ÷ √((n_eff − 1) × days ÷ h) (from n_eff). Code: `analysis/ic.py`. Two universes, one rule: the production names (`logs/journal/`) and the shadow stock universe (`logs/shadow_universe/`, from 2027-01-01; the list below).

**Data used:** The journal's answered lines (scores, `arms.momentum`, the UTC time of the line), and final daily bars (open and close) from the race's price source.

**Compared against:** Zero (no ranking skill), and, for reading, the momentum score's IC on the same lines and days, with the daily difference (blended IC minus momentum IC) and its Newey-West t.

**Main metric:** The owner's decision of 2026-10-03: one primary test per universe, the blended score's mean daily rank-IC at 1 session (Newey-West t, lag 1). These two primary tests are the only IC members of the Benjamini-Hochberg family (section 13.5), and each gets its Deflated Sharpe Ratio on the daily IC series (section 13.6). Secondary and descriptive only, not in the family: the IC at 3 sessions (the blended score's included), the five single scores at 1 and 3 sessions, the momentum score's IC and the daily difference blended minus momentum.

**Survives its history screen if:** No history screen (uses the AI).

**History screen:** Not possible (uses the AI).

**Read on:** At each checkpoint only, from the one at which it is registered: 2026-12-22 (over every line from 2026-09-28), 2027-03-22, 2027-06-16 (estimated: the race's looks). Between checkpoints only counters are computed or shown: answered lines with each score, and days. No IC value is written to any file, page or log before the checkpoint (`analysis/ic.py`, `counters` and `due`).

**Acting differently:** A day with an IC for the primary test (the blended score at 1 session; at least 10 names with both values). Fewer than 20 such days by the final checkpoint is "not tested" (section 13.7).

**Promising if:** At a checkpoint, the primary test's mean IC is above zero and passes Benjamini-Hochberg at 5% (section 13.5). The Deflated Sharpe Ratio is shown beside it (13.6). A promising result is only a candidate for a later registration (for example a ranking arm, which the owner said not to build unless this report shows the scores are too coarse); it changes nothing in this one.

**Dead if:** At any checkpoint the primary test's mean IC is below zero and passes Benjamini-Hochberg in that direction; or at the final checkpoint its mean IC is zero or below (section 13.7).

**Trial number:** 35 (the production names); the shadow stock universe is trial 36, the same rule. The owner's decision of 2026-10-03: two trials in N (two universes) and one idea against the quarterly limit (section 13.8), counted in the first quarter of 2027.

## What is stored on every line (the owner asked)

From the 233 lines the model answered between 2026-09-28 and 2026-10-01: the blended score, the news, technical and fundamental scores and the momentum arm are on every line; the analyst score is on 189 (the 44 without it are the 11 bond and commodity funds, which no analyst covers: SHY, LQD, HYG, SLV, CPER, USO, UNG, CORN, WEAT, SOYB and CANE, 4 lines each); the insider score is on 230 (not on one line each of XLK, VNQ and EWI). So every score can be used, each on the lines that have it.

## The shadow stock universe (published on the registration date)

The list as prepared on 2026-10-02 (`config/shadow_universe.py`). It is checked with `backtest/verify_tickers.py` before the registration date, published here on that date, and never changed afterwards. None of these is one of the 80 production names.

**Replacement rule (written 2026-10-03, before the list freezes).** Until the registration date a name may be replaced for one of three reasons only, and never because of its price, its returns or its scores: (1) a merger, buy-out, spin-off or split-off announced for 2026-2027 that could fall inside the scoring window (the name would stop trading, or a price-only return would record the spun-off part as a loss); (2) the news search for its ticker (`"<ticker> stock"`, `orchestrator/news.py`) finds something else, because the ticker's letters are the usual name of something bigger in market news; (3) it does not resolve in the verify check (the `verify` job of `.github/workflows/shadow-universe.yml`, which also runs on every pull request that changes the list). A replacement comes from the same sector or ADR region, is not a production name, and meets the same rules. From the registration date nothing is replaced.

**Replaced on 2026-10-02, before any score of these names existed** (no price, return or score was looked at): Johnson & Johnson (JNJ, DePuy Synthes separation), Medtronic (MDT, MiniMed separation) and S&P Global (SPGI, Mobility spin-off), by rule (1), with Edwards Lifesciences (EW), IDEXX Laboratories (IDXX) and MetLife (MET); Dow Inc. (DOW: "DOW stock" finds the Dow Jones index) and ASE Technology (ASX: "ASX stock" finds the Australian Securities Exchange), by rule (2), with Martin Marietta Materials (MLM) and United Microelectronics (UMC).

**Replaced on 2026-10-03, by rule (3):** BNY Mellon (BK: Yahoo answered "quote not found" and returned no prices) and AvalonBay Communities (AVB: fewer than two closes in three months) failed the verify check in three runs that day (18:14, 18:15 and 18:16 UTC), while the other 249 names resolved in the same runs, and were replaced with State Street (STT) and Iron Mountain (IRM). Again no price, return or score was looked at beyond whether prices exist.

Shadow stock universe: 251 names, chosen on 2026-10-02, frozen on 2026-12-22.

| Sector | Names | Tickers |
|---|---:|---|
| Energy | 16 | BKR, CNQ, COP, CVX, ENB, EOG, FANG, HAL, KMI, MPC, OKE, OXY, PSX, SLB, VLO, WMB |
| Materials | 14 | ALB, APD, CRH, DD, ECL, FCX, LIN, MLM, NEM, NTR, NUE, PPG, SHW, VMC |
| Industrials | 22 | ADP, BA, CMI, CSX, DE, EMR, ETN, GD, GE, ITW, JCI, LHX, LMT, MMM, NOC, PH, RSG, RTX, TT, UNP, UPS, WM |
| Consumer discretionary | 19 | ABNB, AMZN, AZO, BKNG, CMG, F, GM, HD, HLT, LOW, MAR, MCD, NKE, ORLY, ROST, SBUX, TJX, TSLA, YUM |
| Consumer staples | 16 | ADM, CL, COST, GIS, HSY, KMB, KO, KR, MDLZ, MNST, MO, PEP, PM, SYY, TGT, WMT |
| Health care | 22 | ABBV, ABT, AMGN, BMY, BSX, CI, CVS, DHR, ELV, EW, GILD, HCA, IDXX, ISRG, MRK, PFE, REGN, SYK, TMO, UNH, VRTX, ZTS |
| Financials | 24 | AIG, AXP, BAC, BLK, BX, C, CB, CME, COF, GS, ICE, MA, MCO, MET, MS, PGR, PNC, PYPL, SCHW, STT, TRV, USB, V, WFC |
| Information technology | 23 | AAPL, ACN, ADBE, ADI, AMAT, AMD, ANET, AVGO, CDNS, CRM, CSCO, IBM, INTC, INTU, KLAC, LRCX, MU, NOW, ORCL, PANW, QCOM, SNPS, TXN |
| Communication services | 13 | CHTR, CMCSA, DIS, FOXA, LYV, META, NFLX, OMC, SPOT, T, TMUS, TTWO, VZ |
| Utilities | 12 | AEP, CEG, D, DUK, ED, EXC, NEE, PEG, SO, SRE, VST, XEL |
| Real estate | 12 | AMT, CBRE, CCI, DLR, EQIX, IRM, O, PLD, PSA, SPG, VICI, WELL |
| ADR: Europe | 17 | AZN, BBVA, BP, BTI, DEO, GSK, HSBC, ING, NVS, RIO, SAN, SAP, SHEL, SNY, TTE, UBS, UL |
| ADR: Japan | 8 | HMC, IX, MFG, MUFG, NMR, SMFG, SONY, TAK |
| ADR: China and Hong Kong | 8 | BABA, BEKE, BIDU, JD, NTES, PDD, TCOM, ZTO |
| ADR: India | 5 | IBN, INFY, MMYT, RDY, WIT |
| ADR: Latin America | 9 | ABEV, AMX, BAP, FMX, ITUB, NU, PBR, SQM, VALE |
| ADR: Israel | 5 | CHKP, ICL, MNDY, NICE, WIX |
| ADR: Korea and Taiwan | 5 | KB, PKX, SHG, TSM, UMC |
| ADR: Australia | 1 | BHP |
| **Total** | **251** | |
