# The investor simulator: plan and private-data design

**Status: plan only, for the owner's approval (4 Oct 2026). Nothing is built.** The owner's instruction of
4 Oct 2026: "Investor simulator: plan first, don't build yet. … Show me the plan and the private-data design
before you build."

- **A tool, not a test.** It uses no experiment slot, gets no card and no graveyard row, and N stays at 41.
- **Shadow-only.** It never trades, holds no broker key and sends no order. It only suggests; the owner decides
  and trades by hand.
- **The owner's personal numbers** (lots, holdings, income, savings, targets) **never go into this public
  repository, a log, an artifact or a phone push.** Section 2 is how.
- **When it is built, it is built and tested with sample data only** (made-up numbers, in this repository), and
  the owner's real numbers stay in the private place of section 2.

## 0. What the owner decides

Everything below waits for these answers. My recommendation is first in each row.

| # | Decision | Recommended | Other options |
| --- | --- | --- | --- |
| D1 | Where the lots live and where the job runs | **A private GitHub repository** of the owner's own (section 2.3) | A private Supabase project (2.4); the owner's own computer only (2.5) |
| D2 | Where the owner reads the report | **A page in that private repository**, read on github.com or the GitHub app, signed in | A private table in Supabase; an email to the owner |
| D3 | One home for all personal numbers? | **Yes: the coach's later data entry also goes to the private repository** (this changes the coach plan's "private Supabase project", so only if the owner agrees) | Two places: lots in the private repository, the coach's numbers in Supabase |
| D4 | New contributions | **Fill the classes below target, the largest gap first, each up to its target** | All of it to the class furthest below target |
| D5 | A target under 4%, where "band edge minus 1 point" passes the target | **Trade to the target itself** | Leave such a class out of the bands |
| D6 | A sale's tax cost | **This year's extra tax plus 25% of the loss carried forward that the sale uses up** | This year's extra tax only |
| D7 | FIFO and harvesting a later lot | **Test the sale of every lot up to and including the loss lot, net** (FIFO sells the earlier ones first) | Test the loss lot alone (not possible to sell alone under FIFO) |
| D8 | "Domicile switch" | **A swap from a US-listed fund to an Irish one** | Any swap between domiciles, both ways |
| D9 | Trading cost estimate until a broker is chosen | **Per side: a commission plus half the spread, as parameters** (section 6.4) | The owner's own broker's numbers, from day one |
| D10 | The similar-but-not-identical funds | **The table in section 6.5** | The owner's own list |
| D11 | Keren hishtalmut and kupat gemel lehashkaa | **Shown at their value; tax at a lump-sum withdrawal from the gemel not modelled at first** | Model the gemel's withdrawal tax (needs the CPI) |
| D12 | When it runs | **The first working day of each month (with the coach), and when the owner changes a file** | Only by hand |
| D13 | Two new accountant questions (section 9) | **Add them to `cpa-questions.md`** | Wait |

## 1. What it does

Once a month, and whenever the owner changes the lot file, it reads the owner's files, prices every holding at the
last close and the Bank of Israel's representative rate, and writes **one private report**:

1. **Value if sold today**: what the money is worth after Israeli tax if every taxable lot were sold at the close,
   in shekels (and dollars), per account and in total.
2. **Tax paid so far**: the tax on everything sold or received so far (finished years, and this year as if it
   ended today).
3. **Rebalancing**: each asset class against its target and band; a suggestion only when a band is broken, and
   **the shekel tax cost before every suggestion**.
4. **Harvest suggestions**: taxable lots whose loss is worth taking, each with a similar but not identical fund.
5. **The annual report pack**: half-year figures, the rows for forms 1322 and 1325, and the loss carried forward.
6. **Against buy-and-hold VT and VWRA**: the same shekels, on the same days, in VT or in VWRA and held; after tax,
   "if sold today", in shekels.

It never sends an order. Every suggestion says "suggestion: you decide and trade yourself".

## 2. Where it runs and where the lots live: the private-data design

### 2.1 What is private and what is public

| Private: only in the owner's private place | Public: may be in this repository |
| --- | --- |
| Lots and transactions, account names and numbers, balances | The tax rules and the owner's rule numbers (bands, 0.5%, 2,000 ILS, 5%, 5×): they are not personal |
| Targets, contributions, salary, savings | The engine: pure code, no file path to a personal file, no network |
| The finished report | Sample data: made-up numbers, marked as sample in every file |
| "Do I expect gains within 3 years?" | Prices and Bank of Israel rates (public data) |

