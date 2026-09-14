"""Re-ask the model the questions it has already been asked.

The journal records the full context behind every signal. That makes it
possible to change the prompt and see how the model *would* have answered the
same real inputs, without waiting weeks for new cycles to accumulate.

This is honest in a way a backtest of this strategy could not be: the context
was captured live, at the moment the decision was made. Nothing here
reconstructs a past the model never saw.
"""
