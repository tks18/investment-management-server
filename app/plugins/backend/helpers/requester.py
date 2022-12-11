import requests
from app.plugins.errors import BaseError, InternalServerError


def requester(
    route: str,
    method: str,
    token: str,
    expected_status: int,
    headers: dict = {},
    data: dict = {},
    params: dict = {},
) -> dict:
    try:
        default_headers = {"x-session-token": token}
        merged_headers = {**default_headers, **headers}
        response = requests.request(
            url=route,
            method=method,
            params=params,
            headers=merged_headers,
            data=data,
        )
        if response.status_code == expected_status:
            body_data = response.json()
            return body_data
        else:
            raise InternalServerError(
                "Expected Status Code Not Met", "Request-Response Error"
            )
    except Exception as AppError:
        if isinstance(AppError, BaseError):
            raise AppError
        else:
            raise InternalServerError(
                "Not Able to Communicate with the requested URL", "Request Error"
            )
