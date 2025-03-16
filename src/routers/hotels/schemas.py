from pydantic import BaseModel, Field


class HotelCreate(BaseModel):
    name: str = Field(..., min_length=1, max_length=100)
    location: str = Field(..., min_length=1, max_length=100)


class HotelCreateResponse(BaseModel):
    id: int
    name: str
    location: str
    rating: float = 0.0
    available: bool = True


class HotelDetail(HotelCreateResponse):
    rooms: list = []
