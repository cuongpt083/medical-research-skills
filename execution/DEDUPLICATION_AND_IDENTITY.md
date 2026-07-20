# Record Identity, Deduplication & Version Resolution

Priority:
1. normalized DOI exact match
2. PMID
3. PMCID
4. registry ID
5. trusted provider mapping
6. high-confidence bibliographic fingerprint

Fingerprint: normalized title + first author + year + journal.
Fuzzy title alone must not trigger high-confidence auto-merge.

Relations:
- SAME_RECORD
- SAME_STUDY_DIFFERENT_PUBLICATION
- PREPRINT_SUCCESSOR
- CORRECTION
- DISTINCT
- UNCERTAIN

Represent version graphs explicitly:
`Preprint → peer-reviewed successor → correction`.

Do not double-count multiple publications from the same underlying study.
Uncertain merges preserve both records pending review.
