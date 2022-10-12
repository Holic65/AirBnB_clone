#!/usr/bin/python3
'''console module definition'''
import cmd
import models
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review


class HBNBCommand(cmd.Cmd):
    '''command processor class definition'''

    prompt = '(hbnb)'
    MODELS = [BaseModel, User, Place, State, City, Amenity, Review]

    def do_create(self, line):
        '''creates a new instance of BaseModel saves it and prints the id'''

        if len(line) != 0:
            split_line = line.split()
            for model in self.MODELS:
                if split_line[0] == model.__name__:
                    new_model = model()
                    new_model.save()
                    print(new_model.id)
                    return
            print("** class doesn't exist **")
        else:
            print("** class name missing **")

    def do_show(self, line):
        '''
            Prints the string representation of an
            instance based on the class name and id
        '''

        if len(line) == 0:
            print('** class name missing **')
            return

        split_line = line.split()
        model_name = split_line[0]
        for model in self.MODELS:
            if split_line[0] == model.__name__:
                if len(split_line) > 1:

                    model_id = split_line[1]
                    models.storage.reload()
                    all_objs = models.storage.all()

                    obj_id_list = []
                    for obj_id in all_objs.keys():
                        obj_id_list.append(obj_id)

                    mod_id = model.__name__ + '.' + model_id
                    if mod_id in obj_id_list:
                        obj = all_objs[mod_id]
                        print(obj)
                        return
                    else:
                        print('** no instance found **')
                        return
                else:
                    print('** instance id missing **')
                    return
        print("** class doesn't exist **")
        return

    def do_destroy(self, line):
        '''Deletes an instance based on the class name and id'''
        if len(line) == 0:
            print('** class name missing **')
            return

        split_line = line.split()
        model_name = split_line[0]

        for model in self.MODELS:
            if split_line[0] == model.__name__:
                if len(split_line) > 1:
                    model_id = split_line[1]
                    models.storage.reload()
                    all_objs = models.storage.all()

                    model_id_list = []
                    for all_obj_id in all_objs.keys():
                        model_id_list.append(all_obj_id)

                    mod_id = model.__name__ + '.' + model_id
                    if mod_id in model_id_list:
                        del all_objs[mod_id]
                        models.storage.save()
                        return
                    else:
                        print('** no instance found **')
                        return
                else:
                    print('** instance id missing **')
                    return
        print("** class doesn't exist **")
        return

    def do_all(self, line):
        '''
            prints the class representation of all
            instances based or not on the class name
        '''
        models.storage.reload()
        all_objs = models.storage.all()
        obj_list = []

        if len(line) == 0:
            for obj in all_objs.values():
                obj_list.append(obj.__str__())
            print(obj_list)
            return

        elif len(line) > 0:
            split_line = line.split()
            for model in self.MODELS:
                if split_line[0] == model.__name__:
                    for mod in all_objs:
                        sub_mod = all_objs[mod].to_dict()
                        if sub_mod['__class__'] == split_line[0]:
                            instance = model(**sub_mod)
                            obj_list.append(str(instance))
                    print(obj_list)
                    return
            print("** class doesn't exist **")
            return

    def do_update(self, line):
        '''
            Updates an instance based on the class
            name and id by adding and updating attr
        '''
        if len(line) == 0:
            print("** class name missing **")
            return

        split_line = line.split()
        model_name = split_line[0]
        all_objs = models.storage.all()

        for model in self.MODELS:
            if model_name == model.__name__:
                if len(split_line) > 1:
                    model_id = split_line[1]
                else:
                    print("** instance id missing **")
                    return
                if len(split_line) > 2:
                    attr_name = split_line[2]
                else:
                    print("** attribute name missing **")
                    return
                if len(split_line) > 3:
                    attr_value = split_line[3]
                else:
                    print("** value missing **")
                    return
                obj = model_name + '.' + model_id
                if obj in models.storage.all():
                    objx = models.storage.all()[obj]
                    if attr_name in type(objx).__dict__:
                        v_type = type(objx.__class__.__dict__[attr_name])
                        setattr(objx, attr_name, v_type(attr_value))
                    else:
                        setattr(objx, split_line[2], split_line[3])

                else:
                    print("** no instance found **")
                    return

                models.storage.save()
                return
        print("** class doesn't exist **")

    def emptyline(self):
        return

    def do_quit(self, line):
        '''Quit command to exit the program'''
        return True

    def do_EOF(self, line):
        '''exit the console'''
        return True


if __name__ == '__main__':
    HBNBCommand().cmdloop()
