from dataclasses import dataclass
from typing import Any

@dataclass
class ProviderRegistration:
    name: str
    capabilities: set[str]
    adapter: Any
    priority: int = 100

class ProviderRegistry:
    def __init__(self):
        self._providers = []

    def register(self, registration: ProviderRegistration):
        self._providers.append(registration)

    def resolve(self, capability: str):
        matches = [p for p in self._providers if capability in p.capabilities]
        return sorted(matches, key=lambda p: p.priority)
