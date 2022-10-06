#!/usr/bin/python3
"""
This module takes in the name of a state as an argument and
lists all cities of that state, using the database hbtn_0e_4_usa
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
    state = authenthicate(argv[4])

    db = MySQLdb.connect(
        host='localhost',
        user=username,
        passwd=password,
        db=database
    )
    cursor = db.cursor()
    cursor.execute("""
        SELECT name FROM cities
        WHERE state_id = (
            SELECT id FROM states
            WHERE name = '{}'
        )
    """.format(state))
    states = cursor.fetchall()
    print(", ".join([x for i in states for x in i]))

    cursor.close()
    db.close()
