"""Metadata/citation graph; citation count never equals evidence quality."""
from execution.runtime.provider_base import CapabilityRequest, ProviderResultEnvelope

class OpenAlexAdapter:
    provider_name = "openalex"
    def execute(self, request: CapabilityRequest) -> ProviderResultEnvelope:
        raise NotImplementedError(
            "Implement provider-specific HTTP client, pagination, normalization and provenance"
        )
