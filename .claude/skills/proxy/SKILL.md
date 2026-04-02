---
name: proxy
description: '**WORKFLOW SKILL** — Design, configure, troubleshoot, and operate proxy infrastructure for client access and service routing. USE FOR: forward/reverse proxy setup, HTTP/HTTPS proxy policies, load balancing and routing rules, authentication controls, and proxy diagnostics. DO NOT USE FOR: bypassing security controls, unauthorized traffic interception, or offensive network operations. INVOKES: terminal commands for networking diagnostics, file system tools for proxy config updates, semantic search for proxy patterns and platform best practices.'
---

# Proxy Configuration and Operations Skill

## Overview

This skill provides structured support for proxy workflows across development and production environments. It covers forward proxies, reverse proxies, API gateway-style routing, TLS termination, authentication, observability, and incident response with a security-first approach.

## Key Capabilities

### Proxy Architecture and Design
- Choose between forward proxy, reverse proxy, or layered gateway patterns
- Design routing topology for internal services and external clients
- Plan high availability, failover, and scaling strategy
- Define trust boundaries and traffic flow constraints

### Forward Proxy Setup
- Configure outbound proxy for users, apps, and CI agents
- Apply allow/deny policies by domain, IP, method, or port
- Set up authenticated proxy access with user/group controls
- Manage environment variables (`HTTP_PROXY`, `HTTPS_PROXY`, `NO_PROXY`)

### Reverse Proxy and Load Balancing
- Configure host/path-based routing for upstream services
- Set TLS termination and upstream encryption settings
- Implement sticky sessions, retries, and health checks
- Manage header forwarding (`X-Forwarded-*`, real client IP propagation)

### Security and Compliance
- Enforce TLS best practices and certificate rotation
- Protect against open-proxy misconfiguration
- Apply rate limits, request size limits, and WAF-style rules
- Log access events for auditing and incident investigations

### Operations and Troubleshooting
- Diagnose connectivity, latency, DNS, and routing failures
- Investigate proxy error classes (`407`, `502`, `503`, `504`)
- Validate upstream health and timeout tuning
- Build runbooks and rollback procedures for safe changes

## Usage Examples

### Export proxy settings for CLI tools
```bash
export HTTP_PROXY=http://proxy.example.com:8080
export HTTPS_PROXY=http://proxy.example.com:8080
export NO_PROXY=localhost,127.0.0.1,.internal.example.com
```

### Test outbound proxy connectivity
```bash
curl -x http://proxy.example.com:8080 -I https://example.com
curl -x http://user:password@proxy.example.com:8080 https://api.ipify.org
```

### NGINX reverse proxy baseline
```nginx
server {
  listen 443 ssl;
  server_name app.example.com;

  location /api/ {
    proxy_pass http://backend-api:8080/;
    proxy_set_header Host $host;
    proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
    proxy_set_header X-Forwarded-Proto $scheme;
    proxy_read_timeout 60s;
  }
}
```

### Quick proxy diagnostics
```bash
curl -v https://app.example.com/health
dig +short app.example.com
traceroute app.example.com
```

## Common Patterns

### Environment proxy policy
```text
Use explicit proxy configuration per environment:
- dev: relaxed logging and lower traffic volume
- staging: production-like routing and auth policy
- prod: strict ACLs, rate limiting, and full observability
```

### Standard outage triage
```text
1. Confirm proxy process and listener ports are healthy
2. Verify DNS resolution and certificate validity
3. Check upstream service health and route mappings
4. Inspect recent config changes and deploy history
5. Analyze access/error logs for 4xx/5xx spikes
6. Roll back to last known-good config if needed
```

### Safe header forwarding checklist
```text
- Preserve original host where needed
- Forward client IP chain securely
- Strip untrusted inbound forwarding headers
- Avoid leaking internal topology headers
```

## Best Practices

- Avoid open-proxy behavior unless explicitly required and controlled
- Keep proxy configs in version control with change approvals
- Validate configs before reload (`nginx -t`, equivalent platform checks)
- Use short, explicit timeout and retry policies per upstream
- Separate auth, routing, and TLS concerns for maintainability
- Monitor p95/p99 latency, upstream failures, and saturation metrics
- Rotate certificates and secrets on a defined schedule

## Troubleshooting

### Proxy Authentication Required (407)
- Validate credentials, auth scheme, and user policy mappings
- Confirm clients are sending proxy auth headers correctly
- Check SSO/MFA integration status for proxy gateways

### Bad Gateway / Service Unavailable (502/503)
- Verify upstream target host/port and service health
- Review load balancer pools and health check thresholds
- Inspect connection exhaustion and worker limits

### Gateway Timeout (504)
- Increase upstream timeout only after root-cause analysis
- Check slow backend queries or dependency latency
- Tune keepalive and connection reuse settings

### SSL/TLS handshake errors
- Confirm cert chain, SAN names, and expiration dates
- Ensure compatible TLS versions and cipher suites
- Verify SNI behavior and upstream TLS expectations

## Integration Points

- **Proxy platforms**: NGINX, HAProxy, Squid, Envoy
- **Ingress/API edge**: Kubernetes Ingress, API gateways, service meshes
- **Identity**: LDAP, SSO, OIDC, enterprise auth providers
- **Observability**: Prometheus/Grafana, ELK/OpenSearch, SIEM pipelines
- **Automation**: Bash, Ansible, Terraform, CI/CD config validation
