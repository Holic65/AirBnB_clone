#!/usr/bin/python3
'''
    file storage class file
    Containing file storage class
'''
import json
import models
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review
from os import path


class FileStorage:
    '''file storage class definition'''
    __file_path = "file.json"
    __objects = dict()
    MODELS = [User, BaseModel, Place, State, City, Amenity, Review]

    def new(self, obj):
        ''' a method that sets object with object keys'''
        FileStorage.__objects[obj.__class__.__name__ + '.' + obj.id] = obj

    def all(self):
        ''' a method that returns object stored in obj dict'''
        return FileStorage.__objects

    def save(self):
        ''' a method that serializies object to the json file'''
        dicts = dict()
        for key, obj in FileStorage.__objects.items():
            dicts[key] = obj.to_dict()

        with open(FileStorage.__file_path, 'w', encoding='utf-8') as f:
            json.dump(dicts, f)

    def reload(self):
        ''' a method that deserializies the json file'''

        if path.exists(FileStorage.__file_path) is True:
            with open(FileStorage.__file_path, 'r', encoding='utf-8') as f:
                dicts = json.load(f)

            for key in dicts.keys():
                for model in FileStorage.MODELS:
                    if model.__name__ == dicts[key]["__class__"]:
                        FileStorage.__objects[key] = model(**dicts[key])

        else:
            with open(FileStorage.__file_path, "w", encoding='utf-8') as pathx:
                json.dump({}, pathx)
            self.reload()
