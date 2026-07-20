# Execution & Tooling Architecture — v0.5

## Objective
Translate the reasoning/evidence architecture into executable provider contracts without coupling skills to vendors.

```text
Skill intent
→ Capability interface
→ Provider adapter
→ Raw provider response
→ Normalization
→ Provenance envelope
→ ResearchCase / EvidenceItem
```

Skills must never depend directly on provider-specific JSON.

## Capability interfaces
- `LiteratureSearchProvider`
- `ScholarlyMetadataProvider`
- `CitationGraphProvider`
- `TrialRegistryProvider`
- `GuidelineProvider`
- `RegulatoryProvider`
- `FullTextResolver`
- `PublicationIntegrityProvider`

## Adapter boundary
Adapters handle request construction, authentication/configuration, rate limiting,
retries, parsing, normalization, provider-error mapping and provenance capture.

Adapters must not decide clinical evidence strength, infer regulatory approval,
synthesize evidence, silently merge conflicts, or discard provenance.

## Request lifecycle
```text
Canonical request validation
→ Cache lookup
→ Rate-limit admission
→ Provider request
→ Retry/backoff
→ Parse + normalize
→ Schema validation
→ Cache write
→ Provenance envelope
```

## Failure taxonomy
`AUTH_ERROR`, `RATE_LIMITED`, `TIMEOUT`, `TRANSIENT_PROVIDER_ERROR`,
`PERMANENT_PROVIDER_ERROR`, `INVALID_RESPONSE`, `SCHEMA_VALIDATION_FAILED`,
`NOT_FOUND`, `ACCESS_RESTRICTED`, `ROBOTS_OR_TERMS_BLOCK`, `UNSUPPORTED_QUERY`.

## Runtime rules
- maximum 4 attempts by default;
- exponential backoff + jitter;
- respect `Retry-After`;
- do not loop retries on deterministic auth/validation failures;
- cache metadata separately from current-status conclusions;
- remove unnecessary patient identifiers before external calls;
- log query hashes instead of sensitive raw queries by default.
