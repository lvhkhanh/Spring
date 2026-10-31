#!/usr/bin/env python3
"""CrewAI RPG-to-Java migration template.

Dry-run mode prints the intended crew topology without importing SDK packages.
Adapt the SDK skeleton after installing:

    pip install crewai
"""

from __future__ import annotations

import json


CREW = {
    "framework": "CrewAI",
    "patterns": ["sequential", "hierarchical"],
    "source": ["apps/RPG/EMPCRUD.rpgle", "apps/RPG/EMPCRUD.CLP", "apps/RPG/EMPLOYEE.DDL"],
    "target": "Java/Spring",
    "agents": [
        {
            "role": "RPG Analyst",
            "goal": "Extract RPGLE behavior, procedures, SQL, variables, prompts, and errors.",
        },
        {
            "role": "DB2 Mapper",
            "goal": "Map DB2 DDL and embedded SQL to Java entity and repository design.",
        },
        {
            "role": "Java/Spring Designer",
            "goal": "Design domain, service, repository, controller, DTOs, and transactions.",
        },
        {
            "role": "Code Maker",
            "goal": "Generate the smallest safe Java/Spring migration slice.",
        },
        {
            "role": "Test Maker",
            "goal": "Generate characterization tests for CRUD behavior.",
        },
        {
            "role": "Checker",
            "goal": "Validate behavior preservation, DB2 mapping, tests, security, and assumptions.",
        },
    ],
    "tasks": [
        "Analyze RPGLE/CL behavior.",
        "Map DB2 DDL and SQL.",
        "Design Java/Spring target.",
        "Generate code.",
        "Generate tests.",
        "Check gates and findings.",
    ],
    "gates": [
        "rpg_behavior_documented",
        "db2_mapping_explicit",
        "crud_covered",
        "tests_generated",
        "no_critical_findings",
    ],
}


SDK_SKELETON = r'''
from crewai import Agent, Crew, Process, Task

rpg_analyst = Agent(
    role="RPG Analyst",
    goal="Extract RPGLE behavior, procedures, embedded SQL, prompts, and errors.",
    backstory="Senior IBM i RPGLE analyst.",
    max_iter=5,
)

db2_mapper = Agent(
    role="DB2 Mapper",
    goal="Map DB2 DDL and SQL to Java entity/repository design.",
    backstory="DB2 modernization specialist.",
    max_iter=5,
)

spring_designer = Agent(
    role="Java/Spring Designer",
    goal="Design Java/Spring domain, service, repository, controller, DTOs, and transactions.",
    backstory="Spring modernization architect.",
    max_iter=5,
)

checker = Agent(
    role="Migration Checker",
    goal="Validate objective gates. Never use LLM self-confidence as a pass condition.",
    backstory="Strict modernization reviewer.",
    max_iter=5,
)

analyze_task = Task(
    description="Analyze EMPCRUD.rpgle and EMPCRUD.CLP. Do not generate Java code.",
    expected_output="Structured legacy behavior model.",
    agent=rpg_analyst,
)

map_task = Task(
    description="Map EMPLOYEE.DDL and embedded SQL to Java repository design.",
    expected_output="DB2-to-Java mapping.",
    agent=db2_mapper,
    context=[analyze_task],
)

design_task = Task(
    description="Design Java/Spring target architecture.",
    expected_output="Domain/service/repository/controller design.",
    agent=spring_designer,
    context=[analyze_task, map_task],
)

check_task = Task(
    description="Validate behavior, DB2 mapping, tests, security, and assumptions.",
    expected_output="JSON gate report with findings.",
    agent=checker,
    context=[analyze_task, map_task, design_task],
)

sequential_crew = Crew(
    agents=[rpg_analyst, db2_mapper, spring_designer, checker],
    tasks=[analyze_task, map_task, design_task, check_task],
    process=Process.sequential,
)

# For larger migrations, use Process.hierarchical with manager_agent or manager_llm.
# hierarchical_crew = Crew(
#     agents=[rpg_analyst, db2_mapper, spring_designer, checker],
#     tasks=[migration_goal_task],
#     process=Process.hierarchical,
#     manager_agent=manager_agent,
# )
'''


def dry_run() -> dict:
    output = dict(CREW)
    output["sdk_skeleton"] = SDK_SKELETON.strip()
    return output


def main() -> int:
    print(json.dumps(dry_run(), indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
