from __future__ import annotations

__all__: typing.Sequence[str] = (
    "get_router",
    "auth_settings",
)

import typing

from .config import auth_settings
from .router import get_router
