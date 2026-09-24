"""Setup errors (our key or configuration) against model errors, on the journal's own wording."""

import pytest

from analysis.call_errors import MODEL, SETUP, failure_kind


@pytest.mark.parametrize("error", [
    # 2026-09-24, verbatim shape: the key chain picked another provider's key.
    'https://api.deepinfra.com/v1/openai/chat/completions returned HTTP 401: {"error":{"message":'
    '"User is not authorized"}}',
    "HTTP 403 Forbidden",
    "returned HTTP 402: payment required",
    "returned HTTP 404: model gpt-oss-121b not found",
    "AuthenticationError: invalid x-api-key",
    "no API key configured for the full model",
])
def test_our_own_setup_is_a_setup_error(error):
    assert failure_kind(error) == SETUP


@pytest.mark.parametrize("error", [
    # 2026-09-23, verbatim.
    "https://api.deepinfra.com/v1/openai/chat/completions unreachable: The read operation timed out",
    "returned HTTP 500: internal server error",
    "returned HTTP 429: rate limited",
    "the model's answer did not match the schema",
    "answered for NVDA",
    "",
    None,
])
def test_everything_else_counts_against_the_model(error):
    assert failure_kind(error) == MODEL
