import os
from dataclasses import dataclass
from pathlib import Path

@dataclass
class AppConfig:
    db_path: str = "devmatrix.db"
    port: int = 7890
    debug: bool = False
    data_dir: str = ".devmatrix"

    @classmethod
    def load(cls) -> "AppConfig":
        return cls(
            db_path=os.getenv("DEV_DB_PATH", "devmatrix.db"),
            port=int(os.getenv("DEV_PORT", "7890")),
            debug=os.getenv("DEV_DEBUG", "0") == "1",
        )
