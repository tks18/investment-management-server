from app.plugins.errors.base import BaseError


class BadRequest(BaseError):
    def __init__(self, expected: str, inData: str):
        error_name = "Bad Request"
        message = f"Expected {expected} in {inData}"
        super().__init__(error_name, message, 400)
