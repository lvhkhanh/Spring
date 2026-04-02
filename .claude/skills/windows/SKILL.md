---
name: windows
description: '**WORKFLOW SKILL** — Create, configure, and troubleshoot Windows development and operations workflows. USE FOR: Windows shell usage with PowerShell or Command Prompt, package management, services, processes, file permissions, networking, system diagnostics, and developer environment setup. DO NOT USE FOR: non-Windows operating systems, hardware repair, or unrelated desktop UI walkthroughs unless explicitly requested. INVOKES: terminal commands, file system operations, service management, registry-aware configuration, and developer tooling setup.'
---

# Windows Skill

## Overview

This skill provides Windows-specific guidance for developers and operators working on local machines, remote Windows hosts, CI agents, and mixed Windows plus WSL environments. It focuses on practical command-line workflows, environment setup, diagnostics, automation, and security-conscious troubleshooting.

## Key Capabilities

### Setup & Environment Management
- Configure PowerShell, Command Prompt, environment variables, user profiles, and shell startup behavior
- Install developer tooling such as Git, VS Code, Python, Node.js, Java, and build tools
- Manage PATH updates, execution policy, certificates, and per-user versus machine-wide configuration
- Work effectively across native Windows, WSL, remote desktop sessions, and Windows-based CI runners

### Package Management
- Install, upgrade, and remove software with `winget`, `choco`, `scoop`, `msiexec`, and native installers
- Identify whether software should be installed per-user or system-wide
- Resolve PATH, package source, and installer privilege issues
- Prefer trusted package sources and silent installers for repeatable setup

### File Systems & Permissions
- Work with Windows paths, UNC shares, mapped drives, symbolic links, and junctions
- Manage file ownership and permissions with `icacls`, `takeown`, and PowerShell cmdlets
- Troubleshoot access problems involving NTFS permissions, inherited ACLs, and locked files
- Understand path translation between Windows and WSL

### Processes & Services
- Inspect and control processes with `Get-Process`, `tasklist`, `taskkill`, and Task Manager-compatible workflows
- Manage Windows services with `Get-Service`, `Set-Service`, `sc.exe`, and `services.msc`-equivalent commands
- Troubleshoot startup issues, background processes, scheduled tasks, and port conflicts
- Distinguish user-session apps from machine services when debugging

### Networking & Diagnostics
- Inspect IP configuration, routes, DNS, firewall state, and listening ports with `ipconfig`, `Get-NetIPConfiguration`, `netstat`, `Test-NetConnection`, and `Resolve-DnsName`
- Diagnose connectivity problems between Windows host, WSL, containers, VPNs, and remote systems
- Check proxies, certificates, Windows Firewall rules, and name resolution
- Troubleshoot SMB shares, RDP connectivity, and localhost forwarding behavior

### Automation & Troubleshooting
- Create repeatable PowerShell workflows for setup, diagnostics, and maintenance
- Gather logs and system data with Event Viewer-compatible commands and CLI tooling
- Identify permission, path, environment, and policy mismatches quickly
- Apply least-privilege and elevation-aware practices before using Administrator privileges

## Usage Examples

### Check Windows version and PowerShell edition
```powershell
systeminfo | findstr /B /C:"OS Name" /C:"OS Version"
$PSVersionTable
```

### Install packages with winget
```powershell
winget install --id Git.Git -e
winget install --id Microsoft.VisualStudioCode -e
```

### Inspect a Windows service
```powershell
Get-Service -Name wuauserv
Get-WinEvent -LogName System -MaxEvents 50
```

### Check file permissions
```powershell
Get-Acl C:\path\to\file | Format-List
icacls C:\path\to\file
```

### Check what is listening on a port
```powershell
netstat -ano | findstr :8080
Get-Process -Id <PID>
```

## Common Patterns

### Detect whether a command exists
```powershell
if (Get-Command winget -ErrorAction SilentlyContinue) {
  winget install --id Git.Git -e
} elseif (Get-Command choco -ErrorAction SilentlyContinue) {
  choco install git -y
}
```

### Persist an environment variable for the current user
```powershell
[Environment]::SetEnvironmentVariable("JAVA_HOME", "C:\Java\jdk-21", "User")
$env:JAVA_HOME = "C:\Java\jdk-21"
```

### Inspect network connectivity to a host and port
```powershell
Test-NetConnection github.com -Port 443
Resolve-DnsName github.com
```

### Translate paths between Windows and WSL
```powershell
wsl wslpath 'C:\Users\khanh\project'
wsl.exe
```

## Best Practices

- Prefer PowerShell for modern automation and scripting
- Check whether a task requires elevation before switching to Administrator
- Use package managers and silent install options for repeatable setup
- Distinguish between Windows paths and WSL/Linux paths before editing files
- Verify whether issues come from NTFS ACLs, file locks, or antivirus interference
- Use Event Viewer logs or `Get-WinEvent` alongside command output when debugging services
- Prefer trusted repositories, signed installers, and explicit package versions when possible
- Keep user-specific and machine-wide configuration changes separate

## Troubleshooting

### Permission problems
- Check whether the shell is elevated and whether the target is user-owned or system-owned
- Inspect ACLs with `Get-Acl` or `icacls`
- Consider Controlled Folder Access, antivirus, or corporate endpoint policy as possible blockers

### Command not found
- Verify `PATH`, terminal session state, and whether the tool was installed for the current user or all users
- Confirm whether the command exists only in PowerShell, only in Command Prompt, or only inside WSL
- Reopen the shell after package installs that modify environment variables

### Service failures
- Start with `Get-Service`, `sc query`, and relevant Event Viewer logs
- Check service account permissions, dependent services, bound ports, and config files
- Confirm whether the process should run as a service, a scheduled task, or a user-session app

### Network issues
- Check IP config with `ipconfig /all` and port listeners with `netstat -ano`
- Test DNS separately using `Resolve-DnsName`
- Verify firewall rules, VPN routes, proxy settings, and local loopback behavior

## Integration Points

- PowerShell and Command Prompt automation
- WSL-based development and Windows/Linux path bridging
- Developer tools such as Git, VS Code, Docker Desktop, and language runtimes
- Windows services, scheduled tasks, and CI runners
- Remote administration via RDP, WinRM, SSH, and shared folders
