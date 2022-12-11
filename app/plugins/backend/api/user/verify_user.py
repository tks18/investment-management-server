from app.plugins.backend.helpers import requester
from app.plugins.errors import BaseError, InternalServerError
from app.plugins.backend.routes import backend_routes


def verify_user(token: str):
    try:
        response = requester(
            method="post",
            route=backend_routes["user"]["verify"],
            token=token,
            expected_status=200,
            data={"token": token},
        )
        return response["data"]["authenticated"]
    except Exception as Error:
        if isinstance(Error, BaseError):
            raise Error
        else:
            raise InternalServerError("Error While Authenticating User Token")
