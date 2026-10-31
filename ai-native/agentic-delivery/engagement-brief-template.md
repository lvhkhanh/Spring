# Agentic Delivery Engagement Brief

Copy this file into a dated, versioned delivery folder before starting a new agentic workflow. Complete it with the business and technical owner; unknowns are not approvals.

## 1. Outcome

- **Workflow / decision to improve:**
- **Business owner:**
- **Technical owner:**
- **Users affected:**
- **Baseline:** current time, cost, quality, or risk measure:
- **Target and measurement period:**
- **Non-goals:**
- **Deadline / decision date:**

## 2. Scope and data

- **In-scope source artifacts:**
- **Authoritative data sources:**
- **Data classification and retention requirements:**
- **Tenant / role boundaries:**
- **Out-of-scope systems and actions:**
- **Known business-rule gaps:**

## 3. Agent and tool boundary

| Component | Purpose | Permissions | Failure handling | Human approval required? |
| --- | --- | --- | --- | --- |
| Planner | | Read-only | | |
| Retrieval / context | | Read-only | | |
| Tool(s) | | | | |
| Evaluator | | Read-only | | |
| Human reviewer | Approves business-rule assumptions and high-impact actions | N/A | Escalation owner | Yes |

Set explicit limits: maximum turns ___; tool calls ___; elapsed time ___; spend ___; retry policy ___.

## 4. Thin vertical slice

- **Representative user request:**
- **Expected result / artifact:**
- **Required source citations or provenance:**
- **Read-only path demonstrated:**
- **Write or destructive paths excluded from the slice:**
- **Fallback when the agent cannot proceed:**

## 5. Evaluation and release gates

| Measure | Baseline | Target | Test method | Owner |
| --- | --- | --- | --- | --- |
| Task correctness | | | | |
| Tool correctness | | | | |
| Safety / authorization | | | | |
| Latency | | | | |
| Cost | | | | |
| User acceptance | | | | |

- **Golden cases:**
- **Negative / prompt-injection cases:**
- **Tool-error and recovery cases:**
- **Release criteria:**
- **Rollback / disable condition:**

## 6. Operations and handover

- **Prompt, tool, model, and evaluation versions:**
- **Trace / audit-log location and retention:**
- **Monitoring owner and alert thresholds:**
- **Incident and escalation contacts:**
- **Runbook location:**
- **Reusable assets to return to the team:**
- **Handover acceptance date and owner:**
