module HotelBooking

sig User {}
sig Hotel {}
sig Room {
    hotel: one Hotel
}
sig Booking {
    user: one User,
    room: one Room,
    startDate, endDate: one Int
}

fact NoDoubleBooking {
    all b1, b2: Booking |
        b1 != b2 =>
        (b1.room = b2.room and 
         b1.startDate < b2.endDate and 
         b2.startDate < b1.endDate) implies
        (b1.user != b2.user or b1.startDate != b2.startDate or b1.endDate != b2.endDate)
}

fact ValidDates {
    all b: Booking |
        b.startDate < b.endDate
}

fact UniqueHotelPerRoom {
    all r: Room |
        one r.hotel
}

fact RoomMustHaveHotel {
    all r: Room | some r.hotel
}

fact ValidDateRange {
    all b: Booking |
        b.startDate >= 0 and b.endDate <= 100
}

run {} for 5 User, 5 Hotel, 5 Room, 10 Booking, 10 Int
