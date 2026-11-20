from datetime import datetime
from typing import List, Optional
from ..models.work_log import WorkLog

class LogService:
    def __init__(self, log_repo):
        self.repo = log_repo

    def add_log(self, title: str, category: str = "FEATURE", tags: str = "", duration: int = 30, notes: str = "") -> WorkLog:
        log = WorkLog(
            id=None,
            title=title.strip(),
            category=category.upper(),
            tags=tags.strip(),
            duration_minutes=duration,
            created_at=datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            notes=notes
        )
        log.validate()
        log.id = self.repo.insert(log)
        return log

    def list_logs(self, limit: int = 50) -> List[WorkLog]:
        return self.repo.get_all(limit=limit)

    def remove_log(self, log_id: int) -> bool:
        return self.repo.delete(log_id)
