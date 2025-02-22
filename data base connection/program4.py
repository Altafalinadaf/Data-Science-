import sqlite3  # Use sqlite3 instead of _sqlite3

# Connect to the SQLite database (or create it if it doesn't exist)
conn = sqlite3.connect('example.db')

# Create a cursor object
cursor = conn.cursor()
cursor.execute("select * from employees")

rows= cursor.fetchmany(2) #fetch the first 2 rows

for row in rows:
    print(row)

cursor.close()