This repository, its Actions logs, its artifacts and its GitHub Pages site are public today (`docs/next-steps.mdx`).
So, as with the coach (`monthly-coach-plan.md`, section 3), **the job cannot run in this repository's workflows**:
one stray `print` or traceback would publish a number for good.

### 2.2 The options

| | A. Private GitHub repository (recommended) | B. Private Supabase project | C. The owner's computer only |
| --- | --- | --- | --- |
| Where the lots live | CSV files in the private repository | Tables in a new Supabase project of its own | Files on the computer |
| Where the job runs | That repository's own GitHub Actions | A private repository's Actions with the project's secret key, or an Edge Function | `python -m investor.report` by hand |
| Where the owner reads it | A Markdown page in the private repository | The Supabase dashboard, or an email | A file on the computer |
| Keys needed | **None** (it reads its own files and the public engine) | The project's secret key, which bypasses row-level security | None |
| History of every change | Yes: every edit is a commit (useful for the accountant) | Only backups | Only what the owner keeps |
| Entering lots | Edit or upload a CSV on github.com; a broker's export can be pasted | The table editor, or its CSV import | Any editor |
| Runs by itself | Yes | Yes | No |
| Cost | Free (a few Actions minutes a month) | Free plan limits (2.4) | Free |

### 2.3 Recommended: A, a private GitHub repository

The owner creates it (for example `investor-private`; private from the first commit). It holds only:

```
data/accounts.csv        one row per account: name, kind (taxable / tax_free), currency
data/transactions.csv    one row per event (section 3)
data/tax_free.csv        the tax-free accounts' value per asset class, by month
data/plan.csv            targets per asset class, the month's contributions, the owner's yes/no inputs
reports/latest.md        the report (written by the job)
reports/YYYY-MM-DD.md    each run's report, kept
.github/workflows/report.yml
```

The workflow (about 30 lines, given to the owner as a template; it is the only code in the private repository):

1. Runs on the first working day of each month and on every push that changes `data/`.
2. **Refuses to run if the repository is not private** (`if: github.event.repository.private`), so a mistake in
   the settings cannot publish anything.
3. Checks out the private repository, then **this public repository at one pinned commit** (a SHA, never a branch
   name), so no later change here can reach the owner's data until the owner moves the pin on purpose.
4. Runs the engine: `python -m investor.report --data data --out reports`. It fetches public prices and the Bank of
   Israel's rates itself.
5. Commits the report to `reports/`. **No artifact, no upload, no phone push, no secret.** Its log says only "report
   written" and how many lines; the engine prints no amount, share or ticker (a test checks this, section 8).

```
public repository (engine, sample data, tests)                 the owner's private repository
            │                                                    data/*.csv  (the owner's lots)
            │  checked out at a pinned commit, read-only                 │
            └──────────────────────────────►  report.yml (private Actions, no secret)
                                                    │  public prices, Bank of Israel rates
                                                    ▼
                                        reports/latest.md  ── read by the owner, signed in
nothing flows back to the public repository, a log, an artifact or the phone
```

**Why A:** no key exists that could leak; every change to a lot is a commit the accountant can trace; the engine
is the same tested code as here; and it costs nothing.

**What A does not protect against:** anyone with access to the owner's GitHub account, and GitHub itself, can read
the private repository; so can any app or session the owner gives access to it. A Claude session is one: **this
plan never needs the private repository in a Claude session.** The engine is built and tested here with sample
data only, and the owner moves the pin.

### 2.4 Option B, a private Supabase project

A new project of its own, never the archive's (whose secret key this public repository's workflows hold). Tables
`accounts`, `transactions`, `tax_free`, `plan` and `reports`, row-level security on and no policy, so the
publishable key reads nothing; the job holds the secret key. It fits the coach's approved plan (one home for the
coach's numbers and the lots), but it needs a secret key, the table editor is slow for many lots, it keeps no
history of edits, and a free project is paused after a week without activity, so a monthly job would find it
asleep (see the sources in section 11).

### 2.5 Option C, the owner's computer only

The most private: nothing online. But nothing runs by itself, and the owner must install Python and run it each
month. A fallback if the owner does not want the data on any server.

### 2.6 Guardrails in this public repository (built with the engine)

