

# --- the dispersion measure must not be a magnitude measure ----------------


def _entry(conviction, scores):
    """A journal entry with just the fields the agreement check reads."""
    import dataclasses

    from analysis.reader import JournalEntry

    names = ("news_score", "technical_score", "fundamental_score",
             "analyst_score", "insider_score")
    blank = {f.name: ({} if f.name in ("scores", "blend") else
                      [] if f.name in ("key_factors", "gaps") else
                      "" if f.name in ("ticker", "model") else None)
             for f in dataclasses.fields(JournalEntry)}
    blank.update(ticker="AAA", bias="BULLISH", conviction=conviction,
                 scores=dict(zip(names, scores)))
    if "timestamp_is_exact" in blank:
        blank["timestamp_is_exact"] = False
    # None means "this line recorded no section info", which is what makes
    # available_scores() return the scores as given. An empty set would null
    # every one of them as sourceless.
    blank["sections"] = None
    return JournalEntry(**blank)


def test_a_loud_but_unanimous_model_is_not_called_disobedient():
    """Score spread and 'one dimension is loud' are nearly the same series.
    A model that is confident exactly when one dimension shouts -- and never
    when they conflict -- is doing what the prompt asks, and the controlled
    measure must not condemn it."""
    from analysis.metrics import agreement_check

    entries = []
    for i in range(40):
        loud = 0.1 + i * 0.02
        # Every dimension agrees in sign; only the magnitude varies, and
        # conviction tracks it. Spread rises with magnitude by construction.
        entries.append(_entry(min(0.9, 0.2 + loud), [loud, loud * 0.5, loud * 0.2, None, None]))

    check = agreement_check([e for e in entries])
    assert check.dispersion_vs_magnitude.rho is not None
    assert check.dispersion_vs_magnitude.rho > 0.5, "the confound should be visible"
    controlled = check.dispersion_vs_conviction_controlled.rho
    assert controlled is None or controlled < check.dispersion_vs_conviction.rho, (
        "holding magnitude fixed must weaken a purely magnitude-driven effect"
    )


def test_the_confound_is_reported_so_the_raw_number_can_be_read():
    from analysis.metrics import agreement_check

    check = agreement_check([_entry(0.4, [0.5, -0.4, 0.1, None, None]) for _ in range(30)])
    assert hasattr(check, "dispersion_vs_magnitude")
    assert hasattr(check, "dispersion_vs_conviction_controlled")


def test_the_report_names_the_controlled_number_as_the_finer_one():
    """The old text pointed the reader at the confounded number and called it
    finer. That printed a false alarm on every cycle."""
    from analysis import report
    from analysis.metrics import agreement_check

    check = agreement_check([
        _entry(0.3 + (i % 5) * 0.1, [0.5, -0.4, 0.1, None, None]) for i in range(40)
    ])
    text = report._agreement_section(check) if hasattr(report, "_agreement_section") else None
    if text is None:
        import inspect
        source = inspect.getsource(report)
        assert "THE FINER MEASURE" in source
        assert "read the spread correlation as the finer measure" not in source
