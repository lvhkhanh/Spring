#!/usr/bin/env python3
"""LangGraph RPG-to-Java migration template.

Dry-run mode prints the intended graph without importing SDK packages.
Adapt the SDK skeleton after installing:

    pip install langgraph langchain-core
"""

from __future__ import annotations

import json


GRAPH = {
    "framework": "LangGraph",
    "pattern": "StateGraph + supervisor + evaluator-optimizer",
    "state": [
        "rpg_path",
        "cl_path",
        "ddl_path",
        "plan",
        "rpg_analysis",
        "cl_analysis",
        "db2_mapping",
        "target_design",
        "generated_code",
        "tests",
        "review",
        "iteration",
        "status",
    ],
    "edges": [
        ["START", "planner"],
        ["planner", "parallel_analysis"],
        ["parallel_analysis", "aggregate"],
        ["aggregate", "design"],
        ["design", "make_code"],
        ["make_code", "make_tests"],
        ["make_tests", "check"],
        ["check", "route_after_check"],
        ["route_after_check:pass", "END"],
        ["route_after_check:fix", "make_code"],
        ["route_after_check:human", "END"],
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
from typing import Literal, TypedDict
from langgraph.graph import END, START, StateGraph


class MigrationState(TypedDict):
    rpg_path: str
    cl_path: str
    ddl_path: str
    plan: dict
    rpg_analysis: dict
    cl_analysis: dict
    db2_mapping: dict
    target_design: dict
    generated_code: dict
    tests: list[dict]
    review: dict
    iteration: int
    status: str


def planner(state: MigrationState) -> MigrationState:
    # Call planner LLM/agent here.
    return {**state, "plan": {}}


def parallel_analysis(state: MigrationState) -> MigrationState:
    # Fan out RPG analyst, CL analyst, DB2 mapper.
    return {**state, "rpg_analysis": {}, "cl_analysis": {}, "db2_mapping": {}}


def aggregate(state: MigrationState) -> MigrationState:
    return state


def design(state: MigrationState) -> MigrationState:
    return {**state, "target_design": {}}


def make_code(state: MigrationState) -> MigrationState:
    return {**state, "generated_code": {}, "iteration": state.get("iteration", 0) + 1}


def make_tests(state: MigrationState) -> MigrationState:
    return {**state, "tests": []}


def check(state: MigrationState) -> MigrationState:
    return {
        **state,
        "review": {
            "critical_findings": [],
            "requires_human_approval": False,
            "gates": {
                "rpg_behavior_documented": True,
                "db2_mapping_explicit": True,
                "crud_covered": True,
                "tests_generated": True,
                "no_critical_findings": True,
            },
        },
    }


def route_after_check(state: MigrationState) -> Literal["pass", "fix", "human"]:
    review = state["review"]
    gates = review["gates"]
    if all(gates.values()) and not review["critical_findings"]:
        return "pass"
    if state.get("iteration", 0) >= 3 or review["requires_human_approval"]:
        return "human"
    return "fix"


builder = StateGraph(MigrationState)
builder.add_node("planner", planner)
builder.add_node("parallel_analysis", parallel_analysis)
builder.add_node("aggregate", aggregate)
builder.add_node("design", design)
builder.add_node("make_code", make_code)
builder.add_node("make_tests", make_tests)
builder.add_node("check", check)

builder.add_edge(START, "planner")
builder.add_edge("planner", "parallel_analysis")
builder.add_edge("parallel_analysis", "aggregate")
builder.add_edge("aggregate", "design")
builder.add_edge("design", "make_code")
builder.add_edge("make_code", "make_tests")
builder.add_edge("make_tests", "check")
builder.add_conditional_edges(
    "check",
    route_after_check,
    {"pass": END, "fix": "make_code", "human": END},
)

graph = builder.compile()
'''


def dry_run() -> dict:
    output = dict(GRAPH)
    output["source"] = [
        "apps/RPG/EMPCRUD.rpgle",
        "apps/RPG/EMPCRUD.CLP",
        "apps/RPG/EMPLOYEE.DDL",
    ]
    output["target"] = "Java/Spring"
    output["sdk_skeleton"] = SDK_SKELETON.strip()
    return output


def main() -> int:
    print(json.dumps(dry_run(), indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
