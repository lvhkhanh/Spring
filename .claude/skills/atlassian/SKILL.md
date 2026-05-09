---
name: atlassian
description: '**WORKFLOW SKILL** — Work across the full Atlassian ecosystem: Confluence, Bitbucket, Bamboo, Statuspage, Opsgenie, Atlassian Cloud Admin, Forge and Connect apps, and cross-product integrations. USE FOR: Confluence page and space management, Bitbucket repository and pipeline setup, Bamboo build plans, Statuspage incident communication, Opsgenie alerting and on-call management, Atlassian REST and GraphQL APIs, Forge/Connect app development, and Atlassian Cloud administration. DO NOT USE FOR: Jira-only tasks (use the jira skill instead), non-Atlassian CI/CD platforms, or unrelated collaboration tools. INVOKES: terminal for CLI operations, HTTP calls for Atlassian APIs, file modifications for configs and app code.'
---

# Atlassian Skill

## Overview

This skill provides comprehensive support for the Atlassian platform ecosystem beyond Jira. It covers Confluence knowledge management, Bitbucket source control and pipelines, Bamboo CI/CD, Statuspage incident communication, Opsgenie alerting, Atlassian Cloud administration, and custom app development with Forge and Connect. For Jira-specific tasks, defer to the dedicated `jira` skill.

## Key Capabilities

### Confluence

- Create, update, archive, and delete Confluence pages and blog posts
- Manage spaces, space permissions, and content restrictions
- Use Confluence REST API v2 and v1 for content automation
- Build page templates, blueprints, and macros
- Manage labels, attachments, and inline comments
- Create and maintain knowledge bases, runbooks, and documentation sites
- Convert between Confluence storage format (XHTML) and Atlassian Document Format (ADF)
- Set up Confluence Cloud automation rules for page lifecycle

### Bitbucket

- Create and manage repositories, branches, and branch permissions
- Configure Bitbucket Pipelines with `bitbucket-pipelines.yml`
- Set up pull request workflows, reviewers, merge checks, and merge strategies
- Manage SSH keys, access tokens, and repository variables
- Implement webhooks and repository hooks
- Use Bitbucket REST API for repository automation
- Configure code owners and branch restrictions
- Set up Bitbucket deployment environments and variables

### Bamboo

- Create and configure build plans, stages, jobs, and tasks
- Set up deployment projects with environments and triggers
- Configure build agents, capabilities, and shared artifacts
- Manage plan variables, global variables, and linked repositories
- Implement plan branches and branch-specific configurations
- Use Bamboo REST API for build and deployment automation
- Configure notifications, triggers, and build dependencies
- Set up artifact sharing between stages and plans

### Statuspage

- Create and manage Statuspage components and component groups
- Publish incidents, scheduled maintenances, and postmortems
- Configure subscribers, notification templates, and automation
- Use Statuspage REST API for programmatic incident management
- Set up third-party metric providers and system metrics
- Manage page access, team members, and page branding

### Opsgenie

- Create and manage alert policies, routing rules, and escalation policies
- Configure on-call schedules, rotations, and overrides
- Set up integrations for alert sources (monitoring, CI/CD, ChatOps)
- Use Opsgenie REST API for alert and incident automation
- Manage teams, roles, and notification preferences
- Configure heartbeat monitors and maintenance windows

### Atlassian Cloud Administration

- Manage organizations, sites, and product access
- Configure identity providers, SSO (SAML/OIDC), and user provisioning (SCIM)
- Administer Atlassian Access policies (2FA enforcement, session policies, API token controls)
- Manage user accounts, groups, and product roles across sites
- Use Admin REST APIs and organization APIs for tenant automation
- Configure audit logs, data residency, and compliance settings

### Forge and Connect App Development

- Scaffold, develop, and deploy Forge apps with `forge create` and `forge deploy`
- Build UI Kit and Custom UI components for Forge
- Develop Connect apps with `atlassian-connect.json` descriptors
- Implement webhooks, listeners, scheduled triggers, and async events
- Use Forge storage, Forge bridge APIs, and product REST APIs from apps
- Manage app environments, installations, and marketplace listings
- Handle app authentication (OAuth 2.0, JWT, API tokens)

## Usage Examples

### Create a Confluence Page Via API

