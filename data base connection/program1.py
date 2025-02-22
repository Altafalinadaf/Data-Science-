import sqlite3  # Use sqlite3 instead of _sqlite3

# Connect to the SQLite database (or create it if it doesn't exist)
conn = sqlite3.connect('example.db')

# Create a cursor object
cursor = conn.cursor()

# Create table if it doesn't exist
cursor.execute('''
    CREATE TABLE IF NOT EXISTS employees(
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        salary REAL
    )
''')

# Insert data into the table
cursor.execute("INSERT INTO employees(name, salary) VALUES (?, ?)", ('John Doe', 75000))

cursor.execute("select * from employees")


# Commit the changes and close the connection
conn.commit()
conn.close()
