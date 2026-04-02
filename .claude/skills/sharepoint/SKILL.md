---
name: sharepoint
description: "**WORKFLOW SKILL** — Design, build, configure, and troubleshoot Microsoft SharePoint solutions and automations. USE FOR: SharePoint Online sites, lists, document libraries, permissions, SPFx development, Graph/REST integrations, content operations, and tenant-aware automation. DO NOT USE FOR: unrelated CMS platforms, generic file storage without SharePoint context, or non-Microsoft collaboration tooling. INVOKES: file operations, API calls, PowerShell or CLI workflows, and configuration updates."
---

# SharePoint Skill

## Overview

This skill covers SharePoint Online development, administration, automation, and integration workflows. Use it for modern SharePoint sites, document libraries, lists, permissions, SPFx components, Microsoft Graph and SharePoint REST APIs, and Microsoft 365 content automation patterns.

## Key Capabilities

- Create and configure SharePoint Online sites, pages, lists, libraries, columns, views, and content types.
- Build SharePoint Framework (SPFx) web parts, extensions, command sets, and solution packages.
- Automate SharePoint operations with Microsoft Graph, SharePoint REST API, PnP PowerShell, and CLI for Microsoft 365.
- Manage permissions, groups, inheritance, sharing links, and site access governance.
- Handle document management workflows including metadata, versioning, approvals, and retention-aware processes.
- Integrate SharePoint with Power Automate, Teams, Outlook, Azure, and Microsoft 365 identity.
- Troubleshoot site provisioning, authentication, throttling, permissions, and content access issues.

## Usage Examples

1. Create an SPFx web part

```bash
npm install -g yo gulp @microsoft/generator-sharepoint
yo @microsoft/sharepoint
gulp serve
```

2. Connect with PnP PowerShell

```powershell
Connect-PnPOnline -Url https://contoso.sharepoint.com/sites/ProjectA -Interactive
Get-PnPList
Get-PnPWeb
```

3. Create a list item using Microsoft Graph

```http
POST https://graph.microsoft.com/v1.0/sites/{site-id}/lists/{list-id}/items
Content-Type: application/json
Authorization: Bearer <token>

{
  "fields": {
    "Title": "New item from automation",
    "Status": "Open"
  }
}
```

4. Query files in a document library with SharePoint REST

```http
GET https://contoso.sharepoint.com/sites/ProjectA/_api/web/lists/GetByTitle('Documents')/items?$select=Id,Title,FileLeafRef
Accept: application/json;odata=nometadata
Authorization: Bearer <token>
```

## Common Patterns

- Use Microsoft Graph for tenant-aligned integrations when supported; fall back to SharePoint REST for SharePoint-specific features not exposed in Graph.
- Model document libraries with explicit metadata, content types, and views rather than folder-only organization.
- Use PnP PowerShell or CLI for Microsoft 365 for repeatable admin and provisioning tasks.
- Keep SPFx solutions scoped and modular; isolate web parts, extensions, and shared services cleanly.
- Preserve permission inheritance unless the business case clearly requires item- or library-level breaks.
- Treat site URLs, list IDs, drive IDs, and page names as configuration, not hardcoded constants.

## Best Practices

- Prefer SharePoint Online modern experiences and supported APIs over legacy customization patterns.
- Use least-privilege Graph or SharePoint permissions and document app consent requirements clearly.
- Validate internal names for columns and fields before building automation against them.
- Use metadata, content types, versioning, and retention labels intentionally for document-heavy solutions.
- Package SPFx solutions with predictable environments and avoid tenant-wide deployment unless needed.
- Design flows and scripts to handle throttling, pagination, large libraries, and eventual consistency.
- Keep site structure, list schema, and permission model explicit in code or provisioning scripts.

## Troubleshooting

- Authentication failures: verify Azure AD app registration, delegated vs application permissions, tenant consent, and site-level access.
- `403` or access denied: check site permissions, broken inheritance, sharing link scope, and whether the app principal has been granted access.
- Missing fields or bad updates: confirm SharePoint internal field names, content type requirements, and column validation rules.
- Large list or library issues: review indexing, view thresholds, pagination, and query filters.
- SPFx runtime issues: verify Node.js version compatibility, package versions, local workbench config, and tenant app catalog deployment.
- API inconsistencies: confirm whether the operation is better supported by Graph, SharePoint REST, or PnP abstractions.

## Integration Points

- SharePoint Online sites, lists, libraries, pages, and app catalogs
- Microsoft Graph API and SharePoint REST API
- SharePoint Framework (SPFx), React-based web parts, and extensions
- PnP PowerShell and CLI for Microsoft 365 automation
- Power Automate, Teams, Outlook, and Azure-hosted supporting services
