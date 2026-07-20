# Medical Research Skills — Antigravity Workspace Overview

This repository is a composable skill system for AI-assisted medical research, literature review, drug intelligence, guideline lookup, and evidence synthesis based on Evidence-Based Medicine (EBM) standards.

---

## 🚀 How Antigravity Operates in this Workspace

1. **Skill Auto-Discovery**: All 14 skills in [skills/](file:///home/cuongpt/Workspaces/Personal/medical-research-skills/skills) are indexed via YAML frontmatter in `skills/<skill-name>/SKILL.md`.
2. **System Rules**: Global safety and pipeline directives are configured in [.gemini/rules.md](file:///home/cuongpt/Workspaces/Personal/medical-research-skills/.gemini/rules.md).
3. **Execution Layer**: Python adapters and tooling interfaces are available under [execution/](file:///home/cuongpt/Workspaces/Personal/medical-research-skills/execution). Run tests using `pytest tests/`.
4. **Data Contracts**: Shared data schemas (such as `ResearchCase`) are defined under [contracts/](file:///home/cuongpt/Workspaces/Personal/medical-research-skills/contracts).

---

## 📌 Core Workflow
```text
User Medical Question
  ↓
research-orchestrator
  ↓
clinical-question-formulation (PICO/PEO)
  ↓
evidence-source-selection
  ↓
literature-search / guideline-research / drug-research / emerging-evidence-research
  ↓
fulltext-retrieval → evidence-extraction → evidence-appraisal
  ↓
evidence-synthesis → citation-verification → medical-safety-guardrail
  ↓
Final Evidence Report (Artifact)
```
