from flask import Flask
from waitress import serve


class Server:
    def __init__(self, name, host, port, routes):
        self.host = host
        self.port = port
        self.app = Flask(name)
        self.routes = routes
        self.host_routes(routes)

    def host_routes(self, routes, prev_route=""):
        for route in routes:
            if "routes" in route:
                new_route = prev_route + route["path"] if prev_route else route["path"]
                self.host_routes(route["routes"], new_route)
            else:
                new_route = prev_route + route["path"] if prev_route else route["path"]
                self.app.post(new_route)(route["handler"])

    def start_server(self):
        serve(self.app, host=self.host, port=self.port)
