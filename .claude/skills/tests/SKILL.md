---
name: tests
description: '**WORKFLOW SKILL** — Design, write, organize, and validate automated tests across application and library projects. USE FOR: creating unit, integration, UI, API, and regression tests; improving test coverage; choosing testing boundaries; organizing fixtures, helpers, and mocks; and building maintainable test suites that support confident delivery. DO NOT USE FOR: replacing product requirements with speculative tests, adding low-value coverage that duplicates behavior without signal, or using tests as a substitute for debugging root causes when failures need targeted investigation. INVOKES: file system tools for test and config files, terminal for test runner execution, semantic search for framework-specific testing patterns.'
---

# Software Testing Skill

## Overview

This skill provides structured support for building and maintaining automated tests across unit, integration, UI, API, and regression layers. It helps choose the right test type for a given behavior, author clear and maintainable test cases, organize supporting test utilities, and validate that tests provide real confidence instead of brittle or redundant coverage.

## Key Capabilities

### Test Planning and Strategy
- Choose appropriate test levels for a feature, bugfix, or refactor
- Identify critical paths, edge cases, error handling, and contract boundaries
- Balance unit, integration, and end-to-end coverage based on risk and cost
- Define what should be tested directly versus indirectly through higher-level flows

### Test Authoring
- Write unit, integration, API, UI, and regression tests
- Express behavior clearly through focused scenarios and assertions
- Cover success paths, failure paths, edge cases, and state transitions
- Adapt tests to JavaScript, TypeScript, Java, Python, .NET, and similar stacks

### Test Organization and Reuse
- Structure test files, suites, fixtures, factories, and helper utilities
- Create reusable setup helpers without hiding important behavior
- Decide when to use mocks, stubs, fakes, or real collaborators
- Keep test data readable and close to the scenarios it supports

### Quality and Signal Improvement
- Replace brittle assertions with more behavior-focused checks
- Reduce duplicated test logic and oversized test files
- Improve suite readability, determinism, and diagnostic value
- Use coverage as a guide to find risk gaps, not as a vanity target

### Validation and Execution
- Run targeted tests during development and broader suites before handoff
- Verify that new tests fail for the right reason before implementation changes when appropriate
- Confirm that tests pass consistently in local and CI-like environments
- Identify when gaps remain even after the immediate suite is green

## Usage Examples

### Add Tests for a New Feature
```
Create tests for a new order cancellation workflow.
Cover happy path, invalid status transitions, authorization rules,
and the audit event emitted after a successful cancellation.
```

### Add Regression Coverage for a Bug
```
Write regression tests for a bug where duplicate form submissions
create multiple invoices under slow network conditions.
```

### Improve an Existing Test Suite
```
Review this test file and refactor it to reduce duplication,
clarify scenario names, and replace brittle implementation-detail assertions.
```

### Choose the Right Test Layer
```
For this authentication feature, recommend which behaviors should be covered
by unit tests, integration tests, and end-to-end tests, and then implement them.
```

## Common Patterns

### Test Pyramid Heuristic
```text
- More fast unit tests around pure logic and local behavior
- Fewer integration tests around boundaries and collaboration
- Selective end-to-end tests for critical user journeys
```

### Arrange-Act-Assert Structure
```text
Arrange: prepare inputs, dependencies, and state
Act: execute one behavior
Assert: verify observable outcomes
```

### Regression Test Pattern
```text
1. Reproduce the bug with a focused failing test
2. Confirm the failure matches the reported behavior
3. Apply the fix
4. Re-run the targeted and neighboring tests
```

### Mocking Decision Pattern
```text
Use mocks for slow or external boundaries such as APIs, databases, queues, and filesystems.
Prefer real in-memory collaborators for core business logic when they improve confidence.
Avoid mocking internal details that make refactors unnecessarily painful.
```

## Best Practices

- Write tests around behavior and contracts, not private implementation details
- Keep each test focused on one clear scenario
- Prefer deterministic data and controlled environments over timing-sensitive assertions
- Name tests so failures are easy to understand without opening the file
- Keep shared helpers small and explicit to avoid hidden coupling
- Add regression tests for every real defect that was fixed
- Revisit test scope when a suite is slow, flaky, or hard to maintain

## Troubleshooting

### Tests Are Hard to Read
- Split large suites into smaller behavior-focused groups
- Replace generic fixtures with scenario-specific builders or helpers
- Simplify setup so the intent of each case is visible

### Coverage Is High but Confidence Is Low
- Check whether assertions validate meaningful outcomes
- Add tests around failure modes, boundaries, and important business rules
- Remove or rewrite tests that only mirror implementation steps

### Tests Are Slow
- Move pure logic checks into unit tests
- Reduce expensive integration setup where lower layers are sufficient
- Run focused subsets locally and reserve full suites for broader validation

### Tests Are Brittle
- Stop asserting transient details such as internal call order unless it is contractually important
- Use stable selectors and observable outputs in UI tests
- Reduce shared mutable state, over-mocking, and hidden global setup

## Integration Points

- **Test runners**: Jest, Vitest, pytest, JUnit, NUnit
- **UI testing**: React Testing Library, Cypress, Playwright
- **API and service testing**: Supertest, REST Assured, Postman collections
- **Supporting tools**: fixtures, factories, mock servers, coverage tools
- **Delivery workflows**: CI pipelines, regression gates, pre-merge validation
