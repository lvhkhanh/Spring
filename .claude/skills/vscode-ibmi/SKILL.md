---
name: vscode-ibmi
description: '**WORKFLOW SKILL** — Configure, document, and troubleshoot VS Code extension workflows for IBM i development. USE FOR: Code for IBM i setup, RPGLE/CL/COBOL source editing, source physical files and IFS workflows, library lists, compile actions, SQL tools, object browsing, job log inspection, terminal commands, workspace settings, and team onboarding. DO NOT USE FOR: generic VS Code extension management unrelated to IBM i, z/OS mainframe development, or destructive IBM i commands without explicit approval. INVOKES: file system tools for workspace/settings files, terminal commands for local VS Code extension checks, and IBM i commands only when credentials/context are provided and actions are safe or explicitly approved.'
---

# VS Code IBM i Extensions Skill

## Overview

This skill supports VS Code-based IBM i development workflows. It focuses on the extensions, workspace settings, source organization, compile actions, and operational guardrails needed to work productively with RPGLE, CL, COBOL, SQL, DDS, source physical files, and IFS projects.

## Key Capabilities

### Extension Setup
- Recommend and document IBM i-focused VS Code extensions, especially Code for IBM i.
- Configure supporting language tooling for RPGLE, CL, COBOL, SQL, DDS, Git, YAML, and Markdown.
- Validate installed extensions with `code --list-extensions` when local VS Code CLI access is available.
- Create repeatable onboarding notes for team workspaces.

### Code for IBM i Workflow
- Configure connections without storing credentials in repo files.
- Define library lists, current library, object filters, source file filters, and IFS locations.
- Work with source physical files, members, stream files, and local Git-backed source.
- Set up Actions for compile, deploy, run SQL, inspect job logs, and open spool files.

### IBM i Development Support
- Support RPGLE, SQLRPGLE, CL, COBOL, DDS, DDL, and SQL script editing workflows.
- Explain compile commands such as `CRTBNDRPG`, `CRTRPGMOD`, `CRTBNDCL`, `CRTSQLRPGI`, and `RUNSQLSTM`.
- Map build actions to library/object naming conventions and environment-specific variables.
- Document authority requirements and safe operational boundaries.

### Troubleshooting
- Diagnose connection, SSH, library list, source member, compile, job log, CCSID, and object authority issues.
- Separate local VS Code problems from remote IBM i command or server configuration problems.
- Suggest read-only checks before changing remote objects.

## Usage Examples

### Team Setup Guide
```text
Create a VS Code setup guide for IBM i developers using Code for IBM i,
RPGLE, CL, SQL scripts, source physical files, compile actions, and Git.
```

### Compile Action Design
```text
Design Code for IBM i Actions for:
- deploy RPGLE source
- compile with CRTSQLRPGI
- show job log after failure
- run SQL validation query
Keep environment-specific values configurable.
```

### Troubleshoot Connection
```text
Troubleshoot why VS Code can connect over SSH but Code for IBM i cannot list libraries.
List safe checks for profile authority, library filters, and server jobs.
```

## Common Patterns

### Recommended Extension Areas
- IBM i connection and object/source browsing.
- RPGLE, CL, COBOL, DDS, SQL syntax support.
- Git, diff, Markdown, YAML, and shell tooling.
- Optional SQL client tooling for Db2 for i validation.

### Safe Action Workflow
1. Confirm target system, user profile, library, source file, member, and object name.
2. Use variables for environment-specific values.
3. Run read-only checks before compile or deploy actions.
4. Compile into a development library first.
5. Inspect job logs and spool files after failures.
6. Require approval before deleting, replacing, or changing production objects.

### Workspace Files
```json
{
  "files.associations": {
    "*.rpgle": "rpgle",
    "*.clle": "cl",
    "*.sqlrpgle": "rpgle",
    "*.dspf": "dds"
  }
}
```

## Best Practices

- Do not commit IBM i passwords, SSH keys, tokens, or personal connection profiles.
- Prefer individual developer profiles with least-privilege authority.
- Keep production libraries out of default compile/deploy actions.
- Store team-safe workspace settings in Git and personal connection settings outside Git.
- Make compile commands visible and reviewable instead of hiding them in undocumented tasks.
- Preserve source member metadata and CCSID assumptions in migration notes.
- Use Git-backed stream files where possible, and document when source physical files remain the system of record.

## Troubleshooting

### Extension Not Working
- Verify VS Code version and extension installation.
- Check whether the `code` CLI is available locally.
- Review extension output channels and developer tools logs.

### IBM i Connection Issues
- Confirm SSH is enabled and reachable.
- Verify user profile status, password expiration, and allowed sign-on methods.
- Check library/object authority and object filters.
- Confirm the extension is pointed at the expected system and environment.

### Compile Failures
- Inspect the job log and compiler listing.
- Verify library list, binding directory, service program, copybook/include paths, and source member name.
- Confirm CCSID and source type are correct.

## Integration Points

- **Code for IBM i**: connection, source browsing, Actions, object interaction.
- **IBM i Languages**: RPGLE, CL, COBOL, DDS, SQLRPGLE, DDL.
- **Db2 for i**: SQL validation and query workflows.
- **Git**: local source control, review, branching, and modernization history.
- **AI-Native Modernization**: migration briefs, generated prompts, characterization tests, and human review gates.
