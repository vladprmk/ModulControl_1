from datetime import date

from sqlalchemy import (
    Boolean,
    Column,
    Date,
    Engine,
    Float,
    ForeignKey,
    Integer,
    MetaData,
    String,
    Table,
)

from .models import BookingInDB, HotelInDB, RoomInDB, UserInDB

metadata = MetaData()

user_table = Table(
    "user",
    metadata,
    Column("id", Integer, primary_key=True, autoincrement=True),
    Column("username", String(32)),
    Column("pwhash", String(72)),
)

hotel_table = Table(
    "hotel",
    metadata,
    Column("id", Integer, primary_key=True, autoincrement=True),
    Column("name", String(32)),
    Column("location", String(64)),
    Column("rating", Float, default=0.0),
    Column("available", Boolean, default=True),
)

room_table = Table(
    "room",
    metadata,
    Column("id", Integer, primary_key=True, autoincrement=True),
    Column("hotel_id", Integer, ForeignKey("hotel.id"), nullable=False),
    Column("room_number", String(10), nullable=False),
    Column("room_type", String(50), nullable=False),
    Column("price", Float, nullable=False),
    Column("available", Boolean, default=True),
)

booking_table = Table(
    "booking",
    metadata,
    Column("id", Integer, primary_key=True, autoincrement=True),
    Column("user_id", Integer, nullable=False),
    Column("hotel_id", Integer, nullable=False),
    Column("room_id", Integer, nullable=False),
    Column("check_in", Date, nullable=False),
    Column("check_out", Date, nullable=False),
    Column("confirmed", Boolean, default=False),
)


class UserRepository:
    def __init__(self, engine: Engine, table: Table) -> None:
        self._engine = engine
        self._table = table

    def insert(self, *, username: str, pwhash: str) -> UserInDB | None:
        with self._engine.connect() as conn:
            result = conn.execute(
                self._table.insert()
                .values(username=username, pwhash=pwhash)
                .returning(
                    self._table.c.id,
                    self._table.c.username,
                    self._table.c.pwhash,
                )
            )
            row = result.fetchone()
            conn.commit()
        return (
            UserInDB(
                id=row.id,
                username=row.username,
                pwhash=row.pwhash,
            )
            if row
            else None
        )

    def select_by_username(self, username: str) -> UserInDB | None:
        with self._engine.connect() as conn:
            result = conn.execute(
                self._table.select().where(self._table.c.username == username)
            )
            row = result.fetchone()
        return (
            UserInDB(
                id=row.id,
                username=row.username,
                pwhash=row.pwhash,
            )
            if row
            else None
        )

    def select_by_id(self, user_id: int) -> UserInDB | None:
        with self._engine.connect() as conn:
            result = conn.execute(
                self._table.select().where(self._table.c.id == user_id)
            )
            row = result.fetchone()
        return (
            UserInDB(
                id=row.id,
                username=row.username,
                pwhash=row.pwhash,
            )
            if row
            else None
        )


class HotelRepository:
    def __init__(self, engine: Engine, table: Table):
        self.engine = engine
        self.table = table

    def select_all(self) -> list[HotelInDB]:
        with self.engine.connect() as conn:
            result = conn.execute(self.table.select())
            rows = result.fetchall()
        return [
            HotelInDB(
                id=row.id,
                name=row.name,
                location=row.location,
                rating=row.rating,
                available=row.available,
            )
            for row in rows
        ]

    def insert(
        self,
        name: str,
        location: str,
        rating: float = 0.0,
        available: bool = True,
    ) -> HotelInDB | None:
        with self.engine.connect() as conn:
            result = conn.execute(
                self.table.insert()
                .values(
                    name=name,
                    location=location,
                    rating=rating,
                    available=available,
                )
                .returning(
                    self.table.c.id,
                    self.table.c.name,
                    self.table.c.location,
                    self.table.c.rating,
                    self.table.c.available,
                )
            )
            row = result.fetchone()
            conn.commit()
        return (
            HotelInDB(
                id=row.id,
                name=row.name,
                location=row.location,
                rating=row.rating,
                available=row.available,
            )
            if row
            else None
        )

    def get_hotel_by_id(self, hotel_id: int) -> HotelInDB | None:
        with self.engine.connect() as conn:
            result = conn.execute(
                self.table.select().where(self.table.c.id == hotel_id)
            )
            row = result.fetchone()
        return (
            HotelInDB(
                id=row.id,
                name=row.name,
                location=row.location,
                rating=row.rating,
                available=row.available,
            )
            if row
            else None
        )


