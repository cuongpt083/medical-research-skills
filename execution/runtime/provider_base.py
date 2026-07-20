from __future__ import annotations
from dataclasses import dataclass, field
from typing import Any, Optional, Protocol
import hashlib, json, time, uuid

@dataclass(frozen=True)
class CapabilityRequest:
    capability: str
    query_text: str
    structured_terms: tuple[str, ...] = ()
    filters: dict[str, Any] = field(default_factory=dict)
    cursor: Optional[str] = None
    page_size: int = 20
    research_case_id: str = ""
    intent: str = ""
    request_id: str = field(default_factory=lambda: str(uuid.uuid4()))

    def normalized_payload(self) -> dict[str, Any]:
        return {
            "capability": self.capability,
            "query_text": " ".join(self.query_text.split()),
            "structured_terms": sorted(self.structured_terms),
            "filters": self.filters,
            "cursor": self.cursor,
            "page_size": self.page_size,
            "intent": self.intent,
        }

    def query_hash(self) -> str:
        data = json.dumps(
            self.normalized_payload(), sort_keys=True, ensure_ascii=False
        ).encode("utf-8")
        return hashlib.sha256(data).hexdigest()

@dataclass
class NormalizedRecord:
    record_id: str
    identifiers: dict[str, Optional[str]]
    bibliographic: dict[str, Any]
    links: dict[str, Any]
    graph: dict[str, Any]
    status: dict[str, Any]
    provenance: dict[str, Any]

@dataclass
class ProviderResultEnvelope:
    request_id: str
    provider: str
    capability: str
    retrieved_at: str
    records: list[NormalizedRecord]
    next_cursor: Optional[str] = None
    warnings: list[str] = field(default_factory=list)
    cache_hit: bool = False

class ProviderAdapter(Protocol):
    provider_name: str
    def execute(self, request: CapabilityRequest) -> ProviderResultEnvelope: ...

class ProviderError(RuntimeError):
    def __init__(self, *, provider: str, error_type: str, message: str,
                 retryable: bool, retry_after_seconds: Optional[int] = None):
        super().__init__(message)
        self.provider = provider
        self.error_type = error_type
        self.retryable = retryable
        self.retry_after_seconds = retry_after_seconds

def utc_timestamp() -> str:
    return time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())
