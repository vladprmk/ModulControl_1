from fastapi import Depends, Request
from sqlalchemy.engine import Engine

from src.db.engine import RoomRepository, room_table


def get_engine(request: Request) -> Engine:
    return request.app.state.engine


def get_room_repository(
    engine: Engine = Depends(get_engine),
) -> RoomRepository:
    return RoomRepository(engine=engine, table=room_table)
