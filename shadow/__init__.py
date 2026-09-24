"""Shadow funds: the whole system's real machinery, run on simulated books.

The horse race (``analysis/horse_race.py``) judges each arm's calls one
trade at a time, three sessions each, no portfolio. This package asks the
question the race cannot: what would each arm have done with a real book --
the real engine's sizing, stops, exposure caps and conviction floor, the
real position manager's profit ladder, trailing stop and group-cap trims --
starting from $100,000 of cash.

Nothing here can trade. Every book is a ``SimBroker`` in memory; the
engine and the position manager are the production classes, handed that
broker, a feed that only ever shows them bars they could have seen, and an
audit record of their own. No credential is read, no model is called, no
file is written: results are printed, and a workflow step decides where
they go. CI enforces all of it (``.github/workflows/ci.yml``, "The shadow
funds cannot trade").
"""
