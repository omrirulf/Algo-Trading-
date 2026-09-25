SIGNAL JOURNAL SCORING
----------------------
horizon 3 session(s) | entry rule 'auto' | conviction floor 0.30

Coverage
--------
journal lines read        872
entries                   872
  produced a signal       715
  directional             85  (NEUTRAL: 630)
  scored                  75
  unscored, pending         10  (too recent — no outcome yet)

Does conviction predict the outcome?
------------------------------------
rank correlation, conviction vs signed return: +0.28 (n=75)

conviction        n   hit rate      mean    median
0.30-0.45        50      24.0%     -1.0%     -0.6%
0.45-0.60        25      60.0%     +0.8%     +0.8%

Floor at 0.30 — did it filter the right signals?
  acted on (>= floor)  n=75    hit 36.0%  mean -0.4%
  filtered (< floor)   n=0     hit n/a  mean n/a

Which dimension actually carried information?
---------------------------------------------
Each score against the ticker's raw forward return.

dimension         n     rank corr
news             75         -0.15
technical        75         -0.15
fundamental      75         +0.11
analyst          39         +0.27
insider          32         -0.21

Does the learned blend carry information?
-----------------------------------------
The five scores blended into one, against the ticker's raw forward return.
Every line with a signal and a score counts here, NEUTRAL included: the
blend takes a side on those too. 'learned blend' is the composite as it
was journalled, with whatever weights that cycle had -- the walk-forward
record, never a refit that has seen the return it is judged on.

policy                n  called     rank corr  hit rate
model conviction    602      75         -0.08     36.0%
equal weights       602     595         -0.09     47.1%
learned blend       211     207         +0.06     56.5%
  learned composites from fitted weights: 53; from the equal-weight fallback: 158

  model and blend called opposite directions  n=7     model hit 28.6%  blend hit 71.4%

  READY TO LEAVE SHADOW: the learned blend carries more information than the model's conviction and than equal weights, and was right more often than not

Does conviction fall when the dimensions disagree?
--------------------------------------------------
The prompt requires it. This needs no price data, so it is answerable
from the first cycle onward.

  all dimensions agree   n=206   mean conviction 0.223
  at least one dissents  n=509   mean conviction 0.261
  gap -0.039 — conviction is HIGHER when dimensions conflict — the opposite of the instruction
  rank corr, score spread vs conviction: +0.30 (n=715) (negative is correct)
    ...but spread vs loudest single score: +0.80 (n=715) — the two are nearly the same series,
    so the raw number above mostly asks 'is something shouting?', and charges
    the model for being confident about a strong signal -- which the prompt asks for.
  holding magnitude fixed:               -0.01 (n=715) <- THE FINER MEASURE
  The instruction is directional ('bullish news on a technically broken,
  richly valued name'), so what counts is conviction falling when the
  dimensions CONFLICT, not when one of them is merely large.

Is conviction drifting?
-----------------------
A model that creeps toward always-confident makes the floor a no-op.

  first half   n=357   mean 0.290  above floor 37.0%
  second half  n=358   mean 0.210  above floor 20.7%
  change -0.080

Input health
------------
  cycles with a context gap  20/872 (2.3%)
    news unavailable                         20

  bias distribution (715 signals)
    BULLISH       41  5.7%
    BEARISH       44  6.2%
    NEUTRAL      630  88.1%
  cycles that produced no signal: 71

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
