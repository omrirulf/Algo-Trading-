# The investor simulator: plan and private-data design

**Status: plan only, for the owner's approval (4 Oct 2026). Nothing is built.** The owner's instruction of
4 Oct 2026: "Investor simulator: plan first, don't build yet. … Show me the plan and the private-data design
before you build."

- **A tool, not a test.** It uses no experiment slot, gets no card and no graveyard row, and N stays at 41.
- **Shadow-only.** It never trades, holds no broker key and sends no order. It only suggests; the owner decides
  and trades by hand.
- **The owner's personal numbers** (lots, holdings, income, savings, targets) **never go into this public
  repository, a log, an artifact or a phone push.** Section 2 says how.
- **Built and tested with sample data only** (made-up numbers, in this repository), after the owner approves. The
  owner's real numbers stay in the private place of section 2.
- **The coach is not touched.** It stays a checklist; its data entry is still not built.

## 0. In short

**What it does.** Once a month, it reads the owner's lots and plan in a private place, prices them at the last close
and the Bank of Israel's rate, and writes one private report: the value if sold today, the tax paid so far,
rebalancing suggestions (the shekel tax cost first), harvest suggestions, the annual report pack, and the owner's
money against buy-and-hold VT and VWRA, after tax, in shekels.

**Where (recommended).** The lots are CSV files in **a private GitHub repository of the owner's own**. That
repository's own GitHub Actions job runs this repository's tested engine at a pinned commit, with no key and no
secret, and writes the report as a page in the same private repository. Nothing flows back here.

**What the owner decides.** The table below. Every row has a recommendation; "all as recommended" is a complete
answer, with only the rows the owner wants different named.

| # | Decision | Recommended | Other options |
| --- | --- | --- | --- |
| | **Where** | | |
| D1 | Where the lots live and where the job runs | **A private GitHub repository** (2.3) | A private Supabase project (2.4); the owner's computer only (2.5) |
| D2 | Where the owner reads the report | **A page in that private repository** (github.com or the GitHub app, signed in) | A private Supabase table; an email to the owner |
| D3 | One home for all personal numbers? | **Yes: the coach's later data entry also goes to the private repository.** This changes the coach plan's "private Supabase project", so only if the owner agrees | Two places: lots in the private repository, the coach's numbers in Supabase |
| | **Rebalancing** (section 5) | | |
| D4 | New contributions | **Every month: first to classes below their band, then to the other classes below target, the largest gap first, each up to its target; each account buys only what it holds** | All of it to the class furthest below target |
| D5 | A target of 4% or less, where "band edge minus 1 point" passes the target | **Trade to the target itself** | Leave such classes out of the bands |
| D6 | A sale's tax cost | **This year's extra tax plus 25% of the loss carried forward that the sale uses up** | This year's extra tax only |
| D7 | "Drift above 10 points" | **Absolute points, measured when the taxable sale is considered (after contributions and tax-free moves), for the class most out of band among those the sale helps** | Measured at the start of the run; the sold class's own drift |
| D8 | Several classes out at once | **Out-of-band classes go to their "trade to" point; any money still needed comes from classes above target, the cheapest tax first; money never leaves its account** | Equal shares from every class above target |
| D9 | Which accounts are "tax-free" | **Keren hishtalmut and kupat gemel lehashkaa (no tax on a switch of track); pension left out; shown before any withdrawal tax** | Pension in too; model the gemel's lump-sum withdrawal tax (needs the CPI) |
| | **Harvesting** (section 6) | | |
| D10 | "A lot" under FIFO | **Every lot up to and including the loss lot, net (FIFO sells the earlier ones first); "lot value" = the value of everything sold** | The loss lot's own value |
| D11 | "A net gain this year" | **This year's taxable gain after the loss carried in from earlier years is above 0** | This year's gains less losses, before the loss carried in |
| D12 | "A domicile switch" | **A swap from a US-listed fund to an Irish one; it counts now, as the rule says** | It counts only after the fund-domicile decision (June 2027) |
| D13 | "Tax value (25% × the loss)" | **The test uses 25% × the loss, as written; the report also shows what it is worth this year, what goes against dividends (worth 0) and what is carried forward** | The test leaves out the part that goes against dividends |
| D14 | Several harvests in one run | **Taken one after another, the largest first; "net gain this year" checked again after each** | Each tested on its own |
| D15 | Before the accountant answers question 6 (section 86) | **Show the suggestions, each with "do not act before question 6 is answered"** | Show none until it is answered |
| D16 | Trading cost estimate | **Interactive Brokers' published prices (6.4) until the broker is chosen** | The owner's own broker's prices |
| D17 | Similar but not identical funds | **The table in 6.5** | The owner's own list |
| | **Other** | | |
| D18 | When it runs | **The first working day of each month (Sunday to Thursday, with the coach), and when a file changes** | Only by hand |
| D19 | Three new accountant questions (section 9) | **Add them to `cpa-questions.md` now** | Wait |

## 1. What it does

1. **Value if sold today**: what the money is worth after Israeli tax if every taxable lot were sold at the close,
   in shekels (and dollars), per account and in total.
2. **Tax paid so far**: the tax on everything sold or received so far (finished years, and this year as if it
   ended today), computed. If the owner enters the payments actually made, they are shown beside it.
3. **Rebalancing**: each asset class against its target and band. A suggestion only when a band is broken, and
   **the shekel tax cost before every suggestion**.
4. **Harvest suggestions**: taxable lots whose loss is worth taking, each with a similar but not identical fund.
5. **The annual report pack**: half-year figures, the rows for forms 1325 and 1322, and the loss carried forward.
6. **Against buy-and-hold VT and VWRA**: the same shekels, on the same days, in VT or in VWRA and held; after tax,
   "if sold today", in shekels.

It never sends an order. Every suggestion ends with "Suggestion only: you decide and trade yourself."

## 2. Where it runs and where the lots live: the private-data design

### 2.1 What is private and what is public

