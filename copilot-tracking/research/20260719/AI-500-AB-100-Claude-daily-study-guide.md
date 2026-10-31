# Daily Study Guide: Microsoft AI-500, Microsoft AB-100, Claude CCA-F, Claude CCA-P

Last reviewed: 2026-07-19

## Purpose

This is a self-contained daily study guide for four advanced AI credentials:

- Microsoft AI-500: Microsoft Certified: Multi-Agent AI Solutions Expert
- Microsoft AB-100: Microsoft Certified: Agentic AI Business Solutions Architect
- Claude CCA-F: assumed here as Claude Certified Architect - Foundations, also commonly seen as CCAR-F or CCA-F in public prep material
- Claude CCA-P: assumed here as Claude Certified Architect - Professional, also commonly seen as CCAR-P or CCA-P in public prep material

Use official exam pages as the final authority for registration, price, language, retake, access, blueprint changes, and scoring. This guide is intentionally self-contained for daily learning, but certification programs change quickly.

## Important Assumptions

- Microsoft AI-500 is verified as the exam for Microsoft Certified: Multi-Agent AI Solutions Expert.
- Microsoft AB-100 is verified as the exam for Microsoft Certified: Agentic AI Business Solutions Architect.
- Claude CCA-F and CCA-P are treated as Claude Architect Foundations and Professional tracks. Anthropic certification pages can be access-gated, so the Claude sections are grounded in official Claude Platform and Claude Code docs plus the practical architecture domains those docs support.
- This plan is built for this repo's direction: AI-native legacy modernization with COBOL, RPGLE, CL, DB2, Java/Kotlin/Spring, MCP, agents, and evaluation gates.

## Recommended Exam Order

1. Claude CCA-F
2. Microsoft AB-100
3. Microsoft AI-500
4. Claude CCA-P

Why this order:

- CCA-F builds the Claude architecture foundation: prompting, tools, MCP, Claude Code, context management.
- AB-100 teaches business solution architecture across Microsoft 365, Copilot Studio, Power Platform, Dynamics 365, Foundry, governance, ROI, and ALM.
- AI-500 goes deeper into technical multi-agent architecture, Python, Microsoft Foundry, memory, orchestration, monitoring, security, and deployment.
- CCA-P is the final professional-level architecture pass: production Claude systems, agentic design, context engineering, evaluations, governance, security, cost, and operating model.

## Credential Scope Snapshot

| Credential | Level | Main Focus | Best For |
|---|---|---|---|
| Claude CCA-F | Foundations | Claude architecture basics, prompting, tools, MCP, Claude Code, context | Engineers and architects beginning serious Claude system design |
| Microsoft AB-100 | Architect | Business AI solution design, Copilot Studio, Dynamics 365, Power Platform, Foundry, governance, ROI | Solution architects and consultants |
| Microsoft AI-500 | Advanced/Expert | Production multi-agent systems in Azure, Foundry, Python, MCP, A2A, RAG, monitoring, security | AI engineers, architects, platform engineers |
| Claude CCA-P | Professional | Production Claude architecture, agentic workflows, evals, tool systems, governance | Senior AI architects and platform leads |

## Daily Time Budget

Minimum daily plan:

- 30 minutes concept review
- 45 minutes hands-on lab
- 20 minutes notes or flashcards
- 15 minutes practice questions

Strong daily plan:

- 60 minutes concept review
- 90 minutes hands-on lab
- 30 minutes architecture notes
- 30 minutes practice questions

Weekend plan:

- 2 to 4 hours capstone, mock exam, or repo implementation

## Core Concepts You Must Know

### Agent

An agent is an AI system that can interpret a goal, maintain context, call tools, and continue a workflow across steps. A production agent needs scope, identity, memory policy, tool permissions, observability, and stop conditions.

### Multi-Agent System

A multi-agent system uses more than one specialized agent. Common patterns:

- Sequential: one agent hands results to the next.
- Parallel: multiple agents work at the same time and merge results.
- Hub-and-spoke: a coordinator routes work to specialists.
- Supervisor-subagent: a higher-level agent plans and delegates.
- Peer-to-peer: agents negotiate or collaborate directly.
- Human-in-the-loop: humans approve, correct, or take over important actions.

