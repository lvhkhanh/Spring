---
name: ssl
description: '**WORKFLOW SKILL** — Configure, validate, troubleshoot, and operate SSL/TLS certificates and secure transport settings across development and production environments. USE FOR: certificate creation and renewal, CSR and key management, HTTPS enablement, TLS policy configuration, chain and hostname validation, mTLS workflows, and SSL/TLS handshake debugging. DO NOT USE FOR: bypassing certificate verification without justified short-lived debugging need, weakening transport security for convenience, or offensive interception of traffic. INVOKES: terminal tools for certificate and handshake inspection, file system tools for key/cert/config updates, semantic search for platform-specific TLS patterns and security best practices.'
---

# SSL and TLS Operations Skill

## Overview

This skill provides structured support for SSL/TLS workflows across applications, APIs, proxies, load balancers, and internal services. It covers certificate lifecycle management, HTTPS configuration, chain validation, mutual TLS, protocol and cipher policy decisions, and troubleshooting of handshake or trust failures with a security-first mindset.

## Key Capabilities

### Certificate Lifecycle Management
- Generate private keys, CSRs, self-signed certificates, and signed certificate requests
- Manage certificate issuance, renewal, rotation, and replacement workflows
- Validate expiration dates, subject alternative names, issuer chains, and key usage
- Organize certificate assets safely across local, CI, and production environments

### HTTPS and TLS Configuration
- Configure TLS for web servers, reverse proxies, app servers, and API gateways
- Enable secure redirects, SNI, and hostname-based certificate selection
- Choose supported protocol versions and cipher policies appropriate to the environment
- Configure keystores, truststores, PEM bundles, and platform-specific certificate formats

### Mutual TLS and Trust Management
- Set up client-certificate authentication for service-to-service communication
- Configure trust anchors, CA bundles, and certificate verification rules
- Diagnose truststore mismatches, missing intermediates, and chain order problems
- Support internal PKI and public CA based workflows

### Validation and Diagnostics
- Inspect certificates and chains with `openssl`, `curl`, and platform tooling
- Debug hostname mismatch, expired cert, untrusted issuer, and incomplete chain errors
- Analyze handshake failures caused by protocol mismatch, cipher negotiation, or SNI issues
- Verify endpoint behavior from client, proxy, and upstream perspectives

### Security and Operations
- Protect private keys and limit file permissions and distribution scope
- Plan renewal automation and alerting before expiration windows
- Support zero-downtime certificate rotation and rollback planning
- Document safe exceptions for development while preserving strong defaults in shared environments

## Usage Examples

### Validate a Remote Certificate
```bash
openssl s_client -connect app.example.com:443 -servername app.example.com </dev/null
openssl x509 -in cert.pem -noout -text
```

### Generate a CSR and Private Key
```bash
openssl req -new -newkey rsa:2048 -nodes \
  -keyout server.key \
  -out server.csr \
  -subj '/CN=app.example.com'
```

### Check HTTPS with curl
```bash
curl -vI https://app.example.com/health
curl --cacert ca.pem https://internal-api.example.com/status
```

### Configure NGINX TLS
```nginx
server {
  listen 443 ssl http2;
  server_name app.example.com;

  ssl_certificate     /etc/nginx/certs/fullchain.pem;
  ssl_certificate_key /etc/nginx/certs/privkey.pem;

  location / {
    proxy_pass http://app_upstream;
  }
}
```

## Common Patterns

### Basic Certificate Validation Flow
```text
1. Confirm hostname and port
2. Inspect presented certificate and SAN values
3. Verify expiration and issuer chain
4. Check protocol and cipher negotiation
5. Confirm truststore or CA bundle on the client side
6. Re-test after config or certificate changes
```

### Safe Renewal Workflow
```text
1. Issue or obtain the replacement certificate early
2. Validate chain, SANs, and expiration metadata
3. Stage the certificate in the target environment
4. Reload or rotate with rollback prepared
5. Verify from external and internal clients
6. Retire old assets securely after cutover
```

### Common Error Mapping
```text
- hostname mismatch: SAN/CN does not match requested host
- certificate expired: cert validity window has ended
- unable to get local issuer certificate: missing CA or intermediate chain
- handshake failure: protocol, cipher, SNI, or mTLS mismatch
```

## Best Practices

- Prefer modern TLS versions and disable obsolete protocols unless a controlled exception is required
- Keep private keys restricted, encrypted where appropriate, and out of source control
- Use full certificate chains when required by the serving platform
- Automate renewal and add alerting before expiration deadlines
- Test certificate changes from the same trust context used by real clients
- Avoid `--insecure` or trust bypasses except for short-lived local diagnostics
- Record certificate ownership, renewal path, and rollback steps for operational continuity

## Troubleshooting

### Browser or Client Reports Certificate Is Not Trusted
- Check whether the full chain is being served
- Verify the issuing CA exists in the client trust store
- Confirm internal PKI roots are distributed to the relevant environment

### Hostname Mismatch Errors
- Inspect SAN entries instead of relying on CN alone
- Confirm the requested host matches the certificate presented through SNI
- Check reverse proxy and load balancer certificate selection rules

### Handshake Failures
- Compare supported TLS versions and cipher suites on both sides
- Verify whether client certificates are required for the endpoint
- Check for missing SNI, incompatible proxy settings, or TLS termination mistakes

### Renewed Certificate Still Does Not Appear
- Confirm the correct file paths, secrets, or keystore entries were updated
- Reload or restart the serving component if hot reload is not supported
- Check whether an upstream proxy, CDN, or load balancer is still serving the old certificate

## Integration Points

- **Certificate tools**: OpenSSL, keytool, certbot, platform CA utilities
- **Serving platforms**: NGINX, Apache, HAProxy, Kubernetes Ingress, cloud load balancers
- **Application stacks**: Java keystores, Node.js TLS, Python requests, .NET certificate stores
- **Trust infrastructure**: internal PKI, public CAs, truststores, secret managers
- **Operations workflows**: CI/CD deployment checks, expiration monitoring, incident response, rotation runbooks
