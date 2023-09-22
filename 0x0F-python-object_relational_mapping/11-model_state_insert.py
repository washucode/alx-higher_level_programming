#!/usr/bin/python3
"""
Script that adds the State object “Louisiana” to the database hbtn_0e_6_usa
"""
from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__name__":

    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(argv[1], argv[2],
                                   argv[3]), pool_pre_ping=True)
    Session = sessionmaker()
    session = Session(bind=engine)

    Base.metadata.create_all(engine)
    new_state = State(name='Louisiana')
    session.add(new_state)
    session.commit()
    print("{}".format(new_state.id))

    session.close()
