SIGNAL JOURNAL SCORING
----------------------
horizon 3 session(s) | entry rule 'auto' | conviction floor 0.30

Coverage
--------
journal lines read        2872
entries                   2872
  produced a signal       2214
  directional             225  (NEUTRAL: 1989)
  scored                  204
  unscored, pending         21  (too recent — no outcome yet)

Does conviction predict the outcome?
------------------------------------
rank correlation, conviction vs signed return: +0.15 (n=204)

conviction        n   hit rate      mean    median
0.00-0.30         1       0.0%     -0.7%     -0.7%  (thin)
0.30-0.45        66      31.8%     -0.9%     -0.4%
0.45-0.60        87      51.7%     -0.2%     +0.0%
0.60-0.75        43      58.1%     +0.3%     +0.8%
0.75-1.00         7      28.6%     +0.1%     -1.1%

Floor at 0.30 — did it filter the right signals?
  acted on (>= floor)  n=203   hit 45.8%  mean -0.3%
  filtered (< floor)   n=1     hit 0.0%  mean -0.7%
  edge +0.4% — the floor is keeping the better signals
  too few to conclude anything (n=1, want 20+)

Which dimension actually carried information?
---------------------------------------------
Each score against the ticker's raw forward return.

dimension         n     rank corr
news            204         -0.07
technical       204         -0.08
fundamental     204         -0.17
analyst         164         -0.11
insider         161         -0.15

Does the learned blend carry information?
-----------------------------------------
The five scores blended into one, against the ticker's raw forward return.
Every line with a signal and a score counts here, NEUTRAL included: the
blend takes a side on those too. 'learned blend' is the composite as it
was journalled, with whatever weights that cycle had -- the walk-forward
record, never a refit that has seen the return it is judged on.

policy                n  called     rank corr  hit rate
model conviction   2025     203         -0.02     45.8%
equal weights      2025    1898         +0.00     49.0%
learned blend      1634    1550         -0.00     50.5%
  learned composites from fitted weights: 1306; from the equal-weight fallback: 328

  model and blend called opposite directions  n=65    model hit 43.1%  blend hit 56.9%

  the learned blend beats the model's conviction but not equal weights; the fitted weights are not yet earning their keep

Does conviction fall when the dimensions disagree?
--------------------------------------------------
The prompt requires it. This needs no price data, so it is answerable
from the first cycle onward.

  all dimensions agree   n=899   mean conviction 0.084
  at least one dissents  n=1315  mean conviction 0.161
  gap -0.078 — conviction is HIGHER when dimensions conflict — the opposite of the instruction
  rank corr, score spread vs conviction: +0.27 (n=2214) (negative is correct)
    ...but spread vs loudest single score: +0.83 (n=2214) — the two are nearly the same series,
    so the raw number above mostly asks 'is something shouting?', and charges
    the model for being confident about a strong signal -- which the prompt asks for.
  holding magnitude fixed:               +0.14 (n=2214) <- THE FINER MEASURE
  The instruction is directional ('bullish news on a technically broken,
  richly valued name'), so what counts is conviction falling when the
  dimensions CONFLICT, not when one of them is merely large.

Is conviction drifting?
-----------------------
A model that creeps toward always-confident makes the floor a no-op.

  first half   n=1107  mean 0.182  above floor 22.9%
  second half  n=1107  mean 0.078  above floor 15.1%
  change -0.104

Input health
------------
  cycles with a context gap  199/2872 (6.9%)
    news unavailable                         198
    CFTC positioning unavailable             1

  bias distribution (2214 signals)
    BULLISH      164  7.4%
    BEARISH       61  2.8%
    NEUTRAL     1989  89.8%
  cycles that produced no signal: 152

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
