---
name: save-token
description: '**WORKFLOW SKILL** — Reduce token usage while preserving correctness, context, and user trust. USE FOR: long-running coding sessions, repository exploration, large-file analysis, summarization, prompt compression, minimizing repeated context, and producing concise final answers. DO NOT USE FOR: tasks that require exhaustive legal, medical, security, or financial detail; user requests for full verbatim content; or situations where brevity would hide important risk. INVOKES: file system tools for targeted inspection, terminal for scoped searches, semantic search for focused context retrieval.'
---

# Save Token Skill

## Overview

This skill helps Claude work efficiently in token-sensitive tasks. It focuses on gathering only the context needed, summarizing aggressively but accurately, avoiding repeated information, and producing compact outputs that still contain decisions, evidence, and next actions.

## Key Capabilities

### Context Triage
- Identify the minimum files, commands, logs, or messages needed to answer the request
- Prefer targeted search over broad file reads
- Read only relevant ranges of large files when possible
- Stop exploration once the decision or implementation path is clear

### Concise Reasoning
- Keep internal reasoning focused on high-signal facts and constraints
- Collapse repeated evidence into one clear statement
- Track assumptions explicitly instead of restating background
- Use short plans only when they materially reduce risk

### Output Compression
- Answer in the smallest format that satisfies the user
- Prefer direct prose for simple tasks and short bullets for multi-part results
- Include only the commands, paths, errors, and decisions the user needs
- Avoid long preambles, generic best practices, and repeated summaries

### Long-Session Management
- Summarize completed work before moving into a new phase
- Preserve key facts: user goal, files changed, commands run, failing tests, blockers, and decisions
- Replace stale details with current state when the task evolves
- Reuse prior findings instead of rediscovering the same context

### Large Content Handling
- Summarize large files, logs, diffs, or documents instead of copying them wholesale
- Extract representative snippets only when exact wording matters
- Use line references or section names to anchor claims
- Ask for narrowing only when the scope cannot be reduced safely

## Usage Examples

### Repository Investigation
```
Find the cause of this bug, but keep the investigation lightweight.
Search for the relevant handler and inspect only the code paths needed.
```

### Long Log Review
```
Review this 5,000-line error log and tell me the likely root cause.
Do not paste the full log back.
```

### Compact Final Response
```
Summarize what changed and what was verified in under 8 bullets.
```

### Prompt Compression
```
Condense this agent instruction into a shorter version while preserving behavior.
```

## Common Patterns

### Minimal Context Flow
```text
1. Restate the target outcome in one sentence
2. Search for exact symbols, files, routes, or error strings
3. Read only the most relevant file ranges
4. Decide whether enough context exists to act
5. Implement or answer with concise evidence
6. Verify only the affected behavior
```

### Compact Status Update
```text
Done: changed X.
Checked: ran Y.
Remaining: Z, if any.
```

### Large File Strategy
```text
For large files:
- scan structure first
- jump to relevant headings, symbols, or errors
- summarize irrelevant sections as omitted
- quote only small fragments needed for precision
```

### Final Answer Shape
```text
For simple work:
"Done. I changed <file/path> to <effect>. Verified with <command>."

For larger work:
- Changed: <high-signal change>
- Verified: <command/result>
- Notes: <blocker or follow-up only if relevant>
```

## Best Practices

- Use `rg` or semantic search before opening many files
- Prefer `sed -n` or editor ranges over whole-file reads for large files
- Keep progress updates short and tied to current findings
- De-duplicate repeated errors, stack frames, and test output
- Preserve exact names, paths, versions, and commands when they matter
- Keep final answers focused on outcome, verification, and residual risk
- Mention uncertainty directly instead of padding with broad caveats
- Do not omit important warnings just to be shorter

## Troubleshooting

### Context Is Too Large
- Identify the user's immediate decision or deliverable
- Filter by file type, symbol, timestamp, or error text
- Read summaries, indexes, headings, or tests before implementation files
- Capture a short state summary before continuing

### Answer Became Too Sparse
- Add the missing evidence: file path, command result, or concrete reason
- Restore any caveat that changes user action
- Include the smallest useful example or snippet

### Exploration Is Repeating
- Stop and list what is already known
- Compare new searches against prior findings
- Move to implementation, verification, or a focused question

### User Requested Detail
- Follow the requested depth
- Keep structure compact
- Use references instead of reproducing large content

## Integration Points

- **Coding workflows**: scoped repository search, concise patches, focused tests
- **Debugging**: compact reproduction notes, deduplicated errors, root-cause summaries
- **Documentation**: compressed runbooks, migration notes, handoff summaries
- **Agent workflows**: context compaction, prompt reduction, progress reporting
- **Review workflows**: findings-first reviews with only relevant evidence
