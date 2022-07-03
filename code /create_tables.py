import sqlite3

db = sqlite3.Connection("data.db")

cursor = db.cursor()

sql_users = "CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY ,username text ,password text)"
sql_items = "CREATE TABLE IF NOT EXISTS items (id INTEGER PRIMARY KEY ,name text ,price real)"

cursor.execute(sql_items)
cursor.execute(sql_users)

db.commit()
db.close()