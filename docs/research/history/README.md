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

**Two kinds.** The workflow's `kind` input picks the screen:

- `full` (the default): the rules running live, the race and the funds, from
  2000 to now.
- `stress` (the owner's instruction of 2 Oct 2026): momentum, A, B, C, VT and
  SPY in four bad periods, 2000-2002, 2008, 2020 and 2022 (`history/stress.py`).
  Each fund starts fresh with $100,000 on each period's first session. The
  report shows the total return, the worst fall (maximum drawdown) and the
  return against VT, and against SPY where VT did not exist yet. Where a
  fund's prices did not exist (VT before June 2008, so no VT and no B in
  2000-2002, and no B in 2008), it says "not possible" and why; nothing
  stands in for a missing fund. It is descriptive only: no t and no verdict.
  No AI arm is run, because the model has read about these years. The same
  report also holds VT's 21-day volatility terciles up to 2026-09-30: the
  fixed cut-offs of the regime split (pre-registration section 13.10).
  Its folder is `2026-10-stress-periods` (graveyard rows 37 to 40).

| Screen | Date | What | Summary | Report |
| --- | --- | --- | --- | --- |
| `2026-09-rules-running-live` | 2026-09-28 | The rules already running live: momentum, A, B on VT, B's rule on SPY, C (graveyard rows 30-34) | [summary](2026-09-rules-running-live/summary.md) | [report](2026-09-rules-running-live/report.md) |
| `2026-10-stress-periods` | 2026-10-02 | Stress periods 2000-2002, 2008, 2020, 2022: momentum, A, B, C, VT, SPY; the regime split's cut-offs (graveyard rows 37-40) | - | [report](2026-10-stress-periods/report.md) |
