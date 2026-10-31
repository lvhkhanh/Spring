# LangGraph: RPG To Java Migration

## Why This Framework

Use LangGraph when you want explicit graph state, branching, loops, persistence, streaming, debugging, and deployment for agent workflows.

LangGraph documentation emphasizes common workflow and agent patterns such as prompt chaining, parallelization, routing, orchestrator-worker, and evaluator-optimizer. Those map cleanly to RPG-to-Java modernization.

## Recommended Pattern

```text
StateGraph
  START
    -> planner
    -> parallel_analysis
    -> aggregate
    -> design
    -> make_code
    -> make_tests
    -> check
    -> conditional:
         pass -> END
         fix -> make_code
         human -> END with needs_human_review
```

## State

```python
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
```

## Node Mapping

| Node | Responsibility |
|---|---|
| `planner` | Create task graph and quality gates |
| `parallel_analysis` | Run RPG analyst, CL analyst, and DB2 mapper |
| `aggregate` | Merge and reconcile analysis |
| `design` | Produce Java/Spring target design |
| `make_code` | Generate smallest safe slice |
| `make_tests` | Generate characterization tests |
| `check` | Validate gates and findings |
| `route_after_check` | Decide `pass`, `fix`, or `human` |

## Parallel Fan-Out

Use LangGraph's graph model or node logic to run independent work:

```text
parallel_analysis:
  - RPG analyst
  - CL analyst
  - DB2 mapper
  - security reviewer
```

Fan-in result:

```json
{
  "rpg_analysis": {},
  "cl_analysis": {},
  "db2_mapping": {},
  "security_findings": []
}
```

## Evaluator-Optimizer Loop

This is the best fit for maker-checker and critic-loop:

```text
make_code -> make_tests -> check
              ^             |
              |             |
              +---- fix <---+
```

Stop after at most 3 iterations unless all gates pass.

## Gate Function

```python
def route_after_check(state: MigrationState) -> str:
    review = state["review"]
    gates = review["gates"]

    if all(gates.values()) and not review["critical_findings"]:
        return "pass"

    if state["iteration"] >= 3 or review["requires_human_approval"]:
        return "human"

    return "fix"
```

## Run Template

```bash
python3 ai-native/agents/frameworks/templates/langgraph_rpg_to_java.py
```

The template runs in dry-run mode and prints the graph topology and gates. It also includes a LangGraph SDK skeleton.

## Best Use In This Repo

Use LangGraph for:

- Complex branching.
- Parallel analysis.
- Bounded critic loops.
- Debuggable state transitions.
- Explicit migration gates.
- CI-friendly orchestration tests.
