import sqlite3 as sq

with sq.connect("lab6.db") as con:
    cur = con.cursor()
    cur.execute("""CREATE TABLE Hotel (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    address TEXT NOT NULL,
    phone TEXT NOT NULL,
    email TEXT NOT NULL
    )""")
    cur.execute("""CREATE TABLE Rooms (
    id INTEGER PRIMARY KEY,
    hotel_id INTEGER NOT NULL,
    room_number INTEGER NOT NULL,
    type TEXT NOT NULL,
    price REAL NOT NULL,
    capacity INTEGER NOT NULL,
    FOREIGN KEY(hotel_id) REFERENCES Hotel(id)
    )""")
    cur.execute("""CREATE TABLE Bookings (
    id INTEGER PRIMARY KEY,
    room_id INTEGER NOT NULL,
    guest_name TEXT NOT NULL,
    guest_phone TEXT NOT NULL,
    guest_email TEXT NOT NULL,
    check_in DATE NOT NULL,
    check_out DATE NOT NULL,
    FOREIGN KEY(room_id) REFERENCES Rooms(id)
    )""")
    