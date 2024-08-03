#!/usr/bin/python3
"""This module defines a class User"""
from models.base_model import BaseModel, Base
from sqlalchemy.orm import relationship
from sqlalchemy import Column, String

class User(BaseModel, Base):
    """
    Represents a user in the HBNB project.
    
    Attributes:
        __tablename__ (str): The name of the MySQL table to store users.
        email (sqlalchemy.String): The user's email address.
        password (sqlalchemy.String): The user's password.
        first_name (sqlalchemy.String): The user's first name.
        last_name (sqlalchemy.String): The user's last name.
        places (sqlalchemy.orm.relationship): The relationship between User and Place.
        reviews (sqlalchemy.orm.relationship): The relationship between User and Review.
    """
    __tablename__ = 'users'
    email = Column(String(128), nullable=False)
    password = Column(String(128), nullable=False)
    first_name = Column(String(128), nullable=True)
    last_name = Column(String(128), nullable=True)
    
    # One-to-many relationship with Place
    places = relationship('Place', backref='user', cascade='all, delete-orphan')
    
    # One-to-many relationship with Review
    reviews = relationship('Review', backref='user', cascade='all, delete-orphan')