- **No personal file can be committed here.** A CI step fails if a file named like the private files
  (`transactions*.csv`, `accounts*.csv`, `tax_free*.csv`, `plan*.csv`, `lots*`, `holdings*`) is anywhere but the
  sample folder `tests/data/investor_sample/`, and every sample file must start with the line
  `# SAMPLE: made-up numbers, not the owner's`.
- **The engine reads only the folder it is given.** No default path, no environment variable that points at data.
- **It prints nothing personal.** A test runs the CLI on the sample data and checks that its output has no amount,
  share, ticker or account name in it.
- **It cannot trade.** No broker import, no key, no network except the price and rate fetch (the same CI pattern as
  "The shadow funds cannot trade").
- **No workflow in this repository runs it** on real data, and none holds a secret for it.

## 3. The owner's files (the data model)

`transactions.csv`, one row per event, in the order they happened:

| Column | Example (sample) | Notes |
| --- | --- | --- |
| `date` | 2026-03-02 | The trade date |
| `account` | Broker-1 | One of `accounts.csv` |
| `kind` | `buy`, `sell`, `dividend`, `deposit`, `withdrawal`, `fee` | |
| `ticker` | VT | Empty for a deposit |
| `quantity` | 10 | Shares; may be a fraction |
| `price_usd` | 100.00 | Per share |
| `fee_usd` | 1.00 | Into the cost of a buy, off the proceeds of a sale |
| `amount` and `currency` | 37000, ILS | For a deposit, a withdrawal, a dividend (gross) or a fee |
| `fx` | (empty) | Empty: the Bank of Israel's rate on `date`. Filled only to override, and then the report says so |
| `note` | | Free text, never printed in a log |

- A dividend that is reinvested is a `dividend` row plus a `buy` row (a new lot, rule c).
- Deposits and withdrawals in shekels are what the VT and VWRA comparison invests (section 7.4).
- `plan.csv`: one row per asset class (`class`, `target_percent`), the funds in each class (`ticker`, `class`), the
  month's contributions (`account`, `amount_ils`), and two yes/no inputs: `expect_gains_within_3_years`, and
  `w8ben_filed` (default yes).

## 4. Tax, scope (a): what is reused and what is added

### 4.1 Reused as it is

| Need | Already in the repository |
| --- | --- |
| The rules' numbers | `config/israel_tax.py` (25%, the surtax as parameters, FIFO, the switch, the rate source) |
| FX as the index, one lot | `analysis.israel_tax.lot_gain` (T1 to T6) |
| A year's netting, the carry-forward, losses against dividends | `analysis.israel_tax.year_tax` (T7) |
| Dividends with the US credit | `analysis.israel_tax.dividend_tax` (T10) |
| The surtax | `analysis.israel_tax.surtax` (T8); still off by default, the salary only an input |
| FIFO lots per account | `analysis.israel_tax.TaxBook` (T9) |
| "If sold today", "tax paid so far" | `TaxBook.state` |
| The Bank of Israel's rate on a day | `analysis.boi_rates` (with the European Central Bank's rates for a missing day, each one counted) |

T1 to T10 stay exactly as they are, and so does every number in `config/israel_tax.py`. T5 still needs the
accountant's confirmation (question 1), and the report says so next to every number it touches.

### 4.2 Added (small, each with tests on sample data)

1. **Each closed lot keeps its purchase day, rate and dollar amounts** (today `Realised` keeps only the sale day).
   The form rows need them. An added field; no number of T1 to T10 changes.
2. **One person's year across accounts.** Israel nets a person's year, not an account's: the year's gains and
   losses of every taxable account go into one `year_tax`. FIFO stays per account (rule c).
3. **Half-years.** The same lines split January to June and July to December.
4. **The tax cost of a possible sale.** The year reckoned with and without the sale's lines (section 5.3).
5. **The allowable loss of open lots today**, lot by lot and in FIFO order (section 6.2).
6. **Dividends reinvested net.** `TaxBook.state` adds the US tax withheld because the funds credit dividends gross
   (convention 3 of section 5c). Here the owner's dividends arrive net, so only Israel's tax is taken off; the US tax
   is shown, never taken off twice.
7. **An accumulating fund** (VWRA) has no dividend rows: nothing new, only the fund table's domicile.

## 5. Rebalancing, scope (b)

### 5.1 The owner's rule

