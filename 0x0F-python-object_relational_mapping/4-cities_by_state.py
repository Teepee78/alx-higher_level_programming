#!/usr/bin/python3
"""
Lists all cities from the database hbtn_0e_4_usa
"""
import MySQLdb
from sys import argv

if __name__ == '__main__':

    # credentials
    username = argv[1]
    password = argv[2]
    database = argv[3]

    db = MySQLdb.connect(
        host='localhost',
        user=username,
        passwd=password,
        db=database
    )
    cursor = db.cursor()
    cursor.execute("""
                   SELECT cities.id, cities.name, states.name
                   FROM cities INNER JOIN states
                   ON cities.state_id=states.id"""
                   )
    rows = cursor.fetchall()

    for row in rows:
        print(row)

    cursor.close()
    db.close()
