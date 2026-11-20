import unittest
import os
from devmatrix.storage.connection import Database
from devmatrix.storage.migrator import Migrator
from devmatrix.storage.log_repository import LogRepository
from devmatrix.storage.session_repository import SessionRepository
from devmatrix.services.log_service import LogService
from devmatrix.services.analytics_service import AnalyticsService

class TestServices(unittest.TestCase):
    def setUp(self):
        self.test_db = "test_services.db"
        self.db = Database(self.test_db)
        Migrator(self.db).apply_migrations()
        self.log_repo = LogRepository(self.db)
        self.session_repo = SessionRepository(self.db)
        self.log_service = LogService(self.log_repo)
        self.analytics = AnalyticsService(self.log_repo, self.session_repo)

    def tearDown(self):
        self.db.close()
        if os.path.exists(self.test_db):
            os.remove(self.test_db)

    def test_add_log_service(self):
        log = self.log_service.add_log("Refactor auth", "REFACTOR", "security", 45)
        self.assertIsNotNone(log.id)
        stats = self.analytics.calculate_summary()
        self.assertEqual(stats.total_logs, 1)
        self.assertEqual(stats.total_minutes, 45)
        self.assertEqual(stats.top_category, "REFACTOR")

if __name__ == "__main__":
    unittest.main()
