from collections import Counter
from ..models.metric import MetricSummary

class AnalyticsService:
    def __init__(self, log_repo, session_repo):
        self.log_repo = log_repo
        self.session_repo = session_repo

    def calculate_summary(self) -> MetricSummary:
        logs = self.log_repo.get_all(limit=500)
        sessions = self.session_repo.get_recent(limit=500)

        total_minutes = sum(l.duration_minutes for l in logs)
        completed = sum(1 for s in sessions if s.state == "COMPLETED")

        cats = [l.category for l in logs]
        top_cat = Counter(cats).most_common(1)[0][0] if cats else "NONE"

        return MetricSummary(
            total_logs=len(logs),
            total_minutes=total_minutes,
            total_sessions=len(sessions),
            completed_sessions=completed,
            top_category=top_cat
        )

# Metric aggregation enhancement 53

# Metric aggregation enhancement 58
