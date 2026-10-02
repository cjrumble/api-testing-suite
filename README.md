# API Testing Suite

Python REST API CRUD automation example using `requests` against the GoRest public API.

## What this demonstrates
- REST GET/POST/PUT/DELETE operations
- Bearer-token authentication
- Dynamic test data
- HTTP status and JSON validation
- Timeouts and basic failure handling
- Environment-based credential management

## Secure setup
Set the token locally:
```bash
export GOREST_API_TOKEN="your-token"
python RequestAPI.py
```

For CI, store the token as a repository secret and expose it as `GOREST_API_TOKEN`. Any token previously committed to this repository should be revoked even after the source is corrected.

## Portfolio note
This small example is retained as supporting API-testing evidence; larger quality-engineering projects are the primary portfolio focus.
