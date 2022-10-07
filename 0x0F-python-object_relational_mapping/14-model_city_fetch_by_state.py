#!/usr/bin/python3
"""
This module prints all City objects from the
database hbtn_0e_14_usa
"""
from sys import argv
from model_city import City
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
    # Query database
    cities = session.query(State.name, City.id, City.name).filter(
        City.state_id == State.id).order_by(City.id.asc()).all()
    # Print result
    for city in cities:
        print(f"{city[0]}: ({city[1]}) {city[2]}")
    session.close()
