---
name: evidence-appraisal
description: Evaluate methodological credibility and applicability of each evidence
  item using question- and design-appropriate criteria.
trigger: Evaluate methodological credibility and applicability of each evidence item
  using question- and design-appropriate criteria.
tags:
- medical-research
- evidence
---

> Source of truth: `skills/evidence-appraisal/SKILL.md`
>
> This file is auto-generated. Edit `skills/evidence-appraisal/SKILL.md` and run `python scripts/build-agent-configs.py` to regenerate.

---
name: evidence-appraisal
description: Evaluate methodological credibility, risk of bias, internal validity, and applicability of evidence items using study design-appropriate criteria (e.g. ROBINS-I, RoB 2, AGREE II).
---

# Skill: evidence-appraisal

## Purpose
Evaluate methodological credibility and applicability of each evidence item using question- and design-appropriate criteria.

## Principle
Do not use one universal checklist for all study designs.

## Inputs
- structured evidence item;
- full text when required;
- research question/PICO;
- source type and study design.

## Appraisal dimensions
### Internal validity
- selection/randomization bias;
- deviations from intended intervention/exposure;
- missing data;
- measurement/outcome ascertainment;
- confounding where applicable;
- selective reporting;
- inappropriate analysis.

### Evidence usefulness
- directness to the target question;
- precision;
- applicability/generalizability;
- completeness of reporting;
- follow-up adequacy.

### Contextual signals
- funding/conflicts;
- protocol/registration consistency;
- retraction/correction status;
- unusually influential subgroup/post-hoc analyses.

Funding or conflict disclosures are contextual signals, not automatic proof of bias.

## Design-aware routing
Use an appropriate framework or equivalent criteria:
- RCT → RoB-style domain assessment;
- observational intervention/etiology → confounding/selection/misclassification-focused assessment;
- diagnostic accuracy → patient selection/index test/reference standard/flow-timing;
- systematic review → search, selection, appraisal, synthesis methodology;
- guideline → governance, evidence linkage, currency, recommendation process;
- prediction model → development/validation, overfitting, calibration/discrimination, applicability.

## Output
```yaml
appraisal:
  evidence_id: string
  design: string
  domains:
    - name: string
      judgment: low | some_concerns | high | unclear | not_applicable
      rationale: string
      supporting_fact_ids: []
  overall_risk_of_bias: low | some_concerns | high | unclear
  directness: direct | partially_direct | indirect | unclear
  precision: high | moderate | low | unclear
  applicability: high | moderate | low | unclear
  major_limitations: []
  appraisal_confidence: high | moderate | low
```

## Formal certainty rule
Do NOT label an item or body of evidence as formal `GRADE High/Moderate/Low/Very Low` unless a GRADE-compatible body-of-evidence process is explicitly executed.

A local `confidence` label must be named and described as an internal evidence-confidence estimate, not formal GRADE.

## Quality gates
- Every negative judgment has rationale.
- Appraisal references extracted facts/source locators where possible.
- Study design is correctly classified.
- Applicability is judged against the actual target population/context.

## Abstention
Return `APPRAISAL_INSUFFICIENT_INFORMATION` when critical methodological information is unavailable rather than guessing.

