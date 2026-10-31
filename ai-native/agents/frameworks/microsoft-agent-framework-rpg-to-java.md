# Microsoft Agent Framework: RPG To Java Migration

## Why This Framework

Use Microsoft Agent Framework when the RPG-to-Java migration needs Azure/Foundry integration, explicit workflows, checkpointing, human-in-the-loop gates, middleware, telemetry, and enterprise deployment controls.

Microsoft's docs describe Agent Framework as covering:

- Agents that use LLMs, tools, and MCP servers.
- Harnesses for long multi-step tasks.
- Workflows that connect agents and functions with type-safe routing, checkpointing, and human-in-the-loop support.

For this repo, use **workflows** rather than a free-form autonomous agent because RPG-to-Java migration has well-defined stages.

## Recommended Pattern

```text
Planner Workflow
  -> Analyze RPG/CL/DDL
  -> Design Java/Spring target
  -> Generate code
  -> Generate tests
  -> Checker gate
  -> Human approval for risky assumptions
```

## Agent/Workflow Mapping

| Migration Role | Microsoft Agent Framework Concept |
|---|---|
| Migration Planner | Foundry-backed agent or workflow step |
| RPG Analyst | Agent or executor |
| DB2 Mapper | Agent or deterministic function with read-only DB2 tool |
| Java/Spring Designer | Agent |
| Code Maker | Agent |
| Test Maker | Agent |
| Checker | Agent plus deterministic validation function |
| Human Approval | Workflow HITL request/response |

## Functional Workflow Shape

Microsoft docs describe a Functional Workflow API for Python using `@workflow` and `@step`, with native Python control flow and `asyncio.gather`. Use it for this repo when you want readable Python orchestration:

```text
@workflow
async def migrate_rpg_to_java(ctx, target):
    plan = await plan_migration(target)
    analysis = await analyze_sources(plan)
    design = await design_target(analysis)
    package = await generate_code(design)
    tests = await generate_tests(analysis, package)
    review = await check_package(analysis, design, package, tests)
    if review.has_critical_findings:
        package = await fix_package(package, review)
    if review.requires_human_approval:
        await request_human_approval(review)
    return final_package
```

## Workflow Builder Shape

Use Workflow Builder when you want a fixed graph:

```text
START
  -> planner
  -> source_analysis
  -> db2_mapping
  -> spring_design
  -> code_generation
  -> test_generation
  -> checker
  -> conditional:
       pass -> END
       fixable -> code_generation
       needs_human -> human_approval
```

## Tools

Recommended tools:

- `read_repo_file(path)`: read source files.
- `list_legacy_sources()`: list RPG, CL, COBOL, DDL files.
- `extract_sql(source)`: deterministic SQL extraction.
- `query_db2_readonly(sql)`: optional read-only DB2 discovery.
- `run_tests(command)`: deterministic validation.
- `write_migration_brief(path, content)`: writes reviewed docs.

Tool safety:

- `query_db2_readonly` must reject `insert`, `update`, `delete`, `merge`, `drop`, `alter`, `create`, and `call`.
- Generated code writes should be reviewed before commit.
- Human approval is required for DB writes, deployments, and broad file edits.

## Gate JSON

```json
{
  "rpg_behavior_documented": false,
  "db2_mapping_explicit": false,
  "java_design_complete": false,
  "crud_covered": false,
  "tests_generated": false,
  "no_critical_findings": false,
  "human_approval_points_listed": false
}
```

## Run Template

```bash
python3 ai-native/agents/frameworks/templates/microsoft_agent_framework_rpg_to_java.py
```

The template runs in dry-run mode and prints the workflow topology. It also contains an SDK skeleton you can adapt after installing Microsoft Agent Framework.

## Best Use In This Repo

Use Microsoft Agent Framework as the production-grade path for:

- AI-500 preparation.
- Azure Foundry agent workflows.
- Durable modernization jobs.
- Human approvals.
- Observability.
- Enterprise governance.
