# Agentic AI Pattern 3: Supervisor-Gated RPG To Java Migration

## Best Use

Use this pattern when you want iterative improvement but do not want the model to stop based on self-confidence.

Best repo target:

- Use for generating and reviewing Java/Spring code from `apps/RPG/EMPCRUD.rpgle`.

## Pattern Summary

```text
Migration Supervisor
  -> Analyze
  -> Generate
  -> Test
  -> Review
  -> Fix
  -> Gate
```

The supervisor runs a bounded loop. It calls workers, checks objective gates, and decides whether another iteration is allowed.

## Supervisor Rules

- Maximum iterations: 3.
- Never use LLM confidence as a pass condition.
- Require objective gates.
- Stop early only when all gates pass.
- Escalate to human review when assumptions are risky.

## Agents

### 1. Migration Supervisor

Role:

- Owns the loop.
- Tracks gates.
- Decides whether to continue, stop, or escalate.

System prompt:

```text
You are the Migration Supervisor for RPG to Java/Spring modernization.

Run a bounded migration loop:
1. Analyze legacy source.
2. Generate target Java/Spring design or code.
3. Generate tests.
4. Review behavior, security, and test coverage.
5. Request fixes for objective failures.

Never accept self-confidence as evidence.
Accept only objective gates:
- Compiles or has a clear compile plan.
- Characterization tests exist.
- CRUD behavior is covered.
- DB2 mapping is explicit.
- No critical review findings.
- Human approval points are documented.

If gates fail after 3 iterations, return the best package plus unresolved blockers.
```

### 2. Analysis Worker

Prompt:

```text
Analyze the RPGLE/CL/DB2 source.

Return:
- Behavior summary.
- Procedure map.
- SQL map.
- Inputs and outputs.
- Error handling.
- Side effects.
- Ambiguities.
```

### 3. Generation Worker

Prompt:

```text
Generate Java/Spring migration output from the approved analysis.

Requirements:
- Preserve behavior first.
- Use Employee domain model.
- Use service and repository layers.
- Keep DB2 access behind repository abstraction.
- Include DTOs and error mapping.
- Include migration notes for assumptions.
```

### 4. Test Worker

Prompt:

```text
Generate tests for this migration output.

Required coverage:
- create employee.
- read employee found.
- read employee not found.
- update employee.
- delete employee.
- list employees by ID.
- invalid numeric input.
- SQL error intent.

Return tests and expected outcomes.
```

### 5. Review Worker

Prompt:

```text
Review the migration package.

Return JSON only:
{
  "critical_findings": [],
  "major_findings": [],
  "minor_findings": [],
  "test_gaps": [],
  "security_gaps": [],
  "behavior_gaps": [],
  "human_approval_required": [],
  "gates": {
    "db2_mapping_explicit": false,
    "crud_covered": false,
    "not_found_covered": false,
    "tests_defined": false,
    "no_critical_findings": false
  }
}
```

### 6. Fix Worker

Prompt:

```text
Fix only the issues identified by the review.

Rules:
- Do not refactor unrelated code.
- Do not invent business rules.
- Preserve approved behavior.
- Add tests for every fixed behavior gap.
- Document remaining assumptions.
```

## Supervisor Loop Pseudocode

```python
MAX_ITERATIONS = 3

analysis = analysis_worker(legacy_sources)
package = generation_worker(analysis)
tests = test_worker(analysis, package)

for iteration in range(MAX_ITERATIONS):
    review = review_worker(analysis, package, tests)

    gates_pass = (
        review["gates"]["db2_mapping_explicit"]
        and review["gates"]["crud_covered"]
        and review["gates"]["not_found_covered"]
        and review["gates"]["tests_defined"]
        and review["gates"]["no_critical_findings"]
        and len(review["critical_findings"]) == 0
    )

    if gates_pass:
        break

    package, tests = fix_worker(package, tests, review)

return {
    "analysis": analysis,
    "package": package,
    "tests": tests,
    "review": review,
    "status": "passed" if gates_pass else "needs_human_review",
}
```

## Output Contract

```json
{
  "pattern": "supervisor-gated",
  "iterations": 0,
  "analysis": {},
  "migration_package": {},
  "tests": [],
  "reviews": [],
  "final_gates": {},
  "status": "passed | needs_human_review"
}
```

## Strengths

- Excellent for quality control.
- Prevents premature stopping from model self-confidence.
- Makes review and fixing explicit.
- Good match for CI/CD and evaluation gates.

## Weaknesses

- More LLM calls than a single-shot workflow.
- Needs careful loop limits to control cost.
- Can overfit to review comments if the review rubric is weak.

## Cost Control

Each worker call can be a separate LLM call. To reduce cost:

- Keep analysis structured and reusable.
- Reuse summaries instead of full source when safe.
- Keep maximum iterations low.
- Use cheaper models for formatting and test scaffolding.
- Use stronger models only for architecture, ambiguous behavior, and final review.
- Run deterministic tests instead of asking the LLM to self-grade.

## Stop Condition

Stop only when objective gates pass. Do not stop on:

- "confidence >= 8"
- "looks complete"
- "reviewer says good" without structured gates
- "no obvious issue" without tests
