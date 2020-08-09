#!/usr/bin/python3
"""that prints the State object with the name
"""
import sys
from model_state import Base, State
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker


def getState():
    """tate object with the name passed as argument
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

    states = session.query(State).filter(
        State.name == sys.argv[4]).order_by(State.id).first()

    if states:
        print("{}".format(states.id))
    else:
        print("Not found")
    session.close()


if __name__ == '__main__':
    getState()
