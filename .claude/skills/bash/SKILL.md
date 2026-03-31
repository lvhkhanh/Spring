---
name: bash
description: '**WORKFLOW SKILL** — Create, modify, debug, and optimize Bash scripts and shell automation. USE FOR: writing shell scripts for task automation; managing files/directories; orchestrating command-line tools; handling text processing and pipelines; debugging shell syntax and runtime issues; implementing shell best practices. DO NOT USE FOR: non-shell programming languages, GUI application logic, cloud-specific orchestration outside shell context. INVOKES: terminal command snippets, file system edits, scripting patterns.'
---

# Bash Shell Scripting

## Overview

This skill provides full support for Bash (and POSIX-like shell) scripting, from simple utilities to complex automation workflows. It focuses on robust scripts, error handling, portability, and debugging.

## Key Capabilities

### Script Creation & Automation
- Generate Bash scripts from natural-language requirements
- Create reusable functions and libraries
- Implement automation workflows with loops, conditionals, and functions
- Create cron-ready scripts for scheduled tasks

### File and Process Management
- Manage files and directories (create, move, remove, backup)
- Parse and manipulate text files using grep, awk, sed, cut, sort
- Use pipelines effectively for streaming data between commands
- Manage processes, background jobs, and signals

### Error Handling & Debugging
- Add `set -euo pipefail` for safer script execution
- Validate inputs and required environment variables
- Add logging, dry-run modes, and verbose flags
- Debug using `set -x`, `trap`, and manual tests

### Best Practices Implementation
- Use descriptive variable and function names
- Avoid code duplication with helper functions
- Quote variables to handle spaces and globbing
- Handle edge cases and non-zero exit codes

### Portability & Compatibility
- Write POSIX-compliant constructs when possible
- Avoid Bash-specific extensions unless explicitly required
- Check script compatibility across Linux, macOS, and BSD shells

## Usage Examples

### Basic file processing script
```
Create a Bash script that:
- Finds all `.log` files in `/var/log/app`
- Compresses each file with `gzip`
- Moves compressed files to `/backup/logs`
- Keeps the 7 most recent archives and removes older ones
```

### Argument parsing with flags
```
Add parsing for options:
- `-d|--dir` for input directory
- `-o|--output` for output directory
- `-n|--dry-run` for dry-run mode
- `-h|--help` to display usage
```

### Cron-safe maintenance script
```
Generate a script suitable for cron that:
- Sources `/etc/profile`
- Sets a lockfile to prevent concurrent runs
- Sends status logs to `/var/log/maintenance.log`
```

## Common Patterns

### Robust initialization
```bash
#!/usr/bin/env bash
set -euo pipefail
IFS=$'\n\t'

script_name=$(basename -- "$0")

usage() {
  cat <<EOF
Usage: $script_name [OPTIONS]
  -h | --help   Show this help
EOF
}
```

### Argument parsing
```bash
parse_args() {
  while [[ $# -gt 0 ]]; do
    case "$1" in
      -d|--dir)
        input_dir="$2"; shift 2;;
      -o|--output)
        output_dir="$2"; shift 2;;
      -n|--dry-run)
        dry_run=true; shift;;
      -h|--help)
        usage; exit 0;;
      *)
        echo "Unknown option: $1" >&2; usage; exit 1;;
    esac
  done
}
```

### Validation and checks
```bash
validate() {
  [[ -d "$input_dir" ]] || { echo "Input directory does not exist: $input_dir" >&2; exit 1; }
  mkdir -p "$output_dir"
}
```

### Safe command execution helper
```bash
run_cmd() {
  echo "+ $*"
  if $dry_run; then
    return 0
  fi
  eval "$@"
}
```

## Best Practices

- Always quote variables: `"$var"`
- Use `$()` for command substitution instead of backticks
- Avoid using `ls` or `echo` for parsing filenames (use `find` with `-print0` and `xargs -0`)
- Check command exit codes and handle failures explicitly
- Use `trap` to clean up temporary files and resources
- Keep functions small and testable
- Include usage/help output for user guidance

## Troubleshooting

### Common Issues
- **Permission denied**: check script execute bit and file ownership
- **Command not found**: ensure dependencies are installed and path is correct
- **Globbing issues**: quote variables, use `shopt -s nullglob` when needed
- **Whitespace handling**: avoid unquoted variable expansion

### Debug Steps
1. Run with `bash -x script.sh` to trace commands
2. Add `set -x` temporarily for section-specific debugging
3. Validate with shellcheck: `shellcheck script.sh`
4. Reproduce with minimal input data

## Integration Points

- **CI/CD tools**: Jenkins, GitHub Actions, GitLab CI
- **Cloud CLI tools**: aws-cli, gcloud, az
- **Containers**: Docker, Kubernetes init containers
- **Logging/Monitoring**: syslog, journald, custom log collectors
- **Task schedulers**: cron, systemd timers
