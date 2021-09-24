# Lists (and many other complex Python entities) are stored in different ways than ordinary (scalar) variables.

# 1. the name of an ordinary variable is the name of its content.
# 2. the name of a list is the name of a memory location where the list is stored.

# The assignment: list2 = list1 copies the name of the array, not its contents.
# In effect, the two names (list1 and list2) identify the same location in the computer memory.
# Modifying one of them affects the other, and vice versa.
list1 = [1]
list2 = list1
list1[0] = 2
print(list2)

# A slice is an element of Python syntax that allows you to make a brand new copy of a list, or parts of a list.

# Copying the whole list
list1 = [1]
list2 = list1[:]
list1[0] = 2
print(list2)

# Copying part of the list
myList = [10, 8, 6, 4, 2]
newList = myList[1:3]
print(newList)

# deleting the l3 variable does not delete the list saved in memory.
l1 = ["A", "B", "C"]
l2 = l1
l3 = l2

del l1[0]
del l2

print(l3)
