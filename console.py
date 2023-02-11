#!/usr/bin/python3
"""Defines the HBnB console"""
import cmd

class HBNBCommand(cmd.Cmd):
    """
    HBNBCommand class extends the cmd.Cmd class to implement a custom command line interface for the HBNB project.
    """

    prompt = '(hbnb) '
    """
    The prompt to be displayed in the command line interface.
    """

    def do_quit(self, args):
        """
        Quit command to exit the program.

        Args:
            args: Arguments passed to the quit command (not used in this implementation).

        Returns:
            True: To signal the end of the command line interface.
        """
        return True

    def do_EOF(self, args):
        """
        EOF (end-of-file) command to exit the program.

        Args:
            args: Arguments passed to the EOF command (not used in this implementation).

        Returns:
            True: To signal the end of the command line interface.
        """
        return True

    def emptyline(self):
        """
        Do not execute anything when an empty line is entered.
        """
        pass

if __name__ == '__main__':
    """
    Code to be executed only when the module is run as a standalone program and not when it is imported as a module.
    """
    HBNBCommand().cmdloop()
