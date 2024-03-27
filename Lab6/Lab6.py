import sqlite3 as sq

with sq.connect("lab6.db") as con:
    cur = con.cursor()
    cur.execute('''INSERT INTO Hotel (name, address, phone, email) VALUES ('Отель Россия', 'ул. Пушкина, 10', '+7 (495) 123-45-67', 'hotel@rossiya.ru')''')
    cur.execute('''INSERT INTO Hotel (name, address, phone, email) VALUES ('Гранд Отель', 'ул. Ленина, 25', '+7 (495) 987-65-43', 'grandhotel@mail.ru')''')
    cur.execute('''INSERT INTO Hotel (name, address, phone, email) VALUES ('Отель Уют', 'ул. Горького, 32', '+7 (495) 222-33-55', 'uyut@hotel.ru')''')
    cur.execute('''INSERT INTO Rooms (hotel_id, room_number, type, price, capacity) VALUES (1, 101, 'Одиночный', 3000.0, 1)''')
    cur.execute('''INSERT INTO Rooms (hotel_id, room_number, type, price, capacity) VALUES (1, 102, 'Двухместный', 4000.0, 2)''')
    cur.execute('''INSERT INTO Rooms (hotel_id, room_number, type, price, capacity) VALUES (2, 205, 'Люкс', 7000.0, 2)''')
    cur.execute('''INSERT INTO Bookings (room_id, guest_name, guest_phone, guest_email, check_in, check_out) VALUES (1, 'Иван Петров', '+7 (916) 123-45-67', 'ivan.petrov@mail.ru', '2023-03-01', '2023-03-05')''')
    cur.execute('''INSERT INTO Bookings (room_id, guest_name, guest_phone, guest_email, check_in, check_out) VALUES (2, 'Анна Сидорова', '+7 (903) 987-65-43', 'anna.sidorova@mail.ru', '2023-03-10', '2023-03-12')''')
    cur.execute('''INSERT INTO Bookings (room_id, guest_name, guest_phone, guest_email, check_in, check_out) VALUES (3, 'Петр Иванов', '+7 (926) 222-33-55', 'petr.ivanov@mail.ru', '2023-03-15', '2023-03-18')''')
