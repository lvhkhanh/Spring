# RPG To Java Agent Pattern Catalog

This catalog applies six agentic AI patterns to RPG/CL/DB2 to Java/Spring modernization.

Repo target:

- `apps/RPG/EMPCRUD.rpgle`
- `apps/RPG/EMPCRUD.CLP`
- `apps/RPG/EMPLOYEE.DDL`

Modern target:

- Java or Kotlin.
- Spring Boot.
- `Employee` domain model.
- Repository/service/controller layers.
- Characterization tests proving equivalent CRUD behavior.

## Pattern Selection

| Pattern | Best Use | Main Risk | Control |
|---|---|---|---|
| Hub-and-spoke | Focused migration slice with clear specialist roles | Hub bottleneck | Tool contracts and structured outputs |
| Sequential | Reliable step-by-step migration pipeline | Error propagates downstream | Validate each stage before next |
| Parallel | Independent analysis/review tasks | Conflicting outputs | Fan-in aggregator and quorum policy |
| Planner | Complex migration requiring explicit decomposition | Over-planning | Require executable task graph |
| Maker-checker | Code generation with strict quality gate | Checker misses issues | Deterministic tests plus rubric |
| Critic loop | Iterative improvement of design/code | Endless reflection cost | Max iterations and objective gates |

## 1. Hub-And-Spoke

Definition:

```text
Central orchestrator delegates to specialized spoke agents registered as tools.
```

Applied to RPG to Java:

```text
Migration Hub
  tools:
    analyze_rpg_source
    analyze_cl_workflow
    map_db2_schema
    design_spring_target
    generate_characterization_tests
    review_security
    review_migration
```

Tool registration model:

```json
{
  "name": "analyze_rpg_source",
  "description": "Analyze RPGLE procedures, embedded SQL, data fields, input/output prompts, and business behavior.",
  "input_schema": {
    "type": "object",
    "properties": {
      "path": { "type": "string" },
      "source": { "type": "string" }
    },
    "required": ["path", "source"]
  }
}
```

Workflow:

1. Hub reads target files.
2. Hub calls `analyze_rpg_source`.
3. Hub calls `analyze_cl_workflow`.
4. Hub calls `map_db2_schema`.
5. Hub calls `design_spring_target`.
6. Hub calls `generate_characterization_tests`.
7. Hub calls `review_security`.
8. Hub calls `review_migration`.
9. Hub returns final package.

Best output:

```json
{
  "migration_brief": {},
  "db2_mapping": {},
  "target_design": {},
  "tests": [],
  "security_findings": [],
  "review_findings": [],
  "human_approval_required": []
}
```

## 2. Sequential

Definition:

```text
Linear prompt-chaining: output of one agent becomes input to the next.
```

Applied to RPG to Java:

```text
RPG Analysis
  -> DB2 Mapping
  -> Java/Spring Design
  -> Code Generation
  -> Test Generation
  -> Review
  -> Final Migration Package
```

Stage contract:

- Each stage must produce structured output.
- Each stage validates required fields before the next stage starts.
- If a required field is missing, stop and ask for human clarification or rerun that stage.

Example chain:

```python
rpg_analysis = rpg_analyst(rpg_source)
db2_mapping = db2_mapper(rpg_analysis, ddl_source)
spring_design = spring_designer(rpg_analysis, db2_mapping)
code = java_generator(spring_design)
tests = test_generator(rpg_analysis, spring_design, code)
review = reviewer(rpg_analysis, db2_mapping, spring_design, code, tests)
```

Best for:

- First implementation pass.
- Teaching the modernization flow.
- High traceability.

Avoid when:

- You need multiple independent opinions.
- You need speed through parallel fan-out.

## 3. Parallel

Definition:

```text
Fan-out/fan-in with asyncio.gather and quorum policies.
```

Applied to RPG to Java:

Fan-out:

```text
               -> RPG analyst
Migration task -> CL analyst
               -> DB2 mapper
               -> Security reviewer
               -> Test strategist
```

Fan-in:

```text
Aggregator merges structured results.
Review quorum validates the output.
```

Python sketch:

```python
results = await asyncio.gather(
    run_agent("rpg_analyst", context),
    run_agent("cl_analyst", context),
    run_agent("db2_mapper", context),
    run_agent("security_reviewer", context),
    run_agent("test_strategist", context),
)

merged = aggregate(results)
```

Quorum policy examples:

- Two out of three reviewers must agree there are no critical findings.
- If any security reviewer reports a critical issue, fail the gate.
- If DB2 mapping and RPG analysis disagree, require human review.
- If test coverage misses CRUD not-found behavior, fail the gate.

Best for:

- Fast analysis.
- Independent review.
- Reducing single-agent blind spots.

Cost note:

- Parallel fan-out can cost more because each agent call is a separate model call.
- Use cheaper models for simple extraction and stronger models for architecture/review.

## 4. Planner

Definition:

