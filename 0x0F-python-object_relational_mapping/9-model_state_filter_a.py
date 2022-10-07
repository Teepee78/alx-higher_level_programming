#!/usr/bin/python3
"""
Lists all State objects that contain the letter a
from the database hbtn_0e_6_usa
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
    # create session
    Session = sessionmaker(bind=engine)
    session = Session()
    # Query database
    states = session.query(State).filter(State.name.like("%a%"))\
        .order_by(State.id.asc()).all()
    # Print result
    for state in states:
        print(f"{state.id}: {state.name}")
    session.close()
