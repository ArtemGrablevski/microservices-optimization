import contextlib

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from faststream.rabbit import RabbitBroker

from api.dependencies import setup_dependencies
from api.dependencies.stubs import get_message_broker
from api.routes import setup_routes
from config import Settings
from db.connection.session import get_async_engine, get_sessionmaker


config = Settings()


@contextlib.asynccontextmanager
async def lifespan(app: FastAPI):
    message_broker = RabbitBroker(
        f"amqp://{config.rabbitmq_user}:{config.rabbitmq_password}"
        f"@{config.rabbitmq_host}:{config.rabbitmq_port}/"
    )
    await message_broker.connect()
    app.dependency_overrides[get_message_broker] = lambda: message_broker
    yield
    await message_broker.close()


def create_app() -> FastAPI:

    app = FastAPI(
        title="Auctions API",
        version="1.0",
        docs_url="/api/docs",
        lifespan=lifespan,
    )

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