### Tool Use

Tool use means the model asks an external function, API, database, file system, search system, or hosted tool to perform work. Good tool design requires:

- Clear tool name.
- Strict input schema.
- Least privilege.
- Error handling.
- Result validation.
- Audit logs.
- Human approval for risky actions.

### RAG

Retrieval-augmented generation uses search or retrieval to ground model output in source material. Good RAG design includes:

- Clean source data.
- Chunking strategy.
- Embeddings or hybrid retrieval.
- Metadata filters.
- Reranking.
- Citation discipline.
- Access control.
- Evaluation of retrieval and answer quality separately.

### MCP

Model Context Protocol is a standard for connecting AI systems to tools, APIs, databases, and context providers. For this repo, MCP is relevant because `mcp/db2_mcp.py` is already a DB2-style tool adapter.

### A2A

Agent2Agent is a pattern/protocol area for connecting agents to other agents. For AI-500, study agent discovery, capability routing, context isolation, shared state, and secure cross-agent communication.

### Context Management

Context is the working memory sent to the model. More context can help, but too much context increases cost and can reduce recall quality. Patterns:

- Sliding window.
- Summarization.
- Retrieval.
- Context compaction.
- Prompt caching.
- Memory stores.
- Session state.
- Semantic long-term memory.

### Evaluation

Evaluation is how you decide whether an AI system works. Do not rely on LLM self-confidence. Use objective gates:

- Tests pass.
- JSON schema validates.
- Citations verify.
- No critical review findings.
- Tool results are validated.
- Human approval for risky assumptions.

### Guardrails

Guardrails reduce risk before, during, and after generation:

- Input filtering.
- Prompt injection resistance.
- Tool call policy.
- Tool response validation.
- Output safety checks.
- PII handling.
- Tenant isolation.
- RBAC.
- Audit trails.

### Observability

Production AI systems need:

- Request IDs.
- Trace IDs.
- Token counts.
- Cost per workflow.
- Latency per stage.
- Tool calls.
- Tool errors.
- Retrieval scores.
- User feedback.
- Evaluation results.
- Drift detection.

## Microsoft AI-500 Objective Map

Microsoft AI-500 focuses on production multi-agent AI solutions.

Skills at a glance:

- Architect multi-agent solutions: 15-20%
- Develop multi-agent solutions in Azure: 30-35%
- Evaluate, optimize, and monitor multi-agent solutions: 20-25%
- Secure, govern, and deploy multi-agent solutions: 20-25%

Study emphasis:

- Microsoft Foundry.
- Microsoft Agent Framework.
- Python.
- Azure compute, networking, storage, and data services.
- MCP.
- RAG.
- LangGraph.
- Multi-agent orchestration.
- Memory and context.
- Observability.
- Guardrails.
- CI/CD and deployment.

## Microsoft AB-100 Objective Map

Microsoft AB-100 focuses on architecting AI-powered business solutions.

Skills at a glance:

- Plan AI-powered business solutions: 25-30%
- Design AI-powered business solutions: 25-30%
- Deploy AI-powered business solutions: 40-45%

Study emphasis:

- Microsoft 365 Copilot.
- Copilot Studio.
- Microsoft Foundry tools and models.
- Power Platform.
- Dynamics 365.
- Business process transformation.
- ROI and total cost of ownership.
- Build, buy, or extend decisions.
- ALM.
- Governance.
- Responsible AI.
- Data residency.
- Prompt manipulation defenses.
- Monitoring and telemetry.

## Claude CCA-F Study Map

Use this as the Claude Architect Foundations map:

- Claude prompting best practices.
- System prompts and instructions.
- XML-style structure and clear output requirements.
- Tool use and tool schemas.
- Client tools vs server tools.
- MCP and tool integration.
- Claude Code project configuration.
- Claude Code memory and instructions.
- Subagents.
- Hooks.
- Skills.
- Context windows and compaction.
- Evaluation basics.

## Claude CCA-P Study Map

Use this as the Claude Architect Professional map:

- Production Claude architecture.
- Agentic architecture patterns.
- Tool orchestration and permission boundaries.
- MCP server/client design.
- RAG and source grounding.
- Long-running workflows.
- Context engineering and memory.
- Evals and LLM-as-judge, with deterministic gates.
- Prompt lifecycle management.
- Security and governance.
- Observability and cost.
- Release gates and rollback.
- Enterprise adoption playbooks.