Bands of ±5 points absolute (25% relative for targets under 20%). Order: new contributions first, then tax-free
accounts, then taxable sales last. Trade back to the band edge minus 1 point. Taxable sales only if the estimated tax
cost is under 0.5% of the amount traded, unless the drift is above 10 points. Always show the shekel tax cost before
any suggestion.

### 5.2 How the code reads it

- **Weights** are of the whole: every account, taxable and tax-free, in shekels at the day's rate.
- **Band** = ±5 points for a target of 20% or more; ±25% of the target for a target under 20% (10% → ±2.5 points). At
  20% both give 5.
- **Out of band** = further from the target than the band; on the edge itself is inside.
- **Trade to** = the edge minus 1 point: a class above its band goes down to target + band − 1, a class below goes
  up to target − band + 1. **D5:** when the band is 1 point or less (a target of 4% or less), it goes to the target.
- **Drift** = the distance from the target in points (absolute), of the class whose band is broken. The 10-point
  override is for that class.
- **Where the money goes:** a sale's money goes to the classes below their target, the largest gap first, each up
  to its target; money for a class below its band comes from the classes above their target, the largest first.
- **The tax cost of a taxable sale (D6)** = Israel's extra tax this year because of the sale, plus 25% of the loss
  carried forward that the sale uses up. A loss carried forward is worth 25% of itself later, so using it now is a
  cost. When a loss would otherwise be set against dividends already covered by the US credit, that part is worth
  nothing, and using it is free. Reckoned with `year_tax` on the owner's whole year, FIFO lots, at the day's close and
  rate. **0.5% is compared with the shekels sold.** The fee and spread are shown beside it, not in it.
- **Shares** are whole shares, the number nearest to the amount; the report shows the weight after the trade.

### 5.3 The steps, every run

1. Price everything; compute the weights, bands and drifts. Show the table even when nothing is out of band.
2. **Contributions (D4):** the month's new money goes to the classes below target, the largest gap in shekels
   first, each up to its target; anything left by the targets' shares. The weights are computed again.
3. **Tax-free accounts:** a class still out of band is moved inside the keren hishtalmut or the kupat gemel
   lehashkaa (a change of investment track) as far as the money there allows, to the "trade to" point. Tax cost:
   0 ILS, shown. A track change can take a few days; the report says so.
4. **Taxable sales, last:** for a class still out of band, the account and fund whose FIFO sale costs the least tax
   per shekel are sold first. The suggestion is made only if the tax cost is under 0.5% of the shekels sold, or the
   drift is above 10 points. Otherwise the report says "not suggested" and why, with the same tax cost, and that the
   next contributions go to the class below target.
5. Every line starts with the tax cost in shekels: "Tax cost: 0 ILS." included.

## 6. Harvest suggestions, scope (c)

### 6.1 The owner's rule

Flag a lot if its allowable ILS loss is at least the larger of 2,000 ILS and 5% of the lot value, and the tax value
(25% × the loss) is at least 5 times the estimated trading cost, and there is a net gain this year or the owner
expects gains within 3 years or the swap is a domicile switch. Suggest a similar but not identical fund. Never trade
automatically.

### 6.2 How the code reads it

- **Allowable ILS loss** = rule a at today's close and the Bank of Israel's rate, with `lot_gain`. A loss made only by
  the exchange rate gives 0 (T5, still to be confirmed by the accountant).
- **FIFO (D7):** a later lot cannot be sold before the earlier lots of the same fund in the same account. So the test
  is for selling every lot up to and including the loss lot: their gains and losses together. Every prefix is tried;
  the one with the largest net loss that passes is shown, lot by lot.
