#!/usr/bin/python3
from model_state import Base, State
from sys import argv

from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

# credentials
user = argv[1]
passwd = argv[2]
db = argv[3]
url = f"mysql+mysqldb://{user}:{passwd}@localhost/{db}"

if __name__ == '__main__':
    # connect to database
    engine = create_engine(url, pool_pre_ping=True)
    # create session
    Session = sessionmaker(bind=engine)
    session = Session()
    # Query database
    state = session.query(State).order_by(State.id.asc()).first()
    # print state
    if (state):
        print(f"{state.id}: {state.name}")
    else:
        print("Nothing")
    session.close()
