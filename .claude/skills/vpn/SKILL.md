---
name: vpn
description: '**WORKFLOW SKILL** — Design, configure, troubleshoot, and operate VPN connectivity for users, services, and site-to-site networks. USE FOR: VPN client/server setup, WireGuard/OpenVPN/IPsec workflows, routing and DNS diagnostics, access control hardening, and operational runbooks. DO NOT USE FOR: unauthorized network access, bypassing security controls, or offensive network activity. INVOKES: terminal commands for networking diagnostics, file system tools for config/key management, semantic search for protocol-specific patterns and best practices.'
---

# VPN Configuration and Operations Skill

## Overview

This skill provides structured support for VPN setup and operations across common protocols, including WireGuard, OpenVPN, and IPsec/IKEv2. It focuses on secure configuration, reliable connectivity, route and DNS correctness, and repeatable troubleshooting for endpoint and site-to-site scenarios.

## Key Capabilities

### VPN Architecture and Planning
- Select suitable protocol based on performance, compatibility, and security needs
- Design client-to-site and site-to-site topologies
- Define address ranges, route propagation, and split/full tunnel strategy
- Plan identity, key/certificate lifecycle, and access boundaries

### Protocol Configuration
- Configure WireGuard peers, allowed IPs, and persistent keepalive
- Set up OpenVPN server/client profiles, TLS assets, and auth flows
- Configure IPsec/IKEv2 tunnels with phase 1/2 proposals
- Validate MTU/MSS and NAT traversal parameters

### Security and Access Controls
- Apply least-privilege access to internal subnets and services
- Rotate keys/certificates and revoke compromised credentials
- Enforce MFA/SSO integrations where available
- Harden endpoint and gateway firewall policies

### Connectivity Diagnostics
- Troubleshoot handshake failures, route conflicts, and DNS leaks
- Validate traffic paths with `ping`, `traceroute`, and interface checks
- Inspect logs and tunnel state counters for packet flow issues
- Diagnose performance bottlenecks caused by MTU, CPU, or encryption settings

### Operations and Automation
- Build repeatable setup scripts and provisioning steps
- Create incident runbooks for tunnel outage scenarios
- Integrate health checks and alerting for tunnel availability
- Document rollback procedures for configuration changes

## Usage Examples

### Create a basic WireGuard client config
```ini
[Interface]
PrivateKey = <client-private-key>
Address = 10.20.0.10/32
DNS = 10.20.0.2

[Peer]
PublicKey = <server-public-key>
Endpoint = vpn.example.com:51820
AllowedIPs = 10.0.0.0/8, 192.168.0.0/16
PersistentKeepalive = 25
```

### Bring up a WireGuard tunnel and verify routes
```bash
sudo wg-quick up wg0
wg show
ip route
ping -c 3 10.20.0.1
```

### OpenVPN connection test
```bash
sudo openvpn --config client.ovpn
# In another terminal:
ip addr
ip route
nslookup internal.service.local
```

### Capture VPN path diagnostics
```bash
ping -c 4 10.10.1.20
traceroute 10.10.1.20
dig +short internal.service.local
```

## Common Patterns

### Split tunnel policy
```text
Route only private networks through VPN:
- 10.0.0.0/8
- 172.16.0.0/12
- 192.168.0.0/16
Keep internet-bound traffic on local gateway unless policy requires full tunnel.
```

### Basic incident triage flow
```text
1. Confirm tunnel state (connected/handshake timestamps)
2. Verify client IP assignment and interface status
3. Check route table and DNS resolver settings
4. Validate server-side ACL/firewall rules
5. Test targeted subnet reachability
6. Collect logs and rollback recent changes if needed
```

### Secure key handling checklist
```text
- Store private keys outside source control
- Restrict file permissions on key material
- Rotate credentials on schedule and after incidents
- Revoke lost/stolen endpoints immediately
```

## Best Practices

- Prefer modern protocols and ciphers (for example, WireGuard or strong IKEv2 suites)
- Keep VPN configs environment-specific (`dev`, `staging`, `prod`)
- Separate user-access tunnels from service-to-service tunnels
- Use explicit route declarations and avoid overlapping CIDRs
- Set monitoring for handshake age, packet counters, and uptime
- Enforce change control and configuration backup before updates
- Test failover and disaster recovery paths regularly

## Troubleshooting

### Tunnel connects but no internal access
- Check `AllowedIPs`/routing on client and server
- Validate subnet ACLs, SG/NSG/firewall rules
- Confirm return route exists on destination side

### DNS resolution fails on VPN
- Verify pushed DNS server and search domain settings
- Check resolver order and split-DNS policy
- Test with `dig`/`nslookup` against intended DNS servers

### Intermittent disconnects
- Review keepalive and idle timeout settings
- Confirm NAT traversal and UDP reachability
- Inspect packet loss and path instability

### Slow throughput
- Tune MTU/MSS to avoid fragmentation
- Check endpoint CPU saturation and cipher overhead
- Evaluate nearest gateway region and peering path

## Integration Points

- **Protocols**: WireGuard, OpenVPN, IPsec/IKEv2
- **Identity**: Entra ID/Azure AD, Okta, LDAP/RADIUS, SSO/MFA providers
- **Cloud networking**: AWS, Azure, GCP site-to-site and client VPN gateways
- **Observability**: Syslog, Prometheus/Grafana, SIEM pipelines
- **Automation**: Bash, Ansible, Terraform for repeatable VPN provisioning
