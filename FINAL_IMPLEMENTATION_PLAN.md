# Final Implementation Plan

## Milestone 1 — Vertical slice
Implement one therapy question end-to-end:

```text
Question → PICO → PubMed → normalization → deduplication
→ full text/abstract → extraction → appraisal → synthesis
→ citation verification → safety review → final report
```

Prioritize correctness and traceability over breadth.

## Milestone 2 — Authoritative lanes
Add guideline, regulatory and ClinicalTrials.gov adapters.
Validate approval/status, current-guideline and emerging-evidence cases.

## Milestone 3 — Scholarly expansion
Add OpenAlex/Semantic Scholar and citation-network traversal for discovery coverage.

## Milestone 4 — Runtime hardening
Add durable tasks, checkpoints, idempotency, retries, caching, observability and HITL.

## Milestone 5 — Evaluation
Build benchmark cases across therapy, diagnosis, prognosis, adverse effects,
drug approval, warnings, guideline conflicts, emerging evidence, retractions,
preprint successors, numerical extraction and unsafe patient-specific requests.

## Milestone 6 — Production rollout
Start with clinician education/research support and non-patient-specific evidence lookup.
Enable higher-risk workflows only after benchmark gates, governance review, monitoring and audit pass.
