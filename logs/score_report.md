SIGNAL JOURNAL SCORING
----------------------
horizon 3 session(s) | entry rule 'auto' | conviction floor 0.30

Coverage
--------
journal lines read        792
entries                   792
  produced a signal       664
  directional             84  (NEUTRAL: 580)
  scored                  68
  unscored, pending         16  (too recent — no outcome yet)

Does conviction predict the outcome?
------------------------------------
rank correlation, conviction vs signed return: +0.25 (n=68)

conviction        n   hit rate      mean    median
0.30-0.45        44      27.3%     -0.8%     -0.5%
0.45-0.60        24      54.2%     +0.8%     +1.1%

Floor at 0.30 — did it filter the right signals?
  acted on (>= floor)  n=68    hit 36.8%  mean -0.2%
  filtered (< floor)   n=0     hit n/a  mean n/a

Which dimension actually carried information?
---------------------------------------------
Each score against the ticker's raw forward return.

dimension         n     rank corr
news             68         -0.05
technical        68         -0.07
fundamental      68         +0.21
analyst          33         +0.37
insider          26         -0.02

Does the learned blend carry information?
-----------------------------------------
The five scores blended into one, against the ticker's raw forward return.
Every line with a signal and a score counts here, NEUTRAL included: the
blend takes a side on those too. 'learned blend' is the composite as it
was journalled, with whatever weights that cycle had -- the walk-forward
record, never a refit that has seen the return it is judged on.

policy                n  called     rank corr  hit rate
model conviction    483      68         -0.06     36.8%
equal weights       483     479         -0.04     47.0%
learned blend       165     161         +0.06     54.7%
  learned composites from fitted weights: 7; from the equal-weight fallback: 158

  model and blend called opposite directions  n=1     model hit 100.0%  blend hit 0.0%

  READY TO LEAVE SHADOW: the learned blend carries more information than the model's conviction and than equal weights, and was right more often than not

Does conviction fall when the dimensions disagree?
--------------------------------------------------
The prompt requires it. This needs no price data, so it is answerable
from the first cycle onward.

  all dimensions agree   n=184   mean conviction 0.245
  at least one dissents  n=480   mean conviction 0.274
  gap -0.028 — conviction is HIGHER when dimensions conflict — the opposite of the instruction
  rank corr, score spread vs conviction: +0.33 (n=664) (negative is correct)
    ...but spread vs loudest single score: +0.80 (n=664) — the two are nearly the same series,
    so the raw number above mostly asks 'is something shouting?', and charges
    the model for being confident about a strong signal -- which the prompt asks for.
  holding magnitude fixed:               -0.02 (n=664) <- THE FINER MEASURE
  The instruction is directional ('bullish news on a technically broken,
  richly valued name'), so what counts is conviction falling when the
  dimensions CONFLICT, not when one of them is merely large.

Is conviction drifting?
-----------------------
A model that creeps toward always-confident makes the floor a no-op.

  first half   n=332   mean 0.286  above floor 34.9%
  second half  n=332   mean 0.246  above floor 25.6%
  change -0.040

Input health
------------
  cycles with a context gap  16/792 (2.0%)
    news unavailable                         16

  bias distribution (664 signals)
    BULLISH       40  6.0%
    BEARISH       44  6.6%
    NEUTRAL      580  87.3%
  cycles that produced no signal: 64

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
