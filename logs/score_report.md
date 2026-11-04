SIGNAL JOURNAL SCORING
----------------------
horizon 3 session(s) | entry rule 'auto' | conviction floor 0.30

Coverage
--------
journal lines read        3112
entries                   3112
  produced a signal       2395
  directional             237  (NEUTRAL: 2158)
  scored                  225
  unscored, pending         12  (too recent — no outcome yet)

Does conviction predict the outcome?
------------------------------------
rank correlation, conviction vs signed return: +0.11 (n=225)

conviction        n   hit rate      mean    median
0.00-0.30         1       0.0%     -0.7%     -0.7%  (thin)
0.30-0.45        69      34.8%     -0.7%     -0.3%
0.45-0.60        97      53.6%     -0.3%     +0.1%
0.60-0.75        48      58.3%     +0.2%     +0.8%
0.75-1.00        10      30.0%     -1.0%     -1.2%

Floor at 0.30 — did it filter the right signals?
  acted on (>= floor)  n=224   hit 47.8%  mean -0.3%
  filtered (< floor)   n=1     hit 0.0%  mean -0.7%
  edge +0.4% — the floor is keeping the better signals
  too few to conclude anything (n=1, want 20+)

Which dimension actually carried information?
---------------------------------------------
Each score against the ticker's raw forward return.

dimension         n     rank corr
news            225         -0.07
technical       225         -0.05
fundamental     225         -0.20
analyst         185         -0.08
insider         182         -0.08

Does the learned blend carry information?
-----------------------------------------
The five scores blended into one, against the ticker's raw forward return.
Every line with a signal and a score counts here, NEUTRAL included: the
blend takes a side on those too. 'learned blend' is the composite as it
was journalled, with whatever weights that cycle had -- the walk-forward
record, never a refit that has seen the return it is judged on.

policy                n  called     rank corr  hit rate
model conviction   2214     224         -0.02     47.8%
equal weights      2214    2073         +0.01     50.1%
learned blend      1823    1732         -0.00     49.8%
  learned composites from fitted weights: 1495; from the equal-weight fallback: 328

  model and blend called opposite directions  n=76    model hit 44.7%  blend hit 55.3%

  the learned blend beats the model's conviction but not equal weights; the fitted weights are not yet earning their keep

Does conviction fall when the dimensions disagree?
--------------------------------------------------
The prompt requires it. This needs no price data, so it is answerable
from the first cycle onward.

  all dimensions agree   n=991   mean conviction 0.078
  at least one dissents  n=1404  mean conviction 0.158
  gap -0.080 — conviction is HIGHER when dimensions conflict — the opposite of the instruction
  rank corr, score spread vs conviction: +0.27 (n=2395) (negative is correct)
    ...but spread vs loudest single score: +0.84 (n=2395) — the two are nearly the same series,
    so the raw number above mostly asks 'is something shouting?', and charges
    the model for being confident about a strong signal -- which the prompt asks for.
  holding magnitude fixed:               +0.15 (n=2395) <- THE FINER MEASURE
  The instruction is directional ('bullish news on a technically broken,
  richly valued name'), so what counts is conviction falling when the
  dimensions CONFLICT, not when one of them is merely large.

Is conviction drifting?
-----------------------
A model that creeps toward always-confident makes the floor a no-op.

  first half   n=1197  mean 0.177  above floor 22.8%
  second half  n=1198  mean 0.073  above floor 14.2%
  change -0.104

Input health
------------
  cycles with a context gap  290/3112 (9.3%)
    news unavailable                         289
    CFTC positioning unavailable             1

  bias distribution (2395 signals)
    BULLISH      176  7.3%
    BEARISH       61  2.5%
    NEUTRAL     2158  90.1%
  cycles that produced no signal: 159

How to read this
----------------
* Returns are close-to-close over 3 session(s) and ignore the stop-loss,
  slippage and commission. They measure the signal, not the strategy's P&L.
* Entry rule 'auto': same-session close when the signal fired before the close
  and carried an exact UTC timestamp, next session's close otherwise.
* Anything marked 'too few' has fewer than 20 observations. It is
  arithmetic, not evidence — the sign can flip on one more data point.
* A single earnings day can dominate a small sample; rank correlations are
  used throughout to blunt that, not to eliminate it.
