"""Alpaca credential resolution, including the CLI's stored login.

The Alpaca credential is the one that can move money, so these tests care
less about the happy path than about two properties: a live-trading profile
is never borrowed, and a half-configured environment fails loudly instead of
sending a mismatched pair.
"""

from __future__ import annotations

import logging

import pytest
import yaml

from app import broker_client as bc
from config.settings import Settings

SECRET_VALUE = "super-secret-do-not-log"


def use_settings(monkeypatch, **fields):
    monkeypatch.setattr(bc, "get_settings", lambda: Settings(_env_file=None, **fields))


def write_profile(tmp_path, monkeypatch, name="paper", **fields):
    """Plant a CLI profile and point the lookup at it."""
    monkeypatch.setenv(bc.CLI_CONFIG_DIR_ENV, str(tmp_path))
    profiles = tmp_path / "profiles"
    profiles.mkdir(parents=True, exist_ok=True)
    path = profiles / f"{name}.yaml"
    path.write_text(yaml.safe_dump(fields))
    return path


# --- settings take precedence ---------------------------------------------


def test_settings_credentials_win(monkeypatch):
    use_settings(monkeypatch, alpaca_api_key="PK123", alpaca_secret_key="s3cret")
    creds = bc.resolve_credentials()
    assert (creds.api_key, creds.secret_key) == ("PK123", "s3cret")
    assert creds.source == "settings"
    assert not creds.is_oauth


def test_a_live_profile_is_not_even_consulted_when_settings_are_set(tmp_path, monkeypatch):
    """The live-profile refusal must not fire for someone who never used the CLI.

    Someone with a live CLI profile for their own manual trading should still
    be able to run this system by setting the paper keys explicitly.
    """
    write_profile(tmp_path, monkeypatch, api_key="LIVE", secret_key="LIVE", live_trade=True)
    use_settings(monkeypatch, alpaca_api_key="PK123", alpaca_secret_key="s3cret")

    creds = bc.resolve_credentials()  # must not raise

    assert creds.source == "settings"
    assert creds.api_key == "PK123"


@pytest.mark.parametrize(
    "fields, missing",
    [
        ({"alpaca_api_key": "PK123"}, "ALPACA_SECRET_KEY"),
        ({"alpaca_secret_key": "s3cret"}, "ALPACA_API_KEY"),
    ],
)
def test_half_a_credential_pair_is_an_error(monkeypatch, fields, missing):
    use_settings(monkeypatch, **fields)
    with pytest.raises(bc.BrokerError) as excinfo:
        bc.resolve_credentials()
    assert missing in str(excinfo.value)


def test_no_credentials_anywhere_names_both_options(monkeypatch):
    use_settings(monkeypatch)
    with pytest.raises(bc.BrokerError) as excinfo:
        bc.resolve_credentials()
    message = str(excinfo.value)
    assert "ALPACA_API_KEY" in message
    assert "alpaca profile login" in message


# --- the CLI's stored login -----------------------------------------------


def test_api_keys_are_read_from_the_cli_profile(tmp_path, monkeypatch):
    write_profile(tmp_path, monkeypatch, api_key="PKCLI", secret_key="cli-secret")
    use_settings(monkeypatch)

    creds = bc.resolve_credentials()

    assert (creds.api_key, creds.secret_key) == ("PKCLI", "cli-secret")
    assert creds.source == "cli-apikey:paper"


def test_an_oauth_login_outranks_stored_keys(tmp_path, monkeypatch):
    """Matches the CLI's own precedence: access_token before api_key/secret."""
    write_profile(
        tmp_path, monkeypatch, access_token="tok-abc", api_key="PKCLI", secret_key="cli-secret"
    )
    use_settings(monkeypatch)

    creds = bc.resolve_credentials()

    assert creds.is_oauth
    assert creds.access_token == "tok-abc"
    assert creds.api_key == ""
    assert creds.secret_key == ""