## 56-Day Daily Plan

### Week 1: Foundation Architecture And Prompting

Day 1 - Credential Orientation

- Learn: Read the scope snapshot above. Understand the difference between business architecture, technical multi-agent architecture, and Claude architecture.
- Lab: Run `python3 ai-native/repo_assistant.py inventory`.
- Deliverable: Create a one-page note: "My target role after these certs."
- Review: Explain AI-500 vs AB-100 vs CCA-F vs CCA-P in 5 bullets.

Day 2 - LLM System Design Basics

- Learn: Model, prompt, context, tool, agent, RAG, evaluation, guardrail.
- Lab: Draw this repo as an AI modernization system: legacy source -> brief -> prompt -> code -> tests -> review.
- Deliverable: `ai-native/architecture/study-architecture-notes.md` draft.
- Review: Write 10 flashcards from the Core Concepts section.

Day 3 - Prompt Engineering

- Learn: Direct instructions, role, task, context, constraints, examples, output schema.
- Lab: Improve a weak prompt for `apps/RPG/EMPCRUD.rpgle`.
- Deliverable: One prompt that produces a migration brief without generating code.
- Review: Identify three failure modes of vague prompts.

Day 4 - Structured Outputs

- Learn: JSON output, schemas, validation, retries, null handling.
- Lab: Design a JSON schema for a legacy migration brief.
- Deliverable: Example valid JSON and invalid JSON.
- Review: Explain why model output must be validated in code.

Day 5 - Tools And Function Calling

- Learn: Tool name, description, input schema, result validation, least privilege.
- Lab: Design a read-only DB2 table inventory tool for this repo.
- Deliverable: Tool spec with input and output JSON.
- Review: List five risks of broad SQL tools.

Day 6 - RAG Basics

- Learn: chunking, embeddings, metadata, retrieval, citations, access control.
- Lab: Design RAG for COBOL/RPG modernization docs.
- Deliverable: RAG design with sources, chunking, and access rules.
- Review: Explain when RAG is better than long context.

Day 7 - Weekly Review

- Learn: Re-read all Week 1 notes.
- Lab: Generate a migration brief for `apps/COBOL/FPANALYSIS.cob`.
- Deliverable: Save the brief as study notes.
- Review: Answer 25 practice questions you create yourself from this week.

### Week 2: Claude CCA-F Foundations

Day 8 - Claude Prompting Style

- Learn: Claude responds well to clear instructions, source boundaries, and structured sections.
- Lab: Convert a messy migration prompt into XML-style sections.
- Deliverable: `task`, `context`, `rules`, `output` prompt template.
- Review: Explain why delimiters reduce ambiguity.

Day 9 - Claude Tool Use

- Learn: Claude can call tools you define or server tools provided by Anthropic.
- Lab: Write a tool schema for `lookup_legacy_program(path)`.
- Deliverable: Tool schema plus two example tool results.
- Review: Explain client tool vs server tool.

Day 10 - MCP For Claude

- Learn: MCP standardizes how models connect to tools and data sources.
- Lab: Read `mcp/README.md` and map it to MCP concepts.
- Deliverable: DB2 MCP improvement list: auth, validation, timeout, read-only enforcement.
- Review: Why is MCP useful for legacy modernization?

Day 11 - Claude Code Instructions

- Learn: Project instructions guide Claude behavior across a repo.
- Lab: Review `AGENTS.md`.
- Deliverable: Add five possible future repo rules for AI modernization.
- Review: Explain why repo instructions are better than repeating prompts.

Day 12 - Claude Code Subagents

- Learn: Subagents isolate focused work in their own context.
- Lab: Design four subagents: inventory, migration brief, test generation, code review.
- Deliverable: Subagent names, responsibilities, and tool permissions.
- Review: When should a subagent not have write access?

Day 13 - Claude Code Hooks And Skills

- Learn: Hooks are deterministic automation; skills package repeatable instructions.
- Lab: Design a hook that runs tests after AI edits.
- Deliverable: Hook policy, not necessarily implementation.
- Review: Explain hook vs LLM self-review.

