class DevMatrixError(Exception):
    """Base exception for DevMatrix."""
    pass

class RecordNotFoundError(DevMatrixError):
    pass

class ValidationError(DevMatrixError):
    pass

class StateError(DevMatrixError):
    pass
