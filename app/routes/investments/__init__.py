from app.routes.investments.generate_market_data import generate_market_data

investment_route_config = {
    "path": "/investments",
    "routes": [{"path": "/generate-market-data", "handler": generate_market_data}],
}
