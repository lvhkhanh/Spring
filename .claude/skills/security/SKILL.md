---
name: security
description: '**WORKFLOW SKILL** — Design, review, harden, and troubleshoot software and infrastructure security controls across development and production environments. USE FOR: secure architecture review, vulnerability triage, authentication and authorization design, secrets handling, dependency and configuration hardening, logging and monitoring controls, and defensive remediation planning. DO NOT USE FOR: offensive exploitation, bypassing security controls, covert access, credential theft, or any unauthorized intrusion or surveillance activity. INVOKES: file system tools for code and config review, terminal tools for validation and diagnostics, semantic search for security patterns, defensive best practices, and remediation guidance.'
---

# Security Engineering Skill

## Overview

This skill provides structured support for improving security across applications, APIs, services, infrastructure, and delivery workflows. It focuses on secure design, vulnerability reduction, least-privilege access, secrets protection, dependency and configuration hygiene, and practical remediation steps that lower real risk without disrupting maintainability.

## Key Capabilities

### Secure Design and Threat Review
- Review features and systems for trust boundaries, attack surface, and misuse paths
- Identify common classes of risk such as injection, broken access control, insecure defaults, and sensitive data exposure
- Apply least-privilege, defense-in-depth, and secure-by-default design principles
- Translate abstract security concerns into concrete engineering changes

### Authentication, Authorization, and Access Control
- Design or review login, session, token, and identity flows
- Validate role-based and policy-based access decisions
- Prevent privilege escalation and insecure direct object reference patterns
- Support service-to-service authorization and internal trust boundaries

### Secrets and Sensitive Data Handling
- Keep secrets out of source control, logs, and client-visible surfaces
- Improve credential, token, key, and certificate handling practices
- Review environment variables, secret managers, and rotation workflows
- Reduce unnecessary storage or propagation of sensitive data

### Dependency and Configuration Hardening
- Review package, container, runtime, and infrastructure configurations for risky defaults
- Triage dependency vulnerabilities and prioritize remediation paths
- Strengthen headers, transport settings, permissions, and network exposure
- Support secure baseline configuration for applications and environments

### Detection, Validation, and Remediation
- Investigate security findings, alerts, and suspicious failure modes
- Distinguish true risk from noisy findings or non-exploitable edge cases
- Propose the smallest effective fix that reduces exposure without hiding symptoms
- Define validation steps, regression coverage, and follow-up hardening work

## Usage Examples

### Review a New Feature for Security Risks
```
Review this file upload feature for authentication, authorization, validation,
storage, and malware-handling risks, then suggest concrete defensive changes.
```

### Triage a Vulnerability Report
```
Analyze this dependency alert and explain the real impact, exploitability,
short-term mitigation, and the safest upgrade path.
```

### Harden an API
```
Review this API for input validation, auth gaps, rate limiting, error leakage,
logging of sensitive data, and insecure default behavior.
```

### Improve Secrets Handling
```
Refactor this service so secrets are loaded safely, never logged,
and rotated through a managed secret workflow.
```

## Common Patterns

### Basic Security Review Flow
```text
1. Identify assets, trust boundaries, and entry points
2. Review auth, input handling, data flow, and sensitive operations
3. Check configuration, dependencies, and secret exposure
4. Rank findings by likelihood and impact
5. Apply the smallest effective remediation
6. Validate the fix and add regression protection where needed
```

### High-Value Control Checklist
```text
- least-privilege access
- secure defaults
- validated input and encoded output
- secret isolation and rotation
- strong transport and storage protections
- useful audit logging without leaking sensitive data
```

### Finding Triage Pattern
```text
For each finding, clarify:
- what can be reached or influenced
- what the attacker would need
- what the real impact is
- whether the issue is exploitable in this environment
- what mitigation or fix is proportionate
```

## Best Practices

- Prefer secure-by-default behavior so unsafe paths require explicit opt-in
- Minimize privileges, secret scope, and exposed surface area
- Treat validation, authorization, and logging as first-class design concerns
- Fix root causes instead of suppressing scanners without justification
- Keep remediation steps concrete, incremental, and verifiable
- Re-check nearby code paths when a vulnerability reveals a broader pattern
- Document justified exceptions and time-box temporary risk acceptance

## Troubleshooting

### Security Scanner Reported Many Findings
- Group findings by root cause and actual exposure
- Triage by exploitability and business impact instead of raw count
- Fix shared patterns first to remove clusters of related findings

### Sensitive Data Appears in Logs or Errors
- Trace where data is captured, transformed, and emitted
- Redact or remove secrets, tokens, and personal data from logs
- Review debug paths, exception handling, and third-party middleware output

### Access Control Behavior Is Inconsistent
- Compare route, service, and data-layer authorization checks
- Look for missing ownership validation or role drift across layers
- Centralize repeated permission logic where safe and practical

### Hardening Broke Legitimate Traffic
- Confirm what security change altered the behavior
- Narrow the control to the risky surface instead of disabling it broadly
- Add validation and rollout checks before reapplying the hardening change

## Integration Points

- **Application security**: auth flows, input validation, session handling, secure coding
- **Infrastructure security**: network exposure, IAM, runtime permissions, secret stores
- **Delivery workflows**: CI checks, dependency scanning, policy gates, release validation
- **Observability**: audit logs, alerting, incident triage, security monitoring
- **Related skills**: `ssl` for TLS and certificate-specific workflows, cloud and proxy skills for platform hardening
