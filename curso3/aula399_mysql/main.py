# pylint: disable=missing-module-docstring

import os

import dotenv
import pymysql
import pymysql.cursors

dotenv.load_dotenv()
TABLE_NAME = 'customers'

connection = pymysql.connect(
    host=os.environ['MYSQL_HOST'],
    user=os.environ['MYSQL_USER'],
    password=os.environ['MYSQL_PASSWORD'],
    database=os.environ['MYSQL_DATABASE'],
    cursorclass=pymysql.cursors.DictCursor,
)
# cursor = connection.cursor()
# cursor.close()
# connection.close()
with connection:
    with connection.cursor() as cursor:
        cursor.execute(
            f'CREATE TABLE IF NOT EXISTS {TABLE_NAME} ('
            'id INT NOT NULL AUTO_INCREMENT, '
            'name VARCHAR(50) NOT NULL, '
            'age INT NOT NULL, '
            'PRIMARY KEY (id)'
            ')'
        )
        # CAREFUL: Truncate delete all data
        cursor.execute(f'TRUNCATE TABLE {TABLE_NAME}')
    connection.commit()

    with connection.cursor() as cursor:
        sql = (
            f'INSERT INTO {TABLE_NAME} '
            '(name, age) VALUES '
            '(%s, %s)'
        )
        data = ("Marcelo", 34)
        result = cursor.execute(sql, data)
        # print(result)  # Number of rows affected
    connection.commit()

    with connection.cursor() as cursor:
        sql = (
            f'INSERT INTO {TABLE_NAME} '
            '(name, age) VALUES '
            '(%(nome)s, %(idade)s)'
        )
        data2 = {"nome": "Bruna", "idade": 34}
        result2 = cursor.execute(sql, data2)
        # print(result2)  # Number of rows affected
    connection.commit()

    with connection.cursor() as cursor:
        sql = (
            f'INSERT INTO {TABLE_NAME} '
            '(name, age) '
            'VALUES '
            '(%(name)s, %(age)s)'
        )
        data3 = (
            {"name": "Adriana", "age": 25, },
            {"name": "Joseph", "age": 36, },
            {"name": "Patricia", "age": 42, },
            {"name": "Kevin", "age": 29, },
        )
        result3 = cursor.executemany(sql, data3)
        # print(result3)  # Number of rows affected
    connection.commit()

    with connection.cursor() as cursor:
        sql = (
            f'INSERT INTO {TABLE_NAME} '
            '(name, age) '
            'VALUES '
            '(%s, %s)'
        )
        data4 = (
            ("Anthony", 65, ),
            ("Helena", 8, ),
        )
        result4 = cursor.executemany(sql, data4)
        # print(result4)  # Number of rows affected
    connection.commit()

    with connection.cursor() as cursor:
        sql = f'SELECT id, name, age FROM {TABLE_NAME} '
        cursor.execute(sql)
        data5 = cursor.fetchone()
        print(data5)
        # cursor.scroll(0, 'absolute')
        # There is no need to save the database on a memory,
        # just change the cursor position with scroll
        # (relative) or (index, "absolute")

        # data6 = cursor.fetchall()  # Possible for use more times (after for)
        # for row in data6:  # fetchall returns all
        # _id, name, weight = row
        # print(_id, name, weight)

        for row in cursor.fetchall():  # new cursor: DictCursor
            print(row)
        print()

    with connection.cursor() as cursor:
        sql = f'SELECT id, name, age FROM {TABLE_NAME} WHERE id = 2'
        cursor.execute(sql)
        data7 = cursor.fetchall()
        print(data7)

    with connection.cursor() as cursor:
        sql = (
            f'SELECT id, name, age FROM {TABLE_NAME} WHERE id BETWEEN 3 AND 8'
        )
        cursor.execute(sql)
        data8 = cursor.fetchall()
        print(data8)
        print()

    with connection.cursor() as cursor:
        sql = (
            f'DELETE FROM {TABLE_NAME} WHERE id = 7'
        )
        cursor.execute(sql)
        connection.commit()

        cursor.execute(f'SELECT * FROM {TABLE_NAME} ')
        data9 = cursor.fetchall()
        for row in data9:
            print(row)
        print()

    with connection.cursor() as cursor:
        sql = (
            f'UPDATE {TABLE_NAME} SET name = %s, age = %s WHERE id = %s'
        )
        cursor.execute(sql, ("Adrian", 46, 3,))
        connection.commit()

        cursor.execute(
            f'SELECT id from {TABLE_NAME} ORDER BY id DESC LIMIT 1'
        )
        lastIdFromSelect = cursor.fetchone()

        result_from_select = cursor.execute(f'SELECT * FROM {TABLE_NAME} ')
        data10 = cursor.fetchall()
        for row in data10:
            print(row)
        print("result_from_select", result_from_select)
        print("len(data10)", len(data10))
        print("rowcount", cursor.rowcount)
        print("lastrowid", cursor.lastrowid)  # last row inserted br cursor
        print('lastrowid from select', lastIdFromSelect)

        cursor.scroll(0, 'absolute')
        print('rownumber', cursor.rownumber)
