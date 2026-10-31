#!/usr/bin/env python3
"""Offline orchestration templates for RPG-to-Java agent patterns.

This file demonstrates how to wire six agentic patterns without calling an LLM.
Replace `call_agent` with your real Microsoft Foundry, Claude, OpenAI Agents SDK,
LangGraph, or Semantic Kernel call.
"""

from __future__ import annotations

import argparse
import asyncio
import json
from dataclasses import dataclass, field
from pathlib import Path
from typing import Awaitable, Callable


ROOT = Path(__file__).resolve().parents[2]


@dataclass(frozen=True)
class MigrationContext:
    rpg_path: str = "apps/RPG/EMPCRUD.rpgle"
    cl_path: str = "apps/RPG/EMPCRUD.CLP"
    ddl_path: str = "apps/RPG/EMPLOYEE.DDL"
    target_stack: str = "Java/Spring"


@dataclass
class AgentResult:
    agent: str
    artifact: str
    findings: list[str] = field(default_factory=list)
    gates: dict[str, bool] = field(default_factory=dict)


async def call_agent(agent_name: str, task: str, payload: dict) -> AgentResult:
    """Stub for a real LLM/agent call."""
    await asyncio.sleep(0)
    return AgentResult(
        agent=agent_name,
        artifact=f"{agent_name} completed: {task}",
        findings=[],
        gates={
            "db2_mapping_explicit": "db2" in agent_name or "checker" in agent_name,
            "crud_covered": agent_name in {"test_generator", "checker", "reviewer"},
            "no_critical_findings": True,
        },
    )


def as_json(result: object) -> str:
    def encode(value: object) -> object:
        if isinstance(value, AgentResult):
            return {
                "agent": value.agent,
                "artifact": value.artifact,
                "findings": value.findings,
                "gates": value.gates,
            }
        raise TypeError(f"Cannot encode {type(value).__name__}")

    return json.dumps(result, default=encode, indent=2)


def objective_gates_pass(result: AgentResult) -> bool:
    return (
        result.gates.get("db2_mapping_explicit", False)
        and result.gates.get("crud_covered", False)
        and result.gates.get("no_critical_findings", False)
        and len(result.findings) == 0
    )


def path_line_count(path: str) -> int:
    candidate = Path(path)
    if not candidate.is_absolute():
        candidate = ROOT / path
    try:
        return len(candidate.read_text(encoding="utf-8", errors="ignore").splitlines())
    except OSError:
        return 0


def calibrate_decomposition_depth(
    context: MigrationContext,
    plan: dict | None = None,
    reflection: dict | None = None,
) -> int:
    base = 2
    combined_lines = (
        path_line_count(context.rpg_path)
        + path_line_count(context.cl_path)
        + path_line_count(context.ddl_path)
    )

    if combined_lines < 200:
        base = 2
    elif combined_lines < 500:
        base = 3
    elif combined_lines < 1000:
        base = 4
    else:
        base = 5

    if "spring" in context.target_stack.lower():
        base += 1

    if plan is not None:
        task_count = len(plan.get("tasks", []))
        dependency_count = sum(len(task.get("dependencies", [])) for task in plan.get("tasks", []))
        if task_count > 8 or dependency_count > 8:
            base = max(base, 4)

    if reflection is not None and reflection.get("failed_gates"):
        base = min(base + 1, 6)

    return max(2, min(base, 6))


