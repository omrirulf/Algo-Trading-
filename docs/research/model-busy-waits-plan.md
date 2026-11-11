# Longer waits between the retries of a "Model busy" answer: the plan

**Status: planned.** The owner's decision of 10 Nov 2026 ("waits yes") to the proposal of 4 Nov 2026:
longer waits between the retries of a "Model busy" (HTTP 429) answer, about 15, 30 and 60 seconds. A
model-stage setting is an amendment and the owner's decision, so this is the plan, logged in the
pre-registration's Amendments table as planned; the code changes only after the owner says "build".

## 1. What happens today

`orchestrator/llm.py` asks the full model up to `HTTP_ATTEMPTS` (4) times per name. Between asks it waits
on one ladder for every status it retries (`RETRY_STATUSES`: 429, 500, 502, 503, 504): `RETRY_BASE_SECONDS`
(2.0) doubling to `RETRY_CAP_SECONDS` (60), so 2, 4 and 8 seconds, 14 seconds in all. A `Retry-After` header
up to `RETRY_AFTER_CAP_SECONDS` (120) wins over the ladder when the provider sends one. A name still busy
after the fourth ask is lost for the day: no signal, no trade, and a model error for trigger (c).

DeepInfra's "Model busy" is a token-per-minute ceiling (measured on 23 Sep 2026: 50 of 300 calls at four in
flight, 39 at eight), so a spell lasts tens of seconds, not two. The record since streaming went live
(19 Oct): "Model busy" answers per cycle day 15, 5, 28, 23, 39, 38, 61, 1, 0, 0, 0, 0 (26 Oct to 10 Nov); names
lost 1, 0, 3, 2, 1, 3, 4, 0, 0, 0, 0, 0, nearly all to a 429 spell that outlasted 14 seconds. Since 4 Nov the
provider has answered every ask; the change is for the next busy week, not for today.

## 2. The change

- A second ladder for 429 only: `BUSY_BASE_SECONDS = 15.0`, doubling to the same `RETRY_CAP_SECONDS` (60):
  15, 30 and 60 seconds between the four asks, 105 seconds in all. The 5xx family keeps 2, 4 and 8: a
  server error is a transient, not a bucket to wait out.
- `Retry-After` keeps winning when the provider sends one (still capped at 120 seconds).
- `HTTP_ATTEMPTS` stays 4, the 480-second limit per ask stays, the schema re-asks stay, the concurrency
  (4 names in flight) stays. Nothing about the model, its settings or the prompt changes.

## 3. What it costs and what it risks

- No extra calls: the same four asks, spaced further apart. A name that was lost after 14 seconds of waiting
  now gets 105 seconds for the bucket to refill.
- The model stage takes longer on a busy day: with 4 names in flight, a spell that hits every ask adds up to
  about 1.5 minutes per busy name. On the worst day on record (3 Nov, 61 busy answers over about 20 names)
  that is roughly 25 minutes on a 43-minute stage: under the 90-minute stage budget
  (`FULL_MODEL_STAGE_BUDGET_SECONDS`) and under the 180-minute job cap, but close to the 75-minute line at
  which the daily check tells the owner. A whole provider outage still ends at the stage budget, as today.
- The budget itself does not change in this plan. If the owner wants the stage budget raised with the waits,
  that is its own line in the Amendments table.

## 4. Tests and record

- `tests/test_full_model.py` pins the ladder with a fake sleep: add the 429 ladder (15, 30, 60), keep the 5xx
  ladder (2, 4, 8), keep `Retry-After` winning within its cap, and keep the "gave up after N attempt(s)" count.
- The model-call lines in the log and the journal's `model_calls` record already carry each ask's status and
  attempt number, so the daily check can see the waits at work; nothing new to record.
- The Amendments row below is marked planned; when the change is merged the row gets its effective date (the
  first cycle after the merge), as the 2026-10-09 re-ask row did.

## 5. The Amendments row (planned)

| 2026-11-10 | **Model stage: longer waits between the retries of a "Model busy" answer** (planned; the owner's
"waits yes" of 2026-11-10; a model-stage setting, not a decision rule; takes effect when built) | A "Model busy"
(HTTP 429) answer from DeepInfra is a token-per-minute ceiling, and the retry ladder of 2, 4 and 8 seconds (14
in all over four asks) was shorter than a spell: 1, 0, 3, 2, 1, 3 and 4 names a day were lost to it on 26 Oct
to 3 Nov. The plan (`docs/research/model-busy-waits-plan.md`): a ladder of 15, 30 and 60 seconds for a 429 only
(`orchestrator/llm.py`), the 5xx family keeping 2, 4 and 8, `Retry-After` still winning within its cap; the four
asks, the 480-second limit, the re-asks, the concurrency and the 90-minute stage budget unchanged. No extra
calls. Built only after the owner says "build". |
