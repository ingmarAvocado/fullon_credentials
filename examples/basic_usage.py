"""Basic usage example for fullon_credentials."""

from fullon_credentials import fullon_credentials

# Example: Get credentials for exchange ID 1
# (ex_id 1 is the admin account from demo data)
try:
    secret, key = fullon_credentials(ex_id=1)
    print(f"Successfully retrieved credentials for ex_id 1")
    print(f"Key length: {len(key)} characters")
    print(f"Secret length: {len(secret)} characters")
except ValueError as e:
    print(f"Error: {e}")
    print("Make sure to set EX_ID_1_KEY and EX_ID_1_SECRET in your .env file")