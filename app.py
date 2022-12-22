from os import getcwd, path
from dotenv import load_dotenv

load_dotenv(dotenv_path=path.join(path.dirname(__file__), ".env"))

from app import Server
from app import routes
from app.plugins import get_env_variable

port = get_env_variable("PORT")

investment_server = Server(
    "investment-server", "0.0.0.0", port if port else 5000, routes
)

investment_server.start_server()
