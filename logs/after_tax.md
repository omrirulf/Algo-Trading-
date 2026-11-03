# After Israeli tax and in shekels

Record through 2026-11-02, written 2026-11-03T03:47:53.850556+00:00. Rules: pre-registration section 5c, every number in `config/israel_tax.py` (tax 25%; losses also against dividends: on; W-8BEN: yes; surtax: off).

Rates: the Bank of Israel's representative rate, 2026-09-10 to 2026-11-02; 35 day(s) from the Bank of Israel, 3 day(s) from another source: 2026-09-11 (ecb), 2026-09-21 (ecb), 2026-10-27 (ecb). Table SHA-256 `95ed5860896303d948b368138bad0b7ae93c66ea68379d1d94f06d4e21bcd434`.

Returns since each book's start. "Tax paid so far" is the tax due on everything sold or received so far; "if sold today" adds every open position sold at the close. "From the $/₪ move" is the shekel return minus the dollar return, before tax and after tax (if sold today).

| | Before tax ($) | After tax, if sold today ($) | After tax, tax paid so far ($) | Before tax (₪) | After tax, if sold today (₪) | After tax, tax paid so far (₪) | From the $/₪ move, before tax | From the $/₪ move, after tax | Tax paid so far (₪) | Tax if sold today (₪) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Paper account (real) | $100,924 (+0.92%) | $100,599 (+0.60%) | $100,924 (+0.92%) | ₪314,681 (+4.10%) | ₪313,668 (+3.76%) | ₪314,681 (+4.10%) | +3.17 points | +3.16 points | ₪0 | ₪1,013 |

The funds are shown after tax once calibration has passed, like every fund result.

## The after-tax gate (section 5c)

No look reached yet. Each look's test is made once, on the first night from the night the race reaches it on which the look is readable, the rate table is there and the funds' prices reach the look's last close.


## For information only (not a gate)

An actively traded fund needs about 0.82 points a year more before tax to tie with VT held 20 years (6% growth, 2% dividend yield). `python -m analysis.tax_breakeven --table`.
