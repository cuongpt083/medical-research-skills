"""Tests for YAML contracts and Python execution-layer skeletons."""

from __future__ import annotations

import py_compile
from pathlib import Path

import pytest
import yaml

REPO_ROOT = Path(__file__).resolve().parent.parent
CONTRACTS_DIR = REPO_ROOT / "contracts"
EXECUTION_DIR = REPO_ROOT / "execution"


def test_all_contract_yaml_files_are_valid() -> None:
    yaml_files = sorted(CONTRACTS_DIR.glob("*.yaml"))
    assert yaml_files, "No contract YAML files found"
    for path in yaml_files:
        with path.open(encoding="utf-8") as fh:
            data = yaml.safe_load(fh)
        assert isinstance(data, dict), f"{path.name} did not parse to a dict"
        assert "contracts" in data or "version" in data, f"{path.name} missing expected top-level key"


def test_provider_base_compiles() -> None:
    path = EXECUTION_DIR / "runtime" / "provider_base.py"
    py_compile.compile(str(path), doraise=True)


def test_all_provider_adapters_compile() -> None:
    for path in sorted((EXECUTION_DIR / "providers").glob("*.py")):
        py_compile.compile(str(path), doraise=True)


def test_normalized_record_has_expected_fields() -> None:
    """Smoke-test that the provider base data classes import and behave."""
    from execution.runtime.provider_base import CapabilityRequest, NormalizedRecord, utc_timestamp

    req = CapabilityRequest(capability="literature_search", query_text="apixaban atrial fibrillation")
    assert req.capability == "literature_search"
    assert req.query_hash()

    record = NormalizedRecord(
        record_id="r1",
        identifiers={},
        bibliographic={},
        links={},
        graph={},
        status={},
        provenance={},
    )
    assert record.record_id == "r1"
    assert utc_timestamp().endswith("Z")


def test_research_case_and_final_report_require_rendered_references() -> None:
    """The final report contract must carry a rendered references section and a ReferenceItem type."""
    core = yaml.safe_load((CONTRACTS_DIR / "core-contracts.yaml").read_text(encoding="utf-8"))
    research_case = core["contracts"]["ResearchCase"]
    assert "references" in research_case["fields"], "ResearchCase must declare a references field"

    run = yaml.safe_load((CONTRACTS_DIR / "research-run-contracts.yaml").read_text(encoding="utf-8"))
    assert "ReferenceItem" in run, "ReferenceItem contract must be defined"
    ref_item = run["ReferenceItem"]
    for field in ("id", "kind", "title", "identifiers", "publication_status", "provenance"):
        assert field in ref_item, f"ReferenceItem missing field: {field}"
    final_report = run["FinalReport"]
    assert "references" in final_report["required"], "FinalReport must require references"
    assert final_report["references"] == ["ReferenceItem"]


def test_orchestrator_skill_requires_rendered_references() -> None:
    """The orchestrator source-of-truth skill must mandate a rendered References section."""
    skill = (REPO_ROOT / "skills" / "research-orchestrator" / "SKILL.md").read_text(encoding="utf-8")
    assert "QG-6 Reference rendering" in skill
    assert "References" in skill
    assert "inline citation markers" in skill.lower()
    assert "rendered `References` section" in skill
