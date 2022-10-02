#!/usr/bin/python3
'''
    Class BaseModel that defines all the common attributes
    and method for other classes
'''
import uuid
from datetime import datetime
import models


class BaseModel:
    '''class initialization of Basemodel'''

    def __init__(self, *args, **kwargs):
        '''this is the init method'''
        if kwargs:
            for key, value in kwargs.items():
                if key == '__class__':
                    continue
                elif key == 'created_at':
                    value = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                elif key == 'updated_at':
                    value = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")

                if 'id' not in kwargs.keys():
                    self.id = str(uuid.uuid4())
                if 'created_at' not in kwargs.keys():
                    self.created_at = datetime.now()
                if 'updated_at' not in kwargs.keys():
                    self.updated_at = datetime.now()
                setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

    def __str__(self):
        '''A method that describe class'''
        return "[{}] ({}) {}".format(
                self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        ''' updates public instance attribute updated_at'''
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        ''' a method that returns a dic containg k/v pairs'''
        r = self.__dict__.copy()
        r['__class__'] = self.__class__.__name__
        r['created_at'] = datetime.isoformat(self.created_at)
        r['updated_at'] = datetime.isoformat(self.updated_at)
        return r
