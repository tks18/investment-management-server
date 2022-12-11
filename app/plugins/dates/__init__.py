from datetime import datetime
from app.plugins.errors import BadRequest


def convert_string_to_date(date_str: str, fmt: str) -> datetime:
    try:
        return datetime.strptime(date_str, fmt)
    except Exception:
        raise BadRequest(
            "date_str and fmt to be of type string and datetime format strings respectively",
            "request",
        )


def convert_date_to_string(date: datetime, fmt: str) -> str:
    try:
        return datetime.strftime(date, fmt)
    except Exception:
        raise BadRequest(
            "date and fmt to be of type datetime and datetime format strings respectively",
            "request",
        )
