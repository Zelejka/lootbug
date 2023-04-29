import sqlite3

connection = sqlite3.connect('cgi-bin/data1.db')
cursor = connection.cursor()
cursor.execute('select * from goods;')
x = cursor.fetchall()
connection.close()
print(x)