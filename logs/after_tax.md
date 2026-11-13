# After Israeli tax and in shekels

Record through 2026-11-12, written 2026-11-13T03:01:58.139682+00:00. Rules: pre-registration section 5c, every number in `config/israel_tax.py` (tax 25%; losses also against dividends: on; W-8BEN: yes; surtax: off).

Rates: the Bank of Israel's representative rate, 2026-09-10 to 2026-11-12; 43 day(s) from the Bank of Israel, 3 day(s) from another source: 2026-09-11 (ecb), 2026-09-21 (ecb), 2026-10-27 (ecb). Table SHA-256 `a836b4108df6d8c631dd364c13d1936ea9afd78ff7b5f4e68edc7076059a5761`.

Returns since each book's start. "Tax paid so far" is the tax due on everything sold or received so far; "if sold today" adds every open position sold at the close. "From the $/₪ move" is the shekel return minus the dollar return, before tax and after tax (if sold today).

| | Before tax ($) | After tax, if sold today ($) | After tax, tax paid so far ($) | Before tax (₪) | After tax, if sold today (₪) | After tax, tax paid so far (₪) | From the $/₪ move, before tax | From the $/₪ move, after tax | Tax paid so far (₪) | Tax if sold today (₪) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Paper account (real) | $100,519 (+0.52%) | $100,297 (+0.30%) | $100,519 (+0.52%) | ₪318,845 (+5.47%) | ₪318,143 (+5.24%) | ₪318,845 (+5.47%) | +4.95 points | +4.94 points | ₪0 | ₪702 |

The funds are shown after tax once calibration has passed, like every fund result.

## The after-tax gate (section 5c)

No look reached yet. Each look's test is made once, on the first night from the night the race reaches it on which the look is readable, the rate table is there and the funds' prices reach the look's last close.


## For information only (not a gate)

An actively traded fund needs about 0.82 points a year more before tax to tie with VT held 20 years (6% growth, 2% dividend yield). `python -m analysis.tax_breakeven --table`.
