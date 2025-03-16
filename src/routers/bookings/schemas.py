from datetime import date

from pydantic import BaseModel


class BookingCreate(BaseModel):
    hotel_id: int
    room_id: int
    check_in: date
    check_out: date


class BookingResponse(BaseModel):
    id: int
    user_id: int
    hotel_id: int
    room_id: int
    check_in: date
    check_out: date
    confirmed: bool
