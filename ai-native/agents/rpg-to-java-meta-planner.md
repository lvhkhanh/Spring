# Meta-Agent Planner Architecture for RPG to Java Migration

This document defines a meta-agent planner architecture for migrating IBM i RPG/CL/DB2 applications to Java/Spring. It is meant to sit above the existing planner, supervisor, and specialist agent patterns and provide a structured, audit-friendly orchestration layer.

## Purpose

The meta-agent planner is the top-level coordinator that:

- reads the migration goal and legacy context,
- creates an explicit migration task graph,
- selects or composes the most appropriate agent pattern(s),
- applies quality gates and human approval points,
- routes work to analysis, design, generation, and validation agents,
- supervises the migration lifecycle state.

This architecture is designed for larger or higher-risk migrations where a single-shot agent workflow is too brittle.

## When to Use

Use the meta-agent planner when:

- the migration has multiple legacy inputs (`RPGLE`, `CLP`, `DB2` DDL, reports, screens),
- the migration requires traceability, auditability, or governance,
- you want to combine planner, supervisor, and hierarchical patterns,
- you need explicit quality gates before generation,
- human review and approval points must be enforced,
- the workflow will be executed in LangGraph, CrewAI, or Microsoft Agent Framework.

## Core Architecture

### 1. Meta Planner

The Meta Planner is the root agent.

Responsibilities:

- define the migration objective,
- decompose the migration into tasks,
- assign tasks to specialist roles,
- attach inputs, outputs, dependencies, and gate criteria,
- choose the orchestration pattern(s),
- decide where to place parallel vs sequential work,
- decide what requires human-in-the-loop.

Output contract:

```json
{
  "migration_goal": "Migrate RPG/CL/DB2 EMPCRUD slice to Java/Spring",
  "pattern": "planner + hierarchical + supervisor",
  "tasks": [
    {
      "id": "T1",
      "name": "Extract RPG behavior",
      "role": "legacy_analysis",
      "inputs": ["apps/RPG/EMPCRUD.rpgle"],
      "outputs": ["legacy_behavior_model"],
      "dependencies": [],
      "quality_gate": "legacy_behavior_documented",
      "human_approval": false
    }
  ],
  "gates": {
    "legacy_behavior_documented": false,
    "db2_mapping_explicit": false,
    "java_design_complete": false,
    "tests_defined": false,
    "no_critical_findings": false
  },
  "assumptions": [
    "EMPCRUD.rpgle uses EMPLOYEE.DDL for all CRUD operations."
  ],
  "risks": [
    "Implicit business rules in RPG modcodes may not be explicit in source."
  ]
}
```

### 2. Pattern Selection and Composition

The meta planner should choose from these building blocks:

- `Planner`: explicit task graph creation and dependency management.
- `Hub-and-Spoke`: central task router that delegates to specialist agents.
- `Sequential`: chain design, code generation, and test creation.
- `Parallel`: independent analysis and review steps run in fan-out.
- `Hierarchical`: manager agent delegates sub-plans to domain leads.
- `Supervisor`: bounded loop with objective gates and fix cycles.
- `Maker-Checker`: generation followed by independent validation.
- `Critic-Loop`: reflection and revision until gates pass or budget ends.
- `Plan-Execute-Reflect`: execute the planner graph, inspect output and gate failures, then revise the plan and re-run as needed.

The meta planner can compose patterns such as:

- `Planner -> Hub-and-Spoke -> Sequential -> Maker-Checker`
- `Planner -> Parallel analysis -> Aggregation -> Supervisor loop`
- `Planner -> Hierarchical manager -> specialist crews -> Review`

### 3. Specialist Agents

Specialist agents consume the planner’s task graph and produce artifacts:

- `legacy_analysis_agent`
- `cl_workflow_agent`
- `db2_schema_agent`
- `target_architecture_agent`
- `code_generation_agent`
- `test_definition_agent`
- `quality_review_agent`
- `assumption_review_agent`

Each specialist should return structured outputs, not free-text only.

### 4. Workflow Engine

The meta planner’s task graph is executed by a workflow engine such as:

- `LangGraph` via a `StateGraph` and explicit node transitions,
- `CrewAI` via a manager plus crew/hierarchical processes,
- `Microsoft Agent Framework` via `@workflow` and `@step` constructs.

The workflow engine enforces dependencies, parallelism, and gate evaluation.

### 5. Quality Gates and Human Approval

Quality gates should be explicit, binary, and objective.
Examples:

- `legacy_behavior_documented`
- `db2_mapping_explicit`
- `java_design_complete`
- `crud_behavior_covered`
- `tests_defined`
- `no_critical_findings`
- `assumptions_reviewed`

Human approval points are tasks where the workflow must pause until a reviewer signs off.

## Meta-Agent Planner Workflow

### Phase 1: Discovery

