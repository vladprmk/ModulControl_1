from fastapi import APIRouter, Depends, HTTPException

from src.db.engine import RoomRepository

from .dependencies import get_room_repository
from .schemas import RoomCreate, RoomCreateResponse

router = APIRouter(prefix="/hotels/{hotel_id}/rooms", tags=["rooms"])


@router.get("", response_model=list[RoomCreateResponse])
def list_rooms(
    hotel_id: int,
    room_repository: RoomRepository = Depends(get_room_repository),
):
    return room_repository.select_by_hotel_id(hotel_id)


@router.post("/register", response_model=RoomCreateResponse, status_code=201)
def create_room(
    hotel_id: int,
    room_create: RoomCreate,
    room_repository: RoomRepository = Depends(get_room_repository),
):
    if room := room_repository.insert(
        hotel_id=hotel_id,
        room_number=room_create.room_number,
        price=room_create.price,
        room_type=room_create.room_type,
    ):
        return room

    raise HTTPException(
        status_code=400,
        detail="Failed to create room",
    )