def test_a_profile_with_only_half_a_pair_is_not_usable(tmp_path, monkeypatch):
    write_profile(tmp_path, monkeypatch, api_key="PKCLI")
    use_settings(monkeypatch)
    with pytest.raises(bc.BrokerError) as excinfo:
        bc.resolve_credentials()
    assert "No Alpaca credentials found" in str(excinfo.value)


def test_an_explicitly_paper_profile_is_fine(tmp_path, monkeypatch):
    write_profile(tmp_path, monkeypatch, api_key="PKCLI", secret_key="s", live_trade=False)
    use_settings(monkeypatch)
    assert bc.resolve_credentials().source == "cli-apikey:paper"


# --- the refusal that matters ---------------------------------------------


def test_a_live_profile_is_refused(tmp_path, monkeypatch):
    write_profile(tmp_path, monkeypatch, api_key="PKLIVE", secret_key="live", live_trade=True)
    use_settings(monkeypatch)

    with pytest.raises(bc.BrokerError) as excinfo:
        bc.resolve_credentials()

    message = str(excinfo.value)
    assert "LIVE" in message
    assert "paper-only" in message


def test_a_live_profile_is_refused_before_any_credential_is_taken(tmp_path, monkeypatch):
    """The check runs ahead of extraction, so an OAuth live profile is refused too."""
    write_profile(tmp_path, monkeypatch, access_token="live-token", live_trade=True)
    use_settings(monkeypatch)

    with pytest.raises(bc.BrokerError) as excinfo:
        bc.resolve_credentials()

    assert "live-token" not in str(excinfo.value)
    assert "LIVE" in str(excinfo.value)


def test_the_live_refusal_names_a_way_out(tmp_path, monkeypatch):
    write_profile(tmp_path, monkeypatch, api_key="PKLIVE", secret_key="live", live_trade=True)
    use_settings(monkeypatch)
    with pytest.raises(bc.BrokerError) as excinfo:
        bc.resolve_credentials()
    assert bc.CLI_PROFILE_ENV in str(excinfo.value)


# --- which profile gets picked --------------------------------------------


def test_the_default_profile_is_paper(monkeypatch):
    assert bc.cli_profile_name() == "paper"
    assert bc.CLI_DEFAULT_PROFILE == "paper"


def test_the_profile_env_var_selects_the_profile(tmp_path, monkeypatch):
    write_profile(tmp_path, monkeypatch, name="work", api_key="PKW", secret_key="w")
    monkeypatch.setenv(bc.CLI_PROFILE_ENV, "work")
    use_settings(monkeypatch)

    assert bc.cli_profile_name() == "work"
    assert bc.resolve_credentials().source == "cli-apikey:work"


def test_config_yaml_supplies_the_default_profile(tmp_path, monkeypatch):
    write_profile(tmp_path, monkeypatch, name="alt", api_key="PKA", secret_key="a")
    (tmp_path / "config.yaml").write_text(yaml.safe_dump({"default_profile": "alt"}))
    use_settings(monkeypatch)

    assert bc.cli_profile_name() == "alt"
    assert bc.resolve_credentials().source == "cli-apikey:alt"


def test_the_env_var_beats_config_yaml(tmp_path, monkeypatch):
    (tmp_path / "config.yaml").write_text(yaml.safe_dump({"default_profile": "alt"}))
    monkeypatch.setenv(bc.CLI_CONFIG_DIR_ENV, str(tmp_path))
    monkeypatch.setenv(bc.CLI_PROFILE_ENV, "chosen")
    assert bc.cli_profile_name() == "chosen"


# --- degrading rather than exploding --------------------------------------


def test_a_missing_profile_is_not_an_error(tmp_path, monkeypatch):
    monkeypatch.setenv(bc.CLI_CONFIG_DIR_ENV, str(tmp_path))
    assert bc.credentials_from_cli() is None


def test_malformed_yaml_degrades(tmp_path, monkeypatch):
    monkeypatch.setenv(bc.CLI_CONFIG_DIR_ENV, str(tmp_path))
    profiles = tmp_path / "profiles"
    profiles.mkdir()
    (profiles / "paper.yaml").write_text("api_key: [unclosed\n")
    assert bc.credentials_from_cli() is None


