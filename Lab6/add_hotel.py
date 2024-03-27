import cgi
import sqlite3

conn = sqlite3.connect('lab6.db')
cursor = conn.cursor()

form = cgi.FieldStorage()
name = form.getvalue('name')
address = form.getvalue('address')
phone = form.getvalue('phone')
email = form.getvalue('email')

cursor.execute("""
    INSERT INTO Hotel (name, address, phone, email) VALUES (?, ?, ?, ?)
""", (name, address, phone, email))
conn.commit()

print("Content-type: text/html\n")
print("<html><body>")
print("<h1>Гостиница добавлена</h1>")
print("<p><a href='index.html'>Вернуться к списку гостиниц</a></p>")
print("</body></html>")