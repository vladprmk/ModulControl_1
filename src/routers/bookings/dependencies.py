from fastapi import Depends, Request
from sqlalchemy.engine import Engine

from src.db import (
    BookingRepository,
    UserRepository,
    booking_table,
    user_table,
)


def get_engine(request: Request) -> Engine:
    return request.app.state.engine


def get_booking_repository(
    engine: Engine = Depends(get_engine),
) -> BookingRepository:
    return BookingRepository(engine=engine, table=booking_table)


def get_user_repository(
    engine: Engine = Depends(get_engine),
) -> UserRepository:
    return UserRepository(engine=engine, table=user_table)
