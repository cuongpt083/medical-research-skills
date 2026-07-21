---
name: clinical-question-formulation
description: Transform a medical information need into a precise, researchable evidence
  question without introducing assumptions that distort the user's intent.
trigger: 'Invoke before evidence retrieval when: - the question is clinical, therapeutic,
  diagnostic, prognostic, etiologic, safety-related, or drug-related; - the request
  is broad enough that evidence selection depends on clarification/normalization;
  - multiple interpretations would lead to different source strategies.'
tags:
- medical-research
- evidence
---

> Source of truth: `skills/clinical-question-formulation/SKILL.md`
>
> This file is auto-generated. Edit `skills/clinical-question-formulation/SKILL.md` and run `python scripts/build-agent-configs.py` to regenerate.

---
name: clinical-question-formulation
description: Transform a medical information need into a precise, researchable evidence question (PICO/PEO/PICOT) without introducing bias or false assumptions. Use before evidence retrieval when questions are clinical, therapeutic, diagnostic, prognostic, etiologic, safety, or drug-related.
---

# Skill: clinical-question-formulation

## 1. Mission
Transform a medical information need into a precise, researchable evidence question without introducing assumptions that distort the user's intent.

## 2. Trigger
Invoke before evidence retrieval when:
- the question is clinical, therapeutic, diagnostic, prognostic, etiologic, safety-related, or drug-related;
- the request is broad enough that evidence selection depends on clarification/normalization;
- multiple interpretations would lead to different source strategies.

## 3. Question taxonomy
Assign one primary type and zero or more secondary types:

```yaml
question_type:
  primary: therapy | prevention | diagnosis | screening | prognosis | etiology | harm | guideline | drug | epidemiology | mechanism | emerging_evidence | general_medical_knowledge
  secondary: [string]
```

## 4. Framework selection
| Question type | Preferred framework |
|---|---|
| Therapy / prevention | PICO or PICOT |
| Diagnosis / screening | PIRD/PICO adapted for index test and reference standard |
| Prognosis | PEO/PICOT |
| Etiology / harm | PEO/PICO |
| Drug approval/safety | Entity + jurisdiction + indication + status + time |
| Guideline | Condition + population + intervention/decision + jurisdiction + recency |
| Mechanism/general knowledge | Concept map; do not force PICO |
| Emerging evidence | Entity/topic + development stage + population + outcome + recency |

## 5. Input
```yaml
input:
  original_question: string
  user_intent: string | null
  constraints: object
```

## 6. Output
```yaml
question:
  original: string
  normalized: string
  type:
    primary: string
    secondary: [string]
  framework:
    type: PICO | PICOT | PEO | PIRD | entity_status | concept_map | freeform
    population: string | null
    intervention_or_exposure: string | null
    comparator: string | null
    outcomes: [string]
    timeframe: string | null
    index_test: string | null
    reference_standard: string | null
  context:
    care_setting: string | null
    geography: [string]
    age_group: string | null
    sex: string | null
    comorbidities: [string]
  ambiguities:
    material: [string]
    non_material: [string]
  assumptions: [string]
  search_concepts:
    concepts: [string]
    synonyms: [string]
    controlled_vocabulary_candidates: [string]
  answerability:
    status: answerable | answerable_with_assumptions | clarification_recommended | not_researchable
    reason: string
```

## 7. Formulation algorithm
1. Preserve the original wording.
2. Identify the decision/problem the user is actually trying to resolve.
3. Classify the primary question type.
4. Select the least restrictive suitable framework.
5. Extract explicit population, intervention/exposure, comparator, outcomes, timing, and jurisdiction.
6. Separate explicit facts from inferred assumptions.
7. Identify ambiguity only when it could materially change evidence retrieval or interpretation.
8. Generate normalized search concepts and candidate synonyms.
9. Define the evidence-relevant version of the question.
10. Mark answerability status.

## 8. Ambiguity policy
### Material ambiguity
Examples:
- adult vs pediatric population;
- approved indication vs experimental use;
- prevention vs treatment;
- diagnosis vs screening;
- local vs international guideline when recommendations differ;
- surrogate outcome vs patient-important outcome.

Material ambiguity must be resolved, explicitly assumed, or represented as parallel research branches.

### Non-material ambiguity
Do not interrupt research for details unlikely to change evidence selection.

## 9. Outcome policy
Prefer patient-important outcomes when the user did not specify outcomes.

For therapy questions consider, as relevant:
- mortality;
- morbidity/clinical events;
- symptoms/function/quality of life;
- serious adverse events;
- treatment discontinuation.

Do not substitute surrogate endpoints for clinical outcomes without labeling the distinction.

## 10. Search concept generation
Generate concept groups rather than a single naïve keyword string.

Example:
```yaml
concept_groups:
  population:
    preferred: atrial fibrillation
    synonyms: [nonvalvular atrial fibrillation, NVAF]
  intervention:
    preferred: apixaban
  comparator:
    preferred: warfarin
  outcomes:
    preferred: major bleeding
    synonyms: [major hemorrhage, bleeding events]
```

Controlled vocabulary is a candidate layer, not a replacement for free-text synonyms.

## 11. Quality gates
Pass only when:
- normalized question preserves original intent;
- framework fields do not contain fabricated facts;
- question type is explicit;
- material assumptions are visible;
- search concepts cover major terminology variants;
- outcome interpretation is not silently altered.

## 12. Failure / abstention rules
Return `NOT_RESEARCHABLE_AS_STATED` when the request is too incoherent to map to an evidence question.

Return `PARALLEL_BRANCHES_REQUIRED` when two plausible interpretations would materially change evidence and neither can be safely preferred.

Never invent patient data to complete PICO.

## 13. Examples
### Example A — Therapy
Input: “Apixaban có an toàn hơn warfarin không?”
Normalized branch:
- primary type: therapy/harm
- population: adults with atrial fibrillation, if context supports; otherwise unspecified
- intervention: apixaban
- comparator: warfarin
- outcomes: major bleeding, intracranial hemorrhage, thromboembolic outcomes
- ambiguity: indication/population may be material

### Example B — Drug status
Input: “Semaglutide có được dùng cho béo phì không?”
Framework: entity_status
Required dimensions: product/formulation, indication, jurisdiction, population, current regulatory status.

### Example C — Mechanism
Input: “GLP-1 receptor agonist hoạt động thế nào?”
Do not force PICO. Use concept-map formulation and retrieve authoritative pharmacology/mechanism sources.

