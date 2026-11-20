import json
from dataclasses import dataclass, asdict
from datetime import datetime

@dataclass
class BaseModel:
    def to_dict(self) -> dict:
        return asdict(self)

    def to_json(self) -> str:
        return json.dumps(self.to_dict(), default=str)