```
Create a Confluence Cloud page in space KEY "ENG" with title
"Deployment Runbook" containing structured documentation
using the Confluence REST API v2.
```

### Set Up Bitbucket Pipelines

```
Create a bitbucket-pipelines.yml that builds a Java Maven project,
runs tests, deploys to staging on develop branch,
and deploys to production on main branch with manual trigger.
```

### Publish Statuspage Incident

```
Create a Statuspage incident reporting partial degradation
of the Payment API component, post updates, and resolve
the incident when the fix is confirmed.
```

### Scaffold a Forge App

```
Create a Forge app that adds a Confluence macro
displaying a custom dashboard with data from an external API.
```

### Configure Opsgenie On-Call

```
Set up an Opsgenie on-call schedule with weekly rotations
across 4 team members, with escalation to the team lead
after 5 minutes of no acknowledgment.
```

## Common Patterns

### Confluence REST API v2 — Create Page

```bash
curl -X POST \
  'https://your-domain.atlassian.net/wiki/api/v2/pages' \
  -H 'Authorization: Basic <base64-email:api-token>' \
  -H 'Content-Type: application/json' \
  -d '{
    "spaceId": "123456",
    "status": "current",
    "title": "Deployment Runbook",
    "body": {
      "representation": "storage",
      "value": "<h2>Pre-deployment Checklist</h2><ul><li>Verify staging tests pass</li><li>Notify stakeholders</li></ul>"
    }
  }'
```

### Confluence REST API v1 — Update Page

```bash
curl -X PUT \
  'https://your-domain.atlassian.net/wiki/rest/api/content/{pageId}' \
  -H 'Authorization: Basic <base64-email:api-token>' \
  -H 'Content-Type: application/json' \
  -d '{
    "version": { "number": 2 },
    "title": "Updated Runbook",
    "type": "page",
    "body": {
      "storage": {
        "value": "<h2>Updated content</h2><p>New deployment steps.</p>",
        "representation": "storage"
      }
    }
  }'
```

### Bitbucket Pipelines Configuration

```yaml
# bitbucket-pipelines.yml
image: maven:3.9-eclipse-temurin-17

definitions:
  caches:
    maven: ~/.m2/repository
  steps:
    - step: &build-and-test
        name: Build and Test
        caches:
          - maven
        script:
          - mvn clean verify
        artifacts:
          - target/**

    - step: &deploy-staging
        name: Deploy to Staging
        deployment: staging
        script:
          - mvn deploy -P staging -DskipTests

    - step: &deploy-production
        name: Deploy to Production
        deployment: production
        trigger: manual
        script:
          - mvn deploy -P production -DskipTests

pipelines:
  branches:
    develop:
      - step: *build-and-test
      - step: *deploy-staging
    main:
      - step: *build-and-test
      - step: *deploy-production

  pull-requests:
    '**':
      - step: *build-and-test

  default:
    - step: *build-and-test
```

### Bitbucket REST API — Create Pull Request

```bash
curl -X POST \
  'https://api.bitbucket.org/2.0/repositories/{workspace}/{repo_slug}/pullrequests' \
  -H 'Authorization: Bearer <token>' \
  -H 'Content-Type: application/json' \
  -d '{
    "title": "FEAT-123: Add payment retry logic",
    "source": { "branch": { "name": "feature/payment-retry" } },
    "destination": { "branch": { "name": "develop" } },
    "description": "Implements exponential backoff for failed payment attempts.",
    "reviewers": [{ "uuid": "{reviewer-uuid}" }],
    "close_source_branch": true
  }'
```

### Statuspage — Create Incident

```bash
curl -X POST \
  'https://api.statuspage.io/v1/pages/{page_id}/incidents' \
  -H 'Authorization: OAuth <api-key>' \
  -H 'Content-Type: application/json' \
  -d '{
    "incident": {
      "name": "Partial degradation of Payment API",
      "status": "investigating",
      "impact_override": "minor",
      "body": "We are investigating increased error rates on the Payment API.",
      "component_ids": ["<component-id>"],
      "components": { "<component-id>": "degraded_performance" }
    }
  }'
```

### Opsgenie — Create Alert

