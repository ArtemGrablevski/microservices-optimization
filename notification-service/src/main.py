from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from routes import router


def create_app() -> FastAPI:

    app = FastAPI(
        title="Notification service API",
        version="1.0",
        docs_url="/api/docs"
    )

    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"]
    )

    app.include_router(router)

    return app


app = create_app()
