---
name: postman
description: Assist with Postman workflows, API testing, collection management, environments and CI/CD integration.
INVOKES:
  - api
  - bash
---

# Overview

The Postman skill provides guidance for API development, manual and automated API testing, environment configuration, collection organization, and CI/CD integration. It helps users set up proper request flows, manage variables securely, and collaborate on API contracts.

# Key Capabilities

- Create and configure Postman collections, folders, and requests
- Use environments and variables to parameterize requests
- Apply pre-request scripts and test scripts with JavaScript
- Automate tests and assertions with Newman
- Integrate Postman collections into CI/CD pipelines
- Use monitors, mocks, and API schemas (OpenAPI/RAML)
- Debug requests, inspect response payloads, and handle auth mechanisms (API key, OAuth 2.0, Bearer tokens, etc.)

# Usage Examples

1. Create a simple collection with a GET endpoint.

```postman
# Steps:
# 1. In Postman, create a new collection named "Todo API".
# 2. Add a request "Get Todos" with URL https://api.example.com/todos.
# 3. Set method to GET.
# 4. Save.
```

2. Use environment variables:

```postman
# In environment config:
# - base_url = https://api.example.com
# In request URL: {{base_url}}/todos
```

3. Add a test script:

```javascript
pm.test("Status code is 200", function () {
    pm.response.to.have.status(200);
});
pm.test("Body is JSON", function () {
    pm.response.to.be.json;
});
```

4. Run with Newman for CI:

```bash
echo "Running Postman collection through Newman"
newman run ./collections/todo-api.postman_collection.json -e ./environments/dev.postman_environment.json \
  --reporters cli,junit --reporter-junit-export ./reports/newman-report.xml
```

# Common Patterns

- Use shared environments per stage (dev, staging, production).
- Store secrets in Postman variables or external secret managers; avoid hard-coding credentials.
- Break large suites into smaller collections for modular testing.
- Use folder-level config to apply scripts to related request groups.
- Pair pre-request scripts with tests for dynamic flows (e.g., auth token refresh).

# Best Practices

- Maintain one source-of-truth API schema (OpenAPI, RAML) and generate collections from it.
- Use descriptive names for collections, requests, and variables.
- Keep assertions focused and clear; each script should verify one behavior.
- Integrate Postman runs in PR pipelines to enforce API contract tests.
- Version collections and environments alongside application code in git.

# Troubleshooting

- Check that base URLs and endpoints are correct for the selected environment.
- Validate that variables are set and resolved by checking the Postman console (`View > Show Postman Console`).
- If auth fails, confirm credentials and grant scopes are correct; run the auth request manually.
- For flaky tests, add retries in scripts or use stable dataset states.
- When Newman fails, inspect `--reporters junit` output or `--verbose` logs.

# Integration Points

- CI workflows: GitHub Actions, GitLab CI, Jenkins, Azure Pipelines
- Source control: Git, repository versioning
- API schema: OpenAPI, RAML
- Monitoring and documentation: Postman mock servers, monitors, and API docs
- Team collaboration: Postman workspace sharing and role-based access control
