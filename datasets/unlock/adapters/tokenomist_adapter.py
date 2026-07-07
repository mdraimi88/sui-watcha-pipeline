from __future__ import annotations

from datasets.unlock.adapters.base_adapter import BaseUnlockAdapter
from datasets.unlock.models import UnlockModel


class TokenomistAdapter(BaseUnlockAdapter):

    @property
    def source_name(self) -> str:
        return "Tokenomist"

    @property
    def source_type(self) -> str:
        return "primary"

    def fetch(self) -> UnlockModel:
        raise NotImplementedError
