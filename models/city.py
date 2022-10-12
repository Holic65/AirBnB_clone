#!/usr/bin/python3
''' city class module that inherits from BaseMOdel'''
from models.base_model import BaseModel


class City(BaseModel):
    '''class city defined'''
    state_id = ""
    name = ""
