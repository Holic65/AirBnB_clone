#!/usr/bin/python3
''' review class module definition'''
from models.base_model import BaseModel


class Review(BaseModel):
    '''review class definition'''
    place_id = ""
    user_id = ""
    text = ""
