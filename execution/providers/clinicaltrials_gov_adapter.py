"""Registry evidence remains distinct from peer-reviewed publication evidence."""
from execution.runtime.provider_base import CapabilityRequest, ProviderResultEnvelope

class ClinicalTrialsGovAdapter:
    provider_name = "clinicaltrials_gov"
    def execute(self, request: CapabilityRequest) -> ProviderResultEnvelope:
        raise NotImplementedError(
            "Implement provider-specific HTTP client, pagination, normalization and provenance"
        )
