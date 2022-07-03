import sqlite3

db = sqlite3.Connection("data.db")

cursor = db.cursor()

sql_command = "CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY ,username text ,password text)"

cursor.execute(sql_command)

db.commit()
db.close()