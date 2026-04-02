---
name: devops
description: '**WORKFLOW SKILL** — Design, implement, and troubleshoot DevOps workflows for delivery, infrastructure, and operations. USE FOR: CI/CD pipelines, infrastructure as code, deployment automation, environment management, release strategies, observability, and operational reliability. DO NOT USE FOR: application feature development without delivery or operations context, cloud-specific guidance that belongs to a dedicated platform skill, or ad hoc scripting without automation/release goals. INVOKES: file system edits for pipeline and config files, terminal for build/deploy tooling, and semantic search for infrastructure and delivery patterns.'
---

# DevOps Skill

## Overview

This skill supports modern DevOps practices across build, test, release, infrastructure, monitoring, and operational troubleshooting. It focuses on repeatable delivery, safe change management, environment consistency, and reliable systems. Use it when the problem involves getting software built, deployed, observed, or operated well.

## Key Capabilities

### CI/CD Pipeline Design
- Create and maintain pipelines for build, test, security checks, packaging, and deployment
- Structure workflows for pull requests, mainline builds, releases, and hotfixes
- Separate fast feedback stages from slower integration and deployment stages
- Improve pipeline readability, reuse, caching, and failure diagnostics

### Infrastructure as Code
- Design repeatable infrastructure workflows with Terraform, Bicep, ARM, CloudFormation, Helm, or similar tools
- Manage environments, variables, secrets references, and state handling carefully
- Keep infrastructure definitions versioned, reviewable, and promotion-friendly
- Reduce configuration drift through declarative automation

### Deployment & Release Management
- Implement blue-green, rolling, canary, and feature-flag-aware release strategies
- Coordinate application, database, and configuration changes safely
- Build rollback, smoke-test, and post-deploy verification steps into delivery workflows
- Manage artifact versioning, release promotion, and environment parity

### Reliability & Operations
- Improve service readiness with health checks, alerts, dashboards, runbooks, and incident-oriented diagnostics
- Analyze deployment failures, flaky pipelines, and configuration mismatches
- Strengthen operational safety with approvals, guarded rollouts, and blast-radius awareness
- Automate routine maintenance and recovery steps where appropriate

### Security & Compliance in Delivery
- Integrate secrets management, least privilege, dependency scanning, SAST/DAST, and policy checks
- Avoid embedding credentials in code, config, images, or pipeline logs
- Track auditability of changes, deployments, and approvals
- Balance delivery speed with governance requirements

## Usage Examples

### Create a GitHub Actions pipeline
```yaml
name: ci

on:
  pull_request:
  push:
    branches: [main]

jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-node@v4
        with:
          node-version: 20
          cache: npm
      - run: npm ci
      - run: npm test
```

### Run Terraform plan and apply
```bash
terraform init
terraform fmt -check
terraform validate
terraform plan -out=tfplan
terraform apply tfplan
```

### Deploy with a rolling strategy in Kubernetes
```yaml
strategy:
  type: RollingUpdate
  rollingUpdate:
    maxUnavailable: 0
    maxSurge: 1
```

## Common Patterns

### Pipeline layering
```text
1. Lint and unit tests
2. Build/package artifact
3. Security and policy checks
4. Integration or environment validation
5. Deploy
6. Smoke test and monitor
```

### Environment promotion
```text
dev -> test -> staging -> production

Promote the same artifact when possible instead of rebuilding for each environment.
```

### Safe deployment pattern
```text
1. Validate configuration
2. Deploy incrementally
3. Run health checks
4. Observe metrics and logs
5. Roll forward or roll back decisively
```

### Secrets handling
```text
Prefer:
- secret stores
- short-lived credentials
- environment-specific injection

Avoid:
- hardcoded secrets
- secrets in build logs
- long-lived shared credentials
```

## Best Practices

- Keep pipelines deterministic, observable, and fast enough for frequent use
- Prefer declarative automation over manual release steps
- Promote immutable artifacts across environments when possible
- Make deployments verifiable with health checks, smoke tests, and telemetry
- Treat infrastructure, pipeline config, and operational scripts as version-controlled code
- Isolate environment-specific settings from shared pipeline logic
- Design rollback and recovery paths before incidents force them
- Optimize for small, reversible changes over large risky releases

## Troubleshooting

### Pipeline failures
- Check whether the failure is code, environment, credentials, cache, or runner related
- Reproduce locally when feasible, but verify differences between local and CI environments
- Inspect logs for the first real error instead of downstream noise

### Deployment problems
- Confirm artifact version, configuration values, secrets, and target environment
- Check readiness probes, startup logs, migrations, and dependency availability
- Verify whether the new version is healthy before scaling traffic toward it

### Infrastructure drift or apply errors
- Compare desired state, actual state, and recent manual changes
- Review provider credentials, state locking, resource naming, and dependency ordering
- Avoid forceful recovery steps until the state model is understood

### Weak observability
- Ensure logs, metrics, traces, and alerts cover deployment boundaries and critical paths
- Add correlation IDs and deployment markers where possible
- Make dashboards reflect both system health and recent change activity

## Integration Points

- CI/CD systems such as GitHub Actions, GitLab CI, Azure DevOps, and Jenkins
- Infrastructure tools such as Terraform, Bicep, Helm, Kubernetes, and container build systems
- Secret stores and identity systems for secure automation
- Monitoring and incident tooling including logs, metrics, traces, and alerting platforms
- Release workflows involving artifacts, registries, approvals, and environment promotion
