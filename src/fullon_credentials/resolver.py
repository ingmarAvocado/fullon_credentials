"""Credential resolver for fullon ecosystem."""

import os
from typing import Tuple

from dotenv import load_dotenv


class FullonCredentials:
    """
    Credential resolver that checks .env for development keys,
    fallback to Google Secrets Manager for production.
    """

    def __init__(self, ex_id: int) -> None:
        """Initialize with exchange ID."""
        self.ex_id = ex_id
        load_dotenv()

    def _env_lookup(self) -> Tuple[str, str]:
        """
        Load credentials from environment variables.

        Looks for EX_ID_{ex_id}_KEY and EX_ID_{ex_id}_SECRET

        Returns:
            Tuple of (secret, key)
        """
        key_var = f"EX_ID_{self.ex_id}_KEY"
        secret_var = f"EX_ID_{self.ex_id}_SECRET"

        key = os.getenv(key_var)
        secret = os.getenv(secret_var)

        if not key or not secret:
            raise ValueError(f"Credentials not found for ex_id {self.ex_id}")

        return secret, key

def fullon_credentials(exchange_obj) -> Tuple[str, str]:
      """
      Get credentials for exchange.

      Args:
          exchange_obj: Exchange ORM model OR integer ex_id

      Returns:
          Tuple of (secret, key)
      """
      # Handle both Exchange object and raw ex_id
      if hasattr(exchange_obj, 'ex_id'):
          ex_id = exchange_obj.ex_id
      else:
          ex_id = exchange_obj

      resolver = FullonCredentials(ex_id)
      return resolver._env_lookup()



