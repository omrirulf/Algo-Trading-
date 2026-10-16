# The investor simulator: the private repository's template

Section 10, step 2 of [`investor-simulator-plan.md`](investor-simulator-plan.md) (approved 16 Oct 2026). Everything
below is text for the owner to paste into **a private GitHub repository of their own**. Nothing of the owner's
passes through this public repository or through a Claude session: the engine here is built and tested on sample
data only, and the owner moves the pin.

**Before any data goes in** (section 10, step 3): set every GitHub App installed for "All repositories" (the Claude
GitHub App included) to "Only select repositories", without the private one; revoke every OAuth app and token with
access to private repositories that is not needed; check two-factor login on the GitHub account; create the
repository private from its first commit; set its log and artifact retention to 1 day (Settings, Actions, General);
leave GitHub Pages off; never make it public (that publishes every file and its whole history at once).

## The files

```
data/accounts.csv
data/transactions.csv
data/tax_free.csv
data/plan.csv
data/payments.csv        optional
reports/latest.md        written by the job
reports/YYYY-MM-DD.md    written by the job, one per run
.github/workflows/report.yml
```

**The first line of every data file is the private marker**: a hash sign, a space and the word PRIVATE in capitals,
written as `# PRIVATE` at the very top of the file, on its own. The engine refuses a file without it (a sample file in
the public repository carries `# SAMPLE` instead, and the two are never mixed). The second line is the column names.
`investor/files.py` documents every column; the sample folder `tests/data/investor_sample/` shows each file filled
with made-up numbers.

`accounts.csv`:

```
name,kind,currency
```

One row per account: `kind` is `taxable` (a broker: lots in dollars) or `tax_free` (a keren hishtalmut or a kupat
gemel lehashkaa: tracks in shekels); `currency` is `USD` or `ILS`.

`transactions.csv`, one row per event, in the order they happened:

```
date,account,kind,ticker,quantity,price_usd,fee_usd,amount,currency,withheld_usd,fx,to_account,bought_on,note
```

`kind` is `buy`, `sell`, `dividend`, `deposit`, `withdrawal`, `fee`, `transfer` or `transfer_in`. A dividend's
`amount` is the gross dollars and `withheld_usd` the US tax the broker actually took (left empty only for a US-listed
fund, where the treaty rate is assumed). `fx` is left empty (the Bank of Israel's rate on the day is used) and filled
only to override. `to_account` is only for a `transfer`; `bought_on` only for a `transfer_in` (the lot's original
purchase day). `note` is free text, never printed.

`tax_free.csv`:

```
date,account,track,value_ils
```

`plan.csv`, one row per fact:

```
item,name,class,value,as_of
```

`item` is `target` (a class's percent, all adding up to 100), `fund` (a fund's class, `name` the ticker), `track` (a
tax-free track's mix, `name` as `account:track`, one row per class), `buy_first` (the fund to buy for a class),
`contribution` (an account's new money this month, `value` as an amount and a currency, for example `2700 ILS`),
`carry_in` (the loss carried in from the last assessment, `as_of` its year), `surtax` (`on` or `off`),
`other_income` (the year's other taxable income, only when the surtax is on), `expect_gains_within_3_years` and
`w8ben_filed` (`yes` or `no`, with the date answered in `as_of`), and `pending` (a track change already asked for,
`name` as `account:from>account:to`).

`payments.csv` (optional):

```
date,year,half,amount_ils
```

`half` is `1` or `2` for an advance, `annual` for the year's balance.

## The workflow

`.github/workflows/report.yml`, the only code in the private repository. Replace the two placeholders: `PINNED_SHA`
with the full 40-character commit of this repository's `main` the owner chose (never a branch name), and
`OWNER/REPOSITORY` with this public repository's name. The two actions are pinned by SHA, the same ones
`.github/workflows/ci.yml` here uses.

```yaml
name: Investor report

on:
  schedule:
    # The 1st, 2nd and 3rd at 06:20 UTC: one of them is the month's first Sunday-to-Thursday,
    # and the "first working day" step lets only that one through (D18).
    - cron: "20 6 1-3 * *"
  push:
    paths: ["data/**"]
  workflow_dispatch:

permissions:
  contents: write

concurrency:
  group: investor-report
  cancel-in-progress: false

jobs:
  report:
    runs-on: ubuntu-latest
    steps:
      - name: Stop unless this repository is private
        # A step, not an `if:` on the event: a scheduled run carries no event data.
        env:
          GH_TOKEN: ${{ github.token }}
        run: |
          private=$(gh api "repos/${GITHUB_REPOSITORY}" --jq '.private')
          if [ "$private" != "true" ]; then
            echo "::error::this repository is not private; nothing runs"
            exit 1
          fi

      - name: Only the month's first working day (Sunday to Thursday), unless pushed or asked by hand
        if: github.event_name == 'schedule'
        run: |
          python3 - <<'PY'
          import datetime, sys
          today = datetime.date.today()
          first = next(d for d in (today.replace(day=n) for n in range(1, 8)) if d.weekday() in (6, 0, 1, 2, 3))
          if today != first:
              print("not the first working day; nothing to do")
              sys.exit(0)
          PY

      - uses: actions/checkout@11d5960a326750d5838078e36cf38b85af677262 # v4.4.0
        with:
          persist-credentials: false

      - uses: actions/checkout@11d5960a326750d5838078e36cf38b85af677262 # v4.4.0
        with:
          repository: OWNER/REPOSITORY
          ref: PINNED_SHA
          path: engine
          fetch-depth: 0
          persist-credentials: false

      - name: The pinned commit is on the public repository's main
        run: |
          git -C engine merge-base --is-ancestor PINNED_SHA origin/main \
            || { echo "::error::the pinned commit is not on main"; exit 1; }

      - uses: actions/setup-python@a26af69be951a213d495a4c3e4e4022e16d87065 # v5.6.0
        with:
          python-version: "3.12"

      - name: Install only the engine's own packages, from the hash-locked list
        run: pip install --quiet --require-hashes -r engine/investor/requirements-lock.txt

      - name: Write the report
        # The engine prints "report written" and a line count, nothing else; it gets no token.
        working-directory: engine
        run: python -m investor.report --data "$GITHUB_WORKSPACE/data" --out "$GITHUB_WORKSPACE/reports"

      - name: Commit the report
        run: |
          git config user.name "investor-report"
          git config user.email "investor-report@users.noreply.github.com"
          git add reports
          git commit -m "Investor report" || { echo "nothing new to commit"; exit 0; }
          git push "https://x-access-token:${{ github.token }}@github.com/${GITHUB_REPOSITORY}.git" HEAD
```

What the job can and cannot do: its own short-lived token works only on the private repository and goes to the
privacy check, the two checkouts (which keep no credentials) and the commit step; the install and the engine never
get it. The job holds no secret of the owner's, uploads no artifact and sends no push. The log says "report written"
and how many lines; an error prints only its kind. A bad package could still send the lots out while the engine runs
with network access for prices: the hash lock and the reviewed pin make that unlikely, nothing makes it impossible
(section 2.3).

## Reading the report

`reports/latest.md` on github.com or in the GitHub app, signed in (D2). Every line that proposes a trade starts with
its tax cost and ends with "Suggestion only: you decide and trade yourself." The job never trades.

## Moving the pin

A change to the engine here reaches the owner's data only when the owner replaces `PINNED_SHA` with a newer commit
of `main`, on purpose, after reading what changed. The hash-locked list travels with the commit.