1. Collect source inputs: `EMPCRUD.rpgle`, `EMPCRUD.CLP`, `EMPLOYEE.DDL`.
2. Identify program entry points, RPG procedures, CL call flow, DB2 tables, and implicit business rules.
3. Produce the migration task graph.
4. Emit assumptions and risks.

### Phase 2: Analysis

- Run parallel analysis agents for RPG, CL, and DB2.
- Merge findings into a single legacy behavior model.
- Validate that data flows and side effects are understood.

### Phase 3: Architecture Design

- Create Java/Spring service, repository, controller, DTO, and domain model design.
- Map DB2 `EMPLOYEE` table to entity and repository APIs.
- Define error handling, not-found behavior, and transaction boundaries.

### Phase 4: Code & Test Generation

- Generate the smallest safe Java/Spring slice.
- Generate characterization tests before full migration.
- Keep code generation focused on one slice at a time.

### Phase 5: Validation and Reflection

- Use maker-checker and critic-loop agents.
- Run objective gate checks on generated design, code, and tests.
- If gates fail, invoke fix/revision tasks.
- Capture failed gates, review execution artifacts, and trigger a reflection/replanning cycle.
- Replan by updating the task graph or adjusting agent responsibilities, then re-run the workflow until either gates pass or the reflection budget is exhausted.

### Phase 6: Final Review

- Confirm all gates pass or escalate unresolved blockers.
- Document the final migration package and artifacts.
- Record assumptions and human approvals.

## Framework-Specific Meta-Planner Patterns

### LangGraph

- `StateGraph` with explicit nodes: `start`, `plan`, `analysis`, `design`, `generate`, `validate`, `review`, `finish`.
- Use conditional edges to enforce gate pass/fail transitions.
- Add supervisor nodes that evaluate gate state and trigger fix loops.
- Example:

```text
START -> PLAN
PLAN -> PARALLEL_ANALYSIS
PARALLEL_ANALYSIS -> AGGREGATE
AGGREGATE -> DESIGN
DESIGN -> GENERATE
GENERATE -> VALIDATE
VALIDATE -> GATE_CHECK
GATE_CHECK -> FINISH [if pass]
GATE_CHECK -> FIX_LOOP [if fail]
```

### CrewAI

- Use a `manager_agent` as the meta planner.
- The manager creates the task graph and assigns crew roles.
- Specialist crew members execute analysis, design, generation, and review tasks.
- Use a hierarchical or sequential `Process` depending on migration size.
- Example crew structure:

```text
Manager: Meta Planner
  |- Legacy Analyst Crew
  |- DB2 Mapper Crew
  |- Architecture Crew
  |- Code/Tests Crew
  |- Review Crew
```

### Microsoft Agent Framework

- Use `@workflow` for the meta-planner orchestration.
- Use `@step` functions for discovery, analysis, design, generation, validation, and human approval.
- Use `asyncio.gather` for parallel tasks where safe.
- Example workflow:

```python
@workflow
async def migration_workflow(context):
    plan = await plan_step(context)
    analysis = await asyncio.gather(rpg_step(plan), cl_step(plan), db2_step(plan))
    design = await design_step(analysis)
    package = await generate_step(design)
    review = await validate_step(package)
    if not gates_pass(review):
        package = await fix_step(package, review)
    return await finalize_step(package, review)
```

## Meta-Planner Data Model

Use a shared structured contract for the task graph and gate state.

### Task

- `id`
- `name`
- `role`
- `inputs`
- `outputs`
- `dependencies`
- `quality_gate`
- `human_approval`
- `estimated_effort`
- `status`

### Gate

- `name`
- `description`
- `status`
- `type` (`automated`, `human`, `risk`)

### Artifact

- `name`
- `type`
- `source`
- `content`
- `summary`

## Example Task Graph for `EMPCRUD`

- `T1` Analyze RPGLE source
- `T2` Analyze CL wrapper
- `T3` Map DB2 schema and access patterns
- `T4` Author Java/Spring domain & service design
- `T5` Generate safe Java code slice
- `T6` Generate characterization tests
- `T7` Independent migration review
- `T8` Human approval & assumption validation

## Integration Guidance

- Use `rpg-to-java-decomposition.md` as the foundation for the meta planner.
- Keep the meta planner’s output machine-readable so workflow engines can act on it.
- Prefer explicit gate states over vague progress indicators.
- Reuse existing pattern docs when assigning workflow roles.
- Keep all assumptions and risks visible in the plan.

## Failure Handling

The meta planner must handle common migration failure modes:

- `analysis_incomplete`
- `ambiguous_business_rule`
- `db2_mapping_gap`
- `code_generation_gap`
- `test_gap`
- `review_blocker`
- `human_approval_pending`

For each, the planner should either:

- create a follow-up task,
- route to a fix loop,
- or escalate to human review.

## Benefits

- stronger control over complex migrations,
- better reuse of existing agent patterns,
- explicit traceability and audit history,
- easier integration with enterprise workflow tooling,
- safer handling of assumptions and approvals.
