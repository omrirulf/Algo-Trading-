# After Israeli tax and in shekels

Record through 2026-10-07, written 2026-10-08T02:19:49.213466+00:00. Rules: pre-registration section 5c, every number in `config/israel_tax.py` (tax 25%; losses also against dividends: on; W-8BEN: yes; surtax: off).

Rates: the Bank of Israel's representative rate, 2026-09-10 to 2026-10-07; 18 day(s) from the Bank of Israel, 2 day(s) from another source: 2026-09-11 (ecb), 2026-09-21 (ecb). Table SHA-256 `86c005283a9576db4c9bbdcf4638671d55d74bf404c6ad8b9cbd310fe6147aef`.

Returns since each book's start. "Tax paid so far" is the tax due on everything sold or received so far; "if sold today" adds every open position sold at the close. "From the $/₪ move" is the shekel return minus the dollar return, before tax and after tax (if sold today).

| | Before tax ($) | After tax, if sold today ($) | After tax, tax paid so far ($) | Before tax (₪) | After tax, if sold today (₪) | After tax, tax paid so far (₪) | From the $/₪ move, before tax | From the $/₪ move, after tax | Tax paid so far (₪) | Tax if sold today (₪) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Paper account (real) | $102,463 (+2.46%) | $101,911 (+1.91%) | $102,388 (+2.39%) | ₪312,820 (+3.48%) | ₪311,134 (+2.92%) | ₪312,591 (+3.40%) | +1.02 points | +1.01 points | ₪229 | ₪1,687 |

The funds are shown after tax once calibration has passed, like every fund result.

## The after-tax gate (section 5c)

No look reached yet. Each look's test is made once, on the first night from the night the race reaches it on which the look is readable, the rate table is there and the funds' prices reach the look's last close.


## For information only (not a gate)

An actively traded fund needs about 0.82 points a year more before tax to tie with VT held 20 years (6% growth, 2% dividend yield). `python -m analysis.tax_breakeven --table`.
