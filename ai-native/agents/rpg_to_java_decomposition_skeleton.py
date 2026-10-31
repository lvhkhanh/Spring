#!/usr/bin/env python3
"""Offline skeleton for RPG-to-Java decomposition planning.

This script creates a structured decomposition plan for migration workflows.
It does not call an LLM. Replace `plan_decomposition` with the real agent invocation.
"""

from __future__ import annotations

import argparse
import json
from dataclasses import dataclass, field, asdict
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[2]


@dataclass
class Task:
    id: str
    name: str
    role: str
    inputs: list[str]
    outputs: list[str]
    dependencies: list[str]
    quality_gate: str
    description: str


@dataclass
class DecompositionPlan:
    migration_goal: str
    tasks: list[Task] = field(default_factory=list)
    gates: dict[str, bool] = field(default_factory=dict)
    assumptions: list[str] = field(default_factory=list)
    risks: list[str] = field(default_factory=list)


def plan_decomposition() -> DecompositionPlan:
    """Stub for a real decomposition agent. Replace with actual LLM/agent call."""
    return DecompositionPlan(
        migration_goal="Migrate EMPCRUD RPGLE CRUD behavior to Java/Spring",
        tasks=[
            Task(
                id="T1",
                name="Analyze RPGLE source",
                role="Legacy Analysis",
                inputs=["apps/RPG/EMPCRUD.rpgle"],
                outputs=["legacy_behavior_model"],
                dependencies=[],
                quality_gate="legacy_behavior_documented",
                description="Extract business behavior, procedures, data fields, and embedded SQL from RPGLE.",
            ),
            Task(
                id="T2",
                name="Analyze CL wrapper",
                role="Legacy Analysis",
                inputs=["apps/RPG/EMPCRUD.CLP"],
                outputs=["cl_workflow_model"],
                dependencies=["T1"],
                quality_gate="cl_workflow_documented",
                description="Document runtime control flow and parameter passing in the CL wrapper.",
            ),
            Task(
                id="T3",
                name="Map DB2 DDL and embedded SQL",
                role="DB2 Mapping",
                inputs=["apps/RPG/EMPLOYEE.DDL", "legacy_behavior_model"],
                outputs=["db2_mapping_document"],
                dependencies=["T1"],
                quality_gate="db2_mapping_explicit",
                description="Translate DB2 table and SQL operations to Java entity and repository mappings.",
            ),
            Task(
                id="T4",
                name="Design Java/Spring target",
                role="Target Architecture",
                inputs=["legacy_behavior_model", "db2_mapping_document"],
                outputs=["target_design"],
                dependencies=["T2", "T3"],
                quality_gate="java_design_complete",
                description="Design the Java/Spring domain model, service boundaries, controller, DTOs, and transaction model.",
            ),
            Task(
                id="T5",
                name="Generate smallest safe Java/Spring slice",
                role="Code Generation",
                inputs=["target_design"],
                outputs=["generated_code"],
                dependencies=["T4"],
                quality_gate="crud_behavior_covered",
                description="Produce the smallest safe implementation slice that preserves legacy CRUD behavior.",
            ),
            Task(
                id="T6",
                name="Define characterization tests",
                role="Test Definition",
                inputs=["legacy_behavior_model", "generated_code"],
                outputs=["test_plan"],
                dependencies=["T5"],
                quality_gate="tests_defined",
                description="Define tests covering create, read, update, delete, list, not-found, and error behavior.",
            ),
            Task(
                id="T7",
                name="Review migration package and assumptions",
                role="Quality Review",
                inputs=["generated_code", "test_plan", "target_design"],
                outputs=["review_report"],
                dependencies=["T6"],
                quality_gate="no_critical_findings",
                description="Review the package for behavior gaps, security issues, and undocumented assumptions.",
            ),
            Task(
                id="T8",
                name="Document assumptions and human approval points",
                role="Quality Review",
                inputs=["review_report"],
                outputs=["approval_checklist"],
                dependencies=["T7"],
                quality_gate="human_approval_points_listed",
                description="Capture assumptions, risks, and explicit human approval points for the migration output.",
            ),
        ],
        gates={
            "legacy_behavior_documented": False,
            "cl_workflow_documented": False,
            "db2_mapping_explicit": False,
            "java_design_complete": False,
            "crud_behavior_covered": False,
            "tests_defined": False,
            "no_critical_findings": False,
            "human_approval_points_listed": False,
        },
        assumptions=[
            "EMPCRUD.rpgle uses EMPLOYEE table for all CRUD operations.",
            "CL wrapper only orchestrates program calls and does not contain extra business logic.",
        ],
        risks=[
            "Implicit RPG business rules may not be explicit in current sources.",
            "DB2 SQL paths could include unhandled error handling or multi-row effects.",
        ],
    )


def main() -> int:
    plan = plan_decomposition()
    print(json.dumps(asdict(plan), indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
