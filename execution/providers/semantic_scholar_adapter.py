"""Metadata/graph; AI summaries may assist screening but never become atomic evidence."""
from execution.runtime.provider_base import CapabilityRequest, ProviderResultEnvelope

class SemanticScholarAdapter:
    provider_name = "semantic_scholar"
    def execute(self, request: CapabilityRequest) -> ProviderResultEnvelope:
        raise NotImplementedError(
            "Implement provider-specific HTTP client, pagination, normalization and provenance"
        )