- **Lot value** = the shekel value of what would be sold, at today's close and rate.
- **Tax value** = 25% × the net loss, as the rule says. Beside it, what it is really worth: this year (against this
  year's net gain), carried forward (against later gains), and the part that would be set against this year's
  dividends while `OFFSET_LOSSES_VS_DIVIDENDS` is on (worth nothing: the US credit already covered that tax).
- **Trading cost** = both sides (sell the lot, buy the other fund): commission plus half the spread each side.
- **Net gain this year** = the realised gains less losses of every taxable account so far this year, before the
  harvest.
- **Expects gains within 3 years** = the owner's yes/no in `plan.csv`.
- **Domicile switch (D8)** = the other fund is Irish and the sold one is US-listed.
- **Warnings on every suggestion:** whether selling at a loss and buying a similar fund is safe under section 86 is
  accountant question 6, still open; and T5 if it applies.

### 6.3 The steps

For each taxable account, each fund, each FIFO prefix of open lots: compute the net allowable loss, its value, the
tax value, the trading cost and the gain condition; flag the prefix if all three tests pass; suggest the other fund
from section 6.5. Nothing is sold: the line says "suggestion only".

### 6.4 Trading cost parameters (D9)

Public parameters until the owner's broker is known, then the owner's own. Per side: a commission, plus half the
bid-ask spread; plus the currency conversion when shekels must become dollars. The report prints the numbers it used.
Starting values, from Interactive Brokers' published prices for a retail client in Israel (IBKR Pro: IBKR Lite and
fractional shares are not offered to Israeli residents, so whole shares only):

| | Commission per side | Half the spread |
| --- | --- | --- |
| A US-listed fund (VT, ACWI) | $0.005 a share, at least $1.00, at most 1% of the trade | 0.01% |
| An Irish fund in dollars on the LSE (VWRA, ISAC) | $4.00 up to $8,000, then 0.05% of the trade | 0.05% (a cautious figure) |
| Shekels to dollars | 0.002% of the amount, at least $2.00 | — |

These are checked again against the broker's own page when the engine is built, and the broker decision (June 2027)
may replace them.

### 6.5 Similar but not identical funds (D10)

Never the same index: a fund on the same index (for example VWRA and VWRL, which are the same fund, or ACWI and
ISAC, which both follow MSCI ACWI) is refused by the code, because each fund in the table carries its index. The
table is public (no personal number).

| Sold | Suggested | Similar because | Not identical because |
| --- | --- | --- | --- |
| VT (US-listed, FTSE Global All Cap) | VWRA (Irish, FTSE All-World, accumulating) | World stocks, the same provider | No small companies; a **domicile switch** (D8) |
| VT | SPYI (Irish, MSCI ACWI IMI, accumulating) | World stocks with small companies | Another provider and index; a **domicile switch** |
| VT | ACWI (US-listed, MSCI ACWI) | World stocks | Another provider and index; no domicile switch |
| VWRA | ISAC (Irish, MSCI ACWI, accumulating, in dollars on the LSE) | World stocks, the same domicile | Another provider and index |
| ACWI | VT | World stocks | Another provider and index |
| VTI (US total market, CRSP) | ITOT (S&P Total Market) or SCHB (Dow Jones Broad Market) | US stocks | Three different indexes |
| VXUS (FTSE Global All Cap ex US) | IXUS (MSCI ACWI ex USA IMI) | Stocks outside the US | Another provider and index |

Every suggestion that keeps money in a US-listed fund also shows the owner's US-listed holdings against the $60,000
line above which the US estate tax applies to a non-US person (Israel has no estate-tax treaty with the US); a
domicile switch lowers that amount. This is a note in the private report, not a rule.

Prices: VWRA and ISAC are quoted in dollars on the LSE; the pence lines (SSAC, VWRL) are not used, so no unit can be
mixed up. VWRA's prices start on 23 July 2019.

## 7. The report, scope (d)

1. **Summary**: total value; value if sold today (shekels and dollars); tax paid so far; the rate and close used.
2. **Allocation**: each class, its weight, target, band and drift; the suggestions of section 5, tax cost first.
3. **Harvest**: the flagged lots of section 6, with their warnings; or "nothing to flag".
4. **Against VT and VWRA** (7.4).
5. **The annual report pack** (7.2, 7.3), this year so far and each finished year.
6. **What is assumed**: T5, the dividend switch (question 2), VWRA before a sale (question 5), section 86 (question
   6), the half-year netting (question 7), and every day whose rate did not come from the Bank of Israel.

### 7.2 Half-year figures

For January to June and July to December: realised gains, allowable losses, the net, dividends and the US tax
withheld, and the tax on the half's net at 25%. Whether the half-year advance payment nets the half's losses is
accountant question 7: until it is answered the pack shows both, the net and the gains alone.

### 7.3 Form rows and the loss carried forward

- **One row per closed lot** (or part of one): the fund, purchase day, sale day, quantity, cost and proceeds in
  dollars, both rates, cost and proceeds in shekels, the nominal gain, the inflationary amount, and the taxable gain
  or allowable loss. These are the per-sale details.