def create_sample_plan(context: MigrationContext, target_depth: int = 2) -> dict:
    base_plan = {
        "goal": "Migrate EMPCRUD RPGLE CRUD behavior to Java/Spring",
        "tasks": [
            {
                "id": "T1",
                "name": "Analyze RPG source",
                "role": "legacy_analysis",
                "agent": "rpg_analyst",
                "inputs": [context.rpg_path],
                "outputs": ["legacy_behavior_model"],
                "dependencies": [],
                "gate": "legacy_behavior_documented",
            },
            {
                "id": "T2",
                "name": "Analyze CL wrapper",
                "role": "cl_analysis",
                "agent": "cl_analyst",
                "inputs": [context.cl_path],
                "outputs": ["cl_workflow_model"],
                "dependencies": ["T1"],
                "gate": "cl_workflow_documented",
            },
            {
                "id": "T3",
                "name": "Map DB2 schema and SQL patterns",
                "role": "db2_mapping",
                "agent": "db2_mapper",
                "inputs": [context.ddl_path, "legacy_behavior_model"],
                "outputs": ["db2_mapping"],
                "dependencies": ["T1"],
                "gate": "db2_mapping_explicit",
            },
            {
                "id": "T4",
                "name": "Design Java/Spring target",
                "role": "target_design",
                "agent": "spring_designer",
                "inputs": ["legacy_behavior_model", "db2_mapping"],
                "outputs": ["spring_design"],
                "dependencies": ["T2", "T3"],
                "gate": "java_design_complete",
            },
            {
                "id": "T5",
                "name": "Generate Java/Spring code",
                "role": "code_generation",
                "agent": "java_generator",
                "inputs": ["spring_design"],
                "outputs": ["generated_code"],
                "dependencies": ["T4"],
                "gate": "crud_covered",
            },
            {
                "id": "T6",
                "name": "Generate characterization tests",
                "role": "test_generation",
                "agent": "test_generator",
                "inputs": ["legacy_behavior_model", "generated_code"],
                "outputs": ["tests"],
                "dependencies": ["T5"],
                "gate": "tests_generated",
            },
            {
                "id": "T7",
                "name": "Review migration output",
                "role": "review",
                "agent": "reviewer",
                "inputs": ["legacy_behavior_model", "db2_mapping", "generated_code", "tests"],
                "outputs": ["review"],
                "dependencies": ["T6"],
                "gate": "no_critical_findings",
            },
        ],
        "gates": {
            "legacy_behavior_documented": False,
            "cl_workflow_documented": False,
            "db2_mapping_explicit": False,
            "java_design_complete": False,
            "crud_covered": False,
            "tests_generated": False,
            "no_critical_findings": False,
        },
    }

    if target_depth <= 2:
        return base_plan

    detailed_tasks = []
    detailed_tasks.extend(
        [
            {
                "id": "T1a",
                "name": "Extract RPG data structures and fields",
                "role": "legacy_analysis",
                "agent": "rpg_analyst",
                "inputs": [context.rpg_path],
                "outputs": ["rpg_data_model"],
                "dependencies": [],
                "gate": "legacy_behavior_documented",
            },
            {
                "id": "T1b",
                "name": "Extract RPG business rules and control flow",
                "role": "legacy_analysis",
                "agent": "rpg_analyst",
                "inputs": [context.rpg_path],
                "outputs": ["rpg_business_model"],
                "dependencies": ["T1a"],
                "gate": "legacy_behavior_documented",
            },
            {
                "id": "T1c",
                "name": "Identify embedded SQL and DB2 usage",
                "role": "db2_mapping",
                "agent": "db2_mapper",
                "inputs": [context.rpg_path, context.ddl_path],
                "outputs": ["embedded_sql_map"],
                "dependencies": ["T1a"],
                "gate": "db2_mapping_explicit",
            },
            {
                "id": "T2",
                "name": "Analyze CL wrapper",
                "role": "cl_analysis",
                "agent": "cl_analyst",
                "inputs": [context.cl_path],
                "outputs": ["cl_workflow_model"],
                "dependencies": ["T1b"],
                "gate": "cl_workflow_documented",
            },
            {
                "id": "T3",
                "name": "Refine DB2 entity mapping",
                "role": "db2_mapping",
                "agent": "db2_mapper",
                "inputs": ["embedded_sql_map", context.ddl_path],
                "outputs": ["db2_mapping"],
                "dependencies": ["T1c"],
                "gate": "db2_mapping_explicit",
            },
        ]
    )

    if target_depth >= 4:
        detailed_tasks.extend(
            [
                {
                    "id": "T4a",
                    "name": "Design Java/Spring domain model and DTO mapping",
                    "role": "target_design",
                    "agent": "spring_designer",
                    "inputs": ["rpg_data_model", "db2_mapping"],
                    "outputs": ["domain_design"],
                    "dependencies": ["T2", "T3"],
                    "gate": "java_design_complete",
                },
                {
                    "id": "T4b",
                    "name": "Design transaction and service boundaries",
                    "role": "target_design",
                    "agent": "spring_designer",
                    "inputs": ["domain_design", "rpg_business_model"],
                    "outputs": ["spring_design"],
                    "dependencies": ["T4a"],
                    "gate": "java_design_complete",
                },
            ]
        )
    else:
        detailed_tasks.append(
            {
                "id": "T4",
                "name": "Design Java/Spring target",
                "role": "target_design",
                "agent": "spring_designer",
                "inputs": ["rpg_business_model", "db2_mapping"],
                "outputs": ["spring_design"],
                "dependencies": ["T2", "T3"],
                "gate": "java_design_complete",
            }
        )

    if target_depth >= 5:
        detailed_tasks.extend(
            [
                {
                    "id": "T5a",
                    "name": "Generate Java repository and entity code",
                    "role": "code_generation",
                    "agent": "java_generator",
                    "inputs": ["spring_design"],
                    "outputs": ["repository_code"],
                    "dependencies": ["T4b" if target_depth >= 4 else "T4"],
                    "gate": "crud_covered",
                },
                {
                    "id": "T5b",
                    "name": "Generate Java service and controller code",
                    "role": "code_generation",
                    "agent": "java_generator",
                    "inputs": ["repository_code", "spring_design"],
                    "outputs": ["generated_code"],
                    "dependencies": ["T5a"],
                    "gate": "crud_covered",
                },
            ]
        )
    else:
        detailed_tasks.append(
            {
                "id": "T5",
                "name": "Generate Java/Spring code",
                "role": "code_generation",
                "agent": "java_generator",
                "inputs": ["spring_design"],
                "outputs": ["generated_code"],
                "dependencies": ["T4b" if target_depth >= 4 else "T4"],
                "gate": "crud_covered",
            }
        )

    detailed_tasks.extend(
        [
            {
                "id": "T6",
                "name": "Generate characterization tests",
                "role": "test_generation",
                "agent": "test_generator",
                "inputs": ["rpg_business_model", "generated_code"],
                "outputs": ["tests"],
                "dependencies": ["T5b" if target_depth >= 5 else "T5"],
                "gate": "tests_generated",
            },
            {
                "id": "T7",
                "name": "Review migration output",
                "role": "review",
                "agent": "reviewer",
                "inputs": ["rpg_business_model", "db2_mapping", "generated_code", "tests"],
                "outputs": ["review"],
                "dependencies": ["T6"],
                "gate": "no_critical_findings",
            },
        ]
    )

    return {
        "goal": base_plan["goal"],
        "tasks": detailed_tasks,
        "gates": {
            "legacy_behavior_documented": False,
            "cl_workflow_documented": False,
            "db2_mapping_explicit": False,
            "java_design_complete": False,
            "crud_covered": False,
            "tests_generated": False,
            "no_critical_findings": False,
        },
    }


