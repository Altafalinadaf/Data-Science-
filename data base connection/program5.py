import sqlite3

conn =sqlite3.connect("example.db")

cursor =conn.cursor()

cursor.execute('delete from employees where id in(2,3,4,5)')

conn.commit()
cursor.close()