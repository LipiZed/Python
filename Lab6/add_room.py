import cgi
import sqlite3

conn = sqlite3.connect('lab6.db')
cursor = conn.cursor()

form = cgi.FieldStorage()
hotel_id = form.getvalue('hotel_id')
room_number = form.getvalue('room_number')
room_type = form.getvalue('room_type')
price = form.getvalue('price')
capacity = form.getvalue('capacity')

cursor.execute("""
    INSERT INTO Rooms (hotel_id, room_number, type, price, capacity) VALUES (?, ?, ?, ?, ?)
""", (hotel_id, room_number, room_type, price, capacity))
conn.commit()

print("Content-type: text/html\n")
print("<html><body>")
print("<h1>Номер добавлен</h1>")
print("<p><a href='index.html'>Вернуться к списку номеров</a></p>")
print("</body></html>")