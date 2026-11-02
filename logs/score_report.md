SIGNAL JOURNAL SCORING
----------------------
horizon 3 session(s) | entry rule 'auto' | conviction floor 0.30

Coverage
--------
journal lines read        2952
entries                   2952
  produced a signal       2273
  directional             227  (NEUTRAL: 2046)
  scored                  210
  unscored, pending         17  (too recent — no outcome yet)

Does conviction predict the outcome?
------------------------------------
rank correlation, conviction vs signed return: +0.14 (n=210)

conviction        n   hit rate      mean    median
0.00-0.30         1       0.0%     -0.7%     -0.7%  (thin)
0.30-0.45        66      31.8%     -0.9%     -0.4%
0.45-0.60        91      52.7%     -0.3%     +0.1%
0.60-0.75        44      59.1%     +0.4%     +0.8%
0.75-1.00         8      25.0%     -0.6%     -1.2%

Floor at 0.30 — did it filter the right signals?
  acted on (>= floor)  n=209   hit 46.4%  mean -0.4%
  filtered (< floor)   n=1     hit 0.0%  mean -0.7%
  edge +0.4% — the floor is keeping the better signals
  too few to conclude anything (n=1, want 20+)

Which dimension actually carried information?
---------------------------------------------
Each score against the ticker's raw forward return.

dimension         n     rank corr
news            210         -0.08
technical       210         -0.08
fundamental     210         -0.19
analyst         170         -0.10
insider         167         -0.11

Does the learned blend carry information?
-----------------------------------------
The five scores blended into one, against the ticker's raw forward return.
Every line with a signal and a score counts here, NEUTRAL included: the
blend takes a side on those too. 'learned blend' is the composite as it
was journalled, with whatever weights that cycle had -- the walk-forward
record, never a refit that has seen the return it is judged on.

policy                n  called     rank corr  hit rate
model conviction   2088     209         -0.02     46.4%
equal weights      2088    1958         +0.01     49.3%
learned blend      1697    1611         +0.01     50.9%
  learned composites from fitted weights: 1369; from the equal-weight fallback: 328

  model and blend called opposite directions  n=70    model hit 44.3%  blend hit 55.7%

  READY TO LEAVE SHADOW: the learned blend carries more information than the model's conviction and than equal weights, and was right more often than not

Does conviction fall when the dimensions disagree?
--------------------------------------------------
The prompt requires it. This needs no price data, so it is answerable
from the first cycle onward.

  all dimensions agree   n=932   mean conviction 0.081
  at least one dissents  n=1341  mean conviction 0.161
  gap -0.080 — conviction is HIGHER when dimensions conflict — the opposite of the instruction
  rank corr, score spread vs conviction: +0.27 (n=2273) (negative is correct)
    ...but spread vs loudest single score: +0.83 (n=2273) — the two are nearly the same series,
    so the raw number above mostly asks 'is something shouting?', and charges
    the model for being confident about a strong signal -- which the prompt asks for.
  holding magnitude fixed:               +0.15 (n=2273) <- THE FINER MEASURE
  The instruction is directional ('bullish news on a technically broken,
  richly valued name'), so what counts is conviction falling when the
  dimensions CONFLICT, not when one of them is merely large.

Is conviction drifting?
-----------------------
A model that creeps toward always-confident makes the floor a no-op.

  first half   n=1136  mean 0.182  above floor 23.2%
  second half  n=1137  mean 0.074  above floor 14.5%
  change -0.108

Input health
------------
  cycles with a context gap  207/2952 (7.0%)
    news unavailable                         206
    CFTC positioning unavailable             1

  bias distribution (2273 signals)
    BULLISH      166  7.3%
    BEARISH       61  2.7%
    NEUTRAL     2046  90.0%
  cycles that produced no signal: 155

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
