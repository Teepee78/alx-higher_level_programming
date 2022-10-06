#!/usr/bin/python3
"""This module lists all states from hbtn_0e_0_usa"""
import MySQLdb
from sys import argv

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

rows = cursor.execute("SELECT * FROM states")

print(rows)