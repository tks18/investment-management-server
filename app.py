from os import getcwd, path
from dotenv import load_dotenv

load_dotenv(dotenv_path=path.join(getcwd(), ".env"))

from app import Server
from app import routes


investment_server = Server("investment-server", "0.0.0.0", 5000, routes)

investment_server.start_server()
