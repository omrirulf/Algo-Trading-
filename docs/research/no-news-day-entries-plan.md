# No new entries on a day when a tenth or more of the list has no news: the plan

**Status: planned.** The owner's decision of 10 Nov 2026 ("yes to both", item 5b) to the proposal of 4 Nov
2026. A trading rule for the production account, so it is logged in the pre-registration's Amendments table as
planned and built only after the owner says "build".

## 1. What happens today

Since 21 Sep 2026 a name whose news search fails is judged on its other four sections, and the daily health
check counts those names: a warning for one, **critical when a tenth or more of the list** has no news
(`analysis/health.py`, `FAILED_SHARE_CRITICAL` 0.10, the `news unavailable` gap on the journal line). The
cycle itself does not read that count: it enters trades on such a day as on any other.

The record: 3 Nov, 80 of 80 names without news (a Bright Data outage), six entries -- ASML, EWY and CAT were
stopped out on 5 Nov at 8-9% losses, HDB, TM and PG are in profit; 9 Nov, 11 of 80 without news, two entries
(ITA, EWC); 10 Nov, 14 of 80, two entries (XHB, EPOL, the latter with no headline at all and the lowest
allowed conviction). Under this rule none of those ten entries would have been made. A signal judged on four
fifths of its context is not the signal the race registered, and the day the vendor is down is the day the
model knows least about the news it was built to read.

## 2. The rule

- A **no-news day**: after the context stage of the batched cycle (`orchestrator/heartbeat.py`,
  `run_batched_cycle`, once every name's context is gathered and before the model is asked), the cycle counts
  the names whose context carries a `news unavailable` gap, with the health check's own definition and
  threshold: the gap prefix (`NEWS_GAP_PREFIX`) over every name of the day, held names included, against
  `FAILED_SHARE_CRITICAL` (a tenth). The same count the health check makes, made once, before any trade.
- On a no-news day the model is still asked and every line is journalled as today (the race scores signals,
  not trades, and nothing about the signals changes), but **no new entry is dispatched**: each directional line
  is journalled `REJECTED` with the reason `no new entries today: N of M names have no news` -- the brief, the
  health check and the daily check all read it -- and the engine is not called for it. A NEUTRAL line is
  unchanged (it never trades).
- The rest of the day is unchanged: the management pass, the stops, the profit ladder and the protection pass
  run exactly as before; the positions already held are not closed or trimmed by this rule.
- A day with no news for fewer than a tenth of the list is a normal day.

## 3. Where it applies, and where it does not

- **Production** (the paper account): yes, as above.
- **The calibration copy** (`shadow/calibration.py`): it must do what the account did, so it reads the same
  count from the journal lines of that cycle day (the gaps are on the lines) and refuses the same entries with
  the same reason; otherwise every refused entry would read as a difference. This is the one place outside
  production the rule reaches, and only to keep the copy equal to the account.
- **The four funds, the coin-flip funds and the exploratory funds**: unchanged. The fund test is
  pre-registered (section 11) and runs each arm's signals through the engine as registered; a rule added to the
  model fund's dispatch mid-sample would change the arm the test is measuring. On a no-news day production and
  the model fund will differ, and the daily check will say so. If the owner wants the funds to follow the rule
  as well, that is a separate amendment of the fund test.
- **The race**: unchanged (it scores signals, not executions).

## 4. Tests, record and cost

- `tests/test_heartbeat*.py`: eight of eighty contexts with a news gap refuse every directional line with the
  reason and call the engine for none; seven of eighty enter as usual; held names count in the denominator
  as the health check counts them; a NEUTRAL line is unchanged; the management pass still runs.
- `tests/test_shadow_calibration.py`: the copy refuses the same lines on a no-news day read from the journal,
  and a real entry made that day (none should exist) would read "unexplained".
- The brief's line "N of M ticker(s) were judged without news" is already there; a line "no new entries today"
  is added next to it so the owner sees the rule act.
- Cost: none. The model is asked as today; only the orders are withheld.
- The Amendments row below is marked planned; when the change is merged the row gets its effective date.

## 5. The Amendments row (planned)

| 2026-11-10 | **No new entries on a day when a tenth or more of the list has no news** (planned; the owner's
"yes" of 2026-11-10, item 5b; a trading rule of the production account and its calibration copy; the race, the
four funds and the exploratory funds are unchanged) | Since 2026-09-21 a name whose news search fails is judged
on its other four sections; the health check calls a tenth of the list without news critical, but the cycle
still trades: six entries on 2026-11-03 (80 of 80 without news; three stopped out at 8-9% losses), two on
2026-11-09 (11 of 80) and two on 2026-11-10 (14 of 80). The plan (`docs/research/no-news-day-entries-plan.md`):
after the context stage the cycle counts the names with a `news unavailable` gap by the health check's own
definition and threshold (`FAILED_SHARE_CRITICAL`, a tenth of the day's names); on such a day the model is
still asked and every line journalled, but no new entry is dispatched: each directional line reads REJECTED
with the reason "no new entries today: N of M names have no news"; the management pass, the stops, the ladder
and the protection pass are unchanged. The calibration copy applies the same rule from the journal, so it does
what the account did. Built only after the owner says "build". |
