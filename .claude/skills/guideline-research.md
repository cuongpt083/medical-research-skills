---
name: guideline-research
description: Locate, verify, compare, and extract current authoritative clinical guidance
  relevant to a medical question.
trigger: Use for standard-of-care, recommended management, screening, diagnosis, prevention,
  treatment pathway, monitoring, or “what do current guidelines say?” questions.
tags:
- medical-research
- evidence
---

> Source of truth: `skills/guideline-research/SKILL.md`
>
> This file is auto-generated. Edit `skills/guideline-research/SKILL.md` and run `python scripts/build-agent-configs.py` to regenerate.

# Skill: guideline-research

## 1. Mission
Locate, verify, compare, and extract current authoritative clinical guidance relevant to a medical question.

## 2. Trigger
Use for standard-of-care, recommended management, screening, diagnosis, prevention, treatment pathway, monitoring, or “what do current guidelines say?” questions.

## 3. Inputs
```yaml
guideline_request:
  research_case_id: string
  condition_or_topic: string
  question_type: string
  jurisdiction_priority: [string]
  specialty: [string]
  population_constraints: [string]
  current_as_of: string
```

## 4. Source hierarchy
Prefer in this order, subject to jurisdiction relevance:
1. official issuing organization / government / recognized specialty society;
2. official guideline repository or authoritative host;
3. peer-reviewed guideline publication;
4. trustworthy secondary summaries only for discovery, never as sole authority when primary guidance is accessible.

## 5. Guideline identity verification
For every guideline capture:
```yaml
guideline_identity:
  title: string
  issuing_body: string
  jurisdiction: string
  publication_date: string
  last_update_date: string | null
  version: string | null
  status: current | superseded | archived | unclear
  official_url: string | null
  replacement_guideline: string | null
```

Do not assume the newest publication date equals the currently operative guideline without checking status.

## 6. Extraction protocol
Extract separately:
- recommendation text meaning (paraphrase unless quotation required);
- target population;
- intervention/action;
- strength/class of recommendation if explicitly defined;
- certainty/level of evidence if explicitly defined;
- exceptions/contraindications;
- implementation notes;
- date/version.

Never translate one society's grading system into another without an explicit mapping.

## 7. Comparison protocol
When multiple guidelines are relevant, create:
```yaml
guideline_comparison:
  consensus_points: []
  disagreements:
    - topic: string
      guideline_positions: []
      likely_explanations:
        - jurisdiction
        - evidence_cutoff_date
        - population_scope
        - resource_context
        - value_preferences
        - methodology
  unresolved_uncertainty: []
```

Do not “average” conflicting recommendations.

## 8. Recency protocol
1. Verify current status from issuing body when possible.
2. Record evidence cutoff date if available.
3. Search for focused updates/addenda.
4. Check whether major regulatory changes or pivotal trials post-date the guideline.
5. If newer evidence may materially change guidance, route to literature-search and flag `GUIDELINE_LAG_POSSIBLE`.

## 9. Provider contract
```yaml
GuidelineProvider:
  must_support_one_or_more:
    - official_site_search
    - guideline_catalog_search
    - document_fetch
    - version_status_check
  normalized_output:
    - guideline_identity
    - document_location
    - publication_metadata
    - source_provenance
```

## 10. Stopping rules
Stop when:
- the relevant current guideline(s) for required jurisdictions/specialties are verified;
- major conflicting authoritative guidance has been identified;
- additional low-authority summaries add no new recommendation information.

## 11. Quality gates
- GR-QG1: issuing body and current status verified.
- GR-QG2: recommendation applies to the target population/context.
- GR-QG3: strength/evidence grading is reported only if source-defined.
- GR-QG4: meaningful guideline conflicts are visible.
- GR-QG5: superseded guidance is not presented as current.

## 12. Failure states
- `CURRENT_GUIDELINE_NOT_VERIFIED`
- `JURISDICTION_UNCLEAR`
- `GUIDELINE_CONFLICT_UNRESOLVED`
- `GUIDELINE_LAG_POSSIBLE`

## 13. Tests
### GR-T1 Superseded guideline
A 2021 guideline replaced by a 2025 version must not be reported as current.

### GR-T2 Cross-jurisdiction disagreement
Differences between two credible societies must be preserved and contextualized, not collapsed.

### GR-T3 Missing grading
Do not invent “Class I / Level A” when the guideline does not use that scheme.

## Cross-cutting invariants
- Preserve provenance for every query, result, transformation, and exclusion decision.
- Never infer evidence quality from search rank, citation count, journal prestige, or AI relevance score alone.
- Normalize provider-specific records before downstream reasoning.
- Do not fabricate identifiers, metadata, access status, publication status, or study results.
- Mark uncertainty explicitly; absence of evidence is not evidence of absence.