Day 14 - CCA-F Mock Review

- Learn: Review prompting, tools, MCP, Claude Code, context.
- Lab: Create a CCA-F concept map.
- Deliverable: 30-question practice quiz with answers.
- Review: Score yourself and list weak areas.

### Week 3: Microsoft AB-100 Planning Domain

Day 15 - AB-100 Role And Business Lens

- Learn: AB-100 is solution architecture for AI-driven business solutions.
- Lab: Pick a business process: legacy employee CRUD modernization.
- Deliverable: Business value statement and target users.
- Review: Explain the difference between business value and technical elegance.

Day 16 - Requirements Analysis

- Learn: Analyze task automation, analytics, decision-making, grounding data quality.
- Lab: Analyze `EMPCRUD.rpgle` as a business workflow.
- Deliverable: Requirement list: functional, data, security, operational.
- Review: Identify missing stakeholder questions.

Day 17 - AI Strategy

- Learn: Plan an AI adoption strategy with business outcomes, governance, and platform fit.
- Lab: Decide whether the modernization assistant should use Copilot Studio, Foundry, custom code, or Claude.
- Deliverable: Build/buy/extend decision table.
- Review: Explain why a model alone is not a solution.

Day 18 - Copilot Studio And Business Agents

- Learn: Copilot Studio agents, topics, actions, connectors, knowledge sources, prompt actions.
- Lab: Design a Copilot Studio agent for answering employee policy questions.
- Deliverable: Agent purpose, knowledge, actions, escalation path.
- Review: List when Copilot Studio is better than custom Python.

Day 19 - Foundry Models And Model Router

- Learn: Model selection, model routing, cost, quality, latency, risk.
- Lab: Design routing for: simple FAQ, code migration, architecture review, SQL lookup.
- Deliverable: Model router table.
- Review: Explain why self-confidence is not a release gate.

Day 20 - ROI And TCO

- Learn: Estimate ROI, implementation cost, run cost, support cost, risk reduction.
- Lab: Estimate modernization benefit for COBOL/RPG conversion.
- Deliverable: One-page ROI model.
- Review: Include time saved, defect risk, review cost, cloud/API cost.

Day 21 - Weekly AB-100 Planning Review

- Learn: Review AB-100 planning objectives.
- Lab: Create a planning deck outline for this repo's AI modernization program.
- Deliverable: 10-slide outline in Markdown.
- Review: 25 planning-domain questions.

### Week 4: Microsoft AB-100 Design And Deploy Domains

Day 22 - Design Business AI Solutions

- Learn: Solution architecture across Microsoft 365, Copilot Studio, Power Platform, Dynamics, Foundry.
- Lab: Design an end-to-end agentic business process for legacy modernization intake.
- Deliverable: Architecture text diagram.
- Review: Name each component and why it exists.

Day 23 - Agent Extensibility

- Learn: Custom models, Copilot Studio extensibility, MCP, computer use, Teams, SharePoint.
- Lab: Design a Copilot Studio agent that calls an MCP DB2 schema tool.
- Deliverable: Tool permission model and risk controls.
- Review: Explain prompt manipulation risk.

Day 24 - Dynamics 365 And Power Platform Fit

- Learn: Know where business apps and Power Platform AI features fit.
- Lab: Map a customer service use case and a finance/supply-chain use case.
- Deliverable: "When to use Dynamics/Power Platform vs custom app" table.
- Review: Write five architecture tradeoff questions.

Day 25 - Testing Business AI

- Learn: Agent testing, validation criteria, prompt best practices, end-to-end scenarios.
- Lab: Build a test matrix for an AI modernization assistant.
- Deliverable: 20 test cases: happy, edge, security, failure.
- Review: Explain deterministic test vs human review vs LLM judge.

Day 26 - ALM For AI Solutions

- Learn: ALM for agents, connectors, prompts, custom models, data, and Foundry Agents.
- Lab: Design dev/test/prod environments for this repo.
- Deliverable: ALM diagram and release gates.
- Review: Why are prompts production logic?

Day 27 - Responsible AI, Security, Governance

- Learn: Security, governance, model security, data residency, prompt manipulation, access controls, audit trails.
- Lab: Threat model the DB2 MCP tool.
- Deliverable: Threat table with mitigation.
- Review: Explain least privilege for agents.