| Private: only in the owner's private place | Public: may be in this repository |
| --- | --- |
| Lots and transactions, account names, balances, cash | The tax rules and the owner's rule numbers (bands, 0.5%, 2,000 ILS, 5%, 5×): they are not personal |
| Targets, contributions, salary, savings, the loss carried in from the last assessment | The engine: pure code that reads only the folder it is given |
| "Do I expect gains within 3 years?" | A fund table (ticker, index, domicile, accumulating or not): public facts |
| The finished report, and any payment records | Sample data: made-up numbers, marked SAMPLE in every file |
| | Prices and Bank of Israel rates (public data) |

This repository, its Actions logs, its artifacts and its GitHub Pages site are public today (`docs/next-steps.mdx`).
So, as with the coach (`monthly-coach-plan.md`, section 3), **the job cannot run in this repository's workflows**:
one stray `print` or traceback would publish a number for good.

### 2.2 The options

| | **A. Private GitHub repository** (recommended) | B. Private Supabase project | C. The owner's computer only |
| --- | --- | --- | --- |
| Where the lots live | CSV files in the private repository | Tables in a private Supabase project | Files on the computer |
| Where the job runs | That repository's own GitHub Actions | A private repository's Actions, holding the project's secret key | `python -m investor.report` by hand |
| Where the owner reads it | A Markdown page in the private repository | The Supabase dashboard, or an email | A file on the computer |
| Keys needed | **None**: it reads its own files and the public engine | The project's secret key, which bypasses row-level security | None |
| History of every change | Yes: every edit is a commit, which the accountant can trace | No: and no automatic backups on the free plan | Only what the owner keeps |
| Entering lots | Edit or upload a CSV on github.com (a broker's export can be pasted in) | The table editor, or its CSV import | Any editor |
| Runs by itself | Yes | Yes, but a free project is **paused after 7 days with little activity**, so a monthly job finds it asleep unless something wakes it daily | No |
| Limits | 2,000 free Actions minutes a month for private repositories; this job needs a few | **Two free projects per person**: the archive is one, and the coach's plan already takes the second, so the lots would share the coach's project | None |
| Cost | Free | Free, or $25 a month to avoid the pause | Free |

(The facts in this table are from the research of 4 Oct 2026, section 12.)

### 2.3 Recommended: A, a private GitHub repository

The owner creates it (for example `investor-private`, private from the first commit; two-factor login on the GitHub
account). It holds only:

```
data/accounts.csv        one row per account: name, kind (taxable / tax_free), currency
data/transactions.csv    one row per event (section 3)
data/tax_free.csv        the tax-free accounts' value per track, by date
data/plan.csv            targets, the fund-to-class map, the month's contributions, the owner's inputs
data/payments.csv        optional: tax actually paid (half-year advances, the annual balance)
reports/latest.md        the report (written by the job)
reports/YYYY-MM-DD.md    each run's report, kept
.github/workflows/report.yml
```

Every data file starts with the line `# PRIVATE`, and the engine refuses a file without it (or without the
`# SAMPLE` line of the sample files).

The workflow is about 30 lines. It is given to the owner as text to paste, and it is the only code in the private
repository:

1. Runs on the first working day of each month and on every push that changes `data/`.
2. **Refuses to run if the repository is not private** (`if: github.event.repository.private`), so a mistake in
   the settings cannot publish anything.
3. Checks out the private repository, then **this public repository at one pinned commit** (a 40-character SHA,
   never a branch name). No later change here reaches the owner's data until the owner moves the pin on purpose.
   No token is needed while this repository is public.
4. Runs the engine: `python -m investor.report --data data --out reports`. It fetches public prices and the Bank of
   Israel's rates itself.
5. Commits the report to `reports/`. **No artifact, no upload, no phone push, no secret.** Its log says only "report
   written" and how many lines. The engine prints no amount, share, ticker or account name, and an error prints only
   its kind, never its values.
6. The private repository's log and artifact retention is set to the minimum (1 day).

```
this public repository (engine, sample data, tests)          the owner's private repository
            │                                                  data/*.csv  (the owner's lots)
            │  checked out at a pinned commit, read-only               │
            └────────────────────────────►  report.yml (private Actions, no secret)
                                                  │  public prices, Bank of Israel rates
                                                  ▼
                                      reports/latest.md  ── read by the owner, signed in
nothing flows back to the public repository, a log, an artifact or the phone
```

**Why A:** no key exists that could leak; every change to a lot is a commit the accountant can trace; the engine is
the same tested code as here; no pause, no project limit; and it costs nothing. The report uses text and tables
only, so it reads well in the GitHub app on a phone.

**What A does not protect against:** anyone with access to the owner's GitHub account, and GitHub itself, can read
the private repository, and so can any app or session the owner gives access to it. A Claude session is one: **this
plan never needs the private repository in a Claude session.** The engine is built and tested here with sample data
only, and the owner moves the pin. Git history keeps every old version of a file, so a file committed by mistake
stays in the history unless it is rewritten.

**A note for the before-real-money checklist ("make the repository private"):** a GitHub Pages site from a private
repository is still public on the Pro plan, and on the Free plan making this repository private would take its Pages
site (the dashboard) offline. Its own Actions use would then count against the same 2,000 free minutes a month (an
estimate from the research, not a billed figure: about 4,000 minutes of runs in the last 30 days). Worth knowing
before that decision.

### 2.4 Option B, a private Supabase project

Tables `accounts`, `transactions`, `tax_free`, `plan` and `reports` in the coach's future private project (a third
free project is not possible), in an organization separate from the archive's, with row-level security on, no
policy, and every right taken from the public roles. A new-style secret key made for this job only, held as a secret
in a private repository. It keeps one home for every personal number, as the coach plan says, but it needs a secret
key, it keeps no history of edits and no backups on the free plan, and the 7-day pause needs a daily keep-alive job
or a paid plan. A Supabase Edge Function cannot run the engine (it runs TypeScript, not Python), so the job would
still be in a private repository.