class RoomRepository:
    def __init__(self, engine: Engine, table: Table) -> None:
        self._engine = engine
        self._table = table

    def insert(
        self,
        *,
        hotel_id: int,
        room_number: str,
        room_type: str,
        price: float,
        available: bool = True,
    ) -> RoomInDB | None:
        with self._engine.connect() as conn:
            result = conn.execute(
                self._table.insert()
                .values(
                    hotel_id=hotel_id,
                    room_number=room_number,
                    room_type=room_type,
                    price=price,
                    available=available,
                )
                .returning(
                    self._table.c.id,
                    self._table.c.hotel_id,
                    self._table.c.room_number,
                    self._table.c.room_type,
                    self._table.c.price,
                    self._table.c.available,
                )
            )
            row = result.fetchone()
            conn.commit()
        if row:
            return RoomInDB(
                id=row.id,
                hotel_id=row.hotel_id,
                room_number=row.room_number,
                room_type=row.room_type,
                price=row.price,
                available=row.available,
            )
        return None

    def select_by_hotel_id(self, hotel_id: int) -> list[RoomInDB]:
        with self._engine.connect() as conn:
            stmt = self._table.select().where(
                self._table.c.hotel_id == hotel_id
            )
            result = conn.execute(stmt)
            rows = result.fetchall()
        return [
            RoomInDB(
                id=row.id,
                hotel_id=row.hotel_id,
                room_number=row.room_number,
                room_type=row.room_type,
                price=row.price,
                available=row.available,
            )
            for row in rows
        ]

    def select_by_id(self, room_id: int) -> RoomInDB | None:
        with self._engine.connect() as conn:
            stmt = self._table.select().where(self._table.c.id == room_id)
            result = conn.execute(stmt)
            row = result.fetchone()
        if row:
            return RoomInDB(
                id=row.id,
                hotel_id=row.hotel_id,
                room_number=row.room_number,
                room_type=row.room_type,
                price=row.price,
                available=row.available,
            )
        return None


class BookingRepository:
    def __init__(self, engine: Engine, table: Table) -> None:
        self._engine = engine
        self._table = table

    def insert(
        self,
        *,
        user_id: int,
        hotel_id: int,
        room_id: int,
        check_in: date,
        check_out: date,
        confirmed: bool = False,
    ) -> BookingInDB | None:
        with self._engine.connect() as conn:
            result = conn.execute(
                self._table.insert()
                .values(
                    user_id=user_id,
                    hotel_id=hotel_id,
                    room_id=room_id,
                    check_in=check_in,
                    check_out=check_out,
                    confirmed=confirmed,
                )
                .returning(
                    self._table.c.id,
                    self._table.c.user_id,
                    self._table.c.hotel_id,
                    self._table.c.room_id,
                    self._table.c.check_in,
                    self._table.c.check_out,
                    self._table.c.confirmed,
                )
            )
            row = result.fetchone()
            conn.commit()
        if row:
            return BookingInDB(
                id=row.id,
                user_id=row.user_id,
                hotel_id=row.hotel_id,
                room_id=row.room_id,
                check_in=row.check_in,
                check_out=row.check_out,
                confirmed=row.confirmed,
            )
        return None

    def select_by_id(self, booking_id: int) -> BookingInDB | None:
        with self._engine.connect() as conn:
            stmt = self._table.select().where(self._table.c.id == booking_id)
            result = conn.execute(stmt)
            row = result.fetchone()
        if row:
            return BookingInDB(
                id=row.id,
                user_id=row.user_id,
                hotel_id=row.hotel_id,
                room_id=row.room_id,
                check_in=row.check_in,
                check_out=row.check_out,
                confirmed=row.confirmed,
            )
        return None

    def select_by_user_id(self, user_id: int) -> list[BookingInDB]:
        with self._engine.connect() as conn:
            stmt = self._table.select().where(self._table.c.user_id == user_id)
            result = conn.execute(stmt)
            rows = result.fetchall()
        return [
            BookingInDB(
                id=row.id,
                user_id=row.user_id,
                hotel_id=row.hotel_id,
                room_id=row.room_id,
                check_in=row.check_in,
                check_out=row.check_out,
                confirmed=row.confirmed,
            )
            for row in rows
        ]

    def is_room_booked(
        self, *, room_id: int, check_in: date, check_out: date
    ) -> bool:
        with self._engine.connect() as conn:
            stmt = self._table.select().where(
                self._table.c.room_id == room_id,
                self._table.c.check_in < check_out,
                self._table.c.check_out > check_in,
            )
            result = conn.execute(stmt)
            row = result.fetchone()
        return row is not None

    def delete(self, booking_id: int) -> None:
        with self._engine.connect() as conn:
            conn.execute(
                self._table.delete().where(self._table.c.id == booking_id)
            )
            conn.commit()

    def update_confirmed(
        self, booking_id: int, *, confirmed: bool = True
    ) -> BookingInDB | None:
        with self._engine.connect() as conn:
            conn.execute(
                self._table.update()
                .where(self._table.c.id == booking_id)
                .values(confirmed=confirmed)
            )
            conn.commit()
        return self.select_by_id(booking_id)
