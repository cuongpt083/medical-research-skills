# Evidence Policy

## 1. Core rule

The system must never equate:

```text
Search relevance = evidence quality
Journal legitimacy = study quality
Peer review = correctness
Statistical significance = clinical significance
Preprint = established evidence
Single study = clinical consensus
```

---

## 2. Evidence selection by question type

### Therapy / prevention

Prefer:

1. Current authoritative clinical guidelines
2. High-quality systematic reviews / meta-analyses
3. Randomized controlled trials
4. Strong observational evidence when RCT evidence is unavailable or inappropriate
5. Preprints only as emerging evidence

### Diagnosis

Prefer:

1. Diagnostic guidelines
2. Systematic reviews of diagnostic accuracy
3. Prospective diagnostic accuracy studies
4. Appropriate reference-standard comparisons

### Prognosis

Prefer:

1. Systematic reviews
2. Large prospective cohorts
3. Validated prognostic models

### Harm / adverse effects

Prefer:

1. Regulatory safety communications
2. Pharmacovigilance data
3. Systematic reviews
4. Large observational studies
5. RCT safety data

### Drug questions

Must consider:

- approved indications
- regulatory labeling
- contraindications
- boxed/major warnings where applicable
- dosing context
- safety communications
- major interaction information
- current trials for investigational uses

Academic papers alone are insufficient for regulatory claims.

### Emerging evidence

May include:

- trial registries
- conference materials
- preprints
- early online publications

Must be explicitly labeled as preliminary.

---

## 3. Source classes

### Authoritative clinical / regulatory

Examples of classes:

- national or international health authorities
- regulatory agencies
- recognized specialty society guidelines
- official drug labels
- trial registries

### Scholarly evidence databases

Examples of capabilities:

- biomedical bibliographic databases
- multidisciplinary scholarly indexes
- citation graphs
- open-access repositories

### Access/retrieval sources

A full-text repository may help obtain a paper but does not itself establish evidence quality.

---

## 4. Preprint policy

A preprint:

- must be labeled `PREPRINT`;
- must not be presented as established clinical evidence;
- cannot alone support a treatment recommendation;
- should be checked for later peer-reviewed publication;
- should be contextualized against existing peer-reviewed evidence and guidelines.

---

## 5. Recency policy

Use the most recent authoritative guideline or regulatory document when the question depends on current practice.

Recency must never automatically override evidence quality.

A new small observational study should not displace a mature body of stronger evidence without a justified reason.

---

## 6. Conflict policy

When credible sources disagree:

1. Do not collapse disagreement into a single answer.
2. Identify the conflicting claims.
3. Compare:
   - study design
   - population
   - intervention/comparator
   - outcome definitions
   - risk of bias
   - precision
   - recency
   - guideline/regulatory status
4. State the unresolved uncertainty.

---

## 7. Claim-source traceability

Every material claim must have one or more evidence references.

For high-impact clinical claims, the system should prefer at least one primary or authoritative source instead of relying solely on an AI-generated summary or secondary aggregator.

Traceability must be made visible to the end user, not only kept as internal evidence IDs. The final report must include a rendered `References` section (one human-readable entry per cited evidence item, with stable reference ID, persistent identifier, bibliographic metadata, and publication-status label) and every material claim must carry inline citation markers resolving to those entries. A report that contains material claims but no rendered `References` section fails the reference-rendering quality gate and must not be published as established fact.

---

## 8. Retraction and correction policy

Before relying on a high-impact paper, verify when feasible:

- retraction status
- expression of concern
- major correction/erratum
- replacement publication

A retracted study must not support a positive claim.

---

## 9. Evidence confidence

Use:

- High
- Moderate
- Low
- Very low

Confidence must be justified using:

- study design
- risk of bias
- consistency
- directness
- precision
- publication/reporting concerns
- applicability

Do not infer formal GRADE certainty unless the workflow actually performs a GRADE-compatible assessment.

---

## 10. Clinical safety boundary

The system may summarize evidence and explain guideline recommendations.

It must not silently convert population-level evidence into patient-specific medical advice.

Patient-specific recommendations require explicit acknowledgment of missing clinical context and clinician judgment.
