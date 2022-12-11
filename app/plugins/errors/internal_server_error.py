from app.plugins.errors.base import BaseError


class InternalServerError(BaseError):
    def __init__(self, message: str, error_name="Internal Server Error"):
        super().__init__(error_name, message, 500)
