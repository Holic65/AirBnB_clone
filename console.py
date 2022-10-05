#!/usr/bin/python3
'''console module definition'''
import cmd


class HBNBCommand(cmd.Cmd):
    '''command processor class definition'''

    def do_quit(self):
        '''Quit command to exit the program'''
        exit()

    def do_EOF(self, line):
        return True

if __name__ == '__main__':
    HBNBCommand().cmdloop()
