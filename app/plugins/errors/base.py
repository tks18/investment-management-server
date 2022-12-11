class BaseError(Exception):
    def __init__(self, errorname, message, status):
        super().__init__(message)
        self.errorname = errorname
        self.message = message
        self.status = status
