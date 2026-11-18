# After Israeli tax and in shekels

Record through 2026-11-17, written 2026-11-18T03:57:26.699166+00:00. Rules: pre-registration section 5c, every number in `config/israel_tax.py` (tax 25%; losses also against dividends: on; W-8BEN: yes; surtax: off).

Rates: the Bank of Israel's representative rate, 2026-09-10 to 2026-11-17; 46 day(s) from the Bank of Israel, 3 day(s) from another source: 2026-09-11 (ecb), 2026-09-21 (ecb), 2026-10-27 (ecb). Table SHA-256 `f3589292e5b2f17369992e82ba8be88d25c77bba2f00c95dc3657749bc0c5d89`.

Returns since each book's start. "Tax paid so far" is the tax due on everything sold or received so far; "if sold today" adds every open position sold at the close. "From the $/₪ move" is the shekel return minus the dollar return, before tax and after tax (if sold today).

| | Before tax ($) | After tax, if sold today ($) | After tax, tax paid so far ($) | Before tax (₪) | After tax, if sold today (₪) | After tax, tax paid so far (₪) | From the $/₪ move, before tax | From the $/₪ move, after tax | Tax paid so far (₪) | Tax if sold today (₪) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Paper account (real) | $100,502 (+0.50%) | $100,208 (+0.21%) | $100,502 (+0.50%) | ₪323,917 (+7.15%) | ₪322,969 (+6.84%) | ₪323,917 (+7.15%) | +6.65 points | +6.63 points | ₪0 | ₪947 |

The funds are shown after tax once calibration has passed, like every fund result.

## The after-tax gate (section 5c)

No look reached yet. Each look's test is made once, on the first night from the night the race reaches it on which the look is readable, the rate table is there and the funds' prices reach the look's last close.


## For information only (not a gate)

An actively traded fund needs about 0.82 points a year more before tax to tie with VT held 20 years (6% growth, 2% dividend yield). `python -m analysis.tax_breakeven --table`.
