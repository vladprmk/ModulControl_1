from __future__ import annotations

import os
import typing

from dotenv import load_dotenv

if typing.TYPE_CHECKING:
    from typing import Final

load_dotenv()

JWT_SECRET_KEY: Final[str | None] = os.getenv("JWT_SECRET_KEY")
JWT_ALGORITHM: Final[str | None] = os.getenv("JWT_ALGORITHM")
ACCESS_TOKEN_EXPIRE_MINUTES: Final[str | None] = os.getenv(
    "ACCESS_TOKEN_EXPIRE_MINUTES"
)
