#!/usr/bin/python3
"""
This module lists all states with a name starting with N
from hbtn_0e_0_usa
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
    cursor.execute(
        "SELECT * FROM states WHERE name LIKE 'N%' ORDER BY states.id")
    rows = cursor.fetchall()

    for row in rows:
        if row[1][0] == 'N':
            print(row)

    cursor.close()
    db.close()
