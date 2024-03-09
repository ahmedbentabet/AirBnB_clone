#!/usr/bin/python3
"""Command interpreter for the HBNB project."""
import cmd
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review
from models import storage


class HBNBCommand(cmd.Cmd):
    """Command interpreter class"""

    prompt = "(hbnb) "

    classes = [
      "BaseModel",
      "User",
      "State",
      "City",
      "Amenity",
      "Place",
      "Review",
    ]

    def do_quit(self, arg):
        """
        Quit command to exit the program
        """
        return True

    def do_EOF(self, arg):
        """
        Exit the program on EOF
        """
        print()
        return True

    def emptyline(self):
        """
        Do nothing if the input is an empty line (just pressing ENTER)
        """
        pass

    def do_create(self, arg):
        """
        Create a new instance of BaseModel,
        saves it (to the JSON file) and prints the id.

        Usage: create <class_name>
        """
        if not arg:
            print("** class name missing **")

        try:
            # create an instance
            new_instance = eval(arg)()
            # new_instance -->"<obj_clas>.<id>" = <obj.to_dict()> --> json file
            new_instance.save()
            print(new_instance.id)
        except Exception:
            print("** class doesn't exist **")

    def do_show(self, arg):
        """
        Print the string representation of
        an instance based on the class name and id.

        Usage: show <class_name> <instance_id>
        """
        list_of_args = arg.split()

        if not list_of_args:
            print("** class name missing **")
            return

        class_name = list_of_args[0]
        if class_name not in HBNBCommand.classes:
            print("** class doesn't exist **")
            return

        if len(list_of_args) == 1:
            print("** instance id missing **")
            return

        obj_id = list_of_args[1]
        key = f"{class_name}.{obj_id}"
        if key not in storage.all():
            print("** no instance found **")
            return

        print(storage.all()[key])

    def do_destroy(self, arg):
        """
        Deletes an instance based on the class name and id
        (save the change into the JSON file).

        Usage: destroy <class_name> <instance_id>
        """
        list_of_args = arg.split()

        if not list_of_args:
            print("** class name missing **")
            return

        class_name = list_of_args[0]
        if class_name not in HBNBCommand.classes:
            print("** class doesn't exist **")
            return

        if len(list_of_args) == 1:
            print("** instance id missing **")
            return

        obj_id = list_of_args[1]
        key = f"{class_name}.{obj_id}"
        if key not in storage.all():
            print("** no instance found **")
            return

        del storage.all()[key]
        storage.save()

    def do_all(self, arg):
        """
        Prints all string representation of all instances
        based or not on the class name.

        Usage: all <class_name> or all
        """
        list_of_args = arg.split()
        list_of_objs = []   # list of string representation of objects.

        if not list_of_args:
            # Print all instances
            objs = storage.all().values()
            print([str(obj) for obj in objs])  # check it without str
            return

        class_name = list_of_args[0]
        if class_name not in self.classes:
            print("** class doesn't exist **")
            return

        # Print instances of a specific class
        objs = []
        for key in storage.all().keys():
            if key.startswith(class_name):
                objs.append(storage.all()[key])
        print([str(obj) for obj in objs])

    def do_update(self, arg):
        """
        Updates an instance based on the class name and id
        by adding or updating attribute (save the change into the JSON file).

        Usage: update <class name> <id> <attribute name> "<attribute value>"
        """
        list_of_args = arg.split()

        if not list_of_args:
            print("** class name missing **")
            return

        if len(list_of_args) == 1:
            print("** instance id missing **")
            return

        if len(list_of_args) == 2:
            print("** attribute name missing **")
            return

        if len(list_of_args) == 3:
            print("** value missing **")
            return

        class_name = list_of_args[0]
        if class_name not in self.classes:
            print("** class doesn't exist **")
            return

        obj_id = list_of_args[1]
        key = f"{class_name}.{obj_id}"
        # Check if the instance exists
        if key not in storage.all():
            print("** no instance found **")
            return

        attr_name = list_of_args[2]
    # [1:-1] to remove double quotes and get what is inside
    # if list_of_args[3].startswith('"') and list_of_args[3].endswith('"'):
    #     attr_value = list_of_args[3][1:-1]
    # elif list_of_args[3].startswith("'") and list_of_args[3].endswith("'"):
    #     attr_value = list_of_args[3][1:-1]
    # else:
    #     attr_value = list_of_args[3]

        attr_value = list_of_args[3].strip('"\'')

        obj = storage.all()[key]
        if hasattr(obj, attr_name):
            # If it exists, update its value
            attr_type = type(getattr(obj, attr_name))
            attr_value_casted = attr_type(attr_value)
            setattr(obj, attr_name, attr_value_casted)
        else:
            # If it doesn't exist, add a new attribute
            setattr(obj, attr_name, attr_value)

        storage.save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
