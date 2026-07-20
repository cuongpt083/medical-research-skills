# Skill: evidence-extraction

## Purpose
Transform source documents into structured, source-traceable evidence facts without interpretation drift.

## Principle
Extraction is not synthesis. Extract what the source reports before deciding what it means.

## Inputs
- verified document artifact;
- research question / outcome definitions;
- extraction schema appropriate to source type.

## Source-specific extraction profiles
### Interventional study
Extract:
- study design and setting;
- eligibility criteria;
- sample size and analysis population;
- intervention/comparator;
- randomization/blinding when reported;
- primary/secondary outcomes;
- effect measure, point estimate, CI, p-value where relevant;
- absolute event counts/rates where available;
- follow-up;
- adverse events;
- protocol/registration identifiers;
- funding/conflicts;
- author-stated limitations.

### Diagnostic study
Additionally extract:
- index test;
- reference standard;
- thresholds;
- sensitivity/specificity;
- predictive values or likelihood ratios where reported;
- spectrum/selection characteristics.

### Guideline
Extract:
- recommendation text;
- target population;
- recommendation strength/class;
- evidence certainty/level as stated by guideline;
- exceptions/contraindications;
- publication/update date and issuing body.

### Regulatory document
Extract exact regulatory facts:
- approval/authorization status;
- jurisdiction;
- indication;
- population;
- dosing/route where requested;
- contraindications/warnings;
- date/version.

## Atomic fact model
Every material extracted fact SHOULD include a locator.

```yaml
extracted_fact:
  id: string
  evidence_id: string
  field: string
  value: any
  normalized_value: any | null
  source_locator:
    page: string | null
    section: string | null
    table_figure: string | null
    paragraph_or_line: string | null
  extraction_confidence: high | moderate | low
  verbatim_required: boolean
  notes: string | null
```

## Numerical extraction rules
- Preserve units and denominators.
- Distinguish adjusted from unadjusted estimates.
- Distinguish RR/OR/HR/RD/MD/SMD; never interchange them.
- Preserve CI level and analysis population.
- Do not calculate a missing statistic unless explicitly marked as derived.
- Derived values must record formula and source inputs.

## Quality gates
Before completion:
1. Critical study identity fields present.
2. Primary outcome and time point are not conflated with secondary/subgroup outcomes.
3. Numerical values have locators or explicit `locator_unavailable` status.
4. Extracted claims do not exceed source wording.
5. Preprint/publication status preserved.

## Failure states
- `SOURCE_TEXT_INSUFFICIENT`
- `TABLE_OR_SUPPLEMENT_REQUIRED`
- `OUTCOME_DEFINITION_AMBIGUOUS`
- `NUMERICAL_CONFLICT_IN_SOURCE`
- `EXTRACTION_LOW_CONFIDENCE`

Low-confidence critical facts must be routed to manual/secondary verification.

## Prohibited behavior
- infer causality during extraction;
- translate statistical significance into clinical importance;
- merge multiple time points into one result;
- silently prefer abstract values over corrected/full-text values.
