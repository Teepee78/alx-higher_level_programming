#!/usr/bin/python3
"""
This module lists all City objects from the database hbtn_0e_101_usa
"""
from sys import argv
from relationship_state import Base, State
from relationship_city import City

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
    # Query database
    states = session.query(State, City).filter(
        City.state_id == State.id).order_by(City.id).all()
    # Print result
    for state, city in states:
        print(f"{city.id:d}: {city.name} -> {state.name}")
    session.close()
