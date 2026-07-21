# Medical Research Skills — GitHub Copilot / Codex Instructions

This repository is a composable skill system for AI-assisted medical research, literature review, drug intelligence, guideline lookup, and evidence synthesis.

When generating or editing code here, you are working in a safety-critical evidence domain. Follow the framework below and consult `skills/<skill>/SKILL.md` for the authoritative specification of each skill.

## Core principles

1. Separate scientific reasoning from tool/provider implementation.
2. Select sources based on the question type, not a fixed list of databases.
3. Treat retrieval, appraisal, synthesis, and verification as distinct stages.
4. Enforce claim-to-source traceability.
5. Distinguish peer-reviewed evidence, guidelines, regulatory evidence, trials, and preprints.
6. Never act as the final clinical authority.

## Evidence governance invariant

For every material clinical claim, preserve an auditable chain:

```text
source text
  → extracted fact + locator
  → evidence item
  → appraisal
  → synthesized claim
  → claim-level citation verification
  → safety review
```

A broken chain must lower confidence, trigger further research, or block publication of the claim as established fact.

## Research flow

```text
User Question
  ↓
research-orchestrator
  ↓
clinical-question-formulation
  ↓
evidence-source-selection
  ↓
literature-search / guideline-research / drug-research / emerging-evidence-research
  ↓
fulltext-retrieval
  ↓
evidence-extraction
  ↓
evidence-appraisal
  ↓
evidence-synthesis
  ↓
citation-verification
  ↓
medical-safety-guardrail
  ↓
Final Evidence Report
```

## Skill catalog

Use the matching skill whenever the task fits:

- `research-orchestrator` — coordinate end-to-end medical research cases.
- `clinical-question-formulation` — structure clinical questions before retrieval.
- `evidence-source-selection` — choose source classes and retrieval order.
- `literature-search` — discover biomedical scholarly evidence.
- `guideline-research` — locate and verify authoritative clinical guidance.
- `drug-research` — therapeutic and regulatory drug intelligence.
- `emerging-evidence-research` — trials, preprints, and horizon scanning.
- `citation-network-explorer` — expand from seed papers.
- `fulltext-retrieval` — resolve accessible full-text versions.
- `evidence-extraction` — extract structured, source-traceable facts.
- `evidence-appraisal` — assess credibility and applicability.
- `evidence-synthesis` — combine evidence into calibrated claims.
- `citation-verification` — verify claims against sources.
- `medical-safety-guardrail` — final gate for clinically actionable output.

`medical-safety-guardrail` is mandatory whenever output may influence diagnosis, treatment, medication, screening, or patient-specific decisions.

## Non-negotiable rules

- Never fabricate a citation, DOI, PMID, guideline, trial ID, approval, or regulatory status.
- Never treat search rank as evidence rank.
- Never infer approval from publication alone.
- Never allow a preprint alone to support a clinical recommendation.
- Never hide meaningful disagreement among credible sources.
- Never convert population-level evidence silently into patient-specific advice.
- Never publish a final report containing material claims without a rendered `References` section and inline citation markers resolving to those references.

## Language calibration

- Use `shows/proves` only when justified by strong design and context.
- Prefer `was associated with` for non-causal observational evidence.
- Use `suggests`, `may`, or `preliminary` for uncertain/emerging evidence.
- Distinguish statistical from clinical significance.
- Label source status explicitly: peer-reviewed, preprint, guideline, regulatory, trial registry.

## Quality gates

Before finalizing research output:

1. Question integrity — explicit type, adequate context, ambiguity resolved or declared.
2. Source-plan adequacy — authoritative sources included; regulatory questions include regulatory sources; guideline questions prioritize guideline issuers.
3. Evidence adequacy — directly addresses question or declares indirectness; contradictory evidence not omitted; source status known.
4. Claim traceability — every material claim maps to supporting evidence IDs.
5. Clinical safety — actionable content has completed safety review and uncertainty is visible.
6. Reference rendering — the final report includes a rendered `References` section with stable identifiers, inline citation markers for every material claim, and no fabricated or topic-related-but-non-supportive references.

## Stop / abstention

Do not produce a definitive conclusion when:

- Only low-quality or highly indirect evidence supports a high-stakes claim.
- A current regulatory or guideline fact cannot be verified.
- Evidence conflicts materially and cannot be reconciled.
- A key source is unavailable and the abstract is insufficient.
- Patient-specific advice would require missing clinical data.

Return `INSUFFICIENT_EVIDENCE`, `UNVERIFIED_CURRENT_STATUS`, or `CLINICIAN_REVIEW_REQUIRED` with the reason.

## Repository workflow

- Edit skill specs in `skills/<skill>/SKILL.md` only.
- Regenerate agent configs with `python scripts/build-agent-configs.py`.
- Validate with `python -m pytest tests/` before committing.
- Keep `execution/` provider-agnostic; adapters implement branded APIs, skills call capabilities.

## Cross-platform manifest

See `agent-skills.yaml` for a machine-readable skill manifest usable by Google Antigravity, custom agent SDKs, and other frameworks.
