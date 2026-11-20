from enum import Enum

class SessionState(Enum):
    PENDING = "PENDING"
    ACTIVE = "ACTIVE"
    PAUSED = "PAUSED"
    COMPLETED = "COMPLETED"

class LogCategory(Enum):
    FEATURE = "FEATURE"
    BUGFIX = "BUGFIX"
    REFACTOR = "REFACTOR"
    RESEARCH = "RESEARCH"
    TESTING = "TESTING"
    DEPLOY = "DEPLOY"

DEFAULT_PORT = 7890
DEFAULT_DB = 'devmatrix.db'
APP_NAME = 'DevMatrix'
