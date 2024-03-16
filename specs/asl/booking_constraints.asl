module BookingConstraints

open HotelBooking

fact RoomMustExist {
    all b: Booking |
        some h: Hotel | h = b.room.hotel
}

fact PreventOverbooking {
    all b1, b2: Booking |
        b1 != b2 =>
        (b1.room = b2.room and 
         b1.startDate < b2.endDate and 
         b2.startDate < b1.endDate) implies
        b1.user != b2.user
}

run {} for 5 User, 5 Hotel, 5 Room, 10 Booking
