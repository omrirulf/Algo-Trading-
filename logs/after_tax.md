# After Israeli tax and in shekels

Record through 2026-10-22, written 2026-10-23T01:04:12.909932+00:00. Rules: pre-registration section 5c, every number in `config/israel_tax.py` (tax 25%; losses also against dividends: on; W-8BEN: yes; surtax: off).

Rates: the Bank of Israel's representative rate, 2026-09-10 to 2026-10-22; 29 day(s) from the Bank of Israel, 2 day(s) from another source: 2026-09-11 (ecb), 2026-09-21 (ecb). Table SHA-256 `0bfb876070b927beb097018cdc0b8d7cf37efd675968b7a8a4b3eccfcb77d918`.

Returns since each book's start. "Tax paid so far" is the tax due on everything sold or received so far; "if sold today" adds every open position sold at the close. "From the $/₪ move" is the shekel return minus the dollar return, before tax and after tax (if sold today).

| | Before tax ($) | After tax, if sold today ($) | After tax, tax paid so far ($) | Before tax (₪) | After tax, if sold today (₪) | After tax, tax paid so far (₪) | From the $/₪ move, before tax | From the $/₪ move, after tax | Tax paid so far (₪) | Tax if sold today (₪) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Paper account (real) | $100,341 (+0.34%) | $100,188 (+0.19%) | $100,323 (+0.32%) | ₪310,155 (+2.60%) | ₪309,681 (+2.44%) | ₪310,100 (+2.58%) | +2.26 points | +2.25 points | ₪55 | ₪474 |

The funds are shown after tax once calibration has passed, like every fund result.

## The after-tax gate (section 5c)

No look reached yet. Each look's test is made once, on the first night from the night the race reaches it on which the look is readable, the rate table is there and the funds' prices reach the look's last close.


## For information only (not a gate)

An actively traded fund needs about 0.82 points a year more before tax to tie with VT held 20 years (6% growth, 2% dividend yield). `python -m analysis.tax_breakeven --table`.
