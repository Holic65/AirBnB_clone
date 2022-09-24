#!/usr/bin/python3
'''
    Class BaseModel that defines all the common attributes
    and method for other classes
'''
import uuid
from datetime import datetime


class BaseModel:
    '''class initialization of Basemodel'''

    def __init__(self):
        '''this is the init method'''
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        '''A method that describe class'''
        return "[{}] ({}) {}".format(
                self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        ''' updates public instance attribute updated_at'''
        self.updated_at = datetime.now()

    def to_dict(self):
        my_dict = self.__dict__.copy()
        my_dict["__class__"] = type((self).__name__)
        my_dict["created_at"] = self.created_at.isoformat()
        my_dict["updated_at"] = self.updated_at.isoformat()
        return my_dict
