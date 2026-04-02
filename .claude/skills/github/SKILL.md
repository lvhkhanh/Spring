---
name: github
description: '**WORKFLOW SKILL** — Design, manage, and troubleshoot GitHub-based collaboration, automation, and repository workflows. USE FOR: repositories, pull requests, issues, GitHub Actions, branch protection, release workflows, CODEOWNERS, templates, and GitHub CLI automation. DO NOT USE FOR: low-level git operations better handled by the git skill, non-GitHub hosting platforms, or generic coding tasks without repository workflow context. INVOKES: terminal commands for gh and git-adjacent operations, file system edits for workflow/config files, and semantic search for repository and automation patterns.'
---

# GitHub Skill

## Overview

This skill supports GitHub-centered development workflows across collaboration, automation, governance, and release management. Use it for repository setup, pull request workflows, issue and project hygiene, GitHub Actions, branch protection, templates, and GitHub CLI automation. It complements the `git` skill by focusing on GitHub as a platform rather than raw source control mechanics.

## Key Capabilities

### Repository Management
- Configure repositories, default branches, labels, templates, and contribution workflows
- Manage README, issue templates, pull request templates, CODEOWNERS, and repository settings
- Organize repository structure for onboarding, review, and automation clarity
- Support public, private, and organization-owned repository workflows

### Pull Requests & Code Review
- Create and refine pull request workflows with clear review expectations
- Improve PR descriptions, review checklists, linked issues, and merge strategies
- Use draft PRs, required reviews, status checks, and branch policies effectively
- Help structure smaller, easier-to-review changesets

### Issues, Projects, and Planning
- Create issue templates, labels, milestones, and triage workflows
- Connect issues, pull requests, releases, and projects for traceability
- Support backlog hygiene and team coordination patterns on GitHub
- Automate routine issue and PR lifecycle handling where appropriate

### GitHub Actions & Automation
- Create and troubleshoot GitHub Actions workflows for CI, CD, linting, testing, releases, and repo maintenance
- Use reusable workflows, matrices, caches, artifacts, and environment protections
- Manage secrets, variables, tokens, and permissions safely
- Improve workflow readability, reliability, and debuggability

### Governance & Security
- Configure branch protection, CODEOWNERS, required checks, and approval rules
- Integrate dependency updates, secret scanning, code scanning, and security policies
- Apply least-privilege permissions for workflows and automation tokens
- Support release tagging, changelog generation, and audit-friendly workflows

## Usage Examples

### Create a GitHub Actions CI workflow
```yaml
name: ci

on:
  pull_request:
  push:
    branches: [main]

jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-node@v4
        with:
          node-version: 20
          cache: npm
      - run: npm ci
      - run: npm test
```

### Create an issue with GitHub CLI
```bash
gh issue create \
  --title "Add health check endpoint" \
  --body "We need a lightweight /health endpoint for readiness checks." \
  --label enhancement
```

### Open a pull request with GitHub CLI
```bash
gh pr create \
  --title "Add health check endpoint" \
  --body "Implements a simple health endpoint and tests." \
  --base main
```

### Define CODEOWNERS
```text
* @platform-team
/docs/ @docs-team
/.github/workflows/ @devops-team
```

## Common Patterns

### Pull request hygiene
```text
1. Keep PRs focused
2. Link the relevant issue
3. Explain why the change exists
4. Note testing and rollout impact
5. Request the right reviewers
```

### Branch protection baseline
```text
- require pull requests before merge
- require status checks
- require up-to-date branches
- restrict direct pushes to protected branches
```

### Workflow layering
```text
- fast checks on pull request
- fuller validation on main
- release or deploy workflows on tags or protected branches
```

### Actions security pattern
```text
Prefer:
- least-privilege workflow permissions
- repository or environment secrets
- pinned actions when appropriate

Avoid:
- broad write permissions by default
- secrets echoed into logs
- unreviewed third-party actions with wide access
```

## Best Practices

- Keep repository automation explicit, reviewable, and version-controlled under `.github/`
- Use issue and PR templates to improve consistency without adding heavy process
- Prefer small PRs with clear context over large mixed-purpose changes
- Protect important branches with required checks and review rules
- Scope workflow permissions tightly and separate CI from deployment concerns where helpful
- Use reusable workflows or shared actions when duplication becomes real and stable
- Make releases traceable with tags, notes, and links to changes
- Treat GitHub configuration as part of the product delivery system, not an afterthought

## Troubleshooting

### PR or merge issues
- Check branch protection, required reviewers, required checks, and merge strategy settings
- Verify whether the PR branch is behind the base branch or blocked by CODEOWNERS
- Confirm whether the repo allows squash, merge, or rebase as expected

### GitHub Actions failures
- Inspect the first failing step and surrounding logs rather than only the final job status
- Check event triggers, path filters, permissions, secrets, caches, and runner environment differences
- Confirm whether the workflow is running on forked PRs with restricted token access

### Missing access or permission errors
- Verify repository role, organization policy, team membership, and token scopes
- Check whether environment protection rules or branch rules are blocking automation
- Distinguish user permissions from `GITHUB_TOKEN` or app installation permissions

### Automation drift
- Review duplicated workflows, stale templates, inconsistent labels, and outdated actions versions
- Standardize common repository patterns through templates or reusable workflows
- Keep docs, contribution guidance, and automation behavior aligned

## Integration Points

- GitHub repositories, pull requests, issues, discussions, releases, and projects
- GitHub Actions, reusable workflows, self-hosted runners, and repository environments
- GitHub CLI (`gh`) for automation and administration
- Security tooling such as Dependabot, secret scanning, and code scanning
- Git-based local workflows that feed into GitHub-hosted collaboration
