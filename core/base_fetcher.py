from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Any


class BaseFetcher(ABC):
    """Base class for all dataset fetchers."""

    @property
    @abstractmethod
    def name(self) -> str:
        """Dataset name."""

    @abstractmethod
    def fetch(self) -> Any:
        """Fetch raw data from the source."""

    def __str__(self) -> str:
        return self.name
