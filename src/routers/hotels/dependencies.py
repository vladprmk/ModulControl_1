from fastapi import Depends, Request
from sqlalchemy.engine import Engine

from src.db import HotelRepository, hotel_table


def get_engine(request: Request) -> Engine:
    return request.app.state.engine


def get_hotel_repository(
    engine: Engine = Depends(get_engine),
) -> HotelRepository:
    return HotelRepository(engine=engine, table=hotel_table)
