from __future__ import annotations

from typing import Any

from core.base_fetcher import BaseFetcher
from core.base_generator import BaseGenerator
from core.base_validator import BaseValidator
from core.validation_result import ValidationResult


class PipelineRunner:
    """Coordinates the fetch → validate → generate workflow."""

    def __init__(
        self,
        fetcher: BaseFetcher,
        validator: BaseValidator,
        generator: BaseGenerator,
    ) -> None:
        self._fetcher = fetcher
        self._validator = validator
        self._generator = generator

    def run(self) -> dict[str, Any]:
        # Step 1: Fetch
        raw_data = self._fetcher.fetch()

        # Step 2: Validate
        result: ValidationResult = self._validator.validate(raw_data)

        if not result.valid:
            raise ValueError(
                f"Validation failed: {result.errors}"
            )

        # Step 3: Generate
        return self._generator.generate(raw_data)
