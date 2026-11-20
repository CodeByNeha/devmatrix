import json
from .response import Response

class ApiHandlers:
    def __init__(self, log_service, session_service, analytics_service):
        self.log_service = log_service
        self.session_service = session_service
        self.analytics_service = analytics_service

    def get_logs(self, params, body):
        logs = [l.to_dict() for l in self.log_service.list_logs()]
        return Response.json({"logs": logs})

    def post_log(self, params, body):
        data = json.loads(body.decode("utf-8") or "{}")
        log = self.log_service.add_log(
            title=data.get("title", ""),
            category=data.get("category", "FEATURE"),
            tags=data.get("tags", ""),
            duration=data.get("duration", 30),
            notes=data.get("notes", "")
        )
        return Response.json(log.to_dict(), status=201)

    def get_sessions(self, params, body):
        sessions = [s.to_dict() for s in self.session_service.repo.get_recent()]
        return Response.json({"sessions": sessions})

    def get_metrics(self, params, body):
        metrics = self.analytics_service.calculate_summary().to_dict()
        return Response.json(metrics)

    def get_health(self, params, body):
        return Response.json({"status": "healthy", "service": "DevMatrix", "version": "0.1.0"})
