# Let's assume that you've chosen the following numbers in the lottery: 3, 7, 11, 42, 34, 49.

# The numbers that have been drawn are: 5, 11, 9, 42, 3, 49.
# The question is: how many numbers have you hit?


drawn = [5, 11, 9, 42, 3, 49] # list of numbers drawn in lottery
bets = [3, 7, 11, 42, 34, 49] # list of chosen numbers or our bets
hits = 0  # counts our hits or number of bets successful

for number in bets:
    if number in drawn:
        hits += 1

print("hits:", hits)

#-----------------------------------------------------------------

# program to find the location of a given element in the list
myList = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
toFind = 5 # target value to find
found = False # the current status of the search

for i in range(len(myList)):
    found = myList[i] == toFind
    if found:
        break # when found== true, the for loop is exited

if found:
    print("Element found at index", i)
else:
    print("absent")
