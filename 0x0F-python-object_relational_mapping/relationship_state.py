#!/usr/bin/python3
"""
Contains the class definition of a State improved
"""
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

# Creating an instance of the declarative base.
Base = declarative_base()


class State(Base):
    """Class State that inherits from Base"""
    # Defining the name of the table.
    __tablename__ = 'states'
    # Defining the columns for the table.
    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name = Column(String(128), nullable=False)
    cities = relationship("City", backref="state")
