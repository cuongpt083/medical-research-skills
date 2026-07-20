"""Tests for agent-specific configuration files and the cross-platform manifest."""

from __future__ import annotations

import subprocess
import sys
from pathlib import Path

import pytest
import yaml

REPO_ROOT = Path(__file__).resolve().parent.parent
SKILLS_DIR = REPO_ROOT / "skills"
AGENT_SKILLS_YAML = REPO_ROOT / "agent-skills.yaml"
CLAUDE_DIR = REPO_ROOT / ".claude"
CLAUDE_PROJECT = CLAUDE_DIR / "CLAUDE.md"
CLAUDE_SKILLS_DIR = CLAUDE_DIR / "skills"
CURSOR_DIR = REPO_ROOT / ".cursor"
CURSOR_RULES = CURSOR_DIR / "rules.md"
CURSOR_SKILL_RULES_DIR = CURSOR_DIR / "rules"
GITHUB_DIR = REPO_ROOT / ".github"
COPILOT_INSTRUCTIONS = GITHUB_DIR / "copilot-instructions.md"
BUILD_SCRIPT = REPO_ROOT / "scripts" / "build-agent-configs.py"


@pytest.fixture
def manifest() -> dict:
    with AGENT_SKILLS_YAML.open(encoding="utf-8") as fh:
        return yaml.safe_load(fh)


@pytest.fixture
def skill_dirs() -> list[Path]:
    return sorted(p for p in SKILLS_DIR.iterdir() if p.is_dir() and (p / "SKILL.md").exists())


def test_all_skill_specs_exist(skill_dirs: list[Path]) -> None:
    for skill_dir in skill_dirs:
        assert (skill_dir / "SKILL.md").is_file(), f"Missing SKILL.md in {skill_dir}"


def test_manifest_exists_and_is_valid_yaml(manifest: dict) -> None:
    assert manifest["schema_version"] == "1.0"
    assert manifest["project"] == "medical-research-skills"
    assert "skills" in manifest
    assert len(manifest["skills"]) >= 1


def test_manifest_covers_all_skills(manifest: dict, skill_dirs: list[Path]) -> None:
    manifest_ids = {s["id"] for s in manifest["skills"]}
    dir_ids = {p.name for p in skill_dirs}
    assert manifest_ids == dir_ids


def test_manifest_descriptions_and_triggers(manifest: dict) -> None:
    for skill in manifest["skills"]:
        assert skill["id"], f"Skill missing id: {skill}"
        assert skill["source"] == f"skills/{skill['id']}/SKILL.md"
        # Every skill should have at least a description or a trigger
        assert skill["description"] or skill["trigger"], (
            f"Skill {skill['id']} has neither description nor trigger"
        )


def test_claude_project_context_exists() -> None:
    assert CLAUDE_PROJECT.is_file()
    content = CLAUDE_PROJECT.read_text(encoding="utf-8")
    assert "Medical Research Skills" in content
    assert "evidence governance invariant" in content.lower()


def test_claude_skills_generated_for_all(manifest: dict) -> None:
    for skill in manifest["skills"]:
        skill_file = CLAUDE_SKILLS_DIR / f"{skill['id']}.md"
        assert skill_file.is_file(), f"Missing Claude skill file: {skill_file}"
        content = skill_file.read_text(encoding="utf-8")
        assert content.startswith("---")
        assert "name:" in content
        assert f"skills/{skill['id']}/SKILL.md" in content


def test_cursor_root_rules_exists() -> None:
    assert CURSOR_RULES.is_file()
    content = CURSOR_RULES.read_text(encoding="utf-8")
    assert "Medical Research Skills" in content
    assert "Non-negotiable rules" in content


def test_cursor_per_skill_rules_generated(manifest: dict) -> None:
    for skill in manifest["skills"]:
        rule_file = CURSOR_SKILL_RULES_DIR / f"{skill['id']}.mdc"
        assert rule_file.is_file(), f"Missing Cursor rule file: {rule_file}"
        content = rule_file.read_text(encoding="utf-8")
        assert content.startswith("---")
        assert "description:" in content
        assert f"skills/{skill['id']}/SKILL.md" in content


def test_copilot_instructions_exists() -> None:
    assert COPILOT_INSTRUCTIONS.is_file()
    content = COPILOT_INSTRUCTIONS.read_text(encoding="utf-8")
    assert "Medical Research Skills" in content
    assert "Stop / abstention" in content


def test_build_script_is_runnable() -> None:
    result = subprocess.run(
        [sys.executable, str(BUILD_SCRIPT)],
        cwd=REPO_ROOT,
        capture_output=True,
        text=True,
        check=True,
    )
    assert "Wrote" in result.stdout
