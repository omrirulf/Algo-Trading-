# The monthly coach: plan and private-data design

**Status: a plan for the owner to approve. Nothing here is built.** (The owner's instruction of 2 Oct 2026, item 3:
"plan first, don't build yet".)

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
  `usage.cost_usd` and the month's total before asking, and refuses a second call that would pass $0.10.

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
   Supabase scheduled Edge Function. Either way its logs are private. It reads the two tables with the secret
   key, computes the numbers in memory, sends the model percentages only, checks the answer (section 2), and
   writes the finished message to a third private table, `coach_messages`.
3. **What this public repository gives it**: only the experiment's status, read from the public
   `logs/race_gate.json` (next checkpoint date). Nothing flows the other way.
4. **What is never stored anywhere public**: amounts, balances, salary, contributions, and the finished message.

**A cheaper alternative (not recommended):** keep the job in this repository with a test that fails if the coach
module prints or logs anything, and run it in a step whose output is thrown away. It saves one repository, but
the protection is a rule people must keep, not a wall.

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

## 5. Until the owner enters numbers: the checklist

Sent by push (no personal data in it), once a month:

1. What was your take-home pay this month, and what did you spend? (Enter both in `coach_inputs`.)
2. What is each part of your savings worth today: world stocks, Israeli bonds, cash, anything else?
3. What target share do you want for each part, and how far from target before you rebalance?
4. How much have you put into your keren hishtalmut, kupat gemel lehashkaa and pension this year, and how much
   do you plan to put in?
5. Reminder: the experiment's next checkpoint is 22 Dec 2026. No decisions before it.

## 6. What the owner decides before it is built

1. Approve the design in section 3 (private repository or Supabase Edge Function), or choose the alternative.
2. The asset classes, the targets and the rebalancing band (they go in `coach_targets`, never in the repository).
3. Where to read the full message: the Supabase dashboard, or an email.
4. The day of the month it runs (proposed: the first working day, with the research backlog's monthly update).

## 7. What it will not do

No trading, no security named, no change to any rule of the experiment, no number of the owner's in a public
place, and no second model call in a month.
