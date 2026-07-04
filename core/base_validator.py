from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Any

from core.validation_result import ValidationResult


class BaseValidator(ABC):
    """Base class for all dataset validators."""

    @property
    @abstractmethod
    def name(self) -> str:
        """Dataset name."""
        ...

    @abstractmethod
    def validate(self, data: Any) -> ValidationResult:
        """Validate dataset."""
        ...

    def __str__(self) -> str:
        return self.name
