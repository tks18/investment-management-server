from app.plugins.errors import BaseError, InternalServerError
from app.plugins.server.responses.response_handler import send_response


def exception_response_handler(Exception: Exception):
    if isinstance(Exception, BaseError):
        data = {
            "status": Exception.status,
            "errorname": Exception.errorname,
            "message": Exception.message,
        }
        return send_response(data)
    else:
        error = InternalServerError("Exception Caught in Exception Handler")
        data = {
            "status": error.status,
            "errorname": error.errorname,
            "message": error.message,
        }
        return send_response(data)
