#!/usr/bin/python3
"""script that lists all State objects
"""
import sys
from model_state import Base, State
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker


def firstState():
    """prints the first State object
    """
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
            sys.argv[1],
            sys.argv[2],
            sys.argv[3]),
        pool_pre_ping=True)
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    states = session.query(State).filter(State.name.contains("a"))
    for state in states:
        print("{}: {}".format(state.id, state.name))
    session.close()


if __name__ == '__main__':
    firstState()