### 2.5 Option C, the owner's computer only

The most private: nothing online. But nothing runs by itself; the owner installs Python and runs it each month. A
fallback if the owner wants the data on no server at all.

### 2.6 Guardrails in this public repository (built with the engine)

- **No personal file can be committed here.** A CI step fails if a file named like the private ones
  (`transactions*`, `accounts*`, `tax_free*`, `plan*.csv`, `payments*`, `lots*`, `holdings*`) is anywhere but the
  sample folder `tests/data/investor_sample/`, or if any file carries the `# PRIVATE` line. (`.gitignore` is a second
  net only: `git add -f`, which this repository's workflows use, ignores it.)
- **The engine reads only the folder it is given**: `--data` has no default, and there is no environment variable or
  `.env` lookup. It writes only to `--out`, and refuses a folder inside this repository (so nothing can land in
  `logs/`, `dashboard/` or `docs/`, which are published).
- **It prints nothing personal.** A test runs it on sample files full of distinctive made-up amounts and tickers, and
  checks that none of them appears in its output, its log lines or its error messages. The price fetch's own log
  lines name tickers, so they are switched off in the engine.
- **It cannot trade, ask a model or push.** It imports no broker, model or phone code (the same kind of CI step as
  "The shadow funds cannot trade"); its only network use is the price and rate fetch.
- **No workflow in this repository runs it on real data**, and none holds a secret for it. CI runs its tests on the
  sample data only.
- **The salary stays an input.** The existing test that `SALARY_ILS` is 0 is kept, and a check refuses a non-zero
  salary written into code.

## 3. The owner's files (the data model)

`transactions.csv`, one row per event, in the order they happened:

| Column | Example (sample) | Notes |
| --- | --- | --- |
| `date` | 2026-03-02 | The trade date (accountant question 4 asks whether it should be the settlement date) |
| `account` | Broker-1 | One of `accounts.csv` |
| `kind` | `buy`, `sell`, `dividend`, `deposit`, `withdrawal`, `fee`, `transfer_in` | |
| `ticker` | VT | Empty for a deposit |
| `quantity` | 10 | Shares |
| `price_usd` | 100.00 | Per share |
| `fee_usd` | 1.00 | Into the cost of a buy, off the proceeds of a sale |
| `amount`, `currency` | 37000, ILS | A deposit, a withdrawal, a dividend (gross) or a fee |
| `withheld_usd` | 12.50 | The US tax the broker actually withheld from a dividend (else 25% is assumed) |
| `fx` | (empty) | Empty: the Bank of Israel's rate on `date`. Filled only to override, and the report then says so |
| `note` | | Free text, never printed |

- A dividend that is reinvested is a `dividend` row plus a `buy` row: a new lot (rule c).
- A `transfer_in` keeps the lot's own purchase date, price and rate.
- **Checks before anything is computed:** a sale larger than the account holds is refused (the tax engine would
  otherwise open a short, which for the owner can only be a typing error); a line not in dollars is refused; a lot
  with no price is listed. An error names the row number only, never an amount.
- **A day with no Bank of Israel rate** (a weekend deposit, a holiday) uses the last rate the Bank published before
  it, and the day is counted and listed, like the existing fallback days.
- `plan.csv`: the target for each class; the class of each fund and of each tax-free track (by its published mix);
  the month's contributions per account; the loss carried in from the owner's last assessment; and two dated yes/no
  inputs, `expect_gains_within_3_years` (counted as "no" when more than 12 months old) and `w8ben_filed`.

## 4. Tax, scope (a): what is reused and what is added

### 4.1 Reused as it is

| Need | Already in the repository |
| --- | --- |
| The rules' numbers | `config/israel_tax.py` (25%, the surtax as parameters, FIFO, the dividend switch, the rate source) |
| FX as the index, one lot | `analysis.israel_tax.lot_gain` (T1 to T6) |
| A year's netting, the loss carried forward, losses against dividends | `analysis.israel_tax.year_tax` (T7) |
| Dividends with the US credit | `analysis.israel_tax.dividend_tax` (T10) |
| The surtax | `analysis.israel_tax.surtax` (T8): still off by default; the salary only an input |
| FIFO lots per account | `analysis.israel_tax.TaxBook` (T9) |
| The Bank of Israel's rate on a day | `analysis.boi_rates` (with the European Central Bank's rates for a missing day, each one counted) |
| Prices with dividends | `history.prices` (a check at build time that it reads VWRA in dollars) |
| Dividends reinvested as new lots | the pattern of `analysis.tax_breakeven.held` |
| The report's words ("tax paid so far", "if sold today", "from the $/₪ move") | `shadow/after_tax.py` (copied, not imported: it pulls in the trading engine) |

T1 to T10 stay exactly as they are, and so does every number in `config/israel_tax.py`. T5 still needs the
accountant's confirmation (question 1), and the report says so next to every number it touches.

### 4.2 Added (small, each with tests on sample data)

1. **Each closed lot keeps its purchase day, both rates and its dollar amounts.** Today the record of a closed lot
   keeps only the sale day; the form rows need the rest. Fields added at the end, so no number of T1 to T10 moves.
2. **One person's year across accounts.** Israel nets a person's year, not an account's: every taxable account's
   gains and losses go into one `year_tax`, the loss carried forward chained from year to year, starting from the
   owner's last assessment. FIFO stays per account (rule c; accountant question 3 may change it).
3. **Half-years.** A pure function that reckons any dates (January to June, July to December). The existing
   `TaxBook.state` is not used for it: it counts the whole year whatever the day, and it changes the book's record
   of the year's last rate.
4. **The tax cost of a possible sale** (5.2), on copies, for the whole person.
5. **The allowable loss of open lots today**, lot by lot in FIFO order, and of every FIFO group of lots (6.2).
6. **Dividends paid net.** `TaxBook.state` adds the US tax withheld because the experiment's funds credit dividends
   gross (convention 3 of section 5c). A real broker pays them net, so the simulator takes off Israel's tax only and
   shows the US tax on its own line: never taken off twice (test T35).
