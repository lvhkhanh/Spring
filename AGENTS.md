# AI-Native Repo Instructions

This repository is a learning and modernization workbench. Treat it as a mixed codebase with legacy IBM i assets, Spring/Kotlin demos, database tooling, container/deployment examples, and AI agent experiments.

## Primary AI-Native Goal

Use AI to accelerate legacy modernization while preserving behavior:

- Understand COBOL, RPGLE, CL, and DB2 artifacts.
- Produce migration briefs before code conversion.
- Convert legacy slices into Java/Spring or Kotlin/Spring patterns.
- Generate tests and acceptance checks from legacy behavior.
- Keep humans in the loop for business rules, database writes, and production changes.

## Repository Areas

- `apps/COBOL/`: COBOL samples and function point analysis.
- `apps/RPG/`: RPGLE, CL, and DB2 CRUD sample.
- `demo/` and `demo2/`: Spring/Kotlin web examples.
- `mcp/`: DB2 HTTP adapter intended for agent/tool integration.
- `agent-openai-sdk.py`: OpenAI Agents SDK experiment with math, DB2, and COBOL conversion tools.
- `ai-native/`: AI-native workflows, prompts, evals, and local helper scripts.
- `copilot-tracking/`: research and certification notes.

## Safe AI Working Rules

- Do not execute database writes from AI tools without explicit human approval.
- Prefer read-only DB2 exploration first: table inventory, schema, row samples, and dependency mapping.
- Treat legacy code as the source of truth until tests prove otherwise.
- Preserve business behavior before refactoring style.
- Add migration notes when generated code relies on assumptions.
- Keep generated prompts, eval criteria, and modernization decisions in versioned Markdown.
- Never put secrets, DB2 passwords, API keys, or personal tokens into prompts, logs, docs, or commits.

## Modernization Workflow

1. Inventory the target slice.
2. Identify inputs, outputs, files/tables, jobs, screens, reports, and side effects.
3. Create a migration brief.
4. Generate candidate modern code.
5. Build characterization tests from legacy examples.
6. Compare legacy and modern outputs.
7. Review with a human owner.
8. Only then refactor, optimize, or deploy.

## Suggested Commands

```bash
python3 ai-native/repo_assistant.py inventory
python3 ai-native/repo_assistant.py brief apps/COBOL/FPANALYSIS.cob
python3 ai-native/repo_assistant.py prompt apps/RPG/EMPCRUD.rpgle
```
