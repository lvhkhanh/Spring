---
name: uv
description: '**WORKFLOW SKILL** — Create, manage, and optimize Python projects with `uv`, including environments, dependencies, scripts, and reproducible workflows. USE FOR: initializing Python projects, managing `pyproject.toml`, syncing dependencies, creating virtual environments, running tools with `uv`, handling lockfiles, and replacing slower `pip` or ad-hoc environment flows. DO NOT USE FOR: non-Python package ecosystems, generic Python coding with no environment or dependency workflow involved, or infrastructure tasks unrelated to Python tooling. INVOKES: file system tools for project/config changes, terminal for `uv` commands and environment setup, and language analysis for Python packaging and workflow guidance.'
---

# uv Python Workflow Skill

## Overview

This skill supports Python development workflows built around `uv`, with an emphasis on fast dependency resolution, reproducible environments, clean project setup, and modern `pyproject.toml`-based tooling. It is for projects that want a streamlined alternative to mixed `pip`, `venv`, and manual dependency management workflows.

## Key Capabilities

### Project Initialization
- Create new Python applications, libraries, and tooling projects with `uv`
- Set up `pyproject.toml` for modern packaging and tool configuration
- Establish clean project layout for source code, tests, and scripts
- Add Python version constraints and project metadata consistently

### Dependency & Lockfile Management
- Add, remove, and update dependencies with `uv`
- Maintain reproducible environments with lockfiles and synchronized installs
- Separate runtime, development, and optional dependency groups cleanly
- Replace ad-hoc `pip install` flows with tracked project dependencies

### Environment Management
- Create and use virtual environments through `uv`
- Sync environments to match project dependency state
- Run commands inside the correct environment without fragile shell setup
- Help teams standardize local Python execution across machines

### Tooling & Command Workflows
- Run linters, formatters, test suites, and scripts through `uv run`
- Configure workflows for `pytest`, `ruff`, `mypy`, and other Python tools
- Set up repeatable local development and CI-friendly commands
- Reduce setup friction for contributors and automation

### Migration & Troubleshooting
- Migrate projects from `pip`, `requirements.txt`, `venv`, or mixed setups to `uv`
- Diagnose environment drift, resolver conflicts, and lockfile confusion
- Fix interpreter mismatches and dependency-group issues
- Simplify inconsistent project tooling into one coherent workflow

## Usage Examples

### Initialize a new project
```text
Set up a new Python project using `uv` with a `src/` layout, pytest, and ruff.
Create the project files and recommend the basic commands for local development.
```

### Add dependencies cleanly
```text
Update this project to use `uv` for dependency management.
Move the current packages into `pyproject.toml` and separate dev dependencies properly.
```

### Standardize team workflow
```text
Create a `uv`-based workflow so the team can run tests, linting, and scripts consistently without manual virtualenv activation.
```

### Fix environment issues
```text
This project sometimes installs different dependency versions on different machines.
Use `uv` to make the environment reproducible and explain the likely cause.
```

## Common Patterns

### Initialize a project
```bash
uv init
```

### Add dependencies
```bash
uv add requests
uv add --dev pytest ruff
```

### Sync the environment
```bash
uv sync
```

### Run tools in project context
```bash
uv run pytest
uv run ruff check .
uv run python -m my_package
```

### Create a one-off tool environment
```bash
uvx ruff check .
```

## Best Practices

- Prefer `pyproject.toml` as the single source of truth for project metadata and dependencies
- Keep runtime and development dependencies separated clearly
- Commit lockfiles when the project needs reproducible installs across machines or CI
- Use `uv run` instead of relying on manually activated environments
- Keep Python version requirements explicit in the project configuration
- Standardize contributor workflows around a small set of documented `uv` commands
- Migrate incrementally when replacing legacy `requirements.txt` or shell-based setup flows
- Avoid mixing multiple package-management approaches unless there is a clear reason

## Troubleshooting

### Dependencies differ across machines
- Check whether the project is using a committed lockfile consistently
- Verify Python version constraints and interpreter selection
- Re-sync the environment instead of manually installing packages

### Commands run against the wrong interpreter
- Confirm the project is being executed through `uv run`
- Check local interpreter discovery and configured Python version
- Remove assumptions that a manually activated shell environment is always present

### Dependency resolution fails
- Look for incompatible version constraints or conflicting dependency groups
- Simplify overly broad pins before forcing workarounds
- Revisit optional and dev dependency boundaries

### Mixed old and new tooling causes confusion
- Remove duplicate sources of dependency truth where possible
- Prefer one workflow for install, sync, and command execution
- Document the new `uv` commands that replace the old process

### CI and local behavior differ
- Ensure both use the same `uv` commands and lockfile expectations
- Pin the Python version intentionally
- Avoid hidden machine-specific setup outside the project config

## Integration Points

- **Python project files**: `pyproject.toml`, lockfiles, source layout, test layout
- **Test tools**: pytest, hypothesis, coverage
- **Quality tools**: ruff, mypy, black
- **Execution**: `uv run`, script entry points, module execution
- **Migration sources**: `requirements.txt`, `venv`, `pip`, Poetry, pip-tools
- **Automation**: CI pipelines, local setup scripts, contributor onboarding flows
