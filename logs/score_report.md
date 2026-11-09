SIGNAL JOURNAL SCORING
----------------------
horizon 3 session(s) | entry rule 'auto' | conviction floor 0.30

Coverage
--------
journal lines read        3352
entries                   3352
  produced a signal       2589
  directional             254  (NEUTRAL: 2335)
  scored                  237
  unscored, pending         17  (too recent — no outcome yet)

Does conviction predict the outcome?
------------------------------------
rank correlation, conviction vs signed return: +0.10 (n=237)

conviction        n   hit rate      mean    median
0.00-0.30         1       0.0%     -0.7%     -0.7%  (thin)
0.30-0.45        70      34.3%     -0.9%     -0.4%
0.45-0.60       103      52.4%     -0.5%     +0.1%
0.60-0.75        52      57.7%     +0.1%     +0.8%
0.75-1.00        11      27.3%     -1.1%     -1.2%

Floor at 0.30 — did it filter the right signals?
  acted on (>= floor)  n=236   hit 47.0%  mean -0.5%
  filtered (< floor)   n=1     hit 0.0%  mean -0.7%
  edge +0.2% — the floor is keeping the better signals
  too few to conclude anything (n=1, want 20+)

Which dimension actually carried information?
---------------------------------------------
Each score against the ticker's raw forward return.

dimension         n     rank corr
news            237         -0.08
technical       237         -0.02
fundamental     237         -0.25
analyst         197         -0.05
insider         194         -0.10

Does the learned blend carry information?
-----------------------------------------
The five scores blended into one, against the ticker's raw forward return.
Every line with a signal and a score counts here, NEUTRAL included: the
blend takes a side on those too. 'learned blend' is the composite as it
was journalled, with whatever weights that cycle had -- the walk-forward
record, never a refit that has seen the return it is judged on.

policy                n  called     rank corr  hit rate
model conviction   2395     236         -0.03     47.0%
equal weights      2395    2228         +0.01     50.0%
learned blend      2004    1896         -0.00     50.6%
  learned composites from fitted weights: 1676; from the equal-weight fallback: 328

  model and blend called opposite directions  n=83    model hit 42.2%  blend hit 57.8%

  the learned blend beats the model's conviction but not equal weights; the fitted weights are not yet earning their keep

Does conviction fall when the dimensions disagree?
--------------------------------------------------
The prompt requires it. This needs no price data, so it is answerable
from the first cycle onward.

  all dimensions agree   n=1096  mean conviction 0.074
  at least one dissents  n=1493  mean conviction 0.153
  gap -0.080 — conviction is HIGHER when dimensions conflict — the opposite of the instruction
  rank corr, score spread vs conviction: +0.28 (n=2589) (negative is correct)
    ...but spread vs loudest single score: +0.84 (n=2589) — the two are nearly the same series,
    so the raw number above mostly asks 'is something shouting?', and charges
    the model for being confident about a strong signal -- which the prompt asks for.
  holding magnitude fixed:               +0.15 (n=2589) <- THE FINER MEASURE
  The instruction is directional ('bullish news on a technically broken,
  richly valued name'), so what counts is conviction falling when the
  dimensions CONFLICT, not when one of them is merely large.

Is conviction drifting?
-----------------------
A model that creeps toward always-confident makes the floor a no-op.

  first half   n=1294  mean 0.169  above floor 22.3%
  second half  n=1295  mean 0.071  above floor 13.6%
  change -0.098

Input health
------------
  cycles with a context gap  305/3352 (9.1%)
    news unavailable                         304
    CFTC positioning unavailable             1

  bias distribution (2589 signals)
    BULLISH      190  7.3%
    BEARISH       64  2.5%
    NEUTRAL     2335  90.2%
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
