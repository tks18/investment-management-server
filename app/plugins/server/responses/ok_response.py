from app.plugins.server.responses.response_handler import send_response


def ok_response(data):
    return send_response({"status": 200, "data": data})
