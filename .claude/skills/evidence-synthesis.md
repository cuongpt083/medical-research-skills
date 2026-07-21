---
name: evidence-synthesis
description: Combine appraised evidence into calibrated, traceable conclusions without
  flattening disagreement, uncertainty, or differences in evidence maturity.
trigger: Combine appraised evidence into calibrated, traceable conclusions without
  flattening disagreement, uncertainty, or differences in evidence maturity.
tags:
- medical-research
- evidence
---

> Source of truth: `skills/evidence-synthesis/SKILL.md`
>
> This file is auto-generated. Edit `skills/evidence-synthesis/SKILL.md` and run `python scripts/build-agent-configs.py` to regenerate.

---
name: evidence-synthesis
description: Combine appraised evidence into calibrated, traceable conclusions without flattening disagreement, uncertainty, or evidence maturity. Use after evidence extraction and appraisal.
---

# Skill: evidence-synthesis

## Purpose
Combine appraised evidence into calibrated, traceable conclusions without flattening disagreement, uncertainty, or differences in evidence maturity.

## Preconditions
Do not synthesize material clinical conclusions until:
- evidence items are deduplicated/version-resolved;
- critical facts are extracted;
- material evidence is appraised or explicitly marked unappraised;
- source status (peer-reviewed/preprint/regulatory/guideline) is known.

## Synthesis workflow
1. Group evidence by question, intervention/comparator, outcome, and clinically meaningful time point.
2. Separate evidence lanes:
   - authoritative guideline/regulatory evidence;
   - systematic synthesis;
   - primary established evidence;
   - emerging/preliminary evidence.
3. Identify direction and magnitude of findings.
4. Identify heterogeneity/conflict.
5. Explain plausible reasons for disagreement before choosing any dominant interpretation.
6. Produce atomic claims.
7. Assign calibrated confidence with rationale.
8. Record unresolved evidence gaps.

## Claim contract
```yaml
claim:
  id: string
  text: string
  claim_type: descriptive | association | causal | diagnostic | therapeutic | safety | guideline_recommendation | regulatory | emerging_evidence
  scope:
    population: string | null
    intervention_or_exposure: string | null
    comparator: string | null
    outcome: string | null
    timeframe: string | null
  supporting_evidence_ids: []
  contradicting_evidence_ids: []
  confidence:
    level: high | moderate | low | very_low
    rationale: string
  evidence_maturity: established | mixed | emerging | preliminary
  verification_status: pending | verified | failed
```

## Conflict handling
When credible evidence conflicts:
- retain both directions in the evidence map;
- compare design, population, outcome definitions, time points, bias, precision, and recency;
- state whether conflict is explainable or unresolved;
- never manufacture consensus.

## Quantitative synthesis
Do not perform a de novo meta-analysis unless explicitly requested and methodologically supported.
If combining effect sizes, require compatible estimands, populations/outcomes, and an explicit statistical protocol.

## Language calibration
- `shows/proves` only when justified by strong design and context;
- prefer `was associated with` for non-causal observational evidence;
- use `suggests`, `may`, or `preliminary` for uncertain/emerging evidence;
- distinguish statistical from clinical significance.

## Quality gates
A material claim cannot pass when:
- it has no supporting evidence IDs;
- the evidence cited does not match population/outcome/timeframe;
- a preprint is the sole basis for an established clinical recommendation;
- regulatory status is inferred from academic publications;
- major contradictory evidence is omitted.

## Output
- evidence summary by outcome;
- claim objects;
- contradiction map;
- uncertainty/gap list;
- recommendations for additional research when needed.

