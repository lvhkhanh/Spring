#!/usr/bin/env python3
"""Run all RPG-to-Java migration framework dry-run templates."""

from __future__ import annotations

import importlib.util
import json
from pathlib import Path


def load_dry_run(path: Path):
    spec = importlib.util.spec_from_file_location(path.stem, path)
    assert spec and spec.loader
    module = importlib.util.module_from_spec(spec)
    module.__spec__ = spec
    import sys
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module.dry_run


def main() -> int:
    base_dir = Path(__file__).resolve().parent
    templates_dir = base_dir / "templates"

    dry_run_microsoft = load_dry_run(templates_dir / "microsoft_agent_framework_rpg_to_java.py")
    dry_run_langgraph = load_dry_run(templates_dir / "langgraph_rpg_to_java.py")
    dry_run_crewai = load_dry_run(templates_dir / "crewai_rpg_to_java.py")

    outputs = {
        "MicrosoftAgentFramework": dry_run_microsoft(),
        "LangGraph": dry_run_langgraph(),
        "CrewAI": dry_run_crewai(),
    }

    output_path = base_dir / "framework_dry_run_outputs.json"
    output_path.write_text(json.dumps(outputs, indent=2))
    print(f"Wrote consolidated dry-run output to {output_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
