# Agent Runtime & Workflow Specification — Final

## Objective

Define how all skills execute as one auditable medical research agent.

```text
Question
→ Structured ResearchCase
→ Research Plan
→ Task Graph
→ Provider Execution
→ Evidence Processing
→ Governance
→ Safety Review
→ Final Report
```

No final material claim may bypass evidence governance.

## ResearchRun

Every end-to-end execution is a `ResearchRun` with:
- `run_id`, `research_case_id`
- mode: `quick | standard | deep | systematic_like`
- status: `CREATED | PLANNING | RUNNING | WAITING_FOR_HUMAN | DEGRADED | COMPLETED | FAILED | CANCELLED`
- budgets, checkpoints, tasks, artifacts, warnings, audit events.

## Canonical DAG

```text
Question Formulation
→ Evidence Requirements
→ Source Planning
→ [Literature | Guideline | Drug/Regulatory | Trials/Emerging] in parallel
→ Deduplication + Identity Resolution
→ Screening
→ Full-text Resolution
→ Evidence Extraction
→ Appraisal
→ Synthesis
→ Citation Verification
→ Safety Review
→ Final Report
```

Backward transitions are allowed:
- appraisal insufficient → research expansion;
- unsupported claim → re-extraction or research;
- unverified current status → authoritative source verification.

## Research modes

### quick
Focused lookup; authoritative/high-yield lanes; small candidate set; must still pass citation/safety gates.

### standard
Default; multiple relevant source classes, deduplication, full text when needed, appraisal, synthesis, contradiction checks.

### deep
Broader queries, citation graph traversal, explicit saturation checks, deeper regulatory/guideline reconciliation.

### systematic_like
Requires reproducible searches, inclusion/exclusion criteria, screening log, dedup log, stopping reason, and PRISMA-like accounting where feasible.
Do not call it a formal systematic review unless methodology actually satisfies the required standard.

## Checkpointing

Create checkpoints after:
1. question structuring;
2. source planning;
3. discovery lanes;
4. deduplication/screening;
5. extraction;
6. appraisal;
7. synthesis;
8. citation verification.

Resume must not repeat completed external calls unless data is stale, integrity changed, coverage was incomplete, or a human explicitly requests rerun.

## Human-in-the-loop

Required when:
- patient-specific actionable treatment decisions are requested;
- evidence remains materially conflicting;
- current approval/guideline status cannot be verified;
- uncertain identity resolution could merge distinct studies;
- safety review returns `CLINICIAN_REVIEW_REQUIRED`;
- low-confidence extraction could materially alter a clinical claim.

Human decisions become audit events, not silent edits.

## Degraded mode

Non-authoritative provider failures may degrade coverage but must be explicit.
Authority must never silently degrade for:
- regulatory approval;
- official safety notices;
- current guideline status.

## Parallelism

Safe to parallelize:
- independent source lanes;
- metadata enrichment;
- full-text resolution;
- per-document extraction.

Do not parallelize dependent final steps:
- final identity decisions;
- synthesis;
- claim verification;
- safety review.

## Budget control

Track provider calls, documents, full texts, compute/tokens where available, and elapsed runtime.
When limits approach:
1. prioritize authoritative/high-yield sources;
2. stop low-yield expansion;
3. preserve auditability;
4. emit `RESOURCE_BOUND` if coverage is incomplete.

## Audit

Every meaningful action emits an explicit audit event with actor, action, inputs, outputs, decision rationale, timestamp, and provenance references.

Never use hidden model reasoning as audit evidence.

## Completion gate

A run may be `COMPLETED` only when:
- question is structured;
- required source lanes completed or explicitly degraded;
- deduplication performed;
- material evidence extracted and appraised;
- claims synthesized;
- citations verified;
- safety review passed;
- references section rendered with stable identifiers and inline citation markers for every material claim;
- final report generated with uncertainty and caveats.
