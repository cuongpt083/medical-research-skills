# Medical Research Skills — Project Rules

This repository is a composable skill system for AI-assisted medical research, literature review, drug intelligence, guideline lookup, and evidence synthesis.

When working in this project, you are operating inside a safety-critical domain. Follow the rules below, consult the per-skill files in `.cursor/rules/*.mdc`, and treat `skills/<skill>/SKILL.md` as the source of truth.

## 1. Core design principles

1. Separate **scientific reasoning** from **tool/provider implementation**.
2. Select sources based on the **question type**, not a fixed list of databases.
3. Treat retrieval, appraisal, synthesis, and verification as distinct stages.
4. Enforce **claim-to-source traceability**.
5. Distinguish peer-reviewed evidence, guidelines, regulatory evidence, trials, and preprints.
6. **Never** act as the final clinical authority.

## 2. Evidence governance invariant

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

## 3. Core research flow

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

## 4. Skill catalog

| Skill | When to invoke |
|---|---|
| `research-orchestrator` | Any medical literature research, evidence comparison, guideline lookup, drug intelligence, emerging-evidence tracking, or conflicting-claims appraisal. |
| `clinical-question-formulation` | Before evidence retrieval, whenever the question is clinical, therapeutic, diagnostic, prognostic, etiologic, safety-related, or drug-related. |
| `evidence-source-selection` | After question formulation and before research execution. |
| `literature-search` | Source plan requires primary studies, systematic reviews, meta-analyses, diagnostic/prognostic studies, epidemiologic evidence, or background literature. |
| `guideline-research` | Standard-of-care, recommended management, screening, diagnosis, prevention, treatment pathway, monitoring, or “what do guidelines say?” questions. |
| `drug-research` | Approval, indication, dosing, contraindications/warnings, safety signals, interactions, efficacy, off-label or investigational uses. |
| `emerging-evidence-research` | Latest/newest treatments, active trials, pipeline drugs, preprints, conference findings, horizon scanning. |
| `citation-network-explorer` | A seed paper is known, keyword search feels incomplete, historical evolution or related clusters are needed. |
| `fulltext-retrieval` | Downstream task needs more than metadata/abstract: extraction, verification, appraisal, guideline recommendation extraction, regulatory wording. |
| `evidence-extraction` | Transform source documents into structured, source-traceable evidence facts. |
| `evidence-appraisal` | Evaluate methodological credibility and applicability using question- and design-appropriate criteria. |
| `evidence-synthesis` | Combine appraised evidence into calibrated, traceable conclusions. |
| `citation-verification` | Verify every material claim is supported by the cited source at the required specificity. |
| `medical-safety-guardrail` | Final gate before clinically actionable output is delivered. |

`medical-safety-guardrail` is mandatory whenever output may influence diagnosis, treatment, medication, screening, or patient-specific decisions.

## 5. Non-negotiable rules

- **Never** fabricate a citation, DOI, PMID, guideline, trial ID, approval, or regulatory status.
- **Never** treat search rank as evidence rank.
- **Never** infer approval from publication alone.
- **Never** allow a preprint alone to support a clinical recommendation.
- **Never** hide meaningful disagreement among credible sources.
- **Never** convert population-level evidence silently into patient-specific advice.

## 6. Language calibration

- Use `shows/proves` only when justified by strong design and context.
- Prefer `was associated with` for non-causal observational evidence.
- Use `suggests`, `may`, or `preliminary` for uncertain/emerging evidence.
- Distinguish statistical from clinical significance.
- Label source status explicitly: peer-reviewed, preprint, guideline, regulatory, trial registry.

## 7. Quality gates (must pass before finalizing)

1. **Question integrity** — question type explicit; population/context adequate; ambiguity resolved or declared.
2. **Source-plan adequacy** — authoritative sources included; regulatory questions include regulatory sources; guideline questions prioritize guideline issuers; preprints not sole evidence for clinical recommendations.
3. **Evidence adequacy** — evidence directly addresses question or indirectness declared; contradictory evidence not omitted; source status known.
4. **Claim traceability** — every material claim maps to supporting evidence IDs.
5. **Clinical safety** — clinically actionable content has completed safety review and uncertainty is visible.

## 8. Stop / abstention conditions

Do not produce a definitive conclusion when:

- Only low-quality or highly indirect evidence is found for a high-stakes claim.
- A current regulatory or guideline fact cannot be verified.
- Evidence conflicts materially and cannot be reconciled.
- A key source is unavailable and the abstract is insufficient for the requested appraisal.
- Patient-specific advice would require missing clinical data.

Return `INSUFFICIENT_EVIDENCE`, `UNVERIFIED_CURRENT_STATUS`, or `CLINICIAN_REVIEW_REQUIRED` with the reason.

## 9. Working with this repository

- Edit skill specifications in `skills/<skill>/SKILL.md` only.
- Regenerate agent config files with `python scripts/build-agent-configs.py`.
- Validate with `python -m pytest tests/` before committing.
- Keep the Python execution layer (`execution/`) provider-agnostic; adapters implement branded APIs, skills call capabilities.

## 10. Cross-platform manifest

See `agent-skills.yaml` for the machine-readable skill manifest that can be consumed by other agent frameworks (Google Antigravity, custom agent SDKs, etc.).

