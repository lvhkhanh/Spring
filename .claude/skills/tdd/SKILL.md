---
name: tdd
description: '**WORKFLOW SKILL** — Plan and implement software using test-driven development (TDD). USE FOR: writing tests first, defining behavior through failing tests, implementing minimal code to pass tests, and iteratively refactoring while preserving behavior. DO NOT USE FOR: speculative coding without tests, skipping red-green-refactor cycles, or one-off scripts where test overhead is unnecessary. INVOKES: file system edits for test/code updates, terminal for test execution, semantic search for framework-specific test patterns.'
---

# Test-Driven Development Skill

## Overview

This skill provides structured support for test-driven development (TDD) across unit, integration, and API-level testing. It emphasizes the red-green-refactor cycle, behavior-focused test design, and maintainable test suites that improve confidence and development speed over time.

## Key Capabilities

### Red-Green-Refactor Workflow
- Translate requirements into small, testable increments
- Write a failing test first (`red`)
- Implement the minimum code needed to pass (`green`)
- Refactor code and tests safely while keeping all tests passing (`refactor`)

### Test Design
- Define tests around behavior and outcomes, not implementation details
- Create clear test names using scenario-based language
- Cover edge cases, invalid inputs, and error paths
- Use fixtures/factories to reduce duplication and improve readability

### Implementation Guidance
- Implement only what current tests require
- Avoid premature abstraction during early cycles
- Keep production code simple and explicit
- Preserve backward compatibility when evolving behavior

### Refactoring and Maintainability
- Refactor in small steps with fast feedback loops
- Remove duplicated logic in tests and production code
- Improve naming, structure, and modularity with confidence
- Keep test runtime fast and deterministic

### Quality and Coverage Strategy
- Build confidence with layered tests (unit, integration, end-to-end where needed)
- Identify gaps via failing scenarios before adding features
- Use coverage metrics as a guide, not a target
- Maintain regression tests for every fixed defect

## Usage Examples

### Start a New Feature with TDD
```
Implement a shopping cart discount feature using TDD:
- Write tests for percentage and fixed discounts
- Add edge-case tests for zero/negative values
- Implement minimal code to make tests pass
- Refactor pricing logic for readability
```

### Add Regression Protection for a Bug
```
A bug allows duplicate usernames during registration.
Use TDD to:
- Write a failing test reproducing the bug
- Implement the smallest fix
- Add validation tests for case-insensitive duplicates
```

### Refactor with Confidence
```
Refactor an order service to reduce complexity while preserving behavior:
- Capture current behavior with characterization tests
- Refactor in small steps
- Keep all tests passing after each change
```

## Common Patterns

### Core TDD Loop
```text
1. Pick the smallest behavior increment
2. Write one failing test
3. Make it pass with minimal code
4. Run full relevant test suite
5. Refactor safely
6. Repeat
```

### Good Test Naming Pattern
```text
should_<expected_behavior>_when_<context>
```

### Arrange-Act-Assert Structure
```text
Arrange: setup input, dependencies, and state
Act: execute one behavior
Assert: verify outcomes clearly and specifically
```

### Bugfix Pattern
```text
1. Reproduce the bug with a failing test
2. Apply the smallest production change
3. Confirm test passes
4. Add neighboring edge-case tests
5. Refactor if needed
```

## Best Practices

- Keep test cycles short; run targeted tests frequently
- Prefer deterministic tests; avoid time/network randomness unless controlled
- Mock only external boundaries (APIs, DB, filesystem), not core logic by default
- Ensure each test validates one behavior concern
- Use descriptive assertion messages for faster debugging
- Refactor tests as first-class code to maintain readability
- Commit in small increments aligned to test green states

## Troubleshooting

### Tests Are Slow
- Reduce expensive setup and teardown
- Isolate unit tests from integration concerns
- Run focused subsets locally, full suite in CI

### Flaky Tests
- Remove hidden async race conditions
- Control time, randomness, and external dependencies
- Enforce stable test data and execution order independence

### Over-Mocked Tests
- Replace deep internal mocks with behavior-driven tests
- Prefer real collaborators for simple in-memory components
- Mock at system boundaries only

### Hard-to-Test Code
- Refactor for dependency injection and smaller functions
- Separate pure logic from I/O concerns
- Add seams around side effects before extending features

## Integration Points

- **Unit test frameworks**: Jest, Vitest, JUnit, pytest, NUnit
- **Integration testing**: Testcontainers, Supertest, REST Assured
- **Coverage tools**: Istanbul/nyc, JaCoCo, coverage.py
- **CI/CD**: GitHub Actions, GitLab CI, Jenkins
- **Quality gates**: SonarQube, branch protection with test checks