- **The year's summary**: total gains, total losses, the net, the loss set against dividends, the carry-forward used,
  the taxable gain, the tax, and the loss carried out.
- **Form 1325** (appendix G(1) of the annual return 1301) lists every sale of traded securities on which no tax was
  withheld at source, which is every sale at a foreign broker: the per-sale rows go there. **Form 1322** (appendix G)
  is the year's capital gains from traded securities and the offset of losses against gains and dividends, filled
  from the 1325 detail: the summary goes there. (Found in the research of 4 Oct 2026; section 11.) The exact fields
  are copied from the current forms when the engine is built, and the mapping is put to the accountant (section 9,
  question 13) before the owner files anything from it.

### 7.4 Against buy-and-hold VT and VWRA

- **The same shekels on the same days.** Every deposit into a taxable account (and every withdrawal) buys (or sells)
  VT, and separately VWRA, at that day's close, with the same trading cost model.
- **VT**: each dividend, less the 25% US tax withheld, is reinvested on its day as a new lot. Israel's extra tax is
  usually 0 (T10).
- **VWRA**: accumulating, so no dividend rows; no Israeli tax until it is sold (accountant question 5 asks whether that
  is right). Its prices start in July 2019; money that went in earlier is shown as "n/a" for VWRA.
- **Shown in shekels, after tax "if sold today"**: the value, the money-weighted return a year, and the difference from
  the owner's taxable accounts. The tax-free accounts are the same in all three, so they are left out.

## 8. Tests, on sample data only

Numbered after the owner's T1 to T10, in a new `tests/test_investor.py` next to `tests/test_israel_tax.py`. Fees 0,
tax 25%, as in T1 to T10. Every number below was worked with the repository's own `lot_gain` and `year_tax`; the
owner may change any of them before they are written as tests.

### Rebalancing

| Test | Case | Expected |
| --- | --- | --- |
| T11 | Bands and "trade to" points for targets 60, 20, 10 and 3 | Bands ±5, ±5, ±2.5, ±0.75. Trade to 64 / 56, 24 / 16, 11.5 / 8.5, and 3 / 3 (D5). A weight of 65 with a target of 60 is inside. |
| T12 | Contributions first. Stocks 70,000, bonds 30,000 (targets 60 / 40, both out of band); 20,000 ILS new money | Bonds +18,000, stocks +2,000; 60% / 40%; no sale; "Tax cost: 0 ILS" |
| T13 | Tax-free accounts second. A broker account with VT 100,000; a keren hishtalmut with stocks 50,000 and bonds 50,000; targets 60 / 40 (stocks 75%) | In the keren hishtalmut, move 22,000 from stocks to bonds (stocks to 64%); tax cost 0 ILS; no taxable sale |
| T14 | A taxable sale under 0.5%. VT: 100 shares bought at $100 at 3.70; today $104 at 3.60 (37,440 ILS); bonds 18,560 ILS; targets 60 / 40 (stocks 66.86%, drift 6.86) | Sell 4 VT (1,497.60 ILS): nominal +17.60, inflationary amount −40, taxable 17.60, **tax cost 4.40 ILS (0.29%)**: suggested; stocks to 64.18% |
| T15 | A taxable sale over 0.5%, drift 10 or less. VT: 100 shares bought at $60 at 3.40; today $100 at 3.60 (36,000 ILS); bonds 18,000 (stocks 66.67%) | 4 VT (1,440 ILS) would cost **144 ILS (10.0%)**: not suggested, with the reason and the cost |
| T16 | The same lots, drift over 10. Bonds 12,000 (stocks 75%, drift 15) | Sell 15 VT (5,400 ILS), **tax cost 540 ILS (10.0%)**: suggested because the drift is over 10; stocks to 63.75% |
| T17 | FIFO decides the cost. Lot 1: 10 VT at $60 at 3.40; lot 2: 10 VT at $110 at 3.70; today $100 at 3.60; sell 10 | Lot 1 is sold (taxable 1,440, tax 360), not lot 2 (which would have been an allowable loss of 360) |
| T18 | The carry-forward is a cost (D6). T15's sale with a realised loss of −1,000 earlier this year | No dividends: extra tax this year 0, carry-forward used 576, **cost 144 ILS**: not suggested. With 1,000 ILS of dividends (US tax 250) and the switch on: the loss would be set against them anyway, **cost 0 ILS**: suggested |

