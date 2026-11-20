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

    def is_active(self) -> bool:
        return self.state == "ACTIVE"

    def progress_percentage(self) -> float:
        if self.target_minutes <= 0:
            return 100.0
        return min(100.0, round((self.elapsed_seconds / (self.target_minutes * 60)) * 100, 2))
