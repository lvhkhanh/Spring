---
name: jira
description: '**WORKFLOW SKILL** — Create, manage, and automate Jira issues, projects, boards, workflows, and reports. USE FOR: issue creation and triage; workflow design; filter and dashboard setup; automation rules; JQL query writing; cross-team collaboration via Jira REST API and SDKs. DO NOT USE FOR: unrelated project management tools; deep product strategy; non-Jira incident handling. INVOKES: terminal for CLI operations, HTTP calls for Jira API, and file modifications for configs and scripts.'
---

# Jira Management Skill

## Overview

This skill provides full Jira workflow automation and guidance including issue lifecycle management, workflow design, board setup, and reporting. It supports both Jira Cloud and Jira Server/Data Center environments.

## Key Capabilities

### Issue Lifecycle
- Create, update, transition, and resolve Jira issues (bugs, tasks, stories, epics)
- Manage labels, components, priority, and custom fields
- Add and manage comments, watchers, and attachments
- Bulk issue operations and backlog grooming

### Project and Board Setup
- Create and configure Jira projects (software, business, service desk)
- Set up Scrum and Kanban boards with filters and columns
- Configure sprint planning and backlog refinement
- Manage versions, releases, and roadmaps

### Workflow and Automation
- Design and modify Jira workflows (statuses, transitions, conditions, validators, post-functions)
- Implement automation rules for issue updates, notifications, and escalations
- Enforce business rules with conditions and branching actions
- Configure permissions, issue security levels, and project roles

### Reporting and Dashboards
- Build JQL queries for advanced filtering
- Create dashboards and gadgets for status and cycle time reporting
- Generate sprint and release reports, burndown charts, and cumulative flow diagrams
- Monitor key metrics (lead time, cycle time, throughput)

## Usage Examples

### Create a Jira Issue Via API
```
Create Jira issue with:
- project key: PROJ
- issue type: Bug
- summary: "API failure in payment gateway"
- description: "Null pointer exception on /payments"
- priority: High
```

### Bulk Update Story Status
```
Find all stories in sprint 10 with status "In Progress" and move to "Code Review"
```

### Define Board Filter
```
Create filter for sprint work:
`project = PROJ AND sprint = 10 AND status in ("In Progress", "Code Review")`
```

## Common Patterns

### Issue Triaging
- Use severity, priority, and component tags for assignment
- Set automation to route issues to specific teams
- Apply consistent labels for root cause analysis

### Sprint Planning
- Use story points and capacity limits
- Prioritize by business value and risk
- Keep sprint scope stable and avoid carrying over too many items

### Workflow Governance
- Implement review and QA states
- Use conditions to prevent skipping mandatory approvals
- Add validators for required fields on transitions

## Best Practices

- Keep issue summaries concise and descriptive
- Use templates for issue creation (bug, task, improvement)
- Keep workflows simple and team-friendly
- Regularly clean up stale filters and dashboards
- Use integrations (Slack, email, CI/CD) for status updates
- Document custom fields and workflow conventions

## Troubleshooting

### Common Issues
- **Authentication failures**: verify API tokens / OAuth configs
- **Permission errors**: check project role and security level settings
- **JQL errors**: validate query syntax and field names
- **Transition failures**: check available transitions and required validators

### Validation Steps
1. Execute sample API call with curl or HTTP client
2. Confirm project and issue type availability
3. Inspect workflow transition screens for required fields
4. Review audit logs for automation rule execution
5. Validate dashboards and filters return expected results

## Integration Points

- **CI/CD**: GitHub Actions, GitLab CI, Jenkins
- **ChatOps**: Slack, Microsoft Teams
- **Dev tools**: Bitbucket, GitHub, Azure DevOps
- **Monitoring**: PagerDuty, Grafana, Datadog
- **Documentation**: Confluence, Google Docs
