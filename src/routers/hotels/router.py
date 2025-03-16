from fastapi import APIRouter, Depends, HTTPException

from src.db import HotelRepository

from .dependencies import get_hotel_repository
from .schemas import HotelCreate, HotelCreateResponse, HotelDetail

router = APIRouter(prefix="/hotels", tags=["hotels"])


@router.get("", response_model=list[HotelCreateResponse])
def list_hotels(
    hotel_repository: HotelRepository = Depends(get_hotel_repository),
):
    return hotel_repository.select_all()


@router.get("/{hotel_id}", response_model=HotelDetail)
def get_hotel(
    hotel_id: int,
    hotel_repository: HotelRepository = Depends(get_hotel_repository),
):
    hotel = hotel_repository.get_hotel_by_id(hotel_id)
    if not hotel:
        raise HTTPException(status_code=404, detail="Hotel not found")
    hotel_data = hotel.model_dump()
    hotel_data["rooms"] = []
    return hotel_data


@router.post("/register", response_model=HotelCreateResponse, status_code=201)
def create_hotel(
    hotel: HotelCreate,
    hotel_repository: HotelRepository = Depends(get_hotel_repository),
):
    hotel_in_db = hotel_repository.insert(
        name=hotel.name,
        location=hotel.location,
    )
    if not hotel_in_db:
        raise HTTPException(status_code=500, detail="Failed to create hotel")
    return hotel_in_db


def get_router() -> APIRouter:
    return router