7. **The US tax actually withheld** can be entered per dividend (`withheld_usd`); today the engine always assumes
   25%, which would be wrong for an Irish distributing fund.
8. **A public fund table**: ticker, fund ID, index, domicile, accumulating or distributing, quote currency. An
   accumulating fund (VWRA) has no dividend rows; the report states that it assumes no Israeli tax until the sale
   (accountant question 5).

## 5. Rebalancing, scope (b)

### 5.1 The owner's rule

Bands of ±5 points absolute (25% relative for targets under 20%). Order: new contributions first, then tax-free
accounts, then taxable sales last. Trade back to the band edge minus 1 point. Taxable sales only if the estimated tax
cost is under 0.5% of the amount traded, unless the drift is above 10 points. Always show the shekel tax cost before
any suggestion.

### 5.2 How the code reads it

- **Weights** are of every account in the plan, taxable and tax-free, at market value before tax, in shekels at the
  day's rate. The after-tax value is shown beside it, not used.
- **Band** = the smaller of 5 points and 25% of the target: ±5 for a target of 20% or more, ±2.5 for 10%. At 20%
  both give 5. **Out of band** = further from the target than the band; on the edge is inside. Every test runs on
  unrounded numbers, with a tiny tolerance, so a weight of 65.00000000000001 with a target of 60 is inside.
- **Trade to** = 1 point inside the band, towards the target: target + band − 1 for a class above, target − band + 1
  for a class below. **(D5)** With a band of 1 point or less (a target of 4% or less), the target itself.
- **Drift (D7)** = the distance from the target in points of the whole portfolio (absolute). For the 10-point
  override it is measured at the taxable step, after contributions and tax-free moves, for the class most out of band
  among those the sale moves towards target (the class sold and the classes its money buys). The override waives
  only the 0.5% test; the order and the tax cost display stay.
- **The tax cost of a taxable sale (D6)** = Israel's extra tax this year because of the sale, plus 25% of the loss
  carried forward that the sale uses up (a loss carried forward is worth 25% of itself against later gains, so using
  it now is a cost). It is reckoned with `year_tax` for the whole person: this year's sales so far, the lines already
  suggested in this run, the dividends and the loss carried in, at the last close and the day's rate, FIFO lots.
  When the loss would otherwise be set against dividends already covered by the US credit, using it is free, and the
  cost is 0 (test T18). A negative cost is a saving.
- **0.5%** = the tax cost in shekels against the sale's gross proceeds in shekels, per sale line, strictly under.
  The commission and spread are shown beside it, not in it.
- **Shares** are whole shares: the count that brings the class nearest to its "trade to" point (fewer shares on a
  tie). If no whole count can put a class inside its band (one share is wider than the band), nothing is suggested
  and the report says from what total it will fit.
- **The money stays in its account**: a sale's money buys, in the same account, the classes below target, the largest
  gap first; whatever is left stays as cash and counts as next month's contribution.

### 5.3 The steps, every run

1. **Price and weigh** everything; refuse to run if the targets do not add up to 100 or a fund has no class. Show
   the table of classes, targets, weights, bands and drifts, even when nothing is out of band.
2. **Contributions (D4), tax cost 0.** Each account's new money (and its spare cash) goes first to classes below
   their band (to their "trade to" point, then on towards target), then to the other classes below target, the
   largest shekel gap first, never above target. A broker buys whole shares; a tax-free account takes exact shekels.
3. **The plan (D8).** Each out-of-band class goes to its "trade to" point. Money still needed comes from classes above
   target (never below their target), tax-free holdings first, then taxable ones in order of the lowest tax per
   shekel; money left over goes to classes below target, the largest gap first.
4. **Tax-free accounts, tax cost 0.** Inside the keren hishtalmut or the kupat gemel lehashkaa, money is moved from a
   track of the class to sell to a track of the class to buy. A change of track can take a few days: the owner marks
   it "pending" in `plan.csv`, and the next run counts it as done.
5. **Taxable sales, last.** For each class still out of band, the (account, fund) whose FIFO sale costs the least tax
   per shekel goes first. A line is suggested if its tax cost is under 0.5%, or the drift (D7) is above 10 points.
   Otherwise: "not suggested", with the same tax cost and the reason, and how many months of contributions would
   close the gap. Beside each line: what other funds would have cost, and "with specific lots it would be X, not
   allowed while FIFO applies (question 3)" when that is lower.
6. **A target the owner has just changed** that pushes a drift above 10 points makes the report ask for a
   confirmation before the override applies.
7. **Every line starts with its tax cost**: "Tax cost: 0 ILS." included. And ends with "Suggestion only: you decide
   and trade yourself."

## 6. Harvest suggestions, scope (c)

### 6.1 The owner's rule

Flag a lot if its allowable ILS loss is at least the larger of 2,000 ILS and 5% of the lot value, and the tax value
(25% × the loss) is at least 5 times the estimated trading cost, and there is a net gain this year or the owner
expects gains within 3 years or the swap is a domicile switch. Suggest a similar but not identical fund. Never trade
automatically.

Read as: **A** (the loss test) **and B** (the cost test) **and C** (a net gain this year, **or** gains expected
within 3 years, **or** a domicile switch). The report prints this reading and each test's result.

### 6.2 How the code reads it

- **Allowable ILS loss** = rule a with `lot_gain`, at the last close and the Bank of Israel rate of that close's day.
  A loss made only by the exchange rate gives 0 (T5). While T5 is not confirmed, such a line says "not allowable
  under T5 (accountant question 1 open); it would be flagged / not flagged if T5 is rejected".
- **FIFO (D10):** a later lot cannot be sold before the earlier lots of the same fund in the same account. So each
  test is for a FIFO group: every lot up to and including the loss lot, their gains and losses together. Every group
  is tried; the one with the largest net loss that passes is shown, lot by lot. A later lot's loss is never shown as
  if it could be sold alone. **Lot value** = the shekel value of everything that would be sold.
