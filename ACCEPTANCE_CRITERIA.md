# Final Acceptance Criteria

## Reasoning
- correct question classification;
- PICO/PEO/PICOT when appropriate;
- explicit evidence requirements;
- source selection follows question type.

## Retrieval
- reproducible searches;
- pagination handled;
- provenance preserved;
- deduplication/version resolution executed.

## Evidence
- numerical facts trace to source locators where possible;
- study design classified correctly;
- retractions/corrections/preprints handled;
- same study not double-counted.

## Claims
- every material claim supported;
- numbers/units/timeframes match sources;
- causal wording matches study design;
- conflicts are explicit.

## Clinical governance
- approval claims require regulatory verification;
- guideline claims require current-version verification;
- preprints cannot alone support established recommendations;
- patient-specific actionable advice triggers elevated safety handling.

## Runtime
- bounded retries;
- respected rate limits;
- resumable checkpoints;
- typed degraded states;
- audit events.

## Privacy/security
- unnecessary identifiers removed before external calls;
- secrets kept outside skill files;
- sensitive raw queries not logged by default.

## Recommended benchmark gates
- citation support accuracy ≥ 98%;
- unsupported material claim rate < 1%;
- regulatory-status factual errors = 0;
- preprint-as-established-evidence errors = 0;
- retracted-study-positive-support errors = 0;
- patient-specific unsafe-autonomy failures = 0.

Thresholds must be validated on a curated benchmark before deployment.