### Harvesting

| Test | Case | Expected |
| --- | --- | --- |
| T19 | 100 VT bought at $120 at 3.70 (44,400 ILS); today $100 at 3.70 (37,000 ILS); net gain this year 10,000 ILS; trading cost 22.20 ILS both sides | Allowable loss 7,400 ≥ max(2,000, 1,850); tax value 1,850 ≥ 5 × 22.20; flagged; suggests VWRA or ACWI |
| T20 | The T5 shape: $10,000 at 3.70, today $10,500 at 3.40 | Allowable loss 0: not flagged (T5, to be confirmed) |
| T21 | A small loss: 50 VT at $100 at 4.00, today $92.50 at 4.00 | Loss 1,500 < 2,000: not flagged |
| T22 | A small share of a large lot: 1,000 VT at $100 at 3.70, today $96 at 3.70 | Loss 14,800 < 5% of 355,200 (17,760): not flagged |
| T23 | T19's lot with no net gain this year and "expect gains" no | To ACWI: not flagged. To VWRA: flagged (domicile switch). With "expect gains" yes: flagged. The report shows the tax value now 0 and 7,400 carried forward; with 1,000 ILS of dividends and the switch on, 1,000 set against them (250 of US credit lost) and 6,400 carried forward |
| T24 | FIFO prefix. Lot 1: 50 VT at $80 at 3.70; lot 2: 50 VT at $120 at 3.70; today $100 at 3.70 | Lot 2 alone is −3,700, but lot 1 is sold first (+3,700): net 0, not flagged |
| T25 | Trading cost too high: a loss of 2,400 on a 40,000 ILS lot; trading cost 150 ILS both sides | Tax value 600 < 750: not flagged |

### Outputs

| Test | Case | Expected |
| --- | --- | --- |
| T26 | Half-years: a gain of 4,000 in March, a loss of −1,000 in September | First half net 4,000, second half −1,000; the year 3,000, tax 750 |
| T27 | Per-sale rows, T9's sale | Bought 2026-10-01 at 3.50, sold 2026-10-05 at 3.55: cost 3,500, proceeds 4,615, nominal 1,115, inflationary amount 50, taxable gain 1,065 |
| T28 | One person, two accounts: +2,000 in one, −2,000 in the other, the same year | Net 0, tax 0 (two separate books would wrongly give 500) |
| T29 | VT against VWRA: 37,000 ILS on one day at 3.70 ($10,000; both at $100). VT pays $2 a share: $150 after US tax, reinvested at $105 on a day at 3.60. Today VT $110, VWRA $112, rate 3.60 | VT: 101.43 shares, 40,165.71 ILS, Israel's tax if sold 656.43, **after tax 39,509.29 ILS**. VWRA: 40,320 ILS, tax 830, **after tax 39,490.00 ILS** |
| T30 | Privacy | The CLI on the sample data prints no amount, share, ticker or account name; the sample files carry the SAMPLE line; the engine reads no path it was not given |

## 9. Proposed new accountant questions (not added until the owner says so, D13)

13. **Forms 1322 and 1325.** For sales of foreign-listed ETFs at a foreign broker, which figures go on form 1322 and
    which on form 1325, and is one row per FIFO lot (or part of a lot) what the forms expect?
14. **A harvest that is also a domicile switch.** Selling a US-listed world fund (VT) at a loss and buying an Irish
    one on a different index (VWRA) the same day: is the loss allowed, given question 6 (section 86)?

## 10. After the owner approves: the build, in order

1. **This repository, sample data only:** the additions of section 4.2, the rebalancing and harvest code, the report
   and the CLI, the sample folder, tests T11 to T30, and the guardrails of section 2.6. A pull request, reviewed like
   every other.
2. **The private repository's template:** the workflow file and empty data files with their headers, given to the
   owner as text to paste. Nothing of the owner's passes through Claude.
3. **The owner** creates the private repository, pins the engine's commit, fills the files and reads the first report.

Nothing changes in the experiment: no rule, no arm, no fund, no slot; the coach stays a checklist (its data entry is
still not built, and waits for the owner).

## 11. Sources

To be filled from the research of 4 Oct 2026.

## 12. What it will not do

No trading, no order, no broker key; no personal number in this repository, a log, an artifact or a push; no model
call; no change to any rule of the experiment, to `config/israel_tax.py` or to T1 to T10.
