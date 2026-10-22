# After Israeli tax and in shekels

Record through 2026-10-21, written 2026-10-22T01:01:46.478088+00:00. Rules: pre-registration section 5c, every number in `config/israel_tax.py` (tax 25%; losses also against dividends: on; W-8BEN: yes; surtax: off).

Rates: the Bank of Israel's representative rate, 2026-09-10 to 2026-10-21; 28 day(s) from the Bank of Israel, 2 day(s) from another source: 2026-09-11 (ecb), 2026-09-21 (ecb). Table SHA-256 `b535e8491120a4c9040b5ed04ec76eee0c13c7a59437ed24350e38c8c5ac82b4`.

Returns since each book's start. "Tax paid so far" is the tax due on everything sold or received so far; "if sold today" adds every open position sold at the close. "From the $/₪ move" is the shekel return minus the dollar return, before tax and after tax (if sold today).

| | Before tax ($) | After tax, if sold today ($) | After tax, tax paid so far ($) | Before tax (₪) | After tax, if sold today (₪) | After tax, tax paid so far (₪) | From the $/₪ move, before tax | From the $/₪ move, after tax | Tax paid so far (₪) | Tax if sold today (₪) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Paper account (real) | $100,766 (+0.77%) | $100,496 (+0.50%) | $100,700 (+0.70%) | ₪312,980 (+3.53%) | ₪312,141 (+3.26%) | ₪312,775 (+3.47%) | +2.77 points | +2.76 points | ₪205 | ₪839 |

The funds are shown after tax once calibration has passed, like every fund result.

## The after-tax gate (section 5c)

No look reached yet. Each look's test is made once, on the first night from the night the race reaches it on which the look is readable, the rate table is there and the funds' prices reach the look's last close.


## For information only (not a gate)

An actively traded fund needs about 0.82 points a year more before tax to tie with VT held 20 years (6% growth, 2% dividend yield). `python -m analysis.tax_breakeven --table`.
