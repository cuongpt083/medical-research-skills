# Medical Research Skills

A composable skill system for AI-assisted medical research, literature review, drug intelligence, guideline lookup, and evidence synthesis.

## Design goals

1. Separate **scientific reasoning** from **tool/provider implementation**.
2. Select sources based on the **question type**, not a fixed list of databases.
3. Treat retrieval, appraisal, synthesis, and verification as distinct stages.
4. Enforce **claim-to-source traceability**.
5. Distinguish peer-reviewed evidence, guidelines, regulatory evidence, trials, and preprints.
6. Prevent the AI agent from acting as the final clinical authority.

## Core flow

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

## Skills

- `research-orchestrator`
- `clinical-question-formulation`
- `evidence-source-selection`
- `literature-search`
- `guideline-research`
- `drug-research`
- `emerging-evidence-research`
- `citation-network-explorer`
- `fulltext-retrieval`
- `evidence-extraction`
- `evidence-appraisal`
- `evidence-synthesis`
- `citation-verification`
- `medical-safety-guardrail`

See `ARCHITECTURE.md` and `EVIDENCE_POLICY.md`.

## Foundation specification status

Version 0.2 upgrades the three foundation skills to production-oriented specifications:

- `research-orchestrator`
- `clinical-question-formulation`
- `evidence-source-selection`

Shared contracts are in `contracts/core-contracts.yaml`; regression scenarios are in `tests/foundation-test-cases.md`.


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

## v0.5 — Execution & Tooling Layer

Adds capability interfaces, normalized provider/provenance contracts, adapter
skeletons for PubMed/NCBI, Crossref, OpenAlex, Semantic Scholar and
ClinicalTrials.gov, guideline/regulatory adapter strategy, full-text resolution,
identity/version resolution, retry/rate-limit/cache/privacy policies and tests.

```text
Skills → capability interfaces → provider adapters
→ normalized records + provenance → evidence pipeline
```
