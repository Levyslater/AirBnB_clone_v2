#!/usr/bin/python3
"""Database storage engine for the HBNB project"""
from os import getenv
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from models.base_model import BaseModel, Base
from models.state import State
from models.city import City
from models.place import Place
from models.user import User
from models.amenity import Amenity
from models.review import Review  # Ensure all models are imported


class DBStorage:
    """
    Database storage engine for MySQL storage in the HBNB project.

    Attributes:
        __engine: SQLAlchemy engine.
        __session: SQLAlchemy scoped session.
    """
    __engine = None
    __session = None

    def __init__(self):
        """
        Initializes the DBStorage instance.
        Creates the engine and drops all tables if the environment is test.
        """
        username = getenv('HBNB_MYSQL_USER')
        password = getenv('HBNB_MYSQL_PWD')
        host = getenv('HBNB_MYSQL_HOST')
        db_name = getenv('HBNB_MYSQL_DB')
        db_url = f"mysql+mysqldb://{username}:{password}@{host}/{db_name}"

        self.__engine = create_engine(db_url, pool_pre_ping=True)

        if getenv('HBNB_ENV') == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """
        Queries all objects of a given class or all classes if cls is None.
        Args:
            cls (class or str): The class to query objects from,
            or None to query all classes.
        Returns:
            dict: A dictionary of queried objects,
            with keys in the format <class name>.<object id>.
        """
        obj_lst = []
        if cls:
            if isinstance(cls, str):
                try:
                    cls = globals()[cls]
                except KeyError:
                    return {}
            if issubclass(cls, Base):
                obj_lst = self.__session.query(cls).all()
        else:
            for subclass in Base.__subclasses__():
                obj_lst.extend(self.__session.query(subclass).all())

        obj_dct = {"{}.{}".format(obj.__class__.__name__,
                                  obj.id): obj for obj in obj_lst}
        return obj_dct

    def new(self, obj):
        """
        Adds a new object to the current database session.
        Args:
            obj: The object to add.
        """
        self.__session.add(obj)

    def save(self):
        """
        Commits all changes to the current database session.
        """
        self.__session.commit()

    def delete(self, obj=None):
        """
        Deletes an object from the current database session.
        Args:
            obj: The object to delete, or None to do nothing.
        """
        if obj:
            self.__session.delete(obj)

    def reload(self):
        """
        Creates all tables in the database and initializes the
        session.
        """
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(bind=self.__engine,
                                       expire_on_commit=False)
        Session = scoped_session(session_factory)
        self.__session = Session()

    def close(self):
        """
        Closes the database session.
        """
        self.__session.close()
