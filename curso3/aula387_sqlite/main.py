# pylint: disable=missing-module-docstring

import sqlite3
from pathlib import Path

ROOT_DIR = Path(__file__).parent
DB_NAME = 'db.sqlite3'
DB_FILE = ROOT_DIR / DB_NAME
TABLE_NAME = 'customers'

connection = sqlite3.connect(DB_FILE)
cursor = connection.cursor()

# Delete the table every time the code is updated
cursor.execute(f'DELETE FROM {TABLE_NAME}')
cursor.execute(f'DELETE FROM sqlite_sequence WHERE name="{TABLE_NAME}"')
connection.commit()


cursor.execute(
    f'CREATE TABLE IF NOT EXISTS {TABLE_NAME}'
    '('
    'id INTEGER PRIMARY KEY AUTOINCREMENT,'
    'name TEXT,'
    'weight REAL'
    ')'
)
connection.commit()

sql = (f'INSERT INTO {TABLE_NAME}'
       '(name, weight) VALUES'
       '(:nome, :peso)')  # (?, ?)

# cursor.execute(sql, ['Joana', 4])
# cursor.executemany(sql, (("Bruna", 92), ("Marcelo", 87), ("Joana", 76)))
# cursor.execute(sql, {"nome": "Bruna", "peso": 93})
cursor.executemany(sql, ({"nome": "Bruna", "peso": 93},
                         {"nome": "Marcelo", "peso": 90},
                         {"nome": "Joana", "peso": 86}))
connection.commit()

cursor.execute(f'DELETE FROM {TABLE_NAME} WHERE id = 3')
connection.commit()

cursor.execute(f'UPDATE {TABLE_NAME} SET weight = 60 WHERE id = 1')
connection.commit()

cursor.close()
connection.close()
