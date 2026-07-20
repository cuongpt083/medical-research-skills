# Provider Interfaces

## LiteratureSearchProvider
`search(request) -> ProviderResultEnvelope`

Use for reproducible literature discovery. Preserve translated query, pagination,
stable identifiers and provenance. Candidate: PubMed/NCBI, Europe PMC.

## ScholarlyMetadataProvider
`lookup(identifier)` / `batch_lookup(identifiers)`

Candidate: Crossref, OpenAlex, Semantic Scholar.
Used for DOI/bibliographic reconciliation and enrichment, not clinical authority.

## CitationGraphProvider
`references(record_id)`, `citations(record_id)`, `related(record_id)`

Candidate: OpenAlex, Semantic Scholar.
Citation prominence must never equal evidence quality.

## TrialRegistryProvider
`search_trials(request)`, `get_trial(registry_id)`

Candidate: ClinicalTrials.gov.
Preserve registry ID, design, phase, recruitment status, intervention, outcomes,
enrollment, dates, results availability and last-update timestamp.

## GuidelineProvider
`search_guidelines(request)`, `get_guideline(document_id)`

Prefer first-party health authorities and specialty societies.
Preserve jurisdiction, issuing body, version/update date and supersession status.

## RegulatoryProvider
`search_products`, `get_label`, `get_approval_status`, `get_safety_notices`

Prefer first-party regulators. Never infer approval from scholarly publication.

## FullTextResolver
`resolve(record) -> FullTextResolution`

Prefer canonical/open legal access. Never bypass paywalls/access controls.

## PublicationIntegrityProvider
`check(record) -> IntegrityStatus`

Check retraction, expression of concern, correction/erratum and version/successor links.
