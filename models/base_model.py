#!/usr/bin/python3
"""This module defines a base class for all models in our hbnb clone"""
import uuid
from datetime import datetime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, DateTime, String

Base = declarative_base()

class BaseModel:
    """A base class for all hbnb models"""
    id = Column(String(60), primary_key=True, nullable=False)
    created_at = Column(DateTime, nullable=False, default=datetime.now)
    updated_at = Column(DateTime, nullable=False, default=datetime.now)

    def __init__(self, *args, **kwargs):
        """Instantiates a new model by managing kwargs"""
        from models import storage
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        if kwargs:
            for key, value in kwargs.items():
                if key in ["created_at", "updated_at"]:
                    value = datetime.strptime(value, '%Y-%m-%dT%H:%M:%S.%f')
                if key != '__class__' and hasattr(self.__class__, key):
                    setattr(self, key, value)

    def __str__(self):
        """Returns a string representation of the instance"""
        cls = (str(type(self)).split('.')[-1]).split('\'')[0]
        return f'[{cls}] ({self.id}) {self.__dict__}'

    def save(self):
        """Updates updated_at with current time when instance is changed"""
        from models import storage
        self.updated_at = datetime.now()
        storage.new(self)
        storage.save()

    def to_dict(self):
        """Convert instance into dict format, removing _sa_instance_state"""
        dictionary = self.__dict__.copy()
        dictionary.update({
            '__class__': (str(type(self)).split('.')[-1]).split('\'')[0]})
        dictionary['created_at'] =  self.created_at.isoformat()
        dictionary['updated_at'] = self.updated_at.isoformat()
        del dictionary['_sa_instance_state']
        return dictionary

    def delete(self):
        """Removes object from storage dictionary"""
        from models import storage
        storage.delete(self)