```bash
curl -X POST \
  'https://api.opsgenie.com/v2/alerts' \
  -H 'Authorization: GenieKey <api-key>' \
  -H 'Content-Type: application/json' \
  -d '{
    "message": "CPU usage critical on prod-web-01",
    "alias": "prod-web-01-cpu-critical",
    "description": "CPU utilization exceeded 95% for 5 minutes",
    "priority": "P1",
    "responders": [{ "type": "team", "name": "platform-engineering" }],
    "tags": ["production", "infrastructure", "cpu"]
  }'
```

### Forge App — Basic Confluence Macro

```javascript
// src/index.jsx
import ForgeUI, { render, Macro, Text, useProductContext, useState, useEffect } from '@forge/ui';
import api, { route } from '@forge/api';

const App = () => {
  const context = useProductContext();
  const [data, setData] = useState(null);

  useEffect(async () => {
    const response = await api
      .asUser()
      .requestConfluence(route`/wiki/api/v2/spaces/${context.spaceKey}`);
    const spaceData = await response.json();
    setData(spaceData);
  }, []);

  return (
    <Macro>
      <Text>
        {data ? `Space: ${data.name} (${data.key})` : 'Loading...'}
      </Text>
    </Macro>
  );
};

export const run = render(<App />);
```

### Forge Manifest

```yaml
# manifest.yml
modules:
  macro:
    - key: space-info-macro
      function: main
      title: Space Info
      description: Displays current space information
  function:
    - key: main
      handler: index.run

app:
  id: ari:cloud:ecosystem::app/<app-id>

permissions:
  scopes:
    - read:confluence-space.summary
```

### Forge CLI Commands

```bash
# Install Forge CLI
npm install -g @forge/cli

# Create a new Forge app
forge create

# Deploy to development environment
forge deploy

# Install app on an Atlassian site
forge install

# View logs
forge logs

# Deploy to production
forge deploy --environment production

# Tunnel for local development
forge tunnel
```

### Atlassian Cloud Admin — User Provisioning (SCIM)

```bash
curl -X POST \
  'https://api.atlassian.com/scim/directory/{directoryId}/Users' \
  -H 'Authorization: Bearer <api-token>' \
  -H 'Content-Type: application/scim+json' \
  -d '{
    "userName": "jdoe@company.com",
    "displayName": "John Doe",
    "emails": [{ "value": "jdoe@company.com", "type": "work", "primary": true }],
    "name": { "givenName": "John", "familyName": "Doe" },
    "active": true
  }'
```

### Python — Atlassian Python API

```python
from atlassian import Confluence, Bitbucket

# Confluence operations
confluence = Confluence(
    url='https://your-domain.atlassian.net/wiki',
    username='user@example.com',
    password='<api-token>',
    cloud=True
)

# Create a page
confluence.create_page(
    space='ENG',
    title='API Documentation',
    body='<h2>Endpoints</h2><p>List of API endpoints.</p>',
    parent_id=None,
    type='page',
    representation='storage'
)

# Get page content
page = confluence.get_page_by_title(space='ENG', title='API Documentation')

# Bitbucket operations
bitbucket = Bitbucket(
    url='https://api.bitbucket.org',
    username='user@example.com',
    password='<app-password>',
    cloud=True
)

# List repositories in workspace
repos = bitbucket.get_repositories(workspace='my-workspace')
```

## Best Practices

### Authentication

- Use API tokens (Atlassian account email + API token) for Cloud REST API calls
- Use OAuth 2.0 (3LO) for user-context operations in apps
- Use Forge `api.asUser()` and `api.asApp()` for Forge app authentication
- Store credentials in environment variables, CI/CD secrets, or vault — never hardcode
- Rotate API tokens and app passwords regularly
- Apply least-privilege scopes for OAuth and Forge permissions

### Confluence

- Use the v2 REST API for new integrations; v1 for operations not yet available in v2
- Structure spaces by team, project, or domain — avoid monolithic spaces
- Use page trees and labels for discoverability
- Apply content restrictions only when necessary; prefer space-level permissions
- Use templates and blueprints for consistent page structures
- Keep storage format HTML clean and avoid inline styles
- Archive stale pages rather than deleting to preserve link integrity

### Bitbucket

- Enforce branch permissions and merge checks on protected branches
- Use Pipelines variables and deployment environments for secrets management
- Keep `bitbucket-pipelines.yml` DRY with YAML anchors and definitions
- Limit pipeline step artifacts to what downstream steps actually need
- Use caches for build dependencies to speed up pipeline runs
- Configure code owners for automated review assignment
- Use repository variables and deployment variables — never commit secrets

