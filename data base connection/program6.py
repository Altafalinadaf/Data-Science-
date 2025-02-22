import sqlite3


conn= sqlite3.connect('example.db')

cursor = conn.cursor()

n = int(input("enter the how many data you want to add in your database : "))

for i in range(n):
    name1 = input("enter the name : ")
    salary1 = float(input("enter the salary : "))
    cursor.execute("INSERT INTO employees(name, salary) VALUES (?, ?)", (name1, salary1))
    conn.commit()


cursor.execute('select * from employees ')
rows=cursor.fetchall()

for row in rows : 
    print(row)



conn.close()


