#!/usr/bin/python3
"""
This module creates the State “California”
with the City “San Francisco” from the database hbtn_0e_100_usa
"""
from relationship_state import Base, State
from relationship_city import City
from sys import argv

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
    # Create tables
    Base.metadata.create_all(engine)
    # Create session
    Session = sessionmaker(bind=engine)
    session = Session()
    # Create new objects
    new_city = City(name='San Francisco')
    new_state = State(name='California')
    # Add city to new state
    new_state.cities.append(new_city)
    # Save new objects to database
    session.add_all([new_state, new_city])
    session.commit()
    session.close()
