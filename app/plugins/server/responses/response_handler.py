from flask import Response, json


def send_response(response):
    return Response(
        json.dumps(response), status=response["status"], mimetype="application/json"
    )
