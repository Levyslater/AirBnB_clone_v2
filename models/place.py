#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import (Column, String, Table,
                        ForeignKey, Float, Integer)
from sqlalchemy.orm import relationship
from os import getenv
from models.review import Review
from models.amenity import Amenity
import models

# Association table for many-to-many relationship between Place and Amenity
association_table = Table('place_amenity', Base.metadata,
                          Column('place_id', String(60), ForeignKey('places.id'),
                                 primary_key=True, nullable=False),
                          Column('amenity_id', String(60), ForeignKey('amenities.id'),
                                 primary_key=True, nullable=False))

class Place(BaseModel, Base):
    """ A place to stay """
    __tablename__ = 'places'
    city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024))
    number_rooms = Column(Integer, default=0)
    number_bathrooms = Column(Integer, default=0)
    max_guest = Column(Integer, default=0)
    price_by_night = Column(Integer, default=0)
    latitude = Column(Float)
    longitude = Column(Float)
    amenity_ids = []
    
    # One-to-many relationship with Review
    reviews = relationship('Review', backref='place', cascade='all, delete-orphan')
    
    # Many-to-many relationship with Amenity
    amenities = relationship('Amenity', secondary='place_amenity', viewonly=False)

    if getenv('HBNB_TYPE_STORAGE') != 'db':
        @property
        def reviews(self):
            """Getter for reviews when using file storage."""
            all_reviews = list(models.storage.all(Review).values())
            review_list = [r for r in all_reviews if r.place_id == self.id]
            return review_list
        
        @property
        def amenities(self):
            """Getter for amenities when using file storage."""
            all_amenities = list(models.storage.all(Amenity).values())
            amenity_list = [a for a in all_amenities if a.id in self.amenity_ids]
            return amenity_list
        
        @amenities.setter
        def amenities(self, value):
            """Setter for amenities when using file storage."""
            if not isinstance(value, list):
                raise TypeError("amenities must be a list")
            for amenity in value:
                if not isinstance(amenity, Amenity):
                    raise TypeError("all items in amenities list must be of Amenity class")
                if amenity.id not in self.amenity_ids:
                    self.amenity_ids.append(amenity.id)
            models.storage.save()  # Save changes to storage
