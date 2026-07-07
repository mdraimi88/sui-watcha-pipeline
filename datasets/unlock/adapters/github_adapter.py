from __future__ import annotations

from datasets.unlock.adapters.base_adapter import BaseUnlockAdapter
from datasets.unlock.models import UnlockModel


class GithubAdapter(BaseUnlockAdapter):

    @property
    def source_name(self) -> str:
        return "SUI Watcha Verified Data"

    @property
    def source_type(self) -> str:
        return "fallback"

    def fetch(self) -> UnlockModel:
        raise NotImplementedError
