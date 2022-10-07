#!/usr/bin/python3
"""
This module prints the State object with the name passed
as argument from the database hbtn_0e_6_usa
"""
from sys import argv
from model_state import Base, State

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


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
    user = argv[1]
    passwd = argv[2]
    db = argv[3]
    url = f"mysql+mysqldb://{user}:{passwd}@localhost/{db}"
    state_name = authenthicate(argv[4])

    # connect to database
    engine = create_engine(url, pool_pre_ping=True)
    # Create session
    Session = sessionmaker(bind=engine)
    session = Session()
    # Query database
    state = session.query(State).filter(State.name == state_name).all()
    # Print result
    if state:
        for x in state:
            if x.name == state_name:
                print(f"{x.id}")
    else:
        print("Not found")
    session.close()
