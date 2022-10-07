#!/usr/bin/python3
"""
This module deletes all State objects with a name
containing the letter a from the database hbtn_0e_6_usa
"""
from sys import argv
from model_state import Base, State

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == '__main__':
    # credentials
    user = argv[1]
    passwd = argv[2]
    db = argv[3]
    url = f"mysql+mysqldb://{user}:{passwd}@localhost/{db}"

    # connect to database
    engine = create_engine(url, pool_pre_ping=True)
    # Create session
    Session = sessionmaker(bind=engine)
    session = Session()
    # Query objects
    states = session.query(State).filter(State.name.like("%a%"))
    for state in states:
        session.delete(state)
    session.commit()
    session.close()
