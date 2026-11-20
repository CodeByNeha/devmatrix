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
