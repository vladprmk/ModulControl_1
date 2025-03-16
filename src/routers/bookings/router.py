from typing import Any

from fastapi import APIRouter, Depends, HTTPException

from src.db.engine import BookingRepository, UserRepository
from src.routers.auth.dependencies import get_active_user

from .dependencies import get_booking_repository, get_user_repository
from .schemas import BookingCreate, BookingResponse

router = APIRouter(prefix="/bookings", tags=["bookings"])


@router.post("", response_model=BookingResponse, status_code=201)
def create_booking(
    booking: BookingCreate,
    current_user=Depends(get_active_user),
    booking_repository: BookingRepository = Depends(get_booking_repository),
):
    if booking.check_in >= booking.check_out:
        raise HTTPException(
            status_code=400,
            detail="Check-in date must be earlier than check-out date",
        )

    ok = booking_repository.is_room_booked(
        room_id=booking.room_id,
        check_in=booking.check_in,
        check_out=booking.check_out,
    )
    if ok:
        raise HTTPException(
            status_code=400,
            detail="Room is already booked for the given period",
        )

    return booking_repository.insert(
        user_id=current_user.id,
        hotel_id=booking.hotel_id,
        room_id=booking.room_id,
        check_in=booking.check_in,
        check_out=booking.check_out,
    )


@router.get("", response_model=list[BookingResponse])
def list_user_bookings(
    current_user=Depends(get_active_user),
    booking_repository: BookingRepository = Depends(get_booking_repository),
):
    return booking_repository.select_by_user_id(current_user.id)


@router.delete("/{booking_id}", response_model=dict)
def cancel_booking(
    booking_id: int,
    current_user=Depends(get_active_user),
    booking_repository: BookingRepository = Depends(get_booking_repository),
):
    booking = booking_repository.select_by_id(booking_id)
    if not booking:
        raise HTTPException(status_code=404, detail="Booking not found")
    if booking.user_id != current_user.id:
        raise HTTPException(
            status_code=403,
            detail="You don't have access to cancel this booking",
        )
    booking_repository.delete(booking_id=booking_id)
    return {"message": "Booking cancelled"}


@router.patch("/{booking_id}/confirm", response_model=BookingResponse)
def confirm_booking(
    booking_id: int,
    current_user: dict[str, Any] = Depends(get_active_user),
    user_repository: UserRepository = Depends(get_user_repository),
    booking_repository: BookingRepository = Depends(get_booking_repository),
):
    booking = booking_repository.select_by_id(booking_id)
    if not booking:
        raise HTTPException(status_code=404, detail="Booking not found")

    if booking.user_id != current_user["id"]:
        raise HTTPException(
            status_code=403,
            detail="You don't have access to confirm this booking",
        )

    updated_booking = booking_repository.update_confirmed(booking_id)
    return updated_booking


def get_router() -> APIRouter:
    return router
