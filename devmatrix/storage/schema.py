SCHEMA_SQL = """
CREATE TABLE IF NOT EXISTS work_logs (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    category TEXT NOT NULL,
    tags TEXT DEFAULT '',
    duration_minutes INTEGER DEFAULT 0,
    created_at TEXT NOT NULL,
    notes TEXT DEFAULT ''
);

CREATE TABLE IF NOT EXISTS sessions (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    state TEXT NOT NULL,
    target_minutes INTEGER DEFAULT 25,
    elapsed_seconds INTEGER DEFAULT 0,
    started_at TEXT NOT NULL,
    ended_at TEXT
);

CREATE TABLE IF NOT EXISTS tags (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT UNIQUE NOT NULL,
    color_hex TEXT DEFAULT '#3b82f6',
    usage_count INTEGER DEFAULT 0
);

CREATE INDEX IF NOT EXISTS idx_logs_category ON work_logs(category);
CREATE INDEX IF NOT EXISTS idx_logs_created_at ON work_logs(created_at);
"""

SCHEMA_SQL += """
CREATE INDEX IF NOT EXISTS idx_logs_composite ON work_logs(category, created_at);
"""