- **Tax value (D13)** = 25% × the net loss, for test B, as the rule says. Beside it, what the loss is really worth,
  from `year_tax` with and without the sale: **this year** (against this year's taxable gain), **against dividends**
  (while `OFFSET_LOSSES_VS_DIVIDENDS` is on: worth 0, because the US credit already covered that tax, and US credit
  is lost), and **carried forward** (worth up to 25% of itself, against later gains).
- **Trading cost** = both sides: selling the group and buying the other fund with the money, each side commission
  plus half the spread (6.4), in shekels at the same rate. No currency conversion when both funds trade in dollars.
- **Net gain this year (D11)** = this year's taxable gain of all the owner's taxable accounts so far, after the loss
  carried in, before this harvest. The literal "gains less losses" is shown too.
- **Expects gains within 3 years** = the owner's dated yes/no in `plan.csv`.
- **Domicile switch (D12)** = the sold fund is US-listed and the suggested one is Irish.
- **Several harvests (D14)** are taken one after another, the largest first, and C is checked again after each.
- **Warnings on every suggestion:** section 86 (accountant question 6: "do not act before it is answered", D15);
  the dividend switch (question 2) when part of the loss goes against dividends; T5 when it applies; any purchase of
  the sold fund in any account (a dividend reinvestment included) within 30 days around the sale, a placeholder since
  Israel has no wash-sale rule; an ex-dividend day of a distributing substitute within 5 sessions; "check again on
  the day you trade".
- **In the same run**, contributions and rebalancing buy the suggested fund, never the one sold.

### 6.3 The steps

For each taxable account and fund, for each FIFO group of open lots: the net allowable loss, its value, the tax value,
the trading cost and the gain condition. Flag the best group that passes A, B and C; suggest the first fund of 6.5
that is on another index and has a price. Nothing is sold: the line says "Suggestion only".

### 6.4 Trading cost parameters (D16)

Public parameters until the owner's broker is known (the broker decision waits for June 2027). Per side: commission
plus half the bid-ask spread; plus the currency conversion when shekels must become dollars. The report prints the
numbers it used. Starting values, from Interactive Brokers' published prices for a retail client in Israel (IBKR Pro:
IBKR Lite and fractional shares are not offered to Israeli residents, so whole shares only):

| | Commission per side | Half the spread |
| --- | --- | --- |
| A US-listed fund (VT, ACWI) | $0.005 a share, at least $1.00, at most 1% of the trade | 0.01% |
| An Irish fund in dollars on the LSE (VWRA, ISAC) | $4.00 up to $8,000, then 0.05% of the trade | 0.05% (a cautious figure) |
| Shekels to dollars | 0.002% of the amount, at least $2.00 | — |

These were read from search summaries (the broker's pages could not be opened from here) and are checked again on the
broker's own page when the engine is built.

### 6.5 Similar but not identical funds (D17)

Never the same index and never the same fund: each fund in the table carries its index and fund ID, and the code
refuses a pair that shares either (for example VWRA and VWRL are one fund; ACWI and ISAC both follow MSCI ACWI).

| Sold | Suggested | Similar because | Not identical because |
| --- | --- | --- | --- |
| VT (US-listed, FTSE Global All Cap) | VWRA (Irish, FTSE All-World, accumulating) | World stocks | No small companies; a **domicile switch** |
| VT | SPYI (Irish, MSCI ACWI IMI, accumulating) | World stocks with small companies | Another provider and index; a **domicile switch** |
| VT | ACWI (US-listed, MSCI ACWI) | World stocks | Another provider and index; no domicile switch |
| VWRA | ISAC (Irish, MSCI ACWI, accumulating, in dollars on the LSE) | World stocks, the same domicile | Another provider and index |
| ACWI | VT | World stocks | Another provider and index |
| VTI (US total market, CRSP) | ITOT (S&P Total Market) or SCHB (Dow Jones Broad Market) | US stocks | Three different indexes |
| VXUS (FTSE Global All Cap ex US) | IXUS (MSCI ACWI ex USA IMI) | Stocks outside the US | Another provider and index |

The report also shows, as a note and not a rule, the owner's US-listed holdings against the $60,000 line above which
the US estate tax applies to a non-US person (Israel has no estate-tax treaty with the US); a domicile switch lowers
that amount. Prices: VWRA and ISAC are quoted in dollars on the LSE; the lines quoted in pence (SSAC, VWRL) are not
used, so no unit can be mixed up. VWRA's prices start on 23 July 2019.

## 7. The report, scope (d)

The report is one Markdown page with text and tables only. Its sections:

1. **Summary**: the total value; the value if sold today (shekels and dollars); the tax paid so far; the close and
   the rate used, with their dates, and every day whose rate did not come from the Bank of Israel.
2. **Allocation and rebalancing** (section 5), the tax cost first on every line.
3. **Harvest** (section 6), or "nothing to flag".
4. **Against VT and VWRA** (7.4).
5. **The annual report pack** (7.2 and 7.3), this year so far and each finished year.
6. **What is assumed**: T5 (question 1), the dividend switch (question 2), FIFO per account (question 3), the
   trade-date rate (question 4), VWRA taxed only at sale (question 5), section 86 (question 6), the half-year netting
   (question 7).

### 7.1 Value if sold today, and tax paid so far

- **Value if sold today** = the market value in shekels (positions at the close × the rate, plus cash) − this year's
  Israeli tax if every taxable lot were sold today, for the whole person − any tax of finished years still unpaid (if
  the owner records payments). No selling cost (as the after-tax gate assumes); the cost of selling is shown beside
  it. Dividends arrived net, so the US tax is not taken off again (T35).
- **Tax paid so far** = Israel's tax for each finished year + this year's on what has been sold and received so far +
  the US tax withheld, at each dividend's own day's rate. It is what is due on what has happened, computed. If the
  owner enters `payments.csv`, the payments are shown beside it.
- The tax-free accounts are shown at their value, labelled "before any withdrawal tax" (D9).

### 7.2 Half-year figures

For January to June and July to December: the proceeds, the gains, the losses, the net, and the advance payment.
The advance for the first half is due by 31 July and for the second by 31 January (section 91 of the Income Tax
Ordinance, as the research found it). Whether the half's own losses, and the loss carried in, reduce the advance is
accountant question 7 and the new question 15, so until they are answered the pack shows three figures for each half:
on the gains alone, on the half's own net, and on the year's net so far less what the first half paid. The year's
reconciliation follows (for example: 1,000 paid for the first half, 750 due for the year, 250 back through the annual
return, T32).

### 7.3 Form rows and the loss carried forward

- **Form 1325** (appendix C1 of the annual return 1301) lists every sale of traded securities with no tax withheld at
  source, which is every sale at a foreign broker. **One row per closed lot or part of one**, in FIFO order: the fund
  and its ID, the quantity, the purchase day, the cost in shekels at the purchase day's rate, the rate ratio (the
  index for a dollar security), the adjusted cost, the sale day, the proceeds in shekels, and the real gain or loss.
  The dollar amounts, the nominal gain and the inflationary amount are kept beside them.
