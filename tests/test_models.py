import unittest
from devmatrix.models.work_log import WorkLog
from devmatrix.models.session import FocusSession

class TestModels(unittest.TestCase):
    def test_work_log_validation(self):
        log = WorkLog(id=1, title="Test Feature", category="FEATURE", tags="unit", duration_minutes=25, created_at="2026-01-01 10:00:00")
        log.validate()
        self.assertEqual(log.title, "Test Feature")

    def test_work_log_empty_title(self):
        log = WorkLog(id=1, title="", category="FEATURE", tags="", duration_minutes=10, created_at="2026-01-01 10:00:00")
        with self.assertRaises(ValueError):
            log.validate()

    def test_session_progress(self):
        s = FocusSession(id=1, name="Coding", state="ACTIVE", target_minutes=20, elapsed_seconds=600, started_at="2026-01-01")
        self.assertEqual(s.progress_percentage(), 50.0)

if __name__ == "__main__":
    unittest.main()
