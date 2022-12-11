from app.plugins.backend.helpers import requester
from app.plugins.errors import BaseError, InternalServerError
from app.plugins.backend.routes import backend_routes
from pandas import DataFrame


def get_investment_master_data(token: str) -> DataFrame:
    try:
        response = requester(
            method="post",
            route=backend_routes["data"]["masters"]["investments"]["get"],
            token=token,
            expected_status=200,
        )
        master_docs = response["data"]["docs"]
        master_docs_df = DataFrame(master_docs)
        return master_docs_df
    except Exception as Error:
        if isinstance(Error, BaseError):
            raise Error
        else:
            raise InternalServerError(
                "Error While Getting Investment Master Docs from Backend"
            )
