from flask import request, jsonify
from app.plugins.dates import convert_string_to_date
from app.plugins.backend import api_methods
from app.plugins.finance import get_ticker_data
from app.plugins.server import exception_response_handler, ok_response
from app.plugins.errors import Unauthorized, BadRequest


def format_dates(dates: dict):
    result = {}
    for key, date in dates.items():
        result[key] = convert_string_to_date(date, "%Y-%m-%d")
    return result


def generate_market_data():
    try:
        token = request.headers.get("x-session-token")
        if token != None:
            token_response = api_methods["user"]["verify"](token)
            if token_response:
                data = request.json
                if data:
                    dates = format_dates({"start": data["start"], "end": data["end"]})
                    investment_master = api_methods["investments"]["get"](token)
                    all_ticker_df = get_ticker_data(
                        investment_master=investment_master,
                        start_date=dates["start"],
                        end_date=dates["end"],
                        token=token,
                    )
                    if len(all_ticker_df) > 0:
                        data_records = all_ticker_df.to_dict(orient="records")
                        return ok_response(data=data_records)
                    else:
                        return ok_response(data={})
            else:
                return Unauthorized("Bad Token Found in the Headers")
        else:
            return BadRequest("x-session-token", "request.headers")
    except Exception as Error:
        return exception_response_handler(Error)
