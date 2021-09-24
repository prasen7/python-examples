# takes a string as input and figures out the average length of all words and returns the no. representing the same.
# Remove all punctuations and round up to nearest whole no.
import math
n = input("input a string: ")
s= n.split()
l=0
for i in s:
    l+=len(i)
a = math.ceil(l/len(s))
print(s)
print("average length of each word in string: ", a)