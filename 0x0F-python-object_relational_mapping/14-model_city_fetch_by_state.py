#!/usr/bin/python3
"""
Script that lists all State objects from the database hbtn_0e_6_usa
"""
from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from model_city import City


if __name__ == "__main__":

    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(argv[1], argv[2],
                                   argv[3]), pool_pre_ping=True)
    Session = sessionmaker()
    session = Session(bind=engine)

    Base.metadata.create_all(engine)
    state_q = session.query(State, City).join(City).order_by(City.id).all()
    for state, city in state_q:
        print("{}: ({}) {}".format(state.name, city.id, city.name))

    session.close()
