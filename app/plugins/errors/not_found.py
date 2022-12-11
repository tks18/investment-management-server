from app.plugins.errors.base import BaseError


class NotFound(BaseError):
    def __init__(self, message: str):
        super().__init__("Not Found", message, 404)
