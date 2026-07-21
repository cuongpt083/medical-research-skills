# Medical Research Skills — Project Context

This project is a composable skill system for AI-assisted medical research, literature review, drug intelligence, guideline lookup, and evidence synthesis.

When you work here, you operate in a safety-critical evidence domain. Use the skills in `.claude/skills/` and treat `skills/<skill>/SKILL.md` as the source of truth.

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

## Core research flow

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

## Available skills

Invoke the appropriate skill from `.claude/skills/` based on the task:

- `research-orchestrator` — start any medical research case.
- `clinical-question-formulation` — structure the clinical question before retrieval.
- `evidence-source-selection` — choose source classes and order.
- `literature-search` — find scholarly evidence.
- `guideline-research` — find authoritative clinical guidance.
- `drug-research` — drug approval, labeling, safety, efficacy, interactions.
- `emerging-evidence-research` — trials, preprints, horizon scanning.
- `citation-network-explorer` — expand from seed papers.
- `fulltext-retrieval` — resolve accessible full-text versions.
- `evidence-extraction` — extract structured facts from sources.
- `evidence-appraisal` — assess credibility and applicability.
- `evidence-synthesis` — combine evidence into calibrated claims.
- `citation-verification` — verify claims against cited sources.
- `medical-safety-guardrail` — final safety gate for clinically actionable output.

`medical-safety-guardrail` is mandatory whenever output may influence diagnosis, treatment, medication, screening, or patient-specific decisions.

## Non-negotiable rules

- Never fabricate a citation, DOI, PMID, guideline, trial ID, approval, or regulatory status.
- Never treat search rank as evidence rank.
- Never infer approval from publication alone.
- Never allow a preprint alone to support a clinical recommendation.
- Never hide meaningful disagreement among credible sources.
- Never convert population-level evidence silently into patient-specific advice.
- Never publish a final report containing material claims without a rendered `References` section and inline citation markers resolving to those references.

## Quality gates

Before finalizing any research output, ensure:

1. Question integrity — type explicit, context adequate, ambiguity resolved or declared.
2. Source-plan adequacy — authoritative sources included; regulatory questions include regulatory sources; guideline questions prioritize guideline issuers.
3. Evidence adequacy — directly addresses question or declares indirectness; contradictory evidence not omitted; source status known.
4. Claim traceability — every material claim maps to supporting evidence IDs.
5. Clinical safety — actionable content has completed safety review and uncertainty is visible.
6. Reference rendering — the final report includes a rendered `References` section with stable identifiers, inline citation markers for every material claim, and no fabricated or topic-related-but-non-supportive references.

## Stop / abstention

Return `INSUFFICIENT_EVIDENCE`, `UNVERIFIED_CURRENT_STATUS`, or `CLINICIAN_REVIEW_REQUIRED` when:

- Only low-quality or highly indirect evidence supports a high-stakes claim.
- A current regulatory or guideline fact cannot be verified.
- Evidence conflicts materially and cannot be reconciled.
- A key source is unavailable and the abstract is insufficient.
- Patient-specific advice would require missing clinical data.

## Repository workflow

- Edit skills only in `skills/<skill>/SKILL.md`.
- Regenerate agent configs with `python scripts/build-agent-configs.py`.
- Run tests with `python -m pytest tests/` before committing.
- Keep `execution/` provider-agnostic; adapters implement branded APIs.

## Cross-platform manifest

See `agent-skills.yaml` for a machine-readable manifest usable by Google Antigravity, custom agent SDKs, and other frameworks.