Day 28 - AB-100 Mock Review

- Learn: Review plan, design, deploy objectives.
- Lab: Take Microsoft practice assessment if available; otherwise write 40 questions.
- Deliverable: Weak-area list.
- Review: Decide if AB-100 is ready or needs another week.

### Week 5: Microsoft AI-500 Architecture And Development

Day 29 - AI-500 Role And Prerequisites

- Learn: AI-500 expects production multi-agent experience, Foundry, Python, Azure services, MCP, RAG, LangGraph.
- Lab: Map your current repo gaps against AI-500 objectives.
- Deliverable: Gap table.
- Review: Pick three gaps to close through labs.

Day 30 - Multi-Agent Logical Architecture

- Learn: Decompose goals into workflows, agents, tools, control loops, human-in-the-loop.
- Lab: Design agents for legacy modernization: planner, code reader, converter, reviewer, tester.
- Deliverable: Agent responsibility matrix.
- Review: Define autonomy levels for each agent.

Day 31 - Agent Personas, Scope, Boundaries

- Learn: Personas, tool boundaries, authentication, communication protocols.
- Lab: Write system prompts for three agents with strict boundaries.
- Deliverable: Prompt pack.
- Review: Identify where a human must approve.

Day 32 - Memory Architecture

- Learn: session state, shared team state, long-term semantic memory, tenant isolation.
- Lab: Design memory for modernization sessions.
- Deliverable: Memory table: what to store, where, TTL, access.
- Review: Explain sliding-window amnesia and summary drift.

Day 33 - Multi-Agent RAG

- Learn: multi-agent knowledge integration, RAG, search, semantic search, MCP sources.
- Lab: Design RAG over legacy code, README files, and generated briefs.
- Deliverable: Retrieval pipeline.
- Review: Define retrieval quality metrics.

Day 34 - Tool Ecosystem

- Learn: function calling, specified tools, dynamic tools, MCP servers/clients, fallback.
- Lab: Improve `mcp/db2_mcp.py` design on paper for production readiness.
- Deliverable: API contract and failure modes.
- Review: What should happen when a tool returns bad data?

Day 35 - Weekly AI-500 Build Review

- Learn: Review architecture and development topics.
- Lab: Write a skeleton orchestration flow in pseudocode.
- Deliverable: `orchestrator.md` design.
- Review: 30 AI-500 questions focused on architecture and development.

### Week 6: Microsoft AI-500 Orchestration, Evaluation, Monitoring, Security

Day 36 - Orchestration Patterns

- Learn: hub-and-spoke, sequential, parallel, peer-to-peer, supervisor-subagent.
- Lab: Choose the best pattern for modernizing `EMPCRUD.rpgle`.
- Deliverable: Pattern decision record.
- Review: Explain why not every task needs many agents.

Day 37 - Human-In-The-Loop

- Learn: approval workflows, overrides, edge cases, escalation.
- Lab: Define approvals for DB writes, generated code, deployment, security exceptions.
- Deliverable: Approval matrix.
- Review: What actions are never automatic?

Day 38 - Caching And Cost

- Learn: prompt caching, semantic caching, response caching, token limits, loops, tool calls.
- Lab: Estimate cost for three agent reflection cycles vs one gated cycle.
- Deliverable: Cost control checklist.
- Review: Explain why replaying messages is not the same as running a model.

Day 39 - Evaluation

- Learn: evals for memory, knowledge, tools, prompts; human review; LLM-as-judge.
- Lab: Build eval criteria for COBOL function point modernization.
- Deliverable: Eval JSON schema.
- Review: Replace confidence scoring with objective gates.

Day 40 - Observability

- Learn: reliability, workflow failures, trace correlation, drift detection, quality regression, token/cost monitoring.
- Lab: Design telemetry for the modernization assistant.
- Deliverable: Metrics list and log schema.
- Review: Define p50/p95 latency, tool error rate, eval pass rate.

Day 41 - Security And Guardrails

- Learn: RBAC, identity, network boundaries, OAuth, Key Vault, secrets, custom guardrails.
- Lab: Add guardrail design for DB2 read-only discovery.
- Deliverable: Guardrail table for inputs, tool calls, tool results, outputs.
- Review: Explain prompt injection defense in one paragraph.