- **Form 1322** (appendix C) is the year's summary, filled from the 1325 rows: the total proceeds, the gains, the
  losses, the loss set against dividends (with the figure the other way, for question 2), the loss carried in and
  the part used, the taxable gain, the tax, and the loss carried out.
- **Dividends**: one row each, gross in shekels, the US tax in shekels at its own day's rate, Israel's tax, the
  credit, the extra and any credit lost: the figures the foreign-income appendix (form 1324, question 9) asks for.
- The exact fields of each form are copied from the Tax Authority's current forms when the engine is built (the forms
  could not be opened from here), and the mapping goes to the accountant (new question 13) before the owner files
  anything from it. How a fall of the dollar shows in the 1325 columns (the rule's adjusted cost is never below the
  cost for a gain, T1) is part of that question.

### 7.4 Against buy-and-hold VT and VWRA

- **The same shekels on the same days.** Every shekel deposit into a taxable account (a dollar deposit at its day's
  rate) buys VT, and separately VWRA, at that day's close, in whole shares, after the same trading cost; money left
  over waits for the next deposit. A withdrawal sells the same amount, FIFO. Lots held before the records start, and
  lots transferred in, count as deposits of their cost on their own purchase days. A transfer between the owner's own
  accounts is not a deposit.
- **VT**: each dividend, less the 25% US tax withheld, buys whole shares on its day: a new lot. Israel's extra tax is
  usually 0 (T10).
- **VWRA**: accumulating, so no dividend rows; no Israeli tax until it is sold (accountant question 5). Money that went
  in before 23 July 2019 is shown as "n/a" for VWRA.
- **Each of the three books is its own person-year**: its own netting, loss carried forward and tax. Shown in
  shekels, after tax "if sold today": the value, the money-weighted return a year (the experiment's daily-return
  code is not used: it reads a deposit as a gain), and the difference from the owner's own taxable accounts. The
  tax-free accounts are the same in all three, so they are left out.

## 8. Tests, on sample data only

Numbered after the owner's T1 to T10, in a new `tests/test_investor.py` next to `tests/test_israel_tax.py`, in the
same style. Fees 0 and tax 25% unless a case says otherwise. **Every number below was worked with the repository's
own `lot_gain` and `year_tax` and checked twice.** The owner may change any case before it is written as a test. "B"
is a made-up bond fund at $50 (180 ILS at 3.60); "KH" is a keren hishtalmut.

### Rebalancing

