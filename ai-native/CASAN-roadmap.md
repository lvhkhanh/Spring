# FPT CASAN Positioning And Roadmap For This Repo

Last reviewed: 2026-07-16

## Assumption

I could not verify a public official `FPT CASAN` framework definition. This document treats CASAN as an AI-native capability ladder for software delivery and modernization. If you have the official FPT CASAN rubric, replace the labels here with the official names and keep the evidence/roadmap structure.

## Current Position

For this repository, your current position is best described as:

**AI-Assisted Modernization Engineer, moving toward AI-Native Solution Architect.**

Why:

- You already have legacy assets: COBOL, RPGLE, CL, DB2 DDL.
- You already have modern target examples: Kotlin/Spring demos, REST/UI examples, Helm deployment assets.
- You already have AI/agent experiments: `agent-openai-sdk.py`, DB2 query tooling, and an MCP-style DB2 adapter.
- You now have AI-native process assets: prompts, evaluation checklist, repo assistant, and repo-level AI instructions.
- The missing parts are production-grade modernization slices, automated equivalence tests, CI checks, deeper agent orchestration, security guardrails, and deployment evidence.

In practical leveling terms, you are around **middle to upper-middle** for this repo: beyond basic AI usage, not yet at highest AI-native architect/platform level.

## CASAN-Style Level Map

| Level | Position | Evidence In This Repo | Gap To Next Level |
|---|---|---|---|
| L1 | AI User | Uses AI for explanation, drafting, and coding help | Already exceeded |
| L2 | AI-Assisted Developer | Uses AI to generate code, prompts, and docs | Present through agent scripts and modernization prompts |
| L3 | AI-Enabled Modernization Engineer | Uses AI with legacy inventory, migration briefs, and review checklists | Current strongest fit |
| L4 | AI-Native Solution Architect | Designs repeatable AI workflows with tests, agents, tools, governance, and deployment | Need real modernization slices plus automated evals |
| L5 | AI-Native Platform/Transformation Lead | Builds reusable platform patterns, metrics, CI/CD gates, security controls, and team playbooks | Need production-style architecture, automation, and evidence |

## Highest-Level Target For This Repo

The highest credible target is:

**AI-Native Legacy Modernization Platform Lead**

This means the repo becomes a working reference platform for:

- COBOL/RPG/CL/DB2 discovery.
- AI-generated migration briefs.
- Human-reviewed modernization decisions.
- Java/Kotlin/Spring target implementation.
- Characterization and equivalence tests.
- DB2 read-only analysis tools.
- Agent workflows with approval gates.
- CI/CD validation.
- Deployment through Helm or local containers.
- Governance docs and repeatable team playbooks.

## Roadmap To Highest Level

### Phase 1: Make The Repo Explainable

Goal: any AI assistant or engineer can understand the repo quickly.

Deliverables:

- Keep `AGENTS.md` as the source of AI working rules.
- Expand `ai-native/README.md` with the modernization vision.
- Generate migration briefs for:
  - `apps/COBOL/FPANALYSIS.cob`
  - `apps/RPG/EMPCRUD.rpgle`
  - `apps/RPG/EMPCRUD.CLP`
  - `apps/RPG/EMPLOYEE.DDL`
- Add one architecture note: `ai-native/architecture/modernization-platform.md`.

Success criteria:

- A new engineer can explain the repo in 10 minutes.
- Every legacy sample has a migration brief.
- Unknowns and assumptions are explicit.

### Phase 2: Build One Vertical Modernization Slice

Goal: convert one legacy behavior into modern Spring code with tests.

Recommended first slice:

**COBOL function point calculator -> Kotlin/Spring service.**

Why this first:

- Small scope.
- Clear formula.
- Easy expected outputs.
- Good place to prove the AI-native loop.

Deliverables:

- DTO for function point inputs.
- Service method for `FC = 4*I + 5*R + 10*F + 7*X + 4*Q`.
- REST endpoint.
- Unit tests for normal, zero, and boundary inputs.
- Migration brief linked from the code or docs.

Success criteria:

- Tests prove `I=4, R=2, F=1, X=1, Q=2 -> FC=51`.
- Business formula is isolated from UI/API code.
- AI-generated code passes human review checklist.

### Phase 3: Modernize The RPG/DB2 CRUD Sample

Goal: turn the RPGLE CRUD sample into a Spring-style service/API.

Deliverables:

