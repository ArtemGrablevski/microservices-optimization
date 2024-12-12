from fastapi import FastAPI

from api.routes import (
    auction,
)


def setup_routes(app: FastAPI) -> None:
    app.include_router(auction.router)
