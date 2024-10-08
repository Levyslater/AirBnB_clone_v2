#!/usr/bin/python3
"""State Module for HBNB project"""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from os import getenv
import models
from models.city import City


class State(BaseModel, Base):
    """
    Represents a state in the HBNB project.

    Attributes:
        __tablename__ (str): The name of the MySQL table to store states.
        name (sqlalchemy.String): The name of the state.
        cities (sqlalchemy.orm.relationship or property):
        The relationship between State and City if using db storage,
        or a property to get cities if using file storage.
    """
    __tablename__ = 'states'
    name = Column(String(128), nullable=False)
    cities = relationship('City', backref='state',
                           cascade='all, delete-orphan')

    if getenv('HBNB_TYPE_STORAGE') != 'db':
        name = ''
        cities = []

        @property
        def cities(self):
            """
            Gets the list of City objects linked to this
            State when using file storage.

            Returns:
                list: List of City objects with
                state_id matching this State's id.
            """
            city_list = []
            for city in models.storage.all(City).values():
                if city.state_id == self.id:
                    city_list.append(city)
            return city_list
