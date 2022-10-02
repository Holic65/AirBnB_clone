#!/usr/bin/python3
''' a file containing a class user'''
from models.base_model import BaseModel


class User(BaseModel):
    ''' a base model user class definition'''

    def __init__(self, *args, **kwargs):
        '''init method for the user class'''
        super().__init__(*args, **kwargs)
