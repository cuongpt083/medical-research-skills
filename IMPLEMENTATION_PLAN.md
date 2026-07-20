# Implementation Plan

## Phase 1 — Foundation

Implement:

1. ResearchCase schema
2. EvidenceItem schema
3. Claim schema
4. Evidence Policy
5. research-orchestrator
6. clinical-question-formulation
7. evidence-source-selection

Acceptance criterion:
The same clinical question should produce a structured research plan before any search provider is invoked.

## Phase 2 — Core retrieval

Implement adapters for capabilities:

- biomedical literature search
- scholarly metadata
- citation graph
- guideline lookup
- regulatory lookup
- trial registry search
- full-text resolution

Use provider adapters behind interfaces.

Example:

```text
LiteratureSearchProvider
CitationGraphProvider
GuidelineProvider
RegulatoryProvider
TrialRegistryProvider
FullTextProvider
```

Do not expose provider-specific response formats to reasoning skills.

## Phase 3 — Evidence processing

Implement:

- deduplication
- relevance screening
- evidence extraction
- evidence table generation
- preliminary appraisal

Require provenance for extracted fields.

## Phase 4 — Governance

Implement:

- claim-source mapping
- contradiction detection
- citation verification
- retraction/correction checks
- preprint guardrail
- clinical safety review

## Phase 5 — Evaluation suite

Build benchmark cases across:

- therapy
- diagnosis
- prognosis
- adverse effects
- drug approval/status
- guideline questions
- emerging evidence

Measure:

- source recall
- citation correctness
- claim support rate
- unsupported-claim rate
- source-class appropriateness
- preprint misclassification
- regulatory-status errors
- guideline-recency errors

## Recommended initial MVP skills

Start with 8:

1. research-orchestrator
2. clinical-question-formulation
3. evidence-source-selection
4. literature-search
5. guideline-research
6. drug-research
7. evidence-synthesis
8. citation-verification

Then add appraisal, emerging evidence, citation graphs, full-text extraction, and safety specialization.
