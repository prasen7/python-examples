# Dictionary is a mutable data structure with unordered collection of key-value pairs.
# In Python 3.6x dictionaries have become ordered collections by default.
# a dictionary is a one-way tool - using keys we can look for corresponding vlaues, but not vice versa.
# each key must be unique, a key may be data of any type (except list).
# keys are case-sensitive.
# keys can exist without values(None), but values can't exist without keys.
emptydict=dict.fromkeys(['apple','ball']) # dictionary with only keys and value as None.
# fromkeys() - Returns a dictionary with the specified keys and values
x = ('key1', 'key2', 'key3')
y = 0
thisdict = dict.fromkeys(x, y)
print(thisdict)

# dictionary from english to french
dictionary = {"cat" : "chat", "dog" : "chien", "horse" : "cheval"}
phone_numbers = {'boss' : 5551234567, 'Suzy' : 22657854310}
empty_dictionary = {}

# the len() function works for dictionaries, return the no. of key-value pairs
print(len(dictionary))

# method of printing values of dictonary by using keys
print(dictionary['cat'])
print(phone_numbers['Suzy'])

# list of words to check its french equivalent
words = ['cat', 'lion', 'horse']
# to check if key/word is in dictionary and then print the corresponding value
for word in words:
    if word in dictionary:
        print(word, "->", dictionary[word])
    else:
        print(word, "is not in dictionary")
# To iterate over a dictionary
# dictionary.keys() method returns an iterable object(list) consisting of all the keys gathered within the dictionary.
#Having a group of keys enables you to access the whole dictionary.
#
for key in dictionary.keys():
    print(key, "->", dictionary[key])
# for sorted key order use sorted() function on keys() method.
for key in sorted(dictionary.keys()):
    print(key, "->", dictionary[key])
#
# values() works similarly to keys(), but returns values.
#
for french in dictionary.values():
    print(french)
#
# dictionary.items() method returns list of tuples where each tuple is a key-value pair.
# 
for english, french in dictionary.items():
    print(english, "->", french)
print(dictionary.items())
# assigning a new value to an existing key.
dictionary['cat'] = 'minou'
# this can be done by update method too
# dictionary({"cat":"minou"})
# to add a new key-value pair, assign a value to a new, previously non-existent key.
dictionary['swan'] = 'cygne'
# insert a new item into dictionary by using update method
dictionary.update({"duck" : "canard"})

# removing a key-value pair using del keyword on that key.
# By removing the key, the associated value also gets deleted.
del dictionary['dog']
# del keyword can delete the dictionary completely.
# del dictionary
#To remove the last item in a dictionary, you can use the popitem() method:
# before 3.6.7, the popitem() method removes a random item from a dictionary.
# dictionary.popitem()
# pop() method removes the item with the specified key name:
# dictionary.pop("dog")
# clear() method empties the dictionary:
# dictionary.clear()
#
# "glue" the two dictionaries (d1 and d2) together and create a new one (d3).
d1 = {'Adam Smith':'A', 'Judy Paxton':'B+'}
d2 = {'Mary Louis':'A', 'Patrick White':'C'}
d3 = {}
#
for item in (d1, d2):
    d3.update(item)
print(d3)
#
colors = {
    "white" : (255, 255, 255),
    "grey"  : (128, 128, 128),
    "red"   : (255, 0, 0),
    "green" : (0, 128, 0)
    }

for col, rgb in colors.items():
    print(col, ":", rgb)

# convert tuples to dictionary
colors = (("green", "#008000"), ("blue", "#0000FF"))
colDict = dict(colors)
print(colDict)

#You cannot copy a dictionary simply by typing dict2 = dict1, because:
# dict2 will only be a reference to dict1,
# and changes made in dict1 will automatically also be made in dict2.
# create a new copy of dictionary with dict.copy() method
# the same can be done with dict() function
myDict = {"A":1, "B":2}
copyMyDict = myDict.copy()
# copyMyDict = dict(myDict)
myDict.clear()
print(copyMyDict)
#
#




