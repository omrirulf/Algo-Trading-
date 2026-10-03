# Questions for the accountant

Open tax questions for an Israeli resident who holds US-listed securities at a US broker (Alpaca), as the
after-tax gate assumes it (pre-registration section 5c; every number in `config/israel_tax.py`). Under each
question, *Code today* says what the code assumes until the answer comes, and *Would change* says which setting the
answer could move. Nothing here changes a rule by itself: an answer that changes a setting is a dated entry in the
pre-registration's Amendments table first.

**Where these come from.** Questions 1 to 10 are the owner's own list of 3 Oct 2026, in the owner's words. They
replace the eight questions written on 2 Oct 2026, which had been rebuilt without the owner's tax research.
Questions 11 and 12 are the two the owner added on 2 Oct 2026.

## The owner's questions (3 Oct 2026)

1. **A USD gain that is a shekel loss (test T5).** For a USD ETF sold at a USD gain but a nominal ILS loss (case
   T5), is the allowable loss zero under Circular 10/2025?
   *Code today:* zero. T5 is the owner's reading of the circular's two-step rule, and it **needs confirmation**:
   bought $10,000 at 3.70 (37,000 ILS), sold $10,500 at 3.40 (35,700 ILS), a nominal loss of 1,300 ILS while the
   exchange rate alone took 3,000 ILS; the allowable loss is 0 (`tests/test_israel_tax.py`, T5). *Would change:*
   rule a in `analysis/israel_tax.py` (`lot_gain`).

2. **Losses against foreign dividends.** Must a current-year capital loss first be offset against foreign
   dividends when the foreign tax credit already covers the Israeli tax? Or may I skip that and carry the loss
   forward against future capital gains?
   *Code today:* the loss is offset against the year's dividends (`OFFSET_LOSSES_VS_DIVIDENDS = True`, the harsher
   case for an actively traded fund; test T7), and only the rest carries forward. *Would change:* that switch.

3. **Which lots are sold.** At a foreign broker, may I use specific-lot identification instead of FIFO if broker
   records prove the lot? Does FIFO apply per account, or across all my accounts holding the same security?
   *Code today:* FIFO, per account (`LOT_METHOD = "FIFO"`); every fund and the paper account is its own account.
   *Would change:* `LOT_METHOD`, and whether accounts share one pool of lots.

4. **Which day's rate.** Which Bank of Israel representative rate applies: the trade date or the settlement date?
   Which rate applies on weekends and holidays?
   *Code today:* the trade date; a dividend at its ex-date (the day the funds credit it). For a US trading day with
   no Bank of Israel rate (an Israeli holiday), the European Central Bank's rates crossed through the euro, then
   the Bank of Israel's last earlier rate; every such day is counted (`analysis/boi_rates.py`). Nothing trades on
   a weekend. *Would change:* `FX_SOURCE` and the fallback order.

5. **An accumulating Irish UCITS ETF.** For an accumulating Irish UCITS ETF bought abroad in USD: is there no
   Israeli tax until sale (no deemed distribution, and CFC-type rules do not apply to a widely held ETF)? For the
   same fund bought on the Tel Aviv exchange in ILS: is the tax index the CPI or the USD rate?
   *Code today:* not modelled; every fund holds US-listed securities and VT pays out its dividends. *Would change:*
   nothing now; it matters only if the owner later holds such a fund.

6. **Selling at a loss and buying back (section 86).** Is selling an ETF at a loss and buying a similar-index ETF
   (for example VT to ACWI or VWRA) on the same day exposed to section 86 (artificial transaction)? What about
   buying the same ETF back the next day?
   *Code today:* every loss counts on the day of the sale, with no wash-sale or section 86 rule; the momentum and
   hybrid funds do sell and buy the same names back. *Would change:* how a loss followed by a buy-back is counted
   in the after-tax books.

7. **Half-year advance reports.** Do the half-year advance-payment reports net losses realized in the same half?
   How is an overpayment refunded?
   *Code today:* tax is reckoned per calendar year, and a finished year's tax counts as paid at the year end, so
   "tax paid so far" does not follow half-year payments. *Would change:* when "tax paid so far" counts tax as paid.

8. **Penalties.** What are the penalties for late filing and late payment of the half-year and annual reports?
   *Code today:* not modelled.

9. **Form 1324.** What does Form 1324 cover (foreign income and foreign tax credit, or a declaration of foreign
   assets)? What is the foreign-asset reporting threshold?
   *Code today:* not modelled.

10. **Withholding through HYBRID and Form 867.** With automatic withholding through HYBRID and Form 867, in which
    cases is an annual report still required?
    *Code today:* not modelled; Alpaca is a foreign broker and withholds no Israeli tax.

## Two questions added on 2 Oct 2026

11. **An ILS-hedged fund against a USD ETF.** How is an Israeli fund that tracks a world index with the currency
    hedged to shekels taxed, compared with holding the USD ETF (VT) directly: the inflationary amount and
    currency gains, dividend tax inside the fund against the 25% plus US withholding on VT, the timing of tax
    (inside the fund or on sale), and US estate-tax exposure (which a US-listed ETF has for a non-US person and an
    Israeli fund does not)? (The owner decided on 2 Oct 2026: no ILS fund now; this is a question only.)

12. **The annuity exemption in an investment provident fund (kupat gemel lehashkaa).** Is the tax exemption on
    an annuity taken after age 60 from a kupat gemel lehashkaa still in force? The Arbitrage Committee was
    reported to recommend narrowing it. If it changes, from when, and does it touch money already deposited?

## Not on the list

The owner's list of 3 Oct 2026 replaced the eight questions of 2 Oct, so these points are no longer put to the
accountant. The code keeps its assumption for each:

- **Short sales** (section 5c, conventions 1 and 2): a short sale is measured with the purchase that closes it as the
  cost and the sale as the proceeds, each at its day's rate, and a dividend a short position pays is an allowable
  loss on its day. The model is long-only; the momentum and hybrid funds can short.
- **Capital gains or business income:** every fund is taxed as capital gains at 25%; business-income treatment of
  frequent trading is not modelled.
- **The surtax formula:** off by default (`SURTAX_ENABLED = False`); when on, 2% on all capital income above the
  line, as test T8 has it.
- **Fees:** broker fees are added to the cost and taken off the proceeds.

## Answers

| Question | Date | Answer (the accountant's words) | Setting changed, with its Amendments row |
| --- | --- | --- | --- |
| | | *(none yet)* | |
