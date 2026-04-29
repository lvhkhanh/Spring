---
name: plan
description: '**WORKFLOW SKILL** — Break down work into clear, sequenced, and actionable plans for implementation, migration, debugging, testing, or delivery efforts. USE FOR: task decomposition, milestone planning, dependency mapping, risk identification, prioritization, execution sequencing, and defining validation steps before or during work. DO NOT USE FOR: replacing actual implementation with indefinite planning, producing architecture documents when system design depth is required, or writing full specifications when requirement traceability is the main goal. INVOKES: file system tools for plan and task artifacts, semantic search for context discovery, terminal for repository inspection and validation workflow checks.'
---

# Planning Skill

## Overview

This skill provides structured support for turning ambiguous or large requests into practical execution plans. It helps define scope, break work into manageable steps, order tasks by dependency and risk, identify assumptions and blockers, and create plans that are concrete enough to implement and validate.

## Key Capabilities

### Scope Clarification
- Translate broad requests into specific deliverables and outcomes
- Separate required work from optional improvements or future ideas
- Identify assumptions, open questions, and decision points
- Define boundaries so plans stay focused and realistic

### Task Decomposition
- Break large efforts into smaller actionable work items
- Group tasks into phases, milestones, or streams when helpful
- Identify parallelizable work versus critical-path dependencies
- Size steps so progress and ownership are easy to track

### Sequencing and Prioritization
- Order work by dependency, risk, impact, and feedback speed
- Front-load unknowns and high-risk validation steps
- Distinguish must-have work from nice-to-have follow-ups
- Create implementation sequences that reduce rework

### Risk and Dependency Management
- Surface blockers, external dependencies, and hidden coupling
- Call out prerequisites such as environment setup, access, data, or approvals
- Identify rollback, fallback, or mitigation paths where relevant
- Anticipate coordination points across teams, modules, or systems

### Validation Planning
- Define how each milestone or workstream will be verified
- Include test, review, demo, or rollout checks in the plan
- Ensure completion criteria are observable rather than vague
- Highlight where additional investigation is needed before coding

## Usage Examples

### Plan a Feature Delivery
```
Create an implementation plan for adding multi-factor authentication.
Break it into backend, frontend, test, rollout, and recovery steps,
and call out the highest-risk dependencies first.
```

### Plan a Refactor
```
Turn this legacy module cleanup into a safe phased plan.
Include characterization tests, incremental code moves, and checkpoints
that let us stop without leaving the system in a broken state.
```

### Plan a Bugfix Investigation
```
We have an intermittent production bug with unclear ownership.
Create a debugging and stabilization plan that prioritizes fast signal,
instrumentation, containment, root-cause isolation, and validation.
```

### Plan a Migration
```
Outline a migration plan from the current batch process to a Spring Boot service.
Cover analysis, data contracts, implementation phases, testing, cutover, and rollback.
```

## Common Patterns

### Basic Planning Flow
```text
1. Clarify scope and desired outcome
2. Identify assumptions, blockers, and dependencies
3. Break work into concrete tasks
4. Sequence tasks by risk and dependency
5. Define validation for each major step
6. Capture follow-ups and remaining unknowns
```

### Phase Structure Pattern
```text
Phase 1: discovery and validation
Phase 2: core implementation
Phase 3: integration and hardening
Phase 4: rollout and verification
```

### Good Task Pattern
```text
Each task should answer:
- what will be changed
- why it matters
- what it depends on
- how completion will be verified
```

### Risk-First Planning Pattern
```text
Start with tasks that reduce uncertainty:
- validate assumptions
- prove technical feasibility
- expose hidden dependencies
- establish rollback or containment paths
```

## Best Practices

- Keep plans concrete enough that someone can start the first step immediately
- Prefer short, verifiable tasks over broad vague phases
- Put risky unknowns early so surprises happen before deep implementation
- Include validation, not just build steps
- Call out assumptions explicitly instead of burying them
- Revise the plan when new facts change the critical path
- Avoid planning detail that exceeds the level of current certainty

## Troubleshooting

### Plan Is Too Abstract
- Replace labels like "implement feature" with concrete deliverables
- Add dependencies, owners, and validation criteria
- Split oversized tasks into smaller checkpoints

### Plan Is Too Detailed Too Early
- Collapse speculative later-phase tasks into milestones
- Keep detail highest near the immediate next steps
- Expand deeper only after key unknowns are resolved

### Work Keeps Getting Blocked
- Re-check hidden prerequisites, approvals, and environment needs
- Move dependency discovery earlier in the sequence
- Add explicit mitigation or fallback tasks

### Team Cannot Tell What Done Looks Like
- Add observable success criteria for each milestone
- Define test, review, and rollout checks clearly
- Remove ambiguous completion language

## Integration Points

- **Engineering workflows**: feature delivery, refactors, migrations, bugfixes
- **Documentation**: implementation plans, ADR inputs, sprint notes, task breakdowns
- **Quality workflows**: testing strategy, validation checkpoints, release readiness
- **Coordination**: cross-team dependencies, handoffs, approvals, rollout communication
- **Execution environments**: local development, CI pipelines, staged rollouts, production changes