Day 42 - Deployment

- Learn: DTAP, blue/green, canary, rollback, IaC, testing strategy.
- Lab: Map a deployment path using existing Helm assets.
- Deliverable: Release checklist.
- Review: 40 AI-500 questions across all domains.

### Week 7: Claude CCA-P Professional Architecture

Day 43 - Production Claude Architecture

- Learn: Claude architecture means prompts, context, tools, MCP, evals, observability, governance, deployment.
- Lab: Design Claude-based modernization architecture for this repo.
- Deliverable: C4-style context and container text diagrams.
- Review: Compare Claude architecture to Microsoft Foundry architecture.

Day 44 - Advanced Prompt Lifecycle

- Learn: prompt versioning, templates, variables, test sets, rollout, rollback.
- Lab: Version the modernization prompt from `ai-native/prompts/modernization.md`.
- Deliverable: Prompt release checklist.
- Review: Why should prompt changes go through release gates?

Day 45 - Claude Tool And MCP Design

- Learn: tool definitions, result handling, MCP connector/server, allowlists, deny lists, OAuth.
- Lab: Design a Claude tool suite for legacy modernization.
- Deliverable: Tool catalog with risk level.
- Review: Which tools are safe read-only tools?

Day 46 - Context Engineering

- Learn: context windows, compaction, long context risks, memory, retrieval, context rot.
- Lab: Design context policy for a 1,000-file modernization repo.
- Deliverable: Context assembly algorithm.
- Review: Explain how to avoid summary drift.

Day 47 - Claude Code Operating Model

- Learn: project instructions, subagents, hooks, skills, SDK, permissions.
- Lab: Design `.claude/agents` and `.claude/skills` structure for this repo.
- Deliverable: File tree proposal.
- Review: What should be deterministic hook vs agent judgment?

Day 48 - Evals And Review

- Learn: production evals, regression datasets, LLM judge with rubric, deterministic checks.
- Lab: Expand `ai-native/evals/modernization-checklist.md` with certification-inspired gates.
- Deliverable: Evaluation matrix.
- Review: What are the limits of LLM-as-judge?

Day 49 - Claude CCA-P Mock Review

- Learn: Review CCA-P topics.
- Lab: Write a full architecture case study for this repo.
- Deliverable: 2-page case study.
- Review: 50 mixed Claude architecture questions.

### Week 8: Integrated Capstone And Exam Readiness

Day 50 - Capstone Scope

- Learn: A credible capstone proves multi-vendor architecture thinking.
- Lab: Select one capstone: function point calculator or employee CRUD modernization.
- Deliverable: Capstone brief.
- Review: Define success criteria.

Day 51 - Capstone Architecture

- Learn: Combine AB-100 business architecture, AI-500 technical architecture, Claude architecture.
- Lab: Write the full target architecture.
- Deliverable: Architecture decision record.
- Review: Identify security and governance controls.

Day 52 - Capstone Implementation Plan

- Learn: Convert architecture into tasks.
- Lab: Break implementation into issues: service, API, tests, AI workflow, evals, deployment.
- Deliverable: Backlog with priorities.
- Review: Identify dependencies and risks.

Day 53 - Capstone Testing And Evals

- Learn: Tests and evals are the proof layer.
- Lab: Write characterization tests from legacy behavior.
- Deliverable: Test plan with expected outputs.
- Review: Make sure the tests would catch wrong behavior.

Day 54 - Capstone Security Review

- Learn: Security review covers identity, data, prompts, tools, logs, secrets, tenant isolation.
- Lab: Threat model the capstone.
- Deliverable: Threat model and mitigations.
- Review: Mark any open high-risk items.

Day 55 - Full Mixed Mock

- Learn: Practice switching between vendors and roles.
- Lab: Create and answer 100 questions:
  - 25 CCA-F
  - 25 AB-100
  - 25 AI-500
  - 25 CCA-P
- Deliverable: Score report and weak-area plan.
- Review: Re-study weak areas only.

Day 56 - Final Readiness Gate

- Learn: Review official pages for latest exam updates.
- Lab: Run through exam sandbox/practice assessment where available.
- Deliverable: Exam order and dates.
- Review: Use the readiness checklist below.

