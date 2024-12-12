from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from api.dependencies import setup_dependencies
from api.routes import setup_routes
from config import Settings
from db.connection.session import get_async_engine, get_sessionmaker


def create_app() -> FastAPI:

    app = FastAPI(
        title="Auctions API",
        version="1.0",
        docs_url="/api/docs"
    )

    config = Settings()

    engine = get_async_engine(config.postgres_dsn)
    sessionmaker = get_sessionmaker(engine)

    setup_dependencies(
        app=app,
        sessionmaker=sessionmaker,
    )
    setup_routes(app)

    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"]
    )

    return app


app = create_app()
