#!/usr/bin/python3
""" Review module for the HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey

class Review(BaseModel, Base):
    """
    Represents a review in the HBNB project.
    
    Attributes:
        __tablename__ (str): The name of the MySQL table to store reviews.
        place_id (sqlalchemy.String): The ID of the place being reviewed.
        user_id (sqlalchemy.String): The ID of the user who wrote the review.
        text (sqlalchemy.String): The text content of the review.
    """
    __tablename__ = 'reviews'
    
    place_id = Column(String(60), ForeignKey('places.id'), nullable=False)
    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
    text = Column(String(1024), nullable=False)
