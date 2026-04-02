---
name: linux
description: '**WORKFLOW SKILL** — Create, configure, and troubleshoot Linux development and operations workflows. USE FOR: Linux shell usage, package management, services, processes, file permissions, networking, system diagnostics, and developer environment setup across common distributions. DO NOT USE FOR: non-Linux operating systems, hardware repair, or distro-specific desktop UI guidance unless explicitly requested. INVOKES: terminal commands, file system operations, service management, and configuration file editing.'
---

# Linux Skill

## Overview

This skill provides Linux-specific guidance for developers and operators working in servers, VMs, containers, WSL, and local development environments. It focuses on practical command-line workflows, environment setup, debugging, security-minded operations, and cross-distribution troubleshooting.

## Key Capabilities

### Setup & Environment Management
- Configure shell environments for Bash, Zsh, and POSIX-compatible workflows
- Manage users, groups, environment variables, dotfiles, and SSH access
- Install language runtimes, build tools, and developer dependencies
- Work effectively in local Linux, remote hosts, WSL, and containerized environments

### Package Management
- Install, upgrade, and remove software with `apt`, `dnf`, `yum`, `apk`, `zypper`, and `snap`
- Identify distro and package sources before applying changes
- Clean caches, resolve dependency conflicts, and verify installed packages
- Prefer native package managers before manual binary installation

### File Systems & Permissions
- Navigate Linux directory structures and standard paths such as `/etc`, `/var`, `/usr`, and `/opt`
- Manage file ownership and permissions with `chmod`, `chown`, `umask`, and ACL-aware workflows
- Inspect disk usage, mounts, bind mounts, and symbolic links
- Troubleshoot workspace visibility between host, VM, and container mounts

### Processes & Services
- Inspect and control processes with `ps`, `pgrep`, `top`, `htop`, `kill`, and `nice`
- Manage services and boot behavior with `systemctl`, `journalctl`, and init-compatible tools
- Debug startup failures, background jobs, ports, and process crashes
- Understand container-specific limitations when `systemd` is unavailable

### Networking & Diagnostics
- Inspect interfaces, routes, DNS, sockets, and firewall state with `ip`, `ss`, `ping`, `dig`, `curl`, and `traceroute`
- Diagnose connectivity issues between host, container, and remote systems
- Check open ports, listening services, proxies, and name resolution
- Troubleshoot VPN, SSH, and certificate-related command-line issues

### Automation & Troubleshooting
- Create repeatable Linux shell workflows for setup and maintenance
- Collect logs, system information, and command output for incident debugging
- Identify permission, path, dependency, and environment mismatches quickly
- Apply least-privilege and safe operational practices before using `sudo`

## Usage Examples

### Detect distro and version
```bash
cat /etc/os-release
uname -a
```

### Install packages on Debian/Ubuntu
```bash
sudo apt update
sudo apt install -y git curl build-essential
```

### Inspect a service and its logs
```bash
systemctl status nginx
journalctl -u nginx -n 100 --no-pager
```

### Check file ownership and permissions
```bash
ls -lah /path/to/file
namei -l /path/to/file
```

### See where a workspace is mounted
```bash
pwd
mount | grep /workspaces
df -h /workspaces
```

## Common Patterns

### Package manager detection
```bash
if command -v apt >/dev/null 2>&1; then
  sudo apt update && sudo apt install -y git curl
elif command -v dnf >/dev/null 2>&1; then
  sudo dnf install -y git curl
elif command -v apk >/dev/null 2>&1; then
  sudo apk add git curl
fi
```

### Find what is using a port
```bash
sudo ss -ltnp | grep :8080
```

### Verify mount source and destination
```bash
findmnt
findmnt /workspaces/Batch
cat /proc/mounts | grep /workspaces/Batch
```

### Check disk usage hotspots
```bash
du -sh ./*
df -h
```

## Best Practices

- Detect the Linux distribution before giving package or service commands
- Prefer idempotent, script-friendly commands for setup and automation
- Use `sudo` narrowly and only where required
- Check logs and exit codes before retrying commands blindly
- Preserve existing config files and back them up before major edits
- Prefer official repositories and signed packages when available
- Distinguish between host paths and container paths before changing mounted files
- Use `systemctl` and `journalctl` when available, but fall back gracefully in containers

## Troubleshooting

### Permission problems
- Check ownership with `ls -l` and path traversal permissions with `namei -l`
- Confirm whether the issue is Unix permissions, ACLs, SELinux/AppArmor, or container user mapping
- Test with the exact runtime user rather than assuming root behavior

### Command not found
- Verify `PATH` and shell startup files
- Check whether the package is installed and available for the current distro
- Confirm whether the tool exists only on the host or only inside a container

### Service failures
- Start with `systemctl status <service>` and `journalctl -u <service>`
- Verify config syntax, file permissions, listening ports, and dependent services
- In containers, confirm whether the process should run directly instead of via `systemd`

### Network issues
- Check interface state with `ip addr` and routing with `ip route`
- Test DNS separately from connectivity using `dig`, `nslookup`, or `getent hosts`
- Verify local listeners and firewalls before assuming a remote outage

## Integration Points

- Containers and dev containers running Linux userlands
- CI runners and remote Linux build agents
- SSH-based server administration and deployment workflows
- Developer tools such as Git, Docker, language runtimes, and package managers
- System services, cron jobs, and terminal-based automation
