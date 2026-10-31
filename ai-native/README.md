# AI-Native Modernization Workspace

This folder makes AI a first-class part of the repository instead of a loose chat workflow. It provides reusable prompts, evaluation checklists, and a local helper script for legacy-to-modernization work.

## What "AI-Native" Means Here

AI-native development for this repo means:

- The repo contains enough context for an AI assistant to understand its purpose.
- Legacy modernization work starts with a structured brief, not direct code generation.
- Prompt templates and evaluation criteria are versioned with the code.
- Agent/tool workflows are designed with safety boundaries.
- Modernized code is checked against legacy behavior through tests and review.

## Main Use Cases

1. Legacy understanding
   - Explain COBOL/RPG/CL programs.
   - Identify inputs, outputs, DB2 tables, files, reports, and business rules.
   - Produce migration briefs.

2. Modernization
   - Convert COBOL/RPG slices into Java/Kotlin/Spring services.
   - Translate DB2 table access into repository/service patterns.
   - Map 5250-style interactions into web/API workflows.
   - Visualize legacy program flow with diagrams and Mermaid/PlantUML outputs before coding.

3. Evaluation
   - Generate characterization tests.
   - Compare legacy and modern outputs.
   - Review security, data access, and behavioral risks.

4. Agent/tool integration
   - Use DB2 tools for read-only discovery.
   - Keep write actions gated behind human approval.
   - Make tool calls observable and auditable.

## Files

- `CASAN-roadmap.md`: current position and roadmap to highest AI-native level for this repo.
- `agentic-delivery/`: a vendor-neutral forward-deployed delivery wiki and engagement brief for applying CCAR-P, Google Agentic Architect, Microsoft FTE, and AWS FDE practices.
- `agents/`: agentic AI patterns and orchestration templates for RPG-to-Java modernization.
- `repo_assistant.py`: offline CLI for repository inventory, source briefs, and prompt generation.
- `prompts/modernization.md`: reusable prompt pack for legacy modernization.
- `evals/modernization-checklist.md`: review checklist for AI-generated modernization work.

## Quick Start

From the repository root:

```bash
python3 ai-native/repo_assistant.py inventory
python3 ai-native/repo_assistant.py brief apps/RPG/EMPCRUD.rpgle
python3 ai-native/repo_assistant.py prompt apps/COBOL/FPANALYSIS.cob
```

The helper script is intentionally offline. It does not call any model API. Use the generated brief or prompt with your preferred assistant, then check the result against `evals/modernization-checklist.md`.

## Recommended AI Loop

```text
Inventory -> Brief -> Prompt -> Generate -> Evaluate -> Test -> Review -> Commit
```

Do not skip the brief. The brief is where the assistant identifies assumptions, side effects, and missing context before producing modern code.
