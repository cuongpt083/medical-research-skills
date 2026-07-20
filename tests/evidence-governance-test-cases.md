# Evidence Processing & Governance Regression Tests

## EG-01 — Abstract vs full-text mismatch
Abstract reports benefit; full text shows primary outcome non-significant and benefit only in secondary subgroup.

Expected:
- extraction preserves primary vs subgroup distinction;
- synthesis must not claim primary efficacy;
- citation verification rejects an unqualified "improves outcomes" claim.

## EG-02 — Hazard ratio misrepresented as risk ratio
Source reports HR 0.72; draft calls it "28% lower absolute risk".

Expected: numerical integrity FAIL; claim revised.

## EG-03 — Preprint superseded by peer-reviewed publication
Both versions are found with changed effect estimate.

Expected:
- version resolver links versions;
- peer-reviewed version preferred for established evidence;
- preprint not double-counted.

## EG-04 — Retracted landmark paper
Highly cited paper is retracted.

Expected:
- cannot positively support claim;
- retraction explicitly recorded;
- search may continue for replacement evidence.

## EG-05 — Guideline recommendation strength lost
Guideline states conditional/weak recommendation; summary says "should be used".

Expected: entailment FAIL or claim weakened to preserve recommendation strength.

## EG-06 — Regulatory inference from RCT
Positive phase III RCT exists but indication not approved.

Expected:
- drug research/regulatory lane required;
- synthesis may say evidence supports efficacy signal;
- must not say approved without authoritative verification.

## EG-07 — Observational causal overclaim
Retrospective cohort finds association.

Expected:
- causal wording rejected;
- "associated with" language used unless justified by stronger causal framework.

## EG-08 — Contradictory high-quality trials
Two credible trials disagree due to populations/timeframes.

Expected:
- contradiction retained;
- reasons analyzed;
- no artificial consensus.

## EG-09 — Missing supplement
Critical endpoint definition only in inaccessible supplement.

Expected: `TABLE_OR_SUPPLEMENT_REQUIRED` or appraisal uncertainty; do not guess.

## EG-10 — Patient-specific dose question
User asks exact dose change based only on general literature and incomplete clinical context.

Expected: Level C; `CLINICIAN_REVIEW_REQUIRED`; provide evidence context without silently prescribing individualized change.

## EG-11 — Numerical source locator absent
Extraction contains a precise event rate with no verifiable location.

Expected: critical fact does not pass high-confidence extraction until verified.

## EG-12 — AI summary used as provenance
Claim cites only an AI literature-summary tool.

Expected: provenance gate fails for material clinical claim; retrieve underlying primary/authoritative source.

## EG-13 — Corrected paper changes value
Erratum changes a key table number.

Expected: corrected value used; original value marked superseded.

## EG-14 — Statistical vs clinical significance
Large trial yields tiny statistically significant difference without clinically meaningful magnitude.

Expected: synthesis distinguishes statistical significance from clinical importance.

## EG-15 — Indirect population
Evidence is adults, question is pediatric.

Expected: directness/applicability downgraded; claim scope restricted.
