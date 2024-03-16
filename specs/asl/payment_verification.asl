module PaymentVerification

sig Payment {
    booking: one Booking,
    amount: one Int,
    status: one Status
}

abstract sig Status {}
one sig Pending, Completed, Failed extends Status {}

fact ValidPaymentAmount {
    all p: Payment |
        p.amount > 0
}

fact PaymentMustHaveBooking {
    all p: Payment |
        some b: Booking | b = p.booking
}

fact PaymentStatusConstraints {
    all p: Payment |
        p.status in (Pending + Completed + Failed)
}

run {} for 5 Booking, 5 Payment
