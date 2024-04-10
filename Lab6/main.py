import sqlite3
import xml.dom.minidom as minidom

conn = sqlite3.connect('lab6.db')

cursor = conn.cursor()

cursor.execute('SELECT * FROM Hotel')
doc = minidom.Document()

root = doc.createElement('root')
doc.appendChild(root)

for row in cursor.fetchall():

    row_elem = doc.createElement('row')
    root.appendChild(row_elem)

    for col_index, col_value in enumerate(row):
        col_elem = doc.createElement('col{}'.format(col_index))
        row_elem.appendChild(col_elem)
        text = doc.createTextNode(str(col_value))
        col_elem.appendChild(text)

with open('mytable.xml', 'w') as f:
    f.write(doc.toprettyxml(indent='  '))

cursor.execute('SELECT * FROM Hotel')
result = cursor.fetchall()
print(result)
conn.close()
