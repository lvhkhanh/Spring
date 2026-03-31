---
name: teams
description: "**WORKFLOW SKILL** — Design, build, configure, and troubleshoot Microsoft Teams applications and integrations. USE FOR: Teams app development (tabs, bots, messaging extensions), Teams API usage, Teams app deployment, Teams automation. DO NOT USE FOR: unrelated collaboration tools or non-Teams platforms. INVOKES: file system tools for manifest and code generation, terminal for Teams CLI and Azure tooling."
---

# Microsoft Teams Skill

## Overview

This skill covers Microsoft Teams app development, integration patterns, and deployment workflows.
Use this skill for building teams tabs, bots, connectors, messaging extensions, and automation scripts against Teams APIs. This abstraction is for both _developers_ (code artifacts, bot frameworks) and _admins_ (tenant app policy, deployment rules).

## Key Capabilities

- Create Teams app manifests, tabs, bots, and messages.
- Develop Teams bots with Bot Framework SDK (C#, Node.js) or Teams Toolkit.
- Build message extensions and adaptive cards with rich interactions.
- Manage Teams apps using Graph API and Admin SDK.
- Configure app permission policies, setup policies, and tenant rollout.
- Enable automation for provisioning teams, channels, owners, and access controls.

## Usage Examples

1. Scaffold a Teams app (CLI):

```bash
npm install -g @microsoft/teamsfx-cli
teamsfx new --template "tab" --name acme-tab-app
cd acme-tab-app
teamsfx preview
```

2. Deploy Teams bot using Azure and Teams Toolkit:

```bash
teamsfx provision --env default
teamsfx deploy --env default
teamsfx publish --env default
```

3. Use Microsoft Graph to create a Team programmatically:

```bash
curl -X POST https://graph.microsoft.com/v1.0/teams \
  -H "Authorization: Bearer $TOKEN" \
  -H "Content-Type: application/json" \
  -d '{"template@odata.bind":"https://graph.microsoft.com/v1.0/teamsTemplates/standard","displayName":"Acme Team","description":"Team for Acme project"}'
```

4. Send adaptive card to channel via bot:

```json
{
  "type": "message",
  "attachments": [{
    "contentType": "application/vnd.microsoft.card.adaptive",
    "content": {
      "$schema": "http://adaptivecards.io/schemas/adaptive-card.json",
      "type": "AdaptiveCard",
      "version": "1.4",
      "body": [{"type":"TextBlock","text":"Hello from Teams skill!"}]
    }
  }]
}
```

## Common Patterns

- Use `teamsfx` CLI for local development and scaffold.
- Store `manifest.json` in `appPackage` for Teams app package.
- Implement bot reactions and proactive messages through Azure Bot registration.
- Use Graph API `application` permissions for creating channels, user assignments.
- Apply Teams policy assignment via `Graph` endpoint and tenant-wide setup.

## Best Practices

- Keep app manifest minimal and versioned.
- Use Azure Key Vault for secrets and certificate storage.
- Follow least privilege for Graph permissions and conditionally grant.
- Combine adaptive cards with validation and deep-links.
- Enable telemetry (App Insights) for bots and tabs diagnostics.

## Troubleshooting

- Verify app manifest `developer` URL, endpoints and permissions for app policies.
- Check bot service `Messaging endpoint` and SSL/TLS handshake errors.
- Inspect Teams dev tools with `F12` for tab pages and service object calls.
- Use `teamsfx doctor` and `teamsfx logs` for middleware and runtime diagnostics.
- Validate Graph permission consent scope with `graph explorer` and admin consent.

## Integration Points

- Microsoft Graph API for provisioning Teams resources and membership.
- Azure Bot Service and Azure Functions for backend bot workflows.
- Adaptive Cards, Bot Framework SDK, and Microsoft Identity platform.
- Power Platform integration via Power Automate for workflow connectors.
- CI/CD pipelines (GitHub Actions, Azure DevOps) for Teams app package promotion.
