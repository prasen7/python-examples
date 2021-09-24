# program to demonstrate the use of 'pop' and 'append' method of list objects
lst= ['name1', 'name2', 'name3', 'name4', 'name5']
emp=[]
def rvfunc(li):
    for i in range(len(li)):
        popped=lst.pop()
        emp.append(popped)
        print("i=",i,", popped=",popped,", emp=",emp)

rvfunc(lst)

print(len(emp)) # len function returns the no. of items in the list object.

# list() constructor
# the argument of list can be any iterable object(string, tuples) or collection(set, dictionary)
l1=list(("apple", "banana", "cherry"))
vowel='aeiou'
l2=(list(vowel))
vowel_dict={'a':1,'e':2,'i':3,'o':4,'u':5}
print(list(vowel_dict)) 
# For dictionaries, the keys of the dictionary will be the item of the list. the order of the elements will be random
# list1 = list(list2), list constructor can be used to make a copy from list2 to list1

# list.remove("name1") removes the specified item from the list. throws TypeError if no argument provided.
# 'del list[0]' also removes the specified index. 'del list' command can also delete the list object completely.
# del list[:] clears the list but keeps the list object intact but empty.
# clear(list) method empties the list.
# list.pop(1) removes the specified index. If no index is specified the it removes the last item from the list.
# list.insert(1, "name") inserts an item at the spefied index.
# list1.extend(list2) adds elements from list2 to list1. list2 remains intact.
# list.extend(object) method can append any iterable object to the list( such as tuples, sets, dictionaries etc.).
# list2 = list1.copy() method will make a copy of list1 to list2.

# SORTING A LIST:----------------------------------------------------------------------------------
# list.sort() method sorts the list alphanumerically, ascending, by default.
# list.sort() method has two keyword arguments reverse and key
emp.sort(reverse=True) # to sort descending

# sort a list of numbers based on how close the number is to 50--
def myfunc(n):
    return abs(n-50)
num=[100,50,60,65,82,23]
num.sort(key = myfunc)
print(num)

# Case-insensitive sort-- sort method sorts capital letters before lower case letters
# to remove this problem use str.lower() as key-function.
this=["Prasen", "aakash", "cherry", "Kiwi"]
this.sort(key = str.lower)
print(this)  # Output- ['aakash', 'cherry', 'Kiwi', 'Prasen']
# list.reverse() method simply reverses the current sorting order of the elements.
#---------------------------------------------------------

# list.index('element') method returns the position at the first occurence of the specified value.(starting from 0)
this.reverse()
print(this)
x=this.index("cherry")
print(x)
#---------------------------------------------------------------------------------------------------------------
# Different ways to loop through a list-----
#1. Using for loop:
for x in emp:
    print(x, end=", ")
    if x==emp[-1]:
        print("\n")

for i in range(len(emp)): # by referring to the index of elements
    print(emp[i], end=",")
    if i==4:
        print("\n")

#2. Using while loop:
j=0
while j<len(emp):
    print(emp[j], end=",")
    j+=1
print("\n")

#3. Using list comprehension:
[print(x, end=",") for x in emp]


# List Comprehension--
# A list comprehension is actually a list, but created on-the-fly during program execution, and is not described statically.
# a shorter way to create a new list based on the values of an existing list
# based on a list of fruits, create a new list containing only the fruits with letter 'a' in the name.
fruits=['apple', 'banana', 'cherry', 'kiwi', 'mango']
newlist=[x for x in fruits if "a" in x] 
# syntax--> newlist=['expression' for 'item' in 'iterable' if condition==True]
# the 'iterable' can be any iterable object(list, tuple, set etc.)
# the 'expresson' is the current item in the iteration, but it is also the outcome, which you can manipulate before it ends up 
# like a list item in the new list. for example-
newlist2=[x.upper() for x in fruits]
# the 'expression' can also contain conditions, not like a filter, but as a way to manipulate the outcome.
newlist3=[x if x!="banana" else "orange" for x in fruits] # return the item if it is not banana, if it is banana--> return orange.

#------------------------------------------------------------------------------------------------------------------------------------

# join two lists---
# 1. using '+' operator--
list3= num + this 

# 2. Append method
l1.append(l2)

# 3. extend operator
# l1.extend(l2)

#----------------------------------------------------------------------------
# the in and not in operator- to check if a value is in a list or not
myList = [0, 3, 12, 8, 2]

print(5 in myList)
print(5 not in myList)
print(12 in myList)
