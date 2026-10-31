# RPG To Java Migration With Microsoft Agent Framework, LangGraph, And CrewAI

This folder applies three agent frameworks to the same modernization problem:

- Source: `apps/RPG/EMPCRUD.rpgle`, `apps/RPG/EMPCRUD.CLP`, `apps/RPG/EMPLOYEE.DDL`
- Target: Java or Kotlin with Spring Boot
- Goal: preserve RPG/DB2 CRUD behavior before refactoring

## Framework Fit

| Framework | Best Fit For This Repo | Recommended Pattern |
|---|---|---|
| Microsoft Agent Framework | Azure/Foundry production agent workflows, checkpointing, HITL, type-safe routing, enterprise governance | Planner + workflow + maker-checker |
| LangGraph | Explicit graph orchestration, stateful agent loops, parallel fan-out/fan-in, evaluator-optimizer cycles | StateGraph with supervisor and conditional gates |
| CrewAI | Fast role/task crew setup, sequential or hierarchical team workflows, manager-agent delegation | Sequential first, hierarchical for larger migrations |

## Shared Agent Roles

Use these roles across all three frameworks:

- Migration Planner: decomposes RPG-to-Java migration into tasks.
- RPG Analyst: extracts procedures, variables, I/O, embedded SQL, and business behavior.
- CL Analyst: extracts wrapper workflow and runtime assumptions.
- DB2 Mapper: maps DDL and SQL operations to entity/repository design.
- Java/Spring Designer: designs target service, repository, DTO, and controller layers.
- Code Maker: generates the smallest safe Java/Spring slice.
- Test Maker: generates characterization and unit tests.
- Checker: validates behavior preservation, tests, DB2 mapping, security, and assumptions.
- Supervisor: enforces objective gates and human approval points.

## Shared Gates

Never stop because an LLM says it is confident. Stop only when objective gates pass:

- RPG behavior is documented.
- DB2 table and SQL operations are mapped.
- Java/Spring design is coherent.
- CRUD behavior is covered.
- Not-found and SQL-error intent are covered.
- Tests are generated.
- Security review has no critical findings.
- Human approval points are listed.

## Files

- `microsoft-agent-framework-rpg-to-java.md`: Microsoft Agent Framework application design.
- `langgraph-rpg-to-java.md`: LangGraph state graph design.
- `crewai-rpg-to-java.md`: CrewAI crew/process design.
- `templates/microsoft_agent_framework_rpg_to_java.py`: dry-run topology plus Microsoft Agent Framework skeleton.
- `templates/langgraph_rpg_to_java.py`: dry-run topology plus LangGraph skeleton.
- `templates/crewai_rpg_to_java.py`: dry-run topology plus CrewAI skeleton.

## Dry-Run Commands

These commands do not call any LLM:

```bash
python3 ai-native/agents/frameworks/templates/microsoft_agent_framework_rpg_to_java.py
python3 ai-native/agents/frameworks/templates/langgraph_rpg_to_java.py
python3 ai-native/agents/frameworks/templates/crewai_rpg_to_java.py
```

## Run All Frameworks Together

Use the helper script to execute all three dry-run templates and collect their outputs in one file:

```bash
python3 ai-native/agents/frameworks/run_all_frameworks.py
```

This writes a consolidated JSON summary to `ai-native/agents/frameworks/framework_dry_run_outputs.json`.

## Primary Sources

- Microsoft Agent Framework overview: https://learn.microsoft.com/en-us/agent-framework/overview/
- Microsoft Agent Framework workflows: https://learn.microsoft.com/en-us/agent-framework/workflows/
- LangGraph workflows and agents: https://docs.langchain.com/oss/python/langgraph/workflows-agents
- LangChain multi-agent patterns: https://docs.langchain.com/oss/python/langchain/multi-agent
- CrewAI processes: https://docs.crewai.com/en/concepts/processes
- CrewAI sequential process: https://docs.crewai.com/en/learn/sequential-process
- CrewAI agents: https://docs.crewai.com/en/concepts/agents
