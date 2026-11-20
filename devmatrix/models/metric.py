from dataclasses import dataclass
from .base import BaseModel

@dataclass
class MetricSummary(BaseModel):
    total_logs: int
    total_minutes: int
    total_sessions: int
    completed_sessions: int
    top_category: str
