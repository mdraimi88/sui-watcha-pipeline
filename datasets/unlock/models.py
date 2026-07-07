from __future__ import annotations

from datetime import datetime

from pydantic import BaseModel, ConfigDict


class UnlockModel(BaseModel):
    model_config = ConfigDict(
        frozen=True,
        extra="ignore",
    )

    unlock_date: datetime

    amount: float

    percent: float

    source: str
