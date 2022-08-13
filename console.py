#!/usr/bin/python3
"""script for the console user interface"""
import cmd


class HBNBCommand(cmd.Cmd):
    """class definition"""
    prompt = '(hbnb) '

    def do_EOF(self, line):
        """
            end of line implementation
        """
        return True

    def do_quit(self, line):
        """
            Quit comand to exit program
        """
        return True

    def emptyline(self):
        """
            empty line implementation
        """
        pass

    def help_EOF(self):
        """
            documentation for EOF
        """
        print('press ctrl + d to close console')

    def help_quit(self):
        """
            documentation for quit
        """
        print('Quit command to exit the program')


if __name__ == '__main__':
    HBNBCommand().cmdloop()
