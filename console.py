#!/usr/bin/python3
'''console module definition'''
import cmd


class HBNBCommand(cmd.Cmd):
    '''command processor class definition'''
    
    prompt = '(hbnb)'

    def do_quit(self, line):
        '''Quit command to exit the program'''
        return True

    def do_EOF(self, line):
        '''exit the console'''
        return True

if __name__ == '__main__':
    HBNBCommand().cmdloop()
