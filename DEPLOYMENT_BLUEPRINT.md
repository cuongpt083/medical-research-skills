# Deployment Blueprint

## Service boundaries

```text
API / UI
→ Research Orchestrator
→ Task Runtime / Workflow Engine
→ Provider Adapters
→ Evidence Store + Artifact Store
→ Audit / Observability
```

## Minimal stack

A practical MVP can use:
- Python or TypeScript service;
- PostgreSQL;
- object storage;
- background worker queue;
- provider adapters;
- deterministic database-backed state machine.

Temporal is optional.

Use Temporal when:
- workflows run for minutes/hours;
- durable retries/resume matter;
- many provider/document tasks execute in parallel;
- HITL pauses are common;
- exact workflow history is valuable.

## Persistence model

Recommended entities:
- research_cases
- research_runs
- research_tasks
- provider_calls
- normalized_records
- study_identities
- evidence_items
- extracted_facts
- claims
- citation_verifications
- safety_reviews
- audit_events

## Idempotency

Use deterministic keys based on:
`run_id + task_id + normalized_input_hash + adapter_version`.

## Artifact storage

Store raw provider responses where appropriate/legal, normalized records,
open full text, extracted text/tables, evidence tables and final reports.
Avoid unnecessary sensitive patient data.