## Readiness Checklists

### Claude CCA-F Ready

- [ ] I can write clear Claude prompts with source boundaries and output schemas.
- [ ] I can design safe tool schemas.
- [ ] I understand client tools, server tools, and MCP.
- [ ] I can explain Claude Code instructions, memory, hooks, skills, and subagents.
- [ ] I can manage context with compaction, retrieval, and summaries.
- [ ] I can design a basic evaluation checklist.

### Microsoft AB-100 Ready

- [ ] I can plan AI-powered business solutions from requirements.
- [ ] I can choose Copilot Studio, Foundry, Power Platform, Dynamics 365, or custom code.
- [ ] I can explain build, buy, or extend decisions.
- [ ] I can create ROI and TCO analysis.
- [ ] I can design agent extensibility with MCP and connectors.
- [ ] I can design ALM for agents, prompts, connectors, data, and models.
- [ ] I can design responsible AI, data residency, access controls, and audit trails.

### Microsoft AI-500 Ready

- [ ] I can architect multi-agent systems with clear agent boundaries.
- [ ] I can implement or explain orchestration patterns.
- [ ] I can design memory, context, RAG, MCP, and A2A integration.
- [ ] I can build tool ecosystems with validation and fallback.
- [ ] I can design evals for prompts, memory, knowledge, and tools.
- [ ] I can monitor reliability, drift, token use, cost, and trace correlation.
- [ ] I can secure and deploy multi-agent systems with CI/CD and rollback.

### Claude CCA-P Ready

- [ ] I can design production Claude systems end to end.
- [ ] I can choose models, prompts, tools, MCP, RAG, and memory patterns.
- [ ] I can design agentic workflows with permission boundaries.
- [ ] I can build release gates for prompts and evals.
- [ ] I can design observability, cost controls, and incident response.
- [ ] I can explain governance for enterprise adoption.
- [ ] I can defend architecture tradeoffs clearly.

## Practice Questions

### Mixed Questions

1. Why is LLM self-confidence a weak release gate?

Answer: The model can overrate itself. Use objective gates such as tests, schema validation, verified citations, tool result validation, and human approval.

2. When should you use RAG instead of sending all documents into context?

Answer: Use RAG when knowledge is large, private, changing, permission-scoped, or needs citations.

3. In AB-100, what is the difference between planning and deployment?

Answer: Planning defines requirements, AI strategy, ROI, data readiness, and build/buy/extend choices. Deployment covers monitoring, testing, ALM, responsible AI, governance, security, and compliance.

4. In AI-500, what is an example of a multi-agent orchestration pattern?

Answer: Supervisor-subagent, hub-and-spoke, sequential, parallel, peer-to-peer, or human-in-the-loop.

5. What makes a tool safe for agent use?

Answer: Narrow scope, strict schema, least privilege, authentication, validation, logging, error handling, and approval for risky actions.

6. Why is MCP important?

Answer: It standardizes how AI systems connect to external tools, databases, APIs, and context providers.

7. What is summary drift?

Answer: Summary drift happens when compressed conversation memory gradually loses or changes important facts.

8. What is a good guardrail strategy?

Answer: Use layered guardrails across user input, retrieval, tool calls, tool results, model output, and human approval.

9. What is a model router?

Answer: A routing layer that chooses the best model for a request based on task type, quality, latency, cost, risk, and capability.

10. Why are prompt changes production changes?

Answer: Prompts control behavior, tool use, data handling, output format, safety, cost, and quality.

## Repo Labs

### Lab A: Function Point Modernization

Source:

- `apps/COBOL/FPANALYSIS.cob`

Goal:

- Convert the formula into a tested Spring service.

Expected behavior:

```text
FC = 4*I + 5*R + 10*F + 7*X + 4*Q
I=4, R=2, F=1, X=1, Q=2 -> FC=51
```

Certification mapping:

- CCA-F: prompt and source-grounded brief.
- AB-100: business value and ROI.
- AI-500: eval gate and observability.
- CCA-P: production Claude modernization workflow.

### Lab B: Employee CRUD Modernization

Source:

