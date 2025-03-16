from datetime import date

from pydantic import BaseModel


class UserInDB(BaseModel):
    id: int
    username: str
    pwhash: str


class HotelInDB(BaseModel):
    id: int
    name: str
    location: str
    rating: float
    available: bool


class RoomInDB(BaseModel):
    id: int
    hotel_id: int
    room_number: str
    room_type: str
    price: float
    available: bool


class BookingInDB(BaseModel):
    id: int
    user_id: int
    hotel_id: int
    room_id: int
    check_in: date
    check_out: date
    confirmed: bool
