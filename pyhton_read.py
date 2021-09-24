# python reading materials

#1. decorator:
# a decorator is a design pattern in python that allows a user to add new
# functionality to an existing object without modifying its structure.
from time import time
def timer(func):
    def f(*args, **kwargs):
        before=time()
        rv=func(*args, **kwargs)
        after=time()
        print(f'elapsed time: {afetr-before}')
        return rv
    return f
@timer
def add(x,y,z):
    return x+y+Z
print(add(5,5,5))

# 2. Generator:
# a generator is a special type of function which does not return a single value.
# instead, it returns an iterator object with a sequence of values.
from time import sleep

def compute():
    for i in range(10):
        sleep(.5)
        yield i
for val in compute():
    print val
#------------------------------------------------------------
# 3.setattr and getattr:-
# setattr function sets the value of specified attribute of the specified object.
# getattr method returns the value of the named attribute of an object.

class Person:
    pass
person=Person()
person_info={"first": "Danny", "Last": "Steenman"}
for key, value in person_info.items():
    setattr(person, key, value)

for key in person_info:
    print(getattr(person, key))

# 4. Enumerate :-----------------------------------------------------------
# enumerate adds a counter to an iterable and returns it in a form of enumerate object.
my_list=["apple", "banana", "grapes", "pear"]
for counter, value in enumerate(my_list):
    print(counter, value)

# output:
# 0 apple
# 1 banana
# 2 grapes
# 3 pear
#----------------------------
# 5. ternary operator
# ternary operator quickly tests a condition instead of a multiline if statement
condition=True
x=1 if condition else 0
print(x)
#-------------------------------


