from app.plugins.errors.base import BaseError


class Forbidden(BaseError):
    def __init__(self, message: str):
        super().__init__("Forbidden", message, 403)
