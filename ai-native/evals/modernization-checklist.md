# Modernization Evaluation Checklist

Use this checklist before accepting AI-generated modernization work.

## Behavior Preservation

- [ ] Program purpose matches the legacy source.
- [ ] Inputs are mapped correctly.
- [ ] Outputs are mapped correctly.
- [ ] Business rules are preserved.
- [ ] Calculations preserve precision, rounding, and overflow behavior.
- [ ] Branching behavior matches legacy conditions.
- [ ] Loop behavior matches legacy iteration and termination rules.
- [ ] Error and not-found behavior is preserved.
- [ ] Batch vs interactive behavior is correctly modeled.

## Data And DB2

- [ ] DB2 tables/files are identified.
- [ ] Primary keys and lookup paths are preserved.
- [ ] SQL behavior is equivalent.
- [ ] Null, blank, zero, and default values are handled correctly.
- [ ] Transactions are defined explicitly.
- [ ] Read-only and write operations are separated.
- [ ] Schema assumptions are documented.

## Architecture

- [ ] Business logic is separated from I/O.
- [ ] Domain model names reflect business concepts.
- [ ] Service boundaries are small enough to test.
- [ ] Repository abstractions map cleanly to DB2/file access.
- [ ] API/UI flow matches the original user or job workflow.
- [ ] Unknowns are marked as TODOs with context.

## Tests

- [ ] Characterization tests exist before refactoring.
- [ ] Happy path tests are included.
- [ ] Boundary cases are included.
- [ ] Invalid input cases are included.
- [ ] Empty result/not found cases are included.
- [ ] DB2 failure or unavailable cases are included when relevant.
- [ ] Tests compare expected legacy outputs to modern outputs.

## AI Safety And Governance

- [ ] No secrets are included in prompts, logs, or generated files.
- [ ] Generated code does not bypass authorization.
- [ ] Database writes require explicit user action.
- [ ] Tool calls are auditable.
- [ ] Prompt assumptions are documented.
- [ ] A human owner reviewed the final modernization decision.
