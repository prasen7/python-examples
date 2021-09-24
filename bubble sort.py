# Bubble sort algorithm to sort list using for loop
myList = [8, 10, 6, 2, 4] # list to sort
swapped = True # its task is to observe if any swap has been done during the pass or not
# one pass means completeing one round of comapring adjecent elements of list from left to right

while swapped:
    swapped=False # no swaps so far
    # if no swap is done during the last pass, the while loop will end (swapped == False)
    for i in range(len(myList) - 1): # we need (5 - 1) comparisons
        if myList[i] > myList[i + 1]: # compare adjacent elements
            swapped=True # swap occured!
            myList[i], myList[i + 1] = myList[i + 1], myList[i] 
            # if we end up here it means that we have to swap the elements

print("sorted with Bubble sort algorithm:", myList)

# Python, however, has its own sorting mechanisms.
# No one needs to write their own sorts.
myList = [8, 10, 6, 2, 4]
myList.sort()
print("sorted with built-in list.sort method:", myList)
