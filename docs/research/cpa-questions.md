# Questions for the accountant

Open tax questions for an Israeli resident who holds US-listed securities at a US broker (Alpaca), as the
after-tax gate assumes it (pre-registration section 5c; every number in `config/israel_tax.py`). Each question
says what the code assumes today and which setting would change with the answer. Nothing here changes a rule
by itself: an answer that changes a setting is a dated entry in the pre-registration's Amendments table first.

**A note on where these come from (2 Oct 2026).** The owner asked for "the eight open questions from the Israeli
tax research". That research was not in this repository or in the owner's Google Drive when this file was
written, so questions 1 to 8 below were rebuilt from the points the owner's own rules of 2 Oct 2026 leave open.
**The owner should check them against the research and replace any that differ.** Questions 9 and 10 are the two
new ones the owner asked for.

## The eight open questions

1. **Losses against dividends.** In a year with a net capital loss on foreign securities, must (or may) that loss
   be set against the same year's dividends from foreign securities? If it is, is the US tax withheld on those
   dividends then lost as a credit (it cannot be refunded), and does only the rest of the loss carry forward?
   *Code today:* yes, set against dividends (`OFFSET_LOSSES_VS_DIVIDENDS = True`, the harsher case for an actively
   traded fund; test T7). *Would change:* that switch.

2. **A small nominal loss after the dollar fell (test T5).** Bought $10,000 at 3.70 (37,000 ILS), sold $10,500 at
   3.40 (35,700 ILS): a nominal loss of 1,300 ILS, while the exchange rate alone took 3,000 ILS. Our reading of
   Circular 10/2025's two-step rule is that the allowable loss is 0 (a loss caused only by the exchange rate is
   not deductible). Is that right? *Code today:* 0. *Would change:* rule a in `analysis/israel_tax.py`.

3. **Short sales.** How is a short sale of a USD security measured in shekels: which day's rate is the cost and
   which the proceeds, and how is the inflationary amount figured when the sale comes before the purchase? Is a
   dividend that a short position must pay (a payment in lieu) deductible, and against what? *Code today:* the
   purchase that closes the short is the cost, at its day's rate; the earlier sale is the proceeds, at its day's
   rate; a paid dividend is an allowable loss on its day. The model is long-only, but the momentum and hybrid
   funds can short.

4. **Capital gains or business income.** Could a fully automated account that trades many times a month be
   treated as a business (income taxed at marginal rates, with National Insurance) instead of capital gains at
   25%? Which facts decide it (number of trades, holding time, leverage, time spent, share of income)?
   *Code today:* capital gains at 25% for every fund.

5. **Reporting and advance payments.** With no Israeli withholding at a foreign broker, what must be reported,
   on which forms, and when? Is there a half-year report or an advance payment for gains on securities traded
   abroad, and what does a late one cost? Does "tax paid so far" in our report match when the tax is really
   due? *Code today:* tax is reckoned per calendar year; a finished year's tax counts as paid at the year end.

6. **Which day's rate.** Is the representative rate taken on the trade date or on the settlement date (T+1) for
   purchases and sales? Which day for a dividend: the ex-date or the payment date? On a US trading day when the
   Bank of Israel publishes no rate (an Israeli holiday), which rate is used? *Code today:* the trade date; the
   dividend's ex-date (the day the funds credit it); for a missing day, the European Central Bank's rates
   crossed through the euro, then the Bank of Israel's last earlier rate, each day counted.

7. **Fees and lots.** Are broker commissions and fees added to the cost and taken off the proceeds? Is FIFO
   required, per account, or may specific lots or an average cost be used? If one person has two accounts at
   the same broker, is that one pool of lots or two? *Code today:* fees in the cost and out of the proceeds; FIFO
   per account (`LOT_METHOD = "FIFO"`).

8. **The surtax.** How is the extra 2% on capital income computed: on all capital income above the line (as
   coded, test T8: 2% × (900,000 − 721,560)), or only on the part of total income above the line that is capital
   income? Does capital income here include dividends and gains from an active strategy, and the inflationary
   amount? *Code today:* off by default (`SURTAX_ENABLED = False`); when on, the T8 formula.

## Two new questions (2 Oct 2026)

9. **An ILS-hedged fund against a USD ETF.** How is an Israeli fund that tracks a world index with the currency
   hedged to shekels taxed, compared with holding the USD ETF (VT) directly: the inflationary amount and
   currency gains, dividend tax inside the fund against the 25% plus US withholding on VT, the timing of tax
   (inside the fund or on sale), and US estate-tax exposure (which a US-listed ETF has for a non-US person and an
   Israeli fund does not)? (The owner decided on 2 Oct 2026: no ILS fund now; this is a question only.)

10. **The annuity exemption in an investment provident fund (kupat gemel lehashkaa).** Is the tax exemption on
    an annuity taken after age 60 from a kupat gemel lehashkaa still in force? The Arbitrage Committee was
    reported to recommend narrowing it. If it changes, from when, and does it touch money already deposited?

## Answers

| Question | Date | Answer (the accountant's words) | Setting changed, with its Amendments row |
| --- | --- | --- | --- |
| | | *(none yet)* | |
