#!/usr/bin/python3
"""script that adds the State
"""
import sys
from model_state import Base, State
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker


def getState():
    """object Louisiana to the database
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

    new_states = State(name='Louisiana')
    session.add(new_states)

    for state in session.query(State).order_by(State.id).all():
        if state.name == "Louisiana":
            print("{}".format(state.id))

    session.commit()
    session.close()


if __name__ == '__main__':
    getState()
