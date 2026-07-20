# Skill: emerging-evidence-research

## 1. Mission
Detect, track, and contextualize early or evolving medical evidence without overstating maturity.

## 2. Trigger
Use for:
- “latest/newest” treatments or research;
- active clinical trials;
- pipeline drugs;
- preprints;
- conference findings;
- early-online evidence;
- horizon scanning.

## 3. Evidence maturity model
Classify every item:
```yaml
maturity:
  stage:
    - registered_not_recruiting
    - recruiting
    - active_not_recruiting
    - completed_unreported
    - results_posted_registry
    - conference_only
    - preprint
    - peer_reviewed_early_publication
    - mature_peer_reviewed
  peer_reviewed: boolean
  replicated: boolean | null
  regulatory_status: string | null
```

## 4. Trial registry protocol
For trials capture:
- registry ID;
- sponsor;
- phase;
- design;
- enrollment;
- intervention/comparator;
- primary outcome;
- recruitment status;
- start/completion dates;
- results availability;
- linked publications.

Do not describe an ongoing trial as evidence of efficacy.

## 5. Preprint protocol
For every preprint:
1. mark `PREPRINT` visibly;
2. identify server and date;
3. check whether a peer-reviewed version exists;
4. link versions when found;
5. compare major conclusions for material changes when feasible;
6. prohibit sole-support clinical recommendations.

## 6. Novelty verification
“New” means new relative to a defined date and evidence state.
Check:
- first posting/publication date;
- whether findings are actually new or a secondary analysis;
- prior versions;
- duplicate press-release coverage;
- whether regulatory/guideline status has changed.

## 7. Signal ranking
Prioritize emerging evidence using:
- study phase/design;
- sample size and event count;
- comparator quality;
- endpoint clinical relevance;
- consistency with prior evidence;
- replication;
- sponsor/source transparency;
- peer-review status.

Do not rank by media attention alone.

## 8. Provider contracts
```yaml
TrialRegistryProvider:
  returns: [registry_id, status, phase, design, dates, outcomes, results, linked_publications, provenance]
PreprintProvider:
  returns: [preprint_id, version, posted_date, authors, abstract, doi_or_link, provenance]
EarlyPublicationProvider:
  returns: [publication_metadata, publication_status, provenance]
```

## 9. Stopping rules
Stop when:
- major active/just-reported trials relevant to the question are covered;
- important preprint-to-publication versions are resolved;
- incremental search yields no new evidence likely to change the horizon-scan conclusion.

## 10. Output labels
Every synthesis must separate:
- `ESTABLISHED_EVIDENCE`
- `EMERGING_PEER_REVIEWED`
- `PREPRINT_OR_UNREVIEWED`
- `ONGOING_TRIAL`
- `REGULATORY_STATUS`

## 11. Quality gates
- EE-QG1 Evidence maturity labeled.
- EE-QG2 Trial status verified.
- EE-QG3 Ongoing trials not treated as positive evidence.
- EE-QG4 Preprint/final versions deduplicated and linked.
- EE-QG5 “Latest” claim anchored to explicit dates.

## 12. Tests
### EE-T1 Recruiting phase III
Report as ongoing trial, not demonstrated efficacy.

### EE-T2 Preprint later published
Prefer and link the peer-reviewed version; preserve material differences.

### EE-T3 Press release
A company press release without inspectable study data cannot be treated as equivalent to a paper or registry results record.

## Cross-cutting invariants
- Preserve provenance for every query, result, transformation, and exclusion decision.
- Never infer evidence quality from search rank, citation count, journal prestige, or AI relevance score alone.
- Normalize provider-specific records before downstream reasoning.
- Do not fabricate identifiers, metadata, access status, publication status, or study results.
- Mark uncertainty explicitly; absence of evidence is not evidence of absence.