def test_a_yaml_file_that_is_not_a_mapping_degrades(tmp_path, monkeypatch):
    monkeypatch.setenv(bc.CLI_CONFIG_DIR_ENV, str(tmp_path))
    profiles = tmp_path / "profiles"
    profiles.mkdir()
    (profiles / "paper.yaml").write_text("- just\n- a list\n")
    assert bc.credentials_from_cli() is None


def test_an_unreadable_profile_degrades(tmp_path, monkeypatch):
    monkeypatch.setenv(bc.CLI_CONFIG_DIR_ENV, str(tmp_path))
    profiles = tmp_path / "profiles"
    profiles.mkdir()
    path = profiles / "paper.yaml"
    path.write_text(yaml.safe_dump({"api_key": "PK", "secret_key": "s"}))

    def boom(*args, **kwargs):
        raise PermissionError("nope")

    monkeypatch.setattr(type(path), "open", boom, raising=False)
    assert bc.credentials_from_cli() is None


def test_non_string_fields_are_ignored(tmp_path, monkeypatch):
    write_profile(tmp_path, monkeypatch, api_key=12345, secret_key=None)
    assert bc.credentials_from_cli() is None


# --- the credential never reaches the logs --------------------------------


def test_the_credential_value_is_never_logged(tmp_path, monkeypatch, caplog):
    path = write_profile(tmp_path, monkeypatch, api_key="PKCLI", secret_key=SECRET_VALUE)
    use_settings(monkeypatch)

    with caplog.at_level(logging.DEBUG):
        bc.resolve_credentials()

    assert SECRET_VALUE not in caplog.text
    assert str(path) in caplog.text


def test_the_oauth_token_is_never_logged(tmp_path, monkeypatch, caplog):
    write_profile(tmp_path, monkeypatch, access_token=SECRET_VALUE)
    use_settings(monkeypatch)

    with caplog.at_level(logging.DEBUG):
        bc.resolve_credentials()

    assert SECRET_VALUE not in caplog.text


# --- what actually reaches the SDK ----------------------------------------


class RecordingTradingClient:
    last_kwargs: dict = {}

    def __init__(self, **kwargs):
        RecordingTradingClient.last_kwargs = kwargs


@pytest.fixture
def recorded_client(monkeypatch):
    import alpaca.trading.client as sdk

    monkeypatch.setattr(sdk, "TradingClient", RecordingTradingClient)
    RecordingTradingClient.last_kwargs = {}
    return RecordingTradingClient


def test_cli_api_keys_reach_the_sdk_as_a_key_pair(tmp_path, monkeypatch, recorded_client):
    write_profile(tmp_path, monkeypatch, api_key="PKCLI", secret_key="cli-secret")
    use_settings(monkeypatch)

    bc.AlpacaPaperBroker()

    assert recorded_client.last_kwargs["api_key"] == "PKCLI"
    assert recorded_client.last_kwargs["secret_key"] == "cli-secret"
    assert recorded_client.last_kwargs["oauth_token"] is None


def test_a_cli_oauth_login_reaches_the_sdk_as_a_token(tmp_path, monkeypatch, recorded_client):
    write_profile(tmp_path, monkeypatch, access_token="tok-abc")
    use_settings(monkeypatch)

    bc.AlpacaPaperBroker()

    assert recorded_client.last_kwargs["oauth_token"] == "tok-abc"
    assert recorded_client.last_kwargs["api_key"] is None
    assert recorded_client.last_kwargs["secret_key"] is None


def test_the_broker_is_always_constructed_against_paper(tmp_path, monkeypatch, recorded_client):
    write_profile(tmp_path, monkeypatch, api_key="PKCLI", secret_key="cli-secret")
    use_settings(monkeypatch)

    bc.AlpacaPaperBroker()

    assert recorded_client.last_kwargs["paper"] is True
