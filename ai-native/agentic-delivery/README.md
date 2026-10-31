# Agentic Delivery Wiki

This wiki turns four current learning and delivery tracks into one practical approach for this repository's legacy-modernization work:

- **CCAR-P**: production architecture judgment—solution design, context and model strategy, integration, evaluation, governance, and organizational enablement.
- **Google Cloud Professional Agentic Architect**: build, evaluate, deploy, secure, and govern agentic workflows, with an execution component in addition to the theory exam.
- **Microsoft Frontier Transformation Engineer (FTE)**: apply the Hypervelocity Engineering delivery mindset to customer/business outcomes and repeatable delivery capability.
- **AWS Forward Deployed Engineering (FDE)**: ground, orchestrate, and prove a production agentic system with hands-on validation and customer self-sufficiency as the outcome.

These are complementary perspectives, not four incompatible architectures. The implementation remains vendor-neutral unless a delivery target is chosen. Do not make an AWS, Azure, Google Cloud, or Anthropic platform assumption merely because its framework is being used.

## Credential and program status

| Track | What it represents | Record it as complete only when |
| --- | --- | --- |
| CCAR-P | Claude architecture credential | Anthropic or the authorized certification portal awards the credential. |
| Google Professional Agentic Architect | Google Cloud professional certification | Both required assessment components are completed and Google issues the credential. |
| Microsoft FTE | Frontier Transformation Engineer badge/journey | Microsoft’s applicable partner program issues the badge. Public material describes the learning journey, not a universal public exam. |
| AWS FDE | Partner FDE Validated or Advanced credential | AWS Skill Builder confirms all then-current prerequisites and validation requirements. |

`CCAR-P FDE` is treated here as **CCAR-P architecture skills applied using a forward-deployed delivery model**. It is not asserted to be a distinct Anthropic credential.

## The shared delivery loop

```text
Outcome + owner
  -> bounded workflow and authoritative data
  -> safe vertical slice
  -> objective evaluation and operational controls
  -> production handover and reusable assets
```

1. **Frame an outcome.** Name the business owner, user, current baseline, target measure, non-goals, and deadline. “Build an agent” is not an outcome.
2. **Bound the workflow.** Select one observable workflow. Identify trusted sources, read/write side effects, identities, approvals, and unacceptable failure modes.
3. **Build a thin vertical slice.** Include the actual retrieval/tool path, a small golden dataset, deterministic validation, and a human fallback. A chat-only mockup is not sufficient.
4. **Prove it.** Run representative and adversarial cases; evaluate answer quality, tool correctness, safety, latency, cost, and recovery. Capture baseline-versus-target evidence.
5. **Harden and hand over.** Version prompts/tools/evaluations, establish observability and incident ownership, document runbooks, and leave the team able to operate and extend the solution.

## Repository application: IBM i modernization assistant

Use the existing RPG CRUD sample as the first delivery slice, not a system-wide autonomous migration.

| Delivery concern | Concrete repo artifact | Gate |
| --- | --- | --- |
| Outcome | Migration brief for `apps/RPG/EMPCRUD.rpgle` | Human owner accepts the scope and assumptions. |
| Grounding | Legacy source, CL wrapper, DDL, and approved DB2 read-only tool results | Every claim about behavior cites a source artifact. |
| Agent/tool design | Planner plus analysis, conversion, test, and reviewer agents in `ai-native/agents/` | No DB2 write tool is available to an autonomous agent. |
| Evaluation | Characterization cases and `evals/modernization-checklist.md` | Generated implementation compiles and behavior checks pass. |
| Governance | Prompt/tool version, traceable decisions, approvals for assumptions and writes | High-impact action remains human-gated. |
| Handover | Brief, tests, runbook, and reusable prompt/template committed to the repo | A maintainer can repeat the workflow without the delivery team. |

## Minimum production controls

- Treat legacy code and approved source data as the source of truth; do not let model output become one.
- Start all database exploration read-only. Human approval is required before any database write.
- Give tools narrow schemas, least privilege, timeouts, idempotency behavior, and audit logs.
- Define a turn, tool-call, time, and spend budget for every agent loop.
- Evaluate retrieval, generation, and tool execution independently; model confidence is not an acceptance test.
- Keep a human approval point for business-rule assumptions, destructive actions, customer data exposure, and production release.
- Version prompts, agent/tool definitions, test datasets, and evaluation results together with the code.

## Official references

- [Anthropic Claude Partner Network](https://www.anthropic.com/news/claude-partner-network) — partner certification and production-deployment context.
- [Google Cloud Professional Agentic Architect](https://cloud.google.com/learn/certification/agentic-architect) — capabilities and two-part certification flow.
- [Microsoft Frontier Transformation Engineer announcement](https://techcommunity.microsoft.com/blog/partnernews/differentiate-yourself-for-the-ai-era%E2%80%94earn-your-frontier-transformation-engineer/4528635) and [learning journey overview](https://partner.microsoft.com/en-us/blog/article/skilling-updates-2026-issue-5).
- [AWS Partner FDE pathways](https://aws.amazon.com.cdn.amazon.com/blogs/apn/new-fde-pathways-for-production-agentic-ai-delivery/) — Ground, Orchestrate, Prove and credential conditions.

See [engagement-brief-template.md](engagement-brief-template.md) before beginning a new agentic modernization engagement.