TASK_AGENT_MAP: dict[str, str] = {
    "legacy_analysis": "rpg_analyst",
    "cl_analysis": "cl_analyst",
    "db2_mapping": "db2_mapper",
    "target_design": "spring_designer",
    "code_generation": "java_generator",
    "test_generation": "test_generator",
    "review": "reviewer",
}

AGENT_CAPABILITIES: dict[str, set[str]] = {
    "rpg_analyst": {"legacy_analysis", "rpg", "behavior"},
    "cl_analyst": {"cl_analysis", "cl", "workflow"},
    "db2_mapper": {"db2_mapping", "db2", "sql", "schema"},
    "spring_designer": {"target_design", "spring", "java", "architecture"},
    "java_generator": {"code_generation", "java", "spring", "generator"},
    "test_generator": {"test_generation", "tests", "characterization"},
    "reviewer": {"review", "validation", "quality"},
    "security_reviewer": {"review", "security", "audit"},
    "generic_agent": {"generic"},
}

ROLE_AGENT_POOLS: dict[str, list[str]] = {
    "legacy_analysis": ["rpg_analyst", "generic_agent"],
    "cl_analysis": ["cl_analyst", "generic_agent"],
    "db2_mapping": ["db2_mapper", "generic_agent"],
    "target_design": ["spring_designer", "java_generator", "generic_agent"],
    "code_generation": ["java_generator", "spring_designer", "generic_agent"],
    "test_generation": ["test_generator", "reviewer", "generic_agent"],
    "review": ["reviewer", "security_reviewer", "generic_agent"],
}


