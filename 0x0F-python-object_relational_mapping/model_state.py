#!/usr/bin/python3
"""
This module defines the State class
"""
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy import create_engine

Base = declarative_base()


class State(Base):
    """
    This class defines the states table and links to it
    """

    __tablename__ = 'states'

    id = Column(Integer, nullable=False, primary_key=True,
                autoincrement=True, unique=True)
    name = Column(String(128), nullable=False)
