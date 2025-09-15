"""Type definitions for fullon_credentials."""

import enum
from typing import NamedTuple


class CredentialProvider(str, enum.Enum):
    """Available credential providers."""

    GOOGLE_SECRETS = "google_secrets"
    ENV_FILE = "env_file"

    def __str__(self) -> str:
        return self.value


class CredentialPair(NamedTuple):
    """Container for API key and secret pair."""

    key: str
    secret: str

    def __bool__(self) -> bool:
        """Return True if both key and secret are non-empty."""
        return bool(self.key and self.secret)