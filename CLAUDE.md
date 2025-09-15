# `fullon_credentials` Development Guide for LLMs

## 1. Core Mission & Principles

- **Mission**: Secure credential resolver service for fullon ecosystem that retrieves API credentials from Google Secrets Manager or .env files
- **Architecture (LRRS)**:
    - **Little**: Single purpose: Credential resolution for trading APIs
    - **Responsible**: Secure credential management with fallback mechanisms
    - **Reusable**: Works with any fullon_orm exchange ex_id across ecosystem
    - **Separate**: Zero coupling beyond fullon core libraries (orm, log)

## 2. NON-NEGOTIABLE Development Rules

### A. Input/Output Contract

**CRITICAL**:
- **Input**: fullon_orm.models.exchange.ex_id (integer)
- **Output**: tuple (secret: str, key: str)
- **Integration**: Use fullon_log component logging patterns

### B. Dependencies & Integration

1. **fullon_orm**: Exchange ex_id as input parameter
   ```python
   from fullon_credentials.resolver import fullon_credentials

   # Input MUST be exchange ex_id (integer)
   secret, key = fullon_credentials(ex_id=1)
   ```

2. **fullon_log**: Component-specific logging
   ```python
   from fullon_log import get_component_logger

   logger = get_component_logger("fullon.credentials.resolver")
   logger.info("Credentials retrieved", ex_id=1)
   ```

### C. Security Requirements

1. **Never log credentials**: Only log ex_id
2. **Environment isolation**: Production uses Google Secrets, dev uses .env
3. **Fail securely**: Clear error messages without credential exposure
4. **Validation**: Always validate credential format before returning

## 3. Project Structure

```
fullon_credentials/
├── src/fullon_credentials/
│   ├── __init__.py          # Package exports
│   ├── resolver.py          # Main CredentialResolver class
│   ├── types.py             # CredentialPair, CredentialProvider enums
│   └── exceptions.py        # Custom exceptions
├── tests/
│   ├── unit/               # Unit tests with mocks
│   └── integration/        # Integration tests with real services
├── examples/
│   └── basic_usage.py      # Working examples
└── docs/                   # Additional documentation
```

## 4. Development Environment

Required environment variables:
```bash
# Google Cloud (production)
GOOGLE_CLOUD_PROJECT=your-project-id
GOOGLE_APPLICATION_CREDENTIALS=/path/to/service-account.json

# Development fallback
# Format: EX_ID_{ex_id}_KEY and EX_ID_{ex_id}_SECRET
EX_ID_1_KEY=your_api_key
EX_ID_1_SECRET=your_api_secret
```

## 5. Implementation Guidelines

### A. Credential Resolution Priority
1. Try Google Secrets Manager first (if configured)
2. Fallback to .env file for development
3. Clear error if neither source has credentials

### B. Secret Naming Convention
Google Secrets Manager: `fullon-ex-{ex_id}-api-key` and `fullon-ex-{ex_id}-api-secret`
Environment variables: `EX_ID_{ex_id}_KEY` and `EX_ID_{ex_id}_SECRET`

### C. Error Handling
- Specific exceptions for different failure modes
- Never expose credential values in error messages
- Log attempts without sensitive data

## 6. Testing Strategy

### Unit Tests
- Mock Google Cloud Secret Manager client
- Mock file system for .env testing
- Test credential validation logic
- Test error handling paths

### Integration Tests
- Real Google Cloud integration (with test project)
- Real .env file reading
- End-to-end credential resolution

## 7. Development Workflow

1. **Setup**: `poetry install --with dev`
2. **Tests**: `poetry run pytest`
3. **Linting**: `poetry run black . && poetry run ruff . && poetry run mypy src/`
4. **Coverage**: `poetry run pytest --cov`

## 8. Integration with Fullon Ecosystem

This service integrates with:
- **fullon_orm**: User model input
- **fullon_exchange**: Provides credentials for exchange API calls
- **fullon_log**: Structured logging for security events

The resolver should be used by any fullon service that needs API credentials for external services.