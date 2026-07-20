#!/usr/bin/env python3
"""Sync agent-specific rule/skill files from skills/*/SKILL.md sources of truth.

Run from repository root:
    python scripts/build-agent-configs.py

Outputs:
    - agent-skills.yaml            (cross-platform machine-readable manifest)
    - .claude/skills/<skill>.md    (Claude Code explicit skills)
    - .cursor/rules/<skill>.mdc    (Cursor per-skill rule files)
"""

from __future__ import annotations

import re
import sys
from pathlib import Path
from typing import Any

try:
    import yaml
except ImportError as exc:  # pragma: no cover - build-time only
    raise SystemExit(
        "PyYAML is required. Install with: pip install pyyaml"
    ) from exc

REPO_ROOT = Path(__file__).resolve().parent.parent
SKILLS_DIR = REPO_ROOT / "skills"
AGENT_SKILLS_YAML = REPO_ROOT / "agent-skills.yaml"
CLAUDE_SKILLS_DIR = REPO_ROOT / ".claude" / "skills"
CURSOR_RULES_DIR = REPO_ROOT / ".cursor" / "rules"


def extract_first_paragraph(text: str) -> str:
    """Return the first non-empty paragraph after the H1 title.

    Falls back to the first paragraph under a 'Mission' or 'Purpose' section.
    """
    lines = text.splitlines()
    start = 0
    for i, line in enumerate(lines):
        if line.startswith("# Skill:") or line.startswith("# Skill "):
            start = i + 1
            break
    paragraph_lines: list[str] = []
    for line in lines[start:]:
        stripped = line.strip()
        if stripped.startswith("##"):
            break
        if stripped:
            paragraph_lines.append(stripped)
        elif paragraph_lines:
            break
    paragraph = " ".join(paragraph_lines).strip()
    if paragraph:
        return paragraph

    # Fallback: first paragraph under Mission or Purpose
    match = re.search(
        r"##\s*(?:1\.\s*)?(?:Mission|Purpose)\s*\n+(.*?)(?=\n##|\Z)",
        text,
        re.IGNORECASE | re.DOTALL,
    )
    if match:
        return " ".join(line.strip() for line in match.group(1).splitlines() if line.strip())
    return ""


def extract_trigger(text: str) -> str:
    """Return the first paragraph under a 'Trigger' section."""
    match = re.search(
        r"(?:##\s*2\.\s*Trigger|##\s*Trigger|##\s*When to use)\s*\n+(.*?)(?=\n##|\Z)",
        text,
        re.IGNORECASE | re.DOTALL,
    )
    if not match:
        return ""
    paragraph = " ".join(line.strip() for line in match.group(1).splitlines() if line.strip())
    paragraph = re.sub(r"^-\s+", "", paragraph)
    return paragraph


def load_skills() -> list[dict[str, Any]]:
    skills: list[dict[str, Any]] = []
    for skill_dir in sorted(SKILLS_DIR.iterdir()):
        if not skill_dir.is_dir():
            continue
        skill_file = skill_dir / "SKILL.md"
        if not skill_file.exists():
            print(f"WARNING: {skill_file} missing; skipping.", file=sys.stderr)
            continue
        content = skill_file.read_text(encoding="utf-8")
        skill_id = skill_dir.name
        mission = extract_first_paragraph(content)
        trigger = extract_trigger(content)
        skills.append(
            {
                "id": skill_id,
                "name": skill_id.replace("-", " ").title(),
                "description": mission,
                "trigger": trigger,
                "source": f"skills/{skill_id}/SKILL.md",
                "tags": ["medical-research", "evidence"],
            }
        )
    return skills


def write_agent_skills_yaml(skills: list[dict[str, Any]]) -> None:
    manifest = {
        "schema_version": "1.0",
        "project": "medical-research-skills",
        "description": (
            "Composable medical-research skill system for AI-assisted literature review, "
            "drug intelligence, guideline lookup, and evidence synthesis."
        ),
        "skills": skills,
        "platforms": {
            "cursor": {
                "root_rule": ".cursor/rules.md",
                "per_skill_rules": ".cursor/rules/*.mdc",
            },
            "claude_code": {
                "project_context": ".claude/CLAUDE.md",
                "per_skill_skills": ".claude/skills/*.md",
            },
            "github_copilot": {
                "instructions": ".github/copilot-instructions.md",
            },
        },
        "governance": {
            "source_of_truth": "skills/*/SKILL.md",
            "regenerate_command": "python scripts/build-agent-configs.py",
        },
    }
    AGENT_SKILLS_YAML.write_text(
        yaml.safe_dump(manifest, sort_keys=False, allow_unicode=True, width=120),
        encoding="utf-8",
    )
    print(f"Wrote {AGENT_SKILLS_YAML}")


def write_claude_skill(skill: dict[str, Any], content: str) -> None:
    CLAUDE_SKILLS_DIR.mkdir(parents=True, exist_ok=True)
    out = CLAUDE_SKILLS_DIR / f"{skill['id']}.md"
    frontmatter = {
        "name": skill["id"],
        "description": skill["description"],
        "trigger": skill["trigger"] or skill["description"],
        "tags": skill["tags"],
    }
    header = yaml.safe_dump(frontmatter, sort_keys=False, allow_unicode=True).strip()
    out.write_text(
        f"---\n{header}\n---\n\n"
        f"> Source of truth: `{skill['source']}`\n>\n"
        f"> This file is auto-generated. Edit `{skill['source']}` and run "
        f"`python scripts/build-agent-configs.py` to regenerate.\n\n{content}\n",
        encoding="utf-8",
    )


def write_cursor_rule(skill: dict[str, Any], content: str) -> None:
    CURSOR_RULES_DIR.mkdir(parents=True, exist_ok=True)
    out = CURSOR_RULES_DIR / f"{skill['id']}.mdc"
    frontmatter = {
        "description": skill["description"],
        "globs": [],
        "alwaysApply": False,
    }
    header = yaml.safe_dump(frontmatter, sort_keys=False, allow_unicode=True).strip()
    out.write_text(
        f"---\n{header}\n---\n\n"
        f"**Trigger:** {skill['trigger'] or skill['description']}\n\n"
        f"> Source of truth: `{skill['source']}`\n>\n"
        f"> This file is auto-generated. Edit `{skill['source']}` and run "
        f"`python scripts/build-agent-configs.py` to regenerate.\n\n{content}\n",
        encoding="utf-8",
    )


def generate_per_skill_files(skills: list[dict[str, Any]]) -> None:
    for skill in skills:
        content = (REPO_ROOT / skill["source"]).read_text(encoding="utf-8")
        write_claude_skill(skill, content)
        write_cursor_rule(skill, content)
    print(f"Wrote {len(skills)} Claude skills to {CLAUDE_SKILLS_DIR}")
    print(f"Wrote {len(skills)} Cursor rules to {CURSOR_RULES_DIR}")


def main() -> int:
    skills = load_skills()
    if not skills:
        print("No skills found.", file=sys.stderr)
        return 1

    write_agent_skills_yaml(skills)
    generate_per_skill_files(skills)
    return 0


if __name__ == "__main__":
    sys.exit(main())

