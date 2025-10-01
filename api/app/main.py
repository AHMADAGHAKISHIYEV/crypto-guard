from contextlib import asynccontextmanager

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from .config import get_settings
from .deps import init_db
from .routes import (
    alerts,
    auth,
    backtest,
    health,
    orders,
    portfolio,
    signals,
    status,
)

DISCLAIMER_TEXT = "Yatırım tavsiyesi değildir."


@asynccontextmanager
async def lifespan(app: FastAPI):
    init_db()
    yield


def create_app() -> FastAPI:
    settings = get_settings()
    app = FastAPI(title=settings.app_name, lifespan=lifespan)

    app.add_middleware(
        CORSMiddleware,
        allow_origins=settings.allowed_origins,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    for router in [
        health.router,
        auth.router,
        portfolio.router,
        signals.router,
        orders.router,
        backtest.router,
        alerts.router,
        status.router,
    ]:
        app.include_router(router)

    @app.get("/", tags=["meta"])
    async def root():
        return {"message": "Crypto Guard API", "disclaimer": DISCLAIMER_TEXT}

    return app


app = create_app()
