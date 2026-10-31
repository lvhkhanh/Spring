#!/usr/bin/env python3
"""Microsoft Agent Framework RPG-to-Java migration template.

Dry-run mode prints the intended workflow without importing SDK packages.
Adapt the SDK skeleton after installing:

    pip install agent-framework azure-identity
"""

from __future__ import annotations

import json
from dataclasses import asdict, dataclass


@dataclass(frozen=True)
class WorkflowStep:
    name: str
    role: str
    input: list[str]
    output: str
    gate: str


STEPS = [
    WorkflowStep(
        "planner",
        "Decompose RPG-to-Java migration",
        ["EMPCRUD.rpgle", "EMPCRUD.CLP", "EMPLOYEE.DDL"],
        "migration_task_graph",
        "tasks_have_inputs_outputs_and_gates",
    ),
    WorkflowStep(
        "source_analysis",
        "Analyze RPGLE and CL behavior",
        ["migration_task_graph"],
        "legacy_behavior_model",
        "rpg_behavior_documented",
    ),
    WorkflowStep(
        "db2_mapping",
        "Map DDL and embedded SQL",
        ["legacy_behavior_model", "EMPLOYEE.DDL"],
        "db2_mapping",
        "db2_mapping_explicit",
    ),
    WorkflowStep(
        "spring_design",
        "Design Java/Spring target",
        ["legacy_behavior_model", "db2_mapping"],
        "spring_design",
        "java_design_complete",
    ),
    WorkflowStep(
        "code_generation",
        "Generate smallest safe Java/Spring slice",
        ["spring_design"],
        "generated_code",
        "crud_covered",
    ),
    WorkflowStep(
        "test_generation",
        "Generate characterization tests",
        ["legacy_behavior_model", "generated_code"],
        "tests",
        "tests_generated",
    ),
    WorkflowStep(
        "checker",
        "Validate behavior, DB2 mapping, security, and tests",
        ["legacy_behavior_model", "db2_mapping", "generated_code", "tests"],
        "review",
        "no_critical_findings",
    ),
]


SDK_SKELETON = r'''
# Validate names against your installed agent-framework version.
from agent_framework.foundry import FoundryChatClient
from azure.identity import AzureCliCredential

credential = AzureCliCredential()
client = FoundryChatClient(
    project_endpoint="https://<foundry>.services.ai.azure.com/api/projects/<project>",
    model="<deployment-name>",
    credential=credential,
)

planner = client.as_agent(
    name="RPGMigrationPlanner",
    instructions="Decompose RPG-to-Java migration into typed workflow steps and gates.",
)

rpg_analyst = client.as_agent(
    name="RPGAnalyst",
    instructions="Analyze RPGLE/CL behavior. Do not generate Java code.",
)

db2_mapper = client.as_agent(
    name="DB2Mapper",
    instructions="Map DB2 DDL and embedded SQL to Java entity/repository design.",
)

spring_designer = client.as_agent(
    name="SpringDesigner",
    instructions="Design Java/Spring domain, repository, service, controller, DTOs, and transactions.",
)

checker = client.as_agent(
    name="MigrationChecker",
    instructions="Validate objective gates. Never use self-confidence as a pass condition.",
)

# Option A: Functional Workflow API with @workflow / @step.
# Option B: WorkflowBuilder with executors and edges.
# Use HITL request/response for DB writes, deployment, or risky assumptions.
'''


def dry_run() -> dict:
    return {
        "framework": "Microsoft Agent Framework",
        "pattern": "planner + workflow + maker-checker",
        "source": ["apps/RPG/EMPCRUD.rpgle", "apps/RPG/EMPCRUD.CLP", "apps/RPG/EMPLOYEE.DDL"],
        "target": "Java/Spring",
        "steps": [asdict(step) for step in STEPS],
        "final_gates": [
            "rpg_behavior_documented",
            "db2_mapping_explicit",
            "java_design_complete",
            "crud_covered",
            "tests_generated",
            "no_critical_findings",
            "human_approval_points_listed",
        ],
        "sdk_skeleton": SDK_SKELETON.strip(),
    }


def main() -> int:
    print(json.dumps(dry_run(), indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
