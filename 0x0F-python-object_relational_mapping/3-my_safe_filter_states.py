#!/usr/bin/python3
"""
This module takes in an argument
and displays all values in the states table of hbtn_0e_0_usa
where name matches the argument.
Safe from injection
"""
import MySQLdb
from sys import argv


def authenthicate(string):
    """Prevents SQL Injection"""

    new_string = ""
    if string[0] != "'" or string[0] != '"':
        i = 0
        while i < len(string):
            if string[i] == '"' or string[i] == "'":
                break
            new_string += string[i]
            i += 1
        return new_string


if __name__ == '__main__':

    # credentials
    username = argv[1]
    password = argv[2]
    database = argv[3]
    name = authenthicate(argv[4])

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
        print(row)

    cursor.close()
    db.close()
