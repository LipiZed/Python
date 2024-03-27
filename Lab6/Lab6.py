import sqlite3 as sq

with sq.connect("lab6.db") as con:
    cur = con.cursor()
    cur.execute('''SELECT Hotel.name, COUNT(Rooms.id) AS room_count
    FROM Hotel
    LEFT JOIN Rooms ON Hotel.id = Rooms.hotel_id
    GROUP BY Hotel.id;
    ''')
    result = cur.fetchall()
    print(result)
    cur.execute('''SELECT Rooms.*
    FROM Rooms
    LEFT JOIN Bookings ON Rooms.id = Bookings.room_id
    WHERE Bookings.check_in NOT BETWEEN '2023-03-01' AND '2023-03-10'
    AND Bookings.check_out NOT BETWEEN '2023-03-01' AND '2023-03-10'
    OR Bookings.id IS NULL;
    ''')
    result = cur.fetchall()
    print(result)
    cur.execute('''SELECT DISTINCT guest_name, guest_phone, guest_email
    FROM Bookings
    JOIN Rooms ON Bookings.room_id = Rooms.id
    JOIN Hotel ON Rooms.hotel_id = Hotel.id
    WHERE Hotel.name = 'Отель Россия';
    ''')
    result = cur.fetchall()
    print(result)
