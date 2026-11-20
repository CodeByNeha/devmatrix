from dataclasses import dataclass
from .base import BaseModel

@dataclass
class Tag(BaseModel):
    id: int
    name: str
    color_hex: str = "#3b82f6"
    usage_count: int = 0
