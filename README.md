# `ModulControl_1`

Universal, typed, and high-performance REST API for seamless hotel room booking and management.

* [AlloyTools/org.alloytools.alloy](https://github.com/AlloyTools/org.alloytools.alloy)
* [SonarSource/sonarqube](https://github.com/SonarSource/sonarqube)

---

## **Endpoints**

### **Auth**

#### `POST /api/auth/register`
**Register a new user**

**Input:**
```json
{
    "username": "",
    "password": ""
}
```

**Response:**
```json
{
    "id": 0,
    "username": ""
}
```

#### `POST /api/auth/login`
**Authenticate user and return JWT token**

**Input:**
```json
{
    "username": "",
    "password": ""
}
```

**Response:**
```json
{
    "token": "",
    "token_type": "bearer"
}
```

#### `GET /api/auth/me`
**Retrieve the currently logged-in user**

**Input:**
```json
{
    "token": ""
}
```

**Response:**
```json
{
    "id": 0,
    "username": ""
}
```

---

### **Users**

#### `GET /api/users`
**Retrieve a list of all users (admin only)**

**Response:**
```json
[
    {
        "id": 0,
        "username": "",
        "email": "",
        "role": "user"
    }
]
```

#### `GET /api/users/{user_id}`
**Retrieve details of a specific user**

**Response:**
```json
{
    "id": 0,
    "username": "",
    "email": "",
    "role": "user"
}
```

#### `PUT /api/users/{user_id}`
**Update user details**

**Input:**
```json
{
    "username": "",
    "email": ""
}
```

**Response:**
```json
{
    "id": 0,
    "username": "",
    "email": ""
}
```

#### `DELETE /api/users/{user_id}`
**Delete a user (admin only)**

**Response:**
```json
{
    "message": "User deleted successfully."
}
```

---

### **Hotels**

#### `GET /api/hotels`
**Retrieve all hotels**

**Response:**
```json
[
    {
        "id": 0,
        "name": "",
        "location": "",
        "rating": 0.0,
        "available": true
    }
]
```

#### `GET /api/hotels/{hotel_id}`
**Retrieve details of a specific hotel**

**Response:**
```json
{
    "id": 0,
    "name": "",
    "location": "",
    "rating": 0.0,
    "available": true,
    "rooms": [
        {
            "id": 0,
            "room_number": "101",
            "room_type": "deluxe",
            "price": 100.0,
            "available": true
        }
    ]
}
```

#### `POST /api/hotels/register`
**Register a new hotel (admin only)**

**Input:**
```json
{
    "name": "",
    "location": ""
}
```

**Response:**
```json
{
    "id": 0,
    "name": "",
    "location": "",
    "rating": 0.0,
    "available": true
}
```

---

### **Rooms**

#### `GET /api/rooms/{room_id}`
**Retrieve room details**

**Response:**
```json
{
    "id": 0,
    "room_number": "101",
    "room_type": "deluxe",
    "price": 100.0,
    "available": true
}
```

#### `POST /api/rooms/add`
**Add a new room to a hotel (hotel manager only)**

**Input:**
```json
{
    "hotel_id": 0,
    "room_number": "101",
    "room_type": "deluxe",
    "price": 100.0
}
```

**Response:**
```json
{
    "id": 0,
    "hotel_id": 0,
    "room_number": "101",
    "room_type": "deluxe",
    "price": 100.0,
    "available": true
}
```

#### `DELETE /api/rooms/{room_id}`
**Delete a room (hotel manager only)**

**Response:**
```json
{
    "message": "Room deleted successfully."
}
```

---

### **Bookings**

#### `POST /api/bookings/create`
**Create a new booking**

**Input:**
```json
{
    "user_id": 0,
    "room_id": 0,
    "check_in": "2024-06-01",
    "check_out": "2024-06-05"
}
```

**Response:**
```json
{
    "id": 0,
    "user_id": 0,
    "room_id": 0,
    "check_in": "2024-06-01",
    "check_out": "2024-06-05",
    "status": "confirmed"
}
```

#### `GET /api/bookings/{booking_id}`
**Retrieve booking details**

**Response:**
```json
{
    "id": 0,
    "user_id": 0,
    "room_id": 0,
    "check_in": "2024-06-01",
    "check_out": "2024-06-05",
    "status": "confirmed"
}
```

#### `DELETE /api/bookings/{booking_id}`
**Cancel a booking**

**Response:**
```json
{
    "message": "Booking canceled successfully."
}
```

---

### **Payments**

#### `POST /api/payments/process`
**Process a payment for a booking**

**Input:**
```json
{
    "booking_id": 0,
    "amount": 100.0,
    "payment_method": "credit_card"
}
```

**Response:**
```json
{
    "message": "Payment successful."
}
```

#### `GET /api/payments/{payment_id}`
**Retrieve payment details**

**Response:**
```json
{
    "id": 0,
    "booking_id": 0,
    "amount": 100.0,
    "status": "paid"
}
```
