#!/usr/bin/python3
"""
This module contains the class definition of a City
"""
from model_state import Base, State
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship


class City(Base):
    """This class defines the city table"""
    __tablename__ = 'cities'

    id = Column(Integer, autoincrement=True, unique=True,
                nullable=False, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)

    state = relationship('State', back_populates='cities')


State.cities = relationship('City', order_by=City.id,
                            back_populates='state')
