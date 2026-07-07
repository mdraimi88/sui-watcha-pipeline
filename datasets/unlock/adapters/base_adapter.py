from __future__ import annotations

from abc import ABC, abstractmethod

from datasets.unlock.models import UnlockModel


class BaseUnlockAdapter(ABC):
    """Base adapter for unlock data sources."""

    @property
    @abstractmethod
    def source_name(self) -> str:
        ...

    @property
    @abstractmethod
    def source_type(self) -> str:
        ...

    @abstractmethod
    def fetch(self) -> UnlockModel:
        """Fetch unlock data from the source."""
        ...
