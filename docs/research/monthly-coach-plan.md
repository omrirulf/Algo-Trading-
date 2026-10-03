# The monthly coach: plan and private-data design

**Status: approved by the owner on 3 Oct 2026, with conditions. Only the checklist is built** (`coach/checklist.py`,
`.github/workflows/coach.yml`). (The owner's instruction of 2 Oct 2026, item 3: "plan first, don't build yet".)

## 0. The owner's conditions (3 Oct 2026)

1. **Checklist only for the first two months** (November and December 2026), and after that until the owner
   confirms that they want to enter numbers. **Collect no personal numbers yet.** The checklist is fixed text made
   by code, so no model is asked and it costs nothing.
2. **Later, the owner's numbers go only into a private Supabase project, and the model sees percentages only.**
   Nothing personal goes on ntfy.sh, in the repository, in logs or in artifacts.
3. **The cost cap stays at $0.10 a month.**
4. **The data entry is not built until the owner confirms** that they want to enter numbers. Sections 1 to 4
   below describe that later stage; only section 5 (the checklist) runs now.

## 1. What it does

Once a month, one short message about the base of the investor pyramid -- the part that matters more than any
trading rule:

1. **Savings rate**: the share of take-home pay that was not spent this month, and its 12-month average.
2. **Allocation against the owner's targets**: each asset class's share of the total (for example world stocks,
   Israeli bonds, cash) next to its target share.
3. **Is rebalancing needed?** Yes only when a class is further from its target than the band the owner sets
   (the owner chooses the band; the coach never picks it).
4. **Contributions to tax-advantaged accounts**: what has gone in this year against the owner's plan for each
   account (keren hishtalmut, kupat gemel lehashkaa, pension), as a share of the plan.
5. **The experiment's status**: the next checkpoint date and the words "no decisions before it" (from
   `logs/race_gate.json`; already public, so it may be said plainly).

Until the owner has entered numbers, the message is a short checklist of questions instead (section 5).

## 2. Who computes what

- **Code computes every number.** Savings rate, shares, distance from target, "rebalance: yes/no",
  contribution progress: plain arithmetic in a small module with unit tests, like `analysis/israel_tax.py`.
- **The model only writes the text and asks questions.** It is given percentages only (rounded to whole
  percent), never an amount of money, a balance or a salary. It is told to write at most 120 words in simple
  English, to say what the numbers show, and to ask one or two questions.
- **It never recommends a specific security.** The prompt forbids it, and the code checks the answer before it is
  sent: an answer that names a ticker or fund (every name in `config/watchlist.py` and
  `config/shadow_universe.py`, any 2-5 capital-letter word not on a short allow-list, ISINs, and the words "buy"
  or "sell" next to a name) is thrown away and a fixed text made by code is sent instead.
- **Cost cap: $0.10 a month.** One call a month. With the production model (`openai/gpt-oss-120b` on
  DeepInfra, the provider already in use, so no new key and no new provider) at low reasoning, one call of
  about 1,500 tokens in and 400 out costs well under one cent. The code still checks the call's
  `usage.cost_usd` and the month's total: it makes at most one call a month, and refuses it if the month's total would pass $0.10.

## 3. Where the owner's numbers live (the private-data design)

The owner's personal numbers must never go into the public repository, a log, an artifact or the phone push
text. Today **the repository, its GitHub Actions logs, its workflow artifacts and the GitHub Pages site are all
public** (`docs/next-steps.mdx`, "decide whether to make the repository private"). So the coach cannot live in
this repository's workflows the way the other reports do: one stray `print`, or a traceback that shows a value,
would publish a salary in a public log for good.

**Proposed design (recommended):**

1. **Inputs: a private Supabase table**, `coach_inputs`, in **a new Supabase project of its own** (not the archive's
   project: that project's secret key is held by this public repository's workflows, and it bypasses row-level
   security, so one stray query or print in public code could reach the owner's numbers). The table follows the
   archive's pattern -- row-level security on and no policy, so the publishable key reads nothing -- and the new
   project's secret key lives only in the private job below, never in this repository. One row per month: month, take-home pay, spending, the value of each asset class,
   contributions per account, and (in a second table, `coach_targets`) the target shares, the rebalancing band and
   the yearly contribution plan. The owner types them in once a month in the Supabase dashboard's table editor
   (no form to build, nothing public).
2. **The job runs outside the public repository**: a small private GitHub repository (`coach-private`), or a
   Supabase scheduled Edge Function. Its logs hold nothing personal either: it logs no amount, share or
   message, only whether it ran. It reads the two tables with the secret key, computes the numbers in memory, sends the model percentages only, checks the answer (section 2), and
   writes the finished message to a third private table, `coach_messages`.
3. **What this public repository gives it**: only the experiment's status, read from the public
   `logs/race_gate.json` (next checkpoint date). Nothing flows the other way.
4. **What is never stored anywhere public**: amounts, balances, salary, contributions, and the finished message.

(A cheaper design that kept the job in this public repository was dropped: the owner's conditions of 3 Oct 2026
put nothing personal in the repository or in any log.)

## 4. Is the phone channel private? No.

Checked on 2 Oct 2026. The phone push goes through the public server `ntfy.sh`. The only protection is the topic
name, kept as the GitHub secret `NTFY_TOPIC` (`docs/phone.mdx`: "Anyone who knows the name can read or send, so
treat it like a password"). There is no access token, no reserved topic and no end-to-end encryption, and the
server's operator can see the messages, which it keeps for a while. So **nothing personal is sent by push**.

The push says only what is already public or contains no number of the owner's:

> 🗓️ Monthly check-in ready. Next checkpoint 22 Dec: no decisions before it. Two questions are waiting for you.

The full message, with the percentages, is read in the private place: the `coach_messages` table in the Supabase
dashboard (or, if the owner prefers, an email to the owner's own address from the private job). If the owner
later wants the percentages on the phone, the options are an ntfy topic with access control (a paid ntfy.sh plan
or a self-hosted server) or a private messenger bot; both would need the owner's decision first.

## 5. Now: the checklist (built, runs from November 2026)

Sent by push on the first working day of each month (`coach/checklist.py`, `.github/workflows/coach.yml`). It
asks the owner to think; it asks nobody to send a number, and nothing is collected:

1. Did you save part of your take-home pay last month? Think of the share, not the amount.
2. Your savings by part (world stocks, Israeli bonds, cash, anything else): is any part far from where you want
   it?
3. Have you chosen a target share for each part, and how far from it you let a part drift before you rebalance?
4. Keren hishtalmut, kupat gemel lehashkaa and pension: are this year's deposits on plan?

Then: "Keep your answers to yourself: send no number anywhere. Nothing is collected yet." and the experiment's
next checkpoint date from the public `logs/race_gate.json` ("No decisions before it."). The second month's push
also says that the two checklist-only months are over and asks the owner to tell Claude when they want to start
entering numbers; until then the checklist goes on. No model is asked, so it costs nothing.

## 6. What the owner decides before the data entry is built

Decided on 3 Oct 2026: the plan is approved with the conditions in section 0; the private place is a private
Supabase project; the model sees percentages only; the cap is $0.10 a month; the checklist runs on the first
working day of each month. Still open, for when the owner confirms that they want to enter numbers:

1. Where the private job runs: a small private repository, or a Supabase scheduled Edge Function (section 3).
2. The asset classes, the targets and the rebalancing band (they go in `coach_targets`, never in the repository).
3. Where to read the full message: the Supabase dashboard, or an email.

## 7. What it will not do

No trading, no security named, no change to any rule of the experiment, no number of the owner's in a public
place, and no second model call in a month.
