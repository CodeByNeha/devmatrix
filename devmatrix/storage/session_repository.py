from typing import List, Optional
from ..models.session import FocusSession

class SessionRepository:
    def __init__(self, db):
        self.db = db

    def insert(self, s: FocusSession) -> int:
        conn = self.db.get_connection()
        cur = conn.cursor()
        cur.execute(
            "INSERT INTO sessions (name, state, target_minutes, elapsed_seconds, started_at, ended_at) VALUES (?, ?, ?, ?, ?, ?)",
            (s.name, s.state, s.target_minutes, s.elapsed_seconds, s.started_at, s.ended_at)
        )
        conn.commit()
        return cur.lastrowid

    def get_by_id(self, s_id: int) -> Optional[FocusSession]:
        conn = self.db.get_connection()
        cur = conn.cursor()
        cur.execute("SELECT * FROM sessions WHERE id = ?", (s_id,))
        r = cur.fetchone()
        if not r:
            return None
        return FocusSession(id=r["id"], name=r["name"], state=r["state"], target_minutes=r["target_minutes"],
                            elapsed_seconds=r["elapsed_seconds"], started_at=r["started_at"], ended_at=r["ended_at"])

    def update_state(self, s_id: int, state: str, elapsed: int, ended_at: Optional[str] = None):
        conn = self.db.get_connection()
        conn.execute(
            "UPDATE sessions SET state = ?, elapsed_seconds = ?, ended_at = ? WHERE id = ?",
            (state, elapsed, ended_at, s_id)
        )
        conn.commit()

    def get_recent(self, limit: int = 10) -> List[FocusSession]:
        conn = self.db.get_connection()
        cur = conn.cursor()
        cur.execute("SELECT * FROM sessions ORDER BY id DESC LIMIT ?", (limit,))
        return [FocusSession(id=r["id"], name=r["name"], state=r["state"], target_minutes=r["target_minutes"],
                             elapsed_seconds=r["elapsed_seconds"], started_at=r["started_at"], ended_at=r["ended_at"]) for r in cur.fetchall()]
