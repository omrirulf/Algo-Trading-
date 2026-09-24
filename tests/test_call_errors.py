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
    # orchestrator/heartbeat.full_model_provider, verbatim: the secret unset.
    "MODEL_BASE_URL is 'https://api.deepinfra.com/v1/openai' but FULL_MODEL_API_KEY is empty; "
    "the endpoint that decides what is traded would be asked anonymously",
    # The Anthropic SDK's wording, and its error class reaching the catch-all.
    "Error code: 401 - {'type': 'error', 'error': {'type': 'authentication_error'}}",
    "unexpected AuthenticationError: Error code: 401",
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
    # Text the model or the provider wrote is never searched for setup words.
    "invalid LLM output: 1 validation error for LLMSignal rationale String should have at most 2000 "
    "characters [type=string_too_long, input_value='Unauthorized trading scandal at a bank...', input_type=str]",
    'https://api.deepinfra.com/v1/openai/chat/completions returned HTTP 500: '
    '{"error":"upstream authentication service timeout"}',
    "model declined to answer (category: forbidden content)",
    "",
    None,
])
def test_everything_else_counts_against_the_model(error):
    assert failure_kind(error) == MODEL
