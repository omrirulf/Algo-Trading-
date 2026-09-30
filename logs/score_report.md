SIGNAL JOURNAL SCORING
----------------------
horizon 3 session(s) | entry rule 'auto' | conviction floor 0.30

Coverage
--------
journal lines read        1112
entries                   1112
  produced a signal       887
  directional             92  (NEUTRAL: 795)
  scored                  85
  unscored, pending         7  (too recent — no outcome yet)

Does conviction predict the outcome?
------------------------------------
rank correlation, conviction vs signed return: +0.31 (n=85)

conviction        n   hit rate      mean    median
0.30-0.45        50      24.0%     -1.0%     -0.5%
0.45-0.60        31      58.1%     +0.6%     +0.8%
0.60-0.75         4      75.0%     -0.1%     +1.2%  (thin)

Floor at 0.30 — did it filter the right signals?
  acted on (>= floor)  n=85    hit 38.8%  mean -0.4%
  filtered (< floor)   n=0     hit n/a  mean n/a

Which dimension actually carried information?
---------------------------------------------
Each score against the ticker's raw forward return.

dimension         n     rank corr
news             85         -0.10
technical        85         -0.14
fundamental      85         +0.13
analyst          49         +0.08
insider          42         -0.25

Does the learned blend carry information?
-----------------------------------------
The five scores blended into one, against the ticker's raw forward return.
Every line with a signal and a score counts here, NEUTRAL included: the
blend takes a side on those too. 'learned blend' is the composite as it
was journalled, with whatever weights that cycle had -- the walk-forward
record, never a refit that has seen the return it is judged on.

policy                n  called     rank corr  hit rate
model conviction    715      85         -0.07     38.8%
equal weights       715     696         -0.07     45.8%
learned blend       324     305         +0.06     51.1%
  learned composites from fitted weights: 53; from the equal-weight fallback: 271

  model and blend called opposite directions  n=7     model hit 28.6%  blend hit 71.4%

  READY TO LEAVE SHADOW: the learned blend carries more information than the model's conviction and than equal weights, and was right more often than not

Does conviction fall when the dimensions disagree?
--------------------------------------------------
The prompt requires it. This needs no price data, so it is answerable
from the first cycle onward.

  all dimensions agree   n=276   mean conviction 0.169
  at least one dissents  n=611   mean conviction 0.226
  gap -0.057 — conviction is HIGHER when dimensions conflict — the opposite of the instruction
  rank corr, score spread vs conviction: +0.25 (n=887) (negative is correct)
    ...but spread vs loudest single score: +0.81 (n=887) — the two are nearly the same series,
    so the raw number above mostly asks 'is something shouting?', and charges
    the model for being confident about a strong signal -- which the prompt asks for.
  holding magnitude fixed:               +0.03 (n=887) <- THE FINER MEASURE
  The instruction is directional ('bullish news on a technically broken,
  richly valued name'), so what counts is conviction falling when the
  dimensions CONFLICT, not when one of them is merely large.

Is conviction drifting?
-----------------------
A model that creeps toward always-confident makes the floor a no-op.

  first half   n=443   mean 0.288  above floor 35.2%
  second half  n=444   mean 0.129  above floor 14.0%
  change -0.159

Input health
------------
  cycles with a context gap  28/1112 (2.5%)
    news unavailable                         28

  bias distribution (887 signals)
    BULLISH       46  5.2%
    BEARISH       46  5.2%
    NEUTRAL      795  89.6%
  cycles that produced no signal: 73

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
