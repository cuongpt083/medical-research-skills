"""DOI/bibliographic metadata reconciliation only; not clinical/regulatory authority."""
from execution.runtime.provider_base import CapabilityRequest, ProviderResultEnvelope

class CrossrefAdapter:
    provider_name = "crossref"
    def execute(self, request: CapabilityRequest) -> ProviderResultEnvelope:
        raise NotImplementedError(
            "Implement provider-specific HTTP client, pagination, normalization and provenance"
        )
