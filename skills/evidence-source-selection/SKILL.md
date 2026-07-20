# Skill: evidence-source-selection

## 1. Mission
Select source classes and retrieval order that are fit for the question, evidence purpose, clinical stakes, and recency requirements.

The skill selects capabilities/source classes, not favorite websites.

## 2. Trigger
Invoke after question formulation and before research execution.

## 3. Input
```yaml
input:
  question: ResearchCase.question
  intent: clinical_learning | academic_research | clinical_decision_support | drug_intelligence | horizon_scanning
  requested_depth: quick | standard | deep | systematic_like
  constraints:
    geography: [string]
    recency: string | null
    access: [string]
```

## 4. Output
```yaml
source_plan:
  strategy: authoritative_first | evidence_hierarchy | broad_discovery | horizon_scanning | mixed
  sources:
    - source_class: string
      priority: 1
      purpose: string
      required: true
      query_mode: targeted | structured | semantic | citation_graph | registry_lookup
      verification_level: standard | elevated | critical
  excluded_or_deprioritized:
    - source_class: string
      reason: string
  stopping_rules: [string]
  escalation_rules: [string]
```

## 5. Core decision table
| Question | Priority source classes | Mandatory verification |
|---|---|---|
| Current standard of care | Current authoritative guideline → systematic review → pivotal/recent trials | guideline date/version |
| Therapy effectiveness | guideline/systematic review/meta-analysis → RCTs → relevant observational evidence | directness + major conflicting trials |
| Diagnosis | diagnostic guideline → diagnostic SR/meta-analysis → prospective accuracy studies | reference standard + population |
| Prognosis | systematic reviews → large prospective cohorts → validated models | validation/applicability |
| Harm/adverse effect | regulator safety communications → pharmacovigilance → SRs → large observational/RCT safety | regulatory status + signal context |
| Drug approval/indication | regulator/official label first → clinical trials → publications | current jurisdiction-specific status |
| Dosing/contraindication | official label/formulary/guideline first | current version |
| Emerging drug/evidence | trial registries → preprints/early publications → recent peer-reviewed evidence | preliminary status |
| Mechanism | authoritative pharmacology/reference sources → primary mechanistic studies | avoid overclaiming clinical effect |
| Epidemiology | official surveillance/public health data → systematic reviews → primary population studies | geography/time definition |

## 6. Source-class definitions
### A. Authoritative / normative
- regulatory agencies and official product information;
- public health authorities;
- recognized guideline issuers;
- official trial registries.

Use when the question asks what is approved, recommended, warned, required, or currently standard.

### B. Evidence synthesis
- systematic reviews;
- meta-analyses;
- evidence reports.

Use to map the mature evidence base efficiently.

### C. Primary research
- randomized trials;
- diagnostic accuracy studies;
- cohort/case-control studies;
- mechanistic studies.

Use for pivotal evidence, updates after reviews, and unresolved questions.

### D. Discovery / scholarly graphs
- bibliographic indexes;
- semantic scholarly search;
- citation graphs.

Use for discovery, not as evidence-quality certification.

### E. Access / full-text repositories
Use to obtain documents. Retrieval location does not imply methodological quality.

### F. Emerging / non-final
- preprints;
- conference evidence;
- trial registry results/status.

Use for horizon scanning with mandatory preliminary labels.

## 7. Strategy selection
### authoritative_first
Use for:
- approval;
- labeling;
- warnings;
- guidelines;
- current public health recommendations.

### evidence_hierarchy
Use for:
- therapy;
- diagnosis;
- prognosis;
- harm;
- prevention.

### broad_discovery
Use for:
- academic landscape;
- research-gap exploration;
- unfamiliar topics.

### horizon_scanning
Use for:
- new drugs;
- ongoing trials;
- preprints;
- fast-moving emerging fields.

### mixed
Use when a request combines current status with effectiveness evidence.

## 8. Recency rules
- Current regulatory/guideline facts require current official sources.
- Newer does not automatically mean stronger.
- Search for evidence published after the latest synthesis/guideline when appropriate.
- Record publication/update dates for normative sources.

## 9. Preprint rules
Preprints may be selected only when:
- the intent includes emerging evidence/horizon scanning; or
- peer-reviewed evidence is absent and the limitation is explicit.

They cannot be the sole evidence source supporting a clinical recommendation.

## 10. Redundancy and triangulation
For high-stakes claims, plan source triangulation when feasible:
- normative source + underlying evidence;
- systematic review + pivotal primary study;
- regulator status + official label;
- registry record + publication.

Do not require arbitrary source counts when one authoritative source is definitive for a narrow status claim.

## 11. Stopping rules
A quick/standard search may stop when:
- an authoritative current source directly resolves a normative question;
- a high-quality synthesis plus post-synthesis update search adequately covers a clinical question;
- additional discovery yields no material new evidence class or contradiction.

A deep/systematic-like search must use an explicit reproducible stopping rule and search log.

## 12. Escalation rules
Escalate to broader/deeper sources when:
- authoritative guidance is absent or outdated;
- guidelines disagree;
- evidence is rapidly evolving;
- a pivotal study is newer than existing synthesis;
- safety signals conflict with efficacy literature;
- initial sources rely on indirect evidence.

## 13. Quality gates
Pass when:
- selected source classes match question type;
- normative questions include normative sources;
- discovery tools are not treated as quality authorities;
- preprint status is governed;
- recency requirements are explicit;
- source plan explains why each source class is used.

## 14. Acceptance tests
### T1 — “FDA đã phê duyệt thuốc X cho chỉ định Y chưa?”
Expected: regulatory/official label priority 1; publications secondary.

### T2 — “Điều trị đầu tay tăng huyết áp ở CKD?”
Expected: current guideline priority; evidence synthesis and pivotal trials secondary; jurisdiction/context considered.

### T3 — “Xu hướng nghiên cứu CAR-T trong lupus 2 năm gần đây?”
Expected: mixed broad discovery + horizon scanning; trials and recent peer-reviewed studies; preprints allowed with labels.

### T4 — “Tìm full text của bài PMID ...”
Expected: access/full-text source plan only; no implication that repository choice changes evidence quality.
