from __future__ import annotations

import sys
import typing
from contextlib import asynccontextmanager

from fastapi import FastAPI, Request
from fastapi.responses import RedirectResponse
from loguru import logger
from sqlalchemy import create_engine

from .db import metadata
from .routers import auth

if typing.TYPE_CHECKING:
    from typing import Any, Callable


logger.remove(0)

logger.add(
    sys.stdout,
    format="<green>{time:MMMM D, YYYY > HH:mm:ss}</green> | {level} | <level>{message}</level>",  # noqa: E501
)
logger.add(
    "main.log",
    format="<green>{time:MMMM D, YYYY > HH:mm:ss}</green> | {level} | <level>{message}</level>",  # noqa: E501
)


@asynccontextmanager
async def lifespan(app: FastAPI):
    engine = create_engine(
        "sqlite:///ModulControl_1.db",
        echo=True,
    )
    metadata.create_all(engine)
    app.state.engine = engine

    logger.info("Connected to database")
    yield

    engine.dispose()
    logger.info("Disconnected from database")


app = FastAPI(
    version="0.0.0a0",
    title="ModulControl_1",
    description=(
        "Universal, typed, and high-performance REST API "
        "for seamless hotel room booking and management."
    ),
    lifespan=lifespan,
)

app.include_router(auth.get_router())


@app.middleware("http")
async def http_middleware(
    request: Request, call_next: Callable[[Request], Any]
) -> Any:
    logger.opt(colors=True).info(
        f"<red>{request.method} {request.url.path}</red>"
    )
    response = await call_next(request)
    return response


@app.get("/", include_in_schema=False)
async def docs():
    return RedirectResponse("/docs")
