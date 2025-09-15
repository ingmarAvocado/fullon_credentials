# Fullon Credentials Service

Secure credential resolver service for fullon ecosystem with Google Secrets Manager and .env fallback.

## Overview

This service provides secure API credential resolution for fullon trading ecosystem users. It supports:

- Google Cloud Secrets Manager for production
- .env file fallback for development
- Input: fullon_orm User model objects
- Output: tuple with (key, secret) pairs

## Installation

```bash
poetry install
```

## Development

```bash
poetry install --with dev
poetry run pre-commit install
```

## Usage

TODO: Add usage examples after implementation

## Testing

```bash
poetry run pytest
```