- `apps/RPG/EMPCRUD.rpgle`
- `apps/RPG/EMPCRUD.CLP`
- `apps/RPG/EMPLOYEE.DDL`

Goal:

- Design a Spring service/API that preserves RPG CRUD behavior.

Required behavior:

- Create employee.
- Read employee by ID.
- Update employee.
- Delete employee.
- List employees ordered by ID.
- Preserve not-found behavior.
- Preserve SQL error handling intent.

Certification mapping:

- CCA-F: tool and MCP design.
- AB-100: business process and ALM.
- AI-500: multi-agent workflow, RAG, monitoring, security.
- CCA-P: production architecture and review gates.

### Lab C: DB2 MCP Safety

Source:

- `mcp/db2_mcp.py`

Goal:

- Turn the minimal DB2 adapter into a safe read-only discovery service design.

Required controls:

- Authentication.
- Read-only SQL enforcement.
- Query timeout.
- Row limit.
- Audit logging.
- Secret handling.
- Tenant isolation if multi-user.
- Error responses without leaking stack traces.

Certification mapping:

- AB-100: governance and compliance.
- AI-500: MCP, tool ecosystem, security, observability.
- CCA-P: Claude tool permission design.

## Final Exam Strategy

### For AB-100

Think like a business solution architect. Prefer answers that:

- Align AI with measurable business outcomes.
- Choose the right Microsoft platform component.
- Include governance, ALM, testing, and responsible AI.
- Consider data readiness, ROI, and stakeholder adoption.
- Avoid overbuilding custom code where standard Microsoft services fit.

### For AI-500

Think like a production multi-agent engineer/architect. Prefer answers that:

- Define agent roles and boundaries.
- Use objective evals and monitoring.
- Secure every tool and memory layer.
- Include Python/Foundry/Azure implementation realism.
- Control token cost, loops, concurrency, and failure recovery.
- Deploy with CI/CD, rollback, and environment separation.

### For Claude CCA-F

Think like a Claude system designer. Prefer answers that:

- Use clear prompts and structured context.
- Choose tool use when data is external, private, fresh, or computational.
- Understand MCP and Claude Code workflows.
- Manage context intentionally.
- Validate outputs.

### For Claude CCA-P

Think like a senior production architect. Prefer answers that:

- Balance quality, cost, latency, and risk.
- Use evals before prompt tuning.
- Govern tools, memory, and retrieval.
- Add observability and incident response.
- Treat prompts, agents, and tools as production assets.

## Official And Primary Sources

Microsoft:

- AI-500 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/ai-500
- Microsoft Certified: Multi-Agent AI Solutions Expert: https://learn.microsoft.com/en-us/credentials/certifications/multi-agent-ai-solutions-expert/
- AI-500 learning path: https://learn.microsoft.com/en-us/training/paths/aaai-1-architect-production-grade-multi-agent-ai-solutions/
- AB-100 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/ab-100
- Microsoft Certified: Agentic AI Business Solutions Architect: https://learn.microsoft.com/en-us/credentials/certifications/agentic-ai-business-solutions-architect/
- Microsoft practice assessments: https://learn.microsoft.com/en-us/credentials/certifications/practice-assessments-for-microsoft-certifications

Anthropic:

- Claude Certified Architect - Foundations access page: https://anthropic.skilljar.com/claude-certified-architect-foundations-access-request
- Claude prompting best practices: https://docs.anthropic.com/claude/prompt-library
- Claude prompt engineering overview: https://docs.anthropic.com/en/docs/build-with-claude/prompt-engineering/overview
- Claude tool use overview: https://docs.anthropic.com/en/docs/build-with-claude/tool-use/overview
- Claude MCP connector: https://docs.anthropic.com/en/docs/agents-and-tools/mcp-connector
- Claude Code MCP: https://docs.anthropic.com/en/docs/claude-code/mcp
- Claude Code subagents: https://docs.anthropic.com/en/docs/claude-code/sub-agents
- Claude Code hooks: https://docs.anthropic.com/en/docs/claude-code/hooks
- Claude Code skills: https://docs.anthropic.com/en/docs/claude-code/skills
- Claude context windows: https://docs.anthropic.com/en/docs/build-with-claude/context-windows
- Claude Code SDK: https://docs.anthropic.com/en/docs/claude-code/sdk
