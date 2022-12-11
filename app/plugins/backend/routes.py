from app.plugins.environment import get_env_variable

backend_url = get_env_variable("BACKEND_URL")

backend_routes = {
    "data": {
        "masters": {
            "calendar": {
                "dateid": f"{backend_url}/api/data/masters/calendar/get-date-id"
            },
            "investments": {
                "get": f"{backend_url}/api/data/masters/investments/master/get"
            },
        },
    },
    "user": {"verify": f"{backend_url}/api/user/verify"},
}
