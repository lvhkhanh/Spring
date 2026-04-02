---
name: clean-code
description: '**WORKFLOW SKILL** — Improve code readability, maintainability, and design quality through clean code principles. USE FOR: refactoring confusing code, improving naming, reducing duplication, simplifying functions and classes, clarifying boundaries, and making code easier to understand and change. DO NOT USE FOR: purely cosmetic formatting-only changes, premature abstraction without evidence, or style-guide enforcement detached from maintainability outcomes. INVOKES: file system edits for refactors, terminal for tests and linters, and semantic search for related code paths.'
---

# Clean Code Skill

## Overview

This skill helps improve code quality through readability, simplicity, cohesion, and maintainability. It is for refactoring existing code or shaping new code so that future changes are safer, faster, and easier to understand. The focus is practical clean code, not dogma: optimize for clarity, correct behavior, and changeability.

## Key Capabilities

### Readability & Naming
- Replace vague names with intent-revealing names for variables, functions, classes, and files
- Remove misleading terminology, overloaded names, and unnecessary abbreviations
- Align names with domain language and actual behavior
- Simplify control flow so the main path is easy to follow

### Function & Class Design
- Break down long functions into coherent units with single, clear responsibilities
- Reduce argument complexity and improve parameter meaning
- Separate orchestration from business logic and isolate side effects
- Improve class cohesion and reduce responsibility overlap between modules

### Duplication & Abstraction
- Identify harmful duplication in logic, validation, branching, and data shaping
- Extract shared concepts only when duplication is stable and meaningful
- Avoid speculative abstractions and indirection without concrete payoff
- Consolidate repeated conditionals and error-handling patterns thoughtfully

### Error Handling & Boundaries
- Make failure paths explicit and easier to reason about
- Normalize validation, guard clauses, and error propagation
- Clarify API boundaries, input contracts, and module responsibilities
- Reduce hidden coupling between layers or services

### Safe Refactoring Workflow
- Refactor in behavior-preserving steps with tests or verification at each stage
- Improve structure without mixing unrelated feature work
- Add characterization tests before risky refactors when current behavior is unclear
- Leave the codebase simpler than it was found

## Usage Examples

### Refactor a long service method
```
Refactor this 120-line service method to:
- clarify the happy path
- extract validation and mapping helpers
- improve naming
- preserve behavior with tests
```

### Clean up duplicated business rules
```
Identify duplicated discount-calculation logic across controllers and services.
Extract the right shared abstraction without overengineering it.
```

### Improve code review quality
```
Review this change for clean code issues:
- confusing names
- mixed responsibilities
- duplicated logic
- unnecessary abstraction
```

## Common Patterns

### Guard clauses over deep nesting
```text
Prefer:
1. Validate preconditions early
2. Return or fail fast
3. Keep the main path shallow and readable
```

### Extract by responsibility, not by line count
```text
Good extraction:
- validation
- mapping
- policy decision
- persistence boundary

Bad extraction:
- arbitrary chunks with unclear names
```

### Name by intent
```text
Prefer:
- `calculateInvoiceTotal`
- `isEligibleForUpgrade`
- `loadCustomerProfile`

Avoid:
- `doStuff`
- `handleData`
- `process`
```

### Refactor loop
```text
1. Understand current behavior
2. Add or run tests
3. Make one structural improvement
4. Re-run verification
5. Repeat
```

## Best Practices

- Prefer clarity over cleverness
- Keep units of code small enough to understand in one pass
- Use consistent domain language across files and layers
- Separate decision-making logic from I/O and framework glue
- Reduce boolean flags and ambiguous parameter lists where possible
- Make illegal states harder to represent through better modeling
- Refactor opportunistically, but keep changes scoped and behavior-preserving
- Stop abstracting when the simpler code is already clear enough

## Troubleshooting

### Code is hard to understand
- Look for mixed levels of abstraction within the same function
- Rename variables and helpers to expose intent before larger restructuring
- Separate setup, decision logic, and side effects

### Refactor risk feels high
- Add characterization tests around current behavior first
- Change one concept at a time instead of rewriting whole modules
- Prefer incremental extractions over large structural jumps

### Too much abstraction
- Inline wrappers that add no meaning
- Remove generic helpers that obscure domain behavior
- Keep abstractions only when they simplify multiple concrete use cases

### Duplication keeps returning
- Check whether the repeated code is actually the same concept
- Extract stable business rules, not accidental syntax similarity
- Centralize shared logic at the layer where it naturally belongs

## Integration Points

- Unit and integration tests for safe refactoring
- Linters and static analysis for spotting complexity and duplication
- Code review workflows focused on readability and maintainability
- Architecture and domain modeling practices that shape clean boundaries
- Existing language/framework conventions in the target codebase
