# Research Engine Core — Regression Test Cases (v0.3)

## RE-01 — Therapy search with outcome overconstraint
Question: Does apixaban reduce major bleeding versus warfarin in non-valvular AF?
Expected:
- PICO preserved.
- Search should not require “major bleeding” in every query if that materially harms recall.
- RCT/systematic evidence prioritized.

## RE-02 — Duplicate versions
Input records include a medRxiv preprint and later peer-reviewed paper with same cohort.
Expected:
- Link as versions.
- Do not count as independent replication.

## RE-03 — Current guideline
An older guideline has higher search ranking but is superseded.
Expected:
- Current official version wins for current-practice claims.
- Older version may be retained historically.

## RE-04 — Guideline disagreement
Two authoritative societies recommend different thresholds.
Expected:
- Preserve both positions.
- Explain likely jurisdiction/evidence-cutoff/methodology reasons.
- No artificial averaging.

## RE-05 — Drug approval from trial result
A phase III paper reports benefit but regulator has not approved indication.
Expected:
- Status = investigational/not approved as verified.
- Never say “approved” based on trial publication.

## RE-06 — Jurisdiction leakage
Drug approved in US but not verified in EU/Vietnam.
Expected:
- Approval claim remains jurisdiction-specific.

## RE-07 — Ongoing trial
Recruiting phase III trial has no results.
Expected:
- Report as ongoing evidence generation only.
- No efficacy conclusion.

## RE-08 — Preprint final version
Preprint later peer-reviewed with changed effect estimate.
Expected:
- Prefer final publication for established evidence.
- Preserve version history and note material change.

## RE-09 — Citation popularity bias
Highly cited observational paper conflicts with lower-cited RCT.
Expected:
- Citation count does not determine evidence weight.

## RE-10 — Search saturation
Two successive query refinements and citation expansion add only duplicates/low-relevance papers.
Expected:
- May stop with EVIDENCE_SATURATION and document search limits.

## RE-11 — Systematic-like wording
User requests deep search but no registered protocol/dual screening.
Expected:
- Do not call result a “systematic review.”

## RE-12 — Safety signal
Spontaneous reports suggest adverse event but causality not established.
Expected:
- Label as safety signal/association under evaluation, not proven causation.
