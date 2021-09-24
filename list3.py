# program to find largest element in list

myList = [17, 3, 11, 5, 1, 9, 7, 15, 13]
largest = myList[0]
# with for loop using list indexing
for i in range(1, len(myList)):
    if myList[i] > largest:
        largest = myList[i]

print(largest)
# without indexing
for i in myList:
    if i > largest:
        largest = i
print(largest)

#If you need to save computer power, you can use a slice:

myList = [17, 3, 11, 5, 1, 9, 7, 15, 13]
largest = myList[0]

for i in myList[1:]:
    if i > largest:
        largest = i

print(largest)
#-------------------------------------------
# list comprehension examples:
# Example 1:
squares = [x ** 2 for x in range(10)]
# The snippet produces a ten-element list filled with squares of ten integer numbers starting from zero (0, 1, 4, 9, 16, 25, 36, 49, 64, 81)

# Example #2:
twos = [2 ** i for i in range(8)]
# The snippet creates an eight-element array containing the first eight powers of two (1, 2, 4, 8, 16, 32, 64, 128)

# Example #3:
odds = [x for x in squares if x % 2 != 0 ]
# The snippet makes a list with only the odd elements of the squares list.

# Example #4:
# using nested list comprehension
board1 = [[i**2 for i in range(8)] for j in range(8)]
print(board1)


