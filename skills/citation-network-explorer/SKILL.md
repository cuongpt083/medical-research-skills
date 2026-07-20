# Skill: citation-network-explorer

## 1. Mission
Expand a research landscape from one or more seed papers using citation relationships and similarity signals while controlling graph-induced bias.

## 2. Trigger
Use when:
- a landmark/seed paper is known;
- keyword search appears incomplete;
- historical evidence evolution matters;
- related clusters or follow-up studies are needed;
- searching for replications, critiques, or later evidence.

## 3. Inputs
```yaml
citation_network_request:
  research_case_id: string
  seed_records: [identifier]
  goals: [foundational, follow_up, replication, critique, related_cluster, recent_updates]
  depth: 1 | 2
  max_candidates: integer
```

Depth >2 requires explicit justification because graph expansion grows rapidly and can amplify citation bias.

## 4. Traversal modes
### Backward chaining
Inspect references cited by seed paper.
Best for foundational methods, earlier trials, and historical context.

### Forward chaining
Inspect papers citing seed.
Best for follow-up evidence, replication, critique, and later applications.

### Relatedness expansion
Use co-citation, bibliographic coupling, semantic similarity, or provider-specific related-paper signals.
Treat these as discovery signals, not quality scores.

## 5. Graph candidate scoring
Candidate prioritization may consider:
- topical relevance;
- study design fit;
- recency relative to seed;
- direct citation relationship;
- whether it is a replication/critique;
- novelty relative to already included evidence.

Citation count may be metadata but must not dominate evidence priority.

## 6. Bias controls
Citation graphs can overrepresent:
- famous authors/journals;
- positive findings;
- older publications;
- tightly connected research communities.

Therefore:
1. supplement graph traversal with independent keyword/semantic search when conclusions matter;
2. actively search for contradictory/negative evidence;
3. do not infer consensus from graph density alone.

## 7. Provider contract
```yaml
CitationGraphProvider:
  capabilities:
    - references
    - citations
    - related_records
  returns:
    - relationship_type
    - source_record_id
    - target_record
    - provider_score_optional
    - provenance
```

## 8. Version/entity resolution
Before traversal, resolve seed identity by DOI/PMID/title and distinguish:
- preprint vs final publication;
- protocol vs results;
- correction/retraction;
- secondary analysis vs primary report.

## 9. Stopping rules
Stop when:
- depth limit reached;
- new nodes fail relevance threshold;
- no new high-value study designs/contradictory evidence emerge;
- max candidate budget reached with limitation declared.

## 10. Output
```yaml
citation_network_result:
  seeds: []
  nodes: []
  edges: []
  prioritized_candidates: []
  clusters: []
  contradictory_or_critical_records: []
  saturation_assessment: object
```

## 11. Quality gates
- CN-QG1 Seed identity verified.
- CN-QG2 Relationship provenance retained.
- CN-QG3 Relatedness/citation metrics not treated as evidence quality.
- CN-QG4 Contradictory evidence actively considered.
- CN-QG5 Graph search limitations declared.

## 12. Tests
### CN-T1 Highly cited weak study
High citation count alone must not elevate methodological confidence.

### CN-T2 Seed retracted
A retracted seed must be flagged; graph can be explored historically but cannot silently support claims.

### CN-T3 Citation bubble
A dense cluster from one research group should trigger independent search rather than imply consensus.

## Cross-cutting invariants
- Preserve provenance for every query, result, transformation, and exclusion decision.
- Never infer evidence quality from search rank, citation count, journal prestige, or AI relevance score alone.
- Normalize provider-specific records before downstream reasoning.
- Do not fabricate identifiers, metadata, access status, publication status, or study results.
- Mark uncertainty explicitly; absence of evidence is not evidence of absence.
