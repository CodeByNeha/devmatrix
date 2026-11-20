from typing import List, Optional
from ..models.work_log import WorkLog

class LogRepository:
    def __init__(self, db):
        self.db = db

    def insert(self, log: WorkLog) -> int:
        conn = self.db.get_connection()
        cur = conn.cursor()
        cur.execute(
            "INSERT INTO work_logs (title, category, tags, duration_minutes, created_at, notes) VALUES (?, ?, ?, ?, ?, ?)",
            (log.title, log.category, log.tags, log.duration_minutes, log.created_at, log.notes)
        )
        conn.commit()
        return cur.lastrowid

    def get_all(self, limit: int = 50) -> List[WorkLog]:
        conn = self.db.get_connection()
        cur = conn.cursor()
        cur.execute("SELECT * FROM work_logs ORDER BY id DESC LIMIT ?", (limit,))
        rows = cur.fetchall()
        return [WorkLog(id=r["id"], title=r["title"], category=r["category"], tags=r["tags"],
                        duration_minutes=r["duration_minutes"], created_at=r["created_at"], notes=r["notes"]) for r in rows]

    def delete(self, log_id: int) -> bool:
        conn = self.db.get_connection()
        cur = conn.cursor()
        cur.execute("DELETE FROM work_logs WHERE id = ?", (log_id,))
        conn.commit()
        return cur.rowcount > 0
