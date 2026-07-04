from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Any


class BaseGenerator(ABC):
    """Base class for all dataset generators."""

    @property
    @abstractmethod
    def name(self) -> str:
        """Dataset name."""
        ...

    @abstractmethod
    def generate(self, data: Any) -> dict[str, Any]:
        """Generate normalized output."""
        ...

    def __str__(self) -> str:
        return self.name
