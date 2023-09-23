#!/usr/bin/python3

"""
Contains the class definition of a City.
"""

from sqlalchemy import Column, Integer, String, ForeignKey
from model_state import Base, State


class City(Base):
    """Class City that inherits from Base"""
    # Defining the name of the table.
    __tablename__ = 'cities'
    # Defining the columns for the table.
    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey(State.id), nullable=False)
