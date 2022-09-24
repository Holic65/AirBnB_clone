#!/usr/bin/python3
""" This module contains BaseModel class"""
import uuid
from datetime import datetime
import models


class BaseModel:
    """ This is Base Class from which other subclasses
    will inherit"""
    def __init__(self, *args, **kwargs):
        """ Initializes the objects with the following
        attributes during creations
        and also using kwargs"""
        if kwargs:
            for key, value in kwargs.items():
                if key != "__class__":
                    setattr(self, key, value)
                if key == "created_at":
                    self.created_at = datetime.strptime(value,
                                                        "%Y-%m-%dT%H:%M:%S.%f")
                if key == "updated_at":
                    self.updated_at = datetime.strptime(value,
                                                        "%Y-%m-%dT%H:%M:%S.%f")
                if "id" not in kwargs:
                    self.id = str(uuid.uuid4())
                if "created_at" not in kwargs:
                    self.created_at = datetime.now()
                if "updated_at" not in kwargs:
                    self.created_at = datetime.now()

        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()

        models.storage.new(self)

    def __str__(self):
        """ return the string when object is printed"""
        return "[{}] ({}) {}"\
            .format(self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        """ updates the public instance attribute updated_at with the
        current datetime"""
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """returns a dictionary containing all keys/values of
        __dict__ of the instance"""
        my_dict = dict(self.__dict__)
        my_dict['__class__'] = self.__class__.__name__
        my_dict['created_at'] = self.created_at.isoformat()
        my_dict['updated_at'] = self.updated_at.isoformat()
        return my_dict
