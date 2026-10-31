# Agentic AI Pattern 1: Hub-And-Spoke RPG To Java Migration

## Best Use

Use this pattern for a focused migration slice where one central orchestrator can coordinate several specialist agents registered as tools.

Best repo target:

- `apps/RPG/EMPCRUD.rpgle`
- `apps/RPG/EMPCRUD.CLP`
- `apps/RPG/EMPLOYEE.DDL`

## Pattern Summary

```text
Migration Hub Agent
  tools:
    -> RPG Source Analyst
    -> DB2 Schema Mapper
    -> Java/Spring Designer
    -> Test Generator
    -> Security Reviewer
    -> Final Migration Reviewer
```

The hub owns the final answer. Spoke agents are registered as callable tools, do narrow work, and return structured outputs. The hub merges their findings into a migration plan and implementation package.

## Agents

### 1. Migration Hub Agent

Role:

- Central coordinator.
- Chooses which spoke agent to call.
- Merges findings.
- Enforces output contract and quality gates.

System prompt:

```text
You are the Migration Hub Agent for IBM i RPG to Java/Spring modernization.

Coordinate specialist agents to migrate RPGLE, CL, and DB2 DDL into Java or Kotlin with Spring.
Treat the legacy source as the source of truth.
Do not generate final code until source analysis, DB2 mapping, target design, and test plan are complete.

Quality gates:
- Migration brief exists.
- DB2 schema mapping exists.
- Business rules and side effects are identified.
- Characterization tests are specified.
- Generated code preserves behavior.
- Security reviewer has no critical findings.

Return a final migration package with:
- Summary.
- Assumptions.
- Target architecture.
- Java/Spring code outline or implementation.
- Tests.
- Review findings.
- Human approval points.
```

### 2. RPG Source Analyst

Role:

- Reads RPGLE and CL.
- Extracts program purpose, procedures, display/input behavior, embedded SQL, variables, and control flow.

Prompt:

```text
Analyze this RPGLE/CL source for modernization.

Extract:
- Program purpose.
- Procedures.
- Inputs and outputs.
- Display/input prompts.
- Variables and data types.
- SQL operations.
- Business rules.
- Error handling.
- Side effects.
- Unknowns.

Do not generate Java code.
Return structured Markdown.
```

### 3. DB2 Schema Mapper

Role:

- Reads DDL and embedded SQL.
- Produces Java entity/repository mapping.

Prompt:

```text
Analyze this DB2 DDL and embedded SQL.

Return:
- Tables.
- Columns and types.
- Primary keys.
- Generated identity behavior.
- SQL operations used by the legacy program.
- Java entity fields.
- Repository methods.
- Transaction boundaries.
- Not-found behavior.
- SQL error handling notes.
```

### 4. Java/Spring Designer

Role:

- Converts migration brief into Spring design.
- Produces domain, service, repository, controller plan.

Prompt:

```text
Design the Java/Spring target for this RPG/DB2 migration.

Include:
- Package structure.
- Domain model.
- DTOs.
- Repository interface.
- Service methods.
- REST endpoints.
- Validation.
- Error mapping.
- Transaction rules.

Preserve legacy behavior before improving style.
```

### 5. Test Generator

Role:

- Creates characterization tests.
- Makes sure behavior is measurable.

Prompt:

```text
Generate characterization tests for the RPG-to-Java migration.

Cover:
- Create employee.
- Read employee by ID.
- Update employee.
- Delete employee.
- List employees ordered by ID.
- Employee not found.
- Invalid numeric input.
- SQL failure intent.

Return JUnit-style test cases and expected results.
```

### 6. Security Reviewer

Role:

- Reviews generated design for data access and agent/tool risk.

Prompt:

```text
Review the migration design for security risks.

Focus on:
- DB2 access.
- Injection risk.
- Authorization.
- Secrets.
- Logging.
- Error leakage.
- Data exposure.
- AI tool permissions.
- Human approval for writes.

Return critical, major, and minor findings.
```

### 7. Final Migration Reviewer

Role:

- Reviews the entire package before final output.

Prompt:

```text
Review the complete RPG-to-Java migration package.

Find:
- Behavior mismatches.
- Missing business rules.
- DB2 mapping errors.
- Test gaps.
- Over-refactoring.
- Security issues.
- Unclear assumptions.

Return findings first, ordered by severity.
```

## Workflow

1. Hub receives target files.
2. Hub sends RPGLE/CL to RPG Source Analyst.
3. Hub sends DDL and embedded SQL to DB2 Schema Mapper.
4. Hub sends both outputs to Java/Spring Designer.
5. Hub sends design to Test Generator.
6. Hub sends design and tests to Security Reviewer.
7. Hub sends full package to Final Migration Reviewer.
8. Hub revises if critical findings exist.
9. Hub returns final package.

## Output Contract

```json
{
  "pattern": "hub-and-spoke",
  "legacy_sources": [],
  "target_stack": "Java/Spring",
  "migration_brief": {},
  "db2_mapping": {},
  "target_design": {},
  "generated_code": {},
  "tests": [],
  "security_findings": [],
  "review_findings": [],
  "human_approval_required": []
}
```

## Strengths

- Simple to understand.
- Good for one program or one vertical slice.
- Easy to add/remove specialist agents.
- Hub keeps final output coherent.

## Weaknesses

- Hub can become a bottleneck.
- Specialists may miss cross-cutting constraints if context is incomplete.
- Not ideal for very large application portfolios.

## Stop Condition

Stop only when:

- No critical review findings remain.
- Test plan covers all CRUD paths.
- DB2 mapping is explicit.
- Human approval points are listed.

Do not stop because a model says confidence is high.
