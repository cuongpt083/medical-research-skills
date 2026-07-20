# Provider Selection & Fallback Policy

## Literature
Biomedical bibliographic source + scholarly metadata/graph source +
citation expansion as needed.

## Drug approval / label
First-party regulator → official product information → scholarly evidence
for efficacy/safety context. Never reverse authority order.

## Guidelines
Issuing authority/specialty society → current-version verification →
repository/discovery source only as fallback.

## Trials
Registry record → linked publications/results → reconcile identifiers/status/dates.

Fallback may improve discovery/access but must not silently downgrade authority
for approval status, official warnings or current guideline recommendations.
If first-party verification fails, emit `UNVERIFIED_CURRENT_STATUS`.
