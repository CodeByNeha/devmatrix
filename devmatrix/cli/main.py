import argparse
import sys
from ..storage.connection import Database
from ..storage.migrator import Migrator
from ..storage.log_repository import LogRepository
from ..storage.session_repository import SessionRepository
from ..services.log_service import LogService
from ..services.session_service import SessionService
from ..services.analytics_service import AnalyticsService

def build_parser():
    parser = argparse.ArgumentParser(prog="devmatrix", description="DevMatrix developer work tracking CLI")
    sub = parser.add_subparsers(dest="command")

    # log command
    log_p = sub.add_parser("log", help="Record a work log entry")
    log_p.add_argument("title", help="Work log description")
    log_p.add_argument("--category", "-c", default="FEATURE", help="Log category")
    log_p.add_argument("--minutes", "-m", type=int, default=30, help="Duration in minutes")
    log_p.add_argument("--tags", "-t", default="", help="Comma-separated tags")

    # list command
    sub.add_parser("list", help="List recent work logs")

    # stats command
    sub.add_parser("stats", help="Display work telemetry summary")

    return parser

def run_cli(args=None):
    parser = build_parser()
    opts = parser.parse_args(args)

    db = Database("devmatrix.db")
    Migrator(db).apply_migrations()
    log_repo = LogRepository(db)
    session_repo = SessionRepository(db)
    log_service = LogService(log_repo)
    analytics = AnalyticsService(log_repo, session_repo)

    if opts.command == "log":
        entry = log_service.add_log(title=opts.title, category=opts.category, tags=opts.tags, duration=opts.minutes)
        print(f"[+] Logged #{entry.id}: {entry.title} ({entry.duration_minutes}m, {entry.category})")
    elif opts.command == "list":
        logs = log_service.list_logs(limit=10)
        print("Recent Work Logs:")
        for l in logs:
            print(f"  [{l.id}] {l.created_at} - {l.title} ({l.duration_minutes}m) [{l.category}]")
    elif opts.command == "stats":
        m = analytics.calculate_summary()
        print("DevMatrix Telemetry Summary:")
        print(f"  Total logs:         {m.total_logs}")
        print(f"  Total time tracked: {m.total_minutes} mins")
        print(f"  Top category:       {m.top_category}")
    else:
        parser.print_help()
