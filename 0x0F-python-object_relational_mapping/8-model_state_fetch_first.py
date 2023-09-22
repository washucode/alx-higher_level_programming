#!/usr/bin/python3

"""
Script that prints the first State object from the database hbtn_0e_6_usa
"""

from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":

    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(argv[1], argv[2],
                                   argv[3]), pool_pre_ping=True)
    Session = sessionmaker()
    session = Session(bind=engine)

    Base.metadata.create_all(engine)
    state_q = session.query(State).order_by(State.id).first()
    if state_q is not None:
        print("{}: {}".format(state_q.id, state_q.name))
    else:
        print("Nothing")

    session.close()