```text
Hub acting as explicit decomposition planner before spoke dispatch.
```

Applied to RPG to Java:

The planner does not immediately generate code. It first creates a migration work plan:

```json
{
  "goal": "Migrate EMPCRUD RPGLE CRUD behavior to Java/Spring",
  "tasks": [
    {
      "id": "T1",
      "agent": "rpg_analyst",
      "input": ["EMPCRUD.rpgle"],
      "output": "procedure_behavior_map"
    },
    {
      "id": "T2",
      "agent": "db2_mapper",
      "input": ["EMPLOYEE.DDL", "procedure_behavior_map"],
      "output": "employee_schema_mapping"
    },
    {
      "id": "T3",
      "agent": "spring_designer",
      "input": ["procedure_behavior_map", "employee_schema_mapping"],
      "output": "spring_design"
    }
  ],
  "gates": [
    "legacy_behavior_identified",
    "db2_mapping_explicit",
    "crud_tests_defined",
    "security_review_passed"
  ]
}
```

Planner prompt:

```text
You are a migration planner.

Before dispatching agents, decompose RPG-to-Java migration into tasks.
For each task, define:
- Agent.
- Inputs.
- Expected output.
- Dependencies.
- Quality gate.
- Human approval requirement.

Do not generate code.
```

Best for:

- Larger migrations.
- Work that needs traceability.
- Reducing random agent wandering.

## 5. Maker-Checker

Definition:

```text
Supervisor quality gate: maker agent produces, checker agent validates.
```

Applied to RPG to Java:

```text
Maker Agent:
  generates Java/Spring design, code, and tests.

Checker Agent:
  validates behavior, DB2 mapping, tests, security, assumptions.
```

Maker prompt:

```text
Generate the smallest safe Java/Spring migration slice from this RPG analysis.
Preserve behavior first.
Include code, tests, and migration notes.
```

Checker prompt:

```text
Validate the migration output against the RPG source.

Return JSON:
{
  "passed": false,
  "critical_findings": [],
  "behavior_gaps": [],
  "db2_mapping_gaps": [],
  "test_gaps": [],
  "security_gaps": [],
  "required_fixes": []
}
```

Gate:

```python
passed = (
    checker["passed"]
    and len(checker["critical_findings"]) == 0
    and len(checker["behavior_gaps"]) == 0
    and len(checker["test_gaps"]) == 0
)
```

Best for:

- Code generation.
- Test generation.
- Preventing one agent from approving its own work.

Do not use:

- Same prompt, same model, same context as both maker and checker if stakes are high.
- Self-confidence as the pass condition.

## 6. Critic Loop

Definition:

```text
Reflection cycle: critic agent evaluates and returns feedback to the reasoning agent.
```

Applied to RPG to Java:

```text
Reasoning Agent creates migration output.
Critic Agent finds gaps.
Reasoning Agent revises.
Supervisor checks objective gates.
```

Bounded loop:

```python
MAX_ITERATIONS = 3

draft = reasoning_agent(task)

for i in range(MAX_ITERATIONS):
    critique = critic_agent(draft)

    if objective_gates_pass(critique):
        break

    draft = reasoning_agent({
        "previous_draft": draft,
        "critic_feedback": critique,
        "instruction": "Fix only the identified issues."
    })
```

Critic rubric:

- Did the output preserve RPG behavior?
- Are DB2 operations mapped correctly?
- Are create/read/update/delete/list all covered?
- Is not-found behavior preserved?
- Are invalid numeric inputs handled?
- Are SQL errors represented safely?
- Are tests sufficient?
- Are assumptions explicit?

Best for:

- Improving architecture notes.
- Strengthening migration briefs.
- Fixing review findings.

Cost control:

- Limit iterations.
- Keep critic output concise.
- Use deterministic tests as soon as code exists.
- Do not ask for another reflection cycle if gates already fail due to missing human information.

## Combined Recommended Workflow For This Repo

Use the patterns together:

```text
Planner
  -> creates task graph
Hub-and-spoke
  -> dispatches specialist analysis
Parallel
  -> runs independent analysis/reviews where safe
Sequential
  -> passes approved artifacts through design -> code -> tests
Maker-checker
  -> validates generated package
Critic loop
  -> fixes bounded review findings
```

Recommended flow:

1. Planner creates task graph.
2. Hub dispatches source, CL, and DB2 analysis.
3. Parallel fan-out runs independent analysis.
4. Aggregator merges results.
5. Sequential chain produces design, code, and tests.
6. Maker-checker validates output.
7. Critic loop fixes issues for at most three iterations.
8. Human approves assumptions and risky actions.

## Final Acceptance Gate

Do not accept the migration until:

- RPG behavior is documented.
- DB2 mapping is explicit.
- Java/Spring design is coherent.
- Tests cover CRUD and edge cases.
- Security review has no critical findings.
- Human approval points are listed.
- Generated code compiles or has a clear compile plan.