| Test | Case | Expected |
| --- | --- | --- |
| T11 | Bands and "trade to" points for targets 60, 20, 10 and 3 | Bands ±5, ±5, ±2.5, ±0.75. Trade to 64 / 56, 24 / 16, 11.5 / 8.5, and 3 / 3 (D5). A weight of 65 with a target of 60 is inside, also when the arithmetic gives 65.00000000000001. |
| T12 | Contributions first. A KH with stocks 70,000 and bonds 30,000 ILS; targets 60 / 40 (both out of band); a deposit of 20,000 ILS | Bonds +18,000, stocks +2,000: 60% / 40%; no sale; "Tax cost: 0 ILS" |
| T13 | Tax-free accounts second. A broker account with VT worth 100,000; a KH with stocks 50,000 and bonds 50,000; targets 60 / 40 (stocks 75%) | In the KH, move 22,000 from stocks to bonds (stocks to 64%); "Tax cost: 0 ILS"; no taxable sale |
| T14 | A taxable sale under 0.5%. Broker: 100 VT, one lot at $100 at 3.70, and 103 B; today VT $104 at 3.60 (37,440 ILS), B 18,540 ILS; targets 60 / 40 (stocks 66.88%) | Sell 4 VT (to 64.21%; 5 would give 63.54%): 1,497.60 ILS, nominal +17.60, inflationary amount −40, taxable 17.60, **tax cost 4.40 ILS (0.29%)**: suggested. The money buys 8 B; 57.60 ILS stays as cash |
| T15 | Over 0.5%, drift 10 or less. Broker: 100 VT, one lot at $60 at 3.40, and 100 B; today VT $100 at 3.60 (36,000), B 18,000 (stocks 66.67%) | 4 VT (1,440 ILS) would cost **144 ILS (10.0%)**: not suggested, with the cost and the reason |
| T16 | The same VT lot, drift over 10. 67 B (12,060 ILS): stocks 74.91% | Sell 15 VT (to 63.67%; 14 would give 64.42%): 5,400 ILS, **tax cost 540 ILS (10.0%)**: suggested because the drift is over 10 |
| T17 | FIFO decides the cost. Lot 1: 10 VT at $60 at 3.40; lot 2: 10 VT at $110 at 3.70; today $100 at 3.60; sell 10 | Lot 1 is sold: taxable 1,440, tax 360. Shown beside: "with specific lots (lot 2) it would be a loss of 360; not allowed while FIFO applies (question 3)" |
| T18 | The loss carried forward is a cost (D6). T15's 4 shares, after a realised loss of −1,000 earlier this year | No dividends: no extra tax this year, but 576 of the loss is used up: **cost 144 ILS**, not suggested. With 1,000 ILS of dividends (250 of US tax) and the switch on, the loss would be set against them anyway: **cost 0 ILS**, suggested |
| T19 | The whole order. Broker: 150 VT at $100 (lot A: 100 at $98 at 3.62, first; lot B: 50 at $70 at 3.50); a KH with stocks 6,000 and bonds 20,000; a 2,700 ILS deposit to the broker; rate 3.60; targets 60 / 40 (stocks 75%) | 1) The deposit buys 15 B: stocks 72.55%. 2) The KH moves all 6,000 from stocks to bonds, tax cost 0: stocks 65.30%. 3) Sell 3 VT from lot A (to 63.99%): **tax cost 3.93 ILS (0.36%)**, suggested; the money buys 6 B. Variant, lot A at $90 at 3.60: **27.00 ILS (2.50%)**, not suggested, since the drift at the taxable step is 5.30 (D7) |
| T20 | Which fund. Broker: 100 VT (lot 1: 50 at $60 at 3.40; lot 2: 50 at $110 at 3.70), close $100; 50 VWRA (one lot at $124 at 3.62), close $125; a KH with bonds 30,000; rate 3.60 (stocks 66.10%) | Sell 4 VWRA: **tax cost 1.12 ILS (0.06%)**, suggested. Shown beside: 5 VT would cost 180 ILS (10.0%, FIFO lot 1) |
| T21 | Three classes out (D8). Targets US 30 / outside the US 30 / bonds 40. Broker: 40 VTI (one lot at $248 at 3.62), close $250; 160 VXUS (one lot at $50 at 3.50), close $62.50. A KH with bonds 28,000. Weights 36 / 36 / 28 | Sell 7 VTI: **3.92 ILS (0.06%)**. Sell 9 VXUS: **101.25 ILS (5.00%)**, suggested because bonds are 12 points off (D7). The money buys 46 B; 45 ILS stays as cash. Weights 29.70 / 33.98 / 36.28 |
| T22 | A band narrower than one share. Targets 60 / 37 / gold 3 (band ±0.75). A KH with stocks 10,980 and bonds 6,660; broker: 1 gold share at $100; total 18,000 ILS. Next month: a 1,200 ILS deposit to the broker | Month 1: gold is 2.00%, out, but 0 or 1 or 2 shares give 0 / 2 / 4%: no suggestion, and "it fits once the total is 19,200 ILS". Month 2: buy 1 gold share, 1 VT and 2 B; 120 ILS stays as cash; weights 59.06 / 36.56 / 3.75 (on the edge, so inside) |

### Harvesting

The trading costs below use the parameters of 6.4.