def score_agent(agent_name: str, task: dict, payload: dict) -> int:
    score = 0
    role = task.get("role", "").lower()
    gate = task.get("gate", "").lower()
    inputs = " ".join(str(i).lower() for i in task.get("inputs", []))
    candidates = AGENT_CAPABILITIES.get(agent_name, set())

    if role in candidates:
        score += 10
    if any(keyword in gate for keyword in candidates):
        score += 5
    if any(keyword in inputs for keyword in candidates):
        score += 3
    if "review" in role and "review" in agent_name:
        score += 2
    if "db2" in gate and "db2" in agent_name:
        score += 4
    if task.get("agent") == agent_name:
        score += 20
    return score


def select_agent_for_task(task: dict, payload: dict) -> str:
    explicit_agent = task.get("agent")
    if explicit_agent:
        return explicit_agent

    role = task.get("role", "")
    candidates = ROLE_AGENT_POOLS.get(role, list(AGENT_CAPABILITIES.keys()))
    if not candidates:
        candidates = list(AGENT_CAPABILITIES.keys())

    best_candidate = max(candidates, key=lambda agent: score_agent(agent, task, payload))
    if score_agent(best_candidate, task, payload) == 0:
        return TASK_AGENT_MAP.get(role, "generic_agent")
    return best_candidate


async def execute_task(task: dict, payload: dict) -> AgentResult:
    agent_name = select_agent_for_task(task, payload)
    task_name = task.get("name", "Execute task")
    return await call_agent(agent_name, f"Execute {task_name}", payload)


async def execute_plan(context: MigrationContext, plan: dict) -> dict:
    tasks = [task.copy() for task in plan.get("tasks", [])]
    executed: list[dict] = []
    completed_ids: set[str] = set()
    outputs: dict[str, object] = {}

    while tasks:
        ready = [task for task in tasks if all(dep in completed_ids for dep in task.get("dependencies", []))]
        if not ready:
            return {
                "pattern": "plan-and-execute",
                "status": "blocked",
                "remaining_tasks": [task["id"] for task in tasks],
                "executed": executed,
            }

        for task in ready:
            payload = {
                "context": context.__dict__,
                "task": task,
                "outputs": outputs,
            }
            result = await execute_task(task, payload)
            executed.append({"task": task, "result": result})
            outputs[task["id"]] = result.artifact
            completed_ids.add(task["id"])
            tasks.remove(task)

    return {"pattern": "plan-and-execute", "status": "completed", "executed": executed}


def aggregate_task_gates(execution: dict) -> dict[str, bool]:
    gates: dict[str, bool] = {}
    for entry in execution.get("executed", []):
        result = entry.get("result")
        if isinstance(result, AgentResult):
            for gate, value in result.gates.items():
                gates[gate] = gates.get(gate, False) or bool(value)
        elif isinstance(result, dict):
            for gate, value in result.get("gates", {}).items():
                gates[gate] = gates.get(gate, False) or bool(value)
    return gates


def execution_successful(execution: dict) -> bool:
    if execution.get("status") != "completed":
        return False
    gates = aggregate_task_gates(execution)
    return gates.get("no_critical_findings", False) and gates.get("crud_covered", False)


async def reflect_on_execution(context: MigrationContext, plan: dict, execution: dict) -> dict:
    failed_gates = [gate for gate, passed in aggregate_task_gates(execution).items() if not passed]
    reflection = await call_agent(
        "reflector",
        "Reflect on migration execution results and identify replanning needs",
        {
            "context": context.__dict__,
            "plan": plan,
            "execution": execution,
            "failed_gates": failed_gates,
        },
    )
    return {"reflection": reflection, "failed_gates": failed_gates}


