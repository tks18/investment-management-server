from os import getenv
from app.plugins.errors import InternalServerError


def get_env_variable(key: str) -> str:
    value = getenv(key, "NA")
    if value != "NA":
        return value
    else:
        raise InternalServerError(f"Not Able to find {key} in the Environment")
