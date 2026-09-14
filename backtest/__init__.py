"""Replay price history through the risk engine's own arithmetic.

This does not backtest the *strategy* -- it cannot, because the model's
judgement is not reconstructible from price history. It backtests the
deterministic half: the ATR stop and the position cap. Those are pure
functions of price and volatility, so replaying them against two years of real
bars answers questions that otherwise need months of live trading:

    Is a 2x ATR stop hit so often that it is noise rather than protection?
    What fraction of equity does a single trade actually put at risk?
    How often does price gap straight through the stop?

Every trade here is synthetic. No signal quality is claimed or measured.
"""
