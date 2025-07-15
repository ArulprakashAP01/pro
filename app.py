import sqlite3

user_input = "' OR 1=1 --"
conn = sqlite3.connect('users.db')
cursor = conn.cursor()

query = "SELECT * FROM users WHERE username = '" + user_input + "'"
cursor.execute(query)
