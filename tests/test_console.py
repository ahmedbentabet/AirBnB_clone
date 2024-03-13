#!/usr/bin/python3
"""
Describes PromptTestHBNBCommand classes
"""

import os
import unittest
import sys
from models.engine.file_storage import FileStorage
from console import HBNBCommand
from io import StringIO
from unittest.mock import patch
from models import storage


class PromptTestHBNBCommand(unittest.TestCase):
    """Class for verify prompt functionality
    of the HBNB command interpreter."""

    def test__HBNB_command__prompt(self):
        """Verify that the prompt attribute of
        the HBNB command interpreter is correct."""
        self.assertEqual("(hbnb) ", HBNBCommand.prompt)

    def test__do_quit__method(self):
        """Verify that the quit method of the HBNB command interpreter."""
        cmd__inst = HBNBCommand()
        self.assertTrue(cmd__inst.do_quit(None))

    def test__EOF_command__exits(self):
        """Verify that the 'EOF' command exits
        of the HBNB command interpreter."""
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertTrue(HBNBCommand().onecmd("EOF"))

    def test__not_a_valid_create__syntax(self):
        """Verify the handling of not valid syntax for creat command."""
        expected_output = "*** Unknown syntax: MyModel.create()"
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("MyModel.create()"))
            self.assertEqual(expected_output, output.getvalue().strip())
        expected_output = "*** Unknown syntax: BaseModel.create()"
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("BaseModel.create()"))
            self.assertEqual(expected_output, output.getvalue().strip())

    def test__count_command__State(self):
        """Verify the count command for the State class."""
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create State"))
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("State.count()"))

    def test__Show_command__exits(self):
        """Verify that 'show' command exits with correct error
        message when class name is missing."""
        expected_output = "** class name missing **"
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("show"))
            self.assertEqual(expected_output, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd(".show()"))
            self.assertEqual(expected_output, output.getvalue().strip())

    def test__destroy_command__exits(self):
        """Verify that 'destory' command exits with
        correct error message when class name is missing."""
        expected_output = "** class name missing **"
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("destroy"))
            self.assertEqual(expected_output, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd(".destroy()"))
            self.assertEqual(expected_output, output.getvalue().strip())

    def test__all_command__output(self):
        """Verify the output of the 'all' command."""
        expected_output = "["
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("all"))
            self.assertTrue(expected_output in output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd(".all()"))
            self.assertEqual(expected_output, output.getvalue().strip())

    def test__update_command_missing__class(self):
        """Verify the behaivor of the 'update'
        command when class name is missing."""
        expected_output = "** class name missing **"
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("update"))
            self.assertEqual(expected_output, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd(".update()"))
            self.assertEqual(expected_output, output.getvalue().strip())

    def test_help_command__output(self):
        """Verify the output of the 'help' command."""
        expected_output = "*** Unknown syntax: .help()"
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("help"))
            self.assertTrue("Documented commands" in output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd(".help()"))
            self.assertEqual(expected_output, output.getvalue().strip())

    def test__create_command__behaivor(self):
        """Verify the behaivor of the 'create' command."""
        expected_output = "** class name missing **"
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create"))
            self.assertTrue(expected_output in output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd(".create()"))
            self.assertEqual("*** Unknown syntax: .create()",
                             output.getvalue().strip())

    def test__quit_command__behaivor(self):
        """Verify the behaivor of the 'quit' command."""
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertTrue(HBNBCommand().onecmd("quit"))


if __name__ == "__main__":
    unittest.main()
