# RPG To Java Agentic AI Patterns

This folder defines agentic AI patterns for migrating IBM i RPG/CL/DB2 code to Java or Kotlin with Spring.

Core pattern files:

- `frameworks/`: Microsoft Agent Framework, LangGraph, and CrewAI application designs for RPG-to-Java migration.
- `rpg-to-java-decomposition.md`: agentic decomposition task for RPG-to-Java migration planning.
- `rpg-to-java-agent-pattern-catalog.md`: applies hub-and-spoke, sequential, parallel, planner, maker-checker, and critic-loop patterns to this repo.
- `rpg-to-java-hub-and-spoke.md`: one central migration hub delegates to specialist spoke agents.
- `rpg-to-java-hierarchical.md`: an architect agent decomposes the migration into domain leads and worker agents.
- `rpg-to-java-supervisor.md`: a supervisor agent runs a gated loop across analysis, conversion, testing, and review.
- `rpg_to_java_orchestration_patterns.py`: offline Python orchestration template for the six catalog patterns.

## Recommended Use

For this repo:

1. Use the **Hub-and-Spoke** pattern for small or medium modernization slices such as `apps/RPG/EMPCRUD.rpgle`.
2. Use the **Hierarchical** pattern when migrating a larger application with many RPG programs, CL wrappers, DDL files, screens, reports, and batch jobs.
3. Use the **Supervisor** pattern when you want the agent workflow to iterate until objective quality gates pass.
4. Use the **Pattern Catalog** when you want to combine planner, sequential, parallel, maker-checker, and critic-loop workflows.

## Pattern Template Commands

These commands run offline and do not call an LLM:

```bash
python3 ai-native/agents/rpg_to_java_orchestration_patterns.py hub-and-spoke
python3 ai-native/agents/rpg_to_java_orchestration_patterns.py sequential
python3 ai-native/agents/rpg_to_java_orchestration_patterns.py parallel
python3 ai-native/agents/rpg_to_java_orchestration_patterns.py planner
python3 ai-native/agents/rpg_to_java_orchestration_patterns.py maker-checker
python3 ai-native/agents/rpg_to_java_orchestration_patterns.py critic-loop
```

## Shared Migration Target

Legacy source:

- `apps/RPG/EMPCRUD.rpgle`
- `apps/RPG/EMPCRUD.CLP`
- `apps/RPG/EMPLOYEE.DDL`

Modern target:

- Java or Kotlin.
- Spring Boot.
- Domain model: `Employee`.
- Repository abstraction for DB2 table access.
- Service methods for create, read, update, delete, and list.
- REST controller or UI workflow.
- Characterization tests proving equivalence.

## Shared Safety Rules

- Treat RPG/CL/DDL as source of truth.
- Do not invent missing business rules.
- Mark assumptions explicitly.
- Do not perform database writes without human approval.
- Use read-only DB2 discovery first.
- Generate tests before refactoring.
- Use objective gates instead of LLM self-confidence.

## Shared Quality Gates

A migration output is acceptable only when:

- Migration brief exists.
- Business rules are identified.
- DB2 table mapping is documented.
- Generated Java/Kotlin compiles.
- Characterization tests exist.
- Tests cover create, read, update, delete, list, not found, invalid input, and SQL failure intent.
- AI code review has no critical findings.
- Human reviewer approves assumptions.