async def replan(context: MigrationContext, plan: dict, reflection: dict) -> dict:
    replanner = await call_agent(
        "replanner",
        "Revise the migration plan based on execution reflection",
        {
            "context": context.__dict__,
            "previous_plan": plan,
            "reflection": reflection["reflection"].artifact,
            "failed_gates": reflection["failed_gates"],
        },
    )
    return replanner.artifact if isinstance(replanner.artifact, dict) else plan


async def plan_execute_reflect(context: MigrationContext, max_reflections: int = 2) -> dict:
    current_depth = calibrate_decomposition_depth(context)
    plan = await call_agent(
        "planner",
        "Create RPG-to-Java migration task graph",
        {"context": context.__dict__},
    )
    plan_dict = plan.artifact if isinstance(plan.artifact, dict) else create_sample_plan(context, current_depth)
    history: list[dict] = []
    final_status = "failed"

    for cycle in range(1, max_reflections + 1):
        execution = await execute_plan(context, plan_dict)
        success = execution_successful(execution)
        history.append({"cycle": cycle, "plan": plan_dict, "execution": execution, "success": success})
        if success:
            final_status = "success"
            break

        reflection = await reflect_on_execution(context, plan_dict, execution)
        next_depth = calibrate_decomposition_depth(context, plan_dict, reflection)
        if next_depth > current_depth:
            current_depth = next_depth
            plan_dict = create_sample_plan(context, current_depth)
            continue

        next_plan = await replan(context, plan_dict, reflection)
        if next_plan == plan_dict:
            break
        plan_dict = next_plan

    return {
        "pattern": "plan-execute-reflect",
        "final_status": final_status,
        "history": history,
        "final_plan": plan_dict,
    }


async def hub_and_spoke(context: MigrationContext) -> dict:
    """Central orchestrator delegates to spoke agents registered as tools."""
    tools: dict[str, Callable[[dict], Awaitable[AgentResult]]] = {
        "analyze_rpg_source": lambda payload: call_agent("rpg_analyst", "Analyze RPG source", payload),
        "analyze_cl_workflow": lambda payload: call_agent("cl_analyst", "Analyze CL workflow", payload),
        "map_db2_schema": lambda payload: call_agent("db2_mapper", "Map DB2 schema", payload),
        "design_spring_target": lambda payload: call_agent("spring_designer", "Design Spring target", payload),
        "generate_tests": lambda payload: call_agent("test_generator", "Generate characterization tests", payload),
        "review_security": lambda payload: call_agent("security_reviewer", "Review security", payload),
        "review_migration": lambda payload: call_agent("reviewer", "Review migration", payload),
    }

    payload = {"context": context.__dict__}
    artifacts: list[AgentResult] = []
    for tool_name in tools:
        result = await tools[tool_name](payload)
        artifacts.append(result)
        payload[tool_name] = result.artifact

    return {"pattern": "hub-and-spoke", "artifacts": artifacts}


async def sequential(context: MigrationContext) -> dict:
    """Linear prompt-chain where each artifact becomes input to the next."""
    payload = {"context": context.__dict__}
    chain = [
        ("rpg_analyst", "Analyze RPG behavior"),
        ("db2_mapper", "Map DB2 from RPG analysis and DDL"),
        ("spring_designer", "Design Java/Spring target"),
        ("java_generator", "Generate Java/Spring code"),
        ("test_generator", "Generate tests"),
        ("reviewer", "Review final package"),
    ]

    artifacts: list[AgentResult] = []
    for agent_name, task in chain:
        result = await call_agent(agent_name, task, payload)
        artifacts.append(result)
        payload[agent_name] = result.artifact

    return {"pattern": "sequential", "artifacts": artifacts}


