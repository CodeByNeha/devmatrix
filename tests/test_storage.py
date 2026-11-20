import unittest
import os
from devmatrix.storage.connection import Database
from devmatrix.storage.migrator import Migrator
from devmatrix.storage.log_repository import LogRepository
from devmatrix.models.work_log import WorkLog

class TestStorage(unittest.TestCase):
    def setUp(self):
        self.test_db = "test_devmatrix.db"
        self.db = Database(self.test_db)
        Migrator(self.db).apply_migrations()
        self.repo = LogRepository(self.db)

    def tearDown(self):
        self.db.close()
        if os.path.exists(self.test_db):
            os.remove(self.test_db)

    def test_log_crud(self):
        log = WorkLog(id=None, title="Database test", category="BUGFIX", tags="db", duration_minutes=40, created_at="2026-01-01", notes="testing")
        lid = self.repo.insert(log)
        self.assertIsNotNone(lid)
        all_logs = self.repo.get_all()
        self.assertEqual(len(all_logs), 1)
        self.assertEqual(all_logs[0].title, "Database test")

if __name__ == "__main__":
    unittest.main()
