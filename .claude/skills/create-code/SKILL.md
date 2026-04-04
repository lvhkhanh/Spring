---
name: create-code
description: '**WORKFLOW SKILL** — Create new code or extend existing implementations with minimal churn and clear validation. USE FOR: building features, adding endpoints, creating components, writing utilities, scaffolding modules, and adding tests that should end in concrete code changes. DO NOT USE FOR: review-only requests, pure explanation, broad architecture brainstorming without implementation, or formatting-only edits. INVOKES: file system edits for implementation, terminal for focused verification, and local code search for matching patterns.'
---

# Create Code Skill

## Overview

This skill helps turn implementation requests into small, production-ready code changes that fit the existing codebase. It emphasizes local pattern matching, narrow scope, practical validation, and reviewable diffs over speculative rewrites.

## Key Capabilities

### Feature Implementation
- Add new behavior to existing modules, services, routes, or components
- Complete TODOs and partially implemented flows
- Build thin end-to-end slices before expanding scope
- Keep public interfaces stable unless the requested behavior requires change

### New Code Scaffolding
- Create focused utilities, helpers, classes, hooks, or components
- Mirror nearby naming, folder layout, and dependency patterns
- Introduce only the files needed for the requested outcome
- Avoid over-abstraction in first-pass implementations

### Test-Aware Development
- Add targeted tests when similar tests already exist nearby
- Extend existing test suites before creating new structures
- Protect logic-heavy changes with focused verification
- Call out gaps clearly when validation cannot run

### Low-Churn Refactoring While Implementing
- Reuse existing helpers before creating new ones
- Make the smallest viable change set
- Avoid unrelated cleanup mixed into feature work
- Preserve established conventions even when multiple valid styles exist

## Workflow

### 1. Clarify the implementation target
- Identify the exact behavior the user wants
- Translate vague requests into a concrete deliverable
- Choose the smallest sensible slice that satisfies the request
- Make a reasonable assumption if ambiguity is minor and low-risk

### 2. Study the local code path
- Find adjacent files, tests, types, and entry points
- Follow existing patterns for naming, structure, and error handling
- Check whether a similar implementation already exists
- Prefer extension over invention

### 3. Implement with minimal churn
- Edit the narrowest set of files possible
- Keep logic close to where it belongs
- Add short comments only when the code would otherwise be hard to parse
- Avoid speculative abstractions and broad rewrites

### 4. Validate narrowly
- Run focused tests for the touched area
- Run lint or type checks when interfaces changed
- Use a quick smoke check when automation is unavailable
- Report exactly what was and was not verified

### 5. Close with clear reporting
- Summarize the behavior added or changed
- Mention files affected
- Note validation performed
- Surface assumptions or residual risk briefly

## Usage Examples

### Add a new API endpoint
```text
Create a new endpoint to return active customers only.
Follow the existing controller/service/repository pattern and add focused tests.
```

### Build a UI component
```text
Create a reusable settings panel component that matches the existing design system.
Include loading and empty states if the surrounding pages use them.
```

### Add a utility
```text
Write a utility to parse CSV rows into our internal order model.
Keep it small, typed, and covered with unit tests.
```

### Complete existing code
```text
Finish this partially implemented sync flow using the same patterns as the other background jobs.
Validate only the impacted tests.
```

## Common Patterns

### Smallest Useful Slice
```text
1. Find the entry point
2. Implement one behavior end to end
3. Verify that slice
4. Expand only if needed
```

### Match Local Conventions
```text
Prefer the project's existing:
- file layout
- naming style
- helper usage
- test structure
- error handling approach
```

### Implementation Checklist
```text
- behavior is concrete
- file scope is narrow
- existing helpers were considered
- tests were added or updated when appropriate
- validation was run where possible
```

## Best Practices

- Prefer additive changes over rewrites
- Reuse stable project patterns before introducing new abstractions
- Keep new APIs as small as possible
- Write code that is easy to review in one pass
- Add tests for behavior risk, not just for coverage optics
- Preserve unrelated user changes in the worktree
- Stop once the request is satisfied cleanly

## Troubleshooting

### The request is underspecified
- Infer intent from nearby code and the user's wording
- Choose the safest low-churn interpretation
- Only pause for clarification when different options would materially change behavior or architecture

### The codebase has multiple patterns
- Follow the most local pattern around the touched files
- Prefer consistency with the current feature area over global idealism
- Avoid introducing a third style

### Validation is expensive or unavailable
- Run the narrowest relevant checks
- Explain what could not be verified
- Keep the change especially small when feedback is limited

### The change tempts a large refactor
- Deliver the requested behavior first
- Refactor only the code directly blocking the implementation
- Leave broader cleanup for a separate task

## Integration Points

- Local code search to find matching implementations
- Existing tests, linters, and type checkers for targeted validation
- Adjacent skills such as `clean-code`, `tdd`, or stack-specific skills when the request needs deeper guidance in those areas
