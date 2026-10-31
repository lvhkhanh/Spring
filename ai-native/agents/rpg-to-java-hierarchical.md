# Agentic AI Pattern 2: Hierarchical RPG To Java Migration

## Best Use

Use this pattern for larger IBM i modernization where the system includes many RPG programs, CL wrappers, DDL files, reports, batch jobs, and integration points.

Best repo target:

- Start with `apps/RPG/EMPCRUD.rpgle`.
- Scale later to a portfolio of RPG/COBOL programs.

## Pattern Summary

```text
Chief Modernization Architect
  -> Legacy Analysis Lead
      -> RPG Procedure Analyst
      -> CL Workflow Analyst
      -> DB2 SQL Analyst
  -> Target Architecture Lead
      -> Java Domain Designer
      -> Spring API Designer
      -> Data Access Designer
  -> Quality Lead
      -> Characterization Test Designer
      -> Security Reviewer
      -> Migration Risk Reviewer
```

This pattern creates a tree of responsibility. Leads summarize worker outputs upward. The Chief Modernization Architect makes final architecture decisions.

## Agents

### 1. Chief Modernization Architect

Role:

- Owns migration strategy.
- Creates work breakdown.
- Resolves conflicts between leads.
- Approves final package.

System prompt:

```text
You are the Chief Modernization Architect for RPG to Java/Spring migration.

Decompose the migration into legacy analysis, target architecture, and quality workstreams.
Delegate detailed work to leads and worker agents.
Require every lead to return assumptions, risks, and evidence.
Resolve conflicts using legacy behavior as the source of truth.

Final output must include:
- Executive migration summary.
- Legacy behavior model.
- Target Java/Spring architecture.
- Implementation backlog.
- Test strategy.
- Security and governance controls.
- Decision log.
```

### 2. Legacy Analysis Lead

Role:

- Coordinates RPG, CL, SQL analysis.
- Produces one legacy behavior model.

Prompt:

```text
Lead legacy analysis for this RPG/CL/DB2 application.

Coordinate worker findings into:
- Program inventory.
- Procedure inventory.
- CL workflow.
- DB2 operations.
- Business rules.
- User interaction model.
- Side effects.
- Error handling.
- Unknowns.
```

Worker agents:

- RPG Procedure Analyst.
- CL Workflow Analyst.
- DB2 SQL Analyst.

### 3. Target Architecture Lead

Role:

- Converts legacy behavior into Java/Spring architecture.

Prompt:

```text
Lead target architecture for this RPG-to-Java migration.

Produce:
- Java package structure.
- Domain model.
- Service boundaries.
- Repository boundaries.
- REST API or UI flow.
- DTOs.
- Transaction model.
- Error model.
- Deployment considerations.
```

Worker agents:

- Java Domain Designer.
- Spring API Designer.
- Data Access Designer.

### 4. Quality Lead

Role:

- Ensures generated design is testable, safe, and reviewable.

Prompt:

```text
Lead quality for this migration.

Produce:
- Characterization test plan.
- Unit test plan.
- Integration test plan.
- Security review.
- Migration risk register.
- Acceptance gates.
```

Worker agents:

- Characterization Test Designer.
- Security Reviewer.
- Migration Risk Reviewer.

## Workflow

1. Chief Modernization Architect creates the decomposition plan.
2. Legacy Analysis Lead delegates source analysis to workers.
3. Target Architecture Lead waits for the legacy behavior model, then designs the target architecture.
4. Quality Lead reviews both legacy model and target design.
5. Chief resolves conflicts.
6. Chief creates implementation backlog.
7. Chief authorizes the smallest safe vertical slice.
8. Worker agents generate code and tests only for that slice.
9. Quality Lead reviews results.
10. Chief returns final package.

## Output Contract

```json
{
  "pattern": "hierarchical",
  "chief_decisions": [],
  "legacy_analysis": {
    "rpg": {},
    "cl": {},
    "db2": {},
    "behavior_model": {}
  },
  "target_architecture": {
    "domain": {},
    "api": {},
    "data_access": {},
    "transactions": {}
  },
  "quality": {
    "tests": [],
    "security": [],
    "risks": [],
    "acceptance_gates": []
  },
  "implementation_backlog": []
}
```

## Strengths

- Scales to large portfolios.
- Clear ownership across workstreams.
- Good for architecture reviews and enterprise migration.
- Produces useful decision logs.

## Weaknesses

- More overhead than hub-and-spoke.
- Requires stricter summaries to avoid context bloat.
- Slower for very small programs.

## Stop Condition

Stop only when:

- Each lead signs off.
- Chief decision log is complete.
- Smallest safe vertical slice is identified.
- No critical quality issues remain.
- Human approvals are listed.

## Example For `EMPCRUD.rpgle`

Smallest safe vertical slice:

```text
Read employee by ID
  -> Analyze RPG readRecord procedure.
  -> Map EMPLOYEE columns.
  -> Create Employee domain model.
  -> Create EmployeeRepository.findById.
  -> Create EmployeeService.getEmployee.
  -> Create GET /employees/{id}.
  -> Test found and not found behavior.
```
