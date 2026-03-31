---
name: outlook
description: "**WORKFLOW SKILL** — Create, configure, and optimize Microsoft Outlook integrations and automation. USE FOR: building Outlook add-ins, managing email/message flows, calendar automation, and integrating Outlook with other tools. DO NOT USE FOR: unrelated messaging platforms; generic email handling outside Microsoft 365; backend-only services without Outlook context. INVOKES: file operations, API calls, and configuration updates."
---

# Outlook Skill

## Overview

This skill helps developers and automation engineers build and maintain Outlook solutions following Claude skill format. It covers Outlook add-ins, Office JavaScript API, Graph API mail/calendar operations, flows, and integration patterns.

## Key Capabilities

- Outlook add-in scaffolding (manifest, HTML/CSS/JS, task panes)
- Office JavaScript API usage (Mail, Calendar, Contacts, Tasks)
- Microsoft Graph API for send mail, events, attachments, and user settings
- OAuth 2.0 / OpenID Connect auth flows for delegated and app permissions
- Calendar automation: create/update/delete events, attendees, reminders
- Email automation: send, reply, forward, search, categorize, and flag
- Webhooks and change notifications for incoming mail and event updates
- Error handling, retry, throttling and compliance with Outlook service limits

## Usage Examples

1. Add-in scaffold and manifest

```json
{
  "manifestVersion": "1.1",
  "id": "{your-guid}",
  "version": "1.0.0.0",
  "providerName": "Your Company",
  "defaultLocale": "en-US",
  "name": {
    "short": "Outlook Helper",
    "long": "Outlook Helper Add-in"
  },
  "description": {
    "short": "Work with Outlook items.",
    "long": "A task pane add-in for automating Outlook actions."
  },
  "hosts": ["Mailbox"],
  "requirements": {"sets": [{"name": "Mailbox", "minVersion": "1.5"}]},
  "formSettings": {"form": "read"},
  "actions": [],
  "extensionPoint": {"type": "MessageReadCommandSurface"}
}
```

2. Office JS get current message subject

```javascript
office.context.mailbox.item.subject.getAsync((asyncResult) => {
  if (asyncResult.status === Office.AsyncResultStatus.Succeeded) {
    console.log('Subject:', asyncResult.value);
  }
});
```

3. Graph API send mail via REST

```http
POST https://graph.microsoft.com/v1.0/me/sendMail
Content-Type: application/json
Authorization: Bearer <token>

{
  "message": {
    "subject": "Hello from Claude skill",
    "body": {
      "contentType": "Text",
      "content": "Automated Outlook email from CI/CD."
    },
    "toRecipients": [
      {"emailAddress": {"address": "user@example.com"}}
    ]
  }
}
```

## Common Patterns

- Use Microsoft Authentication Library (MSAL) for acquiring tokens in add-ins and services
- Prefer Graph API over direct SMTP for Outlook/Exchange operations with modern auth
- Use deep link generation: `https://outlook.office.com/mail/deeplink?itemid=...`
- Sync local state with `delta` queries for mail, calendar and contacts updates
- Ensure timezone conversion with `startDateTime` and `endDateTime` in Graph events

## Best Practices

- Use minimal permission scopes (`Mail.ReadWrite`, `Calendars.ReadWrite`) and consent justification
- Avoid blocking UI thread in add-ins; offload long queries to async/await methods
- Refresh tokens and re-auth gracefully for long-lived sessions
- Validate and sanitize all user input before generating message content or events
- Log and profile API latency and throttling responses for operational visibility

## Troubleshooting

- `ErrorItemNotFound` on Graph event/item: ensure correct id, folder, and permissions
- `MailboxNotEnabledForRESTAPI` or `MailboxNotEnabled` for Office365: verify Exchange Online/Outlook setup
- Throttling status `429`: implement exponential backoff and resubmit
- Add-in loading failures: check manifest XML, type and IDs in AppSource/central deployment
- Authentication errors (`invalid_grant`, `unauthorized_client`): check redirect URLs and app registration

## Integration Points

- Microsoft 365 / Azure AD app registrations
- Outlook add-in manifest deployment to Exchange Admin Center
- Power Automate and Logic Apps with Outlook connectors
- Teams messaging extension and adaptive cards integration
- Azure Functions/Web APIs for event-driven email automation
