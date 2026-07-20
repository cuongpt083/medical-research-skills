"""Use approved NCBI APIs/E-utilities; preserve PMID/PMCID/DOI and exact translated query."""
from execution.runtime.provider_base import CapabilityRequest, ProviderResultEnvelope

class PubMedAdapter:
    provider_name = "pubmed"
    def execute(self, request: CapabilityRequest) -> ProviderResultEnvelope:
        raise NotImplementedError(
            "Implement provider-specific HTTP client, pagination, normalization and provenance"
        )
