# After Israeli tax and in shekels

Record through 2026-10-29, written 2026-10-30T02:12:52.618557+00:00. Rules: pre-registration section 5c, every number in `config/israel_tax.py` (tax 25%; losses also against dividends: on; W-8BEN: yes; surtax: off).

Rates: the Bank of Israel's representative rate, 2026-09-10 to 2026-10-29; 33 day(s) from the Bank of Israel, 3 day(s) from another source: 2026-09-11 (ecb), 2026-09-21 (ecb), 2026-10-27 (ecb). Table SHA-256 `39371b05a7e07432b9178fd783d5db11de46c220eb2c58dfdf037c04a55653c3`.

Returns since each book's start. "Tax paid so far" is the tax due on everything sold or received so far; "if sold today" adds every open position sold at the close. "From the $/₪ move" is the shekel return minus the dollar return, before tax and after tax (if sold today).

| | Before tax ($) | After tax, if sold today ($) | After tax, tax paid so far ($) | Before tax (₪) | After tax, if sold today (₪) | After tax, tax paid so far (₪) | From the $/₪ move, before tax | From the $/₪ move, after tax | Tax paid so far (₪) | Tax if sold today (₪) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Paper account (real) | $100,316 (+0.32%) | $100,166 (+0.17%) | $100,316 (+0.32%) | ₪313,790 (+3.80%) | ₪313,320 (+3.65%) | ₪313,790 (+3.80%) | +3.48 points | +3.48 points | ₪0 | ₪470 |

The funds are shown after tax once calibration has passed, like every fund result.

## The after-tax gate (section 5c)

No look reached yet. Each look's test is made once, on the first night from the night the race reaches it on which the look is readable, the rate table is there and the funds' prices reach the look's last close.


## For information only (not a gate)

An actively traded fund needs about 0.82 points a year more before tax to tie with VT held 20 years (6% growth, 2% dividend yield). `python -m analysis.tax_breakeven --table`.
