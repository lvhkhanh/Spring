---
name: curl
description: '**WORKFLOW SKILL** — Build, test, and debug HTTP requests and API integrations using curl. USE FOR: composing REST calls, handling headers/authentication, uploading/downloading files, troubleshooting API responses, and scripting repeatable CLI-based API workflows. DO NOT USE FOR: browser UI automation, non-HTTP protocols that require specialized clients, or full API lifecycle management better handled by dedicated tools. INVOKES: terminal command snippets, file system edits for request scripts, semantic search for API/request best practices.'
---

# cURL API and HTTP Workflow Skill

## Overview

This skill provides structured support for using `curl` to interact with APIs and HTTP services. It focuses on reliable request construction, authentication handling, response inspection, error troubleshooting, and reusable shell-friendly workflows.

## Key Capabilities

### Request Construction
- Build GET, POST, PUT, PATCH, DELETE requests
- Set headers for content type, accept type, and custom metadata
- Send query parameters and path parameters correctly
- Submit JSON, form-encoded, and multipart payloads

### Authentication and Security
- Use Bearer tokens, API keys, basic auth, and custom auth headers
- Pass credentials safely via environment variables
- Handle TLS/SSL settings for secure and development environments
- Avoid leaking secrets in shell history and logs

### Response Handling and Debugging
- Inspect status codes, headers, timing, and response body
- Debug with `-v`, `-i`, and `--trace` options
- Follow redirects and inspect intermediate responses
- Diagnose common HTTP failures (4xx/5xx, auth errors, CORS confusion)

### File Transfer Workflows
- Upload files with multipart form data
- Download files with robust output naming and resume support
- Handle binary responses safely
- Validate content type and response size assumptions

### Automation and Scripting
- Create reusable shell scripts with parameterized endpoints
- Chain `curl` with `jq`, `xargs`, and other CLI tools
- Add retries, timeouts, and fail-fast behavior
- Prepare CI-friendly API smoke tests

## Usage Examples

### Simple JSON GET request
```bash
curl -sS -X GET 'https://api.example.com/v1/users?limit=10' \
  -H 'Accept: application/json'
```

### Authenticated POST request
```bash
curl -sS -X POST 'https://api.example.com/v1/orders' \
  -H 'Authorization: Bearer $API_TOKEN' \
  -H 'Content-Type: application/json' \
  -d '{"sku":"ABC-123","quantity":2}'
```

### Multipart upload
```bash
curl -sS -X POST 'https://api.example.com/v1/files' \
  -H 'Authorization: Bearer $API_TOKEN' \
  -F 'file=@./report.pdf' \
  -F 'category=finance'
```

### Download with fail-fast and retry
```bash
curl -fL --retry 3 --retry-delay 2 --connect-timeout 10 \
  -o artifact.zip 'https://downloads.example.com/artifact.zip'
```

## Common Patterns

### Fail on HTTP errors and print diagnostics
```bash
curl -sS -f -w '\nHTTP %{http_code}\n' \
  -H 'Accept: application/json' \
  'https://api.example.com/health'
```

### Separate response body and status code
```bash
status=$(curl -sS -o /tmp/resp.json -w '%{http_code}' 'https://api.example.com/v1/items')
if [ "$status" -ne 200 ]; then
  echo "Request failed with HTTP $status" >&2
  cat /tmp/resp.json >&2
  exit 1
fi
```

### POST JSON from file
```bash
curl -sS -X POST 'https://api.example.com/v1/import' \
  -H 'Content-Type: application/json' \
  --data @payload.json
```

### Token via environment variable
```bash
: "${API_TOKEN:?API_TOKEN is required}"
curl -sS -H "Authorization: Bearer $API_TOKEN" 'https://api.example.com/v1/me'
```

## Best Practices

- Use `-sS` for script-friendly output with useful errors
- Add `-f` in automation to fail on HTTP 4xx/5xx responses
- Set explicit `--connect-timeout` and `--max-time` for reliability
- Keep secrets in env vars and avoid hard-coded tokens
- Prefer `--data @file.json` for large or reusable payloads
- Use `jq` for JSON parsing instead of fragile string parsing
- Include retries for transient network failures

## Troubleshooting

### TLS or certificate errors
- Verify endpoint certificate chain and hostname
- Avoid `-k/--insecure` except short-lived local debugging
- Check corporate proxy or MITM certificate requirements

### Authentication failures (401/403)
- Confirm token validity, scopes, and expiration
- Check header format and expected auth scheme
- Verify environment variable values before request execution

### Request formatting issues (400/415)
- Match `Content-Type` with actual body format
- Validate JSON payload syntax and field names
- Confirm API version and endpoint path correctness

### Unexpected redirects or empty responses
- Use `-L` to follow redirects intentionally
- Add `-i` or `-v` to inspect headers and flow
- Check if endpoint requires specific accept headers

## Integration Points

- **CLI processing**: jq, sed, awk, xargs
- **Scripting**: Bash automation and cron workflows
- **CI/CD**: GitHub Actions, GitLab CI, Jenkins smoke checks
- **API ecosystems**: REST services, internal gateways, webhook endpoints
- **Debugging tools**: Postman/curl parity checks, API gateway logs