### Bamboo

- Keep build plans modular with stages and jobs
- Use shared artifacts only for cross-stage dependencies
- Set meaningful plan and branch cleanup policies
- Use plan variables for environment-specific configuration
- Avoid storing secrets in plan configurations — use Bamboo linked repositories or variables with encryption

### Statuspage

- Define components that match real infrastructure boundaries
- Use component groups for logical service categories
- Keep incident updates frequent, clear, and timestamped
- Use scheduled maintenance windows for planned changes
- Configure subscriber notification preferences to reduce alert fatigue
- Post postmortems after major incidents

### Opsgenie

- Define clear alert priorities (P1–P5) with SLA expectations
- Keep escalation chains short and actionable
- Use alert deduplication to prevent notification storms
- Configure heartbeat monitors for critical background services
- Review on-call schedules monthly for fairness and coverage
- Use maintenance windows to suppress alerts during planned work

### Forge and Connect Apps

- Prefer Forge for new app development (serverless, hosted by Atlassian)
- Use environment variables for secrets in Forge apps
- Implement proper error handling and logging with `console.log` (visible via `forge logs`)
- Test locally with `forge tunnel` before deploying
- Use Forge storage for small key-value data; external storage for large datasets
- Follow Atlassian Design Guidelines for UI Kit and Custom UI

## Troubleshooting

### Authentication Failures

- Verify API token is valid and not expired
- Check basic auth encoding: `base64(email:api-token)`
- Confirm OAuth scopes match the required permissions for the endpoint
- Ensure the user has product access (Confluence, Bitbucket, etc.)
- For Forge apps, verify `manifest.yml` permissions and app installation

### Confluence Issues

- **403 on page update**: check page restrictions, space permissions, and version number increment
- **Page not found**: verify page ID and that the page is not in trash
- **Storage format errors**: validate HTML against Confluence storage format spec
- **Macro rendering issues**: check macro parameters and ensure the app/plugin is installed
- **Rate limiting**: implement exponential backoff and respect `Retry-After` headers

### Bitbucket Issues

- **Pipeline failures**: check `bitbucket-pipelines.yml` syntax, image availability, and step scripts
- **Pipeline variables not resolving**: ensure variables are set at the correct scope (repository, deployment, workspace)
- **PR merge blocked**: check merge checks, required approvals, and branch permissions
- **Webhook not firing**: verify webhook URL accessibility, event selection, and response codes
- **Repository access denied**: check workspace membership, repository permissions, and app passwords

### Bamboo Issues

- **Build agent offline**: check agent capabilities, memory, and connectivity
- **Artifact not found**: verify artifact naming, subscription patterns, and stage ordering
- **Deployment fails**: check environment permissions, deployment triggers, and release naming

### Statuspage Issues

- **Incident not visible**: check component assignment, page access settings, and subscriber filters
- **Subscriber notifications not sent**: verify notification templates, email delivery, and subscriber preferences
- **API errors**: validate `page_id`, `component_id`, and API key permissions

### Opsgenie Issues

- **Alerts not routed**: check routing rules, team assignments, and integration configurations
- **Escalation not triggering**: verify escalation policy conditions, timing, and responder availability
- **Integration failures**: check API key, webhook URL, and payload format for the alert source

## Integration Points

- **Jira**: cross-product linking, Jira issues from Confluence, Bitbucket commit references in Jira
- **CI/CD**: Bitbucket Pipelines, Bamboo, GitHub Actions, Jenkins, Azure DevOps
- **ChatOps**: Slack, Microsoft Teams, Mattermost via Atlassian integrations
- **Monitoring**: Opsgenie integrations with Datadog, PagerDuty, Prometheus, Grafana, New Relic
- **Identity**: Atlassian Access, SAML SSO, OIDC, SCIM user provisioning
- **Development**: Forge CLI, Connect framework, Atlassian SDK, atlassian-python-api
- **Documentation**: Confluence, Notion import/export, Markdown-to-Confluence converters
- **Incident management**: Statuspage, Opsgenie, Jira Service Management
- **Marketplace**: Atlassian Marketplace for app distribution and licensing