async def parallel(context: MigrationContext) -> dict:
    """Fan-out/fan-in with asyncio.gather and a simple quorum policy."""
    payload = {"context": context.__dict__}

    analysis_results = await asyncio.gather(
        call_agent("rpg_analyst", "Analyze RPG source", payload),
        call_agent("cl_analyst", "Analyze CL wrapper", payload),
        call_agent("db2_mapper", "Map DB2 schema", payload),
        call_agent("security_reviewer", "Initial security review", payload),
        call_agent("test_strategist", "Create test strategy", payload),
    )

    review_results = await asyncio.gather(
        call_agent("checker_a", "Review merged package", {"analysis": [r.artifact for r in analysis_results]}),
        call_agent("checker_b", "Review merged package", {"analysis": [r.artifact for r in analysis_results]}),
        call_agent("checker_c", "Review merged package", {"analysis": [r.artifact for r in analysis_results]}),
    )

    approvals = sum(1 for result in review_results if result.gates.get("no_critical_findings", False))
    quorum_passed = approvals >= 2

    return {
        "pattern": "parallel",
        "analysis": list(analysis_results),
        "reviews": list(review_results),
        "quorum": {"approvals": approvals, "required": 2, "passed": quorum_passed},
    }


async def planner(context: MigrationContext) -> dict:
    """Planner creates explicit task graph before dispatch."""
    plan = await call_agent(
        "planner",
        "Create RPG-to-Java migration task graph",
        {"context": context.__dict__},
    )
    dispatch = await hub_and_spoke(context)
    return {"pattern": "planner", "plan": plan, "dispatch": dispatch}


async def plan_and_execute(context: MigrationContext) -> dict:
    """Planner produces an executable task graph and the workflow executes it."""
    plan = await call_agent(
        "planner",
        "Create RPG-to-Java migration task graph",
        {"context": context.__dict__},
    )
    plan_dict = plan.artifact if isinstance(plan.artifact, dict) else create_sample_plan(context)
    execution = await execute_plan(context, plan_dict)
    return {"pattern": "plan-and-execute", "plan": plan_dict, "execution": execution}


async def maker_checker(context: MigrationContext) -> dict:
    """Maker produces; checker validates through quality gates."""
    analysis = await call_agent("rpg_analyst", "Analyze source", {"context": context.__dict__})
    maker = await call_agent("maker", "Generate migration package", {"analysis": analysis.artifact})
    checker = await call_agent("checker", "Validate migration package", {"package": maker.artifact})

    passed = objective_gates_pass(checker)

    return {
        "pattern": "maker-checker",
        "analysis": analysis,
        "maker": maker,
        "checker": checker,
        "passed": passed,
    }


async def critic_loop(context: MigrationContext, max_iterations: int = 3) -> dict:
    """Bounded reflection loop: critic feedback returns to reasoning agent."""
    draft = await call_agent("reasoning_agent", "Create migration draft", {"context": context.__dict__})
    iterations: list[dict] = []
    passed = False

    for index in range(max_iterations):
        critic = await call_agent("critic", "Critique migration draft", {"draft": draft.artifact})
        passed = objective_gates_pass(critic)
        iterations.append({"iteration": index + 1, "draft": draft, "critic": critic, "passed": passed})
        if passed:
            break
        draft = await call_agent(
            "reasoning_agent",
            "Revise migration draft using critic feedback",
            {"draft": draft.artifact, "critic": critic.artifact},
        )

    return {"pattern": "critic-loop", "iterations": iterations, "final_passed": passed}


PATTERNS = {
    "hub-and-spoke": hub_and_spoke,
    "sequential": sequential,
    "parallel": parallel,
    "planner": planner,
    "plan-and-execute": plan_and_execute,
    "plan-execute-reflect": plan_execute_reflect,
    "maker-checker": maker_checker,
    "critic-loop": critic_loop,
}


async def run(pattern: str) -> dict:
    context = MigrationContext()
    return await PATTERNS[pattern](context)


def main() -> int:
    parser = argparse.ArgumentParser(description="RPG-to-Java agent orchestration pattern templates")
    parser.add_argument("pattern", choices=sorted(PATTERNS))
    args = parser.parse_args()
    result = asyncio.run(run(args.pattern))
    print(as_json(result))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
