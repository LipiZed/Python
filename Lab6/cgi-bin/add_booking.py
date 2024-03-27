#!/usr/bin/env python3

import cgi
import sqlite3

conn = sqlite3.connect('lab6.db')
cursor = conn.cursor()

form = cgi.FieldStorage()
room_id = form.getvalue('room_id')
guest_name = form.getvalue('guest_name')
guest_phone = form.getvalue('guest_phone')
guest_email = form.getvalue('guest_email')
check_in = form.getvalue('check_in')
check_out = form.getvalue('check_out')

cursor.execute("""
    INSERT INTO Bookings (room_id, guest_name, guest_phone, guest_email, check_in, check_out) VALUES (?, ?, ?, ?, ?, ?)
""", (room_id, guest_name, guest_phone, guest_email, check_in, check_out))
conn.commit()

print("Content-type: text/html\n")
print("<html><body>")
print("<h1>Бронирование добавлено</h1>")
print("<p><a href='../index.html'>Вернуться к списку бронирований</a></p>")
print("</body></html>")