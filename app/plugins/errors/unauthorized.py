from app.plugins.errors.base import BaseError


class Unauthorized(BaseError):
    def __init__(self, message: str):
        super().__init__("Unauthorized", message, 401)
