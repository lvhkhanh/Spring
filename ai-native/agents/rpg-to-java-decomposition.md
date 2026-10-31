# RPG To Java Decomposition Agent

This file defines an agentic decomposition task for migrating IBM i RPG/CL/DB2 code to Java/Spring.
It is intended to create a task graph, role assignments, dependencies, and quality gates before any code generation begins.

## Purpose

Use the Decomposition Agent to:

- Break the migration into explicit subtasks.
- Assign responsibilities for legacy analysis, SQL mapping, design, code generation, and validation.
- Capture assumptions, unknowns, and human approval points.
- Feed a workflow engine such as LangGraph, CrewAI, or Microsoft Agent Framework.

## Best Use

Use this pattern when you need a reliable migration plan before generating Java code.
It is especially useful for:

- small RPG slices that still require clear task structure,
- multi-agent workflows,
- audit-friendly migration playbooks,
- handoff to later developer, reviewer, or automation stages.

## Decomposition Agent Role

### Decomposition Planner

- Role: migration planner and task graph author.
- Goal: decompose `apps/RPG/EMPCRUD.rpgle`, `apps/RPG/EMPCRUD.CLP`, and `apps/RPG/EMPLOYEE.DDL` into a sequenced migration plan.
- Output:
  - task list,
  - dependencies,
  - gate definitions,
  - assumptions,
  - risks,
  - execution order,
  - expected artifacts.

### Specialist Roles

The decomposition plan should assign these workstreams:

- `Legacy Analysis` (RPG/CL/DB2 extraction)
- `DB2 Mapping` (DDL and SQL mapping)
- `Target Architecture` (Java/Spring design)
- `Code Generation` (small safe slice)
- `Test Definition` (characterization + regression tests)
- `Quality Review` (gates, findings, human approval)

## Output Contract

The agent must return a structured task graph, for example:

```json
{
  "migration_goal": "Migrate EMPCRUD RPGLE CRUD behavior to Java/Spring",
  "tasks": [
    {
      "id": "T1",
      "name": "Analyze RPGLE source",
      "role": "Legacy Analysis",
      "inputs": ["apps/RPG/EMPCRUD.rpgle"],
      "outputs": ["legacy_behavior_model"],
      "dependencies": [],
      "quality_gate": "legacy_behavior_documented"
    },
    {
      "id": "T2",
      "name": "Analyze CL wrapper",
      "role": "Legacy Analysis",
      "inputs": ["apps/RPG/EMPCRUD.CLP"],
      "outputs": ["cl_workflow_model"],
      "dependencies": ["T1"],
      "quality_gate": "cl_workflow_documented"
    }
  ],
  "gates": {
    "legacy_behavior_documented": false,
    "db2_mapping_explicit": false,
    "java_design_complete": false,
    "crud_behavior_covered": false,
    "tests_defined": false,
    "no_critical_findings": false,
    "human_approval_points_listed": false
  },
  "assumptions": [
    "EMPCRUD.rpgle uses EMPLOYEE table for all CRUD operations.",
    "CL wrapper only passes basic parameters and does not contain extra business logic."
  ],
  "risks": [
    "Missing implicit business rule in RPG logic.",
    "Unseen DB2 SQL path not covered by current analysis."
  ]
}
```

## Suggested Process

1. Read the legacy sources and inventory program structure.
2. Identify RPG procedures, CL runtime flow, and DB2 operations.
3. Create a task graph with clear dependencies and minimal handoff.
4. Assign each task a quality gate.
5. Mark tasks that require human review or assumption validation.
6. Use the plan as input to the chosen framework.

## Example Task Graph

- `T1` Analyze RPG source
- `T2` Analyze CL wrapper
- `T3` Map DB2 DDL and embedded SQL
- `T4` Design Java/Spring domain and service boundaries
- `T5` Generate smallest safe Java/Spring slice
- `T6` Define characterization tests
- `T7` Review migration package and gates
- `T8` Document assumptions and approval points

## Integration with Existing Frameworks

Use the decomposition plan as the shared start point for:

- `ai-native/agents/frameworks/langgraph-rpg-to-java.md`
- `ai-native/agents/frameworks/crewai-rpg-to-java.md`
- `ai-native/agents/frameworks/microsoft-agent-framework-rpg-to-java.md`

A decomposition agent makes those workflows more deterministic by providing a clear plan before code generation.

## Stop Conditions

Stop the decomposition stage only when:

- the migration task graph is complete,
- all required inputs and outputs are explicit,
- assumptions are documented,
- quality gates are defined,
- review and human approval points are listed.

Do not stop on vague statements such as "looks complete" or "model is confident."  Use explicit gate status.
