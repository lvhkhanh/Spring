# CrewAI: RPG To Java Migration

## Why This Framework

Use CrewAI when you want a fast role/task setup for collaborating agents. CrewAI maps naturally to modernization work because agents have roles, goals, tools, tasks, and processes.

CrewAI documents two relevant process styles:

- Sequential: tasks run in order, and output from one task can feed the next.
- Hierarchical: a manager LLM or custom manager agent delegates tasks and validates completion.

For this repo, start with sequential. Move to hierarchical when you want a manager agent to delegate across many RPG/CL/DDL files.

## Sequential Crew

```text
RPG Analyst Task
  -> DB2 Mapper Task
  -> Java/Spring Designer Task
  -> Code Maker Task
  -> Test Maker Task
  -> Checker Task
```

Sequential is best for:

- A single source program.
- First migration pass.
- Clear handoff between tasks.
- Easy monitoring.

## Hierarchical Crew

```text
Manager Agent
  delegates to:
    RPG Analyst
    CL Analyst
    DB2 Mapper
    Java/Spring Designer
    Code Maker
    Test Maker
    Checker
```

Hierarchical is best for:

- Larger application migration.
- Many files and dependencies.
- Dynamic task assignment.
- Manager validation.

## Agents

### RPG Analyst

- Role: IBM i RPGLE source analyst.
- Goal: extract behavior, procedures, SQL, variables, user prompts, errors.

### DB2 Mapper

- Role: DB2 schema and SQL mapper.
- Goal: map DDL and SQL to Java entity/repository design.

### Java/Spring Designer

- Role: Java modernization architect.
- Goal: design domain, service, repository, controller, DTO, and transactions.

### Code Maker

- Role: Java/Spring implementation engineer.
- Goal: generate the smallest safe migration slice.

### Test Maker

- Role: characterization test engineer.
- Goal: prove create/read/update/delete/list and not-found behavior.

### Checker

- Role: migration quality reviewer.
- Goal: find behavior gaps, DB2 mapping gaps, test gaps, security risks.

## CrewAI Process Settings

Sequential:

```python
Crew(
    agents=[rpg_analyst, db2_mapper, spring_designer, code_maker, test_maker, checker],
    tasks=[analyze_task, map_task, design_task, code_task, test_task, check_task],
    process=Process.sequential,
)
```

Hierarchical:

```python
Crew(
    agents=[rpg_analyst, db2_mapper, spring_designer, code_maker, test_maker, checker],
    tasks=[migration_goal_task],
    process=Process.hierarchical,
    manager_agent=manager_agent,
)
```

## CrewAI Guardrails

- Set low `max_iter` for worker agents to control cost.
- Use task context instead of dumping all files into every task.
- Use callbacks to log outputs and token usage.
- Use human input for risky DB/write/deploy decisions.
- Use deterministic test execution outside the LLM.

## Run Template

```bash
python3 ai-native/agents/frameworks/templates/crewai_rpg_to_java.py
```

The template runs in dry-run mode and prints the sequential and hierarchical crew topology. It also contains a CrewAI SDK skeleton.

## Best Use In This Repo

Use CrewAI for:

- Fast local experiments.
- Teaching agent roles and tasks.
- AB-100 style business architecture demos.
- Sequential migration pipelines.
- Manager-agent migration reviews.
