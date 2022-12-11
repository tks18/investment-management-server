from app.plugins.backend.helpers import requester
from app.plugins.errors import BaseError, InternalServerError
from app.plugins.backend.routes import backend_routes


def get_calendar_date_id(token: str, date: str) -> int:
    try:
        response = requester(
            method="post",
            route=backend_routes["data"]["masters"]["calendar"]["dateid"],
            token=token,
            expected_status=200,
            data={"dateToFind": date},
        )
        date_id = response["data"]["dateId"]
        return date_id
    except Exception as Error:
        if isinstance(Error, BaseError):
            raise Error
        else:
            raise InternalServerError("Error Getting Dateid from Backend Server")
