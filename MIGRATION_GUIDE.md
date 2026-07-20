# Migration Guide

Keep all prior reasoning, research-engine, evidence-governance and provider/execution specifications.

Final additions:
- `ResearchRun` contract;
- DAG/task state model;
- checkpoint/resume;
- human-in-the-loop rules;
- depth/budget modes;
- final report contract;
- deployment blueprint;
- acceptance criteria.

Recommended implementation order:
1. contracts/schemas;
2. orchestrator/state machine;
3. provider registry;
4. PubMed + metadata;
5. guideline/regulatory;
6. ClinicalTrials.gov;
7. full-text resolver;
8. dedup/version graph;
9. extraction/appraisal/synthesis;
10. citation verification;
11. safety gate;
12. audit/final report;
13. benchmark suite.

Implement one complete vertical slice before adding every provider.
