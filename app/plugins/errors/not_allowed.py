from app.plugins.errors.base import BaseError


class NotAllowed(BaseError):
    def __init__(self, message: str):
        super().__init__("Not Allowed", message, 406)
