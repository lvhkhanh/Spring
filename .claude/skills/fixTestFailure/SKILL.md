---
name: fixTestFailure
description: '**WORKFLOW SKILL** — Diagnose and fix failing automated tests with minimal, behavior-preserving changes. USE FOR: investigating unit, integration, UI, and API test failures; isolating root causes in test code, fixtures, configuration, mocks, and production behavior; stabilizing flaky tests; and restoring passing test suites with clear validation steps. DO NOT USE FOR: bypassing legitimate failures by weakening assertions without cause, masking regressions with broad skips, or making unrelated refactors while debugging tests. INVOKES: file system tools for test and source updates, terminal for targeted test execution, semantic search for framework-specific failure patterns.'
---

# Test Failure Fix Skill

## Overview

This skill provides structured support for diagnosing and fixing broken tests across application and library projects. It focuses on reproducing failures, narrowing the cause, deciding whether the defect is in the test or the implementation, applying the smallest safe correction, and validating that the fix resolves the issue without hiding regressions.

## Key Capabilities

### Failure Reproduction and Triage
- Reproduce failing tests with targeted commands and clear scope
- Read failure output, stack traces, snapshots, and assertion diffs
- Distinguish deterministic failures from flaky or environment-specific behavior
- Prioritize the first meaningful failure when cascading errors obscure root cause

### Root Cause Analysis
- Determine whether the failure comes from production code, test code, fixtures, mocks, setup, or configuration
- Trace recent behavior changes that invalidated previous expectations
- Identify async timing issues, data leakage, order dependence, and environment mismatches
- Separate legitimate regression signals from brittle or outdated assertions

### Minimal Safe Repair
- Fix the smallest layer that is actually wrong
- Update tests when behavior intentionally changed and expectations are stale
- Update implementation when tests correctly expose a defect
- Preserve test intent while improving readability and reliability

### Flaky Test Stabilization
- Diagnose failures caused by time, randomness, shared state, race conditions, or network dependence
- Add cleanup, synchronization, retries only where justified, and stronger deterministic controls
- Replace hidden implicit waits with explicit stable conditions
- Reduce over-mocking or brittle snapshot dependence when they drive noise

### Validation and Regression Protection
- Re-run the narrow failing test first, then the relevant surrounding suite
- Check for neighboring scenarios that may also need coverage
- Preserve meaningful assertions so the fix continues to guard real behavior
- Document assumptions and any remaining risk when a failure cannot be fully validated locally

## Usage Examples

### Fix a Broken Unit Test
```
This Jest test started failing after a refactor.
Find the root cause, decide whether the bug is in the code or the test,
apply the smallest fix, and rerun the relevant tests.
```

### Stabilize a Flaky UI Test
```
Our React Testing Library test fails intermittently in CI but passes locally.
Investigate timing, cleanup, and mock behavior, then make it deterministic.
```

### Repair Snapshot or Contract Drift
```
These snapshot and API contract tests broke after a deliberate behavior change.
Update only the expectations that are genuinely outdated and keep regression value.
```

### Debug Test Environment Failures
```
Vitest is failing because browser APIs and setup behavior differ from production.
Trace whether the issue belongs in test setup, mocks, config, or the component code.
```

## Common Patterns

### Failure-Fix Loop
```text
1. Reproduce one failing test with the smallest command possible
2. Read the assertion and stack trace carefully
3. Identify whether the defect is in code, test, setup, or config
4. Apply the smallest justified change
5. Re-run the failing test
6. Re-run the relevant suite to check for regressions
```

### Test vs Implementation Decision
```text
Fix the test when:
- expected behavior changed intentionally
- the assertion is brittle or outdated
- fixtures or mocks no longer represent real usage

Fix the implementation when:
- the test still reflects correct business behavior
- the regression breaks a supported contract
- the failure exposes missing edge-case handling
```

### Flaky Test Checklist
```text
- Control time, randomness, and async completion
- Reset mocks and shared state between tests
- Remove order dependence
- Avoid hidden network or filesystem coupling
- Wait for observable outcomes, not arbitrary delays
```

## Best Practices

- Start with the narrowest reproducible failure before touching code
- Avoid weakening assertions unless they are genuinely too specific or incorrect
- Keep fixes small and local until the root cause is proven
- Prefer deterministic setup over retries or sleeps
- Treat test code as production-quality code that deserves clarity
- Add or refine regression coverage when the failure exposed a real bug
- Re-check related tests when shared helpers, fixtures, or setup files change

## Troubleshooting

### Tests Fail Only in CI
- Compare environment variables, timing, filesystem assumptions, and concurrency behavior
- Check for reliance on local state, cached artifacts, or implicit ordering
- Confirm the same test command and config are being exercised locally

### Assertion Looks Wrong but Code Also Changed
- Validate current product behavior and intended contract first
- Update the test only if the new behavior is deliberate and approved
- Fix the implementation if the behavior drift is unintended

### Snapshot Failures Are Noisy
- Inspect the semantic change instead of blindly updating snapshots
- Replace oversized snapshots with focused assertions when possible
- Keep snapshots only where they meaningfully protect output structure

### Many Tests Fail at Once
- Start with the earliest or most foundational failure
- Check shared setup, providers, fixtures, environment config, and common utilities
- Fix the common root cause before chasing downstream breakage

## Integration Points

- **Test runners**: Jest, Vitest, pytest, JUnit, NUnit
- **UI testing**: React Testing Library, Cypress, Playwright
- **Service/API testing**: Supertest, REST Assured, Postman collections
- **Shared infrastructure**: setup files, mock servers, fixtures, factories, CI pipelines
- **Quality workflows**: regression validation, flaky-test triage, pre-merge checks