| Test | Case | Expected |
| --- | --- | --- |
| T23 | 100 VT bought at $120 at 3.70 (44,400 ILS); today $100 at 3.70 (37,000 ILS); this year's taxable gain 10,000 ILS, no dividends | Loss 7,400 ≥ max(2,000, 1,850). Trading cost to VWRA 43.96 ILS (5× = 219.78), to ACWI 14.75. Tax value 1,850, all of it worth now. **Flagged**; suggests VWRA (a domicile switch) or ACWI |
| T24 | What the loss is really worth. 100 VT at $120 at 3.60; today $100 at 3.75; this year's gain 3,000; dividends 1,000 ILS (250 of US tax); switch on | Loss 5,700 (the shekel loss; the dollar loss at the sale rate would be 7,500, and the smaller counts). Tax value 1,425 ≥ 5 × 44.55. **Flagged.** Worth now 750; 1,000 goes against dividends, worth 0 (250 of US credit lost); 1,700 carried forward |
| T25 | T5 decides. 300 VT at $100 at 3.70; today $102 at 3.45; this year's gain 10,000 | A dollar gain but a shekel loss of 5,430: allowable 0, **not flagged**. The line says it would be flagged (tax value 1,357.50 against 5 × 121.13) if the accountant rejects T5 |
| T26 | A small loss. 50 VT at $100 at 4.00; today $92.50 at 4.00 | Loss 1,500 < 2,000: not flagged |
| T27 | A small share of a large lot. 1,000 VT at $100 at 3.70; today $96 | Loss 14,800 < 5% of 355,200 (17,760): not flagged |
| T28 | No gain this year, none expected. T23's lot; no gains; dividends 1,200 ILS (300 of US tax) | To ACWI: not flagged. To VWRA: **flagged**, as a domicile switch (D12); worth now 0, 1,200 against dividends (300 of credit lost), 6,200 carried forward |
| T29 | A FIFO group (D10). Lot 1: 300 VT at $90 at 3.90; lot 2: 100 VT at $125 at 3.55; today $100 at 3.60; this year's gain 6,000 | Lot 2 alone would be −8,375, but lot 1 is sold first (+2,700): the group's net loss is 5,675 on 144,000 ILS sold, under 5% (7,200): **not flagged**. (With the loss lot's own value it would be.) |
| T30 | The cost test fails. A loss of 2,400 on a 40,000 ILS lot; trading cost 150 ILS | Tax value 600 < 750: not flagged |
| T31 | A loss carried in already covers this year's gain (D11). 100 VT at $130 at 3.50; today $100 at 3.50; this year's gain 4,000; loss carried in 5,000; no gains expected | This year's taxable gain is 0: **not flagged** (it would be under the literal reading). Shown: worth now 0; 10,500 carried forward |

### The outputs

| Test | Case | Expected |
| --- | --- | --- |
| T32 | Half-years. A gain of 4,000 in March, a loss of −1,000 in September | First half: advance 1,000. Second half: 0 on the gains alone, 0 on its own net, and −250 on the year's net (750 due less 1,000 paid). The year: 750, with 250 back through the annual return |
| T33 | Form 1325 rows, T9's sale | Bought 2026-10-01 at 3.50, sold 2026-10-05 at 3.55: cost 3,500, proceeds 4,615, nominal 1,115, inflationary amount 50, real gain 1,065 |
| T34 | One person, two accounts: +2,000 in one, −2,000 in the other, the same year | Net 0, tax 0 (two separate books would wrongly give 500) |
| T35 | No tax taken off twice. 100 VT at $100 at 3.70 (Jan 2026); a $50 dividend at 3.65, paid net and kept as cash; 40 sold at $110 at 3.60 (tax 260, paid); today (Mar 2027) $120 at 3.50 | Market value 40,731.25. **Value if sold today 39,981.25** (not 39,677.50, which takes the 2026 tax and the US tax off again). Tax paid so far 305.63 |
| T36 | VT against VWRA. 37,000 ILS on one day at 3.70 ($10,000; both at $100). VT pays $2 a share; $150 after US tax buys 1 share at $105 at 3.60, $45 stays as cash. Today VT $110, VWRA $112, rate 3.60 | VT: 40,158.00 ILS, Israel's tax if sold 654.50, **after tax 39,503.50**. VWRA: 40,320.00, tax 830.00, **after tax 39,490.00** |
| T37 | Privacy | On the sample data, no amount, share, ticker or account name in the output, the log or an error; the engine refuses a file without the SAMPLE or PRIVATE line, a missing `--data`, and an `--out` inside this repository |

## 9. Proposed new accountant questions (not added until the owner says so, D19)

13. **Forms 1325 and 1322.** For sales of foreign-listed ETFs at a foreign broker: is one 1325 row per FIFO lot (or
    part of a lot) what the form expects, with reinvested-dividend lots as their own rows? Which columns take a sale
    after the dollar fell (the index ratio below 1)? Are separate 1325 forms filed per half-year?
14. **A harvest that is also a domicile switch.** Selling a US-listed world fund (VT) at a loss and buying an Irish one
    on a different index (VWRA) on the same day: is the loss allowed, given question 6 (section 86)?
15. **The half-year advance: how, and with which losses.** Which form or channel is used today (a notice to the
    assessing office, form 1399, or form 1325 per half)? May a loss carried in from earlier years reduce the advance
    (question 7 asks about the half's own losses)?

## 10. After the owner approves: the build, in order

1. **This repository, sample data only:** the additions of section 4.2, the rebalancing and harvest code, the report
   and the command line, the fund table, the sample folder, tests T11 to T37, and the guardrails of section 2.6. One
   pull request, reviewed like every other.
2. **The private repository's template:** the workflow and empty data files with their header lines, given to the
   owner as text to paste. Nothing of the owner's passes through Claude.
3. **The owner** creates the private repository, pins the engine's commit, fills the files and reads the first report.

Nothing changes in the experiment: no rule, no arm, no fund, no slot; no change to `config/israel_tax.py` or to T1 to
T10.

## 11. What it will not do

No trading, no order, no broker key; no personal number in this repository, a log, an artifact or a push; no model
call; no change to any rule of the experiment.

## 12. Sources (research of 4 Oct 2026)

The research ran from this repository's environment, whose proxy blocked most primary pages (gov.il, GitHub's and
Supabase's own sites, the brokers' and fund providers' pages). The facts come from search summaries cross-checked
across sources, and from GitHub's and Supabase's documentation sources on raw.githubusercontent.com. Each is checked
again on its own page when the engine is built.

- **Forms 1322, 1325, 1324 and the half-year advance**: the Tax Authority's form files for tax year 2025
  ([1322](https://www.gov.il/BlobFolder/service/reporting-and-payment-2025-annual-tax-report-for-individuals/he/Service_Pages_Income_tax_annual-report-2026_1322-2025.pdf),
  [1325](https://www.gov.il/BlobFolder/service/reporting-and-payment-2025-annual-tax-report-for-individuals/he/Service_Pages_Income_tax_annual-report-2026_1325-2025.pdf));
  [tax4broker's guide to 1322 and 1325](https://tax4broker.com/blog/nispach-gimel-form-1322-1325-guide);
  [Capitax](https://www.capitax.co.il/content/1/192). Losses against dividends (section 92(a)(4)), the carry-forward
  with no expiry (section 92(b)) and Circular 10/2025, from the same sources.
- **US withholding for Israeli residents (25% with a W-8BEN)**: [the US–Israel treaty](https://www.irs.gov/pub/irs-trty/israel.pdf).
  **US estate tax above $60,000 for a non-US person**: [IRS](https://www.irs.gov/businesses/small-businesses-self-employed/frequently-asked-questions-on-estate-taxes-for-nonresidents-not-citizens-of-the-united-states).
- **VWRA** (Irish, accumulating, FTSE All-World, from 23 July 2019): [Vanguard](https://fund-docs.vanguard.com/FTSE_All-World_UCITS_ETF_USD_Accumulating_9679_EU_INT_EN.pdf).
  Same-index pairs to avoid: [justETF on MSCI ACWI funds](https://www.justetf.com/uk/how-to/msci-acwi-etfs.html).
- **Interactive Brokers' commissions**: [US stocks](https://www.interactivebrokers.com/en/pricing/commissions-stocks.php),
  [IBKR Lite and Pro](https://www.interactivebrokers.com/en/general/compare-lite-pro.php).
- **GitHub**: 2,000 free Actions minutes a month for private repositories, Pages of a private repository public on
  Free and Pro, checking out a public repository at a SHA with no token: GitHub's documentation and the
  `actions/checkout` README.
- **Supabase**: free projects paused after 7 days of low activity, two free projects per person, no automatic backups
  on the free plan, secret keys bypassing row-level security: Supabase's documentation.
