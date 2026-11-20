from .schema import SCHEMA_SQL

class Migrator:
    def __init__(self, db):
        self.db = db

    def apply_migrations(self):
        conn = self.db.get_connection()
        with conn:
            conn.executescript(SCHEMA_SQL)
