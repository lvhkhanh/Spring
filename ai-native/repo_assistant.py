#!/usr/bin/env python3
"""Offline helper for AI-native modernization workflows.

This script does not call an AI model. It inventories repo files, creates
source briefs, and assembles prompts that can be pasted into an assistant.
"""

from __future__ import annotations

import argparse
from dataclasses import dataclass
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]

LEGACY_SUFFIXES = {
    ".cob": "COBOL",
    ".cbl": "COBOL",
    ".rpgle": "RPGLE",
    ".clp": "CL",
    ".ddl": "DB2 DDL",
}

MODERN_SUFFIXES = {
    ".kt": "Kotlin",
    ".java": "Java",
    ".ts": "TypeScript",
    ".js": "JavaScript",
    ".py": "Python",
    ".yaml": "YAML",
    ".yml": "YAML",
}

SKIP_DIRS = {
    ".git",
    ".gradle",
    ".sfdx",
    ".vscode",
    "__pycache__",
    "build",
    "bin",
    "node_modules",
    "gradle",
}


@dataclass(frozen=True)
class SourceProfile:
    path: Path
    kind: str
    lines: int
    statements: list[str]
    db2_mentions: list[str]


def iter_repo_files() -> list[Path]:
    files: list[Path] = []
    for path in ROOT.rglob("*"):
        if not path.is_file():
            continue
        if any(part in SKIP_DIRS for part in path.relative_to(ROOT).parts):
            continue
        files.append(path)
    return sorted(files)


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8", errors="replace")


def classify(path: Path) -> str:
    suffix = path.suffix.lower()
    if suffix in LEGACY_SUFFIXES:
        return LEGACY_SUFFIXES[suffix]
    if suffix in MODERN_SUFFIXES:
        return MODERN_SUFFIXES[suffix]
    return "Other"


def find_statement_lines(text: str) -> list[str]:
    interesting_terms = (
        "select",
        "insert",
        "update",
        "delete",
        "display",
        "accept",
        "call",
        "perform",
        "compute",
        "exec sql",
        "dsply",
        "dcl-f",
        "dcl-s",
    )
    statements: list[str] = []
    for raw_line in text.splitlines():
        line = raw_line.strip()
        lower = line.lower()
        if any(term in lower for term in interesting_terms):
            statements.append(line)
    return statements[:40]


def find_db2_mentions(text: str) -> list[str]:
    terms = ("exec sql", "select ", "insert ", "update ", "delete ", "create table", "from ", "into ")
    mentions: list[str] = []
    for raw_line in text.splitlines():
        line = raw_line.strip()
        lower = line.lower()
        if any(term in lower for term in terms):
            mentions.append(line)
    return mentions[:40]


def profile_source(path: Path) -> SourceProfile:
    abs_path = (ROOT / path).resolve() if not path.is_absolute() else path.resolve()
    if not abs_path.exists():
        raise FileNotFoundError(abs_path)
    text = read_text(abs_path)
    return SourceProfile(
        path=abs_path.relative_to(ROOT),
        kind=classify(abs_path),
        lines=len(text.splitlines()),
        statements=find_statement_lines(text),
        db2_mentions=find_db2_mentions(text),
    )


def inventory() -> str:
    files = iter_repo_files()
    buckets: dict[str, list[Path]] = {}
    for path in files:
        kind = classify(path)
        if kind == "Other":
            continue
        buckets.setdefault(kind, []).append(path.relative_to(ROOT))

    lines = ["# Repository AI Inventory", ""]
    for kind in sorted(buckets):
        lines.append(f"## {kind}")
        for path in buckets[kind]:
            lines.append(f"- `{path}`")
        lines.append("")
    return "\n".join(lines).rstrip() + "\n"


def brief(path: Path) -> str:
    profile = profile_source(path)
    lines = [
        f"# Migration Brief: `{profile.path}`",
        "",
        f"- Source kind: {profile.kind}",
        f"- Line count: {profile.lines}",
        "",
        "## Observed Operations",
    ]
    if profile.statements:
        lines.extend(f"- `{statement}`" for statement in profile.statements)
    else:
        lines.append("- No obvious operation lines detected by the offline scanner.")

    lines.extend(["", "## DB2/File Mentions"])
    if profile.db2_mentions:
        lines.extend(f"- `{mention}`" for mention in profile.db2_mentions)
    else:
        lines.append("- No DB2-like statements detected by the offline scanner.")

    lines.extend(
        [
            "",
            "## Questions For Human Review",
            "- What business process owns this program?",
            "- What are the authoritative sample inputs and expected outputs?",
            "- Which DB2 tables/files are read-only and which are updated?",
            "- Are there batch schedules, 5250 screens, reports, or downstream jobs?",
            "- What modern target is preferred: Java/Spring, Kotlin/Spring, API-only, or UI plus API?",
            "",
            "## Recommended Next Step",
            "Use `python3 ai-native/repo_assistant.py prompt "
            f"{profile.path}` and ask an AI assistant to create a detailed modernization plan.",
        ]
    )
    return "\n".join(lines) + "\n"


def modernization_prompt(path: Path) -> str:
    abs_path = (ROOT / path).resolve() if not path.is_absolute() else path.resolve()
    source = read_text(abs_path)
    rel_path = abs_path.relative_to(ROOT)
    kind = classify(abs_path)
    return f"""You are a senior IBM i modernization architect.

Analyze this {kind} source from `{rel_path}` and produce a modernization plan for this repository.

Target repository context:
- Legacy examples live in `apps/COBOL/` and `apps/RPG/`.
- Spring/Kotlin examples live in `demo/` and `demo2/`.
- DB2 tool integration lives in `mcp/`.
- AI modernization workflow lives in `ai-native/`.

Include:
- Program purpose.
- Inputs and outputs.
- DB2 tables, files, reports, screens, and external dependencies.
- Business rules.
- Side effects.
- Error handling.
- Assumptions and unknowns.
- Recommended Java/Kotlin/Spring target design.
- Characterization tests required before conversion.
- Smallest safe vertical modernization slice.

Rules:
- Treat the source as the source of truth.
- Do not invent missing business rules.
- Mark uncertainty explicitly.
- Preserve behavior before refactoring.

<legacy_source>
{source}
</legacy_source>
"""


def main() -> int:
    parser = argparse.ArgumentParser(description="AI-native repo helper")
    subparsers = parser.add_subparsers(dest="command", required=True)
    subparsers.add_parser("inventory", help="Print an AI-oriented repository inventory")

    brief_parser = subparsers.add_parser("brief", help="Create a migration brief for a source file")
    brief_parser.add_argument("path", type=Path)

    prompt_parser = subparsers.add_parser("prompt", help="Create a modernization prompt for a source file")
    prompt_parser.add_argument("path", type=Path)

    args = parser.parse_args()

    if args.command == "inventory":
        print(inventory(), end="")
    elif args.command == "brief":
        print(brief(args.path), end="")
    elif args.command == "prompt":
        print(modernization_prompt(args.path), end="")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
