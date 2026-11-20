from datetime import datetime
from typing import Optional
from ..models.session import FocusSession

class SessionService:
    def __init__(self, session_repo):
        self.repo = session_repo

    def start_session(self, name: str, target_minutes: int = 25) -> FocusSession:
        s = FocusSession(
            id=None,
            name=name,
            state="ACTIVE",
            target_minutes=target_minutes,
            elapsed_seconds=0,
            started_at=datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        )
        s.id = self.repo.insert(s)
        return s

    def complete_session(self, s_id: int) -> Optional[FocusSession]:
        s = self.repo.get_by_id(s_id)
        if not s:
            return None
        now_str = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.repo.update_state(s_id, "COMPLETED", s.target_minutes * 60, ended_at=now_str)
        s.state = "COMPLETED"
        s.elapsed_seconds = s.target_minutes * 60
        s.ended_at = now_str
        return s
