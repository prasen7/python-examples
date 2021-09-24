# Python course- module 5.1
# module - modules, along with the built-in functions, form the Python standard library - a special sort of library where modules play the roles of books (we can even say that folders play the roles of shelves).
# namespace- A namespace is a space(understood in a non-physical context) in which some names exist
# and the names don't conflict with each other (i.e., there are not two different objects of the same name).
# We can say that each social group is a namespace - the group tends to name each of its members in a unique way (e.g., parents won't give their children the same first names).
#Inside a certain namespace, each name must remain unique. This may mean that some names may disappear when any other entity of an already known name enters the namespace.
# This uniqueness may be achieved in many ways, e.g., by using nicknames along with the first names (it will work inside a small group like a class in a school)
# or by assigning special identifiers to all members of the group.
# import-
# If the module of a specified name exists and is accessible (a module is in fact a Python source file), Python imports its contents,
# i.e., all the names defined in the module become known, but they don't enter your code's namespace.
# This means that you can have your own entities in the code named same as the entities in the module imported and they won't be affected by the import in any way.
import math
# we define our own sin and pi entities
def sin(x):
    if 2 * x == pi:
        return 0.99999999
    else:
        return None

pi = 3.14

print(sin(pi/2))
print(math.sin(math.pi/2))
# notice how the two sin functions can work in the same program because of different namespace.
