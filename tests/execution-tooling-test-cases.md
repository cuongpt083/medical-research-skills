# Execution & Tooling Regression Tests — v0.5

1. Provider-specific fields never leak into reasoning skills.
2. HTTP 429 respects Retry-After and records retry count.
3. Invalid authentication returns AUTH_ERROR without retry loop.
4. Cache hits preserve source provenance.
5. Same normalized DOI across providers is not counted twice.
6. Preprint and peer-reviewed successor are linked and not double-counted.
7. Similar titles alone do not auto-merge distinct trials.
8. ClinicalTrials.gov record is never mislabeled peer-reviewed.
9. Efficacy publication cannot prove approval when regulator is unavailable.
10. Superseded guideline must not outrank verified current version.
11. AI/TLDR summaries may screen but cannot be source-text evidence.
12. Paywalled content is not bypassed.
13. New retraction status overrides stale cached metadata.
14. Patient identifiers are removed from external search queries unless necessary.
15. Pagination cursor is preserved; first page is never treated as exhaustive.
16. Provider outage fallback records degraded coverage.
17. Non-authoritative source cannot replace regulator for approval status.
18. Search run preserves translated query, filters, time, adapter version and query hash.
