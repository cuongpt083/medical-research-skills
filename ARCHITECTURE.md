# Medical Research Skill Architecture

## 1. Architectural principle

The system is capability-driven rather than tool-driven.

Do not encode workflows such as:

```text
Search PubMed → Search Elicit → Open SciSpace → Search Connected Papers
```

Instead encode capabilities:

```text
Question formulation
→ source selection
→ evidence discovery
→ citation expansion
→ full-text resolution
→ structured extraction
→ appraisal
→ synthesis
→ verification
```

Providers may change without changing the reasoning architecture.

---

## 2. Three-layer architecture

### Layer A — Scientific Reasoning

Responsible for defining what evidence is needed.

Skills:

- clinical-question-formulation
- research-orchestrator
- evidence-source-selection

### Layer B — Research Operations

Responsible for finding and transforming evidence.

Skills:

- literature-search
- guideline-research
- drug-research
- emerging-evidence-research
- citation-network-explorer
- fulltext-retrieval
- evidence-extraction

### Layer C — Evidence Governance

Responsible for deciding what conclusions are supportable.

Skills:

- evidence-appraisal
- evidence-synthesis
- citation-verification
- medical-safety-guardrail

---

## 3. Shared research object

All skills should exchange a normalized `ResearchCase`.

```yaml
research_case:
  id: string
  original_question: string

  question:
    type:
      - therapy
      - diagnosis
      - prognosis
      - etiology
      - harm
      - prevention
      - screening
      - guideline
      - drug
      - emerging_evidence
      - epidemiology
      - mechanism
      - general_medical_knowledge

    framework:
      type: PICO | PEO | PICOT | freeform
      population: string | null
      intervention: string | null
      comparator: string | null
      outcomes: [string]
      timeframe: string | null

  constraints:
    date_range: string | null
    geography: [string]
    language: [string]
    population_constraints: [string]

  evidence_requirements:
    preferred_evidence_types: [string]
    minimum_source_quality: string
    preprints_allowed: boolean
    regulatory_verification_required: boolean
    guideline_verification_required: boolean

  candidate_sources: []
  evidence_items: []
  claims: []
  unresolved_questions: []
```

---

## 4. Evidence item contract

```yaml
evidence_item:
  id: string

  bibliographic:
    title: string
    authors: [string]
    publication_date: string | null
    journal: string | null
    doi: string | null
    pmid: string | null
    url: string | null

  source:
    provider: string
    source_type:
      - guideline
      - systematic_review
      - meta_analysis
      - randomized_trial
      - observational_study
      - diagnostic_study
      - case_series
      - case_report
      - regulatory_document
      - trial_registry
      - preprint
      - narrative_review
      - other

  status:
    peer_reviewed: boolean | null
    preprint: boolean
    retracted: boolean | null
    corrected: boolean | null

  study:
    design: string | null
    sample_size: integer | null
    population: string | null
    intervention: string | null
    comparator: string | null
    outcomes: []
    effect_estimates: []
    follow_up: string | null

  appraisal:
    risk_of_bias: low | some_concerns | high | unclear
    directness: direct | indirect | unclear
    precision: high | moderate | low | unclear
    applicability: high | moderate | low | unclear
    confidence: high | moderate | low | very_low | unclear

  provenance:
    retrieved_from: [string]
    full_text_available: boolean
    extraction_method: string
    verified_by_source_text: boolean
```

---

## 5. Claim object

Every clinically meaningful conclusion must become a claim object.

```yaml
claim:
  id: string
  text: string
  claim_type:
    - descriptive
    - association
    - causal
    - diagnostic
    - therapeutic
    - safety
    - guideline_recommendation
    - regulatory
    - emerging_evidence

  supporting_evidence_ids: [string]
  contradicting_evidence_ids: [string]

  confidence:
    level: high | moderate | low | very_low
    rationale: string

  safety:
    clinical_actionable: boolean
    requires_human_review: boolean
```

---

## 6. Orchestration state machine

```text
INTAKE
  ↓
QUESTION_STRUCTURED
  ↓
RESEARCH_PLAN_APPROVED
  ↓
DISCOVERY
  ↓
SCREENING
  ↓
FULLTEXT_RESOLUTION
  ↓
STRUCTURED_EXTRACTION
  ↓
APPRAISAL
  ↓
SYNTHESIS
  ↓
CLAIM_VERIFICATION
  ↓
SAFETY_REVIEW
  ↓
FINAL_REPORT
```

A skill may send the case backward when evidence is insufficient.

Example:

```text
APPRAISAL
  → insufficient direct evidence
  → DISCOVERY
```

---

## 7. Autonomy policy

### High autonomy

- query expansion
- metadata normalization
- deduplication
- citation graph traversal
- candidate screening
- full-text discovery
- study data extraction

### Medium autonomy

- PICO extraction
- study classification
- preliminary risk-of-bias assessment
- evidence comparison
- inconsistency detection

### Restricted autonomy

- final certainty judgment
- patient-specific treatment recommendation
- diagnosis
- medication initiation/discontinuation
- interpretation that conflicts with authoritative guidelines or regulatory labeling

These require explicit uncertainty handling and human clinical judgment.
