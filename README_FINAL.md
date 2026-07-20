# Medical Research Skills — Final Baseline

A production-oriented specification for an AI-assisted medical research agent
serving clinicians and medical learners.

## Architecture

```text
Scientific Reasoning
→ Research Planning
→ Research Engine
→ Execution & Provider Layer
→ Evidence Processing
→ Evidence Governance
→ Medical Safety
→ Final Report
```

## Core principles

1. Question type determines evidence strategy.
2. Providers are replaceable implementations, not the architecture.
3. Search relevance is not evidence quality.
4. Every material claim is traceable to evidence.
5. Regulatory/guideline current status requires authoritative verification.
6. Preprints and registries remain distinct from established evidence.
7. Conflicts are surfaced, not averaged away.
8. Patient-specific actionable decisions require elevated safety handling.
9. Runtime is resumable, auditable and idempotent.
10. AI is an evidence assistant, not the final clinical authority.

This package is the recommended baseline for implementation.
