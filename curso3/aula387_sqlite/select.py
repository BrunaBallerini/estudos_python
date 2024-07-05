# pylint: disable=missing-module-docstring

import sqlite3

from main import DB_FILE, TABLE_NAME

connection = sqlite3.connect(DB_FILE)
cursor = connection.cursor()

cursor.execute(f'SELECT * FROM {TABLE_NAME}')
for row in cursor.fetchall():  # fetchall returns all
    _id, name, weight = row
    print(_id, name, weight)

cursor.execute(f'SELECT * FROM {TABLE_NAME} WHERE id = 3')
row = cursor.fetchone()
_id, name, weight = row
print(_id, name, weight)
print(row)

cursor.close()
connection.close()
