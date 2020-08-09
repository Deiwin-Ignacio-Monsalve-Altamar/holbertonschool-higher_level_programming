#!/usr/bin/python3
"""Write a script that changes
"""
import sys
from model_state import Base, State
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker


def updateState():
    """the name of a State object from the database
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

    for state in session.query(State).filter(State.name.like('%a%')):
        session.delete(state)
    
    session.commit()
    session.close()


if __name__ == '__main__':
    updateState()
