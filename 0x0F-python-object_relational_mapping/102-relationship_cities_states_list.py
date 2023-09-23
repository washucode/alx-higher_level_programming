#!/usr/bin/python3
"""
Script that lists all City objects from the database hbtn_0e_101_usa
"""

from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_state import Base, State
from relationship_city import City

if __name__ == "__main__":

    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(argv[1], argv[2],
                                   argv[3]), pool_pre_ping=True)
    Session = sessionmaker()
    session = Session(bind=engine)

    Base.metadata.create_all(engine)
    city_q = session.query(City).order_by(City.id).all()
    for city in city_q:
        print("{}: {} -> {}".format(city.id, city.name, city.state.name))

    session.close()
