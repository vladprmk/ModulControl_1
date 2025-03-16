from pydantic import BaseModel, Field


class RoomCreate(BaseModel):
    room_number: str = Field(..., min_length=1, max_length=10)
    room_type: str = Field(..., min_length=1, max_length=50)
    price: float = Field(..., gt=0)


class RoomCreateResponse(BaseModel):
    id: int
    room_number: str
    room_type: str
    price: float
    available: bool = True
