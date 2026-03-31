---
name: python
description: '**WORKFLOW SKILL** — Create, refactor, debug, and optimize Python code and scripts. USE FOR: writing functions, classes, modules, tests, and tooling; implementing idiomatic Python patterns; applying best practices for maintainability and performance; debugging syntax and runtime issues; managing virtual environments and dependencies. DO NOT USE FOR: non-Python languages, low-level OS configuration, or infrastructure provisioning. INVOKES: file system tools for script creation/modification, terminal for environment commands, language analysis for linting and refactoring suggestions.'
---

# Python Development Skill

## Overview

This skill provides complete support for Python development tasks across script creation, module design, testing, refactoring, and debugging. It is optimized for clear, idiomatic code and fast iteration.

## Key Capabilities

### Code Generation
- Build Python scripts, modules, packages from plain-language requirements
- Create functions and classes with type hints and docstrings
- Implement common libraries: requests, pathlib, pandas, numpy, asyncio, SQLAlchemy, Flask/FastAPI

### Refactoring & Architecture
- Apply naming conventions (snake_case, PascalCase)
- Extract and organize logic into reusable functions/classes
- Create layers: CLI, service, persistence, adapter
- Split large files into packages and modules

### Testing & Quality
- Add pytest/unittest coverage and fixtures
- Write unit, integration, and regression tests
- Use mocking, parametrization, and hypothesis when needed
- Enforce linting: flake8, black, isort, mypy

### Debugging & Troubleshooting
- Identify syntax and exception stack traces
- Reason about state and control flow in loops and async code
- Fix dependency errors, import path issues, and environment setup
- Diagnose performance hotspots and memory issues

### Environment & Tooling
- Create/activate venv or conda environments
- Generate requirements.txt and pyproject.toml
- Handle package installation and lock files
- Setup pre-commit and CI checks for Python quality

## Usage Examples

### Quick script from requirement
```
Write a script to read all CSV files in a folder, normalize columns, and write a combined Parquet file.
```

### Refactor to functions
```
Refactor code that transforms raw API data into a function `normalize_user_data(data)` with validation and error handling.
```

### Add tests
```
Add pytest tests for `calculate_discount(price, quantity)` with edge cases for 0 and negative values.
```

### Fix import issue
```
The module fails with ModuleNotFoundError: myapp.utils. Check how to fix package structure and `PYTHONPATH`.
```

## Common Patterns

### Python CLI entrypoint
```python
if __name__ == '__main__':
    main()
```

### Data class usage
```python
from dataclasses import dataclass

@dataclass
class User:
    id: int
    name: str
    email: str
```

### Context manager
```python
with open('data.txt', 'r') as f:
    for line in f:
        process(line)
```

### Async function pattern
```python
async def fetch(url: str) -> str:
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as resp:
            return await resp.text()
```

## Best Practices

- Use descriptive names, clear function boundaries, and small modules
- Write tests first where practical (TDD)
- Keep dependency list minimal and version-pinned
- Use f-strings and built-in libraries for concise code
- Add type annotations and run `mypy` for checks
- Use `logging` instead of `print` in production code
- Ensure idempotent operations for scripts and tasks

## Troubleshooting

### Syntax / runtime
- `IndentationError`: consistent 4 spaces per level
- `TypeError`: check function signatures and argument types
- `ValueError`: validate input before processing

### Environment
- `ModuleNotFoundError`: check active venv and installed packages
- Version mismatch: lock requirements with `pip freeze > requirements.txt`

### Performance
- Use list/dict comprehensions to replace loops when possible
- Use `profile` or `cProfile` for hotspots
- For data processing, prefer `pandas` vectorized ops over Python loops

## Integration Points

- **Web frameworks**: Flask, FastAPI, Django
- **Data science**: pandas, numpy, scikit-learn
- **Async**: asyncio, aiohttp
- **Database**: SQLAlchemy, psycopg2, sqlite3
- **Testing**: pytest, hypothesis
- **Packaging**: setuptools, poetry, pipx