- `Employee` domain model.
- Repository abstraction for `EMPLOYEE`.
- Service methods: create, read, update, delete, list.
- REST endpoints.
- Tests for create/read/update/delete/list.
- DB2 schema mapping from `EMPLOYEE.DDL`.
- Clear handling for not found and SQL errors.

Success criteria:

- CRUD behavior matches the RPG sample.
- DB write paths are explicit and reviewed.
- Tests cover not found, invalid input, and list ordering.

### Phase 4: Add AI Evaluation Gates

Goal: make AI-generated changes measurable.

Deliverables:

- `ai-native/evals/fixtures/` with sample inputs and expected outputs.
- A modernization review template.
- A generated-code review checklist.
- CI or script command that runs tests before accepting AI output.

Success criteria:

- No AI-generated modernization is accepted without tests.
- Each prompt-generated change has a brief, tests, and review notes.
- Regression failures are easy to reproduce.

### Phase 5: Agentize The Workflow

Goal: move from prompt library to controlled agents.

Deliverables:

- Extend `agent-openai-sdk.py` or create a dedicated modernization agent.
- Agent roles:
  - Inventory agent.
  - Migration brief agent.
  - Test generation agent.
  - Code review agent.
  - DB2 read-only discovery agent.
- Tool rules:
  - Read-only tools can run automatically.
  - Database writes require explicit approval.
  - File edits require review.
  - Deployment commands require approval.

Success criteria:

- Agent can produce a brief from a legacy file.
- Agent can propose tests before code.
- Agent cannot perform risky DB or deployment actions without approval.

### Phase 6: Production-Style Architecture

Goal: demonstrate platform-level readiness.

Deliverables:

- Architecture Decision Records in `ai-native/adrs/`.
- Threat model for DB2 and AI tool use.
- Prompt injection handling notes.
- Observability plan: logs, traces, model/tool calls, costs.
- Helm deployment path for a modernized service.
- Runbook for local demo and review.

Success criteria:

- The repo demonstrates architecture, implementation, tests, deployment, and governance.
- A reviewer can see why each AI-native control exists.
- The system is repeatable for another COBOL/RPG program.

## Skill Path To Highest Level

Study and practice in this order:

1. Legacy systems
   - COBOL structure.
   - RPGLE procedure and embedded SQL.
   - CL program orchestration.
   - DB2 schema and SQL behavior.

2. Modern target stack
   - Kotlin or Java.
   - Spring Boot service/controller/repository patterns.
   - REST API design.
   - Unit and integration testing.

3. AI-native engineering
   - Prompt design.
   - Migration briefs.
   - AI code review.
   - Evaluation datasets.
   - Agent tool safety.

4. Architecture
   - C4 diagrams.
   - ADRs.
   - Threat modeling.
   - CI/CD gates.
   - Observability and cost control.

5. Leadership
   - Reusable playbooks.
   - Standards for AI-assisted modernization.
   - Review process for generated code.
   - Metrics for productivity, quality, and risk.

## Evidence Checklist For Promotion To Highest Level

You can claim the highest level for this repo when you can show:

- [ ] At least two legacy programs modernized into tested Spring components.
- [ ] Characterization tests prove legacy behavior.
- [ ] DB2 schema and access patterns are documented.
- [ ] AI prompts and evaluation checklists are versioned.
- [ ] Agent/tool workflow has safety gates.
- [ ] CI runs the relevant tests.
- [ ] Deployment path exists.
- [ ] ADRs explain major architecture choices.
- [ ] Security and data-handling risks are documented.
- [ ] A repeatable modernization playbook exists for new legacy programs.

## Immediate Next 5 Actions

1. Generate briefs:

```bash
python3 ai-native/repo_assistant.py brief apps/COBOL/FPANALYSIS.cob
python3 ai-native/repo_assistant.py brief apps/RPG/EMPCRUD.rpgle
python3 ai-native/repo_assistant.py brief apps/RPG/EMPCRUD.CLP
python3 ai-native/repo_assistant.py brief apps/RPG/EMPLOYEE.DDL
```

2. Implement the function point calculator as a Spring service.
3. Add unit tests proving the COBOL formula.
4. Implement the Employee CRUD model and service.
5. Add ADRs and CI checks.

## Short Answer

Your current level for this repo:

**L3: AI-Enabled Modernization Engineer.**

Your next target:

**L4: AI-Native Solution Architect.**

Highest target:

**L5: AI-Native Legacy Modernization Platform Lead.**
