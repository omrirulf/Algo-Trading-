# History screens

A **history screen** tests a rule on past prices, with the code that would run
it live, before the rule may be proposed for a live slot. The process is in
[`../backlog.md`](../backlog.md) ("History first, live second"); every screen
has a row in [`../graveyard.md`](../graveyard.md) and counts in N.

A screen is run by hand: the workflow **history screen**
(`.github/workflows/history-screen.yml`) fetches the prices (Yahoo, which the
development sandbox cannot reach), builds a journal from prices only, races
and runs the funds with the real code (`history/`), and commits its
`report.md` and `results.json` to a folder here. The prices and the journal are
kept as a 90-day workflow artifact; their SHA-256s are in the report.

Nothing a screen shows changes the locked test, its rules or its decisions.

| Screen | Date | What | Summary | Report |
| --- | --- | --- | --- | --- |
| `2026-09-rules-running-live` | 2026-09-28 | The rules already running live: momentum, A, B on VT, B's rule on SPY, C (graveyard rows 30-34) | [summary](2026-09-rules-running-live/summary.md) | [report](2026-09-rules-running-live/report.md) |
