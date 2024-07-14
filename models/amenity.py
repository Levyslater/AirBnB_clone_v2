#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship

class Amenity(BaseModel, Base):
    """
    Represents an amenity in the HBNB project.
    
    Attributes:
        __tablename__ (str): The name of the MySQL table to store amenities.
        name (sqlalchemy.String): The name of the amenity.
        place_amenities (sqlalchemy.orm.relationship): The relationship between 
            Place and Amenity using the secondary association table.
    """
    __tablename__ = 'amenities'
    name = Column(String(128), nullable=False)
    
    # Relationship with Place through the association table
    place_amenities = relationship('Place', secondary='place_amenity', viewonly=True)
