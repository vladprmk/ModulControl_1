# `ModulControl_1`

Universal, typed, and high-performance REST API for seamless hotel room booking and management.

* [AlloyTools/org.alloytools.alloy](https://github.com/AlloyTools/org.alloytools.alloy)
* [SonarSource/sonarqube](https://github.com/SonarSource/sonarqube)

---

## **Quality Model Based on ISO/IEC 25010**

### **1. Software Quality Attributes**
The quality model for **ModulControl_1** is designed according to **ISO/IEC 25010** and focuses on the following attributes:

| **Quality Attribute**      | **Sub-Attributes**                                      | **Description** |
|----------------------------|--------------------------------------------------------|-----------------|
| **Functionality**          | Functional completeness, correctness, appropriateness | Ensures API meets all specified functional requirements |
| **Performance Efficiency** | Response time, resource utilization                   | API should handle multiple concurrent requests with minimal latency |
| **Usability**              | Learnability, accessibility, operability              | Endpoints should be easy to use and well-documented |
| **Reliability**            | Availability, fault tolerance                         | Ensures system is always operational and handles failures gracefully |
| **Security**               | Confidentiality, integrity, authentication            | Prevents unauthorized access and ensures data protection |
| **Maintainability**        | Modularity, reusability, testability                  | Code should be structured following SOLID principles |
| **Compatibility**          | Interoperability, co-existence                       | Ensures integration with external systems like third-party payment processors |

### **2. Quality Metrics and Justification**
To measure and evaluate the above quality attributes, we define specific metrics:

#### **2.1 Functionality**
- **Metric:** Coverage of Functional Requirements
- **Formula:** `(Implemented Functionalities / Total Required Functionalities) × 100%`
- **Justification:** Ensures that all required functionalities are covered and implemented correctly.

#### **2.2 Performance Efficiency**
- **Metric:** Average Response Time
- **Formula:** `Σ(Response Time) / Total API Requests`
- **Justification:** Guarantees that API endpoints respond efficiently under normal and high-load conditions.

#### **2.3 Usability**
- **Metric:** User Satisfaction Score
- **Formula:** `(Positive User Feedback / Total Feedback) × 100%`
- **Justification:** Ensures the API is user-friendly, and responses are intuitive.

#### **2.4 Reliability**
- **Metric:** System Uptime Percentage
- **Formula:** `(System Uptime / Total Time) × 100%`
- **Justification:** Measures API availability and resilience against failures.

#### **2.5 Security**
- **Metric:** Number of Security Vulnerabilities
- **Formula:** `Number of Detected Security Issues per Month`
- **Justification:** Ensures the API remains secure against threats like SQL injection, XSS, and unauthorized access.

#### **2.6 Maintainability**
- **Metric:** Code Complexity Score (Cyclomatic Complexity)
- **Justification:** Measures how easy it is to maintain and extend the codebase following SOLID principles.

#### **2.7 Compatibility**
- **Metric:** Number of Successful API Integrations
- **Formula:** `(Successful API Integrations / Total Integration Attempts) × 100%`
- **Justification:** Ensures the system is easily integrable with other platforms (e.g., third-party payment gateways).

## **Conclusion**
The quality model based on **ISO/IEC 25010** ensures **ModulControl_1** meets industry standards for API performance, security, maintainability, and usability. By adhering to **best practices**, the project ensures long-term scalability and reliability. Future improvements will include **automated security testing** and **integration monitoring** to maintain high software quality.


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
