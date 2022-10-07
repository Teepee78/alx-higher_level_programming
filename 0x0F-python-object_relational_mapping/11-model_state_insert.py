#!/usr/bin/python3
"""
This module adds the State object “Louisiana”
to the database hbtn_0e_6_usa
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
    # create Object
    state = State(name='Louisiana')
    # Add object
    session.add(state)
    session.commit()
    print(state.id)
    session.close()
