"""The history screen: a rule tested on past prices, with the real code, before it gets a live slot.

The owner's process of 27 Sep 2026 (``docs/research/backlog.md``, "History
first, live second"): a new rule idea that needs no model must first pass a
registered history screen -- fixed settings, tested on the years after its
source was published, with the registered cost, using the code that would
run it live. Only an idea that survives can be proposed for a live slot. An
idea that uses the model skips this: the model has read about the past, so
the past cannot test it.

This package runs those screens, and the first one: the rules that already
run live (the locked momentum rule, and tests A, B and C of pre-registration
section 13), replayed on history. It changes nothing in the locked test, its
rules or its decisions, and nothing live reads what it writes.

What it reuses, unchanged, is the point of it:

* the technicals: ``orchestrator.technicals.build_snapshot``, on the same
  two years of daily bars production fetches (``orchestrator.context``);
* the rules: ``rules/momentum.py``, and A, B and C in ``shadow/exploratory.py``;
* the race's scoring: ``analysis.horse_race`` (``race_arm``, ``both_sides``,
  the coin flip of ``rules/control.py``), next open, 3 sessions, the ATR
  stop, 0.10% a side;
* the funds: ``shadow.fund`` (the production ``ExecutionEngine`` and
  ``PositionManager`` on a ``SimBroker``), the VT fund, B's ``TimingFund``
  and C's ``PullbackFund``;
* the journal format and its reader (``analysis.reader``), one file per
  month as ``logs/journal/`` is.

What history cannot give, it says: there is no live price in the past, so
the previous session's final close stands in for it; production's technicals
also carry the current session's partial bar, which daily history does not
have; the watchlist is today's, so funds and companies that closed are
missing (survivorship). ``history.report`` writes each of these into the
report.

What it can never do: trade, reach a broker, read a credential, or ask a
model. CI keeps it that way (``.github/workflows/ci.yml``, "The history
screen cannot trade and asks no model"). It writes only the output directory
it is given.
"""
