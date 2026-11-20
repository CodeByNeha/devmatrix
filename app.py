#!/usr/bin/env python3
import http.server
from devmatrix.storage.connection import Database
from devmatrix.storage.migrator import Migrator
from devmatrix.storage.log_repository import LogRepository
from devmatrix.storage.session_repository import SessionRepository
from devmatrix.services.log_service import LogService
from devmatrix.services.session_service import SessionService
from devmatrix.services.analytics_service import AnalyticsService
from devmatrix.api.router import Router
from devmatrix.api.handlers import ApiHandlers
from devmatrix.web.server import DevMatrixHttpHandler

def main():
    db = Database("devmatrix.db")
    Migrator(db).apply_migrations()
    log_repo = LogRepository(db)
    session_repo = SessionRepository(db)
    log_service = LogService(log_repo)
    session_service = SessionService(session_repo)
    analytics_service = AnalyticsService(log_repo, session_repo)

    router = Router()
    handlers = ApiHandlers(log_service, session_service, analytics_service)
    router.add("GET", "/api/logs", handlers.get_logs)
    router.add("POST", "/api/logs", handlers.post_log)
    router.add("GET", "/api/sessions", handlers.get_sessions)
    router.add("GET", "/api/metrics", handlers.get_metrics)
    router.add("GET", "/api/health", handlers.get_health)

    DevMatrixHttpHandler.router = router
    port = 7890
    print(f"[*] DevMatrix Server running on http://127.0.0.1:{port}")
    server = http.server.HTTPServer(("127.0.0.1", port), DevMatrixHttpHandler)
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\n[!] Stopping server...")

if __name__ == "__main__":
    main()
