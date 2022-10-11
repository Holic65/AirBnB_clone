#!/usr/bin/python3
''' user class module defintion '''
from models.base_model import BaseModel


class User(BaseModel):
    '''user class created  that inherits from BaseModel'''

    email = ""
    password = ""
    first_name = ""
    last_name = ""
