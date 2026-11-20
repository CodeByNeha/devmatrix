from dataclasses import dataclass
from typing import Optional
from .base import BaseModel

@dataclass
class FocusSession(BaseModel):
    id: Optional[int]
    name: str
    state: str
    target_minutes: int
    elapsed_seconds: int
    started_at: str
    ended_at: Optional[str] = None
