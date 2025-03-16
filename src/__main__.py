import asyncio

from hypercorn import Config
from hypercorn.asyncio import serve

from .main import app

asyncio.run(serve(app, Config()))  # type: ignore[arg-type]
