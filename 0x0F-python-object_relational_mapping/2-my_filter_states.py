#!/usr/bin/python3
"""
This module takes in an argument
and displays all values in the states table of hbtn_0e_0_usa
where name matches the argument.
"""
import MySQLdb
from sys import argv

if __name__ == '__main__':

    # credentials
    username = argv[1]
    password = argv[2]
    database = argv[3]
    name = argv[4]

    db = MySQLdb.connect(
        user=username,
        passwd=password,
        host='localhost',
        db=database
    )
    cursor = db.cursor()
    cursor.execute("SELECT * FROM states WHERE name = '{}'".format(name))
    rows = cursor.fetchall()

    for row in rows:
        if row[1] == name:
            print(row)

    cursor.close()
    db.close()
